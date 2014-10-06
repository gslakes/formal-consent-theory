#!/usr/bin/env python
"""Usage: python run_as_tptp_test_suite.py [-n|--dry-run] [-v|--verbose] <TPTP input file to test> [<tests to run>]*

Processes the given TPTP input file (e.g. input.tptp), searching for test case markup that denotes
separate tests for a central model or theorem.

Usage examples:

   Run all the tests in a theory file named naive_consent_theory.tptp:

       python run_as_tptp_test_suite.py naive_consent_theory.tptp


   Run an individual test case from that theory file named asking_and_getting_consent_is_ethical:

       python run_as_tptp_test_suite.py naive_consent_theory.tptp asking_and_getting_consent_is_ethical


Markup description:

 - '% Test runner: begin tests.'         denotes the beginning of the section(s) which will be split into test cases.
 - '% Test runner: end tests.'           denotes the end of the sections(s) which will be split into test cases.
 - '% Test case: '                       denotes the beginning of a new test case, which will span until any markup
                                         line is seen. Any text following it will be interpreted as the name of the
                                         test case.
 - '% Negated test case: '               denotes the beginning of a test case where the test result should be
                                         negated/inverted, with successful proof of any conjectures indicating
                                         failure of the test.
 - '% Test case: this_is_the_first_test' denotes a test case with name 'this_is_the_first_test'.


Prover installation:

This script assumes that the E prover (http://www4.informatik.tu-muenchen.de/~schulz/E/E.html) is compiled and
installed in-place under /home/E/, with binary at /home/E/PROVER/eprover

(Other provers could be used in place of the E prover, thanks to the wide adoption of the TPTP format,
 however, success and failure detection in this script is customised for the output of E prover.)

"""

import getopt
import os
import os.path
import re
import string
import subprocess
import sys
import tempfile

eprover_bin = "/home/E/PROVER/eprover"
eprover_options = ["--auto-schedule", "--tstp-format", "-s", "-l 1", "--proof-object", "--memory-limit=2048", "--cpu-limit=10"]

def usage():
    """ Displays the usage information for this program. """
    sys.stdout.write("Usage: python run_as_tptp_test_suite.py [-n|--dry-run] ")
    sys.stdout.write("[-v|--verbose] <TPTP input file to test> [<test to run>]\n")
# end def

def run_test_case(test_case = {}, non_test_matter = "", result_filename = "", dry_run = False, verbosity = 0):
    """ Run the test case specified in the given dictionary structure, putting it at the end of
        given non-test matter for input to TPTP, and storing the results of the TPTP run into
        the given result file.

        The results file is scanned to assess the status of the test, and a status value is calculated and
        returned as the result of this function.
        This return value is a single character, with the value indicating:
         - 'E' for error
         - 'F' for failure, and
         - 'S' for success.
    """

    # Open (or create) the results file, if a non-empty string has been given.
    if len(result_filename) > 0:
        results_file = open(result_filename, 'w')
    else:
        results_file = tempfile.TemporaryFile(prefix = 'run_as_tptp_test_suite_results')
    # end if

    # Create a file to hold the concatenated non-test matter and test text.
    test_case_name = test_case.get('name', 'Unknown Test')
    test_case_text = test_case.get('text', '')
    input_file = tempfile.SpooledTemporaryFile(prefix = 'run_as_tptp_test_suite_input')
    input_file.write(non_test_matter)
    input_file.write(test_case_text)
    input_file.seek(0)

    # Run the test case through TPTP.
    try:
        subprocess.call([eprover_bin] + eprover_options, stdin = input_file, stdout = results_file, stderr = results_file)
    except Exception, e:
        input_file.close()
        results_file.close()
        sys.stdout.write("\nERROR: an error '%s' occurred while running test case '%s'.\n" % (str(e), test_case_name))
        sys.stdout.write("Test text:\n")
        sys.stdout.write(test_case_text)
        sys.stdout.write("\nExiting.\n")
        sys.exit(1)
    # end try

    # Check the output for certain strings that indicate success, failure, or error.
    results_file = open(result_filename, 'r')
    result = 'E'
    success = re.compile('# Proof found')
    failure = re.compile('# No proof found')
    likely_failure = re.compile('# Failure:')
    for line in results_file:
        if success.match(line) != None:
            result = 'S'
        elif failure.match(line) != None:
            result = 'F'
        elif likely_failure.match(line) != None:
            result = '?'
        # end if
    # end for

    # Close the files, and exit.
    input_file.close()
    results_file.close()
    return result
# end def

def run_test_cases(test_cases = {}, tests_to_run = [], test_results_path = os.curdir + os.sep + "results",
                   non_test_matter = "", dry_run = False, verbosity = 0):
    """ Run the test cases listed. """

    # Validate the given test case name(s) against the list of discovered test case names.
    for test_case_name in tests_to_run:
        if test_case_name not in tests_to_run:
            sys.stdout.write("\nERROR: given test name '%s' not found in the available tests to run.\n" % test_case_name)
            sys.stdout.write("Tests found: '%s'\n" % string.join(test_cases.keys(), ', '))
            sys.stdout.write("\nExiting.\n")
            sys.exit(1)
        # end if
    # end for

    # Create the test results path, if it doesn't exist.
    if os.path.exists(test_results_path):
        if not os.path.isdir(test_results_path):
            sys.stdout.write("\nERROR: given test results path '%s' already exists, and isn't a directory. Exiting." % test_results_path)
            sys.exit(1)
        # end if
    else:
        # Try to create the directory.
        try:
            os.makedirs(test_results_path)
        except Exception, e:
            sys.stdout.write("\nERROR: couldn't create the test results path '%s'.\n" % test_results_path)
            sys.stdout.write("Reason: %s\n" % str(e))
            sys.stdout.write("\nExiting.\n")
            sys.exit(1)
        # end try
    # end if

    # Collect a list of test cases we're interested in the details for, storing the status and the names of the files
    # containing the run result.
    test_case_details_to_display = []
    test_results = ""

    # Print a header for the results.
    sys.stdout.write("Test results:\n\n")

    for test_case_name in tests_to_run:
        # Generate a file name to store the results of this test case.
        result_filename = test_results_path + os.sep + test_case_name + ".txt"
        # FIXME: generate a file name for the results of each test, validate test cases, tests_to_run, etc.

        test_case = test_cases.get(test_case_name, {})
        negated = test_case.get('negated', False)
        status = run_test_case(test_case = test_case,
                               non_test_matter = non_test_matter, result_filename = result_filename,
                               dry_run = dry_run, verbosity = verbosity)

        # Invert the status if this is a negated test case.
        if negated:
            if status == 'S':
               status = 'F'
            elif status == 'F':
               status = 'S'
            # end if
        # end if

        # Display a JUnit/unittesting style symbol to indicate whether this test succeed, failed, or was erroneous.
        if status == 'S':
            test_results += '.'
            sys.stdout.write('.')
            if verbosity > 1:
                test_case_details_to_display.append((test_case_name, status, result_filename))
            # end if
        else:
            test_results += status
            sys.stdout.write(status)
            test_case_details_to_display.append((test_case_name, status, result_filename))
        # end if
    # end for

    sys.stdout.write("\n\n")

    # Now display the details of any recorded test cases.
    for (test_case_name, status, result_filename) in test_case_details_to_display:
        # Get the relevant details for this test case.
        line_count = test_cases[test_case_name]['line']
        index = test_cases[test_case_name]['index']
        text = test_cases[test_case_name]['text']
        negated = test_cases[test_case_name]['negated']

        # If the user wants minimally verbose output, we want to display relevant detail from the test
        # results according to what status this test case had.
        results = ""
        status_message = "had ERRORS"
        if negated:
            if status == 'F':
                status_message = "unintentionally/undesirably succeeded"
            elif status == 'S':
                status_message = "failed as intended"
            # end if
        else:
            if status == 'F':
                status_message = "FAILED"
            elif status == 'S':
                status_message = "succeeded"
            # end if
        # end if
        if verbosity > 0:
            results_file = open(result_filename, 'r')
            if status == 'E' or verbosity > 2:
                # If there was an error (or we're being very verbose), the user wants to see the whole file.
                # Read in everything.
                results = results_file.read()
            elif status == 'F' or verbosity > 1:
                # If this test case failed (or the verbosity is high), the user wants to see the test case text, and
                # the search results.
                # Read in the results of the run, skipping everything but the search section, and
                # what follows that.
                results += text
                in_search_results = False
                search_section = re.compile('#.*proof found', re.IGNORECASE)
                for line in results_file:
                    if not in_search_results:
                        if search_section.match(line) != None:
                            in_search_results = True
                        # end if
                    # end if
                    if in_search_results:
                        results += line
                    # end if
                # end for
            # end if
            results_file.close()
        # end if

        # Now format these details.
        sys.stdout.write("Test case #%s named '%s' at line %s %s.\n" % \
              (index, test_case_name, line_count, status_message))

        # If the user wants verbose output, display the test results we retrieved earlier.
        if verbosity > 0:
            sys.stdout.write("\nDetails:\n\n")
            sys.stdout.write(results)
        # end if
        sys.stdout.write("\n\n")
    # end for

    # If there were test cases with problems, summarise the results again for clarity.
    if len(test_case_details_to_display) > 0:
        # Print a header for the results.
        sys.stdout.write("Test results:\n\n")
        sys.stdout.write(test_results)
    # end if

    sys.stdout.write("\n\nTest run complete.\n\n")
# end def

def run_test_suite(input_filename = "", tests_to_run = [], dry_run = False, verbosity = 0):
    """ Runs the test suite in the given input filename, by splitting the TPTP input,
        then calling out to the test case runner with the split/parsed output,
        collating the results, and displaying it.
    """

    # Split the input file into test_cases, getting a section of non-test matter, and a
    # dictionary of test case names and text.
    if verbosity > 1:
        sys.stdout.write("Splitting %s...\n" % input_filename)
    # end if
    non_test_matter, test_case_names, test_cases = split_tptp_input(input_filename, dry_run = dry_run, verbosity = verbosity)

    # Validate the given test case name(s) against the list of discovered test case names.
    for test_case_name in tests_to_run:
        if test_case_name not in test_case_names:
            sys.stdout.write("\nERROR: given test name '%s' not found in the given input file.\n" % test_case_name)
            sys.stdout.write("Tests found: '%s'\n" % string.join(test_case_names, ', '))
            sys.stdout.write("\nExiting.\n")
            sys.exit(1)
        # end if
    # end for

    # If there weren't any test given to run, just run the tests in the order they were discovered.
    if tests_to_run == []:
        tests_to_run = test_case_names
    # end if

    # Run the selected test cases.
    if len(tests_to_run) > 0:
        if verbosity > 0:
            sys.stdout.write("Running the following test cases in %s:\n - %s\n\n" % \
                             (input_filename, string.join(tests_to_run, '\n - ')))
        # end if
        run_test_cases(test_cases = test_cases, tests_to_run = tests_to_run, non_test_matter = non_test_matter,
                       dry_run = dry_run, verbosity = verbosity)
    else:
        sys.stdout.write("\nERROR: no valid test cases found in the given input file, '%s'.\n" % inputfile_name)
        sys.stdout.write("\nExiting.\n")
        sys.exit(1)
    # end def
# end def

def split_tptp_input(input_filename, dry_run = False, verbosity = 0):
    """ Splits the TPTP input file with the given filename, extracting non-test matter, and
        collating named (if available) test case portions in a dictionary.
    """

    # Try to open the file.
    try:
        input_file = open(input_filename, 'r')
    except:
        sys.stdout.write("\nERROR: Couldn't open file with name '%s'. Exiting.\n" % input_filename)
        sys.exit(1)
    # end try

    # Compile some regular expressions for speed.
    # (These describe the markup describe earlier.)
    begin_test_section = re.compile('\s*%\s*Test\s*runner\s*:?\s*begin', re.IGNORECASE)
    test_case = re.compile('\s*%\s*(?P<negated>Negated)?\s*[tT]est\s*case\s*:?\s*(?P<name>.*)\s*$', re.IGNORECASE)
    end_test_section = re.compile('\s*%\s*Test\s*runner\s*:?\s*end', re.IGNORECASE)

    # Read the file in, line by line.
    in_test = False
    in_non_test_matter = True
    current_test_count = 0
    line_count = 0
    non_test_matter = ""
    test_case_names = []
    test_cases = {}
    for line in input_file:
        # Increment the line count.
        line_count += 1

        # Check for markup in the current line.
        test_case_match = test_case.match(line)
        disposable_line = False
        negated = False
        if test_case_match != None:
            # We have a new test case.

            # Get the name, if any, or use a safe default.
            current_test_count += 1
            current_test_name = "Test-%s" % current_test_count
            trial_test_name = test_case_match.group('name')
            if trial_test_name != None and len(trial_test_name.strip()) > 0:
                current_test_name = trial_test_name.strip()
            # end if
            test_case_names.append(current_test_name)
            if verbosity > 1:
                sys.stdout.write("Found test case #%s at line %s named '%s'.\n" % \
                                 (current_test_count, line_count, current_test_name))
            # end if

            # Check if we've seen a test with this name before.
            if test_cases.has_key(current_test_name):
                input_file.close()
                sys.stdout.write("\nERROR: test with duplicate name '%s' found at line %s. Exiting.\n" % \
                                 (current_test_name, line_count))
                sys.exit(1)
            # end if

            # Check if this test case is expected to fail.
            if test_case_match.group('negated') != None:
                negated = True
            # end if

            # Store some useful properties in the test case dictionary under the current test name as a key.
            test_cases[current_test_name] = {}
            test_cases[current_test_name]['index'] = current_test_count
            test_cases[current_test_name]['line'] = line_count
            test_cases[current_test_name]['negated'] = negated

            # Set some blank initial text for this test.
            test_cases[current_test_name]['text'] = ""

            # Flag that we're in a test.
            in_test = True
            in_non_test_matter = False
        elif begin_test_section.match(line) != None:
            # We have a beginning of test section marker.
            # Flag that we're no longer in non-test matter, and this is a disposable line.
            if verbosity > 1:
                sys.stdout.write("Found beginning of test section at line %s.\n" % line_count)
            # end if
            in_non_test_matter = False
            disposable_line = True
        elif end_test_section.match(line) != None:
            # We have an end of test section marker.
            # Flag that we're no longer in a test, and back in non-test matter.
            if verbosity > 1:
                sys.stdout.write("Found end of test section at line %s.\n" % line_count)
            # end if
            in_non_test_matter = True
            in_test = False
            disposable_line = True
        # end if

        # Dispatch the text of this line depending on what flags are currently set.
        if not disposable_line:
            # This is a non-disposable line.
            # If we're in a test, add the current line to the text for the test.
            if in_test:
                test_cases[current_test_name]['text'] = test_cases[current_test_name]['text'] + line
            else:
                # If we're not in a test, we may be in non-test matter.
                # Otherwise, we're in the disposable sections between the beginning of a test section and
                # the first test. Just ignore this.
                if in_non_test_matter:
                    # We're in non-test matter, so just add the line to the non-test matter we have.
                    non_test_matter = non_test_matter + line
                # end if
            # end if
        # end if
    # end for

    # Return the non-test matter, the test case names, and the test cases we're collated.
    return (non_test_matter, test_case_names, test_cases)
# end def

def main(argv):
    """ Handles command-line input and dispatches it to the test suite runner.
    """
    # Set defaults for the command line arguments to read in.
    dry_run = False
    input_filename = ""
    tests_to_run = []
    verbosity = 0

    # Try to parse the given command-line options.
    try:
        options, args = getopt.getopt(sys.argv[1:], 'nv', ['dry-run','verbose'])
    except getopt.GetoptError:
        # The given options are incorrect.
        usage()
        sys.stdout.write("\nERROR: Invalid command line options given. Exiting.\n")
        sys.exit(2)
    # end try

    # Interpret the parsed command-line options.
    for opt, arg in options:
        # Did we get the -n/--dry-run option?
        if opt in ('-n', '--dry-run'):
            # Yes. Set this accordingly.
            dry_run = True
        # end if
        # Did we get the -v/--verbose option?
        if opt in ('-v', '--verbose'):
            # Yes. Increase this accordingly.
            verbosity += 1
        # end if
    # end for

    if verbosity > 1:
        sys.stdout.write("Got options: dry-run: %s verbosity level: %s\n" % (dry_run, verbosity))
        sys.stdout.write("Got arguments: %s\n" % (args))
    # end if

    # Do we have enough arguments? (i.e. we need a file name, at least)
    if len(args) >= 1:
        input_filename = args[0]
        if len(args) > 1:
            tests_to_run = args[1:]
        # end if
    else:
        # We don't have enough arguments to run properly.
        usage()
        sys.stdout.write("\nERROR: Not enough command line arguments were given. Exiting.\n")
        sys.exit(2)
    # end if

    # Start the run using the given inputs.
    run_test_suite(input_filename = input_filename, tests_to_run = tests_to_run, dry_run = dry_run, verbosity = verbosity)
# end def

if __name__ == "__main__":
    main(sys.argv[1:])
# end if
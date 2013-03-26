Formal consent theory-based ethics
==================================

A first-order logic formalisation of consent theory-based ethics, intended for eventual use
as a machine ethics system.

Getting started
---------------

The `.in` files in this code repository contain machine-readable theories and automated tests.
These are for use with the Prover 9 automated theorem prover via a Python-based test suite
runner provided in this code repository, `run_as_prover9_test_suite.py`.

It is recommended to get started by studying the demonstration system in `naive_consent_theory.in`,
which contains a simplistic/'naive' formalisation of consent theory-based ethics.

On a Linux/Unix machine with Prover 9 and a Python interpreter installed, this system may be tested
by the following command line, run from the base directory of a copy of this code repository:

    python run_as_prover9_test_suite.py naive_consent_theory.in

Other systems can be tested by replacing `naive_consent_theory.in` in the above command line with the
file name of the system to be tested.

For further assistance or feedback, please contact the author via lakes<dot>gs<at>gmail<dot>com
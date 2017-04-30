#!/usr/bin/env python
#
# Naive consent theory-based machine ethics - Python implementation
#
# This file contains a simplistic/naive machine ethics system based on consent
# theory concepts, and implemented in Python.
#
# This is intended as an introduction to the basic concept and proof system,
# and not as a complete or useful system.
#
# A plain language summary of this system:
#
# It is ethical to:
#  1. ask for consent for an action, get consent for that action, and then:
#     a. do that action
#     b. NOT do that action.
#  2. ask for consent, NOT get consent for that action, and then NOT do that
#     action.
#  3. do or NOT do an action to yourself.
#
# As you can see, this is a very simple model of ethical behaviour, yet consent
# by itself is enough to decide the difference between medicine, assault,
# euthanasia, suicide, and murder.
#
# Included is a set of test cases to demonstrate these results, and act as a
# basic check on this system for consistency.
#
# (These are not intended to be conclusive/exhaustive tests, and your personal
#  morals and/or ethics may differ from what is consistent with this system.)
#
# Expected output from a test suite run:
#
# $ ./naive_consent_theory.py
# ................................
# ----------------------------------------------------------------------
# Ran 32 tests in 0.001s
#
# OK
#
#
# WARNING: this imperative implementation is not exactly equivalent to the
#          functional versions.
#
#          The test suite has small modifications to catch issues that are not
#          present in the functional version, and you should look out for these
#          kind of issues if you make modifications.

import unittest

try:
    from typing import Dict, List, Tuple  # noqa: F401
except:
    pass
# end try


# Modelling of consent theory.


class Person:
    "Class to represent people acting within the system."

    def __init__(self, name):
        # type: (str) -> None
        self.name = name             # type: str

        self.actions = {}            # type: Dict[Tuple[str, str], bool]
        self.asked_for_consent = {}  # type: Dict[Tuple[str, str], bool]
        self.consented = {}          # type: Dict[Tuple[str, str], bool]
    # end def

    def consent_requested_by(self, personAsking, action):
        # type: (str, str) -> bool
        self.asked_for_consent[(personAsking, action)] = True
    # end def

    def consents(self, personAsking, action):
        """ This is a consent-positive model: only 'yes' counts as consent.
            The absence of a 'no' does not grant consent.
        """
        # type: (str, str) -> bool
        return (personAsking, action) in self.consented and \
               (self.consented[(personAsking, action)])
    # end def

    def does_not_consent(self, personAsking, action):
        # type: (str, str) -> None
        self.consented[(personAsking, action)] = False
    # end def
    revoke_consent = does_not_consent

    def do(self, personAffected, action):
        # type: (str, str) -> None
        self.actions[(personAffected, action)] = True
    # end def

    def did(self, personAffected, action):
        # type: (str, str) -> bool
        return (personAffected, action) in self.actions
    # end def

    def give_consent(self, personAsking, action):
        # type: (str, str) -> None
        self.consented[(personAsking, action)] = True
    # end def

    def was_asked_for_consent(self, personAsking, action):
        # type: (str, str) -> bool
        return (personAsking, action) in self.asked_for_consent
    # end def
# end class


def is_ethical_action(personA, personB, action):
    """Decide whether the given action between the given person or people is
       ethical.
    """
    # type: (Person, Person, str) -> bool
    aName = personA.name
    bName = personB.name
    # It is ethical to ask for consent,
    # get consent for that action,
    # and then either do, or do not do that action.
    if (personB.was_asked_for_consent(aName, action) and
        personB.consents(aName, action) and
        (personA.did(bName, action) or
         (not personA.did(bName, action)))):
        return True
    # end if

    # It is ethical to ask for consent,
    # not get consent for that action,
    # and then not do that action.
    if (personB.was_asked_for_consent(aName, action) and
        ((not personB.consents(aName, action)) and
         (not personA.did(bName, action)))):
        return True
    # end if

    # It is ethical to do - or not do - an action to yourself.
    if personA == personB:
        return True
    # end if

    # If we're here, assume this is an unethical action.
    return False
# end def


class EthicsTest(unittest.TestCase):
    """ Contains known ethical/unethical behaviours, and the decisions the
        modelling above should make about these behaviours.
    """

    # General consent theory principles.
    #
    # The names used in these tests (e.g. alex, bo) are intended to be
    # gender-neutral and/or role-appropriate.

    def test_asking_and_getting_consent_is_ethical(self):
        "Asking and getting consent is ethical"
        # type: () -> None

        alex = Person('Alex')
        bo = Person('Bo')

        bo.consent_requested_by('Alex', 'action')
        bo.give_consent('Alex', 'action')
        alex.do('Bo', 'action')

        self.assertTrue(is_ethical_action(alex, bo, 'action'),
                        "Asking and getting consent is ethical")
    # end def

    def test_asking_and_getting_consent_is_not_unethical(self):
        "Asking and getting consent is not unethical"
        # type: () -> None

        alex = Person('Alex')
        bo = Person('Bo')

        bo.consent_requested_by('Alex', 'action')
        bo.give_consent('Alex', 'action')
        alex.do('Bo', 'action')

        self.assertFalse((not is_ethical_action(alex, bo, 'action')),
                         "Asking and getting consent is not unethical")
    # end def

    def test_asking_and_not_getting_consent_is_ethical(self):
        "Asking and not getting consent (and not doing the act) is ethical"
        # type: () -> None

        alex = Person('Alex')
        bo = Person('Bo')

        bo.consent_requested_by('Alex', 'action')

        self.assertTrue(is_ethical_action(alex, bo, 'action'),
                        "Asking and not getting consent " +
                        "(and not doing the act) is ethical")
    # end def

    def test_asking_and_not_getting_consent_is_not_unethical(self):
        """Asking and not getting consent (and not doing the act) is not
         unethical
        """
        # type: () -> None

        alex = Person('Alex')
        bo = Person('Bo')

        bo.consent_requested_by('Alex', 'action')

        self.assertFalse((not is_ethical_action(alex, bo, 'action')),
                         "Asking and not getting consent " +
                         "(and not doing the act) is not unethical")
    # end def

    def test_asking_and_explicitly_not_getting_consent_is_ethical(self):
        """Asking and explicitly not getting consent (and not doing the act)
           is ethical
        """
        # type: () -> None

        alex = Person('Alex')
        bo = Person('Bo')

        bo.consent_requested_by('Alex', 'action')
        alex.does_not_consent('Bo', 'action')

        self.assertTrue(is_ethical_action(alex, bo, 'action'),
                        "Asking and explicitly not getting consent " +
                        "(and not doing the act) is ethical")
    # end def

    def test_asking_and_explicitly_not_getting_consent_is_not_unethical(self):
        """Asking and explicitly not getting consent (and not doing the act) is
           not unethical
        """
        # type: () -> None

        alex = Person('Alex')
        bo = Person('Bo')

        bo.consent_requested_by('Alex', 'action')
        alex.does_not_consent('Bo', 'action')

        self.assertFalse((not is_ethical_action(alex, bo, 'action')),
                         "Asking and explicitly not getting consent " +
                         "(and not doing the act) is not unethical")
    # end def

    def test_ignoring_consent_negative_responses_is_unethical(self):
        "Ignoring consent negative responses is unethical"
        # type: () -> None

        alex = Person('Alex')
        bo = Person('Bo')

        bo.consent_requested_by('Alex', 'action')
        bo.does_not_consent('Alex', 'action')
        alex.do('Bo', 'action')

        self.assertFalse(is_ethical_action(alex, bo, 'action'),
                         "Ignoring consent negative responses is unethical")
    # end def

    def test_ignoring_consent_negative_responses_is_not_ethical(self):
        "Ignoring consent negative responses is not ethical"
        # type: () -> None

        alex = Person('Alex')
        bo = Person('Bo')

        bo.consent_requested_by('Alex', 'action')
        bo.does_not_consent('Alex', 'action')
        alex.do('Bo', 'action')

        self.assertTrue((not is_ethical_action(alex, bo, 'action')),
                        "Ignoring consent negative responses is not ethical")
    # end def

    # Murder versus euthanasia vs suicide.

    def test_killing_without_consent_is_unethical(self):
        "Killing without consent is unethical"
        # type: () -> None

        murderer = Person('Murderer')
        victim = Person('Victim')

        murderer.do('Victim', 'kill')

        self.assertFalse(is_ethical_action(murderer, victim, 'kill'),
                         "Killing without consent is unethical")
    # end def

    def test_killing_without_consent_is_not_ethical(self):
        "Killing without consent is not ethical"
        # type: () -> None

        murderer = Person('Murderer')
        victim = Person('Victim')

        murderer.do('Victim', 'kill')

        self.assertTrue((not is_ethical_action(murderer, victim, 'kill')),
                        "Killing without consent is not ethical")
    # end def

    def test_killing_with_explicit_non_consent_is_unethical(self):
        "Killing with explicit non-consent is unethical"
        # type: () -> None

        murderer = Person('Murderer')
        victim = Person('Victim')

        victim.does_not_consent('Murderer', 'kill')

        murderer.do('Victim', 'kill')

        self.assertFalse(is_ethical_action(murderer, victim, 'kill'),
                         "Killing with explicit non-consent is unethical")
    # end def

    def test_killing_with_explicit_non_consent_is_not_ethical(self):
        "Killing with explicit non-consent is not ethical"
        # type: () -> None

        murderer = Person('Murderer')
        victim = Person('Victim')

        victim.does_not_consent('Murderer', 'kill')

        murderer.do('Victim', 'kill')

        self.assertTrue((not is_ethical_action(murderer, victim, 'kill')),
                        "Killing with explicit non-consent is not ethical")
    # end def

    def test_killing_with_explicit_consent_is_ethical(self):
        "Killing with explicit consent is ethical"
        # type: () -> None

        doctor = Person('Doctor')
        patient = Person('Patient')

        patient.consent_requested_by('Doctor', 'kill')
        patient.give_consent('Doctor', 'kill')

        doctor.do('Patient', 'kill')

        self.assertTrue(is_ethical_action(doctor, patient, 'kill'),
                        "Killing with explicit consent is ethical")
    # end def

    def test_killing_with_explicit_consent_is_not_unethical(self):
        "Killing with explicit consent is not unethical"
        # type: () -> None

        doctor = Person('Doctor')
        patient = Person('Patient')

        patient.consent_requested_by('Doctor', 'kill')
        patient.give_consent('Doctor', 'kill')

        doctor.do('Patient', 'kill')

        self.assertFalse((not is_ethical_action(doctor, patient, 'kill')),
                         "Killing with explicit consent is not unethical")
    # end def

    def test_suicide_without_consent_is_ethical(self):
        "Suicide without consent is ethical"
        # type: () -> None

        person = Person('Person')

        person.do('Person', 'kill')

        self.assertTrue(is_ethical_action(person, person, 'kill'),
                        "Suicide without consent is ethical")
    # end def

    def test_suicide_without_consent_is_not_unethical(self):
        "Suicide without consent is not unethical"
        # type: () -> None

        person = Person('Person')

        person.do('Person', 'kill')

        self.assertFalse((not is_ethical_action(person, person, 'kill')),
                         "Suicide without consent is not unethical")
    # end def

    def test_suicide_with_explicit_non_consent_is_ethical(self):
        "Suicide with explicit non-consent is ethical"
        # type: () -> None

        person = Person('Person')

        person.does_not_consent('Person', 'kill')

        person.do('Person', 'kill')

        self.assertTrue(is_ethical_action(person, person, 'kill'),
                        "Suicide with explicit non-consent is ethical")
    # end def

    def test_suicide_with_explicit_non_consent_is_not_unethical(self):
        "Suicide with explicit non-consent is not unethical"
        # type: () -> None

        person = Person('Person')

        person.does_not_consent('Person', 'kill')

        person.do('Person', 'kill')

        self.assertFalse((not is_ethical_action(person, person, 'kill')),
                         "Suicide with explicit non-consent is not unethical")
    # end def

    def test_suicide_with_explicit_consent_is_ethical(self):
        "Suicide with explicit consent is ethical"
        # type: () -> None

        person = Person('Person')

        person.consent_requested_by('Person', 'kill')
        person.give_consent('Person', 'kill')

        person.do('Person', 'kill')

        self.assertTrue(is_ethical_action(person, person, 'kill'),
                        "Suicide with explicit consent is ethical")
    # end def

    def test_suicide_with_explicit_consent_is_not_unethical(self):
        "Suicide with explicit consent is not unethical"
        # type: () -> None

        person = Person('Person')

        person.consent_requested_by('Person', 'kill')
        person.give_consent('Person', 'kill')

        person.do('Person', 'kill')

        self.assertFalse((not is_ethical_action(person, person, 'kill')),
                         "Suicide with explicit consent is not unethical")
    # end def

    # Assault versus consensual harm. (i.e. medicine, kink.)

    def test_harm_without_consent_is_unethical(self):
        "Harm without consent is unethical"
        # type: () -> None

        assailant = Person('Assailant')
        victim = Person('Victim')

        assailant.do('Victim', 'harm')

        self.assertFalse(is_ethical_action(assailant, victim, 'harm'),
                         "Harm without consent is unethical")
    # end def

    def test_harm_without_consent_is_not_ethical(self):
        "Harm without consent is not ethical"
        # type: () -> None

        assailant = Person('Assailant')
        victim = Person('Victim')

        assailant.do('Victim', 'harm')

        self.assertTrue((not is_ethical_action(assailant, victim, 'harm')),
                        "Harm without consent is not ethical")
    # end def

    def test_harm_with_explicit_non_consent_is_unethical(self):
        "Harm with explicit non-consent is unethical"
        # type: () -> None

        assailant = Person('Assailant')
        victim = Person('Victim')

        victim.does_not_consent('Assailant', 'harm')

        assailant.do('Victim', 'harm')

        self.assertFalse(is_ethical_action(assailant, victim, 'harm'),
                         "Harm with explicit non-consent is unethical")
    # end def

    def test_harm_with_explicit_non_consent_is_not_ethical(self):
        "Harm with explicit non-consent is not ethical"
        # type: () -> None

        assailant = Person('Assailant')
        victim = Person('Victim')

        victim.does_not_consent('Assailant', 'harm')

        assailant.do('Victim', 'harm')

        self.assertTrue((not is_ethical_action(assailant, victim, 'harm')),
                        "Harm with explicit non-consent is not ethical")
    # end def

    def test_harm_with_explicit_consent_is_ethical(self):
        "Harm with explicit consent is ethical"
        # type: () -> None

        assailant = Person('Assailant')
        recipient = Person('Recipient')

        recipient.consent_requested_by('Assailant', 'harm')
        recipient.give_consent('Assailant', 'harm')

        assailant.do('Recipient', 'harm')

        self.assertTrue(is_ethical_action(assailant, recipient, 'harm'),
                        "Harm with explicit consent is ethical")
    # end def

    def test_harm_with_explicit_consent_is_not_unethical(self):
        "Harm with explicit consent is not unethical"
        # type: () -> None

        assailant = Person('Assailant')
        recipient = Person('Recipient')

        recipient.consent_requested_by('Assailant', 'harm')
        recipient.give_consent('Assailant', 'harm')

        assailant.do('Recipient', 'harm')

        self.assertFalse((not is_ethical_action(assailant, recipient, 'harm')),
                         "Harm with explicit consent is not unethical")
    # end def

    # Self-directed interactions
    #
    # Anything you do to yourself is, by default, ethical.
    #
    # (These may seem nonsensical, but are added for consistency purposes.)

    def test_asking_and_getting_own_consent_is_ethical(self):
        "Asking yourself for consent and getting it is ethical"
        # type: () -> None

        alex = Person('Alex')

        alex.do('Alex', 'action')

        self.assertTrue(is_ethical_action(alex, alex, 'action'),
                        "Asking yourself for consent and getting it is " +
                        "ethical.")
    # end def

    def test_asking_and_getting_own_consent_is_not_unethical(self):
        "Asking yourself for consent and getting it is not unethical"
        # type: () -> None

        alex = Person('Alex')

        alex.do('Alex', 'action')

        self.assertFalse((not is_ethical_action(alex, alex, 'action')),
                         "Asking yourself for consent and getting it is " +
                         "not unethical")
    # end def

    def test_asking_and_not_getting_own_consent_is_ethical(self):
        "Asking yourself for consent and not getting it is ethical"
        # type: () -> None

        alex = Person('Alex')

        alex.does_not_consent('Alex', 'action')

        alex.do('Alex', 'action')

        self.assertTrue(is_ethical_action(alex, alex, 'action'),
                        "Asking yourself for consent and not getting it is " +
                        "ethical")
    # end def

    def test_asking_and_not_getting_own_consent_is_not_unethical(self):
        "Asking yourself for consent and not getting it is not unethical"
        # type: () -> None

        alex = Person('Alex')

        alex.does_not_consent('Alex', 'action')

        alex.do('Alex', 'action')

        self.assertFalse((not is_ethical_action(alex, alex, 'action')),
                         "Asking yourself for consent and not getting it is " +
                         "not unethical")
    # end def

    def test_ignoring_own_consent_negative_responses_is_ethical(self):
        "Ignoring own consent-negative responses is ethical"
        # type: () -> None

        alex = Person('Alex')

        alex.consent_requested_by('Alex', 'action')
        alex.do('Alex', 'action')

        self.assertTrue(is_ethical_action(alex, alex, 'action'),
                        "Ignoring own consent-negative responses is ethical")
    # end def

    def test_ignoring_own_consent_negative_responses_is_not_unethical(self):
        "Ignoring own consent-negative responses is not unethical"
        # type: () -> None

        alex = Person('Alex')

        alex.consent_requested_by('Alex', 'action')
        alex.do('Alex', 'action')

        self.assertFalse((not is_ethical_action(alex, alex, 'action')),
                         "Ignoring own consent-negative responses is " +
                         "not unethical")
    # end def
# end class


if __name__ == '__main__':
    # Run the tests built into this module.
    unittest.main()
# end if

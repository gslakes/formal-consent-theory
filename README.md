Formal consent theory-based ethics
==================================

A first-order logic formalisation of consent theory-based ethics, intended for eventual use
as a machine ethics system.



Frequently asked questions
--------------------------

Q. What does formalisation mean?

A.

This is translating a set of ideas into precise, mathematical rules that can be used by humans and
machines while making decisions.


Q. What is machine ethics? Why is this important or useful?

A.

Machine ethics is teaching machines how to be ethical in their interactions with humans,
through formalising ethical principles.

This is important and useful, as computer-based systems are simultaneously gaining
more autonomy and more influence over human lives.

While this in itself is not necessarily a bad thing, machines need to know what harm and
ethical behaviour is, if they are to understand how to be ethical, and work to avoid harm.


Q. Why consent theory?

A.

Consent theory appears to unify a number of ethical disciplines in a manner that is
relatively easy for both humans and machines to use to make decisions.


Q. Is there a use for a formal consent theory beyond machine ethics?

A.

Yes! This system could also be used as part of legal systems, charters, or contracts to precisely
define what being ethical or unethical means.


Q. Why first-order logic, and not a modal logic, like formal ethics, or another similar system?

A.

First-order logic makes specifying state easier (if with some loss of clarity in temporal
reasoning), and is widely support by automated proof/reasoning tools, such as the automated
theorem prover, `Prover 9`, and the associated model checker, `Mace 4`, which this project uses.

The availability of these tools makes checking safety properties significantly easier, which is
important in systems which, one day, may make life or death decisions.

(The author also admits a bias in having much more familiarity with FOL-based logics.)


Q. Will this bring about SkyNet/an `unfriendly AI` or the Singularity/a `friendly AI`?

A.

No. Or more precisely, not by itself.

This system doesn't have any ability to act on its own (being a system of rules only),
and so can't achieve anything, friendly or unfriendly, by itself.

The purpose of machine ethics is to prevent machines from behaving unethically, so its hoped
that by the time we have the capability to build a general artificial intelligence,
we'll have a robust and well-tested machine ethics system to build into it to prevent it from
being harmful, and to prevent it from being used by others to do harmful things.



Planned features
----------------

 - a positive-consent-only model of consent.

   (i.e. the absence of a negative consent response does not grant consent.)

 - time-aware consent reasoning, with interactions having time spans, revocation of prior
   consent grants (including revocation mid-action), and recognition of the temporary nature
   of consent.

   (i.e. that barring explicitly-negotiated, multiple-interaction-spanning consent grants, each
   new interaction creates a new obligation for a new consent grant.)

 - a multi-mode consent grant model e.g. directly communicated consent, legal instruments,
   consent by proxy.

 - modelling autonomy/self-determination/capability (`agency`) as part of a person's `state`,
   with harm defined as an impact on that agency.

   (This is to allow choice of the most ethical course of action in multiple-choice scenarios.)

 - consent modelled as an agency, with the goal of permitting only interactions that improve
   consent agency when the ability to consent is impaired, where prior consent doesn't exist.

 - a general model of informed consent by adding (doxastic/Smullyan-style) knowledge/`belief`
   statements about the (known/assumed) harm of an interaction to the state observed by the system.

   (e.g. if a disparity in the knowledge/belief of the harm of an interaction exists,
    the more accurately this information is conveyed, the greater the degree of ethical
    behaviour deemed obtained by the initiator, if they had the greater knowledge beforehand.)

 - special treatment of core agencies such as consent (and other agencies that uncoerced/informed
   consent depends upon, e.g. living, communicating, reasoning, learning) in interaction
   comparisons, so that paternalistic/consent-overriding interactions (where consent is not
   granted and would be possible to obtain) that would technically result in a net gain of agency
   are considered unethical.

 - modelling self-directed interactions and harm (i.e. where the ethical system is a direct actor.)

 - a treatment of harassment/repetition-based harm, if previous features don't supply this
   result already.

 - a treatment of the impact of power/privilege/knowledge/agency disparity on ethical behaviour,
   if previous features don't supply this result already.

 - modelling various physical, psychological/emotional, political and social agencies, and testing
   these against scenarios brainstormed with fellow participants of a Queensland Association for
   Healthy Communities (QAHC, http://qahc.org.au) healthy relationships, consent, and violence
   workshop.



Getting started
---------------

The `.in` files in this code repository contain machine-readable theories and automated tests.
These are for use with the Prover 9 (http://www.cs.unm.edu/~mccune/mace4/)
automated theorem prover via a Python-based test suite runner provided in this code repository,
`run_as_prover9_test_suite.py`.

It is recommended to get started by studying the demonstration system in `naive_consent_theory.in`,
which contains a simplistic/'naive' formalisation of consent theory-based ethics.

On a Linux/Unix machine with Prover 9 and a Python interpreter installed, this system may be tested
by the following command line, run from the base directory of a copy of this code repository:

    python run_as_prover9_test_suite.py naive_consent_theory.in

Other systems can be tested by replacing `naive_consent_theory.in` in the above command line with the
file name of the system to be tested.



Contact the author
------------------

For further assistance or to offer constructive feedback, please contact the author via
lakes`dot`gs`at`gmail`dot`com
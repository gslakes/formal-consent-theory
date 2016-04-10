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

Also, many existing systems don't model consent and autonomy, and so there's a range
of interactions permitted by these system that would be commonly deemed illegal or unethical.


Q. Is there a use for a formal consent theory beyond machine ethics?

A.

Yes! This system could also be used as part of legal systems, charters, or contracts to precisely
define what being ethical or unethical means.


Q. Why first-order logic, and not a modal logic, like formal ethics, or another similar system?

A.

First-order logic makes specifying state easier (if with some loss of clarity in temporal
reasoning), and is widely support by a large number of automated proof/reasoning tools.

The availability of these tools makes checking safety properties significantly easier, which is
important in systems which, one day, may make life or death decisions.

(The author also admits a bias in having much more familiarity with FOL-based logics.)


Q. Will this bring about SkyNet/an `unfriendly AI` or the Singularity/a `friendly AI`?

A.

No. Or more precisely, not by itself.

This system doesn't have any ability to act on its own (being a system of rules only),
and so can't achieve anything, friendly or unfriendly, by itself.

The purpose of machine ethics is to prevent machines from behaving unethically, so it's hoped
that by the time we have the capability to build a general artificial intelligence,
we'll have a robust and well-tested machine ethics system to build into it to prevent it from
being harmful, and to prevent it from being used by others to do harmful things.



Planned features
----------------

 - a positive-consent-only model of consent.

   (i.e. the absence of a negative consent response does not grant consent.)

   Why: 'Opt-in'/'affirmative consent'/'enthusiastic consent' helps prevent harmful actions from being
   started in the case where consent is not granted (particularly so when consent/lack of consent can't be
   communicated), and removes uncertainty about if/when consent is/was granted.

   It is also a key principle of many legal/ethical systems i.e. 'opt out' behaviour is recognised to
   be harmful/unethical.


 - time-aware consent reasoning, with interactions having time spans, revocation of prior
   consent grants (including revocation mid-action), and recognition of the temporary nature
   of consent.

   (i.e. that barring explicitly-negotiated, multiple-interaction-spanning consent grants, each
   new interaction creates a new obligation for a new consent grant.)

   Why: consent is typically understood to not endure indefinitely, and that each new transaction
   requires a new grant, as circumstances may have changed in the meanwhile.

   Also, if an action is unexpectedly harmful, proceeding with the action past the point where consent is
   withdrawn is harmful, and typically considered to be assault under most legal/ethical systems.


 - a multi-mode consent grant model e.g. directly communicated consent, legal instruments,
   consent by proxy.

   Why: there are many situations in which direct communication of consent may not be possible
   (i.e. emergency situations), supporting other modes of consent allows ethical behaviour in these situations.


 - modelling autonomy/self-determination/capability (`agency`) as part of a person's `state`,
   with harm defined as an impact on that agency.

   Why: this is to allow choice of the most ethical course of action in multiple-choice scenarios, by
   choosing an option that results in the maximum agency/autonomy afterwards.


 - consent modelled as an agency, with the goal of permitting only interactions that improve
   consent agency when the ability to consent is impaired, where prior consent doesn't exist.

   Why: to prevent the system inadvertently or deliberately impairing the ability to consent (further),
   in order to deem a particular course of action (falsely) ethical under emergency action rules.


 - a general model of informed consent by adding (doxastic/Smullyan-style) knowledge/`belief`
   statements about the (known/assumed) harm of an interaction to the state observed by the system.

   Why: if a difference in the knowledge/belief of the harm of an interaction exists,
   the more accurately this information is conveyed, the more ethical each party can be considered,
   as this allows harm to both/all parties to be minimised through joint planning.


 - special treatment of core agencies such as consent (and other agencies that uncoerced/informed
   consent depends upon, e.g. living, communicating, reasoning, learning) in interaction
   comparisons.

   Why: so that paternalistic/consent-overriding interactions (where consent is not
   granted and would be possible to obtain) that would technically result in a net gain of agency
   are considered unethical.

   (Paternalism often ignores that each person typically possesses special knowledge about their
    circumstances unknown to other parties, beyond that ignoring the need for/not seeking consent is
    typically considered assault in most legal/ethical systems.)


 - modelling self-directed interactions and harm (i.e. where the ethical system is a direct actor.)

   Why: so that the system can choose harm to itself as part of its agency.

   This may mean that a preference exists to allow harm to the system actor before others are harmed.
   Also, that certain acts considered by others to be harmful may not be considered harmful by the
   implementing actor (or are otherwise preferable), or that a smaller harm may be consented to in
   order to prevent a greater harm.

   (This allows modelling consent-respecting utilitarianism involving the system's consent, covering a range of
    activities that are considered assault - or worse - without prior consent e.g. medicine, BDSM, euthanasia.)


 - a treatment of harassment/repetition-based harm, if previous features don't supply this
   result already.

   Why: most ethical/moral/legal frameworks recognise the increased harm caused by repetition of
   actions that may otherwise individually be considered harmless or minimally harmful.


 - a treatment of the impact of power/privilege/knowledge/agency disparity on ethical behaviour,
   if previous features don't supply this result already.

   Why: power differences impair full freedom of choice on the side of the party with less power/status,
   due to the implied or explicitly stated harm if the activity is not consented to.
   (i.e. extortion, implied loss of status/position/opportunity.)



 - a treatment of privacy, for individuals and organisations, if previous features don't supply
   this result already.

   Why: violation of personal privacy often leads to harm, and should be considered an agency in itself.

   Privacy for organisations is more complex, with an argument to be considered that the more
   powerful an organisation, the more transparent its actions and decision making processes should be,
   to help avoid abusive behaviour by the organisation against the public.


 - modelling various physical, psychological/emotional, political, and social agencies, and testing
   these against scenarios brainstormed with fellow participants of a Queensland Association for
   Healthy Communities (QAHC, now the Queensland AIDS Council, http://www.quac.org.au/) healthy relationships,
   consent, and violence workshop.

   Why: these agencies help model a range of complex situations, hopefully to the complexity needed to navigate
   society safely alongside humans.



How to use this system
----------------------

Consider using one of the supported theorem provers in the planning/decision making parts of
your AI/ML system, implementing the range and consequences of potential system actions in this
formal consent theory framework.

This is so that only ethical combinations of actions can even be considered, which will (hopefully!) prevent both
overt and covert planning of unethical/unfriendly/hostile actions.

However, for non-rule-based systems where the decision process is a black box, you may be able to use
this system as an external ethical governor or permissible action framework.

(This is likely riskier, as a particularly sophisticated system may be able to outwit or bypass this framework by
generating false observations, engineering circumstances to permit particular actions,
performing software/hardware self-modification, or some other outside-logic-context trickery.)

Please test exhaustively and imaginatively, and consider opening your final system up to testing by the broader
AI and software verification communities before autonomous/unconstrained continuous-experience-building use, so that
many eyes may make (humanity-threatening) bugs shallow.



Getting started
---------------

The `.in` and `.tptp` files in this code repository contain machine-readable theories and automated tests.


The `.in` files are for use with the Prover9 (http://www.cs.unm.edu/~mccune/mace4/)
automated theorem prover via a Python-based test suite runner provided in this code repository,
`run_as_prover9_test_suite.py`.

The `.tptp` files are versions of the same theories and tests for use with TPTP-compatible provers, and may
be used with a similar test runner, `run_as_tptp_test_suite.py`, which can use either
E prover (http://www.eprover.org) or Z3 prover (https://github.com/z3prover/z3/wiki) as its prover.


It is recommended to get started by studying the demonstration system in `naive_consent_theory.tptp`
(or identically in `naive_consent_theory.in`), which contains a simplistic/'naive' formalisation of
consent theory-based ethics.


For the quickest start, copying definitions and individual test cases from the TPTP version of this
demonstration system into the web-based System on TPTP prover at

    http://www.cs.miami.edu/~tptp/cgi-bin/SystemOnTPTP

should allow basic exploration of the system without needing to install a prover.


For more in-depth/protracted use, installation of either Prover9, E prover, or Z3, and the use of the test runners
is highly recommended, as this is a far more convenient way to test any trial modifications you may wish to make.
(This also avoids taxing the resources of the generous people running System on TPTP.)

Please see the documentation at the start of either test runner for further installation and use instructions.



Contact the author
------------------

For further assistance or to offer constructive feedback, please contact the author via
lakes`dot`gs`at`gmail`dot`com
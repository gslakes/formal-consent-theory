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

Also, many existing systems don't model consent and autonomy (using instead preferences or 
permitted/forbidden actions), and so there's a range of interactions permitted by these
systems that would be commonly deemed illegal or unethical.


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


Current features
----------------

The included 'naive'/simplistic consent theory implements a simple model of consent,
yet consent by itself is enough to distinguish between medicine, assault,
euthanasia, suicide, and murder.

It has the following features in particular: 

 - a positive-consent-only model of consent.

   (i.e. the absence of a negative consent response does not grant consent.)

   Why: 'Opt-in'/'affirmative consent'/'enthusiastic consent' helps prevent harmful actions from being
   started in the case where consent is not granted (particularly so when consent/lack of consent can't be
   communicated), and removes uncertainty about if/when consent is/was granted.

   It is also a key principle of many legal/ethical systems i.e. 'opt out' behaviour is recognised to
   be harmful/unethical.

 - a simple model of self-directed actions.

   Why: consent has one or two simple exemptions, in that you don't need to ask your own consent
   before you do something that has no impact on others.


Planned features
----------------

Future theories are intended to have the following features:

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


 - more modelling of self-directed interactions and harm (particularly where the ethical system is a direct actor.)

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


 - a consideration of the impact of hate speech, if previous features don't supply this result already.

   Why: vilification of minority groups is harmful to those vilified, both directly (i.e. emotional harm,
   reinforcement of incorrect beliefs of inferiority) and indirectly, by the acts it encourages.
   (i.e. abuse, hate crime, genocide.)

   While it's not intended that this system should work to prevent hate speech, or regulate speech at all - this would
   violate the agency of the speaker - it should be understood that such speech is harmful in itself, and understood
   that making this kind of speech registers an intent to harm further.
   
   (Even if such intent is denied or retracted - 'only joking'.)



 - a consideration of how to act to minimise harm, if the system is given responsibility/trust to do so.

   Why: this is a potential use of this system, so reasoning about how to minimise the harm of actions
   taken to prevent harm is important.

   There are many dystopian depictions in fiction of overly-zealous (AI) systems enforcing social policy and
   causing greater harm while doing so, so testing to prevent these pathological scenarios is important.
   
   Restraining someone because they are judged likely to commit harm (aka 'pre-crime') is anti-agency.
   
   Acts to prevent violence should only be taken immediately before the violence would be performed -
   i.e. with weapon poised to strike - in case the harmful act is not perpetrated.
   (At the latest possible causal branching point to establish to human satisfaction that harm would have been done.) 

   Conversely, acts that just look violent (i.e. martial arts or theatre, ala Scheckley's 'Watchbird'), may or even
   will cause harm (i.e. driving, medicine, BDSM, etc) should not be prevented if the participants have
   meaningfully consented to the act.

   An understanding of the proportionality of force (if using force is available/desired) is also important.
   (A system that murders someone to prevent bruises is pathological.)
 


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

It is recommended to get started by studying the demonstration system in `naive_consent_theory.py`
(or more formally in `naive_consent_theory.in` or `naive_consent_theory.tptp`), which contains a
simplistic/'naive' formalisation of consent theory-based ethics.


The `naive_consent_theory.py` file contains a Python implementation of the naive consent theory.
A test suite contained within can be run via `python naive_consent_theory.py`.  

The `naive_consent_theory.in` files are for use with the Prover9 (http://www.cs.unm.edu/~mccune/mace4/)
automated theorem prover via a Python-based test suite runner provided in this code repository,
`run_as_prover9_test_suite.py`.

The `naive_consent_theory.tptp` files are for use with TPTP-compatible provers, and may
be used with a similar test runner, `run_as_tptp_test_suite.py`, which can use either
E prover (http://www.eprover.org) or Z3 prover (https://github.com/z3prover/z3/wiki) as its prover.

(`consent_theory.in` is an in-progress attempt at extending this theory further.)


If you want to extend these theories, please consider doing so using the theorem prover versions
of this theory, as formal proof can give (much needed) assurances of correctness code can not.

The quickest start with the formal proof version will be via copying definitions and
individual test cases from the TPTP version of this demonstration system into the
web-based System on TPTP prover at

    http://www.cs.miami.edu/~tptp/cgi-bin/SystemOnTPTP

which should allow basic exploration of the system without needing to install a prover.


For more in-depth/protracted use, installation of either Prover9, E prover, or Z3, and the use of the test runners
is highly recommended, as this is a far more convenient way to test any trial modifications you may wish to make.
(This also avoids taxing the resources of the generous people running System on TPTP.)

Please see the documentation at the start of either implementation for further installation and
use instructions.



Contact the author
------------------

For further assistance or to offer constructive feedback, please contact the author via
lakes`dot`gs`at`gmail`dot`com
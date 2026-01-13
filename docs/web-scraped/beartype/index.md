# Source: https://beartype.readthedocs.io/en/latest/index/

Tip

💗 **Upbear us** at [GitHub Sponsors](https://github.com/sponsors/leycec) and SonarQube Advanced Security
(Tidelift). **Follow us** [on Bluesky](https://leycec.bsky.social). **Friendzone us** [at Zulip](https://beartype.zulipchat.com).
Your generous support is our quality assurance. 💗

[](https://github.com/beartype/beartype)

[](https://codecov.io/gh/beartype/beartype) [](https://github.com/beartype/beartype/actions?workflow=tests) [](https://beartype.readthedocs.io/en/latest/?badge=latest)

**Beartype** is an [open-source](https://github.com/beartype/beartype/blob/main/LICENSE) [pure-Python](faq/#faq-pure) [PEP-compliant](pep/#pep-pep) [near-real-time](faq/#faq-realtime)
[hybrid runtime-static](faq/#faq-hybrid) [third-generation](faq/#faq-third)
[type-checker](eli5/#eli5-eli5) emphasizing efficiency, usability,
unsubstantiated jargon we just made up, and thrilling puns.
Beartype enforces [type hints](eli5/#eli5-typing) across your entire app in
[two lines of runtime code with no runtime overhead](api_claw/#api-claw-api-claw).
If seeing is believing, prepare to do both those things.
# Install beartype.
$ pip3 install beartype

# Edit the &quot;{your_package}.__init__&quot; submodule with your favourite IDE.
$ vim {your_package}/__init__.py # &lt;-- so, i see that you too vim

# At the very top of your &quot;{your_package}.__init__&quot; submodule:
from beartype.claw import beartype_this_package # &lt;-- boilerplate for victory
beartype_this_package() # &lt;-- yay! your team just won

Beartype now implicitly type-checks *all* annotated classes, callables, and
variable assignments across *all* submodules of your package. Congrats. This day
all bugs die.
But why stop at the burning tires in only *your* code? Your app depends on a
sprawling ghetto of other packages, modules, and services. How riddled with
infectious diseases is *that* code? You’re about to find out.
# ....................{ BIG BEAR }....................
# Warn about type hint violations in *OTHER* packages outside your control;
# only raise exceptions from violations in your package under your control.
# Again, at the very top of your &quot;{your_package}.__init__&quot; submodule:
from beartype import BeartypeConf # &lt;-- this isn&#39;t your fault
from beartype.claw import beartype_all, beartype_this_package # &lt;-- you didn&#39;t sign up for this
beartype_this_package() # &lt;-- raise exceptions in your code
beartype_all(conf=BeartypeConf(violation_type=UserWarning)) # &lt;-- emit warnings from other code

Beartype now implicitly type-checks *all* annotated classes, callables, and
variable assignments across *all* submodules of *all* packages. When **your**
package violates type safety, beartype raises an exception. When any **other**
package violates type safety, beartype just emits a warning. The triumphal
fanfare you hear is probably your userbase cheering. This is how the QA was won.
Beartype also publishes a plethora of APIs for fine-grained control over
type-checking. For those who are about to QA, beartype salutes you.
Would you like to know more?
# So let&#39;s do this.
$ python3

# ....................{ RAISE THE PAW }....................
# Manually enforce type hints across individual classes and callables.
# Do this only if you want a(nother) repetitive stress injury.

# Import the @beartype decorator.
&gt;&gt;&gt; from beartype import beartype # &lt;-- eponymous import; it&#39;s eponymous

# Annotate @beartype-decorated classes and callables with type hints.
&gt;&gt;&gt; @beartype # &lt;-- you too will believe in magic
... def quote_wiggum(lines: list[str]) -&gt; None:
... print(&#39;“{}”\n\t— Police Chief Wiggum&#39;.format(&quot;\n &quot;.join(lines)))

# Call those callables with valid parameters.
&gt;&gt;&gt; quote_wiggum([&quot;Okay, folks. Show&#39;s over!&quot;, &quot; Nothing to see here. Show&#39;s…&quot;,])
“Okay, folks. Show&#39;s over!
 Nothing to see here. Show&#39;s…”
 — Police Chief Wiggum

# Call those callables with invalid parameters.
&gt;&gt;&gt; quote_wiggum([b&quot;Oh, my God! A horrible plane crash!&quot;, b&quot;Hey, everybody! Get a load of this flaming wreckage!&quot;,])
Traceback (most recent call last):
 File &quot;&lt;stdin&gt;&quot;, line 1, in &lt;module&gt;
 File &quot;&lt;string&gt;&quot;, line 30, in quote_wiggum
 File &quot;/home/springfield/beartype/lib/python3.9/site-packages/beartype/_decor/_code/_pep/_error/errormain.py&quot;, line 220, in get_beartype_violation
 raise exception_cls(
beartype.roar.BeartypeCallHintParamViolation: @beartyped
quote_wiggum() parameter lines=[b&#39;Oh, my God! A horrible plane
crash!&#39;, b&#39;Hey, everybody! Get a load of thi...&#39;] violates type hint
list[str], as list item 0 value b&#39;Oh, my God! A horrible plane crash!&#39;
not str.

# ....................{ MAKE IT SO }....................
# Squash bugs by refining type hints with @beartype validators.
&gt;&gt;&gt; from beartype.vale import Is # &lt;---- validator factory
&gt;&gt;&gt; from typing import Annotated # &lt;---------------- if Python ≥ 3.9.0
# &gt;&gt;&gt; from typing_extensions import Annotated # &lt;-- if Python &lt; 3.9.0

# Validators are type hints constrained by lambda functions.
&gt;&gt;&gt; ListOfStrings = Annotated[ # &lt;----- type hint matching non-empty list of strings
... list[str], # &lt;----------------- type hint matching possibly empty list of strings
... Is[lambda lst: bool(lst)] # &lt;-- lambda matching non-empty object
... ]

# Annotate @beartype-decorated callables with validators.
&gt;&gt;&gt; @beartype
... def quote_wiggum_safer(lines: ListOfStrings) -&gt; None:
... print(&#39;“{}”\n\t— Police Chief Wiggum&#39;.format(&quot;\n &quot;.join(lines)))

# Call those callables with invalid parameters.
&gt;&gt;&gt; quote_wiggum_safer([])
beartype.roar.BeartypeCallHintParamViolation: @beartyped
quote_wiggum_safer() parameter lines=[] violates type hint
typing.Annotated[list[str], Is[lambda lst: bool(lst)]], as value []
violates validator Is[lambda lst: bool(lst)].

# ....................{ AT ANY TIME }....................
# Type-check anything against any type hint – anywhere at anytime.
&gt;&gt;&gt; from beartype.door import (
... is_bearable, # &lt;-------- like &quot;isinstance(...)&quot;
... die_if_unbearable, # &lt;-- like &quot;assert isinstance(...)&quot;
... )
&gt;&gt;&gt; is_bearable([&#39;The&#39;, &#39;goggles&#39;, &#39;do&#39;, &#39;nothing.&#39;], list[str])
True
&gt;&gt;&gt; die_if_unbearable([0xCAFEBEEF, 0x8BADF00D], ListOfStrings)
beartype.roar.BeartypeDoorHintViolation: Object [3405692655, 2343432205]
violates type hint typing.Annotated[list[str], Is[lambda lst: bool(lst)]],
as list index 0 item 3405692655 not instance of str.

# ....................{ GO TO PLAID }....................
# Type-check anything in around 1µs (one millionth of a second) – including
# this list of one million 2-tuples of NumPy arrays.
&gt;&gt;&gt; from beartype.door import is_bearable
&gt;&gt;&gt; from numpy import array, ndarray
&gt;&gt;&gt; data = [(array(i), array(i)) for i in range(1000000)]
&gt;&gt;&gt; %time is_bearable(data, list[tuple[ndarray, ndarray]])
 CPU times: user 31 µs, sys: 2 µs, total: 33 µs
 Wall time: 36.7 µs
True

# ....................{ MAKE US DO IT }....................
# Don&#39;t know type hints? Do but wish you didn&#39;t? What if somebody else could
# write your type hints for you? @beartype: it&#39;s somebody. Let BeartypeAI™
# write your type hints for you. When you no longer care, call BeartypeAI™.
&gt;&gt;&gt; from beartype.bite import infer_hint # &lt;----- caring begins

# What type hint describes the root state of a Pygments lexer, BeartypeAI™?
&gt;&gt;&gt; from pygments.lexers import PythonLexer
&gt;&gt;&gt; infer_hint(PythonLexer().tokens[&quot;root&quot;])
list[
 tuple[str | pygments.token._TokenType[str], ...] |
 tuple[str | collections.abc.Callable[
 typing.Concatenate[object, object, ...], object], ...] |
 typing.Annotated[
 collections.abc.Collection[str],
 beartype.vale.IsInstance[pygments.lexer.include]]
] # &lt;---- caring ends

# ...all righty then. Guess I&#39;ll just take your word for that, BeartypeAI™.

Beartype brings [Rust](https://www.rust-lang.org)- and [C++](https://en.wikipedia.org/wiki/C%2B%2B)-inspired [zero-cost abstractions](https://boats.gitlab.io/blog/post/zero-cost-abstractions) into the lawless world of [dynamically-typed](https://en.wikipedia.org/wiki/Type_system) Python by
[enforcing type safety at the granular level of functions and methods](eli5/#eli5-eli5) against [type hints standardized by the Python community](pep/#pep-pep) in \(O(1)\) non-amortized worst-case time with negligible
constant factors. If the prior sentence was unreadable jargon, see
[our friendly and approachable FAQ for a human-readable synopsis](faq/#faq-faq).
Beartype is [portably implemented](https://github.com/beartype/beartype/tree/main/beartype) in [Python 3](https://www.python.org), [continuously stress-tested](https://github.com/beartype/beartype/actions?workflow=tests) via GitHub
Actions **×** [tox](https://tox.readthedocs.io) **×** [pytest](https://docs.pytest.org) **×** [Codecov](https://about.codecov.io), and permissively
distributed under the [MIT license](https://opensource.org/licenses/MIT). Beartype has *no*
runtime dependencies, [only one test-time dependency](https://docs.pytest.org), and only
one documentation-time dependency. Beartype supports all actively
developed Python versions, [all Python package managers](install/#install), and [multiple platform-specific package managers](install/#install).
Beartype [powers quality assurance across the Python ecosystem](https://github.com/beartype/beartype/network/dependents).

# The Typing Tree[¶](#the-typing-tree)

Welcome to the **Bearpedia** – your one-stop Encyclopedia Beartanica for all
things &#64;beartype. It’s “[typing](https://docs.python.org/3/library/typing.html) or bust!” as you…

Bear with Us

- [Bearpedia](#)

[Install](install/)
[Platform](install/#platform)
- [macOS](install/#macos)

- [Arch Linux](install/#arch-linux)

- [Gentoo Linux](install/#gentoo-linux)

- [Badge](install/#badge)

- [tl;dr](tldr/)

[ELI5](eli5/)
[Comparison](eli5/#comparison)
- […versus Static Type-checkers](eli5/#versus-static-type-checkers)

- […versus Runtime Type-checkers](eli5/#versus-runtime-type-checkers)

[Quickstart](eli5/#quickstart)
[Standard Hints](eli5/#standard-hints)
- [Toy Example](eli5/#toy-example)

- [Industrial Example](eli5/#industrial-example)

[Tutorial](eli5/#tutorial)
- [Builtin Types](eli5/#builtin-types)

- [Arbitrary Types](eli5/#arbitrary-types)

- [Unions of Types](eli5/#unions-of-types)

- [Optional Types](eli5/#optional-types)

- [Would You Like to Know More?](eli5/#would-you-like-to-know-more)

[API](api/)
- [The Left-Paw Path](api/#the-left-paw-path)

[FAQ](faq/)
- [What is beartype?](faq/#what-is-beartype)

- [What is typeguard?](faq/#what-is-typeguard)

- [When should I use beartype?](faq/#when-should-i-use-beartype)

- [Does beartype do any bad stuff?](faq/#does-beartype-do-any-bad-stuff)

- [Does beartype actually do anything?](faq/#does-beartype-actually-do-anything)

- [How much does all this *really* cost?](faq/#how-much-does-all-this-really-cost)

- [Beartype just does random stuff? Really?](faq/#beartype-just-does-random-stuff-really)

- [What does “pure-Python” mean?](faq/#what-does-pure-python-mean)

- [What does “near-real-time” even mean? Are you just making stuff up?](faq/#what-does-near-real-time-even-mean-are-you-just-making-stuff-up)

- [What does “hybrid runtime-static” mean? Pretty sure you made that up, too.](faq/#what-does-hybrid-runtime-static-mean-pretty-sure-you-made-that-up-too)

- [“Third-generation type-checker” doesn’t mean anything, does it?](faq/#third-generation-type-checker-doesn-t-mean-anything-does-it)

[How do I type-check…](faq/#how-do-i-type-check)
- […Boto3 types?](faq/#boto3-types)

- […JAX arrays?](faq/#jax-arrays)

- […NumPy arrays?](faq/#numpy-arrays)

- […PyTorch tensors?](faq/#pytorch-tensors)

- […mock types?](faq/#mock-types)

- […pandas data frames?](faq/#pandas-data-frames)

- […the current class?](faq/#the-current-class)

- […under VSCode?](faq/#under-vscode)

- […under [insert-IDE-name-here]?](faq/#under-insert-ide-name-here)

- […with type narrowing?](faq/#with-type-narrowing)

- [How do I *ONLY* type-check while running my test suite?](faq/#how-do-i-only-type-check-while-running-my-test-suite)

- [How do I *NOT* type-check something?](faq/#how-do-i-not-type-check-something)

- [Why is &#64;leycec’s poorly insulated cottage in the Canadian wilderness so cold?](faq/#why-is-leycec-s-poorly-insulated-cottage-in-the-canadian-wilderness-so-cold)

- [Features](pep/)

[Code](code/)
[Beartype Code Generation: It’s All for You](code/#beartype-code-generation-it-s-all-for-you)
- [Identity Decoration](code/#identity-decoration)

- [Unconditional Identity Decoration](code/#unconditional-identity-decoration)

- [Shallow Identity Decoration](code/#shallow-identity-decoration)

- [Deep Identity Decoration](code/#deep-identity-decoration)

[Constant Decoration](code/#constant-decoration)
- [Constant Builtin Type Decoration](code/#constant-builtin-type-decoration)

- [Constant Non-Builtin Type Decoration](code/#constant-non-builtin-type-decoration)

- [Constant Shallow Sequence Decoration](code/#constant-shallow-sequence-decoration)

- [Constant Deep Sequence Decoration](code/#constant-deep-sequence-decoration)

- [Constant Nested Deep Sequence Decoration](code/#constant-nested-deep-sequence-decoration)

[Beartype Dev Handbook: It’s Handy](code/#beartype-dev-handbook-it-s-handy)
- [Dev Workflow](code/#dev-workflow)

- [Moar Depth](code/#moar-depth)

- [Moar Compliance](code/#moar-compliance)

[Math](math/)
[Beartype Timings](math/#beartype-timings)
- [Timings Overview](math/#timings-overview)

[Timings Lower Bound](math/#timings-lower-bound)
- [Formulaic Formulas: They’re Back in Fashion](math/#formulaic-formulas-they-re-back-in-fashion)

- [Function Call Overhead: The New Glass Ceiling](math/#function-call-overhead-the-new-glass-ceiling)

- [Holy Balls of Flaming Dumpster Fires](math/#holy-balls-of-flaming-dumpster-fires)

- [But, But… That’s Not Good Enough!](math/#but-but-that-s-not-good-enough)

- [Nobody Expects the Linearithmic Time](math/#nobody-expects-the-linearithmic-time)

[Moar](moar/)
- [Runtime Type Checkers](moar/#runtime-type-checkers)

- [Runtime Data Validators](moar/#runtime-data-validators)

- [Static Type Checkers](moar/#static-type-checkers)

*Let’s type this.*

# See Also[¶](#see-also)

Beartype plugins adjacent to your interests include:

[ipython-beartype](https://pypi.org/project/ipython-beartype), beartype’s official [IPython](https://ipython.org) plugin. Type-check:

- Browser-based [Jupyter](https://jupyter.org), [Marimo](https://marimo.io), and [Google Colab](https://colab.research.google.com) notebook cells.

- IDE-based [Zasper](https://zasper.io) notebook cells.

- Terminal-based [IPython](https://ipython.org) REPLs.

[pytest-beartype](https://pypi.org/project/pytest-beartype), beartype’s official [pytest](https://docs.pytest.org) plugin. Type-check packages
*only* at [pytest](https://docs.pytest.org) test-time. Fatally obsessed with speed? Fatally accepting of
critical failure? Can’t bear to type-check at runtime? When your team lacks
trust, your team chooses [pytest-beartype](https://pypi.org/project/pytest-beartype).

# License[¶](#license)

Beartype is [open-source software released](https://github.com/beartype/beartype/blob/main/LICENSE) under the
[permissive MIT license](https://opensource.org/licenses/MIT).

# Security[¶](#security)

Beartype encourages security researchers, institutes, and concerned netizens to
responsibly disclose security vulnerabilities as GitHub-originated Security
Advisories – published with full acknowledgement in the
public [GitHub Advisory Database](https://github.com/advisories).

# Funding[¶](#funding)

Beartype is financed as a purely volunteer open-source project via GitHub
Sponsors, to whom our burgeoning community is eternally
indebted. Without your generosity, runtime type-checking would be a shadow of
its current hulking bulk. We genuflect before your selfless charity, everyone!
Prior official funding sources (*yes, they once existed*) include:

A [Paul Allen Discovery Center award](https://www.alleninstitute.org/what-we-do/frontiers-group/news-press/press-resources/press-releases/paul-g-allen-frontiers-group-announces-allen-discovery-center-tufts-university) from the Paul G. Allen Frontiers
Group under the administrative purview of the Paul Allen Discovery
Center at [Tufts University](https://www.tufts.edu) over the period 2015—2018 preceding the
untimely death of [Microsoft co-founder Paul Allen](https://en.wikipedia.org/wiki/Paul_Allen), during
which beartype was maintained as the private `&#64;type_check` decorator in the
[Bioelectric Tissue Simulation Engine (BETSE)](https://github.com/betsee/betse). Phew!

# Contributors[¶](#contributors)

Beartype is the work product of volunteer enthusiasm, excess caffeine, and
sleepless Wednesday evenings. These brave GitHubbers hurtled the pull request
(PR) gauntlet so that you wouldn’t have to:
[](https://github.com/beartype/beartype/graphs/contributors)

It’s a heavy weight they bear. Applaud them as they buckle under the load!

# History[¶](#history)

Beartype’s histrionic past is checkered with drama, papered over in propaganda,
and chock full of the stuff of stars. Gaze upon their glistening visage as they
grow monotonically. But do the stars matter? Neither to mortal nor to bear. Yet,
by starlight, we all howl to commit by dawn.
[](https://github.com/beartype/beartype/stargazers)

 
 
 
 

 
 
 next

 Install

 
 **
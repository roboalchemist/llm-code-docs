# Source: https://beartype.readthedocs.io/en/latest

The Typing Tree — beartype 0.23.0 documentation[](#)
- [Bearpedia](#)
- [Install](install/)
- [tl;dr](tldr/)
- [ELI5](eli5/)
- [API](api/)
- [FAQ](faq/)
- [Features](pep/)
- [Code](code/)
- [Math](math/)
- [Moar](moar/)
- [**Zulip]()
- [**Bluesky]()
- [**GitHub]()
- [**PyPI]()
- [**Anaconda]()
- [**Libraries.io]()
- [**ReadTheDocs]()**
Bear with Us

- [Bearpedia](#)
- [Install](install/)
- [tl;dr](tldr/)
- [ELI5](eli5/)
- [API](api/)**
  - [Beartype Import Hooks](api_claw/)
  - [Beartype Decorator](api_decor/)
  - [Beartype Validators](api_vale/)
  - [Beartype Introspectors](api_door/)
  - [Beartype Errors](api_roar/)
1. [FAQ](faq/)
1. [Features](pep/)
1. [Code](code/)
1. [Math](math/)
1. [Moar](moar/)**On this page
- [The Typing Tree](#)
- [See Also](#see-also)
- [License](#license)
- [Security](#security)
- [Funding](#funding)
- [Contributors](#contributors)
- [History](#history)[**Edit this page]()
Tip

💗**Upbear us**at[GitHub Sponsors](https://github.com/sponsors/leycec)and[SonarQube Advanced Security
(Tidelift)](https://www.sonarsource.com/products/sonarqube/advanced-security).**Follow us**[on Bluesky](https://leycec.bsky.social).**Friendzone us**[at Zulip](https://beartype.zulipchat.com).
Your generous support is our quality assurance. 💗

[](https://github.com/beartype/beartype)

[](https://codecov.io/gh/beartype/beartype)[](https://github.com/beartype/beartype/actions?workflow=tests)[](https://beartype.readthedocs.io/en/latest/?badge=latest)

**Beartype**is an[open-source](https://github.com/beartype/beartype/blob/main/LICENSE)[pure-Python](faq/#faq-pure)[PEP-compliant](pep/#pep-pep)[near-real-time](faq/#faq-realtime)[hybrid runtime-static](faq/#faq-hybrid)[third-generation](faq/#faq-third)[type-checker](eli5/#eli5-eli5)emphasizing efficiency, usability,
unsubstantiated jargon we just made up, and thrilling puns.

Beartype enforces[type hints](eli5/#eli5-typing)across your entire app in[two lines of runtime code with no runtime overhead](api_claw/#api-claw-api-claw).
If seeing is believing, prepare to do both those things.

```
# Install beartype.$pip3installbeartype# Edit the "{your_package}.__init__" submodule with your favourite IDE.$vim{your_package}/__init__.py# <-- so, i see that you too vim
```

```
# At the very top of your "{your_package}.__init__" submodule:frombeartype.clawimportbeartype_this_package# <-- boilerplate for victorybeartype_this_package()# <-- yay! your team just won
```

Beartype now implicitly type-checks*all*annotated classes, callables, and
variable assignments across*all*submodules of your package. Congrats. This day
all bugs die.

But why stop at the burning tires in only*your*code? Your app depends on a
sprawling ghetto of other packages, modules, and services. How riddled with
infectious diseases is*that*code? You’re about to find out.

```
# ....................{ BIG BEAR                        }....................# Warn about type hint violations in *OTHER* packages outside your control;# only raise exceptions from violations in your package under your control.# Again, at the very top of your "{your_package}.__init__" submodule:frombeartypeimportBeartypeConf# <-- this isn't your faultfrombeartype.clawimportbeartype_all,beartype_this_package# <-- you didn't sign up for thisbeartype_this_package()# <-- raise exceptions in your codebeartype_all(conf=BeartypeConf(violation_type=UserWarning))# <-- emit warnings from other code
```

Beartype now implicitly type-checks*all*annotated classes, callables, and
variable assignments across*all*submodules of*all*packages. When**your**package violates type safety, beartype raises an exception. When any**other**package violates type safety, beartype just emits a warning. The triumphal
fanfare you hear is probably your userbase cheering. This is how the QA was won.

Beartype also publishes a[plethora of APIs for fine-grained control over
type-checking](api/#api-api). For those who are about to QA, beartype salutes you.
Would you like to know more?

```
# So let's do this.$python3
```

```
# ....................{ RAISE THE PAW                   }....................# Manually enforce type hints across individual classes and callables.# Do this only if you want a(nother) repetitive stress injury.# Import the @beartype decorator.>>>frombeartypeimportbeartype# <-- eponymous import; it's eponymous# Annotate @beartype-decorated classes and callables with type hints.>>>@beartype# <-- you too will believe in magic...defquote_wiggum(lines:list[str])->None:...print('“{}”\n\t— Police Chief Wiggum'.format("\n".join(lines)))# Call those callables with valid parameters.>>>quote_wiggum(["Okay, folks. Show's over!"," Nothing to see here. Show's…",])“Okay, folks. Show's over!Nothing to see here. Show's…”— Police Chief Wiggum# Call those callables with invalid parameters.>>>quote_wiggum([b"Oh, my God! A horrible plane crash!",b"Hey, everybody! Get a load of this flaming wreckage!",])Traceback (most recent call last):File"<stdin>", line1, in<module>File"<string>", line30, inquote_wiggumFile"/home/springfield/beartype/lib/python3.9/site-packages/beartype/_decor/_code/_pep/_error/errormain.py", line220, inget_beartype_violationraiseexception_cls(beartype.roar.BeartypeCallHintParamViolation:@beartypedquote_wiggum() parameter lines=[b'Oh, my God! A horrible planecrash!', b'Hey, everybody! Get a load of thi...'] violates type hintlist[str], as list item 0 value b'Oh, my God! A horrible plane crash!'not str.# ....................{ MAKE IT SO                      }....................# Squash bugs by refining type hints with @beartype validators.>>>frombeartype.valeimportIs# <---- validator factory>>>fromtypingimportAnnotated# <---------------- if Python ≥ 3.9.0# >>> from typing_extensions import Annotated   # <-- if Python < 3.9.0# Validators are type hints constrained by lambda functions.>>>ListOfStrings=Annotated[# <----- type hint matching non-empty list of strings...list[str],# <----------------- type hint matching possibly empty list of strings...Is[lambdalst:bool(lst)]# <-- lambda matching non-empty object...]# Annotate @beartype-decorated callables with validators.>>>@beartype...defquote_wiggum_safer(lines:ListOfStrings)->None:...print('“{}”\n\t— Police Chief Wiggum'.format("\n".join(lines)))# Call those callables with invalid parameters.>>>quote_wiggum_safer([])beartype.roar.BeartypeCallHintParamViolation: @beartypedquote_wiggum_safer() parameter lines=[] violates type hinttyping.Annotated[list[str], Is[lambda lst: bool(lst)]], as value []violates validator Is[lambda lst: bool(lst)].# ....................{ AT ANY TIME                     }....................# Type-check anything against any type hint – anywhere at anytime.>>>frombeartype.doorimport(...is_bearable,# <-------- like "isinstance(...)"...die_if_unbearable,# <-- like "assert isinstance(...)"...)>>>is_bearable(['The','goggles','do','nothing.'],list[str])True>>>die_if_unbearable([0xCAFEBEEF,0x8BADF00D],ListOfStrings)beartype.roar.BeartypeDoorHintViolation: Object [3405692655, 2343432205]violates type hint typing.Annotated[list[str], Is[lambda lst: bool(lst)]],as list index 0 item 3405692655 not instance of str.# ....................{ GO TO PLAID                     }....................# Type-check anything in around 1µs (one millionth of a second) – including# this list of one million 2-tuples of NumPy arrays.>>>frombeartype.doorimportis_bearable>>>fromnumpyimportarray,ndarray>>>data=[(array(i),array(i))foriinrange(1000000)]>>>%timeis_bearable(data,list[tuple[ndarray,ndarray]])CPU times: user 31 µs, sys: 2 µs, total: 33 µsWall time: 36.7 µsTrue# ....................{ MAKE US DO IT                   }....................# Don't know type hints? Do but wish you didn't? What if somebody else could# write your type hints for you? @beartype: it's somebody. Let BeartypeAI™# write your type hints for you. When you no longer care, call BeartypeAI™.>>>frombeartype.biteimportinfer_hint# <----- caring begins# What type hint describes the root state of a Pygments lexer, BeartypeAI™?>>>frompygments.lexersimportPythonLexer>>>infer_hint(PythonLexer().tokens["root"])list[tuple[str | pygments.token._TokenType[str], ...] |tuple[str | collections.abc.Callable[typing.Concatenate[object, object, ...], object], ...] |typing.Annotated[collections.abc.Collection[str],beartype.vale.IsInstance[pygments.lexer.include]]]  # <---- caring ends# ...all righty then. Guess I'll just take your word for that, BeartypeAI™.
```

Beartype brings[Rust](https://www.rust-lang.org)- and[C++](https://en.wikipedia.org/wiki/C%2B%2B)-inspired[zero-cost abstractions](https://boats.gitlab.io/blog/post/zero-cost-abstractions)into the lawless world of[dynamically-typed](https://en.wikipedia.org/wiki/Type_system)Python by[enforcing type safety at the granular level of functions and methods](eli5/#eli5-eli5)against[type hints standardized by the Python community](pep/#pep-pep)in\(O(1)\)[non-amortized worst-case time with negligible
constant factors](math/#math-time). If the prior sentence was unreadable jargon, see[our friendly and approachable FAQ for a human-readable synopsis](faq/#faq-faq).

Beartype is[portably implemented](https://github.com/beartype/beartype/tree/main/beartype)in[Python 3](https://www.python.org),[continuously stress-tested](https://github.com/beartype/beartype/actions?workflow=tests)via[GitHub
Actions](https://github.com/features/actions)**×**[tox](https://tox.readthedocs.io)**×**[pytest](https://docs.pytest.org)**×**[Codecov](https://about.codecov.io), and[permissively
distributed](https://github.com/beartype/beartype/blob/main/LICENSE)under the[MIT license](https://opensource.org/licenses/MIT). Beartype has*no*runtime dependencies,[only one test-time dependency](https://docs.pytest.org), and[only
one documentation-time dependency](https://www.sphinx-doc.org). Beartype supports[all actively
developed Python versions](https://devguide.python.org/versions/#versions),[all Python package managers](install/#install), and[multiple platform-specific package managers](install/#install).

Beartype[powers quality assurance across the Python ecosystem](https://github.com/beartype/beartype/network/dependents).

# The Typing Tree[¶](#the-typing-tree)

Welcome to the**Bearpedia**– your one-stop Encyclopedia Beartanica for all
things @beartype. It’s “[typing](https://docs.python.org/3/library/typing.html)or bust!” as you…

Bear with Us

- [Bearpedia](#)
- [Install](install/)
  - [Platform](install/#platform)
    - [macOS](install/#macos)
    - [Arch Linux](install/#arch-linux)
    - [Gentoo Linux](install/#gentoo-linux)
  1. [Badge](install/#badge)
1. [tl;dr](tldr/)
1. [ELI5](eli5/)
  - [Comparison](eli5/#comparison)
    - […versus Static Type-checkers](eli5/#versus-static-type-checkers)
    - […versus Runtime Type-checkers](eli5/#versus-runtime-type-checkers)
  1. [Quickstart](eli5/#quickstart)
    - [Standard Hints](eli5/#standard-hints)
      - [Toy Example](eli5/#toy-example)
      - [Industrial Example](eli5/#industrial-example)
  1. [Tutorial](eli5/#tutorial)
    - [Builtin Types](eli5/#builtin-types)
    - [Arbitrary Types](eli5/#arbitrary-types)
    - [Unions of Types](eli5/#unions-of-types)
    - [Optional Types](eli5/#optional-types)
  1. [Would You Like to Know More?](eli5/#would-you-like-to-know-more)
1. [API](api/)
  - [The Left-Paw Path](api/#the-left-paw-path)
1. [FAQ](faq/)
  - [What is beartype?](faq/#what-is-beartype)
  - [What is typeguard?](faq/#what-is-typeguard)
  - [When should I use beartype?](faq/#when-should-i-use-beartype)
  - [Does beartype do any bad stuff?](faq/#does-beartype-do-any-bad-stuff)
  - [Does beartype actually do anything?](faq/#does-beartype-actually-do-anything)
  - [How much does all this*really*cost?]()
  - [Beartype just does random stuff? Really?](faq/#beartype-just-does-random-stuff-really)
  - [What does “pure-Python” mean?](faq/#what-does-pure-python-mean)
  - [What does “near-real-time” even mean? Are you just making stuff up?](faq/#what-does-near-real-time-even-mean-are-you-just-making-stuff-up)
  - [What does “hybrid runtime-static” mean? Pretty sure you made that up, too.](faq/#what-does-hybrid-runtime-static-mean-pretty-sure-you-made-that-up-too)
  - [“Third-generation type-checker” doesn’t mean anything, does it?](faq/#third-generation-type-checker-doesn-t-mean-anything-does-it)
  - [How do I type-check…](faq/#how-do-i-type-check)
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
  1. [How do I *ONLY* type-check while running my test suite?](faq/#how-do-i-only-type-check-while-running-my-test-suite)
  1. [How do I *NOT* type-check something?](faq/#how-do-i-not-type-check-something)
  1. [Why is @leycec’s poorly insulated cottage in the Canadian wilderness so cold?](faq/#why-is-leycec-s-poorly-insulated-cottage-in-the-canadian-wilderness-so-cold)
1. [Features](pep/)
1. [Code](code/)
  - [Beartype Code Generation: It’s All for You](code/#beartype-code-generation-it-s-all-for-you)
    - [Identity Decoration](code/#identity-decoration)
    - [Unconditional Identity Decoration](code/#unconditional-identity-decoration)
    - [Shallow Identity Decoration](code/#shallow-identity-decoration)
    - [Deep Identity Decoration](code/#deep-identity-decoration)
    - [Constant Decoration](code/#constant-decoration)
      - [Constant Builtin Type Decoration](code/#constant-builtin-type-decoration)
      - [Constant Non-Builtin Type Decoration](code/#constant-non-builtin-type-decoration)
      - [Constant Shallow Sequence Decoration](code/#constant-shallow-sequence-decoration)
      - [Constant Deep Sequence Decoration](code/#constant-deep-sequence-decoration)
      - [Constant Nested Deep Sequence Decoration](code/#constant-nested-deep-sequence-decoration)
1. [Beartype Dev Handbook: It’s Handy](code/#beartype-dev-handbook-it-s-handy)
  - [Dev Workflow](code/#dev-workflow)
  - [Moar Depth](code/#moar-depth)
  - [Moar Compliance](code/#moar-compliance)
1. [Math](math/)
  - [Beartype Timings](math/#beartype-timings)
    - [Timings Overview](math/#timings-overview)
    - [Timings Lower Bound](math/#timings-lower-bound)
      - [Formulaic Formulas: They’re Back in Fashion](math/#formulaic-formulas-they-re-back-in-fashion)
      - [Function Call Overhead: The New Glass Ceiling](math/#function-call-overhead-the-new-glass-ceiling)
      - [Holy Balls of Flaming Dumpster Fires](math/#holy-balls-of-flaming-dumpster-fires)
      - [But, But… That’s Not Good Enough!](math/#but-but-that-s-not-good-enough)
  1. [Nobody Expects the Linearithmic Time](math/#nobody-expects-the-linearithmic-time)
1. [Moar](moar/)
  - [Runtime Type Checkers](moar/#runtime-type-checkers)
  - [Runtime Data Validators](moar/#runtime-data-validators)
  - [Static Type Checkers](moar/#static-type-checkers)
*Let’s type this.*

# See Also[¶](#see-also)

Beartype plugins adjacent to your interests include:

- 
[ipython-beartype](https://pypi.org/project/ipython-beartype), beartype’s official[IPython](https://ipython.org)plugin. Type-check:

  - 
Browser-based[Jupyter](https://jupyter.org),[Marimo](https://marimo.io), and[Google Colab](https://colab.research.google.com)notebook cells.

  - 
IDE-based[Zasper](https://zasper.io)notebook cells.

  - 
Terminal-based[IPython](https://ipython.org)REPLs.

1. 
[pytest-beartype](https://pypi.org/project/pytest-beartype), beartype’s official[pytest](https://docs.pytest.org)plugin. Type-check packages*only*at[pytest](https://docs.pytest.org)test-time. Fatally obsessed with speed? Fatally accepting of
critical failure? Can’t bear to type-check at runtime? When your team lacks
trust, your team chooses[pytest-beartype](https://pypi.org/project/pytest-beartype).

# License[¶](#license)

Beartype is[open-source software released](https://github.com/beartype/beartype/blob/main/LICENSE)under the[permissive MIT license](https://opensource.org/licenses/MIT).

# Security[¶](#security)

Beartype encourages security researchers, institutes, and concerned netizens to[responsibly disclose security vulnerabilities as GitHub-originated Security
Advisories](https://github.com/beartype/beartype/blob/main/.github/SECURITY.md)– published with full acknowledgement in the
public[GitHub Advisory Database](https://github.com/advisories).

# Funding[¶](#funding)

Beartype is financed as a[purely volunteer open-source project via GitHub
Sponsors](https://github.com/sponsors/leycec), to whom our burgeoning community is eternally
indebted. Without your generosity, runtime type-checking would be a shadow of
its current hulking bulk. We genuflect before your selfless charity, everyone!

Prior official funding sources (*yes, they once existed*) include:

1. 
A[Paul Allen Discovery Center award](https://www.alleninstitute.org/what-we-do/frontiers-group/news-press/press-resources/press-releases/paul-g-allen-frontiers-group-announces-allen-discovery-center-tufts-university)from the[Paul G. Allen Frontiers
Group](https://www.alleninstitute.org/what-we-do/frontiers-group)under the administrative purview of the[Paul Allen Discovery
Center](http://www.alleninstitute.org/what-we-do/frontiers-group/discovery-centers/allen-discovery-center-tufts-university)at[Tufts University](https://www.tufts.edu)over the period 2015—2018 preceding the
untimely death of[Microsoft co-founder Paul Allen](https://en.wikipedia.org/wiki/Paul_Allen), during
which beartype was maintained as the private`@type_check`decorator in the[Bioelectric Tissue Simulation Engine (BETSE)](https://github.com/betsee/betse).Phew!

# Contributors[¶](#contributors)

Beartype is the work product of volunteer enthusiasm, excess caffeine, and
sleepless Wednesday evenings. These brave GitHubbers hurtled[the pull request
(PR) gauntlet](https://github.com/beartype/beartype/pulls)so that you wouldn’t have to:

[](https://github.com/beartype/beartype/graphs/contributors)

It’s a heavy weight they bear. Applaud them as they buckle under the load!

# History[¶](#history)

Beartype’s histrionic past is checkered with drama, papered over in propaganda,
and chock full of the stuff of stars. Gaze upon their glistening visage as they
grow monotonically. But do the stars matter? Neither to mortal nor to bear. Yet,
by starlight, we all howl to commit by dawn.

[](https://github.com/beartype/beartype/stargazers)
[
next

Install
**]()
© Copyright 2014-2025 Beartype authors.

Created using[Sphinx](http://sphinx-doc.org/)5.3.0.
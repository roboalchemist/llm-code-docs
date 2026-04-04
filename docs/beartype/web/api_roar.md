# Source: https://beartype.readthedocs.io/en/latest/api_roar/

Tip

💗 **Upbear us** at [GitHub Sponsors](https://github.com/sponsors/leycec) and SonarQube Advanced Security
(Tidelift). **Follow us** [on Bluesky](https://leycec.bsky.social). **Friendzone us** [at Zulip](https://beartype.zulipchat.com).
Your generous support is our quality assurance. 💗

# Beartype Errors[¶](#beartype-errors)

...is that bear growling or is it just me?
 — common last words in rural Canada

Beartype only raises:

**Beartype-specific exceptions.** For your safety and ours, exceptions raised
beartype are easily distinguished from exceptions raised by everybody else.
*All* exceptions raised by beartype are instances of:

- Public types importable from the [`beartype.roar`](#module-beartype.roar) subpackage.

- The [`beartype.roar.BeartypeException`](#beartype.roar.BeartypeException) abstract base class (ABC).

**Disambiguous exceptions.** For your sanity and ours, *every* exception
raised by beartype means one thing and one thing only. Beartype *never* reuses
the same exception class to mean two different things – allowing you to
trivially catch and handle the exact exception you’re interested in.

Likewise, beartype only emits beartype-specific warnings and disambiguous
warnings. Beartype is fastidious to a fault. Error handling is no…
*exception*. punny *or* funny? you decide.

**Bear with Us**

- [Exception API](#exception-api)

[Warning API](#warning-api)

[PEP 585 Deprecations](#pep-585-deprecations)

- [What Does This Mean?](#what-does-this-mean)

- [Are We on the Worst Timeline?](#are-we-on-the-worst-timeline)

## [Exception API](#id6)[¶](#exception-api)

Beartype raises fatal exceptions whenever something explodes. Most are
self-explanatory – but some assume prior knowledge of arcane type-hinting
standards *or* require non-trivial resolutions warranting further discussion.
When that happens, don’t be the guy that ignores this chapter.

*exception *beartype.roar.BeartypeException[[source]](../_modules/beartype/roar/_roarexc/#BeartypeException)[¶](#beartype.roar.BeartypeException)

`Superclass(es):` [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

**Beartype exception root superclass.** *All* exceptions raised by beartype
are guaranteed to be instances of concrete subclasses of this abstract base
class (ABC) whose class names strictly match either:

`Beartype{subclass_name}Violation` for type-checking violations
(e.g., `BeartypeCallHintReturnViolation`).
`Beartype{subclass_name}Exception` for non-type-checking violations
(e.g., `BeartypeDecorHintPep3119Exception`).

*exception *beartype.roar.BeartypeDecorException[[source]](../_modules/beartype/roar/_roarexc/#BeartypeDecorException)[¶](#beartype.roar.BeartypeDecorException)

`Superclass(es):` [`BeartypeException`](#beartype.roar.BeartypeException)

**Beartype decorator exception superclass.** *All* exceptions raised by
the `&#64;beartype` decorator at decoration time (i.e., while dynamically
generating type-checking wrappers for decorated callables and classes) are
guaranteed to be instances of concrete subclasses of this abstract base
class (ABC). Since decoration-time exceptions are typically raised from
module scope early in the lifetime of a Python process, you are unlikely to
manually catch and handle decorator exceptions.
A detailed list of subclasses of this ABC is quite inconsequential. Very
well. [&#64;leycec](https://github.com/leycec) admits he was too tired to type it all out. [&#64;leycec](https://github.com/leycec) also
admits he played exploitative video games all night instead… *again*.
[&#64;leycec](https://github.com/leycec) is grateful nobody reads these API notes. checkmate,
readthedocs.

*exception *beartype.roar.BeartypeCallException[[source]](../_modules/beartype/roar/_roarexc/#BeartypeCallException)[¶](#beartype.roar.BeartypeCallException)

`Superclass(es):` [`BeartypeException`](#beartype.roar.BeartypeException)

**Beartype call-time exception superclass.** Beartype type-checkers
(including [`beartype.door.die_if_unbearable()`](../api_door/#beartype.door.die_if_unbearable) and
[`beartype.beartype()`](../api_decor/#beartype.beartype)-decorated callables) raise instances of concrete
subclasses of this abstract base class (ABC) at call-time – typically when
failing a type-check.
*All* exceptions raised by beartype type-checkers are guaranteed to be
instances of this ABC. Since type-checking exceptions are typically raised
from function and method scopes later in the lifetime of a Python process,
you are *much* more likely to manually catch and handle instances of this
exception type than other types of beartype exceptions. This includes the
pivotal [`BeartypeCallHintViolation`](#beartype.roar.BeartypeCallHintViolation) type, which subclasses this type.
In fact, you’re encouraged to do so. Repeat after Kermode Bear:

“Exceptions are fun, everybody.”

*Gotta catch ‘em all!*

*exception *beartype.roar.BeartypeCallHintException[[source]](../_modules/beartype/roar/_roarexc/#BeartypeCallHintException)[¶](#beartype.roar.BeartypeCallHintException)

`Superclass(es):` [`BeartypeCallException`](#beartype.roar.BeartypeCallException)

**Beartype type-checking exception superclass.** Beartype type-checkers
(including [`beartype.door.die_if_unbearable()`](../api_door/#beartype.door.die_if_unbearable) and
[`beartype.beartype()`](../api_decor/#beartype.beartype)-decorated callables) raise instances of concrete
subclasses of this abstract base class (ABC) when failing a type-check at
call time – typically due to you passing a parameter or returning a value
violating a type hint annotating that parameter or return.
For once, we’re not the ones to blame. The relief in our cubicle is palpable.

*exception *beartype.roar.BeartypeCallHintForwardRefException[[source]](../_modules/beartype/roar/_roarexc/#BeartypeCallHintForwardRefException)[¶](#beartype.roar.BeartypeCallHintForwardRefException)

`Superclass(es):` [`BeartypeCallHintException`](#beartype.roar.BeartypeCallHintException)

**Beartype type-checking forward reference exception.** Beartype
type-checkers raise instances of this exception type when a forward
reference type hint (i.e., string referring to a class that has yet to be
defined) erroneously references either:

- An attribute that does *not* exist.

- An attribute that exists but whose value is *not* actually a class.

As we gaze forward in time, so too do we glimpse ourselves – unshaven and
shabbily dressed – in the rear-view mirror.
&gt;&gt;&gt; from beartype import beartype
&gt;&gt;&gt; from beartype.roar import BeartypeCallHintForwardRefException
&gt;&gt;&gt; @beartype
... def i_am_spirit_bear(favourite_foodstuff: &#39;salmon.of.course&#39;) -&gt; None: pass
&gt;&gt;&gt; try:
... i_am_spirit_bear(&#39;Why do you eat all my salmon, Spirit Bear?&#39;)
... except BeartypeCallHintForwardRefException as exception:
... print(exception)
Forward reference &quot;salmon.of.course&quot; unimportable.

*exception *beartype.roar.BeartypeCallHintViolation[[source]](../_modules/beartype/roar/_roarexc/#BeartypeCallHintViolation)[¶](#beartype.roar.BeartypeCallHintViolation)

`Superclass(es):` [`BeartypeCallHintException`](#beartype.roar.BeartypeCallHintException)

**Beartype type-checking violation.** This is the most important beartype
exception you never hope to see – and thus the beartype exception you are
most likely to see. When your code explodes at midnight, instances of this
exception class were lighting the fuse behind your back.
Beartype type-checkers raise an instance of this exception class when an
object to be type-checked violates the type hint annotating that object.
Beartype type-checkers include:

- The [`beartype.door.die_if_unbearable()`](../api_door/#beartype.door.die_if_unbearable) function.

- The [`beartype.door.TypeHint.die_if_unbearable()`](../api_door/#beartype.door.TypeHint.die_if_unbearable) method.

User-defined functions and methods decorated by the
[`beartype.beartype()`](../api_decor/#beartype.beartype) decorator, which then themselves become beartype
type-checkers.

Because type-checking violations are why we are all here, instances of this
exception class offer additional read-only public properties to assist you
in debugging. Inspect these properties at runtime to resolve any lingering
doubts about which coworker(s) you intend to blame in your next twenty Git
commits:

culprits[¶](#beartype.roar.BeartypeCallHintViolation.culprits)

`Type:` [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[[`object`](https://docs.python.org/3/library/functions.html#object), …]

Tuple of one or more **culprits** (i.e., irresponsible objects that
violated the type hints annotating those objects during a recent
type-check).
Specifically, this property returns either:

If a standard slow Python container (e.g., [`dict`](https://docs.python.org/3/library/stdtypes.html#dict),
[`list`](https://docs.python.org/3/library/stdtypes.html#list), [`set`](https://docs.python.org/3/library/stdtypes.html#set), [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)) is responsible for this
violation, the 2-tuple `(root_culprit, leaf_culprit)` where:

`root_culprit` is the outermost such container. This is usually the
passed parameter or returned value indirectly violating this type
hint.
`leaf_culprit` is the innermost item nested in `root_culprit`
directly violating this type hint.

If a non-container (e.g., scalar, class instance) is responsible for
this violation, the 1-tuple `(culprit,)` where `culprit` is that
non-container.

Let us examine what the latter means for your plucky intern who will do
this after fetching more pumpkin spice lattes for The Team™ (currently
engrossed in a critical morale-building “Best of 260” Atari 2600 *Pong*
competition):
# Import the requisite machinery.
from beartype import beartype
from beartype.roar import BeartypeCallHintViolation

# Arbitrary user-defined classes.
class SpiritBearIGiveYouSalmonToGoAway(object): pass
class SpiritBearIGiftYouHoneyNotToStay(object): pass

# Arbitrary instance of one of these classes.
SPIRIT_BEAR_REFUSE_TO_GO_AWAY = SpiritBearIGiftYouHoneyNotToStay()

# Callable annotated to accept instances of the *OTHER* class.
@beartype
def when_spirit_bear_hibernates_in_your_bed(
 best_bear_den: SpiritBearIGiveYouSalmonToGoAway) -&gt; None: pass

# Call this callable with this invalid instance.
try:
 when_spirit_bear_hibernates_in_your_bed(
 SPIRIT_BEAR_REFUSE_TO_GO_AWAY)
# *MAGIC HAPPENS HERE*. Catch violations and inspect their &quot;culprits&quot;!
except BeartypeCallHintViolation as violation:
 # Assert that one culprit was responsible for this violation.
 assert len(violation.culprits) == 1

 # The one culprit: don&#39;t think we don&#39;t see you hiding there!
 culprit = violation.culprits[0]

 # Assert that this culprit is the same instance passed above.
 assert culprit is SPIRIT_BEAR_REFUSE_TO_GO_AWAY

**Caveats apply.** This property makes a good-faith effort to list the
most significant culprits responsible for this type-checking violation. In
two edge cases beyond our control, this property falls back to listing
truncated snapshots of the machine-readable representations of those
culprits (e.g., the first 10,000 characters or so of their [`repr()`](https://docs.python.org/3/library/functions.html#repr)
strings). This safe fallback is triggered for each culprit that:

Has **already been garbage-collected.** To avoid memory leaks, this
property only weakly (rather than strongly) refers to these culprits
and is thus best accessed only where these culprits are accessible.
Technically, this property is safely accessible from any context.
Practically, this property is most usefully accessed from the
`except ...:` block directly catching this violation. Since these
culprits may be garbage-collected at any time thereafter, this property
*cannot* be guaranteed to refer to these culprits outside that block.
If this property is accessed from any other context and one or more of
these culprits have sadly passed away, this property dynamically
reduces the corresponding items of this tuple to only the
machine-readable representations of those culprits. [[1]](#the-haunting)
Is a **builtin variable-sized C-based object** (e.g., [`dict`](https://docs.python.org/3/library/stdtypes.html#dict),
[`int`](https://docs.python.org/3/library/functions.html#int), [`list`](https://docs.python.org/3/library/stdtypes.html#list), [`str`](https://docs.python.org/3/library/stdtypes.html#str)). Long-standing limitations
within CPython itself prevent beartype from weakly referring to those
objects. Openly riot on the [CPython bug tracker](https://github.com/python/cpython/issues) if this displeases
you as much as it does us.

Let us examine what this means for your malding CTO:

# Import the requisite machinery.
from beartype import beartype
from beartype.roar import BeartypeCallHintViolation
from beartype.typing import List

# Callable annotated to accept a standard container.
@beartype
def we_are_all_spirit_bear(
 best_bear_dens: List[List[str]]) -&gt; None: pass

# Standard container deeply violating the above type hint.
SPIRIT_BEAR_DO_AS_HE_PLEASE = [
 [b&#39;Why do you sleep in my pinball room, Spirit Bear?&#39;]]

# Call this callable with this invalid container.
try:
 we_are_all_spirit_bear(SPIRIT_BEAR_DO_AS_HE_PLEASE)
# Shoddy magic happens here. Catch violations and try (but fail) to
# inspect the original culprits, because they were containers!
except BeartypeCallHintViolation as violation:
 # Assert that two culprits were responsible for this violation.
 assert len(violation.culprits) == 2

 # Root and leaf culprits. We just made these words up, people.
 root_culprit = violation.culprits[0]
 leaf_culprit = violation.culprits[1]

 # Assert that these culprits are, in fact, just repr() strings.
 assert root_culprit == repr(SPIRIT_BEAR_DO_AS_HE_PLEASE)
 assert leaf_culprit == repr(SPIRIT_BEAR_DO_AS_HE_PLEASE[0][0])

We see that beartype correctly identified the root culprit as the passed
list of lists of byte-strings (rather than strings) *and* the leaf
culprit as that byte-string. We also see that beartype only returned the
[`repr()`](https://docs.python.org/3/library/functions.html#repr) of both culprits rather than those culprits. Why? Because
CPython prohibits weak references to both lists *and* byte-strings.
This is why we facepalm ourselves in the morning. We did it this morning.
We’ll do it next morning, too. Until the [`weakref`](https://docs.python.org/3/library/weakref.html#module-weakref) module improves,
[&#64;leycec](https://github.com/leycec)’s forehead *will* be swollen with an angry mass of unsightly
red welts that are now festering unbeknownst to his wife.

New in version 0.12.0.

[[1](#id1)]
This exception stores the representations of these culprits inside
itself when first raised. Like a gruesome time capsule, they return to
haunt you.

## [Warning API](#id7)[¶](#warning-api)

Beartype emits non-fatal warnings whenever something looks it might explode in
your lap later… *but has yet to do so.* Since it is dangerous to go alone, let
beartype’s words of anxiety-provoking wisdom be your guide. The codebase you
save might be your own.

### [PEP 585 Deprecations](#id8)[¶](#pep-585-deprecations)

Beartype may occasionally emit non-fatal [**PEP 585**](https://peps.python.org/pep-0585/) deprecation warnings under
Python ≥ 3.9 resembling:
/home/kumamon/beartype/_util/hint/pep/utilpeptest.py:377:
BeartypeDecorHintPep585DeprecationWarning: PEP 484 type hint
typing.List[int] deprecated by PEP 585 scheduled for removal in the first
Python version released after October 5th, 2025. To resolve this, import
this hint from &quot;beartype.typing&quot; rather than &quot;typing&quot;. See this discussion
for further details and alternatives:
 https://github.com/beartype/beartype#pep-585-deprecations

This is that discussion topic. Let’s dissect this like a mantis shrimp
repeatedly punching out giant kraken.

#### [What Does This Mean?](#id9)[¶](#what-does-this-mean)

The [**PEP 585**](https://peps.python.org/pep-0585/) standard first introduced by Python 3.9.0 deprecated (obsoleted)
*most* of the [**PEP 484**](https://peps.python.org/pep-0484/) standard first introduced by Python 3.5.0 in the
official [`typing`](https://docs.python.org/3/library/typing.html#module-typing) module. All deprecated type hints are slated to “be
removed from the [`typing`](https://docs.python.org/3/library/typing.html#module-typing) module in the first Python version released 5
years after the release of Python 3.9.0.” Spoiler: Python 3.9.0 was released on
October 5th, 2020. Altogether, this means that:

Caution

**Most of the “typing” module will be removed in 2025 or 2026.**

If your codebase currently imports from the [`typing`](https://docs.python.org/3/library/typing.html#module-typing) module, *most* of
those imports will break under an upcoming Python release. This is what beartype
is shouting about. Bad changes are coming to dismantle your working code.

#### [Are We on the Worst Timeline?](#id10)[¶](#are-we-on-the-worst-timeline)

Season Eight of *Game of Thrones* previously answered this question, but let’s
try again. You have three options to avert the looming disaster that threatens
to destroy everything you hold dear (in ascending order of justice):

**Import from** `beartype.typing` **instead.** The easiest (and best)
solution is to globally replace all imports from the standard [`typing`](https://docs.python.org/3/library/typing.html#module-typing)
module with equivalent imports from our `beartype.typing` module. So:
# If you prefer attribute imports, just do this...
from beartype.typing import Dict, FrozenSet, List, Set, Tuple, Type

# ...instead of this.
#from typing import Dict, FrozenSet, List, Set, Tuple, Type

# Or if you prefer module imports, just do this...
from beartype import typing

# ...instead of this.
#import typing

The public `beartype.typing` API is a [mypy](http://mypy-lang.org)-compliant replacement for
the [`typing`](https://docs.python.org/3/library/typing.html#module-typing) API offering improved forward compatibility with future
Python releases. For example:

`beartype.typing.Set is set` under Python ≥ 3.9 for [**PEP 585**](https://peps.python.org/pep-0585/)
compliance.
`beartype.typing.Set is typing.Set` under Python &lt; 3.9 for [**PEP 484**](https://peps.python.org/pep-0484/)
compliance.

**Drop Python &lt; 3.9.** The next easiest (but worst) solution is to brutally
drop support for Python &lt; 3.9 by globally replacing all deprecated
[**PEP 484**](https://peps.python.org/pep-0484/)-compliant type hints with equivalent [**PEP 585**](https://peps.python.org/pep-0585/)-compliant type
hints (e.g., `typing.List[int]` with `list[int]`). This is really only
ideal for closed-source proprietary projects with a limited userbase. All
other projects should prefer saner solutions outlined below.
**Hide warnings.** The reprehensible (but understandable) middle-finger
way is to just squelch all deprecation warnings with an ignore warning
filter targeting the
`BeartypeDecorHintPep585DeprecationWarning` category. On the one
hand, this will still fail in 2025 or 2026 with fiery explosions and thus
only constitutes a temporary workaround at best. On the other hand, this has
the obvious advantage of preserving Python &lt; 3.9 support with minimal to no
refactoring costs. The two ways to do this have differing tradeoffs depending
on who you want to suffer most – your developers or your userbase:
# Do it globally for everyone, whether they want you to or not!
# This is the &quot;Make Users Suffer&quot; option.
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning
from warnings import filterwarnings
filterwarnings(&quot;ignore&quot;, category=BeartypeDecorHintPep585DeprecationWarning)
...

# Do it locally only for you! (Hope you like increasing your
# indentation level in every single codebase module.)
# This is the &quot;Make Yourself Suffer&quot; option.
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning
from warnings import catch_warnings, filterwarnings
with catch_warnings():
 filterwarnings(&quot;ignore&quot;, category=BeartypeDecorHintPep585DeprecationWarning)
 ...

**Type aliases.** The hardest (but best) solution is to use [type aliases](https://peps.python.org/pep-0484/#type-aliases)
to conditionally annotate callables with either [**PEP 484**](https://peps.python.org/pep-0484/) *or* [**PEP 585**](https://peps.python.org/pep-0585/)
type hints depending on the major version of the current Python interpreter.
Since this is life, the hard way is also the best way – but also hard. Unlike
the **drop Python &lt; 3.9** approach, this approach preserves backward
compatibility with Python &lt; 3.9. Unlike the **hide warnings** approach, this
approach also preserves forward compatibility with Python ≥ 3.14159265. Type
aliases means defining a new private `{your_package}._typing` submodule
resembling:
# In &quot;{your_package}._typing&quot;:
from sys import version_info

if version_info &gt;= (3, 9):
 List = list
 Tuple = tuple
 ...
else:
 from typing import List, Tuple, ...

Then globally refactor all deprecated [**PEP 484**](https://peps.python.org/pep-0484/) imports from [`typing`](https://docs.python.org/3/library/typing.html#module-typing)
to `{your_package}._typing` instead:
# Instead of this...
from typing import List, Tuple

# ...just do this.
from {your_package}._typing import List, Tuple

What could be simpler? …gagging noises faintly heard

 
 
 
 
 
 
 **
 
 previous

 Beartype DOOR

 
 
 
 
 next

 Ask a Bear Bro Anything (ABBA)

 
 **
# Source: https://beartype.readthedocs.io/en/latest/code/

Tip

💗 **Upbear us** at [GitHub Sponsors](https://github.com/sponsors/leycec) and SonarQube Advanced Security
(Tidelift). **Follow us** [on Bluesky](https://leycec.bsky.social). **Friendzone us** [at Zulip](https://beartype.zulipchat.com).
Your generous support is our quality assurance. 💗

# Code[¶](#code)

Let’s take a deep dive into the deep end of runtime type-checking – the beartype
way.

**Bear with Us**

[Beartype Code Generation: It’s All for You](#beartype-code-generation-it-s-all-for-you)

- [Identity Decoration](#identity-decoration)

- [Unconditional Identity Decoration](#unconditional-identity-decoration)

- [Shallow Identity Decoration](#shallow-identity-decoration)

- [Deep Identity Decoration](#deep-identity-decoration)

[Constant Decoration](#constant-decoration)

- [Constant Builtin Type Decoration](#constant-builtin-type-decoration)

- [Constant Non-Builtin Type Decoration](#constant-non-builtin-type-decoration)

- [Constant Shallow Sequence Decoration](#constant-shallow-sequence-decoration)

- [Constant Deep Sequence Decoration](#constant-deep-sequence-decoration)

- [Constant Nested Deep Sequence Decoration](#constant-nested-deep-sequence-decoration)

## [Beartype Code Generation: It’s All for You](#id6)[¶](#beartype-code-generation-it-s-all-for-you)

Beartype dynamically generates type-checking code unique to each class and
callable decorated by the [`beartype.beartype()`](../api_decor/#beartype.beartype) decorator. Let’s bearsplain
why the code [`beartype.beartype()`](../api_decor/#beartype.beartype) generates for real-world use cases is the
fastest possible code type-checking those cases.

### [Identity Decoration](#id7)[¶](#identity-decoration)

We begin by wading into the torpid waters of the many ways beartype avoids doing
any work whatsoever, because laziness is the virtue we live by. The reader may
recall that the fastest decorator at decoration- *and* call-time is the
**identity decorator** returning its decorated callable unmodified: e.g.,
from collections.abc import Callable

def identity_decorator(func: Callable): -&gt; Callable:
 return func

Beartype silently reduces to the identity decorator whenever it can, which is
surprisingly often. Our three weapons are laziness, surprise, ruthless
efficiency, and an almost fanatical devotion to constant-time type checking.

### [Unconditional Identity Decoration](#id8)[¶](#unconditional-identity-decoration)

Let’s define a trivial function annotated by *no* type hints:

def law_of_the_jungle(strike_first_and_then_give_tongue):
 return strike_first_and_then_give_tongue

Let’s decorate that function by [`beartype.beartype()`](../api_decor/#beartype.beartype) and verify that
[`beartype.beartype()`](../api_decor/#beartype.beartype) reduced to the identity decorator by returning that
function unmodified:
&gt;&gt;&gt; from beartype import beartype
&gt;&gt;&gt; beartype(law_of_the_jungle) is law_of_the_jungle
True

We’ve verified that [`beartype.beartype()`](../api_decor/#beartype.beartype) reduces to the identity decorator
when decorating unannotated callables. That’s but the tip of the efficiency
iceberg, though. [`beartype.beartype()`](../api_decor/#beartype.beartype) unconditionally reduces to a noop
when:

The decorated callable is itself decorated by the [**PEP 484**](https://peps.python.org/pep-0484/)-compliant
[`typing.no_type_check()`](https://docs.python.org/3/library/typing.html#typing.no_type_check) decorator.
The decorated callable has already been decorated by
[`beartype.beartype()`](../api_decor/#beartype.beartype).
Interpreter-wide optimization is enabled: e.g.,

- [CPython is invoked with the “-O” command-line option](https://docs.python.org/3/using/cmdline.html#cmdoption-o).

- [The “PYTHONOPTIMIZE” environment variable is set](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONOPTIMIZE).

### [Shallow Identity Decoration](#id9)[¶](#shallow-identity-decoration)

Let’s define a trivial function annotated by the [**PEP 484**](https://peps.python.org/pep-0484/)-compliant
[`typing.Any`](https://docs.python.org/3/library/typing.html#typing.Any) type hint:
from typing import Any

def law_of_the_jungle_2(never_order_anything_without_a_reason: Any) -&gt; Any:
 return never_order_anything_without_a_reason

Again, let’s decorate that function by [`beartype.beartype()`](../api_decor/#beartype.beartype) and verify that
[`beartype.beartype()`](../api_decor/#beartype.beartype) reduced to the identity decorator by returning that
function unmodified:
&gt;&gt;&gt; from beartype import beartype
&gt;&gt;&gt; beartype(law_of_the_jungle_2) is law_of_the_jungle_2
True

We’ve verified that [`beartype.beartype()`](../api_decor/#beartype.beartype) reduces to the identity decorator
when decorating callables annotated by [`typing.Any`](https://docs.python.org/3/library/typing.html#typing.Any) – a novel category of
type hint we refer to as **shallowly ignorable type hints** (known to be
ignorable by constant-time lookup in a predefined frozen set). That’s but the
snout of the crocodile, though. [`beartype.beartype()`](../api_decor/#beartype.beartype) conditionally reduces
to a noop when *all* type hints annotating the decorated callable are shallowly
ignorable. These include:

[`object`](https://docs.python.org/3/library/functions.html#object), the root superclass of Python’s class hierarchy. Since all
objects are instances of [`object`](https://docs.python.org/3/library/functions.html#object), [`object`](https://docs.python.org/3/library/functions.html#object) conveys no
meaningful constraints as a type hint and is thus shallowly ignorable.
- [`typing.Any`](https://docs.python.org/3/library/typing.html#typing.Any), equivalent to [`object`](https://docs.python.org/3/library/functions.html#object).

[`typing.Generic`](https://docs.python.org/3/library/typing.html#typing.Generic), equivalent to `typing.Generic[typing.Any]`, which
conveys no meaningful constraints as a type hint and is thus shallowly
ignorable.
[`typing.Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol), equivalent to `typing.Protocol[typing.Any]` and
shallowly ignorable for similar reasons.
[`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union), equivalent to `typing.Union[typing.Any]`, equivalent to
[`typing.Any`](https://docs.python.org/3/library/typing.html#typing.Any).
[`typing.Optional`](https://docs.python.org/3/library/typing.html#typing.Optional), equivalent to `typing.Optional[typing.Any]`,
equivalent to `Union[Any, type(None)]`. Since any union subscripted by
ignorable type hints is itself ignorable, [[1]](#union-ignorable) [typing.Optional](https://docs.python.org/3/library/typing.html#typing.Optional)
is shallowly ignorable as well.

[[1](#id1)]
Unions are only as narrow as their widest subscripted argument. However,
ignorable type hints are ignorable *because* they are maximally wide.
Unions subscripted by ignorable arguments are thus the widest possible
unions, conveying no meaningful constraints and thus themselves ignorable.

### [Deep Identity Decoration](#id10)[¶](#deep-identity-decoration)

Let’s define a trivial function annotated by a non-trivial [**PEP 484**](https://peps.python.org/pep-0484/)-,
[**PEP 585**](https://peps.python.org/pep-0585/)- and [**PEP 593**](https://peps.python.org/pep-0593/)-compliant type hint that superficially *appears*
to convey meaningful constraints:
from typing import Annotated, NewType, Union

hint = Union[str, list[int], NewType(&#39;MetaType&#39;, Annotated[object, 53])]
def law_of_the_jungle_3(bring_them_to_the_pack_council: hint) -&gt; hint:
 return bring_them_to_the_pack_council

Despite appearances, it can be shown by exhaustive (and frankly exhausting)
reduction that that hint is actually ignorable. Let’s decorate that function by
[`beartype.beartype()`](../api_decor/#beartype.beartype) and verify that [`beartype.beartype()`](../api_decor/#beartype.beartype) reduced to
the identity decorator by returning that function unmodified:
&gt;&gt;&gt; from beartype import beartype
&gt;&gt;&gt; beartype(law_of_the_jungle_3) is law_of_the_jungle_3
True

We’ve verified that [`beartype.beartype()`](../api_decor/#beartype.beartype) reduces to the identity decorator
when decorating callables annotated by the above object – a novel category of
type hint we refer to as **deeply ignorable type hints** (known to be ignorable
only by recursive linear-time inspection of subscripted arguments). That’s but
the trunk of the elephant, though. [`beartype.beartype()`](../api_decor/#beartype.beartype) conditionally
reduces to a noop when *all* type hints annotating the decorated callable are
deeply ignorable. These include:

Parametrizations of [`typing.Generic`](https://docs.python.org/3/library/typing.html#typing.Generic) and [`typing.Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol) by
type variables. Since [`typing.Generic`](https://docs.python.org/3/library/typing.html#typing.Generic), [`typing.Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol), *and*
type variables all fail to convey any meaningful constraints in and of
themselves, these parametrizations are safely ignorable in all contexts.
- Calls to [`typing.NewType`](https://docs.python.org/3/library/typing.html#typing.NewType) passed an ignorable type hint.

- Subscriptions of [`typing.Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) whose first argument is ignorable.

Subscriptions of [`typing.Optional`](https://docs.python.org/3/library/typing.html#typing.Optional) and [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union) by at least
one ignorable argument.

### [Constant Decoration](#id11)[¶](#constant-decoration)

We continue by trundling into the turbid waters out at sea, where beartype
reluctantly performs its minimal amount of work with a heavy sigh.

#### [Constant Builtin Type Decoration](#id12)[¶](#constant-builtin-type-decoration)

Let’s define a trivial function annotated by type hints that are builtin types:

from beartype import beartype

@beartype
def law_of_the_jungle_4(he_must_be_spoken_for_by_at_least_two: int):
 return he_must_be_spoken_for_by_at_least_two

Let’s see the wrapper function [`beartype.beartype()`](../api_decor/#beartype.beartype) dynamically generated
from that:
def law_of_the_jungle_4(
 *args,
 __beartype_func=__beartype_func,
 __beartypistry=__beartypistry,
 **kwargs
):
 # Localize the number of passed positional arguments for efficiency.
 __beartype_args_len = len(args)
 # Localize this positional or keyword parameter if passed *OR* to the
 # sentinel value &quot;__beartypistry&quot; guaranteed to never be passed otherwise.
 __beartype_pith_0 = (
 args[0] if __beartype_args_len &gt; 0 else
 kwargs.get(&#39;he_must_be_spoken_for_by_at_least_two&#39;, __beartypistry)
 )

 # If this parameter was passed...
 if __beartype_pith_0 is not __beartypistry:
 # Type-check this passed parameter or return value against this
 # PEP-compliant type hint.
 if not isinstance(__beartype_pith_0, int):
 __beartype_get_beartype_violation(
 func=__beartype_func,
 pith_name=&#39;he_must_be_spoken_for_by_at_least_two&#39;,
 pith_value=__beartype_pith_0,
 )

 # Call this function with all passed parameters and return the value
 # returned from this call.
 return __beartype_func(*args, **kwargs)

Let’s dismantle this bit by bit:

- The code comments above are verbatim as they appear in the generated code.

`law_of_the_jungle_4()` is the ad-hoc function name
[`beartype.beartype()`](../api_decor/#beartype.beartype) assigned this wrapper function.
- `__beartype_func` is the original `law_of_the_jungle_4()` function.

`__beartypistry` is a thread-safe global registry of all types, tuples of
types, and forward references to currently undeclared types visitable from
type hints annotating callables decorated by [`beartype.beartype()`](../api_decor/#beartype.beartype). We’ll
see more about the `__beartypistry` in a moment. For know, just know that
`__beartypistry` is a private singleton of the beartype package. This object
is frequently accessed and thus localized to the body of this wrapper rather
than accessed as a global variable, which would be mildly slower.
`__beartype_pith_0` is the value of the first passed parameter, regardless
of whether that parameter is passed as a positional or keyword argument. If
unpassed, the value defaults to the `__beartypistry`. Since *no* caller
should access (let alone pass) that object, that object serves as an efficient
sentinel value enabling us to discern passed from unpassed parameters.
Beartype internally favours the term “pith” (which we absolutely just made up)
to transparently refer to the arbitrary object currently being type-checked
against its associated type hint.
`isinstance(__beartype_pith_0, int)` tests whether the value passed for this
parameter satisfies the type hint annotating this parameter.
`__beartype_get_beartype_violation()` raises a human-readable exception if
this value fails this type-check.

So good so far. But that’s easy. Let’s delve deeper.

#### [Constant Non-Builtin Type Decoration](#id13)[¶](#constant-non-builtin-type-decoration)

Let’s define a trivial function annotated by type hints that are pure-Python
classes rather than builtin types:
from argparse import ArgumentParser
from beartype import beartype

@beartype
def law_of_the_jungle_5(a_cub_may_be_bought_at_a_price: ArgumentParser):
 return a_cub_may_be_bought_at_a_price

Let’s see the wrapper function [`beartype.beartype()`](../api_decor/#beartype.beartype) dynamically generated
from that:
def law_of_the_jungle_5(
 *args,
 __beartype_func=__beartype_func,
 __beartypistry=__beartypistry,
 **kwargs
):
 # Localize the number of passed positional arguments for efficiency.
 __beartype_args_len = len(args)
 # Localize this positional or keyword parameter if passed *OR* to the
 # sentinel value &quot;__beartypistry&quot; guaranteed to never be passed otherwise.
 __beartype_pith_0 = (
 args[0] if __beartype_args_len &gt; 0 else
 kwargs.get(&#39;a_cub_may_be_bought_at_a_price&#39;, __beartypistry)
 )

 # If this parameter was passed...
 if __beartype_pith_0 is not __beartypistry:
 # Type-check this passed parameter or return value against this
 # PEP-compliant type hint.
 if not isinstance(__beartype_pith_0, __beartypistry[&#39;argparse.ArgumentParser&#39;]):
 __beartype_get_beartype_violation(
 func=__beartype_func,
 pith_name=&#39;a_cub_may_be_bought_at_a_price&#39;,
 pith_value=__beartype_pith_0,
 )

 # Call this function with all passed parameters and return the value
 # returned from this call.
 return __beartype_func(*args, **kwargs)

The result is largely the same. The only meaningful difference is the type-check
on line 20:
if not isinstance(__beartype_pith_0, __beartypistry[&#39;argparse.ArgumentParser&#39;]):

Since we annotated that function with a pure-Python class rather than builtin
type, [`beartype.beartype()`](../api_decor/#beartype.beartype) registered that class with the
`__beartypistry` at decoration time and then subsequently looked that class up
with its fully-qualified classname at call time to perform this type-check.
So good so far… so what! Let’s spelunk harder.

#### [Constant Shallow Sequence Decoration](#id14)[¶](#constant-shallow-sequence-decoration)

Let’s define a trivial function annotated by type hints that are [**PEP 585**](https://peps.python.org/pep-0585/)-compliant builtin types subscripted by ignorable arguments:

from beartype import beartype

@beartype
def law_of_the_jungle_6(all_the_jungle_is_thine: list[object]):
 return all_the_jungle_is_thine

Let’s see the wrapper function [`beartype.beartype()`](../api_decor/#beartype.beartype) dynamically generated
from that:
def law_of_the_jungle_6(
 *args,
 __beartype_func=__beartype_func,
 __beartypistry=__beartypistry,
 **kwargs
):
 # Localize the number of passed positional arguments for efficiency.
 __beartype_args_len = len(args)
 # Localize this positional or keyword parameter if passed *OR* to the
 # sentinel value &quot;__beartypistry&quot; guaranteed to never be passed otherwise.
 __beartype_pith_0 = (
 args[0] if __beartype_args_len &gt; 0 else
 kwargs.get(&#39;all_the_jungle_is_thine&#39;, __beartypistry)
 )

 # If this parameter was passed...
 if __beartype_pith_0 is not __beartypistry:
 # Type-check this passed parameter or return value against this
 # PEP-compliant type hint.
 if not isinstance(__beartype_pith_0, list):
 __beartype_get_beartype_violation(
 func=__beartype_func,
 pith_name=&#39;all_the_jungle_is_thine&#39;,
 pith_value=__beartype_pith_0,
 )

 # Call this function with all passed parameters and return the value
 # returned from this call.
 return __beartype_func(*args, **kwargs)

We are still within the realm of normalcy. Correctly detecting this type hint
to be subscripted by an ignorable argument, [`beartype.beartype()`](../api_decor/#beartype.beartype) only
bothered type-checking this parameter to be an instance of this builtin type:
if not isinstance(__beartype_pith_0, list):

It’s time to iteratively up the ante.

#### [Constant Deep Sequence Decoration](#id15)[¶](#constant-deep-sequence-decoration)

Let’s define a trivial function annotated by type hints that are [**PEP 585**](https://peps.python.org/pep-0585/)-compliant builtin types subscripted by builtin types:

from beartype import beartype

@beartype
def law_of_the_jungle_7(kill_everything_that_thou_canst: list[str]):
 return kill_everything_that_thou_canst

Let’s see the wrapper function [`beartype.beartype()`](../api_decor/#beartype.beartype) dynamically generated
from that:
def law_of_the_jungle_7(
 *args,
 __beartype_func=__beartype_func,
 __beartypistry=__beartypistry,
 **kwargs
):
 # Generate and localize a sufficiently large pseudo-random integer for
 # subsequent indexation in type-checking randomly selected container items.
 __beartype_random_int = __beartype_getrandbits(64)
 # Localize the number of passed positional arguments for efficiency.
 __beartype_args_len = len(args)
 # Localize this positional or keyword parameter if passed *OR* to the
 # sentinel value &quot;__beartypistry&quot; guaranteed to never be passed otherwise.
 __beartype_pith_0 = (
 args[0] if __beartype_args_len &gt; 0 else
 kwargs.get(&#39;kill_everything_that_thou_canst&#39;, __beartypistry)
 )

 # If this parameter was passed...
 if __beartype_pith_0 is not __beartypistry:
 # Type-check this passed parameter or return value against this
 # PEP-compliant type hint.
 if not (
 # True only if this pith shallowly satisfies this hint.
 isinstance(__beartype_pith_0, list) and
 # True only if either this pith is empty *OR* this pith is
 # both non-empty and deeply satisfies this hint.
 (not __beartype_pith_0 or isinstance(__beartype_pith_0[__beartype_random_int % len(__beartype_pith_0)], str))
 ):
 __beartype_get_beartype_violation(
 func=__beartype_func,
 pith_name=&#39;kill_everything_that_thou_canst&#39;,
 pith_value=__beartype_pith_0,
 )

 # Call this function with all passed parameters and return the value
 # returned from this call.
 return __beartype_func(*args, **kwargs)

We have now diverged from normalcy. Let’s dismantle this iota by iota:

`__beartype_random_int` is a pseudo-random unsigned 32-bit integer whose
bit length intentionally corresponds to the number of bits generated by each
call to Python’s C-based Mersenne Twister internally
performed by the [`random.getrandbits()`](https://docs.python.org/3/library/random.html#random.getrandbits) function generating this integer.
Exceeding this length would cause that function to internally perform that
call multiple times for no gain. Since the cost of generating integers to
this length is the same as generating integers of smaller lengths, this
length is preferred. Since most sequences are likely to contain fewer items
than this integer, pseudo-random sequence items are indexable by taking the
modulo of this integer with the sizes of those sequences. For big sequences
containing more than this number of items, beartype deeply type-checks
leading items with indices in this range while ignoring trailing items. Given
the practical infeasibility of storing big sequences in memory, this seems an
acceptable real-world tradeoff. Suck it, big sequences!
As before, [`beartype.beartype()`](../api_decor/#beartype.beartype) first type-checks this parameter to be a
list.
[`beartype.beartype()`](../api_decor/#beartype.beartype) then type-checks this parameter to either be:

- `not __beartype_pith_0`, an empty list.

isinstance(__beartype_pith_0[__beartype_random_int %
len(__beartype_pith_0)], str), a non-empty list whose pseudo-randomly
indexed list item satisfies this nested builtin type.

Well, that escalated quickly.

#### [Constant Nested Deep Sequence Decoration](#id16)[¶](#constant-nested-deep-sequence-decoration)

Let’s define a trivial function annotated by type hints that are [**PEP 585**](https://peps.python.org/pep-0585/)-compliant builtin types recursively subscripted by instances of themselves,
because *we are typing masochists*:
from beartype import beartype

@beartype
def law_of_the_jungle_8(pull_thorns_from_all_wolves_paws: (
 list[list[list[str]]])):
 return pull_thorns_from_all_wolves_paws

Let’s see the wrapper function [`beartype.beartype()`](../api_decor/#beartype.beartype) dynamically generated
from that:
def law_of_the_jungle_8(
 *args,
 __beartype_func=__beartype_func,
 __beartypistry=__beartypistry,
 **kwargs
):
 # Generate and localize a sufficiently large pseudo-random integer for
 # subsequent indexation in type-checking randomly selected container items.
 __beartype_random_int = __beartype_getrandbits(32)
 # Localize the number of passed positional arguments for efficiency.
 __beartype_args_len = len(args)
 # Localize this positional or keyword parameter if passed *OR* to the
 # sentinel value &quot;__beartypistry&quot; guaranteed to never be passed otherwise.
 __beartype_pith_0 = (
 args[0] if __beartype_args_len &gt; 0 else
 kwargs.get(&#39;pull_thorns_from_all_wolves_paws&#39;, __beartypistry)
 )

 # If this parameter was passed...
 if __beartype_pith_0 is not __beartypistry:
 # Type-check this passed parameter or return value against this
 # PEP-compliant type hint.
 if not (
 # True only if this pith shallowly satisfies this hint.
 isinstance(__beartype_pith_0, list) and
 # True only if either this pith is empty *OR* this pith is
 # both non-empty and deeply satisfies this hint.
 (not __beartype_pith_0 or (
 # True only if this pith shallowly satisfies this hint.
 isinstance(__beartype_pith_1 := __beartype_pith_0[__beartype_random_int % len(__beartype_pith_0)], list) and
 # True only if either this pith is empty *OR* this pith is
 # both non-empty and deeply satisfies this hint.
 (not __beartype_pith_1 or (
 # True only if this pith shallowly satisfies this hint.
 isinstance(__beartype_pith_2 := __beartype_pith_1[__beartype_random_int % len(__beartype_pith_1)], list) and
 # True only if either this pith is empty *OR* this pith is
 # both non-empty and deeply satisfies this hint.
 (not __beartype_pith_2 or isinstance(__beartype_pith_2[__beartype_random_int % len(__beartype_pith_2)], str))
 ))
 ))
 ):
 __beartype_get_beartype_violation(
 func=__beartype_func,
 pith_name=&#39;pull_thorns_from_all_wolves_paws&#39;,
 pith_value=__beartype_pith_0,
 )

 # Call this function with all passed parameters and return the value
 # returned from this call.
 return __beartype_func(*args, **kwargs)

We are now well beyond the deep end, where the benthic zone and the cruel
denizens of the fathomless void begins. Let’s dismantle this pascal by pascal:

__beartype_pith_1 := __beartype_pith_0[__beartype_random_int %
len(__beartype_pith_0)], a [**PEP 572**](https://peps.python.org/pep-0572/)-style assignment expression
localizing repeatedly accessed random items of the first nested list for
efficiency.
__beartype_pith_2 := __beartype_pith_1[__beartype_random_int %
len(__beartype_pith_1)], a similar expression localizing repeatedly
accessed random items of the second nested list.
- The same `__beartype_random_int` pseudo-randomly indexes all three lists.

Under older Python interpreters lacking [**PEP 572**](https://peps.python.org/pep-0572/) support,
[`beartype.beartype()`](../api_decor/#beartype.beartype) generates equally valid (albeit less efficient) code
repeating each nested list item access.

In the kingdom of the linear-time runtime type checkers, the constant-time
runtime type checker really stands out like a sore giant squid, doesn’t it?
See the next section for further commentary on runtime optimization from the
higher-level perspective of architecture and internal API design. Surely, it is
fun.

# Beartype Dev Handbook: It’s Handy[¶](#beartype-dev-handbook-it-s-handy)

Let’s contribute [pull requests](https://github.com/beartype/beartype/pulls) to beartype for the good of
[typing](https://docs.python.org/3/library/typing.html). The primary maintainer of this repository is a friendly, bald, and
bearded Canadian guy who guarantees that he will *always* be nice
and congenial and promptly merge *most* requests that pass continuous
integration (CI) tests.
And thanks for merely reading this! Like all open-source software, beartype
thrives on community contributions, activity, and interest. This means you,
stalwart Python hero.
Beartype has two problem spots (listed below in order of decreasing importance
and increasing complexity) that could *always* benefit from a
volunteer army of good GitHub Samaritans.

## Dev Workflow[¶](#dev-workflow)

Let’s take this from the top.

- Create a [GitHub user account](https://github.com/join).

- Login to [GitHub with that account](https://github.com/login).

**Click the “Fork” button** in the upper right-hand corner of the
“beartype/beartype” repository page.
**Click the “Code” button** in the upper right-hand corner of your fork page
that appears.
- **Copy the URL** that appears.

- **Open a terminal.**

- **Change to the desired parent directory** of your local fork.

**Clone your fork,** replacing `{URL}` with the previously copied URL.

git clone {URL}

**Add a new remote** referring to this upstream repository.

git remote add upstream https://github.com/beartype/beartype.git

**Uninstall all previously installed versions** of beartype. For
example, if you previously installed beartype with `pip`, manually
uninstall beartype with `pip`.
pip uninstall beartype

Install beartype with `pip` in **editable mode.** This synchronizes changes
made to your fork against the beartype package imported in Python. Note the
`[dev]` extra installs developer-specific mandatory dependencies required
at test or documentation time.
pip3 install -e .[dev]

**Create a new branch** to isolate changes to, replacing `{branch_name}`
with the desired name.
git checkout -b {branch_name}

**Make changes to this branch** in your favourite Integrated Development
Environment (IDE). Of course, this means [Vim](https://www.vim.org).
**Test these changes.** Note this command assumes you have installed *all*
major versions of both CPython and PyPy supported by the next stable
release of beartype you are hacking on. If this is *not* the case,
install these versions with [pyenv](https://operatingops.org/2020/10/24/tox-testing-multiple-python-versions-with-pyenv). This is vital, as type hinting support
varies significantly between major versions of different Python interpreters.
./tox

The resulting output should ideally be suffixed by a synopsis resembling:

________________________________ summary _______________________________
py36: commands succeeded
py37: commands succeeded
py38: commands succeeded
py39: commands succeeded
pypy36: commands succeeded
pypy37: commands succeeded
congratulations :)

**Stage these changes.**

git add -a

**Commit these changes.**

git commit

**Push these changes** to your remote fork.

git push

**Click the “Create pull request” button** in the upper right-hand corner of
your fork page.
Afterward, **routinely pull upstream changes** to avoid desynchronization
with [the “beartype/beartype” repository](https://github.com/beartype/beartype).
git checkout main &amp;&amp; git pull upstream main

## Moar Depth[¶](#moar-depth)

Caution

**This section is badly outdated.** It’s bad. *Real* bad. If you’d like us to
revise this to actually reflect reality, just drop us a line at our issue
tracker. [&#64;leycec](https://github.com/leycec) promises satisfaction.

So, you want to help beartype deeply type-check even *more* type hints than she
already does? Let us help you help us, because you are awesome.
First, an egregious lore dump. It’s commonly assumed that beartype only
internally implements a single type-checker. After all, every *other* static and
runtime type-checker only internally implements a single type-checker. Why would
a type-checker internally implement several divergent overlapping type-checkers
and… what would that even mean? Who would be so vile, cruel, and sadistic as
to do something like that?
*We would.* Beartype often violates assumptions. This is no exception.
Externally, of course, beartype presents itself as a single type-checker.
Internally, beartype is implemented as a two-phase series of orthogonal
type-checkers. Why? Because efficiency, which is the reason we are all here.
These type-checkers are (in the order that callables decorated by beartype
perform them at runtime):

**Testing phase.** In this fast first pass, each callable decorated by
[`beartype.beartype()`](../api_decor/#beartype.beartype) only *tests* whether all parameters passed to and
values returned from the current call to that callable satisfy all type hints
annotating that callable. This phase does *not* raise human-readable
exceptions (in the event that one or more parameters or return values fails
to satisfy these hints). [`beartype.beartype()`](../api_decor/#beartype.beartype) highly optimizes this
phase by dynamically generating one wrapper function wrapping each decorated
callable with unique pure-Python performing these tests in O(1)
constant-time. This phase is *always* unconditionally performed by code
dynamically generated and returned by:

The fast-as-lightning `pep_code_check_hint()` function declared in the
[“beartype._decor._code._pep._pephint” submodule](https://github.com/beartype/beartype/blob/main/beartype/_decor/_code/_pep/_pephint.py),
which generates memoized O(1) code type-checking an arbitrary object
against an arbitrary PEP-compliant type hint by iterating over all child
hints nested in that hint with a highly optimized breadth-first search
(BFS) leveraging extreme caching, fragile cleverness, and other salacious
micro-optimizations.

**Error phase.** In this slow second pass, each call to a callable decorated
by [`beartype.beartype()`](../api_decor/#beartype.beartype) that fails the fast first pass (due to one or
more parameters or return values failing to satisfy these hints) recursively
discovers the exact underlying cause of that failure and raises a
human-readable exception precisely detailing that cause.
[`beartype.beartype()`](../api_decor/#beartype.beartype) does *not* optimize this phase whatsoever. Whereas
the implementation of the first phase is uniquely specific to each decorated
callable and constrained to O(1) constant-time non-recursive operation, the
implementation of the second phase is generically shared between all
decorated callables and generalized to O(n) linear-time recursive operation.
Efficiency no longer matters when you’re raising exceptions. Exception
handling is slow in any language and doubly slow in [dynamically-typed](https://en.wikipedia.org/wiki/Type_system) (and
mostly interpreted) languages like Python, which means that performance is
mostly a non-concern in “cold” code paths guaranteed to raise exceptions.
This phase is only *conditionally* performed when the first phase fails by:

The slow-as-molasses `get_beartype_violation()` function declared in the
[“beartype._decor._error.errormain” submodule](https://github.com/beartype/beartype/blob/main/beartype/_decor/_code/_pep/_error/errormain.py),
which generates human-readable exceptions after performing unmemoized O(n)
type-checking of an arbitrary object against a PEP-compliant type hint by
recursing over all child hints nested in that hint with an unoptimized
recursive algorithm prioritizing debuggability, readability, and
maintainability.

This separation of concerns between performant \(O(1)\) *testing* on the one
hand and perfect \(O(n)\) *error handling* on the other preserves both
runtime performance and readable errors at a cost of developer pain. This is
good! …what?
Secondly, the same separation of concerns also complicates the development of
[`beartype.beartype()`](../api_decor/#beartype.beartype). This is bad. Since [`beartype.beartype()`](../api_decor/#beartype.beartype)
internally implements two divergent type-checkers, deeply type-checking a new
category of type hint requires adding that support to (wait for it) two
divergent type-checkers – which, being fundamentally distinct codebases sharing
little code in common, requires violating the Don’t Repeat Yourself (DRY)
principle by reinventing the wheel in the second type-checker. Such is
the high price of high-octane performance. You probably thought this would be
easier and funner. So did we.
Thirdly, this needs to be tested. After surmounting the above roadblocks by
deeply type-checking that new category of type hint in *both* type-checkers,
you’ll now add one or more unit tests exhaustively exercising that checking.
Thankfully, we already did all of the swole lifting for you. All *you* need to
do is add at least one PEP-compliant type hint, one object satisfying that hint,
and one object *not* satisfying that hint to:

A new `PepHintMetadata` object in the existing tuple passed to the
`data_module.HINTS_PEP_META.extend(...)` call in the existing test data
submodule for this PEP residing under the
[“beartype_test.unit.data.hint.pep.proposal” subpackage](https://github.com/beartype/beartype/blob/main/beartype_test/unit/data/hint/pep/proposal/). For example, if this is a [**PEP 484**](https://peps.python.org/pep-0484/)-compliant type hint, add that
hint and associated metadata to the
[“beartype_test.unit.data.hint.pep.proposal.data_hintpep484” submodule](https://github.com/beartype/beartype/blob/main/beartype_test/unit/data/hint/pep/proposal/data_hintpep484.py).

You’re done! *Praise Guido.*

## Moar Compliance[¶](#moar-compliance)

So, you want to help beartype comply with even *more* Python Enhancement
Proposals (PEPs) than she already complies with? Let us help you help us,
because you are young and idealistic and you mean well.
You will need a spare life to squander. A clone would be most handy. In short,
you will want to at least:

Define a new utility submodule for this PEP residing under the
[“beartype._util.hint.pep.proposal” subpackage](https://github.com/beartype/beartype/blob/main/beartype/_util/hint/pep/proposal)
implementing general-purpose validators, testers, getters, and other
ancillary utility functions required to detect and handle *all* type hints
compliant with this PEP. For efficiency, utility functions performing
iteration or other expensive operations should be memoized via our internal
[&#64;callable_cached](https://github.com/beartype/beartype/blob/main/beartype/_util/cache/utilcachecall.py) decorator.
Define a new data utility submodule for this PEP residing under the
[“beartype._util.data.hint.pep.proposal” subpackage](https://github.com/beartype/beartype/blob/main/beartype/_util/hint/data/pep/proposal/) adding various signs (i.e., arbitrary objects uniquely identifying
type hints compliant with this PEP) to various global variables defined by the
parent [“beartype._util.data.hint.pep.utilhintdatapep” submodule](_beartypeutildatapepparent).
Define a new test data submodule for this PEP residing under the
[“beartype_test.unit.data.hint.pep.proposal” subpackage](https://github.com/beartype/beartype/blob/main/beartype_test/unit/data/hint/pep/proposal/).

You’re probably not done by a long shot! But the above should at least get you
fitfully started, though long will you curse our names. *Praise Cleese.*

 
 
 
 
 
 
 **
 
 previous

 Features

 
 
 
 
 next

 Maths: It’s Plural, Apparently

 
 **
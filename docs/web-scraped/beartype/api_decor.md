# Source: https://beartype.readthedocs.io/en/latest/api_decor/

Tip

💗 **Upbear us** at [GitHub Sponsors](https://github.com/sponsors/leycec) and SonarQube Advanced Security
(Tidelift). **Follow us** [on Bluesky](https://leycec.bsky.social). **Friendzone us** [at Zulip](https://beartype.zulipchat.com).
Your generous support is our quality assurance. 💗

# Beartype Decoration[¶](#beartype-decoration)

wrap anything with runtime type-checking
 ...except that, of course.
 — Thus Spake Bearathustra, Book I

The beating heart of beartype is the eponymous [`beartype()`](#beartype.beartype) decorator. This
is its story.

**Bear with Us**

[Beartype Decorator API](#beartype-decorator-api)

[Callable Mode](#callable-mode)

- […as Decorator](#as-decorator)

- […as Function](#as-function)

- […as Noop](#as-noop)

[Class Mode](#class-mode)

- […versus Callable Mode](#versus-callable-mode)

[Configuration Mode](#configuration-mode)

- [Beartype Configuration API](#beartype-configuration-api)

- [Beartype Strategy API](#beartype-strategy-api)

[Beartype Environment Variables](#beartype-environment-variables)

- [${BEARTYPE_IS_COLOR}](#beartype-is-color)

## [Beartype Decorator API](#id8)[¶](#beartype-decorator-api)

&#64;beartype.beartype(*cls: [type](https://docs.python.org/3/library/functions.html#type) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *func: [collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *conf: [BeartypeConf](#beartype.BeartypeConf) = BeartypeConf()*) &#x2192; [object](https://docs.python.org/3/library/functions.html#object)[[source]](../_modules/beartype/_decor/decorcache/#beartype)[¶](#beartype.beartype)

Parameters:

- **cls** ([*type*](https://docs.python.org/3/library/functions.html#type)* | **None*) – Pure-Python class to be decorated.

- **func** ([*collections.abc.Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)* | **None*) – Pure-Python function or method to be decorated.

**conf** ([*beartype.BeartypeConf*](#beartype.BeartypeConf)) – Beartype configuration. Defaults to the default configuration
performing \(O(1)\) type-checking.

Returns:
Passed class or callable wrapped with runtime type-checking.

Augment the passed object with performant runtime type-checking. Unlike most
decorators, `&#64;beartype` has three orthogonal modes of operation:

[Class mode](#class-mode) – in which you decorate a class
with `&#64;beartype`, which then iteratively decorates all methods declared
by that class with `&#64;beartype`. This is the recommended mode for
**object-oriented logic.**
[Callable mode](#callable-mode) – in which you decorate a
function or method with `&#64;beartype`, which then dynamically generates a
new function or method wrapping the original function or method with
performant runtime type-checking. This is the recommended mode for
**procedural logic.**
[Configuration mode](#configuration-mode) – in which you create your
own app-specific `&#64;beartype` decorator **configured** for your exact use
case.

When chaining multiple decorators, order of decoration is significant but
conditionally depends on the mode of operation. Specifically, in:

[Class mode](#class-mode), `&#64;beartype` should usually be listed
*first*.
[Callable mode](#callable-mode), `&#64;beartype` should usually be listed
*last*.

It’s not our fault. Surely documentation would never decieve you.

### [Callable Mode](#id9)[¶](#callable-mode)

*def* beartype.**beartype**(func: [collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)) -&gt;
[collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)
In callable mode, [`beartype()`](#beartype.beartype) dynamically generates a new **callable**
(i.e., pure-Python function or method) runtime type-checking the passed
callable.

#### […as Decorator](#id10)[¶](#as-decorator)

Because laziness prevails, [`beartype()`](#beartype.beartype) is *usually* invoked as a
decorator. Simply prefix the callable to be runtime type-checked with the line
`&#64;beartype`. In this standard use pattern, [`beartype()`](#beartype.beartype) silently:

Replaces the decorated callable with a new callable of the same name and
signature.
Preserves the original callable as the `__wrapped__` instance variable of
that new callable.

An example explicates a thousand words.

# Import the requisite machinery.
&gt;&gt;&gt; from beartype import beartype

# Decorate a function with @beartype.
&gt;&gt;&gt; @beartype
... def bother_free_is_no_bother_to_me(bothersome_string: str) -&gt; str:
... return f&#39;Oh, bother. {bothersome_string}&#39;

# Call that function with runtime type-checking enabled.
&gt;&gt;&gt; bother_free_is_no_bother_to_me(b&#39;Could you spare a small smackerel?&#39;)
BeartypeCallHintParamViolation: @beartyped bother_free_is_no_bother_to_me()
parameter bothersome_string=b&#39;Could you spare a small smackerel?&#39; violates
type hint &lt;class &#39;str&#39;&gt;, as bytes b&#39;Could you spare a small smackerel?&#39; not
instance of str.

# Call that function with runtime type-checking disabled. WHY YOU DO THIS!?
&gt;&gt;&gt; bother_free_is_no_bother_to_me.__wrapped__(
... b&#39;Could you spare a small smackerel?&#39;)
&quot;Oh, bother. b&#39;Could you spare a small smackerel?&#39;&quot;

Because [`beartype()`](#beartype.beartype) preserves the original callable as `__wrapped__`,
[`beartype()`](#beartype.beartype) seamlessly integrates with other well-behaved decorators that
respect that same pseudo-standard. This means that [`beartype()`](#beartype.beartype) can
*usually* be listed in any arbitrary order when chained (i.e., combined) with
other decorators.
Because this is the NP-hard timeline, however, assumptions are risky. If you
doubt anything, the safest approach is just to list `&#64;beartype` as the
**last** (i.e., bottommost) decorator. This:

Ensures that [`beartype()`](#beartype.beartype) is called first on the decorated callable
*before* other decorators have a chance to really muck things up. Other
decorators: *always the source of all your problems.*
Improves both space and time efficiency. Unwrapping `__wrapped__` callables
added by prior decorators is an \(O(k)\) operation for \(k\) the
number of previously run decorators. Moreover, builtin decorators like
`classmethod`, [`property`](https://docs.python.org/3/library/functions.html#property), and `staticmethod` create
method descriptors; when run *after* a builtin decorator, [`beartype()`](#beartype.beartype)
has no recourse but to:

- Destroy the original method descriptor created by that builtin decorator.

- Create a new method type-checking the original method.

Create a new method descriptor wrapping that method by calling the same
builtin decorator.

An example is brighter than a thousand Suns! astronomers throwing
chalk here
# Import the requisite machinery.
&gt;&gt;&gt; from beartype import beartype

# Decorate class methods with @beartype in either order.
&gt;&gt;&gt; class BlastItAll(object):
... @classmethod
... @beartype # &lt;-- GOOD. this is the best of all possible worlds.
... def good_idea(cls, we_will_dynamite: str) -&gt; str:
... return we_will_dynamite
...
... @beartype # &lt;-- BAD. technically, fine. pragmatically, slower.
... @classmethod
... def save_time(cls, whats_the_charge: str) -&gt; str:
... return whats_the_charge

#### […as Function](#id11)[¶](#as-function)

Because Python means not caring what anyone else thinks, [`beartype()`](#beartype.beartype) can
also be called as a function. This is useful in unthinkable edge cases like
monkey-patching *other* people’s code with runtime type-checking. You usually
shouldn’t do this, but you usually shouldn’t do a lot of things that you do when
you’re the sort of Pythonista that reads tortuous documentation like this.
# Import the requisite machinery.
&gt;&gt;&gt; from beartype import beartype

# A function somebody else defined. Note the bad lack of @beartype.
&gt;&gt;&gt; def oh_bother_free_where_art_thou(botherfull_string: str) -&gt; str:
... return f&#39;Oh, oh! Help and bother! {botherfull_string}&#39;

# Monkey-patch that function with runtime type-checking. *MUHAHAHA.*
&gt;&gt;&gt; oh_bother_free_where_art_thou = beartype(oh_bother_free_where_art_thou)

# Call that function with runtime type-checking enabled.
&gt;&gt;&gt; oh_bother_free_where_art_thou(b&quot;I&#39;m stuck!&quot;)
BeartypeCallHintParamViolation: @beartyped oh_bother_free_where_art_thou()
parameter botherfull_string=b&quot;I&#39;m stuck!&quot; violates type hint &lt;class &#39;str&#39;&gt;,
as bytes b&quot;I&#39;m stuck!&quot; not instance of str.

One `beartype()` to monkey-patch them all and in the darkness type-check them.

#### […as Noop](#id12)[¶](#as-noop)

[`beartype()`](#beartype.beartype) silently reduces to a **noop** (i.e., scoops organic honey out
of a jar with its fat paws rather than doing something useful with its life)
under common edge cases. When *any* of the following apply, [`beartype()`](#beartype.beartype)
preserves the decorated callable or class as is by just returning that callable
or class unmodified (rather than augmenting that callable or class with unwanted
runtime type-checking):

Beartype has been configured with the **no-time strategy**
[`BeartypeStrategy.O0`](#beartype.BeartypeStrategy.O0): e.g.,
# Import the requisite machinery.
from beartype import beartype, BeartypeConf, BeartypeStrategy

# Avoid type-checking *ANY* methods or attributes of this class.
@beartype(conf=BeartypeConf(strategy=BeartypeStrategy.O0))
class UncheckedDangerClassIsDangerous(object):
 # This method raises *NO* type-checking violation despite returning a
 # non-&quot;None&quot; value.
 def unchecked_danger_method_is_dangerous(self) -&gt; None:
 return &#39;This string is not &quot;None&quot;. Sadly, nobody cares anymore.&#39;

That callable or class has already been decorated by:

- The [`beartype()`](#beartype.beartype) decorator itself.

The [**PEP 484**](https://peps.python.org/pep-0484/)-compliant [`typing.no_type_check()`](https://docs.python.org/3/library/typing.html#typing.no_type_check) decorator: e.g.,

# Import more requisite machinery. It is requisite.
from beartype import beartype
from typing import no_type_check

# Avoid type-checking *ANY* methods or attributes of this class.
@no_type_check
class UncheckedRiskyClassRisksOurEntireHistoricalTimeline(object):
 # This method raises *NO* type-checking violation despite returning a
 # non-&quot;None&quot; value.
 def unchecked_risky_method_which_i_am_squinting_at(self) -&gt; None:
 return &#39;This string is not &quot;None&quot;. Why does nobody care? Why?&#39;

That callable is **unannotated** (i.e., *no* parameters or return values in
the signature of that callable are annotated by type hints).
[Sphinx](https://www.sphinx-doc.org) is currently autogenerating documentation (i.e., Sphinx’s
[“autodoc” extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) is currently running).

Laziness **+** efficiency **==** [`beartype()`](#beartype.beartype).

### [Class Mode](#id13)[¶](#class-mode)

*def* beartype.**beartype**(cls: type) -&gt; type

In class mode, [`beartype()`](#beartype.beartype) dynamically replaces *each* method of the
passed pure-Python class with a new method runtime type-checking the original
method.
As with [callable mode](#callable-mode), simply prefix the class to be
runtime type-checked with the line `&#64;beartype`. In this standard use pattern,
[`beartype()`](#beartype.beartype) silently iterates over all instance, class, and static methods
declared by the decorated class and, for each such method:

- Replaces that method with a new method of the same name and signature.

Preserves the original method as the `__wrapped__` instance variable of
that new method.

#### […versus Callable Mode](#id14)[¶](#versus-callable-mode)

Superficially, this is just syntactic sugar – but sometimes you gotta dip your
paws into the honey pot.
# Import the requisite machinery.
from beartype import beartype

# Decorate a class with @beartype.
@beartype
class IAmABearOfNoBrainAtAll(object):
 def i_have_been_foolish(self) -&gt; str:
 return &#39;A fly can&#39;t bird, but a bird can fly.&#39;

 def and_deluded(self) -&gt; str:
 return &#39;Ask me a riddle and I reply.&#39;

# ...or just decorate class methods directly with @beartype.
# The class above is *EXACTLY* equivalent to the class below.
class IAmABearOfNoBrainAtAll(object):
 @beartype
 def i_have_been_foolish(self) -&gt; str:
 return &#39;A fly can&#39;t bird, but a bird can fly.&#39;

 @beartype
 def and_deluded(self) -&gt; str:
 return &#39;Ask me a riddle and I reply.&#39;

Pragmatically, this is *not* just syntactic sugar. You *must* decorate classes
(rather than merely methods) with [`beartype()`](#beartype.beartype) to type-check the following:

**Class-centric type hints** (i.e., type hints like the [**PEP 673**](https://peps.python.org/pep-0673/)-compliant
[typing.Self](https://docs.python.org/3/library/typing.html#typing.Self) attribute that describe the decorated class itself). To
type-check these kinds of type hints, [`beartype()`](#beartype.beartype) needs access to the
class. [`beartype()`](#beartype.beartype) lacks access to the class when decorating methods
directly. Instead, you *must* decorate classes by [`beartype()`](#beartype.beartype) for
classes declaring one or more methods annotated by one or more class-centric
type hints.
**Dataclasses.** The standard [`dataclasses.dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass) decorator
dynamically generates and adds new dunder methods (e.g., `__init__()`,
`__eq__()`, `__hash__()`) to the decorated class. These methods do *not*
physically exist and thus *cannot* be decorated directly with
[`beartype()`](#beartype.beartype). Instead, you *must* decorate dataclasses first by
`&#64;beartype` and then by `&#64;dataclasses.dataclass`. Order is significant, of
course. `&lt;/sigh&gt;`

When decorating classes, `&#64;beartype` should *usually* be listed as the
**first** (i.e., topmost) decorator. This ensures that [`beartype()`](#beartype.beartype) is
called last on the decorated class *after* other decorators have a chance to
dynamically monkey-patch that class (e.g., by adding new methods to that class).
[`beartype()`](#beartype.beartype) will then type-check the monkey-patched functionality as well.
Come for the working examples. Stay for the wild hand-waving.

# Import the requisite machinery.
from beartype import beartype
from dataclasses import dataclass

# Decorate a dataclass first with @beartype and then with @dataclass. If you
# accidentally reverse this order of decoration, methods added by @dataclass
# like __init__() will *NOT* be type-checked by @beartype. (Blame Guido.)
@beartype
@dataclass
class SoTheyWentOffTogether(object):
 a_little_boy_and_his_bear: str | bytes
 will_always_be_playing: str | None = None

### [Configuration Mode](#id15)[¶](#configuration-mode)

*def* beartype.**beartype**(*, conf: beartype.BeartypeConf) -&gt;
collections.abc.Callable[[T], T]
In configuration mode, [`beartype()`](#beartype.beartype) dynamically generates a new
[`beartype()`](#beartype.beartype) decorator – configured uniquely for your exact use case. You
too may cackle villainously as you feel the unbridled power of your keyboard.
# Import the requisite machinery.
from beartype import beartype, BeartypeConf, BeartypeStrategy

# Dynamically create a new @monotowertype decorator configured to:
# * Avoid outputting colors in type-checking violations.
# * Enable support for the implicit numeric tower standardized by PEP 484.
monotowertype = beartype(conf=BeartypeConf(
 is_color=False, is_pep484_tower=True))

# Decorate with this decorator rather than @beartype everywhere.
@monotowertype
def muh_colorless_permissive_func(int_or_float: float) -&gt; float:
 return int_or_float ** int_or_float ^ round(int_or_float)

Configuration: *because you know best*.

#### [Beartype Configuration API](#id16)[¶](#beartype-configuration-api)

*class *beartype.BeartypeConf(***, *is_color: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *is_debug: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *is_pep484_tower: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *strategy: [BeartypeStrategy](#beartype.BeartypeStrategy) = BeartypeStrategy.O1*)[[source]](../_modules/beartype/_conf/confmain/#BeartypeConf)[¶](#beartype.BeartypeConf)
**Beartype configuration** (i.e., self-caching dataclass instance
encapsulating all flags, options, settings, and other metadata configuring
each type-checking operation performed by beartype – including each
decoration of a callable or class by the [`beartype()`](#beartype.beartype) decorator).
The default configuration `BeartypeConf()` configures beartype to:

Perform \(O(1)\) constant-time type-checking for safety, scalability,
and efficiency.
- Disable support for [PEP 484’s implicit numeric tower](https://peps.python.org/pep-0484/#the-numeric-tower).

- Disable developer-specific debugging logic.

- Conditionally output color when standard output is attached to a terminal.

Beartype configurations may be passed as the optional keyword-only `conf`
parameter accepted by *most* high-level runtime type-checking functions
exported by [`beartype`](#module-beartype) – including:

- The [`beartype.beartype()`](#beartype.beartype) decorator.

- The [`beartype.claw.beartype_all()`](../api_claw/#beartype.claw.beartype_all) import hook.

- The [`beartype.claw.beartype_package()`](../api_claw/#beartype.claw.beartype_package) import hook.

- The [`beartype.claw.beartype_packages()`](../api_claw/#beartype.claw.beartype_packages) import hook.

- The [`beartype.claw.beartype_this_package()`](../api_claw/#beartype.claw.beartype_this_package) import hook.

- The `beartype.claw.beartyping()` import hook.

- The [`beartype.door.die_if_unbearable()`](../api_door/#beartype.door.die_if_unbearable) type-checker.

- The [`beartype.door.is_bearable()`](../api_door/#beartype.door.is_bearable) type-checker.

- The [`beartype.door.TypeHint.die_if_unbearable()`](../api_door/#beartype.door.TypeHint.die_if_unbearable) type-checker.

- The [`beartype.door.TypeHint.is_bearable()`](../api_door/#beartype.door.TypeHint.is_bearable) type-checker.

Beartype configurations are immutable objects memoized (i.e., cached) on the
unordered set of all passed parameters:
&gt;&gt;&gt; from beartype import BeartypeConf
&gt;&gt;&gt; BeartypeConf() is BeartypeConf()
True
&gt;&gt;&gt; BeartypeConf(is_color=False) is BeartypeConf(is_color=False)
True

Beartype configurations are comparable under equality:

&gt;&gt;&gt; BeartypeConf(is_color=False) == BeartypeConf(is_color=True)
False

Beartype configurations are hashable and thus suitable for use as dictionary
keys and set members:
&gt;&gt;&gt; BeartypeConf(is_color=False) == BeartypeConf(is_color=True)
False
&gt;&gt;&gt; confs = {BeartypeConf(), BeartypeConf(is_color=False)}
&gt;&gt;&gt; BeartypeConf() in confs
True

Beartype configurations support meaningful [`repr()`](https://docs.python.org/3/library/functions.html#repr) output:

&gt;&gt;&gt; repr(BeartypeConf())
&#39;BeartypeConf(is_color=None, is_debug=False, is_pep484_tower=False, strategy=&lt;BeartypeStrategy.O1: 2&gt;)&#39;

Beartype configurations expose read-only public properties of the same names
as the above parameters:
&gt;&gt;&gt; BeartypeConf().is_color
None
&gt;&gt;&gt; BeartypeConf().strategy
&lt;BeartypeStrategy.O1: 2&gt;

##### Keyword Parameters[¶](#keyword-parameters)

Beartype configurations support **optional read-only keyword-only**
parameters at instantiation time. Most parameters are suitable for passing by
*all* beartype users in *all* possible use cases. Some are only intended to
be passed by *some* beartype users in *some* isolated use cases.
This is their story.

###### General Keyword Parameters[¶](#general-keyword-parameters)

General-purpose configuration parameters are *always* safely passable:

is_debug[¶](#beartype.BeartypeConf.is_debug)

`Type:` [`bool`](https://docs.python.org/3/library/functions.html#bool) = [`False`](https://docs.python.org/3/library/constants.html#False)

[`True`](https://docs.python.org/3/library/constants.html#True) only if debugging the [`beartype()`](#beartype.beartype) decorator. If you’re
curious as to what exactly (if anything) [`beartype()`](#beartype.beartype) is doing on
your behalf, temporarily enable this boolean. Specifically, enabling this
boolean (*in no particular order*):

Caches the body of each type-checking wrapper function dynamically
generated by [`beartype()`](#beartype.beartype) with the standard [`linecache`](https://docs.python.org/3/library/linecache.html#module-linecache)
module, enabling these function bodies to be introspected at runtime
*and* improving the readability of tracebacks whose call stacks contain
one or more calls to these [`beartype()`](#beartype.beartype)-decorated functions.
Prints the definition (including both the signature and body) of each
type-checking wrapper function dynamically generated by :func:.beartype`
to standard output.
Appends to the declaration of each **hidden parameter** (i.e., whose
name is prefixed by `&quot;__beartype_&quot;` and whose value is that of an
external attribute internally referenced in the body of that function)
a comment providing the machine-readable representation of the initial
value of that parameter, stripped of newlines and truncated to a
hopefully sensible length. Since the low-level string munger called to
do so is shockingly slow, these comments are conditionally embedded in
type-checking wrapper functions *only* when this boolean is enabled.

Defaults to [`False`](https://docs.python.org/3/library/constants.html#False). Eye-gouging sample output or it didn’t happen,
so:
# Import the requisite machinery.
&gt;&gt;&gt; from beartype import beartype, BeartypeConf

# Dynamically create a new @bugbeartype decorator enabling debugging.
# Insider D&amp;D jokes in my @beartype? You&#39;d better believe. It&#39;s happening.
&gt;&gt;&gt; bugbeartype = beartype(conf=BeartypeConf(is_debug=True))

# Decorate with this decorator rather than @beartype everywhere.
&gt;&gt;&gt; @bugbeartype
... def muh_bugged_func() -&gt; str:
... return b&#39;Consistency is the bugbear that frightens little minds.&#39;
(line 0001) def muh_bugged_func(
(line 0002) *args,
(line 0003) __beartype_func=__beartype_func, # is &lt;function muh_bugged_func at 0x7f52733bad40&gt;
(line 0004) __beartype_conf=__beartype_conf, # is &quot;BeartypeConf(is_color=None, is_debug=True, is_pep484_tower=False, strategy=&lt;BeartypeStrategy...
(line 0005) __beartype_get_violation=__beartype_get_violation, # is &lt;function get_beartype_violation at 0x7f5273081d80&gt;
(line 0006) **kwargs
(line 0007) ):
(line 0008) # Call this function with all passed parameters and localize the value
(line 0009) # returned from this call.
(line 0010) __beartype_pith_0 = __beartype_func(*args, **kwargs)
(line 0011)
(line 0012) # Noop required to artificially increase indentation level. Note that
(line 0013) # CPython implicitly optimizes this conditional away. Isn&#39;t that nice?
(line 0014) if True:
(line 0015) # Type-check this passed parameter or return value against this
(line 0016) # PEP-compliant type hint.
(line 0017) if not isinstance(__beartype_pith_0, str):
(line 0018) raise __beartype_get_violation(
(line 0019) func=__beartype_func,
(line 0020) conf=__beartype_conf,
(line 0021) pith_name=&#39;return&#39;,
(line 0022) pith_value=__beartype_pith_0,
(line 0023) )
(line 0024)
(line 0025) return __beartype_pith_0

is_pep484_tower[¶](#beartype.BeartypeConf.is_pep484_tower)

`Type:` [`bool`](https://docs.python.org/3/library/functions.html#bool) = [`False`](https://docs.python.org/3/library/constants.html#False)

[`True`](https://docs.python.org/3/library/constants.html#True) only if enabling support for PEP 484’s implicit numeric
tower (i.e., lossy conversion of integers to
floating-point numbers as well as both integers and floating-point numbers
to complex numbers). Specifically, enabling this instructs beartype to
automatically expand:

All [`float`](https://docs.python.org/3/library/functions.html#float) type hints to [`float`](https://docs.python.org/3/library/functions.html#float) `|` [`int`](https://docs.python.org/3/library/functions.html#int), thus
implicitly accepting both integers and floating-point numbers for
objects annotated as only accepting floating-point numbers.
All [`complex`](https://docs.python.org/3/library/functions.html#complex) type hints to [`complex`](https://docs.python.org/3/library/functions.html#complex) `|` [`float`](https://docs.python.org/3/library/functions.html#float)
`|` [`int`](https://docs.python.org/3/library/functions.html#int), thus implicitly accepting integers, floating-point,
and complex numbers for objects annotated as only accepting complex
numbers.

Defaults to [`False`](https://docs.python.org/3/library/constants.html#False) to minimize precision error introduced by lossy
conversions from integers to floating-point numbers to complex numbers.
Since most integers do *not* have exact representations as floating-point
numbers, each conversion of an integer into a floating-point number
typically introduces a small precision error that accumulates over
multiple conversions and operations into a larger precision error.
Enabling this improves the usability of public APIs at a cost of
introducing precision errors.
The standard use case is to dynamically define your own app-specific
[`beartype()`](#beartype.beartype) decorator unconditionally enabling support for the
implicit numeric tower, usually as a convenience to your userbase who do
*not* particularly care about the above precision concerns. Behold the
permissive powers of… `&#64;beartowertype`!
# Import the requisite machinery.
from beartype import beartype, BeartypeConf

# Dynamically create a new @beartowertype decorator enabling the tower.
beartowertype = beartype(conf=BeartypeConf(is_pep484_tower=True))

# Decorate with this decorator rather than @beartype everywhere.
@beartowertype
def crunch_numbers(numbers: list[float]) -&gt; float:
 return sum(numbers)

# This is now fine.
crunch_numbers([3, 1, 4, 1, 5, 9])

# This is still fine, too.
crunch_numbers([3.1, 4.1, 5.9])

New in version 0.12.0.

strategy[¶](#beartype.BeartypeConf.strategy)

`Type:` [`BeartypeStrategy`](#beartype.BeartypeStrategy) = [`BeartypeStrategy.O1`](#beartype.BeartypeStrategy.O1)

**Type-checking strategy** (i.e., [`BeartypeStrategy`](#beartype.BeartypeStrategy) enumeration
member dictating how many items are type-checked at each nesting level of
each container and thus how responsively beartype type-checks containers).
This setting governs the core tradeoff in runtime type-checking between:

- **Overhead** in the amount of time that beartype spends type-checking.

- **Completeness** in the number of objects that beartype type-checks.

As beartype gracefully scales up to check larger and larger containers,
so beartype simultaneously scales down to check fewer and fewer items of
those containers. This scalability preserves performance regardless of
container size while increasing the likelihood of false negatives (i.e.,
failures to catch invalid items in large containers) as container size
increases. You can either type-check a small number of objects nearly
instantaneously *or* you can type-check a large number of objects slowly.
Pick one.
Defaults to [`BeartypeStrategy.O1`](#beartype.BeartypeStrategy.O1), the constant-time \(O(1)\)
strategy – maximizing scalability at a cost of also maximizing false
positives.

###### App-only Keyword Parameters[¶](#app-only-keyword-parameters)

**App-only configuration parameters** are passed *only* by first-party
packages executed as apps, binaries, scripts, servers, or other executable
processes (rather than imported as libraries, frameworks, or other importable
APIs into the current process):

is_color[¶](#beartype.BeartypeConf.is_color)

`Type:` [`bool`](https://docs.python.org/3/library/functions.html#bool) | [`None`](https://docs.python.org/3/library/constants.html#None) = [`None`](https://docs.python.org/3/library/constants.html#None)

Tri-state boolean governing how and whether beartype colours
**type-checking violations** (i.e., human-readable
[`beartype.roar.BeartypeCallHintViolation`](../api_roar/#beartype.roar.BeartypeCallHintViolation) exceptions) with
POSIX-compliant ANSI escape sequences for readability. Specifically, if
this boolean is:

[`False`](https://docs.python.org/3/library/constants.html#False), beartype *never* colours type-checking violations raised
by callables configured with this configuration.
[`True`](https://docs.python.org/3/library/constants.html#True), beartype *always* colours type-checking violations raised
by callables configured with this configuration.
[`None`](https://docs.python.org/3/library/constants.html#None), beartype conditionally colours type-checking violations
raised by callables configured with this configuration only when
standard output is attached to an interactive terminal.

The [${BEARTYPE_IS_COLOR} environment variable](#api-decor-beartype-is-color) globally overrides this parameter, enabling
end users to enforce a global colour policy across their full app stack.
When both that variable *and* this parameter are set to differing (and
thus conflicting) values, the [`BeartypeConf`](#beartype.BeartypeConf) class:

- Ignores this parameter in favour of that variable.

Emits a `beartype.roar.BeartypeConfShellVarWarning` warning
notifying callers of this conflict.

To avoid this conflict, only downstream executables should pass this
parameter; intermediary libraries should *never* pass this parameter.
Non-violent communication begins with you.
Effectively defaults to [`None`](https://docs.python.org/3/library/constants.html#None). Technically, this parameter defaults
to a private magic constant *not* intended to be passed by callers,
enabling [`beartype`](#module-beartype) to reliably detect whether the caller has
explicitly passed this parameter or not.
The standard use case is to dynamically define your own app-specific
[`beartype()`](#beartype.beartype) decorator unconditionally disabling colours in
type-checking violations, usually due to one or more frameworks in your
app stack failing to support ANSI escape sequences. Please file issues
with those frameworks requesting ANSI support. In the meanwhile, behold
the monochromatic powers of… `&#64;monobeartype`!
# Import the requisite machinery.
from beartype import beartype, BeartypeConf

# Dynamically create a new @monobeartype decorator disabling colour.
monobeartype = beartype(conf=BeartypeConf(is_color=False))

# Decorate with this decorator rather than @beartype everywhere.
@monobeartype
def muh_colorless_func() -&gt; str:
 return b&#39;In the kingdom of the blind, you are now king.&#39;

New in version 0.12.0.

#### [Beartype Strategy API](#id17)[¶](#beartype-strategy-api)

*class *beartype.BeartypeStrategy[[source]](../_modules/beartype/_conf/confenum/#BeartypeStrategy)[¶](#beartype.BeartypeStrategy)

`Superclass(es):` [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Enumeration of all kinds of **type-checking strategies** (i.e., competing
procedures for type-checking objects passed to or returned from
[`beartype()`](#beartype.beartype)-decorated callables, each with concomitant tradeoffs with
respect to runtime complexity and quality assurance).
Strategies are intentionally named according to [conventional Big O notation](https://en.wikipedia.org/wiki/Big_O_notation) (e.g., [`BeartypeStrategy.On`](#beartype.BeartypeStrategy.On) enables the \(O(n)\)
strategy). Strategies are established per-decoration at the fine-grained
level of callables decorated by the [`beartype()`](#beartype.beartype) decorator. Simply set
the [`BeartypeConf.strategy`](#beartype.BeartypeConf.strategy) parameter of the [`BeartypeConf`](#beartype.BeartypeConf)
object passed as the optional `conf` parameter to the [`beartype()`](#beartype.beartype)
decorator.
# Import the requisite machinery.
from beartype import beartype, BeartypeConf, BeartypeStrategy

# Dynamically create a new @slowmobeartype decorator enabling &quot;full fat&quot;
# O(n) type-checking.
slowmobeartype = beartype(conf=BeartypeConf(strategy=BeartypeStrategy.On))

# Type-check all items of the passed list. Do this only when you pretend
# to know in your guts that this list will *ALWAYS* be ignorably small.
@bslowmobeartype
def type_check_like_maple_syrup(liquid_gold: list[int]) -&gt; str:
 return &#39;The slowest noop yet envisioned? You&#39;re not wrong.&#39;

Strategies enforce their corresponding runtime complexities (e.g.,
\(O(n)\)) across *all* type-checks performed for callables enabling those
strategies. For example, a callable configured by the
[`BeartypeStrategy.On`](#beartype.BeartypeStrategy.On) strategy will exhibit linear \(O(n)\)
complexity as its overhead for type-checking each nesting level of each
container passed to and returned from that callable.
This enumeration defines these members:

On[¶](#beartype.BeartypeStrategy.On)

`Type:` `beartype.cave.EnumMemberType`

**Linear-time strategy:** the \(O(n)\) strategy, type-checking
*all* items of a container.

Note

**This strategy is currently unimplemented.** Still, interested users
are advised to opt-in to this strategy now; your code will then
type-check as desired on the first beartype release supporting this
strategy.
Beartype: *We’re here for you, fam.*

Ologn[¶](#beartype.BeartypeStrategy.Ologn)

`Type:` `beartype.cave.EnumMemberType`

**Logarithmic-time strategy:** the \(O(\log n)\) strategy,
type-checking a randomly selected number of items `log(len(obj))` of
each container `obj`.

Note

**This strategy is currently unimplemented.** Still, interested users
are advised to opt-in to this strategy now; your code will then
type-check as desired on the first beartype release supporting this
strategy.
Beartype: *We’re here for you, fam.*

O1[¶](#beartype.BeartypeStrategy.O1)

`Type:` `beartype.cave.EnumMemberType`

**Constant-time strategy:** the default \(O(1)\) strategy,
type-checking a single randomly selected item of each container. As the
default, this strategy need *not* be explicitly enabled.

O0[¶](#beartype.BeartypeStrategy.O0)

`Type:` `beartype.cave.EnumMemberType`

**No-time strategy,** disabling type-checking for a decorated callable by
reducing [`beartype()`](#beartype.beartype) to the identity decorator for that callable.
This strategy is functionally equivalent to but more general-purpose than
the standard [`typing.no_type_check()`](https://docs.python.org/3/library/typing.html#typing.no_type_check) decorator; whereas
[`typing.no_type_check()`](https://docs.python.org/3/library/typing.html#typing.no_type_check) only applies to callables, this strategy
applies to *any* context accepting a beartype configuration such as:

- The [`beartype()`](#beartype.beartype) decorator decorating a class.

- The [`beartype.door.is_bearable()`](../api_door/#beartype.door.is_bearable) function.

- The [`beartype.door.die_if_unbearable()`](../api_door/#beartype.door.die_if_unbearable) function.

- The [`beartype.door.TypeHint.is_bearable()`](../api_door/#beartype.door.TypeHint.is_bearable) method.

- The [`beartype.door.TypeHint.die_if_unbearable()`](../api_door/#beartype.door.TypeHint.die_if_unbearable) method.

Just like in real life, there exist valid use cases for doing absolutely
nothing – including:

**Blacklisting callables.** While seemingly useless, this strategy
allows callers to selectively prevent callables that would otherwise be
type-checked (e.g., due to class decorations or import hooks) from
being type-checked:
# Import the requisite machinery.
from beartype import beartype, BeartypeConf, BeartypeStrategy

# Dynamically create a new @nobeartype decorator disabling type-checking.
nobeartype = beartype(conf=BeartypeConf(strategy=BeartypeStrategy.O0))

# Automatically decorate all methods of this class...
@beartype
class TypeCheckedClass(object):
 # Including this method, which raises a type-checking violation
 # due to returning a non-&quot;None&quot; value.
 def type_checked_method(self) -&gt; None:
 return &#39;This string is not &quot;None&quot;. Apparently, that is a problem.&#39;

 # Excluding this method, which raises *NO* type-checking
 # violation despite returning a non-&quot;None&quot; value.
 @nobeartype
 def non_type_checked_method(self) -&gt; None:
 return &#39;This string is not &quot;None&quot;. Thankfully, no one cares.&#39;

**Eliding overhead.** Beartype already exhibits near-real-time
overhead of less than 1µs (one microsecond, one millionth of a second)
per call of type-checked callables. When even that
negligible overhead isn’t negligible enough, brave callers considering
an occupational change may globally disable *all* type-checking
performed by beartype. Prepare your resume beforehand. Also, do so
*only* under production builds intended for release; development builds
intended for testing should preserve type-checking.
Either:

[Pass Python the “-O” command-line option](https://docs.python.org/3/using/cmdline.html#cmdoption-o), which beartype
respects.
- [Run Python under the “PYTHONOPTIMIZE” environment variable](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONOPTIMIZE), which beartype also respects.

Define a new `&#64;maybebeartype` decorator disabling type-checking when
an app-specific constant `I_AM_RELEASE_BUILD` defined elsewhere is
enabled:
# Import the requisite machinery.
from beartype import beartype, BeartypeConf, BeartypeStrategy

# Let us pretend you know what you are doing for a hot moment.
from your_app import I_AM_RELEASE_BUILD

# Dynamically create a new @maybebeartype decorator disabling
# type-checking when &quot;I_AM_RELEASE_BUILD&quot; is enabled.
maybebeartype = beartype(conf=BeartypeConf(strategy=(
 BeartypeStrategy.O0
 if I_AM_RELEASE_BUILD else
 BeartypeStrategy.O1
))

# Decorate with this decorator rather than @beartype everywhere.
@maybebeartype
def muh_performance_critical_func(big_list: list[int]) -&gt; int:
 return sum(big_list)

#### [Beartype Environment Variables](#id18)[¶](#beartype-environment-variables)

Beartype supports increasingly many **environment variables** (i.e., external
shell variables associated with the active Python interpreter). Most of these
variables globally override [`BeartypeConf`](#beartype.BeartypeConf) parameters of similar names,
enabling end users to enforce global configuration policies across their full
app stacks.
Beneath environment variables… *thy humongous codebase shalt rise.*

##### [${BEARTYPE_IS_COLOR}](#id19)[¶](#beartype-is-color)

The `${BEARTYPE_IS_COLOR}` environment variable globally overrides the
[`BeartypeConf.is_color`](#beartype.BeartypeConf.is_color) parameter, enabling end users to enforce a global
colour policy. As with that parameter, this variable is a tri-state boolean with
three possible string values:

`BEARTYPE_IS_COLOR='True'`, forcefully instantiating *all* beartype
configurations across *all* Python processes with the `is_color=True`
parameter.
`BEARTYPE_IS_COLOR='False'`, forcefully instantiating *all* beartype
configurations across *all* Python processes with the `is_color=False`
parameter.
`BEARTYPE_IS_COLOR='None'`, forcefully instantiating *all* beartype
configurations across *all* Python processes with the `is_color=None`
parameter.

Force beartype to obey your unthinking hatred of the colour spectrum. You can’t
be wrong!
BEARTYPE_IS_COLOR=False python3 -m monochrome_retro_app.its_srsly_cool

New in version 0.16.0.

 
 
 
 
 
 
 **
 
 previous

 Beartype Import Hooks

 
 
 
 
 next

 Beartype Validators

 
 **
# Source: https://beartype.readthedocs.io/en/latest/api_vale/

Tip

💗 **Upbear us** at [GitHub Sponsors](https://github.com/sponsors/leycec) and SonarQube Advanced Security
(Tidelift). **Follow us** [on Bluesky](https://leycec.bsky.social). **Friendzone us** [at Zulip](https://beartype.zulipchat.com).
Your generous support is our quality assurance. 💗

# Beartype Validators[¶](#beartype-validators)

Validate anything with two-line type hints
 designed by you ⇄ built by beartype

When standards fail, do what you want anyway. When official type hints fail to
scale to your validation use case, design your own PEP-compliant type hints with
compact **beartype validators:**
# Import the requisite machinery.
from beartype import beartype
from beartype.vale import Is
from typing import Annotated

# Type hint matching any two-dimensional NumPy array of floats of arbitrary
# precision. Aye, typing matey. Beartype validators a-hoy!
import numpy as np
Numpy2DFloatArray = Annotated[np.ndarray, Is[lambda array:
 array.ndim == 2 and np.issubdtype(array.dtype, np.floating)]]

# Annotate @beartype-decorated callables with beartype validators.
@beartype
def polygon_area(polygon: Numpy2DFloatArray) -&gt; float:
 &#39;&#39;&#39;
 Area of a two-dimensional polygon of floats defined as a set of
 counter-clockwise points, calculated via Green&#39;s theorem.

 *Don&#39;t ask.*
 &#39;&#39;&#39;

 # Calculate and return the desired area. Pretend we understand this.
 polygon_rolled = np.roll(polygon, -1, axis=0)
 return np.abs(0.5*np.sum(
 polygon[:,0]*polygon_rolled[:,1] -
 polygon_rolled[:,0]*polygon[:,1]))

Validators enforce arbitrary runtime constraints on the internal structure and
contents of parameters and returns with user-defined lambda functions and
nestable declarative expressions leveraging familiar [`typing`](https://docs.python.org/3/library/typing.html#module-typing) syntax – all
seamlessly composable with [standard type hints](../eli5/#eli5-typing) via an
[expressive domain-specific language (DSL)](#validator-syntax).
Validate custom project constraints *now* without waiting for the open-source
community to officially standardize, implement, and publish those constraints.
Filling in the Titanic-sized gaps between [Python’s patchwork quilt of PEPs](../pep/#pep-pep), validators accelerate your QA workflow with your greatest asset.

Yup. It’s your brain.

See [Validator Showcase](#validator-showcase) for comforting examples – or blithely continue for
uncomfortable details you may regret reading.

**Bear with Us**

- [Validator Overview](#validator-overview)

- [Validator API](#validator-api)

- [Validator Syntax](#validator-syntax)

- [Validator Caveats](#validator-caveats)

[Validator Showcase](#validator-showcase)

- [Full-Fat O(n) Matching](#full-fat-o-n-matching)

- [Trendy String Matching](#trendy-string-matching)

[Type Hint Arithmetic](#type-hint-arithmetic)

[Type Hint Elision](#type-hint-elision)

- [Booleans ≠ Integers](#booleans-integers)

- [Strings ≠ Sequences](#strings-sequences)

- [Tensor Property Matching](#tensor-property-matching)

[Validator Alternatives](#validator-alternatives)

[NumPy Type Hints](#numpy-type-hints)

- [Typed NumPy Arrays](#typed-numpy-arrays)

## [Validator Overview](#id6)[¶](#validator-overview)

Beartype validators are **zero-cost code generators.** Like the rest of beartype
(but unlike other validation frameworks), beartype validators generate optimally
efficient pure-Python type-checking logic with *no* hidden function or method
calls, undocumented costs, or runtime overhead.
Beartype validator code is thus **call-explicit.** Since pure-Python function
and method calls are notoriously slow in [CPython](https://github.com/python/cpython), the code we generate only
calls the pure-Python functions and methods you specify when you subscript
`beartype.vale.Is*` classes with those functions and methods. That’s it. We
*never* call anything without your permission. For example:

The declarative validator Annotated[np.ndarray, IsAttr['dtype',
IsAttr['type', IsEqual[np.float64]]]] detects NumPy arrays of 64-bit
floating-point precision by generating the fastest possible inline expression
for doing so:
isinstance(array, np.ndarray) and array.dtype.type == np.float64

The functional validator Annotated[np.ndarray, Is[lambda array:
array.dtype.type == np.float64]] also detects the same arrays by generating
a slightly slower inline expression calling the lambda function you define:
isinstance(array, np.ndarray) and your_lambda_function(array)

Beartype validators thus come in two flavours – each with attendant tradeoffs:

**Functional validators,** created by subscripting the
[`beartype.vale.Is`](#beartype.vale.Is) factory with a function accepting a single parameter
and returning [`True`](https://docs.python.org/3/library/constants.html#True) only when that parameter satisfies a caller-defined
constraint. Each functional validator incurs the cost of calling that function
for each call to each [`beartype.beartype()`](../api_decor/#beartype.beartype)-decorated callable annotated
by that validator, but is Turing-complete and thus supports all possible
validation scenarios.
**Declarative validators,** created by subscripting any *other* class in the
[`beartype.vale`](#module-beartype.vale) subpackage (e.g., [`beartype.vale.IsEqual`](#beartype.vale.IsEqual)) with
arguments specific to that class. Each declarative validator generates
efficient inline code calling *no* hidden functions and thus incurring no
function costs, but is special-purpose and thus supports only a narrow band of
validation scenarios.

Wherever you can, prefer *declarative* validators for efficiency.

Everywhere else, fallback to *functional* validators for generality.

## [Validator API](#id7)[¶](#validator-api)

*class *beartype.vale.Is[¶](#beartype.vale.Is)

`Subscription API:` beartype.vale.**Is**[[`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[`object`](https://docs.python.org/3/library/functions.html#object)], [`bool`](https://docs.python.org/3/library/functions.html#bool)]]

**Functional validator.** A PEP-compliant type hint enforcing any arbitrary
runtime constraint – created by subscripting (indexing) the [`Is`](#beartype.vale.Is) type
hint factory with a function accepting a single parameter and returning
either:

- [`True`](https://docs.python.org/3/library/constants.html#True) if that parameter satisfies that constraint.

- [`False`](https://docs.python.org/3/library/constants.html#False) otherwise.

# Import the requisite machinery.
from beartype.vale import Is
from typing import Annotated

# Type hint matching only strings with lengths ranging [4, 40].
LengthyString = Annotated[str, Is[lambda text: 4 &lt;= len(text) &lt;= 40]]

Functional validators are caller-defined and may thus validate the internal
integrity, consistency, and structure of arbitrary objects ranging from
simple builtin scalars like integers and strings to complex data structures
defined by third-party packages like NumPy arrays and Pandas DataFrames.

*class *beartype.vale.IsAttr[¶](#beartype.vale.IsAttr)

`Subscription API:` beartype.vale.**IsAttr**[[`str`](https://docs.python.org/3/library/stdtypes.html#str), `beartype.vale.*`]

**Declarative attribute validator.** A PEP-compliant type hint enforcing any
arbitrary runtime constraint on any named object attribute – created by
subscripting (indexing) the [`IsAttr`](#beartype.vale.IsAttr) type hint factory with (in
order):

- The unqualified name of that attribute.

- Any other beartype validator enforcing that constraint.

# Import the requisite machinery.
from beartype.vale import IsAttr, IsEqual
from typing import Annotated

# Type hint matching only two-dimensional NumPy arrays. Given this,
# @beartype generates efficient validation code resembling:
# isinstance(array, np.ndarray) and array.ndim == 2
import numpy as np
Numpy2DArray = Annotated[np.ndarray, IsAttr[&#39;ndim&#39;, IsEqual[2]]]

The first argument subscripting this class *must* be a syntactically valid
unqualified Python identifier string containing only alphanumeric and
underscore characters (e.g., `&quot;dtype&quot;`, `&quot;ndim&quot;`). Fully-qualified
attributes comprising two or more dot-delimited identifiers (e.g.,
`&quot;dtype.type&quot;`) may be validated by nesting successive [`IsAttr`](#beartype.vale.IsAttr)
subscriptions:
# Type hint matching only NumPy arrays of 64-bit floating-point numbers.
# From this, @beartype generates an efficient expression resembling:
# isinstance(array, np.ndarray) and array.dtype.type == np.float64
NumpyFloat64Array = Annotated[np.ndarray,
 IsAttr[&#39;dtype&#39;, IsAttr[&#39;type&#39;, IsEqual[np.float64]]]]

The second argument subscripting this class *must* be a beartype validator.
This includes:

[`beartype.vale.Is`](#beartype.vale.Is), in which case this parent [`IsAttr`](#beartype.vale.IsAttr) class
validates the desired object attribute to satisfy the caller-defined
function subscripting that child [`Is`](#beartype.vale.Is) class.
[`beartype.vale.IsAttr`](#beartype.vale.IsAttr), in which case this parent [`IsAttr`](#beartype.vale.IsAttr)
class validates the desired object attribute to contain a nested object
attribute satisfying the child [`IsAttr`](#beartype.vale.IsAttr) class. See above example.
[`beartype.vale.IsEqual`](#beartype.vale.IsEqual), in which case this [`IsAttr`](#beartype.vale.IsAttr) class
validates the desired object attribute to be equal to the object
subscripting that [`IsEqual`](#beartype.vale.IsEqual) class. See above example.

*class *beartype.vale.IsEqual[¶](#beartype.vale.IsEqual)

`Subscription API:` beartype.vale.**IsEqual**[[`object`](https://docs.python.org/3/library/functions.html#object)]

**Declarative equality validator.** A PEP-compliant type hint enforcing
equality against any object – created by subscripting (indexing) the
[`IsEqual`](#beartype.vale.IsEqual) type hint factory with that object:
# Import the requisite machinery.
from beartype.vale import IsEqual
from typing import Annotated

# Type hint matching only lists equal to [0, 1, 2, ..., 40, 41, 42].
AnswerToTheUltimateQuestion = Annotated[list, IsEqual[list(range(42))]]

[`IsEqual`](#beartype.vale.IsEqual) generalizes the comparable [**PEP 586**](https://peps.python.org/pep-0586/)-compliant
[`typing.Literal`](https://docs.python.org/3/library/typing.html#typing.Literal) type hint. Both check equality against user-defined
objects. Despite the differing syntax, these two type hints enforce the same
semantics:
# This beartype validator enforces the same semantics as...
IsStringEqualsWithBeartype = Annotated[str,
 IsEqual[&#39;Don’t you envy our pranceful bands?&#39;] |
 IsEqual[&#39;Don’t you wish you had extra hands?&#39;]
]

# This PEP 586-compliant type hint.
IsStringEqualsWithPep586 = Literal[
 &#39;Don’t you envy our pranceful bands?&#39;,
 &#39;Don’t you wish you had extra hands?&#39;,
]

The similarities end there, of course:

[`IsEqual`](#beartype.vale.IsEqual) permissively validates equality against objects that are
instances of **any arbitrary type.** [`IsEqual`](#beartype.vale.IsEqual) doesn’t care what
the types of your objects are. [`IsEqual`](#beartype.vale.IsEqual) will test equality against
everything you tell it to, because you know best.
[`typing.Literal`](https://docs.python.org/3/library/typing.html#typing.Literal) rigidly validates equality against objects that are
instances of **only six predefined types:**

- Booleans (i.e., [`bool`](https://docs.python.org/3/library/functions.html#bool) objects).

- Byte strings (i.e., [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes) objects).

- Integers (i.e., [`int`](https://docs.python.org/3/library/functions.html#int) objects).

- Unicode strings (i.e., [`str`](https://docs.python.org/3/library/stdtypes.html#str) objects).

- [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum) members. [[1]](#enum-type)

- The [`None`](https://docs.python.org/3/library/constants.html#None) singleton.

Wherever you can (which is mostly nowhere), prefer [`typing.Literal`](https://docs.python.org/3/library/typing.html#typing.Literal).
Sure, [`typing.Literal`](https://docs.python.org/3/library/typing.html#typing.Literal) is mostly useless, but it’s standardized across
type checkers in a mostly useless way. Everywhere else, default to
[`IsEqual`](#beartype.vale.IsEqual).

*class *beartype.vale.IsInstance[¶](#beartype.vale.IsInstance)

`Subscription API:` beartype.vale.**IsInstance**[[`type`](https://docs.python.org/3/library/functions.html#type), …]

**Declarative instance validator.** A PEP-compliant type hint enforcing
instancing of one or more classes – created by subscripting (indexing) the
[`IsInstance`](#beartype.vale.IsInstance) type hint factory with those classes:
# Import the requisite machinery.
from beartype.vale import IsInstance
from typing import Annotated

# Type hint matching only string and byte strings, equivalent to:
# StrOrBytesInstance = Union[str, bytes]
StrOrBytesInstance = Annotated[object, IsInstance[str, bytes]]

[`IsInstance`](#beartype.vale.IsInstance) generalizes **isinstanceable type hints** (i.e., normal
pure-Python or C-based classes that can be passed as the second parameter to
the [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance) builtin). Both check instancing of classes. Despite
the differing syntax, the following hints all enforce the same semantics:
# This beartype validator enforces the same semantics as...
IsUnicodeStrWithBeartype = Annotated[object, IsInstance[str]]

# ...this PEP 484-compliant type hint.
IsUnicodeStrWithPep484 = str

# Likewise, this beartype validator enforces the same semantics as...
IsStrWithWithBeartype = Annotated[object, IsInstance[str, bytes]]

# ...this PEP 484-compliant type hint.
IsStrWithWithPep484 = Union[str, bytes]

The similarities end there, of course:

[`IsInstance`](#beartype.vale.IsInstance) permissively validates type instancing of arbitrary
objects (including possibly nested attributes of parameters and returns
when combined with [`beartype.vale.IsAttr`](#beartype.vale.IsAttr)) against one or more
classes.
Isinstanceable classes rigidly validate type instancing of only
**parameters and returns** against only **one class.**

Unlike isinstanceable type hints, instance validators support various set
theoretic operators. Critically, this includes
negation. Instance validators prefixed by the negation operator `~` match
all objects that are *not* instances of the classes subscripting those
validators. Wait. Wait just a hot minute there. Doesn’t a
[`typing.Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) type hint necessarily match instances of the class
subscripting that type hint? Yup. This means type hints of the form
`typing.Annotated[{superclass}, ~IsInstance[{subclass}]` match all
instances of a superclass that are *not* also instances of a subclass. And…
pretty sure we just invented [type hint arithmetic](#type-hint-elision)
right there.
That sounded intellectual and thus boring. Yet, the disturbing fact that
Python booleans are integers …yup while Python strings are
infinitely recursive sequences of strings …yup means that
[type hint arithmetic](#type-hint-elision) can save your codebase from
Guido’s younger self. Consider this instance validator matching only
non-boolean integers, which *cannot* be expressed with any isinstanceable
type hint (e.g., [`int`](https://docs.python.org/3/library/functions.html#int)) or other combination of standard off-the-shelf
type hints (e.g., unions):
# Type hint matching any non-boolean integer. Never fear integers again.
IntNonbool = Annotated[int, ~IsInstance[bool]] # &lt;--- bruh

Wherever you can, prefer isinstanceable type hints. Sure, they’re inflexible,
but they’re inflexibly standardized across type checkers. Everywhere else,
default to [`IsInstance`](#beartype.vale.IsInstance).

*class *beartype.vale.IsSubclass[¶](#beartype.vale.IsSubclass)

`Subscription API:` beartype.vale.**IsSubclass**[[`type`](https://docs.python.org/3/library/functions.html#type), …]

**Declarative inheritance validator.** A PEP-compliant type hint enforcing
subclassing of one or more superclasses (base classes) – created by
subscripting (indexing) the [`IsSubclass`](#beartype.vale.IsSubclass) type hint factory with those
superclasses:
# Import the requisite machinery.
from beartype.vale import IsSubclass
from typing import Annotated

# Type hint matching only string and byte string subclasses.
StrOrBytesSubclass = Annotated[type, IsSubclass[str, bytes]]

[`IsSubclass`](#beartype.vale.IsSubclass) generalizes the comparable [**PEP 484**](https://peps.python.org/pep-0484/)-compliant
[`typing.Type`](https://docs.python.org/3/library/typing.html#typing.Type) and [**PEP 585**](https://peps.python.org/pep-0585/)-compliant [`type`](https://docs.python.org/3/library/functions.html#type) type hint
factories. All three check subclassing of arbitrary superclasses. Despite the
differing syntax, the following hints all enforce the same semantics:
# This beartype validator enforces the same semantics as...
IsStringSubclassWithBeartype = Annotated[type, IsSubclass[str]]

# ...this PEP 484-compliant type hint as well as...
IsStringSubclassWithPep484 = Type[str]

# ...this PEP 585-compliant type hint.
IsStringSubclassWithPep585 = type[str]

The similarities end there, of course:

[`IsSubclass`](#beartype.vale.IsSubclass) permissively validates type inheritance of arbitrary
classes (including possibly nested attributes of parameters and returns
when combined with [`beartype.vale.IsAttr`](#beartype.vale.IsAttr)) against one or more
superclasses.
[`typing.Type`](https://docs.python.org/3/library/typing.html#typing.Type) and [`type`](https://docs.python.org/3/library/functions.html#type) rigidly validates type inheritance of
only **parameters and returns** against only **one superclass.**

Consider this subclass validator, which validates type inheritance of a
deeply nested attribute and thus *cannot* be expressed with
[`typing.Type`](https://docs.python.org/3/library/typing.html#typing.Type) or [`type`](https://docs.python.org/3/library/functions.html#type):
# Type hint matching only NumPy arrays of reals (i.e., either integers
# or floats) of arbitrary precision, generating code resembling:
# (isinstance(array, np.ndarray) and
# issubclass(array.dtype.type, (np.floating, np.integer)))
NumpyRealArray = Annotated[
 np.ndarray, IsAttr[&#39;dtype&#39;, IsAttr[&#39;type&#39;, IsSubclass[
 np.floating, np.integer]]]]

Wherever you can, prefer [`type`](https://docs.python.org/3/library/functions.html#type) and [`typing.Type`](https://docs.python.org/3/library/typing.html#typing.Type). Sure, they’re
inflexible, but they’re inflexibly standardized across type checkers.
Everywhere else, default to [`IsSubclass`](#beartype.vale.IsSubclass).

[[1](#id1)]
You don’t want to know the type of [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum) members. Srsly. You
don’t. Okay… you do? Very well. It’s [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum). mic
drop

## [Validator Syntax](#id8)[¶](#validator-syntax)

Beartype validators support a rich domain-specific language (DSL) leveraging
familiar Python operators. Dynamically create new validators on-the-fly from
existing validators, fueling reuse and preserving [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself):

**Negation** (i.e., `not`). Negating any validator with the `~` operator
creates a new validator returning [`True`](https://docs.python.org/3/library/constants.html#True) only when the negated validator
returns [`False`](https://docs.python.org/3/library/constants.html#False):
# Type hint matching only strings containing *no* periods, semantically
# equivalent to this type hint:
# PeriodlessString = Annotated[str, Is[lambda text: &#39;.&#39; not in text]]
PeriodlessString = Annotated[str, ~Is[lambda text: &#39;.&#39; in text]]

**Conjunction** (i.e., `and`). And-ing two or more validators with the
`&amp;` operator creates a new validator returning [`True`](https://docs.python.org/3/library/constants.html#True) only when *all*
of the and-ed validators return [`True`](https://docs.python.org/3/library/constants.html#True):
# Type hint matching only non-empty strings containing *no* periods,
# semantically equivalent to this type hint:
# NonemptyPeriodlessString = Annotated[
# str, Is[lambda text: text and &#39;.&#39; not in text]]
SentenceFragment = Annotated[str, (
 Is[lambda text: bool(text)] &amp;
 ~Is[lambda text: &#39;.&#39; in text]
)]

**Disjunction** (i.e., `or`). Or-ing two or more validators with the `|`
operator creates a new validator returning [`True`](https://docs.python.org/3/library/constants.html#True) only when at least one
of the or-ed validators returns [`True`](https://docs.python.org/3/library/constants.html#True):
# Type hint matching only empty strings *and* non-empty strings containing
# one or more periods, semantically equivalent to this type hint:
# EmptyOrPeriodfullString = Annotated[
# str, Is[lambda text: not text or &#39;.&#39; in text]]
EmptyOrPeriodfullString = Annotated[str, (
 ~Is[lambda text: bool(text)] |
 Is[lambda text: &#39;.&#39; in text]
)]

**Enumeration** (i.e., `,`). Delimiting two or or more validators with
commas at the top level of a [`typing.Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) type hint is an alternate
syntax for and-ing those validators with the `&amp;` operator, creating a new
validator returning [`True`](https://docs.python.org/3/library/constants.html#True) only when *all* of those delimited validators
return [`True`](https://docs.python.org/3/library/constants.html#True).
# Type hint matching only non-empty strings containing *no* periods,
# semantically equivalent to the &quot;SentenceFragment&quot; defined above.
SentenceFragment = Annotated[str,
 Is[lambda text: bool(text)],
 ~Is[lambda text: &#39;.&#39; in text],
]

Since the `&amp;` operator is more explicit *and* usable in a wider variety of
syntactic contexts, the `&amp;` operator is generally preferable to enumeration
(all else being equal).

**Interoperability.** As PEP-compliant type hints, validators are safely
interoperable with other PEP-compliant type hints and usable wherever other
PEP-compliant type hints are usable. Standard type hints are subscriptable
with validators, because validators *are* standard type hints:
# Type hint matching only sentence fragments defined as either Unicode or
# byte strings, generalizing &quot;SentenceFragment&quot; type hints defined above.
SentenceFragment = Union[
 Annotated[bytes, Is[lambda text: b&#39;.&#39; in text]],
 Annotated[str, Is[lambda text: u&#39;.&#39; in text]],
]

[Standard Python precedence rules](_operatorprecedence) may apply.

DSL: *it’s not just a telecom acronym anymore.*

## [Validator Caveats](#id9)[¶](#validator-caveats)

Note

**Validators require:**

**Beartype.** Currently, all *other* static and runtime type checkers
silently ignore beartype validators during type-checking. This includes
[mypy](http://mypy-lang.org) – which we could possibly solve by bundling a [mypy plugin](https://mypy.readthedocs.io/en/stable/extending_mypy.html) with
beartype that extends [mypy](http://mypy-lang.org) to statically analyze declarative beartype
validators (e.g., [`beartype.vale.IsAttr`](#beartype.vale.IsAttr),
[`beartype.vale.IsEqual`](#beartype.vale.IsEqual)). We leave this as an exercise to the
idealistic doctoral thesis candidate. Please do this for us,
someone who is not us.
Either **Python ≥ 3.9** *or* [typing_extensions ≥ 3.9.0.0](https://pypi.org/project/typing-extensions). Validators piggyback onto the
[`typing.Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) class first introduced with Python 3.9.0 and since
backported to older Python versions by the third-party “typing_extensions”
package, which beartype also transparently
supports.

## [Validator Showcase](#id10)[¶](#validator-showcase)

Observe the disturbing (yet alluring) utility of beartype validators in action
as they unshackle type hints from the fetters of PEP compliance. Begone,
foulest standards!

### [Full-Fat O(n) Matching](#id11)[¶](#full-fat-o-n-matching)

Let’s validate **all integers in a list of integers in O(n) time**, because
validators mean you no longer have to accept the QA scraps we feed you:
# Import the requisite machinery.
from beartype import beartype
from beartype.vale import Is
from typing import Annotated

# Type hint matching all integers in a list of integers in O(n) time. Please
# never do this. You now want to, don&#39;t you? Why? You know the price! Why?!?
IntList = Annotated[list[int], Is[lambda lst: all(
 isinstance(item, int) for item in lst)]]

# Type-check all integers in a list of integers in O(n) time. How could you?
@beartype
def sum_intlist(my_list: IntList) -&gt; int:
 &#39;&#39;&#39;
 The slowest possible integer summation over the passed list of integers.

 There goes your whole data science pipeline. Yikes! So much cringe.
 &#39;&#39;&#39;

 return sum(my_list) # oh, gods what have you done

Welcome to **full-fat type-checking.** In our disastrous roadmap to beartype
1.0.0, we reluctantly admit that we’d like to augment the
[`beartype.beartype()`](../api_decor/#beartype.beartype) decorator with a new parameter enabling full-fat
type-checking. But don’t wait for us. Force the issue now by just doing it
yourself and then mocking us all over Gitter! *Fight the bear, man.*
[There are good reasons to believe that O(1) type-checking is preferable](../faq/#faq-o1). Violating that core precept exposes your codebase to scalability and
security concerns. But you’re the Big Boss, you swear you know best, and (in any
case) we can’t stop you because we already let the unneutered tomcat out of his
trash bin by [publishing this API into the badlands of PyPI](https://pypi.org/project/beartype).

### [Trendy String Matching](#id12)[¶](#trendy-string-matching)

Let’s accept strings either at least 80 characters long *or* both quoted and
suffixed by a period. Look, it doesn’t matter. Just do it already, beartype!
# Import the requisite machinery.
from beartype import beartype
from beartype.vale import Is
from typing import Annotated

# Validator matching only strings at least 80 characters in length.
IsLengthy = Is[lambda text: len(text) &gt;= 80]

# Validator matching only strings suffixed by a period.
IsSentence = Is[lambda text: text and text[-1] == &#39;.&#39;]

# Validator matching only single- or double-quoted strings.
def _is_quoted(text): return text.count(&#39;&quot;&#39;) &gt;= 2 or text.count(&quot;&#39;&quot;) &gt;= 2
IsQuoted = Is[_is_quoted]

# Combine multiple validators by just listing them sequentially.
@beartype
def desentence_lengthy_quoted_sentence(
 text: Annotated[str, IsLengthy, IsSentence, IsQuoted]]) -&gt; str:
 &#39;&#39;&#39;
 Strip the suffixing period from a lengthy quoted sentence... &#39;cause.
 &#39;&#39;&#39;

 return text[:-1] # this is horrible

# Combine multiple validators by just &quot;&amp;&quot;-ing them sequentially. Yes, this
# is exactly identical to the prior function. We do this because we can.
@beartype
def desentence_lengthy_quoted_sentence_part_deux(
 text: Annotated[str, IsLengthy &amp; IsSentence &amp; IsQuoted]]) -&gt; str:
 &#39;&#39;&#39;
 Strip the suffixing period from a lengthy quoted sentence... again.
 &#39;&#39;&#39;

 return text[:-1] # this is still horrible

# Combine multiple validators with as many &quot;&amp;&quot;, &quot;|&quot;, and &quot;~&quot; operators as
# you can possibly stuff into a module that your coworkers can stomach.
# (They will thank you later. Possibly much later.)
@beartype
def strip_lengthy_or_quoted_sentence(
 text: Annotated[str, IsLengthy | (IsSentence &amp; ~IsQuoted)]]) -&gt; str:
 &#39;&#39;&#39;
 Strip the suffixing character from a string that is lengthy and/or a
 quoted sentence, because your web app deserves only the best data.
 &#39;&#39;&#39;

 return text[:-1] # this is frankly outrageous

### [Type Hint Arithmetic](#id13)[¶](#type-hint-arithmetic)

**Subtitle:** *From Set Theory They Shall Grow*

[**PEP 484**](https://peps.python.org/pep-0484/) standardized the [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union) factory [disjunctively](https://en.wikipedia.org/wiki/Logical_disjunction) matching any of several equally permissible type hints ala
Python’s builtin `or` operator or the overloaded `|` operator for sets.
That’s great, because set theory is the beating heart behind type theory.
But that’s just [disjunction](https://en.wikipedia.org/wiki/Logical_disjunction). What about [intersection](https://en.wikipedia.org/wiki/Intersection_(set_theory)) (e.g., `and`, `&amp;`),
[complementation](https://en.wikipedia.org/wiki/Complement_(set_theory)#Relative_complement) (e.g., `not`, `~`), or any
of the vast multitude of *other* set theoretic operations? Can we logically
connect simple type hints validating trivial constraints into complex type
hints validating non-trivial constraints via PEP-standardized analogues of
unary and binary operators?
**Nope.** They don’t exist yet. But that’s okay. You use beartype, which means
you don’t have to wait for official Python developers to get there first.
You’re already there. …woah

#### [Type Hint Elision](#id14)[¶](#type-hint-elision)

Python’s core type hierarchy conceals an ugly history of secretive backward
compatibility. In this subsection, we uncover the two filthiest, flea-infested,
backwater corners of the otherwise well-lit atrium that is the Python language
– and how exactly you can finalize them. Both obstruct type-checking, readable
APIs, and quality assurance in the post-Python 2.7 era.
Guido doesn’t want you to know. But you want to know, don’t you? You are about
to enter another dimension, a dimension not only of syntax and semantics but of
shame. A journey into a hideous land of annotation wrangling. Next stop… the
Beartype Zone. Because guess what?

**Booleans are integers.** They shouldn’t be. Booleans aren’t integers in most
high-level languages. Wait. Are you telling me booleans are literally integers
in Python? Surely you jest. That can’t be. You can’t *add* booleans, can you?
What would that even mean if you could? Observe and cower, rigorous data
scientists.
&gt;&gt;&gt; True + 3.1415
4.141500000000001 # &lt;-- oh. by. god.
&gt;&gt;&gt; isinstance(False, int)
True # &lt;-- when nothing is true, everything is true

**Strings are infinitely recursive sequences of…** yup, it’s strings. They
shouldn’t be. Strings aren’t infinitely recursive data structures in any
other language devised by incautious mortals – high-level or not. Wait. Are
you telling me strings are both indistinguishable from full-blown immutable
sequences containing arbitrary items *and* infinitely recurse into themselves
like that sickening non-Euclidean Hall of Mirrors I puked all over when I was
a kid? Surely you kid. That can’t be. You can’t infinitely index into strings
*and* pass and return the results to and from callables expecting either
`Sequence[Any]` or `Sequence[str]` type hints, can you? Witness and
tremble, stricter-than-thou QA evangelists.
&gt;&gt;&gt; &#39;yougottabekiddi—&#39;[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0]
&#39;y&#39; # &lt;-- pretty sure we just broke the world
&gt;&gt;&gt; from collections.abc import Sequence
&gt;&gt;&gt; isinstance(&quot;Ph&#39;nglui mglw&#39;nafh Cthu—&quot;[0][0][0][0][0], Sequence)
True # &lt;-- ...curse you, curse you to heck and back

When we annotate a callable as accepting an [`int`](https://docs.python.org/3/library/functions.html#int), we *never* want that
callable to also silently accept a [`bool`](https://docs.python.org/3/library/functions.html#bool). Likewise, when we annotate
another callable as accepting a `Sequence[Any]` or `Sequence[str]`, we
*never* want that callable to also silently accept a [`str`](https://docs.python.org/3/library/stdtypes.html#str). These are
sensible expectations – just not in Python, where madness prevails.
To resolve these counter-intuitive concerns, we need the equivalent of the
[relative set complement (or difference)](https://en.wikipedia.org/wiki/Complement_(set_theory)#Relative_complement). We now
call this thing… **type elision!** Sounds pretty hot, right? We know.

##### [Booleans ≠ Integers](#id15)[¶](#booleans-integers)

Let’s first validate **non-boolean integers** with a beartype validator
effectively declaring a new `int - bool` class (i.e., the subclass of all
integers that are *not* booleans):
# Import the requisite machinery.
from beartype import beartype
from beartype.vale import IsInstance
from typing import Annotated

# Type hint matching any non-boolean integer. This day all errata die.
IntNonbool = Annotated[int, ~IsInstance[bool]] # &lt;--- bruh

# Type-check zero or more non-boolean integers summing to a non-boolean
# integer. Beartype wills it. So it shall be.
@beartype
def sum_ints(*args: IntNonbool) -&gt; IntNonbool:
 &#39;&#39;&#39;
 I cast thee out, mangy booleans!

 You plague these shores no more.
 &#39;&#39;&#39;

 return sum(args)

##### [Strings ≠ Sequences](#id16)[¶](#strings-sequences)

Let’s next validate **non-string sequences** with beartype validators
effectively declaring a new `Sequence - str` class (i.e., the subclass of all
sequences that are *not* strings):
# Import the requisite machinery.
from beartype import beartype
from beartype.vale import IsInstance
from collections.abc import Sequence
from typing import Annotated

# Type hint matching any non-string sequence. Your day has finally come.
SequenceNonstr = Annotated[Sequence, ~IsInstance[str]] # &lt;--- we doin this

# Type hint matching any non-string sequence *WHOSE ITEMS ARE ALL STRINGS.*
SequenceNonstrOfStr = Annotated[Sequence[str], ~IsInstance[str]]

# Type-check a non-string sequence of arbitrary items coerced into strings
# and then joined on newline to a new string. (Beartype got your back, bro.)
@beartype
def join_objects(my_sequence: SequenceNonstr) -&gt; str:
 &#39;&#39;&#39;
 Your tide of disease ends here, :class:`str` class!
 &#39;&#39;&#39;

 return &#39;\n&#39;.join(map(str, my_sequence)) # &lt;-- no idea how that works

# Type-check a non-string sequence whose items are all strings joined on
# newline to a new string. It isn&#39;t much, but it&#39;s all you ask.
@beartype
def join_strs(my_sequence: SequenceNonstrOfStr) -&gt; str:
 &#39;&#39;&#39;
 I expectorate thee up, sequence of strings.
 &#39;&#39;&#39;

 return &#39;\n&#39;.join(my_sequence) # &lt;-- do *NOT* do this to a string

### [Tensor Property Matching](#id17)[¶](#tensor-property-matching)

Let’s validate the same two-dimensional NumPy array of floats of arbitrary
precision as in the lead example above with an
efficient declarative validator avoiding the additional stack frame imposed by
the functional validator in that example:
# Import the requisite machinery.
from beartype import beartype
from beartype.vale import IsAttr, IsEqual, IsSubclass
from typing import Annotated

# Type hint matching only two-dimensional NumPy arrays of floats of
# arbitrary precision. This time, do it faster than anyone has ever
# type-checked NumPy arrays before. (Cue sonic boom, Chuck Yeager.)
import numpy as np
Numpy2DFloatArray = Annotated[np.ndarray,
 IsAttr[&#39;ndim&#39;, IsEqual[2]] &amp;
 IsAttr[&#39;dtype&#39;, IsAttr[&#39;type&#39;, IsSubclass[np.floating]]]
]

# Annotate @beartype-decorated callables with beartype validators.
@beartype
def polygon_area(polygon: Numpy2DFloatArray) -&gt; float:
 &#39;&#39;&#39;
 Area of a two-dimensional polygon of floats defined as a set of
 counter-clockwise points, calculated via Green&#39;s theorem.

 *Don&#39;t ask.*
 &#39;&#39;&#39;

 # Calculate and return the desired area. Pretend we understand this.
 polygon_rolled = np.roll(polygon, -1, axis=0)
 return np.abs(0.5*np.sum(
 polygon[:,0]*polygon_rolled[:,1] -
 polygon_rolled[:,0]*polygon[:,1]))

## [Validator Alternatives](#id18)[¶](#validator-alternatives)

If the unbridled power of beartype validators leaves you variously queasy,
uneasy, and suspicious of our core worldview, beartype also supports third-party
type hints like [typed NumPy arrays](#numpy-type-hints).
Whereas beartype validators are verbose, expressive, and general-purpose, the
following hints are terse, inexpressive, and domain-specific. Since beartype
internally converts these hints to their equivalent validators, similar
caveats apply. Notably, these hints require:

- Either **Python ≥ 3.9** *or* [typing_extensions ≥ 3.9.0.0](https://pypi.org/project/typing-extensions).

- **Beartype,** which hopefully goes without saying.

### [NumPy Type Hints](#id19)[¶](#numpy-type-hints)

Beartype conditionally supports NumPy type hints (i.e., annotations created by
subscripting (indexing) various attributes of the “numpy.typing” subpackage) when these optional runtime dependencies are *all* satisfied:

- Python ≥ 3.8.0.

- beartype ≥ 0.8.0.

- [NumPy ≥ 1.21.0](https://numpy.org).

- Either **Python ≥ 3.9** *or* [typing_extensions ≥ 3.9.0.0](https://pypi.org/project/typing-extensions).

Beartype internally converts [NumPy type hints](https://numpy.org/devdocs/reference/typing.html) into
[equivalent beartype validators](#beartype-validators) at decoration time.
[NumPy type hints currently only validate dtypes](https://numpy.org/devdocs/reference/typing.html), a common
but limited use case. [Beartype validators](#beartype-validators) validate
*any* arbitrary combinations of array constraints – including dtypes, shapes,
contents, and… well, *anything.* Which is alot. [NumPy type hints](https://numpy.org/devdocs/reference/typing.html#ndarray) are thus just syntactic sugar for beartype
validators – albeit quasi-portable syntactic sugar
also supported by [mypy](http://mypy-lang.org).
Wherever you can, prefer [NumPy type hints](https://numpy.org/devdocs/reference/typing.html) for portability.
Everywhere else, default to [beartype validators](#beartype-validators) for
generality. Combine them for the best of all possible worlds:
# Import the requisite machinery.
from beartype import beartype
from beartype.vale import IsAttr, IsEqual
from numpy import floating
from numpy.typing import NDArray
from typing import Annotated

# Beartype validator + NumPy type hint matching all two-dimensional NumPy
# arrays of floating-point numbers of any arbitrary precision.
NumpyFloat64Array = Annotated[NDArray[floating], IsAttr[&#39;ndim&#39;, IsEqual[2]]]

Rejoice! A one-liner solves everything yet again.

#### [Typed NumPy Arrays](#id20)[¶](#typed-numpy-arrays)

Type NumPy arrays by subscripting (indexing) the [numpy.typing.NDArray](https://numpy.org/devdocs/reference/typing.html#ndarray) class
with one of three possible types of objects:

- An **array dtype** (i.e., instance of the [numpy.dtype](https://numpy.org/doc/stable/reference/arrays.dtypes.html) class).

A **scalar dtype** (i.e., concrete subclass of the [numpy.generic](https://numpy.org/doc/stable/reference/arrays.scalars.html?highlight=numpy%20generic#numpy.generic) abstract
base class (ABC)).
- A **scalar dtype ABC** (i.e., abstract subclass of the [numpy.generic](https://numpy.org/doc/stable/reference/arrays.scalars.html?highlight=numpy%20generic#numpy.generic) ABC).

Beartype generates fundamentally different type-checking code for these types,
complying with both [mypy](http://mypy-lang.org) semantics (which behaves similarly) and our userbase
(which demands this behaviour). May there be hope for our collective future.
*class* numpy.typing.**NDArray**[[numpy.dtype](https://numpy.org/doc/stable/reference/arrays.dtypes.html)]

**NumPy array typed by array dtype.** A PEP-noncompliant type hint enforcing
object equality against any **array dtype** (i.e., [numpy.dtype](https://numpy.org/doc/stable/reference/arrays.dtypes.html) instance),
created by subscripting (indexing) the [numpy.typing.NDArray](https://numpy.org/devdocs/reference/typing.html#ndarray) class with that
array dtype.
Prefer this variant when validating the exact data type of an array:

# Import the requisite machinery.
from beartype import beartype
from numpy import dtype
from numpy.typing import NDArray

# NumPy type hint matching all NumPy arrays of 32-bit big-endian integers,
# semantically equivalent to this beartype validator:
# NumpyInt32BigEndianArray = Annotated[
# np.ndarray, IsAttr[&#39;dtype&#39;, IsEqual[dtype(&#39;&gt;i4&#39;)]]]
NumpyInt32BigEndianArray = NDArray[dtype(&#39;&gt;i4&#39;)]

*class* numpy.typing.**NDArray**[[numpy.dtype.type](https://numpy.org/doc/stable/reference/arrays.dtypes.html)]

**NumPy array typed by scalar dtype.** A PEP-noncompliant type hint
enforcing object equality against any **scalar dtype** (i.e., concrete
subclass of the [numpy.generic](https://numpy.org/doc/stable/reference/arrays.scalars.html?highlight=numpy%20generic#numpy.generic) ABC), created by subscripting (indexing) the
[numpy.typing.NDArray](https://numpy.org/devdocs/reference/typing.html#ndarray) class with that scalar dtype.
Prefer this variant when validating the exact scalar precision of an array:

# Import the requisite machinery.
from beartype import beartype
from numpy import float64
from numpy.typing import NDArray

# NumPy type hint matching all NumPy arrays of 64-bit floats, semantically
# equivalent to this beartype validator:
# NumpyFloat64Array = Annotated[
# np.ndarray, IsAttr[&#39;dtype&#39;, IsAttr[&#39;type&#39;, IsEqual[float64]]]]
NumpyFloat64Array = NDArray[float64]

Common scalar dtypes include:

**Fixed-precision integer dtypes** (e.g., `numpy.int32`,
`numpy.int64`).
**Fixed-precision floating-point dtypes** (e.g.,
`numpy.float32`, `numpy.float64`).

*class* numpy.typing.**NDArray**[[type](https://docs.python.org/3/library/stdtypes.html#bltin-type-objects)[[numpy.dtype.type](https://numpy.org/doc/stable/reference/arrays.dtypes.html)]]

**NumPy array typed by scalar dtype ABC.** A PEP-noncompliant type hint
enforcing type inheritance against any **scalar dtype ABC** (i.e.,
abstract subclass of the [numpy.generic](https://numpy.org/doc/stable/reference/arrays.scalars.html?highlight=numpy%20generic#numpy.generic) ABC), created by subscripting
(indexing) the [numpy.typing.NDArray](https://numpy.org/devdocs/reference/typing.html#ndarray) class with that ABC.
Prefer this variant when validating only the *kind* of scalars (without
reference to exact precision) in an array:
# Import the requisite machinery.
from beartype import beartype
from numpy import floating
from numpy.typing import NDArray

# NumPy type hint matching all NumPy arrays of floats of arbitrary
# precision, equivalent to this beartype validator:
# NumpyFloatArray = Annotated[
# np.ndarray, IsAttr[&#39;dtype&#39;, IsAttr[&#39;type&#39;, IsSubclass[floating]]]]
NumpyFloatArray = NDArray[floating]

Common scalar dtype ABCs include:

- [numpy.integer](https://numpy.org/doc/stable/reference/arrays.scalars.html?highlight=numpy%20generic#numpy.integer), the superclass of all fixed-precision integer dtypes.

[numpy.floating](https://numpy.org/doc/stable/reference/arrays.scalars.html?highlight=numpy%20generic#numpy.floating), the superclass of all fixed-precision floating-point
dtypes.

 
 
 
 
 
 
 **
 
 previous

 Beartype Decoration

 
 
 
 
 next

 Beartype DOOR

 
 **
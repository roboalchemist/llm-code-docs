# Source: https://boltons.readthedocs.io/en/latest/formatutils.html

Title: str.format() toolbox — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/formatutils.html

Markdown Content:
`formatutils` - `str.format()` toolbox[](https://boltons.readthedocs.io/en/latest/formatutils.html#module-boltons.formatutils "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------

[PEP 3101](https://www.python.org/dev/peps/pep-3101/) introduced the [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "(in Python v3.14)") method, and what would later be called “new-style” string formatting. For the sake of explicit correctness, it is probably best to refer to Python’s dual string formatting capabilities as _bracket-style_ and _percent-style_. There is overlap, but one does not replace the other.

> *   Bracket-style is more pluggable, slower, and uses a method.
> 
> *   Percent-style is simpler, faster, and uses an operator.

Bracket-style formatting brought with it a much more powerful toolbox, but it was far from a full one. [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "(in Python v3.14)") uses [more powerful syntax](https://docs.python.org/2/library/string.html#format-string-syntax), but [the tools and idioms](https://docs.python.org/2/library/string.html#string-formatting) for working with that syntax are not well-developed nor well-advertised.

`formatutils` adds several functions for working with bracket-style format strings:

> *   [`DeferredValue`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.DeferredValue "boltons.formatutils.DeferredValue"): Defer fetching or calculating a value until format time.
> 
> *   [`get_format_args()`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.get_format_args "boltons.formatutils.get_format_args"): Parse the positional and keyword arguments out of a format string.
> 
> *   [`tokenize_format_str()`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.tokenize_format_str "boltons.formatutils.tokenize_format_str"): Tokenize a format string into literals and [`BaseFormatField`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.BaseFormatField "boltons.formatutils.BaseFormatField") objects.
> 
> *   [`construct_format_field_str()`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.construct_format_field_str "boltons.formatutils.construct_format_field_str"): Assists in programmatic construction of format strings.
> 
> *   [`infer_positional_format_args()`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.infer_positional_format_args "boltons.formatutils.infer_positional_format_args"): Converts anonymous references in 2.7+ format strings to explicit positional arguments suitable for usage with Python 2.6.

_class_ boltons.formatutils.BaseFormatField(_fname_, _fspec=''_, _conv=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/formatutils.html#BaseFormatField)[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.BaseFormatField "Link to this definition")
A class representing a reference to an argument inside of a bracket-style format string. For instance, in 
```
"{greeting},
world!"
```
, there is a field named “greeting”.

These fields can have many options applied to them. See the Python docs on [Format String Syntax](https://docs.python.org/2/library/string.html#string-formatting) for the full details.

_property_ fstr[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.BaseFormatField.fstr "Link to this definition")
The current state of the field in string format.

set_conv(_conv_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/formatutils.html#BaseFormatField.set_conv)[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.BaseFormatField.set_conv "Link to this definition")
There are only two built-in converters: `s` and `r`. They are somewhat rare and appearlike `"{ref!r}"`.

set_fname(_fname_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/formatutils.html#BaseFormatField.set_fname)[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.BaseFormatField.set_fname "Link to this definition")
Set the field name.

set_fspec(_fspec_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/formatutils.html#BaseFormatField.set_fspec)[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.BaseFormatField.set_fspec "Link to this definition")
Set the field spec.

_class_ boltons.formatutils.DeferredValue(_func_, _cache\_value=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/formatutils.html#DeferredValue)[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.DeferredValue "Link to this definition")
[`DeferredValue`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.DeferredValue "boltons.formatutils.DeferredValue") is a wrapper type, used to defer computing values which would otherwise be expensive to stringify and format. This is most valuable in areas like logging, where one would not want to waste time formatting a value for a log message which will subsequently be filtered because the message’s log level was DEBUG and the logger was set to only emit CRITICAL messages.

The :class:`DeferredValue` is initialized with a callable that takes no arguments and returns the value, which can be of any type. By default DeferredValue only calls that callable once, and future references will get a cached value. This behavior can be disabled by setting _cache\_value_ to `False`.

Parameters:
*   **func** (_function_) – A callable that takes no arguments and computes the value being represented.

*   **cache_value** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether subsequent usages will call _func_ again. Defaults to `True`.

>>> import sys
>>> dv = DeferredValue(lambda: len(sys._current_frames()))
>>> output = "works great in all {0} threads!".format(dv)

PROTIP: To keep lines shorter, use: 
```
from formatutils import
DeferredValue as DV
```

get_value()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/formatutils.html#DeferredValue.get_value)[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.DeferredValue.get_value "Link to this definition")
Computes, optionally caches, and returns the value of the _func_. If `get_value()` has been called before, a cached value may be returned depending on the _cache\_value_ option passed to the constructor.

boltons.formatutils.construct_format_field_str(_fname_, _fspec_, _conv_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/formatutils.html#construct_format_field_str)[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.construct_format_field_str "Link to this definition")
Constructs a format field string from the field name, spec, and conversion character (`fname`, `fspec`, `conv`). See Python String Formatting for more info.

boltons.formatutils.get_format_args(_fstr_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/formatutils.html#get_format_args)[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.get_format_args "Link to this definition")
Turn a format string into two lists of arguments referenced by the format string. One is positional arguments, and the other is named arguments. Each element of the list includes the name and the nominal type of the field.

# >>> get_format_args(“{noun} is {1:d} years old{punct}”) # ([(1, <type ‘int’>)], [(‘noun’, <type ‘str’>), (‘punct’, <type ‘str’>)])

# XXX: Py3k >>> get_format_args(“{noun} is {1:d} years old{punct}”) == ([(1, int)], [(‘noun’, str), (‘punct’, str)]) True

boltons.formatutils.infer_positional_format_args(_fstr_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/formatutils.html#infer_positional_format_args)[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.infer_positional_format_args "Link to this definition")
Takes format strings with anonymous positional arguments, (e.g., “{}” and {:d}), and converts them into numbered ones for explicitness and compatibility with 2.6.

Returns a string with the inferred positional arguments.

boltons.formatutils.tokenize_format_str(_fstr_, _resolve\_pos=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/formatutils.html#tokenize_format_str)[](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.tokenize_format_str "Link to this definition")
Takes a format string, turns it into a list of alternating string literals and [`BaseFormatField`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.BaseFormatField "boltons.formatutils.BaseFormatField") tokens. By default, also infers anonymous positional references into explicit, numbered positional references. To disable this behavior set _resolve\_pos_ to `False`.

# Source: https://docs.pyinvoke.org/en/stable/api/parser.html

Title: parser — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/parser.html

Markdown Content:
The command-line parsing framework is split up into a handful of sub-modules:

*   `parser.argument`

*   `parser.context` (not to be confused with the top level `context`!)

*   `parser.parser`

API docs for all are below.

_class_ invoke.parser.parser.ParseResult(_*args:Any_, _**kwargs:Any_)[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.ParseResult "Permalink to this definition")
List-like object with some extra parse-related attributes.

Specifically, a `.remainder` attribute, which is the string found after a `--` in any parsed argv list; and an `.unparsed` attribute, a list of tokens that were unable to be parsed.

New in version 1.0.

 __init__ (_*args:Any_, _**kwargs:Any_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.ParseResult.__init__ "Permalink to this definition") __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.ParseResult.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_class_ invoke.parser.parser.Parser(_contexts:Iterable[ParserContext]=()_, _initial:Optional[ParserContext]=None_, _ignore\_unknown:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_)[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.Parser "Permalink to this definition")
Create parser conscious of `contexts` and optional `initial` context.

`contexts` should be an iterable of `Context` instances which will be searched when new context names are encountered during a parse. These Contexts determine what flags may follow them, as well as whether given flags take values.

`initial` is optional and will be used to determine validity of “core” options/flags at the start of the parse run, if any are encountered.

`ignore_unknown` determines what to do when contexts are found which do not map to any members of `contexts`. By default it is `False`, meaning any unknown contexts result in a parse error exception. If `True`, encountering an unknown context halts parsing and populates the return value’s `.unparsed` attribute with the remaining parse tokens.

New in version 1.0.

 __init__ (_contexts:Iterable[ParserContext]=()_, _initial:Optional[ParserContext]=None_, _ignore\_unknown:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.Parser.__init__ "Permalink to this definition")parse_argv(_argv:List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]_)→[invoke.parser.parser.ParseResult](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.ParseResult "invoke.parser.parser.ParseResult")[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.Parser.parse_argv "Permalink to this definition")
Parse an argv-style token list `argv`.

Returns a list (actually a subclass, [`ParseResult`](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.ParseResult "invoke.parser.parser.ParseResult")) of [`ParserContext`](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext "invoke.parser.context.ParserContext") objects matching the order they were found in the `argv` and containing [`Argument`](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument "invoke.parser.argument.Argument") objects with updated values based on any flags given.

Assumes any program name has already been stripped out. Good:

Parser(...).parse_argv(['--core-opt', 'task', '--task-opt'])

Bad:

Parser(...).parse_argv(['invoke', '--core-opt', ...])

Parameters
**argv** – List of argument string tokens.

Returns
A [`ParseResult`](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.ParseResult "invoke.parser.parser.ParseResult") (a `list` subclass containing some number of [`ParserContext`](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext "invoke.parser.context.ParserContext") objects).

New in version 1.0.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.Parser.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_class_ invoke.parser.context.ParserContext(_name:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _aliases:Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=()_, _args:Iterable[[invoke.parser.argument.Argument](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument "invoke.parser.argument.Argument")]=()_)[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext "Permalink to this definition")
Parsing context with knowledge of flags & their format.

Generally associated with the core program or a task.

When run through a parser, will also hold runtime values filled in by the parser.

New in version 1.0.

 __init__ (_name:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _aliases:Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=()_, _args:Iterable[[invoke.parser.argument.Argument](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument "invoke.parser.argument.Argument")]=()_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext.__init__ "Permalink to this definition")
Create a new `ParserContext` named `name`, with `aliases`.

`name` is optional, and should be a string if given. It’s used to tell ParserContext objects apart, and for use in a Parser when determining what chunk of input might belong to a given ParserContext.

`aliases` is also optional and should be an iterable containing strings. Parsing will honor any aliases when trying to “find” a given context in its input.

May give one or more `args`, which is a quick alternative to calling `for arg in args: self.add_arg(arg)` after initialization.

 __repr__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext.__repr__ "Permalink to this definition")
Return repr(self).

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

add_arg(_*args:Any_, _**kwargs:Any_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext.add_arg "Permalink to this definition")
Adds given `Argument` (or constructor args for one) to this context.

The Argument in question is added to the following dict attributes:

*   `args`: “normal” access, i.e. the given names are directly exposed as keys.

*   `flags`: “flaglike” access, i.e. the given names are translated into CLI flags, e.g. `"foo"` is accessible via `flags['--foo']`.

*   `inverse_flags`: similar to `flags` but containing only the “inverse” versions of boolean flags which default to True. This allows the parser to track e.g. `--no-myflag` and turn it into a False value for the `myflag` Argument.

New in version 1.0.

_property_ as_kwargs _:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext.as_kwargs "Permalink to this definition")
This context’s arguments’ values keyed by their `.name` attribute.

Results in a dict suitable for use in Python contexts, where e.g. an arg named `foo-bar` becomes accessible as `foo_bar`.

New in version 1.0.

flag_names()→Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),...][¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext.flag_names "Permalink to this definition")
Similar to [`help_tuples`](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext.help_tuples "invoke.parser.context.ParserContext.help_tuples") but returns flag names only, no helpstrs.

Specifically, all flag names, flattened, in rough order.

New in version 1.0.

help_for(_flag:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext.help_for "Permalink to this definition")
Return 2-tuple of `(flag-spec, help-string)` for given `flag`.

New in version 1.0.

help_tuples()→List[Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]][¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext.help_tuples "Permalink to this definition")
Return sorted iterable of help tuples for all member Arguments.

Sorts like so:

*   General sort is alphanumerically

*   Short flags win over long flags

*   Arguments with _only_ long flags and _no_ short flags will come first.

*   When an Argument has multiple long or short flags, it will sort using the most favorable (lowest alphabetically) candidate.

This will result in a help list like so:

--alpha, --zeta # 'alpha' wins
--beta
-a, --query # short flag wins
-b, --argh
-c

New in version 1.0.

invoke.parser.context.flag_key(_arg:[invoke.parser.argument.Argument](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument "invoke.parser.argument.Argument")_)→List[Union[[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)"),[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]][¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.flag_key "Permalink to this definition")
Obtain useful key list-of-ints for sorting CLI flags.

New in version 1.0.

_class_ invoke.parser.argument.Argument(_name:Optional[str]=None_, _names:Iterable[str]=()_, _kind:Any=<class'str'>_, _default:Optional[Any]=None_, _help:Optional[str]=None_, _positional:bool=False_, _optional:bool=False_, _incrementable:bool=False_, _attr\_name:Optional[str]=None_)[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument "Permalink to this definition")
A command-line argument/flag.

Parameters
*   **name** – Syntactic sugar for `names=[<name>]`. Giving both `name` and `names` is invalid.

*   **names** – List of valid identifiers for this argument. For example, a “help” argument may be defined with a name list of `['-h', '--help']`.

*   **kind** – Type factory & parser hint. E.g. `int` will turn the default text value parsed, into a Python integer; and `bool` will tell the parser not to expect an actual value but to treat the argument as a toggle/flag.

*   **default** – Default value made available to the parser if no value is given on the command line.

*   **help** – Help text, intended for use with `--help`.

*   **positional** – Whether or not this argument’s value may be given positionally. When `False` (default) arguments must be explicitly named.

*   **optional** – Whether or not this (non-`bool`) argument requires a value.

*   **incrementable** – Whether or not this (`int`) argument is to be incremented instead of overwritten/assigned to.

*   **attr_name** – A Python identifier/attribute friendly name, typically filled in with the underscored version when `name`/`names` contain dashes.

New in version 1.0.

 __init__ (_name:Optional[str]=None_, _names:Iterable[str]=()_, _kind:Any=<class'str'>_, _default:Optional[Any]=None_, _help:Optional[str]=None_, _positional:bool=False_, _optional:bool=False_, _incrementable:bool=False_, _attr\_name:Optional[str]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument.__init__ "Permalink to this definition") __repr__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument.__repr__ "Permalink to this definition")
Return repr(self).

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_property_ got_value _:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument.got_value "Permalink to this definition")
Returns whether the argument was ever given a (non-default) value.

For most argument kinds, this simply checks whether the internally stored value is non-`None`; for others, such as `list` kinds, different checks may be used.

New in version 1.3.

_property_ name _:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]_[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument.name "Permalink to this definition")
The canonical attribute-friendly name for this argument.

Will be `attr_name` (if given to constructor) or the first name in `names` otherwise.

New in version 1.0.

set_value(_value:Any_, _cast:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument.set_value "Permalink to this definition")
Actual explicit value-setting API call.

Sets `self.raw_value` to `value` directly.

Sets `self.value` to `self.kind(value)`, unless:

*   `cast=False`, in which case the raw value is also used.

*   `self.kind==list`, in which case the value is appended to `self.value` instead of cast & overwritten.

*   `self.incrementable==True`, in which case the value is ignored and the current (assumed int) value is simply incremented.

New in version 1.0.

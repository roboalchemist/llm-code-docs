# Source: https://boltons.readthedocs.io/en/latest/funcutils.html

Title: functools fixes — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/funcutils.html

Markdown Content:
`funcutils` - `functools` fixes[](https://boltons.readthedocs.io/en/latest/funcutils.html#module-boltons.funcutils "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

Python’s built-in [`functools`](https://docs.python.org/3/library/functools.html#module-functools "(in Python v3.14)") module builds several useful utilities on top of Python’s first-class function support. `funcutils` generally stays in the same vein, adding to and correcting Python’s standard metaprogramming facilities.

Sections

*   [Decoration](https://boltons.readthedocs.io/en/latest/funcutils.html#decoration)

*   [Function construction](https://boltons.readthedocs.io/en/latest/funcutils.html#function-construction)

*   [Improved `partial`](https://boltons.readthedocs.io/en/latest/funcutils.html#improved-partial)

*   [Miscellaneous metaprogramming](https://boltons.readthedocs.io/en/latest/funcutils.html#miscellaneous-metaprogramming)

[Decoration](https://boltons.readthedocs.io/en/latest/funcutils.html#id1)[](https://boltons.readthedocs.io/en/latest/funcutils.html#decoration "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Decorators](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators) are among Python’s most elegant and succinct language features, and boltons adds one special function to make them even more powerful.

boltons.funcutils.wraps(_func_, _injected=None_, _expected=None_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#wraps)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.wraps "Link to this definition")
Decorator factory to apply update_wrapper() to a wrapper function.

Modeled after built-in [`functools.wraps()`](https://docs.python.org/3/library/functools.html#functools.wraps "(in Python v3.14)"). Returns a decorator that invokes update_wrapper() with the decorated function as the wrapper argument and the arguments to wraps() as the remaining arguments. Default arguments are as for update_wrapper(). This is a convenience function to simplify applying partial() to update_wrapper().

Same example as in update_wrapper’s doc but with wraps:

>>> from boltons.funcutils import wraps
>>>
>>> def print_return(func):
...     @wraps(func)
...     def wrapper(*args, **kwargs):
...         ret = func(*args, **kwargs)
...         print(ret)
...         return ret
...     return wrapper
...
>>> @print_return
... def example():
...  '''docstring'''
...     return 'example return value'
>>>
>>> val = example()
example return value
>>> example. __name__ 
'example'
>>> example. __doc__ 
'docstring'

[Function construction](https://boltons.readthedocs.io/en/latest/funcutils.html#id2)[](https://boltons.readthedocs.io/en/latest/funcutils.html#function-construction "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Functions are so key to programming in Python that there will even arise times where Python functions must be constructed in Python. Thankfully, Python is a dynamic enough to make this possible. Boltons makes it easy.

_class_ boltons.funcutils.FunctionBuilder(_name_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#FunctionBuilder)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.FunctionBuilder "Link to this definition")
The FunctionBuilder type provides an interface for programmatically creating new functions, either based on existing functions or from scratch.

Values are passed in at construction or set as attributes on the instance. For creating a new function based of an existing one, see the [`from_func()`](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.FunctionBuilder.from_func "boltons.funcutils.FunctionBuilder.from_func") classmethod. At any point, [`get_func()`](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.FunctionBuilder.get_func "boltons.funcutils.FunctionBuilder.get_func") can be called to get a newly compiled function, based on the values configured.

>>> fb = FunctionBuilder('return_five', doc='returns the integer 5',
...                      body='return 5')
>>> f = fb.get_func()
>>> f()
5
>>> fb.varkw = 'kw'
>>> f_kw = fb.get_func()
>>> f_kw(ignored_arg='ignored_val')
5

Note that function signatures themselves changed quite a bit in Python 3, so several arguments are only applicable to FunctionBuilder in Python 3. Except for _name_, all arguments to the constructor are keyword arguments.

Parameters:
*   **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Name of the function.

*   **doc** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – [Docstring](https://en.wikipedia.org/wiki/Docstring#Python) for the function, defaults to empty.

*   **module** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Name of the module from which this function was imported. Defaults to None.

*   **body** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – String version of the code representing the body of the function. Defaults to `'pass'`, which will result in a function which does nothing and returns `None`.

*   **args** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – List of argument names, defaults to empty list, denoting no arguments.

*   **varargs** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Name of the catch-all variable for positional arguments. E.g., “args” if the resultant function is to have `*args` in the signature. Defaults to None.

*   **varkw** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Name of the catch-all variable for keyword arguments. E.g., “kwargs” if the resultant function is to have `**kwargs` in the signature. Defaults to None.

*   **defaults** ([_tuple_](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")) – A tuple containing default argument values for those arguments that have defaults.

*   **kwonlyargs** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – Argument names which are only valid as keyword arguments. **Python 3 only.**

*   **kwonlydefaults** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A mapping, same as normal _defaults_, but only for the _kwonlyargs_. **Python 3 only.**

*   **annotations** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – Mapping of type hints and so forth. **Python 3 only.**

*   **filename** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The filename that will appear in tracebacks. Defaults to “boltons.funcutils.FunctionBuilder”.

*   **indent** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Number of spaces with which to indent the function _body_. Values less than 1 will result in an error.

*   **dict** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – Any other attributes which should be added to the functions compiled with this FunctionBuilder.

All of these arguments are also made available as attributes which can be mutated as necessary.

add_arg(_arg\_name_, _default=NO\_DEFAULT_, _kwonly=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#FunctionBuilder.add_arg)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.FunctionBuilder.add_arg "Link to this definition")
Add an argument with optional _default_ (defaults to `funcutils.NO_DEFAULT`). Pass _kwonly=True_ to add a keyword-only argument

_classmethod_ from_func(_func_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#FunctionBuilder.from_func)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.FunctionBuilder.from_func "Link to this definition")
Create a new FunctionBuilder instance based on an existing function. The original function will not be stored or modified.

get_defaults_dict()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#FunctionBuilder.get_defaults_dict)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.FunctionBuilder.get_defaults_dict "Link to this definition")
Get a dictionary of function arguments with defaults and the respective values.

get_func(_execdict=None_, _add\_source=True_, _with\_dict=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#FunctionBuilder.get_func)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.FunctionBuilder.get_func "Link to this definition")
Compile and return a new function based on the current values of the FunctionBuilder.

Parameters:
*   **execdict** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – The dictionary representing the scope in which the compilation should take place. Defaults to an empty dict.

*   **add_source** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to add the source used to a special `__source__` attribute on the resulting function. Defaults to True.

*   **with_dict** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Add any custom attributes, if applicable. Defaults to True.

To see an example of usage, see the implementation of [`wraps()`](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.wraps "boltons.funcutils.wraps").

get_sig_str(_with\_annotations=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#FunctionBuilder.get_sig_str)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.FunctionBuilder.get_sig_str "Link to this definition")
Return function signature as a string.

with_annotations is ignored on Python 2. On Python 3 signature will omit annotations if it is set to False.

remove_arg(_arg\_name_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#FunctionBuilder.remove_arg)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.FunctionBuilder.remove_arg "Link to this definition")
Remove an argument from this FunctionBuilder’s argument list. The resulting function will have one less argument per call to this function.

Parameters:
**arg_name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the argument to remove.

Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") if the argument is not present.

[Improved `partial`](https://boltons.readthedocs.io/en/latest/funcutils.html#id3)[](https://boltons.readthedocs.io/en/latest/funcutils.html#improved-partial "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

boltons.funcutils.partial[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.partial "Link to this definition")
alias of [`CachedInstancePartial`](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.CachedInstancePartial "boltons.funcutils.CachedInstancePartial")

_class_ boltons.funcutils.InstancePartial[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#InstancePartial)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.InstancePartial "Link to this definition")
`functools.partial` is a huge convenience for anyone working with Python’s great first-class functions. It allows developers to curry arguments and incrementally create simpler callables for a variety of use cases.

Unfortunately there’s one big gap in its usefulness: methods. Partials just don’t get bound as methods and automatically handed a reference to `self`. The `InstancePartial` type remedies this by inheriting from `functools.partial` and implementing the necessary descriptor protocol. There are no other differences in implementation or usage. [`CachedInstancePartial`](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.CachedInstancePartial "boltons.funcutils.CachedInstancePartial"), below, has the same ability, but is slightly more efficient.

_class_ boltons.funcutils.CachedInstancePartial[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#CachedInstancePartial)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.CachedInstancePartial "Link to this definition")
The `CachedInstancePartial` is virtually the same as [`InstancePartial`](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.InstancePartial "boltons.funcutils.InstancePartial"), adding support for method-usage to `functools.partial`, except that upon first access, it caches the bound method on the associated object, speeding it up for future accesses, and bringing the method call overhead to about the same as non-`partial` methods.

See the [`InstancePartial`](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.InstancePartial "boltons.funcutils.InstancePartial") docstring for more details.

[Miscellaneous metaprogramming](https://boltons.readthedocs.io/en/latest/funcutils.html#id4)[](https://boltons.readthedocs.io/en/latest/funcutils.html#miscellaneous-metaprogramming "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

boltons.funcutils.copy_function(_orig_, _copy\_dict=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#copy_function)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.copy_function "Link to this definition")
Returns a shallow copy of the function, including code object, globals, closure, etc.

>>> func = lambda: func
>>> func() is func
True
>>> func_copy = copy_function(func)
>>> func_copy() is func
True
>>> func_copy is not func
True

Parameters:
*   **orig** (_function_) – The function to be copied. Must be a function, not just any method or callable.

*   **copy_dict** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Also copy any attributes set on the function instance. Defaults to `True`.

boltons.funcutils.dir_dict(_obj_, _raise\_exc=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#dir_dict)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.dir_dict "Link to this definition")
Return a dictionary of attribute names to values for a given object. Unlike `obj.__dict__`, this function returns all attributes on the object, including ones on parent classes.

boltons.funcutils.mro_items(_type\_obj_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#mro_items)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.mro_items "Link to this definition")
Takes a type and returns an iterator over all class variables throughout the type hierarchy (respecting the MRO).

>>> sorted(set([k for k, v in mro_items(int) if not k.startswith('__') and 'bytes' not in k and not callable(v)]))
['denominator', 'imag', 'numerator', 'real']

boltons.funcutils.format_invocation(_name=''_, _args=()_, _kwargs=None_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#format_invocation)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.format_invocation "Link to this definition")
Given a name, positional arguments, and keyword arguments, format a basic Python-style function call.

>>> print(format_invocation('func', args=(1, 2), kwargs={'c': 3}))
func(1, 2, c=3)
>>> print(format_invocation('a_func', args=(1,)))
a_func(1)
>>> print(format_invocation('kw_func', kwargs=[('a', 1), ('b', 2)]))
kw_func(a=1, b=2)

boltons.funcutils.format_exp_repr(_obj_, _pos\_names_, _req\_names=None_, _opt\_names=None_, _opt\_key=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#format_exp_repr)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.format_exp_repr "Link to this definition")
Render an expression-style repr of an object, based on attribute names, which are assumed to line up with arguments to an initializer.

>>> class Flag(object):
...    def  __init__ (self, length, width, depth=None):
...        self.length = length
...        self.width = width
...        self.depth = depth
...

That’s our Flag object, here are some example reprs for it:

>>> flag = Flag(5, 10)
>>> print(format_exp_repr(flag, ['length', 'width'], [], ['depth']))
Flag(5, 10)
>>> flag2 = Flag(5, 15, 2)
>>> print(format_exp_repr(flag2, ['length'], ['width', 'depth']))
Flag(5, width=15, depth=2)

By picking the pos_names, req_names, opt_names, and opt_key, you can fine-tune how you want the repr to look.

Parameters:
*   **obj** ([_object_](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")) – The object whose type name will be used and attributes will be checked

*   **pos_names** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – Required list of attribute names which will be rendered as positional arguments in the output repr.

*   **req_names** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – List of attribute names which will always appear in the keyword arguments in the output repr. Defaults to None.

*   **opt_names** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – List of attribute names which may appear in the keyword arguments in the output repr, provided they pass the _opt\_key_ check. Defaults to None.

*   **opt_key** (_callable_) – A function or callable which checks whether an opt_name should be in the repr. Defaults to a `None`-check.

boltons.funcutils.format_nonexp_repr(_obj_, _req\_names=None_, _opt\_names=None_, _opt\_key=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/funcutils.html#format_nonexp_repr)[](https://boltons.readthedocs.io/en/latest/funcutils.html#boltons.funcutils.format_nonexp_repr "Link to this definition")
Format a non-expression-style repr

Some object reprs look like object instantiation, e.g., App(r=[], mw=[]).

This makes sense for smaller, lower-level objects whose state roundtrips. But a lot of objects contain values that don’t roundtrip, like types and functions.

For those objects, there is the non-expression style repr, which mimic’s Python’s default style to make a repr like so:

>>> class Flag(object):
...    def  __init__ (self, length, width, depth=None):
...        self.length = length
...        self.width = width
...        self.depth = depth
...
>>> flag = Flag(5, 10)
>>> print(format_nonexp_repr(flag, ['length', 'width'], ['depth']))
<Flag length=5 width=10>

If no attributes are specified or set, utilizes the id, not unlike Python’s built-in behavior.

>>> print(format_nonexp_repr(flag))
<Flag id=...>

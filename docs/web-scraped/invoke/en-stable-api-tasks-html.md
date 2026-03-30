# Source: https://docs.pyinvoke.org/en/stable/api/tasks.html

Title: tasks — Invoke  documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/tasks.html

Published Time: Sat, 11 Oct 2025 00:42:26 GMT

Markdown Content:
tasks — Invoke documentation
===============

`tasks`[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#module-invoke.tasks "Permalink to this headline")
===============================================================================================================

This module contains the core [`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task") class & convenience decorators used to generate new tasks.

_class_ invoke.tasks.Call(_task:[invoke.tasks.Task](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task")_, _called\_as:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _args:Optional[Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),...]]=None_, _kwargs:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_)[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "Permalink to this definition")
Represents a call/execution of a [`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task") with given (kw)args.

Similar to [`partial`](https://docs.python.org/2.7/library/functools.html#functools.partial "(in Python v2.7)") with some added functionality (such as the delegation to the inner task, and optional tracking of the name it’s being called by.)

New in version 1.0.

 __eq__ (_other:[object](https://docs.python.org/2.7/library/functions.html#object "(in Python v2.7)")_)→[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call.__eq__ "Permalink to this definition")
Return self==value.

 __hash__ _=None_[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call.__hash__ "Permalink to this definition") __init__ (_task:[invoke.tasks.Task](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task")_, _called\_as:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _args:Optional[Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),...]]=None_, _kwargs:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call.__init__ "Permalink to this definition")
Create a new [`Call`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call") object.

Parameters
*   **task** – The [`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task") object to be executed.

*   **called_as** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – The name the task is being called as, e.g. if it was called by an alias or other rebinding. Defaults to `None`, aka, the task was referred to by its default name.

*   **args** (_tuple_) – Positional arguments to call with, if any. Default: `None`.

*   **kwargs** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) – Keyword arguments to call with, if any. Default: `None`.

 __repr__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call.__repr__ "Permalink to this definition")
Return repr(self).

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

clone(_into:Optional[Type[[invoke.tasks.Call](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call")]]=None_, _with\_:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_)→[invoke.tasks.Call](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call")[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call.clone "Permalink to this definition")
Return a standalone copy of this Call.

Useful when parameterizing task executions.

Parameters
*   **into** – A subclass to generate instead of the current class. Optional.

*   **with** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) –

A dict of additional keyword arguments to use when creating the new clone; typically used when cloning `into` a subclass that has extra args on top of the base class. Optional.

Note

This dict is used to `.update()` the original object’s data (the return value from its [`clone_data`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call.clone_data "invoke.tasks.Call.clone_data")), so in the event of a conflict, values in `with_` will win out. 

New in version 1.0.

Changed in version 1.1: Added the `with_` kwarg.

clone_data()→Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any][¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call.clone_data "Permalink to this definition")
Return keyword args suitable for cloning this call into another.

New in version 1.1.

make_context(_config:Config_)→[invoke.context.Context](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context")[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call.make_context "Permalink to this definition")
Generate a [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") appropriate for this call, with given config.

New in version 1.0.

_class_ invoke.tasks.Task(_body:Callable_, _name:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _aliases:Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=()_, _positional:Optional[Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]=None_, _optional:Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=()_, _default:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_, _auto\_shortflags:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_, _help:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_, _pre:Optional[Union[List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")],[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]=None_, _post:Optional[Union[List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")],[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]=None_, _autoprint:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_, _iterable:Optional[Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]=None_, _incrementable:Optional[Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]=None_)[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "Permalink to this definition")
Core object representing an executable task & its argument specification.

For the most part, this object is a clearinghouse for all of the data that may be supplied to the [`@task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.task "invoke.tasks.task") decorator, such as `name`, `aliases`, `positional` etc, which appear as attributes.

In addition, instantiation copies some introspection/documentation friendly metadata off of the supplied `body` object, such as `__doc__`, `__name__` and `__module__`, allowing it to “appear as” `body` for most intents and purposes.

New in version 1.0.

 __call__ (_*args:Any_, _**kwargs:Any_)→invoke.tasks.T[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task.__call__ "Permalink to this definition")
Call self as a function.

 __eq__ (_other:[object](https://docs.python.org/2.7/library/functions.html#object "(in Python v2.7)")_)→[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task.__eq__ "Permalink to this definition")
Return self==value.

 __hash__ ()→[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task.__hash__ "Permalink to this definition")
Return hash(self).

 __init__ (_body:Callable_, _name:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _aliases:Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=()_, _positional:Optional[Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]=None_, _optional:Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=()_, _default:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_, _auto\_shortflags:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_, _help:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_, _pre:Optional[Union[List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")],[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]=None_, _post:Optional[Union[List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")],[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]=None_, _autoprint:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_, _iterable:Optional[Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]=None_, _incrementable:Optional[Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task.__init__ "Permalink to this definition") __repr__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task.__repr__ "Permalink to this definition")
Return repr(self).

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

argspec(_body:Callable_)→Signature[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task.argspec "Permalink to this definition")
Returns a modified `inspect.Signature` based on that of `body`.

Returns
an `inspect.Signature` matching that of `body`, but with the initial context argument removed.

Raises
**TypeError** – if the task lacks an initial positional [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") argument.

New in version 1.0.

Changed in version 2.0: Changed from returning a two-tuple of `(arg_names, spec_dict)` to returning an `inspect.Signature`.

get_arguments(_ignore\_unknown\_help:Optional[[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")]=None_)→List[[invoke.parser.argument.Argument](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.argument.Argument "invoke.parser.argument.Argument")][¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task.get_arguments "Permalink to this definition")
Return a list of Argument objects representing this task’s signature.

Parameters
**ignore_unknown_help** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Controls whether unknown help flags cause errors. See the config option by the same name for details.

New in version 1.0.

Changed in version 1.7: Added the `ignore_unknown_help` kwarg.

invoke.tasks.call(_task:[invoke.tasks.Task](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task")_, _*args:Any_, _**kwargs:Any_)→[invoke.tasks.Call](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call")[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.call "Permalink to this definition")
Describes execution of a [`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task"), typically with pre-supplied arguments.

Useful for setting up [pre/post task invocations](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html#parameterizing-pre-post-tasks). It’s actually just a convenient wrapper around the [`Call`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call") class, which may be used directly instead if desired.

For example, here’s two build-like tasks that both refer to a `setup` pre-task, one with no baked-in argument values (and thus no need to use [`call`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.call "invoke.tasks.call")), and one that toggles a boolean flag:

@task
def setup(c, clean=False):
    if clean:
        c.run("rm -rf target")
    # ... setup things here ...
    c.run("tar czvf target.tgz target")

@task(pre=[setup])
def build(c):
    c.run("build, accounting for leftover files...")

@task(pre=[call(setup, clean=True)])
def clean_build(c):
    c.run("build, assuming clean slate...")

Please see the constructor docs for [`Call`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call") for details - this function’s `args` and `kwargs` map directly to the same arguments as in that method.

New in version 1.0.

invoke.tasks.task(_*args:Any_, _**kwargs:Any_)→Callable[¶](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.task "Permalink to this definition")
Marks wrapped callable object as a valid Invoke task.

May be called without any parentheses if no extra options need to be specified. Otherwise, the following keyword arguments are allowed in the parenthese’d form:

*   `name`: Default name to use when binding to a [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection"). Useful for avoiding Python namespace issues (i.e. when the desired CLI level name can’t or shouldn’t be used as the Python level name.)

*   `aliases`: Specify one or more aliases for this task, allowing it to be invoked as multiple different names. For example, a task named `mytask` with a simple `@task` wrapper may only be invoked as `"mytask"`. Changing the decorator to be `@task(aliases=['myothertask'])` allows invocation as `"mytask"`_or_`"myothertask"`.

*   `positional`: Iterable overriding the parser’s automatic “args with no default value are considered positional” behavior. If a list of arg names, no args besides those named in this iterable will be considered positional. (This means that an empty list will force all arguments to be given as explicit flags.)

*   `optional`: Iterable of argument names, declaring those args to have [optional values](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html#optional-values). Such arguments may be given as value-taking options (e.g. `--my-arg=myvalue`, wherein the task is given `"myvalue"`) or as Boolean flags (`--my-arg`, resulting in `True`).

*   `iterable`: Iterable of argument names, declaring them to [build iterable values](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html#iterable-flag-values).

*   `incrementable`: Iterable of argument names, declaring them to [increment their values](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html#incrementable-flag-values).

*   `default`: Boolean option specifying whether this task should be its collection’s default task (i.e. called if the collection’s own name is given.)

*   `auto_shortflags`: Whether or not to automatically create short flags from task options; defaults to True.

*   `help`: Dict mapping argument names to their help strings. Will be displayed in `--help` output. For arguments containing underscores (which are transformed into dashes on the CLI by default), either the dashed or underscored version may be supplied here.

*   `pre`, `post`: Lists of task objects to execute prior to, or after, the wrapped task whenever it is executed.

*   `autoprint`: Boolean determining whether to automatically print this task’s return value to standard output when invoked directly via the CLI. Defaults to False.

*   `klass`: Class to instantiate/return. Defaults to [`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task").

If any non-keyword arguments are given, they are taken as the value of the `pre` kwarg for convenience’s sake. (It is an error to give both `*args` and `pre` at the same time.)

New in version 1.0.

Changed in version 1.1: Added the `klass` keyword argument.

[Invoke](https://docs.pyinvoke.org/en/stable/index.html)
========================================================

Pythonic task execution

### Navigation

*   [Getting started](https://docs.pyinvoke.org/en/stable/getting-started.html)

*   [`inv[oke]` core usage](https://docs.pyinvoke.org/en/stable/invoke.html)

*   [Configuration](https://docs.pyinvoke.org/en/stable/concepts/configuration.html)
*   [Invoking tasks](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html)
*   [Using Invoke as a library](https://docs.pyinvoke.org/en/stable/concepts/library.html)
*   [Loading collections](https://docs.pyinvoke.org/en/stable/concepts/loading.html)
*   [Constructing namespaces](https://docs.pyinvoke.org/en/stable/concepts/namespaces.html)
*   [Testing Invoke-using codebases](https://docs.pyinvoke.org/en/stable/concepts/testing.html)
*   [Automatically responding to program output](https://docs.pyinvoke.org/en/stable/concepts/watchers.html)

*   [`__init__`](https://docs.pyinvoke.org/en/stable/api/__init__.html)
*   [`collection`](https://docs.pyinvoke.org/en/stable/api/collection.html)
*   [`config`](https://docs.pyinvoke.org/en/stable/api/config.html)
*   [`context`](https://docs.pyinvoke.org/en/stable/api/context.html)
*   [`exceptions`](https://docs.pyinvoke.org/en/stable/api/exceptions.html)
*   [`executor`](https://docs.pyinvoke.org/en/stable/api/executor.html)
*   [`loader`](https://docs.pyinvoke.org/en/stable/api/loader.html)
*   [`parser`](https://docs.pyinvoke.org/en/stable/api/parser.html)
*   [`program`](https://docs.pyinvoke.org/en/stable/api/program.html)
*   [`runners`](https://docs.pyinvoke.org/en/stable/api/runners.html)
*   [`tasks`](https://docs.pyinvoke.org/en/stable/api/tasks.html#)
*   [`terminals`](https://docs.pyinvoke.org/en/stable/api/terminals.html)
*   [`util`](https://docs.pyinvoke.org/en/stable/api/util.html)
*   [`watchers`](https://docs.pyinvoke.org/en/stable/api/watchers.html)

* * *

*   [Main website](https://www.pyinvoke.org/)

### Quick search

### Donate/support

Professionally-supported Invoke is available with the [Tidelift Subscription](https://tidelift.com/subscription/pkg/pypi-invoke?utm_source=pypi-invoke&utm_medium=referral&utm_campaign=docs).

 ©2025 Jeff Forcier. | Powered by [Sphinx 4.3.2](http://sphinx-doc.org/)&[Alabaster 0.7.12](https://github.com/bitprophet/alabaster) | [Page source](https://docs.pyinvoke.org/en/stable/_sources/api/tasks.rst.txt)

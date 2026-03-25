# Source: https://docs.pyinvoke.org/en/stable/api/executor.html

Title: executor — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/executor.html

Markdown Content:
_class_ invoke.executor.Executor(_collection:Collection_, _config:Optional[Config]=None_, _core:Optional[ParseResult]=None_)[¶](https://docs.pyinvoke.org/en/stable/api/executor.html#invoke.executor.Executor "Permalink to this definition")
An execution strategy for Task objects.

Subclasses may override various extension points to change, add or remove behavior.

New in version 1.0.

 __init__ (_collection:Collection_, _config:Optional[Config]=None_, _core:Optional[ParseResult]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/executor.html#invoke.executor.Executor.__init__ "Permalink to this definition")
Initialize executor with handles to necessary data structures.

Parameters
*   **collection** – A [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection") used to look up requested tasks (and their default config data, if any) by name during execution.

*   **config** – An optional [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") holding configuration state. Defaults to an empty [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") if not given.

*   **core** – An optional [`ParseResult`](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.parser.ParseResult "invoke.parser.parser.ParseResult") holding parsed core program arguments. Defaults to `None`.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/executor.html#invoke.executor.Executor.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

dedupe(_calls:List[[invoke.tasks.Call](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call")]_)→List[[invoke.tasks.Call](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call")][¶](https://docs.pyinvoke.org/en/stable/api/executor.html#invoke.executor.Executor.dedupe "Permalink to this definition")
Deduplicate a list of [`tasks`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call").

Parameters
**calls** – An iterable of [`Call`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call") objects representing tasks.

Returns
A list of [`Call`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call") objects.

New in version 1.0.

execute(_*tasks:Union[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]],[invoke.parser.context.ParserContext](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext "invoke.parser.context.ParserContext")]_)→Dict[Task,Result][¶](https://docs.pyinvoke.org/en/stable/api/executor.html#invoke.executor.Executor.execute "Permalink to this definition")
Execute one or more `tasks` in sequence.

Parameters
**tasks** –

An all-purpose iterable of “tasks to execute”, each member of which may take one of the following forms:

**A string** naming a task from the Executor’s [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection"). This name may contain dotted syntax appropriate for calling namespaced tasks, e.g. `subcollection.taskname`. Such tasks are executed without arguments.

**A two-tuple** whose first element is a task name string (as above) and whose second element is a dict suitable for use as `**kwargs` when calling the named task. E.g.:

[
    ('task1', {}),
    ('task2', {'arg1': 'val1'}),
    ...
]

is equivalent, roughly, to:

task1()
task2(arg1='val1')

**A `.ParserContext`** instance, whose `.name` attribute is used as the task name and whose `.as_kwargs` attribute is used as the task kwargs (again following the above specifications).

Note

When called without any arguments at all (i.e. when `*tasks` is empty), the default task from `self.collection` is used instead, if defined.

Returns
A dict mapping task objects to their return values.

This dict may include pre- and post-tasks if any were executed. For example, in a collection with a `build` task depending on another task named `setup`, executing `build` will result in a dict with two keys, one for `build` and one for `setup`.

New in version 1.0.

expand_calls(_calls:List[[invoke.tasks.Call](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call")]_)→List[[invoke.tasks.Call](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call")][¶](https://docs.pyinvoke.org/en/stable/api/executor.html#invoke.executor.Executor.expand_calls "Permalink to this definition")
Expand a list of [`Call`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call") objects into a near-final list of same.

The default implementation of this method simply adds a task’s pre/post-task list before/after the task itself, as necessary.

Subclasses may wish to do other things in addition (or instead of) the above, such as multiplying the [`calls`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call") by argument vectors or similar.

New in version 1.0.

normalize(_tasks:Tuple[Union[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]],[invoke.parser.context.ParserContext](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext "invoke.parser.context.ParserContext")],...]_)→List[[invoke.tasks.Call](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call")][¶](https://docs.pyinvoke.org/en/stable/api/executor.html#invoke.executor.Executor.normalize "Permalink to this definition")
Transform arbitrary task list w/ various types, into [`Call`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Call "invoke.tasks.Call") objects.

See docstring for [`execute`](https://docs.pyinvoke.org/en/stable/api/executor.html#invoke.executor.Executor.execute "invoke.executor.Executor.execute") for details.

New in version 1.0.

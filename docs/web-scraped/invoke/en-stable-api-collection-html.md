# Source: https://docs.pyinvoke.org/en/stable/api/collection.html

Title: collection — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/collection.html

Markdown Content:
_class_ invoke.collection.Collection(_*args:Any_, _**kwargs:Any_)[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "Permalink to this definition")
A collection of executable tasks. See [Constructing namespaces](https://docs.pyinvoke.org/en/stable/concepts/namespaces.html).

New in version 1.0.

 __eq__ (_other:[object](https://docs.python.org/2.7/library/functions.html#object "(in Python v2.7)")_)→[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.__eq__ "Permalink to this definition")
Return self==value.

 __getitem__ (_name:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_)→Any[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.__getitem__ "Permalink to this definition")
Returns task named `name`. Honors aliases and subcollections.

If this collection has a default task, it is returned when `name` is empty or `None`. If empty input is given and no task has been selected as the default, ValueError will be raised.

Tasks within subcollections should be given in dotted form, e.g. ‘foo.bar’. Subcollection default tasks will be returned on the subcollection’s name.

New in version 1.0.

 __hash__ _=None_[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.__hash__ "Permalink to this definition") __repr__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.__repr__ "Permalink to this definition")
Return repr(self).

add_collection(_coll:[invoke.collection.Collection](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection")_, _name:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _default:Optional[[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.add_collection "Permalink to this definition")
Add [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection")`coll` as a sub-collection of this one.

Parameters
*   **coll** – The [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection") to add.

*   **name** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – The name to attach the collection as. Defaults to the collection’s own internal name.

*   **default** – Whether this sub-collection(‘s default task-or-collection) should be the default invocation of the parent collection.

New in version 1.0.

Changed in version 1.5: Added the `default` parameter.

add_task(_task:[invoke.tasks.Task](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task")_, _name:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _aliases:Optional[Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),...]]=None_, _default:Optional[[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.add_task "Permalink to this definition")
Add [`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task")`task` to this collection.

Parameters
*   **task** – The [`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task") object to add to this collection.

*   **name** – Optional string name to bind to (overrides the task’s own self-defined `name` attribute and/or any Python identifier (i.e. `.func_name`.)

*   **aliases** – Optional iterable of additional names to bind the task as, on top of the primary name. These will be used in addition to any aliases the task itself declares internally.

*   **default** – Whether this task should be the collection default.

New in version 1.0.

configuration(_taskpath:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_)→Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any][¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.configuration "Permalink to this definition")
Obtain merged configuration values from collection & children.

Parameters
**taskpath** – (Optional) Task name/path, identical to that used for [`__getitem__`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.__getitem__ "invoke.collection.Collection.__getitem__") (e.g. may be dotted for nested tasks, etc.) Used to decide which path to follow in the collection tree when merging config values.

Returns
A [`dict`](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)") containing configuration values.

New in version 1.0.

configure(_options:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.configure "Permalink to this definition")
(Recursively) merge `options` into the current [`configuration`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.configuration "invoke.collection.Collection.configuration").

Options configured this way will be available to all tasks. It is recommended to use unique keys to avoid potential clashes with other config options

For example, if you were configuring a Sphinx docs build target directory, it’s better to use a key like `'sphinx.target'` than simply `'target'`.

Parameters
**options** – An object implementing the dictionary protocol.

Returns
`None`.

New in version 1.0.

_classmethod_ from_module(_module:module_, _name:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _config:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_, _loaded\_from:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _auto\_dash\_names:Optional[[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")]=None_)→[invoke.collection.Collection](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection")[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.from_module "Permalink to this definition")
Return a new [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection") created from `module`.

Inspects `module` for any [`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task") instances and adds them to a new [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection"), returning it. If any explicit namespace collections exist (named `ns` or `namespace`) a copy of that collection object is preferentially loaded instead.

When the implicit/default collection is generated, it will be named after the module’s `__name__` attribute, or its last dotted section if it’s a submodule. (I.e. it should usually map to the actual `.py` filename.)

Explicitly given collections will only be given that module-derived name if they don’t already have a valid `.name` attribute.

If the module has a docstring (`__doc__`) it is copied onto the resulting [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection") (and used for display in help, list etc output.)

Parameters
*   **name** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – A string, which if given will override any automatically derived collection name (or name set on the module’s root namespace, if it has one.)

*   **config** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) –

Used to set config options on the newly created [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection") before returning it (saving you a call to [`configure`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.configure "invoke.collection.Collection.configure").)

If the imported module had a root namespace object, `config` is merged on top of it (i.e. overriding any conflicts.)

*   **loaded_from** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Identical to the same-named kwarg from the regular class constructor - should be the path where the module was found.

*   **auto_dash_names** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Identical to the same-named kwarg from the regular class constructor - determines whether emitted names are auto-dashed.

New in version 1.0.

serialized()→Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any][¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.serialized "Permalink to this definition")
Return an appropriate-for-serialization version of this object.

See the documentation for [`Program`](https://docs.pyinvoke.org/en/stable/api/program.html#invoke.program.Program "invoke.program.Program") and its `json` task listing format; this method is the driver for that functionality.

New in version 1.0.

subcollection_from_path(_path:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→[invoke.collection.Collection](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection")[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.subcollection_from_path "Permalink to this definition")
Given a `path` to a subcollection, return that subcollection.

New in version 1.0.

_property_ task_names _:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]_[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.task_names "Permalink to this definition")
Return all task identifiers for this collection as a one-level dict.

Specifically, a dict with the primary/”real” task names as the key, and any aliases as a list value.

It basically collapses the namespace tree into a single easily-scannable collection of invocation strings, and is thus suitable for things like flat-style task listings or transformation into parser contexts.

New in version 1.0.

task_with_config(_name:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]_)→Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]][¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.task_with_config "Permalink to this definition")
Return task named `name` plus its configuration dict.

E.g. in a deeply nested tree, this method returns the [`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task"), and a configuration dict created by merging that of this [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection") and any nested [`Collections`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection"), up through the one actually holding the [`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task").

See [`__getitem__`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.__getitem__ "invoke.collection.Collection.__getitem__") for semantics of the `name` argument.

Returns
Two-tuple of ([`Task`](https://docs.pyinvoke.org/en/stable/api/tasks.html#invoke.tasks.Task "invoke.tasks.Task"), [`dict`](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")).

New in version 1.0.

to_contexts(_ignore\_unknown\_help:Optional[[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")]=None_)→List[[invoke.parser.context.ParserContext](https://docs.pyinvoke.org/en/stable/api/parser.html#invoke.parser.context.ParserContext "invoke.parser.context.ParserContext")][¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.to_contexts "Permalink to this definition")
Returns all contained tasks and subtasks as a list of parser contexts.

Parameters
**ignore_unknown_help** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Passed on to each task’s `get_arguments()` method. See the config option by the same name for details.

New in version 1.0.

Changed in version 1.7: Added the `ignore_unknown_help` kwarg.

transform(_name:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection.transform "Permalink to this definition")
Transform `name` with the configured auto-dashes behavior.

If the collection’s `auto_dash_names` attribute is `True` (default), all non leading/trailing underscores are turned into dashes. (Leading/trailing underscores tend to get stripped elsewhere in the stack.)

If it is `False`, the inverse is applied - all dashes are turned into underscores.

New in version 1.0.

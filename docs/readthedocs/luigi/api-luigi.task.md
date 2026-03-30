# luigi.task

The abstract `Task` class.
It is a central concept of Luigi and represents the state of the workflow.
See Tasks for an overview.

Functions

`auto_namespace`([scope])

Same as `namespace()`, but instead of a constant namespace, it will be set to the `__module__` of the task class.

`externalize`(taskclass_or_taskobject)

Returns an externalized version of a Task.

`flatten`(struct)

Creates a flat list of all items in structured output (dicts, lists, items):

`flatten_output`(task)

Lists all output targets by recursively walking output-less (wrapper) tasks.

`getpaths`(struct)

Maps all Tasks in a structured data object to their .output().

`namespace`([namespace, scope])

Call to set namespace of tasks declared after the call.

`task_id_str`(task_family, params)

Returns a canonical string used to identify a particular task

Classes

`Config`(*args, **kwargs)

Class for configuration.

`DynamicRequirements`(requirements[, ...])

Wraps dynamic requirements yielded in tasks's run methods to control how completeness checks of (e.g.) large chunks of tasks are performed.

`ExternalTask`(*args, **kwargs)

Subclass for references to external dependencies.

`MixinNaiveBulkComplete`()

Enables a Task to be efficiently scheduled with e.g. range tools, by providing a bulk_complete implementation which checks completeness in a loop.

`Task`(*args, **kwargs)

This is the base class of all Luigi Tasks, the base unit of work in Luigi.

`WrapperTask`(*args, **kwargs)

Use for tasks that only wrap other tasks and that by definition are done if all their requirements exist.

Exceptions

`BulkCompleteNotImplementedError`

This is here to trick pylint.

luigi.task.namespace(*namespace=None*, *scope=''*)

Call to set namespace of tasks declared after the call.

It is often desired to call this function with the keyword argument
`scope=__name__`.

The `scope` keyword makes it so that this call is only effective for task
classes with a matching [*] `__module__`. The default value for
`scope` is the empty string, which means all classes. Multiple calls with
the same scope simply replace each other.

The namespace of a `Task` can also be changed by specifying the property
`task_namespace`.

```
class Task2(luigi.Task):
    task_namespace = 'namespace2'

```
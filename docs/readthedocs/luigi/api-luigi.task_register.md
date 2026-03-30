# luigi.task_register

Define the centralized register of all `Task` classes.

Functions

`load_task`(module, task_name, params_str)

Imports task dynamically given a module and a task name.

Classes

`Register`(classname, bases, classdict, **kwargs)

The Metaclass of `Task`.

Exceptions

`TaskClassAmbigiousException`

`TaskClassException`

`TaskClassNotFoundException`

exception luigi.task_register.TaskClassException

exception luigi.task_register.TaskClassNotFoundException

exception luigi.task_register.TaskClassAmbigiousException

class luigi.task_register.Register(*classname*, *bases*, *classdict*, ***kwargs*)

The Metaclass of `Task`.

Acts as a global registry of Tasks with the following properties:

- 

Cache instances of objects so that eg. `X(1, 2, 3)` always returns the
same object.

- 

Keep track of all subclasses of `Task` and expose them.

Custom class creation for namespacing.

Also register all subclasses.

When the set or inherited namespace evaluates to `None`, set the task namespace to
whatever the currently declared namespace is.

AMBIGUOUS_CLASS = <object object>

If this value is returned by `_get_reg()` then there is an
ambiguous task name (two `Task` have the same name). This denotes
an error.

classmethod clear_instance_cache()

Clear/Reset the instance cache.

classmethod disable_instance_cache()

Disables the instance cache.

property task_family

Internal note: This function will be deleted soon.

classmethod task_names()

List of task names as strings

classmethod tasks_str()

Human-readable register contents dump.

classmethod get_task_cls(*name*)

Returns an unambiguous class or raises an exception.

classmethod get_all_params()

Compiles and returns all parameters for all `Task`.

Returns:

a generator of tuples (TODO: we should make this more elegant)

luigi.task_register.load_task(*module*, *task_name*, *params_str*)

Imports task dynamically given a module and a task name.
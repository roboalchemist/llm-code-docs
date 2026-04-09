# luigi.batch_notifier

Library for sending batch notifications from the Luigi scheduler. This module
is internal to Luigi and not designed for use in other contexts.

Classes

`BatchNotifier`(**kwargs)

`ExplQueue`(num_items)

`batch_email`(*args, **kwargs)

class luigi.batch_notifier.batch_email(**args*, ***kwargs*)

email_interval

Parameter whose value is an `int`.

batch_mode

A parameter which takes two values:

- 

an instance of `Iterable` and

- 

the class of the variables to convert to.

In the task definition, use

```
class MyTask(luigi.Task):
    my_param = luigi.ChoiceParameter(choices=[0.1, 0.2, 0.3], var_type=float)

```
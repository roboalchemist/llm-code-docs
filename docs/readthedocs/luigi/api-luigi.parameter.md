# luigi.parameter

Parameters are one of the core concepts of Luigi.
All Parameters sit on `Task` classes.
See Parameter for more info on how to define parameters.

Classes

`BoolParameter`(default, parsing, **kwargs)

A Parameter whose value is a `bool`.

`ChoiceListParameter`(default, ...)

A parameter which takes two values:

`ChoiceParameter`(default, *, choices, ...)

A parameter which takes two values:

`ConfigPath`

`DateHourParameter`(default, interval, start, ...)

Parameter whose value is a `datetime` specified to the hour.

`DateIntervalParameter`(default, is_global, ...)

A Parameter whose value is a `DateInterval`.

`DateMinuteParameter`(default, interval, ...)

Parameter whose value is a `datetime` specified to the minute.

`DateParameter`(default, interval, start, **kwargs)

Parameter whose value is a `date`.

`DateSecondParameter`(default, interval, ...)

Parameter whose value is a `datetime` specified to the second.

`DictParameter`(default, *[, schema])

Parameter whose value is a `dict`.

`EnumListParameter`(default, ...)

A parameter whose value is a comma-separated list of `Enum`.

`EnumParameter`(default, *, enum, **kwargs)

A parameter whose value is an `Enum`.

`FloatParameter`(default, is_global, ...)

Parameter whose value is a `float`.

`IntParameter`(default, is_global, ...)

Parameter whose value is an `int`.

`ListParameter`(default, *[, schema])

Parameter whose value is a `list`.

`MonthParameter`(default, interval, start, ...)

Parameter whose value is a `date`, specified to the month (day of `date` is "rounded" to first of the month).

`NumericalParameter`(default, *, var_type, ...)

Parameter whose value is a number of the specified type, e.g. `int` or `float` and in the range specified.

`OptionalBoolParameter`(default, parsing, **kwargs)

Class to parse optional bool parameters.

`OptionalChoiceParameter`(default, var_type, ...)

Class to parse optional choice parameters.

`OptionalDictParameter`(default, *[, schema])

Class to parse optional dict parameters.

`OptionalFloatParameter`(default, is_global, ...)

Class to parse optional float parameters.

`OptionalIntParameter`(default, is_global, ...)

Class to parse optional int parameters.

`OptionalListParameter`(default, *[, schema])

Class to parse optional list parameters.

`OptionalNumericalParameter`(default, **kwargs)

Class to parse optional numerical parameters.

`OptionalParameter`(default, is_global, ...)

Class to parse optional parameters.

`OptionalParameterMixin`()

Mixin to make a parameter class optional and treat empty string as None.

`OptionalPathParameter`(default, *, absolute, ...)

Class to parse optional path parameters.

`OptionalStrParameter`(default, is_global, ...)

Class to parse optional str parameters.

`OptionalTupleParameter`(default, *[, schema])

Class to parse optional tuple parameters.

`Parameter`(default, is_global, significant, ...)

Parameter whose value is a `str`, and a base class for other parameter types.

`ParameterVisibility`(*values)

Possible values for the parameter visibility option.

`PathParameter`(default, *, absolute, exists, ...)

Parameter whose value is a path.

`StrParameter`(default, is_global, ...)

Parameter whose value is a `str`.

`TaskParameter`(default, is_global, ...)

A parameter that takes another luigi task class.

`TimeDeltaParameter`(default, is_global, ...)

Class that maps to timedelta using strings in any of the following forms:

`TupleParameter`(default, *[, schema])

Parameter whose value is a `tuple` or `tuple` of tuples.

`YearParameter`(default, interval, start, **kwargs)

Parameter whose value is a `date`, specified to the year (day and month of `date` is "rounded" to first day of the year).

Exceptions

`DuplicateParameterException`

Exception signifying that a Parameter was specified multiple times.

`MissingParameterException`

Exception signifying that there was a missing Parameter.

`OptionalParameterTypeWarning`

Warning class for OptionalParameterMixin with wrong type.

`ParameterException`

Base exception.

`UnconsumedParameterWarning`

Warning class for parameters that are not consumed by the task.

`UnknownParameterException`

Exception signifying that an unknown Parameter was supplied.

class luigi.parameter.ParameterVisibility(**values*)

Possible values for the parameter visibility option. Public is the default.
See Parameters for more info.

PUBLIC = 0

HIDDEN = 1

PRIVATE = 2

classmethod has_value(*value*)

serialize()

exception luigi.parameter.ParameterException

Base exception.

exception luigi.parameter.MissingParameterException

Exception signifying that there was a missing Parameter.

exception luigi.parameter.UnknownParameterException

Exception signifying that an unknown Parameter was supplied.

exception luigi.parameter.DuplicateParameterException

Exception signifying that a Parameter was specified multiple times.

exception luigi.parameter.OptionalParameterTypeWarning

Warning class for OptionalParameterMixin with wrong type.

exception luigi.parameter.UnconsumedParameterWarning

Warning class for parameters that are not consumed by the task.

class luigi.parameter.ConfigPath

section: str

name: str

class luigi.parameter.Parameter(*default: ~luigi.parameter.T | ~luigi.parameter._NoValueType = <no_value>, is_global: bool = False, significant: bool = True, description: str | None = None, config_path: ~luigi.parameter.ConfigPath | None = None, positional: bool = True, always_in_help: bool = False, batch_method: ~typing.Callable[[~typing.Iterable[~typing.Any]], ~typing.Any] | None = None, visibility: ~luigi.parameter.ParameterVisibility = ParameterVisibility.PUBLIC*)

Parameter whose value is a `str`, and a base class for other parameter types.

Parameters are objects set on the Task class level to make it possible to parameterize tasks.
For instance:

```
class MyTask(luigi.Task):
    foo = luigi.Parameter()

class RequiringTask(luigi.Task):
    def requires(self):
        return MyTask(foo="hello")

    def run(self):
        print(self.requires().foo)  # prints "hello"

```
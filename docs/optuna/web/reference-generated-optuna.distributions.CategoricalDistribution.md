# optuna.distributions.CategoricalDistribution

class optuna.distributions.CategoricalDistribution(*choices*)

A categorical distribution.

This object is instantiated by `suggest_categorical()`, and
passed to `samplers` in general.

Parameters:

**choices** (*Sequence**[**CategoricalChoiceType**]*) – Parameter value candidates. `choices` must have one element at least.

Note

Not all types are guaranteed to be compatible with all storages. It is recommended to
restrict the types of the choices to `None` [https://docs.python.org/3/library/constants.html#None], `bool` [https://docs.python.org/3/library/functions.html#bool], `int` [https://docs.python.org/3/library/functions.html#int],
`float` [https://docs.python.org/3/library/functions.html#float] and `str` [https://docs.python.org/3/library/stdtypes.html#str].
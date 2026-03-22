# optuna.search_space.IntersectionSearchSpace

class optuna.search_space.IntersectionSearchSpace(*include_pruned=False*)

A class to calculate the intersection search space of a `Study`.

Intersection search space contains the intersection of parameter distributions that have been
suggested in the completed trials of the study so far.
If there are multiple parameters that have the same name but different distributions,
neither is included in the resulting search space
(i.e., the parameters with dynamic value ranges are excluded).

Note that an instance of this class is supposed to be used for only one study.
If different studies are passed to
`calculate()`,
a `ValueError` [https://docs.python.org/3/library/exceptions.html#ValueError] is raised.

Parameters:

**include_pruned** (*bool* [https://docs.python.org/3/library/functions.html#bool]) – Whether pruned trials should be included in the search space.

Methods

`calculate`(study[, use_cache])

Returns the intersection search space of the `Study`.

calculate(*study*, *use_cache=False*)

Returns the intersection search space of the `Study`.

Parameters:

- 

**study** (*Study*) – A study with completed trials. The same study must be passed for one instance
of this class through its lifetime.

- 

**use_cache** (*bool* [https://docs.python.org/3/library/functions.html#bool]) – An option to use cached trials for each trial.

Returns:

A dictionary containing the parameter names and parameter’s distributions sorted by
parameter names.

Return type:

dict [https://docs.python.org/3/library/stdtypes.html#dict][str [https://docs.python.org/3/library/stdtypes.html#str], BaseDistribution]
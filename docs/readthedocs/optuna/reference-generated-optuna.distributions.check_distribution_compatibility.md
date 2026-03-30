# optuna.distributions.check_distribution_compatibility

optuna.distributions.check_distribution_compatibility(*dist_old*, *dist_new*)

A function to check compatibility of two distributions.

It checks whether `dist_old` and `dist_new` are the same kind of distributions.
If `dist_old` is `CategoricalDistribution`,
it further checks `choices` are the same between `dist_old` and `dist_new`.
Note that this method is not supposed to be called by library users.

Parameters:

- 

**dist_old** (*BaseDistribution*) – A distribution previously recorded in storage.

- 

**dist_new** (*BaseDistribution*) – A distribution newly added to storage.

Return type:

None
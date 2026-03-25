# optuna.search_space.intersection_search_space

optuna.search_space.intersection_search_space(*trials*, *include_pruned=False*)

Return the intersection search space of the given trials.

Intersection search space contains the intersection of parameter distributions that have been
suggested in the completed trials of the study so far.
If there are multiple parameters that have the same name but different distributions,
neither is included in the resulting search space
(i.e., the parameters with dynamic value ranges are excluded).

Note

`IntersectionSearchSpace` provides the same functionality with
a much faster way. Please consider using it if you want to reduce execution time
as much as possible.
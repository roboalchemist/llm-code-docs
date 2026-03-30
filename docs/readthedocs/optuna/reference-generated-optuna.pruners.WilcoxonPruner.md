# optuna.pruners.WilcoxonPruner

class optuna.pruners.WilcoxonPruner(***, *p_threshold=0.1*, *n_startup_steps=2*)

Pruner based on the Wilcoxon signed-rank test [https://en.wikipedia.org/w/index.php?title=Wilcoxon_signed-rank_test&oldid=1195011212].

This pruner performs the Wilcoxon signed-rank test between the current trial and the current best trial,
and stops whenever the pruner is sure up to a given p-value that the current trial is worse than the best one.

This pruner is effective for optimizing the mean/median of some (costly-to-evaluate) performance scores over a set of problem instances.
Example applications include the optimization of:

- 

the mean performance of a heuristic method (simulated annealing, genetic algorithm, SAT solver, etc.) on a set of problem instances,

- 

the k-fold cross-validation score of a machine learning model, and

- 

the accuracy of outputs of a large language model (LLM) on a set of questions.

There can be “easy” or “hard” instances (the pruner handles correspondence of the instances between different trials).
In each trial, it is recommended to shuffle the evaluation order, so that the optimization doesn’t overfit to the instances in the beginning.

When you use this pruner, you must call `Trial.report(value, step)` method for each step (instance id) with
the evaluated value. The instance id may not be in ascending order.
This is different from other pruners in that the reported value need not converge
to the real value. To use pruners such as `SuccessiveHalvingPruner`
in the same setting, you must provide e.g., the historical average of the evaluated values.

See also

Please refer to `report()`.
# optuna.terminator.BestValueStagnationEvaluator

class optuna.terminator.BestValueStagnationEvaluator(*max_stagnation_trials=30*)

Evaluates the stagnation period of the best value in an optimization process.

This class is initialized with a maximum stagnation period (`max_stagnation_trials`)
and is designed to evaluate the remaining trials before reaching this maximum period
of allowed stagnation. If this remaining trials reach zero, the trial terminates.
Therefore, the default error evaluator is instantiated by `StaticErrorEvaluator(const=0)`.

Parameters:

**max_stagnation_trials** (*int* [https://docs.python.org/3/library/functions.html#int]) – The maximum number of trials allowed for stagnation.

Note

Added in v3.4.0 as an experimental feature. The interface may change in newer versions
without prior notice. See https://github.com/optuna/optuna/releases/tag/v3.4.0.
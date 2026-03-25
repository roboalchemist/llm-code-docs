# optuna.terminator.EMMREvaluator

class optuna.terminator.EMMREvaluator(*deterministic_objective=False*, *delta=0.1*, *min_n_trials=2*, *seed=None*)

Evaluates a kind of regrets, called the Expected Minimum Model Regret(EMMR).

EMMR is an upper bound of “expected minimum simple regret” in the optimization process.

Expected minimum simple regret is a quantity that converges to zero only if the
optimization process has found the global optima.

For further information about expected minimum simple regret and the algorithm,
please refer to the following paper:

- 

A stopping criterion for Bayesian optimization by the gap of expected minimum simple
regrets [https://proceedings.mlr.press/v206/ishibashi23a.html]

Also, there is our blog post explaining this evaluator:

- 

Introducing A New Terminator: Early Termination of Black-box Optimization Based on
Expected Minimum Model Regret [https://medium.com/optuna/introducing-a-new-terminator-early-termination-of-black-box-optimization-based-on-expected-9a660774fcdb]

Parameters:

- 

**deterministic_objective** (*bool* [https://docs.python.org/3/library/functions.html#bool]) – A boolean value which indicates whether the objective function is deterministic.
Default is `False` [https://docs.python.org/3/library/constants.html#False].

- 

**delta** (*float* [https://docs.python.org/3/library/functions.html#float]) – A float number related to the criterion for termination. Default to 0.1.
For further information about this parameter, please see the aforementioned paper.

- 

**min_n_trials** (*int* [https://docs.python.org/3/library/functions.html#int]) – A minimum number of complete trials to compute the criterion. Default to 2.

- 

**seed** (*int* [https://docs.python.org/3/library/functions.html#int]* | **None*) – A random seed for EMMREvaluator.

Example

```
import optuna
from optuna.terminator import EMMREvaluator
from optuna.terminator import MedianErrorEvaluator
from optuna.terminator import Terminator

sampler = optuna.samplers.TPESampler(seed=0)
study = optuna.create_study(sampler=sampler, direction="minimize")
emmr_improvement_evaluator = EMMREvaluator()
median_error_evaluator = MedianErrorEvaluator(emmr_improvement_evaluator)
terminator = Terminator(
    improvement_evaluator=emmr_improvement_evaluator,
    error_evaluator=median_error_evaluator,
)

for i in range(1000):
    trial = study.ask()

    ys = [trial.suggest_float(f"x{i}", -10.0, 10.0) for i in range(5)]
    value = sum(ys[i] ** 2 for i in range(5))

    study.tell(trial, value)

    if terminator.should_terminate(study):
        # Terminated by Optuna Terminator!
        break

```
# optuna.terminator

The `terminator` module implements a mechanism for automatically terminating the optimization process, accompanied by a callback class for the termination and evaluators for the estimated room for improvement in the optimization and statistical error of the objective function. The terminator stops the optimization process when the estimated potential improvement is smaller than the statistical error.

`BaseTerminator`

Base class for terminators.

`Terminator`

Automatic stopping mechanism for Optuna studies.

`BaseImprovementEvaluator`

Base class for improvement evaluators.

`RegretBoundEvaluator`

An error evaluator for upper bound on the regret with high-probability confidence.

`BestValueStagnationEvaluator`

Evaluates the stagnation period of the best value in an optimization process.

`EMMREvaluator`

Evaluates a kind of regrets, called the Expected Minimum Model Regret(EMMR).

`BaseErrorEvaluator`

Base class for error evaluators.

`CrossValidationErrorEvaluator`

An error evaluator for objective functions based on cross-validation.

`StaticErrorEvaluator`

An error evaluator that always returns a constant value.

`MedianErrorEvaluator`

An error evaluator that returns the ratio to initial median.

`TerminatorCallback`

A callback that terminates the optimization using Terminator.

`report_cross_validation_scores`

A function to report cross-validation scores of a trial.

For an example of using this module, please refer to this example [https://github.com/optuna/optuna-examples/tree/main/terminator].
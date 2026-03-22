# Source: https://automl.github.io/SMAC3/latest/3_getting_started/

Title: Getting Started - SMAC3

URL Source: https://automl.github.io/SMAC3/latest/3_getting_started/

Markdown Content:
SMAC needs four core components (configuration space, target function, scenario and a facade) to run an optimization process, all of which are explained on this page.

They interact in the following way:

[![Image 1: Interaction of SMAC's components](https://automl.github.io/SMAC3/latest/images/smac_components_interaction.jpg)](https://automl.github.io/SMAC3/latest/images/smac_components_interaction.jpg)

Interaction of SMAC's components

Configuration Space[#](https://automl.github.io/SMAC3/latest/3_getting_started/#configuration-space "Permanent link")
---------------------------------------------------------------------------------------------------------------------

The configuration space defines the search space of the hyperparameters and, therefore, the tunable parameters' legal ranges and default values.

```
from ConfigSpace import ConfigSpace

cs = ConfigurationSpace({
    "myfloat": (0.1, 1.5),                # Uniform Float
    "myint": (2, 10),                     # Uniform Integer
    "species": ["mouse", "cat", "dog"],   # Categorical
})
```

Please see the documentation of [ConfigurationSpace](https://automl.github.io/ConfigSpace) for more details.

Target Function[#](https://automl.github.io/SMAC3/latest/3_getting_started/#target-function "Permanent link")
-------------------------------------------------------------------------------------------------------------

The target function takes a configuration from the configuration space and returns a performance value. For example, you could use a Neural Network to predict on your data and get some validation performance. If, for instance, you would tune the learning rate of the Network's optimizer, every learning rate will change the final validation performance of the network. This is the target function. SMAC tries to find the best performing learning rate by trying different values and evaluating the target function - in an efficient way.

```
def train(self, config: Configuration, seed: int) -> float:
        model = MultiLayerPerceptron(learning_rate=config["learning_rate"])
        model.fit(...)
        accuracy = model.validate(...)

        return 1 - accuracy  # SMAC always minimizes (the smaller the better)
```

Note

In general, the arguments of the target function depend on the intensifier. However, in all cases, the first argument must be the configuration (arbitrary argument name is possible here) and a seed. If you specified instances in the scenario, SMAC requires `instance` as argument additionally. If you use `SuccessiveHalving` or `Hyperband` as intensifier but you did not specify instances, SMAC passes `budget` as argument to the target function. But don't worry: SMAC will tell you if something is missing or if something is not used.

Warning

SMAC _always_ minimizes the value returned from the target function.

Warning

SMAC passes either `instance` or `budget` to the target function but never both.

Scenario[#](https://automl.github.io/SMAC3/latest/3_getting_started/#scenario "Permanent link")
-----------------------------------------------------------------------------------------------

The [Scenario](https://automl.github.io/SMAC3/latest/api/smac/scenario/#smac.scenario) is used to provide environment variables. For example, if you want to limit the optimization process by a time limit or want to specify where to save the results.

```
from smac import Scenario

scenario = Scenario(
    configspace=cs,
    name="experiment_name",
    output_directory=Path("your_output_directory")
    walltime_limit=120,  # Limit to two minutes
    n_trials=500,  # Evaluated max 500 trials
    n_workers=8,  # Use eight workers
    ...
)
```

Note

If no `name` is given, a hash of the experiment is used. Running the same experiment again at a later time will result in exactly the same hash. This is important, because the optimization will warmstart on the preexisting evaluations, if not otherwise specified in the [Facade](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade).

Facade[#](https://automl.github.io/SMAC3/latest/3_getting_started/#facade "Permanent link")
-------------------------------------------------------------------------------------------

Warn

By default Facades will try to warmstart on preexisting logs. This behavior can be specified using the `overwrite` parameter.

A [facade](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade) is the entry point to SMAC, which constructs a default optimization pipeline for you. SMAC offers various facades, which satisfy many common use cases and are crucial to achieving peak performance. The idea behind the facades is to provide a simple interface to all of SMAC's components, which is easy to use and understand and without the need of deep diving into the material. However, experts are invited to change the components to their specific hyperparameter optimization needs. The following table (horizontally scrollable) shows you what is supported and reveals the default [components](https://automl.github.io/SMAC3/latest/advanced_usage/1_components/#components):

|  | [Black-Box](https://automl.github.io/SMAC3/latest/api/smac/facade/blackbox_facade/#smac.facade.blackbox_facade) | [Hyperparameter Optimization](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperparameter_optimization_facade/#smac.facade.hyperparameter_optimization_facade) | [Multi-Fidelity](https://automl.github.io/SMAC3/latest/api/smac/facade/multi_fidelity_facade/#smac.facade.multi_fidelity_facade) | [Algorithm Configuration](https://automl.github.io/SMAC3/latest/api/smac/facade/algorithm_configuration_facade/#smac.facade.algorithm_configuration_facade) | [Random](https://automl.github.io/SMAC3/latest/api/smac/facade/random_facade/#smac.facade.random_facade) | [Hyperband](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade) |
| --- | --- | --- | --- | --- | --- | --- |
| #Parameters | low | low/medium/high | low/medium/high | low/medium/high | low/medium/high | low/medium/high |
| Supports Instances | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Supports Multi-Fidelity | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ |
| Initial Design | [Sobol](https://automl.github.io/SMAC3/latest/api/smac/initial_design/sobol_design/#smac.initial_design.sobol_design) | [Sobol](https://automl.github.io/SMAC3/latest/api/smac/initial_design/sobol_design/#smac.initial_design.sobol_design) | [Random](https://automl.github.io/SMAC3/latest/api/smac/initial_design/random_design/#smac.initial_design.random_design) | [Default](https://automl.github.io/SMAC3/latest/api/smac/initial_design/default_design/#smac.initial_design.default_design) | [Default](https://automl.github.io/SMAC3/latest/api/smac/initial_design/default_design/#smac.initial_design.default_design) | [Default](https://automl.github.io/SMAC3/latest/api/smac/initial_design/default_design/#smac.initial_design.default_design) |
| Surrogate Model | [Gaussian Process](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/gaussian_process/#smac.model.gaussian_process.gaussian_process) | [Random Forest](https://automl.github.io/SMAC3/latest/api/smac/model/random_forest/random_forest/#smac.model.random_forest.random_forest) | [Random Forest](https://automl.github.io/SMAC3/latest/api/smac/model/random_forest/random_forest/#smac.model.random_forest.random_forest) | [Random Forest](https://automl.github.io/SMAC3/latest/api/smac/model/random_forest/random_forest/#smac.model.random_forest.random_forest) | Not used | Not used |
| Acquisition Function | [Expected Improvement](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/expected_improvement/#smac.acquisition.function.expected_improvement) | [Log Expected Improvement](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/expected_improvement/#smac.acquisition.function.expected_improvement) | [Log Expected Improvement](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/expected_improvement/#smac.acquisition.function.expected_improvement) | [Expected Improvement](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/expected_improvement/#smac.acquisition.function.expected_improvement) | Not used | Not used |
| Acquisition Maximizer | [Local and Sorted Random Search](https://automl.github.io/SMAC3/latest/api/smac/acquisition/maximizer/local_and_random_search/#smac.acquisition.maximizer.local_and_random_search) | [Local and Sorted Random Search](https://automl.github.io/SMAC3/latest/api/smac/acquisition/maximizer/local_and_random_search/#smac.acquisition.maximizer.local_and_random_search) | [Local and Sorted Random Search](https://automl.github.io/SMAC3/latest/api/smac/acquisition/maximizer/local_and_random_search/#smac.acquisition.maximizer.local_and_random_search) | [Local and Sorted Random Search](https://automl.github.io/SMAC3/latest/api/smac/acquisition/maximizer/local_and_random_search/#smac.acquisition.maximizer.local_and_random_search) | Not Used | Not Used |
| Intensifier | [Default](https://automl.github.io/SMAC3/latest/api/smac/intensifier/intensifier/#smac.intensifier.intensifier) | [Default](https://automl.github.io/SMAC3/latest/api/smac/intensifier/intensifier/#smac.intensifier.intensifier) | [Hyperband](https://automl.github.io/SMAC3/latest/api/smac/intensifier/hyperband/#smac.intensifier.hyperband) | [Default](https://automl.github.io/SMAC3/latest/api/smac/intensifier/intensifier/#smac.intensifier.intensifier) | [Default](https://automl.github.io/SMAC3/latest/api/smac/intensifier/intensifier/#smac.intensifier.intensifier) | [Hyperband](https://automl.github.io/SMAC3/latest/api/smac/intensifier/hyperband/#smac.intensifier.hyperband) |
| Runhistory Encoder | [Default](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/encoder/#smac.runhistory.encoder.encoder) | [Log](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/log_encoder/#smac.runhistory.encoder.log_encoder) | [Log](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/log_encoder/#smac.runhistory.encoder.log_encoder) | [Default](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/encoder/#smac.runhistory.encoder.encoder) | [Default](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/encoder/#smac.runhistory.encoder.encoder) | [Default](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/encoder/#smac.runhistory.encoder.encoder) |
| Random Design Probability | 8.5% | 20% | 20% | 50% | Not used | Not used |

Info

The multi-fidelity facade is the closest implementation to [BOHB](https://github.com/automl/HpBandSter).

Note

We want to emphasize that SMAC is a highly modular optimization framework. The facade accepts many arguments to specify components of the pipeline. Please also note, that in contrast to previous versions, instantiated objects are passed instead of _kwargs_.

The facades can be imported directly from the `smac` module.

```
from smac import BlackBoxFacade as BBFacade
from smac import HyperparameterOptimizationFacade as HPOFacade
from smac import MultiFidelityFacade as MFFacade
from smac import AlgorithmConfigurationFacade as ACFacade
from smac import RandomFacade as RFacade
from smac import HyperbandFacade as HBFacade

smac = HPOFacade(scenario=scenario, target_function=train)
smac = MFFacade(scenario=scenario, target_function=train)
smac = ACFacade(scenario=scenario, target_function=train)
smac = RFacade(scenario=scenario, target_function=train)
smac = HBFacade(scenario=scenario, target_function=train)
```

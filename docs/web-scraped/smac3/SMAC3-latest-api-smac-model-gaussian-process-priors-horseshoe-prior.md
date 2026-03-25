# Source: https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/

Title: Horseshoe prior - SMAC3

URL Source: https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/

Markdown Content:
Horseshoe prior - SMAC3
===============
- [x] - [x] 

[Skip to content](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior)

[![Image 1: logo](https://automl.github.io/SMAC3/latest/images/logo.png)](https://automl.github.io/SMAC3/latest/ "SMAC3")

 SMAC3 

 Horseshoe prior 

[](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/?q= "Share")

 Initializing search 

[automl/SMAC3](https://github.com/automl/SMAC3/ "Go to repository")

*   [Home](https://automl.github.io/SMAC3/latest/)
*   [Installation](https://automl.github.io/SMAC3/latest/1_installation/)
*   [Package Overview](https://automl.github.io/SMAC3/latest/2_package_overview/)
*   [Getting Started](https://automl.github.io/SMAC3/latest/3_getting_started/)
*   [Advanced Usage](https://automl.github.io/SMAC3/latest/advanced_usage/1_components/)
*   [Examples](https://automl.github.io/SMAC3/latest/examples/1%20Basics/1_quadratic_function/)
*   [API](https://automl.github.io/SMAC3/latest/api/smac/constants/)
*   [Info & FAQ](https://automl.github.io/SMAC3/latest/6_references/)

[![Image 2: logo](https://automl.github.io/SMAC3/latest/images/logo.png)](https://automl.github.io/SMAC3/latest/ "SMAC3") SMAC3  

[automl/SMAC3](https://github.com/automl/SMAC3/ "Go to repository")

*   [Home](https://automl.github.io/SMAC3/latest/)
*   [Installation](https://automl.github.io/SMAC3/latest/1_installation/)
*   [Package Overview](https://automl.github.io/SMAC3/latest/2_package_overview/)
*   [Getting Started](https://automl.github.io/SMAC3/latest/3_getting_started/)
*   - [x]  Advanced Usage   Advanced Usage  
    *   [Components](https://automl.github.io/SMAC3/latest/advanced_usage/1_components/)
    *   [Multi-Fidelity Optimization](https://automl.github.io/SMAC3/latest/advanced_usage/2_multi_fidelity/)
    *   [Multi-Objective Optimization](https://automl.github.io/SMAC3/latest/advanced_usage/3_multi_objective/)
    *   [Optimization across Instances](https://automl.github.io/SMAC3/latest/advanced_usage/4_instances/)
    *   [Ask-and-Tell Interface](https://automl.github.io/SMAC3/latest/advanced_usage/5_ask_and_tell/)
    *   [Command-Line Interface](https://automl.github.io/SMAC3/latest/advanced_usage/6_commandline/)
    *   [Stopping Criteria](https://automl.github.io/SMAC3/latest/advanced_usage/7_stopping_criteria/)
    *   [Logging](https://automl.github.io/SMAC3/latest/advanced_usage/8_logging/)
    *   [Parallelism](https://automl.github.io/SMAC3/latest/advanced_usage/9_parallelism/)
    *   [Continue](https://automl.github.io/SMAC3/latest/advanced_usage/10_continue/)
    *   [Reproducibility](https://automl.github.io/SMAC3/latest/advanced_usage/11_reproducibility/)
    *   [Optimizations](https://automl.github.io/SMAC3/latest/advanced_usage/12_optimizations/)

*   - [x]  Examples   Examples  
    *   - [x]  1 Basics   1 Basics  
        *   [Quadratic Function](https://automl.github.io/SMAC3/latest/examples/1%20Basics/1_quadratic_function/)
        *   [Support Vector Machine with Cross-Validation](https://automl.github.io/SMAC3/latest/examples/1%20Basics/2_svm_cv/)
        *   [Ask-and-Tell](https://automl.github.io/SMAC3/latest/examples/1%20Basics/3_ask_and_tell/)
        *   [Custom Callback](https://automl.github.io/SMAC3/latest/examples/1%20Basics/4_callback/)
        *   [Continue an Optimization](https://automl.github.io/SMAC3/latest/examples/1%20Basics/5_continue/)
        *   [User Priors over the Optimum](https://automl.github.io/SMAC3/latest/examples/1%20Basics/6_priors/)
        *   [Parallelization on Cluster](https://automl.github.io/SMAC3/latest/examples/1%20Basics/7_parallelization_cluster/)
        *   [Warmstarting SMAC](https://automl.github.io/SMAC3/latest/examples/1%20Basics/8_warmstart/)

    *   - [x]  2 Multi Fidelity and Multi Instances   2 Multi Fidelity and Multi Instances  
        *   [Multi-Layer Perceptron Using Multiple Epochs](https://automl.github.io/SMAC3/latest/examples/2%20Multi-Fidelity%20and%20Multi-Instances/1_mlp_epochs/)
        *   [Stochastic Gradient Descent On Multiple Datasets](https://automl.github.io/SMAC3/latest/examples/2%20Multi-Fidelity%20and%20Multi-Instances/2_sgd_datasets/)
        *   [Specify Number of Trials via a Total Budget in Hyperband](https://automl.github.io/SMAC3/latest/examples/2%20Multi-Fidelity%20and%20Multi-Instances/3_specify_HB_via_total_budget/)

    *   - [x]  3 Multi Objective   3 Multi Objective  
        *   [2D Schaffer Function with Objective Weights](https://automl.github.io/SMAC3/latest/examples/3%20Multi-Objective/1_schaffer/)
        *   [ParEGO](https://automl.github.io/SMAC3/latest/examples/3%20Multi-Objective/2_parego/)

    *   - [x]  4 Advanced Topics   4 Advanced Topics  
        *   [Callback for logging run metadata](https://automl.github.io/SMAC3/latest/examples/4%20Advanced%20Topics/3_metadata_callback/)
        *   [Speeding up Cross-Validation with Intensification](https://automl.github.io/SMAC3/latest/examples/4%20Advanced%20Topics/4_intensify_crossvalidation/)

    *   - [x]  5 Command Line Interface   5 Command Line Interface  
        *   [Call Target Function From Script](https://automl.github.io/SMAC3/latest/examples/5%20Command-Line%20Interface/1_call_target_function_script/)

*   - [x]  API   API  
    *   - [x]  Smac   Smac  
        *   [Constants](https://automl.github.io/SMAC3/latest/api/smac/constants/)
        *   [Scenario](https://automl.github.io/SMAC3/latest/api/smac/scenario/)
        *   - [x]  Acquisition   Acquisition  
            *   - [x]  Function   Function  
                *   [Abstract acquisition function](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/abstract_acquisition_function/)
                *   [Confidence bound](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/confidence_bound/)
                *   [Expected improvement](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/expected_improvement/)
                *   [Integrated acquisition function](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/integrated_acquisition_function/)
                *   [Prior acquisition function](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/prior_acquisition_function/)
                *   [Probability improvement](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/probability_improvement/)
                *   [Thompson](https://automl.github.io/SMAC3/latest/api/smac/acquisition/function/thompson/)

            *   - [x]  Maximizer   Maximizer  
                *   [Abstract acquisition maximizer](https://automl.github.io/SMAC3/latest/api/smac/acquisition/maximizer/abstract_acquisition_maximizer/)
                *   [Differential evolution](https://automl.github.io/SMAC3/latest/api/smac/acquisition/maximizer/differential_evolution/)
                *   [Helpers](https://automl.github.io/SMAC3/latest/api/smac/acquisition/maximizer/helpers/)
                *   [Local and random search](https://automl.github.io/SMAC3/latest/api/smac/acquisition/maximizer/local_and_random_search/)
                *   [Local search](https://automl.github.io/SMAC3/latest/api/smac/acquisition/maximizer/local_search/)
                *   [Random search](https://automl.github.io/SMAC3/latest/api/smac/acquisition/maximizer/random_search/)

        *   - [x]  Callback   Callback  
            *   [Callback](https://automl.github.io/SMAC3/latest/api/smac/callback/callback/)
            *   [Metadata callback](https://automl.github.io/SMAC3/latest/api/smac/callback/metadata_callback/)

        *   - [x]  Facade   Facade  
            *   [Abstract facade](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/)
            *   [Algorithm configuration facade](https://automl.github.io/SMAC3/latest/api/smac/facade/algorithm_configuration_facade/)
            *   [Blackbox facade](https://automl.github.io/SMAC3/latest/api/smac/facade/blackbox_facade/)
            *   [Hyperband facade](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/)
            *   [Hyperparameter optimization facade](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperparameter_optimization_facade/)
            *   [Multi fidelity facade](https://automl.github.io/SMAC3/latest/api/smac/facade/multi_fidelity_facade/)
            *   [Random facade](https://automl.github.io/SMAC3/latest/api/smac/facade/random_facade/)

        *   - [x]  Initial design   Initial design  
            *   [Abstract initial design](https://automl.github.io/SMAC3/latest/api/smac/initial_design/abstract_initial_design/)
            *   [Default design](https://automl.github.io/SMAC3/latest/api/smac/initial_design/default_design/)
            *   [Factorial design](https://automl.github.io/SMAC3/latest/api/smac/initial_design/factorial_design/)
            *   [Latin hypercube design](https://automl.github.io/SMAC3/latest/api/smac/initial_design/latin_hypercube_design/)
            *   [Random design](https://automl.github.io/SMAC3/latest/api/smac/initial_design/random_design/)
            *   [Sobol design](https://automl.github.io/SMAC3/latest/api/smac/initial_design/sobol_design/)

        *   - [x]  Intensifier   Intensifier  
            *   [Abstract intensifier](https://automl.github.io/SMAC3/latest/api/smac/intensifier/abstract_intensifier/)
            *   [Hyperband](https://automl.github.io/SMAC3/latest/api/smac/intensifier/hyperband/)
            *   [Hyperband utils](https://automl.github.io/SMAC3/latest/api/smac/intensifier/hyperband_utils/)
            *   [Intensifier](https://automl.github.io/SMAC3/latest/api/smac/intensifier/intensifier/)
            *   [Successive halving](https://automl.github.io/SMAC3/latest/api/smac/intensifier/successive_halving/)

        *   - [x]  Main   Main  
            *   [Config selector](https://automl.github.io/SMAC3/latest/api/smac/main/config_selector/)
            *   [Smbo](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/)

        *   - [x]  Model   Model  
            *   [Abstract model](https://automl.github.io/SMAC3/latest/api/smac/model/abstract_model/)
            *   [Multi objective model](https://automl.github.io/SMAC3/latest/api/smac/model/multi_objective_model/)
            *   [Random model](https://automl.github.io/SMAC3/latest/api/smac/model/random_model/)
            *   - [x]  Gaussian process   Gaussian process  
                *   [Abstract gaussian process](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/abstract_gaussian_process/)
                *   [Gaussian process](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/gaussian_process/)
                *   [Gpytorch gaussian process](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/gpytorch_gaussian_process/)
                *   [Mcmc gaussian process](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/mcmc_gaussian_process/)
                *   - [x]  Kernels   Kernels  
                    *   [Base kernels](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/)
                    *   [Hamming kernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/hamming_kernel/)
                    *   [Matern kernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/matern_kernel/)
                    *   [Rbf kernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/rbf_kernel/)
                    *   [White kernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/white_kernel/)

                *   - [x]  Priors   Priors  
                    *   [Abstract prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/abstract_prior/)
                    *   [Gamma prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/gamma_prior/)
                    *   - [x]  Horseshoe prior  [Horseshoe prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/) Table of contents  
                        *   [horseshoe_prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior)
                            *   [HorseshoePrior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior)
                                *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior--parameters)
                                *   [get_gradient](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_gradient)
                                    *   [Warning](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_gradient--warning)
                                    *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_gradient--parameters)
                                    *   [Returns](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_gradient--returns)

                                *   [get_log_probability](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_log_probability)
                                    *   [Warning](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_log_probability--warning)
                                    *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_log_probability--parameters)
                                    *   [Returns](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_log_probability--returns)

                                *   [sample_from_prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.sample_from_prior)
                                    *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.sample_from_prior--parameters)
                                    *   [Returns](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.sample_from_prior--returns)

                    *   [Log normal prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/log_normal_prior/)
                    *   [Tophat prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/tophat_prior/)

            *   - [x]  Random forest   Random forest  
                *   [Abstract random forest](https://automl.github.io/SMAC3/latest/api/smac/model/random_forest/abstract_random_forest/)
                *   [Random forest](https://automl.github.io/SMAC3/latest/api/smac/model/random_forest/random_forest/)

        *   - [x]  Multi objective   Multi objective  
            *   [Abstract multi objective algorithm](https://automl.github.io/SMAC3/latest/api/smac/multi_objective/abstract_multi_objective_algorithm/)
            *   [Aggregation strategy](https://automl.github.io/SMAC3/latest/api/smac/multi_objective/aggregation_strategy/)
            *   [Parego](https://automl.github.io/SMAC3/latest/api/smac/multi_objective/parego/)

        *   - [x]  Random design   Random design  
            *   [Abstract random design](https://automl.github.io/SMAC3/latest/api/smac/random_design/abstract_random_design/)
            *   [Annealing design](https://automl.github.io/SMAC3/latest/api/smac/random_design/annealing_design/)
            *   [Modulus design](https://automl.github.io/SMAC3/latest/api/smac/random_design/modulus_design/)
            *   [Probability design](https://automl.github.io/SMAC3/latest/api/smac/random_design/probability_design/)

        *   - [x]  Runhistory   Runhistory  
            *   [Dataclasses](https://automl.github.io/SMAC3/latest/api/smac/runhistory/dataclasses/)
            *   [Enumerations](https://automl.github.io/SMAC3/latest/api/smac/runhistory/enumerations/)
            *   [Errors](https://automl.github.io/SMAC3/latest/api/smac/runhistory/errors/)
            *   [Runhistory](https://automl.github.io/SMAC3/latest/api/smac/runhistory/runhistory/)
            *   - [x]  Encoder   Encoder  
                *   [Abstract encoder](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/abstract_encoder/)
                *   [Boing encoder](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/boing_encoder/)
                *   [Eips encoder](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/eips_encoder/)
                *   [Encoder](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/encoder/)
                *   [Inverse scaled encoder](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/inverse_scaled_encoder/)
                *   [Log encoder](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/log_encoder/)
                *   [Log scaled encoder](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/log_scaled_encoder/)
                *   [Scaled encoder](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/scaled_encoder/)
                *   [Sqrt scaled encoder](https://automl.github.io/SMAC3/latest/api/smac/runhistory/encoder/sqrt_scaled_encoder/)

        *   - [x]  Runner   Runner  
            *   [Abstract runner](https://automl.github.io/SMAC3/latest/api/smac/runner/abstract_runner/)
            *   [Abstract serial runner](https://automl.github.io/SMAC3/latest/api/smac/runner/abstract_serial_runner/)
            *   [Dask runner](https://automl.github.io/SMAC3/latest/api/smac/runner/dask_runner/)
            *   [Exceptions](https://automl.github.io/SMAC3/latest/api/smac/runner/exceptions/)
            *   [Target function runner](https://automl.github.io/SMAC3/latest/api/smac/runner/target_function_runner/)
            *   [Target function script runner](https://automl.github.io/SMAC3/latest/api/smac/runner/target_function_script_runner/)

        *   - [x]  Utils   Utils  
            *   [Configspace](https://automl.github.io/SMAC3/latest/api/smac/utils/configspace/)
            *   [Data structures](https://automl.github.io/SMAC3/latest/api/smac/utils/data_structures/)
            *   [Logging](https://automl.github.io/SMAC3/latest/api/smac/utils/logging/)
            *   [Multi objective](https://automl.github.io/SMAC3/latest/api/smac/utils/multi_objective/)
            *   [Numpyencoder](https://automl.github.io/SMAC3/latest/api/smac/utils/numpyencoder/)
            *   [Pareto front](https://automl.github.io/SMAC3/latest/api/smac/utils/pareto_front/)
            *   - [x]  Subspaces   Subspaces  
                *   [Boing subspace](https://automl.github.io/SMAC3/latest/api/smac/utils/subspaces/boing_subspace/)
                *   [Turbo subspace](https://automl.github.io/SMAC3/latest/api/smac/utils/subspaces/turbo_subspace/)

*   - [x]  Info & FAQ   Info & FAQ  
    *   [References](https://automl.github.io/SMAC3/latest/6_references/)
    *   [Glossary](https://automl.github.io/SMAC3/latest/7_glossary/)
    *   [F.A.Q.](https://automl.github.io/SMAC3/latest/8_faq/)

Horseshoe prior
===============

smac.model.gaussian_process.priors.horseshoe_prior[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### HorseshoePrior[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior "Permanent link")

```
HorseshoePrior(scale: float, seed: int = 0)
```

Bases: `AbstractPrior`

Horseshoe Prior as it is used in spearmint.

##### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior--parameters "Permanent link")

scale: float Scaling parameter. seed : int, defaults to 0

Source code in `smac/model/gaussian_process/priors/horseshoe_prior.py`

[26](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-26)
[27](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-27)
[28](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-28)
[29](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-29)```
def __init__(self, scale: float, seed: int = 0):
    super().__init__(seed=seed)
    self._scale = scale
    self._scale_square = scale**2
```

#### get_gradient[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_gradient "Permanent link")

```
get_gradient(theta: float) -> float
```

Computes the gradient of the prior with respect to theta. Internally, his method calls `self._get_gradient`.

###### Warning[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_gradient--warning "Permanent link")

Theta must be on the original scale.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_gradient--parameters "Permanent link")

theta : float Hyperparameter configuration in log space

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_gradient--returns "Permanent link")

gradient : float The gradient of the prior at theta.

Source code in `smac/model/gaussian_process/priors/abstract_prior.py`

[87](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-87)
[88](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-88)
[89](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-89)
[90](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-90)
[91](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-91)
[92](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-92)
[93](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-93)
[94](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-94)
[95](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-95)
[96](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-96)
[97](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-97)
[98](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-98)
[99](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-99)
[100](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-100)
[101](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-101)
[102](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-102)
[103](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-103)
[104](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-104)```
def get_gradient(self, theta: float) -> float:
    """Computes the gradient of the prior with respect to theta. Internally, his method calls `self._get_gradient`.

    Warning
    -------
    Theta must be on the original scale.

    Parameters
    ----------
    theta : float
        Hyperparameter configuration in log space

    Returns
    -------
    gradient : float
        The gradient of the prior at theta.
    """
    return self._get_gradient(np.exp(theta))
```

#### get_log_probability[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_log_probability "Permanent link")

```
get_log_probability(theta: float) -> float
```

Returns the log probability of theta. This method exponentiates theta and calls `self._get_log_probability`.

###### Warning[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_log_probability--warning "Permanent link")

Theta must be on a log scale!

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_log_probability--parameters "Permanent link")

theta : float Hyperparameter configuration in log space.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.get_log_probability--returns "Permanent link")

float The log probability of theta

Source code in `smac/model/gaussian_process/priors/abstract_prior.py`

[68](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-68)
[69](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-69)
[70](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-70)
[71](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-71)
[72](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-72)
[73](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-73)
[74](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-74)
[75](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-75)
[76](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-76)
[77](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-77)
[78](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-78)
[79](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-79)
[80](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-80)
[81](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-81)
[82](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-82)
[83](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-83)
[84](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-84)
[85](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-85)```
def get_log_probability(self, theta: float) -> float:
    """Returns the log probability of theta. This method exponentiates theta and calls `self._get_log_probability`.

    Warning
    -------
    Theta must be on a log scale!

    Parameters
    ----------
    theta : float
        Hyperparameter configuration in log space.

    Returns
    -------
    float
        The log probability of theta
    """
    return self._get_log_probability(np.exp(theta))
```

#### sample_from_prior[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.sample_from_prior "Permanent link")

```
sample_from_prior(n_samples: int) -> ndarray
```

Returns `n_samples` from the prior. All samples are on a log scale. This method calls `self._sample_from_prior` and applies a log transformation to the obtained values.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.sample_from_prior--parameters "Permanent link")

n_samples : int The number of samples that will be drawn.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#smac.model.gaussian_process.priors.horseshoe_prior.HorseshoePrior.sample_from_prior--returns "Permanent link")

samples : np.ndarray

Source code in `smac/model/gaussian_process/priors/abstract_prior.py`

[42](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-42)
[43](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-43)
[44](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-44)
[45](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-45)
[46](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-46)
[47](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-47)
[48](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-48)
[49](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-49)
[50](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-50)
[51](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-51)
[52](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-52)
[53](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-53)
[54](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-54)
[55](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-55)
[56](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-56)
[57](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-57)
[58](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-58)
[59](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-59)
[60](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-60)
[61](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-61)
[62](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-62)
[63](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-63)
[64](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-64)
[65](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-65)
[66](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/#__codelineno-0-66)```
def sample_from_prior(self, n_samples: int) -> np.ndarray:
    """Returns `n_samples` from the prior. All samples are on a log scale. This method calls
    `self._sample_from_prior` and applies a log transformation to the obtained values.

    Parameters
    ----------
    n_samples : int
        The number of samples that will be drawn.

    Returns
    -------
    samples : np.ndarray
    """
    if np.ndim(n_samples) != 0:
        raise ValueError("argument n_samples needs to be a scalar (is %s)" % n_samples)

    if n_samples <= 0:
        raise ValueError("argument n_samples needs to be positive (is %d)" % n_samples)

    sample = np.log(self._sample_from_prior(n_samples=n_samples))

    if np.any(~np.isfinite(sample)):
        raise ValueError("Sample %s from prior %s contains infinite values!" % (sample, self))

    return sample
```

[Previous Gamma prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/gamma_prior/)[Next Log normal prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/log_normal_prior/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://github.com/automl "github.com")[](https://twitter.com/automl_org "twitter.com")

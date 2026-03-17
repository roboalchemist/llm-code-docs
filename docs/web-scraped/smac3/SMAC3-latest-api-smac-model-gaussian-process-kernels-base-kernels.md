# Source: https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/

Title: Base kernels - SMAC3

URL Source: https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/

Markdown Content:
Base kernels - SMAC3
===============
- [x] - [x] 

[Skip to content](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels)

[![Image 1: logo](https://automl.github.io/SMAC3/latest/images/logo.png)](https://automl.github.io/SMAC3/latest/ "SMAC3")

 SMAC3 

 Base kernels 

[](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/?q= "Share")

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
                    *   - [x]  Base kernels  [Base kernels](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/) Table of contents  
                        *   [base_kernels](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels)
                            *   [AbstractKernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel)
                                *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel--parameters)
                                *   [Attributes](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel--attributes)
                                *   [hyperparameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.hyperparameters)
                                *   [meta](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.meta)
                                *   [n_dims](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.n_dims)
                                *   [__call__](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.__call__)
                                *   [get_params](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.get_params)
                                    *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.get_params--parameters)
                                    *   [Returns](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.get_params--returns)

                            *   [ConstantKernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel)
                                *   [hyperparameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.hyperparameters)
                                *   [meta](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.meta)
                                *   [n_dims](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.n_dims)
                                *   [__call__](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.__call__)
                                    *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.__call__--parameters)
                                    *   [Returns](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.__call__--returns)

                                *   [get_params](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.get_params)
                                    *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.get_params--parameters)
                                    *   [Returns](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.get_params--returns)

                            *   [ProductKernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel)
                                *   [hyperparameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.hyperparameters)
                                *   [meta](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.meta)
                                *   [n_dims](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.n_dims)
                                *   [__call__](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.__call__)
                                    *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.__call__--parameters)
                                    *   [Returns](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.__call__--returns)

                                *   [get_params](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.get_params)
                                    *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.get_params--parameters)
                                    *   [Returns](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.get_params--returns)

                            *   [SumKernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel)
                                *   [hyperparameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.hyperparameters)
                                *   [meta](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.meta)
                                *   [n_dims](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.n_dims)
                                *   [__call__](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.__call__)
                                    *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.__call__--parameters)
                                    *   [Returns](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.__call__--returns)

                                *   [get_params](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.get_params)
                                    *   [Parameters](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.get_params--parameters)
                                    *   [Returns](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.get_params--returns)

                    *   [Hamming kernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/hamming_kernel/)
                    *   [Matern kernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/matern_kernel/)
                    *   [Rbf kernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/rbf_kernel/)
                    *   [White kernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/white_kernel/)

                *   - [x]  Priors   Priors  
                    *   [Abstract prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/abstract_prior/)
                    *   [Gamma prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/gamma_prior/)
                    *   [Horseshoe prior](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/priors/horseshoe_prior/)
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

Base kernels
============

smac.model.gaussian_process.kernels.base_kernels[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### AbstractKernel[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel "Permanent link")

```
AbstractKernel(
    *,
    operate_on: ndarray | None = None,
    has_conditions: bool = False,
    prior: AbstractPrior | None = None,
    **kwargs: Any
)
```

This is a mixin for a kernel to override functions of the kernel. Because it overrides functions of the kernel, it needs to be placed first in the inheritance hierarchy. For this reason it is not possible to subclass the Mixin from the kernel class because this will prevent it from being instantiatable. Therefore, mypy won't know about anything related to the superclass and some type:ignore statements has to be added when accessing a member that is declared in the superclass such as `self.has_conditions`, `self._call`, `super().get_params`, etc.

##### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel--parameters "Permanent link")

operate_on : np.ndarray, defaults to None On which numpy array should be operated on. has_conditions : bool, defaults to False Whether the kernel has conditions. prior : AbstractPrior, defaults to None Which prior the kernel is using.

##### Attributes[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel--attributes "Permanent link")

operate_on : np.ndarray, defaults to None On which numpy array should be operated on. has_conditions : bool, defaults to False Whether the kernel has conditions. Might be changed by the gaussian process. prior : AbstractPrior, defaults to None Which prior the kernel is using. Primarily used by sklearn.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[45](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-45)
[46](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-46)
[47](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-47)
[48](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-48)
[49](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-49)
[50](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-50)
[51](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-51)
[52](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-52)
[53](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-53)
[54](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-54)
[55](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-55)
[56](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-56)
[57](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-57)
[58](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-58)
[59](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-59)
[60](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-60)
[61](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-61)
[62](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-62)
[63](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-63)
[64](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-64)
[65](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-65)```
def __init__(
    self,
    *,
    operate_on: np.ndarray | None = None,
    has_conditions: bool = False,
    prior: AbstractPrior | None = None,
    **kwargs: Any,
) -> None:
    self.operate_on = operate_on
    self.has_conditions = has_conditions
    self.prior = prior
    self._set_active_dims(operate_on)

    # Since this class is a mixin, we just pass all the other parameters to the next class.
    super().__init__(**kwargs)

    # Get variables from next class:
    # We make it explicit here to make sure the next class really has this attributes.
    self._hyperparameters: list[kernels.Hyperparameter] = super().hyperparameters  # type: ignore
    self._n_dims: int = super().n_dims  # type: ignore
    self._len_active: int | None
```

#### hyperparameters`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.hyperparameters "Permanent link")

```
hyperparameters: list[Hyperparameter]
```

Returns a list of all hyperparameter specifications.

#### meta`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.meta "Permanent link")

```
meta: dict[str, Any]
```

Returns the meta data of the created object. This method calls the `get_params` method to collect the parameters of the kernel.

#### n_dims`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.n_dims "Permanent link")

```
n_dims: int
```

Returns the number of non-fixed hyperparameters of the kernel.

#### __call__ [#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.__call__ "Permanent link")

```
__call__(
    X: ndarray,
    Y: ndarray | None = None,
    eval_gradient: bool = False,
    active: ndarray | None = None,
) -> ndarray | tuple[ndarray, ndarray]
```

Call the kernel function. Internally, `self._call` is called, which must be specified by a subclass.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[130](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-130)
[131](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-131)
[132](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-132)
[133](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-133)
[134](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-134)
[135](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-135)
[136](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-136)
[137](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-137)
[138](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-138)
[139](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-139)
[140](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-140)
[141](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-141)
[142](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-142)
[143](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-143)
[144](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-144)
[145](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-145)
[146](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-146)
[147](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-147)
[148](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-148)
[149](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-149)
[150](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-150)
[151](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-151)
[152](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-152)
[153](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-153)
[154](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-154)
[155](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-155)
[156](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-156)
[157](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-157)
[158](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-158)
[159](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-159)
[160](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-160)
[161](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-161)
[162](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-162)
[163](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-163)
[164](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-164)
[165](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-165)
[166](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-166)
[167](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-167)
[168](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-168)
[169](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-169)
[170](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-170)
[171](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-171)```
def __call__(
    self,
    X: np.ndarray,
    Y: np.ndarray | None = None,
    eval_gradient: bool = False,
    active: np.ndarray | None = None,
) -> np.ndarray | tuple[np.ndarray, np.ndarray]:
    """Call the kernel function. Internally, `self._call` is called, which must be specified by a subclass."""
    if active is None and self.has_conditions:
        if self.operate_on is None:
            active = get_conditional_hyperparameters(X, Y)
        else:
            if Y is None:
                active = get_conditional_hyperparameters(X[:, self.operate_on], None)
            else:
                active = get_conditional_hyperparameters(X[:, self.operate_on], Y[:, self.operate_on])

    if self.operate_on is None:
        rval = self._call(X, Y, eval_gradient, active)
    else:
        if self._len_active is None:
            raise RuntimeError("The internal variable `_len_active` is not set.")

        if Y is None:
            rval = self._call(
                X=X[:, self.operate_on].reshape([-1, self._len_active]),
                Y=None,
                eval_gradient=eval_gradient,
                active=active,
            )
            X = X[:, self.operate_on].reshape((-1, self._len_active))
        else:
            rval = self._call(
                X=X[:, self.operate_on].reshape([-1, self._len_active]),
                Y=Y[:, self.operate_on].reshape([-1, self._len_active]),
                eval_gradient=eval_gradient,
                active=active,
            )
            X = X[:, self.operate_on].reshape((-1, self._len_active))
            Y = Y[:, self.operate_on].reshape((-1, self._len_active))

    return rval
```

#### get_params[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.get_params "Permanent link")

```
get_params(deep: bool = True) -> dict[str, Any]
```

Get parameters of this kernel.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.get_params--parameters "Permanent link")

deep : bool, defaults to True If True, will return the parameters for this estimator and contained subobjects that are estimators.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.AbstractKernel.get_params--returns "Permanent link")

params : dict[str, Any] Parameter names mapped to their values.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[99](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-99)
[100](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-100)
[101](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-101)
[102](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-102)
[103](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-103)
[104](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-104)
[105](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-105)
[106](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-106)
[107](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-107)
[108](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-108)
[109](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-109)
[110](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-110)
[111](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-111)
[112](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-112)
[113](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-113)
[114](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-114)
[115](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-115)
[116](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-116)
[117](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-117)
[118](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-118)
[119](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-119)
[120](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-120)
[121](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-121)
[122](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-122)
[123](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-123)
[124](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-124)
[125](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-125)
[126](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-126)
[127](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-127)
[128](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-128)```
def get_params(self, deep: bool = True) -> dict[str, Any]:
    """Get parameters of this kernel.

    Parameters
    ----------
    deep : bool, defaults to True
        If True, will return the parameters for this estimator and
        contained subobjects that are estimators.

    Returns
    -------
    params : dict[str, Any]
        Parameter names mapped to their values.
    """
    params = {}

    # ignore[misc] looks like it catches all kinds of errors, but misc is actually a category from mypy:
    # https://mypy.readthedocs.io/en/latest/error_code_list.html#miscellaneous-checks-misc
    tmp = super().get_params(deep)  # type: ignore[misc] # noqa F821
    args = list(tmp.keys())

    # Sum and Product do not clone the 'has_conditions' attribute by default. Instead of changing their
    # get_params() method, we simply add the attribute here!
    if "has_conditions" not in args:
        args.append("has_conditions")

    for arg in args:
        params[arg] = getattr(self, arg, None)

    return params
```

### ConstantKernel[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel "Permanent link")

```
ConstantKernel(
    constant_value: float = 1.0,
    constant_value_bounds: tuple[float, float] = (
        1e-05,
        100000.0,
    ),
    operate_on: ndarray | None = None,
    has_conditions: bool = False,
    prior: AbstractPrior | None = None,
)
```

Bases: `AbstractKernel`, `ConstantKernel`

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[390](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-390)
[391](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-391)
[392](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-392)
[393](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-393)
[394](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-394)
[395](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-395)
[396](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-396)
[397](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-397)
[398](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-398)
[399](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-399)
[400](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-400)
[401](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-401)
[402](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-402)
[403](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-403)
[404](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-404)```
def __init__(
    self,
    constant_value: float = 1.0,
    constant_value_bounds: tuple[float, float] = (1e-5, 1e5),
    operate_on: np.ndarray | None = None,
    has_conditions: bool = False,
    prior: AbstractPrior | None = None,
) -> None:
    super().__init__(
        operate_on=operate_on,
        has_conditions=has_conditions,
        prior=prior,
        constant_value=constant_value,
        constant_value_bounds=constant_value_bounds,
    )
```

#### hyperparameters`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.hyperparameters "Permanent link")

```
hyperparameters: list[Hyperparameter]
```

Returns a list of all hyperparameter specifications.

#### meta`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.meta "Permanent link")

```
meta: dict[str, Any]
```

Returns the meta data of the created object. This method calls the `get_params` method to collect the parameters of the kernel.

#### n_dims`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.n_dims "Permanent link")

```
n_dims: int
```

Returns the number of non-fixed hyperparameters of the kernel.

#### __call__ [#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.__call__ "Permanent link")

```
__call__(
    X: ndarray,
    Y: ndarray | None = None,
    eval_gradient: bool = False,
    active: ndarray | None = None,
) -> ndarray | tuple[ndarray, ndarray]
```

Return the kernel k(X, Y) and optionally its gradient.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.__call__--parameters "Permanent link")

X : np.ndarray, shape (n_samples_X, n_features) Left argument of the returned kernel k(X, Y).

np.ndarray, shape (n_samples_Y, n_features), (optional, default=None)
Right argument of the returned kernel k(X, Y). If None, k(X, X) is evaluated instead.

bool (optional, default=False)
Determines whether the gradient with respect to the kernel hyperparameter is determined. Only supported when Y is None.

np.ndarray (n_samples_X, n_features) (optional)
Boolean array specifying which hyperparameters are active.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.__call__--returns "Permanent link")

K : np.ndarray, shape (n_samples_X, n_samples_Y) Kernel k(X, Y).

np.ndarray (opt.), shape (n_samples_X, n_samples_X, n_dims)
The gradient of the kernel k(X, X) with respect to the hyperparameter of the kernel. Only returned when eval_gradient is True.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[406](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-406)
[407](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-407)
[408](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-408)
[409](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-409)
[410](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-410)
[411](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-411)
[412](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-412)
[413](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-413)
[414](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-414)
[415](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-415)
[416](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-416)
[417](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-417)
[418](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-418)
[419](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-419)
[420](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-420)
[421](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-421)
[422](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-422)
[423](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-423)
[424](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-424)
[425](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-425)
[426](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-426)
[427](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-427)
[428](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-428)
[429](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-429)
[430](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-430)
[431](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-431)
[432](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-432)
[433](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-433)
[434](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-434)
[435](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-435)
[436](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-436)
[437](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-437)
[438](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-438)
[439](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-439)
[440](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-440)
[441](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-441)
[442](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-442)
[443](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-443)
[444](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-444)
[445](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-445)
[446](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-446)
[447](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-447)
[448](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-448)
[449](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-449)
[450](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-450)
[451](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-451)
[452](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-452)
[453](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-453)
[454](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-454)
[455](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-455)
[456](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-456)
[457](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-457)
[458](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-458)
[459](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-459)
[460](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-460)
[461](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-461)
[462](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-462)
[463](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-463)
[464](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-464)
[465](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-465)```
def __call__(
    self,
    X: np.ndarray,
    Y: np.ndarray | None = None,
    eval_gradient: bool = False,
    active: np.ndarray | None = None,
) -> np.ndarray | tuple[np.ndarray, np.ndarray]:
    """Return the kernel k(X, Y) and optionally its gradient.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples_X, n_features)
        Left argument of the returned kernel k(X, Y).

    Y : np.ndarray, shape (n_samples_Y, n_features), (optional, default=None)
        Right argument of the returned kernel k(X, Y). If None, k(X, X)
        is evaluated instead.

    eval_gradient : bool (optional, default=False)
        Determines whether the gradient with respect to the kernel
        hyperparameter is determined. Only supported when Y is None.

    active : np.ndarray (n_samples_X, n_features) (optional)
        Boolean array specifying which hyperparameters are active.

    Returns
    -------
    K : np.ndarray, shape (n_samples_X, n_samples_Y)
        Kernel k(X, Y).

    K_gradient : np.ndarray (opt.), shape (n_samples_X, n_samples_X, n_dims)
        The gradient of the kernel k(X, X) with respect to the
        hyperparameter of the kernel. Only returned when eval_gradient
        is True.
    """
    X = np.atleast_2d(X)
    if Y is None:
        Y = X
    elif eval_gradient:
        raise ValueError("Gradient can only be evaluated when Y is None.")

    K = np.full(
        (X.shape[0], Y.shape[0]),
        self.constant_value,
        dtype=np.array(self.constant_value).dtype,
    )
    if eval_gradient:
        if not self.hyperparameter_constant_value.fixed:
            return (
                K,
                np.full(
                    (X.shape[0], X.shape[0], 1),
                    self.constant_value,
                    dtype=np.array(self.constant_value).dtype,
                ),
            )
        else:
            return K, np.empty((X.shape[0], X.shape[0], 0))
    else:
        return K
```

#### get_params[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.get_params "Permanent link")

```
get_params(deep: bool = True) -> dict[str, Any]
```

Get parameters of this kernel.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.get_params--parameters "Permanent link")

deep : bool, defaults to True If True, will return the parameters for this estimator and contained subobjects that are estimators.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ConstantKernel.get_params--returns "Permanent link")

params : dict[str, Any] Parameter names mapped to their values.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[99](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-99)
[100](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-100)
[101](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-101)
[102](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-102)
[103](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-103)
[104](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-104)
[105](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-105)
[106](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-106)
[107](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-107)
[108](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-108)
[109](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-109)
[110](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-110)
[111](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-111)
[112](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-112)
[113](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-113)
[114](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-114)
[115](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-115)
[116](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-116)
[117](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-117)
[118](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-118)
[119](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-119)
[120](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-120)
[121](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-121)
[122](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-122)
[123](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-123)
[124](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-124)
[125](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-125)
[126](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-126)
[127](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-127)
[128](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-128)```
def get_params(self, deep: bool = True) -> dict[str, Any]:
    """Get parameters of this kernel.

    Parameters
    ----------
    deep : bool, defaults to True
        If True, will return the parameters for this estimator and
        contained subobjects that are estimators.

    Returns
    -------
    params : dict[str, Any]
        Parameter names mapped to their values.
    """
    params = {}

    # ignore[misc] looks like it catches all kinds of errors, but misc is actually a category from mypy:
    # https://mypy.readthedocs.io/en/latest/error_code_list.html#miscellaneous-checks-misc
    tmp = super().get_params(deep)  # type: ignore[misc] # noqa F821
    args = list(tmp.keys())

    # Sum and Product do not clone the 'has_conditions' attribute by default. Instead of changing their
    # get_params() method, we simply add the attribute here!
    if "has_conditions" not in args:
        args.append("has_conditions")

    for arg in args:
        params[arg] = getattr(self, arg, None)

    return params
```

### ProductKernel[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel "Permanent link")

```
ProductKernel(
    k1: Kernel,
    k2: Kernel,
    operate_on: ndarray | None = None,
    has_conditions: bool = False,
)
```

Bases: `AbstractKernel`, `Product`

Product kernel implementation.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[331](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-331)
[332](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-332)
[333](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-333)
[334](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-334)
[335](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-335)
[336](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-336)
[337](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-337)
[338](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-338)
[339](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-339)
[340](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-340)
[341](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-341)
[342](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-342)
[343](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-343)```
def __init__(
    self,
    k1: kernels.Kernel,
    k2: kernels.Kernel,
    operate_on: np.ndarray | None = None,
    has_conditions: bool = False,
) -> None:
    super().__init__(
        operate_on=operate_on,
        has_conditions=has_conditions,
        k1=k1,
        k2=k2,
    )
```

#### hyperparameters`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.hyperparameters "Permanent link")

```
hyperparameters: list[Hyperparameter]
```

Returns a list of all hyperparameter specifications.

#### meta`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.meta "Permanent link")

```
meta: dict[str, Any]
```

Returns the meta data of the created object. This method calls the `get_params` method to collect the parameters of the kernel.

#### n_dims`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.n_dims "Permanent link")

```
n_dims: int
```

Returns the number of non-fixed hyperparameters of the kernel.

#### __call__ [#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.__call__ "Permanent link")

```
__call__(
    X: ndarray,
    Y: ndarray | None = None,
    eval_gradient: bool = False,
    active: ndarray | None = None,
) -> ndarray | tuple[ndarray, ndarray]
```

Return the kernel k(X, Y) and optionally its gradient.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.__call__--parameters "Permanent link")

X : np.ndarray, shape (n_samples_X, n_features) Left argument of the returned kernel k(X, Y).

np.ndarray, shape (n_samples_Y, n_features), (optional, default=None)
Right argument of the returned kernel k(X, Y). If None, k(X, X) is evaluated instead.

bool (optional, default=False)
Determines whether the gradient with respect to the kernel hyperparameter is determined.

np.ndarray (n_samples_X, n_features) (optional)
Boolean array specifying which hyperparameters are active.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.__call__--returns "Permanent link")

K : np.ndarray, shape (n_samples_X, n_samples_Y) Kernel k(X, Y).

np.ndarray (opt.), shape (n_samples_X, n_samples_X, n_dims)
The gradient of the kernel k(X, X) with respect to the hyperparameter of the kernel. Only returned when eval_gradient is True.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[345](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-345)
[346](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-346)
[347](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-347)
[348](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-348)
[349](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-349)
[350](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-350)
[351](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-351)
[352](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-352)
[353](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-353)
[354](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-354)
[355](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-355)
[356](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-356)
[357](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-357)
[358](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-358)
[359](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-359)
[360](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-360)
[361](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-361)
[362](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-362)
[363](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-363)
[364](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-364)
[365](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-365)
[366](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-366)
[367](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-367)
[368](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-368)
[369](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-369)
[370](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-370)
[371](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-371)
[372](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-372)
[373](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-373)
[374](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-374)
[375](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-375)
[376](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-376)
[377](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-377)
[378](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-378)
[379](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-379)
[380](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-380)
[381](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-381)
[382](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-382)
[383](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-383)
[384](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-384)
[385](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-385)
[386](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-386)```
def __call__(
    self,
    X: np.ndarray,
    Y: np.ndarray | None = None,
    eval_gradient: bool = False,
    active: np.ndarray | None = None,
) -> np.ndarray | tuple[np.ndarray, np.ndarray]:
    """Return the kernel k(X, Y) and optionally its gradient.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples_X, n_features)
        Left argument of the returned kernel k(X, Y).

    Y : np.ndarray, shape (n_samples_Y, n_features), (optional, default=None)
        Right argument of the returned kernel k(X, Y). If None, k(X, X)
        is evaluated instead.

    eval_gradient : bool (optional, default=False)
        Determines whether the gradient with respect to the kernel
        hyperparameter is determined.

    active : np.ndarray (n_samples_X, n_features) (optional)
        Boolean array specifying which hyperparameters are active.

    Returns
    -------
    K : np.ndarray, shape (n_samples_X, n_samples_Y)
        Kernel k(X, Y).

    K_gradient : np.ndarray (opt.), shape (n_samples_X, n_samples_X, n_dims)
        The gradient of the kernel k(X, X) with respect to the
        hyperparameter of the kernel. Only returned when eval_gradient
        is True.
    """
    if eval_gradient:
        K1, K1_gradient = self.k1(X, Y, eval_gradient=True, active=active)
        K2, K2_gradient = self.k2(X, Y, eval_gradient=True, active=active)

        return K1 * K2, np.dstack((K1_gradient * K2[:, :, np.newaxis], K2_gradient * K1[:, :, np.newaxis]))
    else:
        return self.k1(X, Y, active=active) * self.k2(X, Y, active=active)
```

#### get_params[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.get_params "Permanent link")

```
get_params(deep: bool = True) -> dict[str, Any]
```

Get parameters of this kernel.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.get_params--parameters "Permanent link")

deep : bool, defaults to True If True, will return the parameters for this estimator and contained subobjects that are estimators.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.ProductKernel.get_params--returns "Permanent link")

params : dict[str, Any] Parameter names mapped to their values.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[99](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-99)
[100](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-100)
[101](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-101)
[102](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-102)
[103](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-103)
[104](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-104)
[105](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-105)
[106](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-106)
[107](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-107)
[108](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-108)
[109](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-109)
[110](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-110)
[111](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-111)
[112](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-112)
[113](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-113)
[114](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-114)
[115](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-115)
[116](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-116)
[117](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-117)
[118](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-118)
[119](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-119)
[120](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-120)
[121](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-121)
[122](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-122)
[123](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-123)
[124](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-124)
[125](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-125)
[126](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-126)
[127](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-127)
[128](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-128)```
def get_params(self, deep: bool = True) -> dict[str, Any]:
    """Get parameters of this kernel.

    Parameters
    ----------
    deep : bool, defaults to True
        If True, will return the parameters for this estimator and
        contained subobjects that are estimators.

    Returns
    -------
    params : dict[str, Any]
        Parameter names mapped to their values.
    """
    params = {}

    # ignore[misc] looks like it catches all kinds of errors, but misc is actually a category from mypy:
    # https://mypy.readthedocs.io/en/latest/error_code_list.html#miscellaneous-checks-misc
    tmp = super().get_params(deep)  # type: ignore[misc] # noqa F821
    args = list(tmp.keys())

    # Sum and Product do not clone the 'has_conditions' attribute by default. Instead of changing their
    # get_params() method, we simply add the attribute here!
    if "has_conditions" not in args:
        args.append("has_conditions")

    for arg in args:
        params[arg] = getattr(self, arg, None)

    return params
```

### SumKernel[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel "Permanent link")

```
SumKernel(
    k1: Kernel,
    k2: Kernel,
    operate_on: ndarray | None = None,
    has_conditions: bool = False,
)
```

Bases: `AbstractKernel`, `Sum`

Sum kernel implementation.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[270](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-270)
[271](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-271)
[272](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-272)
[273](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-273)
[274](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-274)
[275](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-275)
[276](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-276)
[277](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-277)
[278](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-278)
[279](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-279)
[280](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-280)
[281](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-281)
[282](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-282)```
def __init__(
    self,
    k1: kernels.Kernel,
    k2: kernels.Kernel,
    operate_on: np.ndarray | None = None,
    has_conditions: bool = False,
) -> None:
    super().__init__(
        operate_on=operate_on,
        has_conditions=has_conditions,
        k1=k1,
        k2=k2,
    )
```

#### hyperparameters`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.hyperparameters "Permanent link")

```
hyperparameters: list[Hyperparameter]
```

Returns a list of all hyperparameter specifications.

#### meta`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.meta "Permanent link")

```
meta: dict[str, Any]
```

Returns the meta data of the created object. This method calls the `get_params` method to collect the parameters of the kernel.

#### n_dims`property`[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.n_dims "Permanent link")

```
n_dims: int
```

Returns the number of non-fixed hyperparameters of the kernel.

#### __call__ [#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.__call__ "Permanent link")

```
__call__(
    X: ndarray,
    Y: ndarray | None = None,
    eval_gradient: bool = False,
    active: ndarray | None = None,
) -> ndarray | tuple[ndarray, ndarray]
```

Return the kernel k(X, Y) and optionally its gradient.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.__call__--parameters "Permanent link")

X : np.ndarray, shape (n_samples_X, n_features) Left argument of the returned kernel k(X, Y).

np.ndarray, shape (n_samples_Y, n_features), (optional, default=None)
Right argument of the returned kernel k(X, Y). If None, k(X, X) is evaluated instead.

bool (optional, default=False)
Determines whether the gradient with respect to the kernel hyperparameter is determined.

np.ndarray (n_samples_X, n_features) (optional)
Boolean array specifying which hyperparameters are active.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.__call__--returns "Permanent link")

K : np.ndarray, shape (n_samples_X, n_samples_Y) Kernel k(X, Y).

np.ndarray (opt.), shape (n_samples_X, n_samples_X, n_dims)
The gradient of the kernel k(X, X) with respect to the hyperparameter of the kernel. Only returned when eval_gradient is True.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[284](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-284)
[285](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-285)
[286](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-286)
[287](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-287)
[288](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-288)
[289](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-289)
[290](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-290)
[291](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-291)
[292](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-292)
[293](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-293)
[294](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-294)
[295](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-295)
[296](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-296)
[297](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-297)
[298](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-298)
[299](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-299)
[300](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-300)
[301](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-301)
[302](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-302)
[303](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-303)
[304](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-304)
[305](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-305)
[306](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-306)
[307](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-307)
[308](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-308)
[309](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-309)
[310](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-310)
[311](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-311)
[312](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-312)
[313](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-313)
[314](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-314)
[315](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-315)
[316](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-316)
[317](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-317)
[318](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-318)
[319](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-319)
[320](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-320)
[321](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-321)
[322](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-322)
[323](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-323)
[324](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-324)
[325](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-325)```
def __call__(
    self,
    X: np.ndarray,
    Y: np.ndarray | None = None,
    eval_gradient: bool = False,
    active: np.ndarray | None = None,
) -> np.ndarray | tuple[np.ndarray, np.ndarray]:
    """Return the kernel k(X, Y) and optionally its gradient.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples_X, n_features)
        Left argument of the returned kernel k(X, Y).

    Y : np.ndarray, shape (n_samples_Y, n_features), (optional, default=None)
        Right argument of the returned kernel k(X, Y). If None, k(X, X)
        is evaluated instead.

    eval_gradient : bool (optional, default=False)
        Determines whether the gradient with respect to the kernel
        hyperparameter is determined.

    active : np.ndarray (n_samples_X, n_features) (optional)
        Boolean array specifying which hyperparameters are active.

    Returns
    -------
    K : np.ndarray, shape (n_samples_X, n_samples_Y)
        Kernel k(X, Y).

    K_gradient : np.ndarray (opt.), shape (n_samples_X, n_samples_X, n_dims)
        The gradient of the kernel k(X, X) with respect to the
        hyperparameter of the kernel. Only returned when eval_gradient
        is True.
    """
    if eval_gradient:
        K1, K1_gradient = self.k1(X, Y, eval_gradient=True, active=active)
        K2, K2_gradient = self.k2(X, Y, eval_gradient=True, active=active)

        return K1 + K2, np.dstack((K1_gradient, K2_gradient))
    else:
        return self.k1(X, Y, active=active) + self.k2(X, Y, active=active)
```

#### get_params[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.get_params "Permanent link")

```
get_params(deep: bool = True) -> dict[str, Any]
```

Get parameters of this kernel.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.get_params--parameters "Permanent link")

deep : bool, defaults to True If True, will return the parameters for this estimator and contained subobjects that are estimators.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#smac.model.gaussian_process.kernels.base_kernels.SumKernel.get_params--returns "Permanent link")

params : dict[str, Any] Parameter names mapped to their values.

Source code in `smac/model/gaussian_process/kernels/base_kernels.py`

[99](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-99)
[100](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-100)
[101](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-101)
[102](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-102)
[103](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-103)
[104](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-104)
[105](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-105)
[106](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-106)
[107](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-107)
[108](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-108)
[109](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-109)
[110](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-110)
[111](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-111)
[112](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-112)
[113](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-113)
[114](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-114)
[115](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-115)
[116](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-116)
[117](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-117)
[118](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-118)
[119](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-119)
[120](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-120)
[121](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-121)
[122](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-122)
[123](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-123)
[124](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-124)
[125](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-125)
[126](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-126)
[127](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-127)
[128](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/base_kernels/#__codelineno-0-128)```
def get_params(self, deep: bool = True) -> dict[str, Any]:
    """Get parameters of this kernel.

    Parameters
    ----------
    deep : bool, defaults to True
        If True, will return the parameters for this estimator and
        contained subobjects that are estimators.

    Returns
    -------
    params : dict[str, Any]
        Parameter names mapped to their values.
    """
    params = {}

    # ignore[misc] looks like it catches all kinds of errors, but misc is actually a category from mypy:
    # https://mypy.readthedocs.io/en/latest/error_code_list.html#miscellaneous-checks-misc
    tmp = super().get_params(deep)  # type: ignore[misc] # noqa F821
    args = list(tmp.keys())

    # Sum and Product do not clone the 'has_conditions' attribute by default. Instead of changing their
    # get_params() method, we simply add the attribute here!
    if "has_conditions" not in args:
        args.append("has_conditions")

    for arg in args:
        params[arg] = getattr(self, arg, None)

    return params
```

[Previous Mcmc gaussian process](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/mcmc_gaussian_process/)[Next Hamming kernel](https://automl.github.io/SMAC3/latest/api/smac/model/gaussian_process/kernels/hamming_kernel/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://github.com/automl "github.com")[](https://twitter.com/automl_org "twitter.com")

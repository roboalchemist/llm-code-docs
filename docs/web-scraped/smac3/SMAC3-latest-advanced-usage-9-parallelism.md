# Source: https://automl.github.io/SMAC3/latest/advanced_usage/9_parallelism/

Title: Parallelism - SMAC3

URL Source: https://automl.github.io/SMAC3/latest/advanced_usage/9_parallelism/

Markdown Content:
Parallelism - SMAC3
===============
- [x] - [x] 

[Skip to content](https://automl.github.io/SMAC3/latest/advanced_usage/9_parallelism/#parallelism)

[![Image 1: logo](https://automl.github.io/SMAC3/latest/images/logo.png)](https://automl.github.io/SMAC3/latest/ "SMAC3")

 SMAC3 

 Parallelism 

[](https://automl.github.io/SMAC3/latest/advanced_usage/9_parallelism/?q= "Share")

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
    *   - [x]  Parallelism  [Parallelism](https://automl.github.io/SMAC3/latest/advanced_usage/9_parallelism/) Table of contents  
        *   [Running on a Cluster](https://automl.github.io/SMAC3/latest/advanced_usage/9_parallelism/#running-on-a-cluster)

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

Parallelism[#](https://automl.github.io/SMAC3/latest/advanced_usage/9_parallelism/#parallelism "Permanent link")
================================================================================================================

SMAC supports multiple workers natively via Dask. Just specify `n_workers` in the scenario and you are ready to go.

Note

Please keep in mind that additional workers are only used to evaluate trials. The main thread still orchestrates the optimization process, including training the surrogate model.

Warning

Using high number of workers when the target function evaluation is fast might be counterproductive due to the overhead of communcation. Consider using only one worker in this case.

Warning

When using multiple workers, SMAC is not reproducible anymore.

Running on a Cluster[#](https://automl.github.io/SMAC3/latest/advanced_usage/9_parallelism/#running-on-a-cluster "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------

You can also pass a custom dask client, e.g. to run on a slurm cluster. See our [parallelism example](https://automl.github.io/SMAC3/latest/examples/1%20Basics/7_parallelization_cluster/).

Warning

On some clusters you cannot spawn new jobs when running a SLURMCluster inside a job instead of on the login node. No obvious errors might be raised but it can hang silently.

Warning

Sometimes you need to modify your launch command which can be done with `SLURMCluster.job_class.submit_command`.

```
cluster.job_cls.submit_command = submit_command
cluster.job_cls.cancel_command = cancel_command
```

[Previous Logging](https://automl.github.io/SMAC3/latest/advanced_usage/8_logging/)[Next Continue](https://automl.github.io/SMAC3/latest/advanced_usage/10_continue/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://github.com/automl "github.com")[](https://twitter.com/automl_org "twitter.com")

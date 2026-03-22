# Source: https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/

Title: Hyperband facade - SMAC3

URL Source: https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/

Markdown Content:
```
HyperbandFacade(
    scenario: Scenario,
    target_function: Callable | str | AbstractRunner,
    *,
    model: AbstractModel | None = None,
    acquisition_function: AbstractAcquisitionFunction
    | None = None,
    acquisition_maximizer: AbstractAcquisitionMaximizer
    | None = None,
    initial_design: AbstractInitialDesign | None = None,
    random_design: AbstractRandomDesign | None = None,
    intensifier: AbstractIntensifier | None = None,
    multi_objective_algorithm: AbstractMultiObjectiveAlgorithm
    | None = None,
    runhistory_encoder: AbstractRunHistoryEncoder
    | None = None,
    config_selector: ConfigSelector | None = None,
    logging_level: int
    | Path
    | Literal[False]
    | None = None,
    callbacks: list[Callback] = None,
    overwrite: bool = False,
    dask_client: Client | None = None
)
```

Bases: `RandomFacade`

Facade to use model-free Hyperband [[LJDR18](https://automl.github.io/SMAC3/latest/6_references/#LJDR18)] for algorithm configuration.

Uses Random Aggressive Online Racing (ROAR) to compare configurations, a random initial design and the Hyperband intensifier.

Warning

`smac.main.config_selector.ConfigSelector` contains the `min_trials` parameter. This parameter determines how many samples are required to train the surrogate model. If budgets are involved, the highest budgets are checked first. For example, if min_trials is three, but we find only two trials in the runhistory for the highest budget, we will use trials of a lower budget instead.

Source code in `smac/facade/abstract_facade.py`

```
def __init__(
    self,
    scenario: Scenario,
    target_function: Callable | str | AbstractRunner,
    *,
    model: AbstractModel | None = None,
    acquisition_function: AbstractAcquisitionFunction | None = None,
    acquisition_maximizer: AbstractAcquisitionMaximizer | None = None,
    initial_design: AbstractInitialDesign | None = None,
    random_design: AbstractRandomDesign | None = None,
    intensifier: AbstractIntensifier | None = None,
    multi_objective_algorithm: AbstractMultiObjectiveAlgorithm | None = None,
    runhistory_encoder: AbstractRunHistoryEncoder | None = None,
    config_selector: ConfigSelector | None = None,
    logging_level: int | Path | Literal[False] | None = None,
    callbacks: list[Callback] = None,
    overwrite: bool = False,
    dask_client: Client | None = None,
):
    setup_logging(logging_level)

    if callbacks is None:
        callbacks = []

    if model is None:
        model = self.get_model(scenario)

    if acquisition_function is None:
        acquisition_function = self.get_acquisition_function(scenario)

    if acquisition_maximizer is None:
        acquisition_maximizer = self.get_acquisition_maximizer(scenario)

    if initial_design is None:
        initial_design = self.get_initial_design(scenario)

    if random_design is None:
        random_design = self.get_random_design(scenario)

    if intensifier is None:
        intensifier = self.get_intensifier(scenario)

    if multi_objective_algorithm is None and scenario.count_objectives() > 1:
        multi_objective_algorithm = self.get_multi_objective_algorithm(scenario=scenario)

    if runhistory_encoder is None:
        runhistory_encoder = self.get_runhistory_encoder(scenario)

    if config_selector is None:
        config_selector = self.get_config_selector(scenario)

    # Initialize empty stats and runhistory object
    runhistory = RunHistory(multi_objective_algorithm=multi_objective_algorithm)

    # Set the seed for configuration space
    scenario.configspace.seed(scenario.seed)

    # Set variables globally
    self._scenario = scenario
    self._model = model
    self._acquisition_function = acquisition_function
    self._acquisition_maximizer = acquisition_maximizer
    self._initial_design = initial_design
    self._random_design = random_design
    self._intensifier = intensifier
    self._multi_objective_algorithm = multi_objective_algorithm
    self._runhistory = runhistory
    self._runhistory_encoder = runhistory_encoder
    self._config_selector = config_selector
    self._callbacks = callbacks
    self._overwrite = overwrite

    # Prepare the algorithm executer
    runner: AbstractRunner
    if isinstance(target_function, AbstractRunner):
        runner = target_function
    elif isinstance(target_function, str):
        runner = TargetFunctionScriptRunner(
            scenario=scenario,
            target_function=target_function,
            required_arguments=self._get_signature_arguments(),
        )
    else:
        runner = TargetFunctionRunner(
            scenario=scenario,
            target_function=target_function,
            required_arguments=self._get_signature_arguments(),
        )

    # In case of multiple jobs, we need to wrap the runner again using DaskParallelRunner
    if (n_workers := scenario.n_workers) > 1 or dask_client is not None:
        if dask_client is not None and n_workers > 1:
            logger.warning(
                "Provided `dask_client`. Ignore `scenario.n_workers`, directly set `n_workers` in `dask_client`."
            )
        else:
            available_workers = joblib.cpu_count()
            if n_workers > available_workers:
                logger.info(f"Workers are reduced to {n_workers}.")
                n_workers = available_workers

        # We use a dask runner for parallelization
        runner = DaskParallelRunner(single_worker=runner, dask_client=dask_client)

    # Set the runner to access it globally
    self._runner = runner

    # Adding dependencies of the components
    self._update_dependencies()

    # We have to update our meta data (basically arguments of the components)
    self._scenario._set_meta(self.meta)

    # We have to validate if the object compositions are correct and actually make sense
    self._validate()

    # Finally we configure our optimizer
    self._optimizer = self._get_optimizer()
    assert self._optimizer

    # Register callbacks here
    for callback in callbacks:
        self._optimizer.register_callback(callback)

    # Additionally, we register the runhistory callback from the intensifier to efficiently update our incumbent
    # every time new information are available
    self._optimizer.register_callback(self._intensifier.get_callback(), index=0)
```

#### intensifier`property`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.intensifier "Permanent link")

The optimizer which is responsible for the BO loop. Keeps track of useful information like status.

#### meta`property`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.meta "Permanent link")

Generates a hash based on all components of the facade. This is used for the run name or to determine whether a run should be continued or not.

#### optimizer`property`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.optimizer "Permanent link")

The optimizer which is responsible for the BO loop. Keeps track of useful information like status.

#### runhistory`property`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.runhistory "Permanent link")

The runhistory which is filled with all trials during the optimization process.

#### scenario`property`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.scenario "Permanent link")

The scenario object which holds all environment information.

#### ask[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.ask "Permanent link")

Asks the intensifier for the next trial.

Source code in `smac/facade/abstract_facade.py`

```
def ask(self) -> TrialInfo:
    """Asks the intensifier for the next trial."""
    return self._optimizer.ask()
```

#### get_acquisition_function`staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_acquisition_function "Permanent link")

The random facade is not using an acquisition function. Therefore, we simply return a dummy function.

Source code in `smac/facade/random_facade.py`

```
@staticmethod
def get_acquisition_function(scenario: Scenario) -> AbstractAcquisitionFunction:
    """The random facade is not using an acquisition function. Therefore, we simply return a dummy function."""

    class DummyAcquisitionFunction(AbstractAcquisitionFunction):
        def _compute(self, X: np.ndarray) -> np.ndarray:
            return X

    return DummyAcquisitionFunction()
```

#### get_acquisition_maximizer`staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_acquisition_maximizer "Permanent link")

We return `RandomSearch` as maximizer which samples configurations randomly from the configuration space and therefore neither uses the acquisition function nor the model.

Source code in `smac/facade/random_facade.py`

```
@staticmethod
def get_acquisition_maximizer(scenario: Scenario) -> RandomSearch:
    """We return ``RandomSearch`` as maximizer which samples configurations randomly from the configuration
    space and therefore neither uses the acquisition function nor the model.
    """
    return RandomSearch(
        scenario.configspace,
        seed=scenario.seed,
    )
```

#### get_config_selector`staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_config_selector "Permanent link")

Returns the default configuration selector.

Source code in `smac/facade/abstract_facade.py`

```
@staticmethod
def get_config_selector(
    scenario: Scenario,
    *,
    retrain_after: int = 8,
    retries: int = 16,
) -> ConfigSelector:
    """Returns the default configuration selector."""
    return ConfigSelector(scenario, retrain_after=retrain_after, retries=retries)
```

#### get_initial_design`staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_initial_design "Permanent link")

Returns an initial design, which returns the default configuration.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_initial_design--parameters "Permanent link")

additional_configs: list[Configuration], defaults to [] Adds additional configurations to the initial design.

Source code in `smac/facade/random_facade.py`

```
@staticmethod
def get_initial_design(
    scenario: Scenario,
    *,
    additional_configs: list[Configuration] = None,
) -> DefaultInitialDesign:
    """Returns an initial design, which returns the default configuration.

    Parameters
    ----------
    additional_configs: list[Configuration], defaults to []
        Adds additional configurations to the initial design.
    """
    if additional_configs is None:
        additional_configs = []
    return DefaultInitialDesign(
        scenario=scenario,
        additional_configs=additional_configs,
    )
```

#### get_intensifier`staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_intensifier "Permanent link")

```
get_intensifier(
    scenario: Scenario,
    *,
    eta: int = 3,
    n_seeds: int = 1,
    instance_seed_order: str | None = "shuffle_once",
    max_incumbents: int = 10,
    incumbent_selection: str = "highest_observed_budget"
) -> Hyperband
```

Returns a Hyperband intensifier instance. Budgets are supported.

int, defaults to 3
Input that controls the proportion of configurations discarded in each round of Successive Halving.

n_seeds : int, defaults to 1 How many seeds to use for each instance. instance_seed_order : str, defaults to "shuffle_once" How to order the instance-seed pairs. Can be set to: * None: No shuffling at all and use the instance-seed order provided by the user. * "shuffle_once": Shuffle the instance-seed keys once and use the same order across all runs. * "shuffle": Shuffle the instance-seed keys for each bracket individually. incumbent_selection : str, defaults to "any_budget" How to select the incumbent when using budgets. Can be set to: * "any_budget": Incumbent is the best on any budget i.e., best performance regardless of budget. * "highest_observed_budget": Incumbent is the best in the highest budget run so far. * "highest_budget": Incumbent is selected only based on the highest budget. max_incumbents : int, defaults to 10 How many incumbents to keep track of in the case of multi-objective.

Source code in `smac/facade/hyperband_facade.py`

```
@staticmethod
def get_intensifier(  # type: ignore
    scenario: Scenario,
    *,
    eta: int = 3,
    n_seeds: int = 1,
    instance_seed_order: str | None = "shuffle_once",
    max_incumbents: int = 10,
    incumbent_selection: str = "highest_observed_budget",
) -> Hyperband:
    """Returns a Hyperband intensifier instance. Budgets are supported.

    eta : int, defaults to 3
        Input that controls the proportion of configurations discarded in each round of Successive Halving.
    n_seeds : int, defaults to 1
        How many seeds to use for each instance.
    instance_seed_order : str, defaults to "shuffle_once"
        How to order the instance-seed pairs. Can be set to:
        * None: No shuffling at all and use the instance-seed order provided by the user.
        * "shuffle_once": Shuffle the instance-seed keys once and use the same order across all runs.
        * "shuffle": Shuffle the instance-seed keys for each bracket individually.
    incumbent_selection : str, defaults to "any_budget"
        How to select the incumbent when using budgets. Can be set to:
        * "any_budget": Incumbent is the best on any budget i.e., best performance regardless of budget.
        * "highest_observed_budget": Incumbent is the best in the highest budget run so far.
        * "highest_budget": Incumbent is selected only based on the highest budget.
    max_incumbents : int, defaults to 10
        How many incumbents to keep track of in the case of multi-objective.
    """
    return Hyperband(
        scenario=scenario,
        eta=eta,
        n_seeds=n_seeds,
        instance_seed_order=instance_seed_order,
        max_incumbents=max_incumbents,
        incumbent_selection=incumbent_selection,
    )
```

#### get_model`staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_model "Permanent link")

The model is used in the acquisition function. Since we do not use an acquisition function, we return a dummy model (returning random values in this case).

Source code in `smac/facade/random_facade.py`

```
@staticmethod
def get_model(scenario: Scenario) -> RandomModel:
    """The model is used in the acquisition function. Since we do not use an acquisition function, we return a
    dummy model (returning random values in this case).
    """
    return RandomModel(
        configspace=scenario.configspace,
        instance_features=scenario.instance_features,
        seed=scenario.seed,
    )
```

#### get_multi_objective_algorithm`staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_multi_objective_algorithm "Permanent link")

Returns the mean aggregation strategy for the multi-objective algorithm.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_multi_objective_algorithm--parameters "Permanent link")

scenario : Scenario objective_weights : list[float] | None, defaults to None Weights for averaging the objectives in a weighted manner. Must be of the same length as the number of objectives.

Source code in `smac/facade/random_facade.py`

```
@staticmethod
def get_multi_objective_algorithm(  # type: ignore
    scenario: Scenario,
    *,
    objective_weights: list[float] | None = None,
) -> MeanAggregationStrategy:
    """Returns the mean aggregation strategy for the multi-objective algorithm.

    Parameters
    ----------
    scenario : Scenario
    objective_weights : list[float] | None, defaults to None
        Weights for averaging the objectives in a weighted manner. Must be of the same length as the number of
        objectives.
    """
    return MeanAggregationStrategy(
        scenario=scenario,
        objective_weights=objective_weights,
    )
```

#### get_random_design`staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_random_design "Permanent link")

Just like the acquisition function, we do not use a random design. Therefore, we return a dummy design.

Source code in `smac/facade/random_facade.py`

```
@staticmethod
def get_random_design(scenario: Scenario) -> AbstractRandomDesign:
    """Just like the acquisition function, we do not use a random design. Therefore, we return a dummy design."""

    class DummyRandomDesign(AbstractRandomDesign):
        def check(self, iteration: int) -> bool:
            return True

    return DummyRandomDesign()
```

#### get_runhistory_encoder`staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.get_runhistory_encoder "Permanent link")

Returns the default runhistory encoder.

Source code in `smac/facade/random_facade.py`

```
@staticmethod
def get_runhistory_encoder(scenario: Scenario) -> RunHistoryEncoder:
    """Returns the default runhistory encoder."""
    return RunHistoryEncoder(scenario)
```

#### optimize[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.optimize "Permanent link")

```
optimize(
    *, data_to_scatter: dict[str, Any] | None = None
) -> Configuration | list[Configuration]
```

Optimizes the configuration of the algorithm.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.optimize--parameters "Permanent link")

data_to_scatter: dict[str, Any] | None We first note that this argument is valid only dask_runner! When a user scatters data from their local process to the distributed network, this data is distributed in a round-robin fashion grouping by number of cores. Roughly speaking, we can keep this data in memory and then we do not have to (de-)serialize the data every time we would like to execute a target function with a big dataset. For example, when your target function has a big dataset shared across all the target function, this argument is very useful.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.optimize--returns "Permanent link")

incumbent : Configuration Best found configuration.

Source code in `smac/facade/abstract_facade.py`

```
def optimize(self, *, data_to_scatter: dict[str, Any] | None = None) -> Configuration | list[Configuration]:
    """
    Optimizes the configuration of the algorithm.

    Parameters
    ----------
    data_to_scatter: dict[str, Any] | None
        We first note that this argument is valid only dask_runner!
        When a user scatters data from their local process to the distributed network,
        this data is distributed in a round-robin fashion grouping by number of cores.
        Roughly speaking, we can keep this data in memory and then we do not have to (de-)serialize the data
        every time we would like to execute a target function with a big dataset.
        For example, when your target function has a big dataset shared across all the target function,
        this argument is very useful.

    Returns
    -------
    incumbent : Configuration
        Best found configuration.
    """
    incumbents = None
    if isinstance(data_to_scatter, dict) and len(data_to_scatter) == 0:
        raise ValueError("data_to_scatter must be None or dict with some elements, but got an empty dict.")

    try:
        incumbents = self._optimizer.optimize(data_to_scatter=data_to_scatter)
    finally:
        self._optimizer.save()

    return incumbents
```

#### tell[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.tell "Permanent link")

Adds the result of a trial to the runhistory and updates the intensifier.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.tell--parameters "Permanent link")

info: TrialInfo Describes the trial from which to process the results. value: TrialValue Contains relevant information regarding the execution of a trial. save : bool, optional to True Whether the runhistory should be saved.

Source code in `smac/facade/abstract_facade.py`

```
def tell(self, info: TrialInfo, value: TrialValue, save: bool = True) -> None:
    """Adds the result of a trial to the runhistory and updates the intensifier.

    Parameters
    ----------
    info: TrialInfo
        Describes the trial from which to process the results.
    value: TrialValue
        Contains relevant information regarding the execution of a trial.
    save : bool, optional to True
        Whether the runhistory should be saved.
    """
    return self._optimizer.tell(info, value, save=save)
```

#### validate[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.validate "Permanent link")

Validates a configuration on seeds different from the ones used in the optimization process and on the highest budget (if budget type is real-valued).

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.validate--parameters "Permanent link")

config : Configuration Configuration to validate instances : list[str] | None, defaults to None Which instances to validate. If None, all instances specified in the scenario are used. In case that the budget type is real-valued, this argument is ignored. seed : int | None, defaults to None If None, the seed from the scenario is used.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/facade/hyperband_facade/#smac.facade.hyperband_facade.HyperbandFacade.validate--returns "Permanent link")

cost : float | list[float] The averaged cost of the configuration. In case of multi-fidelity, the cost of each objective is averaged.

Source code in `smac/facade/abstract_facade.py`

```
def validate(
    self,
    config: Configuration,
    *,
    seed: int | None = None,
) -> float | list[float]:
    """Validates a configuration on seeds different from the ones used in the optimization process and on the
    highest budget (if budget type is real-valued).

    Parameters
    ----------
    config : Configuration
        Configuration to validate
    instances : list[str] | None, defaults to None
        Which instances to validate. If None, all instances specified in the scenario are used.
        In case that the budget type is real-valued, this argument is ignored.
    seed : int | None, defaults to None
        If None, the seed from the scenario is used.

    Returns
    -------
    cost : float | list[float]
        The averaged cost of the configuration. In case of multi-fidelity, the cost of each objective is
        averaged.
    """
    return self._optimizer.validate(config, seed=seed)
```

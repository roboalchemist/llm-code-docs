# Source: https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/

Title: Abstract facade - SMAC3

URL Source: https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/

Markdown Content:
Facade is an abstraction on top of the SMBO backend to organize the components of a Bayesian Optimization loop in a configurable and separable manner to suit the various needs of different (hyperparameter) optimization pipelines.

With the exception to scenario and `target_function`, which are expected of the user, the parameters `model`, `acquisition_function`, `acquisition_maximizer`, `initial_design`, `random_design`, `intensifier`, `multi_objective_algorithm`, `runhistory_encoder` can either be explicitly specified in the subclasses' `get_*` methods (defining a specific BO pipeline) or be instantiated by the user to overwrite a pipeline components explicitly.

##### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade--parameters "Permanent link")

scenario : Scenario The scenario object, holding all environmental information. target_function : Callable | str | AbstractRunner This function is called internally to judge a trial's performance. If a string is passed, it is assumed to be a script. In this case, `TargetFunctionScriptRunner` is used to run the script. model : AbstractModel | None, defaults to None The surrogate model. acquisition_function : AbstractAcquisitionFunction | None, defaults to None The acquisition function. acquisition_maximizer : AbstractAcquisitionMaximizer | None, defaults to None The acquisition maximizer, deciding which configuration is most promising based on the surrogate model and acquisition function. initial_design : InitialDesign | None, defaults to None The sampled configurations from the initial design are evaluated before the Bayesian optimization loop starts. random_design : RandomDesign | None, defaults to None The random design is used in the acquisition maximizer, deciding whether the next configuration should be drawn from the acquisition function or randomly. intensifier : AbstractIntensifier | None, defaults to None The intensifier decides which trial (combination of configuration, seed, budget and instance) should be run next. multi_objective_algorithm : AbstractMultiObjectiveAlgorithm | None, defaults to None In case of multiple objectives, the objectives need to be interpreted so that an optimization is possible. The multi-objective algorithm takes care of that. runhistory_encoder : RunHistoryEncoder | None, defaults to None Based on the runhistory, the surrogate model is trained. However, the data first needs to be encoded, which is done by the runhistory encoder. For example, inactive hyperparameters need to be encoded or cost values can be log transformed. logging_level: int | Path | Literal[False] | None The level of logging (the lowest level 0 indicates the debug level). If a path is passed, a yaml file is expected with the logging configuration. If nothing is passed, the default logging.yml from SMAC is used. If False is passed, SMAC will not do any customization of the logging setup and the responsibility is left to the user. callbacks: list[Callback], defaults to [] Callbacks, which are incorporated into the optimization loop. overwrite: bool, defaults to False When True, overwrites the run results if a previous run is found that is consistent in the meta data with the current setup. When False and a previous run is found that is consistent in the meta data, the run is continued. When False and a previous run is found that is not consistent in the meta data, the the user is asked for the exact behaviour (overwrite completely or rename old run first). dask_client: Client | None, defaults to None User-created dask client, which can be used to start a dask cluster and then attach SMAC to it. This will not be closed automatically and will have to be closed manually if provided explicitly. If none is provided (default), a local one will be created for you and closed upon completion.

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

#### intensifier`property`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.intensifier "Permanent link")

The optimizer which is responsible for the BO loop. Keeps track of useful information like status.

#### meta`property`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.meta "Permanent link")

Generates a hash based on all components of the facade. This is used for the run name or to determine whether a run should be continued or not.

#### optimizer`property`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.optimizer "Permanent link")

The optimizer which is responsible for the BO loop. Keeps track of useful information like status.

#### runhistory`property`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.runhistory "Permanent link")

The runhistory which is filled with all trials during the optimization process.

#### scenario`property`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.scenario "Permanent link")

The scenario object which holds all environment information.

#### ask[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.ask "Permanent link")

Asks the intensifier for the next trial.

Source code in `smac/facade/abstract_facade.py`

```
def ask(self) -> TrialInfo:
    """Asks the intensifier for the next trial."""
    return self._optimizer.ask()
```

#### get_acquisition_function`abstractmethod``staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.get_acquisition_function "Permanent link")

Returns the acquisition function instance used in the BO loop, defining the exploration/exploitation trade-off.

Source code in `smac/facade/abstract_facade.py`

```
@staticmethod
@abstractmethod
def get_acquisition_function(scenario: Scenario) -> AbstractAcquisitionFunction:
    """Returns the acquisition function instance used in the BO loop,
    defining the exploration/exploitation trade-off.
    """
    raise NotImplementedError
```

#### get_acquisition_maximizer`abstractmethod``staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.get_acquisition_maximizer "Permanent link")

Returns the acquisition optimizer instance to be used in the BO loop, specifying how the acquisition function instance is optimized.

Source code in `smac/facade/abstract_facade.py`

```
@staticmethod
@abstractmethod
def get_acquisition_maximizer(scenario: Scenario) -> AbstractAcquisitionMaximizer:
    """Returns the acquisition optimizer instance to be used in the BO loop,
    specifying how the acquisition function instance is optimized.
    """
    raise NotImplementedError
```

#### get_config_selector`staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.get_config_selector "Permanent link")

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

#### get_initial_design`abstractmethod``staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.get_initial_design "Permanent link")

Returns an instance of the initial design class to be used in the BO loop, specifying how the configurations the BO loop is 'warm-started' with are selected.

Source code in `smac/facade/abstract_facade.py`

```
@staticmethod
@abstractmethod
def get_initial_design(scenario: Scenario) -> AbstractInitialDesign:
    """Returns an instance of the initial design class to be used in the BO loop,
    specifying how the configurations the BO loop is 'warm-started' with are selected.
    """
    raise NotImplementedError
```

#### get_intensifier`abstractmethod``staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.get_intensifier "Permanent link")

Returns the intensifier instance to be used in the BO loop, specifying how to challenge the incumbent configuration on other problem instances.

Source code in `smac/facade/abstract_facade.py`

```
@staticmethod
@abstractmethod
def get_intensifier(scenario: Scenario) -> AbstractIntensifier:
    """Returns the intensifier instance to be used in the BO loop,
    specifying how to challenge the incumbent configuration on other problem instances.
    """
    raise NotImplementedError
```

#### get_model`abstractmethod``staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.get_model "Permanent link")

Returns the surrogate cost model instance used in the BO loop.

Source code in `smac/facade/abstract_facade.py`

```
@staticmethod
@abstractmethod
def get_model(scenario: Scenario) -> AbstractModel:
    """Returns the surrogate cost model instance used in the BO loop."""
    raise NotImplementedError
```

#### get_multi_objective_algorithm`abstractmethod``staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.get_multi_objective_algorithm "Permanent link")

Returns the multi-objective algorithm instance to be used in the BO loop, specifying the scalarization strategy for multiple objectives' costs.

Source code in `smac/facade/abstract_facade.py`

```
@staticmethod
@abstractmethod
def get_multi_objective_algorithm(scenario: Scenario) -> AbstractMultiObjectiveAlgorithm:
    """Returns the multi-objective algorithm instance to be used in the BO loop,
    specifying the scalarization strategy for multiple objectives' costs.
    """
    raise NotImplementedError
```

#### get_random_design`abstractmethod``staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.get_random_design "Permanent link")

Returns an instance of the random design class to be used in the BO loop, specifying how to interleave the BO iterations with randomly selected configurations.

Source code in `smac/facade/abstract_facade.py`

```
@staticmethod
@abstractmethod
def get_random_design(scenario: Scenario) -> AbstractRandomDesign:
    """Returns an instance of the random design class to be used in the BO loop,
    specifying how to interleave the BO iterations with randomly selected configurations.
    """
    raise NotImplementedError
```

#### get_runhistory_encoder`abstractmethod``staticmethod`[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.get_runhistory_encoder "Permanent link")

Returns an instance of the runhistory encoder class to be used in the BO loop, specifying how the runhistory is to be prepared for the next surrogate model.

Source code in `smac/facade/abstract_facade.py`

```
@staticmethod
@abstractmethod
def get_runhistory_encoder(scenario: Scenario) -> AbstractRunHistoryEncoder:
    """Returns an instance of the runhistory encoder class to be used in the BO loop,
    specifying how the runhistory is to be prepared for the next surrogate model.
    """
    raise NotImplementedError
```

#### optimize[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.optimize "Permanent link")

```
optimize(
    *, data_to_scatter: dict[str, Any] | None = None
) -> Configuration | list[Configuration]
```

Optimizes the configuration of the algorithm.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.optimize--parameters "Permanent link")

data_to_scatter: dict[str, Any] | None We first note that this argument is valid only dask_runner! When a user scatters data from their local process to the distributed network, this data is distributed in a round-robin fashion grouping by number of cores. Roughly speaking, we can keep this data in memory and then we do not have to (de-)serialize the data every time we would like to execute a target function with a big dataset. For example, when your target function has a big dataset shared across all the target function, this argument is very useful.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.optimize--returns "Permanent link")

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

#### tell[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.tell "Permanent link")

Adds the result of a trial to the runhistory and updates the intensifier.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.tell--parameters "Permanent link")

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

#### validate[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.validate "Permanent link")

Validates a configuration on seeds different from the ones used in the optimization process and on the highest budget (if budget type is real-valued).

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.validate--parameters "Permanent link")

config : Configuration Configuration to validate instances : list[str] | None, defaults to None Which instances to validate. If None, all instances specified in the scenario are used. In case that the budget type is real-valued, this argument is ignored. seed : int | None, defaults to None If None, the seed from the scenario is used.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/facade/abstract_facade/#smac.facade.abstract_facade.AbstractFacade.validate--returns "Permanent link")

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

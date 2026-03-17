# Source: https://automl.github.io/SMAC3/latest/api/smac/main/smbo/

Title: Smbo - SMAC3

URL Source: https://automl.github.io/SMAC3/latest/api/smac/main/smbo/

Markdown Content:
Implementation that contains the main Bayesian optimization loop.

##### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO--parameters "Permanent link")

scenario : Scenario The scenario object, holding all environmental information. runner : AbstractRunner The runner (containing the target function) is called internally to judge a trial's performance. runhistory : Runhistory The runhistory stores all trials. intensifier : AbstractIntensifier The intensifier decides which trial (combination of configuration, seed, budget and instance) should be run next. overwrite: bool, defaults to False When True, overwrites the run results if a previous run is found that is inconsistent in the meta data with the current setup. If `overwrite` is set to False, the user is asked for the exact behaviour (overwrite completely, save old run, or use old results).

##### Warning[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO--warning "Permanent link")

This model should be initialized by a facade only.

Source code in `smac/main/smbo.py`

```
def __init__(
    self,
    scenario: Scenario,
    runner: AbstractRunner,
    runhistory: RunHistory,
    intensifier: AbstractIntensifier,
    overwrite: bool = False,
):
    self._scenario = scenario
    self._configspace = scenario.configspace
    self._runhistory = runhistory
    self._intensifier = intensifier
    self._trial_generator = iter(intensifier)
    self._runner = runner
    self._overwrite = overwrite

    # Internal variables
    self._finished = False
    self._stop = False  # Gracefully stop SMAC
    self._callbacks: list[Callback] = []

    # Stats variables
    self._start_time: float | None = None
    self._used_target_function_walltime = 0.0
    self._used_target_function_cputime = 0.0

    # Set walltime used method for intensifier
    self._intensifier.used_walltime = lambda: self.used_walltime  # type: ignore

    # We initialize the state based on previous data.
    # If no previous data is found then we take care of the initial design.
    self._initialize_state()
```

#### budget_exhausted`property`[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.budget_exhausted "Permanent link")

Checks whether the the remaining walltime, cputime or trials was exceeded.

#### intensifier`property`[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.intensifier "Permanent link")

The run history, which is filled with all information during the optimization process.

#### remaining_cputime`property`[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.remaining_cputime "Permanent link")

Subtracts the target function running budget with the used time.

#### remaining_trials`property`[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.remaining_trials "Permanent link")

Subtract the target function runs in the scenario with the used ta runs.

#### remaining_walltime`property`[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.remaining_walltime "Permanent link")

```
remaining_walltime: float
```

Subtracts the runtime configuration budget with the used wallclock time.

#### runhistory`property`[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.runhistory "Permanent link")

The run history, which is filled with all information during the optimization process.

#### used_target_function_cputime`property`[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.used_target_function_cputime "Permanent link")

```
used_target_function_cputime: float
```

Returns how much time the target function spend on the hardware so far.

#### used_target_function_walltime`property`[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.used_target_function_walltime "Permanent link")

```
used_target_function_walltime: float
```

Returns how much walltime the target function spend so far.

#### used_walltime`property`[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.used_walltime "Permanent link")

Returns used wallclock time.

#### ask[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.ask "Permanent link")

Asks the intensifier for the next trial.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.ask--returns "Permanent link")

info : TrialInfo Information about the trial (config, instance, seed, budget).

Source code in `smac/main/smbo.py`

```
def ask(self) -> TrialInfo:
    """Asks the intensifier for the next trial.

    Returns
    -------
    info : TrialInfo
        Information about the trial (config, instance, seed, budget).
    """
    logger.debug("Calling ask...")

    for callback in self._callbacks:
        callback.on_ask_start(self)

    # Now we use our generator to get the next trial info
    trial_info = next(self._trial_generator)

    # Track the fact that the trial was returned
    # This is really important because otherwise the intensifier would most likly sample the same trial again
    self._runhistory.add_running_trial(trial_info)

    for callback in self._callbacks:
        callback.on_ask_end(self, trial_info)

    logger.debug("...and received a new trial.")

    return trial_info
```

#### exists[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.exists "Permanent link")

Checks if the files associated with the run already exist. Checks all files that are created by the optimizer.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.exists--parameters "Permanent link")

filename : str | Path The name of the folder of the SMAC run.

Source code in `smac/main/smbo.py`

```
def exists(self, filename: str | Path) -> bool:
    """Checks if the files associated with the run already exist.
    Checks all files that are created by the optimizer.

    Parameters
    ----------
    filename : str | Path
        The name of the folder of the SMAC run.
    """
    if isinstance(filename, str):
        filename = Path(filename)

    optimization_fn = filename / "optimization.json"
    runhistory_fn = filename / "runhistory.json"
    intensifier_fn = filename / "intensifier.json"

    if optimization_fn.exists() and runhistory_fn.exists() and intensifier_fn.exists():
        return True

    return False
```

#### load[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.load "Permanent link")

```
load() -> None
```

Loads the optimizer, intensifier, and runhistory from the output directory specified in the scenario.

Source code in `smac/main/smbo.py`

```
def load(self) -> None:
    """Loads the optimizer, intensifier, and runhistory from the output directory specified in the scenario."""
    filename = self._scenario.output_directory

    optimization_fn = filename / "optimization.json"
    runhistory_fn = filename / "runhistory.json"
    intensifier_fn = filename / "intensifier.json"

    if filename is not None:
        with open(optimization_fn) as fp:
            data = json.load(fp)

        self._runhistory.load(runhistory_fn, configspace=self._scenario.configspace)
        self._intensifier.load(intensifier_fn)

        self._used_target_function_walltime = data["used_target_function_walltime"]
        self._used_target_function_cputime = data["used_target_function_cputime"]
        self._finished = data["finished"]
        self._start_time = time.time() - data["used_walltime"]
```

#### optimize[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.optimize "Permanent link")

```
optimize(
    *, data_to_scatter: dict[str, Any] | None = None
) -> Configuration | list[Configuration]
```

Runs the Bayesian optimization loop.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.optimize--parameters "Permanent link")

data_to_scatter: dict[str, Any] | None When a user scatters data from their local process to the distributed network, this data is distributed in a round-robin fashion grouping by number of cores. Roughly speaking, we can keep this data in memory and then we do not have to (de-)serialize the data every time we would like to execute a target function with a big dataset. For example, when your target function has a big dataset shared across all the target function, this argument is very useful.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.optimize--returns "Permanent link")

incumbent : Configuration The best found configuration.

Source code in `smac/main/smbo.py`

```
def optimize(self, *, data_to_scatter: dict[str, Any] | None = None) -> Configuration | list[Configuration]:
    """Runs the Bayesian optimization loop.

    Parameters
    ----------
    data_to_scatter: dict[str, Any] | None
        When a user scatters data from their local process to the distributed network,
        this data is distributed in a round-robin fashion grouping by number of cores.
        Roughly speaking, we can keep this data in memory and then we do not have to (de-)serialize the data
        every time we would like to execute a target function with a big dataset.
        For example, when your target function has a big dataset shared across all the target function,
        this argument is very useful.

    Returns
    -------
    incumbent : Configuration
        The best found configuration.
    """
    # We return the incumbent if we already finished the a process (we don't want to allow to call
    # optimize more than once).
    if self._finished:
        logger.info("Optimization process was already finished. Returning incumbent...")
        if self._scenario.count_objectives() == 1:
            return self.intensifier.get_incumbent()
        else:
            return self.intensifier.get_incumbents()

    # Start the timer before we do anything
    # If we continue the optimization, the starting time is set by the load method
    if self._start_time is None:
        self._start_time = time.time()

    for callback in self._callbacks:
        callback.on_start(self)

    dask_data_to_scatter = {}
    if isinstance(self._runner, DaskParallelRunner) and data_to_scatter is not None:
        dask_data_to_scatter = dict(data_to_scatter=self._runner._client.scatter(data_to_scatter, broadcast=True))
    elif data_to_scatter is not None:
        raise ValueError(
            "data_to_scatter is valid only for DaskParallelRunner, "
            f"but {dask_data_to_scatter} was provided for {self._runner.__class__.__name__}"
        )

    # Main BO loop
    while True:
        for callback in self._callbacks:
            callback.on_iteration_start(self)

        try:
            # Sample next trial from the intensification
            trial_info = self.ask()

            # We submit the trial to the runner
            # In multi-worker mode, SMAC waits till a new worker is available here
            self._runner.submit_trial(trial_info=trial_info, **dask_data_to_scatter)
        except StopIteration:
            self._stop = True

        # We add results from the runner if results are available
        self._add_results()

        # Some statistics
        logger.debug(
            f"Remaining wallclock time: {self.remaining_walltime}; "
            f"Remaining cpu time: {self.remaining_cputime}; "
            f"Remaining trials: {self.remaining_trials}"
        )

        if self.runhistory.finished % 50 == 0:
            logger.info(f"Finished {self.runhistory.finished} trials.")

        for callback in self._callbacks:
            callback.on_iteration_end(self)

        # Now we check whether we have to stop the optimization
        if self.budget_exhausted or self._stop:
            if self.budget_exhausted:
                logger.info("Configuration budget is exhausted:")
                logger.info(f"--- Remaining wallclock time: {self.remaining_walltime}")
                logger.info(f"--- Remaining cpu time: {self.remaining_cputime}")
                logger.info(f"--- Remaining trials: {self.remaining_trials}")
            else:
                logger.info("Shutting down because the stop flag was set.")

            # Wait for the trials to finish
            while self._runner.is_running():
                self._runner.wait()
                self._add_results()

            # Break from the intensification loop, as there are no more resources
            break

    for callback in self._callbacks:
        callback.on_end(self)

    # We only set the finished flag if the budget really was exhausted
    if self.budget_exhausted:
        self._finished = True

    if self._scenario.count_objectives() == 1:
        return self.intensifier.get_incumbent()
    else:
        return self.intensifier.get_incumbents()
```

#### print_stats[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.print_stats "Permanent link")

```
print_stats() -> None
```

Prints all statistics.

Source code in `smac/main/smbo.py`

```
def print_stats(self) -> None:
    """Prints all statistics."""
    logger.info(
        "\n"
        f"--- STATISTICS -------------------------------------\n"
        f"--- Incumbent changed: {self.intensifier.incumbents_changed}\n"
        f"--- Submitted trials: {self.runhistory.submitted} / {self._scenario.n_trials}\n"
        f"--- Finished trials: {self.runhistory.finished} / {self._scenario.n_trials}\n"
        f"--- Configurations: {self.runhistory._n_id}\n"
        f"--- Used wallclock time: {round(self.used_walltime)} / {self._scenario.walltime_limit} sec\n"
        "--- Used target function runtime: "
        f"{round(self.used_target_function_walltime, 2)} / {self._scenario.cputime_limit} sec\n"
        "--- Used target function CPU time: "
        f"{round(self.used_target_function_cputime, 2)} / {self._scenario.cputime_limit} sec\n"
        f"----------------------------------------------------"
    )
```

#### register_callback[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.register_callback "Permanent link")

```
register_callback(
    callback: Callback, index: int | None = None
) -> None
```

Registers a callback to be called before, in between, and after the Bayesian optimization loop.

Callback is appended to the list by default.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.register_callback--parameters "Permanent link")

callback : Callback The callback to be registered. index : int, optional The index at which the callback should be registered. The default is None. If it is None, append the callback to the list.

Source code in `smac/main/smbo.py`

```
def register_callback(self, callback: Callback, index: int | None = None) -> None:
    """
    Registers a callback to be called before, in between, and after the Bayesian optimization loop.

    Callback is appended to the list by default.

    Parameters
    ----------
    callback : Callback
        The callback to be registered.
    index : int, optional
        The index at which the callback should be registered. The default is None.
        If it is None, append the callback to the list.
    """
    if index is None:
        index = len(self._callbacks)
    self._callbacks.insert(index, callback)
```

#### reset[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.reset "Permanent link")

```
reset() -> None
```

Resets the internal variables of the optimizer, intensifier, and runhistory.

Source code in `smac/main/smbo.py`

```
def reset(self) -> None:
    """Resets the internal variables of the optimizer, intensifier, and runhistory."""
    self._used_target_function_walltime = 0
    self._used_target_function_cputime = 0
    self._finished = False

    # We also reset runhistory and intensifier here
    self._runhistory.reset()
    self._intensifier.reset()
```

#### save[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.save "Permanent link")

```
save() -> None
```

Saves the current stats, runhistory, and intensifier.

Source code in `smac/main/smbo.py`

```
def save(self) -> None:
    """Saves the current stats, runhistory, and intensifier."""
    path = self._scenario.output_directory

    if path is not None:
        data = {
            "used_walltime": self.used_walltime,
            "used_target_function_walltime": self.used_target_function_walltime,
            "used_target_function_cputime": self.used_target_function_cputime,
            "last_update": time.time(),
            "finished": self._finished,
        }

        # Save optimization data
        with open(str(path / "optimization.json"), "w") as file:
            json.dump(data, file, indent=2, cls=NumpyEncoder)

        # And save runhistory and intensifier
        self._runhistory.save(path / "runhistory.json")
        self._intensifier.save(path / "intensifier.json")
```

#### tell[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.tell "Permanent link")

Adds the result of a trial to the runhistory and updates the stats object.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.tell--parameters "Permanent link")

info : TrialInfo Describes the trial from which to process the results. value : TrialValue Contains relevant information regarding the execution of a trial. save : bool, optional to True Whether the runhistory should be saved.

Source code in `smac/main/smbo.py`

```
def tell(
    self,
    info: TrialInfo,
    value: TrialValue,
    save: bool = True,
) -> None:
    """Adds the result of a trial to the runhistory and updates the stats object.

    Parameters
    ----------
    info : TrialInfo
        Describes the trial from which to process the results.
    value : TrialValue
        Contains relevant information regarding the execution of a trial.
    save : bool, optional to True
        Whether the runhistory should be saved.
    """
    if info.config.origin is None:
        info.config.origin = "Custom"

    for callback in self._callbacks:
        response = callback.on_tell_start(self, info, value)

        # If a callback returns False, the optimization loop should be interrupted
        # the other callbacks are still being called.
        if response is False:
            logger.info("A callback returned False. Abort is requested.")
            self._stop = True

    # Some sanity checks here
    if self._intensifier.uses_instances and info.instance is None:
        raise ValueError("Passed instance is None but intensifier requires instances.")

    if self._intensifier.uses_budgets and info.budget is None:
        raise ValueError("Passed budget is None but intensifier requires budgets.")

    self._runhistory.add(
        config=info.config,
        cost=value.cost,
        time=value.time,
        cpu_time=value.cpu_time,
        status=value.status,
        instance=info.instance,
        seed=info.seed,
        budget=info.budget,
        starttime=value.starttime,
        endtime=value.endtime,
        additional_info=value.additional_info,
        force_update=True,  # Important to overwrite the status RUNNING
    )

    logger.debug(f"Tell method was called with cost {value.cost} ({StatusType(value.status).name}).")

    for callback in self._callbacks:
        response = callback.on_tell_end(self, info, value)

        # If a callback returns False, the optimization loop should be interrupted
        # the other callbacks are still being called.
        if response is False:
            logger.info("A callback returned False. Abort is requested.")
            self._stop = True

    if save:
        self.save()
```

#### update_acquisition_function[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.update_acquisition_function "Permanent link")

Updates the acquisition function including the associated model and the acquisition optimizer.

Source code in `smac/main/smbo.py`

```
def update_acquisition_function(self, acquisition_function: AbstractAcquisitionFunction) -> None:
    """Updates the acquisition function including the associated model and the acquisition
    optimizer.
    """
    if (config_selector := self._intensifier._config_selector) is not None:
        config_selector._acquisition_function = acquisition_function
        config_selector._acquisition_function.model = config_selector._model

        assert config_selector._acquisition_maximizer is not None
        config_selector._acquisition_maximizer.acquisition_function = acquisition_function
```

#### update_model[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.update_model "Permanent link")

Updates the model and updates the acquisition function.

Source code in `smac/main/smbo.py`

```
def update_model(self, model: AbstractModel) -> None:
    """Updates the model and updates the acquisition function."""
    if (config_selector := self._intensifier._config_selector) is not None:
        config_selector._model = model

        assert config_selector._acquisition_function is not None
        config_selector._acquisition_function.model = model
```

#### validate[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.validate "Permanent link")

Validates a configuration on other seeds than the ones used in the optimization process and on the highest budget (if budget type is real-valued). Does not exceed the maximum number of config calls or seeds as defined in the scenario.

###### Parameters[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.validate--parameters "Permanent link")

config : Configuration Configuration to validate In case that the budget type is real-valued budget, this argument is ignored. seed : int | None, defaults to None If None, the seed from the scenario is used.

###### Returns[#](https://automl.github.io/SMAC3/latest/api/smac/main/smbo/#smac.main.smbo.SMBO.validate--returns "Permanent link")

cost : float | ndarray[float] The averaged cost of the configuration. In case of multi-fidelity, the cost of each objective is averaged.

Source code in `smac/main/smbo.py`

```
def validate(
    self,
    config: Configuration,
    *,
    seed: int | None = None,
) -> float | ndarray[float]:
    """Validates a configuration on other seeds than the ones used in the optimization process and on the highest
    budget (if budget type is real-valued). Does not exceed the maximum number of config calls or seeds as defined
    in the scenario.

    Parameters
    ----------
    config : Configuration
        Configuration to validate
        In case that the budget type is real-valued budget, this argument is ignored.
    seed : int | None, defaults to None
        If None, the seed from the scenario is used.

    Returns
    -------
    cost : float | ndarray[float]
        The averaged cost of the configuration. In case of multi-fidelity, the cost of each objective is
        averaged.
    """
    if seed is None:
        seed = self._scenario.seed

    costs = []
    for trial in self._intensifier.get_trials_of_interest(config, validate=True, seed=seed):
        kwargs: dict[str, Any] = {}
        if trial.seed is not None:
            kwargs["seed"] = trial.seed
        if trial.budget is not None:
            kwargs["budget"] = trial.budget
        if trial.instance is not None:
            kwargs["instance"] = trial.instance

        # TODO: Use submit run for faster evaluation
        # self._runner.submit_trial(trial_info=trial)
        _, cost, _, _, _ = self._runner.run(config, **kwargs)
        costs += [cost]

    np_costs = np.array(costs)
    return np.mean(np_costs, axis=0)
```

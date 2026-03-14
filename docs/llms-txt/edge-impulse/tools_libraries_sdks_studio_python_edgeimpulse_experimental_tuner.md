# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/experimental/tuner/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.experimental.tuner

## Functions

### check\_tuner

```python  theme={"system"}
edgeimpulse.experimental.tuner.check_tuner(
	timeout_sec: int | None = None,
	wait_for_completion: bool = True
) ‑> edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse
```

Check the current state of the tuner and optionally waits until the tuner has completed.

| Parameters            |                      |
| --------------------- | -------------------- |
| `timeout_sec`         | `int \| None = None` |
| `wait_for_completion` | `bool = True`        |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse` |

### get\_tuner\_run\_state

```python  theme={"system"}
edgeimpulse.experimental.tuner.get_tuner_run_state(
	tuner_coordinator_job_id: int
) ‑> edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse
```

Retrieve the current state of the tuner run.

Returns:
OptimizeStateResponse: The OptimizeStateResponse object representing the current Tuner state.

| Parameters                 |       |
| -------------------------- | ----- |
| `tuner_coordinator_job_id` | `int` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse` |

### list\_tuner\_runs

```python  theme={"system"}
edgeimpulse.experimental.tuner.list_tuner_runs(
	
) ‑> edgeimpulse_api.models.list_tuner_runs_response.ListTunerRunsResponse
```

List the tuner runs that have been done in the current project.

Returns:
ListTunerRunsResponse: An object containing all the tuner runs

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_tuner_runs_response.ListTunerRunsResponse` |

### print\_tuner\_coordinator\_logs

```python  theme={"system"}
edgeimpulse.experimental.tuner.print_tuner_coordinator_logs(
	limit: int = 500
) ‑> None
```

Retrieve and print logs for the tuner coordinator job.

Returns:
None

| Parameters |             |
| ---------- | ----------- |
| `limit`    | `int = 500` |

| Returns |
| ------- |
| `None`  |

### print\_tuner\_job\_logs

```python  theme={"system"}
edgeimpulse.experimental.tuner.print_tuner_job_logs(
	limit: int = 500
) ‑> None
```

Retrieve and print logs for the tuner job.

Returns:
None

| Parameters |             |
| ---------- | ----------- |
| `limit`    | `int = 500` |

| Returns |
| ------- |
| `None`  |

### set\_impulse\_from\_trial

```python  theme={"system"}
edgeimpulse.experimental.tuner.set_impulse_from_trial(
	trial_id: str,
	timeout_sec: float | None = None,
	wait_for_completion: bool | None = True
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Replace the current Impulse configuration with one found in a trial fromm the tuner.

| Parameters            |                        |
| --------------------- | ---------------------- |
| `trial_id`            | `str`                  |
| `timeout_sec`         | `float \| None = None` |
| `wait_for_completion` | `bool \| None = True`  |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

### start\_custom\_tuner

```python  theme={"system"}
edgeimpulse.experimental.tuner.start_custom_tuner(
	config: edgeimpulse_api.models.optimize_config.OptimizeConfig
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Start a tuner job with custom configuration.

| Parameters |                                                         |
| ---------- | ------------------------------------------------------- |
| `config`   | `edgeimpulse_api.models.optimize_config.OptimizeConfig` |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

### start\_tuner

```python  theme={"system"}
edgeimpulse.experimental.tuner.start_tuner(
	space: List[edgeimpulse_api.models.tuner_space_impulse.TunerSpaceImpulse],
	target_device: str,
	target_latency: int,
	tuning_max_trials: int | None = None,
	name: str | None = None
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Start the EON tuner with default settings. Use `start_custom_tuner` to specify config.

| Parameters          |                                                                      |
| ------------------- | -------------------------------------------------------------------- |
| `space`             | `List[edgeimpulse_api.models.tuner_space_impulse.TunerSpaceImpulse]` |
| `target_device`     | `str`                                                                |
| `target_latency`    | `int`                                                                |
| `tuning_max_trials` | `int \| None = None`                                                 |
| `name`              | `str \| None = None`                                                 |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

### tuner\_report\_as\_df

```python  theme={"system"}
edgeimpulse.experimental.tuner.tuner_report_as_df(
	state: edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse
)
```

Get a tuner trial report dataframe with model metrics and block configuration.

This method needs pandas to be installed.

Generate a dataframe on the tuner trials including used input, model, learn block configuration and model
validation metrics.

| Parameters |                                                                        |
| ---------- | ---------------------------------------------------------------------- |
| `state`    | `edgeimpulse_api.models.optimize_state_response.OptimizeStateResponse` |


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.wandb.ai/models/ref/python/public-api/sweep.md

# Source: https://docs.wandb.ai/models/ref/python/functions/sweep.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# sweep()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/sdk/wandb_sweep.py" />

### <kbd>function</kbd> `sweep`

```python  theme={null}
sweep(
    sweep: 'dict | Callable',
    entity: 'str | None' = None,
    project: 'str | None' = None,
    prior_runs: 'list[str] | None' = None
) → str
```

Initialize a hyperparameter sweep.

Search for hyperparameters that optimizes a cost function of a machine learning model by testing various combinations.

Make note the unique identifier, `sweep_id`, that is returned. At a later step provide the `sweep_id` to a sweep agent.

See [Sweep configuration structure](https://docs.wandb.ai/guides/sweeps/define-sweep-configuration) for information on how to define your sweep.

**Args:**

* `sweep`:  The configuration of a hyperparameter search.  (or configuration generator).  If you provide a callable, ensure that the callable does  not take arguments and that it returns a dictionary that  conforms to the W\&B sweep config spec.
* `entity`:  The username or team name where you want to send W\&B  runs created by the sweep to. Ensure that the entity you  specify already exists. If you don't specify an entity,  the run will be sent to your default entity,  which is usually your username.
* `project`:  The name of the project where W\&B runs created from  the sweep are sent to. If the project is not specified, the  run is sent to a project labeled 'Uncategorized'.
* `prior_runs`:  The run IDs of existing runs to add to this sweep.

**Returns:**

* `str`:  A unique identifier for the sweep.

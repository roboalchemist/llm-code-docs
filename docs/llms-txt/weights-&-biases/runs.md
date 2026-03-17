# Source: https://docs.wandb.ai/models/runs.md

# Source: https://docs.wandb.ai/models/ref/sdk-coding-cheat-sheet/runs.md

# Source: https://docs.wandb.ai/models/ref/python/public-api/runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Runs

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/apis/public/runs.py" />

## <kbd>class</kbd> `Runs`

A lazy iterator of `Run` objects associated with a project and optional filter.

Runs are retrieved in pages from the W\&B server as needed.

This is generally used indirectly using the `Api.runs` namespace.

### <kbd>method</kbd> `Runs.__init__`

```python  theme={null}
__init__(
    client: 'RetryingClient',
    entity: 'str',
    project: 'str',
    filters: 'dict[str, Any] | None' = None,
    order: 'str' = '+created_at',
    per_page: 'int' = 50,
    include_sweeps: 'bool' = True,
    lazy: 'bool' = True,
    service_api: 'ServiceApi | None' = None
)
```

**Args:**

* `client`:  (`wandb.apis.public.RetryingClient`) The API client to use  for requests.
* `entity`:  (str) The entity (username or team) that owns the project.
* `project`:  (str) The name of the project to fetch runs from.
* `filters`:  (Optional\[Dict\[str, Any]]) A dictionary of filters to apply  to the runs query.
* `order`:  (str) Order can be `created_at`, `heartbeat_at`, `config.*.value`, or `summary_metrics.*`.  If you prepend order with a + order is ascending (default).  If you prepend order with a - order is descending.  The default order is run.created\_at from oldest to newest.
* `per_page`:  (int) The number of runs to fetch per request (default is 50).
* `include_sweeps`:  (bool) Whether to include sweep information in the  runs. Defaults to True.

***

### <kbd>property</kbd> Runs.length

***

### <kbd>method</kbd> `Runs.histories`

```python  theme={null}
histories(
    samples: 'int' = 500,
    keys: 'list[str] | None' = None,
    x_axis: 'str' = '_step',
    format: "Literal['default', 'pandas', 'polars']" = 'default',
    stream: "Literal['default', 'system']" = 'default'
) → list[dict[str, Any]] | pd.DataFrame | pl.DataFrame
```

Return sampled history metrics for all runs that fit the filters conditions.

**Args:**

* `samples`:  The number of samples to return per run
* `keys`:  Only return metrics for specific keys
* `x_axis`:  Use this metric as the xAxis defaults to \_step
* `format`:  Format to return data in, options are "default", "pandas",  "polars"
* `stream`:  "default" for metrics, "system" for machine metrics

**Returns:**

* `pandas.DataFrame`:  If `format="pandas"`, returns a `pandas.DataFrame`  of history metrics.
* `polars.DataFrame`:  If `format="polars"`, returns a `polars.DataFrame`  of history metrics.
* `list of dicts`:  If `format="default"`, returns a list of dicts  containing history metrics with a `run_id` key.

***

### <kbd>method</kbd> `Runs.upgrade_to_full`

```python  theme={null}
upgrade_to_full() → None
```

Upgrade this Runs collection from lazy to full mode.

This switches to fetching full run data and upgrades any already-loaded Run objects to have full data. Uses parallel loading for better performance when upgrading multiple runs.

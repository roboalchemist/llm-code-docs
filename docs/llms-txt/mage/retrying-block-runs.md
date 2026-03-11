# Source: https://docs.mage.ai/orchestration/pipeline-runs/retrying-block-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrying block runs from a pipeline run

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<Note>Requires version `0.8.76` or greater.</Note>

## Automatic retry

Mage supports configuring automatic retry for block runs with the following ways

### 1. Global retry config

Add `retry_config` to project's `metadata.yaml`. This `retry_config` will be applied to all block runs.
Here is an example:

```yaml  theme={"system"}
retry_config:
  # Number of retry times
  retries: 3
  # Initial delay (in seconds) before retry. If exponential_backoff is true,
  # the delay time is multiplied by 2 for the next retry
  delay: 5
  # Maximum time between the first attempt and the last retry
  max_delay: 60
  # Whether to use exponential backoff retry
  exponential_backoff: true
```

### 2. Block level retry config

Add `retry_config` to the block config in pipeline's `metadata.yaml`. The block level `retry_config` will
override the global `retry_config`. Here is an example

```yaml  theme={"system"}
blocks:
- uuid: example_data_loader
  type: data_loader
  upstream_blocks: []
  downstream_blocks: []
  retry_config:
    retries: 2
    delay: 5
    max_delay: 10
    exponential_backoff: false
  ...
```

### 3. Pipeline level `retry_config`

<ProOnly source="workspaces" />

Add `retry_config` to the pipeline config in pipeline's `metadata.yaml`. The pipeline level `retry_config` will
override the global `retry_config`. Here is an example

```yaml  theme={"system"}
blocks:
- ...
- ...
- ...
retry_config:
  retries: 2
  delay: 5
  max_delay: 10
  exponential_backoff: false
  ...
```

The retry logs show in the same block run log page.

## Retry incomplete blocks

* Supported pipeline types: Integration and Standard pipelines
* If a pipeline run fails, you can retry from the failed block
  run (instead of retrying the entire pipeline run) by going to the individual
  pipeline runs page (`/pipelines/[pipeline_uuid]/runs/[pipeline_run_id]`).
* At the top of the individual pipeline runs page, there should be a red
  `Retry incomplete blocks` button. Click on it, and the block runs should
  retry from the failed block.

## Retry from selected block

* Supported pipeline types: Integration and Standard pipelines
* If you want to retry block runs for a pipeline run starting from a specific
  block (regardless of the block run's status), go to the same page for the individual
  pipeline run.
* Select a block run row, and a blue `Retry from selected block` button should appear.
* Note that the `Retry from selected block` button will only appear if the pipeline
  run is not currently running.
* If there is a failed block run and you try to retry from a selected block that is
  downstream from that failed block, you may get `upstream_failed` block run errors.

### Accessing the individual pipeline runs page

1. Click on a pipeline from the main Pipelines Dashboard.
2. Click on the `Runs` section or on an individual trigger from the `Triggers` section.
3. Underneath the `Block runs` column of the pipeline runs table, there is a link that
   says something like `See block runs (x)`. Click on that link to redirect to the
   individual pipeline runs page, which lists the blocks runs specific to a pipeline run.


Built with [Mintlify](https://mintlify.com).
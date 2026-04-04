# Source: https://docs.prefect.io/integrations/prefect-dbt/api-ref/prefect_dbt-cloud-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# models

# `prefect_dbt.cloud.models`

Module containing models used for passing data to dbt Cloud

## Functions

### `default_cause_factory` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-dbt/prefect_dbt/cloud/models.py#L10" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
default_cause_factory()
```

Factory function to populate the default cause for a job run to include information
from the Prefect run context.

## Classes

### `TriggerJobRunOptions` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-dbt/prefect_dbt/cloud/models.py#L29" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Defines options that can be defined when triggering a dbt Cloud job run.


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.airbyte.com/developers/pyairbyte/reference/airbyte/cloud/airbyte-cloud-constants.md

# Module airbyte.cloud.constants

Copy Page

Useful constants for working with Airbyte Cloud features in PyAirbyte.

## Variables[​](#variables "Direct link to Variables")

`FAILED_STATUSES: set[airbyte_api.models.jobstatusenum.JobStatusEnum]` : The set of `.JobStatusEnum` strings that indicate a sync job has failed.

`FINAL_STATUSES: set[airbyte_api.models.jobstatusenum.JobStatusEnum]` : The set of `.JobStatusEnum` strings that indicate a sync job has completed.

`READABLE_DESTINATION_TYPES: set[str]` : List of Airbyte Cloud destinations that PyAirbyte is able to read from.

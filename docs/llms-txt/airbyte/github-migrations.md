# Source: https://docs.airbyte.com/integrations/sources/github-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-github/latest/icon.svg)

# GitHub Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [2.1.11](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-github)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-github)(last updated 16 days ago)

* CDK Version

  [7.10.1](https://pypi.org/project/airbyte-cdk/7.10.1/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `ef69ef6e-aa7f-4af1-a01d-ef775033524e`

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

This release introduces breaking changes to the `reactions` object schema, which appears in multiple streams. The GitHub API returns reaction fields named `+1` and `-1`, but these field names contain special characters that are not supported by some destinations, causing sync errors.

### What changed[​](#what-changed "Direct link to What changed")

The reaction fields have been renamed for compatibility:

* `+1` → `plus_one`
* `-1` → `minus_one`

### Affected streams[​](#affected-streams "Direct link to Affected streams")

All streams containing the `reactions` object are affected:

* `comments`
* `commit_comments`
* `issue_events`
* `issues`
* `releases`
* `review_comments`

### Required actions[​](#required-actions "Direct link to Required actions")

After upgrading to version 2.0.0:

1. **Refresh your source schema** in the Airbyte UI to see the updated field names
2. **Reset affected streams** to re-sync data with the new field names (recommended if you need historical data with the corrected schema)
3. **Update downstream queries and dashboards** that reference the old `+1` and `-1` fields to use `plus_one` and `minus_one` instead

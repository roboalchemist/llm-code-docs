# Source: https://docs.airbyte.com/integrations/sources/posthog-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-posthog/latest/icon.svg)

# PostHog Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.25](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-posthog)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-posthog)(last updated a year ago)

* CDK Version

  [0.60.0](https://pypi.org/project/airbyte-cdk/0.60.0/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `af6d50ee-dddf-4126-a8ee-7faee990774f`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

Version 1.0.0 introduces a single change to the `events` stream. It corrects the casting of the `event` field datatype, which was incorrectly labeled as a `json` object. Now, it is accurately attributed only as a `string`, as outlined in the PostHog [documentation](https://posthog.com/docs/api/events). To apply this change, refresh the schema for the 'events' stream and reset your data.

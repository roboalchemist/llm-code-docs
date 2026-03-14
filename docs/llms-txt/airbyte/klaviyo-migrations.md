# Source: https://docs.airbyte.com/integrations/sources/klaviyo-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-klaviyo/latest/icon.svg)

# Klaviyo Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [2.17.0](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-klaviyo)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-klaviyo)(last updated 20 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `95e8cffd-b8c4-4039-968e-d32fb4a69bde`

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

Streams `campaigns`, `email_templates`, `events`, `flows`, `global_exclusions`, `lists`, and `metrics` are now pulling data using latest API which has a different schema. Users will need to refresh the source schemas and reset these streams after upgrading. See the chart below for the API version change.

| Stream             | Current API version | New API version |
| ------------------ | ------------------- | --------------- |
| campaigns          | v1                  | 2023-06-15      |
| email\_templates   | v1                  | 2023-10-15      |
| events             | v1                  | 2023-10-15      |
| flows              | v1                  | 2023-10-15      |
| global\_exclusions | v1                  | 2023-10-15      |
| lists              | v1                  | 2023-10-15      |
| metrics            | v1                  | 2023-10-15      |
| profiles           | 2023-02-22          | 2023-02-22      |

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

`event_properties/items/quantity` for `Events` stream is changed from `integer` to `number`. For a smooth migration, data reset and schema refresh are needed.

# Source: https://docs.airbyte.com/integrations/sources/linkedin-pages-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-linkedin-pages/latest/icon.svg)

# Linkedin Pages Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.25](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-linkedin-pages)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-linkedin-pages)(last updated 4 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `af54297c-e8f8-4d63-a00d-a94695acc9d3`

## Upgrading to 1.0.7[​](#upgrading-to-107 "Direct link to Upgrading to 1.0.7")

* 2 new streams have been added which support time bound incremental sync. They need additional fields `start_date` and `time_granularity_type` to be defined in the config to work. `time_granularity_type` has a default value of `DAY` set, and `start_date` has a default value set 1 year prior to the current date.

# Source: https://docs.airbyte.com/integrations/sources/timely-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-timely/latest/icon.svg)

# Timely Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.0.36](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-timely)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-timely)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `bc617b5f-1b9e-4a2d-bebe-782fd454a771`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

This version add new streams: clients, users, labels and projects. In addition to that fix the date config parameter to be in format `YYYY-MM-DDTHH:mm:ssZ` and be easy to pick up by the user. You need to update your start date to be in the format `YYYY-MM-DDTHH:mm:ssZ`.

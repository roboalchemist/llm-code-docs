# Source: https://docs.airbyte.com/integrations/sources/typeform-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-typeform/latest/icon.svg)

# Typeform Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [1.4.5](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-typeform)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-typeform)(last updated 2 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `e7eff203-90bf-43e5-a240-19ea3056c474`

## Upgrading to 1.1.0[​](#upgrading-to-110 "Direct link to Upgrading to 1.1.0")

This version upgrades the connector to the low-code framework for better maintainability. This migration includes a breaking change to the state format of the `responses` stream.

Any connection using the `responses` stream in `incremental` mode will need to be reset after the upgrade to avoid sync failures.

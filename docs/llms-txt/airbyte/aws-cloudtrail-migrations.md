# Source: https://docs.airbyte.com/integrations/sources/aws-cloudtrail-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-aws-cloudtrail/latest/icon.svg)

# Aws Cloudtrail Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.0](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-aws-cloudtrail)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-aws-cloudtrail)(last updated a year ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `6ff047c0-f5d5-4ce5-8c81-204a830fa7e1`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

The verison migrates the Aws Cloudtrail connector to the low-code framework for greater maintainability. Important update: The management\_events stream changed it's EventTime field from integer to float. Destination should adapt this change if applicable. The connector as default uses us-east-1 region for accessing streams with its custom request signer. You may need to refresh the connection schema (with the reset), and run a sync. The `start_date` parameter is now optional and the connector now takes current date as default start date Connector has a new capability of adding filters to the response attributes using the `lookup_attributes_filter` config in the spec.

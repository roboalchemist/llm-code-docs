# Source: https://docs.airbyte.com/integrations/sources/paystack-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-paystack/latest/icon.svg)

# Paystack Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.25](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-paystack)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-paystack)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `193bdcb8-1dd9-48d1-aade-91cadfd74f9b`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

Version 1.0.0 has a schema change.

The refunds schema has been changed it's 'type' in schema\['properties']\['fully\_deducted'] to integer. Destination should be aware of this change.

# Source: https://docs.airbyte.com/integrations/sources/paypal-transaction-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-paypal-transaction/latest/icon.svg)

# Paypal Transaction Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [2.6.25](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-paypal-transaction)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-paypal-transaction)(last updated 23 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `d913b0f2-cc51-4e55-a44c-8ba1697b9239`

## Upgrading to 2.1.0[​](#upgrading-to-210 "Direct link to Upgrading to 2.1.0")

Version 2.1.0 changes the format of the state object. Upgrading to 2.1.0 is safe, but downgrading to 2.0.0 is not.

To downgrade to 2.0.0:

* Edit your connection state:

  <!-- -->

  * Change the keys for the transactions and balances streams to "date"
  * Change the format of the cursor to "yyyy-MM-dd'T'HH:mm
    <!-- -->
    :ss
    <!-- -->
    +00:00" Alternatively, you can also reset your connection.

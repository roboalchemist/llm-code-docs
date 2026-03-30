# Source: https://docs.airbyte.com/integrations/sources/harvest-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-harvest/latest/icon.svg)

# Harvest Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [1.2.30](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-harvest)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-harvest)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `fe2b4084-3386-4d3b-9ad6-308f61a6f1e6`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

This update results in a change the following streams, requiring them to be cleared and completely synced again:

* `expenses_clients`
* `expenses_categories`
* `expenses_projects`
* `expenses_team`
* `time_clients`
* `time_projects`
* `time_tasks`
* `time_team`
* `uninvoiced`
* `estimate_messages`
* `invoice_payments`
* `invoice_messages`
* `project_assignments`

We're continuously striving to enhance the quality and reliability of our connectors at Airbyte. As part of our commitment to delivering exceptional service, we are transitioning the source Harvest from the Python Connector Development Kit (CDK) to our new low-code framework to improve maintainability and reliability of the connector. However, due to differences between the Python and low-code CDKs, this migration constitutes a breaking change.

## Steps to Clear Streams[​](#steps-to-clear-streams "Direct link to Steps to Clear Streams")

To clear your data for the impacted streams, follow the steps below:

1. Select **Connections** in the main nav bar.
   <!-- -->
   1. Select the connection(s) affected by the update.
2. Select the **Status** tab.
   <!-- -->
   1. In the **Enabled streams** list, click the three dots on the right side of the stream and select **Clear Data**.

After the clear succeeds, trigger a sync by clicking **Sync Now**. For more information on clearing your data in Airbyte, see [this page](/platform/operator-guides/clear.md).

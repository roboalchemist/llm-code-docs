# Source: https://docs.airbyte.com/integrations/sources/dolibarr-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-dolibarr/latest/icon.svg)

# Dolibarr Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.0.14](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-dolibarr)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-dolibarr)(last updated 23 days ago)

* Definition ID

  `10c2652f-00cf-421a-bd16-7758357e5d99`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

### Change Summary[​](#change-summary "Direct link to Change Summary")

* This version implements the incremental sync and date\_modification descendent sortfield for all parent streams, except the `company profile data` stream, as required for incremental sync for no date filter API endpoints.

### Migration Steps[​](#migration-steps "Direct link to Migration Steps")

1. Please update the user inputs of the connector
2. Update all the configured streams
3. Select the corresponding modification date parameter in the schema of the streams with incremental sync
4. Clean and refres your destination.
5. Update your Dolibarr installation to 21.0.0 or higher versions before sync

### Additional Notes[​](#additional-notes "Direct link to Additional Notes")

* This version change the sortfiled to `t.tms` that is the modification date and change sortorder to descendent for all the streams with incremental sync and their child streams.

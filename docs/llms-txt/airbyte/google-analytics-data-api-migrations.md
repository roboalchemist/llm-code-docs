# Source: https://docs.airbyte.com/integrations/sources/google-analytics-data-api-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-google-analytics-data-api/latest/icon.svg)

# Google Analytics 4 (GA4) Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [2.9.26](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-google-analytics-data-api)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-google-analytics-data-api)(last updated 14 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `3cc2eafd-84aa-4dca-93af-322d9dfeec1a`

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

This version update only affects the schema of GA4 connections that sync **more than one property**.

Version 2.0.0 prevents the duplication of stream names by renaming some property streams with a new stream name that includes the property ID.

**If you only are syncing from one property, no changes will occur when you upgrade to the new version.&#x20;**&#x54;he stream names will continue to appear as:

* "daily\_active\_users",
* "weekly\_active\_users"

If you are syncing more than one property, any property after the first will have the property ID appended to the stream name.

For example, if your property IDs are: `0001`, `0002`, `0003`, the streams related to properties `0002` and `0003` will have the property ID appended to the end of the stream name.

* "daily\_active\_users",
* "daily\_active\_users\_property\_0002",
* "daily\_active\_users\_property\_0003",
* "weekly\_active\_users",
* "weekly\_active\_users\_property\_0002"
* "weekly\_active\_users\_property\_0003"

If you are syncing more than one property ID, you will need to reset those streams to ensure syncing continues accurately.

In the future, if you add an additional property ID, all new streams will append the property ID to the stream name without affecting existing streams. A reset is not required if you add the consecutive property after upgrading to 2.0.0.

# Source: https://docs.airbyte.com/integrations/sources/pardot-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-pardot/latest/icon.svg)

# Pardot Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.0.36](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-pardot)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-pardot)(last updated a month ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `ad15c7ba-72a7-440b-af15-b9a963dc1a8a`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

Version 1.0.0 contains a number of fixes and updates to the Pardot source connector:

* Fixed authentication
* Migrate all existing streams to Pardot v5 API (except email\_clicks which is only available in v4)
* Re-implement incremental syncs for existing streams where possible
* Add 23 new streams from the v5 API (folders, emails, engagement\_studio\_programs, folder\_contents, forms, form\_fields, form\_handlers, form\_handler\_fields, landing\_pages, layout\_templates, lifecycle\_stages, lifecycle\_histories, list\_emails, opportunities, tags, tracker\_domains, visitor\_page\_views)
* Add additional configuration options to better handle large accounts (e.g. adjustable split-up windows, page size)
* Align to Pardot-recommended sort/filter/pagination conventions to avoid timeouts (based on Pardot support case #469072278)

The previous implementation of the authentication flow was no longer functional, preventing the instantiation of new sources. All users with existing connections should reconfigure the source and go through the authentication flow before attempting to sync with this connector. OSS users should be sure to manually update their source version to >=1.0.0 before attempting to configure this source.

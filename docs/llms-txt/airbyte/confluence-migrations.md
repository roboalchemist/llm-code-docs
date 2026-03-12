# Source: https://docs.airbyte.com/integrations/sources/confluence-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-confluence/latest/icon.svg)

# Confluence Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.0.21](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-confluence)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-confluence)(last updated 3 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `cf40a7f8-71f8-45ce-a7fa-fca053e4028c`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

With the release of **Confluence API V2**, several changes have been introduced to the connector, impacting endpoint structures and schema definitions. To ensure a seamless transition, follow the migration steps outlined below.

### Key Changes[​](#key-changes "Direct link to Key Changes")

* **Blog Posts:**

  * **Endpoint Change:** `GET /content?type=blogpost` → `GET v2/blogposts`
  * **Breaking Change:** Schema modifications require updating existing integrations.

* **Pages:**

  * **Endpoint Change:** `GET /content?type=page` → `GET v2/pages`
  * **Breaking Change:** Schema modifications require adjustments.

* **Spaces:**

  * **Endpoint Change:** `GET /space` → `GET v2/spaces`
  * **Breaking Change:** Schema updates necessitate migration.

### Migration Steps[​](#migration-steps "Direct link to Migration Steps")

1. **Upgrade** to version **1.0.0**.
2. **Resynchronize** the connector to reset schemas and update existing records.

For more details, refer to the official **[Confluence API V2 Changelog](https://developer.atlassian.com/cloud/confluence/changelog/#CHANGE-2425)**.

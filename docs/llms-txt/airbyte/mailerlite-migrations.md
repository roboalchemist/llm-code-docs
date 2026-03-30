# Source: https://docs.airbyte.com/integrations/sources/mailerlite-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-mailerlite/latest/icon.svg)

# MailerLite Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.23](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-mailerlite)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-mailerlite)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `dc3b9003-2432-4e93-a7f4-4620b0f14674`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

The version migrates the MailerLite connector to the be compatible with connector builder. Important:

* The forms\_popup stream schema from API has a breaking change to schema\['properties']\['settings']\['properties']\['schedule'] field to contain booleans instead of strings,
* The forms\_promotion stream schema from API has a breaking change to schema\['properties']\['double\_optin'], schema\['properties']\['settings']\['properties']\['schedule'] fields to contain booleans instead of strings"

## Connector Upgrade Guide[​](#connector-upgrade-guide "Direct link to Connector Upgrade Guide")

The destination should be ready to receive the current 1.0.0 updates of schema changes

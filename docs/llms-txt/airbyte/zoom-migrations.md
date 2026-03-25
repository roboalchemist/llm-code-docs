# Source: https://docs.airbyte.com/integrations/sources/zoom-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-zoom/latest/icon.svg)

# Zoom Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.2.44](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-zoom)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-zoom)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `cbfd9856-1322-44fb-bcf1-0b39b7a8e92e`

## Upgrading to 1.1.0[​](#upgrading-to-110 "Direct link to Upgrading to 1.1.0")

### Authentication[​](#authentication "Direct link to Authentication")

As of September 8, 2023, Zoom has [deprecated JWT](https://developers.zoom.us/docs/internal-apps/jwt-faq/) authentication and now supports Oauth instead.

### Creating a server-to-server OAuth app[​](#creating-a-server-to-server-oauth-app "Direct link to Creating a server-to-server OAuth app")

To successfully migrate, please use [Zoom's migration guide](https://developers.zoom.us/docs/internal-apps/jwt-app-migration/) to create a new server-to-server OAuth app and generate the necessary credentials.

When creating the app, ensure you grant it access to the following scopes:

* user:read
  <!-- -->
  :admin
* meeting:read
  <!-- -->
  :admin
* webinar:read
  <!-- -->
  :admin
* chat\_channel:read
  <!-- -->
  :admin
* report:read
  <!-- -->
  :admin

To successfully authenticate your connection in Airbyte, you will need to input the following OAuth credentials:

* client\_id
* client\_secret
* account\_id
* authorization\_endpoint

### Schema changes[​](#schema-changes "Direct link to Schema changes")

The type of the 'meeting\_id' field in Meeting Registration Questions stream has been changed from "string" to "integer". Users with existing connections that are syncing data from this stream should refresh their schemas and reset their data.

#### Refresh affected schemas and reset data[​](#refresh-affected-schemas-and-reset-data "Direct link to Refresh affected schemas and reset data")

1. Select **Connections** in the main nav bar.
   <!-- -->
   1. Select the connection affected by the update.

2. Select the **Replication** tab.

   <!-- -->

   1. Select **Refresh source schema**.
   2. Select **OK**.

note

Any detected schema changes will be listed for your review.

3. Select **Save changes** at the bottom of the page.
   <!-- -->
   1. Ensure the **Reset affected streams** option is checked.

note

Depending on destination type you may not be prompted to reset your data.

4. Select **Save connection**.

note

This will reset the data in your destination and initiate a fresh sync.

For more information on resetting your data in Airbyte, see [this page](/platform/operator-guides/clear.md)

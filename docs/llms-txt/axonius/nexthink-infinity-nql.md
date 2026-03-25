# Source: https://docs.axonius.com/docs/nexthink-infinity-nql.md

# Nexthink Query Language (NQL)

Nexthink Query Language (NQL) is a programming language developed by Nexthink for querying data from its platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Software, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Nexthink Query Language (NQL) server.

<Callout icon="📘" theme="info">
  Note

  The URL must be as follows:
  `https://instance.api.region.nexthink.cloud`

  Replace `instance` with the name of the instance and `region` with the name of one of the following regions:

  * `us` for the United States

  * `eu` for the European Union

  * `pac` for Asia-Pacific

  * `meta` for the Middle East, Turkey, and Africa

    For more information, see [Getting an authentication token](https://developer.nexthink.com/docs/api/getting-an-authentication-token).
</Callout>

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets. For information on credentials, see [API credentials](https://developer.nexthink.com/docs/api/api-credentials).
3. **Device Query ID** *(required)* - Enter the device query you created in your system so that Axonius can export the necessary data. For information on creating a query, see [Setting up API credentials](https://developer.nexthink.com/docs/api/nql-api-overview).

<Callout icon="📘" theme="info">
  Note

  The following query is required for proper parsing of devices:
  `devices during past 7d`

  `| list device.name, device.entity, device.hardware.model, device.hardware.type, device.operating_system.name, device.days_since_last_seen, device.cpus, device.disks, device.gpus, device.boot.days_since_last_full_boot, device.connectivity.last_connectivity_type, device.hardware.machine_serial_number, device.location.type, device.login.last_login_user_name, device.operating_system.build, device.organization.entity`

  For query information, see [Nexthink Query Language (NQL)](https://docs.nexthink.com/platform/latest/nexthink-query-language-nql).
  For data model information, see [NQL data model](https://docs.nexthink.com/platform/latest/nql-data-model).
</Callout>

4. **Software Query ID** *(optional)* - Enter the ID of the query to fetch software information.
5. **User Query ID** *(optional)* - Enter the ID of the query to fetch user information.

<Callout icon="📘" theme="info">
  Note

  The following query is required for proper parsing of users:

  `| list user.ad.username, user.days_since_last_seen, user.first_seen, user.last_seen, user.name, user.sid, user.type, user.uid, user.upn, user.upn_privacy_level`
</Callout>

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Nexthink Query Language (NQL)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nexthink%20Query%20Language%20(NQL).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Enrich Download Device Export Endpoint with Download Device Software Export Endpoint** - Select this option to enrich the Download Device Export endpoint with the Download Device Software Export endpoint.
2. **Fetch Users from Download User Export Endpoint** - Select this option to fetch users based on the **User Query ID** in [Parameters](/docs/nexthink-infinity-nql#parameters).
3. [**Custom Parsing**](/docs/nexthink-infinity-nql#custom-parsing)

### Custom Parsing

Enable this option to define how to parse specific fields from the raw data fetched. You can choose to parse the data into an already existing field, or create a new one. This can be set separately for each type of asset fetched by the adapter: devices or users.

<Image alt="Nexthink NQL Custom Parsing.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nexthink%20NQL%20Custom%20Parsing.png" />

Expand each asset type's Custom Parsing section to add fields. For each field, specify the following:

* **Field Title** - Select a column title from the list.

* **Raw Path** - The path to the field in the raw data, for example: `my_path|my_sub_path`

* **Type** - Select a field type from the list: string, boolean, etc. Will be ignored for common fields.

* **Field Type** - Specify whether the filed is a single value or a list field. Will be ignored for common fields.
  Click **+ Add Field** to add as many fields as you like, or **x** to delete the row.

<Image alt="Nexthink NQL AddField.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nexthink%20NQL%20AddField.png" />

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [NQL API](https://developer.nexthink.com/docs/api/api-credentials#accessing-api-credentials).

## Supported From Version

Supported from Axonius version 6.1
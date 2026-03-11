# Source: https://docs.axonius.com/docs/code42.md

# Code42 Incyder

Code42 Incyder (formerly Code42) is a next-gen DLP solution used to detect insider threats, satisfy regulatory compliance, and accelerate incident response investigations.

### Asset Types Fetched

* Devices
* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password for Cloud
* Client ID/Client Secret for on-prem

### APIs

Axonius uses the [Code42 API](https://developer.code42.com/api/).

<Callout icon="📘" theme="info">
  Note

  To use the Code42 Incyder adapter, you must have a product plan that includes access to the Code42 API. For more details, see [Code42 Support - API access](https://support.code42.com/hc/en-us/articles/14827740809239-API-access#api-access-0-0).
</Callout>

### Permissions

The value supplied in [User Name](#required-parameters) must have Read access to devices with a read-only role. This role provides permission to access the data necessary to a given API resource. For more details, see [Code42 support - Manage user roles](https://support.code42.com/Administrator/Cloud/Monitoring_and_managing/Manage_user_roles).

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Code42 Domain** - The hostname or IP address of the Code42 server.
2. **Authentication Method** - Select whether to authenticate via user credentials or client credentials.
3. **User Name** and **Password** - If the authentication method is via user credentials, specify the credentials for a user account that has the Required Permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  These parameters are only displayed when the **User Credentials** option is selected from the **Authentication Method** dropdown.
</Callout>

4. **Client ID** and **Client Secret** - If the authentication method is via client credentials, specify the Client ID and Client Secret to be used to authenticate the request. For more information about obtaining a Client ID and Client Secret, see [API Clients](https://support.code42.com/Incydr/Admin/Code42_console_reference/API_clients).

<Callout icon="📘" theme="info">
  Note

  These parameters are only displayed when the **Client Credentials** option is selected from the **Authentication Method** dropdown.
</Callout>

<Image alt="Code42 Incyder.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Code42%20Incyder.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Use agents as the default for devices** - Select this option to use the `agents` endpoint as the default for fetching devices.
2. **Fetch devices backup usage** - Select this option to fetch the device's backup usage.

<Callout icon="📘" theme="info">
  Note

  This only exists in newer versions (/api/v1) and not in the old version (/api).
</Callout>

2. **Filter by Org ID**  - Toggle on this option to filter by Org IDs. Then enter a comma separated list of Org IDs in the Org ID allow list, to only fetch from these Org IDs.
3. **Ignore Deactivated/Blocked Users** - Select whether to ignore users fetched from Code42 with the values “Deactivated” or “Blocked” in the status field.
4. **Ignore Deactivated/Blocked Devices** - Select whether to ignore devices fetched from Code42 with the values “Deactivated” or “Blocked” in the status field.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Deactivate Code42 Agent](/docs/deactivate-code42-agent)
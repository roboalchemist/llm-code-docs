# Source: https://docs.axonius.com/docs/duo-beyond.md

# Duo Beyond

Duo Beyond identifies corporate vs. personal devices, blocks untrusted devices, and give users secure access to internal applications.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Integration key/Secret key

### APIs

Axonius uses the [Users endpoint](https://duo.com/docs/adminapi#users) of the [Duo Admin API](https://duo.com/docs/adminapi#overview).

### Grant Access to Duo Admin API

<Callout icon="📘" theme="info">
  Note

  Note that only administrators with the Owner role may contact Duo Support to request access to the Admin API application or can create or modify an Admin API application in the Duo Admin Panel.
</Callout>

1. Sign up for a Duo account.
2. Contact Duo Support to request Admin API access.
3. Log in to the Duo Admin Panel and navigate to **Applications**.
4. Click **Protect an Application** and locate **Admin API** in the applications list. Click **Protect this Application** to get your **integration key, secret key**, and **API hostname**.
5. Grant your Admin API application the following permission:
   * **Grant read resource** - required to fetch basic information from Duo Beyond.
   * **Grant administrators** - required to fetch Duo Beyond administrators, and details about their hardware tokens (serial number, etc).

For more details, see [Duo Admin API](https://duo.com/docs/adminapi#overview).

### Permissions

Consult with your vendor for permissions for reading the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Duo Admin API Host** - The API hostname of the Duo Beyond. To get your API hostname, see [Grant Access to Duo Admin API](/docs/duo-beyond#grant-access-to-duo-admin-api). The field value format is: `[instance].duosecurity.com`.
2. **Integration key** and **Secret key** - Specify the integration key and the secret key for your Admin API access. For details, see [Grant Access to Duo Admin API](/docs/duo-beyond#grant-access-to-duo-admin-api).

![Duo Beyond.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Duo%20Beyond.png)

### Optional Parameters

* **HTTPS proxy** - A proxy to use when connecting to the Duo Admin API Host.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch endpoints** *(required, default: false)* - Select whether to fetch endpoints.
2. **Fetch phone credits usage** - Select this option to fetch users with the Telephony Logs (which contain the credit usage for each action) by phone number. This setting requires the `Grant read log` permission.
3. **Fetch phone credits from the specified amount of days back** *(optional, default: 10)* - Specify the amount of days back to look for credit usage logs. This setting is only relevant if `Fetch phone credits usage` is enabled.
4. **Get user activity logs for the last specified amount of days back** *(optional, default: 0)* - Specify the amount of days back to look for user activity logs. If the default amount remains as 0, then activity logs are not fetched.
5. **Fetch admin user details** *(required, default: true)* - Clear option to not fetch admin user details.
6. **User field exclusion list** *(optional)* - Enter a comma separated list of field names from the advanced view of the Duo Beyond user adapter that will be removed from new devices in subsequent discovery cycles from both the basic and advanced views, enabling you to exclude specific fields from being fetched. If this field is empty, all fields are fetched.
7. **Fetch Phones as devices** - By default Axonius fetches phones as devices. If you clear this option, the adapter still fetches phone data, but the data appears under the associated user asset instead of as a separate device asset.
8. **Set a device’s single user as owner** - Select this option to set a device's user as owner if the device only has one user.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>
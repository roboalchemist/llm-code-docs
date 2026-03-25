# Source: https://docs.axonius.com/docs/beyondtrust-password-safe.md

# BeyondTrust Password Safe

BeyondTrust Password Safe provides discovery, management, auditing, and monitoring for any privileged credential.

### Asset Types Fetched

* Devices, Users, Roles, Groups, Activities, Application Resources

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password
* API Token

### APIs

Axonius uses the [BeyondInsight and Password Safe API](https://www.beyondtrust.com/docs/beyondinsight-password-safe/documents/ps/bi-ps-api.pdf).

### Initial Setup Instructions

#### Part 1 - Creating an API Key Policy API Registration

1. Log in to BeyondInsight BeyondTrust.
2. Navigate to **Configuration> General> API Registrations**.
3. In the **API Registrations** pane, click **Create API Registration**.
4. From the dropdown, select **API Key Policy**. The Details pane is displayed.
5. Under **Name**, type **axonius**.
6. Under **Authentication Rules**, click **Add Authentication Rule**.
7. In the **Create New Authentication Rule** pane that opens, select **IP Rule**, and under **Type**, select the **type** of the IP rule: **Single IP Address**, **IP range**, or **CIDR per line**.
8. Provide a valid source **IP Address** (IPv4 or IPv6), **IP Range**, or **CIDR** from which requests can be sent for this API key.
9. Click **Create Rule**.
10. Click **Create Registration**. BeyondInsight generates a unique identifier (API key) in the **Key** field. The API key is masked. Click the Show Key icon to show the key value.

![BeyondTrustSetup1](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrustSetup1.png)

#### Part 2 - Creating an Axonius Group

1. Navigate to **Configuration `>` Role Based Access> User Management**.
2. From the **Groups** tab, click **+ Create New Group**.
3. Select **Create a New Group**.
4. Under **Group Name**, type 'Axonius', then click **Create Group**.
5. Add the API Registration created in Part 1 to the new group.

![BeyondTrustSetup2](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-LYC5MIMC.png)

6. Create an ‘Axonius’ user and add it to the group.

#### Part 3 - Editing the Group Features

1. Navigate to the Axonius Group’s **Features** section.
2. Add the following permissions:
   * Asset Management - Read only
   * User Account Management - Read only

![BeyondTrustSetup3](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-F7UC1208.png)

3. Navigate to the group’s **Smart Groups** section.
4. Add the following permissions:
   * All Assets in Password Safe - Read only. After adding this permission, click the **Edit** option next to it. Check the Information security administrator box and select **Save Roles**.
   * All Managed Accounts - Read only
   * ﻿﻿﻿All Managed Systems - Read only

![BeyondTrustSetup4](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-FLMN253A.png)

### Permissions

The following permissions are required:

* `Permissions AssetManagement.Read` or `ScanManagement.ReadWrite` - Devices
* User Accounts Management (Read) - Users
* Secrets-Safe (Read) - Secrets
* Password Safe Account Management (Read) - Secrets
* Read access to the Smart Rule referenced by ID - Rules
* User Audit Management (Read) - Audit Activities

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the BeyondTrust Password Safe server.
2. **User Name** *(required)* and **Password** *(optional)* - The credentials for a user account that has the Required Permissions to fetch assets. If you use a domain user, you need to enter a backslash ( \ ) between the domain name and the user name, for example: `MyDomain\MyUserName`
3. **API Token** - An API Token associated with a user account that has permissions to fetch assets.

![BeyondTrustPasswordSafe.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrustPasswordSafe\(1\).png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Get auto managed information for accounts** - Select this option to fetch the field 'Auto Managed'.
2. **Do not fetch devices without an Asset ID** - By default Axonius fetches all Managed Devices. Select this option to not fetch Managed Devices with an empty Asset ID.
3. **Fetch platforms** - Select this option to fetch device platforms.
4. **Additional assets to fetch** - From the dropdown, select one or more additional asset types to fetch.
5. **Assets to fetch from Managed Systems** -  From the dropdown, select one or more additional assets to fetch from managed system devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [BeyondTrust Password Safe - Manage Assets](/docs/beyondtrust-password-safe-manage-assets)

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, and it is not functioning as expected.

| Version                                  | Supported | Notes |
| ---------------------------------------- | --------- | ----- |
| BeyondInsight and Password Safe API 21.1 | Yes       |       |
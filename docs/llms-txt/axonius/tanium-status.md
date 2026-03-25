# Source: https://docs.axonius.com/docs/tanium-status.md

# Tanium Client Status

The Tanium Client Status adapter provides an inventory of all clients that have registered with the Tanium platform.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443: REST API

**Authentication Method**

* User Name/Password
* API Token ID/API Token

### Permissions

You must [Create a Micro Admin Role](#create-a-micro-admin-role) since none exists that grants these Micro Admin Permissions:

1. Read System Status

## Create a Micro Admin Role

These are the steps to create a role that grant the required [Micro Admin Permissions](#permissions):

1. Log in to the value supplied in [Hostname or IP Address](#required-parameters) with an account that has the permissions necessary to edit roles.
2. In the navigation menu:
   1. Go to the **Permissions** `>` **Roles** page.
3. In the **Permissions Page**:
   1. Click **New Role**.
   2. Select **Grant Micro Admin Role**.
4. In the **Create Role** page in the **Role Details** section:
   1. Fill in the **Name** field. *(for example: System Status Read Only)*
5. In the **Create Role** page In the **Micro Admin Permissions** section click the plus sign next to the following permissions:
   1. Read System Status
6. The **Create Role** page should look like:

<Image alt="image.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(487).png" />

7. At the bottom of the **Create Role** page:
   1. Click  **Save**.
8. In the **Notice** dialog window:
   1. Click **Continue**.

## Assigning Required Permissions

These are the steps to assign the Required Permissions to the value supplied in [User Name](#required-parameters):

1. Log in to the value supplied in [Hostname or IP Address](#parameters) with an account that has the permissions necessary to edit users.
2. In the navigation menu:
   1. Go to the **Administration** `>` **Users** page.
3. In the **Users** Page:
   1. Select the value supplied in [User Name](#required-parameters) from the list of users.
   2. Click **View User**.
4. In the **User Administration** page in the **Roles and Effective Permissions** section:
   1. Click **Edit Roles**.
5. In the **Assign Roles** page in the **Role Management** `>` **Grant Roles** section:
   1. Click **Edit**.
6. In the **Edit Grant Roles** dialog window:
   1. Select the name of the role created in [Create a Micro Admin Role](#create-a-micro-admin-role).
   2. Click **Save**.
7. In the **Assign Roles** page:
   1. Click **Show Preview to Continue**.
   2. Click **Save**.
8. In the **Notice** dialog window:
   1. Click **Continue**.
9. The **User Administration** page should look like this:

<Image alt="tanium_useradmin_status" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/tanium_useradmin_status.png" />

10. Perform the steps in [Verifying Permissions](#verifying-permissions).

## Verifying Permissions

1. Log in to the value supplied in [Hostname or IP Address](#required-parameters) with the values supplied in [User Name and Password](#required-parameters).
2. In the navigation menu:
   1. Go to the **Administration** `>` **System Status** page.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Hostname or IP Address** - The hostname or IP address of the Tanium server. This adapter supports both on-premise and Tanium Cloud instances. When connecting to a Tanium Cloud instance, "**-api**" must be added to the end of the subdomain of your Tanium Cloud instance. For example: "*domain.cloud.tanium.com*" should be entered as "*domain-api.cloud.tanium.com*".
2. **User Name or API Token ID** - The credentials for a user account that has the Required Permissions to fetch assets. If an API token is being used for authentication, this must be the ID of the API token. The Token ID column in Tanium may be hidden.
3. **Password or API Token** - The credentials for a user account that has the Required Permissions to fetch assets. If an API token is being used for authentication, this must be the API token string.

<Callout icon="📘" theme="info">
  More information on API Tokens

  * When connecting to a Tanium Cloud instance, an API token **must** be used.
  * The API Token string **contains** the word token; when copying this, ensure that `token`is included in your input and not just the numbers within the string.
  * When creating an API token in Tanium, the default value for "Expire in Days" is 7. It is recommended to set this value to the maximum allowed value of 365.
  * Please see the Tanium Documention on [Managing API tokens](https://www.tanium.com/blog/getting-data-out-of-tanium-with-the-api-gateway-and-graphql/) for more information.
</Callout>

![TaniumClientStatus](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TaniumClientStatus.png)

### Optional Parameters

1. **Only fetch clients that have registered in the past N minutes** - Only fetch assets that have registered with the Tanium platform within the past minutes supplied by this value. Tanium considers any agent that has not reported in the past 5 minutes as "broken", however leave this value empty if you want to be able to build queries in Axonius that check for "broken agents". A value of "0" will disable this filter.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **Warn if token expires in X days or less** - Specify how many days before the token expiration to start generating fetch events warning about it.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Number of assets to fetch per page** *(required, default: 1000)* - Control the number of assets that are fetched per page.
2. **Number of seconds to wait in between each page fetch** *(required, default: 10)* - Control the number of seconds to wait in between each page.
3. **Devices to exclude by host name** *(optional)* - A comma-separated list of device host names to exclude.
4. **Devices to exclude by model** *(optional)* - A comma-separated list of device models to exclude.
5. **Devices to exclude by domain** *(optional)* - A comma-separated list of device domain names to exclude.
6. **Deduplicate devices** - Select this option to deduplicate devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Tanium - Create Action](/docs/tanium-create-action)
* [Tanium - Create Software Deployment](/docs/tanium-deploy-software)

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                               | Supported | Notes                                                                      |
| ------------------------------------- | --------- | -------------------------------------------------------------------------- |
| Tanium versions prior to 7.3.314.3424 | No        | This adapter utilizes the REST API, which was added in Tanium 7.3.314.3424 |
| Tanium 7.3.314.3424                   | Yes       |                                                                            |
| Tanium 7.3.314.3668                   | Yes       |                                                                            |
| Tanium 7.3.314.4147                   | Yes       |                                                                            |
| Tanium 7.3.314.4250                   | Yes       |                                                                            |
| Tanium Cloud                          | Yes       |                                                                            |
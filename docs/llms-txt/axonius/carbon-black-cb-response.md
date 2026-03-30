# Source: https://docs.axonius.com/docs/carbon-black-cb-response.md

# VMware Carbon Black EDR (Carbon Black CB Response)

VMware Carbon Black EDR (formerly Carbon Black CB Response) is a threat hunting and incident response solution that delivers continuous visibility in offline, air-gapped, and disconnected environments using threat intel and customizable detections.

**Related Enforcement Actions**

* [VMware Carbon Black Cloud EDR - Isolate/Unisolate Assets](/docs/isolate-unisolate-in-carbon-black-cb-response)

<Callout icon="📘" theme="info">
  Note

  To successfully delpoy this adapter, ensure to add your Axonius server to the allow list in the Carbon Black console's policy settings.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **VMware Carbon Black EDR Domain** *(required)* - The hostname or IP address of the VMware Carbon Black EDR admin local server or the cloud service.
2. **User Name** and **Password** *(optional, default: empty)* - The user name and password for an account that has read access to the API.
   * If supplied, Axonius will use the specified user name and password credentials to fetch data from VMware Carbon Black EDR.
   * If not supplied, Axonius will use the specific API Key to fetch data from VMware Carbon Black EDR.
3. **API Token** *(optional, default: empty)* - API Token to be authenticated against the VMware Carbon Black EDR API. For details, see the section below.
   * If supplied, Axonius will use the specific API Key to fetch data from VMware Carbon Black EDR.
   * If not supplied, Axonius will use the specified username and password credentials to fetch data from VMware Carbon Black EDR.

<Callout icon="📘" theme="info">
  Note

  It is recommended to create and to use an API token as the authentication method, as the user name and password credentials are not supported for all VMware Carbon Black EDR versions.

  You must specify an **API Token** or **Username** and **Password**, but not both. If all of those fields are populated, Axonius will try to authenticate with the supplied **Username** and **Password**.
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![VMware Carbon Black EDR.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VMware%20Carbon%20Black%20EDR.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Fetch uninstalled devices** *(required, default: True)* - Select whether to fetch uninstalled devices.
   * If enabled, all connections for this adapter will  fetch uninstalled devices.
   * If disabled, all connections for this adapter will not fetch uninstalled devices.
2. **Fetch inactive devices in the last X days** *(optional, default: empty)* - Select whether to fetch inactive devices.
   * If supplied, all connections for this adapter will fetch inactive devices that have communicated with the VMware Carbon Black EDR server in that last specified number of days.
   * If not supplied, all connections for this adapter will not fetch inactive devices.
3. **Fetch only the most recent device per computer SID** *(required, default: False)* - Select whether to fetch only the recent device per each SID.
   * If enabled, all connections for this adapter will fetch only the recent device per each SID.
   * If disabled, all connections for this adapter will fetch all devices, even if there is more than one device for a specific SID.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Creating an API Key

To create an API Key, do as follows:

1. As an admin, connect to the VMware Carbon Black EDR admin panel.
   Click on the user management logo to open the user management tab. Then, click "Teams" and "Create Team":

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(125\).png)
 

2. Type a name for the new team and drag the relevant group to "Viewer Access". Click "Save Changes":

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(126\).png)

3. Go to "Users" and click "Add User". Fill in the details and assign the user to the team we just created. Optional: If you want to be able to isolate and un-isolate devices from the Axonius control panel, assign the new user to the "Administrators" group:

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(127\).png)

4. Log out of the admin panel and login as the new user. Then, go to "My Profile". Click on API Token to see your API token

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(128\).png)
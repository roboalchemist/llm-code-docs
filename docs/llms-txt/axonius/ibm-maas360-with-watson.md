# Source: https://docs.axonius.com/docs/ibm-maas360-with-watson.md

# IBM MaaS360 with Watson

IBM MaaS360 with Watson is a Unified Endpoint Management (UEM) platform covering endpoints, end-users, apps, content, and data. It also gives visibility and control to manage mobile devices running iOS, macOS, Android, and Windows.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **IBM MaaS360 Domain** *(required)* - Your IBM MaaS360 domain.
2. **User Name** and **Password** *(required)* - Provide the user name and password for an admin user.
3. **Billing Id** *(required)* - This ID is also referred to as the Account ID. This ID is located in the MaaS360 management console at Setup `>` Deployment Settings.
4. **Application Id, Application Version, Platform Id, Application Access Key** *(required)* - Contact IBM Support and mention that you would like to use the Axonius application in the [IBM X-Force Exchange portal](https://exchange.xforce.ibmcloud.com/hub/MaaS360) and request these values.
5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ibmmasa.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ibmmasa.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Add location information to the devices** - Select this option to fetch location data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>
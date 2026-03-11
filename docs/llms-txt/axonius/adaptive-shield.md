# Source: https://docs.axonius.com/docs/adaptive-shield.md

# Adaptive Shield

Adaptive Shield is a security posture management platform used to help businesses manage their cloud services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.adaptive-shield.com`)* - The hostname or IP address of the Adaptive Shield server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Adaptive Sheild.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adaptive%20Sheild.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Days of events data** *(required, default: 90)* - Specify the number of days to fetch data about events.
2. **Fetch users from Users inventory** *(optional, default: False)* - Select to fetch users managed by the system from Users Inventory, in addition to system users and user activities.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## API

Axonius uses the

* api/v1/accounts/`{account_id}`/device\_inventory  to fetch devices
* api/v1/accounts/`{account_id}`/user\_inventory to fetch users.
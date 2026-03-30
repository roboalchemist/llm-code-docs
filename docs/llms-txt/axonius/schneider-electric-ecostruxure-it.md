# Source: https://docs.axonius.com/docs/schneider-electric-ecostruxure-it.md

# Schneider Electric EcoStruxure IT Expert & Data Center Expert

Schneider Electric EcoStruxure IT provides software and services for IT and Data Center teams to monitor and manage critical IT infrastructure on-premise, in the cloud, and at the edge.

<Callout icon="📘" theme="info">
  Note

  This adapter is for the Schneider Datacenter. To fetch data from Schneider IT advisor see [Schneider Electric EcoStruxure IT Advisor](/docs/schneider-electric-ecostruxure) adapter
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **EcoStruxure IT  Domain** *(required, default: api.ecostruxureit.com)* - The hostname of the EcoStruxure IT API server, in the format *api.ecostruxureit.com*.
2. **User Name** and **Password** *(optional)* - The credentials for a user account that has the required permissions to fetch assets.
3. **API Key** *(optional)* - An API Key associated with a user account that has the required permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  Connect either using a user name and a password, or an API Key.
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Schneider Electric EcoStruxure IT](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Schneider%20Electric%20EcoStruxure%20IT.png)

## APIs

Axonius uses the [EcoStruxure IT API](https://api.ecostruxureit.com/rest/).
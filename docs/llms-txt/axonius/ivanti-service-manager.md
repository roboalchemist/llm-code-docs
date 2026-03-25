# Source: https://docs.axonius.com/docs/ivanti-service-manager.md

# Ivanti Service Manager

Ivanti Service Manager is a cloud based ITSM solution that provides workflows automation, IT help desk and support ticket features, and ITIL service management processes.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Software, SaaS Applications

## Parameters

1. **Ivanti Service Manager Domain** *(required)* - The hostname of the Ivanti Service Manager server.

2. **API Key** *(required)* - REST API key created for a tenant that is used for authorizing REST API endpoints. For details on creating a REST API key from the Ivanti Service Manager configuration console, see [Ivanti Service Manager - Using the REST API Key](https://help.ivanti.com/ht/help/en_US/ISM/2019.2/admin/Content/Configure/API/Using-REST-API-Key.htm#CreatingRESTAPIKey).

3. **URL Base Prefix** *(optional, default: api)* - Enter a suffix to append to the domain (not always requested).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Ivanti Service Manager.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Ivanti%20Service%20Manager.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch software information** - Select this option to fetch software information and correlate to relevant devices.
2. **Additional CI types to fetch** - From the dropdown select additional asset types to fetch as devices.
3. **Assets to fetch per page**  *(default: 100)* - Enter a number of assets to fetch per page using Ivanti Service Manager API requests. The value cannot exceed 100.
4. **Number of requests to perform in parallel** *(default: 10)* - Enter a value for the  amount of requests to send in parallel.
5. **Enrich Devices with network adapter component information** - Select this option to fetch enhanced network interface information for devices from the following table: `frs_cicomponent__networkadapters` .

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Ivanti Service Manager REST API](https://help.ivanti.com/ht/help/en_US/ISM/2019.2/admin/Content/Configure/API/RestAPI-Introduction.htm).

<br />

## **Related Enforcement Actions**

* [Ivanti - Create Assets](/docs/create-ivanti-service-manager-computer)
* [Ivanti - Update Assets](/docs/update-ivanti-service-manager-computer)
* [Ivanti - Create Software](/docs/create-ivanti-service-manager-software)
# Source: https://docs.axonius.com/docs/logmein-central.md

# LogMeIn Central

LogMeIn Central is a cloud-based endpoint management solution that enables monitoring and management of endpoint infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Software
* SaaS Applications

<Callout icon="📘" theme="info">
  Note

  To fetch [System inventory fields](https://documentation.logmein.com/webhelp/EN/CentralDeveloper/LogMein_Central_Developer/LogMeIn_Central_GET_SystemInventory_List.html) and [Hardware inventory fields](https://documentation.logmein.com/webhelp/EN/CentralDeveloper/LogMein_Central_Developer/LogMeIn_Central_GET_HardwareInventory_List.html) along with devices' basic data from the LogMeIn Central server, it is required to [ Activate Inventory Reporting](https://support.logmeininc.com/central/help/how-to-activate-inventory-reporting-central-c-central-configuration-enableinventory).
</Callout>

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the LogMeIn Central server.
2. **Company ID** and **Pre-Shared Key (PSK)** *(required)* - A LogMeIn Central Account holder must obtain their PSK and Company ID from the LogMeIn Central server -> **Configuration** `>` **API** tab.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![LogMeIn Central.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LogMeIn%20Central.png)

## APIs

Axonius uses the [LogMeIn API](https://documentation.logmein.com/webhelp/EN/CentralDeveloper/LogMein_Central_Developer/LogMeIn_Central_API_Welcome.html).
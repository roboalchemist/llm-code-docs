# Source: https://docs.axonius.com/docs/web-server-information.md

# Web Server Information

The Web Server Information adapter provides information about the web server for a given website domain, including the server type, its version and operating system, the content management system (CMS) name and its version, the installed CMS plugins, versions, and more.

### Asset Types Fetched

* Devices, Certificates

## Before You Begin

#### Ports

If **Fetch data from SSL scanner** is enabled, Axonius must be able to communicate with the value supplied in **Web Server Domain** via an SSL port (default: 443).

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Web Server Domain** - Website URL, hostname or an IP address.
2. **Web Server Ports** *(comma separated, default: 443)* - Specify the ports to connect to in order to fetch the web server information.

<Image alt="WebServerInformationParameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-3MX68PF8.png" />

### Optional Parameters

1. **HTTPS Proxy** - A proxy to use when connecting to **Web Server Domain**.
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **Web Server Domain List** - Upload a JSON file with a list of domains. This allows you to add a large number of domains at once. The format of the JSON file should be:
   ```json

   [
     {
       "domain": "",
       "port": "",
       "https_proxy": "",
       "verify_ssl": ""
     },
     {
       "domain": "",
       "port": "",
       "https_proxy": "",
       "verify_ssl": ""
     },
     {
       "domain": "",
       "port": "",
       "https_proxy": "",
       "verify_ssl": ""
     }
   ]

   ```
   To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](https://docs.axonius.com/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch data from SSL scanner** *(default: true)* - Enable this option to fetch data using an SSL scan.
   * When enabled, this will enrich device data with SSL Labs data, that includes information about the server host, its endpoints and indications on exposure to known SSL vulnerabilities, such as Heartbleed and POODLE.
     * To enrich device with data using an SSL scan:
       * Host name is required in the **Web Server Domain** field (see [Required Parameters](/docs/web-server-information#required-parameters)). If the device data does not include a host name, one of the following can be used:
         * Device IP address, that must be a public IP address.
         * Domain, if fetched as part of the SSL Certificate data.
       * An SSL port (default: 443) must be opened for Axonius to use the SSL Labs API.

2. **Save Raw Data** - Select this option to save raw data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](https://docs.axonius.com/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Web Server Information - Enrich Asset Data](/docs/en/enrich-device-data-with-web-server-information)
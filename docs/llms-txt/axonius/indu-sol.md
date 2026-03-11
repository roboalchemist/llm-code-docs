# Source: https://docs.axonius.com/docs/indu-sol.md

# PROmanage NT

PROmanage NT is a network management and monitoring tool that helps IT teams manage and monitor their network infrastructure, including devices, connectivity, and performance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the PROmanage NT server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PROmanage NT](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PROmanage%20NT.png)

## APIs

Axonius uses the PROmanage NT API.

## Generate API Key

To generate a token:

1. Log into the website as an **admin**.
2. Navigate to the **API Token** menu item and click **Create Token**.
   * Click **Copy Token** to copy the generated token to the clipboard.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Supported From Version

Supported from Axonius version 6.1.64
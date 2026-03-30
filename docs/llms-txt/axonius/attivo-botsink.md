# Source: https://docs.axonius.com/docs/attivo-botsink.md

# Attivo BOTSink

Attivo BOTSink offers deception decoy technology and threat detection.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Attivo BOTSink server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Attivo" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Attivo.png" />

## APIs

Axonius uses the Attivo BOTsink Manager REST APIs.

## Required Ports

Axonius must be able to communicate with the REST APIs via the following port:

* **Port 8443**

## Required Permissions

The value supplied in [User Name](#parameters) must have REST API permissions to fetch assets.

To create a user with only API access:

1. From Attivo BOTsink, click **Administration** and navigate to **User Accounts** `>` **Configuration**. The **Configure Users** page is displayed.
2. Click the **Add** button. The **User Add** page is displayed.
3. From the **Access Type** dropdown, select **REST API**.
4. Enter the details in the remaining fields and click **Save**.

## Supported From Version

Supported from Axonius version 4.5
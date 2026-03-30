# Source: https://docs.axonius.com/docs/intel-ema.md

# Intel EMA

Intel® Endpoint Management Assistant (Intel® EMA) software provides the ability to remotely and securely manage Intel® Active Management Technology (Intel® AMT) devices beyond the firewall, via the cloud, on known Wi-Fi networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Intel® EMA server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Auth Method** - Select an Authentication method, either **User Name and Password** (default) or **Client ID and Client Secret**.
   * **User Name** and **Password** - The credentials for a user account that has permission to fetch assets.
   * **Client ID** and **Client Secret** - The Client ID and Client Secret for an account that has permissions to fetch assets. For more information about obtaining a Client ID and Client Secret refer to the [Intel® EMA API Guide](https://www.intel.com/content/dam/support/us/en/documents/software/manageability-products/intel-ema-api-guide.pdf).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Intel%20EMA](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Intel%20EMA.png)

## APIs

Axonius uses the [REST API for Intel(R) Endpoint Management Assistant(Latest)](https://www.intel.com/content/dam/support/us/en/documents/software/manageability-products/Latestswagger.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Supported From Version

Supported from Axonius version 6.0
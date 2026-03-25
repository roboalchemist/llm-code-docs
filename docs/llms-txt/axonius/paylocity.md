# Source: https://docs.axonius.com/docs/paylocity.md

# Paylocity

Paylocity is a cloud-based payroll and human capital management software.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Paylocity server.

2. **Client ID** **Client Secret** *(required)* -  Paylocity  provides the secure client credentials and sets up the scope (type of requests and allowed company numbers). Paylocity then provides a unique client id, secret, and Paylocity public key for the data encryption.[Refer to Paylocity Authorization](https://prod.cdn.paylocity.com/developer/index.html#section/Overview)

3. **Company ID** *(required)* - The company ID.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Paylocity](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Paylocity.png)

## APIs

Axonius uses the [Paylocity API](https://prod.cdn.paylocity.com/developer/index.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [Client ID](#parameters) must be associated with credentials that have read permissions in order to fetch assets.
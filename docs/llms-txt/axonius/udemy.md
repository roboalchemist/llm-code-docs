# Source: https://docs.axonius.com/docs/udemy.md

# Udemy

Udemy is an online learning and teaching marketplace.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Udemy server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To view your Client ID and Client Secret, navigate to Udemy and select **Manage** `>` **Settings** `>` **LMS/LXP Integration**.

3. **Account ID** - The Udemy account used for the connection.
   **To view your Account ID**

   1. Navigate to Udemy and select **Manage** `>` **Settings** `>` **API** `>` **API Documentation**.
   2. Scroll down to the **Your API Client and Your Account Id** section to locate your Udemy BusinessAccount ID. Then paste the value in the Axonius **Acount ID** parameter.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Udemy" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Udemy.png" />

## APIs

Axonius uses the [Udemy Business API](https://udemy.app.box.com/s/uwa9onfjh6y3kousfqss72ufdit38iz8).

## Required Permissions

The value supplied in [Client ID](#parameters) must have Read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.7
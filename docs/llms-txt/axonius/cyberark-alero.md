# Source: https://docs.axonius.com/docs/cyberark-alero.md

# CyberArk Alero

CyberArk Alero secures remote access to critical systems for employees and third-party vendors.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the CyberArk Alero server.

2. **Tenant ID** *(required)* - Specify the Tenant ID value.

3. **Service Account JSON** *(required)* - Upload the JSON file. For information on how to create a service account and the JSON file, see [Service accounts](https://docs.cyberark.com/remote-access-standard/Latest/en/Content/WebServices/ServiceAccounts.htm#Createaserviceaccount).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CyberArk%20Alero" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CyberArk%20Alero.png" />

## APIs

Axonius uses the [Remote Access API](https://api.alero.io/swagger-ui/index.html?urls.primaryName=v2-edge).

## Supported From Version

Supported from Axonius version 6.0

<br />

## **Related Enforcement Actions**

* [CyberArk Alero - Create User Invitation](/docs/cyberark-alero-create-user-invitation)
* [CyberArk Alero - Update User Role](/docs/cyberark-alero-update-user-role)
* [CyberArk Alero - Update User Status](/docs/cyberark-alero-update-user-status)
* [CyberArk Alero - Delete User](/docs/delete-cyberark-alero-user)

<br />
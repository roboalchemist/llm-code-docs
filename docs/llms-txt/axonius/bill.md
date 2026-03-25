# Source: https://docs.axonius.com/docs/bill.md

# BILL

BILL is a leading provider of cloud-based software that digitizes and automates back-office financial processes.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* SaaS data (expenses)

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the BILL server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets.

3. **Dev Key** - The developer key used to uniquely identify your developer account in your API requests.

4. **Organization ID** - The organization ID that is linked to your BILL sandbox developer account. The organization ID is a unique alphanumeric value that begins with 008. For more information, refer to <Anchor label="BILL-generated IDs" target="_blank" href="https://developer.bill.com/docs/classification-of-bill-generated-ids">BILL-generated IDs</Anchor>.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Bill" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Bill.png" />

## APIs

Axonius uses the [BILL API](https://developer.bill.com/#).

* [Sign up process](https://developer.bill.com/docs/sign-up-process) - Customers should contact their BILL account manager to sign up and and set up their BILL developer account for the Sandbox and Production environments.
* [Sandbox sign in](https://developer.bill.com/docs/sandbox-sign-in) - Customers can test if the credentials that they created (username, password, org id and dev key) are valid.

## Supported From Version

Supported from Axonius version 6.0
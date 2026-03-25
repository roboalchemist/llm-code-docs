# Source: https://docs.axonius.com/docs/ramp.md

# Ramp

Ramp is a billing platform that provides businesses with tools to manage and optimize their expenses.

### Asset Types Fetched

* Users
* Expenses
* SaaS Applications

## Before You Begin

### APIs

Axonius uses the [Ramp API](https://docs.ramp.com/developer-api/v1/authorization).

### Permissions

The following permissions are required:

* To fetch users: `users:read`
* To fetch receipts (Expenses): `receipts:read` and `transactions:read`

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://api.ramp.com/`)* - The hostname or IP address of the Ramp server.
2. **Client ID** and **Client Secret** - The credentials of a user account that has the [required permissions](/docs/ramp#permissions) to fetch assets.[Learn how to generate Client ID and Client Secret](https://docs.ramp.com/developer-api/v1/guides/getting-started#quickstart-authorize-with-client-credentials).

<Image alt="RampParameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-P2GNU750.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
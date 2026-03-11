# Source: https://docs.axonius.com/docs/knowbe4-password-iq.md

# KnowBe4 PasswordIQ

KnowBe4 PasswordIQ is a solution that offers secure password management and access control.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key

### APIs

Axonius uses the [KnowBe4 PasswordIQ Product API](https://developer.knowbe4.com/graphql/passwordiq/page/GraphQL-Schema).

### Permissions

To retrieve user-level password vulnerability data, the API token must be associated with an account that has sufficient rights to:

* Access the PasswordIQ product
* View user directory and authentication information
* Retrieve vulnerability assessments and password status flags

If the account doesn't have the appropriate RBAC permissions, the GraphQL queries will return partial or no data, or trigger permission errors.

#### Recommended Steps

1. Ensure the account generating the API token has admin or read-level access to PasswordIQ.
2. Verify the API token has access to the relevant GraphQL operations, especially the directoryUser fields and passwordIssues objects.

#### Supported From Version

Supported from Axonius version 6.1.71

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the KnowBe4 server. Use one of the following endpoints, depending on your region:

| Region | Endpoint                                                       |
| ------ | -------------------------------------------------------------- |
| US     | [https://training.knowbe4.com/](https://training.knowbe4.com/) |
| EU     | ttps\://eu.knowbe4.com/                                        |
| CA     | [https://ca.knowbe4.com/](https://ca.knowbe4.com/)             |
| UK     | [https://uk.knowbe4.com/](https://uk.knowbe4.com/)             |
| DE     | [https://de.knowbe4.com/](https://de.knowbe4.com/)             |

2. **API Key**  - An API Key associated with a user account that has the Required Permissions to fetch assets.

![KnowBe4 PasswordIQ.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/KnowBe4%20PasswordIQ.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
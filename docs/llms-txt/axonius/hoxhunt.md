# Source: https://docs.axonius.com/docs/hoxhunt.md

# Hoxhunt

Hoxhunt provides security awareness training for employees based on cognitive automation and risk calculations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: api.hoxhunt.com)* - The hostname or IP address of the Hoxhunt server.

2. **Authorization Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   To generate an API Key, navigate to [Access Tokens](https://admin.hoxhunt.com/account-settings/access-tokens).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Hoxhunt" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Hoxhunt.png" />

## APIs

Axonius uses the [Hoxhunt GraphQL API](https://app.hoxhunt.com/docs/graphql-external/).

## Supported From Version

Supported from Axonius version 4.7
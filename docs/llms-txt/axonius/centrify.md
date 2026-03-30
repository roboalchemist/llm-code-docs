# Source: https://docs.axonius.com/docs/centrify.md

# Centrify Identity Services

Centrify Identity Services manages application access, endpoints, and network infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Centrify Tenant URL** *(required)* - The URL for the tenant (e.g. mycompany.my.centrify.net)

2. **Application ID** *(required)* - The Application ID (Created in [Step 2](https://developer.centrify.com/docs/client-credentials-flow#step-2-configure-the-new-oauth-20-client))

3. **Client Scope** *(required)* - The Scope name (Created in [Step 3](https://developer.centrify.com/docs/client-credentials-flow#step-3-create-scopes))

4. **Client ID** and **Client Secret** *(required)* - Will be used to authorize the Confidential Client (In [Step 4](https://developer.centrify.com/docs/client-credentials-flow#step-4-create-a-confidential-client)).

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(934).png" />

## Creating a Client Application in Centrify

Creating a Confidential Client for Axonius Application in Centrify is required.
Follow the instructions in [Client Credentials Flow](https://developer.centrify.com/docs/client-credentials-flow).

* The Client Application requires the following **Scope** permissions ([Step 3](https://developer.centrify.com/docs/client-credentials-flow#step-3-create-scopes)):
  * CDirectoryService/GetUsers
  * UPRest/GetResultantAppsForUser
  * Redrock/Query

<Callout icon="📘" theme="info">
  NOTE

  * The adapter performs queries using the Redrock/Query REST API endpoint against the following table(s):
    * VaultAccount

  * The query does not retrieve nor store any information about passwords, hashes, etc.
</Callout>

* Axonius requires the account to be an **OAuth Confidential Client** ([Step 4](https://developer.centrify.com/docs/client-credentials-flow#step-4-create-a-confidential-client))
  * Important to enable the **Is OAuth Confidential Client**
* User must be in a role that gives them access to use the APIs that the server is scoped to.

## API

Axonius uses the [Centrify Identity Services API](https://developer.centrify.com/docs/introduction)
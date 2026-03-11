# Source: https://docs.axonius.com/docs/harness.md

# Harness

Harness is a self-service CI/CD platform that allows engineers and DevOps to build, test, deploy, and verify software.

The Harness adapter enables Axonius to fetch and catalog users, providing visibility into their inventory details and access permissions.

## Asset Types Fetched

* Users

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)

### APIs

Axonius uses the <Anchor label="Harness API" target="_blank" href="https://apidocs.harness.io/user">Harness API</Anchor> to retrieve asset data..

### Supported From Version

Supported from Axonius version 6.1.30.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** *(default: `https://app.harness.io`)* - Enter the hostname or IP address of the Harness server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** - Enter the API Key associated with a user account that has permissions to fetch assets.

<Image alt="Harness" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Harness.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

* **Global Endpoints Config** -
  * **Project Identifier** (*optional*) - Enter a specific Project ID to limit the data fetch to a single project.
  * **Search Term** (*optional*) - Enter a keyword to filter the users or entities retrieved based on a specific search query.
  * **Account Identifier** (*optional*) - Enter the specific Account ID to scope the connection to a particular Harness account.
  * **Organization Identifier** (*optional*) - Enter the Organization ID to restrict the fetch to a specific organization within Harness.
* **Endpoints Config** -
  * **Enrich Users with User Details** - Select this option to fetch full attribute details for each user. When enabled, the adapter performs an additional API request per user to retrieve comprehensive information not included in the default list view.
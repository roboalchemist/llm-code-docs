# Source: https://docs.axonius.com/docs/jetbrains.md

# JetBrains Account Management

JetBrains is an integrated development environment (IDE) for software development that provides a suite of tools and features to help developers write, test, and deploy code.

The JetBrains adapter enables Axonius to fetch and catalog licenses and SaaS application data from the JetBrains account portal.

## Asset Types Fetched

* Licenses
* SaaS Applications

## Before You Begin

### Authentication Methods

* API Key (API Token)

### Required Permissions

The connection requires an API key associated with a user account that has the necessary permissions to fetch assets from the JetBrains server.

### APIs

Axonius uses the <Anchor label="JetBrains Account API" target="_blank" href="https://account.jetbrains.com/api-doc">JetBrains Account API</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 6.1

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the JetBrains server.

2. **API Key** - Enter the API key associated with a user account that has permissions to fetch assets.

3. **Customer Code** - Enter the Company Profile ID that can be found on the JetBrains account portal near the company name.

<Image alt="JetBrains" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JetBrains.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
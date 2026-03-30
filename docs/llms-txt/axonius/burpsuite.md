# Source: https://docs.axonius.com/docs/burpsuite.md

# Burp Suite

Burp Suite is a penetration testing and vulnerability finder tool often used for checking web application security.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications, Domains & URLs

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Burp Suite server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Choose whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Burp_Suite" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Burp_Suite.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Include JIRA tickets** - Select this option to include JIRA tickets.
2. **Include false positives** - Select this option to include false positives.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Burp Suite Enterprise Edition GraphQL API](https://portswigger.net/burp/extensibility/enterprise/graphql-api/index.html).

Accessing the API requires creating an API user in the Burp Suite Enterprise Edition. This will generate an API key that you can use to authenticate any requests that you send to the API.

To obtain an API key:

1. Log in to the Burp Suite Enterprise Edition web UI as an administrator.
2. From the **Burger** menu, navigate to the **Team** page.
3. On the **Users** tab, select **New user**.
4. Enter a name and username that will help you subsequently identify the user, such as "GraphQL API User".
5. Enter an email address, such as the email address of the admin user.
6. Select the **API key** login type.
7. Save your changes.
8. When prompted, copy your new API key and save it to a secure location.

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have permissions to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                              | Supported | Notes |
| ------------------------------------ | --------- | ----- |
| Burp Suite Enterprise Edition 2022.1 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5
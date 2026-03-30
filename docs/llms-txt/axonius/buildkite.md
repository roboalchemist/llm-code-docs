# Source: https://docs.axonius.com/docs/buildkite.md

# Buildkite

Buildkite is a continuous integration tool designed to improve software developer productivity.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.buildkite.com`)* - The hostname or IP address of the Buildkite server.

2. **API Access Token** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To create an API Access Token, see [Creating an API Access Token](/docs/buildkite#creating-an-api-access-token).

3. **Organization Slug** *(required)* - Enter the slug created in Buildkite to indentify your organization.
   **To create an Organization Slug**

   1. From Buildkit, navigate to **Settings**.
   2. In the Organization Settings section, fill-in the **Name** and **Slug** fields.
   3. Click **Save Organization Settings**.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Buildkite" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Buildkite.png" />

## APIs

Axonius uses the [Buildkite REST API](https://buildkite.com/docs/apis/rest-api).

## Creating an API Access Token

**To create an API Access Token**

1. From Buildkit, navigate to **API Access Tokens**.

2. In the New API Access Token section, fill-in the **Description** field.

3. Under **Organization Access**, select the checkbox.

4. Under **REST API Scopes**, select **Read Agents**.

5. Under **Accounts**, select one of the following options:
   * **All accounts**
   * **Only some accounts** to limit API access to specific accounts. Then select the checkbox next to the accounts to include.

6. Click **Create New API Access Token**.

## Required Permissions

The value supplied in [API Access Token](#parameters) must be associated with credentials that have Read Agents permissions to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version          | Supported | Notes |
| ---------------- | --------- | ----- |
| Buildkite API v2 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5
# Source: https://docs.axonius.com/docs/atlassian-jira-asset-platform.md

# Atlassian Jira Assets Platform

<Callout icon="❗️" theme="error">
  Notice

  [Jira](https://community.developer.atlassian.com/t/shutdown-notice-update-on-deprecation-of-the-external-assets-platform/81193) has deprecated this solution. Consequently, this adapter is no longer available in Axonius.
</Callout>

Atlassian Jira Assets Platform links software with Jira to populate an asset inventory, letting users query for assets and link them to issues.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Jira Domain** *(required)* - The hostname or IP address of the Atlassian Jira Assets Platform server.

2. **User Name** and **API Token** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. Note: The API Token is not the same as the Admin Key.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Jira Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Jira Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **Jira Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![AtJiraAssetsPlatform](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AtJiraAssetsPlatform.png)

## APIs

Axonius uses the [Atlassian Jira Asset Platform - Get All Assets API](https://developer.atlassian.com/cloud/assetsapi/rest/#api-asset-get).

## Required Permissions

The value supplied in [User Name](#parameters) and in [API Key](#parameters) must have read access to devices.

To integrate Axonius with Jira, you need to do the following :

1. Create a user in your Atlassian site with access to Jira. The user should be part of the most basic group which is jira-software-users.

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(420\).png)

2. Log in to Jira using the created user and generate an API token.
   For cloud based Atlassian sites, use the following URL to generate an API token: [https://id.atlassian.com/manage/api-tokens#](https://id.atlassian.com/manage/api-tokens#)

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(421\).png)
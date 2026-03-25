# Source: https://docs.axonius.com/docs/bitbucket.md

# Bitbucket

Bitbucket is a web-based version control repository hosting service for source code and development projects that use either Mercurial or Git revision control systems.

<Callout icon="📘" theme="info">
  Note

  To use Bitbucket server enter a User Name and Password, to use Bitbucket Cloud enter a Client ID and App Secret.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Groups
* Application Resources
* Permissions

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Bitbucket server. This adapter supports both Bitbucket Cloud and Bitbucket server.

2. **User Name (V1) or Client ID (V2 Bitbucket Cloud)** *(required)* - The user name for the Bitbucket server, or the client ID for the Bitbucket Cloud that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Password (V1) or App Secret (V2 Bitbucket Cloud)** *(required)* - The password for the Bitbucket server, or the App Secret for the Bitbucket Cloud.

4. **Use Bitbucket Cloud API (V2)** - Select this option to use the Bitbucket Cloud instead of the Bitbucket server.

5. **Use OAuth2 to Authenticate** - Select this option to use OAuth2 client credentials to authenticate Bitbucket API V2.

6. **API Rate Limit per Hour** *(optional, default: 1000)* - Specify a rate limit for the number of requests per hour to be sent to Bitbucket.

7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

8. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

9. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

10. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Bitbucket](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Bitbucket.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Fetch maximum commits** *(optional, default: 50)* - Specify the maximum number of commit records Axonius should fetch from all the connections of this adapter.
2. **Max audit log record pages to parse** *(optional, default: 50)* - Specify the maximum number of pages to parse for the users visit log for all connections for this adapter. The maximum value for this parameter is 1000.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Bitbucket Server - REST](https://docs.atlassian.com/bitbucket-server/rest/7.7.0/bitbucket-rest.html#idp150).

Please note that the repository in Bitbucket must have the default branch set. Before setting up the adapter connection, confirm that the default branch is set correctly. To do so refer to this [link](https://confluence.atlassian.com/bitbucketserverkb/nodefaultbranchexception-error-regarding-the-default-branch-this-branch-does-not-exist-779171277.html).

## Required Permissions

The value supplied in [User Name](#parameters) must have PROJECT\_VIEW, REPO\_READ permissions and  READ permission on the Account scope  to fetch assets.
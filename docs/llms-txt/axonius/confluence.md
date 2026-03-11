# Source: https://docs.axonius.com/docs/confluence.md

# Atlassian Confluence

Atlassian Confluence provides information on Confluence entities, like pages and blog posts, spaces, users, groups, and more.

<br />

## Assets Types Fetched

* Users

<br />

## Before You Begin

### Authentication Methods

* **Basic Authentication** using an  API Token.
* **Bearer Token**  - using an API key. Add this method when you want to use the Last Active Dates advanced configuration.

## APIs

Axonius uses the following Confluence APIs:

* [Cloud](https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-search/#api-wiki-rest-api-search-user-get)
* [On-Prem](https://docs.atlassian.com/ConfluenceServer/rest/8.5.0-m04/#api/user-getUsers)
* /admin/v1/orgs/ orgId /directory/users/ accountId /last-active-dates - to get the last active date

### Create an API token

To successfully connect this adapter, you need to complete the following steps:

1. Login to admin.atlassian.com with the created Atlassian account, and generate an API token, using the following URL: `https://id.atlassian.com/manage/api-tokens#`.
2. To generate an API Token, click on **Create API token**
3. Choose a label that is short, memorable, and easy to remember, and click **Create**.
4. Copy the generated **API token**.
5. In Axonius, paste the copied token in the API Token field.

### Creating an API Key

Create the API key to use as the bearer token in addition to the Basic authentication

1. To authenticate for organization-level data, you must generate an API key through the Atlassian Administration portal:
2. Navigate to Admin: Go to [admin.atlassian.com](admin.atlassian.com). If you manage multiple organizations, select the relevant one.
3. Access API Keys: In the left-hand sidebar, select **Settings** > **API keys**.
4. Generate Key: Click Create **API key** at the top right.
5. Configure: Enter a descriptive name and set an expiration date (maximum 1 year from creation).
6. Save Credentials: Once you click Create, you will see your **Organization ID** and your **API key**.

Crucial: Copy and save these immediately. Atlassian does not store the key value, so you cannot view it again once you close the window.

## Required Permissions

The value supplied in [User Name](#parameters) must have:

**Can use (Site Access)**: permissions.

**View User Profiles**: To see specific details about other users, the "View User Profiles" global permission must be enabled for the group the calling user belongs to.

<br />

To use the "User Last Active Dates" endpoint, your API key or OAuth app needs the following scopes:

* read:directories:admin and
* read:organization or read:user:admin

## Supported From Version

Supported from Axonius version 6.1

<br />

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

<br />

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Atlassian Confluence server.

2. **User Name** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. For Cloud deployment, enter your email address; for On-Prem deployment, enter your user name.

3. **API Token** *(required)* - For Cloud deployment, enter an API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.  For information on how to create an API Token, see [APIs](/docs/confluence#create-an-api-token). For On-Prem deployment, enter your password.

4. **Deployment Type** *(required)* - Select which deployment type to use, either Cloud or On-Prem.

<br />

<Image alt="parameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/AtlassianConfluence.png" />

<br />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**  - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**- The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

5. **Bearer Token** - Authenticate with **Bearer Token** and **Organization ID** in addition to basic authentication, when you want to use the 'Last Active Dates' advanced configuration.  Enter the API Key into the Bearer Token field.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

**Endpoints Config**

**Enrich Users with Last Active Dates** - Select this option to add information about the last date the user was active. To use this setting you need to authenticate with Bearer Token and Organization ID.
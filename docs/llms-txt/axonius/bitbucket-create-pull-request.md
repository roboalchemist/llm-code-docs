# Source: https://docs.axonius.com/docs/bitbucket-create-pull-request.md

# Bitbucket - Create Pull Request

**Bitbucket - Create Pull Request** generates a pull request in Bitbucket for:

* Assets returned by the selected query or assets selected on the relevant asset page.

This Enforcement Action works in two steps, as follows:

1. Creates a branch in the repository with the branch name roughly following the pattern: *axonius-`{normalized_asset_name}`-`{axon_id}`*. The normalized asset name is the asset name with only latin alphabet characters, decimal numbers, and underscores. Other characters in the asset name are dropped.

2. Opens a pull request using the previously created branch. The content of the pull request is a message detailing the asset tags.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Bitbucket adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Bitbucket](/docs/bitbucket) adapter connection.
</Callout>

* **Project Key (V1) or Workspace Slug (V2)** - The project key (for Bitbucket Server connections) or the workspace slug (for Bitbucket Cloud connections). Both can be found in the URL of the project/workspace.

* **Repository Slug** - The slug for the repository where the pull request will be opened. This can be found in the URL of the repository.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname or IP address of the Bitbucket server.

  * **Username (V1) or Client ID (V2 Bitbucket Cloud)** - The user name for the Bitbucket server, or the client ID for the Bitbucket Cloud that has the [Required Permissions](#required-permissions) to fetch assets.

  * **Password (V1) or App Secret (V2 Bitbucket Cloud)** - The password for the Bitbucket server, or the App Secret for the Bitbucket Cloud.

  * **Use Bitbucket Cloud API (V2)** - Select this option to use the Bitbucket Cloud instead of the Bitbucket server.

  * **Use OAuth2 to Authenticate** - Select this option to use OAuth2 client credentials to authenticate Bitbucket API V2.

  * **API Rate Limit per Hour** *(default: 1000)* - Specify a rate limit for the number of requests per hour to be sent to Bitbucket.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the following APIs:

* [**The Bitbucket Cloud REST API (V2)**](https://developer.atlassian.com/cloud/bitbucket/rest/)

  * [Create a pull request](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-post) - Creates a new pull request where the destination repository is this repository and the author is the authenticated user.
  * [Create a branch](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-branches-post) - Creates a new branch in the specified repository.
* [**The Bitbucket Data Center REST API (V1)**](https://developer.atlassian.com/server/bitbucket/rest/)
  * [Create pull request](https://developer.atlassian.com/server/bitbucket/rest/v900/api-group-pull-requests/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-post) - Creates a new pull request from a source branch or tag to a target branch. The source and target may be in the same repository, or different ones.
  * [Create branch](https://developer.atlassian.com/server/bitbucket/rest/v900/api-group-repository/#api-branch-utils-latest-projects-projectkey-repos-repositoryslug-branches-post) - Creates a branch in the specified repository.

## Required Permissions

The following permissions are required to perform this Enforcement Action:

* **Bitbucket Cloud REST API (V2)**:
  * repository:write
  * pullrequest:write

* **Bitbucket Server REST API (V1)**:
  * REPO\_WRITE
  * REPO\_READ

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).
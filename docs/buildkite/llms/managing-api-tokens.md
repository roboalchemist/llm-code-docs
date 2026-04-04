# Source: https://buildkite.com/docs/apis/managing-api-tokens.md

# Managing API access tokens

Buildkite API access tokens are issued to individual Buildkite user accounts, not Buildkite organizations.

## Creating and editing API access tokens

You can [create](#creating-and-editing-api-access-tokens-create-an-api-access-token) and [edit](#creating-and-editing-api-access-tokens-edit-an-existing-api-access-token) API access tokens through your **Personal Settings**.

> 📘
> You'll need to be a member of a Buildkite organization to generate and use an API access token with this organization. This is especially important for contributors to public and open-source projects.
> Once API access tokens have been created within a Buildkite organization, Buildkite organization administrators can use the [API Access Audit](#auditing-tokens) page to view and manage all such tokens that have been created within it.

### Create an API access token

To create a new API access token:

1. Select **Personal Settings** in the global navigation > [**API Access Tokens**](https://buildkite.com/user/api-access-tokens) to open its page.
1. Select **New API Access Token**.

    If prompted, enter your password in the **Confirm Password** field.
1. Enter an appropriate **Description** for your new API access token, and ensure **Token** is selected in **Credential Type**.
1. Ensure the appropriate Buildkite organization is selected in **Organization Access**. This organization is the one that your API access token will have access to and operate within.

    **Note:** Your most recently used Buildkite organization is automatically selected from this list.
1. Select an appropriate **Token Expiry** duration.
1. Select from the appropriate **REST API Scopes** or **GraphQL API** permission, or both. Learn more about these in [Token scopes](#token-scopes).
1. To restrict which network addresses your new API access token can operate from, specify these addresses in the **Allowed IP Addresses** field, using [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
1. Select **Create New API Access Token** to create the token, and enter your password again if prompted.

    **Note:** On the resulting page, don't forget to copy your new API access token's value now, as this is the last time you'll see this value.

### Edit an existing API access token

To edit an existing API access token:

1. Select **Personal Settings** in the global navigation > [**API Access Tokens**](https://buildkite.com/user/api-access-tokens) to open its page.
1. Select the API access token to edit from the list of existing ones on this page.
1. Edit the required fields as you would when you [created the API access token](#creating-and-editing-api-access-tokens-create-an-api-access-token), as well as its [token scopes](#token-scopes).
1. Select **Update API Access Token** to save your changes.

## Token scopes

When an [API access token is being created or edited](#creating-and-editing-api-access-tokens), define the required **REST API Scopes**, for which you select permissions (**READ**, **WRITE**, **DELETE**) for different Buildkite platform features that this token is granted access to. Each individual combination of these permissions and features is known as a _scope_.

You can also select **Enable GraphQL API access** as an additional scope, noting that this is a full-access option that does not provide any further granular scopes/permission restrictions to Buildkite platform features. To restrict an API access token's scope to individual GraphQL API features, you can do so by implementing [GraphQL API portals](/docs/apis/graphql/portals).

A token's **REST API Scopes** are organized by Buildkite platform feature categories and their individual features. See the relevant tables within this section for details of these features, along with the permission types (**READ**, **WRITE**, **DELETE**) that each of these features provide.

For REST API scopes, you can use the following:

- The **Search** feature allows you to filter the available Buildkite platform features.
- The **Presets** feature allows you to select between all **Read only**, all **Read + Write**, or all **Full Access** (which includes **DELETE**) permissions across all of these Buildkite platform features, regardless of whether or not these features have been filtered using **Search**.

Token scopes are also available to OAuth access tokens, which are issued by the Buildkite platform on behalf of your Buildkite user account for certain processes. However, when these processes occur, while you can select a Buildkite organization you're a member of, which the OAuth token grants access to, the Buildkite platform defines the scopes for these access tokens.

A token's REST API scopes are granular, and you can select some or all of the following Buildkite platform features and their scopes.

### CI/CD

<table>
  <thead>
    <tr>
      <th style="width:25%">Feature and scopes</th>
      <th style="width:55%">Description</th>
      <th style="width:7%">Read</th>
      <th style="width:7%">Write</th>
      <th style="width:6%">Delete</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td><strong>Pipelines</strong><br><code>read_pipelines</code>, <code>write_pipelines</code></td>
        <td><p>List and retrieve details of pipelines—create, update, and delete pipelines.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

      <tr>
        <td><strong>Builds</strong><br><code>read_builds</code>, <code>write_builds</code></td>
        <td><p>List and retrieve details of builds—create new builds.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

      <tr>
        <td><strong>Build Logs</strong><br><code>read_build_logs</code>, <code>write_build_logs</code></td>
        <td><p>Retrieve build logs—delete build logs.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

      <tr>
        <td><strong>Job Environment</strong><br><code>read_job_env</code></td>
        <td><p>Retrieve job environment variables.</p>
</td>
        <td>✅</td>
        <td></td>
        <td></td>
      </tr>

      <tr>
        <td><strong>Artifacts</strong><br><code>read_artifacts</code>, <code>write_artifacts</code></td>
        <td><p>Retrieve build artifacts—delete build artifacts.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

      <tr>
        <td><strong>Agents</strong><br><code>read_agents</code>, <code>write_agents</code></td>
        <td><p>List and retrieve details of agents—stop agents. To register self-hosted agents, use an <a href="/docs/agent/self-hosted/tokens">agent token</a> instead.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

      <tr>
        <td><strong>Clusters</strong><br><code>read_clusters</code>, <code>write_clusters</code></td>
        <td><p>List and retrieve details of clusters—create, update, and delete clusters.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

      <tr>
        <td><strong>Pipeline Templates</strong><br><code>read_pipeline_templates</code>, <code>write_pipeline_templates</code></td>
        <td><p>List and retrieve details of pipeline templates—create, update, and delete pipeline templates.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

      <tr>
        <td><strong>Rules</strong><br><code>read_rules</code>, <code>write_rules</code></td>
        <td><p>List and retrieve details of rules—create or delete rules.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

  </tbody>
</table>

### Organization and users

<table>
  <thead>
    <tr>
      <th style="width:25%">Feature and scopes</th>
      <th style="width:55%">Description</th>
      <th style="width:7%">Read</th>
      <th style="width:7%">Write</th>
      <th style="width:6%">Delete</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td><strong>Organizations</strong><br><code>read_organizations</code></td>
        <td><p>List and retrieve details of organizations.</p>
</td>
        <td>✅</td>
        <td></td>
        <td></td>
      </tr>

      <tr>
        <td><strong>Teams</strong><br><code>read_teams</code>, <code>write_teams</code></td>
        <td><p>List teams—create, update, and delete teams.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

      <tr>
        <td><strong>User</strong><br><code>read_user</code></td>
        <td><p>Retrieve basic details of the user.</p>
</td>
        <td>✅</td>
        <td></td>
        <td></td>
      </tr>

  </tbody>
</table>

### Security

<table>
  <thead>
    <tr>
      <th style="width:25%">Feature and scopes</th>
      <th style="width:55%">Description</th>
      <th style="width:7%">Read</th>
      <th style="width:7%">Write</th>
      <th style="width:6%">Delete</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td><strong>Secrets</strong><br><code>read_secrets_details</code>, <code>write_secrets</code></td>
        <td><p>List and retrieve details about secrets—create, update, and delete secrets.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

  </tbody>
</table>

### Test Engine

<table>
  <thead>
    <tr>
      <th style="width:25%">Feature and scopes</th>
      <th style="width:55%">Description</th>
      <th style="width:7%">Read</th>
      <th style="width:7%">Write</th>
      <th style="width:6%">Delete</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td><strong>Suites</strong><br><code>read_suites</code>, <code>write_suites</code></td>
        <td><p>Retrieve suite information—create suites.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

      <tr>
        <td><strong>Test Plan</strong><br><code>read_test_plan</code>, <code>write_test_plan</code></td>
        <td><p>Retrieve test plan information—create test plan.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

  </tbody>
</table>

### Packages

<table>
  <thead>
    <tr>
      <th style="width:25%">Feature and scopes</th>
      <th style="width:55%">Description</th>
      <th style="width:7%">Read</th>
      <th style="width:7%">Write</th>
      <th style="width:6%">Delete</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td><strong>Registries</strong><br><code>read_registries</code>, <code>write_registries</code>, <code>delete_registries</code></td>
        <td><p>List and retrieve details of registries—create and update registries; delete registries.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
      </tr>

      <tr>
        <td><strong>Packages</strong><br><code>read_packages</code>, <code>write_packages</code>, <code>delete_packages</code></td>
        <td><p>List and retrieve details of packages—create packages, delete packages.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
      </tr>

  </tbody>
</table>

### Portals

<table>
  <thead>
    <tr>
      <th style="width:25%">Feature and scopes</th>
      <th style="width:55%">Description</th>
      <th style="width:7%">Read</th>
      <th style="width:7%">Write</th>
      <th style="width:6%">Delete</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td><strong>Portals</strong><br><code>read_portals</code>, <code>write_portals</code></td>
        <td><p>List and retrieve details of portals—create, update, and delete portals.</p>
</td>
        <td>✅</td>
        <td>✅</td>
        <td></td>
      </tr>

  </tbody>
</table>

## Auditing tokens

Viewing the [**API Access Audit** page](https://buildkite.com/organizations/~/api-access-audit) requires Buildkite organization administrator privileges. You can access this page by selecting **Settings** in the global navigation > **API Access Audit** within the **Audit** section.

All API access tokens that users within your Buildkite organization have created, and currently have access to your organization's data will be listed. The table includes the scopes of each token, how long ago they were created, and how long since they've been used.

From the **API Access Audit** page, navigate through to any token to see more detailed information about its scopes and the most recent request, where you can also [remove a token's access to your Buildkite organization's data](#auditing-tokens-removing-an-organization-from-a-token) if required.

<div style="max-width: 910px"><div class="responsive-image-container"><img alt="Screenshot of the API Access Audit page displaying a list of all tokens" src="/docs/assets/all-tokens-view-nwvKr7rc.png" /></div></div>

The list of tokens can be filtered by username, scopes, IP address, or whether the user has admin privileges.

 <div style="max-width: 896px"><div class="responsive-image-container"><img alt="Screenshot of the API Access Audit page displaying a filtered list of tokens that have the GraphQL scope" src="/docs/assets/filter-graphql-view-B-kkvVZn.png" /></div></div>

### Removing an organization from a token

If you have old API access tokens that should no longer be used, or need to prevent such a token from performing further actions, Buildkite organization administrators can remove the token's access to organization data.

From the [**API Access Audit** page](#auditing-tokens), find the API token whose access you want to remove and select it. You can search for tokens using usernames, token scopes, full IP addresses, admin privileges, or the value of the token itself.

<div style="max-width: 894px"><div class="responsive-image-container"><img alt="Screenshot of the API access token page with the Revoke Access button at the bottom of the screen" src="/docs/assets/token-view-CeN_cxlh.png" /></div></div>

Scroll to the end of the specific token's page, then select **Remove Organization from Token**.

Removing access from a token sends a notification email to the token's owner, who cannot re-add your organization to the token's scope.

## Limiting API access by IP address

> 📘 Enterprise plan feature
> Limiting API access by IP address is only available to Buildkite customers on the [Enterprise](https://buildkite.com/pricing) plan.

If you'd like to limit an API token's access to your organization by IP address, you can create an allowlist of IP addresses in the [organization's API security settings](https://buildkite.com/organizations/~/security/api).

You can also manage the allowlist with the [`organizationApiIpAllowlistUpdate`](/docs/apis/graphql/schemas/mutation/organizationapiipallowlistupdate) mutation in the GraphQL API.

## Inactive API tokens revocation

> 📘 Enterprise plan feature
> Revoking inactive API tokens automatically is only available to Buildkite customers on the [Enterprise](https://buildkite.com/pricing) plan.

To enable the inactive API access tokens revocation feature, navigate to your [organization's API security settings](https://buildkite.com/organizations/~/security/api) and specify the maximum timeframe for inactive tokens to remain valid.

An _inactive API access token_ refers to one that has not been used within the specified duration. When an API token surpasses the configured setting, Buildkite will automatically revoke the token's access to your organization.

Upon token revocation, Buildkite will notify the owner of their change in access.

## Programmatically managing tokens

The `access-token` REST API endpoint can be used to retrieve or revoke an API access token. See the [REST API access token](/docs/apis/rest-api/access-token) page for further information.

## API token lifecycle

Buildkite's API access tokens have the following lifecycle characteristics:

- API access tokens are issued for users within a Buildkite organization. The tokens are stored in the Buildkite database (linked to the user ID) and by the user for which they're issued.

- The tokens are associated with a specific user and can only be revoked by that user. Buildkite organization administrators can remove a user from an organization, which prevents the user from accessing any organization resources and pipelines, and prevents access using any API access token associated with that user.

## API token security

This section explains risk mitigation strategies which you can implement, and others which are in place, to prevent your Buildkite API access tokens being compromised.

### Rotation

Buildkite's API access tokens have no built-in expiration date. The best practices regarding regular credential rotation recommended by [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html#key-lifetimes-and-rotation) suggest rotating the tokens at least once a year. In case of a security compromise or breach, it is strongly recommended that the old tokens are [invalidated](/docs/apis/managing-api-tokens#auditing-tokens-removing-an-organization-from-a-token) or inactive ones [revoked](#inactive-api-tokens-revocation), and new tokens are issued.

The [API Access Tokens page](https://buildkite.com/user/api-access-tokens) has a _Duplicate_ button that can be used to create a new token with the same permissions as the existing token.

### GitHub secret scanning program

Learn more about this program in [Token security](/docs/platform/security/tokens).

## FAQs

### Can I view an existing token?

No, you can change the scope and description of a token, or revoke it, but you can't view the actual token after creating it

### Can I re-add my organization to a token?

No. If an organization has revoked a token, it cannot be re-added to the token. The token owner would have to create a new token with access to your organization.

### Can I delete a token?

Yes. If you need to delete a token entirely, you can use the [REST API `access-token` endpoint](/docs/apis/rest-api/access-token#revoke-the-current-token). You will need to know the full token value.

If you own the token, you can revoke your token from the [API access token page](https://buildkite.com/user/api-access-tokens) in your Personal Settings.

### What happens if I remove the access for a token that's currently in use?

The token will lose access to the organization data. Any future API requests will no longer successfully authorize.

### Does limiting API access by IP address apply to the remote MCP server?

Yes. Although the [Buildkite remote MCP server](/docs/apis/mcp-server/remote/configuring-ai-tools) makes API calls from Buildkite's infrastructure, these requests are still subject to your organization's IP allowlist for API token access.


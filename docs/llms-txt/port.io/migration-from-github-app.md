# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/migration-from-github-app.md

# Migration from GitHub app

This guide will walk you through the process of migrating from Port's existing GitHub cloud app to the improved GitHub integration powered by [Ocean](https://ocean.port.io/).

Entity ownership transfer

**This migration focuses on transferring entity ownership from the legacy GitHub App to the new GitHub Ocean integration.**<br /><!-- -->This is a recommended step before uninstalling the old app.

Note that:

* Only the integration that created an entity can delete it.
* If you uninstall before transferring ownership, entities created by the old integration will become orphaned and will have to be deleted manually.

## Improvements[â](#improvements "Direct link to Improvements")

The new Ocean-powered GitHub integration comes with several key improvements:

* **More authentication options** - You can now connect the integration using a Personal Access Token (PAT) that you control, giving you more flexibility.
* **Enhanced performance** - Faster resyncs thanks to improved API efficiency, making your data available sooner.
* **Better selectors** - More granular control over what you sync with improved selectors for `pull requests`, `issues`, `dependabot alerts`, `codescanning alerts`, `files`, and `folders`.

### Multi-organization support[â](#multi-organization-support "Direct link to Multi-organization support")

The GitHub integration supports ingesting data from multiple GitHub organizations starting from **version 3.0.0-beta**. Configure one organization using `githubOrganization`, in your environment variables or list multiple organizations in your port mapping under `organizations`:

```
deleteDependentEntities: true
createMissingRelatedEntities: true
enableMergeEntity: true
organizations:
  - org1
  - org2
# ... rest of your mapping (repositoryType, resources, etc.) ...
```

**Precedence:** If `githubOrganization` is set in the environment variables or config and `organizations` are listed in port mapping, the integration syncs only the `githubOrganization` (singleâorg behavior).

### Authentication model[â](#authentication-model "Direct link to Authentication model")

#### Personal access token (PAT)[â](#personal-access-token-pat "Direct link to Personal access token (PAT)")

You can now authenticate with our GitHub integration using a Personal Access Token (PAT) instead of a GitHub App. This gives you more control over the integration's permissions. For more details, see the [installation page](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md).

Classic PAT required for multi-org

For multi-organization support, you must use a **classic Personal Access Token**. Fine-grained PAT tokens do not work with multi-organization configurations.

Below is a sample Helm value for this configuration:

```
integration:
  secrets:
    githubToken: "<GITHUB_PAT>"
```

#### GitHub App[â](#github-app "Direct link to GitHub App")

If you prefer using a GitHub App, you can still authenticate with our Ocean-powered GitHub integration. You will need to create the app yourself, which is a process similar to our existing self-hosted app installation. This process is documented in the [installation guide](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md?auth=custom-github-app) under the Custom GitHub App tab.

Single organization limitation

GitHub App authentication only supports **one organization** at a time. You must specify exactly one organization using `githubOrganization`.

Below is a sample Helm value for this configuration:

```
integration:
  config:
    githubAppId: "<GITHUB_APP_ID>" # app client id also works
    githubOrganization: "my-org" # Required for single organization support regardlass of token type
  secrets:
    githubAppPrivateKey: "<BASE_64_ENCODED_PRIVATEKEY>"
```

### Webhooks[â](#webhooks "Direct link to Webhooks")

The integration now automatically configures webhooks on GitHub to receive live events. To enable this, you must grant your PAT permission to create organization webhooks. Additionally, you need to provide a public URL for the integration. You can do this by setting `liveEvents.baseUrl` when deploying with Helm or ArgoCD, or by setting the `OCEAN__BASE_URL` environment variable when running the integration as a Docker container. For more details, please refer to the [live events documentation](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md#enabling-live-events).

### Deployment[â](#deployment "Direct link to Deployment")

We've expanded our self-hosted installation examples to support deploying on a Kubernetes cluster using Helm or ArgoCD. For more details, please refer to the [deployment documentation](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md#deploy-the-integration).

### Workflow runs[â](#workflow-runs "Direct link to Workflow runs")

We have increased the number of workflow runs ingested for any given workflow in a repository. The new integration now fetches up to 100 of the latest workflow runs, up from the previous limit of 10 per repository.

### Repository type[â](#repository-type "Direct link to Repository type")

You can now specify the type of repositories (`public`, `private`, or `all`) from which to ingest data. All other data kinds that are associated with repositories (like pull requests, issues, etc.) will only be fetched from repositories that match this configuration.

```
repositoryType: "all" # â fetch pull requests from all repositories. can also be "private", "public", etc
resources:
  - kind: pull-request
    selector:
      # ...
```

## Kind mapping changes[â](#kind-mapping-changes "Direct link to Kind mapping changes")

The data blueprints for GitHub have been updated to provide cleaner data structures and improved relationships between different software catalog entities. Understanding these changes is crucial for a smooth migration.

A key change is how we denote custom attributes. We now add a double underscore prefix (e.g., `__repository`) to attributes that Port adds to the raw API response from GitHub. This makes it clear which fields are part of the original data and which are enrichments from the integration.

### Files & GitOps[â](#files--gitops "Direct link to Files & GitOps")

Organization field in file selectors

The `organization` field is optional when `githubOrganization` is set in the environment variables and it is required when not provided there.

**Existing configuration (click to expand)**

```
resources:
  - kind: file
    selector:
      query: "true"
      files:
        # Note that glob patterns are supported, so you can use wildcards to match multiple files
        - path: "**/package.json"
          # The `repos` key can be used to filter the repositories from which the files will be fetched
          repos:
            - "MyRepo" # â changed
    port:
      entity:
        mappings:
          identifier: .file.path # â Changed
          title: .file.name
          blueprint: '"manifest"'
          properties:
            project_name: .file.content.name
            project_version: .file.content.version
            license: .file.content.license
```

**New configuration (click to expand)**

```
resources:
  - kind: file
    selector:
      query: "true"
      files:
        # Note that glob patterns are supported, so you can use wildcards to match multiple files
        - path: "**/package.json"
          organization:
            my-org # Optional if githubOrganization is set; required if not set
            # The `repos` key can be used to filter the repositories and branch where files should be fetched
          repos:
            - name: MyRepo # â  new key:value pairs rather than a string.
              branch: main # â  new optional branch name for each specified repository
            - name: MyOtherRepo
    port:
      entity:
        mappings:
          identifier: .path
          title: .name
          blueprint: '"manifest"'
          properties:
            project_name: .content.name
            project_version: .content.version
            license: .content.license
```

Here are the key changes for file mappings:

1. The `organization` field can be specified per file pattern when no global organization is configured.
2. The `repos` selector is now a list of objects, where each object can specify the repository `name` and an optional `branch`. This provides more granular control over which files are fetched.
3. File attributes are no longer nested under a `file` key. They are now at the top level of the data structure. For example, instead of `.file.path`, you should now use `.path`.
4. The `repo` key has been renamed to `repository` when referencing the repository a file belongs to, for consistency with other data kinds.

### Repository relationships[â](#repository-relationships "Direct link to Repository relationships")

Fetching related data for a repository, like teams and collaborators, is now managed through a unified `include` selector. This replaces the previous method of using separate boolean flags for each data type, offering a more consistent and streamlined approach.

#### Repository and teams[â](#repository-and-teams "Direct link to Repository and teams")

**Existing configuration (click to expand)**

```
resources:
  - kind: repository
    selector:
      query: "true" # JQ boolean query. If evaluated to false - skip syncing the object.
      teams: true # â changed
    port:
      entity:
        mappings:
          identifier: .name
          title: .name
          blueprint: '"githubRepository"'
          properties:
            readme: file://README.md
            url: .html_url
            defaultBranch: .default_branch
          relations:
            githubTeams: "[.teams[].id | tostring]" # â changed
```

**New configuration (click to expand)**

```
resources:
  - kind: repository
    selector:
      query: "true"
      include: ["teams"] # â new
      includedFiles: # â new, replaces file:// prefix
        - README.md
    port:
      entity:
        mappings:
          identifier: .name
          title: .name
          blueprint: '"githubRepository"'
          properties:
            readme: .__includedFiles["README.md"] # â changed, was file://README.md
            url: .html_url
            defaultBranch: .default_branch
          relations:
            githubTeams: "[.__teams[].id | tostring]" # â new
```

#### Repository and collaborators[â](#repository-and-collaborators "Direct link to Repository and collaborators")

**Existing configuration (click to expand)**

```
resources:
  - kind: repository
    selector:
      query: "true"
      collaborators: true # â changed
    port:
      entity:
        mappings:
          identifier: .name
          title: .name
          blueprint: '"githubRepository"'
          properties:
            readme: file://README.md
            url: .html_url
            defaultBranch: .default_branch
          relations:
            collaborators: "[.collaborators[].login]" # â changed
```

**New configuration (click to expand)**

```
resources:
  - kind: repository
    selector:
      query: "true"
      include: ["collaborators"] # â new
      includedFiles: # â new, replaces file:// prefix
        - README.md
    port:
      entity:
        mappings:
          identifier: .name
          title: .name
          blueprint: '"githubRepository"'
          properties:
            readme: .__includedFiles["README.md"] # â changed, was file://README.md
            url: .html_url
            defaultBranch: .default_branch
          relations:
            collaborators: "[.__collaborators[].login]" # â new
```

### Issues[â](#issues "Direct link to Issues")

We've introduced a new `state` selector. This allows you to filter which objects are ingested based on their state (e.g., `open`, `closed`).

**Existing configuration (click to expand)**

```
resources:
  - kind: issue
    selector:
      query: ".pull_request == null" # JQ boolean query. If evaluated to false - skip syncing the object.
    port:
      entity:
        mappings:
          identifier: ".repo + (.id|tostring)"
          title: ".title"
          blueprint: '"githubIssue"'
          properties:
            creator: ".user.login"
            assignees: "[.assignees[].login]"
            labels: "[.labels[].name]"
            status: ".state"
            createdAt: ".created_at"
          relations:
            repository: ".repo" # â  changed
```

**New configuration (click to expand)**

```
resources:
  - kind: issue
    selector:
      query: ".pull_request == null" # JQ boolean query. If evaluated to false - skip syncing the object.
      state: "closed" # â  new
    port:
      entity:
        mappings:
          identifier: ".__repository + (.id|tostring)"
          title: ".title"
          blueprint: '"githubIssue"'
          properties:
            creator: ".user.login"
            assignees: "[.assignees[].login]"
            labels: "[.labels[].name]"
            status: ".state"
            createdAt: ".created_at"
            closedAt: ".closed_at"
            updatedAt: ".updated_at"
            description: ".body"
            issueNumber: ".number"
            link: ".html_url"
          relations:
            repository: ".__repository" # â  new, uses leading underscore to indicate custom enrichment.
```

### Pull requests[â](#pull-requests "Direct link to Pull requests")

We've introduced new selectors to give you more control over which pull requests are ingested. The `states` selector allows you to filter pull requests by their state (e.g., `open`, `closed`). Additionally, you can use `maxResults` to limit the number of closed pull requests fetched and `since` to fetch pull requests created within a specific time period (in days).

**Existing configuration (click to expand)**

```
resources:
  - kind: pull-request
    selector:
      query: "true" # JQ boolean query. If evaluated to false - skip syncing the object.
    port:
      entity:
        mappings:
          identifier: ".head.repo.name + (.id|tostring)" # The Entity identifier will be the repository name + the pull request ID.
          title: ".title"
          blueprint: '"githubPullRequest"'
          properties:
            creator: ".user.login"
            assignees: "[.assignees[].login]"
            reviewers: "[.requested_reviewers[].login]"
            status: ".status" # merged, closed, opened
            closedAt: ".closed_at"
            updatedAt: ".updated_at"
            mergedAt: ".merged_at"
            createdAt: ".created_at"
          relations:
            repository: .head.repo.name
```

**New configuration (click to expand)**

```
resources:
  - kind: pull-request
    selector:
      query: "true" # JQ boolean query. If evaluated to false - skip syncing the object.
      states: ["open"] # â new
      maxResults: 50 # â new, limit closed PRs to 50 capped at 300
      since: 60 # â new, fetch closed PRs within 60 days capped at 90 days
    port:
      entity:
        mappings:
          identifier: ".head.repo.name + (.id|tostring)" # The Entity identifier will be the repository name + the pull request ID.
          title: ".title"
          blueprint: '"githubPullRequest"'
          properties:
            creator: ".user.login"
            assignees: "[.assignees[].login]"
            reviewers: "[.requested_reviewers[].login]"
            status: ".state" # merged, closed, opened
            closedAt: ".closed_at"
            updatedAt: ".updated_at"
            mergedAt: ".merged_at"
            createdAt: ".created_at"
            prNumber: ".id"
          relations:
            repository: .__repository #  â new, it is now obvious when an attribute is added to the raw API response by the integration.
```

### Folders[â](#folders "Direct link to Folders")

Organization field in folder selectors

The `organization` field is optional when `githubOrganization` is set in the environment variables and is required when not provided (e.g., Classic PAT with multiple organizations defined in your port mapping).

For the `folder` kind, the `folder.name` attribute is no longer part of the response. Instead, you can easily derive the folder name from the `folder.path` using a JQ expression, as shown in the example below:

**Existing configuration (click to expand)**

```
resources:
  - kind: folder
    selector:
      query: "true"
      folders:
        - path: apps/*
          repos:
            - backend-service # â  changed
    port:
      entity:
        mappings:
          identifier: ".folder.name" # â  changed
          title: ".folder.name" # â  changed
          blueprint: '"githubRepository"'
          properties:
            url: .repo.html_url + "/tree/" + .repo.default_branch  + "/" + .folder.path # â  changed
            readme: file://README.md
```

**New configuration (click to expand)**

```
resources:
  - kind: folder
    selector:
      query: "true"
      folders:
        - path: apps/*
          organization: my-org # Optional if githubOrganization is set; required if not set
          repos:
            - name: backend-service # â  new, now has a 'name' key
              branch: main # â  new, optional branch name
      includedFiles: # â  new, replaces file:// prefix
        - README.md
    port:
      entity:
        mappings:
          identifier: .folder.path | split('/') | last # â  new, derived using JQ
          title: .folder.path | split('/') | last
          blueprint: '"githubRepository"'
          properties:
            url: .__repository.html_url + "/tree/" + .__repository.default_branch  + "/" + .folder.path # â  new, repository is a custom enrichment
            readme: .__includedFiles["README.md"] # â  changed, was file://README.md
```

### Teams[â](#teams "Direct link to Teams")

To improve performance when fetching team members, we now use GitHub's GraphQL API instead of the REST API.

This change has two main consequences:

1. The team ID you see may differ depending on whether you are fetching team members. This is due to differences between GitHub's REST and GraphQL APIs.
2. Team members are now located in a `nodes` subarray within the team object.

Team IDs in REST and GraphQL

The `members` selector defaults to `true` when omitted.

When `members: true`, the integration fetches teams using the GitHub GraphQL API.

* In GraphQL, `id` is a global node ID (string).
* In GraphQL, `databaseId` is the numeric ID that matches the team `id` returned by the GitHub REST API.

If you need the numeric team ID (for example, to match an existing REST-based identifier), use `databaseId` in your mappings.

**Existing configuration (click to expand)**

```
- kind: team
  selector:
    query: "true"
    members: true # â  unchanged
  port:
    entity:
      mappings:
        identifier: .id | tostring
        title: .name
        blueprint: '"githubTeam"'
        properties:
          slug: .slug
          description: .description
          link: .url
        relations:
          members: "[.members[].login]" # â  changed
```

**New configuration (click to expand)**

```
- kind: team
  selector:
    query: "true"
    members: true # â  unchanged
  port:
    entity:
      mappings:
        identifier: .databaseId | tostring
        title: .name
        blueprint: '"githubTeam"'
        properties:
          slug: .slug
          description: .description
          link: .url
        relations:
          members: "[.members.nodes[].login]" # â  new, nodes subarray
```

## Other changes[â](#other-changes "Direct link to Other changes")

### `dependabot-alert`[â](#dependabot-alert "Direct link to dependabot-alert")

The `dependabot-alert` kind now supports a `states` selector. This allows you to specify an array of states (e.g., `open`, `fixed`) to control which alerts are ingested:

```
resources:
  - kind: dependabot-alert
    selector:
      query: "true"
      states: # â  new
        - "open"
        - "fixed"
```

### `code-scanning-alerts`[â](#code-scanning-alerts "Direct link to code-scanning-alerts")

The `code-scanning-alerts` kind now supports a `state` selector. This allows you to specify a single state (e.g., `open`) to control which alerts are ingested:

```
resources:
  - kind: code-scanning-alerts
    selector:
      query: "true"
      state: open # â  new
```

### `secret-scanning-alerts`[â](#secret-scanning-alerts "Direct link to secret-scanning-alerts")

The `secret-scanning-alerts` kind is now available in Ocean GitHub. You can filter by a single `state` (e.g., `open`) and control whether the secret content is included using the `hideSecret` option (defaults to `true`, which hides the secret):

```
resources:
  - kind: secret-scanning-alerts
    selector:
      query: "true"
      state: open # ["open", "resolved", "all"]
      hideSecret: true # (default: true)
```

## Summary of key changes[â](#summary-of-key-changes "Direct link to Summary of key changes")

This section provides a high-level summary of the key changes for mappings.

| Area                         | Old Value                            | New Value                                      | Notes                                                                                                                                                                                                                                                                                                         |
| ---------------------------- | ------------------------------------ | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Multi-Organization**       | N/A                                  | `githubOrganization` is not optional           | **Classic PAT supports multiple orgs using the `organization` parameter in port mapping, GitHub App and Fine-grained PAT do not support multi organization and there required the `githubOrganization` configuration**. Syncing multiple organizations increases API calls and may slow down the integration. |
| **File Organization**        | N/A                                  | `organization: "my-org"`                       | Optional if `githubOrganization` is set, required when not (e.g., Classic PAT multi-org).                                                                                                                                                                                                                     |
| **Folder Organization**      | N/A                                  | `organization: "my-org"`                       | Optional if `githubOrganization` is set, required when not set(e.g., Classic PAT multi-org).                                                                                                                                                                                                                  |
| **Authentication**           | GitHub App Installation              | PAT or Self-Created GitHub App                 | The integration can be authenticated using a Personal Access Token (PAT) or a self-created GitHub App. **Multi-org requires classic PAT**.                                                                                                                                                                    |
| **Webhooks**                 | App Webhook                          | Automatic Setup by Integration                 | The integration now manages its own webhooks for live events. This requires `webhook` permissions and `liveEvents.baseUrl` to be set.                                                                                                                                                                         |
| **Workflow Runs**            | 10 per repository                    | 100 per workflow                               | The number of ingested workflow runs has been increased.                                                                                                                                                                                                                                                      |
| **Repository Type**          | N/A                                  | `repositoryType` configuration                 | A new top-level configuration is available to filter repositories by type (`public`, `private`, or `all`).                                                                                                                                                                                                    |
| **Repository Relationships** | `teams: true`, `collaborators: true` | `include: "teams"`, `include: "collaborators"` | The `include` selector replaces boolean flags for fetching related data. The fetched data is also now prefixed with `__` (e.g., `.__teams`).                                                                                                                                                                  |
| **Pull Requests**            | N/A                                  | `states`, `maxResults`, `since` selectors      | New selectors are available for more granular filtering.                                                                                                                                                                                                                                                      |
| **File** properties          | `.file.path`                         | `.path`                                        | All file properties are now at the top level of the object, no longer nested under `.file`.                                                                                                                                                                                                                   |
| **Repository** reference     | `.repo` or `.head.repo.name`         | `.__repository`                                | The integration now consistently provides repository information under the `__repository` field for all relevant kinds.                                                                                                                                                                                       |
| **Folder** name              | `.folder.name`                       | `.folder.path \| split('/') \| last`           | The folder name is no longer directly available and should be derived from the folder path using a JQ expression.                                                                                                                                                                                             |

## Step-by-step migration plan[â](#step-by-step-migration-plan "Direct link to Step-by-step migration plan")

This section provides the practical steps to migrate your entities and transfer ownership to the new GitHub Ocean integration.

### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

#### Get your installation IDs[â](#get-your-installation-ids "Direct link to Get your installation IDs")

Before migrating, you need to identify both installation IDs:

**For the legacy GitHub App installation ID:**

1. Navigate to GitHub App installations:

   * **Personal installations**: `https://github.com/settings/installations`
   * **Organization installations**: `https://github.com/organizations/YOUR-ORG/settings/installations`

2. Click on Port's GitHub App installation from the list.

3. Look at the **URL in your browser address bar** â it contains the installation ID at the end.

**Visual guide:**

![GitHub App installation ID in the URL bar](/img/build-your-software-catalog/sync-data-to-catalog/github/githubAppInstallationId.png)

The installation ID is the numeric value circled in the URL bar (e.g., `97269548` in the example above).

**For the new GitHub Ocean integration:**

* The installation ID is the **name you gave to the new GitHub Ocean integration** when you created it.

#### Install the migrator tool[â](#install-the-migrator-tool "Direct link to Install the migrator tool")

```
curl -sL https://raw.githubusercontent.com/port-labs/port-github-migrator/main/install.sh | bash
```

Gather your Port API credentials:

* Port API client ID.
* Port API client secret.
* Your Port instance URL.

For detailed command reference and usage examples, refer to the [port-github-migrator GitHub repository](https://github.com/port-labs/port-github-migrator#commands-reference). The repository contains complete documentation for all available commands.

### Set up the new integration[â](#set-up-the-new-integration "Direct link to Set up the new integration")

Follow the [installation guide](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md).

**Disable "Create default resources" when migrating** When installing the new GitHub Ocean integration while migrating from the old GitHub app, **you must disable the "Create default resources" toggle** in the **Advanced Configuration** section. If you leave this toggle enabled, the integration will create new default blueprints and mappings that may conflict with your existing data, causing disruptions to your catalog.

![Create default resources toggle disabled in the Advanced Configuration](/img/integrations/github-ocean/HostedByPortCreateDefaultResourcesOff.png)

By disabling this toggle, the integration will start up with empty mapping which ensures that that the integration won't disrupt existing entities.

### Migrate each blueprint (entity ownership transfer)[â](#migrate-each-blueprint-entity-ownership-transfer "Direct link to Migrate each blueprint (entity ownership transfer)")

**This is where you transfer ownership of entities from the old app to the new one.**

For each blueprint, repeat these steps:

**Step 1:** Create temporary blueprint

* Duplicate your existing blueprint and rename to `<blueprint>-ocean-temp` (choose whatever name you want).

**Step 2:** Map the new integration to the temporary blueprint

```
resources:
  - kind: repository
    port:
      entity:
        mappings:
          blueprint: '"githubRepository-ocean-temp"' # Use temp blueprint
          # ... rest of config ...
```

**Step 3:** Compare entities

```
port-github-migrator get-diff githubRepository githubRepository-ocean-temp \
  --client-id <your-client-id> \
  --client-secret <your-client-secret> \
  --old-installation-id <legacy-id> \
  --new-installation-id <ocean-id> \
  --port-url https://api.port.io # use https://api.us.port.io if you are using the US region
```

**Step 4:** Adjust mappings if needed

* Review the [Kind mapping changes](#kind-mapping-changes) section and update your configuration if there are differences.

**Step 5:** Transfer ownership (critical step)

```
port-github-migrator migrate githubRepository \
  --client-id <your-client-id> \
  --client-secret <your-client-secret> \
  --old-installation-id <legacy-id> \
  --new-installation-id <ocean-id> \
  --port-url https://api.port.io # use https://api.us.port.io if you are using the US region
```

**This command transfers ownership of all entities in the blueprint from the old app to the new integration.**

**Step 6:** Update mapping and clean up

* Point the new integration back to the original blueprint.
* Delete the temporary blueprint.

**Step 7:** Repeat for each remaining blueprint

### Update action backend types[â](#update-action-backend-types "Direct link to Update action backend types")

If you have self-service actions or automations that use the legacy GitHub App backend, you must update them to use the new GitHub Ocean backend before uninstalling the old integration.

For each action that uses GitHub workflows:

1. Navigate to the action's configuration in Port.
2. Update the backend type from the legacy GitHub App backend to `GitHub Ocean`.
3. Set the `installationId` field to the name of your GitHub Ocean integration installation.
4. Configure the organization, repository, and workflow details as needed.

For detailed configuration instructions, refer to the [GitHub Ocean backend documentation](/actions-and-automations/setup-backend/github-ocean/.md).

### Finalize and uninstall[â](#finalize-and-uninstall "Direct link to Finalize and uninstall")

Only uninstall the legacy GitHub App **after:**

* â All blueprints are migrated.
* â Ownership is transferred for each blueprint (using the `migrate` command).
* â The new integration is syncing correctly.
* â All actions are migrated to use the GitHub Ocean backend.

### Best practices[â](#best-practices "Direct link to Best practices")

* **Start with non-critical blueprints** â Build confidence before migrating critical data.
* **One blueprint at a time** â Easier to debug if issues arise.
* **Use `get-diff` before migrating** â Verify entities match before transferring ownership.
* **Keep legacy app active** â Don't remove until all migrations complete. Removing it early will leave orphaned entities that can only be deleted manually.
* **Check Port logs** â Monitor for any sync issues after migration.
* **Ownership is reversible** â If issues arise, you can revert by deleting the migrated entities and resyncing the old integration. This will recreate those entities under the old integration ownership.

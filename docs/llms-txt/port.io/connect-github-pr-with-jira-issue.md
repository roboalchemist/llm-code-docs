# Source: https://docs.port.io/guides/all/connect-github-pr-with-jira-issue.md

# Connect GitHub Pull Request with Jira Issue

## Overview[â](#overview "Direct link to Overview")

This guide aims to cover how to connect a GitHub pull request with a Jira Issue to understand the scan results of your pull request.

Available Github Integrations

This guide includes one or more steps that require integration with GitHub.<br /><!-- -->Port supports two GitHub integrations:

* **GitHub (Legacy)** - uses a GitHub app, which is soon to be deprecated.
* **GitHub (Ocean)** - uses the [Ocean framework](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md), recommended for new integrations.

Both integration options are present in this guide via tabs, choose the one that fits your needs.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* This guide assumes you have a Port account and that you have finished the [onboarding process](/getting-started/overview.md).
* Install Port's [Jira integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira/).

- GitHub (Legacy)
- GitHub (Ocean)

* Install Port's [GitHub app](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github/#setup).

- Install [GitHub ocean](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md).

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

* GitHub (Legacy)
* GitHub (Ocean)

We highly recommend you install both the GitHub app and Jira integration to have pull requests and issues automatically ingested into Port in real-time. However, if you haven't installed [Port's GitHub app](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github/) and [Jira integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira/), you'll need to create blueprints for GitHub pull requests and Jira issues in Port. Skip this section if you have already installed the GitHub app and Jira integration.

### Add the pull request blueprint[â](#add-the-pull-request-blueprint "Direct link to Add the pull request blueprint")

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add this JSON schema:

   **GitHub Pull Request Blueprint (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "githubPullRequest",
       "title": "Pull Request",
       "icon": "Github",
       "schema": {
           "properties": {
               "creator": {
                   "title": "Creator",
                   "type": "string"
               },
               "assignees": {
                   "title": "Assignees",
                   "type": "array"
               },
               "reviewers": {
                   "title": "Reviewers",
                   "type": "array"
               },
               "status": {
                   "title": "Status",
                   "type": "string",
                   "enum": [
                       "merged",
                       "open",
                       "closed"
                   ],
                   "enumColors": {
                       "merged": "purple",
                       "open": "green",
                       "closed": "red"
                   }
               },
               "closedAt": {
                   "title": "Closed At",
                   "type": "string",
                   "format": "date-time"
               },
               "updatedAt": {
                   "title": "Updated At",
                   "type": "string",
                   "format": "date-time"
               },
               "mergedAt": {
                   "title": "Merged At",
                   "type": "string",
                   "format": "date-time"
               },
               "link": {
                   "type": "string",
                   "format": "url"
               }
           },
           "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "aggregationProperties": {},
       "relations": {}
   }
   ```

5. Click `Save` to create the blueprint.

### Add pull request mapping config[â](#add-pull-request-mapping-config "Direct link to Add pull request mapping config")

1. Go to your [data sources page](https://app.getport.io/settings/data-sources), and select the Github data source:

   ![](/img/guides/githubIntegration.png)

2. Add the following YAML block into the editor to map the pull request data:

   **Relation mapping (Click to expand)**

   ```
   resources:
       - kind: pull-request
         selector:
             query: "true"
         port:
             entity:
             mappings:
             identifier: ".head.repo.name + '-' + (.number|tostring)" # The Entity identifier will be the repository name + the pull request number
             title: ".title"
             blueprint: '"githubPullRequest"'
             properties:
                 creator: ".user.login"
                 assignees: "[.assignees[].login]"
                 reviewers: "[.requested_reviewers[].login]"
                 status: ".status"
                 closedAt: ".closed_at"
                 updatedAt: ".updated_at"
                 mergedAt: ".merged_at"
                 prNumber: ".id"
                 link: ".html_url"
   ```

3. Click `Save & Resync` to apply the mapping.

Great! Now that the mapping is configured, you will need to manually ingest your pull requests data into Port

We highly recommend you install both GitHub ocean and Jira integration to have pull requests and issues automatically ingested into Port in real-time. However, if you haven't installed [GitHub ocean](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md) and [Jira integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira/), you'll need to create blueprints for GitHub pull requests and Jira issues in Port. Skip this section if you have already installed GitHub ocean and Jira integration.

### Add the pull request blueprint[â](#add-the-pull-request-blueprint-1 "Direct link to Add the pull request blueprint")

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add this JSON schema:

   **GitHub Pull Request Blueprint (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "githubPullRequest",
       "title": "Pull Request",
       "icon": "Github",
       "schema": {
           "properties": {
               "creator": {
                   "title": "Creator",
                   "type": "string"
               },
               "assignees": {
                   "title": "Assignees",
                   "type": "array"
               },
               "reviewers": {
                   "title": "Reviewers",
                   "type": "array"
               },
               "status": {
                   "title": "Status",
                   "type": "string",
                   "enum": [
                       "merged",
                       "open",
                       "closed"
                   ],
                   "enumColors": {
                       "merged": "purple",
                       "open": "green",
                       "closed": "red"
                   }
               },
               "closedAt": {
                   "title": "Closed At",
                   "type": "string",
                   "format": "date-time"
               },
               "updatedAt": {
                   "title": "Updated At",
                   "type": "string",
                   "format": "date-time"
               },
               "mergedAt": {
                   "title": "Merged At",
                   "type": "string",
                   "format": "date-time"
               },
               "link": {
                   "type": "string",
                   "format": "url"
               }
           },
           "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "aggregationProperties": {},
       "relations": {}
   }
   ```

5. Click `Save` to create the blueprint.

### Add pull request mapping config[â](#add-pull-request-mapping-config-1 "Direct link to Add pull request mapping config")

1. Go to your [data sources page](https://app.getport.io/settings/data-sources), and click on your GitHub ocean integration.

   ![](/img/guides/githubOceanIntegration.png)

2. Add the following YAML block into the editor to map the pull request data:

   **Relation mapping (Click to expand)**

   ```
   resources:
     - kind: pull-request
       selector:
         query: "true"
       port:
         entity:
           mappings:
             identifier: .head.repo.name + '-' + (.number|tostring)
             title: .title
             blueprint: '"githubPullRequest"'
             properties:
               creator: .user.login
               assignees: "[.assignees[].login]"
               reviewers: "[.requested_reviewers[].login]"
               status: .state
               closedAt: .closed_at
               updatedAt: .updated_at
               mergedAt: .merged_at
               prNumber: .number
               link: .html_url
   ```

3. Click `Save & Resync` to apply the mapping.

Great! Now that the mapping is configured, you will need to manually ingest your pull requests data into Port

### Add Jira issue blueprint[â](#add-jira-issue-blueprint "Direct link to Add Jira issue blueprint")

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add this JSON schema:

   **Jira Issue Blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "jiraIssue",
     "title": "Jira Issue",
     "icon": "Jira",
     "schema": {
       "properties": {
         "url": {
           "title": "Issue URL",
           "type": "string",
           "format": "url",
           "description": "URL to the issue in Jira"
         },
         "status": {
           "title": "Status",
           "type": "string",
           "description": "The status of the issue"
         },
         "issueType": {
           "title": "Type",
           "type": "string",
           "description": "The type of the issue"
         },
         "components": {
           "title": "Components",
           "type": "array",
           "description": "The components related to this issue"
         },
         "assignee": {
           "title": "Assignee",
           "type": "string",
           "format": "user",
           "description": "The user assigned to the issue"
         },
         "reporter": {
           "title": "Reporter",
           "type": "string",
           "description": "The user that reported to the issue",
           "format": "user"
         },
         "creator": {
           "title": "Creator",
           "type": "string",
           "description": "The user that created to the issue",
           "format": "user"
         },
         "priority": {
           "title": "Priority",
           "type": "string",
           "description": "The priority of the issue"
         },
         "created": {
           "title": "Created At",
           "type": "string",
           "description": "The created datetime of the issue",
           "format": "date-time"
         },
         "updated": {
           "title": "Updated At",
           "type": "string",
           "description": "The updated datetime of the issue",
           "format": "date-time"
         }
       }
     },
     "calculationProperties": {},
     "mirrorProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

5. Click `Save` to create the blueprint.

### Add Jira mapping config[â](#add-jira-mapping-config "Direct link to Add Jira mapping config")

1. Go to your [data sources page](https://app.getport.io/settings/data-sources), and click on your Jira integration.

2. Under the `resources` key, add the following YAML block to map Jira issues:

   **Jira Issue mapping (Click to expand)**

   ```
   resources:
     - kind: issue
       selector:
         query: "true"
       port:
         entity:
           mappings:
             identifier: .key
             title: .fields.summary
             blueprint: '"jiraIssue"'
             properties:
               url: .self
               status: .fields.status.name
               issueType: .fields.issuetype.name
               components: "[.fields.components[].name]"
               assignee: .fields.assignee.emailAddress
               reporter: .fields.reporter.emailAddress
               creator: .fields.creator.emailAddress
               priority: .fields.priority.name
               created: .fields.created
               updated: .fields.updated
   ```

3. Click `Save & Resync` to apply the mapping.

Great! Now that the mapping is configured, you will need to manually ingest your Jira issues data into Port

## Relate pull requests to Jira issues[â](#relate-pull-requests-to-jira-issues "Direct link to Relate pull requests to Jira issues")

Now that Port is synced with our Jira resources, let's map the Jira issues to the Github pull requests.

First, we will need to create a [relation](/build-your-software-catalog/customize-integrations/configure-data-model/relate-blueprints/.md) between our `githubPullRequest` and the corresponding `jiraIssue`.

1. Head back to the [Builder](https://app.getport.io/settings/data-model), choose the `Pull Request` [blueprint](), and click on `New relation`:

   ![](/img/guides/githubPRNewJiraIssueRelation.png)

   <br />

   <br />

2. Fill out the form like this, then click `Create`:

   ![](/img/guides/githubPRCreateNewRelation.png)

   <br />

   <br />

Now that the [blueprints]() are related, we need to assign the relevant Jira Issue to each of our pull requests.<br /><!-- -->This can be done by adding some mapping logic, using one of the following methods:

* Direct identifier mapping
* Search query

The most straightforward way to set a relation's value is to explicitly specify the related entity's identifier.<br /><!-- -->Follow the steps below to map pull request entities with Jira issues using direct identifier mapping:

1. Go to your [data sources page](https://app.getport.io/settings/data-sources)

2. Click on your Github integration:

* GitHub (Legacy)
* GitHub (Ocean)

![](/img/guides/githubIntegrationWithBlueprints.png)

<br />

<br />

3. Under the `resources` key, find the Pull Request block

4. Replace it with the following YAML configuration to map pull request entities with Jira issues:

   **Relation mapping (click to expand)**

   ```
       - kind: pull-request
       selector:
           query: "true"
       port:
           entity:
           mappings:
           identifier: .head.repo.name + (.id|tostring)
           title: .title
           blueprint: '"githubPullRequest"'
           properties:
             creator: .user.login
             assignees: "[.assignees[].login]"
             reviewers: "[.requested_reviewers[].login]"
             status: .status
             closedAt: .closed_at
             updatedAt: .updated_at
             mergedAt: .merged_at
             prNumber: .id
             link: .html_url
           relations:
             repository: .head.repo.name
             jiraIssue: .title | match("^[A-Za-z]+-[0-9]+") .string
   ```

5. Click `Save & Resync` to apply the changes

![](/img/guides/githubOceanIntegrationWithBlueprints.png)

<br />

<br />

3. Under the `resources` key, find the Pull Request block

4. Replace it with the following YAML configuration to map pull request entities with Jira issues:

   **Relation mapping (click to expand)**

   ```
       - kind: pull-request
       selector:
           query: "true"
       port:
           entity:
           mappings:
           identifier: .head.repo.name + (.id|tostring)
           title: .title
           blueprint: '"githubPullRequest"'
           properties:
             creator: .user.login
             assignees: "[.assignees[].login]"
             reviewers: "[.requested_reviewers[].login]"
             status: .state
             closedAt: .closed_at
             updatedAt: .updated_at
             mergedAt: .merged_at
             prNumber: .number
             link: .html_url
           relations:
             repository: .__repository
             jiraIssue: .title | match("^[A-Za-z]+-[0-9]+") .string
   ```

5. Click `Save & Resync` to apply the changes

Mapping explanation

The configuration mapping above ingests all pull requests from Github. It then goes ahead to establish a relation between the `githubPullRequest` entities and the `jiraIssue` entities Â ð.

Please note that the `.head.repo.name` property refers to the name of the repository while the `.id` property refers to the ID of the pull request itself. In our GitHub integration mapping, we have defined these two pieces of information as the identifiers for the `githubPullRequest` entities.

For the `jiraIssue` relation, we extract the Jira Issue key from the title of the pull request. Therefore, only pull requests containing the key of the Jira issue will be mapped to their respective Jira issues. Below are few examples and corresponding output:

| Pull request title                          | Jira issue  |
| ------------------------------------------- | ----------- |
| PORT-4837 \| This is the evening of the day | PORT-4837   |
| GET-14 - This is the evening of the day     | GET-14      |
| This is the evening of the day              | (no output) |

You can also use a [search query](https://docs.port.io/build-your-software-catalog/customize-integrations/configure-mapping#mapping-relations-using-search-queries) to match PRs with Jira issues based on multiple criteria.

This approach is particularly useful when you don't know the entity's identifier, but you do know the value of one of its properties.

Follow the steps below to match PRs with Jira issues based on multiple criteria (title, description, branch name). You can customize these matching rules based on your team's conventions and requirements.

1. Go to your [data sources page](https://app.getport.io/settings/data-sources)

2. Click on your Github integration

   ![](/img/guides/githubIntegrationWithBlueprints.png)

   <br />

   <br />

* GitHub (Legacy)
* GitHub (Ocean)

3. Under the `resources` key, locate the Pull Request block

4. Replace it with the following YAML block to map the pull request entities with Jira issues using search queries:

   **Search query mapping (click to expand)**

   ```
     - kind: pull-request
       selector:
         query: "true"
       port:
         entity:
           mappings:
             identifier: .head.repo.name + (.id|tostring)
             title: .title
             blueprint: '"githubPullRequest"'
             properties:
               creator: .user.login
               assignees: "[.assignees[].login]"
               reviewers: "[.requested_reviewers[].login]"
               status: .status
               closedAt: .closed_at
               updatedAt: .updated_at
               mergedAt: .merged_at
               prNumber: .id
               link: .html_url
             relations:
               jiraIssue:
                 combinator: '"or"'
                 rules:
                   # Match Jira issue key in PR title
                   - property: '"$identifier"'
                     operator: '"="'
                     value: (.title // "") | match("^[A-Za-z]+-[0-9]+") .string

                   # Match Jira issue key in PR description
                   - property: '"$identifier"'
                     operator: '"="'
                     value: (.body // "") | match("[A-Za-z]+-[0-9]+") .string
                   
                   # Match Jira issue key in PR branch name
                   - property: '"$identifier"'
                     operator: '"="'
                     value: (.head.ref // "") | match("[A-Za-z]+-[0-9]+") .string
   ```

5. Click `Save & Resync` to apply the changes

3) Under the `resources` key, locate the Pull Request block

4) Replace it with the following YAML block to map the pull request entities with Jira issues using search queries:

   **Search query mapping (click to expand)**

   ```
     - kind: pull-request
       selector:
         query: "true"
       port:
         entity:
           mappings:
             identifier: .head.repo.name + (.id|tostring)
             title: .title
             blueprint: '"githubPullRequest"'
             properties:
               creator: .user.login
               assignees: "[.assignees[].login]"
               reviewers: "[.requested_reviewers[].login]"
               status: .state
               closedAt: .closed_at
               updatedAt: .updated_at
               mergedAt: .merged_at
               prNumber: .number
               link: .html_url
             relations:
               jiraIssue:
                 combinator: '"or"'
                 rules:
                   # Match Jira issue key in PR title
                   - property: '"$identifier"'
                     operator: '"="'
                     value: (.title // "") | match("^[A-Za-z]+-[0-9]+") .string

                   # Match Jira issue key in PR description
                   - property: '"$identifier"'
                     operator: '"="'
                     value: (.body // "") | match("[A-Za-z]+-[0-9]+") .string
                   
                   # Match Jira issue key in PR branch name
                   - property: '"$identifier"'
                     operator: '"="'
                     value: (.head.ref // "") | match("[A-Za-z]+-[0-9]+") .string
   ```

5) Click `Save & Resync` to apply the changes

![](/img/guides/githubPREntityAfterJiraIssueMapping.png)

## Conclusion[â](#conclusion "Direct link to Conclusion")

By following these steps, you can seamlessly connect a GitHub pull request with a Jira Issue using either:

* Direct identifier mapping (extracting Jira issue keys from PR titles)
* Search relations (matching based on multiple criteria like title, description, and branch name)

Choose the approach that best fits your team's workflow and requirements. Search relations offer more flexibility but may require more configuration, while direct identifier mapping is simpler but less flexible.

More relevant guides and examples:

* [Port's Jira integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira/)
* [Integrate scorecards with Slack](https://docs.port.io/scorecards/manage-using-3rd-party-apps/slack)

# Source: https://docs.port.io/guides/all/create-jira-issue-from-dependabot.md

# Create Jira Issue from Dependabot Alert

## Overview[â](#overview "Direct link to Overview")

This guide will help you implement a self-service action in Port that allows you to create Jira issues from Dependabot alerts. This functionality streamlines vulnerability management by enabling users to quickly create and track issues for security alerts.

Available Github Integrations

This guide includes one or more steps that require integration with GitHub.<br /><!-- -->Port supports two GitHub integrations:

* **GitHub (Legacy)** - uses a GitHub app, which is soon to be deprecated.
* **GitHub (Ocean)** - uses the [Ocean framework](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md), recommended for new integrations.

Both integration options are present in this guide via tabs, choose the one that fits your needs.

You can implement this action in two ways:

1. **GitHub workflow**: A more flexible approach that allows for complex workflows and custom logic, suitable for teams that want to maintain their automation in Git.
2. **Synced webhooks**: A simpler approach that directly interacts with Jira's API through Port, ideal for quick implementation and minimal setup.

## Use cases[â](#use-cases "Direct link to Use cases")

* Automatically create Jira issues from Dependabot alerts.
* Add detailed metadata to Jira issues from Dependabot alerts.
* Link Dependabot alerts to services in your Port catalog.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).

* Access to your Jira organization with permissions to create issues.

* Install the GitHub integration relevant to you:

  * GitHub (Legacy)
  * GitHub (Ocean)

  Install Port's GitHub app by clicking [here](https://github.com/apps/getport-io/installations/new).

  Install [GitHub ocean](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md).

* [Jira API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) with permissions to create new issues.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

If you haven't installed the [Jira integration](/build-your-software-catalog/sync-data-to-catalog/project-management/jira/.md), you'll need to create blueprints for Jira projects and issues.<br /><!-- -->However we highly recommend you install the Jira integration to have these automatically set up for you.

### Create the Jira Project blueprint[â](#create-the-jira-project-blueprint "Direct link to Create the Jira Project blueprint")

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add this JSON schema:

   **Jira Project Blueprint (Click to expand)**

   Create in Port

   ```
   {
      "identifier": "jiraProject",
      "description": "A Jira project",
      "title": "Jira Project",
      "icon": "Jira",
      "schema": {
         "properties": {
            "url": {
               "title": "Project URL",
               "type": "string",
               "format": "url",
               "description": "URL to the project in Jira"
            },
            "totalIssues": {
               "title": "Total Issues",
               "type": "number",
               "description": "The total number of issues in the project"
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

5. Click "Save" to create the blueprint.

### Create the Repository blueprint[â](#create-the-repository-blueprint "Direct link to Create the Repository blueprint")

* GitHub (Legacy)
* GitHub (Ocean)

You should have installed the [Port's GitHub app](https://github.com/apps/getport-io), which automatically creates a `Repository` blueprint for you. If you haven't installed the app, you can create the `Repository` blueprint in Port using the schema below:

If you haven't created a blueprint representing your repositories yet, follow the [GitHub ocean examples](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/examples.md#repositories-dependabot-alerts-code-and-secrets-scan-alerts) and then come back to this guide. If you prefer, you can also create the `Repository` blueprint in Port using the schema below:

**Repository Blueprint (Click to expand)**

Create in Port

```
{
   "identifier": "githubRepository",
   "title": "Repository",
   "icon": "Github",
   "ownership": {
      "type": "Direct"
   },
   "schema": {
      "properties": {
         "readme": {
         "title": "README",
         "type": "string",
         "format": "markdown"
         },
         "url": {
         "icon": "DefaultProperty",
         "title": "Repository URL",
         "type": "string",
         "format": "url"
         },
         "defaultBranch": {
         "title": "Default branch",
         "type": "string"
         },
         "last_contributor": {
         "title": "Last contributor",
         "icon": "TwoUsers",
         "type": "string",
         "format": "user"
         },
         "last_push": {
         "icon": "GitPullRequest",
         "title": "Last push",
         "description": "Last commit to the main branch",
         "type": "string",
         "format": "date-time"
         },
         "require_code_owner_review": {
         "title": "Require code owner review",
         "type": "boolean",
         "icon": "DefaultProperty",
         "description": "Requires review from code owners before a pull request can be merged"
         },
         "require_approval_count": {
         "title": "Require approvals",
         "type": "number",
         "icon": "DefaultProperty",
         "description": "The number of approvals required before merging a pull request"
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

### Create the Dependabot Alert blueprint

Create the Dependabot Alert blueprint using this schema:

**Dependabot Alert Blueprint (Click to expand)**

Create in Port

```
{
   "identifier": "githubDependabotAlert",
   "title": "Dependabot Alert",
   "icon": "Github",
   "schema": {
      "properties": {
         "severity": {
            "icon": "DefaultProperty",
            "title": "Severity",
            "type": "string",
            "enum": [
               "low",
               "medium",
               "high",
               "critical"
            ],
            "enumColors": {
               "low": "green",
               "medium": "orange",
               "high": "red",
               "critical": "red"
            }
         },
         "state": {
            "title": "State",
            "type": "string",
            "enum": [
               "auto_dismissed",
               "dismissed",
               "fixed",
               "open"
            ],
            "enumColors": {
               "auto_dismissed": "green",
               "dismissed": "green",
               "fixed": "green",
               "open": "red"
            },
            "icon": "DefaultProperty"
         },
         "packageName": {
            "icon": "DefaultProperty",
            "title": "Package Name",
            "type": "string"
         },
         "packageEcosystem": {
            "title": "Package Ecosystem",
            "type": "string"
         },
         "manifestPath": {
            "title": "Manifest Path",
            "type": "string"
         },
         "scope": {
            "title": "Scope",
            "type": "string"
         },
         "ghsaID": {
            "title": "GHSA ID",
            "type": "string"
         },
         "cveID": {
            "title": "CVE ID",
            "type": "string"
         },
         "url": {
            "title": "URL",
            "type": "string",
            "format": "url"
         },
         "references": {
            "icon": "Vulnerability",
            "title": "References",
            "type": "array",
            "items": {
               "type": "string",
               "format": "url"
            }
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

To effectively manage your Dependabot alerts, map them to your `Repository` blueprint in Port. This allows you to categorize and link alerts to the appropriate repositories within your catalog, enhancing visibility and traceability.

* GitHub (Legacy)
* GitHub (Ocean)

Follow this [resource mapping guide](/build-your-software-catalog/sync-data-to-catalog/git/github/examples/.md#repositories-dependabot-alerts-and-code-scan-alerts) for detailed steps on how to map Dependabot alerts.

Follow this [resource mapping guide](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/examples.md#repositories-dependabot-alerts-code-and-secrets-scan-alerts) for detailed steps on how to map Dependabot alerts.

## Implementation[â](#implementation "Direct link to Implementation")

* Synced webhook
* GitHub workflow

You can create Jira issues from Dependabot alerts by leveraging Port's **synced webhooks** and **secrets** to directly interact with the Jira's API. This method simplifies the setup by handling everything within Port.

### Add Port secrets

Existing secrets

If you have already installed Port's <!-- -->Jira<!-- --> integration, these secrets should already exist in your portal.<br /><!-- -->To view your existing secrets:

1. Click on the `...` button in the top right corner of your Port application.
2. Choose **Credentials**, then click on the `Secrets` tab.

To add these secrets to your portal:

1. Click on the `...` button in the top right corner of your Port application.

2. Click on **Credentials**.

3. Click on the `Secrets` tab.

4. Click on `+ Secret` and add the following secrets:

   * `JIRA_API_TOKEN` - Your Jira API token

   * `JIRA_USER_EMAIL` - The email of the Jira user that owns the API token

   * `JIRA_AUTH` - Base64 encoded string of your Jira credentials. Generate this by running:

     ```
     echo -n "your-email@domain.com:your-api-token" | base64
     ```

     Replace `your-email@domain.com` with your Jira email and `your-api-token` with your Jira API token.

     One time generation

     The base64 encoded string only needs to be generated once and will work for all webhook calls until you change your API token.

### Set up self-service action

Follow these steps to create the self-service action:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Create Jira Issue from Dependabot Alert (Webhook) (Click to expand)**

   Create in Port

   ```
   {
      "identifier": "create_jira_issue_from_dependabot_webhook",
      "title": "Create Jira Issue from Dependabot (Webhook)",
      "icon": "Jira",
      "description": "Creates a Jira issue from dependabot alert using a webhook",
      "trigger": {
         "type": "self-service",
         "operation": "DAY-2",
         "userInputs": {
            "properties": {
               "project": {
                  "title": "Project Key",
                  "description": "The Jira project key where the issue will be created",
                  "icon": "Jira",
                  "type": "string"
               },
               "type": {
                  "title": "Type",
                  "description": "Issue type",
                  "icon": "Jira",
                  "type": "string",
                  "default": "Task",
                  "enum": [
                     "Task",
                     "Story",
                     "Bug",
                     "Epic"
                  ],
                  "enumColors": {
                     "Task": "blue",
                     "Story": "green",
                     "Bug": "red",
                     "Epic": "pink"
                  }
               }
            },
            "required": [
               "type",
               "project"
            ]
         },
         "blueprintIdentifier": "githubDependabotAlert"
      },
      "invocationMethod": {
         "type": "WEBHOOK",
         "url": "https://<JIRA_ORGANIZATION_URL>/rest/api/3/issue",
         "agent": false,
         "synchronized": true,
         "method": "POST",
         "headers": {
            "Authorization": "Basic {{.secrets.JIRA_AUTH}}",
            "Content-Type": "application/json"
         },
         "body": {
            "fields": {
               "project": {
                  "key": "{{.inputs.project}}"
               },
               "summary": "Dependabot Alert: {{.entity.title}}",
               "description": {
                  "version": 1,
                  "type": "doc",
                  "content": [
                     {
                        "type": "paragraph",
                        "content": [
                           {
                              "type": "text",
                              "text": "Severity",
                              "marks": [
                                 {
                                    "type": "strong"
                                 }
                              ]
                           },
                           {
                              "type": "text",
                              "text": ": {{.entity.properties.severity}}"
                           }
                        ]
                     },
                     {
                        "type": "paragraph",
                        "content": [
                           {
                              "type": "text",
                              "text": "State",
                              "marks": [
                                 {
                                    "type": "strong"
                                 }
                              ]
                           },
                           {
                              "type": "text",
                              "text": ": {{.entity.properties.state}}"
                           }
                        ]
                     },
                     {
                        "type": "paragraph",
                        "content": [
                           {
                              "type": "text",
                              "text": "Package Name",
                              "marks": [
                                 {
                                    "type": "strong"
                                 }
                              ]
                           },
                           {
                              "type": "text",
                              "text": ": {{.entity.properties.packageName}}"
                           }
                        ]
                     },
                     {
                        "type": "paragraph",
                        "content": [
                           {
                              "type": "text",
                              "text": "Package Ecosystem",
                              "marks": [
                                 {
                                    "type": "strong"
                                 }
                              ]
                           },
                           {
                              "type": "text",
                              "text": ": {{.entity.properties.packageEcosystem}}"
                           }
                        ]
                     },
                     {
                        "type": "paragraph",
                        "content": [
                           {
                              "type": "text",
                              "text": "Manifest Path",
                              "marks": [
                                 {
                                    "type": "strong"
                                 }
                              ]
                           },
                           {
                              "type": "text",
                              "text": ": {{.entity.properties.manifestPath}}"
                           }
                        ]
                     },
                     {
                        "type": "paragraph",
                        "content": [
                           {
                              "type": "text",
                              "text": "Scope",
                              "marks": [
                                 {
                                    "type": "strong"
                                 }
                              ]
                           },
                           {
                              "type": "text",
                              "text": ": {{.entity.properties.scope}}"
                           }
                        ]
                     },
                     {
                        "type": "paragraph",
                        "content": [
                           {
                              "type": "text",
                              "text": "GHSA ID",
                              "marks": [
                                 {
                                    "type": "strong"
                                 }
                              ]
                           },
                           {
                              "type": "text",
                              "text": ": {{.entity.properties.ghsaID}}"
                           }
                        ]
                     },
                     {
                        "type": "paragraph",
                        "content": [
                           {
                              "type": "text",
                              "text": "CVE ID",
                              "marks": [
                                 {
                                    "type": "strong"
                                 }
                              ]
                           },
                           {
                              "type": "text",
                              "text": ": {{.entity.properties.cveID}}"
                           }
                        ]
                     },
                     {
                        "type": "paragraph",
                        "content": [
                           {
                              "type": "text",
                              "text": "URL",
                              "marks": [
                                 {
                                    "type": "strong"
                                 }
                              ]
                           },
                           {
                              "type": "text",
                              "text": ": "
                           },
                           {
                              "type": "text",
                              "text": "{{.entity.properties.url}}",
                              "marks": [
                                 {
                                    "type": "link",
                                    "attrs": {
                                       "href": "{{.entity.properties.url}}"
                                    }
                                 }
                              ]
                           }
                        ]
                     }
                  ]
               },
               "issuetype": {
                  "name": "{{.inputs.type}}"
               },
               "labels": ["port-{{.entity.identifier}}"]
            }
         }
      },
      "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Create Jira Issue from Dependabot (Webhook)` action in the self-service page. ð

Configure your Jira url

Replace `<JIRA_ORGANIZATION_URL>` in the webhook URL with your Jira organization URL (e.g., `example.atlassian.net`).

To implement this use-case using a GitHub workflow, follow these steps:

### Add GitHub secrets

In your GitHub repository, [go to **Settings > Secrets**](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) and add the following secrets:

* `JIRA_API_TOKEN` - [Jira API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account) generated by the user.
* `JIRA_BASE_URL` - The URL of your Jira organization. For example, <https://your-organization.atlassian.net>.
* `JIRA_USER_EMAIL` - The email of the Jira user that owns the Jira API token.
* `PORT_CLIENT_ID` - Your port `client id` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).
* `PORT_CLIENT_SECRET` - Your port `client secret` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).

### Add GitHub workflow

Create the file `.github/workflows/create-jira-issue-from-dependabot.yml` in the `.github/workflows` folder of your repository.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

**GitHub Workflow (Click to expand)**

```
name: Create Jira Issue from Dependabot Alert

on:
   workflow_dispatch:
      inputs:
         project:
            required: true
            type: string
         type:
            required: true
            type: string
         port_context:
            required: true
            type: string

jobs:
   create-jira-issue:
      runs-on: ubuntu-latest
      steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Login to Jira
           uses: atlassian/gajira-login@v3
           env:
              JIRA_BASE_URL: ${{ secrets.JIRA_BASE_URL }}
              JIRA_USER_EMAIL: ${{ secrets.JIRA_USER_EMAIL }}
              JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}

         - name: Inform starting of Jira issue creation
           uses: port-labs/port-github-action@v1
           with:
              clientId: ${{ secrets.PORT_CLIENT_ID }}
              clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
              operation: PATCH_RUN
              runId: ${{ fromJson(inputs.port_context).run_id }}
              logMessage: "Creating a new Jira issue from Dependabot alert... â´ï¸"

         - name: Create Jira issue
           id: create_jira
           uses: atlassian/gajira-create@v3
           with:
              project: ${{ inputs.project }}
              issuetype: ${{ inputs.type }}
              summary: "Dependabot Alert: ${{ fromJson(inputs.port_context).entity.title }}"
              description: |
                 **Severity**: ${{ fromJson(inputs.port_context).entity.properties.severity }}
                 **State**: ${{ fromJson(inputs.port_context).entity.properties.state }}
                 **Package Name**: ${{ fromJson(inputs.port_context).entity.properties.packageName }}
                 **Package Ecosystem**: ${{ fromJson(inputs.port_context).entity.properties.packageEcosystem }}
                 **Manifest Path**: ${{ fromJson(inputs.port_context).entity.properties.manifestPath }}
                 **Scope**: ${{ fromJson(inputs.port_context).entity.properties.scope }}
                 **GHSA ID**: ${{ fromJson(inputs.port_context).entity.properties.ghsaID }}
                 **CVE ID**: ${{ fromJson(inputs.port_context).entity.properties.cveID }}
                 **URL**: ${{ fromJson(inputs.port_context).entity.properties.url }}
              fields: |
                 {
                   "labels": ["port-${{ fromJson(inputs.port_context).entity.identifier }}"]
                 }

         - name: Inform creation of Jira issue
           uses: port-labs/port-github-action@v1
           with:
              clientId: ${{ secrets.PORT_CLIENT_ID }}
              clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
              operation: PATCH_RUN
              link: ${{ secrets.JIRA_BASE_URL }}/browse/${{ steps.create_jira.outputs.issue }}
              runId: ${{ fromJson(inputs.port_context).run_id }}
              logMessage: |
                 Jira issue created! â
                 The issue ID is: ${{ steps.create_jira.outputs.issue }}
```

### Set up self-service action

We will create a self-service action to handle creating Jira issues from Dependabot alerts. To create a self-service action follow these steps:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Create Jira Issue from Dependabot Alert (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   * GitHub (Legacy)
   * GitHub (Ocean)

   Create in Port

   ```
   {
      "identifier": "create_jira_issue_from_dependabot",
      "title": "Create Jira Issue from Dependabot",
      "icon": "Jira",
      "description": "Creates a Jira issue from dependabot.",
      "trigger": {
         "type": "self-service",
         "operation": "DAY-2",
         "userInputs": {
            "properties": {
               "project": {
                  "title": "Project",
                  "description": "The issue will be created on this project",
                  "icon": "Jira",
                  "type": "string",
                  "blueprint": "jiraProject",
                  "format": "entity"
               },
               "type": {
                  "title": "Type",
                  "description": "Issue type",
                  "icon": "Jira",
                  "type": "string",
                  "default": "Task",
                  "enum": [
                     "Task",
                     "Story",
                     "Bug",
                     "Epic"
                  ],
                  "enumColors": {
                     "Task": "blue",
                     "Story": "green",
                     "Bug": "red",
                     "Epic": "pink"
                  }
               }
            },
            "required": [
               "type",
               "project"
            ]
         },
         "blueprintIdentifier": "githubDependabotAlert"
      },
      "invocationMethod": {
         "type": "GITHUB",
         "org": "<GITHUB_ORG>",
         "repo": "<GITHUB_REPO>",
         "workflow": "create-jira-issue-from-dependabot.yml",
         "workflowInputs": {
            "type": "{{.inputs.\"type\"}}",
            "project": "{{.inputs.\"project\" | if type == \"array\" then map(.identifier) else .identifier end}}",
            "port_context": {
               "entity": "{{.entity}}",
               "run_id": "{{.run.id}}"
            }
         },
         "reportWorkflowStatus": true
      },
      "requiredApproval": false
   }
   ```

   Create in Port

   ```
   {
      "identifier": "create_jira_issue_from_dependabot",
      "title": "Create Jira Issue from Dependabot",
      "icon": "Jira",
      "description": "Creates a Jira issue from dependabot.",
      "trigger": {
         "type": "self-service",
         "operation": "DAY-2",
         "userInputs": {
            "properties": {
               "project": {
                  "title": "Project",
                  "description": "The issue will be created on this project",
                  "icon": "Jira",
                  "type": "string",
                  "blueprint": "jiraProject",
                  "format": "entity"
               },
               "type": {
                  "title": "Type",
                  "description": "Issue type",
                  "icon": "Jira",
                  "type": "string",
                  "default": "Task",
                  "enum": [
                     "Task",
                     "Story",
                     "Bug",
                     "Epic"
                  ],
                  "enumColors": {
                     "Task": "blue",
                     "Story": "green",
                     "Bug": "red",
                     "Epic": "pink"
                  }
               }
            },
            "required": [
               "type",
               "project"
            ]
         },
         "blueprintIdentifier": "githubDependabotAlert"
      },
      "invocationMethod": {
         "type": "INTEGRATION_ACTION",
         "installationId": "<GITHUB_OCEAN_INSTALLATION_ID>",
         "integrationActionType": "dispatch_workflow",
         "org": "<GITHUB_ORG>",
         "repo": "<GITHUB_REPO>",
         "workflow": "create-jira-issue-from-dependabot.yml",
         "workflowInputs": {
            "type": "{{.inputs.\"type\"}}",
            "project": "{{.inputs.\"project\" | if type == \"array\" then map(.identifier) else .identifier end}}",
            "port_context": {
               "entity": "{{.entity}}",
               "run_id": "{{.run.id}}"
            }
         },
         "reportWorkflowStatus": true
      },
      "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Create Jira Issue from Dependabot` action in the self-service page. ð

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Head to the [self-service page](https://app.getport.io/self-serve) of your portal

2. Choose either the GitHub workflow or webhook implementation:

   * For GitHub workflow: Click on `Create Jira Issue from Dependabot`
   * For webhook: Click on `Create Jira Issue from Dependabot (Webhook)`

3. Select the Dependabot alert you want to create an issue for

4. Select the project where the issue will be created

5. Select the issue type

6. Click on `Execute`

7. Done! wait for the issue to be created in Jira

## More Self Service Jira Actions Examples[â](#more-self-service-jira-actions-examples "Direct link to More Self Service Jira Actions Examples")

* [Report a bug in Jira](https://docs.port.io/guides/all/report-a-bug/) using Port's self-service actions
* [Open Jira issues with automatic labels](https://docs.port.io/guides/all/open-jira-issue-with-automatic-label)
* [Open/close JIRA issues for entities with violated scorecard rules](https://docs.port.io/scorecards/manage-using-3rd-party-apps/jira)
* [Change status and assignee of Jira tickets](https://docs.port.io/guides/all/change-status-and-assignee-of-jira-ticket)

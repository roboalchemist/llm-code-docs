# Source: https://docs.port.io/guides/all/report-a-bug.md

# Report a bug

## Overview[â](#overview "Direct link to Overview")

Available Github Integrations

This guide includes one or more steps that require integration with GitHub.<br /><!-- -->Port supports two GitHub integrations:

* **GitHub (Legacy)** - uses a GitHub app, which is soon to be deprecated.
* **GitHub (Ocean)** - uses the [Ocean framework](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md), recommended for new integrations.

Both integration options are present in this guide via tabs, choose the one that fits your needs.

This guide will help you implement a self-service action in Port that allows you to report bugs in Jira, ensuring prompt issue resolution and improving overall platform reliability.

You can implement this action in two ways:

1. **GitHub workflow**: A more flexible approach that allows for complex workflows and custom logic, suitable for teams that want to maintain their automation in Git.
2. **Synced webhooks**: A simpler approach that directly interacts with Jira's API through Port, ideal for quick implementation and minimal setup.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).

* Access to your Jira organization with permissions to create issues.

* Install Port's GitHub integration (required for GitHub Actions implementation):

  * GitHub (Legacy)
  * GitHub (Ocean)

  [Port's GitHub app](https://github.com/apps/getport-io) installed.

  The [GitHub Ocean integration](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md) installed.

* [Jira API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) with permissions to create new issues.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

If you haven't installed the [Jira integration](/build-your-software-catalog/sync-data-to-catalog/project-management/jira/.md), you'll need to create a blueprint for Jira issues.<br /><!-- -->However we highly recommend you install the Jira integration to have these automatically set up for you.

### Create the jira issue blueprint

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
     "relations": {}
   }
   ```

5. Click "Save" to create the blueprint.

## Implementation[â](#implementation "Direct link to Implementation")

* Synced webhook
* GitHub workflow

You can create Jira bugs by leveraging Port's **synced webhooks** and **secrets** to directly interact with the Jira's API. This method simplifies the setup by handling everything within Port.

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

   **Report a bug action (Webhook) (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "jiraIssue_report_a_bug_webhook",
     "title": "Report a bug (Webhook)",
     "icon": "Jira",
     "description": "Report a bug in Port to our product team using webhook.",
     "trigger": {
       "type": "self-service",
       "operation": "CREATE",
       "userInputs": {
         "properties": {
           "project": {
             "title": "Project",
             "description": "The Jira project where the bug will be created",
             "icon": "Jira",
             "type": "string",
             "blueprint": "jiraProject",
             "format": "entity"
           },
           "description": {
             "icon": "DefaultProperty",
             "title": "Description",
             "type": "string"
           },
           "short_title": {
             "icon": "DefaultProperty",
             "title": "Short title",
             "type": "string"
           }
         },
         "required": [
           "project",
           "short_title",
           "description"
         ],
         "order": [
           "project",
           "short_title",
           "description"
         ]
       }
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
             "key": "{{.inputs.project.identifier}}"
           },
           "summary": "{{.inputs.short_title}}",
           "description": {
             "version": 1,
             "type": "doc",
             "content": [
               {
                 "type": "paragraph",
                 "content": [
                   {
                     "type": "text",
                     "text": "{{.inputs.description}}"
                   }
                 ]
               },
               {
                 "type": "paragraph",
                 "content": [
                   {
                     "type": "text",
                     "text": "Reported by: {{.trigger.by.user.email}}"
                   }
                 ]
               }
             ]
           },
           "issuetype": {
             "name": "Bug"
           }
         }
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Configure your Jira url

Replace `<JIRA_ORGANIZATION_URL>` in the webhook URL with your Jira organization URL (e.g., `example.atlassian.net`).

Now you should see the `Report a bug (Webhook)` action in the self-service page. ð

To implement this use-case using a GitHub workflow, follow these steps:

### Add GitHub secrets

In your GitHub repository, [go to **Settings > Secrets**](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) and add the following secrets:

* `JIRA_API_TOKEN` - [Jira API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account) generated by the user.
* `JIRA_BASE_URL` - The URL of your Jira organization. For example, <https://your-organization.atlassian.net>.
* `JIRA_USER_EMAIL` - The email of the Jira user that owns the Jira API token.
* `PORT_CLIENT_ID` - Your port `client id` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).
* `PORT_CLIENT_SECRET` - Your port `client secret` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).

### Add GitHub workflow

Create the file `.github/workflows/report-a-bug.yml` in the `.github/workflows` folder of your repository.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

**GitHub Workflow (Click to expand)**

```
name: Report a bug in jira

on:
  workflow_dispatch:
    inputs:
      description:
        required: true
        type: string
      short_title:
        required: true
        type: string
      port_context:
        required: true
        type: string

jobs:
  create_jira_issue:
    runs-on: ubuntu-latest
    steps:
      - name: Login
        uses: atlassian/gajira-login@v3
        env:
          JIRA_BASE_URL: ${{ secrets.JIRA_BASE_URL }}
          JIRA_USER_EMAIL: ${{ secrets.JIRA_USER_EMAIL }}
          JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}

      - name: Inform searching of user in user list
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: |
            Searching for user in organization user list... â´ï¸

      - name: Search for reporter among user list
        id: search_for_reporter
        uses: fjogeleit/http-request-action@v1
        with:
          url: "${{ secrets.JIRA_BASE_URL }}/rest/api/3/user/search?query=${{ fromJson(inputs.port_context).triggered_by }}"
          method: "GET"
          username: ${{ secrets.JIRA_USER_EMAIL }}
          password: ${{ secrets.JIRA_API_TOKEN }}
          customHeaders: '{"Content-Type": "application/json"}'

      - name: Install jq
        run: sudo apt-get install jq
        if: steps.search_for_reporter.outcome == 'success'

      - name: Retrieve user list from search
        id: user_list_from_search
        if: steps.search_for_reporter.outcome == 'success'
        run: |
          selected_user_id=$(echo '${{ steps.search_for_reporter.outputs.response }}' | jq -r 'if length > 0 then .[0].accountId else "empty" end')
          selected_user_name=$(echo '${{ steps.search_for_reporter.outputs.response }}' | jq -r 'if length > 0 then .[0].displayName else "empty" end')
          echo "selected_user_id=${selected_user_id}" >> $GITHUB_OUTPUT
          echo "selected_user_name=${selected_user_name}" >> $GITHUB_OUTPUT

      - name: Inform user existence
        if: steps.user_list_from_search.outputs.selected_user_id != 'empty'
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: |
            User found ð¥¹ Bug reporter will be ${{ steps.user_list_from_search.outputs.selected_user_name }}... â´ï¸

      - name: Inform user inexistence
        if: steps.user_list_from_search.outputs.selected_user_id == 'empty'
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: |
            User not found ð­ Bug will be created with default reporter â´ï¸

      - name: Inform starting of jira issue creation
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: |
            Creating a new Jira issue.. â´ï¸

      - name: Create Jira issue
        id: create
        uses: atlassian/gajira-create@v3
        with:
          project: ${{ inputs.project }}
          issuetype: Bug
          summary: ${{inputs.short_title}}
          description: |
            ${{inputs.description}}
          fields: |-
            ${{ steps.user_list_from_search.outputs.selected_user_id != 'empty'
              && format('{{"reporter": {{"id": "{0}" }}}}', steps.user_list_from_search.outputs.selected_user_id)
              || '{}'
            }}

      - name: Inform creation of Jira issue
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          operation: PATCH_RUN
          link: ${{ secrets.JIRA_BASE_URL }}/browse/${{ steps.create.outputs.issue }}
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: |
            Jira issue with ID ${{ steps.create.outputs.issue }} created! â
```

### Set up self-service action

We will create a self-service action to handle creating bugs in Jira. To create a self-service action follow these steps:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Report a bug action (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   * GitHub (Legacy)
   * GitHub (Ocean)

   Create in Port

   ```
   {
     "identifier": "jiraIssue_report_a_bug",
     "title": "Report a bug",
     "icon": "Jira",
     "description": "Report a bug in Port to our product team.",
     "trigger": {
       "type": "self-service",
       "operation": "CREATE",
       "userInputs": {
         "properties": {
           "project": {
             "title": "Project",
             "description": "The Jira project where the bug will be created",
             "icon": "Jira",
             "type": "string",
             "blueprint": "jiraProject",
             "format": "entity"
           },
           "description": {
             "icon": "DefaultProperty",
             "title": "Description",
             "type": "string"
           },
           "short_title": {
             "icon": "DefaultProperty",
             "title": "Short title",
             "type": "string"
           }
         },
         "required": [
           "project",
           "short_title",
           "description"
         ],
         "order": [
           "project",
           "short_title",
           "description"
         ]
       }
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB_ORG>",
       "repo": "<GITHUB_REPO>",
       "workflow": "report-a-bug.yml",
       "workflowInputs": {
         "project": "{{.inputs.project.identifier}}",
         "description": "{{.inputs.\"description\"}}",
         "short_title": "{{.inputs.\"short_title\"}}",
         "port_context": {
           "run_id": "{{ .run.id }}",
           "triggered_by": "{{ .trigger.by.user.email }}"
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
     "identifier": "jiraIssue_report_a_bug",
     "title": "Report a bug",
     "icon": "Jira",
     "description": "Report a bug in Port to our product team.",
     "trigger": {
       "type": "self-service",
       "operation": "CREATE",
       "userInputs": {
         "properties": {
           "project": {
             "title": "Project",
             "description": "The Jira project where the bug will be created",
             "icon": "Jira",
             "type": "string",
             "blueprint": "jiraProject",
             "format": "entity"
           },
           "description": {
             "icon": "DefaultProperty",
             "title": "Description",
             "type": "string"
           },
           "short_title": {
             "icon": "DefaultProperty",
             "title": "Short title",
             "type": "string"
           }
         },
         "required": [
           "project",
           "short_title",
           "description"
         ],
         "order": [
           "project",
           "short_title",
           "description"
         ]
       }
     },
     "invocationMethod": {
       "type": "INTEGRATION_ACTION",
       "installationId": "<GITHUB_OCEAN_INSTALLATION_ID>",
       "integrationActionType": "dispatch_workflow",
       "org": "<GITHUB_ORG>",
       "repo": "<GITHUB_REPO>",
       "workflow": "report-a-bug.yml",
       "workflowInputs": {
         "project": "{{.inputs.project.identifier}}",
         "description": "{{.inputs.\"description\"}}",
         "short_title": "{{.inputs.\"short_title\"}}",
         "port_context": {
           "run_id": "{{ .run.id }}",
           "triggered_by": "{{ .trigger.by.user.email }}"
         }
       },
       "reportWorkflowStatus": true
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Report a bug` action in the self-service page. ð

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Head to the [self-service page](https://app.getport.io/self-serve) of your portal

2. Choose either the GitHub workflow or webhook implementation:

   * For GitHub workflow: Click on `Report a bug`
   * For webhook: Click on `Report a bug (Webhook)`

3. Fill in the bug details:

   * Select the Jira project where the bug will be created
   * Short title of the bug
   * Description of the bug

4. Click on `Execute`

5. Done! wait for the bug to be created in Jira

## More Self Service Jira Actions Examples[â](#more-self-service-jira-actions-examples "Direct link to More Self Service Jira Actions Examples")

* [Open Jira issues with automatic labels](https://docs.port.io/guides/all/open-jira-issue-with-automatic-label)
* [Change status and assignee of Jira tickets](https://docs.port.io/guides/all/change-status-and-assignee-of-jira-ticket)
* [Open/close JIRA issues for entities with violated scorecard rules](https://docs.port.io/scorecards/manage-using-3rd-party-apps/jira)

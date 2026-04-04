# Source: https://docs.port.io/guides/all/create-pagerduty-service.md

# Create a PagerDuty Service

## Overview[â](#overview "Direct link to Overview")

This guide will help you implement a self-service action in Port that allows you to create PagerDuty services directly from Port. This functionality streamlines service management by enabling users to create services without leaving Port.

You can implement this action in two ways:

1. **GitHub workflow**: A more flexible approach that allows for complex workflows and custom logic, suitable for teams that want to maintain their automation in Git.
2. **Synced webhooks**: A simpler approach that directly interacts with PagerDuty's API through Port, ideal for quick implementation and minimal setup.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).
* Access to your PagerDuty organization with permissions to manage services.
* Optional - Install Port's [PagerDuty integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty).

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

If you haven't installed the PagerDuty integration, you'll need to create a blueprint for PagerDuty services. However, we highly recommend you install the PagerDuty integration to have these automatically set up for you.

### Create the PagerDuty service blueprint

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add this JSON schema:

   **PagerDuty Service Blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "pagerdutyService",
     "description": "This blueprint represents a PagerDuty service in our software catalog",
     "title": "PagerDuty Service",
     "icon": "pagerduty",
     "schema": {
       "properties": {
         "description": {
           "type": "string",
           "title": "Description"
         },
         "status": {
           "type": "string",
           "title": "Status",
           "enum": ["active", "warning", "critical", "maintenance", "disabled"]
         },
         "url": {
           "type": "string",
           "format": "url",
           "title": "Service URL"
         },
         "created_at": {
           "type": "string",
           "format": "date-time",
           "title": "Created At"
         },
         "updated_at": {
           "type": "string",
           "format": "date-time",
           "title": "Updated At"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "relations": {}
   }
   ```

5. Click "Save" to create the blueprint.

## Implementation[â](#implementation "Direct link to Implementation")

* Synced webhook
* GitHub workflow

You can create PagerDuty services by leveraging Port's **synced webhooks** and **secrets** to directly interact with the PagerDuty's API. This method simplifies the setup by handling everything within Port.

### Add Port secrets

Existing secrets

If you have already installed Port's <!-- -->PagerDuty<!-- --> integration, these secrets should already exist in your portal.<br /><!-- -->To view your existing secrets:

1. Click on the `...` button in the top right corner of your Port application.
2. Choose **Credentials**, then click on the `Secrets` tab.

To add these secrets to your portal:

1. Click on the `...` button in the top right corner of your Port application.

2. Click on **Credentials**.

3. Click on the `Secrets` tab.

4. Click on `+ Secret` and add the following secrets:

   * `PAGERDUTY_API_TOKEN`: Your PagerDuty API token
   * `PAGERDUTY_USER_EMAIL`: The email of the PagerDuty user that owns the API token

### Set up self-service action

We will create a self-service action to handle creating PagerDuty services using webhooks. To create a self-service action follow these steps:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Create PagerDuty Service (Webhook) (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "create_pagerduty_service_webhook",
     "title": "Create Service (Webhook)",
     "icon": "pagerduty",
     "description": "Create a new PagerDuty service using a webhook",
     "trigger": {
       "type": "self-service",
       "operation": "CREATE",
       "userInputs": {
         "properties": {
           "name": {
             "title": "Name",
             "description": "Name of the PagerDuty Service",
             "icon": "pagerduty",
             "type": "string"
           },
           "description": {
             "title": "Description",
             "description": "Description of the PagerDuty Service",
             "icon": "pagerduty",
             "type": "string"
           },
           "escalation_policy": {
             "title": "Escalation Policy",
             "description": "PagerDuty Escalation Policy ID (e.g., P7LVMYP)",
             "icon": "pagerduty",
             "type": "string"
           }
         },
         "required": [
           "name",
           "escalation_policy"
         ],
         "order": [
           "name",
           "description",
           "escalation_policy"
         ]
       },
       "blueprintIdentifier": "pagerdutyService"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.pagerduty.com/services",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Authorization": "Token token={{.secrets.PAGERDUTY_API_TOKEN}}",
         "Accept": "application/vnd.pagerduty+json;version=2",
         "From": "{{.secrets.PAGERDUTY_USER_EMAIL}}",
         "Content-Type": "application/json"
       },
       "body": {
         "service": {
           "name": "{{.inputs.name}}",
           "description": "{{.inputs.description}}",
           "status": "active",
           "escalation_policy": {
             "id": "{{.inputs.escalation_policy}}",
             "type": "escalation_policy_reference"
           }
         }
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Create Service (Webhook)` actions in the self-service page. ð

### Create an automation to upsert entity in port

After each execution of the action, we would like to update the relevant entity in Port with the latest status.

To achieve this, we can create an automation that will be triggered when the action completes successfully.

To create the automation:

1. Head to the [automation](https://app.getport.io/settings/automations) page.

2. Click on the `+ Automation` button.

3. Copy and paste the following JSON configuration into the editor.

   **Update PagerDuty service in Port automation (Click to expand)**

   Create in Port

   ```
       {
         "identifier": "pagerdutyService_sync_status",
         "title": "Sync PagerDuty Service Status",
         "description": "Update PagerDuty service data in Port after creation",
         "trigger": {
           "type": "automation",
           "event": {
             "type": "RUN_UPDATED",
             "actionIdentifier": "create_pagerduty_service_webhook"
           },
           "condition": {
             "type": "JQ",
             "expressions": [
               ".diff.after.status == \"SUCCESS\""
             ],
             "combinator": "and"
           }
         },
         "invocationMethod": {
           "type": "UPSERT_ENTITY",
           "blueprintIdentifier": "pagerdutyService",
           "mapping": {
             "identifier": "{{.event.diff.after.response.service.id}}",
             "title": "{{.event.diff.after.response.service.name}}",
             "properties": {
               "description": "{{.event.diff.after.response.service.description}}",
               "status": "{{.event.diff.after.response.service.status}}",
               "url": "{{.event.diff.after.response.service.html_url}}",
               "created_at": "{{.event.diff.after.response.service.created_at}}",
               "updated_at": "{{.event.diff.after.response.service.updated_at}}"
             }
           }
         },
         "publish": true
     }
   ```

4. Click `Save`.

Now when you execute the webhook action, the service data in Port will be automatically updated with the latest information from PagerDuty.

To implement this use-case using a GitHub workflow, follow these steps:

### Add GitHub secrets

In your GitHub repository, [go to **Settings > Secrets**](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) and add the following secrets:

* `PAGERDUTY_API_KEY` - [PagerDuty API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account) generated by the user.
* `PORT_CLIENT_ID` - Your port `client id` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).
* `PORT_CLIENT_SECRET` - Your port `client secret` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).

### Add GitHub workflow

Create the file `.github/workflows/create-pagerduty-service.yaml` in the `.github/workflows` folder of your repository.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

**GitHub Workflow (Click to expand)**

```
name: Create PagerDuty Service
on:
  workflow_dispatch:
    inputs:
      name:
        description: 'Name of the PagerDuty Service'
        required: true
        type: string
      description:
        description: 'Description of the PagerDuty Service'
        required: false
        type: string
      escalation_policy:
        description: 'Escalation Policy for the service'
        required: true
        type: string
      port_context:
        required: true
        description: includes blueprint, run ID, and entity identifier from Port.

jobs:
  create-pagerduty-service:
    runs-on: ubuntu-latest
    steps:
      - name: Create Service in PagerDuty
        id : create_service_request
        uses: fjogeleit/http-request-action@v1
        with:
          url: 'https://api.pagerduty.com/services'
          method: 'POST'
          customHeaders: '{"Content-Type": "application/json", "Accept": "application/vnd.pagerduty+json;version=2", "Authorization": "Token token=${{ secrets.PAGERDUTY_API_KEY }}"}'
          data: >-
            {
              "service": {
                "name": "${{ github.event.inputs.name }}",
                "description": "${{ github.event.inputs.description }}",
                "status": "active",
                "escalation_policy": {
                  "id": "${{ github.event.inputs.escalation_policy }}",
                  "type": "escalation_policy_reference"
                  }
                }
              }
          
      - name: Log Create Service Request Failure 
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Request to create service failed ..."
          
      - name: Log Request Success
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: |
             PagerDuty service created! â
             Requesting for on-calls
    
      - name: Request for oncalls for Escalation Policy
        id: fetch_oncalls
        uses: fjogeleit/http-request-action@v1
        with:
          url: 'https://api.pagerduty.com/oncalls?include[]=users&escalation_policy_ids[]=${{ inputs.escalation_policy }}'
          method: 'GET'
          customHeaders: '{"Content-Type": "application/json", "Accept": "application/json", "Authorization": "Token token=${{ secrets.PAGERDUTY_API_KEY }}"}'

      - name: Extract User Emails
        if: steps.fetch_oncalls.outcome == 'success'
        id: extract_user_emails
        run: |
          echo "Extracting user emails..."
          EMAILS=$(echo '${{ steps.fetch_oncalls.outputs.response }}' | jq -c '[.oncalls[].user.email]')
          echo "Extracted emails: $EMAILS"
          echo "user_emails=${EMAILS}" >> $GITHUB_ENV

      - name: Log Fetch Oncalls Request Failure
        if: steps.fetch_oncalls.outcome == 'failure'
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: Failed to fetch on-calls â
          
      - name: Log Before Upserting Entity
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: |
              Upserting Created PagerDuty Entity

      - name: UPSERT PagerDuty Entity
        uses: port-labs/port-github-action@v1
        with:
          identifier: "${{ fromJson(steps.create_service_request.outputs.response).service.id }}" 
          title: "${{ fromJson(steps.create_service_request.outputs.response).service.summary }}"
          icon: pagerduty
          blueprint: "${{fromJson(inputs.port_context).blueprint}}"
          properties: |-
            {
              "status": "${{ fromJson(steps.create_service_request.outputs.response).service.status }}",
              "url": "${{ fromJson(steps.create_service_request.outputs.response).service.html_url }}",
              "oncall": ${{ env.user_emails }}
            }
          relations: "${{ toJson(fromJson(inputs.port_context).relations) }}"
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: UPSERT
          runId: ${{fromJson(inputs.port_context).run_id}}

      - name: Log After Upserting Entity
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: |
              Upserting was successful â
```

### Set up self-service action

We will create a self-service action to handle creating PagerDuty services. To create a self-service action follow these steps:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Create PagerDuty Service (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   Create in Port

   ```
   {
     "identifier": "pagerdutyService_create_service",
     "title": "Create Service",
     "icon": "pagerduty",
     "description": "Create PagerDuty Service",
     "trigger": {
       "type": "self-service",
       "operation": "CREATE",
       "userInputs": {
         "properties": {
           "name": {
             "title": "Name",
             "description": "Name of the PagerDuty Service",
             "icon": "pagerduty",
             "type": "string"
           },
           "description": {
             "title": "Description",
             "description": "Description of the PagerDuty Service",
             "icon": "pagerduty",
             "type": "string"
           },
           "escalation_policy": {
             "title": "Escalation Policy",
             "description": "PagerDuty Escalation Policy ID to apply",
             "icon": "pagerduty",
             "type": "string"
           }
         },
         "required": [
           "name",
           "escalation_policy"
         ],
         "order": [
           "name",
           "description",
           "escalation_policy"
         ]
       },
       "blueprintIdentifier": "pagerdutyService"
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB_ORG>",
       "repo": "<GITHUB_REPO>",
       "workflow": "create-pagerduty-service.yaml",
       "workflowInputs": {
         "name": "{{.inputs.\"name\"}}",
         "description": "{{.inputs.\"description\"}}",
         "escalation_policy": "{{.inputs.\"escalation_policy\"}}",
         "port_context": {
           "blueprint": "{{.action.blueprint}}",
           "entity": "{{.entity.identifier}}",
           "run_id": "{{.run.id}}"
         }
       },
       "reportWorkflowStatus": true
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Create Service` action in the self-service page. ð

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Head to the [self-service page](https://app.getport.io/self-serve) of your portal.

2. Choose either the GitHub workflow or webhook implementation:

   * For GitHub workflow: Click on `Create Service`.
   * For webhook: Click on `Create Service (Webhook)`.

3. Enter the required information:

   * Name of the service.

   * Description (optional).

   * Escalation Policy ID.

     Escalation Policy ID

     The escalation policy ID is a unique identifier (e.g., P7LVMYP) that you can find in your PagerDuty dashboard:

     1. Go to Configuration â Escalation Policies.
     2. Click on the policy you want to use.
     3. The ID is the last part of the URL (e.g., in <https://example-subdomain.pagerduty.com/escalation_policies/P7LAMYP>, the ID is P7LAMYP).

4. Click on `Execute`.

5. Done! Wait for the service to be created in PagerDuty.

## Related guides[â](#related-guides "Direct link to Related guides")

* [Acknowledge Incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/acknowledge-incident).
* [Change On-Call User](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-on-call-user).
* [Create PagerDuty incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/interact-with-pagerduty-incidents).
* [Change PagerDuty incident owner](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-pagerduty-incident-owner).
* [Escalate an incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/escalate-an-incident).
* [Resolve an incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/resolve-incident).
* [Trigger PagerDuty incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/trigger-pagerduty-incident).

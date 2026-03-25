# Source: https://docs.port.io/guides/all/acknowledge-incident.md

# Acknowledge Incident In PagerDuty

## Overview[â](#overview "Direct link to Overview")

Available Github Integrations

This guide includes one or more steps that require integration with GitHub.<br /><!-- -->Port supports two GitHub integrations:

* **GitHub (Legacy)** - uses a GitHub app, which is soon to be deprecated.
* **GitHub (Ocean)** - uses the [Ocean framework](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md), recommended for new integrations.

Both integration options are present in this guide via tabs, choose the one that fits your needs.

This guide will help you implement a self-service action in Port that allows you to acknowledge incidents in PagerDuty directly from Port. This functionality streamlines incident management by enabling users to quickly respond to alerts without leaving Port.

You can implement this action in two ways:

1. **GitHub workflow**: A more flexible approach that allows for complex workflows and custom logic, suitable for teams that want to maintain their automation in Git.
2. **Synced webhooks**: A simpler approach that directly interacts with Pagerduty's API through Port, ideal for quick implementation and minimal setup.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).

* Access to your PagerDuty organization with permissions to manage incidents.

* Install Port's GitHub integration (required for GitHub Actions implementation):

  * GitHub (Legacy)
  * GitHub (Ocean)

  [Port's GitHub app](https://github.com/apps/getport-io) needs to be installed.

  The [GitHub Ocean integration](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md) needs to be installed.

* [PagerDuty API token](https://support.pagerduty.com/docs/api-access-keys) with permissions to update incidents.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

If you haven't installed the [PagerDuty integration](/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/.md), you'll need to create a blueprint for PagerDuty incidents in Port.<br /><!-- -->However, we highly recommend you install the PagerDuty integration to have these automatically set up for you.

### Create the PagerDuty incident blueprint

PagerDuty Incident Blueprint

Create in Port

```
{
  "identifier": "pagerdutyIncident",
  "description": "This blueprint represents a PagerDuty incident in our software catalog",
  "title": "PagerDuty Incident",
  "icon": "pagerduty",
  "schema": {
    "properties": {
      "status": {
        "type": "string",
        "title": "Incident Status",
        "enum": [
          "triggered",
          "annotated",
          "acknowledged",
          "reassigned",
          "escalated",
          "reopened",
          "resolved"
        ]
      },
      "url": {
        "type": "string",
        "format": "url",
        "title": "Incident URL"
      },
      "urgency": {
        "type": "string",
        "title": "Incident Urgency",
        "enum": ["high", "low"]
      },
      "responder": {
        "type": "string",
        "title": "Assignee"
      },
      "escalation_policy": {
        "type": "string",
        "title": "Escalation Policy"
      },
      "created_at": {
        "title": "Create At",
        "type": "string",
        "format": "date-time"
      },
      "updated_at": {
        "title": "Updated At",
        "type": "string",
        "format": "date-time"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "pagerdutyService": {
      "title": "PagerDuty Service",
      "target": "pagerdutyService",
      "required": false,
      "many": true
    }
  }
}
```

## Implementation[â](#implementation "Direct link to Implementation")

* Synced webhook
* GitHub workflow

You can acknowledge PagerDuty incidents by leveraging Port's **synced webhooks** and **secrets** to directly interact with the PagerDuty's API. This method simplifies the setup by handling everything within Port.

### Add Port secrets

Existing secrets

If you have already installed Port's <!-- -->PagerDuty<!-- --> integration, these secrets should already exist in your portal.<br /><!-- -->To view your existing secrets:

1. Click on the `...` button in the top right corner of your Port application.
2. Choose **Credentials**, then click on the `Secrets` tab.

To add this secret to your portal:

1. Click on the `...` button in the top right corner of your Port application.

2. Click on **Credentials**.

3. Click on the `Secrets` tab.

4. Click on `+ Secret` and add the following secret:

   * `PAGERDUTY_API_KEY` - Your PagerDuty API token

### Set up self-service action

Follow these steps to create the self-service action:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Acknowledge Incident In PagerDuty (Webhook) (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "pagerdutyIncident_acknowledge_incident_webhook",
     "title": "Acknowledge Incident (Webhook)",
     "icon": "pagerduty",
     "description": "Acknowledge incident in PagerDuty using webhook",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "from": {
             "icon": "User",
             "title": "From",
             "description": "User Email",
             "type": "string",
             "format": "user"
           }
         },
         "required": [
           "from"
         ],
         "order": [
           "from"
         ]
       },
       "blueprintIdentifier": "pagerdutyIncident"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.pagerduty.com/incidents",
       "agent": false,
       "synchronized": true,
       "method": "PUT",
       "headers": {
         "Content-Type": "application/json",
         "Accept": "application/vnd.pagerduty+json;version=2",
         "Authorization": "Token token={{.secrets.PAGERDUTY_API_KEY}}",
         "From": "{{.inputs.from}}"
       },
       "body": {
         "incidents": [
           {
             "id": "{{.entity.identifier}}",
             "type": "incident_reference",
             "status": "acknowledged"
           }
         ]
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Acknowledge Incident (Webhook)` action in the self-service page. ð

### Create an automation to upsert entity in port

After each execution of the action, we would like to update the relevant entity in Port with the latest status.

To achieve this, we can create an automation that will be triggered when the action completes successfully.

To create the automation:

1. Head to the [automation](https://app.getport.io/settings/automations) page.

2. Click on the `+ Automation` button.

3. Copy and paste the following JSON configuration into the editor.

   **Update PagerDuty incident in Port automation (Click to expand)**

   Create in Port

   ```
       {
         "identifier": "pagerdutyIncident_sync_status",
         "title": "Sync PagerDuty Incident Status",
         "description": "Update PagerDuty incident data in Port after acknowledgment",
         "trigger": {
           "type": "automation",
           "event": {
             "type": "RUN_UPDATED",
             "actionIdentifier": "pagerdutyIncident_acknowledge_incident_webhook"
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
           "blueprintIdentifier": "pagerdutyIncident",
           "mapping": {
             "identifier": "{{.event.diff.after.entity.identifier}}",
             "title": "{{ .event.diff.after.entity.title }}",
             "properties": {
               "status": "{{.event.diff.after.response.incidents.0.status}}",
               "url": "{{.event.diff.after.response.incidents.0.self}}",
               "urgency": "{{.event.diff.after.response.incidents.0.urgency}}",
               "responder": "{{.event.diff.after.response.incidents.0.assignments.0.assignee.summary}}",
               "escalation_policy": "{{.event.diff.after.response.incidents.0.escalation_policy.summary}}",
               "created_at": "{{.event.diff.after.response.incidents.0.created_at}}",
               "updated_at": "{{.event.diff.after.response.incidents.0.updated_at}}"
             },
             "relations": {
               "{{.event.diff.after.entity.relations.key}}": "{{.event.diff.after.entity.relations.value}}"
             }
           }
         },
         "publish": true
     }
   ```

4. Click `Save`.

Now when you execute the webhook action, the incident data in Port will be automatically updated with the latest information from PagerDuty.

To implement this use-case using a GitHub workflow, follow these steps:

### Add GitHub secrets

In your GitHub repository, [go to **Settings > Secrets**](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) and add the following secrets:

* `PAGERDUTY_API_KEY` - [PagerDuty API token](https://support.pagerduty.com/docs/api-access-keys) generated by the user.
* `PORT_CLIENT_ID` - Your port `client id` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).
* `PORT_CLIENT_SECRET` - Your port `client secret` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).

### Add GitHub workflow

Create the file `.github/workflows/acknowledge-incident.yaml` in the `.github/workflows` folder of your repository.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

**GitHub Workflow (Click to expand)**

acknowledge-incident.yaml

```
name: Acknowledge Incident In PagerDuty
on:
  workflow_dispatch:
    inputs:
      from:
        description: The email address of a valid user associated with the account making the request.
        required: true
        type: string
      port_context:
        required: true
        description: includes blueprint, run ID, and entity identifier from Port.

jobs:
  acknowledge_incident:
    runs-on: ubuntu-latest
    steps:
      - name: Log Executing Request to Acknowledge Incident
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "About to make a request to pagerduty..."

      - name: Request to Acknowledge Incident
        id: acknowledge_incident
        uses: fjogeleit/http-request-action@v1
        with:
          url: 'https://api.pagerduty.com/incidents'
          method: 'PUT'
          customHeaders: '{"Content-Type": "application/json", "Accept": "application/vnd.pagerduty+json;version=2", "Authorization": "Token token=${{ secrets.PAGERDUTY_API_KEY }}", "From": "${{ github.event.inputs.from }}"}'
          data: >-
              {
                "incidents": [
                  {
                    "id": "${{ fromJson(inputs.port_context).entity }}",
                    "type": "incident_reference",
                    "status": "acknowledged"
                  }
                ]
              }

      - name: Log Acknowledge Incident Request Failure 
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Request to acknowledge incident failed ..."

      - name: Log Before Upserting Entity
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Reporting the updated incident back to port ..."

      - name: UPSERT Entity
        uses: port-labs/port-github-action@v1
        with:
          identifier: "${{ fromJson(steps.acknowledge_incident.outputs.response).incidents[0].id }}"
          title: "${{ fromJson(steps.acknowledge_incident.outputs.response).incidents[0].title }}"
          blueprint: ${{fromJson(inputs.port_context).blueprint}}
          properties: |-
            {
              "status": "${{ fromJson(steps.acknowledge_incident.outputs.response).incidents[0].status }}",
              "url": "${{ fromJson(steps.acknowledge_incident.outputs.response).incidents[0].self }}",
              "urgency": "${{ fromJson(steps.acknowledge_incident.outputs.response).incidents[0].urgency }}",
              "responder": "${{ fromJson(steps.acknowledge_incident.outputs.response).incidents[0].assignments[0].assignee.summary}}",
              "escalation_policy": "${{ fromJson(steps.acknowledge_incident.outputs.response).incidents[0].escalation_policy.summary }}",
              "created_at": "${{ fromJson(steps.acknowledge_incident.outputs.response).incidents[0].created_at }}",
              "updated_at": "${{ fromJson(steps.acknowledge_incident.outputs.response).incidents[0].updated_at }}"
            }
          relations: "${{ toJson(fromJson(inputs.port_context).relations) }}"
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: UPSERT
          runId: ${{fromJson(inputs.port_context).run_id}}

      - name: Log Upsert Entity Failure 
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Failed to upsert pagerduty incident to port ..."

      - name: Log After Upserting Entity
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Entity upserting was successful â"
```

### Set up self-service action

We will create a self-service action to handle acknowledging incidents in PagerDuty. To create a self-service action follow these steps:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Acknowledge Incident In PagerDuty (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   * GitHub (Legacy)
   * GitHub (Ocean)

   Create in Port

   ```
   {
     "identifier": "pagerdutyIncident_acknowledge_incident",
     "title": "Acknowledge Incident",
     "icon": "pagerduty",
     "description": "Acknowledge incident in PagerDuty",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "from": {
             "icon": "User",
             "title": "From",
             "description": "User Email",
             "type": "string",
             "format": "user"
           }
         },
         "required": [
           "from"
         ],
         "order": [
           "from"
         ]
       },
       "blueprintIdentifier": "pagerdutyIncident"
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB_ORG>",
       "repo": "<GITHUB_REPO>",
       "workflow": "acknowledge-incident.yaml",
       "workflowInputs": {
         "from": "{{.inputs.\"from\"}}",
         "port_context": {
           "blueprint": "{{.action.blueprint}}",
           "entity": "{{.entity.identifier}}",
           "run_id": "{{.run.id}}",
           "relations": "{{.entity.Relations}}"
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
     "identifier": "pagerdutyIncident_acknowledge_incident",
     "title": "Acknowledge Incident",
     "icon": "pagerduty",
     "description": "Acknowledge incident in PagerDuty",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "from": {
             "icon": "User",
             "title": "From",
             "description": "User Email",
             "type": "string",
             "format": "user"
           }
         },
         "required": [
           "from"
         ],
         "order": [
           "from"
         ]
       },
       "blueprintIdentifier": "pagerdutyIncident"
     },
     "invocationMethod": {
       "type": "INTEGRATION_ACTION",
       "installationId": "<GITHUB_OCEAN_INSTALLATION_ID>",
       "integrationActionType": "dispatch_workflow",
       "org": "<GITHUB_ORG>",
       "repo": "<GITHUB_REPO>",
       "workflow": "acknowledge-incident.yaml",
       "workflowInputs": {
         "from": "{{.inputs.\"from\"}}",
         "port_context": {
           "blueprint": "{{.action.blueprint}}",
           "entity": "{{.entity.identifier}}",
           "run_id": "{{.run.id}}",
           "relations": "{{.entity.Relations}}"
         }
       },
       "reportWorkflowStatus": true
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Acknowledge Incident` action in the self-service page. ð

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Head to the [self-service page](https://app.getport.io/self-serve) of your portal

2. Click on the `Acknowledge Incident (Webhook)` action

3. Choose the PagerDuty incident you want to acknowledge (In case you didn't install the [PagerDuty integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty), it means you don't have any PagerDuty incidents in Port yet, so you will need to create one manually in Port to test this action)

4. Enter the email address of a valid user associated with the account making the request

5. Click on `Execute`

6. Wait for the incident's status to be changed in PagerDuty

7. Verify that the entity in Port has been updated with the new status

## More Self Service PagerDuty Actions Examples[â](#more-self-service-pagerduty-actions-examples "Direct link to More Self Service PagerDuty Actions Examples")

* [Change On-Call User](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-on-call-user)
* [Change PagerDuty incident owner](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-pagerduty-incident-owner)
* [Create PagerDuty incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/interact-with-pagerduty-incidents)
* [Create PagerDuty service](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/create-pagerduty-service)
* [Escalate an incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/escalate-an-incident)
* [Resolve an incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/resolve-incident)
* [Trigger PagerDuty incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/interact-with-pagerduty-incidents)

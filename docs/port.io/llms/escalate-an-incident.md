# Source: https://docs.port.io/guides/all/escalate-an-incident.md

# Escalate an Incident in PagerDuty

## Overview[â](#overview "Direct link to Overview")

This guide will help you implement a self-service action in Port that allows you to escalate PagerDuty incidents directly from Port. This functionality streamlines incident management by enabling users to escalate incidents without leaving Port.

You can implement this action in two ways:

1. **GitHub workflow**: A more flexible approach that allows for complex workflows and custom logic, suitable for teams that want to maintain their automation in Git.
2. **Synced webhooks**: A simpler approach that directly interacts with PagerDuty's API through Port, ideal for quick implementation and minimal setup.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).

* Access to your PagerDuty organization with permissions to manage incidents.

* Optional - Install Port's PagerDuty integration [learn more](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty)

  PagerDuty Integration

  This step is not required for this example, but it will create all the blueprint boilerplate for you, and also ingest and update the catalog in real time with your PagerDuty Incidents.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

If you haven't installed the PagerDuty integration, you'll need to create blueprints for PagerDuty incidents and PagerDuty services. However, we highly recommend you install the PagerDuty integration to have these automatically set up for you.

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

You can escalate PagerDuty incidents by leveraging Port's **synced webhooks** and **secrets** to directly interact with the PagerDuty's API. This method simplifies the setup by handling everything within Port.

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

We will create a self-service action to handle escalating PagerDuty incidents using webhooks. To create a self-service action follow these steps:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   Escalation Policy ID

   The escalation policy ID is a unique identifier (e.g., P7LVMYP) that you can find in your PagerDuty dashboard:

   * Go to Configuration â Escalation Policies
   * Click on the policy you want to use
   * The ID is the last part of the URL (e.g., in <https://example-subdomain.pagerduty.com/escalation_policies/P7LVMYP>, the ID is P7LVMYP)

   **Escalate PagerDuty Incident (Webhook) (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "escalate_incident_webhook",
     "title": "Escalate Incident (Webhook)",
     "icon": "pagerduty",
     "description": "Escalate a PagerDuty incident",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "escalation_policy_id": {
             "title": "Escalation Policy ID",
             "description": "PagerDuty Escalation Policy ID (e.g., P7LVMYP)",
             "icon": "pagerduty",
             "type": "string"
           },
           "urgency": {
             "icon": "pagerduty",
             "title": "Urgency",
             "description": "New urgency level for the incident",
             "type": "string",
             "default": "low",
             "enum": [
               "high",
               "low"
             ],
             "enumColors": {
               "high": "orange",
               "low": "lightGray"
             }
           },
           "from": {
             "icon": "User",
             "title": "From",
             "description": "The email address of a valid PagerDuty user associated with the account making the request.",
             "type": "string",
             "format": "user",
             "default": {
               "jqQuery": ".user.email"
             }
           }
         },
         "required": [
           "escalation_policy_id",
           "urgency",
           "from"
         ],
         "order": [
           "escalation_policy_id",
           "urgency",
           "from"
         ]
       },
       "blueprintIdentifier": "pagerdutyIncident"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.pagerduty.com/incidents/{{.entity.identifier}}",
       "agent": false,
       "synchronized": true,
       "method": "PUT",
       "headers": {
         "Authorization": "Token token={{.secrets.PAGERDUTY_API_TOKEN}}",
         "Accept": "application/vnd.pagerduty+json;version=2",
         "From": "{{.inputs.from}}",
         "Content-Type": "application/json"
       },
       "body": {
         "incident": {
           "type": "incident_reference",
           "escalation_policy": {
             "id": "{{.inputs.escalation_policy_id}}",
             "type": "escalation_policy_reference"
           },
           "urgency": "{{.inputs.urgency}}"
         }
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Escalate Incident (Webhook)` action in the self-service page. ð

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
         "description": "Update PagerDuty incident data in Port after escalation",
         "trigger": {
           "type": "automation",
           "event": {
             "type": "RUN_UPDATED",
             "actionIdentifier": "escalate_incident_webhook"
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
             "identifier": "{{.event.diff.after.response.incident.id}}",
             "title": "{{.event.diff.after.response.incident.title}}",
             "properties": {
               "status": "{{.event.diff.after.response.incident.status}}",
               "url": "{{.event.diff.after.response.incident.self}}",
               "urgency": "{{.event.diff.after.response.incident.urgency}}",
               "responder": "{{.event.diff.after.response.incident.assignments.0.assignee.summary}}",
               "escalation_policy": "{{.event.diff.after.response.incident.escalation_policy.summary}}",
               "created_at": "{{.event.diff.after.response.incident.created_at}}",
               "updated_at": "{{.event.diff.after.response.incident.updated_at}}"
             },
             "relations": {
               "pagerdutyService": ["{{.event.diff.after.response.incident.service.id}}"]
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

* `PAGERDUTY_API_KEY` - [PagerDuty API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account) generated by the user.
* `PORT_CLIENT_ID` - Your port `client id` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).
* `PORT_CLIENT_SECRET` - Your port `client secret` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).

### Add GitHub workflow

Create the file `.github/workflows/escalate-incident.yaml` in the `.github/workflows` folder of your repository.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

**GitHub Workflow (Click to expand)**

```
name: Escalate PagerDuty Incident

on:
  workflow_dispatch:
    inputs:
      escalation_policy_id:
        description: PagerDuty Escalation Policy ID to apply
        required: true
        type: string
      urgency:
        description: New urgency level for the incident (e.g., "high")
        required: false
        type: string
      from:
        description: The email address of a valid user associated with the account making the request.
        required: true
        type: string
      port_context:
        required: true
        description: includes blueprint, run ID, and entity identifier from Port.

jobs:
  escalate-incident:
    runs-on: ubuntu-latest
    steps:
      - name: Inform execution of request to escalate incident
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "About to escalate incident in PagerDuty..."

      - name: Escalate Incident in PagerDuty
        id: escalate_incident
        uses: fjogeleit/http-request-action@v1
        with:
          url: 'https://api.pagerduty.com/incidents/${{fromJson(inputs.port_context).entity}}'
          method: 'PUT'
          customHeaders: '{"Content-Type": "application/json", "Accept": "application/vnd.pagerduty+json;version=2", "Authorization": "Token token=${{ secrets.PAGERDUTY_API_KEY }}", "From": "${{ github.event.inputs.from }}"}'
          data: >-
            {
              "incident": {
                "type": "incident_reference",
                "escalation_policy": {
                  "id": "${{ github.event.inputs.escalation_policy_id }}",
                  "type": "escalation_policy_reference"
                },
                "urgency": "${{ github.event.inputs.urgency }}"
              }
            }

      - name: Inform PagerDuty request failure
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Request to escalate incident failed ..."

      - name: Inform ingestion of PagerDuty escalation to Port
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Reporting the escalated incident back to Port ..."

      - name: Upsert pagerduty entity to Port 
        id: upsert_entity
        uses: port-labs/port-github-action@v1
        with:
          identifier: ${{inputs.entity_identifier}}
          title: "${{ fromJson(steps.escalate_incident.outputs.response).incident.title }}"
          blueprint: "pagerdutyIncident"
          properties: |-
            {
              "status": "${{ fromJson(steps.escalate_incident.outputs.response).incident.status }}",
              "url": "${{ fromJson(steps.escalate_incident.outputs.response).incident.self }}",
              "urgency": "${{ fromJson(steps.escalate_incident.outputs.response).incident.urgency }}",
              "responder": "${{ fromJson(steps.escalate_incident.outputs.response).incident.assignments[0].assignee.summary}}",
              "escalation_policy": "${{ fromJson(steps.escalate_incident.outputs.response).incident.escalation_policy.summary }}",
              "created_at": "${{ fromJson(steps.escalate_incident.outputs.response).incident.created_at }}",
              "updated_at": "${{ fromJson(steps.escalate_incident.outputs.response).incident.updated_at }}"
            }
          relations: "${{ toJson(fromJson(inputs.port_context).relations) }}"
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: UPSERT
          runId: ${{fromJson(inputs.port_context).run_id}}

      - name: Inform Entity upsert failure
        if: steps.upsert_entity.outcome == 'failure'
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Failed to report the escalated incident back to Port ..."

      - name: Inform completion of PagerDuty incident escalation
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{fromJson(inputs.port_context).run_id}}
          logMessage: "Incident escalation process was successful â"
```

### Set up self-service action

We will create a self-service action to handle escalating PagerDuty incidents. To create a self-service action follow these steps:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Escalate PagerDuty Incident (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   Create in Port

   ```
   {
     "identifier": "pagerdutyIncident_escalate_incident",
     "title": "Escalate Incident",
     "icon": "pagerduty",
     "description": "Escalate a pagerduty incident",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "escalation_policy_id": {
             "title": "Escalation Policy ID",
             "description": "PagerDuty Escalation Policy ID to apply",
             "icon": "pagerduty",
             "type": "string"
           },
           "urgency": {
             "icon": "pagerduty",
             "title": "Urgency",
             "description": "New urgency level for the incident (e.g., \"high\")",
             "type": "string",
             "default": "low",
             "enum": [
               "high",
               "low"
             ],
             "enumColors": {
               "high": "orange",
               "low": "lightGray"
             }
           },
           "from": {
             "icon": "User",
             "title": "From",
             "description": "The email address of a valid pagerduty user associated with the account making the request.",
             "type": "string",
             "format": "user"
           }
         },
         "required": [
           "escalation_policy_id",
           "urgency",
           "from"
         ],
         "order": [
           "escalation_policy_id",
           "urgency",
           "from"
         ]
       },
       "blueprintIdentifier": "pagerdutyIncident"
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB_ORG>",
       "repo": "<GITHUB_REPO>",
       "workflow": "escalate-incident.yaml",
       "workflowInputs": {
         "escalation_policy_id": "{{.inputs.\"escalation_policy_id\"}}",
         "urgency": "{{.inputs.\"urgency\"}}",
         "from": "{{.inputs.\"from\"}}",
         "port_context": {
           "blueprint": "{{.action.blueprint}}",
           "entity": "{{.entity.identifier}}",
           "run_id": "{{.run.id}}",
           "relations": "{{.entity.relations}}"
         }
       },
       "reportWorkflowStatus": true
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Escalate Incident` action in the self-service page. ð

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Head to the [self-service page](https://app.getport.io/self-serve) of your portal

2. Choose either the GitHub workflow or webhook implementation:

   * For GitHub workflow: Click on `Escalate Incident`
   * For webhook: Click on `Escalate Incident (Webhook)`

3. Select the PagerDuty incident you want to escalate

4. Enter the required information:

   * Escalation Policy ID
   * Urgency level (high/low)
   * From (email address of a valid PagerDuty user)

5. Click on `Execute`

6. Done! Wait for the incident to be escalated in PagerDuty

## More Self Service PagerDuty Actions Examples[â](#more-self-service-pagerduty-actions-examples "Direct link to More Self Service PagerDuty Actions Examples")

* [Acknowledge Incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/acknowledge-incident)
* [Change On-Call User](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-on-call-user)
* [Change PagerDuty incident owner](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-pagerduty-incident-owner)
* [Create PagerDuty incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/interact-with-pagerduty-incidents)
* [Create PagerDuty service](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/create-pagerduty-service)
* [Resolve an incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/resolve-incident)
* [Trigger PagerDuty incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/interact-with-pagerduty-incidents)

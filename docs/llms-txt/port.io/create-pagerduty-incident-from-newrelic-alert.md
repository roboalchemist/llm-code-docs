# Source: https://docs.port.io/guides/all/create-pagerduty-incident-from-newrelic-alert.md

# Create a PagerDuty incident from a New Relic alert

## Overview[â](#overview "Direct link to Overview")

This guide demonstrates how to implement a self-service action in Port that allows you to create **PagerDuty incidents** from a **New Relic alert**.

We will create **PagerDuty incidents** with **New Relic alert** context like APM metrics, service relationships, and automatic service mapping based on your software catalog.

This implementation leverages the relationships between **New Relic alerts** and **PagerDuty services** to provide enhanced incident context. The system automatically correlates monitoring data (APM metrics, error rates, throughput) with service ownership and on-call information, enabling incident creation with pre-populated service mappings, alert details, and proper routing based on established tool relationships.

This approach ensures that incidents are created with the right context and routing, making it easier to triage and resolve issues.

You can implement this action in two ways:

1. **Synced webhooks**: A simpler approach that directly interacts with PagerDuty's API through Port, ideal for quick implementation and minimal setup.
2. **GitHub workflow**: A more flexible approach that allows for complex workflows and custom logic, suitable for teams that want to maintain their automation in Git.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).
* Access to your PagerDuty organization with permissions to manage incidents.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

If you have installed Port's [PagerDuty integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/) and [New Relic integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/apm-alerting/newrelic), the relevant blueprints will be automatically created in your portal.

If you chose not to install the integrations, you will need to create the blueprints manually:

### Create the PagerDuty service blueprint[â](#create-the-pagerduty-service-blueprint "Direct link to Create the PagerDuty service blueprint")

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

### Create the PagerDuty incident blueprint[â](#create-the-pagerduty-incident-blueprint "Direct link to Create the PagerDuty incident blueprint")

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add this JSON schema:

   **PagerDuty Incident Blueprint (Click to expand)**

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

5. Click "Save" to create the blueprint.

### Create the New Relic alert blueprint[â](#create-the-new-relic-alert-blueprint "Direct link to Create the New Relic alert blueprint")

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add this JSON schema:

   **New Relic alert Blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "newRelicAlert",
     "description": "This blueprint represents a New Relic alert in our software catalog",
     "title": "New Relic Alert",
     "icon": "NewRelic",
     "ownership": {
       "type": "Inherited",
       "title": "Owning Teams",
       "path": "alert_to_workload.service"
     },
     "schema": {
       "properties": {
         "priority": {
           "type": "string",
           "title": "Priority",
           "enum": [
             "CRITICAL",
             "HIGH",
             "MEDIUM",
             "LOW"
           ],
           "enumColors": {
             "CRITICAL": "red",
             "HIGH": "red",
             "MEDIUM": "yellow",
             "LOW": "green"
           }
         },
         "state": {
           "type": "string",
           "title": "State",
           "enum": [
             "ACTIVATED",
             "CLOSED",
             "CREATED"
           ],
           "enumColors": {
             "ACTIVATED": "yellow",
             "CLOSED": "green",
             "CREATED": "lightGray"
           }
         },
         "sources": {
           "type": "array",
           "items": {
             "type": "string"
           },
           "title": "Sources"
         },
         "alertPolicyNames": {
           "type": "array",
           "items": {
             "type": "string"
           },
           "title": "Alert Policy Names"
         },
         "conditionName": {
           "type": "array",
           "items": {
             "type": "string"
           },
           "title": "Condition Name"
         },
         "link": {
           "type": "string",
           "title": "Link",
           "format": "url"
         },
         "description": {
           "type": "string",
           "title": "Description"
         },
         "activatedAt": {
           "type": "string",
           "title": "Activated at",
           "format": "date-time"
         }
       },
       "required": []
     },
     "mirrorProperties": {
       "cloud_resource_name": {
         "title": "Cloud Resource",
         "path": "cloud_resource.$title"
       },
       "port_service": {
         "title": "Service",
         "path": "alert_to_workload.service.$title"
       },
       "team": {
         "title": "Team",
         "path": "alert_to_workload.service.$team"
       },
       "workload_name": {
         "title": "Workload name",
         "path": "alert_to_workload.$title"
       },
       "pager_duty_service": {
         "title": "Pager duty service",
         "path": "alert_to_workload.service.pager_duty_service.$identifier"
       }
     },
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "alert_to_workload": {
         "title": "Workload",
         "target": "workload",
         "required": false,
         "many": false
       },
       "cloud_resource": {
         "title": "Cloud resource",
         "target": "newRelicCloudResource",
         "required": false,
         "many": false
       }
     }
   }
   ```

5. Click "Save" to create the blueprint.

## Implementation[â](#implementation "Direct link to Implementation")

* Synced webhook
* GitHub workflow

You can create PagerDuty incidents by leveraging Port's **synced webhooks** and **secrets** to directly interact with the PagerDuty's API. This method simplifies the setup by handling everything within Port.

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

We will create a self-service action to handle creating PagerDuty incidents from New Relic alerts using webhooks. To create a self-service action follow these steps:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Create PagerDuty incident from New Relic alert (Webhook) (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "create_pagerduty_incident_from_newrelic_alert",
     "title": "Create Pagerduty incident from New Relic alert (Webhook)",
     "icon": "pagerduty",
     "description": "create an incident in PagerDuty that will alert the on-call to an issue created by New Relic alert",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "service": {
             "type": "string",
             "blueprint": "service",
             "title": "Select a service",
             "format": "entity",
             "dataset": {
               "combinator": "and",
               "rules": [
                 {
                   "property": "pagerdutyServiceId",
                   "operator": "isNotEmpty"
                 }
               ]
             },
             "default": {
               "jqQuery": ".entity.properties.port_service"
             }
           }
         },
         "required": [
           "service"
         ],
         "order": []
       },
       "blueprintIdentifier": "newRelicAlert"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.pagerduty.com/incidents",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "RUN_ID": "{{ .run.id }}",
         "Authorization": "Bearer {{ .secrets.__PAGERDUTY_PAGERDUTY_TOKEN }}",
         "Accept": "application/vnd.pagerduty+json;version=2",
         "Content-Type": "application/json",
         "From": "{{ .trigger.by.user.email }}"
       },
       "body": {
         "incident": {
           "type": "incident",
           "title": "{{ .entity.title }}",
           "service": {
             "id": "{{ .inputs.service.properties.pagerdutyServiceId}}",
             "type": "service_reference"
           },
           "urgency": "high",
           "body": {
             "type": "incident_body",
             "details": "{{ .entity.properties.description }} \n New Relic link: {{ .entity.properties.link }}"
           }
         }
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Create Pagerduty incident from New Relic alert (Webhook)` action in the self-service page. ð

To implement this use-case using a GitHub workflow, follow these steps:

### Add GitHub secrets

In your GitHub repository, [go to **Settings > Secrets**](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) and add the following secrets:

* `PAGERDUTY_API_KEY` - [PagerDuty API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account) generated by the user.
* `PORT_CLIENT_ID` - Your port `client id` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).
* `PORT_CLIENT_SECRET` - Your port `client secret` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).

### Add GitHub workflow

Create the file `.github/workflows/create-pagerduty-incident.yaml` in the `.github/workflows` folder of your repository.

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

**GitHub Workflow (Click to expand)**

```
name: Create PagerDuty Incident


on:
  workflow_dispatch:
    inputs:
      title:
        description: The title of the incident to create
        required: true
        type: string
      extra_details:
        description: Extra details about the incident to create
        required: false
      urgency:
        description: The urgency of the incident
        required: false
      from:
        description: The email address of a valid user associated with the account making the request.
        required: true
      service:
        required: true
        type: string
      port_context:
        required: true
        description: includes blueprint, run ID, and entity identifier from Port.
jobs: 
  trigger:
    runs-on: ubuntu-latest
    steps:
      - uses: port-labs/pagerduty-incident-gha@v1
        with:
          portClientId: ${{ secrets.PORT_CLIENT_ID }}
          portClientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          token: ${{ secrets.PAGERDUTY_API_KEY }}
          portRunId: ${{fromJson(inputs.port_context).run_id}}
          incidentTitle: "${{ inputs.title }}"
          extraDetails: "${{ inputs.extra_details }}"
          urgency: "${{ inputs.urgency }}"
          actorEmail: "${{ inputs.from }}"
          service: "${{ inputs.service }}"
          blueprintIdentifier: 'pagerdutyIncident'
```

### Set up self-service action

We will create a self-service action to handle creating PagerDuty incidents. To create a self-service action follow these steps:

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Create PagerDuty Incident (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   Create in Port

   ```
   {
     "identifier": "create_pagerduty_incident_from_newrelic_alert_github",
     "title": "Create Pagerduty incident from New Relic alert (GitHub)",
     "icon": "pagerduty",
     "description": "Create an incident in PagerDuty that will alert the on-call to an issue created by New Relic alert",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "service": {
             "type": "string",
             "blueprint": "service",
             "title": "Select a service",
             "format": "entity",
             "dataset": {
               "combinator": "and",
               "rules": [
                 {
                   "property": "pagerdutyServiceId",
                   "operator": "isNotEmpty"
                 }
               ]
             },
             "default": {
               "jqQuery": ".entity.properties.port_service"
             }
           }
         },
         "required": [
           "service"
         ],
         "order": []
       },
       "blueprintIdentifier": "newRelicAlert"
     },
     "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB_ORG>",
       "repo": "<GITHUB_REPO>",
       "workflow": "create-pagerduty-incident.yaml",
       "workflowInputs": {
         "title": "{{ .entity.title }}",
         "extra_details": "{{ .entity.properties.description }} \n New Relic link: {{ .entity.properties.link }}",
         "urgency": "high",
         "from": "{{ .trigger.by.user.email }}",
         "service": "{{ .inputs.service.properties.pagerdutyServiceId}}",
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

Now you should see the `Create Pagerduty incident from New Relic alert (GitHub)` action in the self-service page. ð

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Head to the [self-service page](https://app.getport.io/self-serve) of your portal

2. Choose either the GitHub workflow or webhook implementation:

   * For GitHub workflow: Click on `Create Pagerduty incident from New Relic alert (GitHub)`
   * For webhook: Click on `Create Pagerduty incident from New Relic alert (Webhook)`

3. Select the New Relic alert that you want to trigger the incident from

4. Select the related service for the incident (only services that are connected to a pager duty service are displayed)

5. Click on `Execute`

6. Done! Wait for the incident to be created in PagerDuty

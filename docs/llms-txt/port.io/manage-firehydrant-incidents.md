# Source: https://docs.port.io/guides/all/manage-firehydrant-incidents.md

# Manage FireHydrant incidents

This guide demonstrates how to implement self-service actions that create new FireHydrant incidents or trigger incidents on services directly from Port using synced webhooks or GitHub workflows.

## Use cases[â](#use-cases "Direct link to Use cases")

* Create FireHydrant incidents from Port with name, priority, and description.
* Trigger incidents against FireHydrant services with a chosen condition (Unavailable, Degraded, Bug, Operational).
* Keep your Port catalog in sync by automatically upserting the created incident or updating related service data after execution.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).
* Access to your FireHydrant organization with permissions to manage incidents.
* Optional â Install Port's [FireHydrant integration](/build-your-software-catalog/sync-data-to-catalog/incident-management/firehydrant.md).

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

If you haven't installed the FireHydrant integration, you will need to manually create blueprints for FireHydrant incidents and services. We highly recommend installing the integration to have these resources automatically set up for you.

### Create the FireHydrant incident blueprint

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add this JSON schema:

   **FireHydrant Incident Blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "firehydrantIncident",
     "description": "This blueprint represents a firehydrant incident",
     "title": "FireHydrant Incident",
     "icon": "FireHydrant",
     "schema": {
       "properties": {
         "url": {
           "type": "string",
           "title": "Incident URL",
           "format": "url",
           "description": "the link to the incident"
         },
         "priority": {
           "title": "Priority",
           "type": "string",
           "enum": ["P1", "P2", "P3", "P4"],
           "enumColors": {
             "P1": "red",
             "P2": "red",
             "P3": "orange",
             "P4": "orange"
           }
         },
         "severity": {
           "title": "Severity",
           "type": "string"
         },
         "tags": {
           "title": "Tags",
           "items": { "type": "string" },
           "type": "array"
         },
         "currentMilestone": {
           "type": "string",
           "title": "Current Milestone",
           "default": "started",
           "enum": [
             "started",
             "detected",
             "acknowledged",
             "investigating",
             "identified",
             "mitigated",
             "resolved",
             "postmortem_started",
             "postmortem_completed",
             "closed"
           ],
           "enumColors": {
             "started": "red",
             "detected": "red",
             "acknowledged": "orange",
             "investigating": "yellow",
             "identified": "yellow",
             "mitigated": "green",
             "resolved": "green",
             "postmortem_started": "purple",
             "postmortem_completed": "blue",
             "closed": "green"
           }
         },
         "functionalities": {
           "title": "Functionalities Impacted",
           "items": { "type": "string" },
           "type": "array"
         },
         "customerImpact": {
           "title": "Customers Impacted",
           "type": "string"
         },
         "createdBy": {
           "title": "Created By",
           "type": "string"
         },
         "createdAt": {
           "title": "Created At",
           "type": "string",
           "format": "date-time"
         },
         "description": {
           "title": "Description",
           "type": "string"
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

### Create the FireHydrant service blueprint

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add this JSON schema:

   **FireHydrant Service Blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "firehydrantService",
     "description": "This blueprint represents a FireHydrant service in our software catalog",
     "title": "FireHydrant Service",
     "icon": "FireHydrant",
     "schema": {
       "properties": {
         "name": {
           "title": "Name",
           "description": "The name of the service in FireHydrant",
           "type": "string"
         },
         "description": {
           "title": "Description",
           "description": "Description of the service",
           "type": "string"
         },
         "status": {
           "title": "Status",
           "description": "Current status of the service",
           "type": "string"
         }
       }
     },
     "calculationProperties": {},
     "relations": {}
   }
   ```

5. Click "Save" to create the blueprint.

### Update the service blueprint

Add a relation to your service blueprint to link it with FireHydrant services:

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Find your service blueprint and click on it.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Add the following relation to the `relations` object:

   ```
   {
     "relations": {
       "fh_service": {
         "title": "FireHydrant Service",
         "target": "firehydrantService",
         "required": false,
         "many": false
       }
     }
   }
   ```

5. Click "Save" to update the blueprint.

## Get FireHydrant Condition IDs[â](#get-firehydrant-condition-ids "Direct link to Get FireHydrant Condition IDs")

If you plan to trigger incidents on services, you will need the condition IDs that are specific to your FireHydrant organization. Retrieve them with the FireHydrant API:

```
curl -X GET "https://api.firehydrant.io/v1/severity_matrix/conditions" \
     -H "Authorization: YOUR_FIREHYDRANT_API_KEY" \
     -H "accept: application/json"
```

Example response:

```
{
  "data": [
    { "id": "b1fc9184-b3f3-4af1-a111-68abcad9bf34", "name": "Unavailable", "position": 0 },
    { "id": "465a5b4c-6f95-4707-a777-ab4bb8def27d", "name": "Degraded", "position": 1 },
    { "id": "c2bc11e8-7fcc-428d-9007-26f00700834a", "name": "Bug", "position": 2 },
    { "id": "9a2a8dbb-6b4e-4189-aca1-e2bb73b9c50b", "name": "Operational", "position": 3 }
  ]
}
```

Use your own IDs in the configurations below.

## Implementation[â](#implementation "Direct link to Implementation")

* Synced webhook
* GitHub workflow

Configure two self-service actions using Port's synced webhooks and secrets to interact directly with FireHydrant's API.

### Add Port secrets

Existing secrets

If you have already installed Port's <!-- -->FireHydrant<!-- --> integration, these secrets should already exist in your portal.<br /><!-- -->To view your existing secrets:

1. Click on the `...` button in the top right corner of your Port application.
2. Choose **Credentials**, then click on the `Secrets` tab.

To add these secrets to your portal:

1. Click on the `...` button in the top right corner of your Port application.

2. Click on **Credentials**.

3. Click on the `Secrets` tab.

4. Click on `+ Secret` and add the following secrets:

   * `FIREHYDRANT_API_KEY`: Your [FireHydrant API key](https://docs.firehydrant.com/docs/api-keys).

### Set up self-service actions

#### Create a FireHydrant incident

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Create FireHydrant Incident (Webhook) (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "create_firehydrant_incident_webhook",
     "title": "Create FireHydrant Incident (Webhook)",
     "icon": "FireHydrant",
     "description": "Create a new FireHydrant incident",
     "trigger": {
       "type": "self-service",
       "operation": "CREATE",
       "userInputs": {
         "properties": {
           "name": {
             "type": "string",
             "title": "Name",
             "description": "The name or title of the incident"
           },
           "priority": {
             "icon": "DefaultProperty",
             "title": "Priority",
             "type": "string",
             "enum": ["P1", "P2", "P3", "P4"],
             "enumColors": {
               "P1": "red",
               "P2": "orange",
               "P3": "blue",
               "P4": "darkGray"
             }
           },
           "description": {
             "type": "string",
             "title": "Description",
             "description": "Detailed description about the incident"
           }
         },
         "required": [],
         "order": ["name", "description", "priority"]
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.firehydrant.io/v1/incidents",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Authorization": "{{.secrets.FIREHYDRANT_API_KEY}}",
         "Content-Type": "application/json"
       },
       "body": {
         "name": "{{.inputs.name}}",
         "priority": "{{.inputs.priority}}",
         "description": "{{.inputs.description}}"
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

#### Trigger a FireHydrant incident

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Trigger FireHydrant Incident (Webhook) (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "trigger_an_incident",
     "title": "Trigger an incident",
     "icon": "FireHydrant",
     "description": "Trigger an incident to a FireHydrant service",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "name": {
             "icon": "DefaultProperty",
             "type": "string",
             "title": "Incident name"
           },
           "condition": {
             "icon": "DefaultProperty",
             "title": "Service status",
             "type": "string",
             "enum": ["Unavailable", "Degraded", "Bug", "Operational"],
             "enumColors": {
               "Unavailable": "lightGray",
               "Degraded": "lightGray",
               "Bug": "lightGray",
               "Operational": "lightGray"
             }
           },
           "incident_description": {
             "type": "string",
             "title": "Incident description"
           }
         },
         "required": ["name", "condition"],
         "order": ["name", "condition", "incident_description"]
       },
       "blueprintIdentifier": "service"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.firehydrant.io/v1/incidents",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "RUN_ID": "{{ .run.id }}",
         "Authorization": "{{ .secrets.FIREHYDRANT_API_KEY }}",
         "content-type": "application/json",
         "accept": "application/json"
       },
       "body": {
         "impacts": [
           {
             "type": "service",
             "id": "{{ .entity.relations.fh_service }}",
             "condition_id": "{{ if .inputs.condition == \"Unavailable\" then \"b1fc9184-b3f3-4af1-a111-68abcad9bf34\" elif .inputs.condition == \"Degraded\" then \"465a5b4c-6f95-4707-a777-ab4bb8def27d\" elif .inputs.condition == \"Bug\" then \"c2bc11e8-7fcc-428d-9007-26f00700834a\" elif .inputs.condition == \"Operational\" then \"9a2a8dbb-6b4e-4189-aca1-e2bb73b9c50b\" else null end }}"
           }
         ],
         "name": "{{ .inputs.name }}",
         "description": "{{ .inputs.incident_description }}"
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

### Set up automations

#### Sync FireHydrant incident after creation

1. Head to the [Automations](https://app.getport.io/automations) page.

2. Click on the `+ New Automation` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Sync FireHydrant incident after creation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "firehydrant_incident_sync_status",
     "title": "Sync FireHydrant Incident Status",
     "description": "Update FireHydrant incident data in Port after creation",
     "trigger": {
       "type": "automation",
       "event": { "type": "RUN_UPDATED", "actionIdentifier": "create_firehydrant_incident_webhook" },
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
       "blueprintIdentifier": "firehydrantIncident",
       "mapping": {
         "identifier": "{{.event.diff.after.response.id}}",
         "title": "{{.event.diff.after.response.name}}",
         "properties": {
           "url": "{{.event.diff.after.response.incident_url}}",
           "priority": "{{.event.diff.after.response.priority}}",
           "severity": "{{.event.diff.after.response.severity}}",
           "tags": "{{.event.diff.after.response.tag_list}}",
           "currentMilestone": "{{.event.diff.after.response.current_milestone}}",
           "description": "{{.event.diff.after.response.description}}",
           "customerImpact": "{{.event.diff.after.response.customers_impacted}}",
           "createdBy": "{{.event.diff.after.response.created_by.name}}",
           "createdAt": "{{.event.diff.after.response.created_at}}"
         },
         "relations": {}
       }
     },
     "publish": true
   }
   ```

5. Click `Save`.

#### Sync FireHydrant service after trigger

1. Head to the [Automations](https://app.getport.io/automations) page.

2. Click on the `+ New Automation` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Sync FireHydrant service after trigger (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "firehydrantIncident_sync_after_trigger",
     "title": "Sync FireHydrant Incident After Trigger",
     "description": "Update FireHydrant service data in Port after triggering an incident",
     "trigger": {
       "type": "automation",
       "event": { "type": "RUN_UPDATED", "actionIdentifier": "trigger_an_incident" },
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
       "blueprintIdentifier": "firehydrantService",
       "mapping": {
         "identifier": "{{.event.diff.after.response.id}}",
         "title": "{{.event.diff.after.response.name}}",
         "properties": {
           "name": "{{.event.diff.after.response.name}}",
           "description": "{{.event.diff.after.response.description}}",
           "status": "{{.event.diff.after.response.status}}"
         }
       }
     },
     "publish": true
   }
   ```

5. Click `Save`.

To implement this use-case using GitHub, configure two workflows and corresponding self-service actions.

### Add GitHub secrets

In your GitHub repository, go to Settings â Secrets and add:

* `FIREHYDRANT_API_KEY` â Your FireHydrant API key. See [FireHydrant docs](https://docs.firehydrant.com/docs/api-keys) for generating an API key.
* `PORT_CLIENT_ID` â Your Port client id.
* `PORT_CLIENT_SECRET` â Your Port client secret.

### Add GitHub workflows

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

**Create FireHydrant Incident Workflow (Click to expand)**

Create the file `.github/workflows/create-firehydrant-incident.yaml`:

```
name: Create FireHydrant Incident

on:
  workflow_dispatch:
    inputs:
      name:
        description: The name or title of the incident
        required: true
        type: string
      priority:
        description: New priority level for the incident (e.g., P1)
        required: true
        type: string
      description:
        description: The detailed description of the incident
        required: false
        type: string
      port_context:
        required: true
        description: includes blueprint, run ID, and entity identifier from Port.

jobs:
  trigger-incident:
    runs-on: ubuntu-latest
    steps:
      - name: Inform execution of request to trigger incident
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: "About to trigger an incident in FireHydrant..."

      - name: Trigger Incident in FireHydrant
        id: trigger_incident
        uses: fjogeleit/http-request-action@v1
        with:
          url: 'https://api.firehydrant.io/v1/incidents'
          method: 'POST'
          customHeaders: '{"Content-Type": "application/json", "Authorization": "${{ secrets.FIREHYDRANT_API_KEY }}"}'
          data: >-
            {
              "name": "${{ github.event.inputs.name }}",
              "description": "${{ github.event.inputs.description }}",
              "priority": "${{ github.event.inputs.priority }}"
            }

      - name: Inform Port of FireHydrant failure request
        if: failure()
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: "Request to trigger FireHydrant incident failed ..."

      - name: Inform Port of successful FireHydrant incident creation
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: "Incident successfully created in FireHydrant. Upserting the response entity in Port..."

      - name: Upsert FireHydrant entity to Port 
        id: upsert_entity
        uses: port-labs/port-github-action@v1
        with:
          identifier: "${{ fromJson(steps.trigger_incident.outputs.response).id }}"
          title: "${{ fromJson(steps.trigger_incident.outputs.response).name }}"
          blueprint: "firehydrantIncident"
          properties: |-
            {
              "url": "${{ fromJson(steps.trigger_incident.outputs.response).incident_url }}",
              "priority": "${{ fromJson(steps.trigger_incident.outputs.response).priority }}",
              "severity": "${{ fromJson(steps.trigger_incident.outputs.response).severity }}",
              "tags": "${{ fromJson(steps.trigger_incident.outputs.response).tag_list}}",
              "currentMilestone": "${{ fromJson(steps.trigger_incident.outputs.response).current_milestone }}",
              "description": "${{ fromJson(steps.trigger_incident.outputs.response).description}}",
              "customerImpact": "${{ fromJson(steps.trigger_incident.outputs.response).customers_impacted }}",
              "createdBy": "${{ fromJson(steps.trigger_incident.outputs.response).created_by.name }}",
              "createdAt": "${{ fromJson(steps.trigger_incident.outputs.response).created_at }}"
            }
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: UPSERT
          runId: ${{ fromJson(inputs.port_context).run_id }}

      - name: Inform Entity upsert failure
        if: steps.upsert_entity.outcome == 'failure'
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: "Failed to report the created incident back to Port ..."

      - name: Inform completion of FireHydrant incident creation
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: "Incident creation process was successful â"
```

**Self-service action: Create FireHydrant Incident (Click to expand)**

Modification Required

Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

Create in Port

```
{
  "identifier": "create_firehydrant_incident",
  "title": "Create FireHydrant Incident",
  "icon": "FireHydrant",
  "description": "Create a new FireHydrant incident",
  "trigger": {
    "type": "self-service",
    "operation": "CREATE",
    "userInputs": {
      "properties": {
        "name": { "type": "string", "title": "Name", "description": "The name or title of the incident" },
        "description": { "type": "string", "title": "Description", "description": "Detailed description of the incident" },
        "priority": {
          "type": "string",
          "title": "Priority",
          "enum": ["P1", "P2", "P3", "P4"],
          "enumColors": { "P1": "red", "P2": "orange", "P3": "blue", "P4": "lightGray" }
        }
      },
      "required": [],
      "order": ["name", "description"]
    }
  },
  "invocationMethod": {
    "type": "GITHUB",
    "org": "<GITHUB_ORG>",
    "repo": "<GITHUB_REPO>",
    "workflow": "create-firehydrant-incident.yaml",
    "workflowInputs": {
      "{{ spreadValue() }}": "{{ .inputs }}",
      "port_context": { "run_id": "{{ .run.id }}" }
    },
    "reportWorkflowStatus": true
  },
  "requiredApproval": false
}
```

**Trigger FireHydrant Incident Workflow (Click to expand)**

Create the file `.github/workflows/trigger-firehydrant-incident.yml`:

```
name: Trigger FireHydrant Incident

on:
  workflow_dispatch:
    inputs:
      name:
        description: The name of the incident
        required: true
        type: string
      condition:
        description: The service status
        required: true
        type: string
        default: "Unavailable"
        enum: [Unavailable, Degraded, Bug, Operational]
      incident_description:
        description: Description of the incident
        required: false
        type: string
      port_context:
        required: true
        description: includes blueprint, run ID, and entity identifier from Port.

jobs:
  trigger:
    runs-on: ubuntu-latest
    steps:
      - name: Inform start of FireHydrant incident creation
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: Starting request to create FireHydrant incident

      - name: Get condition ID
        id: condition_id
        run: |
          case "${{ inputs.condition }}" in
            "Unavailable")
              echo "condition_id=b1fc9184-b3f3-4af1-a111-68abcad9bf34" >> $GITHUB_OUTPUT
              ;;
            "Degraded")
              echo "condition_id=465a5b4c-6f95-4707-a777-ab4bb8def27d" >> $GITHUB_OUTPUT
              ;;
            "Bug")
              echo "condition_id=c2bc11e8-7fcc-428d-9007-26f00700834a" >> $GITHUB_OUTPUT
              ;;
            "Operational")
              echo "condition_id=9a2a8dbb-6b4e-4189-aca1-e2bb73b9c50b" >> $GITHUB_OUTPUT
              ;;
          esac

      - name: Trigger FireHydrant Incident
        id: trigger
        uses: fjogeleit/http-request-action@v1
        with:
          url: 'https://api.firehydrant.io/v1/incidents'
          method: 'POST'
          customHeaders: '{"Content-Type": "application/json", "Authorization": "${{ secrets.FIREHYDRANT_API_KEY }}"}'
          data: >-
            {
              "impacts": [
                {
                  "type": "service",
                  "id": "${{ fromJson(inputs.port_context).entity.relations.fh_service }}",
                  "condition_id": "${{ steps.condition_id.outputs.condition_id }}"
                }
              ],
              "name": "${{ inputs.name }}",
              "description": "${{ inputs.incident_description }}"
            }

      - name: Inform completion of FireHydrant incident creation
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: PATCH_RUN
          runId: ${{ fromJson(inputs.port_context).run_id }}
          logMessage: Finished request to create FireHydrant incident

      - name: Update FireHydrant service in Port
        uses: port-labs/port-github-action@v1
        with:
          clientId: ${{ secrets.PORT_CLIENT_ID }}
          clientSecret: ${{ secrets.PORT_CLIENT_SECRET }}
          baseUrl: https://api.port.io
          operation: UPSERT
          runId: ${{ fromJson(inputs.port_context).run_id }}
          identifier: ${{ fromJson(steps.trigger.outputs.response).id }}
          title: ${{ fromJson(steps.trigger.outputs.response).name }}
          blueprint: firehydrantService
          properties: |-
            {
              "name": "${{ fromJson(steps.trigger.outputs.response).name }}",
              "description": "${{ fromJson(steps.trigger.outputs.response).description }}",
              "status": "${{ fromJson(steps.trigger.outputs.response).status }}"
            }
```

**Self-service action: Trigger FireHydrant Incident (Click to expand)**

Modification Required

Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

Create in Port

```
{
  "identifier": "trigger_firehydrant_incident",
  "title": "Trigger FireHydrant Incident",
  "icon": "FireHydrant",
  "description": "Trigger a new FireHydrant incident",
  "trigger": {
    "type": "self-service",
    "operation": "DAY-2",
    "userInputs": {
      "properties": {
        "name": { "icon": "DefaultProperty", "type": "string", "title": "Incident name" },
        "condition": {
          "icon": "DefaultProperty",
          "title": "Service status",
          "type": "string",
          "enum": ["Unavailable", "Degraded", "Bug", "Operational"],
          "enumColors": { "Unavailable": "lightGray", "Degraded": "lightGray", "Bug": "lightGray", "Operational": "lightGray" }
        },
        "incident_description": { "type": "string", "title": "Incident description" }
      },
      "required": ["name", "condition"],
      "order": ["name", "condition", "incident_description"]
    },
    "blueprintIdentifier": "service"
  },
  "invocationMethod": {
    "type": "GITHUB",
    "org": "<GITHUB_ORG>",
    "repo": "<GITHUB_REPO>",
    "workflow": "trigger-firehydrant-incident.yml",
    "workflowInputs": {
      "name": "{{.inputs.\"name\"}}",
      "condition": "{{.inputs.\"condition\"}}",
      "incident_description": "{{.inputs.\"incident_description\"}}",
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

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Head to the [self-service page](https://app.getport.io/self-serve) of your portal.

2. Choose either implementation method and action:

   <!-- -->

   * GitHub workflow: `Create FireHydrant Incident` or `Trigger FireHydrant Incident`.
   * Synced webhook: `Create FireHydrant Incident (Webhook)` or `Trigger an incident`.

3. For the trigger flow, select a service that has a `fh_service` relation to a FireHydrant service.

4. Fill in the incident details as prompted.

5. Click `Execute` and wait for FireHydrant to create or trigger the incident.

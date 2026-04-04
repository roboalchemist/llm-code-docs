# Source: https://docs.port.io/guides/all/interact-with-pagerduty-incidents.md

# Interact with PagerDuty incidents

This guide demonstrates how to implement self-service actions that create new PagerDuty incidents or trigger incidents on services directly from Port using synced webhooks or GitHub workflows.

## Use cases[â](#use-cases "Direct link to Use cases")

* Create PagerDuty incidents from Port with title, urgency, and description.
* Trigger incidents against PagerDuty services with a chosen severity and event action.
* Keep your Port catalog in sync by automatically upserting the created incident or updating related service data after execution.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).

* Access to your PagerDuty organization with permissions to manage incidents.

* A [PagerDuty routing key](https://support.pagerduty.com/docs/services-and-integrations#events-api-v2-integration-key) for the service you want to trigger incidents for.

  Finding your PagerDuty routing key

  To find your PagerDuty routing key (also called integration key):

  * Log in to your PagerDuty account
  * Navigate to **Services** in the main menu
  * Select the service you want to trigger incidents for
  * Click on the **Integrations** tab
  * Look for an existing "Events API V2" integration, or click **Add integration** and select "Events API V2"
  * The **Integration Key** displayed is your routing key

* Optional - Install Port's PagerDuty integration [learn more](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty)

  PagerDuty Integration

  This step is not required for this example, but it will create all the blueprint boilerplate for you, and also ingest and update the catalog in real time with your PagerDuty Incidents.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

If you haven't installed the PagerDuty integration, you'll need to create blueprints for PagerDuty incidents and PagerDuty services. However, we highly recommend you install the PagerDuty integration to have these automatically set up for you.

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

### Create the PagerDuty incident blueprint

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Copy and paste the following JSON configuration into the editor.

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

5. Click "Save" to create the blueprint.

## Implementation[â](#implementation "Direct link to Implementation")

* Synced webhook
* GitHub workflow

Configure two self-service actions using Port's synced webhooks and secrets to interact directly with PagerDuty's API.<br /><!-- -->The self-service actions will be used to create and trigger incidents.

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
   * `PAGERDUTY_ROUTING_KEY`: Your PagerDuty routing key for the service.

### Set up self-service actions

#### Create a PagerDuty incident

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Create PagerDuty Incident (Webhook) (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "create_incident_webhook",
     "title": "Create Incident (Webhook)",
     "icon": "pagerduty",
     "description": "Create a new PagerDuty incident",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "title": {
             "icon": "DefaultProperty",
             "title": "Title",
             "type": "string"
           },
           "extra_details": {
             "title": "Extra Details",
             "type": "string"
           },
           "urgency": {
             "icon": "DefaultProperty",
             "title": "Urgency",
             "type": "string",
             "default": "high",
             "enum": [
               "high",
               "low"
             ],
             "enumColors": {
               "high": "yellow",
               "low": "green"
             }
           }
         },
         "required": [
           "title",
           "urgency"
         ],
         "order": [
           "title",
           "urgency",
           "extra_details"
         ]
       },
       "blueprintIdentifier": "pagerdutyService"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.pagerduty.com/incidents",
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
         "incident": {
           "type": "incident",
           "title": "{{.inputs.title}}",
           "service": {
             "id": "{{.entity.identifier}}",
             "type": "service_reference"
           },
           "urgency": "{{.inputs.urgency}}",
           "body": {
             "type": "incident_body",
             "details": "{{.inputs.extra_details}}"
           }
         }
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

#### Trigger a PagerDuty incident

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Trigger PagerDuty Incident (Webhook) (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "trigger_incident_webhook",
     "title": "Trigger Incident (Webhook)",
     "icon": "pagerduty",
     "description": "Trigger a new PagerDuty incident",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "summary": {
             "icon": "DefaultProperty",
             "title": "Summary",
             "type": "string"
           },
           "source": {
             "icon": "DefaultProperty",
             "title": "Source",
             "type": "string",
             "default": "Port"
           },
           "severity": {
             "icon": "DefaultProperty",
             "title": "Severity",
             "type": "string",
             "default": "critical",
             "enum": [
               "critical",
               "error",
               "warning",
               "info"
             ],
             "enumColors": {
               "critical": "red",
               "error": "red",
               "warning": "yellow",
               "info": "blue"
             }
           },
           "event_action": {
             "icon": "DefaultProperty",
             "title": "Event Action",
             "type": "string",
             "default": "trigger",
             "enum": [
               "trigger",
               "acknowledge",
               "resolve"
             ]
           }
         },
         "required": [
           "summary",
           "source",
           "severity",
           "event_action"
         ],
         "order": [
           "summary",
           "source",
           "severity",
           "event_action"
         ]
       },
       "blueprintIdentifier": "pagerdutyIncident"
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://events.pagerduty.com/v2/enqueue",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Content-Type": "application/json"
       },
       "body": {
         "payload": {
           "summary": "{{.inputs.summary}}",
           "source": "{{.inputs.source}}",
           "severity": "{{.inputs.severity}}"
         },
         "routing_key": "{{.secrets.PAGERDUTY_ROUTING_KEY}}",
         "event_action": "{{.inputs.event_action}}"
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

### Set up automations

#### Sync PagerDuty incident after creation

1. Head to the [Automations](https://app.getport.io/automations) page.

2. Click on the `+ New Automation` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Sync PagerDuty incident after creation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "pagerdutyIncident_sync_status",
     "title": "Sync PagerDuty Incident Status",
     "description": "Update PagerDuty incident data in Port after creation",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "RUN_UPDATED",
         "actionIdentifier": "create_incident_webhook"
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

5. Click `Save`.

#### Sync PagerDuty incident after trigger

1. Head to the [Automations](https://app.getport.io/automations) page.

2. Click on the `+ New Automation` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Sync PagerDuty incident after trigger (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "pagerdutyIncident_sync_after_trigger",
     "title": "Sync PagerDuty Incident After Trigger",
     "description": "Update PagerDuty incident data in Port after triggering",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "RUN_UPDATED",
         "actionIdentifier": "trigger_incident_webhook"
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
         "identifier": "{{.event.diff.after.response.dedup_key}}",
         "title": "{{.event.diff.after.properties.summary}}",
         "properties": {
           "status": "triggered",
           "urgency": "high",
           "created_at": "{{.event.diff.after.createdAt}}"
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

* `PAGERDUTY_API_KEY` â Your PagerDuty API token. See [PagerDuty docs](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account) for generating an API token.
* `PAGERDUTY_ROUTING_KEY` â Your PagerDuty routing key for the service.
* `PORT_CLIENT_ID` â Your Port client id.
* `PORT_CLIENT_SECRET` â Your Port client secret.

### Add GitHub workflows

Dedicated Workflows Repository

We recommend creating a dedicated repository for the workflows that are used by Port actions.

**Create PagerDuty Incident Workflow (Click to expand)**

Create the file `.github/workflows/create-pagerduty-incident.yaml`:

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
          service: "${{fromJson(inputs.port_context).entity}}"
          blueprintIdentifier: 'pagerdutyIncident'
```

**Trigger PagerDuty Incident Workflow (Click to expand)**

Create the file `.github/workflows/trigger-pagerduty-incident.yaml`:

```
name: Trigger PagerDuty Incident

on:
  workflow_dispatch:
    inputs:
      summary:
        description: The summary of the incident to trigger
        required: true
        type: string
      source:
        description: The source of the incident
        required: true
        type: string
      severity:
        description: The severity of the incident
        required: true
        type: string
        default: "critical"
      event_action:
        description: The event action
        required: true
        type: string
        default: "trigger"
      routing_key:
        description: The routing key of the service
        required: true
        type: string
      port_context:
        required: true
        description: includes blueprint, run ID, and entity identifier from Port.

  jobs: 
    trigger:
      runs-on: ubuntu-latest
      steps:
        - name: Trigger PagerDuty Incident
          id: trigger
          uses: fjogeleit/http-request-action@v1
          with:
            url: 'https://events.pagerduty.com/v2/enqueue'
            method: 'POST'
            customHeaders: '{"Content-Type": "application/json"}'
            data: >-
              {
                "payload": {
                  "summary": "${{ inputs.summary }}",
                  "source": "${{ inputs.source }}",
                  "severity": "${{ inputs.severity }}"
                },
                "routing_key": "${{ inputs.routing_key }}",
                "event_action": "${{ inputs.event_action }}"
              }
        
        - name: Log Response
          run: |
            echo "Response status: ${{ steps.trigger.outputs.status }}"
            echo "Response data: ${{ steps.trigger.outputs.response }}"
```

### Add the self-service actions

#### Create PagerDuty Incident Self-Service Action

1. Go to the [Self-Service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Create PagerDuty Incident Self-Service Action(Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   Create in Port

   ```
   {
   "identifier": "pagerdutyService_create_incident",
   "title": "Create Incident",
   "icon": "pagerduty",
   "description": "Create a new PagerDuty incident",
   "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
       "properties": {
           "title": {
           "icon": "DefaultProperty",
           "title": "Title",
           "type": "string"
           },
           "extra_details": {
           "title": "Extra Details",
           "type": "string"
           },
           "urgency": {
           "icon": "DefaultProperty",
           "title": "Urgency",
           "type": "string",
           "default": "high",
           "enum": [
               "high",
               "low"
           ],
           "enumColors": {
               "high": "yellow",
               "low": "green"
           }
           },
           "from": {
           "title": "From",
           "icon": "User",
           "type": "string",
           "format": "user",
           "default": {
               "jqQuery": ".user.email"
           }
           }
       },
       "required": [
           "title",
           "urgency",
           "from"
       ],
       "order": [
           "title",
           "urgency",
           "from",
           "extra_details"
       ]
       },
       "blueprintIdentifier": "pagerdutyService"
   },
   "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB_ORG>",
       "repo": "<GITHUB_REPO>",
       "workflow": "create-pagerduty-incident.yaml",
       "workflowInputs": {
       "title": "{{.inputs.\"title\"}}",
       "extra_details": "{{.inputs.\"extra_details\"}}",
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

#### Trigger PagerDuty Incident Self-Service Action

1. Go to the [Self-Service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Trigger PagerDuty Incident Self-Service Action (Click to expand)**

   Modification Required

   Make sure to replace `<GITHUB_ORG>` and `<GITHUB_REPO>` with your GitHub organization and repository names respectively.

   Create in Port

   ```
   {
   "identifier": "trigger_pagerduty_incident",
   "title": "Trigger Incident",
   "icon": "pagerduty",
   "description": "Trigger a new PagerDuty incident",
   "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
       "properties": {
           "summary": {
           "icon": "DefaultProperty",
           "title": "Summary",
           "type": "string"
           },
           "source": {
           "icon": "DefaultProperty",
           "title": "Source",
           "type": "string",
           "default": "Port"
           },
           "severity": {
           "icon": "DefaultProperty",
           "title": "Severity",
           "type": "string",
           "default": "critical",
           "enum": [
               "critical",
               "error",
               "warning",
               "info"
           ],
           "enumColors": {
               "critical": "red",
               "error": "red",
               "warning": "yellow",
               "info": "blue"
           }
           },
           "event_action": {
           "icon": "DefaultProperty",
           "title": "Event Action",
           "type": "string",
           "default": "trigger",
           "enum": [
               "trigger",
               "acknowledge",
               "resolve"
           ]
           },
           "routing_key": {
           "icon": "DefaultProperty",
           "title": "Routing Key",
           "type": "string",
           "description": "The routing key of the service"
           }
       },
       "required": [
           "summary",
           "source",
           "severity",
           "event_action",
           "routing_key"
       ],
       "order": [
           "summary",
           "source",
           "severity",
           "event_action",
           "routing_key"
       ]
       },
       "blueprintIdentifier": "pagerdutyIncident"
   },
   "invocationMethod": {
       "type": "GITHUB",
       "org": "<GITHUB_ORG>",
       "repo": "<GITHUB_REPO>",
       "workflow": "trigger-pagerduty-incident.yaml",
       "workflowInputs": {
       "summary": "{{.inputs.\"summary\"}}",
       "source": "{{.inputs.\"source\"}}",
       "severity": "{{.inputs.\"severity\"}}",
       "event_action": "{{.inputs.\"event_action\"}}",
       "routing_key": "{{.inputs.\"routing_key\"}}",
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

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Head to the [self-service page](https://app.getport.io/self-serve) of your portal.

2. Choose either implementation method and action:

   <!-- -->

   * GitHub workflow: `Create Incident` or `Trigger Incident`.
   * Synced webhook: `Create Incident (Webhook)` or `Trigger Incident (Webhook)`.

3. For the trigger flow, select a service that has a `pagerduty_service` relation to a PagerDuty service.

4. Fill in the incident details as prompted.

5. Click `Execute` and wait for PagerDuty to create or trigger the incident.

## Related guides[â](#related-guides "Direct link to Related guides")

* [Acknowledge Incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/acknowledge-incident)
* [Change On-Call User](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-on-call-user)
* [Change PagerDuty incident owner](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-pagerduty-incident-owner)
* [Create PagerDuty service](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/create-pagerduty-service)
* [Escalate an incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/escalate-an-incident)
* [Resolve an incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/resolve-incident)

# Source: https://docs.port.io/guides/all/manage-and-visualize-pagerduty-incidents.md

# Manage and visualize your PagerDuty incidents

This guide demonstrates how to bring your incident management experience into Port using PagerDuty.<br /><!-- -->You will learn how to:

* Set up **self-service actions** to manage incidents (trigger, acknowledge, and resolve).
* Build **dashboards** in Port to monitor and take action on your incident response.

![](/img/guides/pagerDutyDashboard1.png) ![](/img/guides/pagerDutyDashboard2.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Empower on-call teams to quickly respond to incidents with self-service actions.
* Monitor the status and health of all incidents across services from a single dashboard.
* Track incident metrics and response times to improve incident management processes.
* Get visibility into incident trends and patterns across your organization.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [PagerDuty integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty) is installed in your account.
* Access to your PagerDuty organization with permissions to manage incidents.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

If you haven't installed the [PagerDuty integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty), you'll need to create blueprints for PagerDuty incidents.<br /><!-- -->However, we highly recommend you install the [PagerDuty integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty) to have these automatically set up for you.

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

## Set up self-service actions[â](#set-up-self-service-actions "Direct link to Set up self-service actions")

Now let's set up self-service actions to manage your PagerDuty incidents directly from Port.<br /><!-- -->We will implement three key incident management workflows using webhook-based actions for simplicity.

### Add Port secrets[â](#add-port-secrets "Direct link to Add Port secrets")

<!-- -->

Existing secrets

If you have already installed Port's <!-- -->PagerDuty<!-- --> integration, these secrets should already exist in your portal.<br /><!-- -->To view your existing secrets:

1. Click on the `...` button in the top right corner of your Port application.
2. Choose **Credentials**, then click on the `Secrets` tab.

First, add the required secrets to your portal:

1. Click on the `...` button in the top right corner of your Port application.

2. Click on **Credentials**.

3. Click on the `Secrets` tab.

4. Click on `+ Secret` and add the following secrets:

   * `PAGERDUTY_ROUTING_KEY`: Your PagerDuty routing key for the service.
   * `PAGERDUTY_API_KEY`: Your PagerDuty API token.

#### Multiple services support

If you want to create incidents for **multiple PagerDuty services**, you can modify the action to use routing key as an input field instead of a secret. This allows you to specify different routing keys for different services when triggering incidents.

To implement this:

1. Remove `PAGERDUTY_ROUTING_KEY` from secrets.

2. Add `routing_key` as a required input property in the action configuration.

3. Update the webhook body to use `{{.inputs.routing_key}}` instead of `{{.secrets.PAGERDUTY_ROUTING_KEY}}`.

### Trigger PagerDuty incidents[â](#trigger-pagerduty-incidents "Direct link to Trigger PagerDuty incidents")

Trigger PagerDuty incidents directly from Port when issues are detected.

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor:

   **Trigger PagerDuty incident (click to expand)**

   Create in Port

   ```
   {
       "identifier": "trigger_pagerduty_incident",
       "title": "Trigger PagerDuty incident",
       "icon": "pagerduty",
       "description": "Trigger a new PagerDuty incident directly from Port",
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

#### Create PagerDuty incident trigger automation

Create an automation to update Port when PagerDuty incidents are triggered:

1. Head to the [automation](https://app.getport.io/settings/automations) page.

2. Click on the `+ Automation` button.

3. Copy and paste the following JSON configuration:

   **Trigger PagerDuty incident automation (click to expand)**

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
         "actionIdentifier": "trigger_pagerduty_incident"
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

4. Click `Save`.

### Acknowledge PagerDuty incidents[â](#acknowledge-pagerduty-incidents "Direct link to Acknowledge PagerDuty incidents")

Acknowledge PagerDuty incidents to signal that someone is working on the issue.

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration:

   **Acknowledge PagerDuty incident (click to expand)**

   Create in Port

   ```
   {
     "identifier": "acknowledge_pagerduty_incident",
     "title": "Acknowledge PagerDuty incident",
     "icon": "pagerduty",
     "description": "Acknowledge PagerDuty incident directly from Port",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {},
         "required": [],
         "order": []
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
         "routing_key": "{{.secrets.PAGERDUTY_ROUTING_KEY}}",
         "event_action": "acknowledge",
         "dedup_key": "{{.entity.identifier}}"
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

#### Create acknowledge PagerDuty incident automation

Create an automation to update Port when PagerDuty incidents are acknowledged:

1. Head to the [automation](https://app.getport.io/settings/automations) page.

2. Click on the `+ Automation` button.

3. Copy and paste the following JSON configuration:

   **Acknowledge PagerDuty incident automation (click to expand)**

   Create in Port

   ```
   {
     "identifier": "pagerdutyIncident_sync_acknowledge_status",
     "title": "Sync PagerDuty Incident Status After Acknowledge",
     "description": "Update PagerDuty incident data in Port after acknowledgment",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "RUN_UPDATED",
         "actionIdentifier": "acknowledge_pagerduty_incident"
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

### Resolve PagerDuty incidents[â](#resolve-pagerduty-incidents "Direct link to Resolve PagerDuty incidents")

Resolve PagerDuty incidents once the underlying issue has been fixed.

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration:

   **Resolve PagerDuty incident (click to expand)**

   Create in Port

   ```
   {
     "identifier": "resolve_pagerduty_incident",
     "title": "Resolve PagerDuty incident",
     "icon": "pagerduty",
     "description": "Resolve a PagerDuty incident directly from Port",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {},
         "required": [],
         "order": []
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
         "routing_key": "{{.secrets.PAGERDUTY_ROUTING_KEY}}",
         "event_action": "resolve",
         "dedup_key": "{{.entity.identifier}}"
       }
     },
     "requiredApproval": false
   }
   ```

5. Click `Save`.

#### Create resolve PagerDuty incident automation

Create an automation to update Port when PagerDuty incidents are resolved:

1. Head to the [automation](https://app.getport.io/settings/automations) page.

2. Click on the `+ Automation` button.

3. Copy and paste the following JSON configuration:

   **Resolve PagerDuty incident automation (click to expand)**

   Create in Port

   ```
   {
       "identifier": "pagerdutyIncident_sync_resolve_status",
       "title": "Sync PagerDuty Incident Status After Resolve",
       "description": "Update PagerDuty incident data in Port after resolution",
       "trigger": {
           "type": "automation",
           "event": {
               "type": "RUN_UPDATED",
               "actionIdentifier": "resolve_pagerduty_incident"
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
               "title": "{{.event.diff.after.entity.title}}",
               "properties": {
                   "status": "resolved",
                   "updated_at": "{{.event.diff.after.endedAt}}"
               }
           }
       },
       "publish": true
   }
   ```

4. Click `Save`.

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. Head to the [self-service page](https://app.getport.io/self-serve) of your portal

2. **Test triggering a PagerDuty incident:**

   * Click on `Trigger PagerDuty incident`

   * Fill in the required information:

     <!-- -->

     * Summary: A description of the PagerDuty incident (e.g., "Database connection timeout").
     * Source: Where the incident originated (default: "Port").
     * Severity: Choose from critical, error, warning, or info.
     * Event Action: Set to "trigger".

   * Click `Execute`

3. **Test acknowledging a PagerDuty incident:**

   * Navigate to an existing PagerDuty incident in your catalog.
   * Click on `Acknowledge PagerDuty incident`
   * Click `Execute`

4. **Test resolving an incident:**

   * Navigate to an acknowledged incident in your catalog.
   * Click on `Resolve PagerDuty incident`
   * Click `Execute`

## Visualize metrics[â](#visualize-metrics "Direct link to Visualize metrics")

With your incident management actions in place and data flowing, we can create a dedicated dashboard in Port to visualize all incidents by status, urgency, or service using customizable widgets.

### Create a dashboard[â](#create-a-dashboard "Direct link to Create a dashboard")

1. Navigate to the [Catalog](https://app.getport.io/organization/catalog) page of your portal.

2. Click on the **`+ New`** button in the left sidebar.

3. Select **New dashboard**.

4. Name the dashboard **PagerDuty Incident Management**.

5. Input `Monitor and manage your PagerDuty incidents` under **Description**.

6. Select the `PagerDuty` icon.

7. Click `Create`.

We now have a blank dashboard where we can start adding widgets to visualize insights from our PagerDuty incidents.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

In the new dashboard, create the following widgets:

**Incidents by status (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Incidents by status` (add the `PagerDuty` icon).

3. Choose the **PagerDuty Incident** blueprint.

4. Under `Breakdown by property`, select the **Incident Status** property

5. Click `Save`

**Incidents by urgency (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Incidents by urgency` (add the `PagerDuty` icon)

3. Choose the **PagerDuty Incident** blueprint.

4. Under `Breakdown by property`, select the **Incident Urgency** property.

5. Click `Save`

**Open incidents (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Open incidents` (add the `Alert` icon)

3. Select `Count entities` **Chart type** and choose **PagerDuty Incident** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter open incidents:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"status",
                   "operator":"in",
                   "value":["triggered", "acknowledged"]
               }
           ]
       }
   ]
   ```

6. Select `custom` as the **Unit** and input `incidents` as the **Custom unit**.

7. Click `Save`

**Resolved incidents (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Resolved incidents` (add the `BadgeAlert` icon)

3. Select `Count entities` **Chart type** and choose **PagerDuty Incident** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter resolved incidents:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"status",
                   "operator":"=",
                   "value":"resolved"
               }
           ]
       }
   ]
   ```

6. Select `custom` as the **Unit** and input `incidents` as the **Custom unit**.

7. Click `Save`

**Critical incidents (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Critical incidents` (add the `Alert` icon)

3. Select `Count entities` **Chart type** and choose **PagerDuty Incident** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter critical incidents from this month:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"urgency",
                   "operator":"=",
                   "value":"high"
               }
           ]
       }
   ]
   ```

6. Select `custom` as the **Unit** and input `incidents` as the **Custom unit**.

7. Click `Save`

**Average resolution time over time (click to expand)**

1. Click `+ Widget` and select **Line Chart**.

2. Title: `Average Resolution Time Over Time`, (add the `LineChart` icon)

3. Select `Aggregate Property (All Entities)` **Chart type** and choose **PagerDuty Incident** as the **Blueprint**.

4. Input `Resolution Time (hours)` as the **Y axis** **Title** and choose `Time to Recovery` as the **Property**.

5. Set `average` as the **Function**.

6. Input `Months` as the **X axis** **Title** and choose `created_at` as the **Measure time by**.

7. Set **Time Interval** to `Month` and **Time Range** to `In the past 365 days`.

8. Add this JSON to the **Additional filters** editor to only include resolved incidents:

   ```
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"status",
                   "operator":"=",
                   "value":"resolved"
               }
           ]
       }
   ```

9. Click `Save`

**All incidents table (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title the widget **All Incidents** (add the `pagerduty` icon)

3. Choose the **PagerDuty Incident** blueprint.

4. Click `Save` to add the widget to the dashboard.

5. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

6. In the top right corner of the table, click on `Manage Properties` and add the following properties:

   * **Incident Status**: The current status of the incident.
   * **Incident Urgency**: The urgency level of the incident.
   * **PagerDuty Service**: The name of the related PagerDuty service.
   * **Assignee**: The person assigned to the incident.
   * **Created At**: When the incident was created.

7. Click on the **save icon** in the top right corner of the widget to save the customized table.

## Related guides[â](#related-guides "Direct link to Related guides")

* **[Trigger a PagerDuty Incident](/guides/all/interact-with-pagerduty-incidents.md)**: Complete guide for creating incidents
* **[Acknowledge Incident In PagerDuty](/guides/all/acknowledge-incident.md)**: Complete guide for acknowledging incidents
* **[Resolve an Incident in PagerDuty](/guides/all/resolve-incident.md)**: Complete guide for resolving incidents
* **[Change On-Call User](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/change-on-call-user)**: Change who's on-call for a service
* **[Escalate an incident](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/escalate-an-incident)**: Escalate incidents when needed
* **[Create PagerDuty service](https://docs.port.io/actions-and-automations/setup-backend/github-workflow/examples/PagerDuty/create-pagerduty-service)**: Create new PagerDuty services

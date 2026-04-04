# Source: https://docs.port.io/guides/all/track-and-show-mtbf-for-services.md

# Track and show MTBF for services

This guide demonstrates how to implement **Mean Time Between Failures (MTBF)** tracking for your PagerDuty services using Port. MTBF measures the average time between service failures and helps identify reliability trends.

**MTBF = Total Operational Time Ã· Number of Failures**

For example: A service running 720 hours with 3 incidents has an MTBF of 240 hours. Higher MTBF values indicate better reliability.

![](/img/guides/mtbfDashboard.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* **Reliability monitoring**: Track how often your services fail and identify patterns over time.
* **SLA compliance**: Monitor service reliability against defined targets and SLAs.
* **Incident reduction**: Identify the most unreliable services that need improvement focus.
* **Team accountability**: Track reliability metrics by team and service ownership.
* **Capacity planning**: Use historical failure patterns to inform infrastructure decisions.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](/getting-started/overview.md).
* Port's [PagerDuty integration](/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/.md) is installed in your account.
* Access to your PagerDuty organization with incident data for your services.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

If you haven't installed the [PagerDuty integration](/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/.md), you'll need to create blueprints for PagerDuty services and incidents.<br /><!-- -->However, we highly recommend installing the [PagerDuty integration](/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/.md) to have these automatically set up for you.

### Create PagerDuty service blueprint[â](#create-pagerduty-service-blueprint "Direct link to Create PagerDuty service blueprint")

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

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
           "status": {
             "title": "Status",
             "type": "string",
             "enum": [
               "active",
               "warning",
               "critical",
               "maintenance",
               "disabled"
             ],
             "enumColors": {
               "active": "green",
               "warning": "yellow",
               "critical": "red",
               "maintenance": "lightGray",
               "disabled": "darkGray"
             }
           },
           "url": {
             "title": "URL",
             "type": "string",
             "format": "url"
           },
           "oncall": {
             "title": "On Call",
             "type": "string",
             "format": "user"
           },
           "meanSecondsToResolve": {
             "title": "Mean Seconds to Resolve",
             "type": "number"
           },
           "meanSecondsToFirstAck": {
             "title": "Mean Seconds to First Acknowledge",
             "type": "number"
           },
           "meanSecondsToEngage": {
             "title": "Mean Seconds to Engage",
             "type": "number"
           }
         },
         "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "relations": {}
     }
   ```

5. Click `Save`.

### Create PagerDuty incident blueprint[â](#create-pagerduty-incident-blueprint "Direct link to Create PagerDuty incident blueprint")

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Add this JSON schema:

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

5. Click `Save`.

### Add aggregation properties[â](#add-aggregation-properties "Direct link to Add aggregation properties")

First, we need to add aggregation properties to count incidents over different time periods. These properties will count the number of PagerDuty incidents related to each service within specific time windows.

Follow the steps below to add aggregation properties to the PagerDuty Service blueprint:

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Click on the **PagerDuty Service** blueprint.

3. Click on the `...` button in the top right corner, and choose `Edit JSON`.

4. Add these aggregation properties to the blueprint JSON:

   **Incident count aggregation properties (click to expand)**

   ```
     "incidents30Days": {
       "title": "Incidents (30 days)",
       "icon": "Alert",
       "description": "Number of incidents in the last 30 days",
       "target": "pagerdutyIncident",
       "calculationSpec": {
         "func": "count",
         "calculationBy": "entities",
         "filter": {
           "combinator": "and",
           "rules": [
             {
               "operator": ">=",
               "property": "created_at",
               "value": "{{(now - 2592000) | strftime(\"%Y-%m-%dT%H:%M:%SZ\")}}"
             }
           ]
         }
       },
       "type": "number"
     },
     "incidents90Days": {
       "title": "Incidents (90 days)",
       "icon": "Alert",
       "description": "Number of incidents in the last 90 days",
       "target": "pagerdutyIncident",
       "calculationSpec": {
         "func": "count",
         "calculationBy": "entities",
         "filter": {
           "combinator": "and",
           "rules": [
             {
               "operator": ">=",
               "property": "created_at",
               "value": "{{(now - 7776000) | strftime(\"%Y-%m-%dT%H:%M:%SZ\")}}"
             }
           ]
         }
       },
       "type": "number"
     }
   ```

5. Click `Save` to update the blueprint.

Understanding aggregation properties

Aggregation properties automatically count or aggregate data from related entities. In this case, they count PagerDuty incidents that are related to each service and filter them by creation date to get incident counts for the last 30 and 90 days.

### Add MTBF calculation properties[â](#add-mtbf-calculation-properties "Direct link to Add MTBF calculation properties")

Now we'll add calculation properties that use the aggregation properties to automatically compute MTBF metrics for each service:

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Click on the **PagerDuty Service** blueprint.

3. Click on the `...` button in the top right corner, and choose `Edit JSON`.

4. Add these calculation properties to the blueprint JSON:

   **MTBF calculation properties (click to expand)**

   ```
   "mtbf_30_days": {
     "title": "MTBF (30 days)",
     "icon": "ClockLoader",
     "description": "Mean Time Between Failures over the past 30 days (in hours)",
     "calculation": "if (.properties.incidents30Days // 0) > 0 then (30 * 24) / .properties.incidents30Days else null end",
     "type": "number"
     
   },
   "mtbf_90_days": {
     "title": "MTBF (90 days)",
     "icon": "ClockLoader", 
     "description": "Mean Time Between Failures over the past 90 days (in hours)",
     "calculation": "if (.properties.incidents90Days // 0) > 0 then (90 * 24) / .properties.incidents90Days else null end",
     "type": "number"
   }
   ```

5. Click `Save` to update the blueprint.

### Add MTBF target and threshold properties[â](#add-mtbf-target-and-threshold-properties "Direct link to Add MTBF target and threshold properties")

Before creating self-service actions, we need to add properties for storing MTBF targets and alert thresholds:

1. Still in the **PagerDuty Service** blueprint JSON, add these properties to the `properties` section:

   **MTBF target and threshold properties (click to expand)**

   ```
   "mtbfTarget": {
     "title": "MTBF Target (hours)",
     "type": "number",
     "description": "Target mean time between failures in hours"
   },
   "mtbfCriticalThreshold": {
     "title": "Critical Threshold (%)",
     "type": "number",
     "description": "Percentage below target that triggers critical alert",
     "default": 50
   },
   "mtbfWarningThreshold": {
     "title": "Warning Threshold (%)", 
     "type": "number",
     "description": "Percentage below target that triggers warning",
     "default": 75
   }
   ```

2. Click `Save` to update the blueprint.

## Set up self-service actions[â](#set-up-self-service-actions "Direct link to Set up self-service actions")

Now let's create self-service actions to help teams monitor and improve MTBF for their services.

### Add Port secrets

<!-- -->

Existing secrets

If you have already installed Port's <!-- -->PagerDuty<!-- --> integration, these secrets should already exist in your portal.<br /><!-- -->To view your existing secrets:

1. Click on the `...` button in the top right corner of your Port application.
2. Choose **Credentials**, then click on the `Secrets` tab.

First, add the required secrets to your portal:

1. Click on the `...` button in the top right corner of your Port application.

2. Click on **Credentials**.

3. Click on the `Secrets` tab.

4. Click on `+ Secret` and add the following secret:

   * `PAGERDUTY_API_KEY`: Your PagerDuty API token.

### Set reliability target action[â](#set-reliability-target-action "Direct link to Set reliability target action")

Create an action to set MTBF targets for services:

1. Click on the `+ New Action` button.

2. Click on the `{...} Edit JSON` button.

3. Copy and paste the following JSON configuration:

   **Set reliability target action (click to expand)**

   Create in Port

   ```
   {
     "identifier": "set_mtbf_target",
     "title": "Set MTBF Target", 
     "icon": "Pagerduty",
     "description": "Set reliability targets and thresholds for the service",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "mtbfTarget": {
             "title": "MTBF Target (hours)",
             "type": "number",
             "description": "Target mean time between failures in hours"
           },
           "criticalThreshold": {
             "title": "Critical Threshold (%)",
             "type": "number", 
             "description": "Percentage below target that triggers critical alert",
             "default": 50
           },
           "warningThreshold": {
             "title": "Warning Threshold (%)",
             "type": "number",
             "description": "Percentage below target that triggers warning",
             "default": 75
           }
         },
         "required": ["mtbfTarget"],
         "order": ["mtbfTarget", "criticalThreshold", "warningThreshold"]
       },
       "blueprintIdentifier": "pagerdutyService"
     },
     "invocationMethod": {
       "type": "UPSERT_ENTITY",
       "blueprintIdentifier": "pagerdutyService",
       "mapping": {
         "identifier": "{{.entity.identifier}}",
         "properties": {
           "mtbfTarget": "{{.inputs.mtbfTarget}}",
           "mtbfCriticalThreshold": "{{.inputs.criticalThreshold}}",
           "mtbfWarningThreshold": "{{.inputs.warningThreshold}}"
         }
       }
     },
     "requiredApproval": false
   }
   ```

4. Click `Save`.

## Create MTBF monitoring automation[â](#create-mtbf-monitoring-automation "Direct link to Create MTBF monitoring automation")

### Set up MTBF monitoring service

Before creating the automation, we need to set up a dedicated PagerDuty service to receive MTBF threshold breach alerts. This ensures all MTBF-related incidents are centrally managed and don't get mixed with incidents from the monitored services themselves.

Create a new PagerDuty service with the following details:

* **Name**: `MTBF Threshold Monitor`.
* **Description**: `Monitors MTBF thresholds across all services and alerts when targets are breached`.
* **Integration Type**: Events API v2.

Create PagerDuty service

If you need help creating a PagerDuty service, you can use Port's self-service action described in our [Create PagerDuty Service guide](/guides/all/create-pagerduty-service.md). This provides both webhook and GitHub workflow options for automated service creation.

### Add routing key to Port secrets

Once you've created your MTBF monitoring service, add its routing key to Port secrets:

1. In your PagerDuty service, go to the **Integrations** tab and copy the **Integration Key** (routing key).

2. In Port, click on the `...` button in the top right corner of your Port application.

3. Click on **Credentials**.

4. Click on the `Secrets` tab.

5. Click on `+ Secret` and add the following:

   * **Key**: `MONITORING_SVC_PAGERDUTY_ROUTING_KEY`.
   * **Value**: Your MTBF monitoring service integration key (e.g., `a1b2c3d4e5f6789012345678901234567890abcd`).

6. Click `Save`.

### Create the automation

Set up an automation to monitor MTBF thresholds and trigger alerts:

1. Head to the [automation](https://app.getport.io/settings/automations) page.

2. Click on the `+ Automation` button.

3. Copy and paste the following JSON configuration:

   **MTBF threshold monitoring automation (click to expand)**

   Create in Port

   ```
   {
     "identifier": "mtbf_threshold_monitor",
     "title": "MTBF Threshold Monitor",
     "description": "Monitor MTBF values against set thresholds and trigger alerts",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ENTITY_UPDATED",
         "blueprintIdentifier": "pagerdutyService"
       },
       "condition": {
         "type": "JQ",
         "expressions": [
           ".diff.after.properties.mtbf_30_days",
           ".diff.after.properties.mtbfTarget",
           "(.diff.after.properties.mtbf_30_days / .diff.after.properties.mtbfTarget * 100) < .diff.after.properties.mtbfCriticalThreshold"
         ],
         "combinator": "and"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://events.pagerduty.com/v2/enqueue",
       "method": "POST",
       "headers": {
         "Content-Type": "application/json"
       },
       "body": {
         "routing_key": "{{.secrets.MONITORING_SVC_PAGERDUTY_ROUTING_KEY}}",
         "event_action": "trigger",
         "payload": {
           "summary": "MTBF Critical Threshold Breached: {{.event.diff.after.title}}",
           "source": "Port MTBF Monitor",
           "severity": "critical",
           "custom_details": {
             "service": "{{.event.diff.after.title}}",
             "current_mtbf": "{{.event.diff.after.properties.mtbf_30_days}}",
             "target_mtbf": "{{.event.diff.after.properties.mtbfTarget}}",
             "threshold_breached": "Critical"
           }
         }
       }
     },
     "publish": true
   }
   ```

4. Click `Save`.

## Visualize MTBF metrics[â](#visualize-mtbf-metrics "Direct link to Visualize MTBF metrics")

With your MTBF data and monitoring actions in place, you can create a dedicated dashboard in Port to visualize service reliability, track MTBF trends, and quickly identify services that need attention.

### Create MTBF dashboard[â](#create-mtbf-dashboard "Direct link to Create MTBF dashboard")

1. Navigate to the [Catalog](https://app.getport.io/organization/catalog) page.

2. Click on the **`+ New`** button in the left sidebar.

3. Select **New dashboard**.

4. Name the dashboard **Service Reliability (MTBF) Monitoring**.

5. Input `Track and monitor Mean Time Between Failures for all services` under **Description**.

6. Select the `pagerduty` icon.

7. Click `Create`.

### Add MTBF widgets[â](#add-mtbf-widgets "Direct link to Add MTBF widgets")

Create the following widgets in your new dashboard:

**MTBF overview widget (click to expand)**

1. Click **`+ Widget`** and select **Number Chart**.

2. Title: `Average MTBF (30 days)` (add the `pagerduty` icon).

3. Select `Aggregate by property` chart type and choose **PagerDuty Service** blueprint.

4. Choose `MTBF (30 days)` property and `average` function.

5. Select `Hour` for **Average of** and set custom unit to `hours`.

6. Click `Save`.

**Low MTBF services widget (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title: `Services Requiring Attention` (add the `Alert` icon).

3. Choose the **PagerDuty Service** blueprint.

4. Add this filter to show services with low MTBF:

   ```
     {
       "combinator": "or",
       "rules": [
         {
           "property": "mtbf_30_days",
           "operator": "<",
           "value": 168
         },
         {
           "property": "incidents30Days",
           "operator": ">",
           "value": 5
         }
       ]
     }
   ```

5. Click `Save`.

**High incident volume services widget (click to expand)**

1. Click **`+ Widget`** and select **Number Chart**.

2. Title: `Total Incidents (30 days)` (add the `Alert` icon).

3. Select `Count entities` chart type and choose **PagerDuty Service** blueprint.

4. Choose `Incidents (30 days)` property and `count` function.

5. Set Unit of measurement to `custom` and type **incidents**.

6. Click `Save`.

**MTBF threshold compliance widget (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title: `MTBF Threshold Compliance` (add the `Target` icon)

3. Choose the **PagerDuty Service** blueprint.

4. Click on `Save`.

5. Click on the `...` button in the top right corner and choose `Customize table`.

6. Group table by `mtbfCriticalThreshold` property.

7. Click on the `Save` icon in the top right corner.

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

1. **Verify MTBF calculations:**

   * Navigate to your [PagerDuty Service catalog](https://app.getport.io/organization/catalog).
   * Open any service and check that MTBF values are populated.
   * Verify the MTBF trend shows the correct status.

2. **Test the Generate MTBF Report action:**

   * Go to a service with incident history.
   * Click `Generate MTBF Report`.
   * Select a time range and execute the action.
   * Review the detailed service information returned.

3. **Set reliability targets:**

   * Click `Set MTBF Target` on a critical service.
   * Set an appropriate target (e.g., 168 hours for weekly failures).
   * Configure warning (75%) and critical (50%) thresholds.

4. **Monitor the dashboard:**

   * Open your **Service Reliability (MTBF) Monitoring** dashboard.
   * Review services requiring attention.
   * Check MTBF trends and target compliance.

## Best practices[â](#best-practices "Direct link to Best practices")

* **Set realistic targets**: Base MTBF targets on historical performance and business requirements.
* **Monitor trends**: Focus on trend direction rather than absolute values - improving trends indicate better reliability.
* **Investigate degrading services**: Services with declining MTBF need immediate attention and investigation.
* **Regular review**: Schedule weekly reviews of MTBF metrics with engineering teams.
* **Combine with MTTR**: Use MTBF alongside MTTR metrics for comprehensive reliability monitoring.

## Related guides[â](#related-guides "Direct link to Related guides")

* **[Manage and visualize your PagerDuty incidents](/guides/all/manage-and-visualize-pagerduty-incidents.md)**: Complete incident management with PagerDuty.
* **[Track SLOs and SLIs for services](/guides/all/track-slos-and-slis-for-services.md)**: Implement comprehensive service level monitoring.
* **[Acknowledge Incident In PagerDuty](/guides/all/acknowledge-incident.md)**: Handle incident acknowledgment workflows.
* **[Resolve an Incident in PagerDuty](/guides/all/resolve-incident.md)**: Manage incident resolution processes.

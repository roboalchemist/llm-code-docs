# Source: https://docs.acceldata.io/documentation/working-with-notification-templates.md

# Working With Notification Templates

## Accessing Notification Templates

### Navigation

1. In ADOC, go to **Settings**. 
2. Select **Notifications**. 
3. Click **Notification Templates**.

You’ll see a list of existing templates and template groups (if configured).

## Creating a Notification Template

### Create the Template Group

1. On the **Notification Templates** page, click **Create Template**.
2. Enter:
    1. **Name**: Use something descriptive (e.g., `Prod – DQ – Slack & PagerDuty`)
    2. **Description** (Optional): Include purpose and audience, e.g., “On-call alerts for prod DQ policies”

3. Click **Save**.

You’ll be redirected to the **Edit Notification Template** page for this new group.

## Customizing Templates by Source and Channel

Templates in a group are defined **per source type and per channel**.

### Select Source Type and Channel

In the **Edit Notification Template** page:

1. From the left panel, choose a **Source Type** (for example, `Data Quality`, `Pipeline Monitoring`, `Profile`).
2. Select a **Channel**:
    1. Email
    2. Webhook
    3. Slack
    4. Google Chat
    5. Microsoft Teams
    6. ServiceNow
    7. Jira

ADOC loads the **system template** for that combination as a starting point.

### Edit Subject / Content

For each channel:

| **Channel** | **What You Edit** | 
| ---- | ---- | 
| Email | **Subject** and **Body** (HTML or plain text) | 
| Webhook | **JSON payload** content | 
| Slack | **Block Kit JSON** body | 
| Google Chat | **Card JSON** body | 
| Microsoft Teams | **MessageCard / Adaptive Card JSON** | 
| ServiceNow | Plain text body or JSON fields | 
| Jira | JSON payload (issue fields / ADF document) | 


You write the content in **FreeMarker Template Language (FTL)** using variables such as: `${policy.name}`, `${execution.resultStatus}`, `${result.qualityScore}`, etc.

For Jira and ServiceNow, the first test **creates** a record; subsequent tests **update the same** record.

## Associating Template Groups to Notification Groups

Once your Template Group is ready:

1. Navigate to **Settings** &gt; **Notifications** &gt; **Notification Groups**.
2. Open or create a **Notification Group**.
3. In the group configuration, select your **Notification Template Group**.
4. Click **Save**.

From now on, alerts that use that **Notification Group** will:

- Use your **custom templates** when available.
- Fall back to **system templates** for source+channel combinations you haven’t customized.

| **Concept** | **Relationship** | 
| ---- | ---- | 
| Notification Group | Who receives the alert and via which channels | 
| Template Group | How each alert looks for each channel and source type | 


## ADOC Variable Model

Variables are exposed to templates based on **policy type** and **execution context**. You can explore them from the **Variables** tab (right panel) in the editor.

Below is a **consolidated reference** of the key categories. Exact availability may vary by source type.

### Variable Categories

| **Category** | **What It Describes** | **Typical Prefix** | 
| ---- | ---- | ---- | 
| Execution Context | Result, severity, timestamps, messages | `execution` | 
| Policy Information | Policy id, name, type, description, tags | `policy` | 
| Data Quality Results | Scores, row counts, rule outcomes | `result`, `rule` | 
| Reconciliation Results | Cross-system record comparison | `result`, `reconciliation` | 
| Schema Drift | Structural changes to assets | `drift` | 
| Data Drift | Distribution changes | `drift` | 
| Freshness | Expected vs. actual arrival times | `freshness` | 
| Pipeline Monitoring | Pipeline execution metrics and errors | `pipeline` | 
| Environmental Context | Tenant, domains, assets, integrations | `tenant`, `asset`, `integration` | 
| Incident Context | Incident entity for failures/warnings only | `incident`, `severity`, `status`, etc. | 


## Detailed Variable Reference

Note This table focuses on the most heavily used fields. Your Variables panel in ADOC is the source of truth for exact names and availability.

### Execution Context

| **Variable** | **Type** | **Description** | **Example Usage** | 
| ---- | ---- | ---- | ---- | 
| `execution.resultStatus` | String | Execution result: SUCCESS / WARNING / FAILED / ERRORED | `${execution.resultStatus}` | 
| `execution.severity` | String | Alert severity: Critical / High / Medium / Low | `${execution.severity}` | 
| `execution.startTime` | Timestamp | Policy execution start time | `${execution.startTime?string["yyyy-MM-dd HH:mm:ss"]}` | 
| `execution.endTime` | Timestamp | Policy execution end time | `${execution.endTime?string["yyyy-MM-dd HH:mm:ss"]}` | 
| `execution.id` | Number | Unique execution identifier | `${execution.id}` | 
| `execution.message` | String | Execution details / error message | `${execution.message}` | 


### Policy Information

| **Variable** | **Type** | **Description** | **Example Usage** | 
| ---- | ---- | ---- | ---- | 
| `policy.name` | String | Human-readable policy name | `${policy.name}` | 
| `policy.id` | Number | Unique policy identifier | `${policy.id}` | 
| `policy.type` | String | Policy type (DATA_QUALITY, RECONCILIATION, etc.) | `${policy.type}` | 
| `policy.description` | String | Policy description | `${policy.description}` | 
| `policy.scheduled` | Boolean | Whether the policy runs on schedule | `${policy.scheduled?string('Yes','No')}` | 
| `policy.tags` | Array | Tags assigned to policy | `${policy.tags?join(", ")}` | 


### Data Quality Results

Applies to Data Quality policies.

| **Variable** | **Type** | **Description** | **Example Usage** | 
| ---- | ---- | ---- | ---- | 
| `result.qualityScore` | Number | Overall quality score (%) | `${result.qualityScore}%` | 
| `result.totalRowsScanned` | Number | Total rows evaluated | `${result.totalRowsScanned?string[",###"]}` | 
| `result.rowsPassed` | Number | Rows that passed all rules | `${result.rowsPassed}` | 
| `result.rowsFailed` | Number | Rows that failed one or more rules | `${result.rowsFailed}` | 
| `result.warningRows` | Number | Rows in warning threshold | `${result.warningRows!0}` | 
| `result.totalRules` | Number | Number of rules evaluated | `${result.totalRules}` | 
| `result.rulesPassed` | Number | Rules that passed | `${result.rulesPassed}` | 
| `result.rulesFailed` | Number | Rules that failed | `${result.rulesFailed}` | 


**Rule-level details** are typically exposed via a `rules` collection:

| **Field Name** | **Description** | 
| ---- | ---- | 
| `rule.name` | Rule name | 
| `rule.description` | Rule description | 
| `rule.status` | FAILED / PASSED | 
| `rule.failedRows` | (If available) Number of bad rows | 


### Reconciliation Results

Applies to reconciliation policies.

| **Variable** | **Type** | **Description** | **Example** **Usage** | 
| ---- | ---- | ---- | ---- | 
| `result.totalRecords` | Number | Total records compared | `${result.totalRecords}` | 
| `result.matchedRecords` | Number | Records that match | `${result.matchedRecords}` | 
| `result.unmatchedRecords` | Number | Records that do not match | `${result.unmatchedRecords}` | 
| `result.equalityPercentage` | Number | Percentage of equality | `${result.equalityPercentage}%` | 
| `result.leftRowCount` | Number | Row count in left/source system | `${result.leftRowCount}` | 
| `result.rightRowCount` | Number | Row count in right/target system | `${result.rightRowCount}` | 
| `reconciliation.leftDataSource` | String | Left/source system identifier | `${reconciliation.leftDataSource}` | 
| `reconciliation.rightDataSource` | String | Right/target system identifier | `${reconciliation.rightDataSource}` | 
| `reconciliation.joinKeys` | Array | Join keys used for matching records | `${reconciliation.joinKeys?join(", ")}` | 


### Schema Drift

Applies to schema drift / structure monitoring policies.

| **Variable** | Type | **Description** | **Example Usage** | 
| ---- | ---- | ---- | ---- | 
| `drift.addedColumns` | Array | Newly added columns | `${drift.addedColumns?join(", ")}` | 
| `drift.removedColumns` | Array | Removed columns | `${drift.removedColumns?join(", ")}` | 
| `drift.modifiedColumns` | Array | Columns with type or constraint changes | `${drift.modifiedColumns?join(", ")}` | 
| `drift.lastAlteredTime` | Timestamp | Most recent schema modification | `${drift.lastAlteredTime?string["yyyy-MM-dd HH:mm:ss"]}` | 
| `drift.changeCount` | Number | Total changes detected | `${drift.changeCount}` | 


Example snippet:

```none
<#if drift.addedColumns?has_content>
  New columns: ${drift.addedColumns?join(", ")}
</#if>
```



### Data Drift

| **Variable** | **Type** | **Description** | 
| ---- | ---- | ---- | 
| `drift.driftScore` | Number | Overall drift score (change magnitude) | 
| `drift.driftedColumns` | Array | Columns with significant distribution changes | 


### Freshness

| **Variable** | **Type** | **Description** | 
| ---- | ---- | ---- | 
| `freshness.expectedTime` | Timestamp | When data was expected | 
| `freshness.actualTime` | Timestamp | When data actually arrived | 
| `freshness.delayMinutes` | Number | Delay in minutes | 
| `freshness.expectedBatchCount` | Number | Expected batch count (if batch-based) | 
| `freshness.actualBatchCount` | Number | Actual batch count | 
| `freshness.warningThreshold` | Number | Warning threshold in minutes | 
| `freshness.failureThreshold` | Number | Failure threshold in minutes | 


### Pipeline Monitoring

Applies to pipeline monitoring policies.

| **Variable** | **Type** | **Description** | 
| ---- | ---- | ---- | 
| `pipeline.id` | Number | Pipeline identifier | 
| `pipeline.name` | String | Pipeline name | 
| `pipeline.status` | String | `SUCCESS`, `FAILED`, etc. | 
| `pipeline.startTime` | Timestamp | Start time | 
| `pipeline.endTime` | Timestamp | End time | 
| `pipeline.duration` | Number | Duration (seconds) | 
| `pipeline.recordsProcessed` | Number | Records processed | 
| `pipeline.bytesProcessed` | Number | Bytes processed | 
| `pipeline.errorMessage` | String | Error message for failed executions | 
| `pipeline.errorType` | String | Error category | 
| `pipeline.dependencies` | Array | Upstream / downstream dependencies | 


### Environmental Context

| **Variable** | **Type** | **Description** | 
| ---- | ---- | ---- | 
| `tenant.name` | String | Tenant name | 
| `tenant.id` | String | Unique tenant identifier | 
| `domains` | Array | Logical domains associated with the asset | 
| `asset.name` | String | Data asset (table / file / view) name | 
| `asset.id` | String | Unique asset identifier | 
| `asset.type` | String | Asset type category | 
| `integration.name` | String | Related integration name | 
| `integration.id` | String | Related integration id | 


### Incident Variables (Failures / Warnings Only)

Available only when an incident is created (FAILED / WARNING executions).

| **Variable** | **Type** | **Description** | 
| ---- | ---- | ---- | 
| `incidentId` | String | Unique incident identifier | 
| `createdAt` | Timestamp | Incident creation time | 
| `updatedAt` | Timestamp | Last updated time | 
| `severity` | String | Incident severity | 
| `status` | String | Incident status | 
| `totalOccurrences` | Number | Number of times this incident occurred | 
| `openInAccelDataUrl` | String | Deep link to incident / execution in ADOC | 


These **are not available** for `SUCCESS` runs. Design templates either to:

- Use conditionals to check availability, or
- Have separate templates for success vs. failure notifications.

## Working With Data Types in FreeMarker

### Booleans

FreeMarker is strict about booleans. Do **not** use `${policy.scheduled}` directly. Instead:

```none
Scheduled: ${policy.scheduled?string('Yes','No')}
```



or:

```none
Scheduled (raw): ${policy.scheduled?c}
```



### Arrays and Collections

Use `?join` for simple lists:

```none
Tags: ${policy.tags?join(", ")}
```



Or iterate:

```none
<#if policy.tags?has_content>
  <#list policy.tags as tag>
    - ${tag}
  </#list>
<#else>
  No tags configured.
</#if>
```



### Null Safety and Defaults

Use `!` to provide default values:

```none
Warning rows: ${result.warningRows!0}
Link: ${openInAccelDataUrl!"Not available"}
```



Use `??` to test if a variable exists:

```none
<#if result.qualityScore??>
  Score: ${result.qualityScore}%
<#else>
  Score not available.
</#if>
```



### Number and Date Formatting

```none
Total Rows: ${result.totalRowsScanned?string[",###"]}
Execution Time: ${execution.startTime?string["yyyy-MM-dd HH:mm:ss"]}
```



## Basic Template Patterns

### Interpolation

```none
Policy ${policy.name} finished with status ${execution.resultStatus}.
```



### Conditionals

```none
<#if execution.resultStatus == "SUCCESS">
  ✅ Check passed for ${policy.name}
<#elseif execution.resultStatus == "WARNING">
  ⚠ Check completed with warnings
<#else>
  🚨 Check failed
</#if>
```



### Iteration

```none
<#list rules as rule>
  - ${rule.name}: ${rule.status}
</#list>
```



## Working Template Examples

This section provides complete, production-ready templates for common notification scenarios. These templates demonstrate best practices and can be used as starting points for your own customizations.

### Data Quality Email Alert - Comprehensive Format

This template provides detailed data quality information in a well-structured HTML email format.

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
    .header { background-color: <#if execution.resultStatus == "SUCCESS">#28a745<#elseif execution.resultStatus == "WARNING">#ffc107<#else>#dc3545</#if>; color: white; padding: 20px; text-align: center; }
    .content { padding: 20px; }
    .metric-box { display: inline-block; background: #f8f9fa; padding: 15px; margin: 10px; border-left: 4px solid #007bff; }
    .metric-label { font-size: 12px; color: #666; text-transform: uppercase; }
    .metric-value { font-size: 24px; font-weight: bold; color: #333; }
    .rule-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    .rule-table th { background: #007bff; color: white; padding: 10px; text-align: left; }
    .rule-table td { padding: 10px; border-bottom: 1px solid #ddd; }
    .status-pass { color: #28a745; font-weight: bold; }
    .status-fail { color: #dc3545; font-weight: bold; }
    .footer { background: #f8f9fa; padding: 15px; margin-top: 20px; text-align: center; font-size: 12px; }
  </style>
</head>
<body>
  <div class="header">
    <h1><#if execution.resultStatus == "SUCCESS">✓<#elseif execution.resultStatus == "WARNING">⚠<#else>✗</#if> Data Quality Alert</h1>
    <h2>${policy.name}</h2>
  </div>
  
  <div class="content">
    <h3>Execution Summary</h3>
    <p><strong>Status:</strong> ${execution.resultStatus}</p>
    <p><strong>Severity:</strong> ${execution.severity}</p>
    <p><strong>Asset:</strong> ${asset.name}</p>
    <p><strong>Execution Time:</strong> ${execution.startTime?string["yyyy-MM-dd HH:mm:ss"]} to ${execution.endTime?string["yyyy-MM-dd HH:mm:ss"]}</p>
    
    <h3>Key Metrics</h3>
    <div>
      <div class="metric-box">
        <div class="metric-label">Quality Score</div>
        <div class="metric-value">${result.qualityScore}%</div>
      </div>
      <div class="metric-box">
        <div class="metric-label">Rows Scanned</div>
        <div class="metric-value">${result.totalRowsScanned?string[",###"]}</div>
      </div>
      <div class="metric-box">
        <div class="metric-label">Rows Failed</div>
        <div class="metric-value">${result.rowsFailed?string[",###"]}</div>
      </div>
      <div class="metric-box">
        <div class="metric-label">Rules Failed</div>
        <div class="metric-value">${result.rulesFailed} / ${result.totalRules}</div>
      </div>
    </div>
    
    <#if result.rulesFailed gt 0>
    <h3>Failed Rules</h3>
    <table class="rule-table">
      <thead>
        <tr>
          <th>Rule Name</th>
          <th>Status</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <#list rules as rule>
          <#if rule.status == "FAILED">
        <tr>
          <td>${rule.name}</td>
          <td class="status-fail">${rule.status}</td>
          <td>${rule.description!""}</td>
        </tr>
          </#if>
        </#list>
      </tbody>
    </table>
    </#if>
    
    <#if execution.message?has_content>
    <h3>Additional Details</h3>
    <p>${execution.message}</p>
    </#if>
  </div>
  
  <div class="footer">
    <p>Policy: ${policy.name} (ID: ${policy.id}) | Tenant: ${tenant.name}</p>
    <p><a href="${openInAccelDataUrl!}"  style="color: #007bff;">View in ADOC</a></p>
  </div>
</body>
</html>
```



### Slack Data Quality Alert - Block Kit Format

This template creates a rich, formatted Slack message using Block Kit for data quality alerts.

```json
{
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "<#if execution.resultStatus == 'SUCCESS'>✅<#elseif execution.resultStatus == 'WARNING'>⚠️<#else>🚨</#if> Data Quality: ${policy.name}"
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Status:*\n${execution.resultStatus}"
        },
        {
          "type": "mrkdwn",
          "text": "*Severity:*\n${execution.severity}"
        },
        {
          "type": "mrkdwn",
          "text": "*Quality Score:*\n${result.qualityScore}%"
        },
        {
          "type": "mrkdwn",
          "text": "*Asset:*\n${asset.name}"
        }
      ]
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Execution Details:*\n• Rows Scanned: ${result.totalRowsScanned?string[",###"]}\n• Rows Failed: ${result.rowsFailed?string[",###"]}\n• Rules Failed: ${result.rulesFailed} of ${result.totalRules}\n• Time: ${execution.startTime?string["HH:mm:ss"]}"
      }
    },
    <#if result.rulesFailed gt 0>
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Failed Rules:*\n<#list rules as rule><#if rule.status == 'FAILED'>• ${rule.name}\n</#if></#list>"
      }
    },
    </#if>
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "View in ADOC"
          },
          "url": "${openInAccelDataUrl!}",
          "style": "primary"
        }
      ]
    },
    {
      "type": "context",
      "elements": [
        {
          "type": "mrkdwn",
          "text": "Policy ID: ${policy.id} | Execution ID: ${execution.id} | ${execution.endTime?string["yyyy-MM-dd HH:mm:ss"]}"
        }
      ]
    }
  ]
}
```



### PagerDuty Webhook - Incident Trigger

This template creates a PagerDuty-compatible webhook payload for critical data quality failures.

```json
{
  "routing_key": "YOUR_INTEGRATION_KEY",
  "event_action": "trigger",
  "payload": {
    "summary": "Data Quality Failure: ${policy.name} - ${asset.name}",
    "severity": "<#if execution.severity == 'Critical'>critical<#elseif execution.severity == 'High'>error<#elseif execution.severity == 'Medium'>warning<#else>info</#if>",
    "source": "${tenant.name}",
    "component": "${asset.name}",
    "group": "data-quality",
    "class": "${policy.type}",
    "custom_details": {
      "policy_name": "${policy.name}",
      "policy_id": "${policy.id}",
      "execution_id": "${execution.id}",
      "asset": "${asset.name}",
      "quality_score": "${result.qualityScore}%",
      "rows_scanned": ${result.totalRowsScanned},
      "rows_failed": ${result.rowsFailed},
      "rules_failed": ${result.rulesFailed},
      "total_rules": ${result.totalRules},
      "execution_time": "${execution.startTime?string["yyyy-MM-dd HH:mm:ss"]}",
      "status": "${execution.resultStatus}",
      "severity": "${execution.severity}",
      <#if execution.message?has_content>"message": "${execution.message}",</#if>
      "adoc_link": "${openInAccelDataUrl!}"
    }
  },
  "dedup_key": "adoc-dq-${policy.id}-${execution.id}",
  "client": "Acceldata ADOC",
  "client_url": "${openInAccelDataUrl!}"
}
```



### ServiceNow Incident Creation

This template creates a ServiceNow incident with appropriate field mappings.

```json
{
  "short_description": "Data Quality ${execution.resultStatus}: ${policy.name}",
  "description": "Data Quality Alert Details:\n\nPolicy: ${policy.name}\nAsset: ${asset.name}\nStatus: ${execution.resultStatus}\nSeverity: ${execution.severity}\n\nMetrics:\n- Quality Score: ${result.qualityScore}%\n- Rows Scanned: ${result.totalRowsScanned?string[",###"]}\n- Rows Failed: ${result.rowsFailed?string[",###"]}\n- Rules Failed: ${result.rulesFailed} of ${result.totalRules}\n\nExecution Time: ${execution.startTime?string["yyyy-MM-dd HH:mm:ss"]} to ${execution.endTime?string["yyyy-MM-dd HH:mm:ss"]}\n\n<#if result.rulesFailed gt 0>Failed Rules:\n<#list rules as rule><#if rule.status == 'FAILED'>- ${rule.name}: ${rule.description!''}\n</#if></#list></#if>\n<#if execution.message?has_content>Additional Details:\n${execution.message}\n</#if>\nView in ADOC: ${openInAccelDataUrl!}",
  "impact": "<#if execution.severity == 'Critical'>1<#elseif execution.severity == 'High'>2<#else>3</#if>",
  "urgency": "<#if execution.resultStatus == 'FAILED'>1<#elseif execution.resultStatus == 'WARNING'>2<#else>3</#if>",
  "category": "Data Quality",
  "subcategory": "${policy.type}",
  "caller_id": "${tenant.name}",
  "u_source_system": "Acceldata ADOC",
  "u_policy_name": "${policy.name}",
  "u_policy_id": "${policy.id}",
  "u_execution_id": "${execution.id}",
  "u_asset": "${asset.name}",
  "u_quality_score": "${result.qualityScore}",
  "work_notes": "Execution ID: ${execution.id}\nPolicy ID: ${policy.id}\nTenant: ${tenant.name}\nDomains: ${domains?join(', ')!''}"
}
```



### Pipeline Monitoring Email - Failure Alert

This template provides comprehensive pipeline failure information.

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
    .alert-banner { background-color: #dc3545; color: white; padding: 20px; text-align: center; font-size: 24px; font-weight: bold; }
    .content { padding: 20px; }
    .info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0; }
    .info-item { background: #f8f9fa; padding: 15px; border-left: 4px solid #dc3545; }
    .label { font-weight: bold; color: #666; font-size: 12px; text-transform: uppercase; }
    .value { font-size: 18px; color: #333; margin-top: 5px; }
    .error-box { background: #fff3cd; border: 1px solid #ffc107; padding: 15px; margin: 20px 0; border-radius: 5px; }
  </style>
</head>
<body>
  <div class="alert-banner">
    🚨 Pipeline Failure Alert
  </div>
  
  <div class="content">
    <h2>${pipeline.name}</h2>
    
    <div class="info-grid">
      <div class="info-item">
        <div class="label">Status</div>
        <div class="value">${pipeline.status}</div>
      </div>
      <div class="info-item">
        <div class="label">Severity</div>
        <div class="value">${execution.severity}</div>
      </div>
      <div class="info-item">
        <div class="label">Start Time</div>
        <div class="value">${pipeline.startTime?string["yyyy-MM-dd HH:mm:ss"]}</div>
      </div>
      <div class="info-item">
        <div class="label">Duration</div>
        <div class="value">${pipeline.duration} seconds</div>
      </div>
      <div class="info-item">
        <div class="label">Records Processed</div>
        <div class="value">${pipeline.recordsProcessed?string[",###"]}</div>
      </div>
      <div class="info-item">
        <div class="label">Bytes Processed</div>
        <div class="value">${pipeline.bytesProcessed?string[",###"]}</div>
      </div>
    </div>
    
    <#if pipeline.errorMessage?has_content>
    <div class="error-box">
      <h3>Error Details</h3>
      <p><strong>Error Type:</strong> ${pipeline.errorType!""}</p>
      <p><strong>Message:</strong> ${pipeline.errorMessage}</p>
    </div>
    </#if>
    
    <#if pipeline.dependencies?has_content>
    <h3>Affected Dependencies</h3>
    <ul>
      <#list pipeline.dependencies as dep>
      <li>${dep}</li>
      </#list>
    </ul>
    </#if>
    
    <p style="margin-top: 30px;">
      <a href="${openInAccelDataUrl!}" style="background: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block;">View Pipeline Details</a>
    </p>
    
    <p style="margin-top: 20px; color: #666; font-size: 12px;">
      Pipeline ID: ${pipeline.id} | Execution ID: ${execution.id} | Tenant: ${tenant.name}
    </p>
  </div>
</body>
</html>
```



### Reconciliation Slack Alert - Mismatch Notification

This template alerts on reconciliation mismatches between source and target systems.

```json
{
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "⚠️ Reconciliation Mismatch Detected"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Policy:* ${policy.name}\n*Status:* ${execution.resultStatus}"
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Source System:*\n${reconciliation.leftDataSource}\n${result.leftRowCount?string[",###"]} records"
        },
        {
          "type": "mrkdwn",
          "text": "*Target System:*\n${reconciliation.rightDataSource}\n${result.rightRowCount?string[",###"]} records"
        }
      ]
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Matched Records:*\n${result.matchedRecords?string[",###"]}"
        },
        {
          "type": "mrkdwn",
          "text": "*Unmatched Records:*\n${result.unmatchedRecords?string[",###"]}"
        },
        {
          "type": "mrkdwn",
          "text": "*Equality:*\n${result.equalityPercentage}%"
        },
        {
          "type": "mrkdwn",
          "text": "*Severity:*\n${execution.severity}"
        }
      ]
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Join Keys:* ${reconciliation.joinKeys?join(', ')}"
      }
    },
    {
      "type": "divider"
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Investigate in ADOC"
          },
          "url": "${openInAccelDataUrl!}",
          "style": "danger"
        }
      ]
    }
  ]
}
```



### Schema Drift Email - Change Summary

This template provides a clear summary of schema changes detected.

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
    .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 25px; text-align: center; }
    .content { padding: 20px; max-width: 800px; margin: 0 auto; }
    .change-section { margin: 20px 0; padding: 15px; border-radius: 5px; }
    .added { background: #d4edda; border-left: 5px solid #28a745; }
    .removed { background: #f8d7da; border-left: 5px solid #dc3545; }
    .modified { background: #fff3cd; border-left: 5px solid #ffc107; }
    .change-title { font-weight: bold; font-size: 16px; margin-bottom: 10px; }
    .column-list { list-style: none; padding-left: 20px; }
    .column-list li { padding: 5px 0; }
    .metadata { background: #f8f9fa; padding: 15px; margin-top: 20px; border-radius: 5px; }
  </style>
</head>
<body>
  <div class="header">
    <h1>📊 Schema Drift Detected</h1>
    <h2>${policy.name}</h2>
  </div>
  
  <div class="content">
    <p><strong>Asset:</strong> ${asset.name}</p>
    <p><strong>Detection Time:</strong> ${execution.endTime?string["yyyy-MM-dd HH:mm:ss"]}</p>
    <p><strong>Total Changes:</strong> ${drift.changeCount}</p>
    <p><strong>Last Schema Alteration:</strong> ${drift.lastAlteredTime?string["yyyy-MM-dd HH:mm:ss"]}</p>
    
    <#if drift.addedColumns?has_content>
    <div class="change-section added">
      <div class="change-title">✅ Added Columns (${drift.addedColumns?size})</div>
      <ul class="column-list">
        <#list drift.addedColumns as column>
        <li>${column}</li>
        </#list>
      </ul>
    </div>
    </#if>
    
    <#if drift.removedColumns?has_content>
    <div class="change-section removed">
      <div class="change-title">❌ Removed Columns (${drift.removedColumns?size})</div>
      <ul class="column-list">
        <#list drift.removedColumns as column>
        <li>${column}</li>
        </#list>
      </ul>
    </div>
    </#if>
    
    <#if drift.modifiedColumns?has_content>
    <div class="change-section modified">
      <div class="change-title">⚠️ Modified Columns (${drift.modifiedColumns?size})</div>
      <ul class="column-list">
        <#list drift.modifiedColumns as column>
        <li>${column}</li>
        </#list>
      </ul>
    </div>
    </#if>
    
    <div class="metadata">
      <p><strong>Policy Description:</strong> ${policy.description!""}</p>
      <p><strong>Domains:</strong> ${domains?join(', ')!""}</p>
      <p><a href="${openInAccelDataUrl!}" style="color: #667eea; font-weight: bold;">View Full Details in ADOC →</a></p>
    </div>
  </div>
</body>
</html>
```



### Data Freshness Microsoft Teams Alert

This template creates an Adaptive Card for Microsoft Teams to alert on data freshness issues.

```json
{
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "type": "AdaptiveCard",
  "version": "1.4",
  "body": [
    {
      "type": "Container",
      "style": "<#if execution.resultStatus == 'FAILED'>attention<#elseif execution.resultStatus == 'WARNING'>warning<#else>good</#if>",
      "items": [
        {
          "type": "TextBlock",
          "text": "<#if execution.resultStatus == 'FAILED'>⏰<#elseif execution.resultStatus == 'WARNING'>⚠️<#else>✅</#if> Data Freshness Alert",
          "weight": "bolder",
          "size": "large",
          "wrap": true
        },
        {
          "type": "TextBlock",
          "text": "${policy.name}",
          "size": "medium",
          "wrap": true
        }
      ]
    },
    {
      "type": "FactSet",
      "facts": [
        {
          "title": "Status",
          "value": "${execution.resultStatus}"
        },
        {
          "title": "Severity",
          "value": "${execution.severity}"
        },
        {
          "title": "Asset",
          "value": "${asset.name}"
        },
        {
          "title": "Expected Time",
          "value": "${freshness.expectedTime?string['HH:mm:ss']}"
        },
        {
          "title": "Actual Time",
          "value": "${freshness.actualTime?string['HH:mm:ss']}"
        },
        {
          "title": "Delay",
          "value": "${freshness.delayMinutes} minutes"
        }
      ]
    },
    <#if freshness.expectedBatchCount??>
    {
      "type": "FactSet",
      "facts": [
        {
          "title": "Expected Batches",
          "value": "${freshness.expectedBatchCount}"
        },
        {
          "title": "Actual Batches",
          "value": "${freshness.actualBatchCount}"
        }
      ]
    },
    </#if>
    {
      "type": "TextBlock",
      "text": "Thresholds: Warning at ${freshness.warningThreshold}min, Failure at ${freshness.failureThreshold}min",
      "size": "small",
      "wrap": true,
      "spacing": "medium"
    }
  ],
  "actions": [
    {
      "type": "Action.OpenUrl",
      "title": "View in ADOC",
      "url": "${openInAccelDataUrl!}"
    }
  ]
}
```



### Generic Webhook - Multi-Purpose Format

This template provides a flexible JSON structure suitable for most webhook integrations.

```json
{
  "notification_type": "adoc_alert",
  "timestamp": "${execution.endTime?string['yyyy-MM-dd\'T\'HH:mm:ss\'Z\'']}",
  "alert": {
    "title": "${policy.type}: ${policy.name}",
    "status": "${execution.resultStatus}",
    "severity": "${execution.severity}",
    "message": "${execution.message!''}"
  },
  "policy": {
    "id": ${policy.id},
    "name": "${policy.name}",
    "type": "${policy.type}",
    "description": "${policy.description!''}",
    "scheduled": ${policy.scheduled?c},
    "tags": [<#list policy.tags as tag>"${tag}"<#sep>, </#list>]
  },
  "execution": {
    "id": ${execution.id},
    "start_time": "${execution.startTime?string['yyyy-MM-dd\'T\'HH:mm:ss\'Z\'']}",
    "end_time": "${execution.endTime?string['yyyy-MM-dd\'T\'HH:mm:ss\'Z\'']}",
    "duration_seconds": ${(execution.endTime?long - execution.startTime?long) / 1000}
  },
  "asset": {
    "name": "${asset.name}",
    "id": "${asset.id}",
    "type": "${asset.type}"
  },
  "tenant": {
    "id": "${tenant.id}",
    "name": "${tenant.name}"
  },
  "context": {
    "domains": [<#list domains as domain>"${domain}"<#sep>, </#list>],
    "integration": {
      "name": "${integration.name!''}",
      "id": "${integration.id!''}"
    }
  },
  <#if policy.type == "DATA_QUALITY">
  "results": {
    "quality_score": ${result.qualityScore},
    "total_rows_scanned": ${result.totalRowsScanned},
    "rows_passed": ${result.rowsPassed},
    "rows_failed": ${result.rowsFailed},
    "warning_rows": ${result.warningRows!0},
    "total_rules": ${result.totalRules},
    "rules_passed": ${result.rulesPassed},
    "rules_failed": ${result.rulesFailed}
  },
  </#if>
  "links": {
    "adoc_url": "${openInAccelDataUrl!''}"
  }
}
```


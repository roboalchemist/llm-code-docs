# Source: https://docs.acceldata.io/documentation/best-practices--design-guidelines--and-troubleshooting.md

# Best Practices and Troubleshooting

## Principles of Effective Template Design

Effective notification templates follow three core principles:

1. **Clarity**: Notifications must be immediately understandable by recipients. Use concise wording, clear headers, structured sections, and consistent formatting.
2. **Actionability**: Every notification should help a user decide:_**“Do I need to act? If so, how quickly?”**_ This applies especially to alerts for failures, warnings, freshness delays, schema drift, and pipeline errors.
3. **Robustness**: Templates must render reliably even if data is missing, variables are null, execution results differ, or the alert structure changes in future versions.

These principles apply to all channels: Email, Webhook, Slack, Teams, Jira, ServiceNow, or any platform receiving a formatted payload.

## Structuring Notifications for Readability

Notifications should follow a consistent structure so users can quickly digest context and severity across all alert types.

Recommended structure:

- **Header**: Type of alert + severity icon
- **Summary**: 2–4 lines describing what happened
- **Key Metrics**: High-value KPIs that indicate severity
- **Detailed Section**: Rule-level or drift-level info (only when needed)
- **Action Links**: Direct link to ADOC or related systems
- **Footer**: Policy, asset, tenant, and execution identifiers

Teams receiving six or more alerts per week rely on consistent structure to scan quickly and act efficiently.

## Choosing What to Display

Not all variables should be displayed in every notification. Use the following guidelines:

- Use high-level metrics in chat-based channels (Slack, Teams, Google Chat).
- Use detailed tables and rule breakdowns in email notifications.
- Use structured machine-readable payloads for webhook targets (PagerDuty, automation systems).
- For Jira/ServiceNow, include enough diagnostic information so the ticket can be triaged without opening ADOC first.

## Boolean, Numeric, and Timestamp Formatting Rules

To avoid formatting errors or unreadable outputs, follow the formatting recommendations below.

### Boolean Formatting

Boolean values must always be formatted using conversion directives.

| **Boolean Variable Example** | **Recommended Formatting** | **Output Example** | 
| ---- | ---- | ---- | 
| `policy.scheduled` | `${policy.scheduled?string("Yes","No")}` | “Yes” or “No” | 
| `execution.alertEnabled` | `${execution.alertEnabled?c}` | true / false | 
| `rule.isBlocking` | `${rule.isBlocking?string("Blocking","Non-Blocking")}` | Blocking | 


### Numeric Formatting

Use string formatting for readability.

| **Value Type** | **Recommended Format** | **Example Output** | 
| ---- | ---- | ---- | 
| Row counts | ?string[",###"] | 1,234,555 | 
| Percentages | Append “%” or use multiplication if needed | 98% | 
| Durations | Provide units | 154 seconds | 


### Timestamp Formatting

Always format timestamps for human readability.

| **Variable** | **Recommended Format** | **Output Example** | 
| ---- | ---- | ---- | 
| `execution.startTime` | yyyy-MM-dd HH:mm:ss | 2025-01-17 13:05:22 | 
| `freshness.expectedTime` | HH:mm:ss | 02:00:00 | 
| `drift.lastAlteredTime` | yyyy-MM-dd | 2025-11-08 | 


## Designing Templates for Different Channels

Each channel has unique constraints and strengths.

**Email (HTML or Plain Text)**

- Best for detailed, long-form alerts
- Supports tables, sections, and rich formatting
- Should include full rule breakdowns and drift details

**Slack / Google Chat**

- Designed for short, scannable summaries
- Should contain only essential metrics
- Use concise blocks or markdown text
- Provide one primary action button

**Microsoft Teams**

- Uses Adaptive Cards with strict schema requirements
- Keep layouts simple and declarative
- Avoid long text blocks (Teams truncates long cards)

**Webhook**

- Must follow strict JSON structure
- Ideal for incident management systems and automation workflows
- Avoid human-language embellishments
- Validate JSON with external linters

**Jira / ServiceNow**

Tickets should summarize the issue

**Include**:

- Policy summary
- Severity
- Key metrics
- Full ADOC link
- Error messages

**Avoid**:

- Large tables
- Multi-level blocks
- Markdown (only Jira supports partial markdown)

## Template Safety: Defensive Techniques

Templates must be safe under all execution conditions (success, warnings, failures, missing fields, missing arrays).

**Key defensive patterns:**

1. **Null safety**
Use the “!” operator for default values:
${result.warningRows!0}
2. **Existence checks**
&lt;#if drift.modifiedColumns??&gt; … &lt;/#if&gt;
3. **Content checks**
&lt;#if rules?has_content&gt; … &lt;/#if&gt;
4. **Conditional severity sections**
&lt;#if execution.resultStatus == "FAILED"&gt; … &lt;/#if&gt;
5. **Avoid assuming arrays have elements**
Columns might be removed or empty; drift events may return empty arrays.

## Scalability and Maintainability Recommendations

Organizations with multiple teams often need multiple template groups. Use the following practices:

1. **Use consistent naming conventions**

**Example**: “DQ_Prod_Slack”, “DQ_Prod_Email”, “Reconciliation_Teams_Alerts”

2. **Group templates by source type, not by policy**
3. **Document which Notification Groups use which Template Group**
4. **Keep templates in version control (Git)**
5. **Require lightweight QA before production enablement**

## Common Mistakes and How to Avoid Them

This section lists the most common causes of broken templates.

**1. Boolean fields without formatting**

Cause: ${policy.scheduled} → fails

Fix: ${policy.scheduled?string("Yes","No")}

**2. Arrays inserted directly**

Cause: ${policy.tags} produces "[Ljava...]"

Fix: ${policy.tags?join(", ")}

**3. JSON webhooks failing to parse**

Cause: Unescaped quotes, trailing commas

Fix: Validate payload in JSONLint; reduce complex string interpolation.

**4. Missing variables for SUCCESS executions**

Incident variables never exist in successful runs. Templates must be checked before accessing.

**5. Slack / Teams rendering failures**

Common reasons:

- Wrong block type
- Invalid adaptive card field
- Unsupported emojis or formatting

## Troubleshooting Guide

Use the table below to identify and resolve issues.

| **Problem** | **Likely Cause** | **Resolution** | 
| ---- | ---- | ---- | 
| Notification failed to send | Template rendering error | Check for null variables, incorrect formatting, or collection misuse | 
| Variable displays literally (${policy.name}) | Typo or incorrect variable name | Verify exact variable spelling | 
| JSON webhook rejected | Invalid JSON structure | Validate JSON, remove trailing commas, quote all strings | 
| Boolean formatting error | Boolean interpolated directly | Use ?c or ?string() | 
| Missing fields on SUCCESS cases | Incident variables unavailable | Wrap in &lt;#if variable??&gt; checks | 
| Slack/Teams message not rendering | JSON schema mismatch | Validate in Slack Block Kit Builder or Teams Card Designer | 
| Excessively long notifications | Too much detail for channel | Move detailed sections to email only | 


## Operational Best Practices

**Separate success and failure templates when necessary**

Success notifications often need minimal formatting; failures require detail.

**Avoid embedding sensitive information**

Never include secrets, passwords, connection strings, or tokens.

**Test with multiple executions**

Test with:

- SUCCESS
- WARNING
- FAILED
- Missing drift arrays
- Zero failed rules
- Large numbers or long names

**Pilot before rollout**

Use test channels before linking templates to production Notification Groups.

## Governance and Change Management

Most organizations benefit from light governance around templates:

- Require review before modifying production templates
- Maintain a changelog with versioned template updates
- Train teams on FreeMarker basics
- Review templates quarterly to ensure relevance
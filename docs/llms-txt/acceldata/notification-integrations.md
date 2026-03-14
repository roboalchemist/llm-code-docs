# Source: https://docs.acceldata.io/documentation/notification-integrations.md

# Integrations

Notifications connect ADOC (Acceldata Data Observability Cloud) with other tools your teams already use. This ensures that alerts raised in ADOC automatically flow into systems like **ServiceNow** or **Jira**, where your teams manage incidents and track resolution.

By integrating ADOC with your ticketing or IT service systems, you:

- **Reduce manual effort** – alerts automatically become tickets.
- **Ensure faster response** – no delays in reporting issues.
- **Improve collaboration** – teams work from tools they already use.

Currently, ADOC supports integration with:

- **ServiceNow** (for IT service management)
- **Jira** (for incident and project tracking)

## Navigating to Integrations

To access integrations:

1. Log in to ADOC.
2. Click the **Settings** icon in the left navigation.
3. Select **Notification Integrations**.

You’ll see a list of available integrations, their status, and options to configure.

**Fields in the Integrations List**

| **Field** | **Description** | 
| ---- | ---- | 
| Name | Name of the integration (ServiceNow, Jira, etc.) | 
| Status | Whether the integration is active or not | 
| Last Updated On | Date the integration was last updated | 
| Edit Config | Opens configuration settings for the integration | 


## ServiceNow Integration

ServiceNow is commonly used by IT teams to manage incidents and service requests. By integrating ServiceNow with ADOC, alerts raised in ADOC can automatically create or update ServiceNow incidents.

ADOC supports two authentication methods:

- **Standard Integration** (username + password)
- **OAuth Integration** (recommended for security and control)

## 1. Standard Integration

This is the simpler setup, using direct credentials.

Steps:

1. In ADOC, navigate to **Settings** &gt; **Notifications** &gt; **Integrations**.
2. Select **ServiceNow** &gt; **Edit Config**.

Fill in the fields:

| **Field** | **Required** | **Description** | 
| ---- | ---- | ---- | 
| URL | Yes | The base URL of your ServiceNow instance | 
| Username | Yes | ServiceNow username with ITIL role | 
| Password | Yes | Corresponding password | 
| Assignment Groups | Optional | Route incidents to specific ServiceNow groups by providing their sys_id | 


**To get Assignment Group ID (sys_id):**

1. In **ServiceNow** &gt; **User Groups** (under Administrator).
2. Right-click the header &gt; Copy sys_id.
3. Paste into ADOC.
4. Click **Update** to save.

## 2. OAuth Integration (Recommended)

OAuth is a safer method that avoids sharing usernames and passwords. Instead, it uses secure tokens that can be managed or revoked.

**Why use OAuth?**

- Improves security by not storing user credentials.
- Gives users more control over data access.
- Allows administrators to revoke access if needed.

Note From **ADOC v2.8.2** onwards, you’ll see an Enable OAuth toggle in the ServiceNow integration screen.

### Step 1: Configure OAuth in ServiceNow

1. Log in to **ServiceNow** as Administrator.
2. Navigate to **OAuth Application**.
3. Click **Create an OAuth API** endpoint for external clients.
4. In **Application Registries**, enter:
    1. A **unique Name**
    2. A **Client Secret** (or let ServiceNow generate it)
    3. **Refresh Token Lifespan** (e.g., 8,640,000)
    4. **Access Token Lifespan** (e.g., 1800)

5. In the **Redirect URL**, enter: https://&lt;tenant_name&gt;.&lt;acceldata_base_domain&gt;/ui/oauth-success
6. Save and update the app.

Note The ServiceNow user must have the ITIL role enabled. Use a large refresh token lifespan, or the integration may stop working when the token expires.

### Step 2: Configure OAuth in ADOC

1. In ADOC, navigate to **Settings** &gt; **Notifications** &gt; **Integrations** &gt; **ServiceNow**.
2. Enable the **OAuth toggle**.

Fill in the fields:

| **Field** | **Required** | **Description** | 
| ---- | ---- | ---- | 
| Auth URL | Yes | https://&lt;instance&gt;.service-now.com/oauth_auth.do | 
| Token URL | Yes | https://&lt;instance&gt;.service-now.com/oauth_token.do | 
| Client ID | Yes | From ServiceNow OAuth application | 
| Client Secret | Yes | From ServiceNow OAuth application | 
| Caller ID | Yes | sys_id of user in ServiceNow | 
| Refresh Token Lifespan (sec) | Yes | Time before re-authentication is needed | 
| Assignment Groups | Optional | Add ServiceNow group sys_ids (as in Standard integration) | 


3. Click **Update & Authenticate**.
4. A popup will appear asking to allow access. Select **Allow**.

A success message confirms the integration is active.

## 3. Two-Way Sync (ADOC ↔ ServiceNow)

With two-way sync, updates flow in both directions:

- ADOC alerts create/update ServiceNow incidents.
- ServiceNow updates (status/priority) reflect back in ADOC.

Steps:

1. In ADOC, after configuring ServiceNow, click **Download Script** (business-rule.txt).
2. In **ServiceNow** &gt; **System Definition** &gt; **Business Rules**.
3. Click **New** and enter:
    1. **Name** (e.g., ADOC Sync)
    2. **Table** = Incident
    3. Check **Active** and **Advanced**

4. In **Advanced** &gt; **Script**, paste the business-rule.txt contents.
5. Save and enable.

### Severity Mapping: ADOC → ServiceNow

| **ADOC Severity** | **ServiceNow Mapping** | 
| ---- | ---- | 
| Critical | Impact: High, Urgency: High → Priority: Critical | 
| High | Impact: High, Urgency: Medium → Priority: High | 
| Medium | Impact: Medium, Urgency: Medium → Priority: Moderate | 
| Low | Impact: Medium, Urgency: Low → Priority: Low | 


## Jira Integration

Jira is widely used for project tracking and incident management. By integrating ADOC with Jira, alerts can automatically create or update Jira tickets. This helps teams track incidents directly in Jira, improving collaboration and speeding up resolution.

ADOC supports both **Standard (API Token)** and **OAuth authentication**, as well as **Two-Way Sync**.

## 1. Standard Integration

Uses an API token for authentication.

**Prerequisites:**

1. User account with permissions:
    1. Browse Projects
    2. Create Issues
    3. Edit Issues

2. API Token generated in Jira.

**Steps:**

1. In ADOC, navigate to **Settings** &gt; **Notifications** &gt; **Integrations** &gt; **Jira**.
2. Enter:

| **Field** | **Description** | 
| ---- | ---- | 
| Server URL | https://&lt;siteName&gt;.atlassian.net (no trailing slash) | 
| Username | Jira account username (linked to API token) | 
| API Token | Token generated in Jira | 


3. Click Update.

## 2. OAuth Integration

OAuth is recommended for enterprise-grade Jira setups.

Steps:

1. In the **Atlassian Developer Portal**, create an **OAuth 2.0 App** for ADOC.
2. Configure:
    1. Authorization type = OAuth 2.0 (3LO).
    2. Callback URL = https://&lt;tenant_name&gt;.&lt;acceldata_base_domain&gt;/ui/oauth-success.

3. Add permissions:
    1. **read:jira-work**
    2. **read:jira-user**
    3. **write:jira-work**

4. In ADOC, configure the integration with:

| **Field** | **Description** | 
| ---- | ---- | 
| Server URL | Jira base URL | 
| Auth URL | From OAuth app settings | 
| Client Secret | From OAuth app settings | 


5. Save and authenticate.

## 3. Two-Way Sync (ADOC ↔ Jira)

Two-way sync keeps Jira and ADOC updated:

- ADOC alert status: updates Jira ticket.
- Jira status/priority changes: update ADOC alert.

Steps:

1. In ADOC &gt; **Enable Two-Way Sync** in Jira integration settings.
2. Click **Download Jira Automation Rule** (JSON file).
3. In **Jira** &gt; **Settings** &gt; **System** &gt; **Global Automation**.
4. Import the rule JSON.
5. Enable the rule.

This ensures updates flow both ways.

## Best Practices

**1. Choose the Right Authentication Method**

- Prefer **OAuth** over username/password. OAuth provides stronger security, limited access, and easier credential management.
- Rotate API tokens and client secrets regularly to reduce security risks.
- Use accounts with only the permissions needed (for example, Create Issues in Jira or ITIL role in ServiceNow).

**2. Keep Configuration Consistent**

- Decide on one incident management tool per workflow (ServiceNow or Jira) to avoid duplication.
- Once a project (Jira) or assignment group (ServiceNow) is mapped to a notification group, avoid changing it. Updates may cause duplicate or disconnected tickets.

**3. Use Severity Mapping Thoughtfully**

- Align ADOC severity levels (Critical, High, Medium, Low) with your organization’s priority structure in Jira or ServiceNow.
- Review mappings regularly so alerts are always triaged correctly.

**4. Enable Two-Way Sync for Accuracy**

- Turn on two-way sync where possible so updates flow in both directions.
- **Example**: If a Jira ticket is closed, ADOC should reflect that the issue is resolved.
- Two-way sync reduces manual updates and prevents confusion between systems.

**5. Test Before Production**

- Send test alerts after setting up or editing an integration.
- Confirm that incidents are created with the right details (severity, description, linked assets).
- Run a short pilot with a small team before expanding to the full org.

**6. Maintain Regularly**

- Review integrations quarterly:
- Remove inactive projects or groups.
- Refresh tokens or OAuth credentials.
- Validate that mappings and workflows are still correct.
- Document integration settings so future admins can manage without starting from scratch.

**7. Avoid Common Pitfalls**

- Don’t configure multiple notification groups with different Jira projects for the same ADOC policy or monitor (leads to duplicate tickets).
- Don’t rely on manual credentials unless absolutely necessary (use OAuth when available).
- Don’t skip role setup — ensure ITIL role in ServiceNow and required Jira project permissions are assigned before configuring.
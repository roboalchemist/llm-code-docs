# Source: https://docs.gitguardian.com/platform/automate-with-playbooks/available-playbooks.md

# Available playbooks

> Available GitGuardian playbooks: notifying developers, sending reminders, severity auto-assignment, and auto-closing ignored incidents.

GitGuardian provides several built-in playbooks that can be applied to internal incidents, public incidents, or both.

### Auto-share incident public link to involved developer

:::info
This playbook is available only for Internal Monitoring.
:::

Automates sharing incidents with involved developers via email with public share links.

**Trigger**: Incident created by non-workspace member  
**Action**: Creates public share link and emails developer  
**Requirements**: Public sharing must be enabled in workspace settings

**Options:**
- **Feedback collection**: Developer can submit feedback via the link
- **Resolution capability**: Developer can resolve/ignore incident via the link

> If the incident is triggered by a workspace member, this playbook won't apply as they can access the incident through the authenticated dashboard.

![Auto-share incident link playbook](/img/platform/playbooks/playbook-auto-share-incident-link.png)

### Auto-grant access to involved developer (in-app)

:::info
This playbook is available for both Internal Monitoring and Public Monitoring.
:::

Automatically grants incident access to workspace members with Restricted or Member access levels when they are involved in the incident.

**Trigger**: A new incident is detected involving a workspace member 
**Action**: Grants the involved user access to view this specific incident. This is done by matching the commit author email against the dashboard user email.  

Note that this playbook only applies to incidents detected after activation - it does not retroactively grant access to historical incidents.

![Auto-grant access playbook](/img/platform/playbooks/playbook-auto-grant-access.png)

### Auto-resolve revoked secrets

:::info
This playbook is available for both Internal Monitoring and Public Monitoring. It is activated by default for Internal Monitoring.
:::

Automatically resolves incidents when previously valid secrets are revoked.

**Trigger**: A secret previously checked as valid by GitGuardian becomes invalid.  
**Action**: Automatically close the incident as "Resolved", with reason "Secret was revoked"

Activating this playbook applies to both real-time detection (when an incident is re-checked and found invalid) and all historical incidents that became invalid in the past. Upon activation, you will see a confirmation prompt indicating how many historical incidents will be automatically resolved.

![Auto-resolve revoked secrets playbook](/img/platform/playbooks/playbook-auto-resolve-revoked.png)

### Auto-ignore invalid secrets

:::info
This playbook is available for both Internal Monitoring and Public Monitoring. It is activated by default for Internal Monitoring.
:::

Automatically ignores incidents that are (or were) already invalid when first detected.

**Trigger**: A new incident is created with a secret directly checked as Invalid
**Action**: Automatically close the incident as "Ignored", with reason "Invalid secret".

Activating this playbook applies to both real-time detection (new incidents directly checked as invalid) and all historical incidents that were already invalid when detected. 
Upon activation, you will see a confirmation prompt indicating how many historical incidents will be automatically resolved.

![Auto-ignore invalid secrets playbook](/img/platform/playbooks/playbook-auto-ignore-invalid.png)

### Auto-ignore false positives

:::info
This playbook is available and enabled by default for both Internal Monitoring and Public Monitoring.
:::

Automatically ignores incidents that have been tagged as false positives by GitGuardian's internal machine learning model.

**Trigger**: An incident is identified as a false positive by the ML model  
**Action**: Automatically close the incident as "Ignored", with reason "False positive (not a secret)"

This playbook works exclusively with generic secrets, as the machine learning model only analyzes this secret type. 
It applies to real-time detection whenever an incident is identified as a false positive, and can also be applied to historical incidents by launching a historical scan on your perimeter.

Activating this playbook applies to both real-time incidents and historical incidents that were already invalid when detected. 
Upon activation, you will see a confirmation prompt indicating how many historical incidents will be automatically resolved.

![Auto-ignore false positive playbook](/img/platform/playbooks/playbook-auto-ignore-false-positive.png)

# Source: https://docs.gitguardian.com/internal-monitoring/detect/secrets-occurrences.md

# Secrets occurrences

> Understand how GitGuardian groups multiple detections of the same secret into a single incident with individual occurrences.

## What are the occurrences of an incident?

The **same secret can be seen multiple times** in your VCS. They are referred to as occurrences.
GitGuardian streamlines the remediation process by automatically **grouping multiple occurrences of the same secret into a single secret incident**.

Thus, an occurrence of a secret incident is uniquely identified by the combination of the following parameters:
 - the source (for instance: a GitHub repository or a GitLab project) impacted by the secret occurrence,
 - the commit in which we detected the secret occurrence,
 - the commit file containing the secret occurrence,
 - the line within the commit file where the secret occurred.

Alerts are sent only when a new incident is created or reopened because of a regression. A new occurrence attached to an already-existing open secret incident won't raise any alerts.

> GitGuardian sets a maximum limit of 1,000 occurrences for a single secret incident (this does not apply to the self-hosted platform).

### Grouping of occurrences into secret incidents

GitGuardian enhances the remediation process by automatically **grouping multiple occurrences of the same secret into a single secret incident**.
However, within Business Workspaces, the workspace Owner has the exclusive ability to adjust how these secret occurrences are grouped within the [settings](https://dashboard.gitguardian.com/settings/workspace/settings/secrets/general). Two levels of granularity are available:
1. **per secret** [default]
   - All occurrences of the same secret across different sources (e.g., repositories) are consolidated into a single secret incident.
   - This means if a particular secret is found in multiple sources, it will generate only one secret incident.
2. **per secret x source:**
   - Occurrences of the same secret are grouped into separate secret incidents based on their respective sources.
   - This means that if the same secret appears in multiple sources, each source will have its own individual secret incident.
   - You can still know as a manager if the same incident has created other incidents in different sources (if you need help filtering by these related incidents via the API, contact support@gitguardian.com for example script).
This configuration helps tailor the grouping strategy to align with your company's remediation processes and data privacy policies.

![Occurrences grouping setting](/img/internal-monitoring/detect/occurrences_grouping_setting.png)

:::warning
Changing the occurrence grouping setting should be done **with utmost care, as it has a significant impact on secret incident population and analytics**. This modification should be considered a **one-off action**.
Upon changing this setting, all existing secret incidents will be migrated to comply with the new grouping mode, and please note that this migration process may take some time.
![Occurrences grouping setting warning modal](/img/internal-monitoring/detect/occurrences_grouping_setting_warning_modal.png)
:::

Alerts are sent only when a new incident is created or reopened because of a regression. A new occurrence attached to an already-existing open secret incident won't raise any alerts.

> GitGuardian sets a maximum limit of 1,000 occurrences for a single secret incident (this does not apply to the self-hosted platform).

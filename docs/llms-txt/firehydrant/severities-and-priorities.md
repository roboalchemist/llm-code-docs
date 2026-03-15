# Source: https://docs.firehydrant.com/docs/severities-and-priorities.md

# Severities and Priorities

When organizations declare incidents, it's fundamentally important to categorize how severe the incident is. This allows teams to understand who needs to be engaged, what needs to be done, and the type of urgency and attention an issue demands.

Some organizations use "severities," while other organizations will make use of "priorities" to classify incidents. FireHydrant provides both.

## Defaults

FireHydrant ships with several default Severities and Priorities. These allow organizations new to incident management as well as orgs testing things to get up and running quickly with best practices.

### Severities

<Image alt="FireHydrant's default severities" align="center" width="650px" src="https://files.readme.io/2d56c9d-image.png">
  FireHydrant's default severities
</Image>

* **SEV1 - SEV5**: Standard industry indicators for the severity of an incident, with lower numbers (e.g. `SEV1`) indicating a higher severity than higher numbers (e.g. `SEV5`). Some organizations may start their numbering at `SEV0`.
* **GAMEDAY**: A FireHydrant-specific severity denoting a "test" incident. `GAMEDAY` incidents are excluded from metrics/analytics.
* **MAINTENANCE**: A FireHydrant-specific severity denoting a standard maintenance outage, or an "expected" outage. Learn more about creating [Scheduled Maintenances](https://docs.firehydrant.com/docs/scheduled-maintenances).
* **UNSET**: A FireHydrant-specific severity denoting a lack of a severity or an unknown severity. Sometimes teams will declare `UNSET` incidents if they do not yet know how severe an issue is, and will escalate the severity as they work through the issue and discover facts.

If an incident is created without a Severity specified, FireHydrant will first check the [Severity Matrix](https://docs.firehydrant.com/docs/severity-matrix) for any entries. If there are none, or no entries match the given conditions, FireHydrant defaults an incident to UNSET

### Priorities

<Image alt="FireHydrant's default priorities" align="center" src="https://files.readme.io/95a1fe3-image.png">
  FireHydrant's default priorities
</Image>

* **P1 - P4**: Standard industry indicators for priority levels of issues, including engineering tickets, incident tickets, and more. Like with Severity, the lower the number, the higher the urgency/impact.

## Customizing Severities and Priorities

Although FireHydrant provides defaults, organizations can customize and tailor both Severities and Priorities according to their needs.

An example of an additional configuration is a `SEC0` severity to denote a security incident. This allows you to, for example, set different rules, such as creating a designated, private Runbook for [Private Incidents](https://docs.firehydrant.com/docs/private-incidents).

### Reordering Severities and Priorities

<Image alt="Click the dots next to each severity/priority on the left to drag and move them up or down" align="center" width="650px" src="https://files.readme.io/f0a5ba0-CleanShot_2024-06-17_at_10.29.03.png">
  Click the dots next to each severity/priority on the left to drag and move them up or down
</Image>

On each of these pages, you can reorder Severities and Priorities. These orders are impacted in every area you can see and select them, including the declaration forms (web UI, Slack, MS Teams, Zendesk, etc.) and the Command Center (web UI, MS Teams).

### Disabling Priority

<Image alt="No priority shown when Priority disabled for organization" align="center" width="400px" src="https://files.readme.io/15272e2-image.png">
  No priority shown when Priority disabled for organization
</Image>

Organizations who don't use the **Priority** field can disable it by heading to **Settings** > **Organization** > **Incident Priority**. If Priority is disabled, these are the locations where changes occur:

* Priority will no longer show up on incidents in Slack or on the user interface
* Priority cannot be selected during declaration or on forms in [Incident Types](https://docs.firehydrant.com/docs/incident-types), [FireHydrant status pages](https://docs.firehydrant.com/docs/status-page-setup-and-configuration), and [Incident field settings](https://docs.firehydrant.com/docs/incident-fields)
* Priority disappears as a filterable option from the Incidents list and Analytics pages. If any Saved Filters exist that use Priority, they will be marked as having "Invalid conditions"
* Priority disappears as a selectable condition in Runbooks and Runbook steps. If any existing steps use Priority as a condition, the condition will become invalid
* Priority disappears as a selectable condition in [Jira Project Field Mapping](https://docs.firehydrant.com/docs/jira-field-mapping). If any existing Jira project configurations use Priority in a field mapping or condition, they will become invalid
* Priority disappears as a selectable condition and usable field in [Alert Routing](https://docs.firehydrant.com/docs/alert-routing). Any existing routes that use Priority will become invalid
* Priority disappears from any CSV data exports
* The Priorities page disappears from the **Settings** view

When disabling Priority, please ensure that each of the areas above in the product is not using Priority; otherwise, they may stop working correctly.

## Role-Based Access Control for Severities

Organizations can now restrict which user roles can use specific severities when declaring incidents. This provides granular control over severity access, ensuring only authorized roles can create incidents with certain severities.

### How Severity RBAC Works

When configuring a severity, you can specify which roles are allowed to use it during incident declaration:

1. Navigate to **Settings** > **Severities**
2. Click on a severity to edit it
3. Select which roles should have access to use this severity
4. Save your changes

This least-privilege approach ensures sensitive severity levels (such as SEV0 or security incidents) can only be used by appropriate personnel while maintaining flexibility for automated systems.

### Form Validation

When creating or editing a severity, the severity type field is required and properly validated. You must select a type before saving to ensure consistency across your incident management process.

## Next Steps

Now that you've gotten an overview of Severities and Priorities:

* See how you can use these severities and priorities to [configure conditional execution on Runbooks](https://docs.firehydrant.com/docs/introduction-to-runbooks).
* Configure automatic severities with the [Severity Matrix](https://docs.firehydrant.com/docs/severity-matrix).
* See a [blog post about Severities and Priorities](https://firehydrant.com/blog/incident-severity-and-priority-101/) for more clarity and definition.
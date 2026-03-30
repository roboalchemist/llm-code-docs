# Source: https://docs.gitguardian.com/internal-monitoring/remediate/bulk-actions.md

# Bulk actions on incidents

> Use bulk actions to perform status changes, assignments, tagging, and sharing across multiple incidents simultaneously.

Bulk actions allow you to perform the same action on multiple incidents simultaneously, improving your remediation workflow efficiency.

## How to use bulk actions

1. Navigate to your [incidents page](https://dashboard.gitguardian.com/incidents)
2. Select multiple incidents using checkboxes
3. The bulk actions toolbar appears at the top
4. Choose your desired action

:::tip
Use the header checkbox to select all incidents on the page, or click "Select all X incidents" to select all matching your current filters.
:::

## Available actions

### Status management
- **Assign/Unassign**: Distribute incidents to team members
- **Resolve**: Mark incidents as fixed (requires resolution reason)
- **Ignore**: Mark as false positives or non-issues (requires ignore reason)
- **Reopen**: Change closed incidents back to open status

### Organization
- **Set severity**: Update priority levels (Critical, High, Medium, Low)
- **Add custom tags**: Categorize incidents (requires workspace configuration)
- **Comment**: Add notes visible in incident timelines

### Collaboration
- **Share**: Grant access to users or teams (Business plan only)
- **Download**: Export incident data as CSV reports

## Using bulk actions with similar incidents

GitGuardian's [ML-powered similar incident grouping](./investigate-incidents.md#ml-powered-similar-incident-grouping) helps you identify related incidents that can be efficiently handled together using bulk actions.

Once you've identified similar incidents during your investigation:

1. **From incident details**: View similar incidents in the sidebar and click on "View X similar incidents" to see them in the main incidents list
2. **Filter by similarity**: In the search box, use `similar_to` to show only incidents similar to a specific incident
3. **Sort by similarity count**: Use the "Similar incidents" column to sort incidents by highest or lowest number of similar incidents
4. **Apply bulk actions**: Select similar incidents and perform bulk operations like resolving, assigning, or tagging them together

This combination is particularly useful for:
- **Identifying false positives**: Group and ignore similar false positive incidents in bulk
- **Consistent remediation**: Apply the same remediation approach to incidents that require similar fixes
- **Reducing incident fatigue**: Focus on unique issues while efficiently handling repetitive incidents

[Learn more about ML-powered similar incident grouping](./investigate-incidents.md#ml-powered-similar-incident-grouping)

## Best practices

- **Filter first**: Use search and filters to narrow your selection
- **Verify selection**: Check the count before executing actions
- **Start small**: Begin with smaller batches to learn the workflow
- **Document actions**: Use comments to explain bulk decisions
- **Use similar grouping**: Leverage ML grouping to identify related incidents before applying bulk actions

## Permissions

- **Can view**: No bulk actions available
- **Can edit**: All actions except sharing
- **Full access**: All bulk actions including sharing

:::note
Some incidents may be excluded if you lack sufficient permissions for those specific incidents.
:::

# Source: https://docs.jit.io/docs/manual-branch-scan.md

# Manual Branch Scanning

## Overview

Jit's On-Demand Branch Scanning allows you to trigger security scans on any branch of your repository, not just the default branch. This enables security teams and developers to identify security issues earlier in the development process, reducing the time to remediation and improving your overall security posture.

## Why Manual Branch Scans?

Many development teams actively develop on feature branches or other non-default branches. Before this feature, security scans were only performed automatically on the default branch, which meant:

1. Security issues were discovered only after merging to the default branch
2. Teams had to wait for the merge to identify security vulnerabilities
3. Fixing security issues required additional commits or reverting changes

With Manual Branch Scan, you can proactively identify and address security issues while still in active development.

## How It Works

The Manual Branch Scan feature allows you to:

1. Select a non-default branch from your repository
2. Trigger a security scan on demand
3. View the findings in your backlog, with clear indication of which branch they belong to
4. Filter findings by branch name
5. Track scan execution through pipelines that are triggered by the manual scan event

## Using Manual Branch Scans

### Triggering a Branch Scan

To trigger a manual scan on a branch:

1. Navigate to  Risks -> Resources page in the Jit platform
2. Choose Risk Factor
3. Choose the Resource you want to scan
4. Locate the "Scan Branch" button (top right)
5. Click the button to open the branch scan dialog
6. Enter the name of the branch you want to scan (e.g., `feature/new-auth-flow`)
7. Click "OK" to trigger the scan

You'll see a banner confirming that the scan was successfully triggered. The scan will run in the background as an asynchronous process. Only resources (repositories) containing the specified branch will be scanned.

### Viewing Branch-Specific Findings

After running a branch scan, you can view the findings in the backlog once the scan completes:

1. Navigate to the Backlog page
2. The "Branch" column will display which branch each finding belongs to

### Filtering Findings by Branch

To focus on findings from a specific branch:

1. On the Backlog page, click the filter icon
2. Select "Branch" from the filter options
3. Choose one or more branch names from the dropdown
4. The findings list will update to show only findings from the selected branch(es)

### Viewing Pipeline Executions

To track the progress of your branch scans:

1. Navigate to the Pipelines section
2. Click on the filter icon
3. Select "Event" from the filter options
4. Choose "Manual Branch Scan" from the dropdown
5. The pipelines list will update to show only executions triggered by branch scans

## Technical Details

* Manual Branch Scan works with all code-related security controls in your security plan
* Scans run with the same depth and coverage as default branch scans
* Only repositories containing the specified branch will be scanned

## Considerations

* **Drift**: When you fix a finding in a branch's code, the finding will remain in the backlog until you run a new scan on that branch.
* **Branch Management**: If a branch is deleted or renamed after scanning, the findings will still be associated with the original branch name.
* **Performance**: Scanning multiple branches across a large amount of repositories may impact system performance.

## Permissions

To trigger manual branch scans, users must have the `jit.trigger.write` permission.

## API Access

The Manual Branch Scan feature can also be triggered via API. For detailed API documentation, see [Trigger branch scan API Reference](https://docs.jit.io/reference/scan).

```
POST https://api.jit.io/trigger/manual-branch-scan
{
  "branch": "your-branch-name"
}
```

Response:

```json
{
  "jit_event_id": "c02fc1d3-db8b-45c5-a222-27595b15aea7"
}
```

## Supported Integrations

Manual Branch Scan is available for repositories hosted on:

* GitHub
* GitLab

## Frequently Asked Questions

**Q: Can I scan multiple branches at once?**\
A: You need to trigger a scan for each branch individually.

**Q: How do I know when a branch scan has completed?**\
A: Branch scans run asynchronously. You can check the Pipelines section to see if the scan has completed, and once finished, findings will appear in your backlog with the associated branch name.

**Q: How do I automate branch scanning?**\
A: Currently, branch scanning is a manual process. You can use the API to integrate with your CI/CD pipeline if needed.

**Q: Can I exclude certain branches from being scanned?**\
A: There are no built-in exclusion rules for branches. Since branch scanning is triggered manually, you simply choose not to scan branches you want to exclude.
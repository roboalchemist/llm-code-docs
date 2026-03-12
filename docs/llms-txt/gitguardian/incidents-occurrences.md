# Source: https://docs.gitguardian.com/public-monitoring/detect-public-secret-incidents/incidents-occurrences.md

# Incidents and occurrences

> Understand how GitGuardian groups multiple public detections of the same secret into a single incident with individual occurrences.

## What is a public secret incident?

Public secret incidents are open issues created when GitGuardian detects secrets within your Public Perimeter. 
<!-- , to add after Explore is delivered -> "or manually from a specific search." -->
When secrets are leaked publicly within your company perimeter, they are likely related to your organization and require your attention to assess their impact, and resolve the incident accordingly.

## What are the occurrences of a public secret incident?

The **same secret can be detected multiple times** across different public sources. These individual detections are called **occurrences**. 
GitGuardian streamlines the remediation process by automatically **grouping multiple occurrences of the same secret into a single public secret incident**.

A public secret occurrence is uniquely identified by the combination of the following parameters:
- The GitHub repository where the secret was detected
- The commit in which the secret was found
- The file containing the secret
- The line within the commit file where the secret occurred.

<!-- 
WHEN WE SUPPORT SEVERAL PUBLIC SOURCES, we should replace the paragraph with: 
A public secret occurrence is uniquely identified by the combination of the following parameters:
- The public source where the secret was detected (typically a GitHub repository)
- The commit or content in which the secret was found
- The file or content containing the secret occurrence
- The specific location within the content where the secret occurred (typically the line within the commit) -->

:::info
Each occurrence may have been detected through different [attachment reasons](../remediate/understand-incident-properties.md#attachment-reasons). For example, the same incident may group:
- An occurrence leaked 'By dev from perimeter' (a developer from your monitored perimeter was involved)
- Another occurrence leaked 'On organization from perimeter' (the secret was found in a repository belonging to one of your monitored GitHub organizations).

As a result, a single public secret incident may have multiple attachment reasons.
:::

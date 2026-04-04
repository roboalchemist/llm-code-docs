# Source: https://docs.datadoghq.com/cloudcraft/getting-started/version-history.md

---
title: Version History
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > Getting started > Version History
---

# Version History

## Overview{% #overview %}

Version history allows users to track changes in their architecture diagrams over time, allowing them to review and restore previous iterations of diagrams. Whether you're managing complex cloud architectures or collaborating with a team, version history provides invaluable insight into your diagram's evolution.

You can access the version history feature by clicking the **Version history** button in the top right corner of the Cloudcraft application.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/version-history/cloudcraft-diagram-aws-infrastructure-version-history.a36318cfe6e66184ee6f80c03b14009e.png?auto=format"
   alt="Cloudcraft diagram showcasing AWS infrastructure with an arrow highlighting the version history button." /%}

## Working with versions{% #working-with-versions %}

Version history isn't just for reviewing past workâit's also a powerful tool for managing your current and future diagrams. Here are some key actions you can take:

1. **Restoring previous versions**: If you need to revert to a previous state of your diagram, you can easily do so. Simply click the **Restore this version** button on the top right side of your screen when viewing a past version.
1. **Creating new blueprints**: Version history allows you to save any specific version of your diagram as a new blueprint. This feature is particularly useful for creating templates or preserving specific architectural states for future reference. To create a new blueprint from a version, click the three dots on the right side of the version name and choose **Save as a new blueprint**.
1. **Comparing versions**: While not explicit, the ability to view different versions allows for manual comparison of how your architecture has changed over time.

**Note**: Manually creating or deleting versions from your history is not available.

### Creation{% #creation %}

Versions are automatically created as you work on your diagrams. By default, each version is timestamped and named after the date and time of its creation. However, for easier reference, you have the option to give specific versions custom names, which is particularly useful for marking significant milestones or changes in your architecture.

To name a version:

1. Select the version you want to name.
1. Click the three dots on the right side of the version name.
1. Choose **Name this version** from the dropdown menu.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/version-history/version-history-interface-cloudcraft.459318780a4328bbafe1a56fe3536dbc.png?auto=format"
   alt="Version history interface with options to name or save versions in Cloudcraft." /%}

Cloudcraft creates new versions intelligently to balance granularity with efficiency. If the current version is more than 5 minutes old, any new updates will trigger the creation of a new version. For changes made within 5 minutes of the latest version, updates are added to that existing version. This approach ensures that your version history remains meaningful without becoming cluttered with minor changes.

It's worth noting that while you cannot manually create a new version, one is automatically generated when you switch from [Snapshot to Live mode](https://docs.datadoghq.com/cloudcraft/getting-started/live-vs-snapshot-diagrams/) in your diagram.

### Metadata{% #metadata %}

Each version in the history includes metadata such as user names and timestamps.

The name of the user who created the version is displayed on the right side of the version name. If a different user last edited the version, their name is also shown, providing clear accountability for changes.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/version-history/cloudcraft-version-history-user-timestamps.e9d7a86285961b902dab2874df833dc3.png?auto=format"
   alt="Version history interface with user details and timestamps." /%}

For Live diagrams, a green lightning bolt icon appears to the left of the version name, distinguishing these dynamic versions from Snapshot versions.

### Searching{% #searching %}

To help you navigate through your version history, Cloudcraft provides a search functionality. You can search for specific versions by name or date, making it easy to locate particular points in your diagram's timeline.

To search for a version, enter your search query in the search bar at the top of the version history panel.

For users who prefer to focus on significant changes, there's an option to filter the view by checking the **Only show named versions** checkbox under the search bar, which allows you to hide unnamed versions, streamlining your version history view.

### Retention{% #retention %}

Named versions are kept indefinitely, maintaining a permanent record of significant diagram states.

Unnamed versions are subject to a retention period that varies based on your plan:

- Free and Pro plan users: Unnamed versions are retained for 30 days.
- Enterprise plan users: Unnamed versions are kept for 90 days.

This tiered approach ensures that casual users maintain a useful history while providing extended retention for enterprise customers with more complex needs.

## Best Practices{% #best-practices %}

To make the most of the version history feature, consider the following best practices:

1. **Name important versions**: Assign meaningful names to significant versions of your diagrams. This practice ensures that crucial stages in your architecture's evolution are easily identifiable and permanently retained.
1. **Regularly review**: Periodically review your version history to track the progression of your architecture. This can provide valuable insights into your design decisions over time.
1. **Leverage search**: Utilize the search functionality and the **Only show named versions** filter to efficiently navigate through your version history, especially for projects with numerous iterations.
1. **Plan for version retention**: If you're on a Free or Pro plan, be mindful of the 30-day retention period for unnamed versions. Name versions you want to keep beyond this period.
1. **Collaborative documentation**: When working in teams, use the version naming feature to document who made specific changes and why. This can serve as a valuable communication tool within the team.
1. **Use versions for proposals**: Before making significant changes to your architecture, create a named version. This allows you to easily revert if the proposed changes aren't approved or implemented.

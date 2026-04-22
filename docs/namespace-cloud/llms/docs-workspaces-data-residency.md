<!-- Source: https://namespace.so/docs/workspaces/data-residency -->

# Data Residency for Workspaces

Namespace provides flexible data residency options to meet your organization's compliance and performance requirements.
This page explains how workspace data is handled across regions and the available residency options.

## Global Distribution

Namespace distributes workloads globally across multiple regions to ensure optimal performance and reliability.
By default, your workspace data may be processed and stored across our global infrastructure to provide the best user experience.

## Regional Preferences

If your organization has specific regional preferences for where workloads should be scheduled, Namespace can accommodate these requirements.
Regional preferences help ensure your data is primarily handled within your preferred geographic areas while maintaining system performance.

To configure regional preferences for your workspace:

1. Check your [current regional preference](https://cloud.namespace.so/workspace/settings)
2. Contact our [support team](mailto:support@namespace.so)
3. Specify your preferred regions

Regional preferences are available on all Namespace plans and provide a balance between compliance needs and system performance.

## Data Residency

For organizations with strict data sovereignty requirements, Namespace offers region-exclusive data residency.
This option ensures that all workloads issued by your workspace are scheduled exclusively within a specific geographic region, providing the highest level of data localization control.

### Data Locality per Region

- **Region-exclusive workload scheduling**: No source code, or binaries, or build outputs, ever leaves the selected exclusive region.
- **Global metadata replication**: Metadata such as scheduling decisions, operational logs and workflow metadata (used for listing and filtering purposes) is replicated globally.

### Important considerations

- Region-exclusive data residency requires an enterprise plan.
- Performance may vary depending on your workspace's geographic restrictions.
- Some advanced features may have limited availability in certain regions.

## Compliance

Our compliance team can provide documentation and certifications to support your organization's audit and regulatory requirements.
For more information, check out Namespace's [security and compliance features](/docs/workspaces/security).
To learn about Namespace's certifications, visit our [Trust Center](https://trust.namespace.so/).

Last updated July 4, 2025

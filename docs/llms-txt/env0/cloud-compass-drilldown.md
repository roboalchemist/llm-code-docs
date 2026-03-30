# Source: https://docs.envzero.com/changelogs/2025/02/cloud-compass-drilldown.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔎⏳New: Spot Drift in Minutes With Cloud Compass - Even Before Fully Onboarding

> Cloud Compass now enables you to detect and analyze drift in your cloud infrastructure before onboarding resources into env zero. This new capability provides instant visibility into drift risks, detailed insights into changes, and helps prioritize remediation efforts - all without requiring full onboarding.

Cloud Compass now enables you to detect and analyze drift across your entire infrastructure within minutes of connecting your cloud account - even for resources not managed in env zero.\
This expanded visibility helps you track changes, assess drift risks, and prioritize remediation as quickly as possible.

### How It Works

Upon activation, Cloud Compass will assign a drift status to all resources in the connected cloud account.\
For resources managed outside env zero, Cloud Compass identifies the likelihood of drift based on data from past operational events, and other nuanced relevant information in cloud logs. Based on the combination of these signals, likely discrepancies will be flagged as ‘Drift Risk’.

For env zero-managed resources, Cloud Compass will leverage env zero’s deterministic understanding of deviation between the infrastructure’s actual state and the desired state, as defined by IaC configuration. These resources will be flagged as ‘Drifted’.

Importantly, for every resource managed by env zero, the system now provides direct links to its corresponding env zero environment, offering easy access to valuable context such as ownership details and deployment history.

With drifted resources, this information can be especially useful for root cause investigation and driving effective reconciliation efforts.

<Image src="/images/changelogs/2025/02/62ee0be12436dd37b7b60787eaa63bf6cc7bc70a02f02ad734c17f0a2ba2e459-image1.png" />

The drift information is displayed in the newly added ‘Drift’ column in the Resources table, inside the Cloud Compass screen.

<Image src="/images/changelogs/2025/02/1879e637f94478ceafb14b631a01a21e138a39f216587f7cbba7694383c37dba-image2.png" />

Clicking 'Details' on a flagged resource now provides full visibility into the events that led to drift. This capability, [Drift Cause](/guides/admin-guide/environments/drift-detection/drift-cause#/), is now available for all resources, showing what changed, who made the change, and when - helping you take action with confidence.

<Image src="/images/changelogs/2025/02/27495eab89e0c86c24c2e6a0fda754a314cd4acf78e62b8499bc8e5e77b0b81d-image3.png" />

[Visit here](/guides/cloud-compass/cloud-compass/linking-environments-to-cloud-compass-resources#/) to learn more about Cloud Compass and its other capabilities.

Built with [Mintlify](https://mintlify.com).

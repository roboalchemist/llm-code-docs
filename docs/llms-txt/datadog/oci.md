# Source: https://docs.datadoghq.com/account_management/billing/oci.md

---
title: OCI Integration Billing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Account Management > Billing > OCI Integration Billing
---

# OCI Integration Billing

## Overview{% #overview %}

Datadog bills for hosts running the Datadog Agent and all Oracle Cloud Infrastructure (OCI) Compute instances detected by the OCI integration. You are not billed twice if the Datadog Agent runs on a Compute instance that is also detected by the OCI integration.

Other OCI resourcesâsuch as Autonomous Database, Object Storage, Load Balancer, and other managed servicesâdo not impact monthly infrastructure billing. These services can send metrics to Datadog through the integration without additional host charges.

If you run containers on OCI (for example, on Oracle Kubernetes Engine), container usage is billed separately. See the [containers billing guide](https://docs.datadoghq.com/account_management/billing/containers/) for details.

## OCI metric exclusion{% #oci-metric-exclusion %}

Use the OCI integration tile to control which resources Datadog collects metrics from:

1. Open the [OCI integration tile](https://app.datadoghq.com/integrations?integrationId=oracle-cloud-infrastructure).
1. Go to the **Metric Collection** tab.
1. For each connected tenancy, optionally:
   - Limit metric collection to specific compartments.

**Note**: You can exclude OCI regions from all data collection (metrics and logs) on the **General** tab of the OCI integration tile.

## OCI log exclusion{% #oci-log-exclusion %}

Use the OCI integration tile to control which resources Datadog collects logs from:

1. Open the [OCI integration tile](https://app.datadoghq.com/integrations?integrationId=oracle-cloud-infrastructure).
1. Go to the **Log Collection** tab.
1. For each connected tenancy, optionally:
   - Limit log collection to specific compartments.

**Note**: You can exclude OCI regions from all data collection (metrics and logs) on the **General** tab of the OCI integration tile.

When you add or change limits for an existing OCI tenancy, previously discovered Compute instances can remain in the [Infrastructure List](https://docs.datadoghq.com/infrastructure/) for up to two hours while filters propagate. During this transition period, affected instances can display a status of `???`. This does not count toward your billing.

Hosts with a running Datadog Agent continue to be included in billing. Limiting metric and log collection in the OCI integration tile applies to instances discovered by the integration and does not exclude hosts that report directly through the Agent.

## Check if a host is monitored by the Agent or OCI{% #check-if-a-host-is-monitored-by-the-agent-or-oci %}

In the Infrastructure Host list:

- Monitored by OCI integration

If a host displays only the OCI logo, or if its metrics are limited to `oci.*` namespaces, the host is monitored exclusively through the OCI integration.

- Monitored by the Datadog Agent

If a host displays the Datadog Agent logo but not the OCI logo, or if its metrics include Agent-collected namespaces (such as `datadog.*`, `system.*`, and others), the host is monitored by the Datadog Agent.

## Troubleshooting{% #troubleshooting %}

For technical questions, contact [Datadog support](https://docs.datadoghq.com/help/).

For billing questions, contact your [Customer Success](mailto:success@datadoghq.com) Manager.

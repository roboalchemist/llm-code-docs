# Source: https://docs.datadoghq.com/account_management/billing/alibaba.md

---
title: Alibaba Integration Billing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Account Management > Billing > Alibaba Integration Billing
---

# Alibaba Integration Billing

## Overview{% #overview %}

Datadog bills for all Alibaba Virtual Machines being monitored in Datadog. These machines are billable regardless of whether the Datadog Agent is installed. **You are not billed twice** if you are running the Agent on an Alibaba VM picked up by the Alibaba integration.

Other Alibaba resources (CDNs, Express Connect Instances, Aspara DBs, etc.) are not part of monthly billing.

## Alibaba VM exclusion{% #alibaba-vm-exclusion %}

Use the [Datadog-Alibaba integration](https://app.datadoghq.com/account/settings#integrations/alibaba-cloud) tile to filter your VMs monitored by Datadog using [host tags](https://docs.datadoghq.com/getting_started/tagging/using_tags/#integrations). Go to the **Configuration** tab and edit an existing account or add a new one. Filtering for each account is controlled by clicking it and filling in the field for **Optionally limit metrics collection to hosts with tag**:

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/alibaba_filter.0e9fbb2f3926c4eb84d1f84c78849a74.png?auto=format"
   alt="Alibaba VM Filter" /%}

When adding limits to existing Alibaba accounts within the integration tile, the previously discovered VMs could stay in the [Infrastructure List](https://docs.datadoghq.com/infrastructure/) up to 2 hours. During the transition period, VMs display a status of `???`. This does not count towards your billing.

VMs with a running Agent still display and are included in billing, so using the limit option is only useful for VMs without a running Agent.

## Troubleshooting{% #troubleshooting %}

For technical questions, contact [Datadog support](https://docs.datadoghq.com/help/).

For billing questions, contact your [Customer Success](mailto:success@datadoghq.com) Manager.

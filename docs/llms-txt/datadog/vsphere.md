# Source: https://docs.datadoghq.com/account_management/billing/vsphere.md

---
title: vSphere Integration Billing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Account Management > Billing > vSphere Integration Billing
---

# vSphere Integration Billing

## Overview{% #overview %}

Datadog bills for each Agent installed on a vCenter server and each VM and ESXi host monitored.

## vSphere VM exclusion{% #vsphere-vm-exclusion %}

Use the `vsphere.yaml` file to filter your VMs monitored by Datadog by using regex. See the [sample vsphere.d/conf.yaml](https://github.com/DataDog/integrations-core/blob/master/vsphere/datadog_checks/vsphere/data/conf.yaml.example) for an example.

When adding limits to existing VMs, the previously discovered VMs could stay in the [Infrastructure List](https://docs.datadoghq.com/infrastructure/) up to 24 hours. During the transition period, VMs display a status of `???`. This does not count towards your billing.

## Troubleshooting{% #troubleshooting %}

For technical questions, contact [Datadog support](https://docs.datadoghq.com/help/).

For billing questions, contact your [Customer Success](mailto:success@datadoghq.com) Manager.

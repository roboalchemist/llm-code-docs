# Source: https://docs.datadoghq.com/security/default_rules/def-000-ak9.md

---
title: Projects should not have legacy networks configured for older projects
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Projects should not have legacy
  networks configured for older projects
---

# Projects should not have legacy networks configured for older projects

## Description{% #description %}

To prevent use of legacy networks, a project should not have a legacy network configured. Legacy networks can no longer be created, and their use is not recommended. This recommendation is to check old projects to ensure that they are not using Legacy Networks.

## Rationale{% #rationale %}

Each legacy network has a single network IPv4 prefix range, and a single gateway IP address. The network is global in scope and spans all cloud regions. Subnetworks cannot be created in a legacy network, and are unable to switch from legacy to auto or custom subnet networks. Legacy networks can have an impact on high network traffic projects, and are subject to a single point of contention or failure.

### Default value{% #default-value %}

By default, networks are not created in the legacy mode.

## Remediation{% #remediation %}

For each Google Cloud Platform project:

1. Read [Create and modify Virtual Private Cloud (VPC) networks](https://cloud.google.com/vpc/docs/create-modify-vpc-networks) to create a non-legacy network suitable for the organization's requirements.
1. Read [Deleting a legacy network](https://cloud.google.com/vpc/docs/using-legacy#deleting_a_legacy_network) to delete the networks in the `legacy` mode.

## References{% #references %}

1. [https://cloud.google.com/vpc/docs/using-legacy#creating_a_legacy_network](https://cloud.google.com/vpc/docs/using-legacy#creating_a_legacy_network)
1. [https://cloud.google.com/vpc/docs/using-legacy#deleting_a_legacy_network](https://cloud.google.com/vpc/docs/using-legacy#deleting_a_legacy_network)

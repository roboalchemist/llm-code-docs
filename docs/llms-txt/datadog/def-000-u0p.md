# Source: https://docs.datadoghq.com/security/default_rules/def-000-u0p.md

---
title: Projects should only use non-default VPC networks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Projects should only use non-default
  VPC networks
---

# Projects should only use non-default VPC networks

## Description{% #description %}

To prevent use of the `default` network, a project should not have a `default` network.

### Default value{% #default-value %}

By default, for each project, a `default` network is created.

## Rationale{% #rationale %}

The `default` network has a preconfigured network configuration and automatically generates the following insecure firewall rules:

- default-allow-internal: Allows ingress connections for all protocols and ports among instances in the network.
- default-allow-ssh: Allows ingress connections on TCP port 22(SSH) from any source to any instance in the network.
- default-allow-rdp: Allows ingress connections on TCP port 3389(RDP) from any source to any instance in the network.
- default-allow-icmp: Allows ingress ICMP traffic from any source to any instance in the network.

These automatically-created firewall rules do not get audit-logged and cannot be configured to enable firewall rule logging.

Furthermore, the `default` network is an auto-mode network, which means that its subnets use the same predefined range of IP addresses. As a result, it's not possible to use Cloud VPN or VPC Network Peering with the `default` network.

Based on organization security and networking requirements, the organization should create a new network and delete the `default` network.

### Impact{% #impact %}

When an organization deletes the `default` network, it may need to migrate services onto a new network.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the [VPC networks](https://console.cloud.google.com/networking/networks/list) page.
1. Click the network named `default`.
1. On the network detail page, click **EDIT**.
1. Click **DELETE VPC NETWORK**.
1. If needed, create a new network to replace the `default` network.

### From the command line{% #from-the-command-line %}

1. Delete the `default` network:

   ```
   gcloud compute networks delete default
   ```

1. If needed, create a new network to replace it:

   ```
   gcloud compute networks create NETWORK_NAME
   ```

## Prevention{% #prevention %}

You can prevent the `default` network and its insecure firewall rules from being created by setting up an Organization Policy to skip `default` network creation at [https://console.cloud.google.com/iam-admin/orgpolicies/compute-skipDefaultNetworkCreation](https://console.cloud.google.com/iam-admin/orgpolicies/compute-skipDefaultNetworkCreation).

## References{% #references %}

1. [https://cloud.google.com/compute/docs/networking#firewall_rules](https://cloud.google.com/compute/docs/networking#firewall_rules)
1. [https://cloud.google.com/compute/docs/reference/latest/networks/insert](https://cloud.google.com/compute/docs/reference/latest/networks/insert)
1. [https://cloud.google.com/compute/docs/reference/latest/networks/delete](https://cloud.google.com/compute/docs/reference/latest/networks/delete)
1. [https://cloud.google.com/vpc/docs/firewall-rules-logging](https://cloud.google.com/vpc/docs/firewall-rules-logging)
1. [https://cloud.google.com/vpc/docs/vpc#default-network](https://cloud.google.com/vpc/docs/vpc#default-network)
1. [https://cloud.google.com/sdk/gcloud/reference/compute/networks/delete](https://cloud.google.com/sdk/gcloud/reference/compute/networks/delete)

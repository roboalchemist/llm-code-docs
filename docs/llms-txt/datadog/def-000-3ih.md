# Source: https://docs.datadoghq.com/security/default_rules/def-000-3ih.md

---
title: SSH access should be restricted from the internet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SSH access should be restricted from
  the internet
---

# SSH access should be restricted from the internet
 
## Description{% #description %}

GCP Firewall Rules are specific to a VPC Network. Each rule either allows or denies traffic when its conditions are met. Its conditions allow the user to specify the type of traffic, such as ports and protocols, and the source or destination of the traffic, including IP addresses, subnets, and instances. Firewall rules are defined at the VPC network level and are specific to the network in which they are defined. The rules themselves cannot be shared among networks. Firewall rules only support IPv4 traffic. When specifying a source for an ingress rule or a destination for an egress rule by address, only an IPv4 address or IPv4 block in CIDR notation can be used. Generic (0.0.0.0/0) incoming traffic from the internet to VPC or VM instance using SSH on Port 22 can be avoided.

## Rationale{% #rationale %}

GCP Firewall Rules within a VPC Network apply to outgoing (egress) traffic from instances and incoming (ingress) traffic to instances in the network. Egress and ingress traffic flows are controlled even if the traffic stays within the network (for example, instance-to-instance communication). For an instance to have outgoing Internet access, the network must have a valid Internet gateway route or custom route whose destination IP is specified. This route simply defines the path to the Internet, to avoid the most general (0.0.0.0/0) destination IP Range specified from the Internet through SSH with the default Port 22. Generic access from the Internet to a specific IP Range needs to be restricted.

## Impact{% #impact %}

All Secure Shell (SSH) connections from outside of the network to the concerned VPC(s) will be blocked. There could be a business need where SSH access is required from outside of the network to access resources associated with the VPC. In that case, specific source IP(s) should be mentioned in firewall rules to include access to SSH port for the concerned VPC(s).

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to VPC Network.
1. Go to the Firewall Rules.
1. Click the Firewall Rule you want to modify.
1. Click Edit.
1. Modify Source IP ranges to specific IP.
1. Click Save.

### From the command line{% #from-the-command-line %}

1.Update the Firewall rule with the new SOURCE_RANGE from the following command:

```
gcloud compute firewall-rules update FirewallName --allow=[PROTOCOL[:PORT[-PORT]],...] --source-ranges=CIDR_RANGE,...]
```

## References{% #references %}

1. [https://cloud.google.com/vpc/docs/firewalls#blockedtraffic](https://cloud.google.com/vpc/docs/firewalls#blockedtraffic)
1. [https://cloud.google.com/blog/products/identity-security/cloud-iap-enables-context-aware-access-to-vms-via-ssh-and-rdp-without-bastion-hosts](https://cloud.google.com/blog/products/identity-security/cloud-iap-enables-context-aware-access-to-vms-via-ssh-and-rdp-without-bastion-hosts)

## Additional Information{% #additional-information %}

As of this writing, GCP VPC only supports IPv4; however, Google is working on adding IPv6 support for VPC. If you are using IPv6, the rule should check for the IPv6 equivalent ::0 along with source IP range 0.0.0.0.

## CIS Controls{% #cis-controls %}

Version 8 - 4.4: Implement and Manage a Firewall on Servers

- Implement and manage a firewall on servers, where supported. Example implementations include a virtual firewall, operating system firewall, or a third-party firewall agent.

Version 8 - 4.5: Implement and Manage a Firewall on End-User Devices

- Implement and manage a host-based firewall or port-filtering tool on end-user devices, with a default-deny rule that drops all traffic except those services and ports that are explicitly allowed.

Version 7 - 9.2: Ensure Only Approved Ports, Protocols and Services Are Running

- Ensure that only network ports, protocols, and services with validated business needs are listening on a system.

Version 7 - 12.4: 12.4 Deny Communication over Unauthorized Ports

- Deny communication or application traffic over unauthorized TCP or UDP ports, to ensure that only authorized protocols are allowed to cross the network boundary in or out of the network, at each of the organization's network boundaries.

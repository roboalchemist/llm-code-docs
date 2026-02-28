# Source: https://docs.datadoghq.com/security/default_rules/def-000-tqp.md

---
title: Instances should have IP forwarding disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Instances should have IP forwarding
  disabled
---

# Instances should have IP forwarding disabled

## Description{% #description %}

Compute Engine instance cannot forward a packet unless the source IP address of the packet matches the IP address of the instance. Similarly, GCP won't deliver a packet whose destination IP address is different than the IP address of the instance receiving the packet. However, both capabilities are required if you want to use instances to help route packets.

Disable the forwarding of data packets to prevent data loss or information disclosure.

## Rationale{% #rationale %}

To enable source and destination IP check, disable the `canIpForward` option, which allows an instance to send and receive packets with non-matching destination or source IPs.

## Impact{% #impact %}

Deleting instances that act as routers or packet forwarders may break network connectivity.

## Exception{% #exception %}

Instances created by GKE should be excluded because they need to have IP forwarding enabled and cannot be changed. Instances created by GKE have names that start with `gke-`.

## Remediation{% #remediation %}

You can only edit the `canIpForward` setting at instance creation time. Therefore, if `canIpForward` is set to false for an instance, you must delete the instance and create a new one.

### From the console{% #from-the-console %}

1. Go to the `VM Instances` page: [https://pantheon.corp.google.com/compute/instances](https://pantheon.corp.google.com/compute/instances).
1. Select the `VM Instance` you want to remediate.
1. Click the `Delete` button.
1. On the `VM Instances` page, click `CREATE INSTANCE`.
1. Create a new instance with the desired configuration. By default, the instance is configured to not allow IP forwarding.

### From the command line{% #from-the-command-line %}

1. Delete the instance:
   ```
   gcloud compute instances delete INSTANCE_NAME
   ```
1. Create a new instance to replace it, with IP forwarding set to Off
   ```
   gcloud compute instances create
   ```

## Default Value{% #default-value %}

By default, instances are not configured to allow IP forwarding.

## References{% #references %}

1. [https://cloud.google.com/vpc/docs/using-routes#canipforward](https://cloud.google.com/vpc/docs/using-routes#canipforward)

## Additional Information:{% #additional-information %}

You can only set the `canIpForward` field at instance creation time. After an instance is created, the field becomes read-only.

## CIS Controls{% #cis-controls %}

Version 8 - 4.4: Implement and Manage a Firewall on Servers

- Implement and manage a firewall on servers, where supported. Example implementations include a virtual firewall, operating system firewall, or a third-party firewall agent.

Version 8 - 4.5: Implement and Manage a Firewall on End-User Devices

- Implement and manage a host-based firewall or port-filtering tool on end-user devices, with a default-deny rule that drops all traffic except those services and ports that are explicitly allowed.

Version 7 - 11.1 Maintain Standard Security Configurations for Network Devices

- Maintain standard, documented security configuration standards for all authorized network devices.

Version 7 - 11.2 Document Traffic Configuration Rules

- All configuration rules that allow traffic to flow through network devices should be documented in a configuration management system with a specific business reason for each rule, a specific individual's name responsible for that business need, and an expected duration of the need.

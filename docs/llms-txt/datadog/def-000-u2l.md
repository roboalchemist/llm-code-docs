# Source: https://docs.datadoghq.com/security/default_rules/def-000-u2l.md

---
title: Compute instances should be launched with Shielded VM enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Compute instances should be launched
  with Shielded VM enabled
---

# Compute instances should be launched with Shielded VM enabled
 
## Description{% #description %}

To defend against advanced threats and ensure that the boot loader and firmware on your VMs are signed and untampered, Datadog recommends launching compute instances with Shielded VM enabled.

## Rationale{% #rationale %}

Shielded VMs are virtual machines on the Google Cloud Platform that are hardened by a set of security controls and help defend against rootkits and bootkits. Shielded VM offers verifiable integrity of your Compute Engine VM instances through Secure Boot, a virtual trusted platform module (vTPM)-enabled measured boot, and integrity monitoring. This ensures your instances are not compromised by boot- or kernel-level malware, or rootkits.

Shielded VM instances run firmware which is signed and verified using Google's Certificate Authority, ensuring that the instance's firmware is unmodified and establishes trust for Secure Boot.

Integrity monitoring helps you understand and make decisions about the state of your VM instances and the Shielded VM vTPM enables Measured Boot by performing the measurements needed to create a known good boot baseline, also known as the integrity policy baseline. The integrity policy baseline is used to compare measurements from subsequent VM boots to determine if anything has changed.

Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halts the boot process if signature verification fails.

## Remediation{% #remediation %}

To turn on Shielded VM on an instance, your instance must use an image with Shielded VM support.

### From the console{% #from-the-console %}

1. In the Google Cloud Console, navigate to [VM Instances page](https://console.cloud.google.com/compute/instances), which lists all instances in your project.
1. Click on the instance name to see a VM Instance Details page.
1. Click **Stop** to stop the instance.
1. When the instance has stopped, click **Edit**.
1. In the **Shielded VM** section, select **Turn on vTPM** and **Turn on Integrity Monitoring**.
1. Optionally, if you do not use any custom or unsigned drivers on the instance, also select **Turn on Secure Boot**.
1. Click the **Save** button to modify the instance and click **Start** to restart it.

### From the command line{% #from-the-command-line %}

You can only enable Shielded VM options on instances that have Shielded VM support. For a list of Shielded VM public images, run the gcloud compute images list command with the following flags:

```
gcloud compute images list --project gce-uefi-images --no-standard-images
```

1. Stop the instance using `gcloud compute instances stop <INSTANCE_NAME>`.
1. Update the instance using `gcloud compute instances update <INSTANCE_NAME> --shielded-vtpm --shielded-vm-integrity-monitoring`.
1. Optionally, if you do not use any custom or unsigned drivers on the instance, also turn on Secure Boot using `gcloud compute instances update <INSTANCE_NAME> --shielded-vm-secure-boot`.
1. Restart the instance using `gcloud compute instances start <INSTANCE_NAME>`.

## Prevention{% #prevention %}

To ensure that all new VMs are created with Shielded VM enabled, create an Organization Policy for Shielded VM in the [Organization Policies page](https://console.cloud.google.com/iam-admin/orgpolicies/compute-requireShieldedVm).

For more information, see the [Google Cloud documentation](https://cloud.google.com/security/shielded-cloud/shielded-vm#organization-policy-constraint).

## Default Value{% #default-value %}

By default, Compute Instances do not have Shielded VM enabled.

## References{% #references %}

1. [https://cloud.google.com/compute/docs/instances/modifying-shielded-vm](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm)
1. [https://cloud.google.com/shielded-vm](https://cloud.google.com/shielded-vm)
1. [https://cloud.google.com/security/shielded-cloud/shielded-vm#organization-policy-constraint](https://cloud.google.com/security/shielded-cloud/shielded-vm#organization-policy-constraint)

## Additional Information{% #additional-information %}

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

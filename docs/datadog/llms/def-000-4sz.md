# Source: https://docs.datadoghq.com/security/default_rules/def-000-4sz.md

---
title: Serial port connection for VM instances should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Serial port connection for VM instances
  should be disabled
---

# Serial port connection for VM instances should be disabled

## Description{% #description %}

Interacting with a serial port is often referred to as the serial console, which is similar to using a terminal window, in that input and output is entirely in text mode and there is no graphical interface or mouse support. If you enable the interactive serial console on an instance, clients can attempt to connect to that instance from any IP address. Therefore interactive serial console support should be disabled.

## Rationale{% #rationale %}

A virtual machine instance has four virtual serial ports. The instance's operating system, BIOS, and other system-level entities often write output to the serial ports, and can accept input such as commands or answers to prompts. Typically, these system-level entities use the first serial port (port 1) and serial port 1 is often referred to as the serial console. The interactive serial console does not support IP-based access restrictions such as IP allow lists. If you enable the interactive serial console on an instance, clients can attempt to connect to that instance from any IP address. This allows anybody to connect to that instance if they know the correct SSH key, username, project ID, zone, and instance name. Therefore interactive serial console support should be disabled.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Login to Google Cloud console.
1. Go to Computer Engine.
1. Go to VM instances.
1. Click on the specific VM.
1. Click `EDIT`.
1. in the `Remote access` section, clear the `Enable connecting to serial ports`.
1. Click `Save`.

### From the command line{% #from-the-command-line %}

Use the following command to disable connecting to serial ports:

```
gcloud compute instances add-metadata <INSTANCE_NAME> --zone=<ZONE> --metadata=serial-port-enable=false
```

or

```
gcloud compute instances add-metadata <INSTANCE_NAME> --zone=<ZONE> --metadata=serial-port-enable=0
```

## Prevention{% #prevention %}

You can prevent VMs from having serial port access by enabling the `Disable VM serial port access` organization policy: [https://console.cloud.google.com/iam-admin/orgpolicies/compute-disableSerialPortAccess](https://console.cloud.google.com/iam-admin/orgpolicies/compute-disableSerialPortAccess)

## Default value{% #default-value %}

By default, connecting to serial ports is not enabled.

## References{% #references %}

1. [https://cloud.google.com/compute/docs/instances/interacting-with-serial-console](https://cloud.google.com/compute/docs/instances/interacting-with-serial-console)

## CIS Controls{% #cis-controls %}

Version 8 - 4.8: Uninstall or Disable Unnecessary Services on Enterprise Assets and Software

- Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web application module, or service function.

Version 7 - 9.2 Ensure Only Approved Ports, Protocols and Services Are Running

- Ensure Only Approved Ports, Protocols and Services Are Running

# Source: https://docs.datadoghq.com/security/default_rules/hvr-5bi-sf6.md

---
title: Docker daemon activities should be audited
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Docker daemon activities should be
  audited
---

# Docker daemon activities should be audited
Classification:complianceFramework:cis-dockerControl:1.2.3
## Description{% #description %}

Audit all Docker daemon activities.

## Rationale{% #rationale %}

As well as auditing the normal Linux file system and system calls, you should also audit the Docker daemon. Because this daemon runs with root privileges, it is very important to audit its activities and usage.

## Audit{% #audit %}

Verify that there are audit rules for the Docker daemon. To see the rules associated with the Docker daemon, run:

```bash
auditctl -l | grep /usr/bin/dockerd
```

## Remediation{% #remediation %}

You should add rules for the Docker daemon. For example, add the following line to a new file in `/etc/audit/rules.d/`. For instance, create a file named `docker.rules`:

```bash
echo "-w /usr/bin/dockerd -k docker" > /etc/audit/rules.d/docker.rules
```

Then, reload the audit rules:

```bash
augenrules --load
```

Next, restart the audit daemon using the following command:

```bash
service auditd restart
```

## Impact{% #impact %}

Auditing can generate large log files. You should ensure that these are rotated and archived periodically. A separate partition should also be created for audit logs to avoid filling up any other critical partition.

## Default value{% #default-value %}

By default, the Docker daemon is not audited.

## References{% #references %}

1. [https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html)

## CIS controls{% #cis-controls %}

Version 6.6.2 Ensure Audit Log Settings Support Appropriate Log Entry Formatting - Validate audit log settings for each hardware device and the software installed on it, ensuring that logs include a date, timestamp, source addresses, destination addresses, and various other useful elements of each packet and/or transaction. Systems should record logs in a standardized format such as syslog entries or those outlined by the Common Event Expression initiative. If systems cannot generate logs in a standardized format, log normalization tools can be deployed to convert logs into such a format.

Version 7.6.2 Activate audit logging - Ensure that local logging has been enabled on all systems and networking devices.

Version 6.3 Enable Detailed Logging - Enable system logging to include detailed information such as an event source, date, user, timestamp, source addresses, destination addresses, and other useful elements.

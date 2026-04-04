# Source: https://docs.datadoghq.com/security/default_rules/wbd-dbk-yf8.md

---
title: /var/lib/docker should be audited
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > /var/lib/docker should be audited
---

# /var/lib/docker should be audited
Classification:complianceFramework:cis-dockerControl:1.2.4
## Description{% #description %}

Audit `/var/lib/docker`.

## Rationale{% #rationale %}

As well as auditing the Linux file system and system calls, you should also audit all Docker-related files and directories. The Docker daemon runs with root privileges and its behavior depends on some key files and directories. For example, audit `/var/lib/docker`, which holds all the information about containers.

## Audit{% #audit %}

Verify that there is an audit rule applied to the `/var/lib/docker` directory. To see the rule for the `/var/lib/docker` directory, run:

```bash
auditctl -l | grep /var/lib/docker
```

## Remediation{% #remediation %}

You should add a rule for the `/var/lib/docker` directory. For example, add the following line to a new file in `/etc/audit/rules.d/`. For instance, create a file named `docker.rules`:

```bash
echo "-w /var/lib/docker -k docker" > /etc/audit/rules.d/docker.rules
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

By default, Docker-related files and directories are not audited.

## References{% #references %}

1. [https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html)

## CIS controls{% #cis-controls %}

Version 6.14.6 Enforce Detailed Audit Logging For Sensitive Information - Enforce detailed audit logging for access to nonpublic data and special authentication for sensitive data.

Version 7.14.9 Enforce Detail Logging for Access or Changes to Sensitive Data - Enforce detailed audit logging for access to sensitive data or changes to sensitive data (utilizing tools such as File Integrity Monitoring or Security Information and Event Monitoring).

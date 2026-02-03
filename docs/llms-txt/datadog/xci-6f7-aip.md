# Source: https://docs.datadoghq.com/security/default_rules/xci-6f7-aip.md

---
title: The default Docker configuration file should be audited on RHEL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The default Docker configuration file
  should be audited on RHEL
---

# The default Docker configuration file should be audited on RHEL
Classification:complianceFramework:cis-dockerControl:1.2.9 
## Description{% #description %}

Audit `/etc/sysconfig/docker`, if applicable.

## Rationale{% #rationale %}

As well as auditing the Linux file system and system calls, you should also audit the Docker daemon. Because this daemon runs with root privileges, it is very important to audit its activities and usage. Its behavior depends on some key files and directories, including `/etc/sysconfig/docker`. It contains various parameters related to the Docker daemon when run on CentOS and RHEL based distributions. If present, it is important that it is audited.

## Audit{% #audit %}

Verify that there is an audit rule associated with the `/etc/sysconfig/docker` file. To see the rule for the `/etc/sysconfig/docker` file, run:

```bash
auditctl -l | grep /etc/sysconfig/docker
```

## Remediation{% #remediation %}

You should add a rule for the `/etc/sysconfig/docker` file. For example, add the following line to a new file in `/etc/audit/rules.d/`. For instance, create a file named `docker.rules`:

```bash
echo "-w /etc/sysconfig/docker -k docker" > /etc/audit/rules.d/docker.rules
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

By default, Docker-related files and directories are not audited. The file `/etc/sysconfig/docker` may not be present on the system and in that case, this recommendation is not applicable.

## References{% #references %}

1. [https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html)

## CIS controls{% #cis-controls %}

Version 6.14.6 Enforce Detailed Audit Logging For Sensitive Information - Enforce detailed audit logging for access to nonpublic data and special authentication for sensitive data.

Version 7.14.9 Enforce Detail Logging for Access or Changes to Sensitive Data - Enforce detailed audit logging for access to sensitive data or changes to sensitive data (utilizing tools such as File Integrity Monitoring or Security Information and Event Monitoring).

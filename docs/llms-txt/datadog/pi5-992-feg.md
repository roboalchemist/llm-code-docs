# Source: https://docs.datadoghq.com/security/default_rules/pi5-992-feg.md

---
title: The docker.service file should have auditing configured if applicable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The docker.service file should have
  auditing configured if applicable
---

# The docker.service file should have auditing configured if applicable
Classification:complianceFramework:cis-dockerControl:1.2.6
## Description{% #description %}

Audit the `docker.service` if applicable.

## Rationale{% #rationale %}

As well as auditing the Linux file system and system calls, you should also audit all Docker-related files and directories. The Docker daemon runs with root privileges and its behavior depends on some key files and directories, including `docker.service`. The `docker.service` file might be present if the daemon parameters have been changed by an administrator. If so, it holds various parameters for the Docker daemon and should be audited.

## Audit{% #audit %}

1. **Locate** the `docker.service` file by running:

   ```bash
   systemctl show -p FragmentPath docker.service
   ```

If the file does not exist, this recommendation does not apply.

1. **Verify** if there is an audit rule corresponding to the `docker.service` file by running:

   ```bash
   auditctl -l | grep docker.service
   ```

## Remediation{% #remediation %}

1. **Create a new audit rule file** if the file exists. For example:

   ```bash
   echo "-w /usr/lib/systemd/system/docker.service -k docker" > /etc/audit/rules.d/docker.rules
   ```

1. **Reload** the audit rules:

   ```bash
   augenrules --load
   ```

1. **Restart** the audit daemon:

   ```bash
   service auditd restart
   ```

## Impact{% #impact %}

Auditing can generate large log files. You should ensure that these are rotated and archived periodically. A separate partition should also be created for audit logs to avoid filling up any other critical partition.

## Default value{% #default-value %}

By default, Docker-related files and directories are not audited. The file `docker.service` may not be present on the system.

## References{% #references %}

1. [https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html)

## CIS controls{% #cis-controls %}

Version 6.14.6 Enforce Detailed Audit Logging For Sensitive Information - Enforce detailed audit logging for access to nonpublic data and special authentication for sensitive data.

Version 7.14.9 Enforce Detail Logging for Access or Changes to Sensitive Data - Enforce detailed audit logging for access to sensitive data or changes to sensitive data (utilizing tools such as File Integrity Monitoring or Security Information and Event Monitoring).

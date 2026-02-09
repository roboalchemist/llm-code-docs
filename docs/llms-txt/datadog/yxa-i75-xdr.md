# Source: https://docs.datadoghq.com/security/default_rules/yxa-i75-xdr.md

---
title: The docker.socket file should be audited, if applicable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The docker.socket file should be
  audited, if applicable
---

# The docker.socket file should be audited, if applicable
Classification:complianceFramework:cis-dockerControl:1.2.7 
## Description{% #description %}

Audit `docker.socket`, if applicable.

## Rationale{% #rationale %}

As well as auditing the Linux file system and system calls, you should also audit the Docker daemon. Because this daemon runs with root privileges, it is very important to audit its activities and usage. Its behavior depends on some key files and directories, including the `docker.socket` file, which holds various parameters for the Docker daemon, it should be audited.

## Audit{% #audit %}

1. Locate the `docker.socket` file by running:

   ```bash
   systemctl show -p FragmentPath docker.socket
   ```

1. If the file does not exist, this recommendation is not applicable. If the `docker.socket` file exists, verify that there is an audit rule corresponding to the `docker.socket` file by running:

   ```bash
   auditctl -l | grep docker.socket
   ```

## Remediation{% #remediation %}

If the file exists, you should add a rule for it. For example, add the following line to a new file in `/etc/audit/rules.d/`. For instance, create a file named `docker.rules`:

```bash
echo "-w /usr/lib/systemd/system/docker.socket -k docker" > /etc/audit/rules.d/docker.rules
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

By default, Docker-related files and directories are not audited. The file `docker.socket` may not be present, but if it is, it should be audited.

## References{% #references %}

1. [https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html)

## CIS controls{% #cis-controls %}

Version 6.14.6 Enforce Detailed Audit Logging For Sensitive Information - Enforce detailed audit logging for access to nonpublic data and special authentication for sensitive data.

Version 7.14.9 Enforce Detail Logging for Access or Changes to Sensitive Data - Enforce detailed audit logging for access to sensitive data or changes to sensitive data (utilizing tools such as File Integrity Monitoring or Security Information and Event Monitoring).

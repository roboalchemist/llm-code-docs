# Source: https://docs.datadoghq.com/security/default_rules/3r2-3jv-hy5.md

---
title: /usr/bin/containerd should be audited if applicable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > /usr/bin/containerd should be audited
  if applicable
---

# /usr/bin/containerd should be audited if applicable
Classification:complianceFramework:cis-dockerControl:1.2.11
## Description{% #description %}

Audit `/usr/bin/containerd`, if applicable.

## Rationale{% #rationale %}

As well as auditing the Linux file system and system calls, you should also audit all Docker-related files and directories. The Docker daemon runs with root privileges and its behavior depends on some key files and directories, including `/usr/bin/containerd`, so it should be audited.

## Audit{% #audit %}

Verify that there is an audit rule corresponding to the `/usr/bin/containerd` file. To display the rule for the `/usr/bin/containerd` file, run:

```bash
auditctl -l | grep /usr/bin/containerd
```

## Remediation{% #remediation %}

You should add a rule for the `/usr/bin/containerd` file. For example, add the following line to a new file in `/etc/audit/rules.d/`. For instance, create a file named `docker.rules`:

```bash
echo "-w /usr/bin/containerd -k docker" > /etc/audit/rules.d/docker.rules
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

By default, Docker-related files and directories are not audited. The file `/usr/bin/containerd` may not be present on the system and in that case, this recommendation is not applicable.

## References{% #references %}

1. [https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/chap-system_auditing.html)
1. [https://github.com/docker/docker/pull/20662](https://github.com/docker/docker/pull/20662)
1. [https://containerd.tools/](https://containerd.tools/)

## CIS controls{% #cis-controls %}

Version 6.14.6 Enforce Detailed Audit Logging For Sensitive Information - Enforce detailed audit logging for access to nonpublic data and special authentication for sensitive data.

Version 7.14.9 Enforce Detail Logging for Access or Changes to Sensitive Data - Enforce detailed audit logging for access to sensitive data or changes to sensitive data (utilizing tools such as File Integrity Monitoring or Security Information and Event Monitoring).

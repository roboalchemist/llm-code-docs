# Source: https://docs.datadoghq.com/security/default_rules/def-000-rph.md

---
title: Verify Root Account Password Modifications on Host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Root Account Password
  Modifications on Host
---

# Verify Root Account Password Modifications on Host

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value                                 |
| ------ | ---------------------- | -------- | ------------------------------------------------- |
| 5      | 2                      | 5        | Monitor and investigate all root password changes |

Root account password modifications should be closely monitored and immediately investigated. The root account has unrestricted access to all system resources, making unauthorized password changes a critical security event that requires immediate attention and response.

## Compliance{% #compliance %}

- Monitor account password modifications ([found in CIS](https://www.cisecurity.org/cis-benchmarks))

## Documentation{% #documentation %}

The `passwd` command is used to change user account passwords on Linux systems. Root account password changes are particularly sensitive because the root account has complete control over the system.

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

You must have:

- `root` privileges or access to another privileged account
- Access to system audit logs and authentication logs
- Knowledge of authorized root password modifications procedures
- Access to recovery mechanisms (console access, single-user mode)
- Agent v7.27 or newer for Workload Security monitoring

### Step-by-step guide{% #step-by-step-guide %}

**Step 1: Investigate the Root Account Password Modifications Immediately**

Identify who modified the root password, when, and from where:

```bash
# Check authentication logs for passwd command execution on root
sudo grep "passwd.*root" /var/log/auth.log | tail -20

# Review audit logs for root password changes
sudo ausearch -c passwd -ts recent | grep root

# Check for recent password changes in shadow file
sudo ls -la /etc/shadow

# Identify the user who executed the passwd command
sudo ausearch -c passwd -ts recent -i

# Check active root sessions and login history
who
last | grep root
```

**Step 2: Verify Authorization with System Administrators**

Immediately verify if the root password change was authorized:

- Check if the change was made by the account owner or administrator
- Review change management tickets or approval records
- Contact the user or administrator who made the change
- Check if the change aligns with scheduled maintenance or rotation policies

# Source: https://docs.datadoghq.com/security/default_rules/def-000-aph.md

---
title: Verify Non-Root Password Modifications on Host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Non-Root Password Modifications
  on Host
---

# Verify Non-Root Password Modifications on Host

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value                            |
| ------ | ---------------------- | -------- | -------------------------------------------- |
| 3      | 2                      | 3        | Monitor and investigate all password changes |

User account password modifications should be monitored and investigated to detect unauthorized access attempts, privilege escalation, and account compromise. All password changes on host systems should be reviewed to ensure they are authorized and legitimate.

## Compliance{% #compliance %}

- Monitor account password modifications ([found in CIS](https://www.cisecurity.org/cis-benchmarks))

## Documentation{% #documentation %}

The `passwd` command is used to change user account passwords on Linux systems. While legitimate password changes are a normal part of system administration, unauthorized or unexpected password modifications should be audited based on organizational policies.

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

You must have:

- `root` or `sudo` privileges to investigate password changes
- Access to system audit logs and authentication logs
- Knowledge of authorized password change procedures in your environment
- Agent v7.27 or newer for Workload Security monitoring

### Step-by-step guide{% #step-by-step-guide %}

#### Step 1: Investigate the password change{% #step-1-investigate-the-password-change %}

Identify who changed the password, when, and from where:

```bash
# Check authentication logs for passwd command execution
sudo grep "passwd" /var/log/auth.log | tail -20

# Review audit logs for password changes
sudo ausearch -c passwd -ts recent

# Check for recent password changes in shadow file
sudo ls -la /etc/shadow

# Review command history for the user who executed passwd
sudo cat /home/[username]/.bash_history | grep passwd

# Check active sessions and login history
who
last -20
```

#### Step 2: Verify authorization{% #step-2-verify-authorization %}

Determine if the password change was authorized:

- Check if the change was made by the account owner or administrator
- Review change management tickets or approval records
- Contact the user or administrator who made the change
- Check if the change aligns with scheduled maintenance or rotation policies

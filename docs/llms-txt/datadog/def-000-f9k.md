# Source: https://docs.datadoghq.com/security/default_rules/def-000-f9k.md

---
title: Verify User Account Creation on Host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify User Account Creation on Host
---

# Verify User Account Creation on Host

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value                                                |
| ------ | ---------------------- | -------- | ---------------------------------------------------------------- |
| 3      | 2                      | 3        | Monitor and investigate all interactive user creation activities |

Interactive user account creation should be monitored and investigated to detect unauthorized account creation, privilege escalation attempts, and persistence mechanisms. User creation activities should align with organizational onboarding and access management policies.

## Compliance{% #compliance %}

- Monitor user account creation ([found in CIS](https://www.cisecurity.org/cis-benchmarks))

## Documentation{% #documentation %}

Interactive user account creation involves creating new user accounts on Linux systems through commands like `useradd` or `adduser` executed from an interactive terminal (TTY).

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

You must have:

- `root` or `sudo` privileges to investigate user creation
- Access to system audit logs and authentication logs
- Knowledge of authorized user provisioning procedures
- Understanding of organizational access management policies
- Agent v7.27 or newer for Workload Security monitoring

### Step-by-step guide{% #step-by-step-guide %}

#### Step 1: Investigate the user creation{% #step-1-investigate-the-user-creation %}

Identify which user was created, by whom, and when:

```bash
# Check authentication logs for user creation commands
sudo grep -E "useradd|adduser" /var/log/auth.log | tail -20

# Review audit logs for user creation activities
sudo ausearch -m ADD_USER -ts recent
sudo ausearch -m USER_MGMT -ts recent

# Check recent user account additions
sudo cat /etc/passwd | tail -10

# Review command history for the administrator who created the user
sudo cat /root/.bash_history | grep -E "useradd|adduser"

# Check when the user account was created
sudo ls -la /home/ | grep [username]
```

#### Step 2: Verify authorization{% #step-2-verify-authorization %}

Determine if the user creation was authorized:

- Verify with HR or management for employee onboarding
- Review change management tickets or approval records
- Check if the creation aligns with access provisioning policies
- Contact the administrator who created the account

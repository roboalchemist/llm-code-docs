# Source: https://docs.datadoghq.com/security/default_rules/def-000-mhp.md

---
title: Verify User Permission Modifications on Host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify User Permission Modifications on
  Host
---

# Verify User Permission Modifications on Host

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value                                          |
| ------ | ---------------------- | -------- | ---------------------------------------------------------- |
| 4      | 2                      | 4        | Monitor and investigate all user access removal activities |

User permission modifications should be monitored and investigated to detect potential impact events, unauthorized account manipulation, or attempts to disrupt system operations. User permission modifications should align with organizational offboarding and access management policies.

## Compliance{% #compliance %}

- Monitor user permission modifications ([found in CIS](https://www.cisecurity.org/cis-benchmarks))

## Documentation{% #documentation %}

User permission modifications activities involve deleting user accounts or disabling user access through account locking, expiration, or inactivation. This detection monitors two primary methods of user access removal:

1. **User account deletion**: Complete removal of user accounts from the system using commands like `userdel`
1. **Account locking/disabling**: Using `passwd` command with flags to lock (`-l`), expire (`-e`), or inactivate (`-i`) user accounts

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

You must have:

- `root` or `sudo` privileges to investigate user permission modifications
- Access to system audit logs and authentication logs
- Knowledge of authorized user management procedures
- User account backup, or directory service access, for recovery
- Agent v7.27 or newer for Workload Security monitoring

### Step-by-step guide{% #step-by-step-guide %}

#### Step 1: Investigate the user access removal{% #step-1-investigate-the-user-access-removal %}

Identify what user access was removed, by whom, and when:

```bash
# Check authentication logs for user deletion or account locking
sudo grep -E "userdel|passwd.*-l|passwd.*-e|passwd.*-i" /var/log/auth.log | tail -20

# Review audit logs for user management activities
sudo ausearch -m USER_MGMT -ts recent
sudo ausearch -m DEL_USER -ts recent

# Check for account status changes
sudo grep "account" /var/log/secure | tail -20

# Review command history for the administrator who made changes
sudo cat /root/.bash_history | grep -E "userdel|passwd"
```

#### Step 2: Verify authorization{% #step-2-verify-authorization %}

Determine if the user access removal was authorized:

- Verify with HR or management for employee offboarding
- Review change management tickets or approval records
- Check if the removal aligns with access review or security policies
- Contact the administrator who performed the removal

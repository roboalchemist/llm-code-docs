# Source: https://docs.datadoghq.com/security/default_rules/def-000-spm.md

---
title: Verify Sudoers Policy File Modifications
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Sudoers Policy File
  Modifications
---

# Verify Sudoers Policy File Modifications

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value             |
| ------ | ---------------------- | -------- | ----------------------------- |
| 3      | 2                      | 2        | No unauthorized modifications |

Sudoers policy files should be protected from unauthorized modifications to maintain proper privilege escalation controls and prevent security bypasses.

## Compliance{% #compliance %}

- Monitor sudoers policy file integrity ([found in CIS](https://www.cisecurity.org/cis-benchmarks))

## Documentation{% #documentation %}

The sudoers policy file (`/etc/sudoers` and files in `/etc/sudoers.d/`) controls which users can execute commands with elevated privileges using the `sudo` command. This file is critical for maintaining proper access controls and preventing unauthorized privilege escalation.

File Integrity Monitoring (FIM) detects various types of modifications to sudoers policy files, including:

- **chmod**: Permission changes that could make the file writable by unauthorized users
- **chown**: Ownership changes that could transfer control to malicious actors
- **link/rename**: File system operations that could replace legitimate policies
- **open**: Write operations that modify policy content
- **unlink**: Deletion attempts that could remove security controls
- **utimes**: Timestamp modifications that could hide evidence of tampering

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

You must have

- `root` privileges to modify sudoers policy files
- Access to system logs to investigate unauthorized changes
- Backup of known-good sudoers configuration
- Agent v7.27 or newer for File Integrity monitoring

### Step-by-step guide{% #step-by-step-guide %}

#### Step 1: Investigate the modification{% #step-1-investigate-the-modification %}

Review system logs to identify what changes were made and by whom:

```bash
# Check recent sudoers modifications
sudo find /etc -name "sudoers*" -exec ls -la {} \;

# Review audit logs for sudoers changes
sudo ausearch -f /etc/sudoers -ts recent

# Check system logs for related activity
sudo journalctl -u sudo -n 50
```

#### Step 2: Validate current sudoers configuration{% #step-2-validate-current-sudoers-configuration %}

Check the current sudoers configuration for unauthorized entries:

```bash
# Validate sudoers syntax
sudo visudo -c

# Review current sudoers content
sudo cat /etc/sudoers
sudo ls -la /etc/sudoers.d/
```

# Source: https://docs.datadoghq.com/security/default_rules/def-000-3zj.md

---
title: Verify SSH Keys Modified on Host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify SSH Keys Modified on Host
---

# Verify SSH Keys Modified on Host

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value             |
| ------ | ---------------------- | -------- | ----------------------------- |
| 3      | 2                      | 3        | No unauthorized modifications |

SSH Keys should only be modified through authorized processes by legitimate users or configuration management systems.

## Compliance{% #compliance %}

- File Integrity Monitoring requirement, [Found in PCI DSS 11.5](https://www.pcisecuritystandards.org/)

## Documentation{% #documentation %}

SSH authorized_keys files control which public keys are authorized to authenticate to a user account via SSH. These files are typically located at `~/.ssh/authorized_keys` for each user account.

File Integrity Monitoring (FIM) tracks changes to `authorized_keys` files by monitoring various file operations including:

- **chmod**: Permission changes that could make the file world-writable or readable by unauthorized users
- **chown**: Ownership changes that could allow unauthorized users to modify authentication settings
- **link**: Creation of hard or symbolic links that could redirect authentication to attacker-controlled key files
- **rename**: Moving or renaming key files, potentially to hide malicious keys or disable legitimate access
- **open**: File modifications that add attacker public keys or remove legitimate keys
- **unlink**: Deletion of authorized_keys files, potentially as part of covering tracks or denial of service
- **utimes**: Timestamp modifications that could hide evidence of unauthorized key additions

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

- You must have `root` or administrative privileges
- Access to system logs and audit trails
- Backup of known-good `authorized_keys` files or user management records
- List of legitimate SSH public keys and their owners

### Step-by-step guide{% #step-by-step-guide %}

**Step 1: Identify Modified File**

Review the Finding to determine which authorized_keys file was modified:

```bash
# Check file details
ls -la ~/.ssh/authorized_keys
ls -la /root/.ssh/authorized_keys
stat /home/username/.ssh/authorized_keys

# Find all authorized_keys files on the system
find / -name authorized_keys -type f 2>/dev/null
```

**Step 2: Review Current Contents**

Examine the current `authorized_keys` file:

```bash
# View the file contents
cat /home/username/.ssh/authorized_keys

# Count the number of keys
grep -c "^ssh-" /home/username/.ssh/authorized_keys

# Check file permissions (should be 600 or 400)
ls -l /home/username/.ssh/authorized_keys

# Check directory permissions (should be 700)
ls -ld /home/username/.ssh/
```

**Step 3: Verify Legitimate Change**

Check if the modification was authorized:

```bash
# Check who last modified the file
stat /home/username/.ssh/authorized_keys

# Review audit logs for the file modification
ausearch -f /home/username/.ssh/authorized_keys -ts recent
auditctl -l | grep authorized_keys

# Check sudo/su logs for administrative actions
grep -E "sudo|su" /var/log/auth.log | tail -20

# Review SSH login attempts
grep "Accepted publickey" /var/log/auth.log | tail -20
```

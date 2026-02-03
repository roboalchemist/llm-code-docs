# Source: https://docs.datadoghq.com/security/default_rules/def-000-4zi.md

---
title: Verify Essential Linux Binary Modified on Host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Essential Linux Binary Modified
  on Host
---

# Verify Essential Linux Binary Modified on Host

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value             |
| ------ | ---------------------- | -------- | ----------------------------- |
| 2      | 3                      | 2        | No unauthorized modifications |

Essential system binaries should remain unchanged unless modifications are part of authorized system updates or patches.

## Compliance{% #compliance %}

- File Integrity Monitoring requirement, [Found in PCI DSS 11.5](https://www.pcisecuritystandards.org/)

## Documentation{% #documentation %}

Essential system binaries are executable files that perform operating system functions and administrative tasks. These binaries typically reside in protected system directories such as `/bin`, `/sbin`, `/usr/bin`, and `/usr/sbin`.

File Integrity Monitoring (FIM) tracks changes to essential system files by monitoring various file operations including:

- **chmod**: Permission changes that could weaken security controls or grant unauthorized access
- **chown**: Ownership changes that could allow unauthorized users to control critical binaries
- **link**: Creation of hard or symbolic links that could redirect execution to malicious code
- **rename**: Moving or renaming binaries, potentially to hide malicious replacements
- **open**: File modifications that alter the binary's behavior or inject malicious code
- **unlink**: Deletion of critical binaries, potentially as part of an attack to disable security controls
- **utimes**: Timestamp modifications that could be used to hide evidence of tampering

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

- You must have `root` or administrative privileges
- Access to system logs and audit trails
- Backup of known-good system state or package manager database

### Step-by-step guide{% #step-by-step-guide %}

**Step 1: Identify Modified Binary**

Review the Finding to determine which essential Linux binary was modified and the nature of the change:

```bash
# Check file details
ls -l /path/to/modified/binary
stat /path/to/modified/binary
```

**Step 2: Verify Legitimate Change**

Check if the modification was part of an authorized system update:

```bash
# For Debian/Ubuntu systems
dpkg -V package-name

# Check recent package manager activity
grep "upgraded\|installed" /var/log/dpkg.log  # Debian/Ubuntu
```

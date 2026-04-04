# Source: https://docs.datadoghq.com/security/default_rules/def-000-r6b.md

---
title: Verify Systemd Service Modified on Host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Systemd Service Modified on Host
---

# Verify Systemd Service Modified on Host

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value             |
| ------ | ---------------------- | -------- | ----------------------------- |
| 4      | 3                      | 3        | No unauthorized modifications |

Systemd service files and configurations should remain unchanged unless modifications are part of authorized system administration, package management, or configuration management processes.

## Compliance{% #compliance %}

- File Integrity Monitoring requirement, [Found in PCI DSS 11.5](https://www.pcisecuritystandards.org/)

## Documentation{% #documentation %}

Systemd is the system and service manager for modern Linux distributions that is responsible for initializing the system and managing services throughout the system's runtime. Systemd service files typically reside in `/etc/systemd/system/`, `/usr/lib/systemd/system/`, and `/lib/systemd/system/`.

File Integrity Monitoring (FIM) tracks changes to systemd service files by monitoring various file operations including:

- **chmod**: Permission changes that could allow unauthorized users to modify service configurations
- **chown**: Ownership changes that could grant inappropriate access to service management
- **link**: Creation of hard or symbolic links that could redirect service execution to malicious binaries
- **rename**: Moving or renaming service files, potentially to disable security services or enable malicious ones
- **open**: File modifications that alter service behavior, commands, or execution parameters
- **unlink**: Deletion of service files, potentially disabling security controls or legitimate services
- **utimes**: Timestamp modifications that could hide evidence of service tampering

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

- You must have `root` or administrative privileges
- Access to system logs and audit trails
- Backup of known-good systemd configurations
- Understanding of your organization's service management policies

### Step-by-step guide{% #step-by-step-guide %}

**Step 1: Identify Modified Service**

Review the Finding to determine which `systemd` service file was modified:

```bash
# Check service file details
ls -l /etc/systemd/system/
ls -l /usr/lib/systemd/system/
stat /path/to/modified/service.service

# View service contents
cat /path/to/modified/service.service
```

**Step 2: Check Service Status and Configuration**

Examine the current state of the modified service:

```bash
# Check service status
systemctl status service-name.service

# Show service unit file
systemctl cat service-name.service

# List all enabled services
systemctl list-unit-files --state=enabled

# Check if service is masked
systemctl is-enabled service-name.service
```

**Step 3: Verify Legitimate Change**

Check if the modification was part of authorized system administration:

```bash
# Check recent package updates
grep "systemd" /var/log/dpkg.log     # Debian/Ubuntu

# Review systemd journal for service changes
journalctl -u service-name.service --since "1 day ago"

# Check audit logs for file modifications
ausearch -f /etc/systemd/system/service-name.service -ts recent
``
```

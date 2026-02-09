# Source: https://docs.datadoghq.com/security/default_rules/def-000-duv.md

---
title: Verify SSL Certificate Modified on Host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify SSL Certificate Modified on Host
---

# Verify SSL Certificate Modified on Host

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value             |
| ------ | ---------------------- | -------- | ----------------------------- |
| 4      | 3                      | 3        | No unauthorized modifications |

SSL/TLS certificates and certificate stores should remain unchanged unless modifications are part of authorized certificate updates, installations, or system package management.

## Compliance{% #compliance %}

- File Integrity Monitoring requirement, [Found in PCI DSS 11.5](https://www.pcisecuritystandards.org/)

## Documentation{% #documentation %}

SSL/TLS certificates are critical components of secure communications, establishing trust between clients and servers. Certificate stores typically reside in system directories such as `/etc/ssl/certs`, `/etc/pki/tls/certs`, and `/usr/share/ca-certificates`.

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

- You must have `root` or administrative privileges
- Access to system logs and audit trails
- Backup of known-good certificate store
- Understanding of your organization's certificate management policies

### Step-by-step guide{% #step-by-step-guide %}

**Step 1: Identify Modified Certificate**

Review the Finding to determine which certificate or certificate store file was modified:

```bash
# Check certificate details
ls -l /etc/ssl/certs/
stat /path/to/modified/certificate

# View certificate information
openssl x509 -in /path/to/modified/certificate -text -noout
```

**Step 2: Verify Legitimate Change**

Check if the modification was part of an authorized certificate update:

```bash
# Check recent certificate updates (Debian/Ubuntu)
grep "ca-certificates" /var/log/dpkg.log

# Check recent certificate updates (RHEL/CentOS)
grep "ca-certificates" /var/log/dnf.log

# Review system update logs
journalctl -u unattended-upgrades --since "1 day ago"
```

# Source: https://docs.datadoghq.com/security/default_rules/def-000-2zi.md

---
title: Remove ftp Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Remove ftp Package
---

# Remove ftp Package
 
## Description{% #description %}

FTP (File Transfer Protocol) is a traditional and widely used standard tool for transferring files between a server and clients over a network, especially where no authentication is necessary (permits anonymous users to connect to a server).

The `ftp` package can be removed with the following command:

```

$ apt-get remove ftp
```

## Rationale{% #rationale %}

FTP does not protect the confidentiality of data or authentication credentials. It is recommended SFTP be used if file transfer is required. Unless there is a need to run the system as a FTP server (for example, to allow anonymous downloads), it is recommended that the package be removed to reduce the potential attack surface.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove ftp
# from the system, and may remove any packages
# that depend on ftp. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "ftp"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Remove ftp Package: Ensure ftp is removed'
  ansible.builtin.package:
    name: ftp
    state: absent
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_ftp_removed
```

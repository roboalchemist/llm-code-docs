# Source: https://docs.datadoghq.com/security/default_rules/def-000-csn.md

---
title: Uninstall DHCP Server Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall DHCP Server Package
---

# Uninstall DHCP Server Package
 
## Description{% #description %}

If the system does not need to act as a DHCP server, the dhcp package can be uninstalled. The `isc-dhcp-server` package can be removed with the following command:

```

$ apt-get remove isc-dhcp-server
```

## Rationale{% #rationale %}

Removing the DHCP server ensures that it cannot be easily or accidentally reactivated and disrupt network operation.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove isc-dhcp-server
# from the system, and may remove any packages
# that depend on isc-dhcp-server. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "isc-dhcp-server"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall DHCP Server Package: Ensure isc-dhcp-server is removed'
  ansible.builtin.package:
    name: isc-dhcp-server
    state: absent
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - package_dhcp_removed
```

# Source: https://docs.datadoghq.com/security/default_rules/def-000-zpz.md

---
title: Uninstall net-snmp Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall net-snmp Package
---

# Uninstall net-snmp Package

## Description{% #description %}

The `snmp` package provides the snmpd service. The `snmp` package can be removed with the following command:

```

$ apt-get remove snmp
```

## Rationale{% #rationale %}

If there is no need to run SNMP server software, removing the package provides a safeguard against its activation.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove snmp
# from the system, and may remove any packages
# that depend on snmp. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "snmp"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall net-snmp Package: Ensure snmp is removed'
  ansible.builtin.package:
    name: snmp
    state: absent
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_net-snmp_removed
  - unknown_severity
```

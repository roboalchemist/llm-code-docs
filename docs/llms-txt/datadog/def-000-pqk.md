# Source: https://docs.datadoghq.com/security/default_rules/def-000-pqk.md

---
title: Uninstall ypserv Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall ypserv Package
---

# Uninstall ypserv Package

## Description{% #description %}

The `ypserv` package can be removed with the following command:

```

$ apt-get remove ypserv
```

## Rationale{% #rationale %}

The NIS service provides an unencrypted authentication service which does not provide for the confidentiality and integrity of user passwords or the remote session. Removing the `ypserv` package decreases the risk of the accidental (or intentional) activation of NIS or NIS+ services.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove ypserv
# from the system, and may remove any packages
# that depend on ypserv. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "ypserv"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall ypserv Package: Ensure ypserv is removed'
  ansible.builtin.package:
    name: ypserv
    state: absent
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-IA-5(1)(c)
  - PCI-DSS-Req-2.2.2
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - high_severity
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_ypserv_removed
```

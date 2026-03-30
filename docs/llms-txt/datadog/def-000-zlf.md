# Source: https://docs.datadoghq.com/security/default_rules/def-000-zlf.md

---
title: Uninstall bind Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall bind Package
---

# Uninstall bind Package

## Description{% #description %}

The `named` service is provided by the `bind` package. The `bind` package can be removed with the following command:

```

$ apt-get remove bind
```

## Rationale{% #rationale %}

If there is no need to make DNS server software available, removing it provides a safeguard against its activation.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove bind9
# from the system, and may remove any packages
# that depend on bind9. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "bind9"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall bind Package: Ensure bind9 is removed'
  ansible.builtin.package:
    name: bind9
    state: absent
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_bind_removed
```

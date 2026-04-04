# Source: https://docs.datadoghq.com/security/default_rules/def-000-dsi.md

---
title: Uninstall apache2 Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall apache2 Package
---

# Uninstall apache2 Package

## Description{% #description %}

The `apache2` package can be removed with the following command:

```

$ apt-get remove apache2
```

## Rationale{% #rationale %}

If there is no need to make the web server software available, removing it provides a safeguard against its activation.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove apache2
# from the system, and may remove any packages
# that depend on apache2. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "apache2"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall apache2 Package: Ensure apache2 is removed'
  ansible.builtin.package:
    name: apache2
    state: absent
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_httpd_removed
  - unknown_severity
```

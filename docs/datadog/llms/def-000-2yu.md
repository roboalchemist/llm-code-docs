# Source: https://docs.datadoghq.com/security/default_rules/def-000-2yu.md

---
title: Uninstall nginx Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall nginx Package
---

# Uninstall nginx Package

## Description{% #description %}

The `nginx` package can be removed with the following command:

```

$ apt-get remove nginx
```

## Rationale{% #rationale %}

If there is no need to make the web server software available, removing it provides a safeguard against its activation.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove nginx
# from the system, and may remove any packages
# that depend on nginx. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "nginx"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall nginx Package: Ensure nginx is removed'
  ansible.builtin.package:
    name: nginx
    state: absent
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_nginx_removed
  - unknown_severity
```

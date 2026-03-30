# Source: https://docs.datadoghq.com/security/default_rules/def-000-5hv.md

---
title: Uninstall dovecot Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall dovecot Package
---

# Uninstall dovecot Package

## Description{% #description %}

The `dovecot-core` package can be removed with the following command:

```

$ apt-get remove dovecot-core
```

## Rationale{% #rationale %}

If there is no need to make the Dovecot software available, removing it provides a safeguard against its activation.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove dovecot-core
# from the system, and may remove any packages
# that depend on dovecot-core. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "dovecot-core"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall dovecot Package: Ensure dovecot-core is removed'
  ansible.builtin.package:
    name: dovecot-core
    state: absent
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_dovecot_removed
  - unknown_severity
```

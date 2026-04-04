# Source: https://docs.datadoghq.com/security/default_rules/def-000-gzr.md

---
title: Uninstall squid Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall squid Package
---

# Uninstall squid Package

## Description{% #description %}

The `squid` package can be removed with the following command:

```
 $ apt-get remove squid
```

## Rationale{% #rationale %}

If there is no need to make the proxy server software available, removing it provides a safeguard against its activation.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove squid
# from the system, and may remove any packages
# that depend on squid. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "squid"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Uninstall squid Package: Ensure squid is removed'
  ansible.builtin.package:
    name: squid
    state: absent
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_squid_removed
  - unknown_severity
```

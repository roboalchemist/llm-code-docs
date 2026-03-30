# Source: https://docs.datadoghq.com/security/default_rules/def-000-ci5.md

---
title: Ensure LDAP client is not installed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure LDAP client is not installed
---

# Ensure LDAP client is not installed

## Description{% #description %}

The Lightweight Directory Access Protocol (LDAP) is a service that provides a method for looking up information from a central database. The `ldap-utils` package can be removed with the following command:

```

$ apt-get remove ldap-utils
```

## Rationale{% #rationale %}

If the system does not need to act as an LDAP client, it is recommended that the software is removed to reduce the potential attack surface.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove ldap-utils
# from the system, and may remove any packages
# that depend on ldap-utils. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "ldap-utils"
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: 'Ensure LDAP client is not installed: Ensure ldap-utils is removed'
  ansible.builtin.package:
    name: ldap-utils
    state: absent
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_openldap-clients_removed
```

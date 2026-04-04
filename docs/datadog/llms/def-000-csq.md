# Source: https://docs.datadoghq.com/security/default_rules/def-000-csq.md

---
title: Remove NIS Client
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Remove NIS Client
---

# Remove NIS Client

## Description{% #description %}

The Network Information Service (NIS), formerly known as Yellow Pages, is a client-server directory service protocol used to distribute system configuration files. The NIS client (`ypbind`) was used to bind a system to an NIS server and receive the distributed configuration files.

## Rationale{% #rationale %}

The NIS service is inherently an insecure system that has been vulnerable to DOS attacks, buffer overflows and has poor authentication for querying NIS maps. NIS generally has been replaced by such protocols as Lightweight Directory Access Protocol (LDAP). It is recommended that the service be removed.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# CAUTION: This remediation script will remove ypbind
#      from the system, and may remove any packages
#      that depend on ypbind. Execute this
#      remediation AFTER testing on a non-production
#      system!

if rpm -q --quiet "ypbind" ; then

    yum remove -y "ypbind"

fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Ensure ypbind is removed
  package:
    name: ypbind
    state: absent
  tags:
  - CCE-27396-1
  - PCI-DSSv4-2.2.4
  - disable_strategy
  - low_complexity
  - low_disruption
  - no_reboot_needed
  - package_ypbind_removed
  - unknown_severity
```

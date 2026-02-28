# Source: https://docs.datadoghq.com/security/default_rules/def-000-8iq.md

---
title: >-
  Make sure that the dconf databases are up-to-date with regards to respective
  keyfiles
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Make sure that the dconf databases are
  up-to-date with regards to respective keyfiles
---

# Make sure that the dconf databases are up-to-date with regards to respective keyfiles

## Description{% #description %}

By default, DConf uses a binary database as a data backend. The system-level database is compiled from keyfiles in the /etc/dconf/db/ directory by the

```
dconf update
```

command. More specifically, content present in the following directories:

```
/etc/dconf/db/gdm.d
```

```
/etc/dconf/db/local.d
```

## Rationale{% #rationale %}

Unlike text-based keyfiles, the binary database is impossible to check by OVAL. Therefore, in order to evaluate dconf configuration, both have to be true at the same time - configuration files have to be compliant, and the database needs to be more recent than those keyfiles, which gives confidence that it reflects them.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if rpm --quiet -q gdm && { [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; }; then

dconf update

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```go
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - CCE-81004-4
  - PCI-DSS-Req-6.2
  - PCI-DSSv4-8.2.8
  - dconf_db_up_to_date
  - high_severity
  - low_complexity
  - medium_disruption
  - no_reboot_needed
  - unknown_strategy

- name: Run dconf update
  ansible.builtin.command:
    cmd: dconf update
  when:
  - '"gdm" in ansible_facts.packages'
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-81004-4
  - PCI-DSS-Req-6.2
  - PCI-DSSv4-8.2.8
  - dconf_db_up_to_date
  - high_severity
  - low_complexity
  - medium_disruption
  - no_reboot_needed
  - unknown_strategy
```

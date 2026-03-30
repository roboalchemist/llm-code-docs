# Source: https://docs.datadoghq.com/security/default_rules/def-000-3om.md

---
title: Ensure a Table Exists for Nftables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure a Table Exists for Nftables
---

# Ensure a Table Exists for Nftables

## Description{% #description %}

Tables in nftables hold chains. Each table only has one address family and only applies to packets of this family. Tables can have one of six families.

## Rationale{% #rationale %}

Nftables doesn't have any default tables. Without a table being built, nftables will not filter network traffic.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'nftables' 2>/dev/null | grep -q '^installed$'; then

var_nftables_family='inet'

var_nftables_table='filter'


if ! nft list table $var_nftables_family $var_nftables_table; then
  nft create table "$var_nftables_family" "$var_nftables_table"
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_table
- name: XCCDF Value var_nftables_family # promote to variable
  set_fact:
    var_nftables_family: !!str inet
  tags:
    - always
- name: XCCDF Value var_nftables_table # promote to variable
  set_fact:
    var_nftables_table: !!str filter
  tags:
    - always

- name: Collect Existing Nftables
  ansible.builtin.command: nft list table {{ var_nftables_family }} {{ var_nftables_table
    }}
  register: result_nftables_table_family
  changed_when: false
  failed_when: result_nftables_table_family.rc not in [0, 1]
  when: '"nftables" in ansible_facts.packages'
  tags:
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_table

- name: Set Nftable Table
  ansible.builtin.command: nft create table {{ var_nftables_family }} {{ var_nftables_table
    }}
  when:
  - '"nftables" in ansible_facts.packages'
  - result_nftables_table_family is not skipped
  - result_nftables_table_family.rc != 0
  tags:
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_table
```

## Warning{% #warning %}

Adding or editing rules in a running nftables can cause loss of connectivity to the system.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-wr3.md

---
title: Ensure Base Chains Exist for Nftables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure Base Chains Exist for Nftables
---

# Ensure Base Chains Exist for Nftables

## Description{% #description %}

Tables in nftables hold chains. Each table only has one address family and only applies to packets of this family. Tables can have one of six families. Chains are containers for rules. They exist in two kinds, base chains and regular chains. A base chain is an entry point for packets from the networking stack, a regular chain may be used as jump target and is used for better rule organization.

## Rationale{% #rationale %}

If a base chain doesn't exist with a hook for input, forward, and delete, packets that would flow through those chains will not be touched by nftables.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'nftables' 2>/dev/null | grep -q '^installed$'; then

#Name of the table
var_nftables_table='filter'

#Familiy of the table
var_nftables_family='inet'

#Name(s) of base chain
var_nftables_base_chain_names='input,forward,output'

#Type(s) of base chain
var_nftables_base_chain_types='filter,filter,filter'

# Hooks for base chain
var_nftables_base_chain_hooks='input,forward,output'

#Priority
var_nftables_base_chain_priorities='0,0,0'

#Policy
var_nftables_base_chain_policies='accept,accept,accept'


#Transfer some of strings to arrays
IFS="," read -r -a  names <<< "$var_nftables_base_chain_names"
IFS="," read -r -a  types <<< "$var_nftables_base_chain_types"
IFS="," read -r -a  hooks <<< "$var_nftables_base_chain_hooks"
IFS="," read -r -a  priorities <<< "$var_nftables_base_chain_priorities"
IFS="," read -r -a  policies <<< "$var_nftables_base_chain_policies"

my_cmd="nft list tables | grep '$var_nftables_family $var_nftables_table'"
eval IS_TABLE_EXIST=\$\($my_cmd\)
if [ -z "$IS_TABLE_EXIST" ]
then
  # We create a table and add chains to it
  nft create table "$var_nftables_family" "$var_nftables_table"
  num_of_chains=${#names[@]}
  for ((i=0; i < num_of_chains; i++))
  do
   chain_to_add="add chain $var_nftables_family $var_nftables_table ${names[$i]} { type ${types[$i]} hook ${hooks[$i]} priority ${priorities[$i]} ; policy ${policies[$i]} ; }"
   my_cmd="nft '$chain_to_add'"
   eval $my_cmd
  done
else
  # We add missing chains to the existing table
  num_of_chains=${#names[@]}
  for ((i=0; i < num_of_chains; i++))
  do
    IS_CHAIN_EXIST=$(nft list table "$var_nftables_family" "$var_nftables_table" | grep "hook ${hooks[$i]}")
    if [ -z "$IS_CHAIN_EXIST" ]
      then
        chain_to_add="add chain '$var_nftables_family' '$var_nftables_table' ${names[$i]} { type ${types[$i]} hook ${hooks[$i]} priority ${priorities[$i]} ; policy ${policies[$i]} ; }"
        my_cmd="nft '$chain_to_add'"
        eval $my_cmd
    fi
  done
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
  - set_nftables_base_chain
- name: XCCDF Value var_nftables_table # promote to variable
  set_fact:
    var_nftables_table: !!str filter
  tags:
    - always
- name: XCCDF Value var_nftables_family # promote to variable
  set_fact:
    var_nftables_family: !!str inet
  tags:
    - always
- name: XCCDF Value var_nftables_base_chain_names # promote to variable
  set_fact:
    var_nftables_base_chain_names: !!str input,forward,output
  tags:
    - always
- name: XCCDF Value var_nftables_base_chain_types # promote to variable
  set_fact:
    var_nftables_base_chain_types: !!str filter,filter,filter
  tags:
    - always
- name: XCCDF Value var_nftables_base_chain_hooks # promote to variable
  set_fact:
    var_nftables_base_chain_hooks: !!str input,forward,output
  tags:
    - always
- name: XCCDF Value var_nftables_base_chain_priorities # promote to variable
  set_fact:
    var_nftables_base_chain_priorities: !!str 0,0,0
  tags:
    - always
- name: XCCDF Value var_nftables_base_chain_policies # promote to variable
  set_fact:
    var_nftables_base_chain_policies: !!str accept,accept,accept
  tags:
    - always

- name: Ensure Base Chains Exist for Nftables - Check Existence of Nftables Table
  ansible.builtin.shell: nft list tables | grep '{{ var_nftables_family }} {{ var_nftables_table
    }}'
  register: existing_nftables
  changed_when: false
  failed_when: false
  when: '"nftables" in ansible_facts.packages'
  tags:
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_base_chain

- name: Ensure Base Chains Exist for Nftables - Set NFTables Table
  ansible.builtin.command: nft create table {{ var_nftables_family }} {{ var_nftables_table
    }}
  when:
  - '"nftables" in ansible_facts.packages'
  - existing_nftables is not skipped and existing_nftables.rc > 0
  tags:
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_base_chain

- name: Ensure Base Chains Exist for Nftables - Add Base Chains
  ansible.builtin.command: nft 'add chain {{ var_nftables_family }} {{ var_nftables_table
    }} {{ item.0 }} { type {{ item.1 }} hook {{ item.2 }} priority {{ item.3 }} ;
    policy {{ item.4 }} ; }'
  with_together:
  - '{{ var_nftables_base_chain_names.split(",") }}'
  - '{{ var_nftables_base_chain_types.split(",") }}'
  - '{{ var_nftables_base_chain_hooks.split(",") }}'
  - '{{ var_nftables_base_chain_priorities.split(",") }}'
  - '{{ var_nftables_base_chain_policies.split(",") }}'
  when: '"nftables" in ansible_facts.packages'
  tags:
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_base_chain
```

## Warning{% #warning %}

Configuring rules over ssh, by creating a base chain with policy drop will cause loss of connectivity. Ensure that a rule allowing ssh has been added to the base chain prior to setting the base cahin's policy to drop

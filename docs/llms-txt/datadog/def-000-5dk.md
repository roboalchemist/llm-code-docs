# Source: https://docs.datadoghq.com/security/default_rules/def-000-5dk.md

---
title: Chrony Configure Pool and Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Chrony Configure Pool and Server
---

# Chrony Configure Pool and Server
 
## Description{% #description %}

`Chrony` is a daemon which implements the Network Time Protocol (NTP). It is designed to synchronize system clocks across a variety of systems and use a source that is highly accurate. More information on `chrony` can be found at [https://chrony-project.org/](https://chrony-project.org/). `Chrony` can be configured to be a client and/or a server. Add or edit server or pool lines to `/etc/chrony/chrony.conf` as appropriate:

```
server <remote-server>
```

Multiple servers may be configured.

## Rationale{% #rationale %}

If `chrony` is in use on the system proper configuration is vital to ensuring time synchronization is working properly.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' && { dpkg-query --show --showformat='${db:Status-Status}' 'chrony' 2>/dev/null | grep -q '^installed$'; }; then

var_multiple_time_servers='0.ubuntu.pool.ntp.org,1.ubuntu.pool.ntp.org,2.ubuntu.pool.ntp.org,3.ubuntu.pool.ntp.org'

var_multiple_time_pools='0.ubuntu.pool.ntp.org,1.ubuntu.pool.ntp.org,2.ubuntu.pool.ntp.org,3.ubuntu.pool.ntp.org'


config_file="/etc/chrony/chrony.conf"

# Check and configigure servers in /etc/chrony/chrony.conf
IFS="," read -a SERVERS <<< $var_multiple_time_servers
for srv in "${SERVERS[@]}"
do
   NTP_SRV=$(grep -w $srv $config_file)
   if [[ ! "$NTP_SRV" == "server "* ]]
   then
     time_server="server $srv"
     echo $time_server >> "$config_file"
   fi
done

# Check and configure pools in /etc/chrony/chrony.conf
IFS="," read -a POOLS <<< $var_multiple_time_pools
for srv in "${POOLS[@]}"
do
   NTP_POOL=$(grep -w $srv $config_file)
   if [[ ! "$NTP_POOL" == "pool "* ]]
   then
     time_server="pool $srv"
     echo $time_server >> "$config_file"
   fi
done

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
  - NIST-800-53-AU-8(1)(a)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.4.3
  - chronyd_configure_pool_and_server
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
- name: XCCDF Value var_multiple_time_servers # promote to variable
  set_fact:
    var_multiple_time_servers: !!str 0.ubuntu.pool.ntp.org,1.ubuntu.pool.ntp.org,2.ubuntu.pool.ntp.org,3.ubuntu.pool.ntp.org
  tags:
    - always
- name: XCCDF Value var_multiple_time_pools # promote to variable
  set_fact:
    var_multiple_time_pools: !!str 0.ubuntu.pool.ntp.org,1.ubuntu.pool.ntp.org,2.ubuntu.pool.ntp.org,3.ubuntu.pool.ntp.org
  tags:
    - always

- name: Chrony Configure Pool and Server - Add missing / update wrong records for
    remote time servers
  ansible.builtin.lineinfile:
    path: /etc/chrony/chrony.conf
    regexp: ^\s*\bserver\b\s*\b{{ item }}\b$
    state: present
    line: server {{ item }}
    create: true
  with_items:
  - '{{ var_multiple_time_servers.split(",") }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - '"chrony" in ansible_facts.packages'
  tags:
  - NIST-800-53-AU-8(1)(a)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.4.3
  - chronyd_configure_pool_and_server
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Chrony Configure Pool and Server - Add missing / update wrong records for
    remote time pools
  ansible.builtin.lineinfile:
    path: /etc/chrony/chrony.conf
    regexp: ^\s*\bpool\b\s*\b{{ item }}\b$
    state: present
    line: pool {{ item }}
    create: true
  with_items:
  - '{{ var_multiple_time_pools.split(",") }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - '"chrony" in ansible_facts.packages'
  tags:
  - NIST-800-53-AU-8(1)(a)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-10.4.3
  - chronyd_configure_pool_and_server
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```

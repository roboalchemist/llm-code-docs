# Source: https://docs.datadoghq.com/security/default_rules/def-000-mkc.md

---
title: Set configuration for IPv6 loopback traffic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Set configuration for IPv6 loopback
  traffic
---

# Set configuration for IPv6 loopback traffic
 
## Description{% #description %}

Configure the loopback interface to accept traffic. Configure all other interfaces to deny traffic to the loopback network.

## Rationale{% #rationale %}

Loopback traffic is generated between processes on machine and is typically critical to operation of the system. The loopback interface is the only place that loopback network traffic should be seen, all other interfaces should ignore traffic on this network as an anti-spoofing measure.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( ! ( dpkg-query --show --showformat='${db:Status-Status}' 'nftables' 2>/dev/null | grep -q '^installed$' ) && ! ( dpkg-query --show --showformat='${db:Status-Status}' 'ufw' 2>/dev/null | grep -q '^installed$' ) && dpkg-query --show --showformat='${db:Status-Status}' 'iptables' 2>/dev/null | grep -q '^installed$' ); then

if [ "$(sysctl -n net.ipv6.conf.all.disable_ipv6)" -eq 0 ]; then
  # IPv6 is not disabled, so run the script
  ip6tables -A INPUT -i lo -j ACCEPT
  ip6tables -A OUTPUT -o lo -j ACCEPT
  ip6tables -A INPUT -s ::1 -j DROP
fi

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
  - PCI-DSS-Req-1.3
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.1
  - medium_severity
  - set_ipv6_loopback_traffic

- name: Check if IPv6 is enabled
  command: sysctl -n net.ipv6.conf.all.disable_ipv6
  register: ipv6_status
  failed_when: ipv6_status.stdout != "0"
  when: ( not ( "nftables" in ansible_facts.packages ) and not ( "ufw" in ansible_facts.packages
    ) and "iptables" in ansible_facts.packages )
  tags:
  - PCI-DSS-Req-1.3
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.1
  - medium_severity
  - set_ipv6_loopback_traffic

- name: Allow incoming traffic on the loopback interface
  ansible.builtin.iptables:
    ipv6: true
    chain: INPUT
    in_interface: lo
    jump: ACCEPT
  when:
  - ( not ( "nftables" in ansible_facts.packages ) and not ( "ufw" in ansible_facts.packages
    ) and "iptables" in ansible_facts.packages )
  - ipv6_status.stdout == '0'
  tags:
  - PCI-DSS-Req-1.3
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.1
  - medium_severity
  - set_ipv6_loopback_traffic

- name: Allow outgoing traffic on the loopback interface
  ansible.builtin.iptables:
    ipv6: true
    chain: OUTPUT
    out_interface: lo
    jump: ACCEPT
  when:
  - ( not ( "nftables" in ansible_facts.packages ) and not ( "ufw" in ansible_facts.packages
    ) and "iptables" in ansible_facts.packages )
  - ipv6_status.stdout == '0'
  tags:
  - PCI-DSS-Req-1.3
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.1
  - medium_severity
  - set_ipv6_loopback_traffic

- name: Drop incoming traffic from the localhost
  ansible.builtin.iptables:
    ipv6: true
    chain: INPUT
    source: ::1
    jump: DROP
  when:
  - ( not ( "nftables" in ansible_facts.packages ) and not ( "ufw" in ansible_facts.packages
    ) and "iptables" in ansible_facts.packages )
  - ipv6_status.stdout == '0'
  tags:
  - PCI-DSS-Req-1.3
  - PCI-DSSv4-1.4
  - PCI-DSSv4-1.4.1
  - medium_severity
  - set_ipv6_loopback_traffic
```

## Warning{% #warning %}

Changing firewall settings while connected over network can result in being locked out of the system.

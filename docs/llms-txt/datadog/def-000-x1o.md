# Source: https://docs.datadoghq.com/security/default_rules/def-000-x1o.md

---
title: Set nftables Configuration for Loopback Traffic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Set nftables Configuration for Loopback
  Traffic
---

# Set nftables Configuration for Loopback Traffic
 
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
if ( dpkg-query --show --showformat='${db:Status-Status}' 'nftables' 2>/dev/null | grep -q '^installed$' && ! (systemctl is-active firewalld &>/dev/null) ); then

var_nftables_family='inet'



grubfile="/boot/grub/grub.cfg"

# Implement the loopback rules:
nft add rule inet filter input iif lo accept
nft add rule inet filter input ip saddr 127.0.0.0/8 counter drop

# Check IPv6 is disabled, if false implement IPv6 loopback rules
disabled="false"
[ -f "$grubfile" ] && ! grep "^\s*linux" "$grubfile" | grep -vq "ipv6.disable=1" && disabled="true"

grep -Eq "^\s*net\.ipv6\.conf\.all\.disable_ipv6\s*=\s*1\b(\s+#.*)?$" \
/etc/sysctl.conf /etc/sysctl.d/*.conf && \
grep -Eq "^\s*net\.ipv6\.conf\.default\.disable_ipv6\s*=\s*1\b(\s+#.*)?$" \
/etc/sysctl.conf /etc/sysctl.d/*.conf && sysctl net.ipv6.conf.all.disable_ipv6 | \
grep -Eq "^\s*net\.ipv6\.conf\.all\.disable_ipv6\s*=\s*1\b(\s+#.*)?$" && \
sysctl net.ipv6.conf.default.disable_ipv6 | \
grep -Eq "^\s*net\.ipv6\.conf\.default\.disable_ipv6\s*=\s*1\b(\s+#.*)?$" && disabled="true"

# Is IPv6 Disabled? (true/false)
if [ "$disabled" = false ] ; then
    nft add rule inet filter input ip6 saddr ::1 counter drop
fi


nft list ruleset > "/etc/${var_nftables_family}-filter.rules"

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
  - PCI-DSS-Req-1.4.1
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_loopback_traffic

- name: Implement Loopback Rules
  ansible.builtin.command: nft add rule inet filter input iif lo accept
  when: ( "nftables" in ansible_facts.packages )
  tags:
  - PCI-DSS-Req-1.4.1
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_loopback_traffic

- name: Create Rule to Drop Input IP Address from Loopback
  ansible.builtin.command: nft add rule inet filter input ip saddr 127.0.0.0/8 counter
    drop
  when: ( "nftables" in ansible_facts.packages )
  tags:
  - PCI-DSS-Req-1.4.1
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_loopback_traffic

- name: Check if IPv6 is Disabled in grub Configuration
  ansible.builtin.shell: |
    [ -z "$(grep "^\s*linux" /boot/grub2/grub.cfg | grep -v ipv6.disabled=1)" ]
  register: ipv6_status
  when: ( "nftables" in ansible_facts.packages )
  tags:
  - PCI-DSS-Req-1.4.1
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_loopback_traffic

- name: Check sysctl value of net.ipv6.conf.all.disable_ipv6
  sysctl:
    name: net.ipv6.conf.all.disable_ipv6
    state: present
    value: '1'
  check_mode: true
  register: sysctl_ipv6_all
  when: ( "nftables" in ansible_facts.packages )
  tags:
  - PCI-DSS-Req-1.4.1
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_loopback_traffic

- name: Check sysctl value of net.ipv6.conf.default.disable_ipv6
  sysctl:
    name: net.ipv6.conf.default.disable_ipv6
    state: present
    value: '1'
  check_mode: true
  register: sysctl_ipv6_default
  when: ( "nftables" in ansible_facts.packages )
  tags:
  - PCI-DSS-Req-1.4.1
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_loopback_traffic

- name: Implement IPv6 loopback rules
  ansible.builtin.command: nft add rule inet filter input ip6 saddr ::1 counter drop
  when:
  - ( "nftables" in ansible_facts.packages )
  - ipv6_status is not skipped
  - sysctl_ipv6_default is not skipped
  - sysctl_ipv6_all is not skipped
  - ipv6_status.rc == 0 or sysctl_ipv6_all.found > 0 or sysctl_ipv6_default.found
    > 0
  tags:
  - PCI-DSS-Req-1.4.1
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_nftables_loopback_traffic
```

## Warning{% #warning %}

Changing firewall settings while connected over network can result in being locked out of the system. Keep in mind the remediation makes changes only to the running system, in order to keep the changes need to take care to save the nft settings to the relvant configutation files.

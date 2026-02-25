# Source: https://docs.datadoghq.com/security/default_rules/def-000-bk3.md

---
title: Deactivate Wireless Network Interfaces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Deactivate Wireless Network Interfaces
---

# Deactivate Wireless Network Interfaces

## Description{% #description %}

Deactivating wireless network interfaces should prevent normal usage of the wireless capability.

Verify that there are no wireless interfaces configured on the system with the following command:

```
$ ls -L -d /sys/class/net/*/wireless | xargs dirname | xargs basename -a
```

## Rationale{% #rationale %}

The use of wireless networking can introduce many different attack vectors into the organization's network. Common attack vectors such as malicious association and ad hoc networks will allow an attacker to spoof a wireless access point (AP), allowing validated systems to connect to the malicious AP and enabling the attacker to monitor and record network traffic. These malicious APs can also serve to create a man-in-the-middle attack or be used to create a denial of service to valid network resources.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( ! ( [ -f /.dockerenv ] || [ -f /run/.containerenv ] ) ); then

if [ -n "$(find /sys/class/net/*/ -type d -name wireless)" ]; then
    interfaces=$(find /sys/class/net/*/wireless -type d -name wireless | xargs -0 dirname | xargs basename)

    for i in $interfaces; do
        ip link set dev "$i" down
        drivers=$(basename "$(readlink -f /sys/class/net/"$i"/device/driver)")
        echo "install $drivers /bin/false" >> /etc/modprobe.d/disable_wireless.conf
        modprobe -r "$drivers"
     done
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
  - DISA-STIG-UBTU-20-010455
  - NIST-800-171-3.1.16
  - NIST-800-53-AC-18(3)
  - NIST-800-53-AC-18(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - PCI-DSS-Req-1.3.3
  - PCI-DSSv4-1.3
  - PCI-DSSv4-1.3.3
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - unknown_strategy
  - wireless_disable_interfaces

- name: Service facts
  ansible.builtin.service_facts: null
  when: ( not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman",
    "container"] ) )
  tags:
  - DISA-STIG-UBTU-20-010455
  - NIST-800-171-3.1.16
  - NIST-800-53-AC-18(3)
  - NIST-800-53-AC-18(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - PCI-DSS-Req-1.3.3
  - PCI-DSSv4-1.3
  - PCI-DSSv4-1.3.3
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - unknown_strategy
  - wireless_disable_interfaces

- name: Ensure NetworkManager is installed
  ansible.builtin.package:
    name: '{{ item }}'
    state: present
  with_items:
  - NetworkManager
  when: ( not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman",
    "container"] ) )
  tags:
  - DISA-STIG-UBTU-20-010455
  - NIST-800-171-3.1.16
  - NIST-800-53-AC-18(3)
  - NIST-800-53-AC-18(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - PCI-DSS-Req-1.3.3
  - PCI-DSSv4-1.3
  - PCI-DSSv4-1.3.3
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - unknown_strategy
  - wireless_disable_interfaces

- name: NetworkManager Deactivate Wireless Network Interfaces
  command: nmcli radio wifi off
  when:
  - ( not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    ) )
  - '''NetworkManager'' in ansible_facts.packages'
  - ansible_facts.services['NetworkManager.service'].state == 'running'
  tags:
  - DISA-STIG-UBTU-20-010455
  - NIST-800-171-3.1.16
  - NIST-800-53-AC-18(3)
  - NIST-800-53-AC-18(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - PCI-DSS-Req-1.3.3
  - PCI-DSSv4-1.3
  - PCI-DSSv4-1.3.3
  - low_complexity
  - medium_disruption
  - medium_severity
  - no_reboot_needed
  - unknown_strategy
  - wireless_disable_interfaces
```

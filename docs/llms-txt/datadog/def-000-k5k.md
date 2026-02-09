# Source: https://docs.datadoghq.com/security/default_rules/def-000-k5k.md

---
title: Use Only Strong Key Exchange algorithms
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Use Only Strong Key Exchange algorithms
---

# Use Only Strong Key Exchange algorithms
 
## Description{% #description %}

Limit the Key Exchange to strong algorithms. The following line in `/etc/ssh/sshd_config` demonstrates use of those:

```
KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256
        
```

## Rationale{% #rationale %}

Key exchange is any method in cryptography by which cryptographic keys are exchanged between two parties, allowing use of a cryptographic algorithm. If the sender and receiver wish to exchange encrypted messages, each must be equipped to encrypt messages to be sent and decrypt messages received

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

sshd_strong_kex='curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256'


if [ -e "/etc/ssh/sshd_config" ] ; then
    
    LC_ALL=C sed -i "/^\s*KexAlgorithms\s\+/Id" "/etc/ssh/sshd_config"
else
    touch "/etc/ssh/sshd_config"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/ssh/sshd_config"

cp "/etc/ssh/sshd_config" "/etc/ssh/sshd_config.bak"
# Insert at the beginning of the file
printf '%s\n' "KexAlgorithms $sshd_strong_kex" > "/etc/ssh/sshd_config"
cat "/etc/ssh/sshd_config.bak" >> "/etc/ssh/sshd_config"
# Clean up after ourselves.
rm "/etc/ssh/sshd_config.bak"

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
  - PCI-DSS-Req-2.3
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.7
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_use_strong_kex
- name: XCCDF Value sshd_strong_kex # promote to variable
  set_fact:
    sshd_strong_kex: !!str curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256
  tags:
    - always

- name: Use Only Strong Key Exchange algorithms
  block:

  - name: Check for duplicate values
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)(?i)^\s*KexAlgorithms\s+
      state: absent
    check_mode: true
    changed_when: false
    register: dupes

  - name: Deduplicate values from /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)(?i)^\s*KexAlgorithms\s+
      state: absent
    when: dupes.found is defined and dupes.found > 1

  - name: Insert correct line to /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)(?i)^\s*KexAlgorithms\s+
      line: KexAlgorithms {{ sshd_strong_kex }}
      state: present
      insertbefore: BOF
      validate: /usr/sbin/sshd -t -f %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - PCI-DSS-Req-2.3
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.7
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_use_strong_kex
```

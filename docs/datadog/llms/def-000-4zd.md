# Source: https://docs.datadoghq.com/security/default_rules/def-000-4zd.md

---
title: Use Only FIPS 140-2 Validated Ciphers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Use Only FIPS 140-2 Validated Ciphers
---

# Use Only FIPS 140-2 Validated Ciphers

## Description{% #description %}

Limit the ciphers to those algorithms which are FIPS-approved. Counter (CTR) mode is also preferred over cipher-block chaining (CBC) mode. The following line in `/etc/ssh/sshd_config` demonstrates use of FIPS-approved ciphers:

```
Ciphers aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc
```

The man page `sshd_config(5)` contains a list of supported ciphers. The rule is parametrized to use the following ciphers: `aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc,rijndael-cbc@lysator.liu.se`.

## Rationale{% #rationale %}

Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and system data may be compromised.

Operating systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules.

FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets industry and government requirements. For government systems, this allows Security Levels 1, 2, 3, or 4 for use on Ubuntu 20.04.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

sshd_approved_ciphers='aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc,rijndael-cbc@lysator.liu.se'


# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^Ciphers")

# shellcheck disable=SC2059
printf -v formatted_output "%s %s" "$stripped_key" "$sshd_approved_ciphers"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^Ciphers\\>" "/etc/ssh/sshd_config"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^Ciphers\\>.*/$escaped_formatted_output/gi" "/etc/ssh/sshd_config"
else
    if [[ -s "/etc/ssh/sshd_config" ]] && [[ -n "$(tail -c 1 -- "/etc/ssh/sshd_config" || true)" ]]; then
        LC_ALL=C sed -i --follow-symlinks '$a'\\ "/etc/ssh/sshd_config"
    fi
    printf '%s\n' "$formatted_output" >> "/etc/ssh/sshd_config"
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
  - CJIS-5.5.6
  - NIST-800-171-3.1.13
  - NIST-800-171-3.13.11
  - NIST-800-171-3.13.8
  - NIST-800-53-AC-17(2)
  - NIST-800-53-AC-17(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(c)
  - NIST-800-53-MA-4(6)
  - NIST-800-53-SC-12(2)
  - NIST-800-53-SC-12(3)
  - NIST-800-53-SC-13
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.7
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_use_approved_ciphers
- name: XCCDF Value sshd_approved_ciphers # promote to variable
  set_fact:
    sshd_approved_ciphers: !!str aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc,rijndael-cbc@lysator.liu.se
  tags:
    - always

- name: Use Only FIPS 140-2 Validated Ciphers
  block:

  - name: Check for duplicate values
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)(?i)^\s*Ciphers\s+
      state: absent
    check_mode: true
    changed_when: false
    register: dupes

  - name: Deduplicate values from /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)(?i)^\s*Ciphers\s+
      state: absent
    when: dupes.found is defined and dupes.found > 1

  - name: Insert correct line to /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)(?i)^\s*Ciphers\s+
      line: Ciphers {{ sshd_approved_ciphers }}
      state: present
      insertbefore: BOF
      validate: /usr/sbin/sshd -t -f %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.5.6
  - NIST-800-171-3.1.13
  - NIST-800-171-3.13.11
  - NIST-800-171-3.13.8
  - NIST-800-53-AC-17(2)
  - NIST-800-53-AC-17(a)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(c)
  - NIST-800-53-MA-4(6)
  - NIST-800-53-SC-12(2)
  - NIST-800-53-SC-12(3)
  - NIST-800-53-SC-13
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.7
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_use_approved_ciphers
```

## Warning{% #warning %}

The system needs to be rebooted for these changes to take effect.

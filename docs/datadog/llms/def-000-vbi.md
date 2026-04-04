# Source: https://docs.datadoghq.com/security/default_rules/def-000-vbi.md

---
title: Use Only Strong MACs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Use Only Strong MACs
---

# Use Only Strong MACs

## Description{% #description %}

Limit the MACs to strong hash algorithms. The following line in `/etc/ssh/sshd_config` demonstrates use of those MACs:

```
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512,hmac-sha2-256

```

## Rationale{% #rationale %}

MD5 and 96-bit MAC algorithms are considered weak and have been shown to increase exploitability in SSH downgrade attacks. Weak algorithms continue to have a great deal of attention as a weak spot that can be exploited with expanded computing power. An attacker that breaks the algorithm could take advantage of a MiTM position to decrypt the SSH tunnel and capture credentials and information

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

sshd_strong_macs='hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512,hmac-sha2-256'


# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^MACs")

# shellcheck disable=SC2059
printf -v formatted_output "%s %s" "$stripped_key" "$sshd_strong_macs"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^MACs\\>" "/etc/ssh/sshd_config"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^MACs\\>.*/$escaped_formatted_output/gi" "/etc/ssh/sshd_config"
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
  - NIST-800-53-AC-17 (2)
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_use_strong_macs
- name: XCCDF Value sshd_strong_macs # promote to variable
  set_fact:
    sshd_strong_macs: !!str hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512,hmac-sha2-256
  tags:
    - always

- name: Use Only Strong MACs
  block:

  - name: Check for duplicate values
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)(?i)^\s*MACs\s+
      state: absent
    check_mode: true
    changed_when: false
    register: dupes

  - name: Deduplicate values from /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)(?i)^\s*MACs\s+
      state: absent
    when: dupes.found is defined and dupes.found > 1

  - name: Insert correct line to /etc/ssh/sshd_config
    lineinfile:
      path: /etc/ssh/sshd_config
      create: true
      regexp: (?i)(?i)^\s*MACs\s+
      line: MACs {{ sshd_strong_macs }}
      state: present
      insertbefore: BOF
      validate: /usr/sbin/sshd -t -f %s
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-AC-17 (2)
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - sshd_use_strong_macs
```

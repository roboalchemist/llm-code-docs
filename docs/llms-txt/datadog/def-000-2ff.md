# Source: https://docs.datadoghq.com/security/default_rules/def-000-2ff.md

---
title: Ensure gpgcheck Enabled In Main yum Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure gpgcheck Enabled In Main yum
  Configuration
---

# Ensure gpgcheck Enabled In Main yum Configuration

## Description{% #description %}

The `gpgcheck` option controls whether RPM packages' signatures are always checked prior to installation. To configure yum to check package signatures before installing them, ensure the following line appears in `/etc/yum.conf` in the `[main]` section:

```
gpgcheck=1
```

## Rationale{% #rationale %}

Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor.

Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization.

Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. Certificates used to verify the software must be from an approved Certificate Authority (CA).

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if rpm --quiet -q yum; then

# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^gpgcheck")

# shellcheck disable=SC2059
printf -v formatted_output "%s = %s" "$stripped_key" "1"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^gpgcheck\\>" "/etc/yum.conf"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^gpgcheck\\>.*/$escaped_formatted_output/gi" "/etc/yum.conf"
else
    if [[ -s "/etc/yum.conf" ]] && [[ -n "$(tail -c 1 -- "/etc/yum.conf" || true)" ]]; then
        LC_ALL=C sed -i --follow-symlinks '$a'\\ "/etc/yum.conf"
    fi
    cce="CCE-26989-4"
    printf '# Per %s: Set %s in %s\n' "${cce}" "${formatted_output}" "/etc/yum.conf" >> "/etc/yum.conf"
    printf '%s\n' "$formatted_output" >> "/etc/yum.conf"
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
  - CCE-26989-4
  - CJIS-5.10.4.1
  - DISA-STIG-RHEL-07-020050
  - NIST-800-171-3.4.8
  - NIST-800-53-CM-11(a)
  - NIST-800-53-CM-11(b)
  - NIST-800-53-CM-5(3)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SA-12
  - NIST-800-53-SA-12(10)
  - NIST-800-53-SC-12
  - NIST-800-53-SC-12(3)
  - NIST-800-53-SI-7
  - PCI-DSS-Req-6.2
  - PCI-DSSv4-6.3.3
  - configure_strategy
  - ensure_gpgcheck_globally_activated
  - high_severity
  - low_complexity
  - medium_disruption
  - no_reboot_needed

- name: Ensure GPG check is globally activated
  ini_file:
    dest: /etc/yum.conf
    section: main
    option: gpgcheck
    value: 1
    no_extra_spaces: true
    create: false
  when: '"yum" in ansible_facts.packages'
  tags:
  - CCE-26989-4
  - CJIS-5.10.4.1
  - DISA-STIG-RHEL-07-020050
  - NIST-800-171-3.4.8
  - NIST-800-53-CM-11(a)
  - NIST-800-53-CM-11(b)
  - NIST-800-53-CM-5(3)
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SA-12
  - NIST-800-53-SA-12(10)
  - NIST-800-53-SC-12
  - NIST-800-53-SC-12(3)
  - NIST-800-53-SI-7
  - PCI-DSS-Req-6.2
  - PCI-DSSv4-6.3.3
  - configure_strategy
  - ensure_gpgcheck_globally_activated
  - high_severity
  - low_complexity
  - medium_disruption
  - no_reboot_needed
```

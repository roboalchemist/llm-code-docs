# Source: https://docs.datadoghq.com/security/default_rules/def-000-qbv.md

---
title: Build and Test AIDE Database
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Build and Test AIDE Database
---

# Build and Test AIDE Database

## Description{% #description %}

Run the following command to generate a new database:

```
$ sudo aideinit
```

By default, the database will be written to the file `/var/lib/aide/aide.db.new`. Storing the database, the configuration file `/etc/aide.conf`, and the binary `/usr/bin/aide.wrapper` (or hashes of these files), in a secure location (such as on read-only media) provides additional assurance about their integrity. The newly-generated database can be installed as follows:

```gdscript3
$ sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db
```

To initiate a manual check, run the following command:

```
$ sudo /usr/bin/aide.wrapper --check
```

If this check produces any unexpected output, investigate.

## Rationale{% #rationale %}

For AIDE to be effective, an initial database of "known-good" information about files must be captured and it should be able to be verified against the installed files.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

DEBIAN_FRONTEND=noninteractive apt-get install -y "aide"

AIDE_CONFIG=/etc/aide/aide.conf
DEFAULT_DB_PATH=/var/lib/aide/aide.db

# Fix db path in the config file, if necessary
if ! grep -q '^database=file:' ${AIDE_CONFIG}; then
    # replace_or_append gets confused by 'database=file' as a key, so should not be used.
    #replace_or_append "${AIDE_CONFIG}" '^database=file' "${DEFAULT_DB_PATH}" '@CCENUM@' '%s:%s'
    echo "database=file:${DEFAULT_DB_PATH}" >> ${AIDE_CONFIG}
fi

# Fix db out path in the config file, if necessary
if ! grep -q '^database_out=file:' ${AIDE_CONFIG}; then
    echo "database_out=file:${DEFAULT_DB_PATH}.new" >> ${AIDE_CONFIG}
fi

/usr/sbin/aideinit -y -f

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
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_build_database
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Build and Test AIDE Database - Ensure AIDE Is Installed
  ansible.builtin.apt:
    name: aide
    state: present
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_build_database
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Build and Test AIDE Database - Check if DB Path in /etc/aide/aide.conf Is
    Already Set
  ansible.builtin.lineinfile:
    path: /etc/aide/aide.conf
    regexp: ^#?(\s*)(database=)(.*)$
    state: absent
  check_mode: true
  changed_when: false
  register: database_replace
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_build_database
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Build and Test AIDE Database - Check if DB Out Path in /etc/aide/aide.conf
    Is Already Set
  ansible.builtin.lineinfile:
    path: /etc/aide/aide.conf
    regexp: ^#?(\s*)(database_out=)(.*)$
    state: absent
  check_mode: true
  changed_when: false
  register: database_out_replace
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_build_database
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Build and Test AIDE Database - Fix DB Path in Config File if Necessary
  ansible.builtin.lineinfile:
    path: /etc/aide/aide.conf
    regexp: ^#?(\s*)(database)(\s*)=(\s*)(.*)$
    line: \2\3=\4file:/var/lib/aide/aide.db
    backrefs: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - database_replace.found > 0
  tags:
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_build_database
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Build and Test AIDE Database - Fix DB Out Path in Config File if Necessary
  ansible.builtin.lineinfile:
    path: /etc/aide/aide.conf
    regexp: ^#?(\s*)(database_out)(\s*)=(\s*)(.*)$
    line: \2\3=\4file:/var/lib/aide/aide.db.new
    backrefs: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - database_out_replace.found > 0
  tags:
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_build_database
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Build and Test AIDE Database - Ensure the Default DB Path is Added
  ansible.builtin.lineinfile:
    path: /etc/aide/aide.conf
    line: database=file:/var/lib/aide/aide.db
    create: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - database_replace.found == 0
  tags:
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_build_database
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Build and Test AIDE Database - Ensure the Default Out Path is Added
  ansible.builtin.lineinfile:
    path: /etc/aide/aide.conf
    line: database_out=file:/var/lib/aide/aide.db.new
    create: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - database_out_replace.found == 0
  tags:
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_build_database
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Build and Test AIDE Database - Build and Test AIDE Database
  ansible.builtin.command: /usr/sbin/aideinit -y -f
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - CJIS-5.10.1.3
  - DISA-STIG-UBTU-20-010450
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_build_database
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```

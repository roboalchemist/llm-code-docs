# Source: https://docs.datadoghq.com/security/default_rules/def-000-r4a.md

---
title: Configure Systemd Timer Execution of AIDE
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Configure Systemd Timer Execution of
  AIDE
---

# Configure Systemd Timer Execution of AIDE

## Description{% #description %}

At a minimum, AIDE should be configured to run a weekly scan. To implement a systemd service and a timer unit to run the service periodically: For example, if a systemd timer is expected to be started every day at 5AM

```
OnCalendar=*-*-* 05:00:0
```

```
[Timer]
```

section in the timer unit and a Unit section starting the AIDE check service unit should be referred.

## Rationale{% #rationale %}

AIDE provides a means to check if unauthorized changes are made to the system. AIDE itself does not setup a periodic execution, so in order to detect unauthorized changes a systemd service to run the check and a systemd timer to take care of periodical execution of that systemd service should be defined.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' && { ( dpkg-query --show --showformat='${db:Status-Status}' 'aide' 2>/dev/null | grep -q '^installed$' && dpkg-query --show --showformat='${db:Status-Status}' 'systemd' 2>/dev/null | grep -q '^installed$' ); }; then

#!/bin/bash

DEBIAN_FRONTEND=noninteractive apt-get install -y "aide"

systemctl unmask dailyaidecheck.service
systemctl unmask dailyaidecheck.timer
systemctl --now enable dailyaidecheck.timer

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
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SI-7
  - NIST-800-53-SI-7(1)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_periodic_checking_systemd_timer
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Configure Systemd Timer Execution of AIDE - Ensure AIDE Service is Enabled
  ansible.builtin.systemd:
    name: dailyaidecheck.service
    enabled: true
    daemon_reload: true
    masked: false
  when:
  - '"linux-base" in ansible_facts.packages'
  - ( "aide" in ansible_facts.packages and "systemd" in ansible_facts.packages )
  tags:
  - CJIS-5.10.1.3
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SI-7
  - NIST-800-53-SI-7(1)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_periodic_checking_systemd_timer
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Configure Systemd Timer Execution of AIDE - Ensure AIDE Service Timer is Enabled
  ansible.builtin.systemd:
    name: dailyaidecheck.timer
    state: started
    enabled: true
    daemon_reload: true
    masked: false
  when:
  - '"linux-base" in ansible_facts.packages'
  - ( "aide" in ansible_facts.packages and "systemd" in ansible_facts.packages )
  tags:
  - CJIS-5.10.1.3
  - NIST-800-53-CM-6(a)
  - NIST-800-53-SI-7
  - NIST-800-53-SI-7(1)
  - PCI-DSS-Req-11.5
  - PCI-DSSv4-11.5.2
  - aide_periodic_checking_systemd_timer
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```

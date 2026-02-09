# Source: https://docs.datadoghq.com/security/default_rules/def-000-vhs.md

---
title: Uninstall setroubleshoot Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall setroubleshoot Package
---

# Uninstall setroubleshoot Package
 
## Description{% #description %}

The SETroubleshoot service notifies desktop users of SELinux denials. The service provides information around configuration errors, unauthorized intrusions, and other potential errors. The `setroubleshoot` package can be removed with the following command:

```

$ sudo yum erase setroubleshoot
```

## Rationale{% #rationale %}

The SETroubleshoot service is an unnecessary daemon to have running on a server, especially if X Windows is removed or disabled.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

# CAUTION: This remediation script will remove setroubleshoot
#	   from the system, and may remove any packages
#	   that depend on setroubleshoot. Execute this
#	   remediation AFTER testing on a non-production
#	   system!

if rpm -q --quiet "setroubleshoot" ; then

    yum remove -y "setroubleshoot"

fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```
- name: Ensure setroubleshoot is removed
  package:
    name: setroubleshoot
    state: absent
  when: ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-80444-3
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_setroubleshoot_removed
```

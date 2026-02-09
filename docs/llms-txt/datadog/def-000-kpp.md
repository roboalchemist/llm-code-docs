# Source: https://docs.datadoghq.com/security/default_rules/def-000-kpp.md

---
title: Uninstall rpcbind Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Uninstall rpcbind Package
---

# Uninstall rpcbind Package
 
## Description{% #description %}

The rpcbind utility maps RPC services to the ports on which they listen. RPC processes notify rpcbind when they start, registering the ports they are listening on and the RPC program numbers they expect to serve. The rpcbind service redirects the client to the proper port number so it can communicate with the requested service. If the system does not require RPC (such as for NFS servers) then this service should be disabled. The `rpcbind` package can be removed with the following command:

```

$ apt-get remove rpcbind
```

## Rationale{% #rationale %}

If the system does not require rpc based services, it is recommended that rpcbind be disabled to reduce the attack surface.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

# CAUTION: This remediation script will remove rpcbind
# from the system, and may remove any packages
# that depend on rpcbind. Execute this
# remediation AFTER testing on a non-production
# system!


DEBIAN_FRONTEND=noninteractive apt-get remove -y "rpcbind"

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
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_rpcbind_removed

- name: 'Uninstall rpcbind Package: Ensure rpcbind is removed'
  ansible.builtin.package:
    name: rpcbind
    state: absent
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - disable_strategy
  - low_complexity
  - low_disruption
  - low_severity
  - no_reboot_needed
  - package_rpcbind_removed
```

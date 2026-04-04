# Source: https://docs.datadoghq.com/security/default_rules/def-000-hdf.md

---
title: Ensure nftables Rules are Permanent
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure nftables Rules are Permanent
---

# Ensure nftables Rules are Permanent

## Description{% #description %}

nftables is a subsystem of the Linux kernel providing filtering and classification of network packets/datagrams/frames. The nftables service reads the /etc/nftables.conf file for a nftables file or files to include in the nftables ruleset. A nftables ruleset containing the input, forward, and output base chains allow network traffic to be filtered.

## Rationale{% #rationale %}

Changes made to nftables ruleset only affect the live system, you will also need to configure the nftables ruleset to apply on boot

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( dpkg-query --show --showformat='${db:Status-Status}' 'nftables' 2>/dev/null | grep -q '^installed$' && ! (systemctl is-active firewalld &>/dev/null) ); then

var_nftables_master_config_file='/etc/nftables.conf'


var_nftables_family='inet'


if [ ! -f "${var_nftables_master_config_file}" ]; then
    touch "${var_nftables_master_config_file}"
fi

nft list ruleset > "/etc/${var_nftables_family}-filter.rules"

grep -qxF 'include "/etc/'"${var_nftables_family}"'-filter.rules"' "${var_nftables_master_config_file}" \
    || echo 'include "/etc/'"${var_nftables_family}"'-filter.rules"' >> "${var_nftables_master_config_file}"

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

# Source: https://docs.datadoghq.com/security/default_rules/def-000-nfl.md

---
title: Require use_authtok for pam_unix.so
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Require use_authtok for pam_unix.so
---

# Require use_authtok for pam_unix.so

## Description{% #description %}

When password changing enforce the module to set the new password to the one provided by a previously stacked password module

## Rationale{% #rationale %}

Require use_authtok in pam_unix.so configuration

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

config_file="/usr/share/pam-configs/cac_unix"
conf_name=cac_unix
conf_path="/usr/share/pam-configs"

if [ ! -f "$conf_path"/"$conf_name" ]; then
    if [ -f "$conf_path"/unix ]; then
        if grep -q "$(md5sum "$conf_path"/unix | cut -d ' ' -f 1)" /var/lib/dpkg/info/libpam-runtime.md5sums;then
            cp "$conf_path"/unix "$conf_path"/"$conf_name"
            sed -i 's/Priority: [0-9]\+/Priority: 257\
Conflicts: unix/' "$conf_path"/"$conf_name"
            DEBIAN_FRONTEND=noninteractive pam-auth-update
        else
            echo "Not applicable - checksum of $conf_path/unix does not match the original." >&2
        fi
    else
        echo "Not applicable - $conf_path/unix does not exist" >&2
    fi
fi
sed -i -E '/^Password:/,/^[^[:space:]]/ {
    /pam_unix\.so/ {
        /use_authtok/! s/$/ use_authtok/g
    }
}'  "$config_file"


DEBIAN_FRONTEND=noninteractive pam-auth-update --remove unix --enable cac_unix

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

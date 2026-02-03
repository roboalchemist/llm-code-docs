# Source: https://docs.datadoghq.com/security/default_rules/def-000-5ez.md

---
title: Verify pam_unix module is activated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify pam_unix module is activated
---

# Verify pam_unix module is activated
 
## Description{% #description %}

`pam_unix` is the standard Unix authentication module. It uses standard calls from the system's libraries to retrieve and set account information as well as authentication. Usually this is obtained from the `/etc/passwd` and if shadow is enabled, the `/etc/shadow` file as well.

The account component performs the task of establishing the status of the user's account and password based on the following shadow elements: `expire, last_change, max_change, min_change, warn_change`. In the case of the latter, it may offer advice to the user on changing their password or, through the `PAM_AUTHTOKEN_REQD` return, delay giving service to the user until they have established a new password. The entries listed above are documented in the shadow(5) manual page. Should the user's record not contain one or more of these entries, the corresponding shadow check is not performed.

The authentication component performs the task of checking the users credentials (password). The default action of this module is to not permit the user access to a service if their official password is blank.

## Rationale{% #rationale %}

The system should only provide access after performing authentication of a user.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

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

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

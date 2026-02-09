# Source: https://docs.datadoghq.com/security/default_rules/def-000-xwu.md

---
title: >-
  Ensure PAM Enforces Password Requirements - Authentication Retry Prompts
  Permitted Per-Session
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure PAM Enforces Password
  Requirements - Authentication Retry Prompts Permitted Per-Session
---

# Ensure PAM Enforces Password Requirements - Authentication Retry Prompts Permitted Per-Session
 
## Description{% #description %}

To configure the number of retry prompts that are permitted per-session: Edit the `pam_pwquality.so` statement in `/etc/pam.d/common-password` to show `retry=3`, or a lower value if site policy is more restrictive. The DoD requirement is a maximum of 3 prompts per session.

## Rationale{% #rationale %}

Setting the password retry prompts that are permitted on a per-session basis to a low value requires some software, such as SSH, to re-connect. This can slow down and draw additional attention to some types of password-guessing attacks. Note that this is different from account lockout, which is provided by the pam_faillock module.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpwquality1' 2>/dev/null | grep -q '^installed$'; then

var_password_pam_retry='3'


conf_name=cac_pwquality
if [ ! -f /usr/share/pam-configs/"$conf_name" ]; then
    cat << EOF > /usr/share/pam-configs/"$conf_name"
Name: Pwquality password strength checking
Default: yes
Priority: 1025
Conflicts: cracklib, pwquality
Password-Type: Primary
Password:
    requisite                   pam_pwquality.so
EOF
fi

DEBIAN_FRONTEND=noninteractive pam-auth-update

PWQUALITY_CONF="/etc/security/pwquality.conf"
    regex="^\s*retry\s*="
    line="retry = $var_password_pam_retry"
    if ! grep -q $regex $PWQUALITY_CONF; then
        echo $line >> $PWQUALITY_CONF
    else
        sed -i --follow-symlinks 's|^\s*\(retry\s*=\s*\)\(\S\+\)|\1'"$var_password_pam_retry"'|g' $PWQUALITY_CONF
    fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

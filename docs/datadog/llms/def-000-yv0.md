# Source: https://docs.datadoghq.com/security/default_rules/def-000-yv0.md

---
title: Set Lockout Time for Failed Password Attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Set Lockout Time for Failed Password
  Attempts
---

# Set Lockout Time for Failed Password Attempts

## Description{% #description %}

This rule configures the system to lock out accounts during a specified time period after a number of incorrect login attempts using `pam_faillock.so`. Ensure that the file `/etc/security/faillock.conf` contains the following entry: `unlock_time=<interval-in-seconds>` where `interval-in-seconds` is `0` or greater. pam_faillock.so module requires multiple entries in pam files. These entries must be carefully defined to work as expected. In order to avoid any errors when manually editing these files, it is recommended to use the appropriate tools, such as `authselect` or `authconfig`, depending on the OS version. If `unlock_time` is set to `0`, manual intervention by an administrator is required to unlock a user. This should be done using the `faillock` tool.

## Rationale{% #rationale %}

By limiting the number of failed logon attempts the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

var_accounts_passwords_pam_faillock_unlock_time='0'


if [ -f /usr/bin/authselect ]; then
    if ! authselect check; then
echo "
authselect integrity check failed. Remediation aborted!
This remediation could not be applied because an authselect profile was not selected or the selected profile is not intact.
It is not recommended to manually edit the PAM files when authselect tool is available.
In cases where the default authselect profile does not cover a specific demand, a custom authselect profile is recommended."
exit 1
fi
authselect enable-feature with-faillock

authselect apply-changes -b
else

conf_name=cac_faillock

if [ ! -f /usr/share/pam-configs/"$conf_name" ]; then
    cat << EOF > /usr/share/pam-configs/"$conf_name"
Name: Enable pam_faillock to deny access
Default: yes
Conflicts: faillock
Priority: 0
Auth-Type: Primary
Auth:
    [default=die]                   pam_faillock.so authfail
EOF
fi

if [ ! -f /usr/share/pam-configs/"$conf_name"_notify ]; then
    cat << EOF > /usr/share/pam-configs/"$conf_name"_notify
Name: Notify of failed login attempts and reset count upon success
Default: yes
Conflicts: faillock_notify
Priority: 1025
Auth-Type: Primary
Auth:
    requisite                       pam_faillock.so preauth
Account-Type: Primary
Account:
    required                        pam_faillock.so
EOF
fi

DEBIAN_FRONTEND=noninteractive pam-auth-update


fi

AUTH_FILES=("/etc/pam.d/common-auth")
SKIP_FAILLOCK_CHECK=true

FAILLOCK_CONF="/etc/security/faillock.conf"
if [ -f $FAILLOCK_CONF ] || [ "$SKIP_FAILLOCK_CHECK" = "true" ]; then
    regex="^\s*unlock_time\s*="
    line="unlock_time = $var_accounts_passwords_pam_faillock_unlock_time"
    if ! grep -q $regex $FAILLOCK_CONF; then
        echo $line >> $FAILLOCK_CONF
    else
        sed -i --follow-symlinks 's|^\s*\(unlock_time\s*=\s*\)\(\S\+\)|\1'"$var_accounts_passwords_pam_faillock_unlock_time"'|g' $FAILLOCK_CONF
    fi

else
    for pam_file in "${AUTH_FILES[@]}"
    do
        if ! grep -qE '^\s*auth.*pam_faillock\.so (preauth|authfail).*unlock_time' "$pam_file"; then
            sed -i --follow-symlinks '/^auth.*required.*pam_faillock\.so.*preauth.*silent.*/ s/$/ unlock_time='"$var_accounts_passwords_pam_faillock_unlock_time"'/' "$pam_file"
            sed -i --follow-symlinks '/^auth.*required.*pam_faillock\.so.*authfail.*/ s/$/ unlock_time='"$var_accounts_passwords_pam_faillock_unlock_time"'/' "$pam_file"
        else
            sed -i --follow-symlinks 's/\(^auth.*required.*pam_faillock\.so.*preauth.*silent.*\)\('"unlock_time"'=\)[0-9]\+\(.*\)/\1\2'"$var_accounts_passwords_pam_faillock_unlock_time"'\3/' "$pam_file"
            sed -i --follow-symlinks 's/\(^auth.*required.*pam_faillock\.so.*authfail.*\)\('"unlock_time"'=\)[0-9]\+\(.*\)/\1\2'"$var_accounts_passwords_pam_faillock_unlock_time"'\3/' "$pam_file"
        fi
    done
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

## Warning{% #warning %}

If the system supports the new `/etc/security/faillock.conf` file but the pam_faillock.so parameters are defined directly in `/etc/pam.d/system-auth` and `/etc/pam.d/password-auth`, the remediation will migrate the `unlock_time` parameter to `/etc/security/faillock.conf` to ensure compatibility with `authselect` tool. The parameters `deny` and `fail_interval`, if used, also have to be migrated by their respective remediation.

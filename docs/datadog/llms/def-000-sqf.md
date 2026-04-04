# Source: https://docs.datadoghq.com/security/default_rules/def-000-sqf.md

---
title: Lock Accounts After Failed Password Attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Lock Accounts After Failed Password
  Attempts
---

# Lock Accounts After Failed Password Attempts

## Description{% #description %}

This rule configures the system to lock out accounts after a number of incorrect login attempts using `pam_faillock.so`. pam_faillock.so module requires multiple entries in pam files. These entries must be carefully defined to work as expected. Ensure that the file `/etc/security/faillock.conf` contains the following entry: `deny = <count>` Where count should be less than or equal to 3 and greater than 0.

## Rationale{% #rationale %}

By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, also known as brute-forcing, is reduced. Limits are imposed by locking the account.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

var_accounts_passwords_pam_faillock_deny='3'


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
    regex="^\s*deny\s*="
    line="deny = $var_accounts_passwords_pam_faillock_deny"
    if ! grep -q $regex $FAILLOCK_CONF; then
        echo $line >> $FAILLOCK_CONF
    else
        sed -i --follow-symlinks 's|^\s*\(deny\s*=\s*\)\(\S\+\)|\1'"$var_accounts_passwords_pam_faillock_deny"'|g' $FAILLOCK_CONF
    fi

else
    for pam_file in "${AUTH_FILES[@]}"
    do
        if ! grep -qE '^\s*auth.*pam_faillock\.so (preauth|authfail).*deny' "$pam_file"; then
            sed -i --follow-symlinks '/^auth.*required.*pam_faillock\.so.*preauth.*silent.*/ s/$/ deny='"$var_accounts_passwords_pam_faillock_deny"'/' "$pam_file"
            sed -i --follow-symlinks '/^auth.*required.*pam_faillock\.so.*authfail.*/ s/$/ deny='"$var_accounts_passwords_pam_faillock_deny"'/' "$pam_file"
        else
            sed -i --follow-symlinks 's/\(^auth.*required.*pam_faillock\.so.*preauth.*silent.*\)\('"deny"'=\)[0-9]\+\(.*\)/\1\2'"$var_accounts_passwords_pam_faillock_deny"'\3/' "$pam_file"
            sed -i --follow-symlinks 's/\(^auth.*required.*pam_faillock\.so.*authfail.*\)\('"deny"'=\)[0-9]\+\(.*\)/\1\2'"$var_accounts_passwords_pam_faillock_deny"'\3/' "$pam_file"
        fi
    done
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

## Warning{% #warning %}

If the system relies on `authselect` tool to manage PAM settings, the remediation will also use `authselect` tool. However, if any manual modification was made in PAM files, the `authselect` integrity check will fail and the remediation will be aborted in order to preserve intentional changes. In this case, an informative message will be shown in the remediation report. If the system supports the `/etc/security/faillock.conf` file, the pam_faillock parameters should be defined in `faillock.conf` file.

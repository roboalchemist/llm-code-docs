# Source: https://docs.datadoghq.com/security/default_rules/def-000-is0.md

---
title: 'Limit Password Reuse: system-auth'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: 'Docs > Datadog Security > OOTB Rules > Limit Password Reuse: system-auth'
---

# Limit Password Reuse: system-auth

## Description{% #description %}

Do not allow users to reuse recent passwords. This can be accomplished by using the `remember` option for the `pam_pwhistory` PAM module.

In the file `/etc/pam.d/system-auth`, make sure the parameter `remember` is present and it has a value equal to or greater than 24

For example:

```
password requisite,required pam_pwhistory.so use_authtok remember=24

```

## Rationale{% #rationale %}

Preventing re-use of previous passwords helps ensure that a compromised password is not re-used by a user.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if rpm --quiet -q pam; then

var_password_pam_remember='24'
var_password_pam_remember_control_flag='requisite,required'


var_password_pam_remember_control_flag="$(echo $var_password_pam_remember_control_flag | cut -d \, -f 1)"

if [ -f /usr/bin/authselect ]; then
    if authselect list-features minimal | grep -q with-pwhistory; then
        if ! authselect check; then
        echo "
        authselect integrity check failed. Remediation aborted!
        This remediation could not be applied because an authselect profile was not selected or the selected profile is not intact.
        It is not recommended to manually edit the PAM files when authselect tool is available.
        In cases where the default authselect profile does not cover a specific demand, a custom authselect profile is recommended."
        exit 1
        fi
        authselect enable-feature with-pwhistory

        authselect apply-changes -b
    else

        if ! authselect check; then
        echo "
        authselect integrity check failed. Remediation aborted!
        This remediation could not be applied because an authselect profile was not selected or the selected profile is not intact.
        It is not recommended to manually edit the PAM files when authselect tool is available.
        In cases where the default authselect profile does not cover a specific demand, a custom authselect profile is recommended."
        exit 1
        fi

        CURRENT_PROFILE=$(authselect current -r | awk '{ print $1 }')
        # If not already in use, a custom profile is created preserving the enabled features.
        if [[ ! $CURRENT_PROFILE == custom/* ]]; then
            ENABLED_FEATURES=$(authselect current | tail -n+3 | awk '{ print $2 }')
            authselect create-profile hardening -b $CURRENT_PROFILE
            CURRENT_PROFILE="custom/hardening"

            authselect apply-changes -b --backup=before-hardening-custom-profile
            authselect select $CURRENT_PROFILE
            for feature in $ENABLED_FEATURES; do
                authselect enable-feature $feature;
            done

            authselect apply-changes -b --backup=after-hardening-custom-profile
        fi
        PAM_FILE_NAME=$(basename "/etc/pam.d/system-auth")
        PAM_FILE_PATH="/etc/authselect/$CURRENT_PROFILE/$PAM_FILE_NAME"

        authselect apply-changes -b
        if ! grep -qP '^\s*password\s+'"$var_password_pam_remember_control_flag"'\s+pam_pwhistory.so\s*.*' "$PAM_FILE_PATH"; then
            # Line matching group + control + module was not found. Check group + module.
            if [ "$(grep -cP '^\s*password\s+.*\s+pam_pwhistory.so\s*' "$PAM_FILE_PATH")" -eq 1 ]; then
                # The control is updated only if one single line matches.
                sed -i -E --follow-symlinks 's/^(\s*password\s+).*(\bpam_pwhistory.so.*)/\1'"$var_password_pam_remember_control_flag"' \2/' "$PAM_FILE_PATH"
            else
                LAST_MATCH_LINE=$(grep -nP "^password.*requisite.*pam_pwquality\.so" "$PAM_FILE_PATH" | tail -n 1 | cut -d: -f 1)
                if [ ! -z $LAST_MATCH_LINE ]; then
                    sed -i --follow-symlinks $LAST_MATCH_LINE' a password     '"$var_password_pam_remember_control_flag"'    pam_pwhistory.so' "$PAM_FILE_PATH"
                else
                    echo 'password    '"$var_password_pam_remember_control_flag"'    pam_pwhistory.so' >> "$PAM_FILE_PATH"
                fi
            fi
        fi
    fi
else
    if ! grep -qP '^\s*password\s+'"$var_password_pam_remember_control_flag"'\s+pam_pwhistory.so\s*.*' "/etc/pam.d/system-auth"; then
        # Line matching group + control + module was not found. Check group + module.
        if [ "$(grep -cP '^\s*password\s+.*\s+pam_pwhistory.so\s*' "/etc/pam.d/system-auth")" -eq 1 ]; then
            # The control is updated only if one single line matches.
            sed -i -E --follow-symlinks 's/^(\s*password\s+).*(\bpam_pwhistory.so.*)/\1'"$var_password_pam_remember_control_flag"' \2/' "/etc/pam.d/system-auth"
        else
            LAST_MATCH_LINE=$(grep -nP "^password.*requisite.*pam_pwquality\.so" "/etc/pam.d/system-auth" | tail -n 1 | cut -d: -f 1)
            if [ ! -z $LAST_MATCH_LINE ]; then
                sed -i --follow-symlinks $LAST_MATCH_LINE' a password     '"$var_password_pam_remember_control_flag"'    pam_pwhistory.so' "/etc/pam.d/system-auth"
            else
                echo 'password    '"$var_password_pam_remember_control_flag"'    pam_pwhistory.so' >> "/etc/pam.d/system-auth"
            fi
        fi
    fi
fi

PWHISTORY_CONF="/etc/security/pwhistory.conf"
if [ -f $PWHISTORY_CONF ]; then
    regex="^\s*remember\s*="
    line="remember = $var_password_pam_remember"
    if ! grep -q $regex $PWHISTORY_CONF; then
        echo $line >> $PWHISTORY_CONF
    else
        sed -i --follow-symlinks 's|^\s*\(remember\s*=\s*\)\(\S\+\)|\1'"$var_password_pam_remember"'|g' $PWHISTORY_CONF
    fi
    if [ -e "/etc/pam.d/system-auth" ] ; then
        PAM_FILE_PATH="/etc/pam.d/system-auth"
        if [ -f /usr/bin/authselect ]; then

            if ! authselect check; then
            echo "
            authselect integrity check failed. Remediation aborted!
            This remediation could not be applied because an authselect profile was not selected or the selected profile is not intact.
            It is not recommended to manually edit the PAM files when authselect tool is available.
            In cases where the default authselect profile does not cover a specific demand, a custom authselect profile is recommended."
            exit 1
            fi

            CURRENT_PROFILE=$(authselect current -r | awk '{ print $1 }')
            # If not already in use, a custom profile is created preserving the enabled features.
            if [[ ! $CURRENT_PROFILE == custom/* ]]; then
                ENABLED_FEATURES=$(authselect current | tail -n+3 | awk '{ print $2 }')
                authselect create-profile hardening -b $CURRENT_PROFILE
                CURRENT_PROFILE="custom/hardening"

                authselect apply-changes -b --backup=before-hardening-custom-profile
                authselect select $CURRENT_PROFILE
                for feature in $ENABLED_FEATURES; do
                    authselect enable-feature $feature;
                done

                authselect apply-changes -b --backup=after-hardening-custom-profile
            fi
            PAM_FILE_NAME=$(basename "/etc/pam.d/system-auth")
            PAM_FILE_PATH="/etc/authselect/$CURRENT_PROFILE/$PAM_FILE_NAME"

            authselect apply-changes -b
        fi

    if grep -qP '^\s*password\s.*\bpam_pwhistory.so\s.*\bremember\b' "$PAM_FILE_PATH"; then
        sed -i -E --follow-symlinks 's/(.*password.*pam_pwhistory.so.*)\bremember\b=?[[:alnum:]]*(.*)/\1\2/g' "$PAM_FILE_PATH"
    fi
        if [ -f /usr/bin/authselect ]; then

            authselect apply-changes -b
        fi
    else
        echo "/etc/pam.d/system-auth was not found" >&2
    fi
else
    PAM_FILE_PATH="/etc/pam.d/system-auth"
    if [ -f /usr/bin/authselect ]; then

        if ! authselect check; then
        echo "
        authselect integrity check failed. Remediation aborted!
        This remediation could not be applied because an authselect profile was not selected or the selected profile is not intact.
        It is not recommended to manually edit the PAM files when authselect tool is available.
        In cases where the default authselect profile does not cover a specific demand, a custom authselect profile is recommended."
        exit 1
        fi

        CURRENT_PROFILE=$(authselect current -r | awk '{ print $1 }')
        # If not already in use, a custom profile is created preserving the enabled features.
        if [[ ! $CURRENT_PROFILE == custom/* ]]; then
            ENABLED_FEATURES=$(authselect current | tail -n+3 | awk '{ print $2 }')
            authselect create-profile hardening -b $CURRENT_PROFILE
            CURRENT_PROFILE="custom/hardening"

            authselect apply-changes -b --backup=before-hardening-custom-profile
            authselect select $CURRENT_PROFILE
            for feature in $ENABLED_FEATURES; do
                authselect enable-feature $feature;
            done

            authselect apply-changes -b --backup=after-hardening-custom-profile
        fi
        PAM_FILE_NAME=$(basename "/etc/pam.d/system-auth")
        PAM_FILE_PATH="/etc/authselect/$CURRENT_PROFILE/$PAM_FILE_NAME"

        authselect apply-changes -b
    fi
    if ! grep -qP '^\s*password\s+'"requisite"'\s+pam_pwhistory.so\s*.*' "$PAM_FILE_PATH"; then
        # Line matching group + control + module was not found. Check group + module.
        if [ "$(grep -cP '^\s*password\s+.*\s+pam_pwhistory.so\s*' "$PAM_FILE_PATH")" -eq 1 ]; then
            # The control is updated only if one single line matches.
            sed -i -E --follow-symlinks 's/^(\s*password\s+).*(\bpam_pwhistory.so.*)/\1'"requisite"' \2/' "$PAM_FILE_PATH"
        else
            echo 'password    '"requisite"'    pam_pwhistory.so' >> "$PAM_FILE_PATH"
        fi
    fi
    # Check the option
    if ! grep -qP '^\s*password\s+'"requisite"'\s+pam_pwhistory.so\s*.*\sremember\b' "$PAM_FILE_PATH"; then
        sed -i -E --follow-symlinks '/\s*password\s+'"requisite"'\s+pam_pwhistory.so.*/ s/$/ remember='"$var_password_pam_remember"'/' "$PAM_FILE_PATH"
    else
        sed -i -E --follow-symlinks 's/(\s*password\s+'"requisite"'\s+pam_pwhistory.so\s+.*)('"remember"'=)[[:alnum:]]+\s*(.*)/\1\2'"$var_password_pam_remember"' \3/' "$PAM_FILE_PATH"
    fi
    if [ -f /usr/bin/authselect ]; then

        authselect apply-changes -b
    fi
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

## Warning{% #warning %}

If the system relies on `authselect` tool to manage PAM settings, the remediation will also use `authselect` tool. However, if any manual modification was made in PAM files, the `authselect` integrity check will fail and the remediation will be aborted in order to preserve intentional changes. In this case, an informative message will be shown in the remediation report.

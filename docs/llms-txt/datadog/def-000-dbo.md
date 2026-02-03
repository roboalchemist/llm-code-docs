# Source: https://docs.datadoghq.com/security/default_rules/def-000-dbo.md

---
title: Enable GNOME3 Login Warning Banner
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Enable GNOME3 Login Warning Banner
---

# Enable GNOME3 Login Warning Banner
 
## Description{% #description %}

In the default graphical environment, displaying a login warning banner in the GNOME Display Manager's login screen can be enabled on the login screen by setting `banner-message-enable` to `true`.

To enable, add or edit `banner-message-enable` to `/etc/dconf/db/gdm.d/00-security-settings`. For example:

```
[org/gnome/login-screen]
banner-message-enable=true
```

Once the setting has been added, add a lock to `/etc/dconf/db/gdm.d/locks/00-security-settings-lock` to prevent user modification. For example:

```
/org/gnome/login-screen/banner-message-enable
```

After the settings have been set, run `dconf update`. The banner text must also be set.

## Rationale{% #rationale %}

Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.

For U.S. Government systems, system use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'gdm3' 2>/dev/null | grep -q '^installed$'; then

mkdir -p /etc/dconf/profile
dconf_profile_path=/etc/dconf/profile/user

[[ -s "${dconf_profile_path}" ]] || echo > "${dconf_profile_path}"

if ! grep -Pzq "(?s)^\s*user-db:user.*\n\s*system-db:local" "${dconf_profile_path}"; then
    sed -i --follow-symlinks "1s/^/user-db:user\nsystem-db:local\n/" "${dconf_profile_path}"
fi

# Make sure the corresponding directories exist
mkdir -p /etc/dconf/db/local.d

# Make sure permissions allow regular users to read dconf settings.
# Also define the umask to avoid `dconf update` changing permissions.
chmod -R u=rwX,go=rX /etc/dconf/profile
(umask 0022 && dconf update)
mkdir -p /etc/dconf/profile
dconf_profile_path=/etc/dconf/profile/gdm

[[ -s "${dconf_profile_path}" ]] || echo > "${dconf_profile_path}"

if ! grep -Pzq "(?s)^\s*user-db:user.*\n\s*system-db:gdm" "${dconf_profile_path}"; then
    sed -i --follow-symlinks "1s/^/user-db:user\nsystem-db:gdm\n/" "${dconf_profile_path}"
fi

# Make sure the corresponding directories exist
mkdir -p /etc/dconf/db/gdm.d

# Make sure permissions allow regular users to read dconf settings.
# Also define the umask to avoid `dconf update` changing permissions.
chmod -R u=rwX,go=rX /etc/dconf/profile
(umask 0022 && dconf update)
# Duplicate the setting also in 'greeter.dconf-defaults' for consistency with
# 'dconf_gnome_login_banner_text' and better alignment with STIG V1R1.
if [ -e "/etc/gdm3/greeter.dconf-defaults" ] ; then
    
    LC_ALL=C sed -i "/^\s*banner\-message\-enable/Id" "/etc/gdm3/greeter.dconf-defaults"
else
    touch "/etc/gdm3/greeter.dconf-defaults"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/gdm3/greeter.dconf-defaults"

cp "/etc/gdm3/greeter.dconf-defaults" "/etc/gdm3/greeter.dconf-defaults.bak"
# Insert after the line matching the regex '\[org/gnome/login-screen\]'
line_number="$(LC_ALL=C grep -n "\[org/gnome/login-screen\]" "/etc/gdm3/greeter.dconf-defaults.bak" | LC_ALL=C sed 's/:.*//g')"
if [ -z "$line_number" ]; then
    # There was no match of '\[org/gnome/login-screen\]', insert at
    # the end of the file.
    printf '%s\n' "banner-message-enable=true" >> "/etc/gdm3/greeter.dconf-defaults"
else
    head -n "$(( line_number ))" "/etc/gdm3/greeter.dconf-defaults.bak" > "/etc/gdm3/greeter.dconf-defaults"
    printf '%s\n' "banner-message-enable=true" >> "/etc/gdm3/greeter.dconf-defaults"
    tail -n "+$(( line_number + 1 ))" "/etc/gdm3/greeter.dconf-defaults.bak" >> "/etc/gdm3/greeter.dconf-defaults"
fi
# Clean up after ourselves.
rm "/etc/gdm3/greeter.dconf-defaults.bak"


# Check for setting in any of the DConf db directories
# If files contain ibus or distro, ignore them.
# The assignment assumes that individual filenames don't contain :
readarray -t SETTINGSFILES < <(grep -r "\\[org/gnome/login-screen\\]" "/etc/dconf/db/" \
                                | grep -v 'distro\|ibus\|gdm.d' | cut -d":" -f1)
DCONFFILE="/etc/dconf/db/gdm.d/00-security-settings"
DBDIR="/etc/dconf/db/gdm.d"

mkdir -p "${DBDIR}"

# Comment out the configurations in databases different from the target one
if [ "${#SETTINGSFILES[@]}" -ne 0 ]
then
    if grep -q "^\\s*banner-message-enable\\s*=" "${SETTINGSFILES[@]}"
    then
        
        sed -Ei "s/(^\s*)banner-message-enable(\s*=)/#\1banner-message-enable\2/g" "${SETTINGSFILES[@]}"
    fi
fi

[ ! -z "${DCONFFILE}" ] && echo "" >> "${DCONFFILE}"
if ! grep -q "\\[org/gnome/login-screen\\]" "${DCONFFILE}"
then
    printf '%s\n' "[org/gnome/login-screen]" >> ${DCONFFILE}
fi

escaped_value="$(sed -e 's/\\/\\\\/g' <<< "true")"
if grep -q "^\\s*banner-message-enable\\s*=" "${DCONFFILE}"
then
        sed -i "s/\\s*banner-message-enable\\s*=\\s*.*/banner-message-enable=${escaped_value}/g" "${DCONFFILE}"
    else
        sed -i "\\|\\[org/gnome/login-screen\\]|a\\banner-message-enable=${escaped_value}" "${DCONFFILE}"
fi
# Make sure permissions allow regular users to read dconf settings.
# Also define the umask to avoid `dconf update` changing permissions.
chmod -R u=rwX,go=rX /etc/dconf/db
(umask 0022 && dconf update)
# Check for setting in any of the DConf db directories
LOCKFILES=$(grep -r "^/org/gnome/login-screen/banner-message-enable$" "/etc/dconf/db/" \
            | grep -v 'distro\|ibus\|gdm.d' | grep ":" | cut -d":" -f1)
LOCKSFOLDER="/etc/dconf/db/gdm.d/locks"

mkdir -p "${LOCKSFOLDER}"

# Comment out the configurations in databases different from the target one
if [[ ! -z "${LOCKFILES}" ]]
then
    sed -i -E "s|^/org/gnome/login-screen/banner-message-enable$|#&|" "${LOCKFILES[@]}"
fi

if ! grep -qr "^/org/gnome/login-screen/banner-message-enable$" /etc/dconf/db/gdm.d/
then
    echo "/org/gnome/login-screen/banner-message-enable" >> "/etc/dconf/db/gdm.d/locks/00-security-settings-lock"
fi
# Make sure permissions allow regular users to read dconf settings.
# Also define the umask to avoid `dconf update` changing permissions.
chmod -R u=rwX,go=rX /etc/dconf/db
(umask 0022 && dconf update)

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

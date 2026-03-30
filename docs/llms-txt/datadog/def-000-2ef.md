# Source: https://docs.datadoghq.com/security/default_rules/def-000-2ef.md

---
title: Disable the GNOME3 Login User List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable the GNOME3 Login User List
---

# Disable the GNOME3 Login User List

## Description{% #description %}

In the default graphical environment, users logging directly into the system are greeted with a login screen that displays all known users. This functionality should be disabled by setting `disable-user-list` to `true`.

To disable, add or edit `disable-user-list` to `/etc/dconf/db/gdm.d/00-security-settings`. For example:

```
[org/gnome/login-screen]
disable-user-list=true
```

Once the setting has been added, add a lock to `/etc/dconf/db/gdm.d/locks/00-security-settings-lock` to prevent user modification. For example:

```
/org/gnome/login-screen/disable-user-list
```

After the settings have been set, run `dconf update`.

## Rationale{% #rationale %}

Leaving the user list enabled is a security risk since it allows anyone with physical access to the system to quickly enumerate known user accounts without logging in.

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
    if grep -q "^\\s*disable-user-list\\s*=" "${SETTINGSFILES[@]}"
    then

        sed -Ei "s/(^\s*)disable-user-list(\s*=)/#\1disable-user-list\2/g" "${SETTINGSFILES[@]}"
    fi
fi

[ ! -z "${DCONFFILE}" ] && echo "" >> "${DCONFFILE}"
if ! grep -q "\\[org/gnome/login-screen\\]" "${DCONFFILE}"
then
    printf '%s\n' "[org/gnome/login-screen]" >> ${DCONFFILE}
fi

escaped_value="$(sed -e 's/\\/\\\\/g' <<< "true")"
if grep -q "^\\s*disable-user-list\\s*=" "${DCONFFILE}"
then
        sed -i "s/\\s*disable-user-list\\s*=\\s*.*/disable-user-list=${escaped_value}/g" "${DCONFFILE}"
    else
        sed -i "\\|\\[org/gnome/login-screen\\]|a\\disable-user-list=${escaped_value}" "${DCONFFILE}"
fi
# Make sure permissions allow regular users to read dconf settings.
# Also define the umask to avoid `dconf update` changing permissions.
chmod -R u=rwX,go=rX /etc/dconf/db
(umask 0022 && dconf update)
# Check for setting in any of the DConf db directories
LOCKFILES=$(grep -r "^/org/gnome/login-screen/disable-user-list$" "/etc/dconf/db/" \
            | grep -v 'distro\|ibus\|gdm.d' | grep ":" | cut -d":" -f1)
LOCKSFOLDER="/etc/dconf/db/gdm.d/locks"

mkdir -p "${LOCKSFOLDER}"

# Comment out the configurations in databases different from the target one
if [[ ! -z "${LOCKFILES}" ]]
then
    sed -i -E "s|^/org/gnome/login-screen/disable-user-list$|#&|" "${LOCKFILES[@]}"
fi

if ! grep -qr "^/org/gnome/login-screen/disable-user-list$" /etc/dconf/db/gdm.d/
then
    echo "/org/gnome/login-screen/disable-user-list" >> "/etc/dconf/db/gdm.d/locks/00-security-settings-lock"
fi
# Make sure permissions allow regular users to read dconf settings.
# Also define the umask to avoid `dconf update` changing permissions.
chmod -R u=rwX,go=rX /etc/dconf/db
(umask 0022 && dconf update)

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

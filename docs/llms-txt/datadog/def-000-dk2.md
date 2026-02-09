# Source: https://docs.datadoghq.com/security/default_rules/def-000-dk2.md

---
title: Disable GNOME3 Automount Opening
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable GNOME3 Automount Opening
---

# Disable GNOME3 Automount Opening
 
## Description{% #description %}

The system's default desktop environment, GNOME3, will mount devices and removable media (such as DVDs, CDs and USB flash drives) whenever they are inserted into the system. To disable automount-open within GNOME3, add or set `automount-open` to `false` in `/etc/dconf/db/local.d/00-security-settings`. For example:

```
[org/gnome/desktop/media-handling]
automount-open=false
```

Once the settings have been added, add a lock to `/etc/dconf/db/local.d/locks/00-security-settings-lock` to prevent user modification. For example:

```
/org/gnome/desktop/media-handling/automount-open
```

After the settings have been set, run `dconf update`.

## Rationale{% #rationale %}

Automatically mounting file systems permits easy introduction of unknown devices, thereby facilitating malicious activity. Disabling automatic mounting in GNOME3 can prevent the introduction of malware via removable media. It will, however, also prevent desktop users from legitimate use of removable media.

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
readarray -t SETTINGSFILES < <(grep -r "\\[org/gnome/desktop/media-handling\\]" "/etc/dconf/db/" \
                                | grep -v 'distro\|ibus\|local.d' | cut -d":" -f1)
DCONFFILE="/etc/dconf/db/local.d/00-security-settings"
DBDIR="/etc/dconf/db/local.d"

mkdir -p "${DBDIR}"

# Comment out the configurations in databases different from the target one
if [ "${#SETTINGSFILES[@]}" -ne 0 ]
then
    if grep -q "^\\s*automount-open\\s*=" "${SETTINGSFILES[@]}"
    then
        
        sed -Ei "s/(^\s*)automount-open(\s*=)/#\1automount-open\2/g" "${SETTINGSFILES[@]}"
    fi
fi

[ ! -z "${DCONFFILE}" ] && echo "" >> "${DCONFFILE}"
if ! grep -q "\\[org/gnome/desktop/media-handling\\]" "${DCONFFILE}"
then
    printf '%s\n' "[org/gnome/desktop/media-handling]" >> ${DCONFFILE}
fi

escaped_value="$(sed -e 's/\\/\\\\/g' <<< "false")"
if grep -q "^\\s*automount-open\\s*=" "${DCONFFILE}"
then
        sed -i "s/\\s*automount-open\\s*=\\s*.*/automount-open=${escaped_value}/g" "${DCONFFILE}"
    else
        sed -i "\\|\\[org/gnome/desktop/media-handling\\]|a\\automount-open=${escaped_value}" "${DCONFFILE}"
fi
# Make sure permissions allow regular users to read dconf settings.
# Also define the umask to avoid `dconf update` changing permissions.
chmod -R u=rwX,go=rX /etc/dconf/db
(umask 0022 && dconf update)
# Check for setting in any of the DConf db directories
LOCKFILES=$(grep -r "^/org/gnome/desktop/media-handling/automount-open$" "/etc/dconf/db/" \
            | grep -v 'distro\|ibus\|local.d' | grep ":" | cut -d":" -f1)
LOCKSFOLDER="/etc/dconf/db/local.d/locks"

mkdir -p "${LOCKSFOLDER}"

# Comment out the configurations in databases different from the target one
if [[ ! -z "${LOCKFILES}" ]]
then
    sed -i -E "s|^/org/gnome/desktop/media-handling/automount-open$|#&|" "${LOCKFILES[@]}"
fi

if ! grep -qr "^/org/gnome/desktop/media-handling/automount-open$" /etc/dconf/db/local.d/
then
    echo "/org/gnome/desktop/media-handling/automount-open" >> "/etc/dconf/db/local.d/locks/00-security-settings-lock"
fi
# Make sure permissions allow regular users to read dconf settings.
# Also define the umask to avoid `dconf update` changing permissions.
chmod -R u=rwX,go=rX /etc/dconf/db
(umask 0022 && dconf update)

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

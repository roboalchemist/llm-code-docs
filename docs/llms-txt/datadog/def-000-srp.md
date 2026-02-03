# Source: https://docs.datadoghq.com/security/default_rules/def-000-srp.md

---
title: Set GNOME3 Screensaver Inactivity Timeout
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Set GNOME3 Screensaver Inactivity
  Timeout
---

# Set GNOME3 Screensaver Inactivity Timeout
 
## Description{% #description %}

The idle time-out value for inactivity in the GNOME3 desktop is configured via the `idle-delay` setting must be set under an appropriate configuration file(s) in the `/etc/dconf/db/local.d` directory and locked in `/etc/dconf/db/local.d/locks` directory to prevent user modification.

For example, to configure the system for a 15 minute delay, add the following to `/etc/dconf/db/local.d/00-security-settings`:

```
[org/gnome/desktop/session]
idle-delay=uint32 900
```

## Rationale{% #rationale %}

A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not logout because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, GNOME3 can be configured to identify when a user's session has idled and take action to initiate a session lock.

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
LOCKFILES=$(grep -r "^/org/gnome/desktop/session/idle-delay$" "/etc/dconf/db/" \
            | grep -v 'distro\|ibus\|local.d' | grep ":" | cut -d":" -f1)
LOCKSFOLDER="/etc/dconf/db/local.d/locks"

mkdir -p "${LOCKSFOLDER}"

# Comment out the configurations in databases different from the target one
if [[ ! -z "${LOCKFILES}" ]]
then
    sed -i -E "s|^/org/gnome/desktop/session/idle-delay$|#&|" "${LOCKFILES[@]}"
fi

if ! grep -qr "^/org/gnome/desktop/session/idle-delay$" /etc/dconf/db/local.d/
then
    echo "/org/gnome/desktop/session/idle-delay" >> "/etc/dconf/db/local.d/locks/00-security-settings-lock"
fi
# Make sure permissions allow regular users to read dconf settings.
# Also define the umask to avoid `dconf update` changing permissions.
chmod -R u=rwX,go=rX /etc/dconf/db
(umask 0022 && dconf update)


inactivity_timeout_value='900'


# Check for setting in any of the DConf db directories
# If files contain ibus or distro, ignore them.
# The assignment assumes that individual filenames don't contain :
readarray -t SETTINGSFILES < <(grep -r "\\[org/gnome/desktop/session\\]" "/etc/dconf/db/" \
                                | grep -v 'distro\|ibus\|local.d' | cut -d":" -f1)
DCONFFILE="/etc/dconf/db/local.d/00-security-settings"
DBDIR="/etc/dconf/db/local.d"

mkdir -p "${DBDIR}"

# Comment out the configurations in databases different from the target one
if [ "${#SETTINGSFILES[@]}" -ne 0 ]
then
    if grep -q "^\\s*idle-delay\\s*=" "${SETTINGSFILES[@]}"
    then
        
        sed -Ei "s/(^\s*)idle-delay(\s*=)/#\1idle-delay\2/g" "${SETTINGSFILES[@]}"
    fi
fi

[ ! -z "${DCONFFILE}" ] && echo "" >> "${DCONFFILE}"
if ! grep -q "\\[org/gnome/desktop/session\\]" "${DCONFFILE}"
then
    printf '%s\n' "[org/gnome/desktop/session]" >> ${DCONFFILE}
fi

escaped_value="$(sed -e 's/\\/\\\\/g' <<< "uint32 ${inactivity_timeout_value}")"
if grep -q "^\\s*idle-delay\\s*=" "${DCONFFILE}"
then
        sed -i "s/\\s*idle-delay\\s*=\\s*.*/idle-delay=${escaped_value}/g" "${DCONFFILE}"
    else
        sed -i "\\|\\[org/gnome/desktop/session\\]|a\\idle-delay=${escaped_value}" "${DCONFFILE}"
fi
# Make sure permissions allow regular users to read dconf settings.
# Also define the umask to avoid `dconf update` changing permissions.
chmod -R u=rwX,go=rX /etc/dconf/db
(umask 0022 && dconf update)

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

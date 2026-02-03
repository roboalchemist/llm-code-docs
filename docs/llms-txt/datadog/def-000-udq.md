# Source: https://docs.datadoghq.com/security/default_rules/def-000-udq.md

---
title: All AppArmor Profiles are in enforce or complain mode
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > All AppArmor Profiles are in enforce or
  complain mode
---

# All AppArmor Profiles are in enforce or complain mode
 
## Description{% #description %}

AppArmor profiles define what resources applications are able to access. To set all profiles to either `enforce` or `complain` mode run the following command to set all profiles to `enforce` mode:

```
$ sudo aa-enforce /etc/apparmor.d/*
```

run the following command to set all profiles to `complain` mode:

```
$ sudo aa-complain /etc/apparmor.d/*
```

To list unconfined processes run the following command:

```
$ sudo apparmor_status | grep processes
```

Any unconfined processes may need to have a profile created or activated for them and then be restarted.

## Rationale{% #rationale %}

Security configuration requirements vary from site to site. Some sites may mandate a policy that is stricter than the default policy, which is perfectly acceptable. This recommendation is intended to ensure that any policies that exist on the system are activated.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ] && { ( [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ] && dpkg-query --show --showformat='${db:Status-Status}' 'apparmor' 2>/dev/null | grep -q '^installed$' ); }; then

var_apparmor_mode='enforce'


# make sure apparmor-utils is installed for aa-complain and aa-enforce
DEBIAN_FRONTEND=noninteractive apt-get install -y "apparmor-utils"

# Reload all AppArmor profiles
apparmor_parser -q -r /etc/apparmor.d/

# Set the mode
APPARMOR_MODE="$var_apparmor_mode"

if [ "$APPARMOR_MODE" = "enforce" ]
then
  
  # Set all profiles to enforce mode except disabled profiles
  find /etc/apparmor.d -maxdepth 1 ! -type d -exec bash -c '[[ -e "/etc/apparmor.d/disable/$(basename "$1")" ]] || aa-enforce "$1"' _ {} \;
  
fi

if [ "$APPARMOR_MODE" = "complain" ]
then
  
  # Load all not-loaded profiles into complain mode
  apparmor_parser -a --Complain /etc/apparmor.d/
  echo "***WARNING***: This remediation will not downgrade any existing AppArmor profiles."
  
fi

if [ "$APPARMOR_MODE" = "keep_existing_mode" ]
then
  echo "***WARNING***: This remediation will not modify any existing AppArmor profiles."
fi


UNCONFINED=$(aa-status | grep "processes are unconfined" | awk '{print $1;}')
if [ $UNCONFINED -ne 0 ];

then
  echo -e "***WARNING***: There are some unconfined processes:"
  echo -e "----------------------------"
  echo "The may need to have a profile created or activated for them and then be restarted."
  for PROCESS in "${UNCONFINED[@]}"
  do
      echo "$PROCESS"
  done
  echo -e "----------------------------"
  echo "The may need to have a profile created or activated for them and then be restarted."
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

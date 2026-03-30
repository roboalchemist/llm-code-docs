# Source: https://docs.datadoghq.com/security/default_rules/def-000-ai1.md

---
title: Ensure AppArmor is enabled in the bootloader configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure AppArmor is enabled in the
  bootloader configuration
---

# Ensure AppArmor is enabled in the bootloader configuration

## Description{% #description %}

Configure AppArmor to be enabled at boot time and verify that it has not been overwritten by the bootloader boot parameters. Note: This recommendation is designed around the grub bootloader, if LILO or another bootloader is in use in your environment, enact equivalent settings.

## Rationale{% #rationale %}

AppArmor must be enabled at boot time in your bootloader configuration to ensure that the controls it provides are not overridden.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; then

# Correct the form of default kernel command line in GRUB
if grep -q '^\s*GRUB_CMDLINE_LINUX=.*apparmor=.*"'  '/etc/default/grub' ; then
       # modify the GRUB command-line if an apparmor= arg already exists
       sed -i "s/\(^\s*GRUB_CMDLINE_LINUX=\".*\)apparmor=[^[:space:]]\+\(.*\"\)/\1apparmor=1\2/"  '/etc/default/grub'
# Add to already existing GRUB_CMDLINE_LINUX parameters
elif grep -q '^\s*GRUB_CMDLINE_LINUX='  '/etc/default/grub' ; then
       # no apparmor=arg is present, append it
       sed -i "s/\(^\s*GRUB_CMDLINE_LINUX=\".*\)\"/\1 apparmor=1\"/"  '/etc/default/grub'
# Add GRUB_CMDLINE_LINUX parameters line
else
       echo "GRUB_CMDLINE_LINUX=\"apparmor=1\"" >> '/etc/default/grub'
fi
# Correct the form of default kernel command line in GRUB
if grep -q '^\s*GRUB_CMDLINE_LINUX=.*security=.*"'  '/etc/default/grub' ; then
       # modify the GRUB command-line if an security= arg already exists
       sed -i "s/\(^\s*GRUB_CMDLINE_LINUX=\".*\)security=[^[:space:]]\+\(.*\"\)/\1security=apparmor\2/"  '/etc/default/grub'
# Add to already existing GRUB_CMDLINE_LINUX parameters
elif grep -q '^\s*GRUB_CMDLINE_LINUX='  '/etc/default/grub' ; then
       # no security=arg is present, append it
       sed -i "s/\(^\s*GRUB_CMDLINE_LINUX=\".*\)\"/\1 security=apparmor\"/"  '/etc/default/grub'
# Add GRUB_CMDLINE_LINUX parameters line
else
       echo "GRUB_CMDLINE_LINUX=\"security=apparmor\"" >> '/etc/default/grub'
fi


update-grub

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

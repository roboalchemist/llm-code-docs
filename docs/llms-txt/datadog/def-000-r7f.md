# Source: https://docs.datadoghq.com/security/default_rules/def-000-r7f.md

---
title: Disable XDMCP in GDM
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable XDMCP in GDM
---

# Disable XDMCP in GDM
 
## Description{% #description %}

XDMCP is an unencrypted protocol, and therefore, presents a security risk, see e.g. [XDMCP Gnome docs](https://help.gnome.org/admin/gdm/stable/security.html.en_GB#xdmcpsecurity). To disable XDMCP support in Gnome, set `Enable` to `false` under the `[xdmcp]` configuration section in `/etc/gdm/custom.conf`. For example:

```

[xdmcp]
Enable=false
```

## Rationale{% #rationale %}

XDMCP provides unencrypted remote access through the Gnome Display Manager (GDM) which does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to login using XDMCP, the privileged user password could be compromised due to typed XEvents and keystrokes will traversing over the network in clear text.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'gdm3' 2>/dev/null | grep -q '^installed$'; then

# Try find '[xdmcp]' and 'Enable' in '/etc/gdm3/custom.conf', if it exists, set
# to 'false', if it isn't here, add it, if '[xdmcp]' doesn't exist, add it there
if grep -qzosP '[[:space:]]*\[xdmcp]([^\n\[]*\n+)+?[[:space:]]*Enable' '/etc/gdm3/custom.conf'; then
    
    sed -i "s/Enable[^(\n)]*/Enable=false/" '/etc/gdm3/custom.conf'
elif grep -qs '[[:space:]]*\[xdmcp]' '/etc/gdm3/custom.conf'; then
    sed -i "/[[:space:]]*\[xdmcp]/a Enable=false" '/etc/gdm3/custom.conf'
else
    if test -d "/etc/gdm3"; then
        printf '%s\n' '[xdmcp]' "Enable=false" >> '/etc/gdm3/custom.conf'
    else
        echo "Config file directory '/etc/gdm3' doesnt exist, not remediating, assuming non-applicability." >&2
    fi
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

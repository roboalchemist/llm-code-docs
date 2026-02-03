# Source: https://docs.datadoghq.com/security/default_rules/def-000-qix.md

---
title: Verify pam_pwquality module is activated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify pam_pwquality module is
  activated
---

# Verify pam_pwquality module is activated
 
## Description{% #description %}

The `pam_pwquality.so` module ensures password quality by evaluating user-created passwords against a system dictionary and a set of rules designed to detect weak choices. Originally derived from the pam_cracklib module, this module is backward-compatible with options of pam_cracklib.

The module's process includes prompting the user for a password, checking its strength, and if it meets the criteria requesting the password again for confirmation. If both entries match, the password is passed to subsequent modules to be set as the new authentication token.

## Rationale{% #rationale %}

Strong passwords significantly increase the time and effort required for unauthorized access, increasing overall system security.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

conf_name=cac_pwquality
if [ ! -f /usr/share/pam-configs/"$conf_name" ]; then
    cat << EOF > /usr/share/pam-configs/"$conf_name"
Name: Pwquality password strength checking
Default: yes
Priority: 1025
Conflicts: cracklib, pwquality
Password-Type: Primary
Password:
    requisite                   pam_pwquality.so
EOF
fi

DEBIAN_FRONTEND=noninteractive pam-auth-update

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

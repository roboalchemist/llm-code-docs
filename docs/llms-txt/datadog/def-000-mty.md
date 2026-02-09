# Source: https://docs.datadoghq.com/security/default_rules/def-000-mty.md

---
title: Verify ufw Active
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify ufw Active
---

# Verify ufw Active
 
## Description{% #description %}

Verify the ufw is enabled on the system with the following command:

```
# sudo ufw status
```

If the above command returns the status as "inactive" or any type of error, this is a finding.

## Rationale{% #rationale %}

Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Ubuntu 22.04 LTS functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components.

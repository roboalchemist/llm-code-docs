# Source: https://docs.datadoghq.com/security/default_rules/def-000-6ju.md

---
title: Limit Users' SSH Access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Limit Users' SSH Access
---

# Limit Users' SSH Access

## Description{% #description %}

By default, the SSH configuration allows any user with an account to access the system. There are several options available to limit which users and group can access the system via SSH. It is recommended that at least one of the following options be leveraged:

- AllowUsers variable gives the system administrator the option of allowing specific users to ssh into the system. The list consists of space separated user names. Numeric user IDs are not recognized with this variable. If a system administrator wants to restrict user access further by specifically allowing a user's access only from a particular host, the entry can be specified in the form of user@host.
- AllowGroups variable gives the system administrator the option of allowing specific groups of users to ssh into the system. The list consists of space separated group names. Numeric group IDs are not recognized with this variable.
- DenyUsers variable gives the system administrator the option of denying specific users to ssh into the system. The list consists of space separated user names. Numeric user IDs are not recognized with this variable. If a system administrator wants to restrict user access further by specifically denying a user's access from a particular host, the entry can be specified in the form of user@host.
- DenyGroups variable gives the system administrator the option of denying specific groups of users to ssh into the system. The list consists of space separated group names. Numeric group IDs are not recognized with this variable.

## Rationale{% #rationale %}

Specifying which accounts are allowed SSH access into the system reduces the possibility of unauthorized access to the system.

## Warning{% #warning %}

Automated remediation is not available for this configuration check because each system has unique user names and group names.

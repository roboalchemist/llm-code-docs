# Source: https://docs.datadoghq.com/security/default_rules/def-000-ktl.md

---
title: Okta Org2Org application user syncing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Okta Org2Org application user syncing
---

# Okta Org2Org application user syncing
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detects configuration of user or password synchronization for an Okta instance through the Okta Org2Org integration.

## Strategy{% #strategy %}

This rule monitors Okta activity for [Org2Org](https://www.okta.com/integrations/okta-org2org/) events resulting in pushing, importing, or syncing users from one organization to the target organization. Okta Org2Org feature enables the connection of multiple source organizations to a single target organization. The integration allows a source organization to push users to the target organization.

Enabling synchronization between Okta tenants can result in persistence through attacker controlled users [persistent user](https://www.okta.com/integrations/okta-org2org/).

## Triage & Response{% #triage--response %}

1. Review the change details to confirm the specific sync capability enabled (user push, import, or password sync) and the associated `Org2Org` application instance.
1. Identify the actor, `{{@usr.email}}`, and determine whether an approved change request exists for establishing or modifying the users within the target Okta instance.
1. Check recent activity from the same actor and source IP `{{@network.client.ip}}` for additional administrative actions or unusual authentication patterns.
1. Review subsequent provisioning events (user creations, updates, group assignments).
1. If user activity is suspicious, begin your organization's incident response process and investigate for any account takeovers.

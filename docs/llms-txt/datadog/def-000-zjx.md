# Source: https://docs.datadoghq.com/security/default_rules/def-000-zjx.md

---
title: Okta policy rule modified to downgrade MFA
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta policy rule modified to downgrade
  MFA
---

# Okta policy rule modified to downgrade MFA
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detects modification of an Okta policy rule that downgrades multiâfactor authentication to `1FA`. Alerts when a policy rule is updated to require singleâfactor authentication.

## Strategy{% #strategy %}

This rule monitors when an administrator updates an Okta policy rule, indicating by a `policy.rule.update` event. The policy rule action details includes the previous and updated policy rule. When the previous policy logic does not contain `1FA` but the updated logic does, an alert will trigger.

A higherâseverity alert is generated when the source IP address has been classified as `suspicious` or `malicious`. Downgrading multi-factor authentication requirements reduces security posture and can be used by an attacker to maintain persistence. The change also increases likelihood of an account compromise through social engineering or credential compromise.

## Triage & Response{% #triage--response %}

- Examine `@target.changeDetails.from.policyRuleActionJson` and `@target.changeDetails.to.policyRuleActionJson` to verify the exact requirement change.
- Identify the administrator and source IP `{{@network.client.ip}}` associated with the action.
- Check for additional policy, group, or application changes by the same actor to assess scope and potential misuse.
- Determine which users and applications are governed by `{{@target.displayName}}` and evaluate the risk of singleâfactor access.
- If the policy change event is unexpected or resulted in suspicious activities, initiate your incident response plan.

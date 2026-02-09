# Source: https://docs.datadoghq.com/security/default_rules/vvv-5pb-z59.md

---
title: An AWS S3 bucket mfaDelete is disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > An AWS S3 bucket mfaDelete is disabled
---

# An AWS S3 bucket mfaDelete is disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect if versioning or MFA delete was disabled within an AWS S3 bucket's Lifecycle configuration.

## Strategy{% #strategy %}

This rule has two separate queries. The first query determines if `@requestParameters.VersioningConfiguration.MfaDelete` is set to `Disabled`. The second query determines if `@requestParameters.VersioningConfiguration.Status` is set to `Suspended`. For generating a signal, there are two cases. Case one generates a `Medium` signal if query one AND two return `true`. Case two will generate a `Low` signal if query one OR two returns `true`.

**NOTE**: Versioning cannot be disabled permanently; only suspended until turned back on, once it has been enabled on a bucket.

## Triage & Response{% #triage--response %}

Determine if `{{@evt.name}}` should have occurred on the `{{@requestParameters.bucketName}}` by `username:` `{{@userIdentity.sessionContext.sessionIssuer.userName}}`, `accountId:` `{{@userIdentity.accountId}}` of `type:` `{{@userIdentity.assumed_role}}`.

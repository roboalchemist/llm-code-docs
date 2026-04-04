# Source: https://docs.datadoghq.com/security/default_rules/def-000-ta5.md

---
title: SES should use Email Address Identities
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > SES should use Email Address Identities
---

# SES should use Email Address Identities

## Description{% #description %}

Amazon SES must use Email Address Identities for verification of identities allowed to send email, to prevent unauthorized email sending and maintain sender reputation.

## Remediation{% #remediation %}

Configure Email Address Identities in Amazon SES to verify and authorize specific email addresses for sending. Remove any domain-based identities that are not necessary. Refer to the [Amazon SES identity management documentation](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html) for detailed steps.

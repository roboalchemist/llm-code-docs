# Source: https://docs.datadoghq.com/security/default_rules/def-000-fdu.md

---
title: KMS key policy should not allow everyone to use it
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > KMS key policy should not allow
  everyone to use it
---

# KMS key policy should not allow everyone to use it
 
## Description{% #description %}

KMS keys are assigned a resource-based policy that controls who can use and manage the key.

## Rationale{% #rationale %}

When the key policy is misconfigured, it can allow any unauthenticated user with knowledge of the key ID to use it for encryption, decryption, signing and verification purposes.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the list of customer-managed KMS keys at [https://console.aws.amazon.com/kms/home#/kms/keys](https://console.aws.amazon.com/kms/home#/kms/keys).

1. Click the vulnerable KMS key name.

1. In the **Key Policy** tab, remove the statement making the key publicly accessible.

### From the command line{% #from-the-command-line %}

1. Retrieve the current key policy:

```
aws kms get-key-policy \
   --key-id <KEY_ARN> \
   --policy-name default \
   --query Policy --output text > key_policy.json
```
Remove the statement making the key publicly accessible, then update the key policy:
```
aws kms put-key-policy \
   --key-id <KEY_ARN> \
   --policy-name default \
   --policy file://./key_policy.json
```

## References{% #references %}

1. [https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html]
1. [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-resources.html#access-analyzer-kms-key]

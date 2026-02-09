# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/s3_bucket_allows_access_to_all_authenticated_users.md

---
title: S3 bucket allows authenticated users access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket allows authenticated users access
---

# S3 bucket allows authenticated users access

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d4e5f6g7-h8i9-0jkl-1234-mn567opq8901`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_acl)

### Description{% #description %}

This check verifies if AWS S3 bucket ACLs are configured to prevent access from all authenticated AWS users. When an S3 bucket grants access to the `AuthenticatedUsers` group, it allows any AWS account holder worldwide to access your data, not just users within your organization. This significantly increases the risk of unauthorized data access, potential data breaches, and violation of data governance policies.

To secure your S3 bucket, use specific canonical user IDs rather than the global authenticated users group. For example, instead of using:

```
grantee {
  type = "Group"
  uri  = "http://acs.amazonaws.com/groups/global/AuthenticatedUsers"
}
```

Use a specific user configuration:

```
grantee {
  type = "CanonicalUser"
  id   = "1234567890abcdef1234567890abcdef12345678"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_s3_bucket_acl" "good_example" {
  bucket = aws_s3_bucket.example.id

  access_control_policy {
    grant {
      grantee {
        type = "CanonicalUser"
        id   = "1234567890abcdef1234567890abcdef12345678" # â Restricted access
      }
      permission = "READ"
    }
    owner {
      id = aws_s3_bucket.example.owner_id
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_s3_bucket_acl" "bad_example" {
  bucket = aws_s3_bucket.example.id

  access_control_policy {
    grant {
      grantee {
        type = "Group"
        uri  = "http://acs.amazonaws.com/groups/global/AuthenticatedUsers" # â Allows access to all authenticated users
      }
      permission = "READ"
    }
    owner {
      id = aws_s3_bucket.example.owner_id
    }
  }
}
```

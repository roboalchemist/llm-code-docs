# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/dnssec_using_rsasha1.md

---
title: DNSSEC using RSASHA1
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > DNSSEC using RSASHA1
---

# DNSSEC using RSASHA1

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ccc3100c-0fdd-4a5e-9908-c10107291860`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dns_managed_zone#algorithm)

### Description{% #description %}

DNSSEC should not use the RSASHA1 algorithm, which is considered weak and vulnerable to cryptographic attacks. If a `dnssec_config` block contains a `default_key_specs` attribute with `algorithm = "rsasha1"`, attackers may be able to exploit known weaknesses in the algorithm to forge DNS records, potentially redirecting users to malicious sites or causing other security issues. Instead, use a stronger algorithm such as `rsasha256`:

```
dnssec_config {
    default_key_specs {
        algorithm = "rsasha256"
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_dns_managed_zone" "negative1" {
    name        = "example-zone"
    dns_name    = "example-${random_id.rnd.hex}.com."
    description = "Example DNS zone"
    labels = {
        foo = "bar"
    }

    dnssec_config {
        default_key_specs{
            algorithm = "rsasha256"
        }
    }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_dns_managed_zone" "positive1" {
    name        = "example-zone"
    dns_name    = "example-${random_id.rnd.hex}.com."
    description = "Example DNS zone"
    labels = {
        foo = "bar"
    }

    dnssec_config {
        default_key_specs{
            algorithm = "rsasha1"
        }
    }
}
```

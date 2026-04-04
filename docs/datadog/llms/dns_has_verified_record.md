# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/dns_has_verified_record.md

---
title: Beta - Nifcloud DNS has verified record
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud DNS has verified record
---

# Beta - Nifcloud DNS has verified record

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a1defcb6-55e8-4511-8c2a-30b615b0e057`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/dns_record#record)

### Description{% #description %}

Remove the verification TXT record used for DNS authentication (records containing `nifty-dns-verify=`) after verification is complete. If the authentication record remains, others could reuse it to claim or re-register the zone, exposing DNS control to unauthorized parties. This rule flags `nifcloud_dns_record` resources that include `nifty-dns-verify=` and returns attributes `documentId`, `resourceType`, `resourceName`, `searchKey`, `issueType`, `keyExpectedValue`, and `keyActualValue`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_dns_record" "negative" {
  zone_id = nifcloud_dns_zone.example.id
  name    = "test.example.test"
  type    = "TXT"
  ttl     = 300
  record  = "negative"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_dns_record" "positive" {
  zone_id = nifcloud_dns_zone.example.id
  name    = "test.example.test"
  type    = "TXT"
  ttl     = 300
  record  = "nifty-dns-verify=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
```

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/firewall_ingress_allows_unrestricted_ftp_access.md

---
title: Google Compute firewall ingress allows unrestricted FTP access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Google Compute firewall ingress allows
  unrestricted FTP access
---

# Google Compute firewall ingress allows unrestricted FTP access

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d3f8e9c1-7a2b-4d5f-90e2-123456789abc`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall)

### Description{% #description %}

Allowing ingress from `0.0.0.0/0` on port 21 (FTP) in a firewall rule (`source_ranges = ["0.0.0.0/0"]`) exposes the FTP service to the entire internet, significantly increasing the risk of unauthorized access and brute-force attacks. FTP traffic is often unencrypted, which could enable attackers to intercept credentials or exfiltrate sensitive data if unrestricted access is permitted. Restricting ingress to trusted IP ranges (for example, `source_ranges = ["192.168.1.0/24"]`) reduces the attack surface and helps maintain data security.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_compute_firewall" "good_example" {
  name    = "good-firewall"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["21"]
  }

  source_ranges = ["192.168.1.0/24"] # Restricted ingress for FTP
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_compute_firewall" "bad_example" {
  name    = "bad-firewall"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["21"]
  }

  source_ranges = ["0.0.0.0/0"] # Unrestricted ingress for FTP
}
```

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/firewall_ingress_allows_unrestricted_mysql_access.md

---
title: Google Compute firewall ingress allows unrestricted MySQL access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Google Compute firewall ingress allows
  unrestricted MySQL access
---

# Google Compute firewall ingress allows unrestricted MySQL access

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d0a1b2c3-d4e5-6789-abcd-ef0123456789`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall)

### Description{% #description %}

Allowing ingress traffic from `0.0.0.0/0` on port 3306, as shown in the Terraform attribute `source_ranges = ["0.0.0.0/0"]`, exposes MySQL databases to the internet, making them susceptible to unauthorized access and potential attacks. This misconfiguration can lead to data breaches, data loss, or system compromise if malicious actors exploit the open MySQL port. Restricting access to trusted IP ranges, for example `source_ranges = ["192.168.1.0/24"]`, significantly reduces this risk by limiting who can attempt to connect to the database.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_compute_firewall" "good_example" {
  name    = "good-firewall-mysql"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["3306"]
  }

  source_ranges = ["192.168.1.0/24"] # Restricted ingress for MySQL
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_compute_firewall" "bad_example" {
  name    = "bad-firewall-mysql"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["3306"]
  }

  source_ranges = ["0.0.0.0/0"] # Unrestricted ingress for MySQL
}
```

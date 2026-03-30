# Source: https://docs.datadoghq.com/security/default_rules/def-000-6jk.md

---
title: Cloud DNS should have DNSSEC enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Cloud DNS should have DNSSEC enabled
---

# Cloud DNS should have DNSSEC enabled

## Description{% #description %}

Cloud Domain Name System (DNS) is a fast, reliable, and cost-effective domain name system that powers millions of domains on the internet. Domain Name System Security Extensions (DNSSEC) in Cloud DNS enables domain owners to take easy steps to protect their domains against DNS hijacking, man-in-the-middle attacks, and more.

## Rationale{% #rationale %}

Domain Name System Security Extensions (DNSSEC) adds security to the DNS protocol by enabling the DNS responses to be validated. A trustworthy DNS that translates a domain name like `www.example.com` into its associated IP address is an increasingly important building block for modern web-based applications.

Attackers can hijack this process of domain/IP lookup and redirect users to a malicious site through DNS hijacking and man-in-the-middle attacks. DNSSEC helps mitigate the risk of such attacks by cryptographically signing DNS records to prevent attackers from issuing fake DNS responses that may misdirect browsers to nefarious websites.

By default, DNSSEC is not enabled.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Navigate to the [Cloud DNS page](https://console.cloud.google.com/net-services/dns/zones).
1. For each Type Public zone, set `DNSSEC` to **On**.

### From the command line{% #from-the-command-line %}

Use this command to enable DNSSEC for Cloud DNS Zone Name:

```
gcloud dns managed-zones update ZONE_NAME --dnssec-state on
```

## References{% #references %}

1. [https://cloudplatform.googleblog.com/2017/11/DNSSEC-now-available-in-Cloud-DNS.html](https://cloudplatform.googleblog.com/2017/11/DNSSEC-now-available-in-Cloud-DNS.html)
1. [https://cloud.google.com/dns/dnssec-config#enabling](https://cloud.google.com/dns/dnssec-config#enabling)
1. [https://cloud.google.com/dns/dnssec](https://cloud.google.com/dns/dnssec)

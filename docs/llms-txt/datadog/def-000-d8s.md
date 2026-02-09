# Source: https://docs.datadoghq.com/security/default_rules/def-000-d8s.md

---
title: Cloud DNS logging should be enabled for VPC networks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cloud DNS logging should be enabled for
  VPC networks
---

# Cloud DNS logging should be enabled for VPC networks
 
## Description{% #description %}

Cloud DNS logging records the queries from the name servers within your VPC to Stackdriver. Logged queries can come from Compute Engine VMs, GKE containers, or other GCP resources provisioned within the VPC.

### Default value{% #default-value %}

Cloud DNS logging is disabled by default on each network.

## Rationale{% #rationale %}

Security monitoring and forensics cannot depend solely on IP addresses from VPC flow logs, especially when considering the dynamic IP usage of cloud resources, HTTP virtual host routing, and other technology that can obscure the DNS name used by a client from the IP address. Monitoring Cloud DNS logs provides visibility into DNS names requested by the clients within the VPC. These logs can be monitored for anomalous domain names and evaluated against threat intelligence.

To fully capture DNS logging records, your firewall must block egress for UDP/53 (DNS) and TCP/443 (DNS over HTTPS) to prevent the client from using an external DNS name server for resolution.

Only queries that reach a name server are logged. Cloud DNS resolvers cache responses, queries answered from caches, and direct queries to an external DNS resolver outside the VPC are not logged.

### Impact{% #impact %}

Enabling of Cloud DNS logging might result in your project being charged for the additional logs usage.

## Remediation{% #remediation %}

### From the command line{% #from-the-command-line %}

For VPC networks that need a new DNS policy with logging enabled, run the following:

```
gcloud dns policies create enable-dns-logging --enable-logging --
description="Enable DNS Logging" --networks=VPC_NETWORK_NAME
```

The `VPC_NETWORK_NAME` can be one or more networks in a comma-separated list. For VPC networks that have existing DNS policies, run the following to enable logging:

```
gcloud dns policies update POLICY_NAME --enable-logging --
networks=VPC_NETWORK_NAME
```

The `VPC_NETWORK_NAME` can be one or more networks in a comma-separated list.

## References{% #references %}

1. [https://cloud.google.com/dns/docs/monitoring](https://cloud.google.com/dns/docs/monitoring)

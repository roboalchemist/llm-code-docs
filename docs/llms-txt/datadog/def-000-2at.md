# Source: https://docs.datadoghq.com/security/default_rules/def-000-2at.md

---
title: Authentication using Client Certificates should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Authentication using Client
  Certificates should be disabled
---

# Authentication using Client Certificates should be disabled
 
## Description{% #description %}

Client certificates should be disabled, which require certificate rotation, for authentication. [Kubernetes does not have a way to revoke certificates at present and you should use another authentication method like OAuth](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_authn_methods).

**Note:** Basic authentication(static password) has been removed as of v1.19 in Kubernetes.

## Remediation{% #remediation %}

1. Go to the [Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)
1. Click `CREATE CLUSTER`
1. Configure the cluster as required and the click on `Availability, networking, security, and additional features` section
1. Ensure that the `Issue a client certificate` checkbox is not ticked
1. Click `CREATE`.

## References{% #references %}

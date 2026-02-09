# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/audit_policy_not_cover_key_security_concerns.md

---
title: Audit policy does not cover key security concerns
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Audit policy does not cover key security
  concerns
---

# Audit policy does not cover key security concerns

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1828a670-5957-4bc5-9974-47da228f75e2`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/debug-application-cluster/audit/)

### Description{% #description %}

The audit policy should cover key security concerns about sensitive data logged in Kubernetes audit logs. The policy requires rules for specific resources to be defined at the required audit levels (Metadata, Request, RequestResponse). These resources include: secrets, tokenreviews, configmaps, pods, deployments, and pod/service sub-resources (pods/exec, pods/portforward, pods/proxy, services/proxy). Missing any required level for a listed resource indicates the policy may not adequately prevent sensitive information from being recorded or exposed via audit events.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: audit.k8s.io/v1 # This is required.
kind: Policy
# Don't generate audit events for all requests in RequestReceived stage.
omitStages:
  - "RequestReceived"
rules:
  - level: Metadata
    resources:
    - group: ""
      resources: ["secrets","configmaps","tokenreviews"]
  - level: Metadata
    resources:
    - group: ""
      resources: ["pods","deployments"]
  - level: RequestResponse
    resources:
    - group: ""
      resources: ["pods/exec", "pods/portforward", "pods/proxy", "services/proxy"]
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: audit.k8s.io/v1 # This is required.
kind: Policy
# Don't generate audit events for all requests in RequestReceived stage.
rules:
  - level: RequestResponse
    resources:
    - group: ""
      resources: ["secrets","configmaps","tokenreviews"]
  - level: Metadata
    resources:
    - group: ""
      resources: ["pods","deployments"]
  - level: None
    resources:
    - group: ""
      resources: ["pods/exec", "pods/portforward", "pods/proxy", "services/proxy"]
```

```yaml
apiVersion: audit.k8s.io/v1 # This is required.
kind: Policy
# Don't generate audit events for all requests in RequestReceived stage.
omitStages:
  - "RequestReceived"
rules:
  - level: Metadata
    resources:
    - group: ""
      resources: ["secrets","configmaps","tokenreviews"]
  - level: Metadata
    resources:
    - group: ""
      resources: ["pods"]
  - level: RequestResponse
    resources:
    - group: ""
      resources: ["pods/exec", "pods/portforward", "pods/proxy", "services/proxy"]
```

```yaml
apiVersion: audit.k8s.io/v1 # This is required.
kind: Policy
# Don't generate audit events for all requests in RequestReceived stage.
omitStages:
  - "RequestReceived"
rules:
```

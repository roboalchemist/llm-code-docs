# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/net_raw_capabilities_not_being_dropped.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/net_raw_capabilities_not_being_dropped.md

---
title: NET_RAW capabilities not dropped
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > NET_RAW capabilities not dropped
---

# NET_RAW capabilities not dropped

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `dbbc6705-d541-43b0-b166-dd4be8208b54`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

### Description{% #description %}

Containers should drop `ALL` or at least `NET_RAW` capabilities.The container's `securityContext.capabilities.drop` field must include `ALL` or `NET_RAW`.If the `drop` list is undefined or does not include these capabilities, the policy reports a violation.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example
spec:
  containers:
      - name: payment
        image: nginx
        securityContext:
          capabilities:
            drop:
              - ALL
            add:
              - NET_BIND_SERVICE
  privileged: false
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  runAsUser:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
  volumes:
  - '*'
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-unhealthy-deployment
  labels:
    app: redis
spec:
  replicas: 3
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      hostNetwork: true
      hostPID: true
      hostIPC: true
      containers:
      - name: redis
        image: redis:latest
        ports:
        - containerPort: 9001
          hostPort: 9001
        securityContext:
          privileged: true
          readOnlyRootFilesystem: false
          allowPrivilegeEscalation: true
          runAsUser: 0
          capabilities:
            add:
              - NET_ADMIN
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example
spec:
  containers:
      - name: payment
        image: nginx
        securityContext:
          capabilities:
            drop:
              - SYS_ADMIN
      - name: payment2
        image: nginx
      - name: payment4
        image: nginx
        securityContext:
          capabilities:
            add:
              - NET_BIND_SERVICE
      - name: payment3
        image: nginx
        securityContext:
          allowPrivilegeEscalation: false
```

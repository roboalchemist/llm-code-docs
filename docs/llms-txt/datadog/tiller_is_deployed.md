# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/tiller_is_deployed.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/tiller_is_deployed.md

---
title: Tiller (Helm v2) deployed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Tiller (Helm v2) deployed
---

# Tiller (Helm v2) deployed

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `6d173be7-545a-46c6-a81d-2ae52ed1605d`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/containers/images/)

### Description{% #description %}

Tiller (Helm v2) must not be deployed because it is deprecated and no longer supported. This rule detects resources that reference Tiller by resource name or labels (for example, `metadata.name`, `metadata.labels.app == "helm"`, or a `metadata.labels.name` containing "tiller"). It also detects Tiller container images by name in `containers` or `initContainers`, including within pod templates (`spec.template`).

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
  volumes:
    - name: sec-ctx-vol
  containers:
    - name: sec-ctx-demo
      image: busybox
      command: [ "sh", "-c", "sleep 1h" ]
      volumeMounts:
        - name: sec-ctx-vol
          mountPath: /data/demo
      securityContext:
        allowPrivilegeEscalation: false
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
---
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  labels:
    app: helm
    name: tiller
  name: tiller-deploy
spec:
  containers:
    -
      image: tiller-image
      name: tiller-v1
  template:
    metadata:
      labels:
        app: helm
        name: tiller
    spec:
      containers:
        -
          args:
            - "--listen=10.7.2.8:44134"
          image: tiller-image
          name: tiller-v2
          ports:
            -
              containerPort: 44134
              name: tiller
              protocol: TCP
            -
              containerPort: 44135
              name: http
              protocol: TCP
      serviceAccountName: tiller
```

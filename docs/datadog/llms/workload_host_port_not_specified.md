# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/workload_host_port_not_specified.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/workload_host_port_not_specified.md

---
title: Workload host port not specified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Workload host port not specified
---

# Workload host port not specified

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2b1836f1-dcce-416e-8e16-da8c71920633`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/#exposing-the-service)

### Description{% #description %}

Checks whether a Kubernetes workload defines a container port with a specified hostPort. It inspects both top-level pod specs and workload templates (spec.template.spec) for entries in containers and initContainers and reports any ports where hostPort is defined. Findings are reported as "IncorrectValue" because container port entries should not include hostPort.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: firstpod
spec:
  containers:
  - name: container
    image: nginx
    ports:
    - containerPort: 80
      hostIP: 10.0.0.1
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: firstpod
spec:
  containers:
  - name: container
    image: nginx
    ports:
    - containerPort: 80
      hostIP: 10.0.0.1
      hostPort: 8080
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secondpod
spec:
  template:
    spec:
      containers:
      - name: container2
        image: nginx
        ports:
        - containerPort: 81
          hostIP: 10.0.0.2
          hostPort: 8081
    metadata:
      labels:
        app: nginx
  selector:
    matchLabels:
      app: nginx
```

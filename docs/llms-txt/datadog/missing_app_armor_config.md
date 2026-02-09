# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/missing_app_armor_config.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/missing_app_armor_config.md

---
title: Missing AppArmor profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Missing AppArmor profile
---

# Missing AppArmor profile

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8b36775e-183d-4d46-b0f7-96a6f34a723f`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tutorials/clusters/apparmor/)

### Description{% #description %}

Containers should be configured with an AppArmor profile to enforce fine-grained access control over low-level system resources. This rule requires each container to have the annotation `container.apparmor.security.beta.kubernetes.io/<container>` set to `runtime/default` or to a `localhost/<profile>` value. Missing or invalid annotations are reported as MissingAttribute or IncorrectValue issues. The rule validates annotations on Pod templates, Job templates, and top-level Pod resources.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hello-apparmor-2positive
  annotations:
    container.apparmor.security.beta.kubernetes.io/hello: localhost/k8s-apparmor-example-allow-write
spec:
  containers:
  - name: hello
    image: busybox
    command: [ "sh", "-c", "echo 'Hello AppArmor!' && sleep 1h" ]
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hello-apparmor-1
  annotations:
    container.apparmor.security.beta.kubernetes.io/hello1: dummy
    container.apparmor.security.beta.kubernetes.io/hello2: dummy
spec:
  containers:
  - name: hello1
    image: busybox
    command: [ "sh", "-c", "echo 'Hello AppArmor!' && sleep 1h" ]
  - name: hello2
    image: busybox
    command: [ "sh", "-c", "echo 'Hello AppArmor!' && sleep 1h" ]
  - name: hello3
    image: busybox
    command: [ "sh", "-c", "echo 'Hello AppArmor!' && sleep 1h" ]
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ubuntu-test1
  namespace: testns
  labels:
    deployment: ubuntu-1
spec:
  replicas: 1
  selector:
    matchLabels:
      container: ubuntu-1
  template:
    metadata:
      labels:
        container: ubuntu-1
      annotations:
        container.apparmor.security.beta.kubernetes.io/ubuntu-1-container: dummy
    spec:
      containers:
      - name: ubuntu-1-container
        image: 0x010/ubuntu-w-utils:latest
```

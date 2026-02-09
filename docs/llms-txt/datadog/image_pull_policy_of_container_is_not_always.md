# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/image_pull_policy_of_container_is_not_always.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/image_pull_policy_of_container_is_not_always.md

---
title: Image pull policy of the container is not set to always
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Image pull policy of the container is not set
  to always
---

# Image pull policy of the container is not set to always

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `caa3479d-885d-4882-9aac-95e5e78ef5c2`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/containers/images/#updating-images)

### Description{% #description %}

The container `imagePullPolicy` must be set to `Always`. This requirement applies when the image is referenced with an explicit tag (contains ':') and is not referenced by digest (`@...`) or by the `:latest` tag. Setting `imagePullPolicy` to `Always` ensures the image is pulled on every start and prevents relying on mutable images cached locally.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-image-test-1
spec:
  containers:
    - name: uses-private-image
      image: $PRIVATE_IMAGE_NAME
      imagePullPolicy: Always
      command: [ "echo", "SUCCESS" ]
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-with-image-pull-policy
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: library/nginx:1.20.0
          imagePullPolicy: IfNotPresent
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-with-image-pull-policy1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: library/nginx:1.20.0
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-image-test-always
spec:
  containers:
    - name: uses-private-image
      image: $PRIVATE_IMAGE_NAME:1.2
      imagePullPolicy: Never
      command: [ "echo", "SUCCESS" ]
```

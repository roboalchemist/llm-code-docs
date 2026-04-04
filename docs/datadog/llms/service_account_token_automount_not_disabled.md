# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/service_account_token_automount_not_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/service_account_token_automount_not_disabled.md

---
title: Service account token auto-mount not disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Service account token auto-mount not disabled
---

# Service account token auto-mount not disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `48471392-d4d0-47c0-b135-cdec95eb3eef`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Insecure Defaults

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server)

### Description{% #description %}

Service account tokens are automatically mounted even if not necessary. This rule detects workloads where `automountServiceAccountToken` is set to true on the pod spec or inherited from the referenced ServiceAccount, and flags resources that should set it to false. Pod-level `automountServiceAccountToken` takes precedence over the ServiceAccount setting. If the pod-level key is missing, the ServiceAccount value is evaluated. The rule reports IncorrectValue when the token is enabled, and MissingAttribute when the attribute is undefined on both the pod and the referenced ServiceAccount.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo
spec:
  automountServiceAccountToken: false
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
  volumes:
    - name: sec-ctx-vol
      emptyDir: { }
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

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: redistest-sa
automountServiceAccountToken: false
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demoenv
  labels:
    app: redis
spec:
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      serviceAccountName: redistest-sa
      containers:
      - name: redis
        image: redis:latest
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: redistest-sa
automountServiceAccountToken: true
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demoenv
  labels:
    app: redis
spec:
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      serviceAccountName: redistest-sa
      containers:
      - name: redis
        image: redis:latest
```

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
      emptyDir: { }
  containers:
    - name: sec-ctx-demo
      image: busybox
      command: [ "sh", "-c", "sleep 1h" ]
      volumeMounts:
        - name: sec-ctx-vol
          mountPath: /data/demo
      securityContext:
        allowPrivilegeEscalation: false
---
apiVersion: v1
kind: Pod
metadata:
  name: security.context.demo
spec:
  automountServiceAccountToken: true
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
  volumes:
    - name: sec-ctx-vol
      emptyDir: { }
  containers:
    - name: sec-ctx-demo
      image: busybox
      command: [ "sh", "-c", "sleep 1h" ]
      volumeMounts:
        - name: sec-ctx-vol
          mountPath: /data/demo
      securityContext:
        allowPrivilegeEscalation: false
---
apiVersion: serving.knative.dev/v1
kind: Configuration
metadata:
  name: dummy-config
  namespace: knative-sequence
spec:
  template:
    spec:
      automountServiceAccountToken: true
      securityContext:
        runAsUser: 1000
        runAsGroup: 3000
        fsGroup: 2000
      volumes:
        - name: sec-ctx-vol
          emptyDir: { }
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

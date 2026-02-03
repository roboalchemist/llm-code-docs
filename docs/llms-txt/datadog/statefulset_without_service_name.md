# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/statefulset_without_service_name.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/statefulset_without_service_name.md

---
title: StatefulSet without service name
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > StatefulSet without service name
---

# StatefulSet without service name

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `bb241e61-77c3-4b97-9575-c0f8a1e008d0`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Availability

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

### Description{% #description %}

StatefulSets should reference an existing headless Service via `spec.serviceName`. The referenced Service must be headless (`spec.clusterIP` set to "None") and located in the same namespace. All selector labels defined on the Service must be present on the StatefulSet pod template labels so the Service can target the StatefulSet's pods.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this is a problematic code where the query should report a result(s)
apiVersion: v1
kind: Service
metadata:
  name: nginx2
  namespace: nginx2
  labels:
    app: nginx2
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx2
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web2
  namespace: nginx2
spec:
  selector:
    matchLabels:
      app: nginx2
  serviceName: "nginx2"
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx2
        foo: bar
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx2
        image: k8s.gcr.io/nginx-slim:0.8
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "my-storage-class"
      resources:
        requests:
          storage: 1Gi
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
#this is a problematic code where the query should report a result(s)
apiVersion: v1
kind: Service
metadata:
  name: nginx
  namespace: nginx
  labels:
    app: nginx2
spec:
  ports:
  - port: 80
    name: web
  clusterIP: All
  selector:
    app: nginx
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
  namespace: nginx
spec:
  selector:
    matchLabels:
      app: nginx
  serviceName: "nginx"
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: k8s.gcr.io/nginx-slim:0.8
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "my-storage-class"
      resources:
        requests:
          storage: 1Gi
```

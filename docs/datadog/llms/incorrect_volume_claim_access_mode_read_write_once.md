# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/incorrect_volume_claim_access_mode_read_write_once.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/incorrect_volume_claim_access_mode_read_write_once.md

---
title: Incorrect volume claim access mode ReadWriteOnce
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Incorrect volume claim access mode
  ReadWriteOnce
---

# Incorrect volume claim access mode ReadWriteOnce

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3878dc92-8e5d-47cf-9cdd-7590f71d21b9`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Build Process

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

### Description{% #description %}

Kubernetes StatefulSets must include exactly one volume claim template with the access mode `ReadWriteOnce`. The rule flags StatefulSets that either do not include any `spec.volumeClaimTemplates` with `accessModes` containing `ReadWriteOnce` (issue type: MissingAttribute) or include more than one such template (issue type: IncorrectValue). The check inspects each entry in `spec.volumeClaimTemplates[].spec.accessModes` to determine the presence of `ReadWriteOnce`.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: nginx # has to match .spec.template.metadata.labels
  serviceName: "nginx"
  replicas: 3 # by default is 1
  template:
    metadata:
      labels:
        app: nginx # has to match .spec.selector.matchLabels
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

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
#this is a problematic code where the query should report a result(s)
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: nginx # has to match .spec.template.metadata.labels
  serviceName: "nginx"
  replicas: 3 # by default is 1
  template:
    metadata:
      labels:
        app: nginx # has to match .spec.selector.matchLabels
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
  - metadata:
      name: aaa
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "my-storage-class"
      resources:
        requests:
          storage: 1Gi

---

apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web2
spec:
  selector:
    matchLabels:
      app: nginx # has to match .spec.template.metadata.labels
  serviceName: "nginx"
  replicas: 3 # by default is 1
  template:
    metadata:
      labels:
        app: nginx # has to match .spec.selector.matchLabels
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
      accessModes: [ "ReadWrite" ]
      storageClassName: "my-storage-class"
      resources:
        requests:
          storage: 1Gi
  - metadata:
      name: aaa
    spec:
      accessModes: [ "ReadWrite" ]
      storageClassName: "my-storage-class"
      resources:
        requests:
          storage: 1Gi
```

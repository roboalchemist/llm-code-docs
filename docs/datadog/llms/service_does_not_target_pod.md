# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/service_does_not_target_pod.md

---
title: Service does not target a Pod
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Service does not target a Pod
---

# Service does not target a Pod

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3ca03a61-3249-4c16-8427-6f8e47dda729`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/services-networking/service/)

### Description{% #description %}

The Service must target at least one Pod. Its `.spec.selector` must match labels on Pod-bearing resources (Pod, ReplicationController, ReplicaSet, Deployment, DaemonSet, StatefulSet, Job, or CronJob job template). Each Service port must reference a container port on at least one matched Pod â either by numeric `targetPort`, by named `targetPort`, or by falling back to the Service `port` when `targetPort` is unspecified.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml

apiVersion: v1
kind: Service
metadata:
  name: helloworld
spec:
  type: NodePort
  selector:
    app: helloworld
  ports:
    - name: http
      nodePort: 30475
      port: 8089
      protocol: TCP
      targetPort: 8089

---

apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: helloworld
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
      - containerPort: 8089
```

```yaml
apiVersion: v1
kind: Service
metadata:
  name: helloworld
spec:
  type: NodePort
  selector:
    app: helloworld
  ports:
    - name: http
      nodePort: 30475
      port: 8089
      protocol: TCP
      targetPort: 8089
---
apiVersion: v1
kind: Pod
metadata:
  name: nginx3
  labels:
    app: helloworld
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
      - containerPort: 808
---
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: helloworld
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
      - containerPort: 8089
```

```yaml
apiVersion: v1
kind: Service
metadata:
  name: negative4
spec:
  selector:
    app: negative4
    tier: backend
  ports:
  - protocol: TCP
    port: 80
    targetPort: http
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
spec:
  selector:
    matchLabels:
      app: negative4
      tier: backend
      track: stable
  replicas: 3
  template:
    metadata:
      labels:
        app: negative4
        tier: backend
        track: stable
    spec:
      containers:
        - name: negative4
          image: "gcr.io/google-samples/hello-go-gke:1.0"
          ports:
            - name: http
              containerPort: 80
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Service
metadata:
  name: helloworld3
spec:
  type: NodePort
  selector:
    app: helloworld3
  ports:
    - name: http
      nodePort: 30475
      port: 9377
      protocol: TCP
      targetPort: 9377
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: helloworld3
spec:
  replicas: 3
  selector:
    matchLabels:
      app: helloworld3
  template:
    metadata:
      labels:
        app: helloworld3
    spec:
      containers:
        - name: nginx
          image: nginx:1.14.2
          ports:
            - containerPort: 80
```

```yaml
apiVersion: v1
kind: Service
metadata:
  name: helloworld2
spec:
  type: NodePort
  selector:
    app: helloworld2
  ports:
    - name: http
      nodePort: 30475
      port: 9377
      protocol: TCP
      targetPort: 9377
---
apiVersion: v1
kind: Pod
metadata:
  name: nginx2
  labels:
    app: hellowwwworld
spec:
  containers:
    - name: nginx
      image: nginx
      ports:
        - containerPort: 9377
```

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/service_with_external_load_balancer.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/service_with_external_load_balancer.md

---
title: Service with external load balancer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Service with external load balancer
---

# Service with external load balancer

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `26763a1c-5dda-4772-b507-5fca7fb5f165`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/)

### Description{% #description %}

This Service uses a LoadBalancer and therefore creates an external load balancer, which may allow access from other networks and the internet. Annotations must be set to indicate an internal load balancer for supported cloud providers (for example, `networking.gke.io/load-balancer-type=Internal`, `cloud.google.com/load-balancer-type=Internal`, `service.beta.kubernetes.io/aws-load-balancer-internal=true`, `service.beta.kubernetes.io/azure-load-balancer-internal=true`) to avoid external exposure.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Service
metadata:
  name: sample-service 01
  annotations:
    cloud.google.com/load-balancer-type: 'Internal'
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: LoadBalancer
  selector:
    app: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: sample-service 02
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-internal: 'true'
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: LoadBalancer
  selector:
    app: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: sample-service 03
  annotations:
    service.beta.kubernetes.io/azure-load-balancer-internal: 'true'
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: LoadBalancer
  selector:
    app: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: sample-service 04
  annotations:
    networking.gke.io/load-balancer-type: 'Internal'
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: LoadBalancer
  selector:
    app: nginx
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Service
metadata:
  name: sample-service 05
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: LoadBalancer
  selector:
    app: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: sample-service 05334443
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-internal: 'false'
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: LoadBalancer
  selector:
    app: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: sample-service 07
  annotations:
    service.beta.kubernetes.io/azure-load-balancer-internal: 'false'
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: LoadBalancer
  selector:
    app: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: sample-service 08
  annotations:
    networking.gke.io/load-balancer-type: 'External'
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: LoadBalancer
  selector:
    app: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: sample-service 09
  annotations:
    cloud.google.com/load-balancer-type: 'External'
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  type: LoadBalancer
  selector:
    app: nginx
```

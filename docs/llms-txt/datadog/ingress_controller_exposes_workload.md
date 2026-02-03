# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/ingress_controller_exposes_workload.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/ingress_controller_exposes_workload.md

---
title: Ingress controller exposes workload
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Ingress controller exposes workload
---

# Ingress controller exposes workload

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `69bbc5e3-0818-4150-89cc-1e989b48f23b`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)

### Description{% #description %}

Ingress controllers should not expose workloads, as this can create vulnerabilities and enable denial-of-service (DoS) attacks. This rule detects Ingress entries that route traffic to Services whose ports map directly to pod targetPorts, indicating direct exposure of workload ports. When such mappings are found, the rule flags the Ingress resource with an IncorrectValue issue identifying the resource and offending backend path.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app
  labels:
    app: app
spec:
  type: ClusterIP
  ports:
  - port: 3000
    targetPort: 3000
  selector:
    app: app


---

apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    kubernetes.io/ingress.class: "nginx"
  labels:
    app: app
spec:
  rules:
  - host: app.acme.org
    http:
      paths:
      - backend:
          serviceName: app2
          servicePort: 3000
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app
  labels:
    app: app
spec:
  type: ClusterIP
  ports:
  - port: 3000
    targetPort: 3000
  selector:
    app: app


---

apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    kubernetes.io/ingress.class: "nginx"
  labels:
    app: app
spec:
  rules:
  - host: app.acme.org
    http:
      paths:
      - backend:
          serviceName: app
          servicePort: 3000
```

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/cluster_allows_unsafe_sysctls.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/cluster_allows_unsafe_sysctls.md

---
title: Cluster allows unsafe sysctls
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cluster allows unsafe sysctls
---

# Cluster allows unsafe sysctls

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9127f0d9-2310-42e7-866f-5fd9d20dcbad`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/)

### Description{% #description %}

A Kubernetes cluster must not allow unsafe sysctls. Allowing unsafe sysctls can let a Pod influence other Pods, harm node stability, or consume CPU or memory beyond resource limits. `spec.securityContext.sysctls` must not include unsafe sysctls, and `allowedUnsafeSysctls` must be undefined. This rule detects PodSecurityPolicy resources where `allowedUnsafeSysctls` is defined and flags any `spec.securityContext.sysctls` entries that are not in the defined safe list. Only a limited set of sysctls are considered safe; all others are treated as unsafe and should not be used.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
apiVersion: v1
kind: Pod
metadata:
  name: sysctl-example
spec:
  securityContext:
    sysctls:
    - name: kernel.shm_rmid_forced
      value: "0"
    - name: net.ipv4.ip_local_port_range
      value: "0"
  containers:
    - name: test1
      image: nginx
---
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: sysctl-psp
spec:
  forbiddenSysctls:
  - kernel.shm_rmid_forced
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  runAsUser:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-app-neg
  labels:
    app: test-app-neg
spec:
  selector:
    matchLabels:
      app: test-app-neg
  template:
    metadata:
      labels:
        app: test-app-neg
    spec:
      securityContext:
        sysctls:
        - name: kernel.shm_rmid_forced
          value: "0"
        - name: net/ipv4/tcp_syncookies
          value: "1"
      containers:
      - name: test-ubuntu
        image: ubuntu
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-app
  labels:
    app: test-app
spec:
  selector:
    matchLabels:
      app: test-app
  template:
    metadata:
      labels:
        app: test-app
    spec:
      securityContext:
        sysctls:
        - name: kernel.sem
          value: "128 32768 128 4096"
      containers:
      - name: test-ubuntu
        image: ubuntu
```

```yaml
#this is a problematic code where the query should report a result(s)
apiVersion: v1
kind: Pod
metadata:
  name: sysctl-example
spec:
  securityContext:
    sysctls:
    - name: kernel.shm_rmid_forced
      value: "0"
    - name: net.core.somaxconn
      value: "1024"
    - name: kernel.msgmax
      value: "65536"
  containers:
    - name: test1
      image: nginx
---
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: sysctl-psp
spec:
  allowedUnsafeSysctls:
  - kernel.msg*
  forbiddenSysctls:
  - kernel.shm_rmid_forced
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  runAsUser:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
```

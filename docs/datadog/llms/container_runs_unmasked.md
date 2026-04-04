# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/container_runs_unmasked.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/container_runs_unmasked.md

---
title: Container with unmasked /proc access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Container with unmasked /proc access
---

# Container with unmasked /proc access

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f922827f-aab6-447c-832a-e1ff63312bd3`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#allowedprocmounttypes)

### Description{% #description %}

Containers should not have full (unmasked) access to the host's `/proc` filesystem, as this can expose sensitive information and allow kernel parameter changes. A PodSecurityPolicy's `spec.allowedProcMountTypes` must not include the value "Unmasked" and should include "Default" to restrict proc mount behavior. Allowing "Unmasked" increases the risk of information disclosure and potential host compromise.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  annotations:
    kubernetes.io/description: 'restricted psp for all standard use-cases'
    seccomp.security.alpha.kubernetes.io/allowedProfileNames: docker/default
    seccomp.security.alpha.kubernetes.io/defaultProfileName: docker/default
  name: restricted
spec:
  allowPrivilegeEscalation: false                   # Disallow privilege escalation to any special capabilities
  allowedProcMountTypes:
    - Default                                       # Disallow full /proc mounts, only allow the "default" masked /proc
  fsGroup:                                          # disallow root fsGroups for volume mounts
    rule: MustRunAs
    ranges:
      - max: 65535
        min: 1
  hostIPC: false                                    # disallow sharing the host IPC namespace
  hostNetwork: false                                # disallow host networking
  hostPID: false                                    # disallow sharing the host process ID namespace
  hostPorts:                                        # disallow low host ports (this seems to only apply to eth0 on EKS)
    - max: 65535
      min: 1025
  privileged: false                                 # disallow privileged pods
  readOnlyRootFilesystem: true                      # change default from 'false' to 'true'
  requiredDropCapabilities:                         # Drop all privileges in the Linux kernel
    - AUDIT_CONTROL
    - CHOWN
  runAsGroup:                                       # disallow GID 0 for pods (block root group)
    rule: MustRunAs
    ranges:
      - max: 65535
        min: 1
  runAsUser:                                        # disallow UID 0 for pods
    rule: MustRunAsNonRoot
  seLinux:                                          # Harness for SELinux
    rule: RunAsAny
  supplementalGroups:                               # restrict supplemental GIDs to be non-zero (non-root)
    rule: MustRunAs
    ranges:
    - max: 65535
      min: 1
  volumes:                                          # allow only these volume types
  - configMap
  - downwardAPI
  - emptyDir
  - projected
  - secret
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
#this is a problematic code where the query should report a result(s)
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  annotations:
    kubernetes.io/description: 'restricted psp for all standard use-cases'
    seccomp.security.alpha.kubernetes.io/allowedProfileNames: docker/default
    seccomp.security.alpha.kubernetes.io/defaultProfileName: docker/default
  name: restricted
spec:
  allowPrivilegeEscalation: false                   # Disallow privilege escalation to any special capabilities
  allowedProcMountTypes:
    - Unmasked
  fsGroup:                                          # disallow root fsGroups for volume mounts
    rule: MustRunAs
    ranges:
      - max: 65535
        min: 1
  hostIPC: false                                    # disallow sharing the host IPC namespace
  hostNetwork: false                                # disallow host networking
  hostPID: false                                    # disallow sharing the host process ID namespace
  hostPorts:                                        # disallow low host ports (this seems to only apply to eth0 on EKS)
    - max: 65535
      min: 1025
  privileged: false                                 # disallow privileged pods
  readOnlyRootFilesystem: true                      # change default from 'false' to 'true'
  requiredDropCapabilities:                         # Drop all privileges in the Linux kernel
    - AUDIT_CONTROL
    - CHOWN
  runAsGroup:                                       # disallow GID 0 for pods (block root group)
    rule: MustRunAs
    ranges:
      - max: 65535
        min: 1
  runAsUser:                                        # disallow UID 0 for pods
    rule: MustRunAsNonRoot
  seLinux:                                          # Harness for SELinux
    rule: RunAsAny
  supplementalGroups:                               # restrict supplemental GIDs to be non-zero (non-root)
    rule: MustRunAs
    ranges:
    - max: 65535
      min: 1
  volumes:                                          # allow only these volume types
  - configMap
  - downwardAPI
  - emptyDir
  - projected
  - secret
```

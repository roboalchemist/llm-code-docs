# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/tls_connection_certificate_not_setup.md

---
title: TLS connection certificate not set up
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > TLS connection certificate not set up
---

# TLS connection certificate not set up

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `fa750c81-93c2-4fab-9c6d-d3fd3ce3b89f`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/)

### Description{% #description %}

TLS certificate files for TLS connections should be set.

For API server containers, the rule verifies that the `--tls-cert-file` and `--tls-private-key-file` flags are included in their command. For `KubeletConfiguration` documents, the rule verifies that the `tlsCertFile` and `tlsPrivateKeyFile` fields are present. If any of these are absent, the rule reports a MissingAttribute issue with the expected and actual values.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: command-demo
  labels:
    purpose: demonstrate-command
spec:
  containers:
    - name: command-demo-container
      image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
      command: ["kube-apiserver"]
      args: ["--tls-cert-file=someFile.txt","--tls-private-key-file=someFile.txt"]
  restartPolicy: OnFailure
```

```json
{
  "kind": "KubeletConfiguration",
  "apiVersion": "kubelet.config.k8s.io/v1beta1",
  "port": 10250,
  "readOnlyPort": 10255,
  "cgroupDriver": "cgroupfs",
  "hairpinMode": "promiscuous-bridge",
  "serializeImagePulls": false,
  "tlsCertFile": "someFile.txt",
  "tlsPrivateKeyFile": "someFile.txt",
  "featureGates": {
    "RotateKubeletClientCertificate": true,
    "RotateKubeletServerCertificate": true
  }
}
```

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
address: "192.168.0.8"
port: 20250
serializeImagePulls: false
tlsCertFile: "someFile.txt"
tlsPrivateKeyFile: "someFile.txt"
evictionHard:
    memory.available:  "200Mi"
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
address: "192.168.0.8"
port: 20250
serializeImagePulls: false
evictionHard:
    memory.available:  "200Mi"
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: command-demo
  labels:
    purpose: demonstrate-command
spec:
  containers:
    - name: command-demo-container
      image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
      command: ["kube-apiserver"]
      args: []
  restartPolicy: OnFailure
```

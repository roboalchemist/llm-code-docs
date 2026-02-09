# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/using_kubernetes_native_secret_management.md

---
title: Using Kubernetes native secret management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Using Kubernetes native secret management
---

# Using Kubernetes native secret management

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b9c83569-459b-4110-8f79-6305aa33cb37`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/configuration/secret/)

### Description{% #description %}

Use of an external secret storage and management system should be considered for complex secret management needs, instead of using Kubernetes Secrets directly. In Kubernetes clusters, prefer solutions that integrate external stores via SecretProviderClass (CSI) or external secret operators rather than embedding secrets in resource manifests. Additionally, apply least-privilege access, enable encryption at rest, and enforce rotation and auditing of secret material.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: azure-kvname
  namespace: myNameSpace
spec:
  provider: azure
  parameters:
    usePodIdentity: "true"              
    keyvaultName: "<key Vault Name>"               
    objects:  |
      array:
        - |
          objectName: secret1          
          objectType: secret                                      
        - |
          objectName: key1               
          objectType: key
    tenantId: "<tenant ID which the Key Vault sits under"            
  secretObjects:                             
  - secretName: appsecrets   
    data:
    - key: secret1                          
      objectName: secret1                                        
    type: Opaque  
```

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cluster-secrets
data:
  # Fill with your encoded base64 CA
  certificate-authority-data: Cg==
stringData:
  # Fill with your string Token
  bearerToken: "my-token"
---
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: azure-kvname
  namespace: myNameSpace
spec:
  provider: azure
  parameters:
    usePodIdentity: "true"              
    keyvaultName: "<key Vault Name>"               
    objects:  
      array:
        - {objectName: secret1, objectType: secret}
        - {objectName: key1 , objectType: key}                                      
    tenantId: "<tenant ID which the Key Vault sits under"            
  secretObjects:                             
  - secretName: appsecrets   
    data:
    - key: secret1                          
      objectName: secret1                                        
    type: Opaque  
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cluster-secrets
data:
  # Fill with your encoded base64 CA
  certificate-authority-data: Cg==
stringData:
  # Fill with your string Token
  bearerToken: "my-token"
```

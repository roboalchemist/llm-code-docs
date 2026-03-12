# Source: https://docs.gitguardian.com/self-hosting/installation/fluxcd.md

# Install using Flux CD

> Install GitGuardian self-hosted on an existing Kubernetes cluster using Flux CD for GitOps-based deployment.

## Introduction

Using the GitGuardian Helm repository, you can easily install GitGuardian on your existing Kubernetes cluster with [Flux CD](https://fluxcd.io/).

:::caution Requirements
Before starting the installation, ensure to review the **[system](../system-requirements)** and **[network](../network-requirements)** requirements.
:::

## Add the GitGuardian Helm repository

First, you need to add the GitGuardian Helm repository to Flux CD using the following command:

```shell
flux create source helm gitguardian \
    --url=oci://registry.replicated.com/gitguardian/gitguardian \
    --username=<your.name@yourcompany.com> \
    --password=<your.password>
```

The GitGuardian team will provide you the username and the password.

## Configure the GitGuardian Application

You can configure the GitGuardian application by providing custom Helm values, follow the [Helm instructions](./installation-existing-cluster-helm) to proceed.

We highly recommend managing secrets on your own and referencing them via `existingSecret` Helm parameters (See [Helm Secrets Management](./helm-secrets#existing-secret) page).

## Install the GitGuardian Application

You can define a Helm release to install the GitGuardian application using Flux CD by applying the following manifest:

```yaml
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: gitguardian
spec:
  interval: 10m
  install:
    timeout: 30m
  upgrade:
    timeout: 30m
  chart:
    spec:
      chart: gitguardian
      version: 2025.x.y
      sourceRef:
        kind: HelmRepository
        name: gitguardian
      interval: 10m
  values:
    <include the GitGuardian values configured in the previous step>
```

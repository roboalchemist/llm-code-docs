# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/ingress-routes-legacy.md

# Ingress routes (legacy)

> [Deprecated] Legacy experimental ingress routes configuration for GitGuardian self-hosted Helm installations.

:::warning
Ingress routes are a legacy experimental feature that is no longer recommended. Please use the standard **[nginx-based ingress configuration](./ingress)** instead.
:::

:::info
This page only concerns installation on an existing cluster using **[Helm](/self-hosting/installation/installation-existing-cluster-helm)**.
:::

## Overview

We redesigned how we access the cluster using Ingress to get rid of our all-in-one nginx container. This option works for a limited number of Ingress Controller: ingress-nginx, traefik, contour, aws_alb, openshift, istio. Activation is optional and disabled by default.

![Ingress routes](/img/self-hosting/management/infrastructure-management/new_ingress_routes.png)

## Activation

To activate Ingress routes, update the `values.yaml`:

```yaml
experimental:
  # -- Use new Ingress routes instead of legacy nginx
  ingressRoutes: true
```

If you notice any unwanted behavior, please let us know and switch back to `ingressRoutes: false`.

## Ingress-NGINX Configuration

If you are using `Ingress-NGINX` as your ingress controller, by default, it blocks custom directive injection via annotations.

To allow GitGuardian to configure `Ingress-NGINX` using the `nginx.ingress.kubernetes.io/configuration-snippet` annotation, you must explicitly enable snippets in your deployment configuration.

Here is an example of the necessary configuration to add to the `Ingress-NGINX` Helm chart values:

```yaml
controller:
  allowSnippetAnnotations: true
  config:
    # configuration-snippet annotation is considered "Critical"
    annotations-risk-level: "Critical"
```

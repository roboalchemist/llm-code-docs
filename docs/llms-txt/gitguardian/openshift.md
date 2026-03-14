# Source: https://docs.gitguardian.com/self-hosting/installation/openshift.md

# Install using OpenShift

> Install GitGuardian self-hosted on OpenShift 4 clusters, including security context and route configuration.

GitGuardian has been tested with OpenShift 4.

Several requirements specific to OpenShift are required for installing GitGuardian application on OpenShift clusters.

## Deactivate securityContext

GitGuardian Self-Hosted enforces `securityContext` directives by default. These settings can conflict with the `securityContext` requirements for some OpenShift security context constraints (SCCs) and must therefore be disabled.

:::tip Security note
Disabling our default `securityContext` does not mean a `securityContext` will not be set--it just means the SCC is responsible for setting the `securityContext`.
:::

With Helm, the `securityContext` must be disabled in the values:

```yaml
securityContext:
  enabled: false

loki-minio:
  podSecurityContext:
    enabled: false
  containerSecurityContext:
    enabled: false

loki:
  loki:
    podSecurityContext:
      fsGroup: null
      runAsGroup: null
      runAsUser: null

ggscout:
  securityContext:
    enabled: false
```

## Use OpenShift Route instead of Ingress

OpenShift proposes `Route` instead of regular Kubernetes `Ingress`. Helm installations do not enable Ingress by default.

The `Route` can be defined as:

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: gitguardian-helm
spec:
  host: <INSTANCE FQDN>
  path: /
  port:
    targetPort: http
  tls:
    certificate: |
      <CERTIFICATE FULLCHAIN>
    insecureEdgeTerminationPolicy: Redirect
    key: |
      <CERTIFICATE PRIVKEY>
    termination: edge
  to:
    kind: Service
    name: nginx
    weight: 100
  wildcardPolicy: None
```

Where:

- `<INSTANCE FQDN>` is the full qualified domain name of your instance
- `<CERTIFICATE FULLCHAIN>` is the TLS Certificate
- `<CERTIFICATE PRIVKEY>` is the TLS Certificate's private key

Note that if your GitGuardian instance has been created before October 2023, the service name is called `gitguardian` instead of `nginx`

## Handle resource quotas per Project

When setting resource quotas per Project, it's essential to ensure that the quotas are sufficient for all your pods. With Helm installations, all resource requests and limits, including those for ephemeral storage, can be fully configured. Refer to our [Scaling GitGuardian](../management/infrastructure-management/scaling#additional-tuning-ephemeral-storage) page for more details.

:::tip Ephemeral Storage
Ephemeral Storage is used to clone repositories during Historical Scans. Ensure that your `scanner` pods are allocated sufficient space to handle the largest repositories.
:::

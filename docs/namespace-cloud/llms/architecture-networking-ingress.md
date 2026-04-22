<!-- Source: https://namespace.so/docs/architecture/networking/ingress -->

# Ingress

Namespace instances can create ingresses exposing container ports.
Ingresses preserve original headers for application-level routing and support path-based and header-based
routing within your application.

## Managed TLS Certificates

All ingresses use managed TLS certificates.
Namespace's ingress manager automatically provisions and rotates TLS certificates ensuring secure connections with zero-downtime renewals.
In case of wildcard previews, all subdomains receive a valid TLS certificate.

### Custom Domain Support

Custom ingress domain support enables white-label preview environments with your organization's branding and domain structure.
Through customizing the domain used for your ingresses, you can ensure brand consistency across development and production environments.

Registering a custom ingress domain is limited to enterprise customers.

## Access Controls

By default, any member of your workspace has access to any ingress.
Namespace ensures high security standards and comprehensive access control mechanisms
to help you manage who can access your workspace and what actions they can perform.

[More information on Workspace access](/docs/workspaces/access)

### Unauthenticated Access

When creating an ingress, you can permit unauthenticated access for it.
This can be useful to simplify end-to-end test setups, especially if not all parts of your testing pipeline run on Namespace.
To learn how to allow unauthenticated ingress access, check out the [reference documentation](/docs/reference/cli/expose).

### Custom Authentication Providers

Apart from workspace-level access controls, Namespace also supports custom authentication providers allowing you to maintain full control over who is supposed to access which ingress.
This option is beneficial if you want to grant ingress access to people outside your workspace, without disabling ingress authentication entirely.

Registering a custom authentication provider is limited to enterprise customers.

### Programmatic Access

When accessing authenticated ingresses exposed on Namespace from a browser, Namespace automatically performs an authorization flow.
In order to access an ingress endpoint programmatically, add the `x-nsc-ingress-auth` HTTP header. The content should be a bearer token containing an [ingress access token](/docs/reference/cli/ingress-generate-access-token).

## API Reference

Ingresses can be managed programmatically via the [ComputeService API](https://buf.build/namespace/cloud/docs/main:namespace.cloud.compute.v1beta):

- **`CreateIngress`**: Expose a backend port from a running instance to the public internet.
  Each ingress has a `name`, an `exported_port_backend` (the port number), and optional `http_match_rule`s
  to configure path-based routing and authentication requirements.
- **`ListIngresses`**: Returns all active ingresses for an instance, including those created via
  `CreateIngress` and those declaratively exposed via the Kubernetes ingress manager.

### Protocols

When creating container-level ingresses via `ContainerPort`, two protocols are supported:

- **HTTP**: The platform exposes the port using an HTTPS-terminating reverse proxy that communicates
  with the container over plain HTTP.
- **TCP**: The platform exposes the port using TLS passthrough, requiring a Namespace-issued
  certificate for authentication.

### Wildcard Domains

Instances can be configured with a wildcard domain by setting `enable_wildcard_domain` at creation
time. When enabled, ingresses can set `wildcard: true` to route all first-level subdomains to
that ingress.

Last updated March 20, 2026

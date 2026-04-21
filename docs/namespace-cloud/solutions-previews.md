<!-- Source: https://namespace.so/docs/solutions/previews -->

# Container Previews

Deploy container image previews with enterprise-grade security and performance.
Namespace's Previews enable development teams to test applications in isolated, ephemeral environments accessible to the whole team enabling quick feedback cycles.

## Why Namespace Previews?

[Seamless collaboration share your previews with your team](/docs/workspaces/access)

[Easy to debug via container logs, metrics, and OOM detection](/docs/solutions/previews#monitoring-and-debugging)

[Authenticated access URLs with automatic TLS management](/docs/architecture/networking/ingress)

[Available in seconds scales up to 32 vCPUs and 512GB RAM](/docs/architecture/compute/machine-shapes)

[Flexible, competitive pricing custom plans available for larger customers](/docs/workspaces/billing-and-limits)

[Enterprise ready SAML SSO, managed partner domains, audit logs and SLAs](/docs/workspaces/access)

## Getting Started

#### Ensure access to Namespace

Using the [CLI](/docs/reference/cli/installation), log into your workspace.
If you're accessing Namespace from a cloud provider or your CI platform, we recommend to set up [workflow federation](/docs/federation) instead.

```
$ nsc login
```

#### Start your preview

```
$ nsc run --image nginx -p 80
# Prints a preview URL, e.g.: https://4bi2reg-grijlvs6ciapa.ord2.namespaced.app
```

#### Done!

Your preview is now available. All requests to the exposed URL require authentication.

## How it works

Namespace preview clusters build on [Namespace Compute](/docs/architecture/compute) to deliver interactive access to a flexible, isolated test environment.
Any public images, or any image present in your [private container registry](/docs/architecture/storage/container-registry) can seamlessly run in a preview.
Namespace generates public, authenticated ingress URLs using managed TLS certificates, whether you use a Namespace-provided app domain, or employ [custom domain configurations](/docs/architecture/networking/ingress#custom-domain).

![Preview Access](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Faccess.291b4187.png&w=828&q=75)

Namespace ingresses preserve original headers for application-level routing and support path-based and header-based
routing within your application.

### Monitoring and Debugging

By building on [Namespace Compute](/docs/architecture/compute), you directly benefit from its comprehensive observability features providing deep insights into preview environment performance and behavior.

- **Real-time Logging** Access centralized logs from all pods, from the CLI or the [Dashboard](https://cloud.namespace.so).
- **Performance Monitoring** Track resource utilization and network performance.

![Preview Summary](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcontainersummary.4a9e80cd.png&w=1200&q=75)

Namespace also grants root [SSH access](/docs/architecture/compute/ssh-remote-display#ssh-access) to each instance, allowing you to inspect the underlying infrastructure powering the preview.

![Terminal access](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcontainerterminal.c335f0e9.png&w=1200&q=75)

## Wildcard Ingresses

For complex applications requiring multiple endpoints or dynamic routing, Namespace supports wildcard ingress configurations.
Wildcard ingresses excel in scenarios requiring microservice architectures with dynamic service discovery and when testing API gateways managing multiple backend services.

#### Enable wildcard support

Create an instance with wildcard ingress capability.

```
$

```
nsc create --ingress wildcard
```
```

This outputs the ID of the created cluster, e.g.: 072higp5dg0bg

#### Start your application

Connect your local Docker to the remote preview environment.

```
$

```
nsc docker attach-context --to 072higp5dg0bg --use
```
```

Using your existing tooling, you can now run your application in the preview.

```
$

```
docker run --name nginx-foobar -p 80:80 -d nginx
```
```

#### Configure a wildcard ingress

```
$

```
nsc expose container 072higp5dg0bg --wildcard --container nginx-foobar --container_port 80
```
```

After creating a wildcard ingress, all subdomain traffic is routed to your specified service:

`*.<instance-id>.<region>.namespaced.app`

Last updated September 17, 2025

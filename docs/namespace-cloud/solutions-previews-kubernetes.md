<!-- Source: https://namespace.so/docs/solutions/previews/kubernetes -->

# Kubernetes Previews

Deploy Kubernetes previews with enterprise-grade security and performance.
Namespace's Kubernetes Previews enable development teams to test applications in isolated, ephemeral clusters that mirror production environments, accelerating feature development while maintaining operational standards.

## Why Namespace Previews?

[Production-equivalent testing using your existing Kubernetes configuration](/docs/solutions/previews/kubernetes#getting-started)

[Easy to debug via container logs, metrics, and OOM detection](/docs/solutions/previews/kubernetes#monitoring-and-debugging)

[Authenticated access URLs with automatic TLS management](/docs/architecture/networking/ingress)

[Available in seconds scales up to 32 vCPUs and 512GB RAM](/docs/architecture/compute/machine-shapes)

[Flexible, competitive pricing custom plans available for larger customers](/docs/workspaces/billing-and-limits)

[Enterprise ready SAML SSO, managed partner domains, audit logs and SLAs](/docs/workspaces/access)

## Getting Started

#### Create a preview cluster

1. Using the [CLI](/docs/reference/cli/installation), log into your workspace.
   If you're accessing Namespace from a cloud provider or your CI platform, we recommend to set up [workflow federation](/docs/federation) instead.

   ```
   $

   ```
   nsc login
   ```
   ```
2. Create a Kubernetes cluster to host your preview.

   ```
   $ nsc create
   # Outputs the ID of the created cluster, e.g.: 072higp5dg0bg
   ```

#### Apply your Kubernetes configuration

1. Point your local `kubectl` to the preview cluster.

   ```
   $ nsc kubeconfig write 072higp5dg0bg --output_to /path/kubeconfig.yaml
   $ export KUBECONFIG=/path/kubeconfig.yaml
   ```
2. Deploy your application to the preview.

   ```
   $

   ```
   kubectl run nginx --image=nginx
   ```
   ```

#### Expose your application

1. Expose a service of type LoadBalancer to wire access to your application.

   ```
   $

   ```
   kubectl expose pod nginx --type=LoadBalancer --port=80
   ```
   ```
2. Expose your service with Namespace.

   ```
   $ nsc expose kubernetes 072higp5dg0bg --service=nginx --name=nginx-foobar \
      --namespace=default
   Exported port 80 from default/nginx:
   https://nginx-foobar-072higp5dg0bg.ord2.namespaced.app
   ```

## How it works

Namespace preview clusters build on [Namespace Compute](/docs/architecture/compute) to deliver interactive access to a flexible, isolated test environment.
When creating an instance, Namespace provisions a ready-to-use Kubernetes cluster in it and provides seamless access to the Kubernetes API.
You can deploy and expose your applications using your existing tooling.
Namespace will generate public, authenticated ingress URLs using managed TLS certificates, whether you use a Namespace-provided app domain, or employ [custom domain configurations](/docs/architecture/networking/ingress#custom-domain).

![Preview Access](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Faccess.291b4187.png&w=828&q=75)

Namespace ingresses preserve original headers for application-level routing and support path-based and header-based
routing within your application.

### Kubernetes API access

Namespace previews provide full access to the Kubernetes API under test.

To configure your local `kubectl` client to access the remote test environment, use our [CLI](/docs/reference/cli/installation) to produce and apply a kubeconfig.

```
$ nsc kubeconfig write <instance-id>
# Outputs the path of the produced kubeconfig, e.g.: /path/kubeconfig.yaml
$ export KUBECONFIG=/path/kubeconfig.yaml
```

To access the Kubernetes API without reconfiguring your local client, use the inline `kubectl` integration:

```
$

```
nsc kubectl <instance-id> get pods,services
```
```

### Monitoring and Debugging

By building on [Namespace Compute](/docs/architecture/compute), you directly benefit from its comprehensive observability features providing deep insights into preview environment performance and behavior.

- **Real-time Logging** Access centralized logs from all pods, from the CLI or the [Dashboard](https://cloud.namespace.so).
- **Performance Monitoring** Track resource utilization and network performance.

![Preview Summary](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fkubesummary.072af8f2.png&w=1200&q=75)

In case Kubernetes API access is not sufficient, Namespace also grants root [SSH access](/docs/architecture/compute/ssh-remote-display#ssh-access) to each instance, allowing you to inspect the underlying infrastructure powering the preview.

![Terminal access](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fwebterminal.2c3ff973.png&w=1200&q=75)

## Wildcard Ingresses

For complex applications requiring multiple endpoints or dynamic routing, Namespace supports wildcard ingress configurations.
Wildcard ingresses excel in scenarios requiring microservice architectures with dynamic service discovery and when testing API gateways managing multiple backend services.

#### Enable wildcard support

Create a cluster with wildcard ingress capability.

```
$

```
nsc create --ingress wildcard
```
```

This outputs the ID of the created cluster, e.g.: 072higp5dg0bg

#### Deploy and expose your applications

```
$ nsc kubectl 072higp5dg0bg create deployment app --image=myapp:latest
$ nsc kubectl 072higp5dg0bg expose deployment app --type=LoadBalancer --port=80
```

#### Configure a wildcard ingress

```
$ nsc expose kubernetes 072higp5dg0bg --service app --wildcard --port=80 \
    --namespace=default
```

After creating a wildcard ingress, all subdomain traffic is routed to your specified service:

`*.<instance-id>.<region>.namespaced.app`

## Automatic Previews

Namespace's Kubernetes Ingress Manager automates preview creation through service annotations, eliminating manual exposure commands and integrating preview generation directly into your deployment pipeline.

#### Enable the ingress manager

Create a preview cluster, enable the ingress manager and point your local `kubectl` to it.

```
$ nsc create --features EXP_KUBERNETES_INGRESS_MANAGER
# Outputs the ID of the created cluster, e.g.: dr9flh12238uk
$ nsc kubeconfig write dr9flh12238uk --output_to /path/kubeconfig.yaml
$ export KUBECONFIG=/path/kubeconfig.yaml
```

#### Annotation-based service exposure

Control preview generation through Kubernetes service annotations:

```
apiVersion: v1
kind: Service
metadata:
  name: frontend
  annotations:
    kubernetes.namespace.so/expose: "true"
    kubernetes.namespace.so/exposed-port-80: "ingress-name=my-app"
spec:
  selector:
    app: frontend
  ports:
    - port: 80
      targetPort: 8080
  type: LoadBalancer
```

#### Verify the exposed ingress

```
$ nsc ingress list dr9flh12238uk
https://my-app-80-dr9flh12238uk.ord2.namespaced.app (port: 80; default/frontend)
```

### Annotation Reference

| Annotation key | Valid values |
| --- | --- |
| **kubernetes.namespace.so/expose** Enable automatic preview generation. | Either `true` or `false`. |
| **kubernetes.namespace.so/exposed-port-<port>** Configure ingress options for specific port. | Comma-separated list using the following option:  - `ingress-name=<selected-name>` - `wildcard` - `noauth` |

## Autoscaling Clusters

Namespace Kubernetes Previews can scale cluster resources based on workload demands, ensuring optimal performance while controlling costs.
Horizontal cluster scaling is performed automatically through a workspace-private network (VPC) as an increase in required resources is detected.  
**Note:** Automatic cluster scaling is not enabled by default. Contact our [support](mailto:support@namespace.so) to get enrolled.

Last updated September 17, 2025

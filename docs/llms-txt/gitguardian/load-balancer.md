# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/load-balancer.md

# Load balancer

> Configure load balancer access for GitGuardian self-hosted installations on existing Kubernetes clusters.

## Existing clusters (Helm-based or KOTS-based)

:::info
This section only concerns installation on an existing cluster using **[KOTS](/self-hosting/installation/installation-existing-cluster-kots)** or **[Helm](/self-hosting/installation/installation-existing-cluster-helm)**.
:::

### Helm-based installation

The Kubernetes cluster must include a LoadBalancer controller add-on (for AWS, this would be an ALB), which is not provided by our Helm charts. This setup is an alternative to using Ingress, which is not activated by default in the On-Prem values. Customers need to override these values to access the dashboard via a LoadBalancer.

Switch the frontend serviceType from `ClusterIP` to `LoadBalancer` in your `local-values.yaml` file:

```yaml
front:
  service:
    type: LoadBalancer
    annotations:
      # example when using an ELB on AWS
      service.beta.kubernetes.io/aws-load-balancer-backend-protocol: http
      service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:iam::12345678
```

### KOTS-based installation

For existing clusters, the Service type can be changed from ClusterIP to LoadBalancer. This allows for the creation of a dedicated cloud load balancer (e.g., an AWS Application Load Balancer) specifically for the GitGuardian dashboard.

Note: This modification does not impact the KOTS Admin Console, which remains accessible only through port forwarding, unless manually configured otherwise.

#### Annotations

Annotations enable service customization. For example, on AWS, you can add the following annotations in the KOTS Admin Console's annotations section:

```
service.beta.kubernetes.io/aws-load-balancer-backend-protocol: http
service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:iam::12345678
```

You can add those in the annotations section of the [KOTS Admin Console](./admin-console).

![Loadbalancer annotations](/img/self-hosting/management/infrastructure-management/replicated_loadbalancer_service.png)

## Embedded clusters

### Configure your instance to work behind a load balancer

In case you plan to expose your embedded cluster behind a load balancer (allowing your cluster to run in private network), you may need to configure additional settings.

The GitGuardian dashboard on an Embedded cluster installation is, by default, exposed using an HTTPs configuration that requires [SNI TLS extension](https://en.wikipedia.org/wiki/Server_Name_Indication). Unfortunately, some load balancers (such as AWS ones) are not able to deal with SNI enforced backends.

In KOTS, check the parameter `Use NodePort Service` and choose to expose a port (for example `8080`).

Then:

- On the instance firewall/security group, allow connection from the load balancer to instance port `8080`.
- On the load balancer:
  - Configure certificate(s) to terminate the TLS connection. Endpoint should match the hostname you use in the configuration.
  - Target the instance on port `8080`.
  - For instance health checks, you can target the `/health` endpoint.

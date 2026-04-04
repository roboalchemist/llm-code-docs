# Source: https://uptrace.dev/raw/get/hosted/k8s.md

# Deploying Uptrace on Kubernetes

> Deploy Uptrace on Kubernetes via the Helm chart, provision dependencies, and manage namespaces plus upgrades with kubectl.

This comprehensive guide walks you through deploying Uptrace, an open-source APM and observability platform, on Kubernetes using Helm charts. Uptrace supports distributed tracing, metrics, and log management to help you monitor your applications effectively.

## Prerequisites

### Kubernetes Cluster

You'll need a running Kubernetes cluster. For local development and testing, you can create one using:

- **K3s** - Lightweight Kubernetes distribution
- **Kind** - Kubernetes in Docker
- **Minikube** - Local Kubernetes cluster

### Required Tools

- **kubectl** - Kubernetes command-line tool
- **Helm** - Kubernetes package manager

## Understanding Helm

Helm is a package manager for Kubernetes, similar to `apt` or `yum` for Linux systems, but specifically designed for deploying and managing applications on Kubernetes clusters.

A **Helm chart** is a packaged Kubernetes application containing all necessary resources (YAML manifests) and configurations needed to deploy an application on Kubernetes.

The Uptrace Helm chart includes the Uptrace application and all required dependencies:

- Redis (for caching)
- PostgreSQL (for metadata storage)
- ClickHouse (for observability data)
- OpenTelemetry Collector (for metrics collection)

## Initial Setup

### Add Uptrace Helm Repository

First, add the Uptrace Helm repository to your local Helm installation:

```shell
helm repo add uptrace https://charts.uptrace.dev --force-update
```

### Create Monitoring Namespace

Create a dedicated namespace for Uptrace and its dependencies. This provides logical separation and makes resource management easier:

```shell
kubectl create namespace monitoring
```

**Note**: You can delete all resources created in this guide by removing the namespace:

```shell
kubectl delete namespace monitoring
```

## Configuration Management

### Understanding values.yaml Files

Helm uses `values.yaml` files to customize chart deployments without modifying the original templates. These files act as a central configuration point for defining variables that populate Helm template placeholders.

### View Default Configuration

To see all available configuration options for the Uptrace chart:

```shell
helm show values uptrace/uptrace --devel
```

### Get Sample Configuration Files

For complete configuration examples, clone the Uptrace Helm charts repository:

```shell
git clone https://github.com/uptrace/helm-charts.git
cd helm-charts
cat uptrace-values.yml
```

This repository contains sample `*-values.yaml` files for all components.

## Dependency Setup

### Redis Configuration

Uptrace uses Redis for in-memory caching. Since caching data is ephemeral, no persistent storage is required. A Redis instance with 32MB of free RAM is sufficient.

#### Installing Redis

If you don't have an existing Redis server, install one using the Bitnami chart:

```shell
helm install redis oci://registry-1.docker.io/bitnamicharts/redis \
  -f redis-values.yaml \
  -n monitoring
```

Create a `redis-values.yaml` file with minimal configuration:

```yaml
auth:
  enabled: false
```

For all available Redis parameters, see the [Bitnami Redis chart documentation](https://github.com/bitnami/charts/tree/main/bitnami/redis#parameters).

#### Connecting to Redis

To connect to your Redis instance for testing:

```shell
kubectl port-forward service/redis-master 6379:6379 -n monitoring
redis-cli
```

#### Using Existing Redis

If you have an existing Redis database, configure Uptrace to use it by adding this to your `uptrace-values.yaml`:

```yaml
uptrace:
  config:
    redis_cache:
      addrs:
        alpha: 'redis-master:6379'
```

### PostgreSQL Configuration

Uptrace uses PostgreSQL to store metadata including users, projects, and monitors. The metadata volume is typically small â a 1GB persistent volume should be sufficient.

#### Installing PostgreSQL

Install PostgreSQL using the CloudNativePG operator, which provides enterprise-grade PostgreSQL management:

```shell
# Add the CloudNativePG repository
helm repo add cnpg https://cloudnative-pg.github.io/charts

# Install the PostgreSQL operator
helm upgrade --install cnpg \
  --namespace cnpg-system \
  --create-namespace \
  cnpg/cloudnative-pg
```

Verify the installation:

```shell
kubectl get all -n cnpg-system
```

#### Using Existing PostgreSQL

If you have an existing PostgreSQL database, disable the bundled one and configure your connection details:

```yaml
postgresql:
  enabled: false

uptrace:
  config:
    pg:
      addr: 'your-postgresql-host:5432'
      user: uptrace
      password: your-password
      database: uptrace
```

### ClickHouse Configuration

ClickHouse stores all observability data including spans, logs, events, and metrics. Start with a pod having 4 CPUs, 1GB RAM, and 10GB disk space, then scale vertically as needed.

#### Installing ClickHouse

Install ClickHouse using the Altinity operator:

```shell
kubectl apply -f https://raw.githubusercontent.com/Altinity/clickhouse-operator/master/deploy/operator/clickhouse-operator-install-bundle.yaml
```

Verify the operator is running:

```shell
kubectl get pods -n kube-system | grep clickhouse-operator
```

#### Using Existing ClickHouse

For existing ClickHouse installations, disable the bundled one and configure your cluster details:

```yaml
clickhouse:
  enabled: false

uptrace:
  config:
    ch_cluster:
      cluster: 'your-cluster-name'
      replicated: false
      distributed: false

      shards:
        - replicas:
            - addr: 'your-clickhouse-host:9000'
              database: uptrace
              user: uptrace
              password: your-password
              dial_timeout: 3s
              write_timeout: 5s
              max_retries: 3
              max_execution_time: 15s
              query_settings:
                session_timezone: UTC
                async_insert: 1
                query_cache_nondeterministic_function_handling: 'save'
                allow_suspicious_types_in_group_by: 1
                allow_suspicious_types_in_order_by: 1
```

**Troubleshooting**: If ClickHouse encounters issues in Kubernetes, refer to [this troubleshooting guide](https://altinity.com/blog/fixing-the-dreaded-clickhouse-crash-loop-on-kubernetes).

### OpenTelemetry Collector Setup

The chart uses the OpenTelemetry Operator to deploy collectors that gather pod metrics and other observability data.

#### Install cert-manager

OpenTelemetry Operator requires cert-manager for certificate management:

```shell
helm repo add jetstack https://charts.jetstack.io --force-update
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.17.2 \
  --set crds.enabled=true
```

#### Install OpenTelemetry Operator

```shell
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts --force-update
helm install otel-operator open-telemetry/opentelemetry-operator \
  --set "manager.collectorImage.repository=otel/opentelemetry-collector-k8s" \
  --set "manager.collectorImage.tag=0.123.0" \
  --set admissionWebhooks.certManager.enabled=false \
  --set admissionWebhooks.autoGenerateCert.enabled=true \
  --namespace opentelemetry \
  --create-namespace
```

#### Disable OpenTelemetry Collector (Optional)

If you prefer to manage OpenTelemetry Collector separately, disable it in your `uptrace-values.yaml`:

```yaml
otelcol:
  enabled: false

otelcolDaemonset:
  enabled: false
```

## Installing Uptrace

With all dependencies configured, install Uptrace using your custom values file:

```shell
helm install uptrace uptrace/uptrace \
  -f uptrace-values.yaml \
  -n monitoring \
  --devel
```

### Verify Installation

Check that all resources are running:

```shell
kubectl get all -n monitoring
```

View Uptrace application logs:

```shell
kubectl logs uptrace-0 -n monitoring
```

### Database Connections

Connect to ClickHouse for troubleshooting:

```shell
kubectl port-forward service/chi-uptrace1-uptrace1-0-0 9000:9000 -n monitoring
clickhouse-client
```

## Accessing Uptrace

### Local Access Setup

Uptrace will be available at [http://uptrace.local](http://uptrace.local) with these default credentials:

- **Username**: `admin@uptrace.local`
- **Password**: `admin`

Add the domain to your `/etc/hosts` file:

```text
127.0.0.1 uptrace.local
```

### Platform-Specific Configuration

#### Minikube Setup

Enable the ingress controller:

```shell
minikube addons enable ingress
```

Wait for ingress pods to be ready:

```shell
kubectl get pods -n ingress-nginx
```

Get Minikube's IP address:

```shell
minikube ip
```

Update your `/etc/hosts` file with the Minikube IP:

```text
192.168.49.2 uptrace.local  # Replace with your minikube ip
```

#### AWS EKS Deployment

For external access on AWS EKS using the AWS Load Balancer Controller, add these annotations to your `uptrace-values.yaml`:

```yaml
service:
  type: LoadBalancer
  port: 80
  loadBalancerSourceRanges:
    - '0.0.0.0/0' # Restrict this to your IP ranges for security
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: 'external'
    service.beta.kubernetes.io/aws-load-balancer-nlb-target-type: 'ip'
    service.beta.kubernetes.io/aws-load-balancer-target-group-attributes: 'preserve_client_ip.enabled=true'
    service.beta.kubernetes.io/aws-load-balancer-backend-protocol: 'http'
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-protocol: 'http'
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-port: '80'
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-path: '/'
```

## Scaling and Maintenance

### Horizontal Scaling

Scale Uptrace by increasing replicas in your `uptrace-values.yaml`:

```yaml
uptrace:
  replicaCount: 3 # Increase based on your load requirements
```

Apply the changes:

```shell
helm upgrade uptrace uptrace/uptrace \
  -f uptrace-values.yaml \
  -n monitoring \
  --devel
```

### Upgrading Uptrace

Only upgrades to the next minor version are tested and supported, for example, upgrading from 1.1 to 1.2. Skipping minor versions (e.g., 1.1 to 1.3) is not supported â upgrade one minor version at a time.

To upgrade Uptrace:

1. **Back up your databases.** Create backups of both PostgreSQL and ClickHouse before proceeding.
2. **Update the Helm repository and upgrade the release:**```shell
helm repo update uptrace
helm upgrade uptrace uptrace/uptrace \
  -f uptrace-values.yaml \
  -n monitoring \
  --devel
```

Helm automatically validates the config, runs database migrations, and restarts Uptrace.

### Resource Management

#### Monitor Resource Usage

Keep an eye on resource consumption:

```shell
kubectl top pods -n monitoring
kubectl top nodes
```

#### Adjust Resource Limits

Configure resource requests and limits in your `uptrace-values.yaml`:

```yaml
uptrace:
  resources:
    requests:
      memory: '512Mi'
      cpu: '500m'
    limits:
      memory: '1Gi'
      cpu: '1000m'
```

## Troubleshooting

### Common Issues

1. **Pods not starting**: Check resource availability and node capacity
2. **Database connection errors**: Verify database credentials and network policies
3. **Ingress not working**: Ensure ingress controller is properly installed and configured
4. **Performance issues**: Monitor resource usage and scale components as needed

### Useful Commands

View all resources in the monitoring namespace:

```shell
kubectl get all -n monitoring -o wide
```

Describe problematic pods:

```shell
kubectl describe pod <pod-name> -n monitoring
```

Check events for troubleshooting:

```shell
kubectl get events -n monitoring --sort-by='.lastTimestamp'
```

## Cleanup

### Uninstall Uptrace

Remove the Uptrace release:

```shell
helm uninstall uptrace -n monitoring
```

### Complete Cleanup

Delete the entire monitoring namespace and all resources:

```shell
kubectl delete namespace monitoring
```

### Remove Operators (Optional)

If you installed operators specifically for this deployment:

```shell
# Remove OpenTelemetry Operator
helm uninstall otel-operator -n opentelemetry
kubectl delete namespace opentelemetry

# Remove cert-manager
helm uninstall cert-manager -n cert-manager
kubectl delete namespace cert-manager

# Remove CloudNativePG Operator
helm uninstall cnpg -n cnpg-system
kubectl delete namespace cnpg-system
```

## Alternative Deployment Methods

Kubernetes is one of several deployment options for Uptrace:

- [Docker](/get/hosted/docker) - Quick deployment for development and small-scale production
- [DEB/RPM packages](/get/hosted/install) - Traditional server deployments
- [Ansible](/get/hosted/ansible) - Automated bare metal deployments

Choose the method that best fits your infrastructure and requirements.

## Next Steps

Once Uptrace is running successfully:

1. **Configure Applications**: Set up your applications to send telemetry data to Uptrace
2. **Create Dashboards**: Build custom dashboards for your specific monitoring needs
3. **Set Up Alerts**: Configure alerting rules for critical metrics and traces
4. **Explore Features**: Discover advanced features like distributed tracing visualization and log correlation
5. **Performance Tuning**: Optimize configuration based on your data volume and query patterns

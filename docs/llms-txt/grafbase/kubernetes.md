# Source: https://grafbase.com/docs/gateway/deployment/kubernetes.md

# Deploy to Kubernetes

Deploy the Grafbase Gateway through different options that fit diverse infrastructure needs. Choose from a [multi-platform binary](https://github.com/grafbase/grafbase/releases?q=gateway) for direct installation on various operating systems, or use a [Docker image](https://github.com/grafbase/grafbase/pkgs/container/gateway) that integrates into containerized environments like Kubernetes. This flexibility lets teams deploy the gateway in ways that best fit their workflow on local machines, cloud platforms, or hybrid infrastructures.

## Kubernetes

Kubernetes offers popular container orchestration with wide adoption for its scalability, reliability, and powerful ecosystem. This ecosystem includes tools like Helm, which simplifies the deployment and management of Kubernetes workloads through a templated, versioned, and reusable configuration framework. Use Helm to package applications into charts and streamline complex workload deployments consistently across environments.

### Gateway Helm Chart

Grafbase provides a Helm chart to simplify gateway deployment. The GitHub Container Registry hosts it with [Open Container Initiative (OCI)](https://helm.sh/docs/topics/registries/) compliance. Find the chart and versions at:

```bash
https://ghcr.io/grafbase/helm-charts/gateway
```

## Deploying

The chart includes default installation configuration for quick gateway setup with minimal configuration. While functional and easy to start with, tune this setup to accommodate real use cases.

Follow these steps to install the default configuration and customize settings for:

1. Number of replicas
2. Auto-scaling
3. Compute resources
4. External federated schema
5. External configuration

### Setup

Complete these prerequisites before deploying:

1. _Kubernetes Cluster:_ Get access to a Kubernetes cluster. Set up a local cluster like [kind](https://kind.sigs.k8s.io/) if needed.
2. _helm:_ Install Helm. Get started [here](https://helm.sh/docs/intro/quickstart/).
3. _kubectl:_ Install kubectl and point it to your cluster. Get started [here](https://kubernetes.io/docs/tasks/tools/#kubectl).

### Basic deployment

Start running the gateway with:

```bash
helm install test oci://ghcr.io/grafbase/helm-charts/gateway --version <version>
```

Verify gateway operation:

```bash
kubectl get pods
```

Look for a running pod named `test-gateway`.

### Customize deployment

Use a Helm [values file](https://helm.sh/docs/chart_template_guide/values_files/) to customize your deployment:

```yaml
# 1. number of desired replicas running
replicaCount: 2

# 2. auto-scaling behaviour
autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
  targetMemoryUtilizationPercentage: 70

# 3. compute resources
resources:
  limits:
    cpu: 2
    memory: 2Gi
  requests:
    cpu: 1
    memory: 1Gi

# 4. and 5. External schema and configuration from cluster configmaps
gateway:
  externalConfig: true
  externalSchema: true
  args:
    - --config
    - /etc/grafbase/config/config.toml
    - --graph-ref
    - graph-name@branch
volumes:
  - name: configuration
    configMap:
      name: grafbase-gateway-configuration
volumeMounts:
  - name: configuration
    mountPath: /etc/grafbase/config
```

This configuration:

1. Maintains 2 gateway replicas
2. Sets auto-scaling between 2 and 10 instances, scaling up at 70% CPU or memory usage
3. Allocates 1-2 CPU and 1-2GB memory per replica
4. Uses cluster configmaps for gateway configuration and federated schema, mounting them in specified paths

View all customizable values with:

```bash
helm show values oci://ghcr.io/grafbase/helm-charts/gateway --version <version>
```

To apply customizations:

1. Save your settings to a file
2. Run:

```
helm upgrade test oci://ghcr.io/grafbase/helm-charts/gateway --version <version> -f custom-values.yaml
```

Verify the deployment:

```bash
helm list

kubectl get pods
```

### Providing the schema to your Gateway deployment

There are three ways to pass your federated GraphQL schema to the gateway.

1. With a graph ref

The schema will be downloaded from object storage and regularly polled for new versions. When a new version becomes available, the Gateway hot-reloads with the new schema version.

Graph refs taking the shape of a `graph-name@branch` string, where the branch is optional. So if your graph is called `booking-api`, a graph ref could be just `booking-api`, or with a branch name, `booking-api@main`.

The Graph ref can be passed either as an argument (`--graph-ref`):

```yaml
gateway:
  externalConfig: true
  externalSchema: true
  args:
    - --config
    - /etc/grafbase/config/config.toml
    - --graph-ref
    - graph-name@branch
volumes:
  - name: configuration
    configMap:
      name: grafbase-gateway-configuration
volumeMounts:
  - name: configuration
    mountPath: /etc/grafbase/config
```

or an environment variable (`GRAFBASE_GRAPH_REF`)

```yaml
gateway:
  externalSchema: true
  args:
    - --config
    - /etc/grafbase/config/config.toml
    - --graph-ref
    - graph-name@branch
configmap:
  enabled: true
  values:
    GRAFBASE_GRAPH_REF: graph-name@branch
```

2. Create a Docker image that includes the schema, with the Gateway image as the base.

In your Dockerfile, copy the schema that you previously composed locally (with `grafbase compose`) or downloaded:

```dockerfile
FROM ghcr.io/grafbase/gateway:latest

COPY federated_schema.graphql /etc/grafbase/schema/schema.sdl
```

Then build, tag and push your image, and reference it in `values.yaml`.

```yaml
gateway:
  externalSchema: true
  args:
    - --schema
    - /etc/grafbase/schema/schema.sdl
image:
  repository: ghcr.io/<my-org>/grafbase-gateway-with-schema
  tag: latest
```

3. Using a ConfigMap. This method is deprecated because there is a low size limit on ConfigMaps that can easily be exceeded by large federated GraphQL schemas.

```yaml
gateway:
  externalConfig: true
  externalSchema: true
  args:
    - --config
    - /etc/grafbase/config/config.toml
    - --schema
    - /etc/grafbase/schema/schema.sdl
volumes:
  - name: configuration
    configMap:
      name: grafbase-gateway-configuration
  - name: schema
    configMap:
      name: grafbase-gateway-schema
volumeMounts:
  - name: configuration
    mountPath: /etc/grafbase/config
  - name: schema
    mountPath: /etc/grafbase/schema
```
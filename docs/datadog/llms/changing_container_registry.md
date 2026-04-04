# Source: https://docs.datadoghq.com/containers/guide/changing_container_registry.md

---
title: Changing Your Container Registry
description: >-
  Switch between Datadog container image registries for different deployment
  environments and requirements
breadcrumbs: Docs > Containers > Containers Guides > Changing Your Container Registry
---

# Changing Your Container Registry

Datadog publishes container images in Google's gcr.io, Azure ACR, AWS' ECR, and on Docker Hub:

| datadoghq.azurecr.io                                    | dockerhub.io                               | gcr.io                                              | public.ecr.aws                                            |
| ------------------------------------------------------- | ------------------------------------------ | --------------------------------------------------- | --------------------------------------------------------- |
| datadoghq.azurecr.io/agent                              | datadog/agent                              | gcr.io/datadoghq/agent                              | public.ecr.aws/datadog/agent                              |
| datadoghq.azurecr.io/cluster-agent                      | datadog/cluster-agent                      | gcr.io/datadoghq/cluster-agent                      | public.ecr.aws/datadog/cluster-agent                      |
| datadoghq.azurecr.io/operator                           | datadog/operator                           | gcr.io/datadoghq/operator                           | public.ecr.aws/datadog/operator                           |
| datadoghq.azurecr.io/dogstatsd                          | datadog/dogstatsd                          | gcr.io/datadoghq/dogstatsd                          | public.ecr.aws/datadog/dogstatsd                          |
| datadoghq.azurecr.io/synthetics-private-location-worker | datadog/synthetics-private-location-worker | gcr.io/datadoghq/synthetics-private-location-worker | public.ecr.aws/datadog/synthetics-private-location-worker |

Pulling from the ACR, GCR or ECR registry works the same (except for Notary) as pulling from Docker Hub. You can use the same command (with different parameters) and get the same image.

**Note**: ACR, ECR and GCR do not support Notary. If you are verifying the signature of images pulled from Docker, this feature does not work on GCR or ECR.

To update your registry, you need to update your registry values based on the type of container environment you are deploying on.

**Note**: You can also use a private registry, but you will need to create a pull secret to be able the pull the images from the private registry. For more information about creating a pull secret, see the [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#registry-secret-existing-credentials).

## Docker{% #docker %}

### Updating your registry{% #updating-your-registry %}

To update your containers registry, run the pull command for the new registry. To see the Docker pull commands for different container registries, see the examples in the [Overview of the Docker docs page](https://docs.datadoghq.com/agent/docker/?tab=standard).

## Kubernetes with Helm chart{% #kubernetes-with-helm-chart %}

To update your containers registry while deploying the Datadog Agent (or Datadog Cluster Agent) with the Datadog helm chart on Kubernetes (including GKE, EKS, AKS, and OpenShift) update the `values.yaml` to specify a different registry:

### Datadog Helm chart >= v2.7.0{% #datadog-helm-chart--v270 %}

1. Update your `values.yaml`:
   ```yaml
   registry: gcr.io/datadoghq
   ```
1. Remove any overrides for `agents.image.repository`, `clusterAgent.image.repository`, or `clusterChecksRunner.image.repository` in the `values.yaml`.

### Datadog Helm chart < v2.7.0{% #datadog-helm-chart--v270-1 %}

Change the repository to `gcr.io`:

```yaml
agents:
  image:
    repository: gcr.io/datadoghq/agent

clusterAgent:
  image:
    repository: gcr.io/datadoghq/cluster-agent

clusterChecksRunner:
  image:
    repository: gcr.io/datadoghq/agent
```

For more information about using the Datadog Helm chart, see the [Datadog Kubernetes documentation](https://docs.datadoghq.com/agent/kubernetes/?tab=helm) and the example [`values.yaml`](https://github.com/DataDog/helm-charts/blob/dae884481c5b3c9b67fc8dbd69c944bf3ec955e9/charts/datadog/values.yaml#L19) file.

If using a private registry, you will need to add a pull secret to the `[key].image.pullSecrets` field to each image.

```yaml
agents:
  image:
    pullSecrets:
      - name: PrivateRegistrySecret

clusterAgent:
  image:
    pullSecrets:
    - name: PrivateRegistrySecret

clusterChecksRunner:
  image:
    pullSecrets:
    - name: PrivateRegistrySecret
```

## Kubernetes with the Datadog Operator{% #kubernetes-with-the-datadog-operator %}

To update your registry while deploying the Datadog Agent (or Datadog Cluster Agent) with the Datadog Operator:

1. Update the Datadog Agent manifest file to override the default registry (`gcr.io/datadoghq`). For example, with `public.ecr.aws/datadog`:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    registry: gcr.io/datadoghq
  // ..
```
Remove any overrides for the `spec.override.nodeAgent.image.name`, `spec.override.clusterAgent.image.name`, and `spec.override.clusterChecksRunner.image.name` fields.If using a private registry, you will need to add a pull secret to the `[key].image.pullSecrets` field to each image.
```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  override:
    nodeAgent:
      image:
        pullSecrets:
          - name: PrivateRegistrySecret
    clusterAgent:
      image:
        pullSecrets:
          - name: PrivateRegistrySecret
    clusterChecksRunner:
      image:
        pullSecrets:
          - name: PrivateRegistrySecret
  // ..
```

For more information about the Datadog Operator, see [Deploying an Agent with the Operator](https://docs.datadoghq.com/agent/kubernetes/?tab=operator#deploy-an-agent-with-the-operator).

### Using another container registry with Helm{% #using-another-container-registry-with-helm %}

You could also switch from the default `gcr.io/datadoghq` registry to another registry, such as `datadoghq.azurecr.io` when installing the Operator with the Helm chart:

Update [`values.yaml`](https://github.com/DataDog/helm-charts/blob/main/charts/datadog-operator/values.yaml#L28) with the new image:

```yaml
image:
  repository: datadoghq.azurecr.io
```

## ECS{% #ecs %}

To update your registry while deploying on ECS, in the `datadog-agent-ecs.json` file, change the value of the `"image"` key under `containerDefinitions` to `"public.ecr.aws/datadog/agent:latest"`:

```json
"image": "public.ecr.aws/datadog/agent:latest",
```

For more information about deploying Datadog on ECS, see the [Datadog ECS documentation](https://docs.datadoghq.com/agent/amazon_ecs/?tab=awscli) and the example [`datadog-agent-ecs.json`](https://docs.datadoghq.com/agent/amazon_ecs/?tab=awscli) file.

## Fargate{% #fargate %}

To update your registry while deploying on Fargate, update the image in the Fargate task definition to use `public.ecr.aws`:

```json
"image": "public.ecr.aws/datadog/agent:latest"
```

The next time the task starts, it pulls from `public.ecr.aws` instead of Docker Hub. For more information about deploying on Fargate, see [Deploying the Agent on ECS](https://www.datadoghq.com/blog/aws-fargate-monitoring-with-datadog/#deploy-the-agent-on-ecs) and [Deploying the Agent on EKS](https://www.datadoghq.com/blog/aws-fargate-monitoring-with-datadog/#deploy-the-agent-on-eks).

## Cluster Agent{% #cluster-agent %}

If you're using the Helm chart to deploy the Datadog Agent and the Datadog Cluster Agent, follow the instructions in Kubernetes with Helm chart, and no other updates are needed. The change to the Helm `values.yaml` outlined above changes the repository that both the Cluster Agent and the Datadog Agent are pulled from.

If you're using the Datadog Operator to deploy the Datadog Cluster Agent, follow the instructions in Kubernetes with the Datadog Operator, and no other updates are needed. The instructions for updating the Operator configuration updates the repository that both the Cluster Agent and the Datadog Agent are pulled from.

For more information about the Datadog Cluster Agent, see the [Cluster Agent docs](https://docs.datadoghq.com/agent/cluster_agent/), and the [setup docs](https://docs.datadoghq.com/agent/cluster_agent/setup/?tab=helm).

## Kubernetes Helm for the Datadog Private Location worker{% #kubernetes-helm-for-the-datadog-private-location-worker %}

To update your registry for the Private Location worker, update the `datadog/synthetics-private-location-worker` image to the `public.ecr.aws/datadog/synthetics-private-location-worker` or `gcr.io/datadoghq/synthetics-private-location-worker` images.

To change the default repository (`gcr.io/datadoghq`), update the `values.yaml` with the new image:

```yaml
image:
  repository: gcr.io/datadoghq/synthetics-private-location-worker
```

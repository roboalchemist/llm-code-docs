# Source: https://docs.anyscale.com/k8s/helm-ref.md

# Kubernetes Helm configuration reference

[View Markdown](/k8s/helm-ref.md)

# Kubernetes Helm configuration reference

This page provides a complete reference for all configuration parameters available in the Anyscale operator Helm chart.

important

This page describes the Helm chart parameters introduced in Anyscale operator version 1.0.0.

If you have a deployment of the Anyscale operator configured with an earlier version, see [Migrate from legacy Anyscale operator Helm charts](#migrate-legacy).

## How to use this reference[​](#how-to-use-this-reference "Direct link to How to use this reference")

Anyscale provides a default `values.yaml` file with settings required for the operator. **Don't modify the Anyscale-provided file.** Instead, create your own custom values file with only the parameters you need to configure.

Parameters in this reference fall into three categories:

1. **Required user configuration**: Parameters you must set in your custom values file.
2. **Optional user configuration**: Parameters you can optionally set to customize behavior.
3. **Anyscale-managed defaults**: Parameters with default values that you usually shouldn't change. You can override these if needed, but contact [Anyscale support](mailto:support@anyscale.com) for guidance.

See [Configure the Helm chart for the Anyscale operator](/k8s/configure-helm.md) for workflow examples and [Deploy Anyscale on Kubernetes](/admin/cloud/kubernetes.md) for deployment procedures.

## Required user configuration[​](#required "Direct link to Required user configuration")

You must set the following parameters in your custom values file for the Anyscale operator to function:

| Parameter                      | Type   | Description                                                                                                                                                                                                      | Example                                                                                                                                                                                      |
| ------------------------------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `global.cloudDeploymentId`     | string | Anyscale cloud deployment ID created when you register the cloud. Retrieve using the following command:`anyscale cloud config get --name <cloud_name>`                                                           | `cldrsrc_abcdefgh12345678ijklmnop12`                                                                                                                                                         |
| `global.cloudProvider`         | string | Cloud provider environment. Options:- `aws` - Amazon Web Services.<br />- `gcp` - Google Cloud.<br />- `azure` - Microsoft Azure.<br />- `generic` - Other Kubernetes environments.                              | `aws`                                                                                                                                                                                        |
| `global.aws.region`            | string | **AWS only**: AWS region for deployment. Required when using workload identity authentication (when `global.auth.anyscaleCliToken` isn't provided).                                                              | `us-west-2`                                                                                                                                                                                  |
| `global.auth.anyscaleCliToken` | string | Anyscale CLI token for control plane authentication.**Required for Azure and generic deployments**. Not required for EKS or GKE when using workload identity.                                                    | `tkn_1234567890abcdef`                                                                                                                                                                       |
| `global.auth.iamIdentity`      | string | Cloud provider IAM identity:- **AWS**: IAM role ARN.<br />- **Google Cloud**: Service account email.<br />- **Azure**: Client ID of the Azure AD Application associated with the user-assigned managed identity. | - AWS: `arn:aws:iam::123456789012:role/anyscale-operator-role`<br />- Google Cloud: `anyscale-operator@project.iam.gserviceaccount.com`<br />- Azure: `00000000-1111-2222-3333-444444444444` |
| `global.auth.audience`         | string | **Azure only**: The audience of the Anyscale Control Plane API. Required for Azure deployments.                                                                                                                  | `api://086bc555-6989-4362-ba30-fded273e432b/.default`                                                                                                                                        |

## Optional user configuration[​](#optional "Direct link to Optional user configuration")

The following sections describe parameters you can optionally set in your custom values file to customize operator behavior.

### Instance types[​](#instance-types "Direct link to Instance types")

Anyscale uses the term **instance types** to describe compute resources such as virtual machines. For Kubernetes, you define custom pod resource configurations that match your node pools and accelerators.

| Parameter                                  | Description                                                                                                                                                            | Example                                                                                                                                                                                                                                                                         |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `workloads.instanceTypes.enableDefaults`   | Whether to enable default instance types provided by Anyscale. Set to `false` to use only custom instance types. Default: `true`.                                      | ```
workloads:
  instanceTypes:
    enableDefaults: true
```                                                                                                                                                                                                                        |
| `workloads.instanceTypes.configMap.name`   | Name of the ConfigMap that stores instance type definitions. Default: `instance-types`.                                                                                | ```
workloads:
  instanceTypes:
    configMap:
      name: "instance-types"
```                                                                                                                                                                                                      |
| `workloads.instanceTypes.additional`       | Custom pod resource configurations. Define your own instance types matching your node pools and accelerators. These merge with defaults if `enableDefaults` is `true`. | ```
workloads:
  instanceTypes:
    additional:
      16CPU-64GB-2xA100:
        resources:
          CPU: 16
          GPU: 2
          memory: 64Gi
          accelerators:
            - A100-40G
        nodeSelector:
          cloud.google.com/gke-accelerator: nvidia-tesla-a100
``` |
| `workloads.instanceTypes.additional` (ARM) | For ARM-based nodes (for example, AWS Graviton), set `cpuArchitecture: "arm64"` on each ARM instance type (Anyscale operator 1.3.2 or later).                          | ```
workloads:
  instanceTypes:
    additional:
      2CPU-8GB-ARM:
        resources:
          CPU: 2
          memory: 8Gi
        cpuArchitecture: "arm64"
```                                                                                                                       |

For complete guidance on sizing and configuring instance types, see [Configure custom instance types](/k8s/configure-helm.md#custom-instance-types).

### Networking configuration[​](#networking-config "Direct link to Networking configuration")

Configure ingress, gateway, and DNS settings for accessing dashboards and services.

important

Anyscale recommends using ingress for most deployments. See [Configure networking](/k8s/configure-helm.md#networking).

| Parameter                                               | Description                                                                                                                                                               |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `networking.ingress.address`                            | DNS address (IP or hostname) for ingress. By default, Anyscale reads this from the Ingress resource status field. Override if needed for your environment.                |
| `networking.ingress.classNameOverride`                  | Ingress class name to use for workloads. If unset, the operator defaults to `nginx`. Use a custom value when you use a different ingress controller.                      |
| `networking.gateway.enabled`                            | Set to `true` to use gateway for load balancing instead of ingress controller. Default: `false`.                                                                          |
| `networking.gateway.name`                               | Name of the gateway resource when using gateway mode.                                                                                                                     |
| `networking.gateway.ip` / `networking.gateway.hostname` | Gateway address. Provide either the IP or hostname.                                                                                                                       |
| `networking.gateway.apiVersion`                         | Gateway API version. Supports `gateway.networking.k8s.io/v1` (Kubernetes Gateway API) or `networking.istio.io/v1alpha3` (Istio). Default: `gateway.networking.k8s.io/v1`. |

warning

If you change the value of `networking.gateway.hostname` or `networking.gateway.ip`, you must redeploy all existing Anyscale services or you might run into issues with DNS updates. New services automatically use the updated gateway configuration.

### High availability[​](#user-ha "Direct link to High availability")

Configure operator redundancy for production deployments.

| Parameter                                | Description                                                                                                                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `operator.replicas`                      | Number of operator replicas. Values greater than 1 enable leader election for high availability. Default: `1`.                                                                                                   |
| `operator.serviceAccount.name`           | Name of the Kubernetes service account used by the operator. Default: `anyscale-operator`.                                                                                                                       |
| `workloads.enableAnyscaleRayHeadNodePDB` | Create PodDisruptionBudget to prevent head node evictions. This can block Kubernetes cluster upgrades. Default: `true`. See [Configure high availability with PodDisruptionBudgets](/k8s/configure-helm.md#pdb). |

### Workload features[​](#workload-features "Direct link to Workload features")

Configuration options for workload behavior and scheduling.

| Parameter                                          | Description                                                                                                                                                                                                                                                       |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `workloads.enableKarpenterSupport`                 | Enable support for Karpenter autoscaler on AWS. Configures appropriate node selectors and scheduling parameters. Default: `false`.                                                                                                                                |
| `workloads.enableZoneSelector`                     | Enable zone-based node selection using `topology.kubernetes.io/zone` nodeSelector. Disabled by default because many cluster autoscalers don't respect this selector. Default: `false`.                                                                            |
| `workloads.enableCrossNamespaceResourceManagement` | Enable cross-namespace resource management. If `true`, the operator manages resources across namespaces specified in `workloads.managedNamespaces`. Default: `false`.                                                                                             |
| `workloads.managedNamespaces`                      | List of namespaces where the operator copies secrets from its own namespace. Use with `workloads.enableCrossNamespaceResourceManagement`. Default: `[]`.                                                                                                          |
| `workloads.serviceAccount.name`                    | Service account assigned to Anyscale workload pods. Leave empty to use the default service account.                                                                                                                                                               |
| `workloads.serviceAccount.iamMappingAnnotation`    | Annotation key used to identify pods that use IAM mapping. Default: `anyscale.com/iam-mapping`.                                                                                                                                                                   |
| `workloads.enableProcessTracing`                   | When `true`, Ray containers get `SYS_PTRACE` so you can profile Ray processes and view actor flamegraphs and stack traces. Default: `true`. Set to `false` if your cluster disallows `SYS_PTRACE`, or pod creation will fail. (Anyscale operator 1.4.0 or later). |

### Advanced features[​](#user-advanced "Direct link to Advanced features")

Additional configuration options for specialized deployments.

| Parameter                                                              | Description                                                                                                                                                                    |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `patches`                                                              | Custom JSON patches applied to pods and other Kubernetes resources. Use for cluster-specific customization. See [Apply custom patches](/k8s/configure-helm.md#custom-patches). |
| `operator.nodeSelector` / `operator.affinity` / `operator.tolerations` | Control operator pod placement. Useful for dedicating nodes to the operator.                                                                                                   |
| `operator.deployment.annotations` / `operator.deployment.labels`       | Annotations and labels applied to the operator Deployment. Useful for integration with policy or monitoring systems that categorize workloads by metadata.                     |
| `global.aws.s3.usePathStyle`                                           | Use path-style S3 URLs instead of virtual-hosted-style. Enable for S3-compatible storage such as MinIO. Default: `false`.                                                      |
| `global.azure.workloadIdentity.proxyPort`                              | **Azure only**: Port for the Azure workload identity proxy. Default: `10000`.                                                                                                  |

### AWS credential mounting[​](#aws-credential-mounting "Direct link to AWS credential mounting")

When workload identity isn't available, mount AWS credentials from a Kubernetes secret so the operator and workload pods can authenticate to AWS.

| Parameter                                           | Description                                                                                                                                                                                | Default                    |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| `credentialMount.aws.enabled`                       | When `true`, the operator and workload pods mount AWS credentials from the secret.                                                                                                         | `false`                    |
| `credentialMount.aws.fromSecret.name`               | Name of the Kubernetes Secret containing the AWS credentials.                                                                                                                              | `anyscale-aws-credentials` |
| `credentialMount.aws.fromSecret.operatorMountPath`  | Path where the credential is mounted in the operator pod.                                                                                                                                  | `/root/.aws`               |
| `credentialMount.aws.fromSecret.podMountPath`       | Path where the credential is mounted in workload pods.                                                                                                                                     | `/tmp/.aws`                |
| `credentialMount.aws.createSecret.create`           | When `false`, you must create a secret with the name in `credentialMount.aws.fromSecret.name`. When `true`, the chart creates the secret.                                                  | `false`                    |
| `credentialMount.aws.createSecret.accessKeyId`      | AWS access key ID. Required if `credentialMount.aws.createSecret.create` is `true`.                                                                                                        | `""`                       |
| `credentialMount.aws.createSecret.secretAccessKey`  | AWS secret access key. Required if `credentialMount.aws.createSecret.create` is `true`.                                                                                                    | `""`                       |
| `credentialMount.aws.createSecret.endpointUrl`      | Custom S3 endpoint URL (optional). Use for S3-compatible storage.                                                                                                                          | `""`                       |
| `credentialMount.aws.createSecret.addressingStyle`  | S3 addressing style. Options: `path`, `virtual` (Anyscale operator 1.4.0 or later). See [AWS CLI S3 config](https://docs.aws.amazon.com/cli/latest/topic/s3-config.html#addressing-style). | `""`                       |
| `credentialMount.aws.createSecret.signatureVersion` | S3 signature version for API requests. Options: `s3` (SigV2), `s3v4` (SigV4) (Anyscale operator 1.4.1 or later).                                                                           | `""`                       |

### Google Cloud credential mounting[​](#gcp-credential-mounting "Direct link to Google Cloud credential mounting")

When workload identity isn't available, mount a Google Cloud service account JSON key so the operator and workload pods can authenticate to Google Cloud (Anyscale operator 1.3.0 or later).

| Parameter                                          | Description                                                                                                                                                         | Default                    |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `global.gcp.projectId`                             | Google Cloud project ID set in workload environment variables.                                                                                                      | `""`                       |
| `credentialMount.gcp.enabled`                      | Enable mounting a Google Cloud credential from a Kubernetes secret into the operator and workload pods.                                                             | `false`                    |
| `credentialMount.gcp.fromSecret.name`              | Name of the Kubernetes Secret containing the credential JSON key.                                                                                                   | `anyscale-gcp-credentials` |
| `credentialMount.gcp.fromSecret.operatorMountPath` | Path where the credential file is mounted in the operator pod.                                                                                                      | `/var/secrets`             |
| `credentialMount.gcp.fromSecret.podMountPath`      | Path where the credential file is mounted in workload pods.                                                                                                         | `/var/secrets`             |
| `credentialMount.gcp.createSecret.create`          | When set to `false`, you must create a Kubernetes secret with the name in `credentialMount.gcp.fromSecret.name`. Set to `true` to automatically create the secret.  | `false`                    |
| `credentialMount.gcp.createSecret.keyJsonB64`      | Base64-encoded Google Cloud credential JSON. You must provide this value if `credentialMount.gcp.createSecret.create` is `true` to automatically create the secret. | `""`                       |

### Resource overrides[​](#user-resources "Direct link to Resource overrides")

Override default CPU and memory allocations if your environment requires different values.

| Parameter                                            | Description                                                                                                                                               |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `operator.container.resources`                       | CPU and memory requests/limits for the operator container. See [Configure operator resources](/k8s/configure-helm.md#resource-config) for examples.       |
| `operator.vector.resources`                          | CPU and memory requests/limits for the Vector sidecar container. See [Configure operator resources](/k8s/configure-helm.md#resource-config) for examples. |
| `operator.config.kubernetesClient.rateLimiter.qps`   | Kubernetes API server query per second rate limit. Increase for large workloads. Default: `1000`.                                                         |
| `operator.config.kubernetesClient.rateLimiter.burst` | Kubernetes API server burst rate limit. Increase for large workloads. Default: `2000`.                                                                    |

## Anyscale-managed defaults[​](#managed-defaults "Direct link to Anyscale-managed defaults")

The following parameters have default values managed by Anyscale. You can override these if needed, but most deployments should use the defaults. Contact [Anyscale support](mailto:support@anyscale.com) before modifying these values.

### Operator configuration[​](#operator-config "Direct link to Operator configuration")

Anyscale provides default operator configuration values.

| Parameter                           | Description                                                                                                      | Default                                                                   |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `operator.container.image.registry` | Docker registry for the operator image.                                                                          | `us-docker.pkg.dev`                                                       |
| `operator.container.image.image`    | Docker image path for the Anyscale operator.                                                                     | `anyscale-artifacts/public/kubernetes_manager`                            |
| `operator.container.image.tag`      | Docker image tag for the Anyscale operator. Each operator version requires a specific image tag.                 | Version-specific (example: `ci-fe4d6d5d24deb02caa5ea9b60c8e837ac1ca9e05`) |
| `operator.vector.image.registry`    | Docker registry for the Vector sidecar. Empty string means `docker.io`.                                          | `""`                                                                      |
| `operator.vector.image.image`       | Docker image path for the Vector telemetry sidecar that forwards logs and metrics to the Anyscale control plane. | `timberio/vector`                                                         |
| `operator.vector.image.tag`         | Docker image tag for the Vector sidecar.                                                                         | `0.40.0-debian`                                                           |

### Default instance types[​](#managed-instance-types "Direct link to Default instance types")

Anyscale provides default pod resource configurations. Use `workloads.instanceTypes.additional` to create custom instance types instead of modifying these.

| Parameter                          | Description                                               | Default configurations                                                                                                                                                  |
| ---------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `workloads.instanceTypes.defaults` | Default pod resource configurations provided by Anyscale. | - `2CPU-8GB`: 2 CPUs, 8GB memory<br />- `4CPU-16GB`: 4 CPUs, 16GB memory<br />- `8CPU-32GB`: 8 CPUs, 32GB memory<br />- `8CPU-32GB-1xT4`: 8 CPUs, 32GB memory, 1 T4 GPU |

### Accelerator mappings[​](#managed-accelerators "Direct link to Accelerator mappings")

Maps Ray accelerator types to cloud-specific node labels for scheduling.

| Cloud provider | Supported accelerators                                           |
| -------------- | ---------------------------------------------------------------- |
| AWS            | V100, T4, L4, A10G, L40S, A100-40G, A100-80G, H100, RTX-PRO-6000 |
| Azure          | T4, A10, A100, H100                                              |
| Google Cloud   | T4, L4, A100-40G, A100-80G, H100, H100-MEGA, RTX-PRO-6000        |

Control accelerator behavior with these parameters:

* `workloads.accelerator.enableDefaults`: Enable default accelerator mappings. Default: `true`.
* `workloads.accelerator.customNodeSelectorKey`: Custom node selector key instead of cloud provider defaults.
* `workloads.accelerator.nodeSelectors`: Accelerator type to node selector value mappings per cloud provider.
* `workloads.accelerator.tolerations.default`: Default tolerations applied to all GPU/accelerator workloads.

### Market type configuration[​](#managed-market-types "Direct link to Market type configuration")

The operator includes default market type configurations using JSON patches. These configurations handle spot and on-demand instance scheduling based on your cloud provider.

Control market type behavior with these parameters:

* `workloads.marketType.enableDefaults`: Enable default market type patches. Default: `true`.
* `workloads.marketType.generic`: Patches for any cloud provider.
* `workloads.marketType.aws`: AWS-specific patches.
* `workloads.marketType.gcp`: Google Cloud-specific patches.
* `workloads.marketType.azure`: Azure-specific patches.
* `workloads.marketType.karpenter`: Karpenter-specific patches (overrides cloud provider defaults when `workloads.enableKarpenterSupport` is `true`).

### Other managed defaults[​](#managed-other "Direct link to Other managed defaults")

| Parameter                                                   | Description                                                                                                                                                                                          | Default                        |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `operator.config.status.reportingEnabled`                   | Enable status reporting to Anyscale control plane.                                                                                                                                                   | `true`                         |
| `operator.config.status.checkInterval`                      | How often the operator checks status.                                                                                                                                                                | `5m`                           |
| `operator.config.status.reportInterval`                     | How often the operator reports status to the control plane.                                                                                                                                          | `30s`                          |
| `operator.config.unscheduledPodReaper.reconcileInterval`    | How often the operator checks for unscheduled pods.                                                                                                                                                  | `1m`                           |
| `operator.config.unscheduledPodReaper.terminationThreshold` | Time before terminating pods that remain unscheduled.                                                                                                                                                | `10m`                          |
| `operator.config.status.excludeComponentVerification`       | Skip verification of specific components during operator startup. Options: `STORAGE_BUCKET`, `KUBERNETES_VERSION`, `GATEWAY_RESOURCES`, `CLOUD_RESOURCES`, `IAM_IDENTITY`, `KUBERNETES_PERMISSIONS`. | `[]` (all components verified) |
| `operator.name`                                             | Name of the operator. Used to identify resources related to the operator in the Kubernetes cluster.                                                                                                  | `anyscale-operator`            |

## Common configuration examples[​](#examples "Direct link to Common configuration examples")

The following examples show complete custom values files for common deployment scenarios. Save these as your custom values file (for example, `my-custom-values.yaml`) in YAML format and use with `helm install` or `helm upgrade`.

### Basic AWS deployment[​](#example-aws "Direct link to Basic AWS deployment")

Minimal configuration for AWS EKS (save as `my-custom-values.yaml`):

```
global:
  cloudDeploymentId: "cldrsrc_abcdefgh12345678ijklmnop12"
  cloudProvider: "aws"
  aws:
    region: "us-west-2"
  auth:
    iamIdentity: "arn:aws:iam::123456789012:role/anyscale-operator-role"
```

### Google Cloud with custom instance types[​](#example-gcp "Direct link to Google Cloud with custom instance types")

Google Cloud deployment with additional GPU instance types:

```
global:
  cloudDeploymentId: "cldrsrc_abcdefgh12345678ijklmnop12"
  cloudProvider: "gcp"
  auth:
    iamIdentity: "anyscale-operator@my-project.iam.gserviceaccount.com"

workloads:
  instanceTypes:
    additional:
      16CPU-64GB-2xA100:
        resources:
          CPU: 16
          GPU: 2
          memory: 64Gi
          accelerators:
            - A100-40G
        nodeSelector:
          cloud.google.com/gke-accelerator: nvidia-tesla-a100
        tolerations:
          - key: "nvidia.com/gpu"
            operator: "Exists"
            effect: "NoSchedule"
```

### High availability configuration[​](#example-ha "Direct link to High availability configuration")

Production setup with multiple replicas and resource limits:

```
global:
  cloudDeploymentId: "cldrsrc_abcdefgh12345678ijklmnop12"
  cloudProvider: "aws"
  aws:
    region: "us-west-2"
  auth:
    iamIdentity: "arn:aws:iam::123456789012:role/anyscale-operator-role"

# Enable HA with 3 replicas
operator:
  replicas: 3
  
  # Increase resources for production workloads
  container:
    resources:
      requests:
        memory: 1Gi
        cpu: 2
      limits:
        memory: 4Gi
  
  # Dedicated node pool for operator
  nodeSelector:
    node-role.kubernetes.io/control-plane: "true"
  tolerations:
    - key: "node-role.kubernetes.io/control-plane"
      operator: "Exists"
      effect: "NoSchedule"
```

### Basic Azure deployment[​](#example-azure "Direct link to Basic Azure deployment")

Minimal configuration for Azure AKS (save as `my-custom-values.yaml`):

```
global:
  cloudDeploymentId: "cldrsrc_abcdefgh12345678ijklmnop12"
  cloudProvider: "azure"
  auth:
    # Client ID of the Azure AD Application associated with the user-assigned managed identity
    iamIdentity: "00000000-1111-2222-3333-444444444444"
    # Audience for the Anyscale Control Plane API
    audience: "api://086bc555-6989-4362-ba30-fded273e432b/.default"
```

### Gateway configuration with Istio[​](#example-gateway "Direct link to Gateway configuration with Istio")

Using Istio gateway instead of ingress:

```
global:
  cloudDeploymentId: "cldrsrc_abcdefgh12345678ijklmnop12"
  cloudProvider: "gcp"
  auth:
    iamIdentity: "anyscale-operator@my-project.iam.gserviceaccount.com"

# Enable gateway mode
networking:
  gateway:
    enabled: true
    name: "anyscale-gateway"
    hostname: "anyscale.example.com"
    apiVersion: "networking.istio.io/v1alpha3"
```

## Source files[​](#source "Direct link to Source files")

The complete Helm chart source is available on GitHub:

* [Anyscale operator repository](https://github.com/anyscale/helm-charts)
* [`values.yaml` with all defaults](https://github.com/anyscale/helm-charts/blob/master/charts/anyscale-operator/values.yaml)
* [Helm chart README](https://github.com/anyscale/helm-charts/blob/master/charts/anyscale-operator/README.md)

## Migrate from legacy Anyscale operator Helm charts[​](#migrate-legacy "Direct link to Migrate from legacy Anyscale operator Helm charts")

If you have an Anyscale operator configured using version 0.9.2 or earlier, you must migrate your Helm chart values before upgrading to version 1.0.0.

See the [Anyscale operator Helm chart migration guide](https://github.com/anyscale/helm-charts/blob/master/charts/anyscale-operator/MIGRATION_README.md).

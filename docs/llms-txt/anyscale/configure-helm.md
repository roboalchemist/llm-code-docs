# Source: https://docs.anyscale.com/k8s/configure-helm.md

# Configure the Helm chart for the Anyscale operator

[View Markdown](/k8s/configure-helm.md)

# Configure the Helm chart for the Anyscale operator

This page provides an overview of configuring Helm chart values to control how Helm installs the Anyscale operator on your Kubernetes cluster.

You must configure Helm chart parameters when deploying an Anyscale cloud to Kubernetes for the first time. You can also update settings and apply changes to an existing Anyscale cloud. See [Deploy Anyscale on Kubernetes](/admin/cloud/kubernetes.md).

important

This page describes the Helm chart parameters introduced in Anyscale operator version 1.0.0.

If you have a deployment of the Anyscale operator configured with an earlier version, see [Migrate from legacy Anyscale operator Helm charts](/k8s/helm-ref.md#migrate-legacy).

## Configuration workflow overview[​](#configuration-workflow-overview "Direct link to Configuration workflow overview")

Anyscale provides a `values.yaml` file with default settings required for the operator to function correctly. **Don't modify the Anyscale-provided values file directly.** Instead, create your own custom values file (for example, `my-custom-values.yaml`) to configure settings specific to your environment.

When you run `helm install` or `helm upgrade` with your custom values file, Helm merges your custom settings with Anyscale's defaults. This approach ensures that:

* You receive updated default values when upgrading to new operator versions.
* Your custom configurations persist across upgrades.
* You can version-control your configurations separately from Anyscale's defaults.

important

Anyscale requires default or Anyscale-provided values for some Helm chart parameters. These required values might change between operator versions.

For assistance configuring your Anyscale operator, contact [Anyscale support](mailto:support@anyscale.com).

See the following resources for more details:

* The [Anyscale operator Helm chart GitHub repository](https://github.com/anyscale/helm-charts/blob/master/charts/anyscale-operator/values.yaml) includes a `values.yaml` file with parameters and docstrings.
* For parameter descriptions and default values, see [Kubernetes Helm configuration reference](/k8s/helm-ref.md).

## Apply custom configurations for your Anyscale operator[​](#apply-config "Direct link to Apply custom configurations for your Anyscale operator")

Complete the following steps to configure and deploy the Anyscale operator:

important

Specific configuration requirements and recommendations might differ based on how you've configured your Kubernetes cluster.

Some configurations might require updates to settings or IAM permissions in your cloud provider account.

To successfully customize the Anyscale operator, you should be familiar with your existing Kubernetes environment and have admin permissions in your cloud provider account.

1. Create a custom values file (for example, `my-custom-values.yaml`) with your configuration:

   ```
   # Required: Global configuration
   global:
     cloudDeploymentId: "cldrsrc_abcdefgh12345678ijklmnop12"
     cloudProvider: "aws"
     aws:
       region: "us-west-2"
     auth:
       iamIdentity: "arn:aws:iam::123456789012:role/anyscale-operator-role"

   # Optional: Add custom instance types
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
             custom-node-selector: value
           tolerations:
             - key: "custom-taint"
               operator: "Exists"
               effect: "NoSchedule"
     
     # Optional: Enable Karpenter support
     enableKarpenterSupport: true
   ```

2. For initial installation, run the following command:

   ```
   helm install anyscale-operator anyscale/anyscale-operator \
     -n <namespace> \
     -f my-custom-values.yaml
   ```

3. To upgrade to a new operator version with your existing configuration:

   ```
   helm repo update
   helm upgrade anyscale-operator anyscale/anyscale-operator \
     -n <namespace> \
     -f my-custom-values.yaml
   ```

warning

If your cluster disallows `SYS_PTRACE` for pods, set `workloads.enableProcessTracing: false` when upgrading to Anyscale operator version 1.4.0 or later. This overrides new default behavior that will cause pod creation to fail. See [Workload features](/k8s/helm-ref.md#workload-features).

warning

**Don't use `--reuse-values` alone when upgrading.**

The `--reuse-values` flag uses old chart default values and doesn't pick up important updates from Anyscale (such as IngressClass collision prevention). Always use the `-f` flag with your custom values file, which automatically merges with the latest chart defaults.

If you previously used `--set` flags and need to preserve those values while getting new defaults, use `--reset-then-reuse-values` instead of `--reuse-values`.

## Configure custom instance types[​](#custom-instance-types "Direct link to Configure custom instance types")

When running on Kubernetes, an Anyscale instance type maps to a Pod shape with specific CPU, memory, and accelerator resources. You define instance types through the Helm chart to make them available in the Anyscale console and for compute configs.

important

Anyscale recommends using the `workloads.instanceTypes.additional` parameter to define custom resources. See [Add custom instance types](#custom-instances).

You can disable defaults entirely with `workloads.instanceTypes.enableDefaults: false`. You can also override the `workloads.instanceTypes.defaults` parameter but this can make troubleshooting with Anyscale support more difficult.

For complete parameter details, see [Instance types](/k8s/helm-ref.md#instance-types).

### How to size instance type for Anyscale on Kubernetes[​](#how-to-size-instance-type-for-anyscale-on-kubernetes "Direct link to How to size instance type for Anyscale on Kubernetes")

You must correctly size your pod specs to ensure they respect CPU and memory reservations required by Anyscale and Kubernetes.

When the Anyscale operator applies a Pod spec to Kubernetes for an Anyscale workload, the operator uses the shapes defined in the Instance Type ConfigMap as an upper bound for the sum of all of the memory requests and limits across all containers in the pod. Anyscale reserves some memory and CPU for critical-path Anyscale sidecar containers and provides the rest to the Ray container to run the primary workload.

Kubernetes reserves a portion of CPU and memory for running the Kubelet and other Kubernetes system components. To accommodate for CPU usage by Kubernetes and Anyscale, the pod shapes defined in the ConfigMap must be smaller than the actual node shape. See [Reserve Compute Resources for System Daemons](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/) in the Kubernetes documentation for more details.

As an example, an AWS `m5.4xlarge` virtual machine has 16 vCPUs and 64 GiB memory. Anyscale recommends configuring this instance as a `14CPU-56GB` pod. Attempting to define the pod as `16CPU-64GB` might make the pod unschedulable.

### Add custom instance types[​](#custom-instances "Direct link to Add custom instance types")

Anyscale recommends using the `workloads.instanceTypes.additional` parameter to define all your custom instance types. This keeps your configurations separate from Anyscale's defaults.

Instance type names can include alphanumeric characters, dashes, and underscores. The Anyscale console updates with new instance types approximately every 30 seconds.

The following example shows a configuration for an A100 for GKE:

```
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

The `accelerators` list must contain [Ray-supported accelerators](https://docs.ray.io/en/latest/ray-core/accelerator-types.html).

Accelerators must map to the `workloads.accelerator.nodeSelectors` values for your cloud provider. Not all accelerators are available in all regions.

See [Instance types](/k8s/helm-ref.md#instance-types) for a list of supported accelerators by cloud and more details.

For an example configuring support for TPUs on GKE, see [Leverage Cloud TPUs on GKE](/administration/cloud-deployment/leverage-cloud-tpus-on-kubernetes.md).

### Anyscale default instance types for Kubernetes[​](#default-instance-types "Direct link to Anyscale default instance types for Kubernetes")

Anyscale recommends against modifying default instance types. Use the `workloads.instanceTypes.additional` field to configure your own instance types.

Anyscale defines the following instance types by default:

```
workloads:
  instanceTypes:
    enableDefaults: true  # Set to false to disable all defaults
    defaults:
      2CPU-8GB:
        resources:
          CPU: 2
          memory: 8Gi
      4CPU-16GB:
        resources:
          CPU: 4
          memory: 16Gi
      8CPU-32GB:
        resources:
          CPU: 8
          memory: 32Gi
      8CPU-32GB-1xT4:
        resources:
          CPU: 8
          GPU: 1
          memory: 32Gi
          accelerators:
            - T4
```

## Set up Karpenter autoscaling[​](#karpenter-support "Direct link to Set up Karpenter autoscaling")

[Karpenter](https://github.com/aws/karpenter-provider-aws) is an open source node provisioning project built for Kubernetes on AWS. When you enable Karpenter support, the Anyscale operator configures appropriate node selectors and scheduling parameters for proper pod placement with Karpenter-managed nodes.

To enable Karpenter support:

1. Add the Karpenter flag to your custom values file:

   ```
   workloads:
     enableKarpenterSupport: true  # Default is false.
   ```

2. Configure taints and labels on your node groups following the [Karpenter documentation](https://karpenter.sh/docs/).

3. Apply the configuration using `helm upgrade` with your custom values file as shown in [Apply custom configurations for your Anyscale operator](#apply-config).

For complete parameter details, see [workloads.enableKarpenterSupport](/k8s/helm-ref.md#workload-features) in the Helm reference.

tip

Consider using the [Anyscale Terraform provider for Kubernetes](https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules) to automate Karpenter configuration.

## Configure high availability with PodDisruptionBudgets[​](#pdb "Direct link to Configure high availability with PodDisruptionBudgets")

PodDisruptionBudgets (PDBs) prevent cluster maintenance from evicting your Ray head nodes. This ensures your workloads remain stable but requires special procedures for cluster upgrades.

To enable PDB protection, set the following parameter:

```
workloads:
  enableAnyscaleRayHeadNodePDB: true  # Default is true.
```

important

To prevent eviction of head nodes for running Ray clusters, PDBs block rolling Kubernetes cluster upgrades.

With PDBs enabled, you must pause or terminate all running Anyscale services, jobs, and workspaces to upgrade your Kubernetes cluster.

## Configure networking[​](#networking "Direct link to Configure networking")

You must allow ingress to your Kubernetes cluster to support features such as dashboards and Anyscale services.

Anyscale recommends using ingress for most deployments. Anyscale also supports Istio and Kubernetes gateway custom resource definitions. Use a gateway if you already have gateway infrastructure in place or other requirements mandate gateway usage. See [Networking configuration](/k8s/helm-ref.md#networking-config).

By default, the Anyscale operator configures ingress automatically. To manually specify the DNS address, set the following:

```
networking:
  ingress:
    address: "<IP_ADDRESS_OR_HOSTNAME>"
```

Anyscale uses this address for the following:

* User access to the Ray Dashboard through the Anyscale console.
* DNS resolution for Anyscale services.
* Service endpoint connectivity.

### Configure operator resources[​](#resource-config "Direct link to Configure operator resources")

You can customize CPU and memory allocations for the operator and Vector telemetry sidecar. The default values work for most deployments.

```
operator:
  container:
    resources:
      requests:
        cpu: 1
        memory: 512Mi
      limits:
        memory: 2Gi
  vector:
    resources:
      requests:
        cpu: 100m
        memory: 512Mi
      limits:
        memory: 512Mi
```

For all resource parameters, see [Operator configuration](/k8s/helm-ref.md#operator-config) in the Helm reference.

## Apply custom patches[​](#custom-patches "Direct link to Apply custom patches")

The Patch API lets you customize Anyscale-managed resources for your specific Kubernetes environment. Use patches to handle variations in spot instances, accelerators, or other cluster-specific requirements.

Patches use [JSON Patch syntax](https://jsonpatch.com/) ([IETF RFC 6902](https://datatracker.ietf.org/doc/html/rfc6902)).

Each patch requires a `kind` field specifying the resource type and a `patch` field with the JSON Patch operations. You can optionally provide a `selector` field to filter which resources the patch applies to.

note

The `selector` field is optional and uses **annotation** selectors (not label selectors). If you omit the selector, the patch applies to all resources of the specified kind. See [Set-based requirement](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#set-based-requirement) in the Kubernetes documentation for selector syntax.

### Example: Add node selector for on-demand instances[​](#example-add-node-selector-for-on-demand-instances "Direct link to Example: Add node selector for on-demand instances")

```
patches:
  - kind: Pod
    # Optional: An annotation selector to filter resources. Omit to apply to all Pods.
    selector: "anyscale.com/market-type in (ON_DEMAND)"
    # See: https://jsonpatch.com/
    patch:
      - op: add
        path: /spec/nodeSelector/eks.amazonaws.com~1capacityType # use ~1 to escape the forward-slash
        value: "ON_DEMAND"
```

This patch adds the `eks.amazonaws.com/capacityType` node selector to all on-demand pods. The operator applies patches to resources that match the annotation selector.

View all annotations provided by Anyscale that you can use for custom patches

The Anyscale control plane applies these annotations on resources created by Anyscale.

| Label Name                                                                                                                                                                                                                         | Possible Label Values                            | Description                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `anyscale.com/market-type`                                                                                                                                                                                                         | SPOT, ON\_DEMAND                                 | Users with workloads that support preemption may opt to run their workloads on spot node types through the compute config. All other workloads are run on on-demand node types. This should most likely be transformed into a node affinity.                                                                                       |
| `anyscale.com/zone`                                                                                                                                                                                                                | user-defined through cloud setup                 | For Pods that have a specific zone affinity, the Anyscale operator sets this label to the zone that the Pod should be launched into (`us-west-2a`, for example). Zones are provided as \[]string at cloud registration time and can be selected from the Anyscale UI. This should most likely be transformed into a node affinity. |
| `anyscale.com/accelerator-type`                                                                                                                                                                                                    | user-defined through instance type configuration | When requesting a GPU Pod, the Anyscale operator sets one of the following values: [Anyscale accelerator types](https://docs.ray.io/en/latest/ray-core/accelerator-types.html).                                                                                                                                                    |
| `anyscale.com/instance-type`                                                                                                                                                                                                       | user-defined through instance type configuration | The operator sets this value for all Pods created through Anyscale.                                                                                                                                                                                                                                                                |
| `anyscale.com/canary-weight`<br />`anyscale.com/canary-exists`<br />`anyscale.com/canary-svc`<br />`anyscale.com/ingress-type`<br />`anyscale.com/bearer-token`<br />`anyscale.com/primary-weight`<br />`anyscale.com/primary-svc` | various                                          | For advanced use only (when using an ingress other than NGINX for inference / serving workloads with Anyscale services). Contact Anyscale for more details.                                                                                                                                                                        |

View a sample of common advanced configuration options

```
{
  "metadata": {
    // Add a new label.
    "labels": {"new-label": "example-value"},
    // Add a new annotation.
    "annotations": {"new-annotation": "example-value"}
  },
  "spec": {
    // Add a node selector.
    "nodeSelector": {"disktype": "ssd"},
    "tolerations": [{
      "effect": "NoSchedule",
      "key": "dedicated",
      "value": "example-anyscale"
    }]
    "containers": [{
      // Add a PersistentVolumeClaim to the Ray container.
      "name": "ray",
      "volumeMounts": [{
        "name": "pvc-volume",
        "mountPath": "/mnt/pvc-data"
      }]
    },{
      // Add a sidecar for exporting logs and metrics.
      "name": "monitoring-sidecar",
      "image": "timberio/vector:latest",
      "ports": [{
        "containerPort": 9000
      }],
      "volumeMounts": [{
        "name": "vector-volume",
        "mountPath": "/mnt/vector-data"
      }]
    }],
    "volumes": [{
      "name": "pvc-volume",
      "persistentVolumeClaim": {
        "claimName": "my-pvc"
      }
    },{
      "name": "vector-volume",
      "emptyDir": {}
    }]
  }
}
```

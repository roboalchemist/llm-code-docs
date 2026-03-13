# Source: https://kueue.sigs.k8s.io/docs/installation/

Title: Installation

URL Source: https://kueue.sigs.k8s.io/docs/installation/

Markdown Content:
Installing Kueue to a Kubernetes Cluster

*   [Before you begin](https://kueue.sigs.k8s.io/docs/installation/#before-you-begin)
*   [Install a released version](https://kueue.sigs.k8s.io/docs/installation/#install-a-released-version)
    *   [Install by kubectl](https://kueue.sigs.k8s.io/docs/installation/#install-by-kubectl)
    *   [Install by Helm](https://kueue.sigs.k8s.io/docs/installation/#install-by-helm)
    *   [Add metrics scraping for prometheus-operator](https://kueue.sigs.k8s.io/docs/installation/#add-metrics-scraping-for-prometheus-operator)
    *   [Add API Priority and Fairness configuration for the visibility API](https://kueue.sigs.k8s.io/docs/installation/#add-api-priority-and-fairness-configuration-for-the-visibility-api)
    *   [Uninstall](https://kueue.sigs.k8s.io/docs/installation/#uninstall)

*   [Install a custom-configured released version](https://kueue.sigs.k8s.io/docs/installation/#install-a-custom-configured-released-version)
*   [Install the latest development version](https://kueue.sigs.k8s.io/docs/installation/#install-the-latest-development-version)
    *   [Uninstall](https://kueue.sigs.k8s.io/docs/installation/#uninstall-1)

*   [Build and install from source](https://kueue.sigs.k8s.io/docs/installation/#build-and-install-from-source)
    *   [Add metrics scraping for prometheus-operator](https://kueue.sigs.k8s.io/docs/installation/#add-metrics-scraping-for-prometheus-operator-1)
    *   [Uninstall](https://kueue.sigs.k8s.io/docs/installation/#uninstall-2)

*   [Install via Helm](https://kueue.sigs.k8s.io/docs/installation/#install-via-helm)
*   [Change the feature gates configuration](https://kueue.sigs.k8s.io/docs/installation/#change-the-feature-gates-configuration)
    *   [Feature gates for alpha and beta features](https://kueue.sigs.k8s.io/docs/installation/#feature-gates-for-alpha-and-beta-features)
    *   [Feature gates for graduated or deprecated features](https://kueue.sigs.k8s.io/docs/installation/#feature-gates-for-graduated-or-deprecated-features)

*   [What’s next](https://kueue.sigs.k8s.io/docs/installation/#whats-next)

Before you begin [](https://kueue.sigs.k8s.io/docs/installation/#before-you-begin)
----------------------------------------------------------------------------------

Make sure the following conditions are met:

*   A Kubernetes cluster with version 1.29 or newer is running. Learn how to [install the Kubernetes tools](https://kubernetes.io/docs/tasks/tools/).
*   The kubectl command-line tool has communication with your cluster.

Kueue publishes [metrics](https://kueue.sigs.k8s.io/docs/reference/metrics/) to monitor its operators. You can scrape these metrics with Prometheus. Use [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus) if you don’t have your own monitoring system.

The webhook server in kueue uses an internal cert management for provisioning certificates. If you want to use a third-party one, e.g. [cert-manager](https://github.com/cert-manager/cert-manager), follow the [cert manager guide](https://kueue.sigs.k8s.io/docs/tasks/manage/productization/cert_manager/).

Install a released version [](https://kueue.sigs.k8s.io/docs/installation/#install-a-released-version)
------------------------------------------------------------------------------------------------------

### Install by kubectl [](https://kueue.sigs.k8s.io/docs/installation/#install-by-kubectl)

To install a released version of Kueue in your cluster by kubectl, run the following command:

```
kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.16.2/manifests.yaml
```

To wait for Kueue to be fully available, run:

```
kubectl wait deploy/kueue-controller-manager -nkueue-system --for=condition=available --timeout=5m
```

### Install by Helm [](https://kueue.sigs.k8s.io/docs/installation/#install-by-helm)

To install a released version of Kueue in your cluster by [Helm](https://helm.sh/), run the following command:

```
helm install kueue oci://registry.k8s.io/kueue/charts/kueue \
  --version=0.16.2 \
  --namespace  kueue-system \
  --create-namespace \
  --wait --timeout 300s
```

You can also use the following command:

```
helm install kueue https://github.com/kubernetes-sigs/kueue/releases/download/v0.16.2/kueue-0.16.2.tgz \
  --namespace kueue-system \
  --create-namespace \
  --wait --timeout 300s
```

### Add metrics scraping for prometheus-operator [](https://kueue.sigs.k8s.io/docs/installation/#add-metrics-scraping-for-prometheus-operator)

To allow [prometheus-operator](https://github.com/prometheus-operator/prometheus-operator) to scrape metrics from kueue components, run the following command:

```
kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.16.2/prometheus.yaml
```

For more detailed setup instructions and optional metrics configuration, see the [Observability guide](https://kueue.sigs.k8s.io/docs/tasks/manage/observability/).

### Add API Priority and Fairness configuration for the visibility API [](https://kueue.sigs.k8s.io/docs/installation/#add-api-priority-and-fairness-configuration-for-the-visibility-api)

See [Configure API Priority and Fairness](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#configure-api-priority-and-fairness) for more details.

### Uninstall [](https://kueue.sigs.k8s.io/docs/installation/#uninstall)

To uninstall a released version of Kueue from your cluster by kubectl, run the following command:

```
kubectl delete -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.16.2/manifests.yaml
```

To uninstall a released version of Kueue from your cluster by Helm, run the following command:

```
helm uninstall kueue --namespace kueue-system
```

Install a custom-configured released version [](https://kueue.sigs.k8s.io/docs/installation/#install-a-custom-configured-released-version)
------------------------------------------------------------------------------------------------------------------------------------------

To install a custom-configured released version of Kueue in your cluster, execute the following steps:

1.   Download the release’s `manifests.yaml` file:

```
wget https://github.com/kubernetes-sigs/kueue/releases/download/v0.16.2/manifests.yaml
```

1.   With an editor of your preference, open `manifests.yaml`.
2.   In the `kueue-manager-config` ConfigMap manifest, edit the `controller_manager_config.yaml` data entry. The entry represents the default [KueueConfiguration](https://kueue.sigs.k8s.io/docs/reference/kueue-config.v1beta1/). The contents of the ConfigMap are similar to the following:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: kueue-manager-config
  namespace: kueue-system
data:
  controller_manager_config.yaml: |
    apiVersion: config.kueue.x-k8s.io/v1beta2
    kind: Configuration
    namespace: kueue-system
    health:
      healthProbeBindAddress: :8081
    metrics:
      bindAddress: :8443
      # enableClusterQueueResources: true
    webhook:
      port: 9443
    manageJobsWithoutQueueName: true
    internalCertManagement:
      enable: true
      webhookServiceName: kueue-webhook-service
      webhookSecretName: kueue-webhook-server-cert
    waitForPodsReady:
      timeout: 10m
    integrations:
      frameworks:
      - "batch/job"
```

**The `integrations.externalFrameworks` field is available in Kueue v0.7.0 and later.**

1.   Apply the customized manifests to the cluster:

```
kubectl apply --server-side -f manifests.yaml
```

Install the latest development version [](https://kueue.sigs.k8s.io/docs/installation/#install-the-latest-development-version)
------------------------------------------------------------------------------------------------------------------------------

To install the latest development version of Kueue in your cluster, run the following command:

```
kubectl apply --server-side -k "github.com/kubernetes-sigs/kueue/config/default?ref=main"
```

The controller runs in the `kueue-system` namespace.

### Uninstall [](https://kueue.sigs.k8s.io/docs/installation/#uninstall-1)

To uninstall Kueue, run the following command:

```
kubectl delete -k "github.com/kubernetes-sigs/kueue/config/default?ref=main"
```

Build and install from source [](https://kueue.sigs.k8s.io/docs/installation/#build-and-install-from-source)
------------------------------------------------------------------------------------------------------------

To build Kueue from source and install Kueue in your cluster, run the following commands:

```
git clone https://github.com/kubernetes-sigs/kueue.git
cd kueue
IMAGE_REGISTRY=registry.example.com/my-user make image-local-push deploy
```

### Add metrics scraping for prometheus-operator [](https://kueue.sigs.k8s.io/docs/installation/#add-metrics-scraping-for-prometheus-operator-1)

To allow [prometheus-operator](https://github.com/prometheus-operator/prometheus-operator) to scrape metrics from kueue components, run the following command:

```
make prometheus
```

### Uninstall [](https://kueue.sigs.k8s.io/docs/installation/#uninstall-2)

To uninstall Kueue, run the following command:

```
make undeploy
```

Install via Helm [](https://kueue.sigs.k8s.io/docs/installation/#install-via-helm)
----------------------------------------------------------------------------------

To install and configure Kueue with [Helm](https://helm.sh/), follow the [instructions](https://github.com/kubernetes-sigs/kueue/blob/main/charts/kueue/README.md).

Change the feature gates configuration [](https://kueue.sigs.k8s.io/docs/installation/#change-the-feature-gates-configuration)
------------------------------------------------------------------------------------------------------------------------------

Kueue uses a similar mechanism to configure features as described in [Kubernetes Feature Gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates).

You can edit the `kueue-manager-config``ConfigMap` and add the feature gate you would like to manage, for example:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: kueue-manager-config
  namespace: kueue-system
data:
  controller_manager_config.yaml: |
    apiVersion: config.kueue.x-k8s.io/v1beta1
    kind: Configuration
    featureGates:
      ManagedJobsNamespaceSelectorAlwaysRespected: true
  ...
```

After changing the `ConfigMap`, you need to restart the `kueue-controller-manager` deployment to have the change enforced, for example using: `kubectl rollout restart deploy kueue-controller-manager -n kueue-system`.

Alternatively, you can edit the `kueue-controller-manager` deployment within the kueue installation namespace and change the `manager` container arguments to include

```
--feature-gates=...,<FeatureName>=<true|false>
```

For example, to enable `PartialAdmission`, you should change the manager deployment as follows:

```
kind: Deployment
...
spec:
  ...
  template:
    ...
    spec:
      containers:
      - name: manager
        args:
        - --config=/controller_manager_config.yaml
        - --zap-log-level=2
+       - --feature-gates=PartialAdmission=true
```

### Feature gates for alpha and beta features [](https://kueue.sigs.k8s.io/docs/installation/#feature-gates-for-alpha-and-beta-features)

| Feature | Default | Stage | Since | Until |
| --- | --- | --- | --- | --- |
| `AdmissionFairSharing` | `false` | Alpha | 0.12 | 0.15 |
| `AdmissionFairSharing` | `true` | Beta | 0.15 | — |
| `DynamicResourceAllocation` | `false` | Alpha | 0.14 | — |
| `ElasticJobsViaWorkloadSlices` | `false` | Alpha | 0.13 | — |
| `FailureRecoveryPolicy` | `false` | Alpha | 0.15 | — |
| `FlavorFungibility` | `true` | Beta | 0.5 | — |
| `HierarchicalCohorts` | `true` | Beta | 0.11 | — |
| `LendingLimit` | `false` | Alpha | 0.6 | 0.9 |
| `LendingLimit` | `true` | Beta | 0.9 | — |
| `LocalQueueDefaulting` | `false` | Alpha | 0.10 | 0.12 |
| `LocalQueueDefaulting` | `true` | Beta | 0.12 | — |
| `LocalQueueMetrics` | `false` | Alpha | 0.10 | — |
| `ManagedJobsNamespaceSelectorAlwaysRespected` | `false` | Alpha | 0.13 | 0.15 |
| `ManagedJobsNamespaceSelectorAlwaysRespected` | `true` | Beta | 0.15 | — |
| `MultiKueue` | `false` | Alpha | 0.6 | 0.9 |
| `MultiKueue` | `true` | Beta | 0.9 | — |
| `MultiKueueAdaptersForCustomJobs` | `false` | Alpha | 0.14 | 0.15 |
| `MultiKueueAdaptersForCustomJobs` | `true` | Beta | 0.15 | — |
| `MultiKueueAllowInsecureKubeconfigs` | `false` | Alpha | 0.15 | — |
| `MultiKueueBatchJobWithManagedBy` | `false` | Alpha | 0.8 | 0.15 |
| `MultiKueueBatchJobWithManagedBy` | `true` | Beta | 0.15 | — |
| `MultiKueueClusterProfile` | `false` | Alpha | 0.15 | — |
| `MultiKueueRedoAdmissionOnEvictionInWorker` | `true` | Beta | 0.16 | — |
| `MultiKueueWaitForWorkloadAdmitted` | `true` | Beta | 0.16 | — |
| `ObjectRetentionPolicies` | `false` | Alpha | 0.12 | 0.13 |
| `ObjectRetentionPolicies` | `true` | Beta | 0.13 | — |
| `PartialAdmission` | `false` | Alpha | 0.4 | 0.5 |
| `PartialAdmission` | `true` | Beta | 0.5 | — |
| `PrioritySortingWithinCohort` | `true` | Beta | 0.6 | — |
| `PropagateBatchJobLabelsToWorkload` | `true` | Beta | 0.15 | — |
| `ReclaimablePods` | `true` | Beta | 0.15 | — |
| `SanitizePodSets` | `true` | Beta | 0.13 | — |
| `SkipFinalizersForPodsSuspendedByParent` | `true` | Beta | 0.16 | — |
| `TASBalancedPlacement` | `false` | Alpha | 0.15 | — |
| `TASFailedNodeReplacement` | `false` | Alpha | 0.12 | 0.14 |
| `TASFailedNodeReplacement` | `true` | Beta | 0.14 | — |
| `TASFailedNodeReplacementFailFast` | `false` | Alpha | 0.13 | 0.14 |
| `TASFailedNodeReplacementFailFast` | `true` | Beta | 0.14 | — |
| `TASProfileLeastFreeCapacity` | `false` | Alpha | 0.10 | 0.11 |
| `TASProfileMixed` | `false` | Alpha | 0.10 | 0.15 |
| `TASProfileMixed` | `true` | Beta | 0.15 | — |
| `TASReplaceNodeOnPodTermination` | `false` | Alpha | 0.13 | 0.14 |
| `TASReplaceNodeOnPodTermination` | `true` | Beta | 0.14 | — |
| `TLSOptions` | `true` | Beta | 0.16 | — |
| `TopologyAwareScheduling` | `false` | Alpha | 0.9 | 0.14 |
| `TopologyAwareScheduling` | `true` | Beta | 0.14 | — |
| `VisibilityOnDemand` | `false` | Alpha | 0.6 | 0.9 |
| `VisibilityOnDemand` | `true` | Beta | 0.9 | — |
| `WorkloadRequestUseMergePatch` | `false` | Alpha | 0.14 | — |

### Feature gates for graduated or deprecated features [](https://kueue.sigs.k8s.io/docs/installation/#feature-gates-for-graduated-or-deprecated-features)

| Feature | Default | Stage | Since | Until |
| --- | --- | --- | --- | --- |
| `TASProfileLeastFreeCapacity` | `false` | Deprecated | 0.11 | — |

What’s next [](https://kueue.sigs.k8s.io/docs/installation/#whats-next)
-----------------------------------------------------------------------

*   Read the [API reference](https://kueue.sigs.k8s.io/docs/reference/kueue-config.v1beta1/#Configuration) for `Configuration`

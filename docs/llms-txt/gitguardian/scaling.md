# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/scaling.md

# Scaling

> Configure resource scaling for GitGuardian self-hosted deployments, including replicas, CPU, and memory for different workload types.

## Application topology

GitGuardian application consists of several Kubernetes resources. Here are key aspects based on the installation type:

  - **KOTS-based Installations**: Allows configuration of replicas, CPU, and memory requests/limits for main deployments/pods.
  - **Helm-based Installations**: Provides more comprehensive customization, including:
    - Creation of new classes of workers.
    - Customization of other resource types such as ephemeral storage, huge pages, etc.
    - Setting nodeSelector, tolerations, and additional configurations.

For detailed insights into deployment/pod names, types, and their usage, visit the [GitGuardian Application Topology](../../troubleshoot/topology) page.

## Scaling for GitGuardian: Historical Scans, Real-Time Scans, Public API and ML Secret Engine

When using GitGuardian for monitoring repositories, it's crucial to scale the resources appropriately for historical scans, real-time scans, and public API requests. This ensures efficient and timely processing regardless of the load. These recommendations are only for **[existing cluster installations](../../installation/choose-embedded-existing#what-is-an-existing-cluster-installation)**.

### General Guidelines

:::tip Performing your first Historical Scans
When you add a high number of sources, consider temporarily increasing the number of pods for the time of the initial historical scan. Afterward, you can decrease those pods' replicas and resources.
:::

When performing [a historical scan](../../../internal-monitoring/integrate-sources/monitored-perimeter#historical-scanning) on a git repository, GitGuardian clones the repository on the pod's ephemeral storage and will traverse all branches and commits in search of potential secrets. The full scan is done by a single Pod and can last from a few seconds to many hours depending on the repository size. The more pods you'll add, the more historical scans can be done concurrently. When sizing your nodes, keep in mind that each Pod must have enough ephemeral storage and memory to run. **To improve performance and reduce scan times, it is recommended to use SSD disks for the ephemeral storage.**

For real-time scans, these are triggered by `Push` events sent by the VCS to GitGuardian. These scans typically complete in under a second and should always be under 3 seconds. To handle peaks of pushes, you may want to increase the count of `worker-worker` Pods that are processing real-time scans.

The public API, used mainly by [ggshield](../../../platform/gitguardian-suite/gitguardian-cli-ggshield), is deployed under the `webapp-public_api` pod. This pod is essential for enabling interactions between ggshield and GitGuardian. To ensure the public API can handle the expected traffic, you may need to adjust the number of `webapp-public_api` Pods.

The `webapp-internal_api` pods handle internal requests for the Dashboard, while the `webapp-internal_api_long` pods manage longer-running operations, ensuring reliable performance and preventing timeouts during extended tasks.

Adjust the number of pods and node capacity according to the size and number of repositories, expected volume of push events, and expected volume of API requests to ensure efficient and effective scanning and interactions.

To avoid manual scaling, you may be interested in autoscaling to adapt dynamically to the load, see [Autoscaling](./autoscaling.md).

#### Container Registry Scanning Considerations

- **Replica Configuration**: By default, container registry replicas are set to 0, causing container registry scanning to fall back to using scanner workers. It is recommended to configure this to a non-zero replica count for dedicated container registry scanning performance.
- **Cache Usage**: Consumes significant Redis memory and database storage (several GB). Consider scaling Redis or using a dedicated instance.
- **Database Pressure**: Scanner pods can pressure the database, especially during initial scans. Scale carefully with the recommended minimum replica counts.
- **Data Transfer Costs**: Scanning large registries can result in high network transfer costs. Start with a few repositories to evaluate costs before scaling to full scan.

#### Check Runs Considerations

- **Replica Configuration**: By default, check runs replicas are set to 0, causing check run processing to be handled by `worker-worker`. If you experience high volumes of GitHub check runs, you can enable dedicated `worker-check-runs` pods by setting `celeryWorkers.check-runs.replicas` to offload the `check_run` queue from `worker-worker`.

#### Slack Scanning Considerations

- **Replica Configuration**: By default, Slack scanners replicas are set to 0, causing Slack registry scanning to fall back to using scanner workers. It is recommended to configure this to a non-zero replica count for dedicated Slack registry scanning performance. Configuring a large number of replicas is unnecessary, as Slack scanning is restricted to one channel at a time due to Slack API rate limits.

#### Binary Files Scanning Considerations

Binary Files Scanning is currently only available for Microsoft Sharepoint Online and 
Microsoft OneDrive.
When performing an historical scan on sources containing binary files, the files will be downloaded locally on the pod ephemeral storage. **To improve performance and reduce scan times, it is recommended to use SSD disks for the ephemeral storage and to provision enough ephemeral storage for these pods (100GB).**

#### Package Registry Scanning Considerations

- **Replica Configuration**: `scanners-db-less.replicas` must be set to a value greater than 0 for JFrog Package Registries, SharePoint, and OneDrive integrations. By default, replicas are set to 0.
- **Cache Usage**: The `commit-cache` Redis instance is used for JFrog Package Registries scanning. If `commit-cache` is not configured, the main Redis instance will be used instead.

#### ML Secret Engine Scaling Considerations

The ML Secret Engine requires specific resource allocation and scaling considerations. For detailed setup instructions, see the [Machine Learning documentation](../application-management/machine-learning).

- **Per-pod resources**: 3 vCPU and 2.5 GiB RAM each.
- **Instance recommendation**: Use AWS Gen 7 Intel (M7i) instances with amd64 architecture. CPU-only instances are far more cost-effective than GPU instances (g4dn/p3) for ML analysis.
- **Scaling**: Use the sizing recommendations below (Small/Medium/Large) as baseline configuration. For dynamic scaling during backfills, consider configuring [Horizontal Pod Autoscaling (HPA)](./autoscaling) for the `ml-api-priority` worker.

#### Analytics (in beta)

[Advanced Analytics](../../../platform/analytics/internal-monitoring) requires additional resources when enabled. The job executes once a day and has the following default resource configuration:

- **Memory request**: 8 GB
- **Memory limit**: 12 GB
- **Database usage increase**: 15-20% (minimum 5-6 GB)

Plan your cluster and database capacity accordingly.

### Small

#### Core System Components

For up to 2000 repositories, handling up to 500 pushes per hour, and up to 1000 API requests per hour:

| Component                | Required Capacity                                                                              | Count |
| :----------------------- | :--------------------------------------------------------------------------------------------- | :---- |
| Kubernetes compute nodes | 4 vCPU  16 GB memory  50 GB ephemeral disk space, 10 GB persistent disk space        | 3     |
| PostgreSQL Master        | 4 vCPU  8 GB memory  200 GB disk space                                               | 1     |
| Redis                    | 2 vCPU  2 GB memory  20 GB disk space                                                | 1     |
| **Total**                | **18 vCPU  58 GB memory  150 GB ephemeral disk space, 250 GB persistent disk space** | **5** |

If you plan to use global ephemeral storage, add 20 GB to the persistent disk space on each of your Kubernetes compute nodes.

#### Historical Scans (up to 5GB in size)

| Component              | Required Capacity              | Count |
| :--------------------- | :----------------------------- | :---- |
| `worker-scanners` Pods | Memory request and limit: 6 GB | 4     |

#### Real-Time Scans (up to 500 pushes/h)

| Component            | Required Capacity         | Count |
| :------------------- | :------------------------ | :---- |
| `worker-worker` Pods | Default resource settings | 2     |

#### Public API (up to 1k requests/h)

| Component                        | Required Capacity         | Count |
| :------------------------------- | :------------------------ | :---- |
| `webapp-public_api` Pods         | Default resource settings | 2     |
| `nginx` (dashboard and API) Pods | Default resource settings | 2     |

#### Dashboard (up to 200 active users)

| Component                       | Required Capacity         | Count |
| :------------------------------ | :------------------------ | :---- |
| `webapp-internal_api` Pods      | Default resource settings | 2     |
| `webapp-internal_api_long` Pods | Default resource settings | 2     |

#### Machine learning (up to 500 events/h)

| Component                     | Required Capacity         | Count |
| :---------------------------- | :------------------------ | :---- |
| `ml-secret-engine` Pods       | Default resource settings | 1     |
| `worker-ml-api-priority` Pods | Default resource settings | 1     |

#### Historical Scans and Real-Time Scans for Container registries

| Component                          | Required Capacity              | Count |
|:-----------------------------------|:-------------------------------|:------|
| `worker-container-registries` Pods | Memory request and limit: 4 GB | 2     |

#### Historical Scans for Slack

| Component                          | Required Capacity              | Count |
|:-----------------------------------|:-------------------------------|:------|
| `worker-scanners-slack` Pods       | Default resource settings      | 1     |

#### Historical Scans for Sharepoint / OneDrive

| Component                          | Required Capacity              | Count |
|:-----------------------------------|:-------------------------------|:------|
| `worker-scanners-ods-highdisk` Pods | Default resource settings      | 1     |
| `apacheTika` Pods                  | Default resource settings      | 1     |

#### Package Registry Scanning

| Component                          | Required Capacity              | Count |
|:-----------------------------------|:-------------------------------|:------|
| `worker-scanners-db-less` Pods     | Default resource settings      | 1     |

### Medium

#### Core System Components

For up to 10000 repositories, handling up to 1000 pushes per hour, and up to 25000 API requests per hour:

| Component                | Required Capacity                                                                               | Count |
| :----------------------- | :---------------------------------------------------------------------------------------------- | :---- |
| Kubernetes compute nodes | 8 vCPU  32 GB memory  50 GB ephemeral disk space, 10 GB persistent disk space         | 5     |
| PostgreSQL Master        | 8 vCPU  32 GB memory  250 GB disk space                                               | 1     |
| Redis                    | 4 vCPU  8 GB memory  40 GB disk space                                                 | 1     |
| **Total**                | **52 vCPU  200 GB memory  250 GB ephemeral disk space, 340 GB persistent disk space** | **7** |

If you plan to use global ephemeral storage, add 120 GB to the persistent disk space on each of your Kubernetes compute nodes.

#### Historical Scans (up to 10GB in size)

| Component              | Required Capacity               | Count |
| :--------------------- | :------------------------------ | :---- |
| `worker-scanners` Pods | Memory request and limit: 11 GB | 12    |

#### Real-Time Scans (up to 1k pushes/h)

| Component            | Required Capacity         | Count |
| :------------------- | :------------------------ | :---- |
| `worker-worker` Pods | Default resource settings | 4     |

#### Public API (up to 25k requests/h)

| Component                        | Required Capacity         | Count |
| :------------------------------- | :------------------------ | :---- |
| `webapp-public_api` Pods         | Default resource settings | 4     |
| `nginx` (dashboard and API) Pods | Default resource settings | 2     |

#### Dashboard (up to 500 active users)

| Component                       | Required Capacity         | Count |
| :------------------------------ | :------------------------ | :---- |
| `webapp-internal_api` Pods      | Default resource settings | 4     |
| `webapp-internal_api_long` Pods | Default resource settings | 2     |

#### Machine learning (up to 1k events/h)

| Component                     | Required Capacity         | Count |
| :---------------------------- | :------------------------ | :---- |
| `ml-secret-engine` Pods       | Default resource settings | 2     |
| `worker-ml-api-priority` Pods | Default resource settings | 2     |

#### Historical Scans for Slack

| Component                          | Required Capacity              | Count |
|:-----------------------------------|:-------------------------------|:------|
| `worker-scanners-slack` Pods       | Default resource settings      | 2     |

#### Historical Scans for Sharepoint / OneDrive

| Component                          | Required Capacity                 | Count |
|:-----------------------------------|:----------------------------------|:------|
| `worker-scanners-ods-highdisk` Pods | Memory request, limit: 4GiB, 6GiB | 4     |
| `apacheTika` Pods                   | Default resource settings         | 2     |

#### Package Registry Scanning

| Component                          | Required Capacity              | Count |
|:-----------------------------------|:-------------------------------|:------|
| `worker-scanners-db-less` Pods     | Default resource settings      | 2     |

### Large

#### Core System Components

For up to 40000 repositories, handling up to 2000 pushes per hour, and up to 50000 API requests per hour:

| Component                | Required Capacity                                                                               | Count  |
| :----------------------- | :---------------------------------------------------------------------------------------------- | :----- |
| Kubernetes compute nodes | 8 vCPU  64 GB memory  50 GB ephemeral disk space, 10 GB persistent disk space         | 7      |
| PostgreSQL Master        | 16 vCPU  64 GB memory  300 GB disk space                                              | 1      |
| Redis                    | 8 vCPU  16 GB memory  100 GB disk space                                               | 1      |
| **Total**                | **80 vCPU  528 GB memory  350 GB ephemeral disk space, 470 GB persistent disk space** | **9**  |

If you plan to use global ephemeral storage, add 160 GB to the persistent disk space on each of your Kubernetes compute nodes.

#### Historical Scans (up to 15GB in size)

| Component                  | Required Capacity               | Count |
|:---------------------------|:--------------------------------|:------|
| `worker-scanners` Pods     | Memory request and limit: 16 GB | 16    |
| `worker-scanners-ods` Pods | Memory request and limit: 4 GB  | 10    |

Define specific `worker-scanners-ods` pods especially if you integrate large Slack or MS Teams instances (5k+ channels). It's better to isolate these workloads.
Otherwise, it's fine to share the same queue and workers with the `worker-scanners` workload.

#### Real-Time Scans (up to 2k pushes/h)

| Component            | Required Capacity         | Count |
| :------------------- | :------------------------ | :---- |
| `worker-worker` Pods | Default resource settings | 8     |

#### Public API (up to 50k requests/h)

| Component                        | Required Capacity         | Count |
| :------------------------------- | :------------------------ | :---- |
| `webapp-public_api` Pods         | Default resource settings | 6     |
| `nginx` (dashboard and API) Pods | Default resource settings | 2     |

#### Dashboard (up to 1k active users)

| Component                       | Required Capacity         | Count |
| :------------------------------ | :------------------------ | :---- |
| `webapp-internal_api` Pods      | Default resource settings | 6     |
| `webapp-internal_api_long` Pods | Default resource settings | 2     |

#### Machine learning (up to 2k events/h)

| Component                     | Required Capacity         | Count |
| :---------------------------- | :------------------------ | :---- |
| `ml-secret-engine` Pods       | Default resource settings | 2     |
| `worker-ml-api-priority` Pods | Default resource settings | 2     |

#### Historical Scans for Slack

| Component                          | Required Capacity              | Count |
|:-----------------------------------|:-------------------------------|:------|
| `worker-scanners-slack` Pods       | Default resource settings      | 2     |

#### Historical Scans for Sharepoint / OneDrive

| Component                          | Required Capacity                 | Count |
|:-----------------------------------|:----------------------------------|:------|
| `worker-scanners-ods-highdisk` Pods | Memory request, limit: 4GiB, 6GiB | 4     |
| `apacheTika` Pods                   | Default resource settings         | 2     |

#### Package Registry Scanning

| Component                          | Required Capacity              | Count |
|:-----------------------------------|:-------------------------------|:------|
| `worker-scanners-db-less` Pods     | Default resource settings      | 4     |

## Configure scaling settings

You may size your infrastructure according to the above recommendations but you may also use Kubernetes autoscaling to adapt dynamically to the load, see [Autoscaling](./autoscaling.md).

### KOTS-based installation

:::caution
Ensure that you update the **[Kubernetes Application RBAC](../../installation/installation-existing-cluster-kots#kubernetes-application-rbac)** by adding the `patch` permission to the `servicemonitors` resource.
:::

Navigate under **Config > Scaling** in the [KOTS Admin Console](./admin-console), you will have access to the worker scaling options.

- **Front replicas**: Scale `nginx` pods.
- **API replicas**: Scale `api` pods.
- **Workers replicas**: Scale `workers` pods (including the `scanners` pods)

:::info
Changing these values doesn't affect the rollout upgrade strategy.
Workers are configured to spread across nodes if there are multiple nodes.
If you have configured your cluster for high availability, do not use less than 2 workers of each type.
:::

**Non-VCS Sources Integration:**

For non-VCS integrations (messaging, documentation, ticketing, and container registries), worker configuration varies by integration type:

- Some integrations can optionally use generic VCS workers but benefit from dedicated workers
- Others require their own specialized workers and cannot share VCS workers
- By default, all non-VCS source workers are deactivated (replicas set to 0)

For detailed configuration instructions, worker requirements, and activation steps, see the [Non-VCS Sources](../application-management/non-vcs-sources) documentation.

This scaling page focuses on performance optimization after initial activation.

### Helm-based installation

Customize Helm applications using your `local-values.yaml` file, submitted with the `helm` command.

Configure deployments with `replicas`: `use webapps.[name].replicas` for web pods, `celeryWorkers.[name].replicas`
for async workers and `secretEngine.replicas` for Machine Learning Secret Engine. Additionally, set resources `requests` and `limits` as needed.

**Example**

```yaml
migration:
  # Set resources for pre-deploy and post-deploy jobs
  resources:
    limits:
      cpu: 1000m
      memory: 500Mi
front:
  nginx:
    # Set resources for nginx init containers
    init:
      resources:
        limits:
          cpu: 1000m
          memory: 500Mi
    replicas: 2
    resources:
      limits:
        memory: 1Gi
webapps:
  public_api:
    replicas: 5
    resources:
      requests:
        cpu: 200m
        memory: 500Mi
      limits:
        memory: 4Gi
celeryWorkers:
  scanners:
    replicas: 8
    resources:
      requests:
        cpu: 200m
        memory: 4Gi
      limits:
        memory: 16Gi
secretEngine:
  replicas: 2
```

See [the values reference documentation](./helm-values) for further details.

:::tip Scaling Recommendation
For optimal performance, consider scaling the following pods to a minimum of 2 replicas each: `hook`, `internal-api-long`, `public-api`, `worker-email`, `worker-long`, and `worker-worker`.
:::

## Additional tuning ephemeral storage

:::info
Only available for **[helm-based installations](../../installation/installation-existing-cluster-helm)**.
:::

In certain scenarios, optimizing ephemeral storage configurations becomes essential for achieving better performance and stability, particularly for `scanners` workers. This section outlines additional configurations for fine-tuning ephemeral storage, focusing on leveraging "On Demand" nodes with nvme disks and integrating Generic Ephemeral Inline Volumes.

### "On Demand" nodes with nvme disks

In the following example, we specify that `scanners` workers only use "On Demand" VMs with nvme disks and that pods'
ephemeral storage will use these disks

```yaml
celeryWorkers:
  scanners:
    replicas: 8
    localStoragePath: /nvme/disk # Used for pods ephemeral storage
    nodeSelector: # Must run on "On Demand" nodes with nvme disks
      eks.amazonaws.com/capacityType: ON_DEMAND
      local-nvme-ready: 'true'
    tolerations:
      - key: worker-highdisk
        operator: Equal
        value: 'true'
        effect: NoSchedule
    resources:
      requests:
        cpu: 200m
        memory: 16Gi
      limits:
        memory: 16Gi
```

### Generic Ephemeral Inline Volumes

In the following example, we leverage Kubernetes' Generic Ephemeral Inline Volumes within Helm charts. This feature facilitates dynamic provisioning and reclamation of storage, particularly beneficial when dealing with small limits on Ephemeral storage. Note that it's supported starting Kubernetes 1.23 ([learn more](https://docs.openshift.com/container-platform/4.15/storage/generic-ephemeral-vols.html)).

```yaml
celeryWorkers:
  scanners:
    replicas: 8
    resources:
      requests:
        cpu: 200m
        memory: 4Gi
      limits:
        memory: 16Gi
    # -- Worker ephemeral storage
    ephemeralStorage:
      enabled: true
      size: 2Gi
```

### Node Affinity Scheduling

Use the nodeSelector parameter in Helm values to schedule worker pods on specific nodes, ensuring they run in designated zones or meet specific criteria ([learn more](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/#create-a-pod-that-gets-scheduled-to-your-chosen-node)).

```yaml
celeryWorkers:
  long:
    nodeSelector:
      topology.kubernetes.io/zone: eu-central-1c
  scanners:
    nodeSelector:
      topology.kubernetes.io/zone: eu-central-1c
  worker:
    nodeSelector:
      topology.kubernetes.io/zone: eu-central-1c
```

### Pod Anti-Affinity

GitGuardian's Helm chart provides configurable pod anti-affinity settings to control how pods are distributed across your Kubernetes cluster nodes. This feature allows you to optimize availability and resource utilization by ensuring pods are spread evenly across different nodes and availability zones.

**Default configuration:**

By default, the chart applies a `podAntiAffinityPreset: soft` configuration for webApps and workers. This `soft` anti-affinity preference attempts to distribute pods across nodes but does not guarantee uniform distribution. The scheduler will try to place pods on different nodes when possible, but will still schedule pods even if the preferred distribution cannot be achieved.

**Hardened Configuration:**

For environments requiring guaranteed uniform pod distribution, you can specify `podAntiAffinityPreset: hard`. This configuration enforces strict anti-affinity rules that ensure pods are evenly distributed across:

- Availability zones (topology key: `topology.kubernetes.io/zone`)
- Individual nodes (topology key: `kubernetes.io/hostname`)

To enable hard pod anti-affinity for the scanner worker component, configure your Helm values as follows:

```yaml
celeryWorkers:
  scanners:
    replicas: 10
    podAntiAffinityPreset: hard
```

This configuration will ensure that each scanner worker pod runs on a different node, providing maximum distribution and fault tolerance.

**Node Capacity Requirements:**

`hard` anti-affinity preset requires that you have sufficient nodes in your cluster to satisfy the desired number of replicas. If your cluster does not have enough nodes to accommodate all pods with the strict anti-affinity rules, some pods will remain in a "**Pending**" state until additional nodes become available.
For example, if you configure 10 replicas with hard anti-affinity but only have 8 available nodes, 2 pods will remain pending until more nodes are added to the cluster.

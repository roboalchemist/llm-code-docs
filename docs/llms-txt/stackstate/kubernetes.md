# Source: https://archivedocs.stackstate.com/5.1/stackpacks/integrations/kubernetes.md

# Kubernetes

## Overview

The Kubernetes integration is used to create a near real-time synchronization of topology and associated internal services from a Kubernetes cluster to StackState. This StackPack allows monitoring of the following:

* Workloads
* Nodes, pods, containers and services
* Configmaps, secrets and volumes

Kubernetes is a [StackState core integration](https://archivedocs.stackstate.com/5.1/stackpacks/about_integrations#stackstate-core-integrations).

![Data flow](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-4fc3f6f7a289da825adb8ce834c40d3242e6e938%2Fstackpack-kubernetes.svg?alt=media)

The Kubernetes integration collects topology data in a Kubernetes cluster as well as metrics and events.

* Data is retrieved by the deployed [StackState Agents](https://archivedocs.stackstate.com/5.1/setup/agent/kubernetes-openshift#agent-types) and then pushed to StackState via the Agent StackPack and the Kubernetes StackPack.
* In StackState:
  * [Topology data](#topology) is translated into components and relations.
  * [Tags](#tags) defined in Kubernetes are added to components and relations in StackState.
  * [Metrics data](#metrics) is stored and accessible within StackState. Relevant metrics data is mapped to associated components and relations in StackState.
  * [Kubernetes events](#events) are available in the StackState UI Events Perspective. They're also included in the **Event** list in the right panel **View summary** tab and the details tabs - **Component details** and **Direct relation details**.
  * [Object change events](#events) are created for every detected change to `spec` or `metadata` in Kubernetes objects

## Setup

### Prerequisites

The following prerequisites are required to install the Kubernetes StackPack and deploy the StackState Agent and Cluster Agent:

* A Kubernetes Cluster must be up and running.
* A recent version of Helm 3.
* A user with permissions to create privileged pods, ClusterRoles and ClusterRoleBindings:
  * ClusterRole and ClusterRoleBinding are needed to grant StackState Agents permissions to access the Kubernetes API.
  * StackState Agents need to run in a privileged pod to be able to gather information on network connections and host information.

### Supported container runtimes

From StackState Agent V2.16, the following container runtimes are supported:

* containerd
* CRI-O
* Docker

Note that versions of StackState Agent prior to v2.16 support the Docker container runtime only.

### Install

Install the Kubernetes StackPack from the StackState UI **StackPacks** > **Integrations** screen. You will need to enter the following details:

* **Kubernetes Cluster Name** - A name to identify the cluster. This doesn't need to match the cluster name used in `kubeconfig`, however, that's usually a good candidate for a unique name.

If the Agent StackPack isn't already installed, this will be automatically installed together with the Kubernetes StackPack. StackState requires the Agent StackPack to work with the StackState Agent, which will need to be deployed on each node in the Kubernetes cluster.

### Deploy: Agent and Cluster Agent

For the Kubernetes integration to retrieve topology, events and metrics data, you will need to have the following installed on your Kubernetes cluster:

* StackState Agent V3 on each node in the cluster
* StackState Cluster Agent on one node
* StackState Checks Agent on one node
* kube-state-metrics

➡️ [Deploy StackState Agents and kube-state-metrics](https://archivedocs.stackstate.com/5.1/setup/agent/kubernetes-openshift).

{% hint style="info" %}
To integrate with other services, a separate instance of the [StackState Agent](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent) should be deployed on a standalone VM. It isn't currently possible to configure a StackState Agent deployed on a Kubernetes cluster with checks that integrate with other services.
{% endhint %}

### Configure kube-state-metrics (stackstate/stackstate-agent helm chart versions prior to and including version 3.3.0)

The kubernetes\_state check is responsible for gathering metrics from kube-state-metrics and sending them to StackState. The kubernetes\_state check runs in the [StackState Checks Agent](https://archivedocs.stackstate.com/5.1/setup/agent/kubernetes-openshift#checks-agent) by default and is configured in the [StackState Cluster Agent](https://archivedocs.stackstate.com/5.1/setup/agent/kubernetes-openshift#cluster-agent).

The default URL that the kubernetes\_state check uses is:

```
http://<release-name>-kube-state-metrics.<namespace>.svc.cluster.local:8080/metrics
```

If an alternative kube-state-metrics pod (i.e. Prometheus) is installed, the default StackState kube-state-metrics pod can be disabled and the kubernetes\_state check redirected to the alternative service:

1. Update the `values.yaml` file used to deploy the `checks-agent`, for example:

   ```yaml
   dependencies:
     kubeStateMetrics:
       enabled: false
   checksAgent:
     kubeStateMetrics:
       url: http://YOUR_KUBE_STATE_METRICS_SERVICE_NAME:8080/metrics
   ```
2. Deploy the `cluster_agent` using the updated `values.yaml`:

   ```yaml
   helm upgrade --install \
   --namespace stackstate \
   --create-namespace \
   --set-string 'stackstate.apiKey'='<STACKSTATE_RECEIVER_API_KEY>' \
   --set-string 'stackstate.cluster.name'='<KUBERNETES_CLUSTER_NAME>' \
   --set-string 'stackstate.cluster.authToken=<CLUSTER_AUTH_TOKEN>' \
   --set-string 'stackstate.url'='<STACKSTATE_RECEIVER_API_ADDRESS>' \
   --values values.yaml \
   stackstate-agent stackstate/stackstate-agent
   ```

### Configure kube-state-metrics (stackstate/stackstate-agent helm chart versions later than and including version 3.5.0)

The kube\_state\_metrics Python integration has been deprecated and removed in favour of the kube\_state\_core check. The key difference lies in the deployment of the helm chart. There is no longer a need for running a kube\_state\_state\_metrics pod, as the kube\_state\_core check is now part of the StackState Agent. The kube\_state\_core check queries the relevant Kubernetes api endpoints directly, and sends the metrics to StackState, without the need for a separate kube-state-metrics pod. It is therefore also no longer required to set a value for the kubeStateMetrics.url in the values.yaml file.

If an alternative kube-state-metrics pod (i.e. Prometheus) is installed, it can remain and will not be affected by the agent deployment.

### Status

To check the status of the Kubernetes integration, check that the StackState Cluster Agent (`cluster-agent`) pod, StackState Checks Agent pod (`checks-agent`) and all of the StackState Agent (`node-agent`) pods have status ready.

```
❯ kubectl get deployment,daemonset --namespace stackstate

NAME                                                 READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/stackstate-agent-cluster-agent       1/1     1            1           5h14m
deployment.apps/stackstate-agent-checks-agent        1/1     1            1           5h14m
NAME                                                 DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
daemonset.apps/stackstate-agent-node-agent           10        10        10      10           10          <none>          5h14m
```

## Integration details

### Data retrieved

The Kubernetes integration retrieves the following data:

* [Events](#events)
* [Metrics](#metrics)
* [Tags](#tags)
* [Topology](#topology)

#### Events

* All [Kubernetes events](#kubernetes-events) are retrieved from the Kubernetes cluster.
* StackState `Element Properties Change` events will be generated for [changes detected in a Kubernetes object](#object-change-events).

**Kubernetes events**

The Kubernetes integration retrieves all events from the Kubernetes cluster. The table below shows which event category will be assigned to each event type in StackState:

| StackState event category | Kubernetes events                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Activities**            | `BackOff` `ContainerGCFailed` `ExceededGracePeriod` `FileSystemResizeSuccessful` `ImageGCFailed` `Killing` `NodeAllocatableEnforced` `NodeNotReady` `NodeSchedulable` `Preempting` `Pulling` `Pulled` `Rebooted` `Scheduled` `Starting` `Started` `SuccessfulAttachVolume` `SuccessfulDetachVolume` `SuccessfulMountVolume` `SuccessfulUnMountVolume` `VolumeResizeSuccessful` |
| **Alerts**                | `NotTriggerScaleUp`                                                                                                                                                                                                                                                                                                                                                            |
| **Changes**               | `Created` (created container) `NodeReady` `SandboxChanged` `SuccessfulCreate` `SuccessfulDelete` `Completed`                                                                                                                                                                                                                                                                   |
| **Others**                | All other events                                                                                                                                                                                                                                                                                                                                                               |

**Object change events**

The Kubernetes integration will detect changes in Kubernetes objects and will create an event of type `Element Properties Change` with a diff with a YAML representation of the changed object.

![Element Properties Change event](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-ca0782eba4a6fe0bb2f09175b5b5e687933443ba%2Fk8s-change-event.png?alt=media)

Changes will be detected in the following object types:

* `ConfigMap`
* `CronJob`
* `DaemonSet`
* `Deployment`
* `Ingress`
* `Job`
* `Namespace`
* `Node`
* `PersistentVolume`
* `Pod`
* `ReplicaSet`
* `Secret` (a hash of the content will be compared)
* `Service`
* `StatefulSet`

{% hint style="info" %}
Note that, to reduce noise of changes, the following object properties **won't** be compared:

* `metadata`
  * `managedFields`
  * `resourceVersion`
  * `annotations`
    * `kubectl.kubernetes.io/last-applied-configuration`
* `status` (except for `Node`, `Pod` and `PersistentVolume` objects)
  {% endhint %}

You can also see the current [or past](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/timeline-time-travel#topology-time) YAML definition of the object in the [Component properties](https://archivedocs.stackstate.com/5.1/use/concepts/components#component-details):

![Kubernetes Component properties](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-ddbebc2cfe302bac1b9473800e197ec9be79ecc6%2Fk8s-component-properties-yaml.png?alt=media)

#### Metrics

The Kubernetes integration makes all metrics from the Kubernetes cluster available in StackState. Relevant metrics are automatically mapped to the associated components.

All retrieved metrics can be browsed or added to a component as a telemetry stream. Select the data source **StackState Metrics** and type `kubernetes` in the **Select** box to get a full list of all available metrics.

![Add a Kubernetes metrics stream to a component](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-d29d20afb262573f52670cf60668ca52b971533c%2Fv51_add_k8s_stream.png?alt=media)

#### Topology

The Kubernetes integration retrieves components and relations for the Kubernetes cluster.

{% hint style="info" %}
**StackState Agent versions prior to 2.16:** Topology information is only gathered from Kubernetes clusters that use the Docker container runtime.
{% endhint %}

**Components**

The following Kubernetes topology data is available in StackState as components:

|            |                   |
| ---------- | ----------------- |
| Cluster    | Ingress           |
| Namespace  | Job               |
| Node       | Persistent Volume |
| Pod        | ReplicaSet        |
| Container  | Secret            |
| ConfigMap  | Service           |
| CronJob    | StatefulSet       |
| DaemonSet  | Volume            |
| Deployment |                   |

**Relations**

The following relations between components are retrieved:

* Container → PersistentVolume, Volume
* CronJob → Job
* DaemonSet → Pod
* Deployment → ReplicaSet
* Job → Pod
* Ingress → Service
* Namespace → CronJob, DaemonSet, Deployment, Job, ReplicaSet, Service, StatefulSet
* Node → Cluster relation
* Pod → ConfigMap, Container, Deployment, Node, Secret, Volume
* ReplicaSet → Pod
* Service → ExternalService, Pod
* StatefulSet → Pod
* Direct communication between processes
* Process → Process communication via Kubernetes service
* Process → Process communication via headless Kubernetes service

#### Traces

The Kubernetes integration doesn't retrieve any traces data.

#### Tags

All tags defined in Kubernetes will be retrieved and added to the associated components and relations in StackState as labels.

The following labels will also be added to imported elements as relevant:

* `image_name`
* `kube_cluster_name`
* `kube_container_name`
* `kube_cronjob`
* `kube_daemon_set`
* `kube_deployment`
* `kube_job`
* `kube_namespace`
* `kube_replica_set`
* `kube_replication_controller`
* `kube_stateful_set`
* `pod_name`
* `pod_phase`

### REST API endpoints

The StackState Agent talks to the kubelet and kube-state-metrics API.

The StackState Agent and Cluster Agent connect to the Kubernetes API to retrieve cluster wide information and Kubernetes events. The following API endpoints used:

| Resource type                                  | REST API endpoint                                                 |
| ---------------------------------------------- | ----------------------------------------------------------------- |
| Cluster > ComponentStatus                      | `GET /api/v1/componentstatuses`                                   |
| Cluster > Event                                | `GET /apis/events.k8s.io/v1/events`                               |
| Cluster > Namespace                            | `GET /api/v1/namespaces`                                          |
| Cluster > Node                                 | `GET /api/v1/nodes`                                               |
| Services > Endpoints                           | `GET /api/v1/namespaces/{namespace}/endpoints`                    |
| Services > Ingress                             | `GET /apis/networking.k8s.io/v1/namespaces/{namespace}/ingresses` |
| Services > Service                             | `GET /api/v1/namespaces/{namespace}/services`                     |
| Workloads > CronJob                            | `GET /apis/batch/v1beta1/namespaces/{namespace}/cronjobs`         |
| Workloads > DaemonSet                          | `GET /apis/apps/v1/namespaces/{namespace}/daemonsets`             |
| Workloads > Deployment                         | `GET /apis/apps/v1/namespaces/{namespace}/deployments`            |
| Workloads > Job                                | `GET /apis/batch/v1/namespaces/{namespace}/jobs`                  |
| Workloads > Pod                                | `GET /api/v1/namespaces/{namespace}/pods`                         |
| Workloads > ReplicaSet                         | `GET /apis/apps/v1/namespaces/{namespace}/replicasets`            |
| Workloads > StatefulSet                        | `GET /apis/apps/v1/namespaces/{namespace}/statefulsets`           |
| Config and Storage > ConfigMap                 | `GET /api/v1/namespaces/{namespace}/configmaps`                   |
| Config and Storage > Secret                    | `GET /api/v1/secrets`                                             |
| Config and Storage > PersistentVolume          | `GET /api/v1/persistentvolumes`                                   |
| Config and Storage > PersistentVolumeClaimSpec | `GET /api/v1/namespaces/{namespace}/persistentvolumeclaims`       |
| Config and Storage > VolumeAttachment          | `GET /apis/storage.k8s.io/v1/volumeattachments`                   |
|                                                | `/version`                                                        |
|                                                | `/healthz`                                                        |

For further details, refer to the [Kubernetes API documentation (kubernetes.io)](https://kubernetes.io/docs/reference/kubernetes-api/).

### Component actions

A number of [actions](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/topology-perspective#actions) are added to StackState when the Kubernetes StackPack is installed. They're available from the **Actions** section in the right panel details tab - **Component details** - when a Kubernetes component is selected or from the component context menu, displayed when you hover the mouse pointer over a Kubernetes component in the Topology Perspective

| Action                             | Available for component types                                                     | Description                                                                      |
| ---------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Show configuration and storage** | pods containers                                                                   | Display the selected pod or container with its configmaps, secrets and volumes   |
| **Show dependencies (deep)**       | deployment replicaset replicationcontroller statefulset daemonset job cronjob pod | Displays all dependencies (up to 6 levels deep) of the selected pod or workload. |
| **Show pods**                      | deployment replicaset replicationcontroller statefulset daemonset job cronjob     | Displays the pods for the selected workload.                                     |
| **Show pods and services**         | namespace                                                                         | Opens a view for the pods/services in the selected namespace                     |
| **Show services**                  | namespace                                                                         | Open a view for the service and ingress components in the selected namespace     |
| **Show workloads**                 | namespace                                                                         | Show workloads in the selected namespace                                         |

Details of installed actions can be found in the StackState UI **Settings** > **Actions** > **Component Actions** screen.

### Kubernetes views in StackState

When the Kubernetes integration is enabled, the following Kubernetes views are available in StackState for each cluster:

* Kubernetes - Applications -
* Kubernetes - Infrastructure -
* Kubernetes - Namespaces -
* Kubernetes - Workload Controllers -

### Open source

The code for the StackState Agent Kubernetes check is open source and available on GitHub at:

* <https://github.com/StackVista/stackstate-agent/tree/master/pkg/collector/corechecks/cluster>
* <https://github.com/stackvista/stackstate-agent>
* <https://github.com/StackVista/stackstate-agent-integrations/tree/master/kubernetes>

## Troubleshooting

Troubleshooting steps for any known issues can be found in the [StackState support Knowledge base](https://support.stackstate.com/hc/en-us/search?utf8=%E2%9C%93\&query=kubernetes).

## Uninstall

To uninstall the Kubernetes StackPack, go to the StackState UI **StackPacks** > **Integrations** > **Kubernetes** screen and click **UNINSTALL**. All Kubernetes StackPack specific configuration will be removed from StackState.

See the Kubernetes Agent documentation for instructions on [how to uninstall the StackState Cluster Agent and the StackState Agent](https://archivedocs.stackstate.com/5.1/setup/agent/kubernetes-openshift#uninstall) from your Kubernetes cluster.

## Release notes

**Kubernetes StackPack v3.10.2 (2022-09-28)**

* Improvement: Updated documentation.

**Kubernetes StackPack v3.10.1 (2022-09-15)**

* Improvement: Added validation for cluster name

**Kubernetes StackPack v3.9.13 (2022-06-21)**

* Bug Fix: Fixed description for services/ingresses view.

**Kubernetes StackPack v3.9.12 (2022-06-03)**

* Improvement: Updated documentation.

**Kubernetes StackPack v3.9.11 (2022-05-23)**

* Bug Fix: Fixed broken link in integration StackState Agent V2 integration documentation.

**Kubernetes StackPack v3.9.10 (2022-04-11)**

* Bug Fix: Show kubernetes view names on StackPack instance

**Kubernetes StackPack v3.9.9 (2022-03-02)**

* Improvement: Documentation for `agent.containerRuntime.customSocketPath` option.

**Kubernetes StackPack v3.9.8 (2021-11-30)**

* Bug Fix: Support nodes without instanceId

## See also

* [Deploy StackState Agent V3, the Cluster Agent and kube-state-metrics](https://archivedocs.stackstate.com/5.1/setup/agent/kubernetes-openshift)
* [StackState Agent V3 StackPack](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/agent)
* [StackState Agent Kubernetes check (github.com)](https://github.com/StackVista/stackstate-agent-integrations/tree/master/kubernetes)
* [StackState Agent Helm Chart (github.com)](https://github.com/StackVista/helm-charts/tree/master/stable/stackstate-agent)
* [Kubernetes API documentation (kubernetes.io)](https://kubernetes.io/docs/reference/kubernetes-api/)

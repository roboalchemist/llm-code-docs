# Source: https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/

Title: Setup a MultiKueue environment

URL Source: https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/

Published Time: 2024-02-26T00:00:00+00:00

Markdown Content:
Additional steps needed to setup the multikueue clusters.

This tutorial explains how you can configure a management cluster and one worker cluster to run [JobSets](https://kueue.sigs.k8s.io/docs/tasks/run/jobsets/#jobset-definition) and [batch/Jobs](https://kueue.sigs.k8s.io/docs/tasks/run/jobs/#1-define-the-job) in a MultiKueue environment.

Check the concepts section for a [MultiKueue overview](https://kueue.sigs.k8s.io/docs/concepts/multikueue/).

Let’s assume that your manager cluster is named `manager-cluster` and your worker cluster is named `worker1-cluster`. To follow this tutorial, ensure that the credentials for all these clusters are present in the kubeconfig in your local machine. Check the [kubectl documentation](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) to learn more about how to Configure Access to Multiple Clusters.

In the Worker Cluster [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#in-the-worker-cluster)
-------------------------------------------------------------------------------------------------------------

When MultiKueue dispatches a workload from the manager cluster to a worker cluster, it expects that the job’s namespace and LocalQueue also exist in the worker cluster. In other words, you should ensure that the worker cluster configuration mirrors the one of the manager cluster in terms of namespaces and LocalQueues.

To create the sample queue setup in the `default` namespace, you can apply the following manifest:

```
apiVersion: kueue.x-k8s.io/v1beta2
kind: ResourceFlavor
metadata:
  name: "default-flavor"
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue
metadata:
  name: "cluster-queue"
spec:
  namespaceSelector: {} # match all.
  resourceGroups:
  - coveredResources: ["cpu", "memory"]
    flavors:
    - name: "default-flavor"
      resources:
      - name: "cpu"
        nominalQuota: 9
      - name: "memory"
        nominalQuota: 36Gi
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: LocalQueue
metadata:
  namespace: "default"
  name: "user-queue"
spec:
  clusterQueue: "cluster-queue"
```

### MultiKueue Specific Kubeconfig [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#multikueue-specific-kubeconfig)

In order to delegate the jobs in a worker cluster, the manager cluster needs to be able to create, delete, and watch workloads and their parent Jobs.

While `kubectl` is set up to use the worker cluster, download:

```
#!/bin/bash

# Copyright 2024 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -o errexit
set -o nounset
set -o pipefail

KUBECONFIG_OUT=${1:-kubeconfig}
MULTIKUEUE_SA=multikueue-sa
NAMESPACE=kueue-system

# Creating a restricted MultiKueue role, service account and role binding"
kubectl apply -f - <<EOF
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ${MULTIKUEUE_SA}
  namespace: ${NAMESPACE}
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: ${MULTIKUEUE_SA}-role
rules:
- apiGroups:
  - batch
  resources:
  - jobs
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - batch
  resources:
  - jobs/status
  verbs:
  - get
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - apps
  resources:
  - statefulsets
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - apps
  resources:
  - statefulsets/status
  verbs:
  - get
- apiGroups:
  - jobset.x-k8s.io
  resources:
  - jobsets
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - jobset.x-k8s.io
  resources:
  - jobsets/status
  verbs:
  - get
- apiGroups:
  - kueue.x-k8s.io
  resources:
  - workloads
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - kueue.x-k8s.io
  resources:
  - workloads/status
  verbs:
  - get
  - patch
  - update
- apiGroups:
  - kubeflow.org
  resources:
  - tfjobs
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - kubeflow.org
  resources:
  - tfjobs/status
  verbs:
  - get
- apiGroups:
  - kubeflow.org
  resources:
  - paddlejobs
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - kubeflow.org
  resources:
  - paddlejobs/status
  verbs:
  - get
- apiGroups:
  - kubeflow.org
  resources:
  - pytorchjobs
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - kubeflow.org
  resources:
  - pytorchjobs/status
  verbs:
  - get
- apiGroups:
  - kubeflow.org
  resources:
  - xgboostjobs
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - kubeflow.org
  resources:
  - xgboostjobs/status
  verbs:
  - get
- apiGroups:
  - kubeflow.org
  resources:
  - mpijobs
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - kubeflow.org
  resources:
  - mpijobs/status
  verbs:
  - get
- apiGroups:
  - ray.io
  resources:
  - rayjobs
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - ray.io
  resources:
  - rayjobs/status
  verbs:
  - get
- apiGroups:
  - ray.io
  resources:
  - rayclusters
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - ray.io
  resources:
  - rayclusters/status
  verbs:
  - get
- apiGroups:
  - workload.codeflare.dev
  resources:
  - appwrappers
  verbs:
  - create
  - delete
  - get
  - list
  - watch
- apiGroups:
  - workload.codeflare.dev
  resources:
  - appwrappers/status
  verbs:
  - get
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: ${MULTIKUEUE_SA}-crb
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: ${MULTIKUEUE_SA}-role
subjects:
- kind: ServiceAccount
  name: ${MULTIKUEUE_SA}
  namespace: ${NAMESPACE}
EOF

# Get or create a secret bound to the new service account.
SA_SECRET_NAME=$(kubectl get -n ${NAMESPACE} sa/${MULTIKUEUE_SA} -o "jsonpath={.secrets[0]..name}")
if [ -z "$SA_SECRET_NAME" ]
then
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: ${MULTIKUEUE_SA}
  namespace: ${NAMESPACE}
  annotations:
    kubernetes.io/service-account.name: "${MULTIKUEUE_SA}"
EOF

SA_SECRET_NAME=${MULTIKUEUE_SA}
fi

# Note: service account token is stored base64-encoded in the secret but must
# be plaintext in kubeconfig.
SA_TOKEN=$(kubectl get -n ${NAMESPACE} "secrets/${SA_SECRET_NAME}" -o "jsonpath={.data['token']}" | base64 -d)
CA_CERT=$(kubectl get -n ${NAMESPACE} "secrets/${SA_SECRET_NAME}" -o "jsonpath={.data['ca\.crt']}")

# Extract cluster IP from the current context
CURRENT_CONTEXT=$(kubectl config current-context)
CURRENT_CLUSTER=$(kubectl config view -o jsonpath="{.contexts[?(@.name == \"${CURRENT_CONTEXT}\"})].context.cluster}")
CURRENT_CLUSTER_ADDR=$(kubectl config view -o jsonpath="{.clusters[?(@.name == \"${CURRENT_CLUSTER}\"})].cluster.server}")

# Create the Kubeconfig file
echo "Writing kubeconfig in ${KUBECONFIG_OUT}"
cat > "${KUBECONFIG_OUT}" <<EOF
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: ${CA_CERT}
    server: ${CURRENT_CLUSTER_ADDR}
  name: ${CURRENT_CLUSTER}
contexts:
- context:
    cluster: ${CURRENT_CLUSTER}
    user: ${CURRENT_CLUSTER}-${MULTIKUEUE_SA}
  name: ${CURRENT_CONTEXT}
current-context: ${CURRENT_CONTEXT}
kind: Config
preferences: {}
users:
- name: ${CURRENT_CLUSTER}-${MULTIKUEUE_SA}
  user:
    token: ${SA_TOKEN}
EOF
```

And run:

```
chmod +x create-multikueue-kubeconfig.sh
./create-multikueue-kubeconfig.sh worker1.kubeconfig
```

To create a Kubeconfig that can be used in the manager cluster to delegate Jobs in the current worker.

### Kubeflow Installation [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#kubeflow-installation)

Install Kubeflow Trainer in the Worker cluster (see [Kubeflow Trainer Installation](https://www.kubeflow.org/docs/components/training/installation/) for more details). Please use version v1.7.0 or a newer version for MultiKueue.

In the Manager Cluster [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#in-the-manager-cluster)
---------------------------------------------------------------------------------------------------------------

### CRDs installation [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#crds-installation)

For installation of CRDs compatible with MultiKueue please refer to the dedicated pages [here](https://kueue.sigs.k8s.io/docs/tasks/run/multikueue/).

### Create worker’s Kubeconfig secret [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#create-workers-kubeconfig-secret)

For the next example, having the `worker1` cluster Kubeconfig stored in a file called `worker1.kubeconfig`, you can create the `worker1-secret` secret by running the following command:

```
kubectl create secret generic worker1-secret -n kueue-system --from-file=kubeconfig=worker1.kubeconfig
```

Check the [worker](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#multikueue-specific-kubeconfig) section for details on Kubeconfig generation.

### Create a sample setup [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#create-a-sample-setup)

Apply the following to create a sample setup in which the Jobs submitted in the ClusterQueue `cluster-queue` are delegated to a worker `worker1`

```
apiVersion: kueue.x-k8s.io/v1beta2
kind: ResourceFlavor
metadata:
  name: "default-flavor"
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue
metadata:
  name: "cluster-queue"
spec:
  namespaceSelector: {} # match all.
  resourceGroups:
  - coveredResources: ["cpu", "memory"]
    flavors:
    - name: "default-flavor"
      resources:
      - name: "cpu"
        nominalQuota: 9
      - name: "memory"
        nominalQuota: 36Gi
  admissionChecksStrategy:
    admissionChecks:
    - name: sample-multikueue
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: LocalQueue
metadata:
  namespace: "default"
  name: "user-queue"
spec:
  clusterQueue: "cluster-queue"
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: AdmissionCheck
metadata:
  name: sample-multikueue
spec:
  controllerName: kueue.x-k8s.io/multikueue
  parameters:
    apiGroup: kueue.x-k8s.io
    kind: MultiKueueConfig
    name: multikueue-test
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: MultiKueueConfig
metadata:
  name: multikueue-test
spec:
  clusters:
  - multikueue-test-worker1
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: MultiKueueCluster
metadata:
  name: multikueue-test-worker1
spec:
  clusterSource:
    kubeConfig:
      locationType: Secret
      location: worker1-secret
      # a secret called "worker1-secret" should be created in the namespace the kueue
      # controller manager runs into, holding the kubeConfig needed to connect to the
      # worker cluster in the "kubeconfig" key;
```

Upon successful configuration the created ClusterQueue, AdmissionCheck and MultiKueueCluster will become active.

Run:

```
kubectl get clusterqueues cluster-queue -o jsonpath="{range .status.conditions[?(@.type == \"Active\")]}CQ - Active: {@.status} Reason: {@.reason} Message: {@.message}{'\n'}{end}"
kubectl get admissionchecks sample-multikueue -o jsonpath="{range .status.conditions[?(@.type == \"Active\")]}AC - Active: {@.status} Reason: {@.reason} Message: {@.message}{'\n'}{end}"
kubectl get multikueuecluster multikueue-test-worker1 -o jsonpath="{range .status.conditions[?(@.type == \"Active\")]}MC - Active: {@.status} Reason: {@.reason} Message: {@.message}{'\n'}{end}"
```

And expect an output like:

```
CQ - Active: True Reason: Ready Message: Can admit new workloads
AC - Active: True Reason: Active Message: The admission check is active
MC - Active: True Reason: Active Message: Connected
```

### Create a sample setup with TAS [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#create-a-sample-setup-with-tas)

To enable Topology-Aware Scheduling (TAS) in a MultiKueue setup, configure the worker clusters with topology levels and the manager cluster with delayed topology requests.

Worker cluster configuration:

```
apiVersion: kueue.x-k8s.io/v1beta2
kind: Topology
metadata:
  name: default
spec:
  levels:
  - nodeLabel: kubernetes.io/hostname
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: ResourceFlavor
metadata:
  name: tas-flavor
spec:
  nodeLabels:
    cloud.provider.com/node-group: tas-node
  topologyName: default
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue
metadata:
  name: worker-cluster-queue
spec:
  namespaceSelector: {}
  resourceGroups:
  - coveredResources: ["cpu", "memory"]
    flavors:
    - name: tas-flavor
      resources:
      - name: cpu
        nominalQuota: 8
      - name: memory
        nominalQuota: 16Gi
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: LocalQueue
metadata:
  namespace: default
  name: user-queue
spec:
  clusterQueue: worker-cluster-queue
```

Manager cluster configuration:

```
apiVersion: kueue.x-k8s.io/v1beta2
kind: Topology
metadata:
  name: default
spec:
  levels:
  - nodeLabel: kubernetes.io/hostname
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: ResourceFlavor
metadata:
  name: tas-flavor
spec:
  nodeLabels:
    cloud.provider.com/node-group: tas-node
  topologyName: default
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: MultiKueueConfig
metadata:
  name: multikueue-config
spec:
  clusters:
  - worker1
  - worker2
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: AdmissionCheck
metadata:
  name: multikueue-ac
spec:
  controllerName: kueue.x-k8s.io/multikueue
  parameters:
    apiGroup: kueue.x-k8s.io
    kind: MultiKueueConfig
    name: multikueue-config
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: MultiKueueCluster
metadata:
  name: worker1
spec:
  clusterSource:
    kubeConfig:
      locationType: Secret
      location: worker1-secret
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: MultiKueueCluster
metadata:
  name: worker2
spec:
  clusterSource:
    kubeConfig:
      locationType: Secret
      location: worker2-secret
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue
metadata:
  name: cluster-queue
spec:
  namespaceSelector: {}
  resourceGroups:
  - coveredResources: ["cpu", "memory"]
    flavors:
    - name: tas-flavor
      resources:
      - name: cpu
        nominalQuota: 16
      - name: memory
        nominalQuota: 32Gi
  admissionChecksStrategy:
    admissionChecks:
    - name: multikueue-ac
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: LocalQueue
metadata:
  namespace: default
  name: user-queue
spec:
  clusterQueue: cluster-queue
```

For a complete setup guide including local development with Kind, see the [Setup MultiKueue with Topology-Aware Scheduling](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/) guide.

(Optional) Setup MultiKueue with Open Cluster Management [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#optional-setup-multikueue-with-open-cluster-management)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Open Cluster Management (OCM)](https://open-cluster-management.io/) is a community-driven project focused on multicluster and multicloud scenarios for Kubernetes apps. It provides a robust, modular, and extensible framework that helps other open source projects orchestrate, schedule, and manage workloads across multiple clusters.

The integration with OCM is an optional solution that enables Kueue users to streamline the MultiKueue setup process, automate the generation of MultiKueue specific Kubeconfig, and enhance multicluster scheduling capabilities. For more details about this solution, please refer to this [link](https://github.com/open-cluster-management-io/ocm/tree/main/solutions/kueue-admission-check).

Configure federated credential discovery via the ClusterProfile API [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#configure-federated-credential-discovery-via-the-clusterprofile-api)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Feature state alpha since Kueue v0.15

The [Cluster Inventory API](https://multicluster.sigs.k8s.io/) provides a standardized, vendor-neutral interface for representing a cluster’s properties and status. It defines a `ClusterProfile` resource that encapsulates the identity, metadata, and status of a specific cluster within a multi-cluster environment.

Kueue can leverage the configuration contained within a `ClusterProfile` object to obtain credentials and connect to the cluster it represents. In practice, this means that instead of using Kubeconfig files to specify the connection to its workers, the manager cluster uses the state and access providers contained in the existing `ClusterProfile`s. This eliminates a large portion of management required from the administrator and allows to delegate credentialing to the entity managing the clusters (like a cloud provider).

### Enable the `MultiKueueClusterProfile` feature gate [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#enable-the-multikueueclusterprofile-feature-gate)

The `MultiKueueClusterProfile` feature gate has to be enabled for Kueue to consider `ClusterProfile` objects when connecting to clusters. Refer to the [Installation guide](https://kueue.sigs.k8s.io/docs/installation/#change-the-feature-gates-configuration) for instructions on configuring feature gates.

### Provision the `ClusterProfile` objects for your clusters [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#provision-the-clusterprofile-objects-for-your-clusters)

#### Cloud provider managed cluster inventory [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#cloud-provider-managed-cluster-inventory)

When using a cloud provider that supports the automatic generation and synchronization of a cluster inventory, the `ClusterProfile` objects are managed directly by their platform and do not require that the user sets them up manually or uses a dedicated controller.

To enable the generation of an inventory, refer to your cloud provider’s documentation:

*   Google Cloud Platform:
    *   [Full walkthrough of MultiKueue setup with ClusterProfile](https://github.com/GoogleCloudPlatform/gke-fleet-management/blob/b9fe08386c48f84617cb8ab7b042f2790741e893/multikueue-clusterprofile/README.md).
    *   [Inventory generation documentation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/generate-inventory-for-integrations).

When using cloud provider managed cluster inventory, you should expect a `ClusterProfile` object to be created in your MultiKueue manager cluster, one per cluster (including the manager itself).

For example:

```
apiVersion: multicluster.x-k8s.io/v1alpha1
kind: ClusterProfile
metadata:
  labels:
    x-k8s.io/cluster-manager: <cloud-provider-service-name>
  name: multikueue-worker-1
  namespace: kueue-system
spec:
  clusterManager:
    name: <cloud-provider-service-name>
  displayName: multikueue-worker-1
status:
  accessProviders:
  - cluster:
      server: <cluster-url>
    name: <access-provider-name>
```

Where:

*   `cloud-provider-service-name` is the name of the service within the cloud provider that manages the cluster. For example `gke-fleet`.
*   `cluster-url` is the URL of the cluster’s control plane.
*   `access-provider-name` is the name of the provider of the cluster’s credentials. For example `google`.

#### Cluster management platform inventory [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#cluster-management-platform-inventory)

When using a cluster management platform that supports the automatic generation and synchronization of a cluster inventory, the `ClusterProfile` objects are managed directly by the platform and do not require that the user sets them up manually.

To enable the generation of an inventory, refer to the cluster management platform’s documentation:

*   Open Cluster Management:
    *   [Full walkthrough of MultiKueue setup with ClusterProfile](https://open-cluster-management.io/docs/scenarios/clusterprofile-access-providers/).

#### Manually created cluster inventory [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#manually-created-cluster-inventory)

In principle, the `ClusterProfile` objects can be provisioned without the use of a cloud provider.

Firstly, the `ClusterProfile` CRDs have to be manually installed within the cluster:

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/cluster-inventory-api/refs/heads/main/config/crd/bases/multicluster.x-k8s.io_clusterprofiles.yaml
```

Next, the `ClusterProfile` objects can be created:

```
apiVersion: multicluster.x-k8s.io/v1alpha1
kind: ClusterProfile
metadata:
  name: worker1-cluster
  namespace: kueue-system
spec:
  ...
status:
  accessProviders:
  - name: <access-provider-name>
    cluster:
      ...
```

### Install the access provider plugin [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#install-the-access-provider-plugin)

The access provider defined in `ClusterProfile` depends upon an executable plugin being available to the Kueue controller manager pods running within the MultiKueue manager cluster. It’s the responsibility of the Kueue administrator to make sure that the required command is available.

An example plugin can be found [here](https://github.com/kubernetes-sigs/cluster-inventory-api/tree/445319b6307a88778b930e154ed3e2f38d85a689/cmd/secretreader-plugin) (secret reader) or [here](https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke) (Google Cloud Platform).

#### Mount the executable with `initContainers`[](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#mount-the-executable-with-initcontainers)

The [`initContainers`](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) field within the pods specification can be used to populate a volume with the required plugin. The image used by the init container has to be built beforehand.

The `kueue-controller-manager` container within the Kueue manager deployment can then mount this volume in its filesystem to access the executable. For example:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kueue-controller-manager
  namespace: kueue-system
spec:
  template:
    spec:
      initContainers:
      - name: add-auth-plugin
        image: <plugin-image>
        command: ["cp", "<plugin-command>", "/plugins/<plugin-command>"]
        volumeMounts:
        - name: clusterprofile-plugins
          mountPath: "/plugins"
      containers:
      - name: manager
        volumeMounts:
        - name: clusterprofile-plugins
          mountPath: "/plugins"
      volumes:
      - name: clusterprofile-plugins
        emptyDir: {}
```

Where:

*   `plugin-image` is the image reference of an image that contains the plugin executable.
*   `plugin-command` is the name of the executable. For example `gcp-auth-plugin`.

#### (Kubernetes 1.35+) Mount the executable using an image volume [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#kubernetes-135-mount-the-executable-using-an-image-volume)

The ability to [mount content from OCI registries into containers](https://kubernetes.io/docs/tasks/configure-pod-container/image-volumes/) reached beta in Kubernetes 1.35. This feature streamlines some aspects of the `initContainers` approach.

For example:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kueue-controller-manager
  namespace: kueue-system
spec:
  template:
    spec:
      containers:
      - name: manager
        volumeMounts:
        - name: clusterprofile-plugins
          mountPath: "/plugins"
      volumes:
      - name: clusterprofile-plugins
        image:
          reference: <plugin-image>
          pullPolicy: IfNotPresent
```

Where:

*   `plugin-image` is the image reference of an image that contains the plugin executable.

The files inside the `plugin-image` will be accessible under the `mountPath` (in this case `/plugins`) and can be called analogously to the `initContainers` approach (`/plugins/<plugin-command>`).

#### Build a custom Kueue manager image [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#build-a-custom-kueue-manager-image)

Alternatively, a custom Kueue manager image can be built to include the plugin executable. The image reference in the Kueue manager deployment should then point to the user-managed custom image.

### Define the credentials provider in the Kueue manager config [](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#define-the-credentials-provider-in-the-kueue-manager-config)

To connect the access providers specified in the `ClusterProfile`s with the mounted plugin, an entry within the Kueue configuration has to be created:

```
apiVersion: v1
data:
  controller_manager_config.yaml: |
    ...
    multiKueue:
      clusterProfile:
        credentialsProviders:
        - name: <access-provider-name>
          execConfig:
            apiVersion: client.authentication.k8s.io/v1beta1
            command: /plugins/<plugin-command>
            interactiveMode: Never
kind: ConfigMap
metadata:
  labels:
    app.kubernetes.io/name: kueue
    control-plane: controller-manager
  name: kueue-manager-config
  namespace: kueue-system
```

Where:

*   `access-provider-name` is the name of the provider of the cluster’s credentials. It has to match the `accessProviders` name in the relevant `ClusterProfile`s.
*   `plugin-command` is the name of the executable within the manager container.

This definition will configure the `ClusterProfile`s using the `access-provider-name` to retrieve cluster credentials via the `plugin-command` executable.

### Link `MultiKueueCluster` objects to their corresponding `ClusterProfile`[](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_multikueue/#link-multikueuecluster-objects-to-their-corresponding-clusterprofile)

When using the `ClusterProfile` API for authentication, the `MultiKueueCluster` objects have to reference a `ClusterProfile` via the `clusterProfileRef` field, instead of providing `kubeconfig` directly.

Here’s an example `MultiKueueCluster` object using a `clusterProfileRef`:

```
apiVersion: kueue.x-k8s.io/v1beta2
kind: MultiKueueCluster
metadata:
  name: worker1-cluster
spec:
  clusterSource:
    clusterProfileRef:
      name: worker1-cluster
```

# Source: https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/

Title: Setup MultiKueue Development Environment

URL Source: https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/

Published Time: 2026-01-13T00:00:00+00:00

Markdown Content:
Configure MultiKueue for local development and testing.

This tutorial explains how you can configure a manager cluster and worker clusters to run jobs with [Topology-Aware Scheduling (TAS)](https://kueue.sigs.k8s.io/docs/tasks/run/leaderworkerset/#configure-topology-aware-scheduling) in a MultiKueue environment. We also outline the automated steps using Kind for local testing.

Check the concepts section for a [MultiKueue overview](https://kueue.sigs.k8s.io/docs/concepts/multikueue/) and [Topology-Aware Scheduling overview](https://kueue.sigs.k8s.io/docs/concepts/topology_aware_scheduling/).

Setup MultiKueue with E2E Test Cluster [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#setup-multikueue-with-e2e-test-cluster)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [e2e test development mode](https://kueue.sigs.k8s.io/docs/contribution_guidelines/testing/#dev-mode-recommended) can be used to maintain a MultiKueue cluster setup and run end-to-end tests against it without recreating and tearing it down each time.

For example:

```
E2E_MODE=dev make kind-image-build test-multikueue-e2e
```

For more information about the DEV mode, refer to the testing documentation.

Setup MultiKueue with TAS [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#setup-multikueue-with-tas)
------------------------------------------------------------------------------------------------------------------------------------------

### Automated Setup [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#automated-setup)

For a quick setup, download and run the setup script:

```
git clone https://github.com/kubernetes-sigs/kueue.git
cd kueue/examples/multikueue/dev
./setup-kind-multikueue-tas.sh
```

The script will set up a complete MultiKueue environment that is additionally configured with TAS.

Alternatively, follow the manual steps below.

### Step 1: Create Kind Clusters [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#step-1-create-kind-clusters)

Create three Kind clusters (manager and two workers):

```
# Manager cluster
cat <<EOF | kind create cluster --name manager --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
  labels:
    instance-type: on-demand
    cloud.provider.com/node-group: tas-node
EOF

# Worker 1 cluster
cat <<EOF | kind create cluster --name worker1 --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
  labels:
    instance-type: on-demand
    cloud.provider.com/node-group: tas-node
EOF

# Worker 2 cluster
cat <<EOF | kind create cluster --name worker2 --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
  labels:
    instance-type: on-demand
    cloud.provider.com/node-group: tas-node
EOF
```

Verify all clusters are created:

```
kind get clusters
# Expected output:
# manager
# worker1
# worker2
```

### Step 2: Install Kueue on All Clusters [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#step-2-install-kueue-on-all-clusters)

```
KUEUE_VERSION=v0.15.0
kubectl --context kind-manager apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/${KUEUE_VERSION}/manifests.yaml
kubectl --context kind-worker1 apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/${KUEUE_VERSION}/manifests.yaml
kubectl --context kind-worker2 apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/${KUEUE_VERSION}/manifests.yaml

for ctx in kind-manager kind-worker1 kind-worker2; do
  kubectl --context $ctx wait --for=condition=available --timeout=300s deployment/kueue-controller-manager -n kueue-system
done
```

### Step 3: Configure Manager for Kind [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#step-3-configure-manager-for-kind)

Enable the feature gate for insecure kubeconfigs and configure integrations:

```
# Enable feature gate (required for Kind clusters with insecure-skip-tls-verify)
kubectl --context kind-manager patch deployment kueue-controller-manager -n kueue-system --type='json' \
  -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--feature-gates=MultiKueueAllowInsecureKubeconfigs=true"}]'

# Configure to use only batch/job integration
cat > /tmp/kueue-integrations-patch.yaml <<'EOF'
data:
  controller_manager_config.yaml: |
    apiVersion: config.kueue.x-k8s.io/v1beta2
    kind: Configuration
    health:
      healthProbeBindAddress: :8081
    metrics:
      bindAddress: :8443
    webhook:
      port: 9443
    leaderElection:
      leaderElect: true
      resourceName: c1f6bfd2.kueue.x-k8s.io
    controller:
      groupKindConcurrency:
        Job.batch: 5
        Pod: 5
        Workload.kueue.x-k8s.io: 5
        LocalQueue.kueue.x-k8s.io: 1
        Cohort.kueue.x-k8s.io: 1
        ClusterQueue.kueue.x-k8s.io: 1
        ResourceFlavor.kueue.x-k8s.io: 1
    clientConnection:
      qps: 50
      burst: 100
    integrations:
      frameworks:
      - "batch/job"
EOF
kubectl --context kind-manager patch configmap kueue-manager-config -n kueue-system --patch-file=/tmp/kueue-integrations-patch.yaml

# Restart controller to apply changes
kubectl --context kind-manager rollout restart deployment/kueue-controller-manager -n kueue-system
kubectl --context kind-manager rollout status deployment/kueue-controller-manager -n kueue-system --timeout=180s
```

### Step 4: Configure Worker Clusters [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#step-4-configure-worker-clusters)

Apply the worker configuration with TAS:

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

```
kubectl --context kind-worker1 apply -f examples/multikueue/tas/worker-setup.yaml
kubectl --context kind-worker2 apply -f examples/multikueue/tas/worker-setup.yaml
```

Create ServiceAccounts and kubeconfigs for MultiKueue on both workers:

```
for cluster in worker1 worker2; do
  # Create ServiceAccount
  kubectl --context kind-${cluster} create sa multikueue-sa -n kueue-system

  # Create ClusterRoles
  kubectl --context kind-${cluster} create clusterrole multikueue-role \
    --verb=create,delete,get,list,watch \
    --resource=jobs.batch,workloads.kueue.x-k8s.io,pods

  kubectl --context kind-${cluster} create clusterrole multikueue-role-status \
    --verb=get,patch,update \
    --resource=jobs.batch/status,workloads.kueue.x-k8s.io/status,pods/status

  # Create ClusterRoleBindings
  kubectl --context kind-${cluster} create clusterrolebinding multikueue-crb \
    --clusterrole=multikueue-role \
    --serviceaccount=kueue-system:multikueue-sa

  kubectl --context kind-${cluster} create clusterrolebinding multikueue-crb-status \
    --clusterrole=multikueue-role-status \
    --serviceaccount=kueue-system:multikueue-sa

  # Create token and kubeconfig
  TOKEN=$(kubectl --context kind-${cluster} create token multikueue-sa -n kueue-system --duration=24h)

  cat > ${cluster}.kubeconfig <<EOF
apiVersion: v1
kind: Config
clusters:
- cluster:
    insecure-skip-tls-verify: true
    server: https://${cluster}-control-plane:6443
  name: ${cluster}
contexts:
- context:
    cluster: ${cluster}
    user: multikueue-sa
  name: ${cluster}
current-context: ${cluster}
users:
- name: multikueue-sa
  user:
    token: ${TOKEN}
EOF
done
```

### Step 5: Configure Manager Cluster [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#step-5-configure-manager-cluster)

Create secrets and apply configuration:

```
kubectl --context kind-manager create secret generic worker1-secret -n kueue-system --from-file=kubeconfig=worker1.kubeconfig
kubectl --context kind-manager create secret generic worker2-secret -n kueue-system --from-file=kubeconfig=worker2.kubeconfig
```

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

```
kubectl --context kind-manager apply -f examples/multikueue/tas/manager-setup.yaml
```

### Step 6: Validate the Setup [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#step-6-validate-the-setup)

Verify that all components are active:

```
kubectl --context kind-manager get clusterqueue,admissioncheck,multikueuecluster
```

Expected output:

```
NAME                                        COHORT   PENDING WORKLOADS
clusterqueue.kueue.x-k8s.io/cluster-queue            0

NAME                                          AGE
admissioncheck.kueue.x-k8s.io/multikueue-ac   5m

NAME                                       CONNECTED   AGE
multikueuecluster.kueue.x-k8s.io/worker1   True        5m
multikueuecluster.kueue.x-k8s.io/worker2   True        5m
```

### Step 7: Submit a TAS Job [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#step-7-submit-a-tas-job)

Submit a sample job that requires topology-aware scheduling:

```
apiVersion: batch/v1
kind: Job
metadata:
  name: tas-sample-job
  namespace: default
  labels:
    kueue.x-k8s.io/queue-name: user-queue
spec:
  parallelism: 2
  completions: 2
  template:
    metadata:
      annotations:
        kueue.x-k8s.io/podset-required-topology: kubernetes.io/hostname
    spec:
      restartPolicy: Never
      containers:
      - name: sample-container
        image: registry.k8s.io/e2e-test-images/agnhost:2.40
        args: ["pause"]
        resources:
          requests:
            cpu: "1"
            memory: "1Gi"
          limits:
            cpu: "1"
            memory: "1Gi"
      terminationGracePeriodSeconds: 5
---
apiVersion: batch/v1
kind: Job
metadata:
  name: implicit-tas-job
  namespace: default
  labels:
    kueue.x-k8s.io/queue-name: user-queue
spec:
  parallelism: 3
  completions: 3
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: sample-container
        image: registry.k8s.io/e2e-test-images/agnhost:2.40
        args: ["pause"]
        resources:
          requests:
            cpu: "500m"
            memory: "512Mi"
          limits:
            cpu: "500m"
            memory: "512Mi"
      terminationGracePeriodSeconds: 5
```

```
kubectl --context kind-manager apply -f examples/multikueue/dev/sample-tas-job.yaml
kubectl --context kind-manager get workloads.kueue.x-k8s.io -n default
```

Expected output showing the workload was admitted and delegated to a worker cluster:

```
NAME               QUEUE        RESERVED IN   ADMITTED   AGE
tas-sample-job     user-queue   worker1       True       5s
implicit-tas-job   user-queue   worker2       True       5s
```

Cleanup [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#cleanup)
------------------------------------------------------------------------------------------------------

Delete the Kind clusters:

```
kind delete clusters manager worker1 worker2
```

Next Steps [](https://kueue.sigs.k8s.io/docs/tasks/dev/setup_multikueue_development_environment/#next-steps)
------------------------------------------------------------------------------------------------------------

*   Learn more about [Topology-Aware Scheduling](https://kueue.sigs.k8s.io/docs/concepts/topology_aware_scheduling/)
*   Explore [MultiKueue concepts](https://kueue.sigs.k8s.io/docs/concepts/multikueue/)

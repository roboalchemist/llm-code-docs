# Source: https://docs.together.ai/docs/instant-clusters.md

> Create, scale, and manage Instant Clusters in Together Cloud

# Instant Clusters

## Overview

Instant Clusters allows you to create high-performance GPU clusters in minutes. With features like on-demand scaling, long-lived resizable high-bandwidth shared DC-local storage, Kubernetes and Slurm cluster flavors, a REST API, and Terraform support, you can run workloads flexibly without complex infrastructure management.

## Quickstart: Create an Instant Cluster

1. Log into api.together.ai.
2. Click **GPU Clusters** in the top navigation menu.
3. Click **Create Cluster**.
4. Choose whether you want **Reserved** capacity or **On-demand**, based on your needs.
5. Select the **cluster size**, for example `8xH100`.
6. Enter a **cluster name**.
7. Choose a **cluster type** either Kubernetes or Slurm.
8. Select a **region**.
9. Choose the reservation **duration** for your cluster.
10. Create and name your **shared volume** (minimum size 1 TiB).
11. Optional: Select your **NVIDIA driver** and **CUDA** versions.
12. Click **Proceed**.

Your cluster will now be ready for you to use.

### Capacity Types

* **Reserved**: You pay upfront to reserve GPU capacity for a duration between 1-90 days.
* **On-demand**: You  pay as you go for GPU capacity on an hourly basis. No pre-payment or reservation needed, and you can terminate your cluster at any time.

### Node Types

We have the following node types available in Instant Clusters.

* NVIDIA HGX B200
* NVIDIA HGX H200
* NVIDIA HGX H100 SXM
* NVIDIA HGX H100 SXM - Inference (lower Infiniband multi-node GPU-to-GPU bandwidth, suitable for single-node inference)

If you don't see an available node type, select the "Notify Me" option to get notified when capacity is online. You can also contact us with your request via [support@together.ai](mailto:support@together.ai).

### Pricing

Pricing information for different GPU node types can be found [here](https://www.together.ai/instant-gpu-clusters).

### Cluster Status

* From the UI, verify that your cluster transitions to Ready.
* Monitor progress and health indicators directly from the cluster list.

### Start Training with Kubernetes

#### Install kubectl

Install `kubectl` in your environment, for example on [MacOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/).

#### Download kubeconfig

From the Instant Clusters UI, download the kubeconfig and copy it to your local machine:

```bash  theme={null}
~/.kube/together_instant.kubeconfig
export KUBECONFIG=$HOME/.kube/together_instant.kubeconfig
kubectl get nodes
```

> You can rename the file to `config`, but back up your existing config first.

#### Verify Connectivity

```bash  theme={null}
kubectl get nodes
```

You should see all worker and control plane nodes listed.

#### Deploy a Pod with Storage

* Create a PersistentVolumeClaim for shared storage. We provide a static PersistentVolume with the same name as your shared volume. As long as you use the static PV, your data would persist.

```yaml  theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared-pvc
spec:
  accessModes:
    - ReadWriteMany   # Multiple pods can read/write
  resources:
    requests:
      storage: 10Gi   # Requested size
  volumeName: <shared volume name>
```

* Create a PersistentVolumeClaim for local storage.

```yaml  theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-pvc
spec:
  accessModes:
    - ReadWriteOnce   # Only one pod/node can mount at a time
  resources:
    requests:
      storage: 50Gi
  storageClassName: local-storage-class
```

* Mount them into a pod:

```yaml  theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  restartPolicy: Never
  containers:
    - name: ubuntu
      image: debian:stable-slim
      command: ["/bin/sh", "-c", "sleep infinity"]
      volumeMounts:
        - name: shared-pvc
          mountPath: /mnt/shared
        - name: local-pvc
          mountPath: /mnt/local
  volumes:
    - name: shared-pvc
      persistentVolumeClaim:
        claimName: shared-pvc
    - name: local-pvc
      persistentVolumeClaim:
        claimName: local-pvc
```

Apply and connect:

```bash  theme={null}
kubectl apply -f manifest.yaml
kubectl exec -it test-pod -- bash
```

#### Kubernetes Dashboard Access

* From the cluster UI, click the K8s Dashboard URL.
* Retrieve your access token using the following command:

```bash  theme={null}
kubectl -n kubernetes-dashboard get secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user-token | awk '{print $1}') -o jsonpath='{.data.token}' | base64 -d | pbcopy
```

## Cluster Scaling

Clusters can scale flexibly in real time. By adding on-demand compute to your cluster, you can temporarily scale up to more GPUs when workload demand spikes and then scale back down as it wanes.

Scaling up or down can be performed using the UI, tcloud CLI, or REST API.

### Targeted Scale-down

If you wish to mark which node or nodes should be targeted for scale-down, you can:

* Either cordon the k8s node(s) or add the node.together.ai/delete-node-on-scale-down: "true" annotation to the k8s node(s).
  \= Then trigger scale-down via the cloud console UI (or CLI, REST API).
* Instant Clusters will ensure that cordoned + annotated nodes are prioritized for deletion above all others.

## Storage Management

Instant Clusters supports long-lived, resizable in-DC shared storage with user data persistence.

You can dynamically create and attach volumes to your cluster at cluster creation time, and resize as your data grows.

All shared storage is backed by multi-NIC bare metal paths, ensuring high-throughput and low-latency performance for shared storage.

### Upload Your Data

To upload data to the cluster from your local machine, follow these steps:

* Create a PVC using the shared volume name as the VolumeName as well as a pod to mount the volume
* Run `kubectl cp LOCAL_FILENAME YOUR_POD_NAME:/data/`
* Note: This method is suitable for smaller datasets, for larger datasets we recommend scheduling a pod on the cluster that can download from S3.

## Compute Access

You can run workloads on Instant Clusters using Kubernetes or Slurm-on-Kubernetes.

### Kubernetes

Use `kubectl` to submit jobs, manage pods, and interact with your cluster. See [Quickstart](#quickstart) for setup details.

### Slurm Direct SSH

For HPC workflows, you can enable Slurm-on-Kubernetes:

* Directly SSH into a Slurm node.
* Use familiar Slurm commands (`sbatch`, `srun`, etc.) to manage distributed training jobs.

This provides the flexibility of traditional HPC job scheduling alongside Kubernetes.

#### SSH to Slurm Login Pod

Please note that at this time, you must add your SSH key to your account prior to deploying a cluster in order for the key to register
in your LDAP server.

Tip: When you click your cluster in the Together Cloud UI, the Cluster details page shows copy-ready Slurm commands tailored to your cluster (for example, `squeue`, `sinfo`, `srun`, `sbatch`). Use these to quickly verify connectivity and submit jobs.

The hostname of worker pods will always be the name of the node with `.slurm.pod` at the end. For instance, `gpu-dp-hmqnh-nwlnj.slurm.pod`.

The hostname of the login pod, which is the place you will likely wish to start most jobs and routines from is always `slurm-login`.

## APIs and Integrations

### tcloud CLI

Download the CLI:

* [Mac](https://tcloud-cli-downloads.s3.us-west-2.amazonaws.com/releases/latest/tcloud-darwin-universal.tar.gz)
* [Linux](https://tcloud-cli-downloads.s3.us-west-2.amazonaws.com/releases/latest/tcloud-linux-amd64.tar.gz)

Authenticate via Google SSO:

```bash  theme={null}
tcloud sso login
```

Create a cluster:

```bash  theme={null}
tcloud cluster create my-cluster \ 
  --num-gpus 8 \
  --reservation-duration 1 \  
  --instance-type H100-SXM \ 
  --region us-central-8 \  
  --shared-volume-name my-volume \   
  --size-tib 1
```

Optionally, you can specify whether you want to provision reserved capacity or on-demand by using the `billing-type` field and setting its value to either `prepaid` (i.e. a reservation) or `on_demand`.

```bash  theme={null}
tcloud cluster create my-cluster \
  --num-gpus 8 \
  --billing-type prepaid \
  --reservation-duration 1 \
  --instance-type H100-SXM \
  --region us-central-8 \
  --shared-volume-name my-volume \
  --size-tib 1
```

Delete a cluster:

```bash  theme={null}
tcloud cluster delete <CLUSTER_UUID>
```

### REST API

All cluster management actions (create, scale, delete, storage, etc.) are available via REST API endpoints for programmatic control.

The API documentation can be found [here](https://docs.together.ai/api-reference/gpuclusterservice/create-gpu-cluster).

### Terraform Provider

Use the Together Terraform Provider to define clusters, storage, and scaling policies as code. This allows reproducible infrastructure management integrated with existing Terraform workflows.

### SkyPilot

You can orchestrate AI workloads on Instant Clusters using SkyPilot.

The following example shows how to use Together with SkyPilot and orchestrate `gpt-oss-20b` finetuning on it.

#### Use Together Instant Cluster with SkyPilot

1. ```bash  theme={null}
    uv pip install skypilot[kubernetes]
   ```

2. Launch a Together Instant Cluster with cluster type selected as Kubernetes

* Get the Kubernetes config for the cluster
* Save the kubeconfig to a file say `./together.kubeconfig`
* Copy the kubeconfig to your `~/.kube/config` or merge the Kubernetes config with your existing kubeconfig file.
  ```bash  theme={null}
  mkdir -p ~/.kube
  cp together-kubeconfig ~/.kube/config
  ```
  or
  ```bash  theme={null}
  KUBECONFIG=./together-kubeconfig:~/.kube/config kubectl config view --flatten > /tmp/merged_kubeconfig && mv /tmp/merged_kubeconfig ~/.kube/config    
  ```
  SkyPilot automatically picks up your credentials to the Together Instant Cluster.

3. Check that SkyPilot can access the Together Instant Cluster
   ```console  theme={null}
   $ sky check k8s
   Checking credentials to enable infra for SkyPilot.
     Kubernetes: enabled [compute]
       Allowed contexts:
       └── t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6: enabled.

   🎉 Enabled infra 🎉
     Kubernetes [compute]
       Allowed contexts:
       └── t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6

   To enable a cloud, follow the hints above and rerun: sky check
   If any problems remain, refer to detailed docs at: https://docs.skypilot.co/en/latest/getting-started/installation.html
   ```
   Your Together cluster is now accessible with SkyPilot.

4. Check the available GPUs on the cluster:
   ```console  theme={null}
   $ sky show-gpus --infra k8s
   Kubernetes GPUs
   Context: t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6
   GPU   REQUESTABLE_QTY_PER_NODE  UTILIZATION  
   H100  1, 2, 4, 8                8 of 8 free  
   Kubernetes per-node GPU availability
   CONTEXT                                                                              NODE                GPU   UTILIZATION  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  cp-8ct86            -     0 of 0 free  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  cp-fjqbt            -     0 of 0 free  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  cp-hst5f            -     0 of 0 free  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  gpu-dp-gsd6b-k4m4x  H100  8 of 8 free  
   ```

#### Example: Finetuning gpt-oss-20b on the Together Instant Cluster

Launch a gpt-oss finetuning job on the Together cluster is now as simple as a single command:

```bash  theme={null}
sky launch -c gpt-together gpt-oss-20b.yaml
```

You can download the yaml file [here](https://github.com/skypilot-org/skypilot/tree/master/llm/gpt-oss-finetuning#lora-finetuning).

## Billing

#### Compute Billing

Instant Clusters offer two compute billing options: **reserved** and **on-demand**.

* **Reservations** – Credits are charged upfront or deducted for the full
  reserved duration once the cluster is provisioned. Any usage beyond the reserved
  capacity is billed at on-demand rates.
* **On-Demand** – Pay only for the time your cluster is running, with no upfront
  commitment.

See our [pricing page](https://www.together.ai/instant-gpu-clusters) for current rates.

#### Storage Billing

Storage is billed on a **pay-as-you-go** basis, as detailed on our [pricing
page](https://www.together.ai/instant-gpu-clusters). You can freely increase or
decrease your storage volume size, with all usage billed at the same rate.

#### Viewing Usage and Invoices

You can view your current usage anytime on the [Billing page in
Settings](https://api.together.ai/settings/billing). Each invoice includes a
detailed breakdown of reservation, burst, and on-demand usage for compute and
storage

#### Cluster and Storage Lifecycles

Clusters and storage volumes follow different lifecycle policies:

* **Compute Clusters** – Clusters are automatically decommissioned when their
  reservation period ends. To extend a reservation, please contact your account
  team.
* **Storage Volumes** – Storage volumes are persistent and remain available as
  long as your billing account is in good standing. They are not automatically
  deleted. The user data persists as long as you use the static PV we provide.

#### Running Out of Credits

When your credits are exhausted, resources behave differently depending on their
type:

* **Reserved Compute** – Existing reservations remain active until their
  scheduled end date. Any additional on-demand capacity used to scale beyond the
  reservation is decommissioned.
* **Fully On-Demand Compute** – Clusters are first paused and then
  decommissioned if credits are not restored.
* **Storage Volumes** – Access is revoked first, and the data is later
  decommissioned.

You will receive alerts before these actions take place. For questions or
assistance, please contact your billing team.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt
# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/cluster.md

# Cluster

Manage and monitor your compute cluster nodes for ML workloads.

![Cluster Overview](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-eb1b1e444152724673997582ca3178eac41c1d5d%2Fcluster_list_view.png?alt=media)

## Overview

The Cluster section provides comprehensive management of compute nodes that power your ML experiments, training jobs, and deployments. Monitor resource utilization, manage node configurations, and ensure optimal cluster health.

## Cluster Dashboard

The dashboard displays key cluster metrics at a glance:

**Summary Cards**:

* **Total Nodes**: Total number of nodes in the cluster
* **Online**: Number of nodes currently online
* **Busy**: Number of nodes actively processing workloads
* **CPU Usage (%)**: Average CPU usage across cluster
* **Memory Usage (%)**: Average memory usage across cluster

## Node List View

The cluster table shows all nodes with the following information:

**Columns**:

* **Node**: Node name and details (hostname, IP address)
* **Type**: Node type (GPU, CPU)
* **Status**: Current status (Online, Offline, Maintenance)
* **Resources**: Available resources (CPU cores, RAM, GPU)
* **Usage**: Real-time CPU and Memory usage with progress bars
* **Jobs**: Running jobs count
* **Uptime**: Node uptime duration
* **Health**: Health status (Healthy, Warning, Critical)
* **Actions**: Quick actions menu

**Filtering and Search**:

* Search by node name or IP
* Filter by Type (GPU, CPU, All)
* Filter by Status (Online, Offline, Busy, Maintenance)

## Creating a Cluster Node

Navigate to **Deep Learning Platform** → **Cluster** → Click **Create**

![Create Cluster Node](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-e3ab7a5032fb62882c021a1e7b4579b8bdbfdb6a%2Fcluster_create_form.png?alt=media)

### Basic Information

**Node Name**\* (Required)

* Unique identifier for the cluster node
* Example: `gpu-node-01`, `cpu-node-high-mem`

**Hostname**\* (Required)

* Network hostname
* Example: `gpu01.cluster.local`

**IP Address**\* (Required)

* IPv4 address of the node
* Example: `192.168.1.101`

**Node Type**\* (Required)

* Select from dropdown: GPU, CPU
* Default: `GPU`

**Status**\* (Required)

* Select from dropdown: Online, Offline
* Default: `Online`

### CPU Resources

**CPU Cores**\* (Required)

* Total number of CPU cores
* Example: `16`

**Total number of CPU Cores** (Helper text)

**Available CPU Cores**\* (Required)

* Number of available CPU cores
* Example: `8`

**Number of available CPU cores** (Helper text)

### Memory Resources

**Total Memory (GB)**\* (Required)

* Total RAM in GB
* Example: `64`

**Total RAM in GB** (Helper text)

**Available Memory (GB)**\* (Required)

* Available RAM in GB
* Example: `32`

**Available memory (GB)** (Helper text)

### GPU Resources (Optional)

**GPU Count**

* Number of GPUs (0 for CPU-only nodes)
* Example: `0`, `4`, `8`

**Number of GPUs (0 for CPU-only nodes)** (Helper text)

**GPU Type**

* Select GPU model from dropdown
* Options: NVIDIA A100, NVIDIA V100, NVIDIA T4, etc.

**GPU Memory per GPU (GB)**

* Memory per GPU in GB
* Example: `80` (for A100)

**VRAM per GPU in GB** (Helper text)

### Storage & Network

**Total Storage (GB)**\* (Required)

* Total disk storage in GB
* Example: `1000`

**Total disk space in GB** (Helper text)

**Network Bandwidth (Mbps)**\* (Required)

* Network bandwidth in Mbps
* Example: `10000` (10 Gbps)

**Network speed in Mbps** (Helper text)

**Network Latency (ms)**\* (Required)

* Average network latency in milliseconds
* Example: `1`

**Average network latency** (Helper text)

### Configuration

**Max Concurrent Jobs**\* (Required)

* Maximum number of jobs that can run simultaneously
* Example: `4`

**Maximum number of jobs that can run simultaneously** (Helper text)

**Priority**

* Node priority (1-10, higher is better)
* Example: `5`

**Node priority (1-10, higher is better)** (Helper text)

**Tags**

* Comma-separated tags for categorization
* Example: `production,high-memory,gpu`

### Location (Optional)

**Datacenter**

* Datacenter location
* Example: `Datacenter`

**Rack**

* Rack identifier
* Example: `R-10`

**Zone**

* Availability zone
* Example: `Zone-A`

### Actions

* **Cancel**: Discard and close
* **Create Cluster Node**: Submit and create the node

## Viewing Node Details

To view detailed information about a cluster node:

1. Navigate to **Deep Learning Platform** → **Cluster**
2. Click on a node from the list
3. View comprehensive details in the modal dialog

![View Cluster Node](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-c5fb3b62ac87bc81b3fd451ca97fc398d34c604f%2Fcluster_details_view.png?alt=media)

**Details Panel Sections**:

**Basic Information**:

* Node Name: e.g., "gpu-node-01"
* Hostname: e.g., "gpu01.cluster.local"
* IP Address: e.g., "192.168.1.101"
* Node Type: GPU or CPU
* Status: Online, Offline, Busy, Maintenance

**CPU Resources**:

* CPU Cores: Total cores (e.g., 32)
* Total number of CPU cores
* Available CPU Cores: Available cores (e.g., 11)
* Number of available CPU cores

**Memory Resources**:

* Total Memory (GB): Total RAM (e.g., 128)
* Total RAM in GB
* Available Memory (GB): Available RAM (e.g., 32)
* Available memory (GB)

**GPU Resources (Optional)**:

* GPU Count: Number of GPUs (e.g., 4)
* Number of GPUs (0 for CPU-only nodes)
* GPU Type: GPU model (e.g., A100)
* GPU Memory per GPU (GB): VRAM per GPU (e.g., 80)
* VRAM per GPU in GB

**Storage & Network**:

* Total Storage (GB): Total disk space
* Total disk space in GB
* Network Bandwidth (Mbps): Network speed
* Network speed in Mbps
* Network Latency (ms): Average latency
* Network speed in Mbps

**Configuration**:

* Max Concurrent Jobs: Maximum simultaneous jobs
* Maximum number of jobs that can run simultaneously
* Priority: Node priority
* Node priority (1-10, higher is better)
* Tags: Comma-separated tags for categorization

**Location (Optional)**:

* Datacenter: Datacenter location
* Rack: Rack identifier
* Zone: Availability zone

## Editing a Node

To update node configuration:

1. Open node details page
2. Click **Edit** button (or three-dot menu → Edit)
3. Modify editable fields in the Edit Cluster Node modal

![Edit Cluster Node](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-c070253b720872ee5450c4afab2bbc40c5a7d8d4%2Fcluster_edit_form.png?alt=media)

4. Click **Update Cluster Node** to save changes

> \[!NOTE] The Edit form is identical to the View form, but with editable fields and an "Update Cluster Node" button.

**Editable Fields**:

* ✅ Hostname
* ✅ Status (Online, Offline, Maintenance)
* ✅ Available CPU Cores
* ✅ Available Memory (GB)
* ✅ GPU configuration
* ✅ Storage & Network settings
* ✅ Max Concurrent Jobs
* ✅ Priority
* ✅ Tags
* ✅ Location information
* ❌ Node Name (cannot edit)
* ❌ IP Address (cannot edit)
* ❌ Node Type (cannot edit)
* ❌ Total CPU Cores (cannot edit)
* ❌ Total Memory (cannot edit)

## Node Management

### Changing Node Status

**Setting to Maintenance**:

1. Open node details
2. Click **Edit**
3. Change Status to "Maintenance"
4. Save changes
5. Node will stop accepting new jobs

**Bringing Node Online**:

1. Open node details
2. Click **Edit**
3. Change Status to "Online"
4. Save changes
5. Node will start accepting jobs

### Monitoring Node Health

**Health Indicators**:

* **Healthy** (Green): All systems normal
* **Warning** (Orange): High resource usage or minor issues
* **Critical** (Red): Node failure or severe issues

**When to Check**:

* High CPU/Memory usage (>90%)
* Jobs failing frequently
* Network connectivity issues
* Hardware errors

### Deleting a Node

To remove a node from the cluster:

1. Navigate to node details
2. Click **Delete** button
3. Confirm deletion

> \[!WARNING] You cannot delete a node with running jobs. Stop or migrate jobs first.

**Before Deleting**:

* Ensure no jobs are running
* Migrate important jobs to other nodes
* Backup any local data
* Update cluster capacity planning

## Best Practices

**Resource Allocation**:

* Reserve some resources for system overhead
* Don't allocate 100% of available resources
* Monitor usage patterns and adjust

**Node Naming**:

* Use descriptive names: `gpu-node-01`, `cpu-highmem-02`
* Include node type in name
* Use consistent naming convention

**Maintenance**:

* Schedule regular maintenance windows
* Update node status before maintenance
* Monitor health indicators
* Keep firmware and drivers updated

**Tagging Strategy**:

* Use tags for organization: `production`, `development`
* Tag by capability: `high-memory`, `gpu`, `fast-storage`
* Tag by location: `datacenter-a`, `rack-10`

## Next Steps

* Submit [Jobs](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/jobs) to cluster nodes
* Run [Experiments](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/experiments) on GPU nodes
* Monitor resource usage in [Analytics](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/analytics)
* Deploy models via [Deployments](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/deployments)

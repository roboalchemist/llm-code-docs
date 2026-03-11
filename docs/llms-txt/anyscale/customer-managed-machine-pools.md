# Source: https://docs.anyscale.com/archive/customer-managed-machine-pools.md

# Customer-managed on-prem machine pools (legacy)

[View Markdown](/archive/customer-managed-machine-pools.md)

# Customer-managed on-prem machine pools (legacy)

warning

Customer-managed machine pools are deprecated and will be fully removed from the Anyscale platform on December 5, 2025. Contact your Anyscale account representative if you're using customer-mananged machine pools and require an extension.

Anyscale recommends using Kubernetes to register on-premises resources for use with Anyscale. You can use Anyscale-managed machine pools with cloud resources backed by Kubernetes, including on-premises Kubernetes clusters. See [Deploy Anyscale on Kubernetes](/admin/cloud/kubernetes.md) and contact [Anyscale Support](mailto:support@anyscale.com) to get started.

Customer-managed machine pools allow you to submit jobs to on-premises machines from Anyscale.

![](/img/machine-pools/machine-pools.png)

## Requirements[​](#requirements "Direct link to Requirements")

To set up a customer-managed machine pool, you need:

1. The Anyscale CLI.

2. An Anyscale cloud deployed on the VM compute stack on either AWS or GCP.

3. One or more target machines (for example, on-premises machines).

4. Networking between the machine pool location and the Anyscale cloud's VPC. This can be done in one of two ways:

   <!-- -->

   1. [Anyscale-managed overlay networking (recommended)](#overlay-network).

   2. A private network between the machine pool location and the Anyscale cloud's VPC.

      <!-- -->

      1. Updated Anyscale cloud firewall rules or security group rules to allow:

         <!-- -->

         1. Preferably - all traffic from the on-prem environment on all ports.
         2. Minimally - traffic destined to ports: 80, 443, 1010, 1012, 2222, 5555, 5903, 6379, 6822, 6823, 6824, 6826, 7878, 8000, 8076, 8085, 8201, 8265, 8266, 8686, 8687, 8912, 8999, 9090, 9092, 9100, 9478, 9479, 9480, 9481, 9482.

## Example workflow[​](#workflow "Direct link to Example workflow")

### Create a machine pool[​](#create "Direct link to Create a machine pool")

To create a machine pool, run the following command:

```
pip install --upgrade anyscale

anyscale machine-pool create --name MACHINE_POOL_NAME
```

### Attach the machine pool to one or more clouds[​](#attach "Direct link to Attach the machine pool to one or more clouds")

To attach a machine pool to a cloud, run the following command:

```
anyscale machine-pool attach --name MACHINE_POOL_NAME --cloud CLOUD_NAME
```

### Register a machine into the machine pool[​](#register "Direct link to Register a machine into the machine pool")

#### Step 1 - Validate dependencies[​](#validate "Direct link to Step 1 - Validate dependencies")

On all distributions, make sure that `containerd`, `runc`, `nfs-common`, and Nvidia drivers are installed. Also, make sure your [host OS uses cgroupv2](https://unix.stackexchange.com/a/508826). Below is a script that can be used to install all dependencies. Note that there are some sections that are specific to a single distribution.

Click to view installation script

```
#!/usr/bin/env bash
set -vex

# ------------------------------------------------------------------------------------------
# [COMMON INSTRUCTIONS]
# ------------------------------------------------------------------------------------------

# Install containerd

sudo apt-get update && sudo apt-get upgrade

sudo apt-get install pigz

VERSION="1.7.6"
CONTAINERD_TAR=containerd-$VERSION-linux-amd64.tar.gz
curl -fsSL https://github.com/containerd/containerd/releases/download/v$VERSION/$CONTAINERD_TAR -o /tmp/$CONTAINERD_TAR
sudo tar Cxzvf /usr/local /tmp/$CONTAINERD_TAR
sudo mkdir -p /usr/local/lib/systemd/system

sudo tee /usr/local/lib/systemd/system/containerd.service <<EOF
# Copyright The containerd Authors.
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
[Unit]
Description=containerd container runtime
Documentation=https://containerd.io
After=network.target local-fs.target
[Service]

ExecStartPre=-/sbin/modprobe overlay
ExecStart=/usr/local/bin/containerd
Type=notify
Delegate=yes
KillMode=process
Restart=always
RestartSec=5


LimitNPROC=infinity
LimitCORE=infinity
LimitNOFILE=infinity

TasksMax=infinity
OOMScoreAdjust=-999
[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now containerd

# Install runc

curl -fsSL https://github.com/opencontainers/runc/releases/download/v1.1.9/runc.amd64 -o /tmp/runc.amd64
sudo install -m 755 /tmp/runc.amd64 /usr/local/sbin/runc

# Install nfs-common and stunnel4

sudo apt-get install -y nfs-common stunnel4
stunnel -help
mount.nfs -V

# ------------------------------------------------------------------------------------------
# [UNCOMMENT FOR RHEL8 DISTRIBUTIONS ONLY]
# ------------------------------------------------------------------------------------------

# Change to cgroupv2
# sudo grubby --update-kernel=ALL --args='systemd.unified_cgroup_hierarchy'

# Disable selinux
# sudo grubby --update-kernel ALL --args selinux=0

# Reboot the machine
# sudo reboot
# ------------------------------------------------------------------------------------------
```

#### Step 2 - Install the `anyscalemachine` binary[​](#step-2---install-the-anyscalemachine-binary "Direct link to step-2---install-the-anyscalemachine-binary")

Run the following installation script to install the Anyscale machine manager. **Note that this script requires Anyscale credentials, and also must be run as root.**

Click to view installation script

```
#!/bin/bash

set -euo pipefail

curl -s -L -X 'GET' \
	"${ANYSCALE_HOST:-https://console.anyscale.com}/api/v2/machines/cli" \
	-H "Authorization: Bearer ${ANYSCALE_CLI_TOKEN}" | tar -x
mv -f anyscalemachine /usr/local/bin/

chmod +x /usr/local/bin/anyscalemachine
```

#### Step 3 - Start the `anyscalemachine` binary[​](#step-3---start-the-anyscalemachine-binary "Direct link to step-3---start-the-anyscalemachine-binary")

Finally, start the machine manager on the machine using the following command. **This also requires Anyscale credentials.**

Click to see start script

```
/usr/local/bin/anyscalemachine up --anyscale-host=<ANYSCALE_HOST> \
  --anyscale-cli-token=<ANYSCALE_CLI_TOKEN> \
  --machine-pool <MACHINE_POOL_NAME> \
  --machine-type <MACHINE_TYPE> \
  --internal-network-interface <INTERNAL_NETWORK_INTERFACE>
```

Optionally, you can explicitly specify the number of CPUs, GPUs, and amount of memory:

```
/usr/local/bin/anyscalemachine up --anyscale-host=<ANYSCALE_HOST> \
  --anyscale-cli-token=<ANYSCALE_CLI_TOKEN> \
  --machine-type <MACHINE_TYPE> \
  --internal-network-interface <INTERNAL_NETWORK_INTERFACE> \
  --num-cpus=<cpu> \
  --num-gpus=<gpu> \
  --memory-bytes=<num>
```

Anyscale recommends setting `INTERNAL_NETWORK_INTERFACE` to the network interface you want node-to-node communication to occur over, such as the Tailscale interface. To find the network interface to use, use `route` or `ip link show`.

### List machines using the `anyscale` CLI[​](#list-machines-using-the-anyscale-cli "Direct link to list-machines-using-the-anyscale-cli")

When the machine manager has successfully started, the machine should show up when querying for the list of machines in a cloud using the Anyscale CLI. **This should be done in an environment in which you have the Anyscale CLI installed, such as your laptop.**

```
anyscale machine list --machine-pool-name MACHINE_POOL_NAME
```

### Launch a workload using the machine[​](#launch-a-workload-using-the-machine "Direct link to Launch a workload using the machine")

Create a new compute config using the following template. This includes a head node that's deployed in your cloud's primary provider/region and worker nodes that are running in your on-prem environment.

* AWS (EC2)
* GCP (GCE)

Example compute config for AWS.

```
cloud: CLOUD_NAME

head_node:
  instance_type: m5.8xlarge

worker_nodes:
- instance_type: MACHINE_TYPE
  flags:
    cloud_deployment:
      machine_pool: MACHINE_POOL_NAME
  min_nodes: 1
  max_nodes: 1

# Other (regular) worker nodes may be added here as well.

# flags:
  # Uncomment the following flag for RHEL8.
  #
  # RHEL8 doesn't support squashfs, which is used by
  # Anyscale's snapshotter to accelerate cluster startup. This flag
  # configures the snapshotter to use ext4 images instead.
  # enable_snapshotter_ext4_image: true

  # Uncomment the following flag if using Anyscale-managed overlay networking.
  #
  # Anyscale-managed overlay networking is an opt-in feature that enables a
  # secure connection between your data center and cloud VPC. Contact Anyscale
  # support to enable this feature.
  #
  # use_anyscale_managed_overlay_network: true
```

Example compute config for GCP.

```
cloud: CLOUD_NAME

head_node:
  instance_type: n2-standard-8

worker_nodes:
- instance_type: MACHINE_TYPE
  flags:
    cloud_deployment:
      machine_pool: MACHINE_POOL_NAME
  min_nodes: 1
  max_nodes: 1

# Other (regular) worker nodes may be added here as well.

flags:
  # NOTE: RHEL8 doesn't support squashfs, which is used by
  # Anyscale's snapshotter to accelerate cluster startup. This flag
  # configures the snapshotter to use ext4 images instead.
  enable_snapshotter_ext4_image: true

  # NOTE: To use Anyscale-managed overlay networking between your
  # cloud and on-prem deployment, set this flag. For more details,
  # see below.
  use_anyscale_managed_overlay_network: true
```

With the YAML file created, create the compute config using the Anyscale CLI:

```
anyscale compute-config create -f PATH_TO_YAML --name COMPUTE_CONFIG_NAME
```

Once you create the compute config, launch an Anyscale workspace, job, or service using the compute config defined above, and check the event log for any errors.

## Anyscale managed overlay network[​](#overlay-network "Direct link to Anyscale managed overlay network")

When on-prem machines join a cluster based in a cloud environment such as AWS or GCP VPC, direct connectivity is required between these two networks. To streamline connectivity between nodes in an Anyscale cluster, you may choose to opt-in to an Anyscale-managed overlay network where Anyscale transparently manages the network path between machines in a cluster. Contact Anyscale support to opt-in to this feature.

Disclaimer

The Anyscale-managed overlay network uses Tailscale under the hood. See [How Tailscale works](https://tailscale.com/blog/how-tailscale-works).

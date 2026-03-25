# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/cluster-management.md

# Cluster management

> Manage your GitGuardian self-hosted Kubernetes cluster, including node operations, storage, and resource management.

## Overview

An overview of your cluster is available under the "Cluster Management" tab in
the Admin Console.

![Cluster Overview](/img/self-hosting/management/infrastructure-management/replicated_cluster_management.png)

Some key pieces of information:

- Nodes in the cluster.
- CPU, RAM, and disk availability on each node.

Nodes don't need to be of the same size.

Here, you can also find instructions to add a new node. You can also drain nodes.

## Adding worker nodes to Embedded cluster

If you want more processing power, you can scale your instance vertically by
using a more powerful machine.
But it is not always practical because it needs to be done before the
installation, and it also means a big machine will always be running.

Usually, a better solution is to scale horizontally by adding worker nodes to
the cluster. This solution is more flexible and allows to add and remove
processing capabilities when needed. A common use case is the initial historical
scan. If you have a lot of repositories, adding more CPUs can speed up this
process a lot.

**For nodes to communicate together, you need to open `30000` and [the following ports](https://docs.k0sproject.io/v0.13.1/networking/#needed-open-ports-protocols) between them.**

You can add a node at anytime ([installation](../../installation/installation-embedded-cluster-v2) included).

1. Connect with SSH to your other node.
2. Run the following to download the installer:

```bash
LICENSE_ID=your_license
curl -f https://replicated.app/embedded/gitguardian/stable -H "Authorization: $LICENSE_ID" -o gitguardian.tgz
tar -xvzf gitguardian.tgz
```

3. Go to the [KOTS Admin Console](./admin-console). Go to the "Cluster Management" tab. Click on "Add node"
4. Select roles to assign to the node
   1. `management` is used for control-plane/worker nodes (for high availability).
   2. The other roles are to be set depending on which kind of workload you intend to run.
   3. If you just need processing power and you don't know the exact usage, just select all roles (except `management`)
5. It will show you a command to add a node.
   ![Add Node Command](/img/self-hosting/management/infrastructure-management/replicated_v2_add_node_command.png)
6. Run it on your new node.
7. Run the join command
   ![Node added](/img/self-hosting/management/infrastructure-management/replicated_v2_add_node_success.png)

<!--  ## Remove a node -->

<!-- TODO -->

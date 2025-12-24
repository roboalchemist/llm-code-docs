# Source: https://documentation.ubuntu.com/lxd/en/latest/explanation/

[]

# Explanation[¶](#explanation "Link to this heading")

The explanatory guides in this section introduce you to the concepts used in LXD and help you understand how things fit together.

[]

## Important concepts[¶](#important-concepts "Link to this heading")

Before you start working with LXD, you need to be familiar with some important concepts about LXD and the instance types it provides.

-   [[`lxd`] and [`lxc`]](lxd_lxc/)
-   [Containers and VMs](instances/)

[]

## Entities in LXD[¶](#entities-in-lxd "Link to this heading")

When working with LXD, you should have a basic understanding of the different entities that are used in LXD. See the [[How-to guides]](../howto/#howtos) for instructions on how to work with these entities, and the following guides to understand the concepts behind them.

-   [Local and remote images](../image-handling/)
-   [Storage pools, volumes, and buckets](storage/)
-   [Networking setups](networks/)
-   [The LXD Dqlite database](../database/)
-   [[`lxc`] [`show`] and [`info`]](lxc_show_info/)

[]

## Access management[¶](#access-management "Link to this heading")

In LXD, access to the API is controlled through TLS or OpenID Connect authentication. When using OpenID Connect, you can grant permissions to access specific entities to different clients. You can also restrict access to LXD entities by confining them to specific projects.

-   [Remote API authentication](../authentication/)
-   [Remote API authorization](authorization/)
-   [Instances grouping with projects](projects/)

[]

## Production setup[¶](#production-setup "Link to this heading")

When you're ready to move your LXD setup to production, you should read up on the concepts that are important for providing a scalable, reliable, and secure environment.

-   [Clusters](clusters/)
-   [Performance tuning](performance_tuning/)
-   [Security](security/)
-   [Privilege delegation using BPF Token](bpf/)

[]

## The LXD CSI driver[¶](#the-lxd-csi-driver "Link to this heading")

The LXD CSI driver is an open source implementation of the Container Storage Interface (CSI) that integrates LXD storage backends with Kubernetes.

-   [The LXD CSI driver](csi/)
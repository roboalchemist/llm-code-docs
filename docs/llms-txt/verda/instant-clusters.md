# Source: https://docs.verda.com/clusters/instant-clusters.md

# Instant Clusters

You can now deploy high-performance GPU training clusters with Infiniband interconnect from your [Verda Cloud Console](https://console.verda.com/), the same way you would deploy a single GPU instance.

The only available contract length is: **Pay As You Go.**

Instant clusters are available with either Nvidia B200 SXM6 GPUs or Nvidia H200 SXM5 GPUs, a 3.2 Tb/s Infiniband interconnect per node (eight 400 Gb/s links), and a 100 Gbit/s Ethernet network. The uplink to the Internet is symmetric 2 Gb/s.

Our instant clusters range from 16 to 128 GPUs. Each cluster has up to 16 worker nodes, with 8 GPUs per worker node, and one jump host. Each worker node has local NVMe storage and access to a configurable shared filesystem with up to 50TB of storage.

Clusters have [Slurm](https://docs.verda.com/clusters/instant-clusters/slurm) pre-installed for easy job management and [Grafana dashboard](https://docs.verda.com/clusters/instant-clusters/monitoring) for monitoring and alerts. The Nvidia B200 instant clusters are currently available in `FIN-03` location and H200 instant clusters in `ICE-01` location.

**View more:**

[Deploying an Instant cluster](https://docs.verda.com/clusters/instant-clusters/deploying-your-cluster)

[Slurm](https://docs.verda.com/clusters/instant-clusters/slurm)

[Environments](https://docs.verda.com/clusters/instant-clusters/spack)

[Containers](https://docs.verda.com/containers)

[Monitoring](https://docs.verda.com/clusters/instant-clusters/monitoring)

[Good to know](https://docs.verda.com/clusters/instant-clusters/good-to-know)

[Local Users](https://docs.verda.com/clusters/instant-clusters/good-to-know-1)

{% embed url="<https://verda.com/instant-clusters>" %}

# Source: https://docs.verda.com/clusters/instant-clusters/good-to-know.md

# Good to know

### Cluster node naming convention

Cluster node names will be based on the `Hostname` you specify when creating the cluster:

* Jump host: `hostname-jumphost`
* Worker nodes: `hostname-1`, `hostname-2` , etc.

### Storage

There is a shared network filesystem mounted at `/home`on every node on the cluster.

Each worker node has a local NVMe drive mounted on `/mnt/local_disk` for extra fast I/O.

### Infiniband partitioning

Worker nodes are interconnected using a partitioned 400 Gb/s Infiniband fabric with `M_KEY`. For this reason commands like `ibhosts` will not work, while distributed workloads like MPI work correctly.

To use Infiniband and NCCL from inside a Docker container make sure to set environment variable `NCCL_IB_PKEY=1`.

For example:

```bash
docker run -e NCCL_IB_PKEY=1
```

### Other

Worker nodes are using the jump host as a default gateway, NAT firewall and Slurm controller.

`CUDA`, `OpenMPI`, `doca-ofed` and `nvidia-drivers` are installed on each server

Pytorch installer setup script is available in `/home/pytorch.setup.sh`.

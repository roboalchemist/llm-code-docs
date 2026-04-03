# Introduction -

Source: https://docs.lambda.ai/public-cloud/1-click-clusters/

---

[1-click clusters ](../../tags/#tag:1-click-clusters)[distributed training ](../../tags/#tag:distributed-training)
# Introduction [# ](#introduction)

1-Click Clusters (1CC) are high-performance clusters composed of both GPU and CPU nodes, featuring 16 to 512 NVIDIA H100 or B200 SXM Tensor Core GPUs. GPU nodes are interconnected using an NVIDIA Quantum-2 400 Gb/s InfiniBand non-blocking fabric in a rail-optimized topology, enabling peer-to-peer GPUDirect RDMA at up to 3200 Gb/s. All nodes (GPU and CPU) are equipped with 2x100 Gb/s Ethernet for IP communication and 2x100 Gb/s Direct Internet Access (DIA) connections. 

Each 1CC includes 3x CPU management (head) nodes for use as jump boxes (bastion hosts) and for cluster administration and job scheduling. These management nodes are assigned public IP addresses and are directly accessible over the Internet via SSH. 

All nodes can be directly accessed using [JupyterLab ](../on-demand/getting-started/#how-do-i-open-jupyterlab-on-my-instance)from the Lambda Cloud console. 

1CC nodes are in an isolated private network and can communicate freely with each other using private IP addresses. 

Generic CPU nodes can optionally be launched in the same regions as 1CCs. These generic CPU nodes run independently of 1CCs and don't terminate when 1CC reservations end. 

Each compute node includes 24TB of usable local ephemeral NVMe storage. Each management node includes 208GB of usable local ephemeral NVMe storage. [Lambda filesystems ](../filesystems/)are automatically created and attached to each 1CC node, and can also be attached to Lambda On-Demand instances. Existing filesystems in the same region can additionally be attached. [You’re billed only for the storage you actually use ](../billing/#filesystems). 

All 1CC nodes are preinstalled with Ubuntu 22.04 LTS and [Lambda Stack ](https://lambda.ai/lambda-stack-deep-learning-software), including NCCL, Open MPI, PyTorch® with DDP and FSDP support, TensorFlow, OFED, and other popular libraries and frameworks for distributed ML workloads, allowing ML engineers and researchers to begin their large-scale experiments and other work immediately after launching a 1CC. 

Note 

It's highly recommended that you use Lambda Stack's Python packages. Lambda Stack packages are extensively tested for compatibility and reliability in 1CC environments. Packages installed outside of Lambda Stack might not work properly, especially with newer GPUs. 

See our documentation on [creating a Python virtual environment ](../../education/programming/virtual-environments-containers/#creating-a-python-virtual-environment)to learn how to use Lambda Stack's Python packages.

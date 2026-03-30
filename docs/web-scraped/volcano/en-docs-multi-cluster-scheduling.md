# Source: https://volcano.sh/en/docs/multi_cluster_scheduling/

Title: Multi-Cluster AI Job Scheduling | Volcano

URL Source: https://volcano.sh/en/docs/multi_cluster_scheduling/

Published Time: 2025-01-21T00:00:00+00:00

Markdown Content:
Multi-Cluster AI Job Scheduling | Volcano
===============

Search
======

[](https://volcano.sh/en/docs/multi_cluster_scheduling/#)

[![Image 1: Volcano](https://volcano.sh/img/volcano_logo.svg)](https://volcano.sh/en/)

*   [Home](https://volcano.sh/en/#home_slider)
*   [About](https://volcano.sh/en/#about)
*   [Why Volcano](https://volcano.sh/en/#required)
*   [Blog](https://volcano.sh/en/#posts)
*   [Documentation](https://volcano.sh/en/docs/multi_cluster_scheduling/#)
    *   [latest](https://volcano.sh/en/docs)
    *   [v1.12.0](https://volcano.sh/en/docs/v1-12-0)
    *   [v1.11.0](https://volcano.sh/en/docs/v1-11-0)
    *   [v1.10.0](https://volcano.sh/en/docs/v1-10-0)
    *   [v1.9.0](https://volcano.sh/en/docs/v1-9-0)
    *   [v1.8.2](https://volcano.sh/en/docs/v1-8-2)
    *   [v1.7.0](https://volcano.sh/en/docs/v1-7-0)

*   [](https://volcano.sh/en/docs/multi_cluster_scheduling/#) 
*   [](https://github.com/volcano-sh/)
*   [](https://x.com/volcano_sh)
*   [![Image 2: slack](https://volcano.sh/img/icon_slack.svg)](https://cloud-native.slack.com/archives/C011GJDQS0N)
*   [English](https://volcano.sh/en/docs/multi_cluster_scheduling/#)
    *   [中文 (简体)](https://volcano.sh/zh/docs/multi_cluster_scheduling/)

[Home](https://volcano.sh/en/docs/)
*   [Introduction](https://volcano.sh/en/docs/)
*   [Architecture](https://volcano.sh/en/docs/architecture/)

[Getting Started](https://volcano.sh/en/docs/installation/)
*   [Installation](https://volcano.sh/en/docs/installation/)
*   [Tutorials](https://volcano.sh/en/docs/tutorials/)

[Concepts](https://volcano.sh/en/docs/queue/)
*   [Queue](https://volcano.sh/en/docs/queue/)
*   [PodGroup](https://volcano.sh/en/docs/podgroup/)
*   [VolcanoJob](https://volcano.sh/en/docs/vcjob/)
*   [Cron VolcanoJob](https://volcano.sh/en/docs/cron_volcanojob/)

[Key Features](https://volcano.sh/en/docs/network_topology_aware_scheduling/)
*   [Network Topology Aware Scheduling](https://volcano.sh/en/docs/network_topology_aware_scheduling/)
*   [Multi-Cluster AI Job Scheduling](https://volcano.sh/en/docs/multi_cluster_scheduling/)
*   [Cloud Native Colocation](https://volcano.sh/en/docs/colocation/)
*   [Load-aware Descheduling](https://volcano.sh/en/docs/descheduler/)
*   [Queue Resource Management](https://volcano.sh/en/docs/queue_resource_management/)
*   [Hierarchical Queue](https://volcano.sh/en/docs/hierarchical_queue/)
*   [Unified Scheduling](https://volcano.sh/en/docs/unified_scheduling/)
*   [GPU Virtualization](https://volcano.sh/en/docs/gpu_virtualization/)

[User Guide](https://volcano.sh/en/docs/user-guide/)
*   [Ascend vNPU User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_vnpu/)
*   [Capacity Plugin User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_capacity_plugin/)
*   [Cooldown Protection Plugin User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_cdp_plugin/)
*   [Extender User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_extender/)
*   [GPU Number User guide](https://volcano.sh/en/docs/user-guide/how_to_use_gpu_number/)
*   [GPU Sharing User guide](https://volcano.sh/en/docs/user-guide/how_to_use_gpu_sharing/)
*   [How to configure priorityclass for job](https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/)
*   [How to Configure Scheduler](https://volcano.sh/en/docs/user-guide/how_to_configure_scheduler/)
*   [How to Enable Dynamic Resource Allocation (DRA) in Volcano Scheduler](https://volcano.sh/en/docs/user-guide/how_to_enable_dra/)
*   [How to Tune Volcano Performance in Large-Scale Scenarios](https://volcano.sh/en/docs/user-guide/how_to_tune_volcano_performance/)
*   [HyperNode Auto Discovery User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_hypernode_auto_discovery/)
*   [MPI Plugin User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_mpi_plugin/)
*   [Network Topology Aware Scheduling User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_network_topology_aware_scheduling/)
*   [Nodegroup Plugin User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_nodegroup_plugin/)
*   [NUMA Aware User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_numa_aware/)
*   [Pytorch Plugin User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_pytorch_plugin/)
*   [Ray Plugin User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_ray_plugin/)
*   [Resource Strategy Fit Plugin User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/)
*   [Task Topology Plugin User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_task_topology_plugin/)
*   [Volcano Job Plugin -- Env User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_env_plugin/)
*   [Volcano Job Plugin -- SSH User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_ssh_plugin/)
*   [Volcano Job Plugin -- SVC User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_svc_plugin/)
*   [Volcano Job Policy User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_job_policy/)
*   [Volcano Job Time to Live User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_job_ttl/)
*   [Volcano vGPU User Guide](https://volcano.sh/en/docs/user-guide/how_to_use_volcano_vgpu/)

[Ecosystem](https://volcano.sh/en/docs/flink_on_volcano/)
*   [Flink](https://volcano.sh/en/docs/flink_on_volcano/)
*   [Kubeflow](https://volcano.sh/en/docs/kubeflow_on_volcano/)
*   [MindSpore](https://volcano.sh/en/docs/mindspore_on_volcano/)
*   [MPI](https://volcano.sh/en/docs/mpi_on_volcano/)
*   [PaddlePaddle](https://volcano.sh/en/docs/pp_on_volcano/)
*   [TensorFlow](https://volcano.sh/en/docs/tf_on_volcano/)
*   [Spark](https://volcano.sh/en/docs/spark_on_volcano/)
*   [Ray](https://volcano.sh/en/docs/ray_on_volcano/)

[Scheduler](https://volcano.sh/en/docs/schduler_introduction/)
*   [Overview](https://volcano.sh/en/docs/schduler_introduction/)
*   [Actions](https://volcano.sh/en/docs/actions/)
*   [Plugins](https://volcano.sh/en/docs/plugins/)
*   [Scenario & Configuration](https://volcano.sh/en/docs/referrals/)

[CLI](https://volcano.sh/en/docs/cli/)
*   [Commandline](https://volcano.sh/en/docs/cli/)

[Contribution](https://volcano.sh/en/docs/contribution/)
*   [Volcano Contribution](https://volcano.sh/en/docs/contribution/)
*   [Community Membership](https://volcano.sh/en/docs/membership/)

On this page

*       *   [Background](https://volcano.sh/en/docs/multi_cluster_scheduling/#background)
    *   [Features](https://volcano.sh/en/docs/multi_cluster_scheduling/#features)
    *   [Architecture](https://volcano.sh/en/docs/multi_cluster_scheduling/#architecture)
    *   [Usage Guide](https://volcano.sh/en/docs/multi_cluster_scheduling/#usage-guide)

*   [Back to top](https://volcano.sh/en/docs/multi_cluster_scheduling/#)

Multi-Cluster AI Job Scheduling
===============================

 Last updated on Jul 10, 2025 

Background
----------

With the rapid growth of enterprise business, a single Kubernetes cluster often cannot meet the demands of large-scale AI training and inference tasks. Users typically need to manage multiple Kubernetes clusters to achieve unified AI workload distribution, deployment, and management. Currently, many users are running Volcano across multiple clusters and using [Karmada](https://github.com/karmada-io/karmada) for management. To better support AI tasks in multi-cluster environments with features such as global queue management, task priority, and fair scheduling, the Volcano community has incubated the [Volcano Global](https://github.com/volcano-sh/volcano-global) sub-project. This project extends Volcano’s scheduling capabilities from single clusters to multi-cluster scenarios, providing a unified scheduling platform for multi-cluster AI tasks. It supports cross-cluster task distribution, resource management, and priority control.

Features
--------

Volcano Global enhances Karmada with the following features to meet the complex requirements of multi-cluster AI job scheduling:

1.   **Cross-Cluster Scheduling for Volcano Job** Users can deploy and schedule Volcano Jobs in a multi-cluster environment, fully utilizing the resources of multiple clusters to improve task execution efficiency.
2.   **Queue Priority Scheduling** Supports cross-cluster queue priority management, ensuring that tasks in high-priority queues can obtain resources first.
3.   **Job Priority Scheduling and Queuing** In a multi-cluster environment, supports job-level priority scheduling and queuing mechanisms, ensuring that critical tasks are executed promptly.
4.   **Multi-Tenant Fair Scheduling** Provides cross-cluster multi-tenant fair scheduling capabilities, ensuring fair and reasonable resource allocation among different tenants and avoiding resource contention.

Architecture
------------

![Image 3: image](https://volcano.sh/img/multi-cluster/volcano_global_design.svg)

Volcano Global consists of two components:

*   **Volcano Webhook:** Listens for the creation events of `ResourceBinding` resources and sets the `ResourceBinding` to a paused state.
*   **Volcano Controller:** Listens for `ResourceBinding` resources in the paused state, performs priority and fair scheduling based on the priority of the Job’s queue and the Job itself, and runs the resource admission mechanism to determine whether the Job can be scheduled. Once admission is successful, it resumes the `ResourceBinding`, allowing Karmada to distribute the resources.

Usage Guide
-----------

Please refer to: [Volcano Global Deploy](https://github.com/volcano-sh/volcano-global/blob/main/docs/deploy/README.md).

[![Image 4: up icon](https://volcano.sh/img/icon_up1.png)](https://volcano.sh/en/docs/multi_cluster_scheduling/#)

©2025 Volcano

# Source: https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/

Title: How to configure priorityclass for job | Volcano

URL Source: https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/

Published Time: 2026-02-03T00:00:00+00:00

Markdown Content:
How to configure priorityclass for job | Volcano
===============

Search
======

[](https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/#)

[![Image 1: Volcano](https://volcano.sh/img/volcano_logo.svg)](https://volcano.sh/en/)

*   [Home](https://volcano.sh/en/#home_slider)
*   [About](https://volcano.sh/en/#about)
*   [Why Volcano](https://volcano.sh/en/#required)
*   [Blog](https://volcano.sh/en/#posts)
*   [Documentation](https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/#)
    *   [latest](https://volcano.sh/en/docs)
    *   [v1.12.0](https://volcano.sh/en/docs/v1-12-0)
    *   [v1.11.0](https://volcano.sh/en/docs/v1-11-0)
    *   [v1.10.0](https://volcano.sh/en/docs/v1-10-0)
    *   [v1.9.0](https://volcano.sh/en/docs/v1-9-0)
    *   [v1.8.2](https://volcano.sh/en/docs/v1-8-2)
    *   [v1.7.0](https://volcano.sh/en/docs/v1-7-0)

*   [](https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/#) 
*   [](https://github.com/volcano-sh/)
*   [](https://x.com/volcano_sh)
*   [![Image 2: slack](https://volcano.sh/img/icon_slack.svg)](https://cloud-native.slack.com/archives/C011GJDQS0N)
*   [English](https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/#)
    *   [中文 (简体)](https://volcano.sh/zh)

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

How to configure priorityclass for job
======================================

 Last updated on Feb 4, 2026 

Background[](https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/#background)
------------------------------------------------------------------------------------------------------

When a user creates a job, if there is no `PriorityClassName` specified in the template of the task, the task will use the `PriorityClassName` specified by the job. The user can specify `PriorityClassName` in each task’s template to override the configuration of job, so that priority can be configured separately for each task.

Key Points[](https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/#key-points)
------------------------------------------------------------------------------------------------------

*   If the task does not specify `PriorityClassName` but the job does, the task will use the job’s PriorityClass, and the `PreemptionPolicy` and priority value will also be the same as the job.
*   When user needs to allow task in job to preempt other tasks if the resources are insufficient, a separate `PriorityClassName` must be set in the task’s template, and **it is important to note that if there are multiple tasks that need to be set to different priorities, then user need to set the `PriorityClassName` for all of them**, otherwise the task that does not specify `PriorityClassName` will use the PriorityClass of the job it belongs to.

Example[](https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/#example)
------------------------------------------------------------------------------------------------

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: job-priority
value: 1
preemptionPolicy: Never
---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: task-priority
value: 10
---
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: job
spec:
  schedulerName: volcano
  priorityClassName: job-priority
  minAvailable: 1
  tasks:
    - replicas: 1
      name: preempt-task
      template:
        spec:
          priorityClassName: task-priority # The priorityclass is specified individually for this task
          containers:
            - image: alpine
              command: ["/bin/sh", "-c", "sleep 1000"]
              name: preempt
              resources:
                requests:
                  cpu: 1
    - replicas: 1
      name: non-preempt-task # This task does not specify PriorityClassName, so it will use the "job-priority" priorityclass specified by job
      template:
        spec:
          containers:
            - image: alpine
              command: ["/bin/sh", "-c", "sleep 1000"]
              name: non-preempt
              resources:
                requests:
                  cpu: 1
```
Copy

[![Image 3: up icon](https://volcano.sh/img/icon_up1.png)](https://volcano.sh/en/docs/user-guide/how_to_configure_priorityclass_for_job/#)

©2025 Volcano

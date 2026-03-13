# Source: https://kueue.sigs.k8s.io/docs/concepts/workload/

Title: Workload

URL Source: https://kueue.sigs.k8s.io/docs/concepts/workload/

Published Time: 2022-02-14T00:00:00+00:00

Markdown Content:
An application that will run to completion. It is the unit of admission in Kueue. Sometimes referred to as job.

A _workload_ is an application that will run to completion. It can be composed by one or multiple Pods that, loosely or tightly coupled, as a whole, complete a task. A workload is the unit of [admission](https://kueue.sigs.k8s.io/docs/concepts/#admission) in Kueue.

The prototypical workload can be represented with a [Kubernetes `batch/v1.Job`](https://kubernetes.io/docs/concepts/workloads/controllers/job/). For this reason, we sometimes use the word _job_ to refer to any workload, and Job when we refer specifically to the Kubernetes API.

However, Kueue does not directly manipulate Job objects. Instead, Kueue manages Workload objects that represent the resource requirements of an arbitrary workload. Kueue automatically creates a Workload for each Job object and syncs the decisions and statuses.

The manifest for a Workload looks like the following:

```
apiVersion: kueue.x-k8s.io/v1beta2
kind: Workload
metadata:
  name: sample-job
  namespace: team-a
spec:
  active: true
  queueName: team-a-queue
  podSets:
  - count: 3
    name: main
    template:
      spec:
        containers:
        - name: container
          image: registry.k8s.io/e2e-test-images/agnhost:latest
          args: ["pause"]
          imagePullPolicy: Always
          resources:
            requests:
              cpu: "1"
              memory: 200Mi
        restartPolicy: Never
```

Active [](https://kueue.sigs.k8s.io/docs/concepts/workload/#active)
-------------------------------------------------------------------

You can stop or resume a running workload by setting the [Active](https://kueue.sigs.k8s.io/docs/reference/kueue.v1beta1/#kueue-x-k8s-io-v1beta1-WorkloadSpec) field. The active field determines if a workload can be admitted into a queue or continue running, if already admitted. Changing `.spec.Active` from true to false will cause a running workload to be evicted and not be requeued.

Queue name [](https://kueue.sigs.k8s.io/docs/concepts/workload/#queue-name)
---------------------------------------------------------------------------

To indicate in which [LocalQueue](https://kueue.sigs.k8s.io/docs/concepts/local_queue/) you want your Workload to be enqueued, set the name of the LocalQueue in the `.spec.queueName` field.

Pod sets [](https://kueue.sigs.k8s.io/docs/concepts/workload/#pod-sets)
-----------------------------------------------------------------------

A Workload might be composed of multiple Pods with different pod specs.

Each item of the `.spec.podSets` list represents a set of homogeneous Pods and has the following fields:

*   `spec` describes the pods using a [`v1/core.PodSpec`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#PodSpec).
*   `count` is the number of pods that use the same `spec`.
*   `name` is a human-readable identifier for the pod set. You can use the role of the Pods in the Workload, like `driver`, `worker`, `parameter-server`, etc.

### Resource requests [](https://kueue.sigs.k8s.io/docs/concepts/workload/#resource-requests)

Kueue uses the `podSets` resources requests to calculate the quota used by a Workload and decide if and when to admit a Workload.

Kueue calculates the total resources usage for a Workload as the sum of the resource requests for each `podSet`. The resource usage of a `podSet` is equal to the resource requests of the pod spec multiplied by the `count`.

#### Requests values adjustment [](https://kueue.sigs.k8s.io/docs/concepts/workload/#requests-values-adjustment)

Depending on the cluster setup, Kueue will adjust the resource usage of a Workload based on:

*   The cluster defines default values in [Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/), the default values will be used if not provided in the `spec`.
*   The created pods are subject of a [Runtime Class Overhead](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/).
*   The spec defines only resource limits, case in which the limit values will be treated as requests.

#### Requests values validation [](https://kueue.sigs.k8s.io/docs/concepts/workload/#requests-values-validation)

In cases when the cluster defines Limit Ranges, the values resulting from the adjustment above will be validated against the ranges. Kueue will mark the workload as `Inadmissible` if the range validation fails.

#### Reserved resource names [](https://kueue.sigs.k8s.io/docs/concepts/workload/#reserved-resource-names)

In addition to the usual resource naming restrictions, you cannot use the `pods` resource name in a Pod spec, as it is reserved for internal Kueue use. You can use the `pods` resource name in a [ClusterQueue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/#resources) to set quotas on the maximum number of pods.

Priority [](https://kueue.sigs.k8s.io/docs/concepts/workload/#priority)
-----------------------------------------------------------------------

Workloads have a priority that influences the [order in which they are admitted by a ClusterQueue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/#queueing-strategy). There are two ways to set the Workload priority:

*   **Pod Priority**: You can see the priority of the Workload in the field `.spec.priority`. For a `batch/v1.Job`, Kueue sets the priority of the Workload based on the [pod priority](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/) of the Job’s pod template.

*   **WorkloadPriority**: Sometimes developers would like to control workload’s priority without affecting pod’s priority. By using [`WorkloadPriority`](https://kueue.sigs.k8s.io/docs/concepts/workload_priority_class/), you can independently manage the priority of workloads for queuing and preemption, separate from pod’s priority.

Custom Workloads [](https://kueue.sigs.k8s.io/docs/concepts/workload/#custom-workloads)
---------------------------------------------------------------------------------------

As described previously, Kueue has built-in support for workloads created with the Job API. But any custom workload API can integrate with Kueue by creating a corresponding Workload object for it.

Dynamic Reclaim [](https://kueue.sigs.k8s.io/docs/concepts/workload/#dynamic-reclaim)
-------------------------------------------------------------------------------------

It’s a mechanism allowing a currently Admitted workload to release a part of it’s Quota Reservation that is no longer needed.

Job integrations communicate this information by setting the `reclaimablePods` status field, enumerating the number of pods per podset for which the Quota Reservation is no longer needed.

```
status:
  reclaimablePods:
  - name: podset1
    count: 2
  - name: podset2
    count: 2
```

The `count` can only increase while the workload holds a Quota Reservation.

All-or-nothing semantics for Job Resource Assignment [](https://kueue.sigs.k8s.io/docs/concepts/workload/#all-or-nothing-semantics-for-job-resource-assignment)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

This mechanism allows a Job to be evicted and re-queued if the job doesn’t become ready. Please refer to the [All-or-nothing with ready Pods](https://kueue.sigs.k8s.io/docs/tasks/manage/setup_wait_for_pods_ready/) for more details.

### Exponential Backoff Requeueing [](https://kueue.sigs.k8s.io/docs/concepts/workload/#exponential-backoff-requeueing)

Once evictions with `PodsReadyTimeout` reasons occur, a Workload will be re-queued with backoff. The Workload status allows you to know the following:

*   `.status.requeueState.count` indicates the numbers of times a Workload has already been backoff re-queued by Eviction with PodsReadyTimeout reason
*   `.status.requeueState.requeueAt` indicates the time when a Workload will be re-queued the next time

```
status:
  requeueState:
    count: 5
    requeueAt: 2024-02-11T04:51:03Z
```

When a Workload deactivated by All-or-nothing with ready Pods is re-activated, the requeueState (`.status.requeueState`) will be reset to null.

Replicate labels from Jobs into Workloads [](https://kueue.sigs.k8s.io/docs/concepts/workload/#replicate-labels-from-jobs-into-workloads)
-----------------------------------------------------------------------------------------------------------------------------------------

You can configure Kueue to copy labels, at Workload creation, into the new Workload from the underlying Job or Pod objects. This can be useful for Workload identification and debugging. You can specify which labels should be copied by setting the `labelKeysToCopy` field in the configuration API (under `integrations`). By default, Kueue does not copy any Job or Pod label into the Workload.

Maximum execution time [](https://kueue.sigs.k8s.io/docs/concepts/workload/#maximum-execution-time)
---------------------------------------------------------------------------------------------------

You can configure a Workload’s maximum execution time by specifying the expected maximum number of seconds for it to run in:

```
spec:
  maximumExecutionTimeSeconds: n
```

If the workload spends more then `n` seconds in `Admitted` state, including the time spent as `Admitted` in previous “Admit/Evict” cycles, it gets automatically deactivated. Once deactivated, the accumulated time spent as active in previous “Admit/Evict” cycles is set to 0.

If `maximumExecutionTimeSeconds` is not specified, the workload has no execution time limit.

You can configure the `maximumExecutionTimeSeconds` of the Workload associated with any supported Kueue Job by specifying the desired value as `kueue.x-k8s.io/max-exec-time-seconds` label of the job.

Workload updates by Kueue [](https://kueue.sigs.k8s.io/docs/concepts/workload/#workload-updates-by-kueue)
---------------------------------------------------------------------------------------------------------

Feature state alpha since Kueue v0.14

By default Workload status updates are performed by Kueue using the [Server-Side Apply (SSA)](https://kubernetes.io/docs/reference/using-api/server-side-apply/).

However due to the limitations of SSA ([missing support for duplicated key/value pairs](https://github.com/kubernetes/kubernetes/issues/113482)) we also offer to enable updating the Workload status with Merge Patches, by enabling the `WorkloadRequestUseMergePatch` feature gate.

In particular, this allows users of Kueue to handle the following two issues:

*   [Add option to disable strict pod spec validation](https://github.com/kubernetes-sigs/kueue/issues/3540) Switching from ServerSideApply to Merge Patch allows partial updates without requiring the entire resource specification. This can bypass the strict validation rules causing issues with duplicated environment variables, aligning Kueue’s behavior more closely with plain Kubernetes
*   [MultiKueue: remove the limitation that the external dispatches need to use kueue-admission field manager](https://github.com/kubernetes-sigs/kueue/issues/6185)Using ServerSideApply blocked the ability for Workload Status to be modified from external controllers. Once the field e.g. `.status.nominatedClusterNames` was modified and owned by the controller (regardless if Kueue or external one) it can not be modified or cleared by the other. This effectively prevent External Dispatching mechanism to work properly in multi cluster enviroment.

What’s next [](https://kueue.sigs.k8s.io/docs/concepts/workload/#whats-next)
----------------------------------------------------------------------------

*   Learn about [workload priority class](https://kueue.sigs.k8s.io/docs/concepts/workload_priority_class/).
*   Learn how to [run jobs](https://kueue.sigs.k8s.io/docs/tasks/run/jobs/)
*   Read the [API reference](https://kueue.sigs.k8s.io/docs/reference/kueue.v1beta1/#kueue-x-k8s-io-v1beta1-Workload) for `Workload`

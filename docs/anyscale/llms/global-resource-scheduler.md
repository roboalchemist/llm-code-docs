# Source: https://docs.anyscale.com/machine-pools/global-resource-scheduler.md

# What is the global resource scheduler?

[View Markdown](/machine-pools/global-resource-scheduler.md)

# What is the global resource scheduler?

The global resource scheduler maximizes utilization and maintains fairness while assigning compute resources from Anyscale machine pools to jobs, workspaces, and services. The global resource scheduler controls the following behaviors for workloads configured to use machine pools:

* Allocates machines from the machine pool to a workload.
* Schedules workloads based on priority, required resources, time, and workload type.
* Evicts machines being used by other workloads to make room for an incoming workload.
* Queues workloads until machines are available.

See [Share compute resources with Anyscale machine pools](/machine-pools.md).

info

Machine pools and the global resource scheduler are in beta release.

## How does the global resource scheduler work?[​](#how-does-the-global-resource-scheduler-work "Direct link to How does the global resource scheduler work?")

The global resource scheduler is a service in the Anyscale control plane that manages scheduling for machine pool resources.

When a workload requests machine pool instances, the global resource scheduler evaluates the request based on user-defined rules. It then makes a scheduling decision based on workload priority and available resources.

You configure the rules for your machine pools with regards to scheduling priorities, then set complementary rules in the compute config for your workloads. For example, you can configure the global resource scheduler to reserve up to 25% of the GPUs in a machine pool for development work, but let production jobs or services expand to 100% of GPU capacity when development resources aren't in use.

## How does Anyscale queue workloads?[​](#how-does-anyscale-queue-workloads "Direct link to How does Anyscale queue workloads?")

If the machine pool doesn't have sufficient machines for a workload, the global resource scheduler places the workload in a first-in, first-out (FIFO) queue. The workload state reports as `STARTING` or `PENDING`. Workloads can bypass the queue if they're runnable while earlier submissions aren't.

The scheduler preempts running jobs when a job with higher priority requires resources. When preempted, a job enters the queue with the following behaviors:

* The scheduler enqueues the job using its start time. Because the job was previously running, this typically means the job is at the front of the queue relative to other jobs of the same priority.
* The job attempts to acquire the resources defined by the `min_nodes` parameter.
* The `workload_recovering_timeout` parameter defines how long the job continues to try to acquire resources. The job terminates due to timeout if it can't acquire enough resources in the defined window.
* If the `max_retries` parameter is greater than 0, the scheduler adds a new job to the end of the queue with a new workload start time.

## Set a workload timeout[​](#set-a-workload-timeout "Direct link to Set a workload timeout")

Anyscale respects the `workload_recovering_timeout` and `workload_starting_timeout` parameters when scheduling with machine pools.

Set timeout flags in the compute configuration to help manage queuing and recovery, as in the following example:

```
flags:
  # If the cluster doesn't satisfy min_resources for > 5 minutes while
  # in a RUNNING state, then terminate the workload (and re-queue
  # it if it's a job).
  workload_recovering_timeout: 5m
  # If the cluster doesn't satisfy min_resources for > 24h while in
  # a STARTING state, then terminate the workload. 
  workload_starting_timeout: 24h
```

These timeouts apply only to jobs and workspaces, not to services.

## Fall back to cloud capacity[​](#fall-back-to-cloud-capacity "Direct link to Fall back to cloud capacity")

Anyscale recommends including spot and on-demand instances as part of your machine pool definition, then defining an instance ranking strategy in your compute config to use these machine pool instances. This ensures that the global resource scheduler can manage request priority, preemption, and scheduling across your reserved capacity as well as spot and on-demand instances. For an example, see [Configure an Anyscale-managed machine pool](/machine-pools.md#configure).

## Machine pool observability[​](#machine-pool-observability "Direct link to Machine pool observability")

Anyscale provides a dashboard for monitoring machine pools in the Anyscale console. See [Monitor and observe machine pools in the Anyscale console](/machine-pools/console.md).

You can also use the following Anyscale CLI syntax to describe your machine pool:

```
anyscale machine-pool describe --name <machine-pool-name>
```

Returned details can help you debug scheduling behavior, view pending machine requests, and view recent cloud instance launch failures.

When the global resource schedule evicts a machine from a workload, it sends an eviction notice to the impacted workload. Eviction notices detail the cloud, project, user, and workload name that caused the eviction event. You can use these details to further tune priority ranking.

## Scheduling rules[​](#selector "Direct link to Scheduling rules")

You can assign scheduling rules to control how different workloads, clouds, and projects get priority on partitions when queueing workloads. Rules with higher numbers have higher priority for scheduling. Rules evaluate in the order specified. If a workloads matches multiple rules, it receives the priority for the first matching rule. If a workload doesn't match any rules or matches a rule with priority set to `0`, the global resource scheduler doesn't schedule the workload.

For a full example of a machine pool configuration with rules assigned to partitions, see [Machine pool configuration file reference](/machine-pools/config-ref.md).

Anyscale provides the following default labels for scheduling:

| Label           | Description                                 |
| --------------- | ------------------------------------------- |
| `workload-type` | Either `job`, `service`, or `workspace`.    |
| `cloud`         | The name of an Anyscale cloud.              |
| `project`       | The name of a project in an Anyscale cloud. |

You can also use custom resource tags to define scheduling rules. See [Example: Use custom resource tags for scheduling rules](#custom-tags).

Express Anyscale priority rules using the Kubernetes selector syntax. The following table contains examples of using this syntax:

| Objective                                                         | Example selector syntax                              |
| ----------------------------------------------------------------- | ---------------------------------------------------- |
| Select workloads of type `workspace` in cloud named `dev-cloud`   | `workload-type in (workspace), cloud in (dev-cloud)` |
| Select workloads of type `job`                                    | `workload-type=job`                                  |
| Select workloads of type `job` or `service`                       | `workload-type in (job,service)`                     |
| Select all workloads (all workloads have a `workload-type` label) | `workload-type`                                      |

See [Rule fields](/machine-pools/config-ref.md#rules).

note

You can block scheduling by setting rules with priority `0` at the top of your rules list. For example, the following rule explicitly excludes workspaces, even if they're in a cloud named `dev`, `qa`, or `prod`:

```
rules:
  - selector: workload-type=workspace
    priority: 0
  - selector: cloud=prod
    priority: 200
  - selector: cloud in (dev, qa)
    priority: 100
```

### Example: Use custom resource tags for scheduling rules[​](#custom-tags "Direct link to Example: Use custom resource tags for scheduling rules")

important

Custom resource tags are in beta release.

Define selector rules for custom tags to allow workloads to receive priority based on user-assigned labels.

You set custom tags in workload configurations, using CLI flags, or using CLI commands. Users with permissions to configure or submit workloads have the ability to set any tag. See [Add custom tags to workloads and cloud resources](/resources/custom-tags.md).

note

You can combine custom tag rules with the system-provided default labels `workload-type`, `cloud`, and `project`.

Anyscale doesn't prevent you from using the default labels as keys when setting custom tags, but the global resource scheduler always uses system-provided values for rules that uses these labels.

Changing tags for a running or queued workload impacts the priority for the workload. The global resource scheduler recalculates priority for the workload using the new tags, which might impact queue order or cause workload eviction for a higher priority workload. New priority for your workload applies after several minutes.

The following example configuration shows priority rules using the custom tags `prio`, `user`, and `team`:

```
rules:
  - selector: team=analytics
    priority: 30
  - selector: prio=p0
    priority: 200
  - selector: user=user3.company.com, prio=p1
    priority: 50
  - selector: user in (user1.company.com, user2.company.com)
    priority: 100
  - selector: team in (design, ml)
    priority: 80
```

The following table demonstrates the applied priority for different groups of labels:

| Labels                              | Priority | Description                           |
| ----------------------------------- | -------- | ------------------------------------- |
| `{user=user1.company.com, team=ml}` | 100      | Both rules match. Use the first rule. |
| `{team=finance, prio=p2}`           | 0        | Neither rule matches. No priority.    |
| `{team=finance, prio=p0}`           | 200      | One rule matches. Use that priority.  |
| `{team=analytics, prio=p0}`         | 30       | Both rules match. Use the first rule. |

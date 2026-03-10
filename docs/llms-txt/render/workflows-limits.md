# Source: https://render.com/docs/workflows-limits.md

# Limits and Pricing for Render Workflows


> *Render Workflows is in public beta.*
>
> During the beta, bugs or changes in API/SDK behavior are possible as we continue refining the product. We welcome any and all feedback at *workflows-feedback@render.com*.

Render bills for the following components of workflows:

| Billable | Description |
| --- | --- |
| *Compute usage* | Render bills for each task run based on its instance type and duration. [See details.](#instance-types-compute-specs) |
| *Added concurrency* | For an additional monthly charge, you can increase your workspace's max allowed number of concurrent task runs. [See details.](#concurrent-task-runs) |

Task runs can also contribute to your workspace's usage of outbound bandwidth.

## Instance types (compute specs)

Your workflow task runs execute on one of the following instance types:

| Instance Type | Specs | Price |
| --- | --- | --- |
| *`starter`* | 0.5 CPU 512 MB RAM | $0.05 / hour |
| *`standard`* (default) | 1 CPU 2 GB RAM | $0.20 / hour |
| *`pro`* | 2 CPU 4 GB RAM | $0.40 / hour |

- Billing for compute usage is prorated by the second.
    - If a task run executes on the `standard` instance type for half an hour, Render bills you $0.10, not $0.20.
- You can specify which instance type to use for each task you define. [Learn how.](/workflows-defining#instance-type-compute-specs)

### Larger instances

If you need to handle more resource-intensive workloads, you can request access to the following larger instance types for your workspace:

| Instance Type | Specs | Price |
| --- | --- | --- |
| *`pro_plus`* | 4 CPU 8 GB RAM | $1.00 / hour |
| *`pro_max`* | 8 CPU 16 GB RAM | $2.00 / hour |
| *`pro_ultra`* | 16 CPU 32 GB RAM | $7.00 / hour |

## Concurrent task runs

Render limits the total number of task runs that can execute concurrently in a single workspace, based on the workspace's [plan](/pricing):

| Workspace Plan | Base Concurrency | Max Concurrency (additional cost) |
| --- | --- | --- |
| *Hobby* | 20 runs | 200 runs |
| *Professional* | 50 runs | 200 runs |
| *Organization* | 100 runs | 300 runs |
| *Enterprise* | 100 runs | 300+ runs |

- *Base concurrency:* The number of concurrent runs your plan allows if you purchase no [additional concurrency](#increasing-concurrency).
- *Max concurrency:* The number of concurrent runs your plan allows if you purchase the maximum amount of [additional concurrency](#increasing-concurrency).

Whenever you trigger a run when your workspace is at its concurrency limit, Render queues the run to execute after another run completes.

> *This concurrency limit is workspace-wide.*
>
> Creating multiple workflow services in a workspace does not increase this limit.

### Increasing concurrency

You can increase the max number of concurrent runs allowed for your workspace by purchasing additional concurrency in the [Render Dashboard](https://dashboard.render.com).

#### Billing details

- You can add concurrency in multiples of 5 additional runs.
- Concurrency is billed monthly at $0.20 per additional run.
    - In other words, the smallest possible increase is 5 additional runs for $1.00 per month.
- Billing for concurrency is prorated by the second.
    - If you increase your concurrency by 5 additional runs halfway through a month, you're billed an additional $0.50 that month, not $1.00.
- Render bills for concurrency regardless of whether you trigger enough concurrent runs to use it.

#### Steps to increase concurrency

1. Open your workspace's *Settings* page and scroll down to the *Workflows* section:

    [image: Workflows settings in the Render Dashboard]

2. Under *Added concurrency*, click *Edit* and specify a number of concurrent runs to add.

3. Verify the amount of your additional monthly cost and click *Save changes*.

## Additional limits

| Limit | Description |
| --- | --- |
| *Argument size* | The total size of all arguments passed to a single task run cannot exceed *4 MB*. |
| *Run duration* | By default, task runs time out after *2 hours*. You can extend this to up to *24 hours* on a [per-task basis](/workflows-defining#timeout). |
| *Task definitions* | A single workflow service can register a maximum of *500* different tasks. |


---

##### Appendix: Glossary definitions

###### run

A single execution of a workflow *task*.

A run spins up in its own *instance*, executes, returns a value, and is deprovisioned.

Related article: https://render.com/docs/workflows-running.md

###### instance type

Specifies the RAM and CPU available to your service's *instances*.

Common instance types for a new web service include:

- *Free*: 512 MB RAM / 0.1 CPU
- *Starter*: 512 MB RAM / 0.5 CPU
- *Standard*: 2 GB RAM / 1 CPU

For the full list, see the [pricing page](/pricing#services).

###### outbound bandwidth

The amount of network traffic you send to destinations outside of Render (HTTP responses, third-party API calls, and so on).

Your workspace receives a monthly included amount of outbound bandwidth. If you exceed this amount, Render bills you for a supplementary amount.

Related article: https://render.com/docs/outbound-bandwidth.md

###### task

A function you can execute on its own compute as part of a *workflow*.

Each execution of a task is called a *run*.

Related article: https://render.com/docs/workflows-defining.md
# Source: https://render.com/docs/scaling.md

# Scaling Render Services — Run multiple instances to handle additional load.

You can run multiple instances of a web service, private service, or background worker to handle additional load. For services that receive incoming traffic, Render load balances that traffic evenly across all running instances:

[diagram]

Each instance of a scaled service uses the same instance type and is [billed accordingly](#billing-for-scaled-services). You can scale each service up to a maximum of 100 instances.

Render supports two scaling methods: *manual scaling* and *autoscaling*.

| Scaling Method | Description |
| --- | --- |
| [*Manual scaling*](#manual-scaling) | Render runs a fixed number of instances that you specify. Manual scaling is available for all Render workspaces. |
| [*Autoscaling*](#autoscaling) | *Available only for [Professional workspaces](professional-features) and higher.* Render automatically scales your number of instances between a specified minimum and maximum, based on target CPU and/or memory utilization. |

## Manual scaling

You can manually scale your service to any fixed number of instances, up to a maximum of 100.

1. In the [Render Dashboard](https://dashboard.render.com), open your service's *Scaling* page and scroll down to the *Manual Scaling* section:

   [image: Manual scaling settings in the Render Dashboard]

2. Drag the slider to the desired number of instances, or enter a value between `1` and `100` in the text box.
3. Click *Save Changes*.

Render immediately provisions or deprovisions instances as needed to match the new instance count.

Manual scaling events appear in the timeline on your service's *Events* page:

[image: Manual scaling event in the Render Dashboard]

## Autoscaling

> *Autoscaling requires a [*Professional workspace*](professional-features) or higher.*

Render can automatically scale your service up and down based on CPU and/or memory utilization targets that you specify. This helps you handle periods of high traffic while also minimizing compute costs.

Enable autoscaling for your service from its *Scaling* page in the [Render Dashboard](https://dashboard.render.com):

[image: Enabling autoscaling in the Render Dashboard]

1. Use the slider to set your desired minimum and maximum instance count, or enter a value in each text box.
   - Render always keeps your instance count within the specified range, even if resource utilization is significantly below or above your specified target.
2. Scroll down to set your target CPU and/or memory utilization:

   [image: Autoscaling settings in the Render Dashboard]

   Enable one or both of the toggles and set your target utilization percentage(s).

> If you enable _neither_ toggle, autoscaling is _disabled_ for the service.

3. Click *Save Changes*.

Render begins monitoring resource utilization and automatically scales your service up or down as needed based on your specified targets.

Autoscaling events appear in the timeline on your service's *Events* page:

[image: Autoscaling events in the Render Dashboard]

### How autoscaling works

Render periodically calculates average resource utilization across all instances of your autoscaled service. Using that value (`current_util`), Render determines whether to scale your service based on the following formula:

```
new_instances = ceil[current_instances * (current_util / target_util)]
```

If `new_instances` doesn't equal `current_instances`, Render scales your service up or down to the new instance count.

> *Render waits a few minutes before scaling a service _down_.*
>
> If utilization rises again during this period, Render does _not_ scale the service down. This minimizes unnecessary scaling actions during periods of "spiky" usage.
>
> Render always scales a service _up_ immediately to handle increased load.

#### Example 1: Scaling up

| Current instances | Current CPU | Target CPU |
| --- | --- | --- |
| 2 | 80% | 60% |

```
new_instances = ceil[2 * (80% / 60%)] = 3
```

In this scenario, Render immediately scales the service up from 2 instances to 3.

#### Example 2: Scaling down

| Current instances | Current Memory | Target Memory |
| --- | --- | --- |
| 5 | 20% | 60% |

```
new_instances = ceil[5 * (20% / 60%)] = 2
```

In this scenario, Render waits a few minutes, then scales the service down from 5 instances to 2 if memory utilization remains low.

> If you set targets for both CPU _and_ memory utilization, Render calculates `new_instances` based on each and uses the larger result.

## Billing for scaled services

Billing for a scaled service is based entirely on compute usage, which is prorated by the second. There is no additional cost for performing a scaling action.

Here are some example scenarios:

| Scenario | Billing Result |
| --- | --- |
| You run exactly two instances of your service for an entire month. | You're billed for **2x** the monthly price of your service's instance type. |
| Exactly halfway through a month, you manually scale your service from two instances down to one. It remains at one instance for the rest of the month. | You're billed for **1.5x** the monthly price of your service's instance type. |
| Every day of a month, your service autoscales from one instance to two for exactly six hours. It then autoscales back down to one instance. | You're billed for **1.25x** the monthly price of your service's instance type. |

See your exact compute usage for the month on your [Billing page](https://dashboard.render.com/billing). You can also review your [invoice history](https://dashboard.render.com/billing#invoice-history).

## Application considerations

- Services with an attached persistent disk _cannot_ scale to multiple instances.

- You can update your service's scaling configuration programmatically via the [Render API](api).

  - Separate endpoints are available for [manual scaling](https://api-docs.render.com/reference/scale-service) and [autoscaling](https://api-docs.render.com/reference/autoscale-service).

- If you configure both manual scaling _and_ autoscaling for a service, Render enables autoscaling and ignores the manual scaling configuration.

## Horizontal vs. vertical scaling

The sections above describe Render's support for *horizontal scaling*, where you adjust a service's number of running instances.

In contrast, *vertical scaling* refers to adjusting a service's compute resources (RAM and CPU). You vertically scale a service by changing its instance type in the [Render Dashboard](https://dashboard.render.com).

### When to use each

- *Scale horizontally* to handle a higher number of _simultaneous_ tasks (such as incoming requests).
- *Scale vertically* if each _single_ task requires additional RAM or CPU to run efficiently.
  - For particularly resource-intensive tasks, consider offloading to a background worker to keep your web services responsive.

*Horizontal scaling usually occurs much more frequently than vertical scaling.* Autoscaled services might change their instance count multiple times per day, whereas you might upgrade a service's instance type once in a year.

---

##### Appendix: Glossary definitions

###### web service

Deploy this *service type* to host a dynamic application at a public URL.

Ideal for full-stack web apps and API servers.

Related article: https://render.com/docs/web-services.md

###### private service

Deploy this *service type* to host a dynamic application that is not internet-reachable.

Ideal for internal apps that only your other Render services can access.

Related article: https://render.com/docs/private-services.md

###### background worker

Deploy this *service type* to continuously run code that does not receive incoming requests.

Ideal for processing jobs from a queue.

Related article: https://render.com/docs/background-workers.md

###### instance type

Specifies the RAM and CPU available to your service's *instances*.

Common instance types for a new web service include:

- *Free*: 512 MB RAM / 0.1 CPU
- *Starter*: 512 MB RAM / 0.5 CPU
- *Standard*: 2 GB RAM / 1 CPU

For the full list, see the [pricing page](/pricing#services).

###### instance

A virtual machine that runs your service's code on Render.

You can select from a range of *instance types* with different compute specs.

###### instance count

The number of individual *instances* currently running for a given service. Can be scaled manually or automatically based on resource usage.

Related article: https://render.com/docs/scaling.md

###### persistent disk

A high-performance SSD that you can attach to a service to preserve filesystem changes across deploys and restarts.

Disables [zero-downtime deploys](/deploys#zero-downtime-deploys) for the service.

Related article: https://render.com/docs/disks.md
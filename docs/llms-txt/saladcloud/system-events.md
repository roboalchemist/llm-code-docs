# Source: https://docs.salad.com/container-engine/explanation/container-groups/system-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# System Events

*Last Updated: January 17, 2025*

System Events include useful Container Group and Instance events for overall understanding and troubleshooting of your
deployment on SaladCloud. You can access System Events for your container group through the System Events tab in the
SaladCloud Portal page for your container group.

<img src="https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-system-events.png?fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=dd1746043918226f5d63416466d1c2da" alt="System Events tab in the Portal" data-og-width="1577" width="1577" data-og-height="611" height="611" data-path="container-engine/images/portal-system-events.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-system-events.png?w=280&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=a8683445ab900143f1f8e7f84f194ae9 280w, https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-system-events.png?w=560&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=19bec8dd127390ea356163674f98c76f 560w, https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-system-events.png?w=840&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=455c55975bed8108f21b982b0a5ed589 840w, https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-system-events.png?w=1100&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=4165752426578ce2c2cedcd0fa49e0ee 1100w, https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-system-events.png?w=1650&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=098b27ed337bc6e41c9d9a94a1622d63 1650w, https://mintcdn.com/salad/V4S3_t1JxH3zhOLs/container-engine/images/portal-system-events.png?w=2500&fit=max&auto=format&n=V4S3_t1JxH3zhOLs&q=85&s=a08388986f0773e4f0c2b88cee671db3 2500w" />

### Container Group System Events

* `Container Group Started`
* `Container Group Stopped`
* `Container Group Desired Replica Count Updated from XX to XX`
* `Container Group Updated (Version X)` : The container group was updated to the version indicated.

### Instance Status System Events

These events describe phases of the
[deployment lifecycle](/container-engine/explanation/container-groups/deployment-lifecycle) on SaladCloud.

* `Instance Allocated`
* `Instance Creating`
* `Instance Downloading`
* `Instance Starting`
* `Instance Running`
* `Instance Restarted`
* `Instance Recreated`
* `Instance Reallocated by User`
* `Instance Reallocated by Platform`: We automatically reallocated an instance that is not meeting internal checks for
  time-to-start or networking.
* `Instance Interrupted (Priority)`: The instances was interrupted by a higher priority workload. Consider increasing
  the [priority](/container-engine/explanation/billing-pricing/priority-pricing#priority-levels) of your workload.
* `Instance Interrupted (Node Offline)`: The node running the instance has gone offline. This is expected to occur with
  our [infrastructure](/container-engine/explanation/billing-pricing/priority-pricing#saladcloud-infrastructure).

### Instance Exit System Events

These System Events record exits and the exit code provided by your container.

* `Instance Exited:XXX (Error)`: Other exit events with the error code provided by your container.
* `Instance Exited:137 (Likely Out of System Memory)`: A 137 exit code often, but not always, indicates the container
  exceeded it's allotted memory. If this could be the case, try increasing the RAM allocated.
* `Instance Exited:0 (Exited Successfully)`

### Health Probe System Events

If you have setup [health probes](/container-engine/explanation/infrastructure-platform/health-probes) for your
container group, these System Events record state changes of those probes.

* `Instance Interrupted (Liveness Probe Failure)`
* `Instance Interrupted (Startup Probe Failure)`
* `Instance Startup Probe Passed`
* `Instance Not Ready (Readiness Probe Failure)`
* `Instance Ready (Readiness Probe Passed)`

# Source: https://docs.salad.com/container-engine/explanation/infrastructure-platform/availability.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Availability

> Learn how to access and interpret the availability of CPU and GPU resources at different priority levels on SaladCloud.

*Last Updated: November 06, 2025*

SaladCloud provides estimated availability to help you understand how many nodes are available to run your workloads at
different [priority levels](/container-engine/explanation/billing-pricing/priority-pricing#priority-levels).
Availability is shown in the SaladCloud Portal when creating container groups and via the
[Get GPU Availability](/reference/saladcloud-api/organizations/get-gpu-availability) and
[Get CPU Availability](/reference/saladcloud-api/organizations/get-cpu-availability) API endpoints.

<div style={{ textAlign: 'center' }}>
  <img src="https://mintcdn.com/salad/lmi25xqe590w-U5r/container-engine/images/availability.png?fit=max&auto=format&n=lmi25xqe590w-U5r&q=85&s=86913155f2d69a8f380b3597cfab79fd" alt="Availability shown in the Portal" data-og-width="515" width="515" data-og-height="236" height="236" data-path="container-engine/images/availability.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/lmi25xqe590w-U5r/container-engine/images/availability.png?w=280&fit=max&auto=format&n=lmi25xqe590w-U5r&q=85&s=8b5b4157f0b558ac8c1b1f0587b70216 280w, https://mintcdn.com/salad/lmi25xqe590w-U5r/container-engine/images/availability.png?w=560&fit=max&auto=format&n=lmi25xqe590w-U5r&q=85&s=915e1f6184a87da5786cfd06ba87758b 560w, https://mintcdn.com/salad/lmi25xqe590w-U5r/container-engine/images/availability.png?w=840&fit=max&auto=format&n=lmi25xqe590w-U5r&q=85&s=c12c0820ae8b1b69d47cc6e3738b4369 840w, https://mintcdn.com/salad/lmi25xqe590w-U5r/container-engine/images/availability.png?w=1100&fit=max&auto=format&n=lmi25xqe590w-U5r&q=85&s=d0c6c4967179fe49c33f10439491329c 1100w, https://mintcdn.com/salad/lmi25xqe590w-U5r/container-engine/images/availability.png?w=1650&fit=max&auto=format&n=lmi25xqe590w-U5r&q=85&s=671da40483721d47efefad0bf4fa15de 1650w, https://mintcdn.com/salad/lmi25xqe590w-U5r/container-engine/images/availability.png?w=2500&fit=max&auto=format&n=lmi25xqe590w-U5r&q=85&s=cb16f34d9e09f2afa6d9f768163afd97 2500w" />
</div>

In the portal, availability is shown under the Estimated Cost when creating a container group. The numbers indicate how
many nodes are currently online and available to run workloads at each priority level. In this example, there are 557
nodes available at the "Lowest" priority level and 1,950 nodes available at the "Low" priority level. Clicking a
priority level card will update the priority level of the container group.

Keep in mind the following considerations when interpreting availability counts:

* **Availability only includes currently online nodes.** Many more nodes are available on our network and can be
  activated as needed. If you need more capacity than is currently available, reach out to
  [SaladCloud support](mailto:support@salad.com) and we can work to grow the network based on anticipated needs.

* **Node allocation depends on multiple factors, not just priority level.** Even if few nodes are shown as available at
  your selected priority level, your workload may be able to be allocated nodes from other workloads. For example, if
  your workload has higher RAM requirements, nodes from same-priority workloads may be reallocated to meet those needs.

* **Nodes where your workload exited will still appear in availability counts.** Availability data can include nodes
  that previously ran your workload and exited with a non-zero exit code and will not be reassigned to it. Check your
  workload’s system events to confirm whether it has failed on nodes.

* **Available nodes may not be immediately reassigned.** Some nodes remain with their current workloads for a minimum
  running duration before being reallocated. This prevents excessive workload churn and repeated image pulls. The
  minimum duration varies by priority level—from about 30 minutes for low-priority workloads to indefinitely for
  high-priority workloads, which are never reallocated.

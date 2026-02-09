# Source: https://www.aptible.com/docs/how-to-guides/app-guides/horizontal-autoscaling-guide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Horizontal Autoscaling Guide

<Note>This feature is is only available on the [Production and Enterprise plans.](https://www.aptible.com/pricing)</Note>

[Horizontal Autoscaling (HAS)](/core-concepts/scaling/app-scaling#horizontal-autoscaling) is a powerful feature that allows your application to automatically adjust its computing resources based on ongoing usage. This guide will walk you through the benefits, ideal use cases, and best practices for implementing HAS in your Aptible deployments.

By leveraging HAS, you can optimize resource utilization, improve application performance, and potentially reduce costs. Whether you're running a web service, API, or any other scalable application, understanding and properly configuring HAS can significantly enhance your infrastructure's efficiency and reliability.

Let's dive into the key aspects of Horizontal Autoscaling and how you can make the most of this feature for your Aptible-hosted applications.

# Key Benefits of Horizontal Autoscaling

* Cost efficiency & Performance: Ensure your App Services are always using the optimal amount of containers. Scale loads with periods of high and low usage that can be parallelized - efficiently.
* Greater reliability: Reduce the likelihood of an expensive computation (ie. a web request) consuming all of your fixed size processing capability
* Reduced engineering time: Save time manually scaling your app services with greater automation

# What App Services are good candidates for HAS?

**First, let’s consider what sort of process is NOT a candidate:**

* Job workers, unless your jobs are idempotent and/or your queue follows exactly-once semantics
* Services that cannot be easily parallelized
  * If your workload is not easily parallelized, you could end up in a scenario where all the load is on one container and the others do near-zero work.

### So what’s a good candidate?

* Services that have predictable and well-understood load patterns
  * We talk about this more in [How to determine the right Horizontal Autoscaling configuration for your App Services](#how-to-determine-the-right-horizontal-autoscaling-configuration-for-your-app-services)
* Services that have a workload that can be easily parallelized
  * Web workers as an example, since each web request is completely independent from another
* Services that experience periods of high/low load
  * However, there’s no real risk to setting up HAS on any service just in case they ever experience higher load than expected, as long as having multiple processes running at the same time is not a problem (see above for processed that are not candidates).

# How to determine the right Horizontal Autoscaling configuration for your App Services

Horizontal Autoscaling is configured per App Service. Guidelines to keep in mind for configuration:

* Minimum number of containers - Should be set to 2 as a minimum if you want High-Availability
* Max number of containers - This one depends on how many requests you want to be able to handle under load, and will differ due to specifics of how your app behaves. If you’ve done load testing with your app and understand how many requests your app can handle with the container size you’re currently using, it is a matter of calculating how many more containers you’d want.
* Min CPU threshold - You should set this to slightly above the CPU usage your app exhibits when there’s no/minimal usage to ensure scale downs happen, any lower and your app will never scale down. If you want scale downs to happen faster, you can set this threshold higher.
* Max CPU threshold - A good rule of thumb is 80-90%. There is some lead time to scale ups occurring, as we need a minimum amount of metrics to have been gathered before the next scale-up event happens, so setting this close to 100% can lead to bottlenecks. If you want scale ups to happen faster, you can set this threshold lower.
* Scale Up, and Scale Down Steps - These are set to 1 by default, but you are able to modify the values if you want autoscaling events to jump up or down by more than 1 container at a time.

<Tip>CPU thresholds are expressed as a decimal between 0 and 1, representing the percentage of your container's allocated CPU that is actively used by your app. For instance, if a container with a 25% CPU limit is using 12% of its allocated CPU, this would be expressed as 0.48 (or 48%).</Tip>

## Percentile + Scale Up / Down Thresholds (CPU Usage)

Percentiles decide how aggressively the autoscaler reacts to spikes in CPU usage. For example:

* **P90:** Ignores the top 10% of CPU spikes. This ensures that application performance is mostly within the desired range by focusing on general performance trends.
* **P95:** Ignores the top 5% of CPU spikes. This ensures better overall performance, but will also result in more scaling activity.
* **P99:** Ignores the top 1% of CPU spikes. This results in the most scaling activity, but also the best performance.

Below is an example of what P90, P95, and P99 might look like for the same exact application Scale Up Threshold of 80%.

<img src="https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p90.png?fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=baafdacf9a556c746b0408ed5e1e44b3" alt="" data-og-width="1788" width="1788" data-og-height="1182" height="1182" data-path="images/p90.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p90.png?w=280&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=1bb69ef8a01461f51f02d9bce2500b94 280w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p90.png?w=560&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=8e9904acad3e0f30530a0726e74b9abe 560w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p90.png?w=840&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=4196a095b1314a22d7efd7575fd8d925 840w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p90.png?w=1100&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=9317fd91ee961aebdc2b9a146a0c5649 1100w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p90.png?w=1650&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=7fb0d0347c1b6556e6c764f56774bd6d 1650w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p90.png?w=2500&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=3a1e693e0ebbfb87940775a1b4573eed 2500w" />
<img src="https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p95.png?fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=6692f7615d76c6d24245cede71a79141" alt="" data-og-width="1708" width="1708" data-og-height="1144" height="1144" data-path="images/p95.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p95.png?w=280&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=b5a5338e6d4c200506e279af3035e2ad 280w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p95.png?w=560&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=c10ead40d61815af40649c25624612fe 560w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p95.png?w=840&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=7f4cf3c5c6985d6a8082ecce6929f90a 840w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p95.png?w=1100&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=44bf3fba342fb54f6fc96213c50f2483 1100w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p95.png?w=1650&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=b2f4947cc63e1fec87638d36f8c7511e 1650w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p95.png?w=2500&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=2c316ca096c9c2c1c66d341ef2b28793 2500w" />
<img src="https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p99.png?fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=47db9aa08fd91cadb0e9c1c01f097ba4" alt="" data-og-width="1690" width="1690" data-og-height="1128" height="1128" data-path="images/p99.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p99.png?w=280&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=3d8e0c480bb6b0b15c57120ec5ce70ae 280w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p99.png?w=560&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=50166d7ba51d28cbe3508fe6912e60f4 560w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p99.png?w=840&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=9d1bbee8d6a66f64e6d2f7bd9eef0a70 840w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p99.png?w=1100&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=b2052444947c7d2b9de8365b11866c35 1100w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p99.png?w=1650&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=a72ec297cdce0a44c1b7339e4d7829dc 1650w, https://mintcdn.com/aptible/8NQsSsvvmQQmCkXD/images/p99.png?w=2500&fit=max&auto=format&n=8NQsSsvvmQQmCkXD&q=85&s=b0232ae174dea918ad68d22239e75852 2500w" />

## Scale Up/Down Cooldowns

Cooldowns add deliberate pauses between scaling events to give your app time to stabilize and to prevent rapid repeated scaling events.

In the example below, we wouldn’t scale up during the Scale Up Cooldown, even though CPU usage remains consistently over the Scale Up Threshold of 80%.

<img src="https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/scale-up-cooldown.png?fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=7fac16f756155f640546d979a6633df4" alt="" data-og-width="1440" width="1440" data-og-height="1564" height="1564" data-path="images/scale-up-cooldown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/scale-up-cooldown.png?w=280&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=d12c8828ae31115855fbc83714f0eaff 280w, https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/scale-up-cooldown.png?w=560&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=ac90e98b37e4fcd6cd496a60680c7dd7 560w, https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/scale-up-cooldown.png?w=840&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=6845ee85cb6be28fe1ef994930b5c874 840w, https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/scale-up-cooldown.png?w=1100&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=ae728b5eff87e1e536047d072bf27364 1100w, https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/scale-up-cooldown.png?w=1650&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=0550770cf8b52e52fd4f196952498224 1650w, https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/scale-up-cooldown.png?w=2500&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=4b4a8da7f320e0c8150a5612a5c334b4 2500w" />

## Post Release Cooldown

After a deployment, Aptible discards metrics within this interval to allow for service stabilization.

In the example below, we would not scale up even though usage is over the 80% Scale Up Threshold for
most of the Metric Lookback Time Interval. This is because the data within the Post Release Cooldown window is not included when evaluating whether or not to autoscale.

<img src="https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/post-release-cooldown.png?fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=0c9070868ef632cac1a1f3b87c0c35e0" alt="" data-og-width="2050" width="2050" data-og-height="1596" height="1596" data-path="images/post-release-cooldown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/post-release-cooldown.png?w=280&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=dbb80743fd72b12b3b4f0db48f6feac7 280w, https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/post-release-cooldown.png?w=560&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=b6e7f34e5133fbce2c691d25f9bad534 560w, https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/post-release-cooldown.png?w=840&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=14b0ca5772e81ff29314fbf10c9c0c9c 840w, https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/post-release-cooldown.png?w=1100&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=c178a502f7379f717986588f7c255435 1100w, https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/post-release-cooldown.png?w=1650&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=29bdbe01a8a9882211a838d9f26c12b2 1650w, https://mintcdn.com/aptible/p0whILmnyYbyENhF/images/post-release-cooldown.png?w=2500&fit=max&auto=format&n=p0whILmnyYbyENhF&q=85&s=d570244060f8cfbf91b286b0d46cd98f 2500w" />

### Let’s go through an example:

We have a service that exhibits periods of load and periods of near-zero use. It is a production service that is critical to us, so we want a high-availability setup, which means our minimum containers will be 2. Metrics for this service are as follows:

| Container Size | CPU Limit | Low Load CPU Usage     | High Load CPU Usage     |
| -------------- | --------- | ---------------------- | ----------------------- |
| 1GB            | 25%       | 3% (12% of allocation) | 22% (84% of allocation) |

Since our low usage is 12%, the HAS default of 0.1 won’t work for us - we would never scale down. Let’s set it to 0.2 to be conservative

At 84% usage when under load, we’re near the limit but not quite topped out. Usually this would mean you need to validate whether this service would actually benefit from having more containers running. In this case, let’s say our monitoring tools have surfaced that request queueing gets high during these times. We could set our scale up threshold to 0.8, the default, or set it a bit lower if we want to be conservative.

With this, we can expect our service to scale up during periods of high load, up to the maximum number of containers if necessary. If we had set our max CPU limit to something like 0.9, the scaling up would be unlikely to trigger *in this particular scenario.* We may want to also consider enabling [Restart Free Scaling](/core-concepts/scaling/app-scaling#horizontal-autoscaling) to avoid the additional overhead of restarting all containers when scaling up during times of already high load.

With the metrics look-back period set to 10 minutes and our scale-up cooldown set to a minute(the default), we can expect our service to scale up by 1 container every 5 minutes as long as our load across all containers stays above 80%, until we reach the maximum containers we set in the configuration. Note the 5 minutes between each event - that is currently a hardcoded minimum cooldown.

Since we set a min CPU (scale down) threshold high enough to be above our containers minimal usage, we have guaranteed scale downs will occur. We could set our scale-down threshold higher if we want to be more aggressive about maximizing container utility.

### Autoscaling Worker/Job processes

You can use horizontal autoscaling to scale your worker/job processes. However, you should consider some additional configurations:

* **Restart Free Scaling**: When enabled, scale operations for modifying the number of running containers will not restart the other containers in the service. This is particularly useful for worker/job processes, as it allows you to scale up without interrupting work on the containers already processing jobs.
* **Service Stop Timeout**: When scaling down, the service stop timeout is respected. This is particularly useful for worker/job processes, since it allows time to either finish processing the current job, or put the job back on the queue for processing by another container. Note that containers are selected for removal based on the [`APTIBLE_PROCESS_INDEX` metadata variable](/reference/aptible-metadata-variables), selecting higher indices first, so if possible you should prefer to process long running jobs on containers with a lower index.

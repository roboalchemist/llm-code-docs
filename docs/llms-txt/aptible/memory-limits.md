# Source: https://www.aptible.com/docs/core-concepts/scaling/memory-limits.md

# Memory Management

> Learn how Aptible enforces memory limits to ensure predictable performance

# Overview

Memory limits are enforced through a feature called Memory Management.

When memory management is enabled on your infrastructure and a Container exceeds its memory allocation, the following happens:

1. Aptible sends a log message to your [Log Drains](/core-concepts/observability/logs/log-drains/overview) (this includes [`aptible logs`](/reference/aptible-cli/cli-commands/cli-logs)) indicating that your Container exceeded its memory allocation, and dumps a list of the processes running in your Container for troubleshooting purposes.
2. If there is free memory on the instance, Aptible increases your Container's memory allowance by 10%. This gives your Container a better shot at exiting cleanly.
3. Aptible delivers a `SIGTERM` signal to all the processes in your Container, and gives your Container 10 seconds to exit. If your Container does not exit within 10 seconds, Aptible delivers a `SIGKILL` signal, effectively terminating all the processes in your Container immediately.
4. Aptible triggers [Container Recovery](/core-concepts/architecture/containers/container-recovery) to restart your Container.

The [Metrics](/core-concepts/observability/metrics/overview) you see in the Dashboard are captured every minute. If your Container exceeds its RAM allocation very quickly and then is restarted, **the metrics you see in the Dashboard may not reflect the usage spike**.
As such, it's a good idea to refer to your logs as the authoritative source of information to know when you're exceeding your memory allocation.
Indeed, whenever your Containers are restarted, Aptible will log this message to all your [Log Drains](/core-concepts/observability/logs/log-drains/overview):

```
container exceeded its memory allocation
```

This message will also be followed by a snapshot of the memory usage of all the processes running in your Container, so you can identify memory hogs more easily.

Here is an example. The column that shows RAM usage is `RSS`, and that usage is expressed in kilobytes.

```
           PID    PPID      VSZ      RSS  STAT    COMMAND
          2688    2625      820       36  S       /usr/lib/erlang/erts-7.3.1/bin/epmd -daemon
          2625     914     1540      936  S       /bin/sh -e /srv/rabbitmq_server-3.5.8/sbin/rabbitmq-server
         13255     914     6248      792  S       /bin/bash
          2792    2708      764       12  S       inet_gethost 4
          2793    2792      764       44  S       inet_gethost 4
          2708    2625  1343560  1044596  S       /usr/lib/erlang/erts-7.3.1/bin/beam.smp [...]
```

## Understanding Memory Utilization

There are two main categories of memory on Linux: RSS and caches.

In Metrics on Aptible, RSS is published as an individual metric, and the sum of RSS + caches (i.e. total memory usage) is published as a separate metric.

It's important to understand the difference between RSS and Caches when optimizing against memory limits.

At a high level, RSS is memory that is allocated and used by your App or Database, and caches represent memory that is used by the operating system (Linux) to make your App or Database faster. In particular, caches are used to accelerate disk access.

If your container approaches its memory limit, the host system will attempt to reclaim some memory from your Container or terminate it if that's not possible. Memory used for caches can usually be reclaimed, whereas anonymous memory and memory-mapped files (RSS) usually cannot.

When monitoring memory usage, you should make sure RSS never approaches the memory limit. Crossing the limit would result in your Containers being restarted. For Databases, you should also usually ensure a decent amount of memory is available to be used for caches by the operating system.

In practice, you should normally ensure RSS does not exceed about \~70% of the memory limit. That said, this advice is very Database dependent: for [PostgreSQL](/core-concepts/managed-databases/supported-databases/postgresql), 30% is a better target, and for [Elasticsearch](/core-concepts/managed-databases/supported-databases/elasticsearch), 50% is a good target.

However, Linux allocates caches very liberally, so don't be surprised if your Container is using a lot of memory for caches. In fact, for a Database, cache usage will often cause your total memory usage to equal 100% of your memory limit: that's expected.

# Memory Limits FAQ

**What should my app do when it receives a `SIGTERM` from Aptible?**

Your app should try and exit gracefully within 10 seconds.

If your app is processing background work, you should ideally try and push it back to whatever queue it came from.

**How do I know the memory usage for a Container?**

See [Metrics](/core-concepts/observability/metrics/overview).

**How do I know the memory limit for a Container?**

You can view the current memory limit for any Container by looking at the Container's [Metrics](/core-concepts/observability/metrics/overview) in your Dashboard: the memory limit is listed right next to your current usage.

Additionally, Aptible sets the `APTIBLE_CONTAINER_SIZE` environment variable when starting your Containers. This indicates your Container's memory limit, in MB.

**How do I increase the memory limit for a Container?**

See [Scaling](/core-concepts/scaling/overview).

# Source: https://www.aptible.com/docs/core-concepts/scaling/app-scaling.md

# App Scaling

> Learn about scaling Apps CPU, RAM, and containers - manually or automatically

# Overview

Aptible Apps are scaled at the [Service](/core-concepts/apps/deploying-apps/services) level, meaning each App Service is scaled independently.

App Services can be scaled by adding more CPU/RAM (vertical scaling) or by adding more containers (horizontal). App Services can be scaled manually via the CLI or UI, automatically with the Autoscaling, or programmatically with Terraform.

Apps with more than two containers are deployed in a high-availability configuration, ensuring redundancy across different zones.

When Apps are scaled, a new set of [containers](/core-concepts/architecture/containers/overview) will be launched to replace the existing ones for each of your App's [Services](/core-concepts/apps/deploying-apps/services).

# High-availability Apps

Apps scaled to 2 or more Containers are automatically deployed in a high-availability configuration, with Containers deployed in separate [AWS Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html).

# Horizontal Scaling

Scale Apps horizontally by adding more [Containers](/core-concepts/architecture/containers/overview) to a given Service. Each App Service can scale up to 32 Containers via the Aptible Dashboard. Scaling above 32 containers for a service (with a maximum of 128 containers) is supported via the [Aptible CLI](https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-apps-scale#aptible-apps-scale) and the [Aptible Terraform Provider.](https://registry.terraform.io/providers/aptible/aptible/latest)

### Manual Horizontial Scaling

App Services can be manually scaled via the Dashboard or [`aptible apps:scale`](https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-apps-scale) CLI command. Example:

```
  aptible apps:scale SERVICE [--container-count COUNT] 
```

### Horizontal Autoscaling

<Frame>
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/horizontal-autoscale.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7d0dd277f0695a14c1f7cda7452d3124" alt="Horizontal Autoscaling" data-og-width="5120" width="5120" data-og-height="2560" height="2560" data-path="images/horizontal-autoscale.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/horizontal-autoscale.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=23a85ee7860db5903505d047e228872b 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/horizontal-autoscale.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=cdfb1a01d2f7317b983e822bb88a0ba2 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/horizontal-autoscale.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=452d314273d2d234067dec3de5e5d73b 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/horizontal-autoscale.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=b09d2ff3137e3bb96a1afcaa414f816b 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/horizontal-autoscale.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=697b14862d7ecccf47e50e86dc08375d 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/horizontal-autoscale.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=9a04498ee957a67ca654d83eed996e8b 2500w" />
</Frame>

<Info>
  Horizontal Autoscaling is only available on the [Production and Enterprise plans.](https://www.aptible.com/pricing)
</Info>

When Horizontal Autoscaling is enabled on a Service, the autoscaler evaluates Services every 5 minutes and generates scaling adjusted based on CPU usage (as percentage of total cores). Data is analyzed over a 30-minute period. Autoscaling will not create a scaling operation when your service or app is already being scaled, configured, or deployed.  Post-scaling cooldowns are 5 minutes for scaling down and 1 minute for scaling up. After any release, an additional 5-minute cooldown applies. Metrics are evaluated at the 99th percentile aggregated across all of the service containers over the past 30 minutes.

This feature can also be configured via [Terraform](/reference/terraform) or the [`aptible services:autoscaling_policy:set`](/reference/aptible-cli/cli-commands/cli-services-autoscalingpolicy-set) CLI command.

By default, a [Horizontal Autoscaling Operation](https://www.aptible.com/docs/core-concepts/scaling/app-scaling#horizontal-autoscaling) follows the regular [Container Lifecycle](https://www.aptible.com/docs/core-concepts/architecture/containers/overview#container-lifecycle) and [Releases](https://www.aptible.com/docs/core-concepts/apps/deploying-apps/releases/overview#releases) pattern of restarting all current containers when modifying the number of running containers. However, this behavior can be disabled by enabling the **Restart Free Scaling** (`use_horizontal_scale` in Terraform) setting when configuring autoscaling for the service. With restart free scaling enabled, containers are added and removed without restarting the existing ones. When removing containers in this configuration, the service's stop timeout is still respected. Note that if the service has a [TCP](/core-concepts/apps/connecting-to-apps/app-endpoints/tcp-endpoints), ELB, or [GRPC](/core-concepts/apps/connecting-to-apps/app-endpoints/grpc-endpoints) endpoint, the regular full restart will still occur even with restart free scaling enabled. Additionally, if any endpoint associated with the service failed its most recent `provision` operation (which is an operation that is called on create of a new endpoint, or update of an existing endpoint), the regular full restart will still occur even with restart free scaling enabled.

<Card title="Guide for Configuring Horizontial Autoscaling" icon="book-open-reader" iconType="duotone" href="https://www.aptible.com/docs/how-to-guides/app-guides/horizontal-autoscaling-guide" />

#### Configuration Options

<AccordionGroup>
  <Accordion title="Container & CPU Threshold Settings" icon="gear">
    The following container & CPU threshold settings are available for configuration:

    <Info>
      CPU thresholds are expressed as a number between 0 and 1, reflecting the actual percentage usage of your container's CPU limit. For instance, 2% usage with a 12.5% limit equals 16%, or 0.16.
    </Info>

    * **Percentile**: Determines the percentile for evaluating RAM and CPU usage.
    * **Minimum Container Count**: Sets the lowest container count to which the service can be scaled down by Autoscaler.
    * **Maximum Container Count**: Sets the highest container count to which the service can be scaled up to by Autoscaler.
    * **Scale Up Steps**: Sets the amount of containers to add when autoscaling (ex: a value of 2 will go from 1->3->5). Container count will never exceed the configured maximum.
    * **Scale Down Steps**: Sets the amount of containers to remove when autoscaling (ex: a value of 2 will go from 4->2->1). Container count will never exceed the configured minimum.
    * **Scale Down Threshold (CPU Usage)**: Specifies the percentage of the current CPU usage at which an up-scaling action is triggered.
    * **Scale Up Threshold (CPU Usage)**: Specifies the percentage of the current CPU usage at which a down-scaling action is triggered.
  </Accordion>

  <Accordion title="Time-Based Settings" icon="gear">
    The following time-based settings are available for configuration:

    * **Metrics Lookback Time Interval**: The duration in seconds for retrieving past performance metrics.
    * **Post Scale Up Cooldown**: The waiting period in seconds after an automated scale-up before another scaling action can be considered. The period of time the service is on cooldown is still considered in the metrics for the next potential scale.
    * **Post Scale Down Cooldown**: The waiting period in seconds after an automated scale-down before another scaling action can be considered. The period of time the service is on cooldown is still considered in the metrics for the next potential scale.
    * **Post Release Cooldown**: The time in seconds to ignore following any general scaling operation, allowing stabilization before considering additional scaling changes. For this metric, the cooldown period is *not* considered in the metrics for the next potential scale.
  </Accordion>

  <Accordion title="General Settings" icon="gear">
    The following general settings are available for configuration:

    * **Restart Free Scaling**: When enabled, scale operations for modifying the number of running containers will not restart the other containers in the service.
  </Accordion>
</AccordionGroup>

# Vertical Scaling

Scale Apps vertically by changing the size of Containers, i.e., changing their [Memory Limits](/core-concepts/scaling/memory-limits) and [CPU Limits](/core-concepts/scaling/container-profiles). The available sizes are determined by the [Container Profile.](/core-concepts/scaling/container-profiles)

### Manual Vertical Scaling

App Services can be manually scaled via the Dashboard or [`aptible apps:scale`](https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-apps-scale) CLI command. Example:

```
    aptible apps:scale SERVICE [--container-size SIZE_MB]
```

### Vertical Autoscaling

<Frame>
    <img src="https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/vertical-autoscale.png?fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=05218ac6eaa3b1154deae569f874a2be" alt="Vertical Autoscaling" data-og-width="5120" width="5120" data-og-height="2560" height="2560" data-path="images/vertical-autoscale.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/vertical-autoscale.png?w=280&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=b5580e88e08ef112118ecaeb4a69a897 280w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/vertical-autoscale.png?w=560&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=67effeed2362a455284b66f4bc7b8f2b 560w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/vertical-autoscale.png?w=840&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=386561e3ec8358a25d3da9e5d6e24f35 840w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/vertical-autoscale.png?w=1100&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=d6f0c04391e05722c7f4aa91cc3569e1 1100w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/vertical-autoscale.png?w=1650&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=d3d1af8291d4fb760a93495000f80489 1650w, https://mintcdn.com/aptible/uXP5kmz3uSl-opiv/images/vertical-autoscale.png?w=2500&fit=max&auto=format&n=uXP5kmz3uSl-opiv&q=85&s=7f9bdfb8c00c5a92038ce580c297b615 2500w" />
</Frame>

<Info>
  Vertical Autoscaling is only available on the [Enterprise plan.](https://www.aptible.com/pricing)
</Info>

When Vertical Autoscaling is enabled on a Service, the autoscaler also evaluates services every 5 minutes and generates scaling recommendations based:

* RSS usage in GB divided by the CPU
* RSS usage levels

Data is analyzed over a 30-minute lookback period. Autoscaling will not create a scaling operation when your service or app is already being scaled, configured, or deployed. Post-scaling cooldowns are 5 minutes for scaling down and 1 minute for scaling up. An additional 5-minute cooldown applies after a service release. Metrics are evaluated at the 99th percentile aggregated across all of the service containers over the past 30 minutes.

This feature can also be configured via [Terraform](/reference/terraform) or the [`aptible services:autoscaling_policy:set`](/reference/aptible-cli/cli-commands/cli-services-autoscalingpolicy-set) CLI command.

#### Configuration Options

<AccordionGroup>
  <Accordion title="RAM & CPU Threshold Settings" icon="gear">
    The following RAM & CPU Threshold settings are available for configuration:

    * **Percentile**: Sets the percentile of current RAM and CPU usage to use when evaluating autoscaling actions.
    * **Minimum Memory (MB)**: Sets the lowest container size the service can be scaled down to.
    * **Maximum Memory (MB)**: Sets the highest container size the service can be scaled up to. If blank, the container can scale to the largest size available.
    * **Memory Scale Up Percentage**: Specifies a threshold based on a percentage of the current memory limit at which the service's memory usage triggers a scale up.
    * **Memory Scale Down Percentage**: Specifies a threshold based on the percentage of the next smallest container size's memory limit at which the service's memory usage triggers a scale down.
    * **Memory Optimized Memory/CPU Ratio Threshold**: Establishes the ratio of Memory (in GB) to CPU (in CPUs) at which values exceeding the threshold prompt a shift to an R (Memory Optimized) profile.
    * **Compute Optimized Memory/CPU Ratio Threshold**: Sets the Memory-to-CPU ratio threshold, below which the service is transitioned to a C (Compute Optimized) profile.
  </Accordion>

  <Accordion title="Time-Based Settings" icon="gear">
    The following time-based settings are available for configuration:

    * **Metrics Lookback Time Interval**: The duration in seconds for retrieving past performance metrics.
    * **Post Scale Up Cooldown**: The waiting period in seconds after an automated scale-up before another scaling action can be considered. The period of time the service is on cooldown is still considered in the metrics for the next potential scale.
    * **Post Scale Down Cooldown**: The waiting period in seconds after an automated scale-down before another scaling action can be considered. The period of time the service is on cooldown is still considered in the metrics for the next potential scale.
    * **Post Release Cooldown**: The time in seconds to ignore following any general scaling operation, allowing stabilization before considering additional scaling changes. For this metric, the cooldown period is *not* considered in the metrics for the next potential scale.
  </Accordion>
</AccordionGroup>

***

# FAQ

<AccordionGroup>
  <Accordion title="How do I scale my apps and services?">
    See our guide here for [How to scale apps and services](https://www.aptible.com/docs/how-to-guides/app-guides/how-to-scale-apps-services)
  </Accordion>
</AccordionGroup>

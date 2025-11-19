# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-services-autoscalingpolicy-set.md

# aptible services:autoscaling_policy:set

Sets the sizing (autoscaling) policy for a service. This is not incremental, all arguments must be sent at once or they will be set to defaults. Also aliased to `services:sizing_policy:set`.

For more information, see the [Autoscaling documentation](/core-concepts/scaling/app-scaling)

# Synopsis

```
Usage:
  aptible services:autoscaling_policy:set SERVICE --autoscaling-type (horizontal|vertical) [--metric-lookback-seconds SECONDS] [--percentile PERCENTILE] [--post-scale-up-cooldown-seconds SECONDS] [--post-scale-down-cooldown-seconds SECONDS] [--post-release-cooldown-seconds SECONDS] [--mem-cpu-ratio-r-threshold RATIO] [--mem-cpu-ratio-c-threshold RATIO] [--mem-scale-up-threshold THRESHOLD] [--mem-scale-down-threshold THRESHOLD] [--minimum-memory MEMORY] [--maximum-memory MEMORY] [--min-cpu-threshold THRESHOLD] [--max-cpu-threshold THRESHOLD] [--min-containers CONTAINERS] [--max-containers CONTAINERS] [--scale-up-step STEPS] [--scale-down-step STEPS]

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
      [--autoscaling-type=AUTOSCALING_TYPE]                # The type of autoscaling. Must be either "horizontal" or "vertical"
      [--metric-lookback-seconds=N]                        # (Default: 1800) The duration in seconds for retrieving past performance metrics.
      [--percentile=N]                                     # (Default: 99) The percentile for evaluating metrics.
      [--post-scale-up-cooldown-seconds=N]                 # (Default: 60) The waiting period in seconds after an automated scale-up before another scaling action can be considered.
      [--post-scale-down-cooldown-seconds=N]               # (Default: 300) The waiting period in seconds after an automated scale-down before another scaling action can be considered.
      [--post-release-cooldown-seconds=N]                  # (Default: 60) The time in seconds to ignore in metrics following a deploy to allow for service stabilization.
      [--mem-cpu-ratio-r-threshold=N]                      # (Default: 4.0) Establishes the ratio of Memory (in GB) to CPU (in CPUs) at which values exceeding the threshold prompt a shift to an R (Memory Optimized) profile.
      [--mem-cpu-ratio-c-threshold=N]                      # (Default: 2.0) Sets the Memory-to-CPU ratio threshold, below which the service is transitioned to a C (Compute Optimized) profile.
      [--mem-scale-up-threshold=N]                         # (Default: 0.9) Vertical autoscaling only - Specifies a threshold based on a percentage of the current memory limit at which the service's memory usage triggers a scale up.
      [--mem-scale-down-threshold=N]                       # (Default: 0.75) Vertical autoscaling only - Specifies a threshold based on the percentage of the next smallest container size's memory limit at which the service's memory usage triggers a scale down.
      [--minimum-memory=N]                                 # (Default: 2048) Vertical autoscaling only - Sets the lowest memory limit to which the service can be scaled down by Autoscaler.
      [--maximum-memory=N]                                 # Vertical autoscaling only - Defines the upper memory threshold, capping the maximum memory allocation possible through Autoscaler. If blank, the container can scale to the largest size available.
      [--min-cpu-threshold=N]                              # Horizontal autoscaling only - Specifies the percentage of the current CPU usage at which a down-scaling action is triggered.
      [--max-cpu-threshold=N]                              # Horizontal autoscaling only - Specifies the percentage of the current CPU usage at which an up-scaling action is triggered.
      [--min-containers=N]                                 # Horizontal autoscaling only - Sets the lowest container count to which the service can be scaled down.
      [--max-containers=N]                                 # Horizontal autoscaling only - Sets the highest container count to which the service can be scaled up to.
      [--restart-free-scale|--no-restart-free-scale]       # Horizontal autoscaling only - Sets the autoscaling to use a restart-free scaling strategy.
      [--scale-up-step=N]                                  # (Default: 1) Horizontal autoscaling only - Sets the amount of containers to add when autoscaling (ex: a value of 2 will go from 1->3->5). Container count will never exceed the configured maximum.
      [--scale-down-step=N]                                # (Default: 1) Horizontal autoscaling only - Sets the amount of containers to remove when autoscaling (ex: a value of 2 will go from 4->2->1). Container count will never exceed the configured minimum.
```

# Source: https://docs.mystic.ai/docs/scaling-configuration.md

# Scaling configuration

Control the scaling parameters of your Pipeline to best suit your products needs - scale to 0 or 1k GPUs without writing code or touching a cloud provider.

> 📘 This is premium feature, register and read more here: <https://www.mystic.ai/bring-your-own-cloud>

# Overview

Scaling Configurations allow you to define how your Pipeline should scale up or down in the cloud. As your traffic will vary, it's important to use an appropriate configuration to make sure you have a good cost/performance trade off according to your products need. Scaling Configurations also allow you to set minimum and maximum bounds for scaling to make sure a model can always be ready and does not scale up too high.

**Key features:**

* **Scale to 0** - If you want a pipeline to scale down completely with no traffic to minimise costs
* **Minimum & Maximum** cache control - Upper and lower bounds for pipeline caching
* **Scale up/down speeds** - This allows you to scale up or down based on traffic within a time period you set

Scaling configurations are accessible via generic CRUD endpoints in all products offered by Mystic, including the enterprise PipelineCore, as well as controllable via the python SDK and command line interface.

<br>

# General definition

Scaling configurations all have the following fields:

* `type` string Enum, values (read more about types below in [Scaling types](#scaling-types)):
  * `windows` - Apply a weighted average to user defined windows to calculate the target number of nodes
* `args` dictionary, specific to what `type` is defined

When running live the scaling configuration settings are used to calculate a target scaling metric, this will then be used internally to set the number of **replicas** (live copies of the pipeline).

# Concurrency

Most approaches to scaling use the concept of concurrency to calculate the ideal number of nodes for a pipeline. The concurrency is defined as:

`concurrency = frequency of requests * duration of requests`

As this is a decimal based number, we convert it to the ideal number of machines by always rounding up (ceiling) the number:

`num_nodes (replicas) = ceil( concurrency )`

By calculating this we know the number of nodes that should be present given a calculated concurrency.

# Scaling types

There are multiple scaling algorithms provided by Mystic on all of our cluster types - currently the only configurable public one is `windows`. Scaling algorithms allow you to select different approaches to responding to inbound traffic over time in a way that's most appropriate for your product or cost/performance needs.

Scaling types coming to the public soon:

* `pid` - Proportional, Integral and Differential control. This allows more controlled responsiveness to drastic changes in traffic
* `exponential_decay` - This algorithm reduces noise with in noisy traffic
* `historic_lookback` - This looks back at the traffic in a given time period, such as a day, week, or other arbitrary time offset.

## `windows`

The `windows` scaling type takes in an array of times weight a weight value to calculate a weighted average for scaling. For example the following args look back and calculate their concurrency  1, 5, and 30 minutes:

```json json
[
  {
  "lookback_time": 60,
  "weight": 0.6
	},
  {
  "lookback_time": 300,
  "weight": 0.3
	},
  {
  "lookback_time": 1800,
  "weight": 0.1
	},
]
```

Fields:

* `lookback_time` - Time to view run traffic
* `weight` - the weight to apply to the value for the time period

*Note: Weights must sum to 1.*

# Default scaling example

When you upload a pipeline to Mystic there's a default scaling configuration that's assigned to it, it has the following definition:

```json
{
  "windows": [
    {
      "weight": 0.5,
      "lookback_time": 60
    },
    {
      "weight": 0.5,
      "lookback_time": 600
    }
  ]
}
```

Here we have two windows to look back: 1 minute, and 10 minutes. They both have a weight of 0.5. This scaling means that traffic within the last 1 minute will be equally weighted as the traffic with the last 10 minutes.

Let's walkthrough an example situation to calculate the number of GPUs that will be running based on this scaling configuration. For this example lets say we are running an image generation model that takes 2.5s to complete per request.

**Situation:** 2000 total requests with the past 10 minutes and 100 in the past minute. Concurrency will be:

```
1 minute (60s) frequency = 100 / 60 = 1.667
10 minute (600s) frequency = 2000 / 600 = 3.333

1 minute (60s) concurrency = 1.667 * 2.5 = 4.1675
10 minute ( 600s) concurrency = 8.3325

Concurrency = 0.5 * 4.1675 + 0.5 * 8.3325 = 6.25
Number of replicas (live pipeline number)  = ceil( 6.25 ) = 7
```

In this situation we can see that the longer term traffic (10mins) is higher than the short term (1min) traffic which means we'll keep up more replicas of the pipeline. You can change these weights as you please to fit your responsiveness requirements.

# Create and link scaling configurations

To create a scaling configuration that keeps a pipeline alive based on traffic in the past 5 minutes via the CLI you can simply run:

```shell
pipeline create scalings username/my_new_scaling_config --type windows --args '{"windows": [{"lookback_time": 300,"weight": 1}]}' --min-nodes 0 --max-nodes 10
```

This can then be attached to a pipeline by running:

```shell
pipeline edit pl pipeline_123456789 -s username/my_new_scaling_config
```

<br>
# Source: https://docs.statsig.com/statsig-warehouse-native/features/autotune.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Autotune (Beta)

Autotune Experiments in Warehouse Native have a very similar setup to cloud [Autotunes](/autotune/overview). In Warehouse Native, Autotune success events will be pulled from a Metric Source, and computation of results will happen in your warehouse.

<Info>
  Continuous Autotune in WHN is currently in beta, please contact the team to
  get it enabled in your account
</Info>

# Creating an Autotune

To set up an Autotune on Warehouse Native, start by defining your objective. This can either be an *event* or a *value* from a Metric Source. For detailed instructions, see [how to set up a Metric Source](/statsig-warehouse-native/configuration/metric-sources).

You can also specify the optimization direction (Maximize or Minimize) to determine how Autotune evaluates variant performance.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/5MDCxJRZjsFHpl_V/images/statsig-warehouse-native/features/autotune/autotune-config.png?fit=max&auto=format&n=5MDCxJRZjsFHpl_V&q=85&s=e4389511269169ce0c9eaea8b8c1869b" alt="Autotune configuration interface" width="399" height="262" data-path="images/statsig-warehouse-native/features/autotune/autotune-config.png" />
</Frame>

1. Navigate to the [Experiments section](https://console.statsig.com/experiments) in the sidebar of the Statsig Console.
2. Click on the [Autotune tab](https://console.statsig.com/autotune) at the top.
3. Click the Create button and enter the name and description of the Autotune Experiment that you want to create.
4. Select an ID Type for your Experiment.
5. Create and name your variants for your Autotune Experiment. The variant that's listed as Control/Default will be returned when the Autotune Experiment is not running.
6. Select your Metric Source that you defined earlier as shown below.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/5MDCxJRZjsFHpl_V/images/statsig-warehouse-native/features/autotune/autotune-metric-source.png?fit=max&auto=format&n=5MDCxJRZjsFHpl_V&q=85&s=d08562ca4003d348d51e15b2794653e1" alt="Autotune metric source configuration interface" width="1605" height="345" data-path="images/statsig-warehouse-native/features/autotune/autotune-metric-source.png" />
</Frame>

There are a few parameters you can specify:

* Exploration Window - The initial time period where Autotune will equally split the traffic. This is useful for noisy or temporal metrics where hourly swings in data can bias Autotune's initial measurements.
* Attribution Window - The maximum duration between the exposure and success event that counts as a success. We recommend 1 hr for most applications, but adjust accordingly if you expect the success event to lag the exposure event by several hours.
* Winner Threshold - The "probability of best" threshold a variant needs to achieve for Autotune to declare it the winner, stop collecting data, and direct all traffic. Setting a lower number will result in faster decisions but increases the probability of making suboptimal decisions (picking the wrong winner).

Click "Create" to finalize the setup.

7. Your Autotune is set up and ready to go. Click "Start" when you're ready to launch your Autotune test.


Built with [Mintlify](https://mintlify.com).
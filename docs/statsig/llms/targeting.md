# Source: https://docs.statsig.com/statsig-warehouse-native/features/targeting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Targeting

## How to Target Experiments

Experiments integrate natively with Statsig's Feature Gates product in order to target interventions. Feature gates provide a rich language for targeting users by properties or segments, and experiments can be given a targeting gate in order to only test an intervention on units which pass that gate. Read more about [Feature Gates](/feature-flags/overview).

## When to Target an Experiment

Targeting an experiment makes sense when

* You want to gradually release the experiment to tiers of users
* Part of your hypothesis is that the experiment intervention will only work for a target subset of users, e.g. mobile users


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.statsig.com/statsig-warehouse-native/connecting-your-warehouse/scheduled-reloads.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduled Reloads

## Overview

You can control daily reload settings for Metrics and Experiments. While these can be configured on each entity, you can also set defaults that entities can inherit from in your Project Settings. You also have the option of using the Console API to [trigger experiment result loads](/console-api/experiments#post-/experiments/-experiment_id-/load_pulse) (experiment results). This is often used for triggering refreshes when your data pipelines are ready.

<Frame>
  <img width="1443" alt="Project-level scheduled reload settings interface" src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/connecting-your-warehouse/scheduled-reloads/d056be8d-19a0-43ae-91e1-cf5e16d23b53.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=c0bfa0c19da5a671f3a3c574222ee4d7" data-path="images/statsig-warehouse-native/connecting-your-warehouse/scheduled-reloads/d056be8d-19a0-43ae-91e1-cf5e16d23b53.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/connecting-your-warehouse/scheduled-reloads/efc232e7-4189-4ee7-b35a-5b1530041c70.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=67f97fe29f2d3c48b870deaaa840d726" alt="Individual experiment pulse scheduling interface" width="1677" height="865" data-path="images/statsig-warehouse-native/connecting-your-warehouse/scheduled-reloads/efc232e7-4189-4ee7-b35a-5b1530041c70.png" />
</Frame>

## Gate/Experiment Pulse Scheduling

For feature gates and experiments, individual Pulse scheduling is available separately from the project-level settings. You can schedule daily Pulse metric reloads for individual feature gates and experiments.

To access this feature:

1. Navigate to your feature gate/experiment in the Statsig Console
2. Go to the Pulse Results tab
3. Use the scheduling controls to configure daily reloads

The scheduling allows you to:

* Set a daily reload time in UTC
* Choose between Full and Incremental reload types
* Save, edit, or cancel scheduled reloads

This feature requires gates with partial rollout rules and overrides any project-level settings.


Built with [Mintlify](https://mintlify.com).
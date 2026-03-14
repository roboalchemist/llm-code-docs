# Source: https://docs.statsig.com/statsig-warehouse-native/features/turbo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Turbo Mode

> Use turbo mode to reduce cost

By default, Statsig and other warehouse native platforms calculate cumulative results for every day in an experiment. This lets users take a historical analysis and get a rich historical view, or make changes and see how those changes "would have" impacted an analysis on previous days.

This is a heavily optimized flow, but at the end of the day does take additional compute to achieve. Many customers want to run large experiments with minimal compute cost, so Turbo Mode was built to give control of the tradeoff between compute and historical tracking.

## How to use Turbo

When loading pulse, there is a checkbox to enable Turbo mode. Subsequent scheduled loads use the last setting. Note that using Turbo Mode changes the shape of the underlying data, so switching back to standard analysis requires a full reload with Turbo Mode disabled.

There is also a project-level setting for Turbo Mode being on or off by default in a project's experimentation settings.

## What Turbo Mode Removes

Turbo removes two functionalities from Statsig. The first is the ability to click into the date picker and see pulse results "as of" various historical dates. The second - and associated - is the cumulative timeseries.

These will both exist if an experiment is loaded daily using incremental reloads, but they may miss dates if there are gaps in the loading schedule, and they will not retroactively update when a full reload is run.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/y4LPJ9r3dQ39KuxK/images/whn/cumulative_timeseries.png?fit=max&auto=format&n=y4LPJ9r3dQ39KuxK&q=85&s=07cd959010a30b4ac93c79d82b5e5a07" alt="Cumulative Timeseries" width="1260" height="902" data-path="images/whn/cumulative_timeseries.png" />
</Frame>

## What Turbo Mode Keeps

Turbo mode and standard loads both calculate identical pulse results (including CUPED and other advanced techniques) for the latest day of the experiment analysis, and Turbo mode still calculates the "daily" and "days since exposure" timeseries for diagnosis, as well as pre-experiment bias checks.

## What to expect

This will vary depending on an experiment's settings, but generally there is a 40-80% reduction in load time and compute cost for turbo jobs on large, long-running experiments. This is likely biased and is best used as a ballpark estimate, since this observation comes from cases where standard loads were slower than desired and Turbo Mode was applied in response; there is not a good counterfactual for companies who default to turbo being on.

## When to Use Turbo

Turbo Mode is more effective for long-running experiments using full reloads, since the job would have to recreate the entire history of "user state" on each day. Since Turbo Mode only calculates statistics for the latest snapshot, it can skip many calculations.

Turbo Mode is also more effective for experiments with an unusually large number of users or metrics compared to other experiments in a project, since it prevents the warehouse from spilling to disk by reducing memory requirements; spill dramatically slows down jobs and adds expense because of that.

Of note, holdouts benefit from Turbo Mode since they typically have a large battery of metrics, expose a large portion of a project's end users, and are commonly run for 3-6 months.

Turbo Mode will be less effective for experiments that have scheduled/incremental reloads, or for smaller experiments.


Built with [Mintlify](https://mintlify.com).
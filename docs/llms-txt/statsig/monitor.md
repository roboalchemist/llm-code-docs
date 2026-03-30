# Source: https://docs.statsig.com/experiments/monitor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitor an Experiment

> Track health checks, exposures, and diagnostics for active experiments in Statsig Cloud.

Once an experiment launches you can monitor its health and exposure mix directly from the Statsig console.

## Experiment Health Checks

1. Open **Experiments** from the navigation.
2. Select the experiment you want to inspect.
3. Review the **Experiment Health Checks** banner at the top of the scorecard.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/experiments/monitor/health-checks.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=b9430a5aae23a7b7c12b630f4d446c97" alt="Experiment health checks showing status icons" width="1414" height="397" data-path="images/experiments/monitor/health-checks.png" />
</Frame>

Hover a status icon to read the summary, then click for full context. Common checks include:

* **Checks started** - Verifies the SDK is reporting config checks shortly after launch.
* **Checks have valid unit type** - Confirms checks include the configured unit identifier (userID by default).
* **Event metrics have data** - Ensures events carry the same unit ID as exposures so Pulse can compute metrics. This often surfaces when downstream tooling (e.g., Segment) omits stableID or custom IDs.
* **Pulse metrics available** - Indicates Pulse results have landed (typically the day after launch).
* **Exposures are balanced** - Runs a chi-squared test for sample ratio mismatch (SRM). Occasional warnings happen due to randomness, but persistent red alerts point to assignment or logging issues.
  * p-value between 0.001 and 0.01 -> Warning (yellow).
  * p-value \< 0.01 with \<0.1% absolute deviation -> Warning (yellow) with low expected impact.
  * p-value \< 0.001 and >=0.1% deviation -> Alert (red) requiring investigation.
* **Crossover units detected** - Flags users exposed to multiple variants. Statsig Cloud keeps these users in both groups (since the SDK rarely produces crossovers) but highlights them so you can address root causes. Reach out if you see rates above 1%.
* **Default value type mismatch** - Warns if an experiment's fallback default value type disagrees with the parameter definition.
* **Group assignment healthy** - Surfaces unexpected assignment reasons (e.g., `Uninitialized`, `InvalidBootstrap`). Click **View Assignment Reasons** to see the hourly breakdown.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/TkTlZF5H4SWQBYsY/images/experiments/monitor/assignment-reasons.png?fit=max&auto=format&n=TkTlZF5H4SWQBYsY&q=85&s=e0f6af7642d4fa79c829deca25e56e9e" alt="Assignment reasons breakdown chart" width="990" height="614" data-path="images/experiments/monitor/assignment-reasons.png" />
</Frame>

## Crossover Troubleshooting

Crossover warnings usually mean:

1. The request bootstrapped with a different stable ID (`BootstrapStableIDMismatch`).
2. Both client and server SDKs are checking the same gate/experiment without synchronized updates.

If you can't pinpoint the cause, ping us in Slack - we're happy to help.

## Exposure Streams

Scroll below the health checks to view exposure streams. These tables show every recent check, including the rule that matched and any secondary exposures (holdouts, targeting gates, etc.). They’re handy for validating targeting and confirming ramp progress.

## Cumulative Exposures

To track growth per variant:

1. Open the **Results** tab.
2. Locate the **Cumulative Exposures** chart.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/TkTlZF5H4SWQBYsY/images/experiments/monitor/cumulative-exposures.png?fit=max&auto=format&n=TkTlZF5H4SWQBYsY&q=85&s=e83ba8634df3b1da3d912251f59605ae" alt="Cumulative exposures chart" width="2214" height="604" data-path="images/experiments/monitor/cumulative-exposures.png" />
</Frame>

The chart highlights how many users have entered each group over time, making it easy to spot ramp issues early.

Keeping an eye on these diagnostics helps you resolve issues quickly and keep experiments on track.


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.statsig.com/statsig-warehouse-native/features/statistics/methodologies/srm-checks.md

# Source: https://docs.statsig.com/stats-engine/methodologies/srm-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SRM Checks

> Understand how Statsig detects sample ratio mismatch (SRM) and how to debug skewed traffic splits.

## SRM - Sample Ratio Mismatch

Sample ratio mismatch (SRM for short) is when the observed allocation of **unique** users between test groups differs from the expected allocation or "split" of the test. We have a brief [rundown on this topic here](https://www.statsig.com/blog/sample-ratio-mismatch) on our blog.

This is a signal that there could be some unknown bias in the test. This is a major problem because unless you can clearly diagnose the reason for the imbalance, there's not an easy way to know how much this bias impacts your results.

## SRM Checks

Statsig runs SRM checks on all experiments and feature gates as part of our Health Checks (described [here](/experiments-plus/monitor)). We use a Chi-squared test to identify if the split of users between groups is indicative of a Sample Ratio Mismatch.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/experiments/srm-checks-health.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=6510b99234256b023b7e135f2f6d64a2" alt="SRM health check results interface" width="1745" height="765" data-path="images/experiments/srm-checks-health.png" />
</Frame>

We automatically analyze data by common dimensions logged by the Statsig SDK to identify potential drivers of SRM. These include sdk\_type, sdk\_version, reason, is\_bot, browser\_name, browser\_version, os, os\_version, and region to identify potential causes.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/experiments/srm-checks-dimensions.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=9e8aa7a648b3eda015f4beafd55c3123" alt="SRM dimension analysis breakdown" width="993" height="545" data-path="images/experiments/srm-checks-dimensions.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).
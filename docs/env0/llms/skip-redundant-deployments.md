# Source: https://docs.envzero.com/guides/policies-governance/skip-redundant-deployments.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Avoiding Redundant Deployments

> Skip queued deployments and deploy only the latest version to speed up continuous deployment in env zero

A skip redundant deployments policy is especially useful for dynamic environments with frequent changes, in case you only care about the latest changes and want fast continuous deployment.

If enabled under "Project Settings" -> "Policies" tab -> “Skip redundant deployments”, when multiple deploy executions are queued, we will skip up to the next destroy execution. If there is no destroy execution queued, we will skip to the last queued deployment. We will not, however, skip destroy deployments nor PR plans since their sequence matters.

In the example below, we can see that we saved about 80 minutes by skipping 4 queued deployments that would have taken about 20 minutes each.

Instead of waiting almost 2 hours, we deployed the latest version in 20 minutes.

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/f2cef98-screen_shot_2021-10-24_at_17.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=0b888fb3464b9670065e6b56e31023c7" alt="" width="1111" height="781" data-path="images/guides/policies-governance/f2cef98-screen_shot_2021-10-24_at_17.png" />

Built with [Mintlify](https://mintlify.com).

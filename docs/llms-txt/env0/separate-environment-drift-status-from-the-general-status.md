# Source: https://docs.envzero.com/changelogs/2024/02/separate-environment-drift-status-from-the-general-status.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🛠️ BREAKING CHANGE - Seperate environment "Drift Status" from the Deployment status

> Starting Feb 29th, we will enhance user experience by separating Drift Detection and Deployment status into distinct values. This improvement is part of our ongoing efforts to provide users with a seamless and efficient experience. Users will now find it easier to monitor both the latest deployment queue action and any drift detection without the need for extensive deployment log reviews.

Starting Feb 29th, we will enhance user experience by separating Drift Detection and Deployment status into distinct values. This improvement is part of our ongoing efforts to provide users with a seamless and efficient experience. Users will now find it easier to monitor both the latest deployment queue action and any drift detection without the need for extensive deployment log reviews.

# Why the change?

In env0, an environment's status, determined by the last action in its deployment queue, can be overshadowed by drift status. For example, an environment marked as `DRIFTED` may obscure the result of its latest deployment, and performing a deployment after drift detection can alter the `DRIFTED` status, potentially masking detected drift.

# What will break?

The environment status `DRIFTED` **will be deprecated**. Instead, a new property, `driftStats`, will be added to the environment modal, indicating drift status with the following values:

* `DISABLED`- DD is disabled
* `OK`-The last Drift deployment detects no drift.
* `DRIFTED` - The last Drift deployment detects a drift.
* `ERROR`- The last Drift deployment had an error.
* `NEVER_RUN`- Drift deployment never run since DD was enabled.

Built with [Mintlify](https://mintlify.com).

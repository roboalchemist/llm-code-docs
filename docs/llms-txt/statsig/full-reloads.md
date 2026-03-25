# Source: https://docs.statsig.com/statsig-warehouse-native/features/full-reloads.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Full Reloads

Full reloads will completely wipe the Staging/Results Datasets Statsig has used for previous pulse calculations, and Statsig will recalculate results from scratch.

Generally, this is used for

* Initial or historical pulse loads.
* Cases where data has been lost or dropped on the customer side, meaning incremental reloads have lost state.
* Cases where data changes frequently, e.g. a DBT full reload changes historical data due to chargebacks, model changes, or other reasons.
* There's complex data dependencies, and a team wants to ensure that the gap between Statsig and Internal Systems doesn't cause inconsistencies.


Built with [Mintlify](https://mintlify.com).
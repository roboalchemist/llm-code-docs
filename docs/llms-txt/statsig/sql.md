# Source: https://docs.statsig.com/statsig-warehouse-native/guides/sql.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View SQL

Statsig Warehouse Native runs SQL in your warehouse to generate the experiment results, and the queries are fully transparent and made visible in console. This means that you can trace any results you see on the Statsig console back to its calculation, artifacts, and raw events.

The [pipeline-overview](/statsig-warehouse-native/pipeline-overview) provides an overview of how the queries are orchestrated to produce the experiment results. If you are curious about the details or want to debug, you can find the experiment-specific SQL by going to the experiment’s Pulse view -> view history -> view details on a specific pulse load. You’ll be able to see all the jobs that went into that pulse load.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/oeabJ0ow-rt3PoHE/images/statsig-warehouse-native/guides/sql/f34e1265-e303-4705-b8cd-1a170a2af91e.png?fit=max&auto=format&n=oeabJ0ow-rt3PoHE&q=85&s=7a4bc3a03105f904a203ab05067716e0" alt="Pulse view SQL query details interface" width="994" height="701" data-path="images/statsig-warehouse-native/guides/sql/f34e1265-e303-4705-b8cd-1a170a2af91e.png" />
</Frame>

There are a few queries with \[Health Check] as a prefix that automatically check the health of the experiment. You can view [this page](/statsig-warehouse-native/features/monitor-an-experiment) to understand what they do.

For experiment result calculation queries, below are one-sentence summaries of what each query does.

* First exposure: Generate the first exposure time of this experiment at the unit level, given the assignment source.
* Exposure summary: Summarize the first exposures at the group level and generate cumulative exposures.
* User-level calculations: Calculate unit-level metrics at unit \_ metric \_ day grain.
* Windowed rollups: Rollup unit-level metrics at different time windows.
* Plus calculation: Generate the sample parameters that are necessary for calculating treatment effects, such as units, total, mean, standard deviation, population variance, covariance, etc.


Built with [Mintlify](https://mintlify.com).
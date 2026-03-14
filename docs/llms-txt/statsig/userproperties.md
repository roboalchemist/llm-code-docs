# Source: https://docs.statsig.com/experiments/interpreting-results/userproperties.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Slicing by User Properties

Statsig let's you slice results by user properties. Common examples of doing this include breaking down results by user's home country, subscription status or engagement level.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/interpreting-results/userproperties/60ad9a4f-8e85-42a6-8c36-147fc6c85873.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=55c4f2b64a35c095788897c484f8176d" alt="Pulse results sliced by user properties" width="1161" height="145" data-path="images/experiments/interpreting-results/userproperties/60ad9a4f-8e85-42a6-8c36-147fc6c85873.png" />
</Frame>

For Statsig Cloud, these user properties are captured (and frozen) from the properties set on the user's first exposure. Statsig Warehouse Native also adds support for reading them from a warehouse table (Entity Properties). You can always run custom queries on experiments to slice by user properties.

## Pre-Computed User Properties

User properties that are frequently used to slice results can be pre-computed when using Statsig Warehouse Native. To do this, you can configure these properties to be pre-computed on the experiment setup page, under the advanced settings. It's also possible to configure team-level defaults for this - or pre-configure it on an experiment template.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/interpreting-results/userproperties/196bd217-dd29-4b63-9f1b-d08639e0d36d.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=96598ce2b206e820e60e4d4b7e210f49" alt="Experiment setup page with pre-computed user properties configuration" width="886" height="591" data-path="images/experiments/interpreting-results/userproperties/196bd217-dd29-4b63-9f1b-d08639e0d36d.png" />
</Frame>

Once configured, you can also apply filters to all metrics on your results.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/interpreting-results/userproperties/8b5c6dcc-feac-46c9-a6fa-331daafc4864.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=96696e1fab4251c96f00e8f2f94564e5" alt="Metrics results with user property filters applied" width="1758" height="431" data-path="images/experiments/interpreting-results/userproperties/8b5c6dcc-feac-46c9-a6fa-331daafc4864.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.statsig.com/metrics/directionality.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metric Directionality

> Configure whether increases or decreases in metric values should be considered positive or negative in experiments.

# Setting Metric Directionality

By default, increases to a metric value are assumed to be 'good', and are represented by a green color in Experiment results. However for many metrics, it’s actually a good thing when the metric decreases and similarly bad to see an increase (e.g. page load times or many performance metrics)

For these types of metrics, you can set the desired direction you want to see a metric move and experiment results will update the color-coding in metric lifts accordingly. To do so, go to any metric detail view page and click the Edit Pencil next to the 'Directionality' section in the right rail of the page to see the “Set Metric Directionality” option.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/directionality/fa0cbf9f-c84f-4db6-b9fa-84d672358a72.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=3a02f6df4f01826be9d343f76ad132b8" alt="Metric directionality configuration interface" width="1477" height="933" data-path="images/metrics/directionality/fa0cbf9f-c84f-4db6-b9fa-84d672358a72.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).
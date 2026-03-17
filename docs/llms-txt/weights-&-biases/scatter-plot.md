# Source: https://docs.wandb.ai/models/app/features/panels/scatter-plot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Scatter plots

> Create and customize scatter plots in W&B to compare runs and visualize relationships between experiment metrics.

This page shows how to use scatter plots in W\&B.

## Use case

Use scatter plots to compare multiple runs and visualize the performance of an experiment:

* Plot lines for minimum, maximum, and average values.
* Customize metadata tooltips.
* Control point colors.
* Adjust axis ranges.
* Use a log scale for the axes.

## Example

The following example shows a scatter plot displaying validation accuracy for different models over several weeks of experimentation. The tooltip includes batch size, dropout, and axis values. A line also shows the running average of validation accuracy.

[See a live example →](https://app.wandb.ai/l2k2/l2k/reports?view=carey%2FScatter%20Plot)

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/88iR80mZ8tuFCZUU/images/general/scatter-plots-1.png?fit=max&auto=format&n=88iR80mZ8tuFCZUU&q=85&s=0fc0dbcbfb6f21e881e160f07bc80b08" alt="Validation accuracy scatter plot" width="1300" height="864" data-path="images/general/scatter-plots-1.png" />
</Frame>

## Create a scatter plot

To create a scatter plot in the W\&B UI:

1. Navigate to the **Workspaces** tab.
2. In the **Charts** panel, click the action menu `...`.
3. From the pop-up menu, select **Add panels**.
4. In the **Add panels** menu, select **Scatter plot**.
5. Set the `x` and `y` axes to plot the data you want to view. Optionally, set maximum and minimum ranges for your axes or add a `z` axis.
6. Click **Apply** to create the scatter plot.
7. View the new scatter plot in the Charts panel.

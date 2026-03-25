# Source: https://docs.wandb.ai/models/app/features/panels/parallel-coordinates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Compare results across machine learning experiments

# Parallel coordinates

Parallel coordinates charts summarize the relationship between large numbers of hyperparameters and model metrics at a glance.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/parallel_coordinates.gif?s=0340236d2ff617e9704824e513adc388" alt="Parallel coordinates plot" width="1482" height="1056" data-path="images/app_ui/parallel_coordinates.gif" />
</Frame>

* **Axes**: Different hyperparameters from [`wandb.Run.config`](/models/evaluate-models/) and metrics from [`wandb.Run.log()`](/models/evaluate-models/).
* **Lines**: Each line represents a single run. Mouse over a line to see a tooltip with details about the run. All lines that match the current filters will be shown, but if you turn off the eye, lines will be grayed out.

## Create a parallel coordinates panel

1. Navigate to the landing page for your workspace
2. Click **Add Panels**
3. Select **Parallel coordinates**

## Panel settings

To configure the panel, click the edit button in the upper right corner of the panel.

* **Tooltip**: On hover, a legend shows up with info on each run
* **Titles**: Edit the axis titles to be more readable
* **Gradient**: Customize the gradient to be any color range you like
* **Log scale**: Each axis can be set to view on a log scale independently
* **Flip axis**: Switch the axis direction— this is useful when you have both accuracy and loss as columns

[Interact with a live parallel coordinates panel](https://app.wandb.ai/example-team/sweep-demo/reports/Zoom-in-on-Parallel-Coordinates-Charts--Vmlldzo5MTQ4Nw)

# Source: https://docs.wandb.ai/models/sweeps/visualize-sweep-results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Visualize the results of your W&B Sweeps with the W&B App UI.

# Visualize sweep results

Visualize the results of your W\&B Sweeps with the W\&B App. Navigate to the [W\&B App](https://wandb.ai/home). Choose the project that you specified when you initialized a sweep. You will be redirected to your project [workspace](/models/track/workspaces/). Select the **Sweep icon** in the project sidebar (broom icon). From the Sweep UI, select the name of your Sweep from the list.

By default, W\&B will automatically create a parallel coordinates plot, a parameter importance plot, and a scatter plot when you start a W\&B Sweep job.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/6bJLb4DIApn2yeFO/images/sweeps/navigation_sweeps_ui.gif?s=dad637ada03b92f50ebe9e831a221275" alt="Sweep UI in project sidebar" width="3794" height="1802" data-path="images/sweeps/navigation_sweeps_ui.gif" />
</Frame>

Parallel coordinates charts summarize the relationship between large numbers of hyperparameters and model metrics at a glance. For more information on parallel coordinates plots, see [Parallel coordinates](/models/app/features/panels/parallel-coordinates/).

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/6bJLb4DIApn2yeFO/images/sweeps/example_parallel_coordiantes_plot.png?fit=max&auto=format&n=6bJLb4DIApn2yeFO&q=85&s=0b516bbdd116f71e98a21e945b3da0ae" alt="Example parallel coordinates plot." width="3088" height="750" data-path="images/sweeps/example_parallel_coordiantes_plot.png" />
</Frame>

The scatter plot(left) compares the W\&B Runs that were generated during the Sweep. For more information about scatter plots, see [Scatter Plots](/models/app/features/panels/scatter-plot/).

The parameter importance plot(right) lists the hyperparameters that were the best predictors of, and highly correlated to desirable values of your metrics. For more information on parameter importance plots, see [Parameter Importance](/models/app/features/panels/parameter-importance/).

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/6bJLb4DIApn2yeFO/images/sweeps/scatter_and_parameter_importance.png?fit=max&auto=format&n=6bJLb4DIApn2yeFO&q=85&s=8078fed195644319979c0cd251cb051b" alt="Scatter plot and parameter importance" width="3086" height="846" data-path="images/sweeps/scatter_and_parameter_importance.png" />
</Frame>

You can alter the dependent and independent values (x and y axis) that are automatically used. Within each panel there is a pencil icon called **Edit panel**. Choose **Edit panel**. A model will appear. Within the modal, you can alter the behavior of the graph.

For more information on all default W\&B visualization options, see [Panels](/models/app/features/panels/). See the [Data Visualization docs](/models/tables/) for information on how to create plots from W\&B Runs that are not part of a W\&B Sweep.

# Source: https://docs.wandb.ai/models/app/features/panels/bar-plot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Visualize metrics, customize axes, and compare categorical data as bars.

# Bar plots

A bar plot presents categorical data with rectangular bars which can be plotted vertically or horizontally. Bar plots show up by default with `wandb.Run.log()` when all logged values are of length one.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/bar_plot.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=8bd5ac92c15450ebc1a47b4684e6ab67" alt="Plotting Box and horizontal Bar plots in W&B" width="1376" height="580" data-path="images/app_ui/bar_plot.png" />
</Frame>

Customize with chart settings to limit max runs to show, group runs by any config and rename labels.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/bar_plot_custom.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=a2f9a1b60502bfcb6b400617dad8fa8c" alt="Customized bar plot" width="2674" height="1194" data-path="images/app_ui/bar_plot_custom.png" />
</Frame>

## Customize bar plots

You can also create **Box** or **Violin** Plots to combine many summary statistics into one chart type\*\*.\*\*

1. Group runs via runs table.
2. Click 'Add panel' in the workspace.
3. Add a standard 'Bar Chart' and select the metric to plot.
4. Under the 'Grouping' tab, pick 'box plot' or 'Violin', etc. to plot either of these styles.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/bar_plots.gif?s=216388a6ac06020687f8030edde0330b" alt="Customize Bar Plots" width="800" height="395" data-path="images/app_ui/bar_plots.gif" />
</Frame>

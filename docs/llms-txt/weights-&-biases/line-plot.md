# Source: https://docs.wandb.ai/models/app/features/panels/line-plot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Visualize metrics, customize axes, and compare multiple lines on a plot

# Line plots overview

Line plots display by default for metrics logged with `wandb.Run.log()` over time. Line plots support plotting multiple metrics, calculating custom axes, and more.

This page shows how to create, configure, and manage line plots in a [workspace](/models/track/workspaces).

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/line_plot_example.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=a914f7927b484c0002116e609920d83f" alt="Line plot example" width="1838" height="622" data-path="images/app_ui/line_plot_example.png" />
</Frame>

<Tip>
  For [runs](/models/runs) that execute on [CoreWeave](https://coreweave.com) infrastructure, [CoreWeave Mission Control](https://www.coreweave.com/mission-control) monitors your compute infrastructure. If an error occurs, W\&B populates infrastructure information onto your run's plots in your project's workspace. For details, see [Visualize CoreWeave infrastructure alerts](/models/runs/infrastructure-alerts).
</Tip>

## Add a line plot

This section shows how to create a line plot for a single metric or multiple metrics.

<Tabs>
  <Tab title="Single-metric line plot">
    In an [automatic workspace](/models/app/features/panels#workspace-modes), a single-metric line plot is created automatically for each logged metric. Follow these steps to re-add a line plot that was deleted from an automatic workspace, or to add a line plot to a manual workspace.

    1. Navigate to your workspace.
    2. To add a line plot globally, click **Add panels** in the control bar near the panel search field.

       To add a line plot directly to a section instead, click the section's action `...` menu, then click **+ Add panels**.
    3. To add a single-metric plot with default settings, click **Quick panel builder**.
       1. In the **Single-key panels** tab, hover over a metric, then click **Add**. Repeat this step for each panel you want to add.
       2. Click **Create \<number> panels**.
    4. To add a custom line plot instead, click **Line plot**.
       1. Configure the line plot's data, grouping, and display preferences using the corresponding tabs. For details, see [Edit line plot settings](#edit-line-plot-settings).
       2. To add calculated expressions to the x or y axis, click **Expressions**. [JavaScript regular expressions](https://www.w3schools.com/js/js_regexp.asp) are supported.
          Select the type of panel to add, such as a chart. The panel's configuration details appear with selected defaults.
    5. Optionally, customize the panel and its display preferences. Configuration options depend on the type of panel you select. To learn more about the options for each type of panel, refer to the relevant section below, such as [Line plots](/models/app/features/panels/line-plot/) or [Bar plots](/models/app/features/panels/bar-plot/).
    6. Click **Apply**.
  </Tab>

  <Tab title="Multi-metric line plot">
    <Note>
      This feature is in preview, available by invitation only. To request enrollment, contact [support](mailto:support@wandb.com) or your AISE.
    </Note>

    In an [automatic workspace](/models/app/features/panels#workspace-modes), a single-metric line plot is created automatically for each logged metric. This section shows how to create a single line plot that shows multiple metrics together, defined by a JavaScript regular expression. You can optionally consolidate many single-metric plots into a single multi-metric plot. This can improve the performance of a workspace with many logged metrics, and can help you analyze the results of your runs efficiently.

    1. Navigate to your workspace.
    2. To add a line plot globally, click **Add panels** in the control bar near the panel search field.

       To add a line plot directly to a section instead, click the section's action `...` menu, then click **+ Add panels**.
    3. Click **Quick panel builder**, then click the **Multi-metric panels** tab.
    4. In **Regex** enter an expression in [JavaScript regular expression](https://www.w3schools.com/js/js_regexp.asp) format. As you type, the UI updates to show which metrics match the expression. By default, the plot name shows the regular expression used by the plot. The plot includes lines for all metrics that match the expression, including metrics logged in the future.
    5. To optionally remove duplicate single-metric panels when the multi-metric plot is created, toggle **Clean up auto-generated panels**. A preview shows which panels will be cleaned up. <Note>When this option is turned on, a single-metric plot will not be created for a newly logged metric that matches the expression. Instead, it will be included only in this multi-metric plot.</Note>
    6. Click **Create \<number> panels**.

    ### More about multi-metric regular expressions

    Multi-metric line plots use [JavaScript regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions) to match metric names. These section demonstrate some common use cases and gives more details about how the regular expressions work, such as how capture groups affect the panels that are created.

    #### Common use cases

    This section shows some ways you can use multi-metric panels to help you analyze your experiment results.

    **Compare metrics across layers or model components**
    Instead of creating separate panels for each layer's metrics, you can view them together in a single panel. For example, if you log metrics with consistent naming, like `layer_0_loss`, `layer_1_loss`, and `layer_2_loss` in this Python example code, you can use the regex `layer_\d+_loss` to display all layer losses on one plot.

    ```python  theme={null}
    with wandb.init(project="multi-layer-model") as run:
        for step in range(100):
            run.log({
                "layer_0_loss": loss_0,
                "layer_1_loss": loss_1,
                "layer_2_loss": loss_2,
                "step": step
            })
    ```

    **Group related metrics by prefix or suffix**
    Match all metrics that share a common naming pattern. For example:

    * `train_.*` matches all training metrics like `train_loss`, `train_accuracy`, `train_f1_score`
    * `.*_accuracy` matches accuracy metrics across different datasets like `train_accuracy`, `val_accuracy`, `test_accuracy`

    **Match specific metric variations**
    Use alternation to match only the metrics you want. For example, the non-capture group `(?:layer_0|layer_10)_loss` matches only the first and tenth layer losses, excluding intermediate layers.

    #### Understanding capture groups

    Capture groups in your regular expression control how multi-metric panels are created. This behavior can be confusing if you're not expecting it.

    * **Capture groups create multiple panels**
      When your regular expression includes parentheses that form a capture group, the UI creates a separate panel for each unique value captured by that group.

      For example, the expression `(layer_0|layer_10)_loss` includes a capture group and will create two separate panels:

      1. One panel for metrics matching `layer_0`.
      2. One panel for metrics matching `layer_10`.

    * **Non-capturing groups keep metrics together**
      To match multiple alternatives without creating separate panels, use a non-capturing group with the `?:` syntax. The expression `(?:layer_0|layer_10)_loss` matches the same metrics as the previous example, but displays them together in a single panel.

    Here's the difference:

    * `(layer_0|layer_10)_loss` - Creates two panels, one for each layer.
    * `(?:layer_0|layer_10)_loss` - Creates one panel showing both layers together.

    This gives you flexibility to choose the approach that best fits your analysis needs. Use capture groups when you want to separate metrics into distinct panels. Use non-capturing groups when you want to compare metrics together on a single plot.
  </Tab>
</Tabs>

## Edit line plot settings

This section shows how to edit the settings for an individual line plot panel, all line plot panels in a section, or all line plot panels in a workspace. For comprehensive details about line plot settings, see [Line plot reference](/models/app/features/panels/line-plot/reference).

### Individual line plot

A line plot's individual settings override the line plot settings for the section or the workspace. To customize a line plot:

1. Navigate to your workspace.
2. Hover your mouse over the panel, then click the gear icon.
3. Within the drawer that appears, select a tab to edit its settings.
4. Click **Apply**.

Line plot settings are organized into tabs:

* **Data**: Configure x-axis, y-axis, sampling method, smoothing, outliers, and chart type.
* **Grouping**: Configure whether and how to group and aggregate runs in the plot.
* **Chart**: Specify titles for the panel and axes, and configure legend visibility and position.
* **Legend**: Customize the appearance and content of the panel's legend.
* **Expressions**: Add custom calculated expressions for the axes.

For detailed information about each setting, see the [Line plot reference](/models/app/features/panels/line-plot/reference).

### All line plots in a section

To customize the default settings for all line plots in a section, overriding workspace settings for line plots:

1. Navigate to your workspace.
2. Click the section's gear icon to open its settings.
3. Within the drawer that appears, select the **Data** or **Display preferences** tabs to configure the default settings for the section. For details about each **Data** setting, see the [Line plot reference](/models/app/features/panels/line-plot/reference). For details about each display preference, refer to [Configure section layout](../#configure-section-layout).

### All line plots in a workspace

To customize the default settings for all line plots in a workspace:

1. Navigate to your workspace.
2. Click the workspace settings icon, which has a gear with the label **Settings**.
3. Click **Line plots**.
4. Within the drawer that appears, select the **Data** or **Display preferences** tabs to configure the default settings for the workspace.
   * For details about each **Data** setting, see the [Line plot reference](/models/app/features/panels/line-plot/reference).
   * For details about each **Display preferences** section, refer to [Workspace display preferences](../#configure-workspace-layout). At the workspace level, you can configure the default **Zooming** behavior for line plots. This setting controls whether to synchronize zooming across line plots with a matching x-axis key. Disabled by default.

## Visualize average values on a plot

If you have several different experiments and you'd like to see the average of their values on a plot, you can use the Grouping feature in the table. Click "Group" above the run table and select "All" to show averaged values in your graphs.

Here is what the graph looks like before averaging:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/demo_precision_lines.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=bf4eea30b134cf71b5740ea363796a9f" alt="Individual precision lines" width="849" height="440" data-path="images/app_ui/demo_precision_lines.png" />
</Frame>

The proceeding image shows a graph that represents average values across runs using grouped lines.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/demo_average_precision_lines.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=2daca68510da1850a385677fe3493eea" alt="Averaged precision lines" width="852" height="441" data-path="images/app_ui/demo_average_precision_lines.png" />
</Frame>

## Visualize NaN value on a plot

You can also plot `NaN` values including PyTorch tensors on a line plot with `wandb.Run.log()`. For example:

```python  theme={null}
with wandb.init() as run:
    # Log a NaN value
    run.log({"test": float("nan")})
```

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/visualize_nan.png?fit=max&auto=format&n=UhAQoGpm-LvpH3-8&q=85&s=437bc74f55904256a87eeb0168fe0ca1" alt="NaN value handling" width="936" height="688" data-path="images/app_ui/visualize_nan.png" />
</Frame>

## Compare multiple metrics on one chart

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/visualization_add.gif?s=d2653cc4090ac8e61469e9c1fa037294" alt="Adding visualization panels" width="3866" height="2574" data-path="images/app_ui/visualization_add.gif" />
</Frame>

1. Navigate to your workspace.
2. Select the **Add panels** button in the top right corner of the page.
3. From the drawer that appears, expand the Evaluation dropdown.
4. Select **Run comparer**

## Change the colors of the lines

Sometimes the default color of runs is not helpful for comparison. To help overcome this, wandb provides two instances with which one can manually change the colors.

<Tabs>
  <Tab title="From the run table">
    Each run is given a random color by default upon initialization.

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/line_plots_run_table_random_colors.png?fit=max&auto=format&n=UhAQoGpm-LvpH3-8&q=85&s=b1e19999cb48b8f0fe26a4d510996d41" alt="Random colors given to runs" width="272" height="174" data-path="images/app_ui/line_plots_run_table_random_colors.png" />
    </Frame>

    Upon clicking any of the colors, a color palette appears from which we can manually choose the color we want.

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/line_plots_run_table_color_palette.png?fit=max&auto=format&n=UhAQoGpm-LvpH3-8&q=85&s=c82cc1818f19c107094050393cc29f8d" alt="The color palette" width="261" height="393" data-path="images/app_ui/line_plots_run_table_color_palette.png" />
    </Frame>
  </Tab>

  <Tab title="From the chart legend settings">
    1. Navigate to your workspace.
    2. Hover your mouse over the panel you want to edit its settings for.
    3. Select the pencil icon that appears.
    4. Choose the **Legend** tab.

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/plot_style_line_plot_legend.png?fit=max&auto=format&n=UhAQoGpm-LvpH3-8&q=85&s=a2681364700e100f42e96eda1de6d52a" alt="Line plot legend settings" width="2682" height="1166" data-path="images/app_ui/plot_style_line_plot_legend.png" />
    </Frame>
  </Tab>
</Tabs>

## Visualize on different x axes

If you'd like to see the absolute time that an experiment has taken, or see what day an experiment ran, you can switch the x axis. Here's an example of switching from steps to relative time and then to wall time.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/howto_use_relative_time_or_wall_time.gif?s=e0f557baf67f90f59ca30d1110c74226" alt="X-axis time options" width="3348" height="1880" data-path="images/app_ui/howto_use_relative_time_or_wall_time.gif" />
</Frame>

To use a custom x-axis, log the metric in the same call to `wandb.Run.log()` where you log the y-axis. For example:

```python  theme={null}
with wandb.init() as run:
    for i in range(100):
        run.log({"accuracy": acc, "custom_x": i * 10})
```

For more details, see [Customize log axes](/models/track/log/customize-logging-axes#customize-log-axes).

## Zoom

Click and drag a rectangle to zoom vertically and horizontally at the same time. This changes the x-axis and y-axis zoom.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/line_plots_zoom.gif?s=6867f5c8e2beead862ca231c31134bed" alt="Plot zoom functionality" width="1056" height="473" data-path="images/app_ui/line_plots_zoom.gif" />
</Frame>

## Hide chart legend

Turn off the legend in the line plot with this simple toggle:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/demo_hide_legend.gif?s=2cf76705cb4e9ce763414eaa5d878835" alt="Hide legend toggle" width="2720" height="1246" data-path="images/app_ui/demo_hide_legend.gif" />
</Frame>

## Create a run metrics notification

Use [Automations](/models/automations/) to notify your team when a run metric meets a condition you specify. An automation can post to a Slack channel or run a webhook.

From a line plot, you can quickly create a [run metrics notification](/models/automations/automation-events/#run-events) for the metric it shows:

1. Navigate to your workspace.
2. Hover over the panel, then click the bell icon.
3. Configure the automation using the basic or advanced configuration controls. For example, apply a run filter to limit the scope of the automation, or configure an absolute threshold.

Learn more about [Automations](/models/automations/).

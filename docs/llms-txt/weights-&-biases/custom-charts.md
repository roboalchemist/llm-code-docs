# Source: https://docs.wandb.ai/models/ref/python/custom-charts.md

# Source: https://docs.wandb.ai/models/app/features/custom-charts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom charts overview

> Create custom charts in W&B projects with Vega visualizations

Create custom charts in your W\&B project. Log arbitrary tables of data and visualize them exactly how you want. Control details of fonts, colors, and tooltips with the power of [Vega](https://vega.github.io/vega/).

* Code: Try an example [Colab Colab notebook](https://tiny.cc/custom-charts).
* Video: Watch a [walkthrough video](https://www.youtube.com/watch?v=3-N9OV6bkSM).
* Example: Quick Keras and Sklearn [demo notebook](https://colab.research.google.com/drive/1g-gNGokPWM2Qbc8p1Gofud0_5AoZdoSD?usp=sharing)

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/supported_charts.png?fit=max&auto=format&n=UhAQoGpm-LvpH3-8&q=85&s=0c8fb6be9c8c62db8ec918b68cc69edc" alt="Supported charts from vega.github.io/vega" max-width="90%" width="2634" height="588" data-path="images/app_ui/supported_charts.png" />
</Frame>

### How it works

1. **Log data**: From your script, log [config](/models/track/config/) and summary data.
2. **Customize the chart**: Pull in logged data with a [GraphQL](https://graphql.org) query. Visualize the results of your query with [Vega](https://vega.github.io/vega/), a powerful visualization grammar.
3. **Log the chart**: Call your own preset from your script with `wandb.plot_table()`.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/pr_roc.png?fit=max&auto=format&n=UhAQoGpm-LvpH3-8&q=85&s=e0f85cc0f90235b9831b980d68540f35" alt="PR and ROC curves" width="1114" height="422" data-path="images/app_ui/pr_roc.png" />
</Frame>

If you do not see the expected data, the column you are looking for might not be logged in the selected runs. Save your chart, go back out to the runs table, and verify selected runs using the **eye** icon.

## Log charts from a script

### Builtin presets

W\&B has a number of builtin chart presets that you can log directly from your script. These include line plots, scatter plots, bar charts, histograms, PR curves, and ROC curves.

<Tabs>
  <Tab title="Line plot">
    `wandb.plot.line()`

    Log a custom line plot—a list of connected and ordered points (x,y) on arbitrary axes x and y.

    ```python  theme={null}
    with wandb.init() as run:
      data = [[x, y] for (x, y) in zip(x_values, y_values)]
      table = wandb.Table(data=data, columns=["x", "y"])
      run.log(
          {
              "my_custom_plot_id": wandb.plot.line(
                  table, "x", "y", title="Custom Y vs X Line Plot"
              )
          }
      )
    ```

    A line plot logs curves on any two dimensions. If you plot two lists of values against each other, the number of values in the lists must match exactly (for example, each point must have an x and a y).

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/line_plot.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=503d371af79f936e93fbecc2ca0e58d0" alt="Custom line plot" width="1930" height="1228" data-path="images/app_ui/line_plot.png" />
    </Frame>

    [See an example report](https://wandb.ai/wandb/plots/reports/Custom-Line-Plots--VmlldzoyNjk5NTA) or [try an example Google Colab notebook](https://tiny.cc/custom-charts).
  </Tab>

  <Tab title="Scatter plot">
    `wandb.plot.scatter()`

    Log a custom scatter plot—a list of points (x, y) on a pair of arbitrary axes x and y.

    ```python  theme={null}
    with wandb.init() as run:
      data = [[x, y] for (x, y) in zip(class_x_prediction_scores, class_y_prediction_scores)]
      table = wandb.Table(data=data, columns=["class_x", "class_y"])
      run.log({"my_custom_id": wandb.plot.scatter(table, "class_x", "class_y")})
    ```

    You can use this to log scatter points on any two dimensions. Note that if you're plotting two lists of values against each other, the number of values in the lists must match exactly (for example, each point must have an x and a y).

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/demo_scatter_plot.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=daa89597ff20df723eb7e67bc0bf23cd" alt="Scatter plot" width="2194" height="940" data-path="images/app_ui/demo_scatter_plot.png" />
    </Frame>

    [See an example report](https://wandb.ai/wandb/plots/reports/Custom-Scatter-Plots--VmlldzoyNjk5NDQ) or [try an example Google Colab notebook](https://tiny.cc/custom-charts).
  </Tab>

  <Tab title="Bar chart">
    `wandb.plot.bar()`

    Log a custom bar chart—a list of labeled values as bars—natively in a few lines:

    ```python  theme={null}
    with wandb.init() as run:
      data = [[label, val] for (label, val) in zip(labels, values)]
      table = wandb.Table(data=data, columns=["label", "value"])
      run.log(
          {
              "my_bar_chart_id": wandb.plot.bar(
                  table, "label", "value", title="Custom Bar Chart"
              )
          }
      )
    ```

    You can use this to log arbitrary bar charts. Note that the number of labels and values in the lists must match exactly (for example, each data point must have both).

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/demo_bar_plot.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=645a1d143323e73289a2b16afc6947b8" alt="Demo bar plot" width="659" height="579" data-path="images/app_ui/demo_bar_plot.png" />
    </Frame>

    [See an example report](https://wandb.ai/wandb/plots/reports/Custom-Bar-Charts--VmlldzoyNzExNzk) or [try an example Google Colab notebook](https://tiny.cc/custom-charts).
  </Tab>

  <Tab title="Histogram">
    `wandb.plot.histogram()`

    Log a custom histogram—sort list of values into bins by count/frequency of occurrence—natively in a few lines. Let's say I have a list of prediction confidence scores (`scores`) and want to visualize their distribution:

    ```python  theme={null}
    with wandb.init() as run:
      data = [[s] for s in scores]
      table = wandb.Table(data=data, columns=["scores"])
      run.log({"my_histogram": wandb.plot.histogram(table, "scores", title=None)})
    ```

    You can use this to log arbitrary histograms. Note that `data` is a list of lists, intended to support a 2D array of rows and columns.

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/demo_custom_chart_histogram.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=2afa613cd9ba55442aa5275d8513be27" alt="Custom histogram" width="1252" height="558" data-path="images/app_ui/demo_custom_chart_histogram.png" />
    </Frame>

    [See an example report](https://wandb.ai/wandb/plots/reports/Custom-Histograms--VmlldzoyNzE0NzM) or [try an example Google Colab notebook](https://tiny.cc/custom-charts).
  </Tab>

  <Tab title="PR curve">
    `wandb.plot.pr_curve()`

    Create a [Precision-Recall curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve) in one line:

    ```python  theme={null}
    with wandb.init() as run:
      plot = wandb.plot.pr_curve(ground_truth, predictions, labels=None, classes_to_plot=None)

      run.log({"pr": plot})
    ```

    You can log this whenever your code has access to:

    * a model's predicted scores (`predictions`) on a set of examples
    * the corresponding ground truth labels (`ground_truth`) for those examples
    * (optionally) a list of the labels/class names (`labels=["cat", "dog", "bird"...]` if label index 0 means cat, 1 = dog, 2 = bird, etc.)
    * (optionally) a subset (still in list format) of the labels to visualize in the plot

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/demo_average_precision_lines.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=2daca68510da1850a385677fe3493eea" alt="Precision-recall curves" width="852" height="441" data-path="images/app_ui/demo_average_precision_lines.png" />
    </Frame>

    [See an example report](https://wandb.ai/wandb/plots/reports/Plot-Precision-Recall-Curves--VmlldzoyNjk1ODY) or [try an example Google Colab notebook](https://colab.research.google.com/drive/1mS8ogA3LcZWOXchfJoMrboW3opY1A8BY?usp=sharing).
  </Tab>

  <Tab title="ROC curve">
    `wandb.plot.roc_curve()`

    Create an [ROC curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve) in one line:

    ```python  theme={null}
    with wandb.init() as run:
      # ground_truth is a list of true labels, predictions is a list of predicted scores
      ground_truth = [0, 1, 0, 1, 0, 1]
      predictions = [0.1, 0.4, 0.35, 0.8, 0.7, 0.9]

      # Create the ROC curve plot
      # labels is an optional list of class names, classes_to_plot is an optional subset of those labels to visualize
      plot = wandb.plot.roc_curve(
          ground_truth, predictions, labels=None, classes_to_plot=None
      )

      run.log({"roc": plot})
    ```

    You can log this whenever your code has access to:

    * a model's predicted scores (`predictions`) on a set of examples
    * the corresponding ground truth labels (`ground_truth`) for those examples
    * (optionally) a list of the labels/ class names (`labels=["cat", "dog", "bird"...]` if label index 0 means cat, 1 = dog, 2 = bird, etc.)
    * (optionally) a subset (still in list format) of these labels to visualize on the plot

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/demo_custom_chart_roc_curve.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=4a40f16fed643f98e4567163fbd54a0a" alt="ROC curve" width="1338" height="788" data-path="images/app_ui/demo_custom_chart_roc_curve.png" />
    </Frame>

    [See an example report](https://wandb.ai/wandb/plots/reports/Plot-ROC-Curves--VmlldzoyNjk3MDE) or [try an example Google Colab notebook](https://colab.research.google.com/drive/1_RMppCqsA8XInV_jhJz32NCZG6Z5t1RO?usp=sharing).
  </Tab>
</Tabs>

### Custom presets

Tweak a builtin preset, or create a new preset, then save the chart. Use the chart ID to log data to that custom preset directly from your script. [Try an example Google Colab notebook](https://tiny.cc/custom-charts).

```python  theme={null}
# Create a table with the columns to plot
table = wandb.Table(data=data, columns=["step", "height"])

# Map from the table's columns to the chart's fields
fields = {"x": "step", "value": "height"}

# Use the table to populate the new custom chart preset
# To use your own saved chart preset, change the vega_spec_name
my_custom_chart = wandb.plot_table(
    vega_spec_name="carey/new_chart",
    data_table=table,
    fields=fields,
)
```

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/custom_presets.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=dfbf9e99b8c25acc99fca47cc7121ae9" alt="Custom chart presets" max-width="90%" width="2946" height="728" data-path="images/app_ui/custom_presets.png" />
</Frame>

## Log data

You can log the following data types from your script and use them in a custom chart:

* **Config**: Initial settings of your experiment (your independent variables). This includes any named fields you've logged as keys to `wandb.Run.config` at the start of your training. For example: `wandb.Run.config.learning_rate = 0.0001`
* **Summary**: Single values logged during training (your results or dependent variables). For example, `wandb.Run.log({"val_acc" : 0.8})`. If you write to this key multiple times during training via `wandb.Run.log()`, the summary is set to the final value of that key.
* **History**: The full time series of the logged scalar is available to the query via the `history` field
* **summaryTable**: If you need to log a list of multiple values, use a `wandb.Table()` to save that data, then query it in your custom panel.
* **historyTable**: If you need to see the history data, then query `historyTable` in your custom chart panel. Each time you call `wandb.Table()` or log a custom chart, you're creating a new table in history for that step.

### How to log a custom table

Use `wandb.Table()` to log your data as a 2D array. Typically each row of this table represents one data point, and each column denotes the relevant fields/dimensions for each data point which you'd like to plot. As you configure a custom panel, the whole table will be accessible via the named key passed to `wandb.Run.log()`(`custom_data_table` below), and the individual fields will be accessible via the column names (`x`, `y`, and `z`). You can log tables at multiple time steps throughout your experiment. The maximum size of each table is 10,000 rows. [Try an example a Google Colab](https://tiny.cc/custom-charts).

```python  theme={null}
with wandb.init() as run:
  # Logging a custom table of data
  my_custom_data = [[x1, y1, z1], [x2, y2, z2]]
  run.log(
      {"custom_data_table": wandb.Table(data=my_custom_data, columns=["x", "y", "z"])}
  )
```

## Customize the chart

Add a new custom chart to get started, then edit the query to select data from your visible runs. The query uses [GraphQL](https://graphql.org) to fetch data from the config, summary, and history fields in your runs.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/customize_chart.gif?s=c8fc8cbb157811f23183339b301d7e2b" alt="Custom chart creation" max-width="90%" width="1942" height="1334" data-path="images/app_ui/customize_chart.gif" />
</Frame>

### Custom visualizations

Select a **Chart** in the upper right corner to start with a default preset. Next, select **Chart fields** to map the data you're pulling in from the query to the corresponding fields in your chart.

The following image shows an example on how to select a metric then mapping that into the bar chart fields below.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/demo_make_a_custom_chart_bar_chart.gif?s=80322f70da54341cfe2767f340290fc0" alt="Creating a custom bar chart" max-width="90%" width="2804" height="1588" data-path="images/app_ui/demo_make_a_custom_chart_bar_chart.gif" />
</Frame>

### How to edit Vega

Click **Edit** at the top of the panel to go into [Vega](https://vega.github.io/vega/) edit mode. Here you can define a [Vega specification](https://vega.github.io/vega/docs/specification/) that creates an interactive chart in the UI. You can change any aspect of the chart. For example, you can change the title, pick a different color scheme, show curves as a series of points instead of as connected lines. You can also make changes to the data itself, such as using a Vega transform to bin an array of values into a histogram. The panel preview will update interactively, so you can see the effect of your changes as you edit the Vega spec or query. Refer to the [Vega documentation and tutorials ](https://vega.github.io/vega/).

**Field references**

To pull data into your chart from W\&B, add template strings of the form `"${field:<field-name>}"` anywhere in your Vega spec. This will create a dropdown in the **Chart Fields** area on the right side, which users can use to select a query result column to map into Vega.

To set a default value for a field, use this syntax: `"${field:<field-name>:<placeholder text>}"`

### Saving chart presets

Apply any changes to a specific visualization panel with the button at the bottom of the modal. Alternatively, you can save the Vega spec to use elsewhere in your project. To save the reusable chart definition, click **Save as** at the top of the Vega editor and give your preset a name.

## Articles and guides

1. [The W\&B Machine Learning Visualization IDE](https://wandb.ai/wandb/posts/reports/The-W-B-Machine-Learning-Visualization-IDE--VmlldzoyNjk3Nzg)
2. [Visualizing NLP Attention Based Models](https://wandb.ai/kylegoyette/gradientsandtranslation2/reports/Visualizing-NLP-Attention-Based-Models-Using-Custom-Charts--VmlldzoyNjg2MjM)
3. [Visualizing The Effect of Attention on Gradient Flow](https://wandb.ai/kylegoyette/gradientsandtranslation/reports/Visualizing-The-Effect-of-Attention-on-Gradient-Flow-Using-Custom-Charts--VmlldzoyNjg1NDg)
4. [Logging arbitrary curves](https://wandb.ai/stacey/presets/reports/Logging-Arbitrary-Curves--VmlldzoyNzQyMzA)

## Common use cases

* Customize bar plots with error bars
* Show model validation metrics which require custom x-y coordinates (like precision-recall curves)
* Overlay data distributions from two different models/experiments as histograms
* Show changes in a metric via snapshots at multiple points during training
* Create a unique visualization not yet available in W\&B (and hopefully share it with the world)

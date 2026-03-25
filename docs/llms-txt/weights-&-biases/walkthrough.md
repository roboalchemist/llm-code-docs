# Source: https://docs.wandb.ai/models/sweeps/walkthrough.md

# Source: https://docs.wandb.ai/models/app/features/custom-charts/walkthrough.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Tutorial of using the custom charts feature in the W&B UI

# Tutorial: Use custom charts

Use custom charts to control the data you're loading in to a panel and its visualization.

## 1. Log data to W\&B

First, log data in your script. Use [wandb.Run.config](/models/track/config/) for single points set at the beginning of training, like hyperparameters. Use [wandb.Run.log()](/models/track/log/) for multiple points over time, and log custom 2D arrays with `wandb.Table()`. We recommend logging up to 10,000 data points per logged key.

```python  theme={null}
with wandb.init() as run: 

  # Logging a custom table of data
  my_custom_data = [[x1, y1, z1], [x2, y2, z2]]
  run.log(
    {"custom_data_table": wandb.Table(data=my_custom_data, columns=["x", "y", "z"])}
  )
```

[Try a quick example notebook](https://bit.ly/custom-charts-colab) to log the data tables, and in the next step we'll set up custom charts. See what the resulting charts look like in the [live report](https://app.wandb.ai/demo-team/custom-charts/reports/Custom-Charts--VmlldzoyMTk5MDc).

## 2. Create a query

Once you've logged data to visualize, go to your project page and click the **`+`** button to add a new panel, then select **Custom Chart**. You can follow along in the [custom charts demo workspace](https://app.wandb.ai/demo-team/custom-charts).

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/create_a_query.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=12a5238b280f7267a132aa9c28f03c9d" alt="Blank custom chart" width="2204" height="968" data-path="images/app_ui/create_a_query.png" />
</Frame>

### Add a query

1. Click `summary` and select `historyTable` to set up a new query pulling data from the run history.
2. Type in the key where you logged the `wandb.Table()`. In the code snippet above, it was `my_custom_table` . In the [example notebook](https://bit.ly/custom-charts-colab), the keys are `pr_curve` and `roc_curve`.

### Set Vega fields

Now that the query is loading in these columns, they're available as options to select in the Vega fields dropdown menus:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/UhAQoGpm-LvpH3-8/images/app_ui/set_vega_fields.png?fit=max&auto=format&n=UhAQoGpm-LvpH3-8&q=85&s=7361682df6416c191f77ac5288139963" alt="Pulling in columns from the query results to set Vega fields" width="2572" height="950" data-path="images/app_ui/set_vega_fields.png" />
</Frame>

* **x-axis:** runSets\_historyTable\_r (recall)
* **y-axis:** runSets\_historyTable\_p (precision)
* **color:** runSets\_historyTable\_c (class label)

## 3. Customize the chart

Now that looks pretty good, but I'd like to switch from a scatter plot to a line plot. Click **Edit** to change the Vega spec for this built in chart. Follow along in the [custom charts demo workspace](https://app.wandb.ai/demo-team/custom-charts).

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/88iR80mZ8tuFCZUU/images/general/custom-charts-1.png?fit=max&auto=format&n=88iR80mZ8tuFCZUU&q=85&s=697c5ba95464271ebf0fe599e71712c4" alt="Custom chart selection" width="416" height="67" data-path="images/general/custom-charts-1.png" />
</Frame>

I updated the Vega spec to customize the visualization:

* add titles for the plot, legend, x-axis, and y-axis (set “title” for each field)
* change the value of “mark” from “point” to “line”
* remove the unused “size” field

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/customize_vega_spec_for_pr_curve.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=3667d49e8bff3ae6b2bfbf45d2d68d4a" alt="PR curve Vega spec" width="2070" height="1244" data-path="images/app_ui/customize_vega_spec_for_pr_curve.png" />
</Frame>

To save this as a preset that you can use elsewhere in this project, click **Save as** at the top of the page. Here's what the result looks like, along with an ROC curve:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/88iR80mZ8tuFCZUU/images/general/custom-charts-2.png?fit=max&auto=format&n=88iR80mZ8tuFCZUU&q=85&s=be4c61d484b9fa0bb61611ca5bfb97a3" alt="PR curve chart" width="1114" height="422" data-path="images/general/custom-charts-2.png" />
</Frame>

## Bonus: composite histograms

Histograms can visualize numerical distributions to help us understand larger datasets. Composite histograms show multiple distributions across the same bins, letting us compare two or more metrics across different models or across different classes within our model. For a semantic segmentation model detecting objects in driving scenes, we might compare the effectiveness of optimizing for accuracy versus intersection over union (IOU), or we might want to know how well different models detect cars (large, common regions in the data) versus traffic signs (much smaller, less common regions). In the[ demo Colab](https://bit.ly/custom-charts-colab), you can compare the confidence scores for two of the ten classes of living things.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/composite_histograms.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=9f41a947f36a94db4d75aacc9cf4bdfd" alt="Composite histogram" width="1518" height="608" data-path="images/app_ui/composite_histograms.png" />
</Frame>

To create your own version of the custom composite histogram panel:

1. Create a new Custom Chart panel in your Workspace or Report (by adding a “Custom Chart” visualization). Hit the “Edit” button in the top right to modify the Vega spec starting from any built-in panel type.
2. Replace that built-in Vega spec with my [MVP code for a composite histogram in Vega](https://gist.github.com/staceysv/9bed36a2c0c2a427365991403611ce21). You can modify the main title, axis titles, input domain, and any other details directly in this Vega spec [using Vega syntax](https://vega.github.io/) (you could change the colors or even add a third histogram :)
3. Modify the query in the right hand side to load the correct data from your wandb logs. Add the field `summaryTable` and set the corresponding `tableKey` to `class_scores` to fetch the `wandb.Table` logged by your run. This will let you populate the two histogram bin sets (`red_bins` and `blue_bins`) via the dropdown menus with the columns of the `wandb.Table` logged as `class_scores`. For my example, I chose the `animal` class prediction scores for the red bins and `plant` for the blue bins.
4. You can keep making changes to the Vega spec and query until you’re happy with the plot you see in the preview rendering. Once you’re done, click **Save as** in the top and give your custom plot a name so you can reuse it. Then click **Apply from panel library** to finish your plot.

Here’s what my results look like from a very brief experiment: training on only 1000 examples for one epoch yields a model that’s very confident that most images are not plants and very uncertain about which images might be animals.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/88iR80mZ8tuFCZUU/images/general/custom-charts-3.png?fit=max&auto=format&n=88iR80mZ8tuFCZUU&q=85&s=d702517b0ff53a3579dcc131aeed3794" alt="Chart configuration" width="1646" height="600" data-path="images/general/custom-charts-3.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/88iR80mZ8tuFCZUU/images/general/custom-charts-4.png?fit=max&auto=format&n=88iR80mZ8tuFCZUU&q=85&s=986352cb4140f0fd344332901449aa5f" alt="Chart result" width="1358" height="1274" data-path="images/general/custom-charts-4.png" />
</Frame>

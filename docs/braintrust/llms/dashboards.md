# Source: https://braintrust.dev/docs/observe/dashboards.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitor with dashboards

> Visualize metrics and trends across logs and experiments

The <Icon icon="chart-no-axes-column" /> **Monitor** page provides custom dashboards that aggregate metrics across logs and experiments in your project. Track request counts, latency, token usage, costs, scores, and custom metrics over time.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=4c4b117a23bf49845bd74197c4429dce" alt="Monitor page" data-og-width="3138" width="3138" data-og-height="1372" height="1372" data-path="images/guides/monitor/monitor-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=83d842d1748e3b426226f1413cb2d3f6 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=4601a72cdc69c776a8a3440c87c2848f 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=064fd20702529c4d00cb6d1b15edeee0 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=aa25a846492a840b4740375f4109d6ba 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=d432626a514d2961a15b7d639192da7d 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-overview.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=992db3d4cb5bc1049cb1962464b1c778 2500w" />

## Filter and group data

Apply filters and groupings at the top of the page to affect all charts. This lets you focus on specific subsets of your data or compare different segments side by side.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-filter-group.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=eb5fee0899516fb798f0ccd75a4381d2" alt="Monitor page" data-og-width="1442" width="1442" data-og-height="154" height="154" data-path="images/guides/monitor/monitor-filter-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-filter-group.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=48b0f0733d171606e79bd0e85d01ca9e 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-filter-group.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=06591e1ab47b2f3e5a162b05c2f5323a 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-filter-group.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a7d9147da6cacd3926b3233dfa78ea3b 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-filter-group.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=ece1614e2e651612feeeeecddd127fa9 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-filter-group.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=4191cc56c464777b1eba9ec276b060d2 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-filter-group.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=042c3ccad61e84a5108d0136ddac306b 2500w" />

## Create custom charts

Select **+Chart** to open the chart editor, or select the pencil icon next to any chart title. [Measures](https://www.braintrust.dev/docs/reference/sql#group-by-with-aggregations) and [filters](https://www.braintrust.dev/docs/reference/sql#where) correspond to SQL options. The "group by" option is a SQL dimension.

### Time series

Visualize data over time with lines or stacked bars. Time series charts help you spot trends, anomalies, and correlations.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=3501bf16d5c08ef0fd488a9f6a878304" alt="Monitor page" data-og-width="2458" width="2458" data-og-height="1598" height="1598" data-path="images/guides/monitor/monitor-custom-chart-editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=d3c4c860dbd052680e153e824ffd50b0 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=081b9d2bfb8b63c10889cbef6d6bd6b9 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=cd6d6e71ef94fe70427ff26b8db5fa75 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=6b28324ae0d55d755d33bdb0562457d7 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=f5336b8d9d8a0469f97814931f2ae052 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=89be9d68d3287ea166f1bf64df45cb47 2500w" />

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-2.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=271c946045d98ab9d8238da7a05d088e" alt="Monitor page" data-og-width="2386" width="2386" data-og-height="1560" height="1560" data-path="images/guides/monitor/monitor-custom-chart-editor-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-2.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a929c0516507efd093282b9d7caa0653 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-2.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=bab822600afa0f602193c2400eaaaba0 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-2.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=5500b2dfb4804f5d97632d15c5aac4d0 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-2.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=918f16d404522e1cba2032a4bb352fd4 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-2.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=802e90fc81c35f4359cbd0a836946db3 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-2.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2e215ff9a20ee87ec3d98b2216fbe166 2500w" />

### Top list

Show values of multiple groups over the entire timeframe. Order by value or alphabetically (ascending or descending).

<div style={{maxWidth: '600px'}}>
    <img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-top-list.jpg?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=9d2676087b3667ddc71ee231415c6e38" alt="Monitor page" data-og-width="964" width="964" data-og-height="708" height="708" data-path="images/guides/monitor/monitor-custom-chart-top-list.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-top-list.jpg?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=31d155a459176cad068014f741821091 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-top-list.jpg?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=f3294bd4dd98f076382d67a643263b42 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-top-list.jpg?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=e2b050c93f9aa92ac1c46c5f1f93ecbc 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-top-list.jpg?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=b43bd63558a9427fe8b4d4ce533dc8f6 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-top-list.jpg?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=1e71659c5ab25205fc884b2457065b0e 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-top-list.jpg?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=00d671235e12cf8fa819d8c03711bcd3 2500w" />
</div>

### Big number

Display a single aggregate value as one large number. Useful for highlighting key metrics like total requests or average score.

<div style={{maxWidth: '600px'}}>
    <img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-big-number.jpg?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=9cde51ff57b4a6c5cf4a94ef9efb3e05" alt="Monitor page" data-og-width="820" width="820" data-og-height="698" height="698" data-path="images/guides/monitor/monitor-custom-chart-big-number.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-big-number.jpg?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=1c36b07cf05528b69ce281f07f1e9030 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-big-number.jpg?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=cb0abf52484f5e9391c1c6831f351a78 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-big-number.jpg?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=ee85e81d8975e002fdbb35d19b5e71e6 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-big-number.jpg?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=41ed0dd859086fe0b37f6498ffe44569 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-big-number.jpg?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=561eb6741b20cf9b355d8a2735212547 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-big-number.jpg?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=cdc23d5c6ca1f4a0d507a4b9a11e1308 2500w" />
</div>

### Presets

Preset charts are included by default on the **Monitor** page, covering common metrics like request count, latency, token usage, and scores.

<div style={{maxWidth: '600px'}}>
    <img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-presets.jpg?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=f7a2cd43f4ac4b0c44b97ec783acacc3" alt="Monitor page" data-og-width="966" width="966" data-og-height="586" height="586" data-path="images/guides/monitor/monitor-custom-chart-editor-presets.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-presets.jpg?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=eefa2e6ec833c73ef35586a2d006d214 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-presets.jpg?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=ef1124e3990fdb0370bee43c7430dd25 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-presets.jpg?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=b1df0eaf487f8230bc643be8d5806796 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-presets.jpg?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=67b863989fce9a005a3f6b5910771aa6 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-presets.jpg?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2243ab45ac885a0b2eb1cf7874442602 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-custom-chart-editor-presets.jpg?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=8c749ebaede2ef7611b05a8f2f79a4e7 2500w" />
</div>

## Select timeframes

Choose from preset timeframes or click and drag horizontally on time series charts to zoom into a specific period. Double-click to zoom out.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-timeframe.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=d11a7a6d7173000c85bba30c80ac6468" alt="Monitor page" data-og-width="604" width="604" data-og-height="728" height="728" data-path="images/guides/monitor/monitor-timeframe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-timeframe.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=db3c706c8adb515206362e7d3800d5b6 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-timeframe.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=cd2b0012a4ef2235475ce3d2fa0faf57 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-timeframe.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=37a1b1f1c753ddabdd32f5ac222c061d 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-timeframe.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2763f578113c765f614e120707a1cd84 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-timeframe.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=c61775460a64d19a245cebac8ee99d28 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/monitor/monitor-timeframe.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=71a7b814fecc1d7366382046ab09955a 2500w" />

## View traces

Select any data point on a chart to navigate to the logs or experiments page, filtered to the corresponding time range and series. This lets you quickly investigate specific data points.

## Create custom dashboards

The default view shows all data for your project. To create a custom dashboard:

1. Add or edit any chart - you'll be prompted to create a new view before saving
2. Use the dropdown in the top left to duplicate the current view and save as a new dashboard

## Unit types

Charts display values with appropriate unit formatting:

* **Duration**: Seconds (e.g., "1.5s", "0.3s")
* **Cost**: US dollars (e.g., "$0.05", "$1.23")
* **Percent**: Percentages (e.g., "75%", "100%")
* **Bytes**: Binary byte units using base-1024 (e.g., "1 KB", "2 GB", "500 B")
* **Count**: Generic countable things (e.g., "1,234", "5.5")

The unit type affects how values appear in chart axes, tooltips, and legends.

## Next steps

* [Use the Loop](/observe/loop) to ask questions about your data
* [Score online](/observe/score-online) to add quality metrics to dashboards
* [Build datasets](/annotate/datasets) from patterns you identify
* Read the [SQL reference](/reference/sql) for advanced queries

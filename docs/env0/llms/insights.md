# Source: https://docs.envzero.com/guides/cloud-analyst/cloud-analyst/insights.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Insights

> Create and view single-chart insights for key infrastructure trends in env zero Cloud Analyst

Cloud Analyst Insights provide quick, focused answers to specific questions through single-chart visualizations.

Each Insight is designed to highlight key trends, usage patterns, or performance metrics, giving users immediate clarity on important topics.

## Predefined Insights

env zero provides multiple predefined out of the box insights that answer common questions, you can see those in the Insights table, they will be marked with a verified icon.

## Create Your Own

Create your own insights by using the AI Chat Interface and hitting "Save" to save the results as an Insight, or by Create New Insight button on the Insights table.

<img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/cloud-analyst/cloud-analyst/baa55c69b7da567b9572f6642eb8e7bfa23872e430c5408011e998bac9cea704-image.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=4e88a5bd213e976ef582cb91602a794f" alt="" width="670" height="502" data-path="images/guides/cloud-analyst/cloud-analyst/baa55c69b7da567b9572f6642eb8e7bfa23872e430c5408011e998bac9cea704-image.png" />

## Editing

When Editing an insight, you can use the data search to directly specify fields, aggregations, filters and more in order to build your visualizations.

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-analyst/cloud-analyst/e21d5f1d2ebca15d3f7f06780badecdd4ac22231c8326374aa738146a46caa22-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=edaa320ec116fc59fe20abd6cdd66e77" alt="" width="1408" height="755" data-path="images/guides/cloud-analyst/cloud-analyst/e21d5f1d2ebca15d3f7f06780badecdd4ac22231c8326374aa738146a46caa22-image.png" />

### The Search Bar

The search bar allows an easy way to build your query. It is based on a list of keywords. Here are some keywords that can be used:

* **Fields**: Search the the field name you are interested in seeing such as "Environment Name". The fields are also visible on the left panel, and you can select them from there.
* **Filters**: You can add filters in different ways, such as `Environment Name=X`, or keywords like `Top 5` or `Bottom 10` to limit the results.
* **Grouping**: Add keywords like `by Environment Type` to group by certain attributes
* **Aggregation**: Add keywords like `count`/`sum`/`max` before attributes to count and aggregate measures
* **Sorting**: Add keywords like `sort by` to control the order

<img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/cloud-analyst/cloud-analyst/d8c94480ca3e6dc12db01a2effdd422d108479167b47f36810aa447e892568a6-image.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=d81a4524752ffceef0ea5c4129c663d8" alt="" width="964" height="147" data-path="images/guides/cloud-analyst/cloud-analyst/d8c94480ca3e6dc12db01a2effdd422d108479167b47f36810aa447e892568a6-image.png" />

### Insight Settings

On the right panel, there are several options to help you customize the chart to your needs:

* **Chart Library** - Select the visualization that best serves your needs from a variety of over 20 options
* **Chart Configuration** - Configure the chart by setting up labels, assign fields to axis, and more.
* **Query Details** - See a breakdown of the full query details, to make sure it behaves as you expect.
* To view the data in a tabular format click on the `View Table` icon at the top

<img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/cloud-analyst/cloud-analyst/44e39695081edb8a4695685d0c207a6bff48ab820ea0960dc73b14e1dbc44fb2-image.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=35db5b98cb3985b8c96cbe85cd082e5e" alt="" width="318" height="566" data-path="images/guides/cloud-analyst/cloud-analyst/44e39695081edb8a4695685d0c207a6bff48ab820ea0960dc73b14e1dbc44fb2-image.png" />

### Fields, Formulas and Parameters

On the left panel you can see the full list of fields available in the env zero data model. You can select any field to construct your query, as well as use them along with filters or aggregations, as described above.

If you need to create a complex calculation, you can use **Formulas**.

<img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/cloud-analyst/cloud-analyst/282e3d9dc372e3aaeae5288b0cae0d178b984087ab9a70fe9f2f963b4df6c773-image.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=c7d37455ff5300c704cecec568820378" alt="" width="1027" height="546" data-path="images/guides/cloud-analyst/cloud-analyst/282e3d9dc372e3aaeae5288b0cae0d178b984087ab9a70fe9f2f963b4df6c773-image.png" />

Formulas contain large number of functions that can be used while referencing attributes and measures from the env zero model. The functions along with their explanations are available in the formula editor.

Built with [Mintlify](https://mintlify.com).

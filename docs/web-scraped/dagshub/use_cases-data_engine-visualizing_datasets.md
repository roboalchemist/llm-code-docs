# Source: https://dagshub.com/docs/use_cases/data_engine/visualizing_datasets/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/use_cases/data_engine/visualizing_datasets.md "Edit this page")

# Visualizing your data[¶](#visualizing-your-data "Permanent link")

Data Engine provides an easy way to visualize data points and their enrichments. By displaying data with enrichments such as annotations, predictions, and metadata - you can quickly:

- See your data points & better understand your datasets
- Discover use cases, in which your model is underperforming
- Create a new dataset out of it using visual filters
- Send your data for annotation or re-annotation

This way you can make sense of the datasets youâ€™re using to train and improve your model.

DagsHub\'s Dataset Viewer allows you to visualize datasources, datasets, as well as individual queries. You can select the metadata you\'d like to view. It can also overlay annotations for columns in the Label Studio format!

To visualize a query while working with the python client, you can run the following command:

    # Query datasource
    query = ds["annotation"].is_null()  # query of your choice

    # Visualize the quried datasource
    query.visualize(visualizer="dagshub")

This should return a link, which you can follow to explore the query directly within the DagsHub UI.

To visualize queries using just the DagsHub UI, follow the documentation under [query and create subsets](../query_and_create_subsets/#2-using-the-web-ui) to utilize the web query builder.

## Save query results as a dataset[¶](#save-query-results-as-a-dataset "Permanent link")

Once you explore a dataset, you may want to filter out subsets to work with further (e.g. retraining with upweighted loss). Doing so with the DagsHub Dataset Viewer is easy!

For example: in the [sawit dataset project](https://dagshub.com/jinensetpal/sawit/), some data is annotated using a vision model. This is generally less reliable than human annotators. I can filter them out by checking if the annotator field is equal to \'human\':

[![filtered-data](../assets/visualizing_datasets/filtered-data.png)](../assets/visualizing_datasets/filtered-data.png)

Next, I can save this query as a dataset, giving it an appropriate name:

[![save-dataset](../assets/visualizing_datasets/save-dataset.png)](../assets/visualizing_datasets/save-dataset.png)

Once you do the same for your project, use the `get_datasets()` command or navigate to your repository and check the datasets tab to see your new dataset.

## Edit metadata[¶](#edit-metadata "Permanent link")

Metadata can be edited both through the UI, or the python client. To start, select the datapoint you\'d like to update:

[![single-datapoint](../assets/visualizing_datasets/single-datapoint.png)](../assets/visualizing_datasets/single-datapoint.png)

To the left, you see a visualization of this datapoint. To the right, we have the metadata. We can add metadata by updating and adding new fields.

You can add a new field by entering in the field name, setting the type and assigning a value:

[![edit-metadata](../assets/visualizing_datasets/edit-metadata.png)](../assets/visualizing_datasets/edit-metadata.png)

To update metadata for a large set of datapoints, it is recommended to follow our documentation on [enriching metadata using the client API](../enrich_datasource/).

## Display Options[¶](#display-options "Permanent link")

From the bar above your datapoints, you can also select Display Options. Hereâ€™s what they all do:

1.  Show labels: Whether or not the labels from LabelStudio should be overlaid over datapoint.

2.  Show bounding boxes: Whether or not the bounding boxes from LabelStudio should be overlaid over each datapoint.

3.  Show filenames: Whether or not filenames should overlay over each datapoint.

4.  Show keypoint indices: Shows the keypoints traced during semantic segmentation.

5.  Color annotations by:

    - Field: The color is set to the annotation column - different columns have different colors.
    - Class: The color is set against the union of all labels in the annotation columns.
    - Instance: The color is set by the instance of annotation (the first, second, etc., instances. Annotations are colored left-to-right from the available colors).

[![Display Options](../assets/visualizing_datasets/display_options.png)](../assets/visualizing_datasets/display_options.png)

## Annotate your data or create a dataloader for training[¶](#annotate-your-data-or-create-a-dataloader-for-training "Permanent link")

You can also use DagsHub to [annotate your datasets](../../annotation/) or to [convert it to a dataloader](../train_model/) for training or evaluation.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).
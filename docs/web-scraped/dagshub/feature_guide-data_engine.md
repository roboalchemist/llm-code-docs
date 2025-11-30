# Source: https://dagshub.com/docs/feature_guide/data_engine/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/feature_guide/data_engine.md "Edit this page")

# Data Engine[¶](#data-engine "Permanent link")

# An error occurred. 

Unable to execute JavaScript.

Data Engine is a toolset built to make iterating on unstructured datasets easy by providing a seamless flow to [create training ready datasets](../../use_cases/data_engine/). The flow includes:

- Collecting data from different sources and enriching it with custom metadata, annotations, and predictions
- Querying your data to easily create subsets for different use cases
- Visualizing your datasets to analyze and understand your data
- Annotating relevant data points
- Generating training-ready datasets to retrain your model on
- Tracking your dataset & model lineage

[![Data Engine Flow Chart](../assets/data_engine/data_engine_flow_chart.png)](../assets/data_engine/data_engine_flow_chart.png)

## Data Engine Architecture[¶](#data-engine-architecture "Permanent link")

Data Engine includes a few important components covered below:

### Enrichments[¶](#enrichments "Permanent link")

Data Engine works with your data and enrichments. Enrichments are metadata fields that include extra information about a data file, like its size, location, from which customer the data was received, and other details. They can also include annotations and predictions made by models.

Data Engine supports almost any enrichment type, including numbers, strings, and booleans, but also arbitrary binary data, so you can add custom annotation formats, images, or pickle files as enrichments too. This means you can associate the metadata you need with your data, without worrying youâ€™ll need to manage it in a custom way for each unique column. It just works. Enrichments are all attached to their corresponding data points which live inside a data source.

In addition to enrichments, there are three main classes that are used to query, visualize, annotate, and regenerate data.

### Datasource [show source](https://dagshub.com/docs/client/reference/data_engine/datasource.html)[¶](#datasource-show-source "Permanent link")

The top-level class of the Data Engine represents the source of the data points. It contains the data points and their enrichments. Datasources are queryable, meaning you can filter them to create subsets. When you run a query on a datasource, e.g. `q = ds['size'] < 5` the returned object is another datasource. You can also add the enrichments mentioned above. After a Datasource is queried, you can save it as a dataset.

### QueryResult [show source](https://dagshub.com/docs/client/reference/data_engine/query_result.html)[¶](#queryresult-show-source "Permanent link")

When youâ€™ve set up your datasource and filters, you can get the appropriately filtered datapoints using `all()` which returns all datapoints, or `head()` which returns a sample of datapoints (100 by default). When you run `q.all()` or `q.head()` the returned object is a QueryResult. You can use it to transform the results into a dataframe, [visualize them](../../use_cases/data_engine/visualizing_datasets/) , [convert them to a dataloader](../../use_cases/data_engine/train_model/), or download the relevant files locally.

### Datapoint [show source](https://dagshub.com/docs/client/reference/data_engine/datapoint.html)[¶](#datapoint-show-source "Permanent link")

Represents a single data file and its associated enrichments. Data points can be downloaded individually, and their metadata can be accessed similar to a `dict`.

Here is a simple example on creating a dataframe from a datasource:

    from dagshub.data_engine import datasources

    # Create a datasource from the 'dataset/' folder in a repo it
    ds = datasources.create_from_repo(repo="<repo_owner>/<repo_name>", name="my-dataset", path="dataset")

    # Get the first 100 datapoints
    query_res = ds.head()

    # Create a pandas data frame from the query results
    df = query_res.dataframe
    print(df)

## Next Steps[¶](#next-steps "Permanent link")

Take your next steps with Data Engine by learning how to [create training ready datasets](../../use_cases/data_engine/) with Data Engine.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).
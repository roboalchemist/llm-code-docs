# Source: https://dagshub.com/docs/use_cases/data_engine/version_datasets/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/use_cases/data_engine/version_datasets.md "Edit this page")

# Version Datasets (with Data Engine)[¶](#version-datasets-with-data-engine "Permanent link")

Most datasets in the real world are add-only. Data is added to the dataset, and enrichments, like metadata, annotations and predictions change, but actual file contents remain the same. The best way to manage those changes and version them is with DagsHub Data Engine.

To do this, we need to upload our data to DagsHub, and create a datasource from it in Data Engine. Then, using Data Engine\'s [version query syntax](../query_and_create_subsets/#versioning-filters), we can easily revert to the dataset state at any point in time.

## Uploading The First Dataset Version to DagsHub[¶](#uploading-the-first-dataset-version-to-dagshub "Permanent link")

DagsHub supports a few different ways to upload or connect data to our platform. Choose the best approach for you:

1.  **When your data files are local** or if you\'d like to host your data on DagsHub directly â€" [Upload your data files to DagsHub Storage](../../../quick_start/upload_data/).
2.  **When your data files are already in cloud storage** â€" DagsHub supports a variety of [external storage integrations](../../../integration_guide/set_up_remote_storage_for_data_and_models/). If your data is already in one of these storage buckets, you can simply [connect it to DagsHub](../../../quick_start/connect_external_storage/)
3.  **When file contents also change** â€" If your data files also change, read the guide on [versioning data files](../../../quick_start/version_data/). Then come back to this guide to learn how to version metadata on top of your uploaded DVC versions.

Let\'s assume we\'ve uploaded a dataset of 50 files to our connected storage bucket with [option 1](../../../quick_start/upload_data/) into a folder named `data/`.

This is how the bucket storage looks like now: [![Bucket storage after first upload](../assets/version_datasets/first_data_version.jpeg)](../assets/version_datasets/first_data_version.jpeg)

## Creating a datasource to generate the first version of our dataset[¶](#creating-a-datasource-to-generate-the-first-version-of-our-dataset "Permanent link")

Now that our data is in our DagsHub repository, we can create a datasource from it.

To create a datasource in the UI:

1.  Click on the \"Datasets\" tab
2.  Select \"Add new source\" and \"Choose from existing data\...\"
3.  Select the data folder inside the connected bucket
4.  Give it a name you like.
5.  DagsHub scans your folder and creates a \"table representing your dataset\"

~Datasource\ Creation~

To create a datasource in Python:

    from dagshub.data_engine import datasources
    datasources.create_datasource(repo="<repo_owner>/<repo_name>", name="my-first-datasource", path="s3://<repo_name>/data")

You can [add any custom enrichments](../enrich_datasource/) to your datasource, including metadata, annotations, and predictions. Each change is logged, and you\'ll be able to revert to an older version at any time.

## Adding more data to the dataset.[¶](#adding-more-data-to-the-dataset "Permanent link") 

Now that we have our dataset with V1, lets add 50 more datapoints to it, for V2.

To do that, put your new data files in your local data folder, then run the following code:

    dagshub upload --bucket <repo_owner>/<repo_name> "data/" "data/"

Note

If you connected your external storage, simply add the new files there, or if you used DVC to upload versioned data files, repeat that step with the new data files.

Now, if we refresh the page on DagsHub, we\'ll see the new files were added to the folder.

## Updating the datasource and creating a new version[¶](#updating-the-datasource-and-creating-a-new-version "Permanent link")

To update our datasource, we can either click the rescan button in the UI:

[![Datasource Rescan](../assets/version_datasets/rescan_datasource.jpeg)](../assets/version_datasets/rescan_datasource.jpeg)

Or use the Python command:

    ds = datasources.get('<repo_owner>/<repo_name>', 'my-first-datasource')
    ds.scan_source()

If we visualize the datasource in the UI, we\'ll see the new data files.

So where\'s the new version?

## Returning to old versions and states of our datasource[¶](#returning-to-old-versions-and-states-of-our-datasource "Permanent link")

DagsHub Data Engine keeps a log of all states and changes to your datasource metadata, and provides a simple way to return to old versions. It has a lot more capabilities, which you can read about in the full [versioning query syntax](https://dagshub.com/docs/client/reference/data_engine/datasource.html#dagshub.data_engine.model.datasource.Datasource.as_of)

The simplest syntax is the global `as_of(t)` query. Let\'s see how we can get 2 versions of our datasource easily:

    from datetime import *
    t_now = datetime.now()
    v2 = ds.as_of(t_now)
    v2.all() # Output: QueryResult of datasource my-first-datasource with 100 datapoint(s)

Since I create the new version 10 minutes ago, if I go back in time 15 minutes, I\'ll get my old version:

    t_prev = datetime.now() - timedelta(minutes=15)
    v1 = ds.as_of(t_prev)
    v1.all() # Output: QueryResult of datasource my-first-datasource with 50 datapoint(s)

In practice, you\'ll be able to get your experiment\'s start time, then use that to retrieve your dataset state at that time.

This versioning works for any metadata change, including, for example, if you update your annotation versions and want to revert to an older version of annotations. Data Engine also offers an easy way to compare different versions of the same metadata column using our `select()` combined with `as_of()` functionality. [Read more about that here](../query_and_create_subsets/#query-select-with-previous-versions).

## Next Steps[¶](#next-steps "Permanent link")

Now that you\'ve started managing your dataset versions, learn how to [enrich them with your custom metadata](../enrich_datasource/), [visualize them](../visualizing_datasets/), [annotate them](../../annotation/) or [convert them to dataloaders for training](../train_model/).

You can also continue to learn how to [track your experiments on DagsHub](../../track_ml_experiments/).

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).
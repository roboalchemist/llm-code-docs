# Source: https://dagshub.com/docs/use_cases/data_engine/enrich_datasource/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/use_cases/data_engine/enrich_datasource.md "Edit this page")

# Enriching your data and using it[¶](#enriching-your-data-and-using-it "Permanent link")

In order to improve a model you need to train it on the most relevant data points - the ones that represent use cases in which the model is underperforming. Focusing on these relevant use cases is a hard task, especially when dealing with large datasets. This is why Data Engine provides the ability to intuitively query and create new subsets of your data, so you will be able to zoom in on these use cases and improve your model effectively.

To query and generate training-ready data sets from your connected data source, you will first need to enrich it by adding custom metadata thatâ€™s relevant to your use case. Data Engine enrichments can include metadata, annotations, and model predictions. There are 3 ways to upload enrichments using the DagsHub Client:

1.  [The Pandas Dataframe interface](#1-enriching-with-pandas-dataframe-interface)
2.  [The metadata context interface](#2-enriching-with-metadata-context-interface)
3.  [Dictionary assignments on datapoints](#3-enriching-with-with-dictionary-like-assignment)

## 1. Enriching with Pandas Dataframe interface[¶](#1-enriching-with-pandas-dataframe-interface "Permanent link") 

To enrich datasource with an existing data frame, use the following command:

    ds.upload_metadata_from_dataframe(dataFrame, path_column="path")

`path_column` supports either an index or the name of the column, which specifies the path of the data file you want to attach metadata to. If not specified, the first dataframe column will be assumed by default. All other columns in the data frame are considered as metadata columns.

For example:

    # Create a pandas dataframe
    columns = ["path", "squirrel_detected"]
    data = [["data/dataPoint1.png", True],
            ["data/dataPoint2.png", False]]

    df = pd.DataFrame(data, columns=columns)

    # Enriching data with the data frame
    ds.upload_metadata_from_dataframe(df, path_column="path")

## 2. Enriching with metadata context interface[¶](#2-enriching-with-metadata-context-interface "Permanent link") 

To Enrich your data source with the metadata context interface, you can use the `metadata_context` with the following commands:

    with ds.metadata_context() as ctx:
        metadata = 

        # To add enrichments to a single data point within the data source:
        ctx.update_metadata("path/to/datapoint.png", metadata)

        # To add enrichments to several data points within the data source:
        ctx.update_metadata(["path/to/datapoint1.png", "path/to/datapoint2.png"], metadata)

Where `path/to/datapoint*.png` is the path relative to the root of the datasource.

For example, for our [baby Yoda segmentation repo](https://dagshub.com/Simon/baby-yoda-segmentation-dataset):

    with ds.metadata_context() as metadata_context:
        metadata = 

        # Enriching one data point
        metadata_context.update_metadata("images/005.jpg", metadata)

        # Enriching several data points 
        metadata_context.update_metadata(["images/006.jpg", "images/007.jpg"], metadata)

In our baby Yoda segmentation repository - where the data is located at `repo://simon/baby-yoda-segmentor/data` - the data point path will be `images/005.jpg`

## 3. Enriching with with dictionary-like assignment[¶](#3-enriching-with-with-dictionary-like-assignment "Permanent link") 

    datapoints = ds.all()
    datapoints["images/005.jpg"]["episode"] = 5
    datapoints["images/005.jpg"].save()

`save()` should be called for each datapoint eventually for changes to be commited.

when looping over many datapoints the preferred method (to avoid many network writes) is to work within a metadata context block, but dictionary syntax can still be used:

    with ds.metadata_context() as ctx:
        for dp in datapoints:
            dp["episode"] = 4

note that in the above example `save()` is omitted as a commit is done once the context is exited.

**Supported metadata types:**

- Int
- Float
- Boolean
- String
- Blobs (`bytes`):

  ::: highlight
      with ds.metadata_context() as ctx:
          with open("file1_depth.png", "rb") as f:
              ctx.update_metadata("file1", )
  :::
- Datetimes (we\'re also saving the timezone. If it\'s not provided, then we assume UTC):

  ::: highlight
      import datetime
      # +3 Hours UTC Offset
      tz = datetime.timezone(datetime.timedelta(hours=3))     
      # 10th February 2024, 14:00 + 03:00
      dt = datetime.datetime(2024, 2, 10, 14, 0, 0, tzinfo=tz)

      with ds.metadata_context() as ctx:
          ctx.update_metadata("file1", )
  :::

## 4. Import metadata from CSV, TSV, or Parquet in the UI[¶](#4-import-metadata-from-csv-tsv-or-parquet-in-the-ui "Permanent link") 

Using DagsHub\'s UI, you can easily add metadata to your data points. Follow these steps to upload metadata:

In the data source page, look for the vertical three dots icon on the right side of the top navigation bar (see image below):

[![Accessing Metadata Options](../assets/enrich_datasource/enrich-data-from-ui-1.png)](../assets/enrich_datasource/enrich-data-from-ui-1.png)

Click the three dots, and a pop-up menu will appear. Select the option to upload a file containing your metadata:

[![Uploading Metadata](../assets/enrich_datasource/enrich-data-from-ui-2.png)](../assets/enrich_datasource/enrich-data-from-ui-2.png)

Choose a file to upload. The file should be a CSV in the following format:

    path,metadata1,metadata2
    path/to/datapoint1.png,value1,value2

Here, path points to each data point, and additional columns represent metadata values.

Note: We also support parquet files and CSV files compressed in a zip archive.

Once your file is selected, click the \"Upload\" button. You will get notified when the metadata is uploaded successfully.

## Deleting datapoints and metadata[¶](#deleting-datapoints-and-metadata "Permanent link")

To delete a datapoint from a datasource, simply run:

    datapoints["images/005.jpg"].delete()

Or, delete a list of datapoints from a datasource:

    datapoints = ds.all()
    ds.delete_datapoints(datapoints)

Note

1.  Deleted datapoints will no longer show up in queries.
2.  Does not delete the datapoint\'s file, only removing the data from the datasource.
3.  You can still query deleted datapoints and associated metadata with versioned queries whose time is before deletion time.
4.  You can re-add deleted datapoints to the datasource.
5.  Datasource scanning will *not* add this datapoint back.

Delete one or more metadata fields from a datapoint:

    datapoints["images/005.jpg"].delete_metadata("episode")
    # or
    datapoints["images/005.jpg"].delete_metadata(["episode", "annotation"])

Or, delete fields at the source level, from multiple datapoints:

    datapoints = ds.all()
    ds.delete_metadata_from_datapoints(datapoints, ["episode", "annotation"])

Note

Deleted values can be accessed using versioned query with time set before the deletion.

## Viewing and using datasource content[¶](#viewing-and-using-datasource-content "Permanent link")

The easiest way to display your datapoints is `ds.head().dataframe` or `ds.all().dataframe`, though you can leave out the `.dataframe` to get the actual QueryResult object.

You can fetch the data points (set of filenames + their enrichments) that exist in a data source. To display data points within a datasource, use the following commands:

    # Fetch the first 100 data points 
    ds.head()

    # Fetch the first 42 data points 
    ds.head(42)

    # Fetch all data points
    ds.all()

The returned object will include the fetched datapoints and their metadata.

If you want to do sophisticated computations, aggregations, etc. on the fetched metadata, you can easily do that by transforming the fetched datapoints to a Pandas DataFrame. Each row will represent a datapoint, with one column specifying its file path and the other columns showing its metadata values.

    df = ds.head().dataframe

### Downloading datapoint files[¶](#downloading-datapoint-files "Permanent link")

To download the raw data files referenced in the `path` field of the fetched query results, use the download_files function:

    ds.all().download_files(target_directory="path/to/directory")

If target_directory is not specified, data points will be downloaded to the `~/dagshub/datasets/<user>/<repo>/<datasource_id>` directory.

If you have another column that includes valid paths inside youâ€™re repository, for example if you have images that you use as labels, and are also stored in your project, you can download them using:

    ds.all().download_files(target_directory="path/to/directory", path_field="label_path")

Where `path_field` is the name of the column that has the paths youâ€™d like to download.

### Download files directly from your storage bucket[¶](#download-files-directly-from-your-storage-bucket "Permanent link")

If your data source is a cloud object storage bucket, which you connected to DagsHub, then you can download raw data files directly from your bucket. This can lead to massive savings of time and data transfer costs, so we recommend doing that. Use the following example to enable bucket downloaders:

    from dagshub.common.download import enable_s3_bucket_downloader, enable_gcs_bucket_downloader

    # S3
    enable_s3_bucket_downloader()
    # GCS
    enable_gcs_bucket_downloader()

    # You can also use a custom client, if the default auth is not set up
    import boto3

    client = boto3.client("s3", endpoint_url=...)
    enable_s3_bucket_downloader(client)

For this to work, you need to be authenticated with your cloud provider and have proper permissions. Usually, that means downloading the appropriate cloud vendor SDK (`aws` or `gcloud`). If you donâ€™t use bucket downloaders, everything will still work - you will download the raw files from dagshub.com using your DagsHub credentials.

### Downloading Blob fields[¶](#downloading-blob-fields "Permanent link")

Blob fields are not downloaded by default, to download the data, use the following function:

    df = ds.all().get_blob_fields(âbinary_1â, âbinary_2â, load_into_memory = True)

### Working with Annotation Columns[¶](#working-with-annotation-columns "Permanent link")

Data Engine treats certain data types, like annotations uniquely, enabling you to [send them to be annotated](../../annotation/), or [visualize](../visualizing_datasets/) them.

If you created the annotation with [DagsHub Annotations](../../../feature_guide/annotations/), then this will be automatically taken care of.

However, if you import annotations from a different place, and convert them into the correct label studio format, you\'ll need to mark them as metadata type annotation. To do this simply run:

    from dagshub.data_engine import datasources
    ds = datasources.get('<user_name>/<repo_name>', '<datasource_name>')

    ds.metadata_field("<your annotation column name>").set_annotation().apply()

Then you\'ll be able to see and use the annotations as necessary.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).
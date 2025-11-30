# Source: https://dagshub.com/docs/use_cases/annotation/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/use_cases/annotation.md "Edit this page")

# Annotate Datasets[¶](#annotate-datasets "Permanent link")

DagsHub provides an easy way to annotate your datasets, via [DagsHub Annotations](../../feature_guide/annotations/) (based on the [Label Studio Integration](../../integration_guide/label_studio/)).

<figure>
<a href="../assets/annotation/annotate.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/annotation/annotate.png" alt="DagsHub Annotations UI" /></a>
<figcaption>DagsHub Annotations UI for NER</figcaption>
</figure>

Annotations are also integrated into [Data Engine](../../feature_guide/data_engine/), providing an easy way to annotate data and generate high-quality datasets for training.

Let\'s see how you can easily annotate your datasets and visualize the annotations, and use them to train a model with DagsHub. For the full annotation features, see the [feature page](../../feature_guide/annotations/).

DagsHub annotations are free for public projects, and part of the [Team Tier](https://dagshub.com/pricing) for private projects.

## Uploading or connecting your dataset[¶](#uploading-or-connecting-your-dataset "Permanent link")

Before annotating your data, you\'ll need to [upload](../../quick_start/upload_data/) or [connect](../../quick_start/connect_external_storage/) the first version of your dataset, and [create a datasource](../data_engine/connect_datasource/) from it.

For the purpose of this guide, we\'ll go with the simplest option, uploading a dataset to DagsHub. We\'ll use a segment of the [COCO 1K](https://dagshub.com/Dean/COCO_1K/datasets?gallery=datasource&id=325) dataset. Make sure to [create a repository](../../quick_start/create_new_project/), then in the following snippet replace the `<repo_owner>` and `<repo_name>` with your user and repository name respectively. Everything else should work.

Start by installing DagsHub (`pip install -U dagshub`), and make sure you\'re in your workspace.

Then run the following snippet:

    from dagshub import get_repo_bucket_client
    from dagshub.data_engine import datasources

    # This retrieves the sample dataset an puts it in a folder called "data/". If you already have your own data there, then skip this line
    ds = datasources.get('Dean/COCO_1K', 'COCO_1K')
    ds.head(50).download_files(target_dir=".")

    # Upload folder contents
    client = get_repo_bucket_client("<repo_owner>/<repo_name>", flavor="s3fs")
    client.put("data/", "<repo_name>/data", recursive=True)

    # Create a datasource
    datasources.create_datasource(repo="<repo_owner>/<repo_name>", name="hello-world", path="s3://<repo_name>/data")

After this you should see the dataset in your project\'s Datasets tab (the view below is after you click on \"visualize\" that dataset): [![Visualize New Dataset](../assets/annotation/create_simple_dataset.jpeg)](../assets/annotation/create_simple_dataset.jpeg)

## Import existing annotations[¶](#import-existing-annotations "Permanent link")

DagsHub\'s client enables you to import existing annotations from your previous projects.

Assuming your annotation files are saved to a local file and have a YOLO or CVAT compatible YAML file - e.g. `annotations.yaml`, use the following Python command to import them.

    ds.import_annotations_from_files(
        annotation_type="yolo", # or 'cvat'
        path="annotations.yaml",
        field="imported_annotations", # name of the field that we'll import the annotations into
        yolo_type="segmentation" # required for YOLO annotations
    )

Where `ds` is the [Data Engine Datasource](https://dagshub.com/docs/client/reference/data_engine/datasource.html#) which has the relevant images scanned. To see the full documentation for this function, see the [client docs](https://dagshub.com/docs/client/reference/data_engine/datasource.html#dagshub.data_engine.model.datasource.Datasource.import_annotations_from_files).

### Supported formats for annotation imports[¶](#supported-formats-for-annotation-imports "Permanent link")

We currently support the following annotation formats for import:

1.  Computer Vision:
    1.  **YOLO**: bounding boxes, segmentation maps, keypoints
    2.  **CVAT**: bounding boxes, segmentation maps, keypoints

## Send data points to be annotated[¶](#send-data-points-to-be-annotated "Permanent link")

There are 3 ways to send datasets to be annotated. You can use the DagsHub UI, DagsHub client or use the local visualization instance.

### Send to annotation using the DagsHub UI[¶](#send-to-annotation-using-the-dagshub-ui "Permanent link")

Sending through the UI is the easiest, most straight forward way for most users as it doesn\'t require running any code.

1.  You can annotate an entire datasource by clicking the annotate button in the datasets tab: [![Visualize from the UI](../assets/annotation/annotate_datasource.jpeg)](../assets/annotation/annotate_datasource.jpeg)

2.  You can also select specific data points to annotate, by going into the dataset or datasource view, selecting any number of images, and clicking the Annotate button. [![Send to Annotations from UI](../assets/annotation/send_to_annotation_ui.jpeg)](../assets/annotation/send_to_annotation_ui.jpeg)

Tip: easily select multiple datapoints

You can use Shift+Click to select multiple data points easily, or the checkbox at the top to select all the datapoints.

### Send to annotation using the DagsHub client[¶](#send-to-annotation-using-the-dagshub-client "Permanent link")

Sending to annotations using the client gives you the flexibility to [pre-filter](../data_engine/query_and_create_subsets/) your dataset and only send parts of it to be annotated. This can be especially useful when working on improving the quality of your dataset, where you wouldn\'t necessarily want to redo the entire dataset\'s labels, but only parts.

To send data points to annotations using Dagshub client, use the `.annotate()` function:

    # Get the datasource we just created
    ds = datasources.get("<repo_owner>/<repo_name>", "hello-world")

    # Send all the data points in the datasource to annotation
    ds.annotate()

    # Send only the first 5 samples to be annotated
    ds.head(5).annotate()

### Send to annotation from the local dataset visualizer (Voxel51)[¶](#send-to-annotation-from-the-local-dataset-visualizer-voxel51 "Permanent link")

To annotate selected data points from the [local visualization instance](../data_engine/visualizing_datasets/), start by visualizing your dataset:

    ds.visualize()

Select the images you\'d like to annotate, then navigate to the DagsHub tab (if there is no DagsHub tab, click on the â€˜+â€™ button and choose DagsHub) and click on the â€˜Annotate selected in LabelStudioâ€™ button:

[![Send to Annotations from Voxel](../assets/annotation/annotate_from_local_ui.jpeg)](../assets/annotation/annotate_from_local_ui.jpeg)

## Configuring the annotation project[¶](#configuring-the-annotation-project "Permanent link")

After sending data points for annotation, a new window with the DagsHub web platform will open. It might take a few moments to spin up the labeling server. You can play pong while waiting :)

From here you can either choose the annotation project to add the tasks to, or create a new project. This means you can manage the annotation process with multiple annotators, assigning the right tasks to the relevant annotator.

To add the selected annotation tasks to an existing annotation project, select the first option, **Continue with one of the existing projects**, and choose an existing one (You\'ll only see this option if you have a labeling project set up). To create a new annotation project, select the second option, **Create new**, and specify a name for it.

[![Add Datapoints to Annotation Project](../assets/annotation/create_new_annotation_project.jpeg)](../assets/annotation/create_new_annotation_project.jpeg)

Using Existing Labeling Project Configurations

You can import existing configurations (annotation templates, auto-labelers, etc.) to your new project by checking the \*\* Use project settings of:\*\* option and choosing an existing project.

[![Select Existing Settings](../assets/annotation/select_existing_settings.jpeg)](../assets/annotation/select_existing_settings.jpeg)

Click start, and you will be directed to your project with the relevant tasks.

[![Annotation Project with Tasks](../assets/annotation/existing_settings.jpeg)](../assets/annotation/existing_settings.jpeg)

## Saving annotations back to your datasource[¶](#saving-annotations-back-to-your-datasource "Permanent link")

You can update your datasource with the new annotations. To do that, annotate a datapoint (a task), then: 1. Click on the **Submit** button (or **Update** if you\'re updating an existing annotation. 2. Click the **Save** button at the top right of the screen.

[![save_annotations](../assets/annotation/save_annotations.jpeg)](../assets/annotation/save_annotations.jpeg)

Each annotation is saved as an [enrichment field](../data_engine/enrich_datasource/), named after the annotation project name you used + the word *annotation*, on the corresponding data point. The annotation is saved as blob with a Label Studio json format as the content.

In addition to the annotation metadata layer, it will create another enrichment layer with the annotation classes (called `<annotation_enrichment_name>.labels.str`). You can use this to query the classes per datapoint easily (e.g. `ds["annotation.labels.str"].contains("cat")`).

## Visualizing the new annotations[¶](#visualizing-the-new-annotations "Permanent link")

After saving the annotations your enrichment fields will be updated. You can return to your dataset view, enable the relevant annotation field in the metadata sidebar, and view the various annotations.

[![Display Annotations in DagsHub](../assets/annotation/updated_annotations.jpeg)](../assets/annotation/updated_annotations.jpeg)

## Auto Labeling with ML Models[¶](#auto-labeling-with-ml-models "Permanent link")

Label Studio supports active learning with automatic labeling with existing models. If you need this check out the docs on [auto-labeling](../auto_labeling/) and [active learning](../active_learning/).

## Next steps[¶](#next-steps "Permanent link")

Now that you have labeled your dataset, you might be interested in [converting it into a dataloader for training](../data_engine/train_model/), or, if you already know how to do that, learn how to [track your experiments](../track_ml_experiments/).

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).
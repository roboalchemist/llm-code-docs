# Source: https://dagshub.com/docs/feature_guide/annotations/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/feature_guide/annotations.md "Edit this page")

# DagsHub Annotations[¶](#dagshub-annotations "Permanent link")

DagsHub Annotations provides a fully configured labeling workspace, with full access to your project files, fired up and ready to go. It is fully integrated with [Data Engine](../data_engine/), and built on our integration with [Label Studio](../../integration_guide/label_studio/).

DagsHub Annotations provide a unique labeling flow that ensures full reproducibility, scalability, and efficient version control of your annotations and data.

Looking for the Old Annotation Flow?

In the past, DagsHub used a git-flow based annotation system, which will soon be deprecated. See the [old annotation docs](../annotations_git_flow/)

# An error occurred. 

Unable to execute JavaScript.

## How DagsHub Annotations works?[¶](#how-dagshub-annotations-works "Permanent link")

Every repository on DagsHub is configured with a labeling workspace based on Label Studio.

When you create a data engine dataset or datasource, you can easily send any datapoint to be annotated from the Python Client, the UI, and our locally support Voxel51 visualization instance.

The workspace has full access to the project files, making them available to annotate directly from DagsHub\'s interface. To scale your work, DagsHub Annotations enable you to create multiple labeling projects on the workspace that are isolated from one another.

Once you\'re done labeling, you can save the annotations to your [Data Engine enrichments](../../use_cases/data_engine/enrich_datasource/), which are fully [versioned](../../use_cases/data_engine/version_datasets/). This enables you to return to previous annotation versions, compare them, and select the best option to train your model on.

In addition to the annotation metadata layer, it will create another enrichment layer with the annotation classes (called `<annotation_enrichment_name>.labels.str`). You can use this to query the classes per datapoint easily (e.g. `ds["annotation.labels.str"].contains("cat")`).

## Getting Started with Annotations[¶](#getting-started-with-annotations "Permanent link")

The easiest way to get started with annotations is through our [annotations use case guide](../../use_cases/annotation/).

## Annotation Project & Annotator Management[¶](#annotation-project-annotator-management "Permanent link")

DagsHub Annotations provides an easy way to have multiple annotators work simultaneously. When you [send a dataset to be annotated](../../use_cases/annotation/#send-data-points-to-be-annotated), you can select whether to add the annotation tasks to an existing workspace or create a new one.

[![Add or create new annotation workspace](../../use_cases/assets/annotation/select_existing_settings.jpeg)](../../use_cases/assets/annotation/select_existing_settings.jpeg)

When you save annotations, each workspace will get it\'s dedicated metadata column, enabling you to [version annotations](../../use_cases/data_engine/query_and_create_subsets/#versioning-filters), and compare between different options to get the best quality annotations for your training data.

## Custom Label Configurations[¶](#custom-label-configurations "Permanent link")

DagsHub Annotations supports all of Label Studio\'s annotation templates, and the ability to create custom templates. To choose or customize label templates, simply click the settings button inside your label studio project, and select \"Labeling Interface\".

~Go\ to\ label\ studio\ labeling\ interface~

You can also fully customize your labeling interface by clicking on the \"code\" tab. For the full customization options see the [Label Studio documentation](https://labelstud.io/tags).

[![Custom Labeling Interface](../assets/annotations/custom_interface.jpeg)](../assets/annotations/custom_interface.jpeg)

## Auto Labeling with custom Machine Learning models[¶](#auto-labeling-with-custom-machine-learning-models "Permanent link")

Auto labeling is critical for active learning, and can boost the amount of annotated data you have significantly. DagsHub supports connecting custom models to pre-annotate your data. We even wrote an entire tutorial about it. [Read it now](https://dagshub.com/blog/active-learning-pipeline-with-data-engine/).

## Label Studio SDK[¶](#label-studio-sdk "Permanent link")

DagsHub Annotations is fully compatible with the [Label Studio Python SDK](https://pypi.org/project/label-studio-sdk/).\
This SDK is the easiest way to try advanced usage of Label Studio - such as uploading custom tasks, computing metrics on annotations, programmatically doing active learning, etc.\
[The DagsHub Python client makes it very easy to get an authenticated instance of the Label Studio Python client!](https://dagshub.com/docs/client/reference/ls_client.html)

## Label Studio API[¶](#label-studio-api "Permanent link")

DagsHub Annotations is fully compatible with the [Label Studio API](https://labelstud.io/api). You can use it to hook into your label studio project and use it for any of your production annotation needs.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).
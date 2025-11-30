# Source: https://dagshub.com/docs/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/index.md "Edit this page")

# DagsHub: A Single AI Platform to Manage Multimodal AI Datasets & Models[¶](#dagshub-a-single-ai-platform-to-manage-multimodal-ai-datasets-models "Permanent link")

## What is DagsHub?[¶](#what-is-dagshub "Permanent link")

DagsHub is an AI platform that helps developers and teams manage the entire lifecycle from data collection, through dataset curation and annotation, tracking experimentation (both model training and prompt engineering), to model management. DagsHub is based on open source tools and formats (such as Git, [DVC](integration_guide/dvc/), [MLflow](integration_guide/mlflow_tracking/), [Label Studio](integration_guide/label_studio/), and [others](integration_guide/)) so it should quickly feel familiar.

**If you\'re not sure where to start, check out the [Quick Start](quick_start/) section - it will take you step by step through the flow below with short video tutorials.**

<figure>
<a href="assets/index/dagshub-flow.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="assets/index/dagshub-flow.png" alt="DagsHub Workflow Diagram" /></a>
<figcaption>DagsHub Workflow Diagram</figcaption>
</figure>

DagsHub was particularly designed for unstructured and multimodal data types â€" e.g. text, images, audio, video, documents, medical imaging, and binary files.

Above you can see a simplified ML/AI workflow diagram and where DagsHub fits in. DagsHub integrates with your storage and compute providers, and while you can host your data on the platform with [DagsHub Storage](feature_guide/dagshub_storage/), we don\'t currently provide compute resources, and rely on the compute infrastructure you have, which can range from running training and deployments locally, in the cloud, or on edge devices.

## Not Sure Where to Start?[¶](#not-sure-where-to-start "Permanent link")

DagsHub offers many ways to improve your machine learning workflow. If you know what you\'re doing, feel free to explore. If not, here are 2 recommended options:

- [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTkuNTA0LjQzYTEuNTE2IDEuNTE2IDAgMCAxIDIuNDM3IDEuNzEzTDEwLjQxNSA1LjVoMi4xMjNjMS41NyAwIDIuMzQ2IDEuOTA5IDEuMjIgMy4wMDRsLTcuMzQgNy4xNDJhMS4yNSAxLjI1IDAgMCAxLS44NzEuMzU0aC0uMzAyYTEuMjUgMS4yNSAwIDAgMS0xLjE1Ny0xLjcyM0w1LjYzMyAxMC41SDMuNDYyYy0xLjU3IDAtMi4zNDYtMS45MDktMS4yMi0zLjAwNHptMS4wNDcgMS4wNzRMMy4yODYgOC41NzFBLjI1LjI1IDAgMCAwIDMuNDYyIDlINi43NWEuNzUuNzUgMCAwIDEgLjY5NCAxLjAzNGwtMS43MTMgNC4xODggNi45ODItNi43OTNBLjI1LjI1IDAgMCAwIDEyLjUzOCA3SDkuMjVhLjc1Ljc1IDAgMCAxLS42ODMtMS4wNmwyLjAwOC00LjQxOC4wMDMtLjAwNi0uMDA0LS4wMDktLjAwNi0uMDA2LS4wMDgtLjAwMXEtLjAwNSAwLS4wMDkuMDA0IiAvPjwvc3ZnPg==)]  **[Getting Started](quick_start/)**

  ------------------------------------------------------------------------

  Check out our step-by-step guides and video tutorials that will take you through the flow above

- [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE2Ljk0MSA0Ljk3NmE3LjAzIDcuMDMgMCAwIDAtNC45MyAyLjA2NCA3LjAzMyA3LjAzMyAwIDAgMC0uMTI0IDkuODA3bDIuMzk1LTIuMzk1YTMuNjQ2IDMuNjQ2IDAgMCAxIDUuMTUtNS4xNDhsMi4zOTctMi4zOTlhNy4wMyA3LjAzIDAgMCAwLTQuODg4LTEuOTNtLTkuODcxLjAxYTcuMDMgNy4wMyAwIDAgMC00Ljg4OCAxLjkzMWwyLjM5MSAyLjM5MWEzLjY0MyAzLjY0MyAwIDAgMSA1LjAyMy4xMjdsMS43MzQtMi45NzMtLjEtLjA4YTcuMDMgNy4wMyAwIDAgMC00LjE2LTEuMzk2bTE1LjAxIDIuMTcyLTIuMzkgMi4zOWEzLjY0NiAzLjY0NiAwIDAgMS01LjE1IDUuMTVsLTIuNDA2IDIuNDA3YTcuMDM2IDcuMDM2IDAgMCAwIDkuOTQ1LTkuOTQ3bS0yMC4xNDguMDFhNy4wMzMgNy4wMzMgMCAwIDAtLjAwMiA5LjY4MWwyLjM5Ny0yLjM5N2EzLjY0MyAzLjY0MyAwIDAgMS0uMDA0LTQuODkyem03LjY2NCA3LjQyM2EzLjYzNSAzLjYzNSAwIDAgMS01LjAxNy4xMTNMMi4xODIgMTcuMWE3LjAzIDcuMDMgMCAwIDAgOS4wMDcuNTQ2bC4xMzctLjExMnoiIC8+PC9zdmc+)]  **[Hello World Colab](https://colab.research.google.com/#fileId=https%3a%2f%2fdagshub.com%2fDagsHub%2fhello-world-vision%2fraw%2fmain%2fhello-world-vision.ipynb)**

  ------------------------------------------------------------------------

  A step-by-step computer vision tutorial, zero local setup needed. For other data types, see our [tutorials section](tutorials/)

## Key Use Cases[¶](#key-use-cases "Permanent link")

You can do a lot of things with DagsHub, but here are some of the things DagsHub users usually use the platform for:

- **[Dataset Management & Versioning](use_cases/data_versioning/)**

  ------------------------------------------------------------------------

  Manage your data, and version your datasets to create a fully reproducible project.

- **[Experiment Tracking](use_cases/track_ml_experiments/)**

  ------------------------------------------------------------------------

  Keep track of your experimentation process, log parameters and metrics, and analyze results

- **[Annotating Data](use_cases/annotation/)**

  ------------------------------------------------------------------------

  Label your data, then use the results easily without writing custom data pipelines

- **[Model Registry & Deployment](use_cases/deploy_ml_model_to_cloud/)**

  ------------------------------------------------------------------------

  Manage model versions, status and deployments

## DagsHub Overview Video[¶](#dagshub-overview-video "Permanent link")

# An error occurred. 

Unable to execute JavaScript.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).
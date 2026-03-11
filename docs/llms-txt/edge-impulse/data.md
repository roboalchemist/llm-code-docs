# Source: https://docs.edgeimpulse.com/studio/organizations/data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

Since the creation of Edge Impulse, we have been helping customers to deal with complex data pipelines, complex data transformation methods and complex clinical validation studies.

In most cases, before even thinking about machine learning algorithms, researchers need to build quality datasets from real-world data. These data come from various devices (prototype devices being developed vs clinical/industrial-grade reference devices), have different formats (excel sheets, images, csv, json, etc...), and be stored in various places (researchers' computers, Dropbox folders, Google Drive, S3 buckets, etc...).

Dealing with such complex data infrastructure is time-consuming and expensive to develop and maintain. With the organizational data, we want to give you tools to centralize, validate and transform datasets so they can be easily imported into your projects to train your machine learning models.

**Health reference design**

We have built a [**health reference design**](/knowledge/guides/reference-designs/health-reference-design) that describes an end-to-end ML workflow for building a wearable health product using Edge Impulse.

In this reference resign, we want to help you understand how to create a full clinical data pipeline by using a public dataset from the [PPG-DaLiA](https://archive.ics.uci.edu/dataset/495/ppg+dalia)
repository. This tutorial will guide you through the following steps:

* [Synchronizing clinical data with a bucket](/knowledge/guides/reference-designs/health-reference-design/synchronizing-clinical-data)
* [Validating clinical data](/knowledge/guides/reference-designs/health-reference-design/validating-clinical-data)
* [Querying clinical data](/knowledge/guides/reference-designs/health-reference-design/querying-clinical-data)
* [Transforming clinical data](/knowledge/guides/reference-designs/health-reference-design/transforming-clinical-data)
* [Building data pipelines](/studio/organizations/data-pipelines)

## Buckets

Before we get started, you must link your organization with one or more storage buckets. Further details about how to integrate with cloud storage providers can be found in the [Cloud data storage](/studio/organizations/data/cloud-data-storage) document.

## Datasets

Two types of dataset structures can be used - **Generic datasets (default)** and **Clinical datasets**.

<Info>
  There is no required format for data files. You can upload data in any format, whether it's CSV, Parquet, or a proprietary data format.

  However, to import data items to an Edge Impulse project, you will need to use the right format as our studio ingestion API only supports these formats:

  * JPG, PNG images
  * MP4, AVI video files
  * WAV audio files
  * JSON/CBOR files in the Edge Impulse [data acquisition format](/tools/specifications/data-acquisition/json-cbor)
  * CSV files

  **Tip: You can use** [**transformation blocks**](/studio/organizations/custom-blocks/custom-transformation-blocks) **to convert your data**
</Info>

<Frame caption="Datasets overview">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/organization-datasets-overview.png?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=b573b517d622b7d3f6c76680271c5805" width="1600" height="652" data-path=".assets/images/organization-datasets-overview.png" />
</Frame>

<Tabs>
  <Tab title="Default dataset">
    The **default dataset structure** is a file-based one, no matter the directory structure:

    For example:

    ```
    images/
    ├── testing/
    │   ├── 1.jpg
    │   ├── 2.jpg
    │   ├── 3.jpg
    │   ...
    │   └── 200.jpg
    └── training/
        ├── 1.jpg
        ├── 2.jpg
        ├── 3.jpg
        ...
        └── 800.jpg
    ```

    or:

    ```
    keywords/
    ├── french-accent/
    │   ├── hello.wav
    │   ├── yes.wav
    │   ├── no.wav
    ├── greek-accent/
    │   ├── hello.wav
    │   ├── yes.wav
    │   ├── no.wav
    └── unlabeled/
        ├── 1.wav
        ├── 2.wav
        ├── 3.wav
        ...
        └── 20.wav
    ```

    *Note that you will be able to associate the labels of your data items from the file name or the directory name when importing your data in a project.*
  </Tab>

  <Tab title="Clinical dataset">
    The **clinical datasets structure** in Edge Impulse has three layers:

    1. The dataset, a larger set of data items, grouped together.
    2. Data item, an item with metadata and files attached.
    3. Data file, the actual files.

    See the [health reference design](/knowledge/guides/reference-designs/health-reference-design) tutorial for a deeper explanation.
  </Tab>
</Tabs>

### Create a new dataset

Once you successfully linked your storage bucket to your organization, head to the **Datasets** tab and click on **+ Add new dataset**:

<Frame caption="Add new dataset">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/organization-add-dataset.png?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=17135ec2ba80358f8a37cc0f7dbb2820" width="1600" height="888" data-path=".assets/images/organization-add-dataset.png" />
</Frame>

Fill out the following form:

<Frame caption="Add dataset">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/organization-add-dataset-2.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=5608ce76f83acc3cbb2f9236d84ba28b" width="975" height="1000" data-path=".assets/images/organization-add-dataset-2.png" />
</Frame>

Click on **Create dataset**

## Data

With your datasets imported, you can now navigate into your dataset, create folders, [query your dataset](/knowledge/guides/reference-designs/health-reference-design/querying-clinical-data), add data items and import your data to an Edge Impulse project.

<Tabs>
  <Tab title="Default dataset">
    #### Default view

    The default view lets you navigate in your bucket following the directory structure. You can easily add data using the "**+ New folder**" button. To add new data, use the right panel - drag and drop your files and folders and it will automatically upload them to your bucket.

    <Frame caption="Data items overview">
      <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/organization-datasets-view-data.png?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=dc68bb87e4f49f664c9c6aa1df4e03e8" width="1540" height="1000" data-path=".assets/images/organization-datasets-view-data.png" />
    </Frame>
  </Tab>

  <Tab title="Clinical dataset">
    #### Clinical view

    The clinical view is slightly different, see [synchronizing clinical data with a bucket](/knowledge/guides/reference-designs/health-reference-design/synchronizing-clinical-data) for more information. This view lets you easily [query your clinical dataset](/knowledge/guides/reference-designs/health-reference-design/querying-clinical-data) but to import data, you will need to set up an [upload portal](/studio/organizations/upload-portals) or upload them directly to your bucket.

    *Tip: You can add two distinct datasets in Edge Impulse that point to the same bucket path, one generic and one clinical. This way you can leverage both the easy upload and the ability to query your datasets.*

    <Frame caption="Clinical dataset overview">
      <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/research-data-dataset.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=aff9749b2630820086b1004a078391cc" width="1588" height="1000" data-path=".assets/images/research-data-dataset.png" />
    </Frame>
  </Tab>
</Tabs>

### Adding data to your project

Go to the **Actions...->Import data into a project**, select the project you wish to import to and click **Next, Configure how to label this data**:

<Frame caption="Uploading Files">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/organization-data-add-to-project.png?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=bf2829f2cb4b8b2de159e143d2aac490" width="1600" height="970" data-path=".assets/images/organization-data-add-to-project.png" />
</Frame>

This will import the data into the project and optionally create a new label for each file in the dataset. This labeling step helps you keep track of different classes or categories within your data.

After importing the data into the project, in the **Next, post-sync actions** step, you can configure a [data pipeline](/studio/projects/data-acquisition/data-sources) to automatically retrieve and trigger actions in your project:

<Frame caption="Label your files">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/organization-data-post-sync-action.png?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=dddf0bb0ace4174729706f4279a918cb" width="1600" height="979" data-path=".assets/images/organization-data-post-sync-action.png" />
</Frame>

### Previewing Data

We also have added a data preview feature, allowing you to visualize certain types of data directly within the organization data tab.

Supported data types include tables (CSV/Parquet), images, PDFs, audio files (WAV/MP3), and text files (TXT/JSON). This feature gives you a quick overview of your data and helps ensure its integrity and correctness.

<Frame caption="Data items overview - CSV/Parquet type">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/organization-data-visualization.png?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=4155315c559616a95c8e22d5d4cf1fc3" width="1600" height="978" data-path=".assets/images/organization-data-visualization.png" />
</Frame>

<br />

<Frame caption="Data items overview - image type">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/organization-data-visualization-2.png?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=255dc53d7587cee8c2a4b1688a7a5024" width="1600" height="978" data-path=".assets/images/organization-data-visualization-2.png" />
</Frame>

## Recap

If you need to get data into your organization, you can now do this in a few simple steps. To go further and use advanced features, query your datasets or transform your dataset, please have a look at the [health reference design tutorial](/knowledge/guides/reference-designs/health-reference-design) :rocket:

Any questions, or interested in the enterprise version of Edge Impulse? [Contact us](https://edgeimpulse.com/contact) for more information.


Built with [Mintlify](https://mintlify.com).
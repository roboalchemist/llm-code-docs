# Source: https://docs.edgeimpulse.com/studio/projects/data-acquisition/data-sources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data sources

The **data sources** page is much more than just adding data from external sources. It lets you create complete **automated data pipelines** so you can work on your **active learning strategies**.

From there, you can import datasets from existing cloud storage buckets, automate and schedule the imports, and, trigger actions such as explore and label your new data, retrain your model, automatically build a new deployment task and more.

<Info>
  #### Run transformation jobs directly from your projects

  You can also trigger cloud jobs, known as [transformation blocks](/studio/organizations/custom-blocks/custom-transformation-blocks), these are particularly useful if you want to generate synthetic datasets or automate tasks using the Edge Impulse API. We provide several pre-built transformation blocks available for organizations' projects:

  * [DALL-E 3 Image Generation Block](https://github.com/edgeimpulse/example-transform-Dall-E-images)
  * [Whisper Voice Synthesis Block](https://github.com/edgeimpulse/example-transform-whisper-keywords)
  * [Find best Visual AD model](https://github.com/edgeimpulse/find-best-fomo-ad-model)
</Info>

<Frame caption="Data sources">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-pipeline-success-3.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=706b959138ef55a734ae4b8ebfed9e05" width="1600" height="837" data-path=".assets/images/data-pipeline-success-3.png" />
</Frame>

<Info>
  This view, originally accessible from the main left menu, has been moved to the **Data acquisition** tab for better clarity. The screenshots have not yet been updated.
</Info>

<iframe src="https://www.youtube.com/embed/nZRrt6vIDTQ" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

### Add a data source

Click in **+ Add new data source** and select where your data lives:

You can either use:

* [Cloud data storage](/studio/organizations/data/cloud-data-storage)
* [Organizational datasets](/studio/organizations/data) (enterprise feature)
* [Upload portals](/studio/organizations/upload-portals) (enterprise feature)
* [Transformation blocks](/studio/organizations/custom-blocks/custom-transformation-blocks) (enterprise feature)
* Don't import data (if you just need to create a pipeline)

<Frame caption="Add new data source">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-sources-2.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=59fddd24b8e08815310e1156c0719016" width="1600" height="967" data-path=".assets/images/studio-data-sources-2.png" />
</Frame>

See how to configure your storage buckets:

* [Amazon S3](/studio/organizations/data/cloud-data-storage#amazon-s3-bucket)
* [Microsoft Azure Blob Storage](/studio/organizations/data/cloud-data-storage#microsoft-azure-blob-storage-blob-container)
* [Google Cloud Storage](/studio/organizations/data/cloud-data-storage#google-cloud-storage-bucket)
* or any [S3 compatible storage](/studio/organizations/data/cloud-data-storage#other-s3-compatible-buckets).

Click on **Next, provide credentials**:

<Frame caption="Provide your credentials">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-sources-add-2.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=96cf42467f7e6a908dec8e1fc5d6be60" width="1600" height="967" data-path=".assets/images/studio-data-sources-add-2.png" />
</Frame>

Click on **Verify credentials**:

<Frame caption="Automatically label your data">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-data-sources-add-3.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=fb408e71e96002b166787ad2876c4273" width="1600" height="919" data-path=".assets/images/studio-data-sources-add-3.png" />
</Frame>

Here, you have several options to automatically label your data:

#### Infer from folder name

In the example above, the structure of the folder is the following:

```
.
├── cars
│   ├── cars.01741.jpg
│   ├── cars.01743.jpg
│   ├── cars.01745.jpg
│   ├── ... (400 items)
├── unknown
│   ├── unknown.test_2547.jpg
│   ├── unknown.test_2548.jpg
│   ├── unknown.test_2549.jpg
│   ├── ... (400 items)
└── unlabeled
    ├── cars.02066.jpg
    ├── cars.02067.jpg
    ├── cars.02068.jpg
    └── ... (14 items)

3 directories, 814 files
```

The labels will be picked from the folder name and will be split between your **training** and **testing** set using the following ratio `80/20`.

<Info>
  The samples present in an `unlabeled/` folder will be kept unlabeled in Edge Impulse Studio.
</Info>

Alternatively, you can also organize your folder using the following structure to automatically split your dataset between **training** and **testing** sets:

```
.
├── testing
│   ├── cars
│   │   ├── cars.00012.jpg
│   │   ├── cars.00031.jpg
│   │   ├── cars.00035.jpg
│   │   └── ... (~150 items)
│   └── unknown
│       ├── unknown.test_1012.jpg
│       ├── unknown.test_1026.jpg
│       ├── unknown.test_1027.jpg
│       ├── ... (~150 items)
├── training
│   ├── cars
│   │   ├── cars.00006.jpg
│   │   ├── cars.00025.jpg
│   │   ├── cars.00065.jpg
│   │   └── ... (~600 items)
│   └── unknown
│       ├── unknown.test_1002.jpg
│       ├── unknown.test_1005.jpg
│       └── unknown.test_46.jpg
│       └── ... (~600 items)
└── unlabeled
    ├── cars.02066.jpg
    ├── cars.02067.jpg
    ├── cars.02068.jpg
    └── ... (14 items)

7 directories, 1512 files
```

#### Infer from file name

When using this option, only the file name is taken into account. The part before the first `.` will be used to set the label. E.g. `cars.01741.jpg` will set the label to `cars`.

#### Keep the data unlabeled

All the data samples will be unlabeled, you will need to label them manually before using them.

Finally, click on **Next, post-sync actions**.

<Frame caption="Trigger actions">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-data-sources-add-4.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=0a6ce907a9b2cbdb5df6b1879875158c" width="1600" height="814" data-path=".assets/images/studio-data-sources-add-4.png" />
</Frame>

From this view, you can automate several actions:

* **Recreate data explorer**

  The [data explorer](/studio/projects/data-acquisition/data-explorer) gives you a one-look view of your dataset, letting you quickly label unknown data. If you enable this you'll also get an email with a screenshot of the data explorer whenever there's new data.
* **Retrain model**

  If needed, will retrain your model with the same impulse. If you enable this you'll also get an email with the new validation and test set accuracy.

  *Note: You will need to have trained your project at least once.*
* **Create new version**

  Store all data, configuration, intermediate results and final models.
* **Create new deployment**

  Builds a new library or binary with your updated model. Requires 'Retrain model' to also be enabled.

### Run the pipeline

Once your pipeline is set, you can run it directly from the UI, from external sources or by scheduling the task.

<Frame caption="Run your pipeline">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-source-run.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=f0b3d6c88e5904ea953d36da86cd75f6" width="1600" height="800" data-path=".assets/images/studio-data-source-run.png" />
</Frame>

#### Run the pipeline from the UI

To run your pipeline from Edge Impulse studio, click on the `⋮` button and select **Run pipeline now**.

#### Run the pipeline from code

To run your pipeline from Edge Impulse studio, click on the `⋮` button and select **Run pipeline from code**. This will display an overlay with `curl`, `Node.js` and `Python` code samples.

<Info>
  You will need to create an **API key** to run the pipeline from code.
</Info>

<Frame caption="Run the pipeline from code">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-data-sources-run-from-code.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=5475f438fff946deffe30322f736c26d" width="1303" height="1000" data-path=".assets/images/studio-data-sources-run-from-code.png" />
</Frame>

#### Schedule your pipeline jobs

By default, your pipeline will run every day. To schedule your pipeline jobs, click on the `⋮` button and select **Edit pipeline**.

<Info>
  Free users can only run the pipeline every 4 hours. If you are an enterprise customer, you can run this pipeline up to every minute.
</Info>

<Frame caption="Edit pipeline">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-explorer-edit-pipeline.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=b4dd45b4526164d23f19ca1dbd96f8b5" width="1600" height="962" data-path=".assets/images/studio-data-explorer-edit-pipeline.png" />
</Frame>

Once the pipeline has successfully finish, you will receive an email like the following:

<Frame caption="Email example containing the full results">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-sources-email.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=f757b12690299f187a71fca6376442ae" width="636" height="1000" data-path=".assets/images/data-sources-email.png" />
</Frame>

<Info>
  You can also define who can receive the email. The users have to be part of your project. See: [*Dashboard -> Collaboration*](/studio/projects/dashboard#3.-collaboration).
</Info>

#### Webhooks

Another useful feature is to create a **webhook** to call a URL when the pipeline has ran. It will run a POST request containing the following information:

```
{
    "organizationId":XX,
    "pipelineId":XX,
    "pipelineName":"Import data from portal \"Data sources demo\"",
    "projectId":XXXXX,
    "success":true,
    "newItems":0,
    "newChecklistOK":0,
    "newChecklistFail":0
}
```

<Frame caption="Data sources webhooks">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-data-sources-webhooks.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=b469396a4e3771880ebe285a0f9cb026" width="1600" height="741" data-path=".assets/images/studio-data-sources-webhooks.png" />
</Frame>

### Edit your pipeline

As of today, if you want to update your pipeline, you need to edit the configuration json available in `⋮` -> **Run pipeline from code**.

Here is an example of what you can get if all the actions have been selected:

```
[
    {
        "name": "Fetch data from s3://data-pipeline/data-pipeline-example/infer-from-folder/",
        "builtinTransformationBlock": {
            "type": "s3-to-project",
            "endpoint": "https://s3.your-endpoint.com",
            "path": "s3://data-pipeline/data-pipeline-example/infer-from-folder/",
            "region": "fr-par",
            "accessKey": "XXXXX",
            "category": "split",
            "labelStrategy": "infer-from-folder-name",
            "secretKeyEncrypted": "xxxxxx"
        }
    },
    {
        "name": "Refresh data explorer",
        "builtinTransformationBlock": {
            "type": "project-action",
            "refreshDataExplorer": true
        }
    },
    {
        "name": "Retrain model",
        "builtinTransformationBlock": {
            "type": "project-action",
            "retrainModel": true
        }
    },
    {
        "name": "Create new version",
        "builtinTransformationBlock": {
            "type": "project-action",
            "createVersion": true
        }
    },
    {
        "name": "Create on-device deployment (C++ library)",
        "builtinTransformationBlock": {
            "type": "project-action",
            "buildBinary": "zip",
            "buildBinaryModelType": "int8"
        }
    }
]
```

Free projects have only access to the above `builtinTransformationBlock`.

If you are part of an [organization](/studio/organizations/dashboard), you can use your custom transformation jobs in the pipeline. In your organization workspace, go to **Custom blocks -> Transformation** and select **Run job** on the job you want to add.

<Frame caption="Transformation blocks">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/organisation-transformation-blocks.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=34021c730a0fc3e7923414158f39c945" width="1600" height="902" data-path=".assets/images/organisation-transformation-blocks.png" />
</Frame>

Select **Copy as pipeline step** and paste it to the configuration json file.

<Frame caption="Copy">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/organisation-transformation-blocks-run.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=ff85a92c095d1c5acf8b15147b2b67de" width="1600" height="815" data-path=".assets/images/organisation-transformation-blocks-run.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).
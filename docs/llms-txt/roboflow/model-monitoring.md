# Source: https://docs.roboflow.com/developer/rest-api/model-monitoring.md

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/model-monitoring.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/model-monitoring.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/model-monitoring.md

# Source: https://docs.roboflow.com/deploy/model-monitoring.md

# Model Monitoring

Roboflow's Model Monitoring dashboard gives you unparalleled visibility into your models, from prototyping, all the way through production. With Model Monitoring, you can view high-level statistics to get insight into how your models are performing over time, or even view individual inference requests, to see how your models perform on edge cases.

## Accessing Model Monitoring

{% hint style="info" %}
Model Monitoring is only available for select plans. For the latest information, see our [Pricing page](https://roboflow.com/pricing)
{% endhint %}

To view your Model Monitoring dashboard, click the "Monitoring" tab in your workspace.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-08439e11cc4c936bde7187adb58b72a71515f2c5%2Fimage.png?alt=media" alt="" width="312"><figcaption></figcaption></figure>

## Workspace Dashboard

Immediately, you will see three statistics pertaining to your models:

* **Total requests**: The total number of inferences made to all models in your workspace
* **Average confidence:** The average confidence across all predictions made by your models.
* **Average inference time**: The average inference time across all inferences (The time in seconds it took to produce the predictions including image preprocessing)

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-00a88ae4ffc0ffb5c7cc150479aec32f8dc2c12d%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The % change values are based on the current period vs the previous period. By default, these statistics will show your data for the last week. However, you can modify the time range using the buttons on top of the statistics.

<img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-b3cf0d46eaca184d244c4208cae0656f99bde61a%2Fimage%20(4)%20(8).png?alt=media" alt="" data-size="original">
{% endhint %}

The Models table shows all models that have inferences on them and clicking on them will take you to the [Model Dashboard](#model-dashboard).

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-ecac74de3be1e2b8edb1a48dd17c3a89edf86155%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

You can also access tabs for viewing Recent Inferences (across all models) and [setting Alerts](#alerting).

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-3c8a1d2992fe4573c7b9cdf93411d5ff18171c76%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

## Model Dashboard

Under the Models tab, you can select a specific model to view its data. There, you'll see the same statistics as the Workspace Overview, but specific to one model.

Here, in addition to the statistics, you can view the number of detections for each class in the model, and see its distribution with respect to other classes.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-0baf9cb0b75c74c2b341606235b7b5cd89bd9e59%2FScreenshot%202024-05-23%20at%2020.44.57.png?alt=media" alt=""><figcaption></figcaption></figure>

Clicking on the "See All Inferences" button at the top right of the table will navigate you to the [Inferences Table](#inferences-table).

## Inferences Table

Here, you can see all the prediction results for your model. In addition, you will also see any custom metadata that was added to your inferences. To view a subset of your inferences, you can use the filters on the top-right of the table.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c0e48d4b2d25fea504b7eb38ecfc3a0ce664c5b5%2FScreenshot%202024-05-23%20at%2020.50.13.png?alt=media" alt=""><figcaption></figcaption></figure>

### Inference Details

From the Inferences Table, you have the ability to drill down into a specific inference and see more details. Let's break it down in the order shown in this image:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-ce546fe2b1798e05122b3de07944b699094213fc%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

1. **Image:** Here, you can see the image that was inferred. *Note: This isn't enabled by default. See* [*Enabling Inference Images*](#enabling-inference-images)
2. **Inference Details:** On this panel, you can view all the details and properties about your inference request. All available fields are shown by default, but if you want to hide some, you can click the "Cog" icon in the top right corner to hide fields. (This setting will persist on your browser)
3. On some fields, if available, there will be an option to search for inferences based on that field. On the highlighted example, it will search for inferences from the same model.
4. **Detections:** This collapsable pane shows a list of detections received from that inference. You can click on the "Class" and "Confidence" table headers to choose the sort order of the table.
5. **Download & Link buttons:** Here, you can download the image associated with the inference or copy a link to this Inference Details for later reference.

### Enabling Inference Images

{% hint style="info" %}
Images saved by Active Learning or Dataset Upload will count the same as uploading an image to your project. Credit, limit or quota usage may apply according to your plan type.
{% endhint %}

There are two ways to enable inference images to show up in Model Monitoring:

* **Roboflow Dataset Upload block:** In Workflows, you can add a "Roboflow Dataset Upload" block. Once you hook up the predictions and prediction image, it will show up in Model Monitoring.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2e0fe2213137512f9d235bb38ecce7c3463998ef%2Fimage%20(1)%20(8).png?alt=media" alt="" width="151"><figcaption></figcaption></figure>

* **Active Learning (legacy):** For legacy workspaces, you can enable "Active Learning" rules from your project's page:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2dd831a903dc127197efcec47e81026339de962c%2Fimage.png?alt=media" alt="" width="198"><figcaption></figcaption></figure>

## Alerting

You and other members of your team can subscribe to real-time alerts when issues or anomalies occur with your model. For example, if the confidence of your model suddenly decreases, or your Inference Server goes down, and your model stops running, your team will receive an email notification.

See more info on the Alerting page:

{% content-ref url="model-monitoring/alerting" %}
[alerting](https://docs.roboflow.com/deploy/model-monitoring/alerting)
{% endcontent-ref %}

## Custom Metadata

To attach additional metadata to an inference, you can use Model Monitoring's custom metadata feature. Using custom metadata, you can add information to an inference such as the location of where the image was taken, the expected value of the prediction, and so on. Your custom metadata will show up in the "Recent Inferences" and "All Inferences" views.

To attach custom metadata to an inference result, please see the [Custom Metadata API](https://docs.roboflow.com/api-reference/model-monitoring/custom-metadata) documentation.

## Model Monitoring API

For automation and integration into external systems, you can pull Model Monitoring statistics using [our API for model monitoring](https://app.gitbook.com/s/e5GEiPeDoFksvZv1vH3A/rest-api/model-monitoring).

## Supported Deployments

Model Monitoring supports inference requests made using Roboflow's Hosted API or the Roboflow Inference Server, granted the Inference Server has internet access. This includes edge deployments which use Roboflow's [License Server](https://blog.roboflow.com/roboflow-license-server/).

{% hint style="info" %}
At this time, Model Monitoring does not support inference requests made using the Inference Pipeline, however, we plan to add support in the near future.
{% endhint %}

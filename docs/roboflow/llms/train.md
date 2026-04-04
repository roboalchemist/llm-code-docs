# Source: https://docs.roboflow.com/roboflow/roboflow-ko/train/train.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/torningu/train.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/train/train.md

# Source: https://docs.roboflow.com/train/train.md

# Train a Model

You can train computer vision models in the Roboflow interface.

Roboflow offers two training options:

* Roboflow Train: Our flagship training service, ideal for creating production-ready models.
* [Roboflow Instant](https://docs.roboflow.com/train/automatic-model-training-with-roboflow-instant): Train models in a few minutes that are ideal for testing.

When you approve a batch of image annotations, Instant models are automatically trained. These models can be used immediately.

Models trained on Roboflow can be deployed with Inference, our on-device inference server, or in the cloud using our Serverless Hosted API with Workflows, Batch Processing with Workflows, or with your model API endpoint.

{% hint style="info" %}
Read our [licensing guidance](https://roboflow.com/licensing) to learn more about how models trained on Roboflow are licensed.
{% endhint %}

### Train a Model

To train a computer vision model, first [generate a dataset version](https://docs.roboflow.com/datasets/dataset-versions/create-a-dataset-version).

Click the "Custom Train" button to start configuring a training job:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-1ee541a880c492b76f0ede4a3e94e3b8d46f59b0%2FScreenshot%202025-05-14%20at%2014.04.15.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Select a Model Architecture

Next, you need to select a model architecture. This is the machine learning technology used to train your model.

The model architectures you can train depend on the type of project you have set up. Refer to the [Supported Models table](https://docs.roboflow.com/deploy/supported-models) for details on training compatibility.

For object detection, RF-DETR offers the best accuracy. For instance segmentation, RF-DETR Seg (Preview) offers the best accuracy.

Choose an architecture available for your project type, then click "Continue":

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-5637da3613366cf3a90d807925534fdef9f5d411%2FScreenshot%202025-07-23%20at%2011.36.11.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Select a Model Size

Next, you need to set a size for your model.

Model sizes will vary depending on the architecture of the model you choose. For example, RF-DETR — a state-of-the-art object detection model — offers Nano, Small, Medium, and Base:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-10f70e832223d53f1cd3e0d0b7226ff8b149b078%2FScreenshot%202025-07-23%20at%2011.36.34.png?alt=media" alt=""><figcaption></figcaption></figure>

For Roboflow 3.0, Fast and Accurate training options are available to all users. Medium, Large, and Extra Large are available only to paid users.

#### Select a Checkpoint

After selecting a training option, you will be asked whether you want to train from a checkpoint. The tabs below show the configuration options for each model type.

{% tabs %}
{% tab title="Object Detection" %}
You have three options:

* Trai**n from a Previous Checkpoint:** Ideal for when you already have a working model that you want to improve.
* **Train from Public Checkpoint**: Ideal for your first model version, or for when a previous training run did not achieve the expected results.
* **Train from Random Initialization**: **For advanced users only**, this option gives you a blank slate from which to train. Most users see worse results when using this option.
  {% endtab %}

{% tab title="Classification/Semantic Segmentation" %}
For Classification and Semantic Segmentation models, only one checkpoint is available.
{% endtab %}
{% endtabs %}

<details>

<summary>How do I choose a training option?</summary>

We recommend training from a Public Checkpoint for new object detection projects. By default, we offer training from a model trained on the Microsoft COCO dataset. For classification and semantic segmentation, we only support training from an ImageNet.

You can train from checkpoints based on projects hosted on Universe (object detection only). To do so, first [star a project in Universe](https://blog.roboflow.com/launch-universe-model-checkpoint/). Then, the project will be available as a training checkpoint in the Roboflow web application.

Furthermore, you can train from a checkpoint based on a previous version of a model (object detection, instance segmentation, and keypoint detection only). This method allows for a faster training process. We only recommend training from a previous checkpoint for your model if your model achieves strong performance).

Training from a Checkpoint means that you are employing [Transfer Learning](https://blog.roboflow.com/what-is-transfer-learning/). Transfer Learning will initialize your model training from the model you have selected. This can help to reduce training time, and provide you with improved training scores.

Training from Scratch means that you are *not* employing Transfer Learning. This will initialize your model training with randomized initial values for the model weights.

</details>

#### Start the Training Job

Once you have chosen a Checkpoint from which to train, click Start Training.

Your dataset will then be zipped and prepared for training in the Roboflow cloud.

After your dataset has been prepared, you will receive an estimate that shows how long training will take:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-18d9396cb8b4f7bf0e73319da14e3cb287251177%2FScreenshot%202025-05-14%20at%2014.12.53.png?alt=media" alt=""><figcaption></figcaption></figure>

The larger the dataset, and the larger the images in your dataset, the longer it will take for your model to train.

We will email you when the training process finished. In most cases, this should be under 24 hours.

#### Pricing

Training on Roboflow is priced on the length of the train job. You can see more information on our [credits page](https://www.roboflow.com/credits).

If you are a student or researcher and need credits for a project on which you are working, you can [apply for additional credits](https://roboflow.com/contribute).

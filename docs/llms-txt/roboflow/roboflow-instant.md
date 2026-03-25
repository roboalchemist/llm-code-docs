# Source: https://docs.roboflow.com/changelog/februrary-2025/roboflow-instant.md

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/train/roboflow-instant.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/torningu/roboflow-instant.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/train/roboflow-instant.md

# Source: https://docs.roboflow.com/train/roboflow-instant.md

# Roboflow Instant

Roboflow Instant is a quick-to-train, few-shot model you can use while developing a Proof of Concept.

Instant automatically trains a model using your dataset as soon as you approve a new batch of images in your dataset.

This model is then available for use in Roboflow Workflows, like any other model trained on Roboflow.

Instant only supports Object Detection projects.

Roboflow Instant models are free to train.

### Train a Roboflow Instant Model

Roboflow Instant models are automatically trained when you add <1000 images to your dataset and no Instant model exists for that project yet.

You can also trigger an Instant training job manually.

To trigger an Instant training job, navigate to a Project, click Models in the sidebar, then click "Train Model":

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-b450618cb1ce68fd34de18d816f1111baa7604db%2FScreenshot%202025-05-20%20at%2010.51.55.png?alt=media" alt=""><figcaption></figcaption></figure>

Choose "Roboflow Instant Model":

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cf1740ead8c2f28c458884a70c42050522900201%2FScreenshot%202025-05-20%20at%2010.52.39.png?alt=media" alt=""><figcaption></figcaption></figure>

You will then be asked to confirm your training job:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-9135313eac542828dccaad0650681debf3fae076%2FScreenshot%202025-05-20%20at%2010.53.09.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You cannot apply preprocessing or augmentation steps to Instant models.
{% endhint %}

Click "Create New Instant Model" to start your Roboflow Instant training job.

Your training job will then begin.

It may take several minutes for your model to be ready to use.

Your Instant model will then appear in your model list:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-7f578272d0b7f18d4e5b0e15516e30c576f37cfe%2FScreenshot%202025-05-20%20at%2010.54.40.png?alt=media" alt=""><figcaption></figcaption></figure>

### Deploy an Instant Model

To use your model, click the Deploy Model button on the right side of the row of the model you want to deploy:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-65217bd6e33f8de0ba5a03cff3d5194f702d5a20%2FScreenshot%202025-05-20%20at%2010.54.57.png?alt=media" alt=""><figcaption></figcaption></figure>

A window will appear from which you can choose Workflow template to use in your deployment. You can also opt to build your own Workflow.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6e732b5367d8b2c4332956f3f5b6c22868430690%2FScreenshot%202025-05-20%20at%2010.56.06.png?alt=media" alt=""><figcaption></figcaption></figure>

When you select an option, a Workflow will be created. This Workflow will be accessible from the Workflows page in your Roboflow Workspace.

Here is an example of a Workflow created from the Detect, Count, and Visualize template:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2c0f66c608bca7ef34b7e1c3cfacc1f7f32698f4%2FScreenshot%202025-05-20%20at%2010.57.02.png?alt=media" alt=""><figcaption></figcaption></figure>

This Workflow uses the Roboflow Instant model.

You can test your Workflow to see the Instant model in action:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-f1df3d5faa12464a47ef114193a649bef577f582%2FScreenshot%202025-05-20%20at%2011.01.28.png?alt=media" alt=""><figcaption></figcaption></figure>

### Run an Instant Model with an API

Refer to our [Run a Roboflow Instant Model ](https://docs.roboflow.com/deploy/serverless-hosted-api-v2/use-with-python-sdk)documentation to see how to call an Instant model directly using the Python SDK and Serverless Hosted API V2.

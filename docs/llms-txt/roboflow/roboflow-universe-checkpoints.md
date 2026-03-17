# Source: https://docs.roboflow.com/roboflow/roboflow-ko/train/train/roboflow-universe-checkpoints.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/torningu/train/roboflow-universe-checkpoints.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/train/train/roboflow-universe-checkpoints.md

# Source: https://docs.roboflow.com/train/train/roboflow-universe-checkpoints.md

# Train from a Universe Checkpoint

### Training from a Roboflow Universe Checkpoint

First, ensure you have selected the Workspace for your current project in your Universe profile, and "Starred" the dataset you'd like to use for Transfer Learning.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c571efa92326d45722f5b17fc0a261d047a0a3a6%2Fimage.png?alt=media" alt=""><figcaption><p>Switching Your Workspace Profile in Roboflow Universe</p></figcaption></figure>

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-3c2404f27a15c7c41c67858b519227d966001099%2Fimage.png?alt=media) ![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-3837bb6a0ad2b8f803d0958c7510af21571c3e7d%2Fimage.png?alt=media)

Additionally, check to see the dataset you select has a "Model" tag on it, and/or "Try Pre-Trained" model on the project's landing page in Roboflow Universe, or it will not be available within your Workspace as a training checkpoint.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-14049633fcb9e91b62bc91ba0e5358e5e92fa0d8%2Fimage.png?alt=media" alt=""><figcaption><p>The Model tag on a Roboflow Universe dataset</p></figcaption></figure>

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-4dbbbb822f7cda125a21e42fa4f60212731e8b5c%2Fimage.png?alt=media" alt=""><figcaption><p>"Try Pre-Trained Model" and the Model tag on a Roboflow Universe dataset's landing page</p></figcaption></figure>

Now, within the Roboflow Main App UI, navigate to the "Versions" page of your target dataset/project. Select the version you wish to train.

* You can only start a training job from a dataset version that has not already been trained with Roboflow Train (no green checkmark is present on the version).

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-b5549aaae79978a496141c807cf099b923cafd99%2Fimage%20(13)%20(1)%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

Click "Start Training."

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cc81ffe0a64b210d637a4153693f8eeda553e2bf%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Next, choose the Fast or Accurate model, and click "Continue."

* If you are training a Single-Label Classification, Multi-Label Classification, or Semantic Segmentation project, you will not have this Fast or Accurate option. For these project types, you can just click "Continue," and then "Start Training" to kick off your training job.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-3ea915d3e069aa27e5b45f405d3a0b02826426bf%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Under "Select a Model," choose the project name for the dataset you marked (Starred) in Roboflow Universe.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-7f59867b5f0b1055d6602711ad24eacc98a354ed%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Now click "Start Training" to begin your training job. You will receive an email to the account email on file when the training job is complete.

### [Viewing Your Training Results](https://docs.roboflow.com/train/training-results)

You can monitor your training job's progress. The UI will show your machine starting up to begin training.

### Deploying Your Model

After training, your model is ready to be used for inference and embedded in a custom application! See the [Inference Documentation page](https://docs.roboflow.com/inference) for all the options.

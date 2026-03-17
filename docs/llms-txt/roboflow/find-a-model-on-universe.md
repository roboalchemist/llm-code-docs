# Source: https://docs.roboflow.com/roboflow/roboflow-ko/universe/find-a-model-on-universe.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/universe/find-a-model-on-universe.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/universe/find-a-model-on-universe.md

# Source: https://docs.roboflow.com/universe/find-a-model-on-universe.md

# Find a Model on Universe

Over 50,000 datasets on Universe also have trained models associated with the dataset. These models can be used in your computer vision project with [Workflows](https://docs.roboflow.com/workflows/what-is-workflows).

To find a dataset on Universe, type in what you want to identify into the search bar. On the search page, check the "Has a Model" box:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-e9331847a6d5051b0ab94801e3b41e5f1b604929%2FScreenshot%202025-05-20%20at%2010.13.45.png?alt=media" alt=""><figcaption></figcaption></figure>

This will refine your search to only datasets that contain trained models.

Click on a result to find out more about the project.

The dataset home page will show metrics. These metrics will depend on the model type. For object detection, for example, you will see mAP, precision, and recall; for classification you will see accuracy.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-e6246e7a169c34a612ea5bf819f4c98847b7299f%2FScreenshot%202025-05-20%20at%2010.16.39.png?alt=media" alt=""><figcaption></figcaption></figure>

You can upload an image into the "Try This Model" section to try the most recent model version.

You can also click "Models" in the sidebar to see all trained models and choose one to try:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-4b0f7ab4489c3f79e4e5fe12bc4c8088419e73dc%2FScreenshot%202025-05-20%20at%2010.15.59.png?alt=media" alt=""><figcaption></figcaption></figure>

When you open the Models page, you will see the results from an example image in the project test set plotted onto the image:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6f7da6ce88c6c3eff016730b6377c23f6e564482%2FScreenshot%202025-05-20%20at%2010.17.56.png?alt=media" alt=""><figcaption><p>The class "occupied forklift" is identified in the image.</p></figcaption></figure>

### Use a Universe Model in a Workflow

You can use Universe models in Workflows.

To use a model, open Roboflow Workflows, [create a Workflow](https://docs.roboflow.com/workflows/create-a-workflow), then add a model block:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-5e588c8be0059a1de9090e02248140917b9fa86d%2FScreenshot%202025-05-20%20at%2010.19.30.png?alt=media" alt=""><figcaption></figcaption></figure>

Click "Model" in the block editor to select a model:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-b6304df12505582edb50238bd18c6204a3d056f1%2FScreenshot%202025-05-20%20at%2010.20.13.png?alt=media" alt=""><figcaption></figcaption></figure>

Then, click the Public Models tab:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-478007ad46ea8bfcb0061813edea32792d65d756%2FScreenshot%202025-05-20%20at%2010.21.10.png?alt=media" alt=""><figcaption></figcaption></figure>

Go back to the Universe model page that corresponds with the model you want to use and click the copy icon to copy the model ID. This appears at the top of the model page:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-4cafb009a0fddff802142865602a86f938966ddb%2FScreenshot%202025-05-20%20at%2010.21.46.png?alt=media" alt=""><figcaption></figcaption></figure>

Then, paste the model ID into the Public Models search bar:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-39554bbd2c1badf1d49b2a79feb218d7a432ab28%2FScreenshot%202025-05-20%20at%2010.20.10.png?alt=media" alt=""><figcaption></figcaption></figure>

Click "Use model ID" to use the model.

Your Workflow block will now use the Universe model.

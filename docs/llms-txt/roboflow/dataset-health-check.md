# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/dataset-health-check.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/dataset-health-check.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/dataset-health-check.md

# Source: https://docs.roboflow.com/datasets/dataset-health-check.md

# Dataset Analytics

Dataset Analytics shows a range of statistics about the dataset associated with a project. You can see the following pieces of information:

* Number of images in your dataset;
* Number of annotations;
* Average image size;
* Median image ratio;
* Number of missing annotations;
* Number of null annotations;
* Image dimensions across your dataset;
* Object count histogram, and;
* A heatmap of annotation locations.

Using Dataset Analytics, you can derive a range of insights about your dataset. For example, if you have no null annotations, you may want to consider adding a few depending on the project on which you are working; if there are images with missing annotations, you can dig deeper to add the requisite annotations.

To see Dataset Analytics for a project, click "Analytics" in the left sidebar of a project:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-088e5e12e4a8d3196e187a5b4d97bffb73d7cc9a%2FScreenshot%202025-05-19%20at%2011.49.32.png?alt=media" alt=""><figcaption></figcaption></figure>

The Dataset Analytics tab will then open:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-4dab0946c168b9f6f769eeba3e07ae10e075b2c8%2FScreenshot%202025-05-19%20at%2011.51.10.png?alt=media" alt=""><figcaption></figcaption></figure>

On this page, you can see:

* A breakdown of the number of classes in the images in your train, test, and valid datasets.
* An overview of the sizes and aspect ratios of the images in your dataset.
* A heatmap showing where most of your annotations are.
* A histogram showing how many classes are annotated in each image in your dataset.

### Dimension Insights

The Dimension Insights section describes the sizes and aspect ratios of raw images in your dataset.

If you apply the Resize augmentation when you create a project version — which we strongly recommend for almost all use cases — images in your version will be resizes, but the raw images will stay the same.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-8935ad4d22a4d55d4c53a676164a03f364ce7d67%2FScreenshot%202025-06-09%20at%2011.38.21.png?alt=media" alt=""><figcaption></figcaption></figure>

### Annotation Heat Map

When you are training a model, it is important that your dataset is representative of the conditions in which your model will be deployed.

If your model will be deployed in an environment in which annotations may appear anywhere in the camera frame — for example, on a factory line where objects of different sizes are moving in real time, or in an image taken on a phone of an object — it is important that you annotate objects that appear in different places in an image.

Labeling objects in different parts of an image will ensure your model doesn't overfit to learn only how to identify objects in specific places.

The Annotation Heat Map shows where there are more or less annotations in images. This can be used to identify scenarios where your dataset annotations are too concentrated in a particular place.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-e2b93242f6a34898ac5f12ed79be48e3e9531e35%2FScreenshot%202025-06-09%20at%2011.40.13.png?alt=media" alt=""><figcaption></figcaption></figure>

You can drag over an area in the Heat Map to see images in the chosen range:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6148d58b35b272cd092604e6902d9bdefd04809b%2FScreenshot%202025-06-09%20at%2011.45.20.png?alt=media" alt=""><figcaption></figcaption></figure>

### Histogram of Object Count by Image

This shows you the distribution of how many annotated objects appear in each image.

If images that you pass through your model may contain multiple instances of an object, we recommend ensuring your dataset contains images with different numbers of object instances. This will help you ensure your model can generalise well to images with no, one, or multiple objects of interest.

Here if an example of a histogram:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-f6bdf31894a57af06ca4b95039e6c4fb05959f26%2FScreenshot%202025-06-09%20at%2011.49.58.png?alt=media" alt=""><figcaption></figcaption></figure>

You can select any of the bars on the histogram to see images with a given count:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cd8792293afc23a08597db128922600f0ae84ddd%2FScreenshot%202025-06-09%20at%2011.50.30.png?alt=media" alt=""><figcaption></figcaption></figure>

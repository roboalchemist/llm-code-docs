# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/ai-labeling/automated-annotation-with-autodistill.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/ai-labeling/automated-annotation-with-autodistill.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/ai-labeling/automated-annotation-with-autodistill.md

# Source: https://docs.roboflow.com/annotate/ai-labeling/automated-annotation-with-autodistill.md

# Auto Label

{% hint style="info" %}
Auto Label is one of many [AI Labeling](https://docs.roboflow.com/annotate/ai-labeling) features. Using this feature will consume [credits](https://docs.roboflow.com/billing/credits) at the rates listed on our [credits page](https://roboflow.com/credits).
{% endhint %}

Roboflow Auto Label lets you use large foundation vision models (i.e. Grounding DINO) or Roboflow trained models to automatically label images.

Roboflow Auto Label will try to use the following models to identify the objects you specify:

* Grounding DINO (Object detection)
* Grounded SAM (Segmentation)
* CLIP (Single- and multi-label classification)
* Models trained in Roboflow ([train](https://docs.roboflow.com/train/train "mention"))
  * Note: Only models from the same dataset as your Annotation Batch are currently supported.

Auto Label is powered by [Autodistill](https://github.com/autodistill/autodistill), an open source framework for auto-labeling image datasets developed by Roboflow.

Auto Label has been used to label millions of images for use in training computer vision models.

### When to Use Roboflow Auto Label

You should use Roboflow Auto Label if you need to annotate common objects such as vehicles (i.e. forklifts), people, generic defects (i.e. cracks), and generic products (i.e. vinyl records, bread).

You should not use foundation models in Autodistill if you need to identify specific variants of an object. For example, Autodistill cannot distinguish between different types of crack, or identify unique defects in electronics.

## Label Data with Roboflow Auto Label

The Roboflow platform lets you preview how Autodistill will perform on labeling classes of data in your dataset. Then, Roboflow will share a code snippet that you can use to auto-label images on your own hardware. You can upload your labeled dataset back to Roboflow for quality assurance (recommended) and to train a model.

### Step #1: Upload Data

First, upload data to Roboflow. See our [adding-data](https://docs.roboflow.com/datasets/adding-data "mention") instructions for more information.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-fe3c09375969482e7a921eedaf3d020b21ca43b8%2FScreenshot%202024-03-26%20at%2008.59.56.png?alt=media" alt=""><figcaption><p>Uploading images into Roboflow.</p></figcaption></figure>

### Step #2: Enter Auto Label

Once you have uploaded all of your images, you will be asked how you want to label your images. Select "Auto Label".

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-950d476161ba6ec84080f5e3baeef2181f55ad31%2FScreenshot%202024-03-26%20at%2009.00.42.png?alt=media" alt="" width="353"><figcaption><p>Select "Auto Label" to open the Roboflow Auto Label interface.</p></figcaption></figure>

### Step #3: Configure Auto Label

The Auto Label labeling interface will appear in which you can configure your auto labeling job.

#### Classes (& Descriptions)

Classes represent the labels you want to assign to objects in the image. Descriptions represent a visual description of the class that your chosen foundation model (Grounding DINO by default) will use to identify instances of those classes. By default, the description will be the class name.

Auto Label works best when labeling common objects with clear visual descriptions. For example, Auto Label will be able to identify the location of an aluminum can on a production line. But, Auto Label will be unable to label images according to specific requirements, such as distinguishing the brand of an aluminum can.

#### Generating Test Results

Once you have configured Auto Label, click "Generate Test Results" to test your classes on a small subset of your dataset. By default, four images are selected.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-f67fac5e50f37beb91c4defd53c49db449550de2%2FScreenshot%202024-03-26%20at%2009.02.20.png?alt=media" alt=""><figcaption><p>The Auto Label interface.</p></figcaption></figure>

### Step #4: Evaluate Roboflow Auto Label Labels

Here are the test results when using the class "aluminum can" on an example image. From here, you can:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-763dd88db20f8172858d8f9e57401986d1977def%2FScreenshot%202024-03-22%20at%2011.33.02.png?alt=media" alt=""><figcaption><p>Auto Label annotating aluminum cans.</p></figcaption></figure>

#### Adjust your classes & descriptions

If Auto Label doesn't label images as expected, try testing different descriptions for your classes.

{% hint style="info" %}
All test results are free & don't use any credits.
{% endhint %}

#### Adjust the confidence

The number to the right of each class is represented as (boxes of this class that are shown) / (total boxes of this class). You can adjust the confidence threshold of each class to filter out more or less boxes. Higher confidence means less boxes will be shown.

{% hint style="info" %}
The confidence threshold set here will be the same one used when labeling the entire batch, so make sure it looks right!
{% endhint %}

#### Test on different images

To review Auto Label's performance on different images from your batch, click on an image in the "Test images" section on the bottom left. The preview for that image should load immediately without pressing additional buttons.

### Run Auto Label On Your Batch

If Auto Label labels your images as you expect, click "Auto Label with This Model". Review the summary modal, and click to proceed. It should take a few minutes to label a thousand images.

Auto Label will run in the background, so you can sit back and relax until it's time to review results.

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/adding-data.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/adding-data.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/adding-data.md

# Source: https://docs.roboflow.com/datasets/adding-data.md

# Upload Images, Videos, and Annotations

The first step to training and deploying a model with Roboflow is to upload data to a Project.

First, you will need to [create a Project](https://docs.roboflow.com/datasets/create-a-project).

Then, you will be taken to a web page from which you can upload data. You can also access this page from the "Upload Data" button available in your project sidebar.

## How to Add Data

You can add data to your Roboflow account by:

* Using the web application: Recommended for datasets with fewer than 1,000 images.
* Using the command line: Recommended for datasets with greater than 1,000 images.
* Using the Dataset Upload Workflow Block: Recommended for collecting data from Workflows with a model already in production.

From the web application and command line, you can upload:

* JPG, PNG, WEBP, AVIF, and BMP images.\*
* MOV and MP4 videos.
* PDF files.
* [Annotations in any supported format.](https://roboflow.com/formats)

\**Max size of 20MB and 16,400 x 10,900 pixels.*

You can only upload annotations with their associated images. You cannot upload annotations for images that have already been imported into your dataset.

## Upload Data with the Web Application

When you create a project, or on the Upload Data page, you will see a box into which you can drag and drop images, videos, and annotations:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-deb24c5aa34b10e1ccab8bec61e7f55ed2f8c273%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

[Over 40+ annotation formats are supported.](https://roboflow.com/formats) The formats supported vary based on your project type.

<details>

<summary>How file names are processed</summary>

We sanitize class names both at upload/import and export so image file names can be standardized. At upload and dataset export, we perform the following:

* Trimming leading/trailing whitespace
* All whitespace (including newlines & tabs) are converted to a space
* Double spaces are removed
* `/.[]#~*` characters are replaced with a dash (`-`)
* `|'"` characters are removed

</details>

### Upload Video

Uploaded videos are broken up into individual frames you can annotate. If you upload a video, a window will open from which you can choose how often frames are sampled for use in your dataset:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cf44e0be4457594150131cc10df8421038599b3e%2FScreenshot%202025-05-20%20at%2007.52.45.png?alt=media" alt=""><figcaption></figcaption></figure>

Once you click "Choose Frame Rate", your video will be split up into frames. These frames will then be uploaded to your dataset.

Once you have uploaded your dataset, you will be able to assign the data for labeling.

Once you drop them into the Web UI, a dialog box will ask you to choose the **frame rate**. This will tell us how many images we should sample from your video per second.

* The highest frame rate you can select is 60 frames per second, which will generate 60 images for each second of video you upload.
* The lowest frame rate you can select is 1 frame per 60 seconds.

After sampling from your video, the images will appear as if you had originally uploaded images to Roboflow.

<details>

<summary>Supported video file formats</summary>

Roboflow uses your browser's built in support for video files to parse videos into frame images that you can use to train your models. That means you can use many different video formats, including MOV and MP4 files, depending on what browser you are using.

You can [check which video formats are supported by your browser](https://caniuse.com/?search=video%20format).

Note that e.g. HEVC/H.265 encoded MP4 files are only supported by the Safari browser. If you are importing from a GoPro or iPhone that shoots in H.265 you may want to change the settings to H.264 which is more widely supported.

If you are having trouble getting your video file loaded into Roboflow, you can post on our [forum](https://discuss.roboflow.com/) or contact your account representative.

</details>

## Upload Datasets with the Command Line

You can upload larger datasets using the Roboflow Python command line interface.

You can only upload images with the command line interface. If you have videos, you will need to [split them into frames saved as files](https://superuser.com/questions/1044444/how-do-i-use-ffmpeg-to-split-a-video-into-images-and-then-reassemble-exactly-the). These files can then be uploaded to Roboflow.

To get started, first install `roboflow-python`:

```
pip install roboflow
```

Next, [retrieve your Workspace ID](https://docs.roboflow.com/developer/rest-api/workspace-and-project-ids).

Finally, prepare a command in the following format:

```
roboflow import -w testupload -p project-1-8zgld /path/to/dataset/folder
```

Here are the arguments you need to specify:

* `-w testupload`: This is the workspace name.
* `-p <project-id>`: This is your project ID.

When you run the command, you will see a message that indicates the upload process has started. You will then see logs as images upload:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cb3c6b1fff1fa6883a6fb226f8a3704493263a70%2FCleanShot%202024-03-13%20at%2011.29.09%402x.png?alt=media" alt=""><figcaption><p>Uploading a dataset using the command-line</p></figcaption></figure>

We have a video walkthrough that shows how to upload data from the command line:

{% embed url="<https://www.loom.com/share/19637984033a466b831af56f9404fa89>" %}

## View Your Uploaded Data

All data uploaded to Roboflow is uploaded in a "batch". These batches can be viewed on your Project Annotate page:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-e02e3663f94fef52256a1528c2361066bcc4d89f%2FScreenshot%202025-05-20%20at%2008.04.10.png?alt=media" alt=""><figcaption></figcaption></figure>

## Image Size limits

The maximum size for an image is 20 MB

The maximum pixel dimensions are 16,400 × 10,900 pixels.

## Duplicate Images

If you try to upload an image that is already in a Project, upload for that image will be skipped.

{% hint style="info" %}
If you [merge two datasets](https://docs.roboflow.com/merge-datasets), the merged dataset and the two original datasets exist in your account. Therefore, there is no charge for the merge, because the images are duplicates.
{% endhint %}

## Data Ownership

You retain ownership over all images and videos you upload to Roboflow. This is defined in [our Section 23B of our Terms of Service](https://roboflow.com/terms):

> You retain all ownership rights in any content, information, or materials You post, submit, publish, display, or transmit

## Data Privacy

**Public Plan:** If you are on the Public plan unless explicitly specified and arranged by Roboflow, your datasets will be public on Roboflow Universe.

**Paid Plans (including Enterprise):** Unless otherwise specified, your data is private to your account.

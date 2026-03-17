# Source: https://docs.roboflow.com/developer/command-line-interface/download-a-dataset.md

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/download-a-dataset.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/download-a-dataset.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/download-a-dataset.md

# Source: https://docs.roboflow.com/datasets/download-a-dataset.md

# Download a Dataset

To download a dataset from Roboflow, you must first [create a dataset version](https://docs.roboflow.com/datasets/dataset-versions/create-a-dataset-version).

{% hint style="info" %}
Refer to the [Download a Roboflow Universe Dataset](https://docs.roboflow.com/universe/download-a-universe-dataset) documentation if you want to download a dataset from Roboflow Universe.
{% endhint %}

Navigate to the Version that you want to download in the Roboflow dashboard. Then, click the "Download Dataset" button in the top right corner:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-ccc91c1b06f21a5306598939a72594c14228b893%2FScreenshot%202025-05-20%20at%2017.46.17.png?alt=media" alt=""><figcaption></figcaption></figure>

A modal will appear giving you options for formats to download your data as. Roboflow supports [over 50 different annotation formats](https://roboflow.com/formats).

You can also choose to either download your dataset directly as a zip file or be provided with a code snippet to download the data locally.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-7436741ed93bdc6acc7e65a247bf8bc1297e0f50%2FScreenshot%202025-05-20%20at%2017.48.19.png?alt=media" alt=""><figcaption></figcaption></figure>

If you choose the code option, you will be able to choose from a Python code snippet, a curl command, or a direct download link to your dataset.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-071f28d85175df4ce367e59b4ae84f4f8346d2bf%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

## FAQs

<details>

<summary>Why don't my zipped image counts match the UI?</summary>

There are two possibilities for this:

* An image randomly failed to download in the respective cloudly service.
* The image is corrupt or too large, leading to some errors.

Our application only generates the export zip once and then re-downloads the same export if the same format (e.g. COCO) is selected. If you ever notice that the image count is off in the download, you can always create a new version and re-download.

\\

</details>

<details>

<summary>Are the downloaded images the original quality?</summary>

No. To prevent training slowdowns, we compress images at a level that maintains a balance between training speed and resolution needed for sufficient model performance.

If you're looking to download a single original quality image, you can do so by clicking on a image on your dataset and selecting "Download Image".

If you're looking to download multiple original quality images, we recommend using our [CLI](https://docs.roboflow.com/developer/command-line-interface/download-a-dataset) or our [Image Search API](https://docs.roboflow.com/developer/search-images-in-a-dataset).

</details>

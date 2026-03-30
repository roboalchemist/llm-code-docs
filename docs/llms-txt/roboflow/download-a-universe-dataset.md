# Source: https://docs.roboflow.com/roboflow/roboflow-ko/universe/download-a-universe-dataset.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/universe/download-a-universe-dataset.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/universe/download-a-universe-dataset.md

# Source: https://docs.roboflow.com/universe/download-a-universe-dataset.md

# Download a Universe Dataset

You can download a Universe dataset in [any format supported by Roboflow](https://roboflow.com/formats).

You may want to download a dataset if you want to train a model in a notebook.

If you want to train a model in the cloud on Roboflow, we recommend [forking a Universe dataset](https://docs.roboflow.com/universe/fork-a-universe-dataset) instead of downloading it. Forking a dataset lets you upload a dataset from Universe without downloading it to your computer and re-uploading it.

### How to Download a Universe Dataset

To download a Universe dataset, navigate to a dataset on Universe. Then, click "Dataset" in the left sidebar:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-0e4e98200ac10d3d4662ee76a582a2acf9c825ab%2FScreenshot%202025-05-20%20at%2010.27.50.png?alt=media" alt=""><figcaption></figcaption></figure>

You will be taken to a page where you can see information about the dataset, including the images in the dataset version, the dataset split, and the preprocessing and augmentation steps applied to the dataset:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c4fbd58af623d4dce57c9eefb27367e0ba2c51ab%2FScreenshot%202025-05-20%20at%2010.28.10.png?alt=media" alt=""><figcaption></figcaption></figure>

To download the dataset, click Download Dataset. A window will appear with options on how to download the dataset:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2e7fd91821f975bd9cc1b327eeafac5f5c5707b8%2FScreenshot%202025-05-20%20at%2010.25.44.png?alt=media" alt=""><figcaption></figcaption></figure>

There are three options:

* Train a model with this dataset: [Fork the dataset](https://docs.roboflow.com/universe/fork-a-universe-dataset) into your workspace for use in training.
* Train from a portion of this dataset: Select specific images to import into an existing project.
* Download dataset: Download the full dataset as a ZIP file.

To download a dataset as a ZIP, select "Download dataset" then click "Continue".

You will then be able to choose into what format you want to export your data:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-8c620ec94a7117ecfa034fce65e168364b0b6630%2FScreenshot%202025-05-20%20at%2010.30.37.png?alt=media" alt=""><figcaption></figcaption></figure>

There are two download options:

* Download as a ZIP
* Show download code

The "Show download code" option is ideal if you are going to train your model in a notebook.

If you download as a ZIP, a ZIP file will be prepared and start downloading.

If you opt to show a download code, you will see options for downloading your data in a notebook or in your terminal.

{% hint style="info" %}
All datasets are subject to the license described on the Universe project landing page. [Learn how to find the license under which a dataset is licensed](https://docs.roboflow.com/universe/find-a-dataset-on-universe#roboflow-universe-dataset-licenses).
{% endhint %}

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/train/train/train-from-google-cloud.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/torningu/train/train-from-google-cloud.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/train/train/train-from-google-cloud.md

# Source: https://docs.roboflow.com/train/train/train-from-google-cloud.md

# Train from Google Cloud

{% hint style="info" %}
This training option is only available on Enterprise plans.
{% endhint %}

## Google Cloud Platform Training Integration

Once you've created a version of your dataset in Roboflow, you can export it directly to Google Cloud Platform Vision AutoML for training.

### **Pre-requisites:**

**Dataset version in Roboflow:**

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-9db1cb471a11b238ed077439555a0b63d44809e4%2Fimage%20\(34\)%20\(1\).png?alt=media)

**Google Cloud Platform account**

### **Training in Google Cloud Vision AutoML**

1\. Export your dataset in the "Google Cloud AutoML" format

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-f70c208400dabf2f1147158fef8b4d9276424770%2Fimage.png?alt=media)

2\. Copy the resulting link you're provided, and click "Continue to Cloud Vision." Ensure you're logged into Google Cloud Platform in the same browser as your Roboflow account.

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-63317002ac727f4e6ea3d3543b300d99760fcdd8%2Fimage.png?alt=media)

3\. Once in Google Cloud Platform, select "New Dataset," the type of dataset you exported from Roboflow (e.g. Object Detection) and proceed by clicking "Create Dataset"

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-4c85a90e746e73eb04c85f664193de66cfb3faf6%2Fimage.png?alt=media)

4\. Paste your link from Roboflow into the "Destination on Cloud Storage" bucket option.

From here, your dataset version is successfully imported to GCP Vision AutoML, and you can proceed with training in GCP.

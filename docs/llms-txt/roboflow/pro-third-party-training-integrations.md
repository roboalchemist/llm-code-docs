# Source: https://docs.roboflow.com/roboflow/roboflow-ko/train/train/pro-third-party-training-integrations.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/torningu/train/pro-third-party-training-integrations.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/train/train/pro-third-party-training-integrations.md

# Source: https://docs.roboflow.com/train/train/pro-third-party-training-integrations.md

# Train from Azure Vision

{% hint style="info" %}
This training option is only available on Enterprise plans.
{% endhint %}

## Microsoft Azure Custom Vision Training Integration

Once you've created a version of your dataset in Roboflow, you can export it directly to Microsoft Azure Custom Vision for training.

### **Pre-requisites:**

A dataset version in Roboflow:

![Example generated dataset version in Roboflow](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-9db1cb471a11b238ed077439555a0b63d44809e4%2Fimage%20\(34\)%20\(1\).png?alt=media)

**A Custom Vision project in Microsoft Azure:**

![Example Custom Vision project in Microsoft Azure](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-867f52eabb58942485e21c66baab6abd2d614d25%2Fimage%20\(22\)%20\(1\)%20\(1\).png?alt=media)

### Setup: Adding Your Microsoft Azure API Keys to Roboflow

1\. Select your project name in Microsoft Azure

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-df68122ff892972083b24d3453d6fff448652a5e%2Fimage.png?alt=media)

2\. Select API Key under "1" in order to take you to this page:

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-33a74bf192645b5bc8dd49e82d6316b916ba32ad%2Fimage%20\(26\)%20\(1\)%20\(1\).png?alt=media)

We'll copy the keys from this page to your Roboflow Workspace.

\
3\. Navigate to your Roboflow Workspace's API keys in settings by clicking the dropdown menu n the Workspace.

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-1c1ffbc2eafa76ce3df646eb3641017559354d4d%2Fimage.png?alt=media)

You'll see "API Keys" as a sub menu:

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-53de50b52904d7fbc5d330e4d42f90add716561d%2Fimage.png?alt=media)

4\. Copy **KEY 1** from your Microsoft Azure account to the **"training-key"** in Roboflow

*NOTE: For datasets larger than 1000 images, Azure will require S0 pricing tier.*

5\. Update the **Endpoint** field in Roboflow to match the **Endpoint** field from your Microsoft Custom Vision project.

From here, you're ready to start training with Roboflow and Microsoft Custom Azure together. Steps 1-5 only need to be completed once. To continue training with Azure, proceed.

### **Training in Azure Custom Vision**

6\. Once you've generated a dataset version, export the project as "Azure Custom Vision."

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-ec6ab52ca98080f185b0a7b92cde6a6367efa3eb%2Fimage.png?alt=media)

The project will automatically upload to your Azure account, and you'll be able to proceed with training there.

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-85da5d5bf20f385a4baabadb33f54ce8c46323b8%2Fimage.png?alt=media)

(Note: ensure you're logged into your Microsoft Azure account in the same browser as your Roboflow account.)

Your exported dataset version will appear directly in your Azure account.

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-93eccd93d9698a4d0356dc48228e8775006f7975%2Fimage.png?alt=media)

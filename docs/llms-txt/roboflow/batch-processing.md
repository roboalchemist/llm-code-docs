# Source: https://docs.roboflow.com/changelog/explore-by-month/march-2025/batch-processing.md

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/batch-processing.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/batch-processing.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/batch-processing.md

# Source: https://docs.roboflow.com/deploy/batch-processing.md

# Batch Processing

Batch Processing is a cost-effective way to run [Workflows](https://docs.roboflow.com/workflows/what-is-workflows) on batches of images and stored videos. It's ideal for asynchronously processing large amounts of data.

Batch Processing automatically provisions the infrastructure needed to run a large batch.

You can configure a Batch Processing job through the Roboflow web interface or through our API (via the CLI).

When you start a job, machines will be provisioned in the cloud to process your data. You will then receive a JSON file with the output from the Workflow you chose to run on your data.

The following video explains Batch Processing in depth:

{% embed url="<https://www.youtube.com/watch?v=S7K2j2IeQrM>" %}

### Create a Batch Processing Job

To create a Batch Processing job, click Deployments in the left sidebar of your Roboflow dashboard. Then, click on the "Batch Jobs" tab:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-1193fa943b014f1b279c123ad5ccc88fac10f551%2FScreenshot%202025-05-19%20at%2012.14.51.png?alt=media" alt=""><figcaption></figcaption></figure>

Click "New Batch Job" to create a Batch Processing job.

A window will open in which you can configure your job:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-10667231b1e727c9344565e52171e0d1cb26b90c%2FScreenshot%202025-05-19%20at%2012.16.27.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Choose a Workflow

To start configuring a job, first select a Workflow. If you do not already have a Workflow, refer to our Workflows documentation to get started.

#### Upload Images or Videos

Next, you need to upload the images or videos on which you want to run your Workflow.

#### Configure Hardware

You can run your Batch Processing job on a CPU or a GPU. GPU jobs are faster but more expensive.

For pricing information, refer to the Roboflow pricing documentation.

Select either a CPU or GPU for your job:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-18c4999be68bfb6ede2dccb3ecd3fcc1d3c593c7%2FScreenshot%202025-05-19%20at%2012.19.21.png?alt=media" alt=""><figcaption></figcaption></figure>

Several advanced configuration options are also available under the "Advanced Options" tab. We recommend leaving these options as the default.

#### Start the Job

To start the Batch Processing job, click "Create Batch Job".

The infrastructure for your job will be provisioned and processing will begin.

### Monitor Job Progress

When you start your job, a status indicator will appear indicating when processing is being configured, when the batch data is being processed, and when the job is complete.

You can monitor how much of a batch has been processed in real time.

The amount of time it will take to process your data depends on how many images.

### Create a Batch Processing Job with the Roboflow CLI

To create a Batch Processing job with the Roboflow CLI, refer to our [Batch Processing developer documentation](https://inference.roboflow.com/workflows/batch_processing/about/#cli).

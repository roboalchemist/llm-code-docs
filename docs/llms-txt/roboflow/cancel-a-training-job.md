# Source: https://docs.roboflow.com/roboflow/roboflow-ko/train/cancel-a-training-job.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/torningu/cancel-a-training-job.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/train/cancel-a-training-job.md

# Source: https://docs.roboflow.com/train/cancel-a-training-job.md

# Cancel a Training Job

A model training job can be canceled at any time using the "Cancel Training" button.

If you cancel a training job, the job will stop. If you cancel early in the training process, your credits will be refunded. If you are many epochs into training, no refund will be issued.

When you cancel a training job, the weights used in training will not be saved. This is in contrast to [Early Stopping](https://docs.roboflow.com/train/stop-training-early), which lets you stop a training job and save the weights. Early Stopping charges you for used training credits since you will end up with a model you can train.

To cancel a training job, click the "Cancel Training" button:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6746685187a307ad6d29d783e4ff353856cbc175%2FScreenshot%202025-05-19%20at%2011.41.51.png?alt=media" alt=""><figcaption></figcaption></figure>

After canceling a job, you can still train a model using the same dataset version.

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/train/training-results.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/torningu/training-results.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/train/training-results.md

# Source: https://docs.roboflow.com/train/training-results.md

# View Training Results

Training graphs let you see the status of your model during training. Training graphs are available for all models trained on Roboflow.

You will also see metrics that summarise your model performance.

The metrics you will see will depend on your model type:

* Object detection projects show the precision, recall, and mAP of the model.
* Classification projects show accuracy.
* Segmentation and keypoint models show mAP score.
* Multimodal models show perplexity.

## During Training

After you start training a model, a message will appear on the dataset version page associated with the model you are training. This message will first say that a training machine is starting.

You will then see training graphs appear live as your model trains:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-60a42e0f454daf4899e4d270bbec386e5c482a73%2FScreenshot%202025-05-20%20at%2013.05.35.png?alt=media" alt=""><figcaption><p>Training graphs as a model trains.</p></figcaption></figure>

## After Training

When your model has finished training, you can view metrics from the training process.

To find your training graphs for a model after training, first click the Models tab in the sidebar:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-eba886ca21455e8f0b4be719f06596c84ce34d30%2FScreenshot%202025-05-20%20at%2007.34.41.png?alt=media" alt=""><figcaption></figcaption></figure>

Then, click on the model version whose training graphs you want to see.

Scroll down on the page until you see the Training Graphs section:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-784d68e6d838a5b38ba5c53552c97a121119197d%2FScreenshot%202025-05-20%20at%2007.35.41.png?alt=media" alt=""><figcaption></figcaption></figure>

## Test Your Model

You can test your model on an image from the Visualize page. Visualize is a good way to run quick checks to see how your model performs before you build your application logic in Workflows.

The Visualize feature works for object detection, segmentation, classification, and keypoint models. Visualize is not supported for multimodal projects.

To test a model, click Visualize on the right sidebar. The Visualize page will then open:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-d0c91f352d8f443b384a189a93a1e0314b5a6758%2FScreenshot%202025-05-20%20at%2007.38.37.png?alt=media" alt=""><figcaption></figcaption></figure>

The Visualize tab will show several images from your test set from which you can select to run on your model. You can also uplaod your own images and videos, or try with your webcam.

To find deployment instructions for your model, click Try on My Machine. You can also deploy your model on Roboflow Workflows.

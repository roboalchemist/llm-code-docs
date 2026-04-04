# Source: https://docs.roboflow.com/roboflow/roboflow-ko/train/evaluate-trained-models.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/torningu/evaluate-trained-models.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/train/evaluate-trained-models.md

# Source: https://docs.roboflow.com/train/evaluate-trained-models.md

# Evaluate Trained Models

Model evaluations show:

1. A production metrics explorer, which helps you find the optimal confidence threshold at which to run your model;
2. Model improvement recommendations, which provide suggestions on how you can increase the accuracy of your model;
3. Performance by class, which shows how well your model identifies different classes;
4. A confusion matrix, which you can use to find specific classes on which your model thrives and struggles, and;
5. An interactive vector explorer which lets you identify clusters of images where your model does well or poorly;

You can use model evaluation to identify areas of improvement for your model.

Model evaluations are automatically run for all versioned models trained on, or uploaded to Roboflow by paid users. It may take several minutes for an evaluation to run for a dataset of a few hundred images, and several hours for large datasets with thousands or more images.

### Open Model Evaluation

To find the confusion matrix and vector explorer for your model, open any trained model version in your project. Then, click the "View Evaluation" button:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-8c6db60420e1905df8d6f3c824f91f0f219e8a76%2FScreenshot%202025-05-14%20at%2014.41.23.png?alt=media" alt=""><figcaption></figcaption></figure>

A window will open where you can view your confusion matrix and vector analysis.

### Production Metrics Explorer

The production metrics explorer shows the Precision, Recall, and F1 score for your model at all possible confidence thresholds. This information is presented on a graph.

Using these statistics, the production metrics explorer will recommend an "optimal confidence". This is the threshold that will give you the best Precision/Recall/F1 Score trade-off.

You can use this tool to help inform the confidence threshold you set for your model in production.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cf7be3e1155f28ab47c87709fe072e767b536898%2FScreenshot%202025-07-23%20at%2011.15.02.png?alt=media" alt=""><figcaption></figcaption></figure>

You can drag the slider to see the F1/Precision/Recall values at difference confidence thresholds:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c0f91bfa945e226cba1bdb659ef70c507779add8%2FScreenshot%202025-07-23%20at%2011.15.39.png?alt=media" alt=""><figcaption></figcaption></figure>

### Model Improvement Recommendations

The model improvement recommendations section of your model evaluation lists suggestions on how you can increase the accuracy of your model. These improvements are based on the results of the confusion matrix calculated with your model. (See more information on your confusion matrix later on this page).

The model improvement recommendations feature can make suggestions related to:

* How to improve a model that predicts many false negatives.
* How to improve a model that predicts many false positives.
* What classes are often confused (mis-identified).
* What classes need more data to improve accuracy.
* When a test or validation set may be too small.
* And more.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cb54b251f5e115f9a1eb549b0c03117d5b263b3b%2FScreenshot%202025-07-23%20at%2011.17.09.png?alt=media" alt=""><figcaption></figcaption></figure>

### Performance by Class

The performance by class chart shows how many correct predictions, misclassifications, false negatives, and false positives there are across all classes in your dataset.

You can use this information to see, at a glance, which classes your model can identify well and the classes our model struggles to identify.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-ffaf491bbb2d955905c575d90aeb04a4fd94f257%2FScreenshot%202025-07-23%20at%2011.18.34.png?alt=media" alt=""><figcaption></figcaption></figure>

If your dataset has a large number of classes, you can focus the chart on specific classes by opening the "All Classes" dropdown and selecting the classes you want to highlight:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-9656c52d9fc2be6f7da56bcd9bd4f2538677dba3%2FScreenshot%202025-07-23%20at%2011.19.30.png?alt=media" alt=""><figcaption></figcaption></figure>

You can also see how this chart changes at different confidence thresholds by moving the Confidence Threshold slider:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-443ab7ce57aba56477ab17435cb9f27f622fe7c1%2FScreenshot%202025-07-23%20at%2011.20.12.png?alt=media" alt=""><figcaption></figcaption></figure>

By default, this chart will use the optimal confidence threshold we recommend.

### Confusion Matrix

Your confusion matrix shows how well your model performs on different classes.

Your confusion matrix is calculated by running images from your test and validation sets with your trained model. The results from your model are then compared with the "ground truth" from your dataset annotations.

With the confusion matrix tool, you can identify:

* Classes where your model performs well.
* Classes where your model identifies the wrong class for an object (false positives).
* Instances where your model identifies an object where none is present (false negatives).

Here is an example confusion matrix:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cd0af50fa3e0c4158310901798a285245a9d87bc%2FScreenshot%202025-07-23%20at%2011.20.53.png?alt=media" alt=""><figcaption></figcaption></figure>

If your model detects many classes, scroll bars will appear that let you navigate your confusion matrix.

By default, the confusion matrix shows how your model performs when run at the optimal threshold calculated for your model.

You can adjust the confidence threshold using the Confidence Threshold slider. Your confusion matrix, precision, and recall will update as you configure the slider:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-37d06af76a4e8f6a660dec67c79f30d7d47e67ea%2FScreenshot%202025-07-23%20at%2011.21.19.png?alt=media" alt=""><figcaption></figcaption></figure>

You can click on each box in the confusion matrix to see what images appear in the corresponding category.

For example, you can click any box in the "False Positive" column to identify images where an object was identified where one was not present in your ground truth data.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-5372c962df1b4125d6d89098a5b43ea4df21e74c%2FScreenshot%202025-07-23%20at%2011.22.08.png?alt=media" alt=""><figcaption></figcaption></figure>

You can click on an individual image to enter an interactive view where you can toggle between the ground truth (your annotations) and the model predictions:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-15edd76d7c3b4f61ddd86e3581a91b90f0b72608%2FScreenshot%202025-07-23%20at%2011.22.30.png?alt=media" alt=""><figcaption></figcaption></figure>

Click "Ground Truth" to see your annotations and "Model Predictions" to see what your model returned.

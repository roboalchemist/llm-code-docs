# Source: https://docs.roboflow.com/changelog/explore-by-month/june-2025/model-evaluation-for-roboflow-instant-models.md

# Model Evaluation for Roboflow Instant Models

{% embed url="<https://www.loom.com/share/dbf456ea90fa4b88a63b43467d882e73?sid=c16b8ede-270c-4a42-91a3-b767b6660ce3>" %}

You can now run [Model Evaluations](https://docs.roboflow.com/train/evaluate-trained-models) on [Roboflow Instant models](https://docs.roboflow.com/train/roboflow-instant).

This release lets you:

* Access tools like the Confusion Matrix, Vector Analysis, and view Precision and Recall metrics for Instant models
* Compare Ground Truth vs Predictions in the image viewer
* Runs on validation and test set images
* Supports custom confidence thresholds for Instant (90–99%) → Use the confidence slider to explore optimal confidence

Evaluations trigger automatically after Instant training if your dataset contains images in the valid or test datasets. You can also trigger a model evaluation manually for existing models as long as you have valid or test images in your dataset.

This feature is available for all Roboflow Instant models.<br>

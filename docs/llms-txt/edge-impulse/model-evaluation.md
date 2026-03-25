# Source: https://docs.edgeimpulse.com/knowledge/metrics/model-evaluation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Model evaluation

In **Edge AI**, where models are deployed on resource-constrained devices like microcontrollers, evaluation metrics are critical. They ensure that your model performs well in terms of accuracy and runs efficiently on the target hardware. By understanding these metrics, you can fine-tune your models to achieve the best balance between performance and resource usage.

These metrics serve several important purposes:

* **Model Comparison:** Metrics allow you to compare different models and see which one performs better.
* **Model Tuning:** They help you adjust and improve your model by showing where it might be going wrong.
* **Model Validation:** Metrics ensure that your model generalizes well to new data, rather than just memorizing the training data (a problem known as overfitting).

## When to Use Different Metrics

Choosing the right metric depends on your specific task and the application's requirements:

* **Precision**: Needed when avoiding false positives, such as in medical diagnosis. (Read on [Scikit-learn Precision](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html) | Read on [TensorFlow Precision](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision))
* **Recall**: Vital when missing detections is costly, like in security applications. (Read on [Scikit-learn Recall](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html) | Read on [TensorFlow Recall](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Recall))
* **Lower IoU Thresholds**: Suitable for tasks where rough localization suffices.
* **Higher IoU Thresholds**: Necessary for tasks requiring precise localization.

Understanding these metrics in context ensures that your models are not only accurate but also suitable for their intended applications.

## Types of Evaluation Metrics

<Tabs>
  <Tab title="Classification Metrics">
    <Frame caption="Classification Metrics">
      <img src="https://mintcdn.com/edgeimpulse/IkcBZl70N8rCiFhA/.assets/images/metrics1.png?fit=max&auto=format&n=IkcBZl70N8rCiFhA&q=85&s=c792dbef9405f7fc24935faccf910834" width="1454" height="462" data-path=".assets/images/metrics1.png" />
    </Frame>

    Used for problems where the output is a category, such as detecting whether a sound is a cough or not:

    * **Accuracy**: Measures the percentage of correct predictions out of all predictions. For instance, in a model that classifies sounds on a wearable device, accuracy tells you how often the model gets it right. (Read on [Scikit-learn Accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) | Read on [TensorFlow Accuracy](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy))

      $$
      \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
      $$

      * ( TP ): True Positives
      * ( TN ): True Negatives
      * ( FP ): False Positives
      * ( FN ): False Negatives
    * **Precision**: The percentage of true positive predictions out of all positive predictions made by the model. This is crucial in cases where false positives can have significant consequences, such as in health monitoring devices. (Read on [Scikit-learn Precision](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html) | Read on [TensorFlow Precision](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision))

      $$
      \text{Precision} = \frac{TP}{TP + FP}
      $$
    * **Recall**: The percentage of actual positive instances that the model correctly identified. For example, in a fall detection system, recall is vital because missing a fall could lead to serious consequences. (Read on [Scikit-learn Recall](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html) | Read on [TensorFlow Recall](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Recall))

      $$
      \text{Recall} = \frac{TP}{TP + FN}
      $$
    * **F1 Score**: The harmonic mean of precision and recall, useful when you need to balance the trade-offs between false positives and false negatives. (Read on [Scikit-learn F1 Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html) | Read on [TensorFlow F1 Score](https://www.tensorflow.org/addons/api_docs/python/tfa/metrics/F1Score))

      $$
      \text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
      $$
    * **Confusion Matrix**: A table that shows the number of correct and incorrect predictions made by the model. It helps visualize the model's performance across different classes. (Read on [Scikit-learn Confusion Matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html) | Read on [TensorFlow Confusion Matrix](https://www.tensorflow.org/api_docs/python/tf/math/confusion_matrix))

    <Frame caption="Confusion Matrix for Activity Recognition (UCI HAR Dataset - Simulated)">
      <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/confusion_matrix_real_dataset_updated.png?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=ff272c8de8913bf1a0f5df6f6a914431" width="640" height="480" data-path=".assets/images/confusion_matrix_real_dataset_updated.png" />
    </Frame>

    This confusion matrix helps evaluate the performance of the model by showing where it is performing well (high values along the diagonal) and where it is making mistakes (off-diagonal values).

    Here's how to interpret it:

    * **Labels**: The "True label" on the Y-axis represents the actual class labels of the activities. The "Predicted label" on the X-axis represents the class labels predicted by the model.
    * **Classes**: The dataset seems to have three classes, represented as 0, 1, and 2. These likely correspond to different human activities.
    * **Matrix Cells**: The cells in the matrix contain the number of samples classified in each combination of actual versus predicted class.
      * For instance: The top-left cell (44) indicates that the model correctly predicted class 0 for 44 instances where the true label was also 0.
      * The off-diagonal cells represent misclassifications. For example, the cell at row 0, column 1 (29) shows that 29 samples were true class 0 but were incorrectly predicted as class 1.
    * **Color Scale**: The color scale on the right represents the intensity of the values in the cells, with lighter colors indicating higher values and darker colors indicating lower values.
    * **ROC-AUC**: The area under the receiver operating characteristic curve, showing the trade-off between true positive rate and false positive rate. (Read on [Scikit-learn ROC-AUC](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html) | Read on [TensorFlow AUC](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/AUC))

      * The ROC curve plots **True Positive Rate (Recall)** against **False Positive Rate (FPR)**, where:

        $$
        \text{FPR} = \frac{FP}{FP + TN}
        $$

    <Frame caption="ROC Curve for Walking vs Rest (UCI HAR Dataset - Simulated)">
      <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/roc_curve_real_dataset_updated.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=463e77a070073e0ad443106435e55b44" width="640" height="480" data-path=".assets/images/roc_curve_real_dataset_updated.png" />
    </Frame>

    The **ROC (Receiver Operating Characteristic) curve** is a commonly used tool for evaluating the performance of binary classification models. The ROC curve plots the trade-off between the true positive rate (TPR or Recall) and the false positive rate (FPR) for different threshold values.

    * **True Positive Rate (Y-axis)**: This is the proportion of actual positives (walking instances) that the model correctly identifies (recall).
    * **False Positive Rate (X-axis)**: This is the proportion of actual negatives (rest instances) that the model incorrectly identifies as positives (false positives).
    * **Precision-Recall Curve**: Useful in evaluating binary classification models, especially when dealing with imbalanced datasets, like in the context of walking vs resting activities. The Precision-Recall curve shows the trade-off between precision and recall for various threshold settings of the classifier.

      * **Precision (Y-axis)**: Precision measures the proportion of true positive predictions among all positive predictions made by the model. High precision means that when the model predicts "Walking," it is correct most of the time.
      * **Recall (X-axis)**: Recall (or True Positive Rate) measures the proportion of actual positives (walking instances) that the model correctly identifies. High recall indicates that the model successfully identifies most instances of walking.

        <Frame caption="Precision-Recall Curve for Walking vs Rest (UCI HAR Dataset - Simulated)">
          <img src="https://mintcdn.com/edgeimpulse/AQr6kHeg-keHHzV6/.assets/images/precision_recall_curve_real_dataset_updated.png?fit=max&auto=format&n=AQr6kHeg-keHHzV6&q=85&s=1590b7132f090e3f0650454c004325fb" width="640" height="480" data-path=".assets/images/precision_recall_curve_real_dataset_updated.png" />
        </Frame>
    * **Log Loss**: The negative log-likelihood of the true labels given the model predictions. (Read on [Scikit-learn Log Loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html) | Read on [TensorFlow Log Loss](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryCrossentropy))

      $$
      \text{Log Loss} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]
      $$

      * ( y\_i ): Actual label
      * ( p\_i ): Predicted probability
      * ( N ): Number of samples
  </Tab>

  <Tab title="Regression Metrics">
    Used for problems where the output is a continuous value, like predicting the temperature from sensor data:

    <Frame caption="Regression Metrics">
      <img src="https://mintcdn.com/edgeimpulse/IkcBZl70N8rCiFhA/.assets/images/metrics2.png?fit=max&auto=format&n=IkcBZl70N8rCiFhA&q=85&s=20e1ab0580d0d6f9c9a693a95bf46e97" width="1438" height="390" data-path=".assets/images/metrics2.png" />
    </Frame>

    * **Mean Squared Error (MSE)**: The average of the squared differences between the predicted values and the actual values. In an edge device that predicts temperature, MSE penalizes larger errors more heavily, making it crucial for ensuring accurate predictions. (Read on [Scikit-learn MSE](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html) | Read on [TensorFlow MSE](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/MeanSquaredError))

      $$
      \text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2
      $$

      * ( y\_i ): Actual value
      * ( \hat{y}\_i ): Predicted value
      * ( N ): Number of samples
    * **Mean Absolute Error (MAE)**: The average of the absolute differences between predicted and actual values, providing a straightforward measure of prediction accuracy. This is useful in energy monitoring systems where predictions need to be as close as possible to the actual values. (Read on [Scikit-learn MAE](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html) | Read on [TensorFlow MAE](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/MeanAbsoluteError))

      $$
      \text{MAE} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|
      $$
    * **R-Squared (R2)**: Measures how well your model explains the variability in the data. A higher R2 indicates a better model fit, which is useful when predicting variables like energy consumption in smart homes. (Read on [Scikit-learn R2 Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html) | Read on [TensorFlow R2 Score (Custom Implementation)](https://www.tensorflow.org/tfx/model_analysis/metrics#r_squared))

      $$
      R^2 = 1 - \frac{\sum_{i=1}^{N} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{N} (y_i - \bar{y})^2}
      $$

      * ( \bar{y} ): Mean of the actual values

    ### Regression Accuracy

    Regression **accuracy** is the percentage of **windowed samples** whose absolute error is within the configured threshold.

    1. **Compute window error**: For each windowed sample, compute the absolute error between prediction and ground truth
       *(for multi-output regression, a window is only correct if all outputs meet the threshold).*
    2. **Apply the threshold**: Mark the window correct if its absolute error is ≤ the configured threshold.
    3. **Accuracy**: The percentage of windowed samples marked correct.

       $$
       \text{Regression Accuracy} = \frac{\text{Number of correct windowed samples}}{\text{Total number of windowed samples}} \times 100\%
       $$
  </Tab>

  <Tab title="Object Detection Metrics">
    Used for problems where the goal is to identify and locate objects in an image, such as detecting pedestrians in a self-driving car system.

    Focusing on the COCO mAP Score:

    <Frame caption="Object Detection Metrics can be complex">
      <img src="https://mintcdn.com/edgeimpulse/IkcBZl70N8rCiFhA/.assets/images/metrics-od.png?fit=max&auto=format&n=IkcBZl70N8rCiFhA&q=85&s=ffcf6c9bc831d2ff51e522ff932b1c68" width="604" height="519" data-path=".assets/images/metrics-od.png" />
    </Frame>

    The **COCO mAP (Mean Average Precision)** score is a key metric used to evaluate the performance of an object detection model. It measures the model's ability to correctly identify and locate objects within images.

    This result shows a mAP of 0.3, which may seem low, but it accurately reflects the model's performance. The mAP is averaged over Intersection over Union (IoU) thresholds from 0.5 to 0.95, capturing the model's ability to localize objects with varying degrees of precision.

    #### How It Works

    * **Detection and Localization**: The model attempts to detect objects in an image and draws a bounding box around each one.
    * **Intersection over Union (IoU)**: IoU calculates the overlap between the predicted bounding box and the actual (true) bounding box. An IoU of 1 indicates perfect overlap, while 0 means no overlap.
    * **Precision Across Different IoU Thresholds**: The mAP score averages the precision (the proportion of correctly detected objects) across different IoU thresholds (e.g., 0.5, 0.75). This demonstrates the model's performance under both lenient (low IoU) and strict (high IoU) conditions.
    * **Final Score**: The final mAP score is the average of these precision values. A higher mAP score indicates that the model is better at correctly detecting and accurately placing bounding boxes around objects in various scenarios.

    #### IoU Thresholds

    * **mAP\@IoU=0.5 (AP50)**: A less strict metric, useful for broader applications where rough localization is acceptable.
    * **mAP\@IoU=0.75 (AP75)**: A stricter metric requiring higher overlap between predicted and true bounding boxes, ideal for tasks needing precise localization.
    * **mAP@\[IoU=0.5:0.95]**: The average of AP values computed at IoU thresholds ranging from 0.5 to 0.95. This primary COCO challenge metric provides a balanced view of the model's performance.

    #### Area-Based Evaluation

    **mAP** can also be broken down by object size—small, medium, and large—to assess performance across different object scales:

    * **Small Objects**: Typically smaller than 32x32 pixels.
    * **Medium Objects**: Between 32x32 and 96x96 pixels.
    * **Large Objects**: Larger than 96x96 pixels.

    Models generally perform better on larger objects, but understanding performance across all sizes is crucial for applications like aerial imaging or medical diagnostics.

    #### Recall Metrics

    Recall in object detection measures the ability of a model to find all relevant objects in an image:

    * **Recall@\[max\_detections=1, 10, 100]**: These metrics measure recall when considering only the top 1, 10, or 100 detections per image, providing insight into the model's performance under different detection strictness levels.
    * **Recall by Area**: Similar to mAP, recall can also be evaluated based on object size, helping to understand how well the model recalls objects of different scales.
  </Tab>
</Tabs>

## Importance of Evaluation Metrics

Evaluation metrics serve multiple purposes in the impulse lifecycle:

* **Model Selection:** They enable you to compare different models and choose the one that best suits your needs.
* **Model Tuning:** Metrics guide you in fine-tuning models by providing feedback on their performance.
* **Model Interpretation:** Metrics help understand how well a model performs and where it might need improvement.
* **Model Deployment:** Before deploying a model in real-world applications, metrics are used to ensure it meets the required standards.
* **Model Monitoring:** After deployment, metrics continue to monitor the model's performance over time.

## How to Choose the Right Metric

Choosing the right metric depends on the specific task and application requirements:

* **For classification**: In an Edge AI application like sound detection on a wearable device, precision might be more important if you want to avoid false alarms, while recall might be critical in safety applications where missing a critical event could be dangerous.
* **For regression**: If you're predicting energy usage in a smart home, MSE might be preferred because it penalizes large errors more, ensuring your model's predictions are as accurate as possible.
* **For object detection**: If you're working on an edge-based animal detection camera, mAP with a higher IoU threshold might be crucial for ensuring the camera accurately identifies and locates potential animals.

## Conclusion

Evaluation metrics like mAP and recall provide useful insights into the performance of machine learning models, particularly in object detection tasks. By understanding and appropriately focusing on the correct metrics, you can ensure that your models are robust, accurate, and effective for real-world deployment.


Built with [Mintlify](https://mintlify.com).
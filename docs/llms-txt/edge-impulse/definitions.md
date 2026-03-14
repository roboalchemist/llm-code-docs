# Source: https://docs.edgeimpulse.com/knowledge/metrics/definitions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Definitions

## Accuracy

Accuracy is the fraction of predictions our model got right. It is defined as:

$$
accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$

## Area Under ROC Curve (AUC-ROC)

The Area Under the Receiver Operating Characteristic Curve (AUC-ROC) is a performance measurement for classification problems. The ROC curve is a plot of true positive rate (recall) against the false positive rate (1 - specificity). The AUC represents the degree or measure of separability, and it tells how much the model is capable of distinguishing between classes. The higher the AUC, the better the model. It is defined as:

$$
AUC = \int_{0}^{1} TPR(f) \, df
$$

where:

* (TPR) is the true positive rate (recall),
* (f) is the false positive rate.

## Cross-Entropy Loss

Cross-Entropy Loss is a measure used to quantify the difference between two probability distributions for a given random variable or set of events. It is defined as:

$$
H(y, \hat{y}) = -\sum_{i} y_i \log(\hat{y}_i)
$$

## Explained Variance Score

The Explained Variance Score measures the proportion to which a mathematical model accounts for the variation (dispersion) of a given data set. It is defined as:

$$
\text{Explained Variance} = 1 - \frac{\text{Var}(y - \hat{y})}{\text{Var}(y)}
$$

where:

* (\text{Var}(y - \hat{y})) is the variance of the errors,
* (\text{Var}(y)) is the variance of the actual values.

An Explained Variance Score close to 1 indicates that the model explains a large portion of the variance in the data.

## F1 Score

The F1 score is a harmonic mean of precision and recall, providing a balance between them. It is calculated as:

$$
F1 = 2 \cdot \frac{precision \cdot recall}{precision + recall}
$$

where:
[precision](/knowledge/metrics/definitions#precision)
[recall](/knowledge/metrics/definitions#recall)

## IoU (Intersection over Union) for Object Detection

IoU is a measure of the overlap between two bounding boxes. It is defined as:

$$
IoU = \frac{area\_of\_overlap}{area\_of\_union}
$$

## mAP (Mean Average Precision)

Mean Average Precision (mAP) is a common metric used to evaluate object detection models. It summarizes the precision-recall curve for different classes. It is calculated as:

$$
mAP = \frac{1}{N} \sum_{i=1}^{N} AP_i
$$

where:

* (N) is the number of classes,
* (AP\_i) is the Average Precision for class (i).

Average Precision (AP) is computed as the area under the precision-recall curve for a specific class. It integrates the precision over all recall values from 0 to 1. For object detection, AP can be calculated at different [IoU](/knowledge/metrics/definitions#iou-intersection-over-union-for-object-detection) thresholds to provide a comprehensive evaluation.

In addition to the standard mAP, specific metrics include:

* mAP@\[IoU=50]: mAP at 50% IoU threshold.
* mAP@\[IoU=75]: mAP at 75% IoU threshold.
* mAP@\[area=small]: mAP for small objects.
* mAP@\[area=medium]: mAP for medium objects.
* mAP@\[area=large]: mAP for large objects.

## Mean Absolute Error (MAE)

Mean Absolute Error (MAE) measures the average magnitude of the errors in a set of predictions, without considering their direction. It is calculated as:

$$
MAE = \frac{1}{n} \sum{(i=1)}^{n} |y_i - \hat{y}_i|
$$

where:

* (n) is the number of data points,
* (y\_i) is the actual value,
* (\hat{y}\_i) is the predicted value.

## Mean Squared Error (MSE)

Mean Squared Error (MSE) measures the average of the squares of the errors—that is, the average squared difference between the estimated values and the actual value. It is calculated as:

$$
MSE = \frac{1}{n} \sum{(i=1)}^{n} (y_i - \hat{y}_i)^2
$$

where:

* (n) is the number of data points,
* (y\_i) is the actual value,
* (\hat{y}\_i) is the predicted value.

## Precision

Precision indicates the accuracy of positive predictions. It is defined as:

$$
precision = \frac{TP}{TP + FP}
$$

where:

* (TP) is the number of true positives,
* (FP) is the number of false positives,
* (FN) is the number of false negatives.

## Recall

Recall measures the ability of a model to find all relevant cases within a dataset. It is defined as:

$$
recall = \frac{TP}{TP + FN}
$$

where:

* (TP) is the number of true positives,
* (FP) is the number of false positives,
* (FN) is the number of false negatives.

Recall for object detection can also be specified with additional parameters:

* Recall@\[max\_detections=1]: Recall when considering only the top 1 detection per image.
* Recall@\[max\_detections=10]: Recall when considering the top 10 detections per image.
* Recall@\[max\_detections=100]: Recall when considering the top 100 detections per image.
* Recall@\[area=small]: Recall for small objects.
* Recall@\[area=medium]: Recall for medium objects.
* Recall@\[area=large]: Recall for large objects.

## Sigmoid Function

The Sigmoid function is used for binary classification in logistic regression models. It is defined as:

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

## Softmax Function

The Softmax function is used for multi-class classification. It converts logits to probabilities that sum to 1. It is defined for class (j) as:

$$
\sigma(z)_j = \frac{e^{z_j}}{\sum{(k=1)}^{K} e^{z_k}} \; \text{for} \; j = 1, ..., K
$$

## Weighted Average F1 Score

Weighted Average F1 Score takes into account the F1 score of each class and the number of instances for each class. It is defined as:

$$
Weighted\ Average\ F1\ Score = \sum{(i=1)}^{n} \left( \frac{TP_i + FN_i}{TP + FN} \cdot F1_i \right)
$$

where:

* (n) is the number of classes,
* (TP\_i) is the true positives for class (i),
* (FN\_i) is the false negatives for class (i),
* (TP) is the total number of true positives,
* (FN) is the total number of false negatives,
* (F1\_i) is the F1 score for class (i).

## Weighted Average Precision

Weighted Average Precision takes into account the precision of each class and the number of instances for each class. It is defined as:

$$
Weighted\ Average\ Precision = \sum{(i=1)}^{n} \left( \frac{TP_i + FN_i}{TP + FN} \cdot Precision_i \right)
$$

where:

* (n) is the number of classes,
* (TP\_i) is the true positives for class (i),
* (FN\_i) is the false negatives for class (i),
* (TP) is the total number of true positives,
* (FN) is the total number of false negatives,
* (Precision\_i) is the precision for class (i).

## Weighted Average Recall

Weighted Average Recall takes into account the recall of each class and the number of instances for each class. It is defined as:

$$
Weighted\ Average\ Recall = \sum{(i=1)}^{n} \left( \frac{TP_i + FN_i}{TP + FN} \cdot Recall_i \right)
$$

where:

* (n) is the number of classes,
* (TP\_i) is the true positives for class (i),
* (FN\_i) is the false negatives for class (i),
* (TP) is the total number of true positives,
* (FN) is the total number of false negatives,
* (Recall\_i) is the recall for class (i).


Built with [Mintlify](https://mintlify.com).
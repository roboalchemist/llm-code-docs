# Source: https://docs.galileo.ai/galileo-ai-research/errors-in-object-detection.md

# Errors In Object Detection

> This page describes the rich error types offered by Galileo for Object Detection

An Object Detection (OD) model receives an image as input and outputs a list of rectangular boxes representing objects within the image. Each box is associated with a label/class and can be positioned anywhere on the image. Unlike other tasks with limited output spaces (such as single labels in classification or labels and spans in NER), OD entails a significantly larger number of possible outputs due to two factors:

1. The model can generate a substantial quantity of boxes (several thousand for YOLO before NMS).

2. Each box can be positioned at any location on the image, as long as it has integer coordinates.

This level of freedom necessitates the use of complex algorithms to establish diverse pairings between predictions and annotations, which in turn gives very rich error types. In this article we will explain what these error types are and how to use Galileo to focus on any of them and fix your data.

For a high-level introduction to error types and Galileo see [here](/galileo/how-to-and-faq/galileo-product-features/error-types-breakdown).

## The 6 Error Types

The initial stage in assigning error types to flawed boxes involves identifying the boxes that are not deemed correct. We will refer to inaccurate predictions as False Positives (FP) and erroneous annotations as False Negatives (FN). There are many ways in which a predicted box can turn into a FP, so we will classify them further in more granular buckets:

* **Duplicate Error:** the predicted box highly overlaps with an annotation that is already used

* **Classification Error:** the predicted box highly overlaps with an annotation of different label

* **Localization Error:** the predicted box slightly overlaps with an annotation of same label

* **Classification and Localization Error:** the predicted box slightly overlaps with an annotation of different label

* **Background Error:** the predicted box does not even slightly overlap with an annotation.

Similarly, some FN annotations will be assigned the following error type:

* **Missed Error:** the annotation was not used by any prediction (either used to declare a prediction a TP or used to bin a prediction in any of the above errors).

The following illustration summarizes the above discussion:

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-1.png)

Note that the above error types were introduced in the [TIDE toolbox](https://dbolya.github.io/tide/) paper. We refer to their paper and to the Technical deep dive below for more details.

## The 6 error types and Galileo

### Count and Impact on mAP

In the Galileo Console, we surface two metrics for each of the 6 error types: their count and their impact on mAP. The count is simply the number of boxes tagged with that error type, and the impact on mAP is the amount by which mAP would increase if we were to fix all errors of that type.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-2.png)

We suggest starting analyzing the error with highest impact on mAP and trying to understand why the model and annotations disagree.

### Focus on a single Error Type to gain insight

Galileo allows you to focus on any of the error types in order to dig and understand in each case whether the data quality is poor or the model is not well trained. For this you can either click on an error type in the above bar chart, or simply add the error type filter by clicking on Add Filters.

Once a single error type is selected, Galileo will only display the boxes with that error type together with any other box that is necessary context in order to explain that error type.

For example, a prediction is tagged as a classification error because it significantly overlaps with an annotation of different label. In this case, we will show this annotation and its label.

We refer to the Technical deep dive below for more details on associated boxes.

### Improve your data quality

Galileo offers the possibility to fix your annotations in a few clicks from the console. After adding a filter by error type, select the images with miss-annotated boxes either one-by-one, or by selecting them all and, if any, unselecting the images with correct annotations.

<Frame caption="Update your annotations in a few clicks from the console.">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-3.png" />
</Frame>

Clicking on Overwrite Ground Truth will overwrite the annotation with the prediction that links to that annotation. More concretely, we explain below the typical scenario for every error type.

* **Duplicate error:** this is often a model error, and duplicates can be reduced by decreasing the IoU threshold in the NMS step. However, sometimes a duplicate box will have more accurate localization that both the TP prediction and the annotation, in which case we would overwrite the annotation with the duplicate box.

  <Frame caption="  The inner prediction has higher confidence than the larger box, and is thus selected as a TP. The duplicated outer prediction is however a better bounding box than both the TP prediction and the annotation..">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-4.png" />
  </Frame>

* **Classification error:** more often than not, classification errors in OD represent mislabeled annotation. Correcting this error would simply relabel the annotation with the predicted one. Note that these errors have overlap with the Likely Mislabeled feature.

<Frame caption=" Typical classification error where the annotation is mislabeled.">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-5.png" />
</Frame>

* **Localization error:** localization errors surface inaccuracies in the annotations localization. Correcting this error would overwrite the annotation's coordinates with the predicted ones. Note that this error is very sensitive to the IoU threshold chosen (the mAP threshold).

  <Frame caption="Localization error exhibiting an inaccurate annotation.">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-6.png" />
  </Frame>

* **Classification and Localization error:** these errors are less predictable and can be due to various phenomena. We suggest going through these images one-by-one and taking action accordingly.

* **Background error:** more often than not a background error is due to a missed annotation. In this setting, the Overwrite Ground Truth button adds the missing annotation.

* **Missed error:** these errors are sometimes due to the model not predicting the appropriate box, and sometimes due to poor annotations. Some common scenarios include:

  * poor/gibberish annotations that do not represent an object or do not represent an object that we want to predict

    <Frame caption="The annotation does not represent any object.">
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-7.png" />
    </Frame>

  * multiple annotations for the same object

    <Frame caption="There are multiple annotations for the same object.">
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-8.png" />
    </Frame>

    In this case, overwriting the ground truth means removing the bad annotation.

## The 6 error types: Technical deep dive

In this section, we will elaborate on our methodology for determining the suitable error type associated with a box that fails to meet the criteria for correctness.

### Coarse Errors: FPs and FNs

The first step consists of a coarser association is determining all wrong predictions (False Positives, FP), and all wrong annotations (False Negatives, FN). This algorithm is also used for calculating the main metric in Object Detection: the mean Average Precision (mAP). We summarize the steps necessary for finding our error types, and refer to a [modern definition](https://jonathan-hui.medium.com/map-mean-average-precision-for-object-detection-45c121a31173) for more details:

1. Pick a global IoU threshold. This is used to decide when two boxes overlap enough to be paired together.

2. Loop over labels. For every label, only consider the predictions and annotations of that label.

3. Sort all predictions descending by their score and go through them one by one. At the beginning all annotation are unused.

4. If a prediction overlaps enough with an unused annotation: call that prediction at True Positive (TP) and declare that annotation as used.

5. If it doesn't, call that prediction a FP.

6. When all predictions are exhausted, call all unused annotations become FNs.

The Galileo console offers three IoU thresholds: 0.5, 0.7 and 0.9. Note that the higher the threshold, the harder it is for a prediction to be a TP as it has to considerably overlap with a detection. Moreover, this is even harder for smaller objects, where moving a box by a few pixels dramatically decreases the IoU.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-9.png)

### Finer Errors: The 6 Error Types of TIDE

The 6 error types cited above were introduced in the [TIDE toolbox](https://dbolya.github.io/tide/) paper, to which we refer for more details. For a concise definition, we will re-use the illustration posted above.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-10.png)

The `[0,1]` interval appearing below the image indicates the range (in orange) for the IoU between the predicted box (in red) and an annotated box (in yellow). Note that it contains two thresholds: the background threshold `t_b` and the foreground threshold `t_f`. Galileo sets the background threshold `t_b` at `0.1` and the foreground threshold `t_f` at the `mAP threshold` used to compute the mAP score. As an example, a predicted box overlapping with an annotation with `IoU >= t_f` will be given the classification error type if the class of the annotation doesn't match that of the prediction.

With the above ambiguous definition, there are cases where a predicted box could be part of multiple error types. To avoid ambiguity, Galileo classifies the errors in the following order:

1. **Localization**

2. **Classification**

3. **Duplicate**

4. **Background**

5. **Classification and Localization.**

That is, we check in order, if the predicted box

1. has IoU with an annotation with same label in the range `[t_b, t_f]`

2. has IoU with an annotation with different label in the range `[t_f, 1]`

3. has IoU with an annotation already used, with same label in the range `[t_f, 1]`

4. has IoU `< t_b` with all annotations.

If none of these occur, then the box is a classification and localization error (it is easy to see that this implies that the prediction has IoU in the range `[t_b, t_f]` with a box of different label).

Finally, the **Missed** error type is given to any annotation that is already considered a FN, and that was not used in the above definition by either a Classification Error or a Localization Error. Note that Missed annotations can overlap with predictions, for example, they can overlap `< t_b` with a classification and localization error.

### Associated boxes

The above definitions beg for better terminology. We will say that an annotation is associated with a prediction, or that a prediction links to an annotation in any of the following cases

* the prediction is a TP corresponding to the annotation

* the prediction is an FP (except background error), and the annotation is the one involved in the IoU deciding so.

For example, if a predicted box is tagged as a classification error, it will link to the annotations with which it overlaps and has a different label. In particular, this associated annotation explains the error type of the predicted box and provides the necessary context to understand the error.

<Frame caption="The predicted box is a localization error. Without the context of the associated annotation, this would be confusing since the prediction looks correct. With the context, one can see that the annotation is inaccurate and should be updated.">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/object-detection-error-11.png" />
</Frame>

The Galileo Console will always show the context in order to explain all error types. This explains why predicted boxes will be visible when filtering and only showing Missed errors, or why annotations will be visible when filtering for, say, Classification errors.

Note that an annotation can be associated with multiple predictions (the simplest case to see is for a TP and a duplicate, but there are countless other possibilities). With this definition, one can notice that a Missed error is an annotation that is either associated with no box or only a classification and localization error (or multiple, but this is rare).

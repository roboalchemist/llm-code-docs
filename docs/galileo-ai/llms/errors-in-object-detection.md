# Source: https://docs.galileo.ai/galileo-ai-research/errors-in-object-detection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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

<img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-1.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c7060d592b001bc073375f045dd9da71" alt="" data-og-width="2816" width="2816" data-og-height="874" height="874" data-path="images/object-detection-error-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-1.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c1e9d13a211e9630173db627ea4108ed 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-1.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=9acde55f2f2f5d74759319934fff0698 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-1.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=9f938f651ef9c34399ccd209cfaf5bdb 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-1.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=3eca663fa11080b88317762c2d64dafc 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-1.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=5212470f864ddf2b31b1a409ae870e5c 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-1.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=4f97cc4c083fdb131f32e449ee83b6d7 2500w" />

Note that the above error types were introduced in the [TIDE toolbox](https://dbolya.github.io/tide/) paper. We refer to their paper and to the Technical deep dive below for more details.

## The 6 error types and Galileo

### Count and Impact on mAP

In the Galileo Console, we surface two metrics for each of the 6 error types: their count and their impact on mAP. The count is simply the number of boxes tagged with that error type, and the impact on mAP is the amount by which mAP would increase if we were to fix all errors of that type.

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-2.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=40a966e19b9bc1f3e587a7c64c4da1a1" alt="" data-og-width="407" width="407" data-og-height="373" height="373" data-path="images/object-detection-error-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-2.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=f3c9f333c8f881f8c58e608aaa475596 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-2.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=a8539f19535b49cbac6840eb0be38551 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-2.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d32848846ad84fa664d574297de91a63 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-2.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=3b8d5c0492e2b14d6b7e582e5baa4efe 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-2.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=55749e6e74222396aa6c7c7b2b8d100a 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-2.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=bfbed0ce3790ca4deec7d28be9cee8b8 2500w" />

We suggest starting analyzing the error with highest impact on mAP and trying to understand why the model and annotations disagree.

### Focus on a single Error Type to gain insight

Galileo allows you to focus on any of the error types in order to dig and understand in each case whether the data quality is poor or the model is not well trained. For this you can either click on an error type in the above bar chart, or simply add the error type filter by clicking on Add Filters.

Once a single error type is selected, Galileo will only display the boxes with that error type together with any other box that is necessary context in order to explain that error type.

For example, a prediction is tagged as a classification error because it significantly overlaps with an annotation of different label. In this case, we will show this annotation and its label.

We refer to the Technical deep dive below for more details on associated boxes.

### Improve your data quality

Galileo offers the possibility to fix your annotations in a few clicks from the console. After adding a filter by error type, select the images with miss-annotated boxes either one-by-one, or by selecting them all and, if any, unselecting the images with correct annotations.

<Frame caption="Update your annotations in a few clicks from the console.">
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-3.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=6c8906af8af29367fcbf2be414cbc62f" data-og-width="1186" width="1186" data-og-height="616" height="616" data-path="images/object-detection-error-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-3.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ba6fe85585a73162b315f561d37017a1 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-3.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=1063f6eba6d1e42a2a366f4cdb4969b9 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-3.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=740e246e2a140817e85c22a0866eea85 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-3.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=27f5a28124e02eb53601cfdf5bfa5e18 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-3.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ff5a7b27b01560a5bc936506ff7a1bca 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-3.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b8356710c1422e6bbffa515c8de48733 2500w" />
</Frame>

Clicking on Overwrite Ground Truth will overwrite the annotation with the prediction that links to that annotation. More concretely, we explain below the typical scenario for every error type.

* **Duplicate error:** this is often a model error, and duplicates can be reduced by decreasing the IoU threshold in the NMS step. However, sometimes a duplicate box will have more accurate localization that both the TP prediction and the annotation, in which case we would overwrite the annotation with the duplicate box.

  <Frame caption="  The inner prediction has higher confidence than the larger box, and is thus selected as a TP. The duplicated outer prediction is however a better bounding box than both the TP prediction and the annotation..">
    <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-4.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=999df20cff7d2140d099d1cd00271c6a" data-og-width="238" width="238" data-og-height="182" height="182" data-path="images/object-detection-error-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-4.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=5953a7ed1d4c66d94d0070d8a393d22a 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-4.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=f0368d00692342282cf56123f9c517ae 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-4.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b072a01c6542ccf19fc8210d0ecf536d 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-4.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ed9395ff17d30aa99eb0c0605f864930 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-4.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=1815782ece806bc76f899ac962557be5 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-4.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=573dbb08fd6e9ae8405565b1afed4650 2500w" />
  </Frame>

* **Classification error:** more often than not, classification errors in OD represent mislabeled annotation. Correcting this error would simply relabel the annotation with the predicted one. Note that these errors have overlap with the Likely Mislabeled feature.

<Frame caption=" Typical classification error where the annotation is mislabeled.">
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-5.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=99c2a891168230a0e0e29ce3cf021224" data-og-width="269" width="269" data-og-height="221" height="221" data-path="images/object-detection-error-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-5.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d2ff41be4c1bb8e82bd6876d8d057741 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-5.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=30196a424659e76ffd6fde17e0bbf500 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-5.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=3ec48aeab9474ccab4efa9f6c276e80d 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-5.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=93195bc0f4680f894129239e1159b994 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-5.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d4e4c29b05263c1b0930f06bc0a8f2a4 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-5.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=90a0d4b6db2b391a80e54ba547ac7aa6 2500w" />
</Frame>

* **Localization error:** localization errors surface inaccuracies in the annotations localization. Correcting this error would overwrite the annotation's coordinates with the predicted ones. Note that this error is very sensitive to the IoU threshold chosen (the mAP threshold).

  <Frame caption="Localization error exhibiting an inaccurate annotation.">
    <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-6.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=0e2fe49065a0849d3357e2d3174e186d" data-og-width="276" width="276" data-og-height="370" height="370" data-path="images/object-detection-error-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-6.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=855d5828cd19ceff4a5846af6246cd45 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-6.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=000a203d07bec644543b62972230bd88 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-6.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=35bbfff03c41df3f9f6a8608ca6082cc 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-6.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=de6884bb69e46bb80391b2420812b9d1 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-6.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=817fd4424819507a9464f7b83a0cfc72 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-6.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d05f44873b415e43168c086e436506f9 2500w" />
  </Frame>

* **Classification and Localization error:** these errors are less predictable and can be due to various phenomena. We suggest going through these images one-by-one and taking action accordingly.

* **Background error:** more often than not a background error is due to a missed annotation. In this setting, the Overwrite Ground Truth button adds the missing annotation.

* **Missed error:** these errors are sometimes due to the model not predicting the appropriate box, and sometimes due to poor annotations. Some common scenarios include:
  * poor/gibberish annotations that do not represent an object or do not represent an object that we want to predict

    <Frame caption="The annotation does not represent any object.">
      <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-7.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b5ad83e2d275181f1bed3d6c2a855bf4" data-og-width="286" width="286" data-og-height="140" height="140" data-path="images/object-detection-error-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-7.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=34adaa588e5475f6998a7e0ce4d183c2 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-7.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=bb6ab1ef0feb51411f59f40ad4a8a4ae 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-7.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d3cc9aba1b6342e2c50ddbd2b85ab7cd 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-7.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=cd95067514147e39b3e7558cab7acbed 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-7.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=8c25c555254ee1bb308df6438a012b4d 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-7.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=7c003e45df6c43aa24b1c70c254cbe04 2500w" />
    </Frame>

  * multiple annotations for the same object

    <Frame caption="There are multiple annotations for the same object.">
      <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-8.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=6558f716305891f4ae7c0236c7c70116" data-og-width="263" width="263" data-og-height="181" height="181" data-path="images/object-detection-error-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-8.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=5c26595bd88d0c79afc94c26331bbd20 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-8.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=e623019375148bbe79434c8eef0a764d 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-8.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=1225a027e54f36ce1c76cdce682ebe05 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-8.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=c90dfa1d7e6d453f2ff7473c51d8f3f3 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-8.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=54548b186ae1e207ee2aecc583a2f8ae 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-8.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=fe3a8ebc522c56a4c4365b918198f98a 2500w" />
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

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-9.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=3689758916be0bffd15521f21f5b9521" alt="" data-og-width="444" width="444" data-og-height="238" height="238" data-path="images/object-detection-error-9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-9.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=83d374aa421f3ff4920d192e491bae69 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-9.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=2da0a9ae3c09e0cff717106afbc7024a 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-9.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=37d07b51d994fd956fdc8f94f631d0eb 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-9.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ca611cd982e10799c95c485fbab79849 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-9.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=71ec459cc4da8a88e58318fde56f218c 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/object-detection-error-9.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=091a789273ecd7e9eb3a51025b8d3e7f 2500w" />

### Finer Errors: The 6 Error Types of TIDE

The 6 error types cited above were introduced in the [TIDE toolbox](https://dbolya.github.io/tide/) paper, to which we refer for more details. For a concise definition, we will re-use the illustration posted above.

<img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-10.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=56187956d8e05c1df23a61d39a14980e" alt="" data-og-width="2816" width="2816" data-og-height="874" height="874" data-path="images/object-detection-error-10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-10.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=581a5d09c53b2be7e78eed224188b2a3 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-10.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=e481095f57872e5d844f199f24ca1fee 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-10.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=e26285cd1e8796d2043007e70fe36da2 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-10.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=5f1ca6a8b7aed6d598a15972d59b9bd3 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-10.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=fc78bef8e23d0b284fde0fccd5f6b390 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-10.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=44146a62a8d6d1ec599924722c05e114 2500w" />

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
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-11.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=2df19931548b9a7966277e21b80266a9" data-og-width="399" width="399" data-og-height="291" height="291" data-path="images/object-detection-error-11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-11.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=48a0587ede86c5668fe8449aedc370a2 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-11.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=b4e7dfc0a6f8720417ffb9d0b2ad0430 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-11.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=0ae2102ad63763b5deecfb641e050928 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-11.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d1097a8ec1b9519d9a16c7d6b07d7fa2 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-11.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c60633f7ca14ec5c50f44269b7eb12fa 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/object-detection-error-11.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d33af01eddcc32d92c52cbd9e54d129d 2500w" />
</Frame>

The Galileo Console will always show the context in order to explain all error types. This explains why predicted boxes will be visible when filtering and only showing Missed errors, or why annotations will be visible when filtering for, say, Classification errors.

Note that an annotation can be associated with multiple predictions (the simplest case to see is for a TP and a duplicate, but there are countless other possibilities). With this definition, one can notice that a Missed error is an annotation that is either associated with no box or only a classification and localization error (or multiple, but this is rare).

# Source: https://docs.edgeimpulse.com/studio/projects/model-testing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Model testing

When collecting data, we split the dataset into training and testing sets. The model was trained with only the training set, and the testing set is used to validate how well the model will perform on unseen data. This will ensure that the model has not learned to overfit the training data, which is a common occurrence.

## Prerequisites

Make sure to have data samples on your test set, you can add data samples from the **Data Acquisition** page or the **Live Classification** page.

<Frame caption="Test dataset">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/test-dataset.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=c2c74e89129b7379a9c8872de3295f94" width="1421" height="1000" data-path=".assets/images/test-dataset.png" />
</Frame>

## Model testing

To test your model, go to **Model testing**, select the desired model version from the dropdown (either **Unoptimized (float32)** or **Quantized (int8)**), and click **Test all**. The model will classify all of the test set samples and give you an overall accuracy of how your model performed.

<Info>
  Quantized (int8) model is not enabled by default and the fist step of enabling is in the settings menu beside the **Classify all** button
</Info>

#### Float32 vs int8 models

You can choose to test your model using either the **float32** or **int8** quantized version. The **float32** version offers higher precision but may use more resources, while the **int8** quantized version is optimized for memory and computational efficiency, making it suitable for edge devices with limited resources.

To select the model format:

1. In the **Model Testing** page, open the **Model version** dropdown.
2. Choose between **Unoptimized (float32)** or **Quantized (int8)** models.
3. Click **Test all** to evaluate your model with the selected format.

This flexibility allows you to evaluate and optimize your model depending on your deployment needs.

<Frame caption="classify all test images">
  <img src="https://mintcdn.com/edgeimpulse/lnCwBUvZVOz6Veyh/.assets/images/model-testing.png?fit=max&auto=format&n=lnCwBUvZVOz6Veyh&q=85&s=ef0bcbeced8bbab8c021a8c73296ad05" width="1319" height="1000" data-path=".assets/images/model-testing.png" />
</Frame>

This is also accompanied by a confusion matrix to show you how your model performs for each class and an interactive feature explorer that lets you click on a sample to easily visualize this dedicated result.

<Frame caption="Model testing confusion matrix">
  <img src="https://mintcdn.com/edgeimpulse/lnCwBUvZVOz6Veyh/.assets/images/model-testing-results.png?fit=max&auto=format&n=lnCwBUvZVOz6Veyh&q=85&s=66f81b9ecd1ae406bdaeb1969ad0d3c6" width="710" height="1000" data-path=".assets/images/model-testing-results.png" />
</Frame>

The model testing data table has some quick actions available for each samples:

<Frame caption="Model testing data table">
  <img src="https://mintcdn.com/edgeimpulse/lnCwBUvZVOz6Veyh/.assets/images/model-testing-table.png?fit=max&auto=format&n=lnCwBUvZVOz6Veyh&q=85&s=2926343867ed99ca4d1aaf0127c1a7fc" width="1109" height="1000" data-path=".assets/images/model-testing-table.png" />
</Frame>

<Warning>
  #### Limitation for anomaly detection

  Make sure to label your samples exactly as `anomaly` or `no anomaly` in your test dataset so they can be used in the F1 score calculation for anomaly detection projects. We are working on making this more flexible.
</Warning>

Also note that the samples who does not match the known classes for the classifiers or `anomaly` for anomaly detection learning blocks are ignored from the accuracy or the F1 score calculation:

<Frame caption="Ignored samples">
  <img src="https://mintcdn.com/edgeimpulse/lnCwBUvZVOz6Veyh/.assets/images/model-testing-ignored-samples.png?fit=max&auto=format&n=lnCwBUvZVOz6Veyh&q=85&s=27b67873aa34d3bc382c2645ff033213" width="1396" height="750" data-path=".assets/images/model-testing-ignored-samples.png" />
</Frame>

## Setting confidence threshold

Every learning block has a threshold. This can be the minimum confidence that a neural network needs to have, or the maximum anomaly score before a sample is tagged as an anomaly. You can configure these thresholds to tweak the sensitivity of these learning blocks. This affects both live classification and model testing.

<Frame caption="Setting confidence threshold">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-model-testing-gmm-set-confidence-threshold.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=07136885b0a90cde855c2e1866eedc93" width="1468" height="730" data-path=".assets/images/studio-model-testing-gmm-set-confidence-threshold.png" />
</Frame>

<br />

<Frame caption="Setting confidence threshold values">
  <img src="https://mintcdn.com/edgeimpulse/lnCwBUvZVOz6Veyh/.assets/images/model-testing-confidence-threshold.png?fit=max&auto=format&n=lnCwBUvZVOz6Veyh&q=85&s=3fbd8a406557b40989238665b3f8d688" width="1600" height="810" data-path=".assets/images/model-testing-confidence-threshold.png" />
</Frame>

## Evaluating individual samples

To see a classification in detail, go to the individual sample you are want to evaluate and click the three dots next to it, then just select show classification.  This will open a new window that will display the expected outcome, and the predicted output of your model with its accuracy. This detailed view can also give you a hint on why an item has been misclassified.

<Frame caption="Classification result. Showing the conclusions, the raw data and processed features in one overview.">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-continuous-motion-live-classification.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=1eb20b49d42d027f481a8c8bcf807d11" width="675" height="1000" data-path=".assets/images/tutorial-continuous-motion-live-classification.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/blocks/anomaly-detection-custom.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Anomaly detection

The **Anomaly detection** learning block is a flexible anomaly detection option available when designing an impulse in Edge Impulse Studio. Unlike specific anomaly algorithms such as GMM or K-means, this block does **not** enforce a particular method — instead, it provides a generic container for any supported custom anomaly detection approach. This is the default destination for custom anomaly detection blocks (excluding visual anomaly detection, which uses the [Visual anomaly detection](../blocks/visual-anomaly-detection-fomo-ad) block).

## Overview

Anomaly detection is the process of learning a representation of **normal (non-anomalous)** behavior and identifying deviations from that baseline. Models trained for anomaly detection output an **anomaly score**, with higher scores indicating greater deviation from the learned normal pattern.

Typical anomaly detection workflows:

* Train on samples that **do not include anomalies**
* Build a model of normal behavior
* Evaluate new inputs to compute an anomaly score

The **Anomaly Detection** block acts as a general host for any custom algorithm that implements the expected learning block interface. This includes Edge Impulse-provided blocks and [custom learning blocks](/studio/organizations/custom-blocks/custom-learning-blocks).

## Setting up the Anomaly Detection learning block

To add this block to your impulse:

1. In Edge Impulse Studio, open **Create impulse**
2. Click **Add learning block**
3. Select **Anomaly Detection** from the list
4. Configure any available parameters exposed by your [custom learning block](/studio/organizations/custom-blocks/custom-learning-blocks) implementation
5. Click **Save impulse**

### Example configuration

Custom anomaly detection blocks may vary, but typical parameters include:

* **Thresholds** or **confidence settings** — may be exposed to control when an anomaly is triggered.
* **Model-specific hyperparameters** — depending on the algorithm.

## Train

Once configured, click **Start training** to begin learning your anomaly detection model. Unlike classification or regression, training for anomaly detection normally expects *no anomalies* in the training set.

After training completes, Edge Impulse Studio will show the training status and allowable controls such as **Model testing**.

## Testing the Anomaly Detection learning block

Navigate to the **Model testing** page and click **Classify all** to score your test dataset. You can inspect individual samples and their anomaly scores.

If your custom block supports it, you may also see options for:

* **Anomaly Explorer** visualizations of multi-dimensional feature space
* **Threshold adjustment** to tune sensitivity

## How does it work?

Unlike fixed algorithm blocks (e.g., GMM or K-means), the **Anomaly Detection** block itself does not define a specific method. Each custom block packaged under this learning block must:

1. Receive training features (from upstream processing blocks)
2. Learn a model of normal behavior
3. Output a per-sample anomaly score at inference

These steps are implemented by the custom block according to its algorithm.

## Additional resources

* [Custom blocks](/studio/organizations/custom-blocks)
* [Custom learning blocks](/studio/organizations/custom-blocks/custom-learning-blocks)
* [Bring your own model (BYOM)](/studio/projects/dashboard/byom)
* [Anomaly detection (GMM)](../blocks/anomaly-detection-gmm)
* [Anomaly detection (K-means)](../blocks/anomaly-detection-k-means)
* [Visual anomaly detection (FOMO-AD)](../blocks/visual-anomaly-detection-fomo-ad)
* [Advanced Anomaly Detection with Feature Importance](https://edgeimpulse.com/blog/advanced-anomaly-detection-with-feature-importance)


Built with [Mintlify](https://mintlify.com).
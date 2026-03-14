# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/blocks/anomaly-detection-k-means.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Anomaly detection (K-means)

Neural networks are great, but they have one big flaw. They're terrible at dealing with data they have never seen before (like a new gesture). Neural networks cannot judge this, as they are only aware of the training data. If you give it something unlike anything it has seen before it'll still classify as one of the four classes.

<Info>
  #### Tutorial

  Want to see the **Anomaly Detection (K-means)** block in action? Check out our [Continuous Motion Recognition](/tutorials/end-to-end/motion-recognition) tutorial.
</Info>

**K-means clustering**

This method looks at the data points in a dataset and groups those that are similar into a predefined number K of clusters. A threshold value can be added to detect anomalies: if the distance between a data point and its nearest centroid is greater than the threshold value, then it is an anomaly.

The main difficulty resides in choosing K, since data in a time series is always changing and different values of K might be ideal at different times. Besides, in more complex scenarios where there are both local and global outliers, many outliers might pass under the radar and be assigned to a cluster.

Looking for another anomaly detection technique? See [Anomaly detection (GMM)](/studio/projects/learning-blocks/blocks/anomaly-detection-gmm)

K-Means has some overlap with GMM. However, GMMs work using the assumption that the samples within a dataset can be modeled using different Gaussian distributions. If this is not the case for your dataset, K-Means will likely be a better option for you.

## Features importance (optional)

In most of our DSP blocks, you have the option to calculate the **feature importance**. Edge Impulse Studio will then output a Feature Importance list that will help you determine which axes generated from your DSP block are most significant to analyze when you want to do anomaly detection.

See [Processing blocks > Feature importance](/studio/projects/processing-blocks#feature-importance)

## Setting up the Anomaly Detection (K-Means) learning block

The K-Means anomaly detection learning block has two adjustable parameters:  the **Cluster count** and **The axes**

* **Cluster count**: the `K` clusters.

* **Axes**: The different axes correspond to the generated features from the pre-processing block. The chosen axes will use the features as the input data for the training.

<Info>
  Click on the **Select suggested axes** button to harness the results of the [feature importance](/studio/projects/processing-blocks#feature-importance) output.
</Info>

Click on **Start training** to trigger the learning process. Once trained you will obtain a view that looks like the following:

<Frame caption="Anomaly detection view">
  <img src="https://mintcdn.com/edgeimpulse/XwnzH-Jo3nDoEg0b/.assets/images/anomaly-view-2.png?fit=max&auto=format&n=XwnzH-Jo3nDoEg0b&q=85&s=4203d715fb25dfb961a0bc5283e9deeb" width="1600" height="947" data-path=".assets/images/anomaly-view-2.png" />
</Frame>

*Note: By definition, there should not be any anomalies in the training dataset, and thus accuracy is not calculated during training. Run Model testing to learn more about the model performance. Additionally, you can also select a test data sample in the **Anomaly Explorer** directly on this page.*

<Frame caption="Anomaly explorer">
  <img src="https://mintcdn.com/edgeimpulse/XwnzH-Jo3nDoEg0b/.assets/images/anomaly-explorer-2.png?fit=max&auto=format&n=XwnzH-Jo3nDoEg0b&q=85&s=87cbabd5cec48cca96e7e3a866b45594" width="1004" height="1000" data-path=".assets/images/anomaly-explorer-2.png" />
</Frame>

In the above picture, known clusters are in blue, new classified data are in orange. It's clearly outside of any known clusters and can thus be tagged as an anomaly.

## How does it work?

Here is the process in the background:

* Create X number of clusters and group all the data.
* For each of these clusters, we store the center and the size of the cluster.
* During the inference, we calculate the closest cluster for a new data point and show the distance from the edge of the cluster. If it’s *within* a cluster (no anomaly) you thus get a value below 0.

## Additional resources

* Tutorial: [Continuous Motion Recognition](/tutorials/end-to-end/motion-recognition)
* Blog post: [Advanced Anomaly Detection with Feature Importance](https://edgeimpulse.com/blog/advanced-anomaly-detection-with-feature-importance)


Built with [Mintlify](https://mintlify.com).
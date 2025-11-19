# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/insights-panel.md

# Insights Panel

> Utilize Galileo's Insights Panel to analyze data trends, detect issues, and gain actionable insights for improving NLP model performance.

Galileo provides a dynamic *Insights Panel* that provides a bird's eye view of your model's performance on the data currently in scope. Specifically, the Insights Panel contains three sections:

* [Alerts](/galileo/how-to-and-faq/galileo-product-features/xray-insights)

* Metrics (see below)

* [Clusters](/galileo/how-to-and-faq/galileo-product-features/clusters)

**Metrics**

Under the "Metrics" tab you can find a number of charts and insights that update dynamically. Through these charts you can get greater insights into the subset of data you're currently looking at. These content of these charts differ depending on the task type. Generally, they include

* Overall model and dataset metrics

* Class level model performance

* Class level DEP scores

* Class distributions

* Top most misclassified pairs

* Error distributions

* Class Overlap

The Insights Panel allows you to keep a constant check on model performance as you continue the inspection process (through the [Dataset View](/galileo/how-to-and-faq/galileo-product-features/dataset-view) and [Embeddings View](/galileo/how-to-and-faq/galileo-product-features/embeddings-view)).

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/insight-panel.gif" />
</Frame>

### Model and Dataset Metrics

The top of the Insights Panel displays aggregate model performance (default to F1 for NLP, Accuracy, mAP and IOU for Image Classification, Object Detection or Semantic Segmentation) and allow you to select between Precision, Recall, and F1. Additionally, the Insights Panel shows the number of current data samples in scope along with what % of the total data is represented.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/insight-panel-1.png" />
</Frame>

### Class Level Model Performance

Based on the model metric selected (F1, Precision, Recall), the "Model performance" bar chart displays class level model performance.

<Frame caption="Class Level Model Performance Chart">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/insight-panel-2.png" />
</Frame>

### Class Distribution

The Class Distribution chart shows the breakdown of samples within each class. This insights chart is critical for quickly drawing insights about the class makeup of the data in scope and for detecting issues with class imbalance.

<Frame caption="Fig. Class Distribution plot">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/insight-panel-3.png" />
</Frame>

### Top most misclassified pairs

At the bottom of the Insights Panel we show the "Top five 5 most misclassified data label pairs", where each pair shows a gold label, the incorrect prediction label, and the number of samples falling into this misclassified pairing. This insights chart provides a snapshot into the most common mistakes made by the model (i.e. mistaking ground truth label X for prediction label Y).

<Frame caption="Fig. Top 5 misclassified label pairs - surfaces the most common mistakes made by the model">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/insight-panel-4.png" />
</Frame>

### Interacting with Insights Charts

In addition to providing visual insights, each insights chart can also be interacted with. Within the "Model performance", "Data Error Potential (DEP)", and "Class distribution" charts selecting one of the bars restricts the data in scope to data with `Gold Label` equal to the selected `bar label`.

An even more powerful interaction exists in the "Top 5 most misclassified label pairs" panel. Clicking on a row within this insights chart filters for *misclassified data* matching the `gold label` and `prediction label` of the misclassified label pair.

<Frame caption="Fig. Interaction with `Most misclassified label pairs` chart allows for quick dataset filtering">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/insight-panel-5.gif" />
</Frame>

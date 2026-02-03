# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/insights-panel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel.gif?s=a20dd77eba9678179b0bb59a6732a5fc" data-og-width="576" width="576" data-og-height="1294" height="1294" data-path="images/insight-panel.gif" data-optimize="true" data-opv="3" />
</Frame>

### Model and Dataset Metrics

The top of the Insights Panel displays aggregate model performance (default to F1 for NLP, Accuracy, mAP and IOU for Image Classification, Object Detection or Semantic Segmentation) and allow you to select between Precision, Recall, and F1. Additionally, the Insights Panel shows the number of current data samples in scope along with what % of the total data is represented.

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-1.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=456aec562ef0c5f755f283cb9e673fd2" data-og-width="576" width="576" data-og-height="126" height="126" data-path="images/insight-panel-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-1.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=ab315ea46b359b9752ac68e5e2865d09 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-1.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=472802dcff095b73e1896fe55e5b0fe7 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-1.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=36e212c617a2f4897318b385b708bae0 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-1.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c7e2e939bb03e530c5c4a82be7be6e19 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-1.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6b7ef85e6b09d76d1a8ed41b41c2f866 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-1.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=829dab66daf139a8609980769caf3d9c 2500w" />
</Frame>

### Class Level Model Performance

Based on the model metric selected (F1, Precision, Recall), the "Model performance" bar chart displays class level model performance.

<Frame caption="Class Level Model Performance Chart">
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-2.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=e6f91434dc86a11ed430817b1b94a504" data-og-width="490" width="490" data-og-height="377" height="377" data-path="images/insight-panel-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-2.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=61be78c503ab587dc156daabbf318dbf 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-2.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=b94214c519d42f21f204217b243ce813 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-2.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=27f981f361bc984449b39b5f8806000e 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-2.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=8c7130a58a1675400de6e722cf4ef7fc 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-2.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=0172262db345b41218f46599469bd381 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-2.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=9c4eb6918dc81b057816d3f6968167e5 2500w" />
</Frame>

### Class Distribution

The Class Distribution chart shows the breakdown of samples within each class. This insights chart is critical for quickly drawing insights about the class makeup of the data in scope and for detecting issues with class imbalance.

<Frame caption="Fig. Class Distribution plot">
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-3.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=0bc1637b2dcc33c8d0190ea78d1fd345" data-og-width="503" width="503" data-og-height="328" height="328" data-path="images/insight-panel-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-3.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=70feb27969e12ce13be0b400e97e24d6 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-3.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=5b59669aacf1e694be1dcd7b9b8ba96b 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-3.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6363d79d4d937ef48a3014ae9a4fd11b 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-3.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=a6c03f17695389f690ad794554b5a8a2 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-3.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=54d65d14d420b76ef4a6eafe26fa3d55 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-3.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=55301a230c313b9e7c38373d91f2635f 2500w" />
</Frame>

### Top most misclassified pairs

At the bottom of the Insights Panel we show the "Top five 5 most misclassified data label pairs", where each pair shows a gold label, the incorrect prediction label, and the number of samples falling into this misclassified pairing. This insights chart provides a snapshot into the most common mistakes made by the model (i.e. mistaking ground truth label X for prediction label Y).

<Frame caption="Fig. Top 5 misclassified label pairs - surfaces the most common mistakes made by the model">
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-4.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=95d7fd676109856421e94f97af7207c6" data-og-width="503" width="503" data-og-height="284" height="284" data-path="images/insight-panel-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-4.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c305e8582a9dd79b8c4b732fbee2a7de 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-4.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=470e966c022f5571f86df109cbaa6844 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-4.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=deae97e9bccc467de6fcaa90fe023341 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-4.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=cb02b0f5931e55ec9e81534eab7c9f8f 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-4.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=111841f82e8e900a8c1abb784a442478 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-4.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=fe07cb405d8cc0edeea046fa9a190104 2500w" />
</Frame>

### Interacting with Insights Charts

In addition to providing visual insights, each insights chart can also be interacted with. Within the "Model performance", "Data Error Potential (DEP)", and "Class distribution" charts selecting one of the bars restricts the data in scope to data with `Gold Label` equal to the selected `bar label`.

An even more powerful interaction exists in the "Top 5 most misclassified label pairs" panel. Clicking on a row within this insights chart filters for *misclassified data* matching the `gold label` and `prediction label` of the misclassified label pair.

<Frame caption="Fig. Interaction with `Most misclassified label pairs` chart allows for quick dataset filtering">
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/insight-panel-5.gif?s=a46ea87f8aeff209ede2fab4e01d1b1d" data-og-width="600" width="600" data-og-height="330" height="330" data-path="images/insight-panel-5.gif" data-optimize="true" data-opv="3" />
</Frame>

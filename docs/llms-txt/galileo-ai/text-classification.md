# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/text-classification.md

# Text Classification

> Using Galileo for Text Classification you can improve your classification models by improving the quality of your training data.

During Training and Pre-Training, Galileo for CV helps you to identify and fix data and label errors quickly. Through Insights such [**Mislabeled Samples**](/galileo/gen-ai-studio-products/galileo-ai-research/likely-mislabeled), [**Class Overlap**](/galileo/gen-ai-studio-products/galileo-ai-research/class-boundary-detection), [**Data Error Potential**](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep) and others, you can see what's wrong with your data in a matter of seconds instead of hours.

Once errors are identified, Galileo allows you to take action in-tool or helps you take these erroneous samples to your labeling tool or Python environments. Fixing erroneous training data consistently leads to significant improvements in your model quality in production.

**What is Text Classification?**

Text classification is a sequence classification problem, where given an input document, the task is to correctly classify it into one of the given target classes. Here's an example:

```
input = "Perfectly works fine after 10 years, would highly recommend. Great buy!!"
output = "positive review"

input = "The product did not last long, and was bad quality"
output = "negative review"
```

**How to use Galileo for Text Classification?**

<iframe src="https://cdn.iframe.ly/WF8Ho2s" width="100%" height="480px" allow="encrypted-media *;" />

## Discover the Console

Upon completing a run, you'll be taken to the Galileo Console. The first thing you'll notice is your dataset on the right. On each row, we show you the sample's text, its Ground Truth and Prediction labels, and the [Data Error Potential](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep) of the sample. By default, your samples are sorted by Data Error Potential.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/text-cl-1.png" />
</Frame>

You can also view your samples in the [embeddings space](/galileo/how-to-and-faq/galileo-product-features/embeddings-view) of the model. This can help you get a semantic understanding of your dataset. Using features like *Color-By DEP,* you might discover pockets of problematic data (e.g. decision boundaries that might benefit from more samples or a cluster of garbage samples).

Your left pane is called the [Insights Menu](/galileo/how-to-and-faq/galileo-product-features/insights-panel). On the top you can see your dataset size and choose the metric you want to guide your exploration by (F1 by default). Size and metric update as you add filters to your dataset.

Your main source of insights will be [Alerts](/galileo/how-to-and-faq/galileo-product-features/xray-insights), [Metrics](/galileo/how-to-and-faq/galileo-product-features/insights-panel) and [Clusters](/galileo/how-to-and-faq/galileo-product-features/clusters). Alerts are a distilled list of different issues we've identified in your dataset. Insights such as [*Mislabeled Samples*](/galileo/gen-ai-studio-products/galileo-ai-research/likely-mislabeled), Class Imbalance, [Overlapping Classes](/galileo/gen-ai-studio-products/galileo-ai-research/class-boundary-detection), etc will be surfaced as Alerts.

Clicking on an Alert will filter the dataset to the subset of data that corresponds to the Alert.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/text-cl-2.png" />
</Frame>

Under metrics, you'll find different charts, such as:

* F1 by Class

* Sample Count by Class

* Overlapping Classes

* Top Misclassified Pairs

* DEP Distribution

These charts are dynamic and update as you add different filters. They're also interactive - clicking on a class or group of classes will filter the dataset accordingly, allowing you to inspect and fix the samples.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/text-cl-3.gif" />
</Frame>

The third tab are your [Clusters](/galileo/how-to-and-faq/galileo-product-features/clusters). We automatically cluster your dataset taking into account frequent words and semantic distance. For each Cluster, we show you its average DEP score, F1, and the size of the cluster - factors you can use to determine which clusters are worth looking into. We also show you the common words in the cluster, and, if you enable your OpenAI integration, we leverage GPT to generate summaries of your clusters (more details [here](/galileo/how-to-and-faq/galileo-product-features/clusters)).

**Taking Action**

Once you've identified a problematic subset of data, Galileo allows you to fix your samples with the goal of improving your F1 or performance metric of choice. In Text Classification runs, we allow you to:

* Change Label - Re-assign the label of your image right in-tool

* Remove - Remove problematic images you want to discard from your dataset

* Edit Data - Fix typos or extraneous characters in your samples

* Send to Labelers - Send your samples to your labelers through our [Labeling Integrations](/galileo/how-to-and-faq/galileo-product-features/3p-integrations)

* Export - Download your samples so you can fix them elsewhere

Your changes are tracked in your Edits Cart. There you can view a summary of the changes you've made, you can undo them, or download a clean and fixed dataset to retrain your model.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/text-cl-4.gif" />
</Frame>

**Changing Splits**

Your dataset splits are maintained on Galileo. Your data is logged as Training, Test and/or Validation split. Galileo allows you to explore each split independently. Some alerts, such as Underfitting Classes or Overfitting Classes look at cross-split performance. However, for the most part, each split is treated independently.

To switch splits, find the *Splits* dropdown next to your project and run name near the top of the screen. By default, the Training split is shown first.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/text-cl-5.png" />
</Frame>

### Get started with a notebook <Icon icon="book" />

* [Huggingface](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/text_classification/Text_Classification_using_Huggingface_Trainer_and_%F0%9F%94%AD_Galileo.ipynb) <Icon icon="face-smiling-hands" /> [Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/text_classification/Text_Classification_using_Huggingface_Trainer_and_%F0%9F%94%AD_Galileo.ipynb)

* [PyTorch Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/text_classification/Text_Classification_using_PyTorch_and_%F0%9F%94%AD_Galileo_Simple.ipynb)

* [TensorFlow Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/text_classification/Text_Classification_using_Tensorflow_and_%F0%9F%94%AD_Galileo.ipynb)

* [Keras Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/text_classification/Text_Classification_using_Keras_and_%F0%9F%94%AD_Galileo.ipynb)

* [SetFit Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/text_classification/Text_Classification_using_SetFit_and_%F0%9F%94%AD_Galileo.ipynb)

### Start integrating Galileo with our supported frameworks <Icon icon="laptop" />

* HuggingFace <Icon icon="face-smiling-hands" />

* PyTorch

* TensorFlow

* Keras

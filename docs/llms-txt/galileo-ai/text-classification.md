# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/text-classification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-1.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=e5ce9028f0fe53acd130c3d85f9cf930" data-og-width="2214" width="2214" data-og-height="578" height="578" data-path="images/text-cl-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-1.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=38f70246c2d7157f3d3466ece167bf3b 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-1.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=1a5d7b8e372f0c4ae5ccd1716bb2e332 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-1.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=089edaf35290dae5328c971ae803775c 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-1.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=bbc109754354dfc690a4ce7210edc1f8 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-1.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=1c555d27682188bad2e829f4057f011b 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-1.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=cbdf26957c5a931770c0fb82d83f4f52 2500w" />
</Frame>

You can also view your samples in the [embeddings space](/galileo/how-to-and-faq/galileo-product-features/embeddings-view) of the model. This can help you get a semantic understanding of your dataset. Using features like *Color-By DEP,* you might discover pockets of problematic data (e.g. decision boundaries that might benefit from more samples or a cluster of garbage samples).

Your left pane is called the [Insights Menu](/galileo/how-to-and-faq/galileo-product-features/insights-panel). On the top you can see your dataset size and choose the metric you want to guide your exploration by (F1 by default). Size and metric update as you add filters to your dataset.

Your main source of insights will be [Alerts](/galileo/how-to-and-faq/galileo-product-features/xray-insights), [Metrics](/galileo/how-to-and-faq/galileo-product-features/insights-panel) and [Clusters](/galileo/how-to-and-faq/galileo-product-features/clusters). Alerts are a distilled list of different issues we've identified in your dataset. Insights such as [*Mislabeled Samples*](/galileo/gen-ai-studio-products/galileo-ai-research/likely-mislabeled), Class Imbalance, [Overlapping Classes](/galileo/gen-ai-studio-products/galileo-ai-research/class-boundary-detection), etc will be surfaced as Alerts.

Clicking on an Alert will filter the dataset to the subset of data that corresponds to the Alert.

<Frame>
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-2.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=086bc07a1d22dfb44aa6e349572c71eb" data-og-width="696" width="696" data-og-height="1298" height="1298" data-path="images/text-cl-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-2.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b663a195d655ae05113fdde9558714d2 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-2.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=4efbeb872591763b3d4286b5db6168cb 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-2.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=355d9248eb8fd1afa36282cf379f17b0 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-2.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=145864c08de92e994a8d3149e76d6af4 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-2.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=dc58aaa8c765808e1341721ee8a0add6 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-2.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=78089cc6f0b25f441d9c99df9bdc345b 2500w" />
</Frame>

Under metrics, you'll find different charts, such as:

* F1 by Class

* Sample Count by Class

* Overlapping Classes

* Top Misclassified Pairs

* DEP Distribution

These charts are dynamic and update as you add different filters. They're also interactive - clicking on a class or group of classes will filter the dataset accordingly, allowing you to inspect and fix the samples.

<Frame>
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-3.gif?s=7f33b5711f0bbad873e97b3e06e7359f" data-og-width="600" width="600" data-og-height="1424" height="1424" data-path="images/text-cl-3.gif" data-optimize="true" data-opv="3" />
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
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-4.gif?s=03dca3f83f6104814d5cc44c693b10a9" data-og-width="600" width="600" data-og-height="321" height="321" data-path="images/text-cl-4.gif" data-optimize="true" data-opv="3" />
</Frame>

**Changing Splits**

Your dataset splits are maintained on Galileo. Your data is logged as Training, Test and/or Validation split. Galileo allows you to explore each split independently. Some alerts, such as Underfitting Classes or Overfitting Classes look at cross-split performance. However, for the most part, each split is treated independently.

To switch splits, find the *Splits* dropdown next to your project and run name near the top of the screen. By default, the Training split is shown first.

<Frame>
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-5.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=45f2bd4806f2b157467239f078c38f37" data-og-width="2182" width="2182" data-og-height="114" height="114" data-path="images/text-cl-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-5.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=539130d786ac593e9b379bf1815608bc 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-5.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ee40e42b173d8d42928b227d8393309e 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-5.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=3083aafa7621409b8b19d00338534807 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-5.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=489da78dc8feee3b0cf554a7540265e0 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-5.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=058b88a43edf3b0b64f2ac9400de6097 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/text-cl-5.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=bf114dc16b30c35172097f3f04473038 2500w" />
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

# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/named-entity-recognition.md

# Named Entity Recognition

> NER is a sequence tagging problem, where given an input document, the task is to correctly identify the span boundaries for various entities and also classify the spans into correct entity types.

Galileo supports NER for various tagging schema including - BIO, BIOES, and BILOU. Additionally, you can use Galileo for other span classification tasks that follow similar schemas. Here's an example:

```

input = "Galileo was an Italian astronomer born in Pisa, and he discovered the moons of planet Jupiter"
output = [{"span_text": "Galileo", "start": 0, "end": 1, "label": "PERSON"},
          {"span_text": "Italian", "start": 3, "end": 4, "label": "MISCELANEOUS"},
          {"span_text": "Pisa", "start": 6, "end": 7, "label": "LOCATION"},
          {"span_text": "Jupiter", "start": 13, "end": 14, "label": "LOCATION"}]
```

### How to use Galileo for Named Entity Recognition?

<iframe src="https://cdn.iframe.ly/zyZqYox" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

## Discover the Console

Upon completing a run, you'll be taken to the Galileo Console. The first thing you'll notice is your dataset on the right. On each row, we show you your sample with its Ground Truth annotations, the same sample with your model's prediction, the [Data Error Potential](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep) of the sample and an error count. By default, your samples are sorted by Data Error Potential.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity.webp" />
</Frame>

You can also view your samples in the [embeddings space](/galileo/how-to-and-faq/galileo-product-features/embeddings-view) of the model. This can help you get a semantic understanding of your dataset. Using features like *Color-By DEP,* you
might discover pockets of problematic data (e.g. decision boundaries that might benefit from more samples or a cluster of garbage samples).

Your left pane is called the [Insights Menu](/galileo/how-to-and-faq/galileo-product-features/insights-panel). On the top you can see your dataset size and choose the metric you want to guide your exploration by (F1 by default). Size and metric update as you add filters to your dataset.

Your main source of insights will be [Alerts](/galileo/how-to-and-faq/galileo-product-features/xray-insights), [Metrics](/galileo/how-to-and-faq/galileo-product-features/insights-panel) and [Clusters](/galileo/how-to-and-faq/galileo-product-features/clusters). Alerts are a distilled list of different issues we've identified in your dataset. Insights such as [*Mislabeled Samples*](/galileo/gen-ai-studio-products/galileo-ai-research/likely-mislabeled), Class Imbalance, [Overlapping Classes](/galileo/gen-ai-studio-products/galileo-ai-research/class-boundary-detection), etc will be surfaced as Alerts.

Clicking on an Alert will filter the dataset to the subset of data that corresponds to the Alert.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-2.png" />
</Frame>

Under metrics, you'll find different charts, such as:

* High Problematic Words

* Error Distribution

* F1 by Class

* Sample Count by Class

* Overlapping Classes

* Top Misclassified Pairs

* DEP Distribution

These charts are dynamic and update as you add different filters. They're also interactive - clicking on a class or group of classes will filter the dataset accordingly, allowing you to inspect and fix the samples.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-3.gif" />
</Frame>

**Taking Action**

Once you've identified a problematic subset of data, Galileo allows you to fix your samples with the goal of improving your F1 or performance metric of choice. In Text Classification runs, we allow you to:

* Change Label - Re-assign the label of your image right in-tool

* Remove - Remove problematic images you want to discard from your dataset

* Edit Data - Add or Move Spans, fix fypos or extraneous characters in your samples

* Send to Labelers - Send your samples to your labelers through our [Labeling Integrations](/galileo/how-to-and-faq/galileo-product-features/3p-integrations)

* Export - Download your samples so you can fix them elsewhere

Your changes are tracked in your Edits Cart. There you can view a summary of the changes you've made, you can undo them, or download a clean and fixed dataset to retrain your model.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-4.gif" />
</Frame>

**Changing Splits**

Your dataset splits are maintained on Galileo. Your data is logged as Training, Test and/or Validation split. Galileo allows you to explore each split independently. Some alerts, such as Underfitting Classes or Overfitting Classes look at cross-split performance. However, for the most part, each split is treated independently.

To switch splits, find the *Splits* dropdown next to your project and run name near the top of the screen. By default, the Training split is shown first.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-image-4-1.avif" />
</Frame>

## Galileo features to quickly help you find errors in your data

### 1. Rows sorted by span-level DEP scores

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-5.avif" />
</Frame>

For NER, the Data Error Potential ([DEP](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep)) score is calculated at a span level. This allows rows with spans that the model had a particularly hard time with to bubble up at the top.

You can always adjust the DEP slider to filter this view and update the Insights.

### 2. Sort by 4 out-of-the-box Error types

Galileo automatically identifies whether any of the following errors are present per row:

a. **Span Shift:** A count of the misaligned spans that have overlapping predicted and gold spans

b. **Wrong Tag:** A count of aligned predicted and gold spans that primarily have mismatched labels

c. **Missed Span:** A count of the spans that have gold spans, but no corresponding predicted spans

d. **Ghost Span:** A count of the spans that have predicted spans, but no corresponding gold spans

### 3. Explore the most frequent words with the highest DEP Score

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-6.png" />
</Frame>

Often it is critical to get a high level view of what specific words the model is struggling with most. This NER specific insight lists out the words that are most frequently contained within spans with high DEP scores.

Click on any word to get a filtered view of the high DEP spans containing that word.

### 4. Explore span-level embedding clusters

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-7.avif" />
</Frame>

For NER, [embeddings](/galileo/how-to-and-faq/galileo-product-features/embeddings-view) are at a span level as well (that is, each dot is a span).

Hover over any region to get a list of spans and the corresponding DEP scores in a list.

Click the region to get a detailed view for a particular span that has been clicked.

### 5. Find similar spans

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-8.png" />
</Frame>

We leverage the Galileo [similarity clustering](/galileo/how-to-and-faq/galileo-product-features/similarity-search) to find all similar samples to a particular span quickly -- select a span and click the 'Similar to' button.

### 6. Remove and re-label rows/spans by adding to the Edits Cart

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-9.png" />
</Frame>

After every run, you might want to prune your dataset to either

a. Prep it for the next training job

b. Send the dataset for re-labeling

You can think of the 'Edits Cart' as a means to capture all the dataset changes done during the discovery phase (removing/re-labeling rows and spans) to collectively take action upon a curated dataset.

### 7. Export your filtered dataset to CSV

At any point you can export the dataset to a CSV file in a easy to view format.

## Types of NER Errors

### A*nnotation mistakes of overlooked spans*

As shown in Figure 1, observing the samples that have a high DEP score (i.e. they are hard for the model), and a non-zero count for ghost spans, can help identify samples where the annotators overlooked actual spans. Such annotation errors can cause inconsistencies in the dataset, which can affect model generalization.

<Frame caption="Figure 1">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-10.gif" />
</Frame>

### *Annotation mistakes of incorrectly labelled spans*

As shown in Figure 2, observing the subset of data with span labels in pairs with high confusion matrix and having high DEP, can help identify samples where the annotators incorrectly labelled the spans with a different class tag. Example: An annotator confused "ACTOR" spans with "DIRECTOR" spans, thereby contributing to the model biases.

<Frame caption="Figure 2">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-11.gif" />
</Frame>

### *Most frequent erroneous words across spans*

As shown in Figure 3, the insights panel provides top erroneous words across all spans in the dataset. These words have the highest average DEP across spans, and should be further inspected for error patterns. Example: "rated" had high DEP because it was inconsistently labelled as "RATING\_AVERAGE" or "RATING" by the annotators.

<Frame caption="Figure 3">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-12.gif" />
</Frame>

### *Error patterns for least performing class*

As shown in Figure 4, the model performance charts can be used to identify and filter on the least performing class. The erroneously annotated spans surface to the top.

<Frame caption="Figure 4">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-13.gif" />
</Frame>

### H*ard spans for the model*

As shown in the Figure 5, the "color-by" feature can be used to observe predicted embeddings, and see the spans that are present in ground truth data, but were not predicted by the model. These spans are hard for the model to predict on

<Frame caption="Figure 5">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-14.gif" />
</Frame>

### *Confusing spans*

As shown in Figure 6, the error distribution chart can be used to identify which classes have highly confused spans, where the span class was predicted incorrectly. Sorting by DEP and wrong tag error can help surface such confusing spans.

<Frame caption="Figure 6">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-15.gif" />
</Frame>

### *Smart features: to find malformed samples*

As shown in Figure 7, the smart features from Galileo allow one to quickly find ill-formed samples. Example: Adding text length as a column and sorting based on it will surface malformed samples.

<Frame caption="Figure 7">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/named-entity-16.gif" />
</Frame>

### Get started with a notebook <Icon icon="book" />

* [Huggingface](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/named_entity_recognition/Named_Entity_Recognition_with_Huggingface_Trainer_and_%F0%9F%94%AD_Galileo.ipynb) <Icon icon="face-smiling-hands" /> [Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/named_entity_recognition/Named_Entity_Recognition_with_Huggingface_Trainer_and_%F0%9F%94%AD_Galileo.ipynb)

* [PyTorch Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/named_entity_recognition/Named_Entity_Recognition_with_Pytorch_and_%F0%9F%94%AD_Galileo.ipynb)

* [TensorFlow Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/named_entity_recognition/Named_Entity_Recognition_with_Tensorflow_and_%F0%9F%94%AD_Galileo.ipynb)

* [Spacy Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/named_entity_recognition/Named_Entity_Recognition_with_SpaCy_and_%F0%9F%94%AD_Galileo.ipynb)

### Start integrating Galileo with our supported frameworks <Icon icon="laptop" />

* PyTorch

* TensorFlow

* Spacy

### Technicalities <Icon icon="robot" />

* Required format for logging data

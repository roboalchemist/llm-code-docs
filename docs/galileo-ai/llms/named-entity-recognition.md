# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/named-entity-recognition.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity.webp?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=f667ba589a74f52fff3ae9b734c6cd37" data-og-width="2220" width="2220" data-og-height="1202" height="1202" data-path="images/named-entity.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity.webp?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=1ea5b9946335e5a44086342de47e09ba 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity.webp?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=31118e245e18061b76713818968a0816 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity.webp?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=34da7b869eb58ad461a7501039903234 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity.webp?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=8dff4fc1d42cf0f41322d40771b1bdf3 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity.webp?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=aba372706aa36b86e7f5f0b8680a807c 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity.webp?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=f9d7cf43402abc662564dfa2f3acfab0 2500w" />
</Frame>

You can also view your samples in the [embeddings space](/galileo/how-to-and-faq/galileo-product-features/embeddings-view) of the model. This can help you get a semantic understanding of your dataset. Using features like *Color-By DEP,* you
might discover pockets of problematic data (e.g. decision boundaries that might benefit from more samples or a cluster of garbage samples).

Your left pane is called the [Insights Menu](/galileo/how-to-and-faq/galileo-product-features/insights-panel). On the top you can see your dataset size and choose the metric you want to guide your exploration by (F1 by default). Size and metric update as you add filters to your dataset.

Your main source of insights will be [Alerts](/galileo/how-to-and-faq/galileo-product-features/xray-insights), [Metrics](/galileo/how-to-and-faq/galileo-product-features/insights-panel) and [Clusters](/galileo/how-to-and-faq/galileo-product-features/clusters). Alerts are a distilled list of different issues we've identified in your dataset. Insights such as [*Mislabeled Samples*](/galileo/gen-ai-studio-products/galileo-ai-research/likely-mislabeled), Class Imbalance, [Overlapping Classes](/galileo/gen-ai-studio-products/galileo-ai-research/class-boundary-detection), etc will be surfaced as Alerts.

Clicking on an Alert will filter the dataset to the subset of data that corresponds to the Alert.

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-2.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=a0277662f1f62a45705feaf268430169" data-og-width="796" width="796" data-og-height="1298" height="1298" data-path="images/named-entity-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-2.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=238c2c31f635d6b302f28eb637322e44 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-2.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c0f6ff43c7d4f42a204fdabddf7f4b27 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-2.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6550979562b63fb97ed0118a883995d4 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-2.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=68ae9425b5461f0df3f08c1526732ec1 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-2.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=648f7ec19c9c4927597b373005dfb104 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-2.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6839830b4156873860aa844496aef476 2500w" />
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
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-3.gif?s=3279b9324f2e9469db23f7828de8fdfe" data-og-width="600" width="600" data-og-height="1423" height="1423" data-path="images/named-entity-3.gif" data-optimize="true" data-opv="3" />
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
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-4.gif?s=081777704c98d5e37cf7a62e91269013" data-og-width="600" width="600" data-og-height="321" height="321" data-path="images/named-entity-4.gif" data-optimize="true" data-opv="3" />
</Frame>

**Changing Splits**

Your dataset splits are maintained on Galileo. Your data is logged as Training, Test and/or Validation split. Galileo allows you to explore each split independently. Some alerts, such as Underfitting Classes or Overfitting Classes look at cross-split performance. However, for the most part, each split is treated independently.

To switch splits, find the *Splits* dropdown next to your project and run name near the top of the screen. By default, the Training split is shown first.

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-image-4-1.avif?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=cf6e6b258c4862d0de53ee9192b2c4c1" data-og-width="900" width="900" data-og-height="47" height="47" data-path="images/named-image-4-1.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-image-4-1.avif?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=3c90a9df8120f932fd5bf434f31615b8 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-image-4-1.avif?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d6c24003a8affe76a70de5ea577a052a 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-image-4-1.avif?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=ae7012cad1e74a4f1adb8ec252d3cd14 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-image-4-1.avif?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d0481aa6717c0cf7d58bbcb143de511a 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-image-4-1.avif?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=bbfabcf649b306bba3a3b790f2156808 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-image-4-1.avif?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=e77bf346a8323bf4f7b72d46123864dc 2500w" />
</Frame>

## Galileo features to quickly help you find errors in your data

### 1. Rows sorted by span-level DEP scores

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-5.avif?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=107210a57e11702b2e8d090260899a8a" data-og-width="2304" width="2304" data-og-height="730" height="730" data-path="images/named-entity-5.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-5.avif?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c2938bdd573eb56dbc7367cea207a415 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-5.avif?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d526325dc04a1ccdf2819c36ed48c817 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-5.avif?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=b666a89c987a66f11dec7be959416224 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-5.avif?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=29d6b1d78464a278a7ead6e54c2c7656 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-5.avif?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=eb29cd2e691c0d4ec20011926579153a 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-5.avif?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=4dc42c96950fbed32958c00902076a5a 2500w" />
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
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-6.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=1ce85e7b9823f7cda3afc051d6617b3e" data-og-width="720" width="720" data-og-height="338" height="338" data-path="images/named-entity-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-6.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=138babc1bbb309e732b07832d26099d6 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-6.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=97dac4d4a4c4c102ac711259093698ba 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-6.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=b352135fdfb79535859e9d0b2bda3932 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-6.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=722e064f4e2c360bdd834a9dc36c5db6 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-6.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=318852cf4a91f4643c240ee780d32bc1 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-6.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=94f915a3b470a68c246edfb62b23beaf 2500w" />
</Frame>

Often it is critical to get a high level view of what specific words the model is struggling with most. This NER specific insight lists out the words that are most frequently contained within spans with high DEP scores.

Click on any word to get a filtered view of the high DEP spans containing that word.

### 4. Explore span-level embedding clusters

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-7.avif?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7a8ad97af39fc43bc859fabf939ab172" data-og-width="2304" width="2304" data-og-height="901" height="901" data-path="images/named-entity-7.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-7.avif?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=9db197e184c5e9a7fb0dd98157c89054 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-7.avif?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=1459ab273581cf3e7a04747905fa243e 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-7.avif?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=cc4905bf6404c82494d4d034625d7764 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-7.avif?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=0efca05f72afb26f7a416b983680f398 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-7.avif?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d0befa87e41f75d930b127602cf843ae 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-7.avif?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=4a46a42995cdd45d99a819abf4299995 2500w" />
</Frame>

For NER, [embeddings](/galileo/how-to-and-faq/galileo-product-features/embeddings-view) are at a span level as well (that is, each dot is a span).

Hover over any region to get a list of spans and the corresponding DEP scores in a list.

Click the region to get a detailed view for a particular span that has been clicked.

### 5. Find similar spans

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-8.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=fded8ebdedc35afb7ffd14fc291fbf5b" data-og-width="2142" width="2142" data-og-height="972" height="972" data-path="images/named-entity-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-8.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=a77045b0177c50a24745b8cdf4f61e2a 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-8.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=162b4bd8df5c3f8a1e9deb7f003991be 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-8.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c3c48f9db833aa406e3be79e8d2cc74f 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-8.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=5c26bd5111e5effa8753461974511f20 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-8.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=58d394faab68c8321eff049ebf9233f0 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-8.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=755d84888e3f4bee155503f1091f75f1 2500w" />
</Frame>

We leverage the Galileo [similarity clustering](/galileo/how-to-and-faq/galileo-product-features/similarity-search) to find all similar samples to a particular span quickly -- select a span and click the 'Similar to' button.

### 6. Remove and re-label rows/spans by adding to the Edits Cart

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-9.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=542d5f3764af4dbed77d9726754afd19" data-og-width="2076" width="2076" data-og-height="702" height="702" data-path="images/named-entity-9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-9.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=3967d52898ff9d78deaca2e77ba9bf37 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-9.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d59cb41dd9f2805b4deeb509b26cb0c1 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-9.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=8eee3a22095e2fc625cbf0678f7cc12b 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-9.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=ca318978eaa3a5826f0d4a1c368e5958 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-9.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=5da1efee53634f30fc909dd5f8caadc7 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-9.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=05043796cb4ddb405d7ba95ae2de84f2 2500w" />
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
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-10.gif?s=96b8f3267140bb13084936f630cc8ad4" data-og-width="600" width="600" data-og-height="311" height="311" data-path="images/named-entity-10.gif" data-optimize="true" data-opv="3" />
</Frame>

### *Annotation mistakes of incorrectly labelled spans*

As shown in Figure 2, observing the subset of data with span labels in pairs with high confusion matrix and having high DEP, can help identify samples where the annotators incorrectly labelled the spans with a different class tag. Example: An annotator confused "ACTOR" spans with "DIRECTOR" spans, thereby contributing to the model biases.

<Frame caption="Figure 2">
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-11.gif?s=751b7b2f44f9b5f3051eda1dd0c943d0" data-og-width="600" width="600" data-og-height="311" height="311" data-path="images/named-entity-11.gif" data-optimize="true" data-opv="3" />
</Frame>

### *Most frequent erroneous words across spans*

As shown in Figure 3, the insights panel provides top erroneous words across all spans in the dataset. These words have the highest average DEP across spans, and should be further inspected for error patterns. Example: "rated" had high DEP because it was inconsistently labelled as "RATING\_AVERAGE" or "RATING" by the annotators.

<Frame caption="Figure 3">
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-12.gif?s=3bc7154913f76e9e0a9c983eb91dec0d" data-og-width="600" width="600" data-og-height="311" height="311" data-path="images/named-entity-12.gif" data-optimize="true" data-opv="3" />
</Frame>

### *Error patterns for least performing class*

As shown in Figure 4, the model performance charts can be used to identify and filter on the least performing class. The erroneously annotated spans surface to the top.

<Frame caption="Figure 4">
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-13.gif?s=d189e7a56e3b85bac110c84a97f1617d" data-og-width="600" width="600" data-og-height="348" height="348" data-path="images/named-entity-13.gif" data-optimize="true" data-opv="3" />
</Frame>

### H*ard spans for the model*

As shown in the Figure 5, the "color-by" feature can be used to observe predicted embeddings, and see the spans that are present in ground truth data, but were not predicted by the model. These spans are hard for the model to predict on

<Frame caption="Figure 5">
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-14.gif?s=1b2adeee474bcffcd5d0c61e1508160e" data-og-width="600" width="600" data-og-height="311" height="311" data-path="images/named-entity-14.gif" data-optimize="true" data-opv="3" />
</Frame>

### *Confusing spans*

As shown in Figure 6, the error distribution chart can be used to identify which classes have highly confused spans, where the span class was predicted incorrectly. Sorting by DEP and wrong tag error can help surface such confusing spans.

<Frame caption="Figure 6">
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-15.gif?s=031151b0fed5efeb31d4ad4c6f91c6bb" data-og-width="600" width="600" data-og-height="311" height="311" data-path="images/named-entity-15.gif" data-optimize="true" data-opv="3" />
</Frame>

### *Smart features: to find malformed samples*

As shown in Figure 7, the smart features from Galileo allow one to quickly find ill-formed samples. Example: Adding text length as a column and sorting based on it will surface malformed samples.

<Frame caption="Figure 7">
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/named-entity-16.gif?s=c5d3dd9c85348807f905aac173f26d60" data-og-width="600" width="600" data-og-height="318" height="318" data-path="images/named-entity-16.gif" data-optimize="true" data-opv="3" />
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

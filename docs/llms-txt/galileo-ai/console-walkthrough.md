# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/console-walkthrough.md

# Console Walkthrough

> Upon completing a run, you'll be taken to the Galileo Console.

By default, your Training split will be shown first. You can use the dropdown on the top-right to change it. The first thing you'll notice is your dataset on the right.

By default you will see on each row the Input, its Target (Expected Output), the Generated Output if available, and the [Data Error Potential (DEP)](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep) of the sample. The samples are sorted by DEP, showing the hardest samples first. Each Token in the Target also has a DEP value, which can easily be seen via highlighting.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-walkthrough-dep.png)

You can also view your samples in the [embeddings space](/galileo/how-to-and-faq/galileo-product-features/embeddings-view) of the model. This can help you get a semantic understanding of your dataset. Using features like *Color-By DEP,* you might discover pockets of problematic data (e.g. decision boundaries that might benefit from more samples or a cluster of garbage samples).

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-walkthrough-embeddings.png)

Your left pane is called the [Insights Menu](/galileo/how-to-and-faq/galileo-product-features/insights-panel). On the top, you can see your dataset size and choose the metric you want to guide your exploration by (F1 by default). Size and metric value update as you add filters to your dataset.

Your main source of insights will be [Alerts](/galileo/how-to-and-faq/galileo-product-features/xray-insights), [Metrics](/galileo/how-to-and-faq/galileo-product-features/insights-panel), and [Clusters](/galileo/how-to-and-faq/galileo-product-features/clusters). Alerts are a distilled list of different issues we've identified in your dataset. Under *Metrics*, you'll find different charts to help you debug your data.

Clicking on an Alert will filter the dataset to the subset of data that corresponds to the Alert.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-walkthrough-insights-pane.png)

These charts are dynamic and update as you add different filters. They are also interactive - clicking on a class or group of classes will filter the dataset accordingly, allowing you to inspect and fix the samples.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-walkthrough-insights-pane-2.png)

The third tab is for your [Clusters](/galileo/how-to-and-faq/galileo-product-features/clusters). We automatically cluster your dataset taking into account frequent words and semantic distance. For each Cluster, we show you its average DEP score and the size of the cluster - factors you can use to determine which clusters are worth looking into.

We also show you the common words in the cluster, and, if you enable your OpenAI integration, we leverage GPT to generate summaries of your clusters (more details [here](/galileo/how-to-and-faq/galileo-product-features/clusters)).

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-walkthrough-clusters.png)

Analyzing the various Clusters side-by-side with the embeddings view is often a hepful way to discover interesting pockets of data.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-walkthrough-clusters-embeddings.png)

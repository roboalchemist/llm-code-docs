# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/embeddings-view.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Embeddings View

> The Embeddings View provides a visual playground for you to interact with your datasets.

To visualize your datasets, we leverage your model's embeddings logged during training, validation, testing or inference. Given these embeddings, we plot the data points on the 2D plane using the techniques explained below.

## Scalable Visualization

After experimenting with a host of different dimensionality reduction techniques, we have adopted the principles of UMAP \[[1](https://arxiv.org/abs/1802.03426)]. Given a high dimensional dataset, UMAP seeks to preserve the positional information of each data sample while projecting the data into a lower dimensional space (the 2D plane in our case). We additionally use a parameterized version of UMAP along with custom compression techniques to efficiently scale our data visualization to O(million) samples.

## Embedding View Interaction

The Embedding View allows you to visually detect patterns in the data, interactively select dataset sub populations for further exploration, and visualize different dataset features and insights to identify model decision boundaries and better gauge overall model performance. Visualizing data embeddings provides a key component in going beyond traditional dataset level metrics for analyzing model performance and understanding data quality.

### General Navigation

Navigating the embedding view is made easy with interactive plotting. While exploring your dataset you can easily adjust and drag the embedding plane with the P*an* tool, zoom in and out on specific data regions with S*croll to Zoom,* and reset the visualization with the *Reset Axes* tool\*.\* To interact with individual data samples, simply hover the cursor over a data sample of interest to display information and insights.

<Frame caption="Fig. General embeddings view navigation">
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/emb-view-1.gif?s=3e0698b66dbddd17409cbd0bce21594a" data-og-width="600" width="600" data-og-height="380" height="380" data-path="images/emb-view-1.gif" data-optimize="true" data-opv="3" />
</Frame>

### Color By

One powerful feature is the ability to color data points by different data fields e.g. `ground truth labels`, `data error potential (DEP)`, etc. Different data coloring schemes reveal different dataset insights (i.e. using color by `predicted labels` reveals the model's perceived decision boundaries) and altogether provide a more holistic view of the data.

<Frame caption="Fig. Coloring by different data fields opens the door to a range of insights">
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/emb-view-2.gif?s=08a610e9aa6f4ace26802d1a6844abca" data-og-width="600" width="600" data-og-height="380" height="380" data-path="images/emb-view-2.gif" data-optimize="true" data-opv="3" />
</Frame>

### Subset Selection

Once you have identified a data subset of interest, you can explicitly select this subset to further analyze and view insights on. We offer two different selection tools: *lasso selection* and *box* *select*.

After selecting a data subset, the embeddings view, insights charts, and the general data table are all updated to reflect *just* the selected data. As shown below, given a cluster of miss-classified data points, you can make a lasso selection to easily inspect subset specific insights. For example, you can view model performance on the selected sub population, as well as develop insights into which classes are most significantly underperforming.

<Frame caption="Fig. Lasso Selection">
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/emb-view-3.gif?s=bc6f644b3275a65e7c8703c041c290b5" data-og-width="600" width="600" data-og-height="401" height="401" data-path="images/emb-view-3.gif" data-optimize="true" data-opv="3" />
</Frame>

### Similarity Search

In the Embeddings View, you can easily interact with Galileo's *similarity search* feature. Hovering over a data point reveals the "Show similar" button. When selected, your inspection dataset is restricted to the data samples with most similar embeddings to the selected data sample, allowing you to quickly inspect model performance over a highly focused data sub-population. See the [*similarity search*](/galileo/how-to-and-faq/galileo-product-features/similarity-search) \_\_ documentation for more details.

<Frame caption="Fig. Similarity search enables quick surfacing of similar data samples">
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/emb-view-4.gif?s=abe07dba21bcac16ed09dfef679413e4" data-og-width="600" width="600" data-og-height="332" height="332" data-path="images/emb-view-4.gif" data-optimize="true" data-opv="3" />
</Frame>

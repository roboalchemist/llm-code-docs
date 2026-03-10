# [Anchor](https://qdrant.tech/documentation/cloud/cluster-upgrades/\#updating-qdrant-cloud-clusters) Updating Qdrant Cloud Clusters

As soon as a new Qdrant version is available. Qdrant Cloud will show you an update notification in the Cluster list and on the Cluster details page.

To update to a new version, go to the Cluster details page, choose the new version from the version dropdown and click **Update**.

![Cluster Updates](https://qdrant.tech/documentation/cloud/cluster-upgrades.png)

If you have a multi-node cluster and if your collections have a replication factor of at least **2**, the update process will be zero-downtime and done in a rolling fashion. You will be able to use your database cluster normally.

If you have a single-node cluster or a collection with a replication factor of **1**, the update process will require a short downtime period to restart your cluster with the new version.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-upgrades.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-upgrades.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-158-lllmstxt|>
## data-exploration
- [Articles](https://qdrant.tech/articles/)
- Data Exploration

#### Data Exploration

Learn how you can leverage vector similarity beyond just search. Reveal hidden patterns and insights in your data, provide recommendations, and navigate data space.

[![Preview](https://qdrant.tech/articles_data/distance-based-exploration/preview/preview.jpg)\\
**Distance-based data exploration** \\
Explore your data under a new angle with Qdrant's tools for dimensionality reduction, clusterization, and visualization.\\
\\
Andrey Vasnetsov\\
\\
March 11, 2025](https://qdrant.tech/articles/distance-based-exploration/)[![Preview](https://qdrant.tech/articles_data/discovery-search/preview/preview.jpg)\\
**Discovery needs context** \\
Discovery Search, an innovative way to constrain the vector space in which a search is performed, relying only on vectors.\\
\\
Luis Cossío\\
\\
January 31, 2024](https://qdrant.tech/articles/discovery-search/)[![Preview](https://qdrant.tech/articles_data/vector-similarity-beyond-search/preview/preview.jpg)\\
**Vector Similarity: Going Beyond Full-Text Search \| Qdrant** \\
Discover how vector similarity expands data exploration beyond full-text search. Explore diversity sampling and more for enhanced data discovery!\\
\\
Luis Cossío\\
\\
August 08, 2023](https://qdrant.tech/articles/vector-similarity-beyond-search/)[![Preview](https://qdrant.tech/articles_data/dataset-quality/preview/preview.jpg)\\
**Finding errors in datasets with Similarity Search** \\
Improving quality of text-and-images datasets on the online furniture marketplace example.\\
\\
George Panchuk\\
\\
July 18, 2022](https://qdrant.tech/articles/dataset-quality/)

×

[Powered by](https://qdrant.tech/)

<|page-159-lllmstxt|>
## pdf-retrieval-at-scale
- [Documentation](https://qdrant.tech/documentation/)
- [Advanced tutorials](https://qdrant.tech/documentation/advanced-tutorials/)
- Scaling PDF Retrieval with Qdrant
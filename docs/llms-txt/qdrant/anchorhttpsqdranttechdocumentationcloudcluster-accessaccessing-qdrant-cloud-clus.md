# [Anchor](https://qdrant.tech/documentation/cloud/cluster-access/\#accessing-qdrant-cloud-clusters) Accessing Qdrant Cloud Clusters

Once you [created](https://qdrant.tech/documentation/cloud/create-cluster/) a cluster, and set up an [API key](https://qdrant.tech/documentation/cloud/authentication/), you can access your cluster through the integrated Cluster UI, the REST API and the GRPC API.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-access/\#cluster-ui) Cluster UI

There is the convenient link on the cluster detail page in the Qdrant Cloud Console to access the [Cluster UI](https://qdrant.tech/documentation/web-ui/).

![Cluster Cluster UI](https://qdrant.tech/documentation/cloud/cloud-db-dashboard.png)

The Overview tab also contains direct links to explore Qdrant tutorials and sample datasets.

![Cluster Cluster UI Tutorials](https://qdrant.tech/documentation/cloud/cloud-db-deeplinks.png)

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-access/\#api) API

The REST API is exposed on your cluster endpoint at port `6333`. The GRPC API is exposed on your cluster endpoint at port `6334`. When accessing the cluster endpoint, traffic is automatically load balanced across all healthy Qdrant nodes in the cluster. For all operations, but the few mentioned at [Node specific endpoints](https://qdrant.tech/documentation/cloud/cluster-access/#node-specific-endpoints), you should use the cluster endpoint. It does not matter which node in the cluster you land on. All nodes can handle all search and write requests.

![Cluster cluster endpoint](https://qdrant.tech/documentation/cloud/cloud-endpoint.png)

Have a look at the [API reference](https://qdrant.tech/documentation/interfaces/#api-reference) and the official [client libraries](https://qdrant.tech/documentation/interfaces/#client-libraries) for more information on how to interact with the Qdrant Cloud API.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-access/\#node-specific-endpoints) Node Specific Endpoints

Next to the cluster endpoint which loadbalances requests across all healthy Qdrant nodes, each node in the cluster has its own endpoint as well. This is mainly usefull for monitoring or manual shard management purpuses.

You can finde the node specific endpoints on the cluster detail page in the Qdrant Cloud Console.

![Cluster node endpoints](https://qdrant.tech/documentation/cloud/cloud-node-endpoints.png)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-access.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-access.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-87-lllmstxt|>
## gridstore-key-value-storage
- [Articles](https://qdrant.tech/articles/)
- Introducing Gridstore: Qdrant's Custom Key-Value Store

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)
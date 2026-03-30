# Source: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/llms.txt

# Neptune Analytics Neptune Analytics User Guide

> A guide to using the Neptune Analytics graph database engine.

- [Latest updates](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/doc-history.html)
- [Create a graph](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/create-graph-using-console.html)
- [Limits](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/analytics-limits.html)
- [API reference](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/api-ref.html)

## [What is Neptune Analytics?](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html)

- [Features](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/neptune-analytics-features.html): Neptune Analytics operates in a managed environment that can load data extremely fast into memory and run graph algorithms natively.
- [Neptune Analytics vs. Neptune Database](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/neptune-analytics-vs-neptune-database.html): Amazon Neptune makes it easy to work with graph data in the AWS Cloud.


## [Getting started](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted.html)

- [Create an empty Neptune graph](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-creating-a-graph.html): Learn how to create an empty graph using Neptune Analytics.
- [Create a Neptune graph from existing sources](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-existing-sources.html): Learn how to create a Neptune Analytics graph from an existing source.

### [Connecting to a graph](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting.html)

In Neptune Analytics, you can provision your graph to be accessed publicly over the internet or have a private endpoint to access the graph within a VPC.

### [AWS PrivateLink](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-private-link.html)

With AWS PrivateLink for Neptune Analytics, you can provision interface Amazon VPC endpoints (interface endpoints) in your virtual private cloud (Amazon VPC).

- [Types of interface endpoint services for Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-private-link-types.html): Neptune Analytics supports two services via interface VPC endpoints on AWS PrivateLink: neptune-graph for accessing Neptune Analytics control plane API operations like CreateGraph, DeleteGraph etc. and neptune-graph-data for accessing Neptune Analytics data plane API operations like GetQuery, ListQueries, ExecuteQuery etc.
- [Considerations when using AWS PrivateLink for Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-private-link-considerations.html): Amazon VPC considerations apply to AWS PrivateLink for Neptune Analytics.
- [Accessing Neptune Analytics interface endpoints](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-private-link-access.html): When you create an interface endpoint for Neptune Analytics, AWS PrivateLink generates two types of endpoint-specific, Neptune Analytics DNS names: Regional and zonal.
- [Accessing Neptune Analytics graph from Neptune Analytics interface endpoints](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-private-link-access-interface.html): You can use the AWS CLI or AWS SDKs to access Neptune Analytics graph API operations through Neptune Analytics interface endpoints.
- [Creating an Amazon VPC endpoint policy for Neptune Analytics data plane](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-private-link-create-policy.html)
- [Connecting from the same VPC](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-within-VPC.html): Learn how to connect to a private endpoint from within the same VPC when using Neptune Analytics.
- [Connecting from a different VPC](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-different-VPC.html): Learn how to connect to a private endpoint from a different VPC when using Neptune Analytics.
- [Accessing the graph](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-accessing.html): Learn how to access a graph.
- [Best practices](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-best-practices.html): Learn about best practices when getting started with Neptune Analytics.


## [Using notebooks](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/notebooks.html)

- [Create a notebook with CloudFormation](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/create-notebook-cfn.html): Learn how to create a new Neptune Analytics notebook using a CloudFormation template.
- [Create a notebook on the console](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/create-notebook-console.html): Learn how to create a new Neptune Analytics notebook using the AWS Management Console.
- [Local hosting](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/create-notebook-local.html): Learn how to create a Neptune Analytics notebook on your local machine.


## [Loading data](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/loading-data.html)

### [Data formats](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/loading-data-formats.html)

Learn about the data format for loading from Amazon S3 into Neptune Analytics.

- [Using CSV data](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-CSV-data.html): Neptune Analytics, like Neptune Database, supports two csv formats for loading graph data: csv and opencypher.
- [Using Parquet data](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-Parquet-data.html): Neptune Analytics supports importing data using the Parquet format.

### [Using RDF data](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html)

Learn how to use RDF data with Neptune Analytics.

- [Referencing IRIs in queries](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/rdf-handling-iri-ref.html): Learn about referencing IRIs in queries.
- [Mapping RDF triples to LPG concepts](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/rdf-mapping-triples.html): How to map RDF triples to LPG concepts in Neptune Analytics.
- [Batch load](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/batch-load.html): Learn how to batch load data into Neptune Analytics.

### [Bulk import](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import.html)

Learn how to bulk import data into a Neptune Analytics graph.

### [Create a graph from Amazon S3, a Neptune cluster, or a snapshot](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-into-a-graph.html)

Learn how to create a Neptune Analytics graph from Amazon S3, a Neptune cluster, or a snapshot.

- [Creating a Neptune Analytics graph from Amazon S3](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-create-from-s3.html): Learn how to create a Neptune Analytics graph from Amazon S3.
- [Creating a Neptune Analytics graph from Neptune cluster or snapshot](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-create-from-neptune.html): Learn how to create a Neptune Analytics graph from a Neptune cluster, or a snapshot.
- [Bulk import data into an existing Neptune Analytics graph](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/loading-data-existing-graph.html): Learn how to bulk import data into an existing Neptune Analytics graph
- [Checking the details and progress of an import task](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-checking-details.html): Learn how to check the details and progress of an import task.
- [Canceling an import task](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-cancelling-import.html): Learn how to cancel an import task.
- [Troubleshooting](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-troubleshooting.html): Troubleshooting bulk load and batch load.

### [neptune.read()](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/neptune-read.html)

Neptune supports a CALL procedure neptune.read to read data from Amazon S3 and then run an openCypher query (read, insert, update) using the data.

- [Query examples using Parquet](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/parquet-examples.html): The following example query returns the number of rows in a given Parquet file:
- [Supported Parquet column types](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/parquet-column-types.html)
- [Sample Parquet output](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/parquet-output.html): Given a Parquet file like this:
- [Query examples using CSV](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/csv-examples.html): In this example, the query returns the number of rows in a given CSV file:
- [Property column headers](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/property-column-headers.html): You can specify a column (:) for a property by using the following syntax.
- [Supported CSV column types](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/csv-column-types.html)
- [Sample CSV output](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/csv-output.html): Given the following CSV file:


## [Exporting data](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/exporting-data.html)

- [start-export-task](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/start-export-task.html): Learn about using the start-export-task command to export data from a Neptune Analytics graph.
- [get-export-task](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/get-export-task.html): Learn about using the get-export-task command to export data from a Neptune Analytics graph.
- [list-export-task](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/list-export-task.html): Learn about using the list-export-task command to export data from a Neptune Analytics graph.
- [cancel-export-task](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/cancel-export-task.html): Learn about using the cancel-export-task command to export data from a Neptune Analytics graph.
- [Structure of exported files](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/export-structure.html)

### [Specifying a filter](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/export-filter.html)

The vertexFilter is used to specify filters on a per-label basis for vertices.

- [Sample filters](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/export-filter-samples.html)


## [Graph snapshots](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/graph-snapshots.html)

- [Creating a snapshot](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/graph-snapshots-creating.html): Learn how to create a graph snapshot.
- [Listing snapshots](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/graph-snapshots-listing.html): Learn how to list existing graph snapshots.
- [Restoring a snapshot](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/graph-snapshots-restoring.html): Learn to restore a graph from a snapshot.
- [Deleting snapshots](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/graph-snapshots-deleting.html): Learn how to delete a graph snapshot.


## [Managing your graphs](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing.html)

- [Modifying](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-modifying.html): Learn how to modify a Neptune Analytics graph.
- [Maintaining](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-maintaining.html): Learn how to maintain a Neptune Analytics graph.
- [Deleting](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-deleting.html): Learn to delete a Neptune Analytics graph.
- [Stopping](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-stopping.html): Learn how to stop a Neptune Analytics graph.
- [Starting](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-starting.html): Learn how to start a Neptune Analytics graph.
- [Tagging](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-tagging.html): Learn how to tag Neptune Analytics graph resources.
- [Working with ARNs](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-ARN.html): Learn how to work with ARNs in Neptune Analytics graph.


## [Monitoring](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/monitoring.html)

- [Neptune Analytics information in CloudTrail](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/monitoring-cloudtrail-info.html): Learn about monitoring Neptune Analytics using AWS CloudTrail.
- [Understanding log file entries](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/monitoring-cloudtrail-understanding.html): Understanding Neptune Analytics log files entries.
- [Monitoring your graphs](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/monitoring-cw.html): Amazon Neptune and Amazon CloudWatch are integrated so that you can gather and analyze performance metrics.


## [Security](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Neptune Analytics.

### [Identity and access management](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Neptune Analytics resources.

- [Working with IAM](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Neptune Analytics, learn what IAM features are available to use with Neptune Analytics.
- [Identity-based policy examples](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Neptune Analytics resources.
- [Troubleshooting](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Neptune Analytics and IAM.
- [Compliance validation](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Neptune Analytics features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/infrastructure-security.html): Learn how Neptune Analytics isolates service traffic.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/cross-service-confused-deputy-prevention.html): Learn about preventing the confused deputy problem in Neptune Analytics.
- [Service-linked roles](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/nan-service-linked-roles.html): Learn about how to use service-linked roles in Neptune Analytics.
- [Import/export permissions](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/import-export-permissions.html): Neptune Analytics Export writes data into customer-owned Amazon S3 buckets.


## [Queries](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query.html)

### [Query APIs](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs.html)

The Neptune Analytics data API provides support for data operations including query execution, query status checking, query cancellation, and graph summarizing via the HTTPS endpoint, the AWS CLI, and the SDK.

- [ExecuteQuery](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-execute-query.html): ExecuteQuery runs queries against a Neptune Analytics graph.
- [ListQueries](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-list-queries.html): ListQueries API fetches the list of running/waiting/cancelling queries on the graph.
- [GetQuery](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-get-query.html): The GetQuery API can be used to get the status of a specific query request.
- [CancelQuery](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-cancel-query.html): CancelQuery cancels a specific query request.
- [GraphSummary](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-graph-summary.html): You can use the GetGraphSummary API to quickly gain a high-level understanding of your graph data, size and content.
- [IAM role mappings](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-IAM-role-mappings.html): When you're calling Neptune Analytics API methods on a cluster, you require an IAM policy attached to the user or role making the calls that provides permissions for the actions you want to make.

### [Query plan cache](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-plan-cache.html)

When a query is submitted to Neptune , the query string is parsed and translated into a query plan, which then gets optimized and executed by the engine.

- [Mitigation for query plan cache issue](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/engine-releases-mitigation.html): We have detected an issue in query plan cache when skip or limit is used in an inner WITH clause and are parameterized.
- [Query explain](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-explain.html): The openCypher explain feature is a feature that helps users to understand how the query is executed.
- [Statistics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-statistics.html): Neptune Analytics uses similar statistics for planning query execution as in Neptune Database.
- [Exceptions](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-exceptions.html): Learn about the different exceptions you can encounter when working with Neptune Analytics
- [Data model](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-openCypher-data-model.html): Learn about using the openCypher data model with Neptune Analytics
- [OpenCypher specification compliance](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-openCypher-standards-compliance.html): Learn about OpenCypher specification compliance in Neptune Analytics
- [Isolation levels](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-isolation-level.html): Neptune Analytics has some differences with isolation level supported by Neptune Database.


## [Algorithms](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/algorithms.html)

### [Path-finding algorithms](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/path-finding-algorithms.html)

Path-finding algorithms are a category of graph algorithms that focus on finding a path, a connected set of nodes and edges, between two or more sets of nodes within a graph.

### [BFS algorithms](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bfs-algorithms.html)

Breadth-first search (BFS) path-finding algorithms search for nodes in breadth-first order, starting from a single vertex.

- [.bfs](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bfs-standard.html): Standard breadth-first search (BFS) is an algorithm for finding nodes from a starting node or nodes in a graph in breadth-first order.
- [.bfs.parents](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bfs-parents.html): The parents variant of breadth-first search is an algorithm for finding nodes from a starting node or vertices in breadth-first order and then performing a breadth-first search for the parent of each node.
- [.bfs.levels](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bfs-levels.html): The levels variant of breadth-first search is an algorithm for searching nodes from a starting node or nodes in breadth-first order.

### [SSSP algorithms](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/sssp-algorithms.html)

A single-source-shortest-path algorithm finds the shortest paths (or the distance of the shortest paths) between a given vertex and all reachable vertices in the graph (including itself).

- [.sssp.bellmanFord](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/sssp-bellmanFord.html): The .sssp.bellmanFord algorithm computes the shortest path distances from a single source vertex to all other vertices in the graph using the Bellman-Ford algorithm.
- [.sssp.bellmanFord.parents](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/sssp-bellmanFord-parents.html): The .sssp.bellmanFord.parents algorithm uses the Bellman-Ford algorithm to find the parent nodes along with the shortest path distances from the source node to all other nodes in the graph.
- [.sssp.bellmanFord.path](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/sssp-bellmanFord-path.html): The .sssp.bellmanFord.path algorithm uses the Bellman-Ford algorithm to find the shortest path along with the shortest path distances from a source node to a target node in the graph.
- [.sssp.deltaStepping](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/sssp-deltaStepping.html): The .sssp.deltaStepping algorithm computes the shortest path distances from a single source vertex to all other vertices in the graph using a delta-stepping algorithm.
- [.sssp.deltaStepping.parents](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/sssp-deltaStepping-parents.html): The .sssp.deltaStepping.parents algorithm computes the shortest path distances from a single source vertex to all other vertices in the graph using a delta-stepping algorithm.
- [.sssp.deltaStepping.path](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/sssp-deltaStepping-path.html): The .sssp.deltaStepping.path algorithm uses the deltaStepping algorithm to find the shortest path along with the shortest path distances from a source node to a target node in the graph.
- [.topksssp](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/topk-sssp.html): The .topkssspalgorithm finds the single-source weighted shortest paths from a source node to its neighbors out to the distance specified by maxDepth.

### [Egonet algorithms](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/egonet-algorithms.html)

This EgoNet algorithm finds the (filtered) EgoNet of a vertex to its hopCount-neighbors.

- [.egonet](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/egonet.html): This EgoNet algorithm finds the (filtered) EgoNet of a vertex to its hopCount-neighbors.
- [.egonet.edgeList](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/egonet-edgelist.html): This EgoNet EdgeList algorithm is the same as the standard EgoNet algorithm, except that this variant has a different output schema, which returns the EgoNet in an edge list form.

### [Centrality algorithms](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/centrality-algorithms.html)

Centrality algorithms utilize the topology of a network to determine the relative importance or influence of a specific node within the graph.

- [.degree](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/degree.html): The .degree centrality algorithm counts the number of incident edges at each node that it traverses.
- [.degree.mutate](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/degree-mutate.html): The .degree.mutate centrality algorithm counts the number of incident edges of every node in the graph.
- [.degreeDistribution](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/degreeDistribution.html): The .degreeDistribution algorithm is a tool for analyzing and visualizing the structural characteristics of a graph.
- [.pageRank](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/page-rank.html): PageRank is an algorithm originally developed by Larry Page and Sergey Brin, co-founders of Google.
- [.pageRank.mutate](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/page-rank-mutate.html): The ranking metric computed by .pageRank.mutate can indicate the importance of a node within a given graph, with the most important nodes having the highest score, and the least important node having the lowest score.
- [.closenessCentrality](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/closeness-centrality.html): The closeness centrality algorithm computes a Closeness Centrality (CC) metric for specified nodes in a graph.
- [.closenessCentrality.mutate](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/closeness-centrality-mutate.html): The closeness centrality mutate algorithm computes a Closeness Centrality (CC) metric for specified nodes in a graph.

### [Similarity algorithms](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/similarity-algorithms.html)

Graph similarity algorithms allow you to compare and analyze the similarities and dissimilarities between different graph structures, which can provide insight into relationships, patterns, and commonalities across diverse datasets.

- [.neighbors.common](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/common-neighbors.html): Common neighbors is an algorithm that counts the number of common neighbors of two input nodes, which is the intersection of their neighborhoods.
- [.neighbors.total](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/total-neighbors.html): Total neighbors is an algoithm that counts the total number of unique neighbors of two input vertices, which is the union of the neighborhoods of those vertices.
- [.jaccardSimilarity](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/jaccard-similarity.html): The Jaccard similarity algorithm measures the similarity between two sets.
- [.overlapSimilarity](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/overlap-similarity.html): Overlap Similarity is an algorithm that measures the overlap between the neighbors of two nodes.

### [Community detection](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/clustering-algorithms.html)

Clustering algorithms evaluate how nodes are clustered in communities, in closely-knit sets, or in highly or loosely interconnected groups.

- [.wcc](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/wcc.html): The Weakly Connected Components (WCC) algorithm finds the weakly-connected components in a directed graph.
- [.wcc.mutate](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/wcc-mutate.html): The mutate variant of the weakly connected components (WCC) algorithm performs the weakly connected components calculation over the entire graph unless the configuration parameters establish a filter, and each traversed node's calculated WCC value is stored as a property on the node.
- [.labelPropagation](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/label-propagation.html): Label Propagation Algorithm (LPA) is an algorithm for community detection that is also used in semi-supervised machine learning for data classification.
- [.labelPropagation.mutate](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/label-propagation-mutate.html): Label Propagation Algorithm (LPA) is an algorithm for community detection that is also used in semi-supervised machine learning for data classification.
- [.scc](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/scc.html): Strongly connected components (SCC) are the maximally connected subgraphs of a directed graph where every node is reachable from every other node (in other words, there exists a path between every node in the subgraph).
- [.scc.mutate](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/scc-mutate.html): Strongly connected components (SCC) are the maximally connected subgraphs of a directed graph, where every node is reachable from every other node (in other words, there exists a path between every node in the subgraph).
- [.louvain](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/louvain.html): The Louvain algorithm is a hierarchical clustering method for detecting community structures within networks.
- [.louvain.mutate](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/louvain-mutate.html): The Louvain algorithm is a hierarchical clustering method for detecting community structures within networks.

### [Misc. graph procedures](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/custom-algorithms.html)

The miscellaneous graph procedures can be ran on your graphs to give you insight into your graphs and their metrics.

- [Property graph information](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/custom-algorithms-property-graph.html): Property Graph Information (graph.pg_info) summarizes some of the basic metrics of the graph, such as the number of vertices, the number of edges, the number of edge properties, the number of vertex properties, the number of edge labels, and the number of vertex labels.
- [Property graph schema](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/custom-algorithms-property-graph-schema.html): The neptune.graph.pg_schema() procedure provides a comprehensive overview of the graph structure.


## [Vector similarity](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vector-similarity.html)

- [Vector indexing](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vector-index.html): You can only create a vector search index for a Neptune Analytics graph at the time the graph is created.

### [VSS algorithms](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vss-algorithms.html)

Vector simlarity search algorithms identify similar vectors based on the vector distance between them.

- [.vectors.distance (deprecated)](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors-distance.html): The .vectors.distance algorithm computes the distance between two nodes based on their embeddings.
- [.vectors.distance.byNode](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors.distance.byNode.html): The .vectors.distance.byNode algorithm computes the distance between two nodes based on their embeddings.
- [.vectors.distanceByEmbedding (deprecated)](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors-distance-embedding.html): The .vectors.distanceByEmbedding algorithm computes the distance between an embedding vector and the embedding of an input node.
- [.vectors.distance.byEmbedding](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors.distance.byEmbedding.html): The .vectors.distance.byEmbedding algorithm computes the distance between an embedding vector and the embedding of an input node.
- [.vectors.get](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors-get.html): The .vectors.get algorithm retrieves the embedding for a node.
- [.vectors.topKByEmbedding (deprecated)](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors-topKByEmbedding.html): The .vectors.topKByEmbedding algorithm finds the topK nearest neighbors of an embedding based on the distance of their vector embeddings.
- [.vectors.topK.byEmbedding](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors.topK.byEmbedding.html): The .vectors.topKByEmbedding algorithm finds the topK nearest neighbors of an embedding based on the distance of their vector embeddings.
- [.vectors.topKByNode (deprecated)](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors-topKByNode.html): The .vectors.topKByNode algorithm finds the topK nearest neighbors of a node based on the distance of their vector embeddings from the node.
- [.vectors.topK.byNode](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors.topK.byNode.html): The .vectors.topK.byNode algorithm finds the topK nearest neighbors of a node based on the distance of their vector embeddings from the node.
- [.vectors.upsert](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors-upsert.html): The .vectors.upsert algorithm is used to add a new embedding or update an existing one for a node.
- [.vectors.remove](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors-remove.html): The .vectors.remove algorithm is used to remove the embedding from a node.


## [Best practices](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bestPractices.html)

- [openCypher query best practices](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/best-practices-content.html)


## [Tools and utilities](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/tools-and-utils.html)

- [Nodestream](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/tools-Nodestream.html): Nodestream is a framework for dealing with semantically modeling data as a graph.


## [Visualization tools](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/visualization-tools.html)

- [G.V() graph database client](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gv-tool.html): G.V() is a comprehensive graph database client for Amazon Neptune that helps you explore, visualize, and interact with your graph data.
- [Graph Explorer](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/graph-explorer-tool.html): Graph Explorer is an open-source tool for visualizing and exploring graph data in Amazon Neptune.

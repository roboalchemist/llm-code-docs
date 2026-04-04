# Source: https://www.elastic.co/docs/reference/glossary

﻿---
title: Glossary
description: 
url: https://www.elastic.co/docs/reference/glossary
products:
  - Elastic Cloud on Kubernetes
  - Elastic Common Schema (ECS)
  - Elastic Stack
---

# Glossary
<definitions>
  <definition term="@metadata">
    A special field for storing content that you don't want to include in output [events](#glossary-event). For example, the `@metadata` field is useful for creating transient fields for use in [conditional](#glossary-conditional) statements.
  </definition>
</definitions>


## A

<definitions>
  <definition term="action">
    1. The rule-specific response that occurs when an alerting rule fires. A rule can have multiple actions. See [Connectors and actions](https://www.elastic.co/docs/reference/kibana/connectors-kibana).
    2. In Elastic Security, actions send notifications through other systems when a detection alert is created, such as email, Slack, PagerDuty, and Webhook.
  </definition>
  <definition term="administration console">
    A component of Elastic Cloud Enterprise that provides the API server for the [Cloud UI](#glossary-cloud-ui). Also syncs cluster and allocator data from ZooKeeper to Elasticsearch.
  </definition>
  <definition term="Advanced Settings">
    Enables you to control the appearance and behavior of Kibana by setting the date format, default index, and other attributes. Part of Kibana Stack Management. See [Advanced Settings](https://www.elastic.co/docs/reference/kibana/advanced-settings).
  </definition>
  <definition term="Agent policy">
    A collection of inputs and settings that defines the data to be collected by Elastic Agent. An agent policy can be applied to a single agent or shared by a group of agents; this makes it easier to manage many agents at scale. See [Elastic Agent policies](https://www.elastic.co/docs/reference/fleet/agent-policy).
  </definition>
  <definition term="alias">
    Secondary name for a group of [data streams](#glossary-data-stream) or [indices](#glossary-index). Most Elasticsearch APIs accept an alias in place of a data stream or index. See [Aliases](https://www.elastic.co/docs/manage-data/data-store/aliases).
  </definition>
  <definition term="allocator affinity">
    Controls how Elastic Stack deployments are distributed across the available set of allocators in your Elastic Cloud Enterprise installation.
  </definition>
  <definition term="allocator tag">
    In Elastic Cloud Enterprise, characterizes hardware resources for Elastic Stack deployments. Used by [instance configurations](#glossary-instance-configuration) to determine which instances of the Elastic Stack should be placed on what hardware.
  </definition>
  <definition term="allocator">
    Manages hosts that contain Elasticsearch and Kibana nodes. Controls the lifecycle of these nodes by creating new [containers](#glossary-container) and managing the nodes within these containers when requested. Used to scale the capacity of your Elastic Cloud Enterprise installation.
  </definition>
  <definition term="analysis">
    Process of converting unstructured [text](#glossary-text) into a format optimized for search. See [Text analysis](https://www.elastic.co/docs/manage-data/data-store/text-analysis).
  </definition>
  <definition term="annotation">
    A way to augment a data display with descriptive domain knowledge.
  </definition>
  <definition term="anomaly detection job">
    Anomaly detection jobs contain the configuration information and metadata necessary to perform an analytics task. See [Machine learning jobs](/docs/explore-analyze/machine-learning/anomaly-detection/ml-ad-run-jobs#ml-ad-create-job).
  </definition>
  <definition term="API key">
    Unique identifier for authentication in Elasticsearch. When [transport layer security (TLS)](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/installing-elasticsearch) is enabled, all requests must be authenticated using an API key or a username and password.
  </definition>
  <definition term="APM agent">
    An open-source library, written in the same language as your service, which [instruments](#glossary-instrumentation) your code and collects performance data and errors at runtime.
  </definition>
  <definition term="APM Server">
    An open-source application that receives data from [APM agents](#glossary-apm-agent) and sends it to Elasticsearch.
  </definition>
  <definition term="app">
    A top-level Kibana component that is accessed through the side navigation. Apps include core Kibana components such as Discover and Dashboard, solutions like Observability and Security, and special-purpose tools like Maps and Stack Management.
  </definition>
  <definition term="auto-follow pattern">
    [Index pattern](#glossary-index-pattern) that automatically configures new [indices](#glossary-index) as [follower indices](#glossary-follower-index) for [cross-cluster replication](#glossary-ccr). See [Manage auto-follow patterns](https://www.elastic.co/docs/deploy-manage/tools/cross-cluster-replication/manage-auto-follow-patterns).
  </definition>
  <definition term="availability zone">
    Contains resources available to an Elastic Cloud Enterprise installation that are isolated from other availability zones to safeguard against failure. Could be a rack, a server zone or some other logical constraint that creates a failure boundary. In a highly available cluster, the nodes of a cluster are spread across two or three availability zones to ensure that the cluster can survive the failure of an entire availability zone. Also see [Fault Tolerance (High Availability)](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise/ece-ha).
  </definition>
</definitions>


## B

<definitions>
  <definition term="Background search">
    A long-running query that is queued and that runs while you perform other tasks. The results of the background search are stored for a period of time, so you can access it once it has completed. Background searches are user specific. Before Elastic Stack 9.2, background searches are called ["search sessions"](#glossary-search-session).
  </definition>
  <definition term="basemap">
    The background detail necessary to orient the location of a map.
  </definition>
  <definition term="beats runner">
    Used to send Filebeat and Metricbeat information to the logging cluster.
  </definition>
  <definition term="bucket aggregation">
    An aggregation that creates buckets of documents. Each bucket is associated with a criterion (depending on the aggregation type), which determines whether or not a document in the current context falls into the bucket.
  </definition>
  <definition term="bucket">
    1. A set of documents in Kibana that have certain characteristics in common. For example, matching documents might be bucketed by color, distance, or date range.
    2. The machine learning features also use the concept of a bucket to divide the time series into batches for processing. The *bucket span* is part of the configuration information for anomaly detection jobs. It defines the time interval that is used to summarize and model the data. This is typically between 5 minutes to 1 hour and it depends on your data characteristics. When you set the bucket span, take into account the granularity at which you want to analyze, the frequency of the input data, the typical duration of the anomalies, and the frequency at which alerting is required.
  </definition>
</definitions>


## C

<definitions>
  <definition term="Canvas expression language">
    A pipeline-based expression language for manipulating and visualizing data. Includes dozens of functions and other capabilities, such as table transforms, type casting, and sub-expressions. Supports TinyMath functions for complex math calculations. See [Canvas function reference](https://www.elastic.co/docs/explore-analyze/visualize/canvas/canvas-function-reference).
  </definition>
  <definition term="Canvas">
    Enables you to create presentations and infographics that pull live data directly from Elasticsearch. See [Canvas](https://www.elastic.co/docs/explore-analyze/visualize/canvas).
  </definition>
  <definition term="certainty">
    Specifies how many documents must contain a pair of terms before it is considered a useful connection in a graph.
  </definition>
  <definition term="CA">
    Certificate authority. An entity that issues digital certificates to verify identities over a network.
  </definition>
  <definition term="client forwarder">
    Used for secure internal communications between various components of Elastic Cloud Enterprise and ZooKeeper.
  </definition>
  <definition term="Cloud UI">
    Provides web-based access to manage your Elastic Cloud Enterprise installation, supported by the [administration console](#glossary-admin-console).
  </definition>
  <definition term="cluster">
    1. A group of one or more connected Elasticsearch [nodes](#glossary-node). See [Clusters, nodes, and shards](https://www.elastic.co/docs/deploy-manage/production-guidance/elasticsearch-in-production-environments).
    2. A layer type and display option in the **Maps** application. Clusters display a cluster symbol across a grid on the map, one symbol per grid cluster. The cluster location is the weighted centroid for all documents in the grid cell.
    3. In Elastic Cloud on Kubernetes, it can refer to either an [Elasticsearch cluster](https://www.elastic.co/docs/deploy-manage/maintenance/add-and-remove-elasticsearch-nodes) or a Kubernetes cluster depending on the context.
  </definition>
  <definition term="codec plugin">
    A Logstash [plugin](#glossary-plugin) that changes the data representation of an [event](#glossary-event). Codecs are essentially stream filters that can operate as part of an input or output. Codecs enable you to separate the transport of messages from the serialization process. Popular codecs include json, msgpack, and plain (text).
  </definition>
  <definition term="cold phase">
    Third possible phase in the [index lifecycle](#glossary-index-lifecycle). In the cold phase, data is no longer updated and seldom [queried](#glossary-query). The data still needs to be searchable, but it's okay if those queries are slower. See [Index lifecycle](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management/index-lifecycle).
  </definition>
  <definition term="cold tier">
    [Data tier](#glossary-data-tier) that contains [nodes](#glossary-node) that hold time series data that is accessed occasionally and not normally updated. See [Data tiers](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers).
  </definition>
  <definition term="component template">
    Building block for creating [index templates](#glossary-index-template). A component template can specify [mappings](#glossary-mapping), [index settings](https://www.elastic.co/docs/reference/elasticsearch/index-settings), and [aliases](#glossary-alias). See [index templates](https://www.elastic.co/docs/manage-data/data-store/templates).
  </definition>
  <definition term="condition">
    Specifies the circumstances that must be met to trigger an alerting [rule](#glossary-rule).
  </definition>
  <definition term="conditional">
    A control flow that executes certain actions based on whether a statement (also called a condition) is true or false. Logstash supports `if`, `else if`, and `else` statements. You can use conditional statements to apply filters and send events to a specific output based on conditions that you specify.
  </definition>
  <definition term="connector">
    A configuration that enables integration with an external system (the destination for an action). See [Connectors and actions](https://www.elastic.co/docs/reference/kibana/connectors-kibana).
  </definition>
  <definition term="Console">
    In Kibana, a tool for interacting with the Elasticsearch REST API. You can send requests to Elasticsearch, view responses, view API documentation, and get your request history. See [Console](https://www.elastic.co/docs/explore-analyze/query-filter/tools/console).
    In Elastic Cloud, provides web-based access to manage your Elastic Cloud deployments.
  </definition>
  <definition term="constructor">
    Directs [allocators](#glossary-allocator) to manage containers of Elasticsearch and Kibana nodes and maximizes the utilization of allocators. Monitors plan change requests from the Cloud UI and determines how to transform the existing cluster. In a highly available installation, places cluster nodes within different availability zones to ensure that the cluster can survive the failure of an entire availability zone.
  </definition>
  <definition term="container">
    Includes an instance of Elastic Cloud Enterprise software and its dependencies. Used to provision similar environments, to assign a guaranteed share of host resources to nodes, and to simplify operational effort in Elastic Cloud Enterprise.
  </definition>
  <definition term="content tier">
    [Data tier](#glossary-data-tier) that contains [nodes](#glossary-node) that handle the [indexing](#glossary-index) and [query](#glossary-query) load for content, such as a product catalog. See [Data tiers](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers).
  </definition>
  <definition term="coordinator">
    Consists of a logical grouping of some Elastic Cloud Enterprise services and acts as a distributed coordination system and resource scheduler.
  </definition>
  <definition term="cross-cluster replication (CCR)">
    Replicates [data streams](#glossary-data-stream) and [indices](#glossary-index) from [remote clusters](#glossary-remote-cluster) in a [local cluster](#glossary-local-cluster). See [Cross-cluster replication](https://www.elastic.co/docs/deploy-manage/tools/cross-cluster-replication).
  </definition>
  <definition term="cross-cluster search (CCS)">
    Searches [data streams](#glossary-data-stream) and [indices](#glossary-index) on [remote clusters](#glossary-remote-cluster) from a [local cluster](#glossary-local-cluster). See [Search across clusters](https://www.elastic.co/docs/explore-analyze/cross-cluster-search).
  </definition>
  <definition term="CRD">
    [Custom resource definition](https://kubernetes.io/docs/reference/glossary/?fundamental=true#term-CustomResourceDefinition). Elastic Cloud on Kubernetes extends the Kubernetes API with CRDs to allow users to deploy and manage Elasticsearch, Kibana, APM Server, Enterprise Search, Beats, Elastic Agent, Elastic Maps Server, and Logstash resources just as they would do with built-in Kubernetes resources.
  </definition>
  <definition term="custom rule">
    A set of conditions and actions that change the behavior of anomaly detection jobs. You can also use filters to further limit the scope of the rules. See [Custom rules](/docs/explore-analyze/machine-learning/anomaly-detection/ml-ad-run-jobs#ml-ad-rules). Kibana refers to custom rules as job rules.
  </definition>
</definitions>


## D

<definitions>
  <definition term="dashboard">
    A collection of [visualizations](#glossary-visualization), [saved searches](#glossary-saved-search), and [maps](#glossary-map) that provide insights into your data from multiple perspectives.
  </definition>
  <definition term="data center">
    Check [availability zone](#glossary-zone).
  </definition>
  <definition term="data frame analytics job">
    Data frame analytics jobs contain the configuration information and metadata necessary to perform machine learning analytics tasks on a source index and store the outcome in a destination index. See [Data frame analytics overview](https://www.elastic.co/docs/explore-analyze/machine-learning/data-frame-analytics/ml-dfa-overview).
  </definition>
  <definition term="data source">
    A file, database, or service that provides the underlying data for a map, Canvas element, or visualization.
  </definition>
  <definition term="data stream">
    A named resource used to manage [time series data](#glossary-time-series-data). A data stream stores data across multiple backing [indices](#glossary-index). See [Data streams](https://www.elastic.co/docs/manage-data/data-store/data-streams).
  </definition>
  <definition term="data tier">
    Collection of [nodes](#glossary-node) with the same [data role](https://www.elastic.co/docs/reference/elasticsearch/configuration-reference/node-settings) that typically share the same hardware profile. Data tiers include the [content tier](#glossary-content-tier), [hot tier](#glossary-hot-tier), [warm tier](#glossary-warm-tier), [cold tier](#glossary-cold-tier), and [frozen tier](#glossary-frozen-tier). See [Data tiers](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers).
  </definition>
  <definition term="data view">
    An object that enables you to select the data that you want to use in Kibana and define the properties of the fields. A data view can point to one or more [data streams](#glossary-data-stream), [indices](#glossary-index), or [aliases](#glossary-alias). For example, a data view can point to your log data from yesterday, or all indices that contain your data.
  </definition>
  <definition term="datafeed">
    Anomaly detection jobs can analyze either a one-off batch of data or continuously in real time. Datafeeds retrieve data from Elasticsearch for analysis.
  </definition>
  <definition term="dataset">
    A collection of data that has the same structure. The name of a dataset typically signifies its source. See [data stream naming scheme](https://www.elastic.co/docs/reference/fleet/data-streams).
  </definition>
  <definition term="delete phase">
    Last possible phase in the [index lifecycle](#glossary-index-lifecycle). In the delete phase, an [index](#glossary-index) is no longer needed and can safely be deleted. See [Index lifecycle](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management/index-lifecycle).
  </definition>
  <definition term="deployment template">
    A reusable configuration of Elastic products and solutions used to create an Elastic Cloud [deployment](#glossary-deployment).
  </definition>
  <definition term="deployment">
    One or more products from the Elastic Stack configured to work together and run on Elastic Cloud.
  </definition>
  <definition term="detection alert">
    Elastic Security produced alerts. Detection alerts are never received from external systems. When a rule's conditions are met, Elastic Security writes a detection alert to an Elasticsearch alerts index.
  </definition>
  <definition term="detection rule">
    Background tasks in Elastic Security that run periodically and produce alerts when suspicious activity is detected.
  </definition>
  <definition term="detector">
    As part of the configuration information that is associated with anomaly detection jobs, detectors define the type of analysis that needs to be done. They also specify which fields to analyze. You can have more than one detector in a job, which is more efficient than running multiple jobs against the same data.
  </definition>
  <definition term="director">
    Manages the [ZooKeeper](#glossary-zookeeper) datastore. This role is often shared with the [coordinator](#glossary-coordinator), though in production deployments it can be separated.
  </definition>
  <definition term="Discover">
    Enables you to search and filter your data to zoom in on the information that you are interested in.
  </definition>
  <definition term="distributed tracing">
    The end-to-end collection of performance data throughout your microservices architecture.
  </definition>
  <definition term="document">
    JSON object containing data stored in Elasticsearch. See [Documents and indices](https://www.elastic.co/docs/manage-data/data-store/index-basics).
  </definition>
  <definition term="drilldown">
    A navigation path that retains context (time range and filters) from the source to the destination, so you can view the data from a new perspective. A dashboard that shows the overall status of multiple data centers might have a drilldown to a dashboard for a single data center. See [Drilldowns](https://www.elastic.co/docs/explore-analyze/dashboards).
  </definition>
</definitions>


## E

<definitions>
  <definition term="edge">
    A connection between nodes in a graph that shows that they are related. The line weight indicates the strength of the relationship.  See [Graph](https://www.elastic.co/docs/explore-analyze/visualize/graph).
  </definition>
  <definition term="Elastic Agent">
    A single, unified way to add monitoring for logs, metrics, and other types of data to a host. It can also protect hosts from security threats, query data from operating systems, forward data from remote services or hardware, and more. See [Elastic Agent overview](https://www.elastic.co/docs/reference/fleet).
  </definition>
  <definition term="Elastic Cloud Enterprise (ECE)">
    The official enterprise offering to host and manage the Elastic Stack yourself at scale. Can be installed on a public cloud platform, such as AWS, GCP or Microsoft Azure, on your own private cloud, or on bare metal.
  </definition>
  <definition term="Elastic Cloud on Kubernetes (ECK)">
    Built on the Kubernetes Operator pattern, ECK extends the basic Kubernetes orchestration capabilities to support the setup and management of Elastic products and solutions on Kubernetes.
  </definition>
  <definition term="Elastic Common Schema (ECS)">
    A document schema for Elasticsearch, for use cases such as logging and metrics. ECS defines a common set of fields, their datatype, and gives guidance on their correct usage. ECS is used to improve uniformity of event data coming from different sources.
  </definition>
  <definition term="Elastic Kubernetes Service (EKS)">
    A managed Kubernetes service provided by Amazon Web Services (AWS).
  </definition>
  <definition term="Elastic Maps Service (EMS)">
    A service that provides basemap tiles, shape files, and other key features that are essential for visualizing geospatial data.
  </definition>
  <definition term="Elastic Package Registry (EPR)">
    A service hosted by Elastic that stores Elastic package definitions in a central location. See the [EPR GitHub repository](https://github.com/elastic/package-registry).
  </definition>
  <definition term="Elastic Security indices">
    Indices containing host and network source events (such as `packetbeat-*`, `log-*`, and `winlogbeat-*`). When you [create a new rule in Elastic Security](https://www.elastic.co/docs/solutions/security/detect-and-alert/create-detection-rule), the default index pattern corresponds to the values defined in the `securitySolution:defaultIndex` advanced setting.
  </definition>
  <definition term="Elastic Stack">
    Also known as the *ELK Stack*, the Elastic Stack is the combination of various Elastic products that integrate for a scalable and flexible way to manage your data.
  </definition>
  <definition term="Elasticsearch">
    The [open source](https://github.com/elastic/elasticsearch) search and analytics engine, data store, and vector database which powers the Elastic platform and is fundamental to every Elastic [deployment type](https://www.elastic.co/docs/deploy-manage/deploy).
    The term "Elasticsearch" has several additional meanings depending on the context in which it is used:
    - Elasticsearch is the name of a [**project** type](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/create-serverless-project) on Elastic Cloud Serverless, tailored for general-purpose search use cases.
    - Elasticsearch is also the name of a **solution** in other Elastic deployment types. Each [space](#glossary-space) has its own navigation or **solution view**.
    - The **Elasticsearch platform** (also known as the Elastic platform or Search AI Platform) is the umbrella term for Elastic's full suite of products and capabilities, built on the core Elasticsearch technology. It encompasses what was initially known as the Elastic Stack, extended with additional capabilities (such as the Search AI Lake) to power Elastic's various deployment types and managed services.
  </definition>
  <definition term="Elasticsearch Service">
    The former name of Elastic Cloud Hosted, which is the official hosted Elastic Stack offering, from the makers of Elasticsearch. Available as a software-as-a-service (SaaS) offering on different cloud platforms, such as AWS, GCP, and Microsoft Azure.
  </definition>
  <definition term="element">
    A [Canvas](#glossary-canvas) workpad object that displays an image, text, or visualization.
  </definition>
  <definition term="endpoint exception">
    [Exceptions](#glossary-exception) added to both rules and Endpoint agents on hosts. Endpoint exceptions can only be added when:
    - Endpoint agents are installed on the hosts.
    - The Elastic Endpoint Security rule is activated.
  </definition>
  <definition term="Event Query Language (EQL)">
    [Query](#glossary-query) language for event-based time series data, such as logs, metrics, and traces. EQL supports matching for event sequences. See [EQL](https://www.elastic.co/docs/explore-analyze/query-filter/languages/eql).
  </definition>
  <definition term="event">
    A single unit of information, containing a timestamp plus additional data. An event arrives through an input, and is subsequently parsed, timestamped, and passed through the Logstash [pipeline](#glossary-pipeline).
  </definition>
  <definition term="exception">
    In Elastic Security, exceptions are added to rules to prevent specific source event field values from generating alerts.
  </definition>
  <definition term="external alert">
    Alerts Elastic Security receives from external systems, such as Suricata.
  </definition>
</definitions>


## F

<definitions>
  <definition term="Feature Controls">
    Enables administrators to customize which features are available in each [space](#glossary-space). See [Spaces](https://www.elastic.co/docs/deploy-manage/manage-spaces).
  </definition>
  <definition term="feature importance">
    In supervised machine learning methods such as regression and classification, feature importance indicates the degree to which a specific feature affects a prediction. See [Regression feature importance](/docs/explore-analyze/machine-learning/data-frame-analytics/ml-dfa-regression#dfa-regression-feature-importance) and [Classification feature importance](/docs/explore-analyze/machine-learning/data-frame-analytics/ml-dfa-classification#dfa-classification-feature-importance).
  </definition>
  <definition term="feature influence">
    In outlier detection, feature influence scores indicate which features of a data point contribute to its outlier behavior. See [Feature influence](/docs/explore-analyze/machine-learning/data-frame-analytics/ml-dfa-finding-outliers#dfa-feature-influence).
  </definition>
  <definition term="feature state">
    The indices and data streams used to store configurations, history, and other data for an Elastic feature, such as Elasticsearch security or Kibana. A feature state typically includes one or more [system indices or data streams](#glossary-system-index). It may also include regular indices and data streams used by the feature. You can use [snapshots](#glossary-snapshot) to back up and restore feature states. See [feature states](/docs/deploy-manage/tools/snapshot-and-restore#feature-state).
  </definition>
  <definition term="field reference">
    A reference to an event [field](#glossary-field). This reference may appear in an output block or filter block in the Logstash config file. Field references are typically wrapped in square (`[]`) brackets, for example `[fieldname]`. If you are referring to a top-level field, you can omit the `[]` and simply use the field name. To refer to a nested field, you specify the full path to that field: `[top-level field][nested field]`.
  </definition>
  <definition term="field">
    1. Key-value pair in a [document](#glossary-document). See [Mapping](https://www.elastic.co/docs/manage-data/data-store/mapping).
    2. In Logstash, this term refers to an [event](#glossary-event) property. For example, each event in an apache access log has properties, such as a status code (200, 404), request path ("/", "index.html"), HTTP verb (GET, POST), client IP address, and so on. Logstash uses the term "fields" to refer to these properties.
  </definition>
  <definition term="filter plugin">
    A Logstash [plugin](#glossary-plugin) that performs intermediary processing on an [event](#glossary-event). Typically, filters act upon event data after it has been ingested through inputs, by mutating, enriching, or modifying the data according to configuration rules. Filters are often applied conditionally depending on the characteristics of the event. Popular filter plugins include grok, mutate, drop, clone, and geoip. Filter stages are optional.
  </definition>
  <definition term="filter">
    [Query](#glossary-query) that does not score matching documents. See [filter context](https://www.elastic.co/docs/explore-analyze/query-filter/languages/querydsl).
  </definition>
  <definition term="Fleet Server">
    Fleet Server is a component used to centrally manage Elastic Agents. It serves as a control plane for updating agent policies, collecting status information, and coordinating actions across agents.
  </definition>
  <definition term="Fleet">
    Fleet provides a way to centrally manage Elastic Agents at scale. There are two parts: The Fleet app in Kibana provides a web-based UI to add and remotely manage agents, while the Fleet Server provides the backend service that manages agents. See [Elastic Agent overview](https://www.elastic.co/docs/reference/fleet).
  </definition>
  <definition term="flush">
    Writes data from the [transaction log](https://www.elastic.co/docs/reference/elasticsearch/index-settings/translog) to disk for permanent storage.
  </definition>
  <definition term="follower index">
    Target [index](#glossary-index) for [cross-cluster replication](#glossary-ccr). A follower index exists in a [local cluster](#glossary-local-cluster) and replicates a [leader index](#glossary-leader-index). See [Cross-cluster replication](https://www.elastic.co/docs/deploy-manage/tools/cross-cluster-replication).
  </definition>
  <definition term="force merge">
    Manually triggers a [merge](#glossary-merge) to reduce the number of [segments](#glossary-segment) in an index's [shards](#glossary-shard).
  </definition>
  <definition term="frozen phase">
    Fourth possible phase in the [index lifecycle](#glossary-index-lifecycle). In the frozen phase, an [index](#glossary-index) is no longer updated and [queried](#glossary-query) rarely. The information still needs to be searchable, but it's okay if those queries are extremely slow. See [Index lifecycle](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management/index-lifecycle).
  </definition>
  <definition term="frozen tier">
    [Data tier](#glossary-data-tier) that contains [nodes](#glossary-node) that hold time series data that is accessed rarely and not normally updated. See [Data tiers](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers).
  </definition>
</definitions>


## G

<definitions>
  <definition term="GCS">
    Google Cloud Storage. Block storage service provided by Google Cloud Platform (GCP).
  </definition>
  <definition term="GKE">
    [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/). Managed Kubernetes service provided by Google Cloud Platform (GCP).
  </definition>
  <definition term="gem">
    A self-contained package of code that's hosted on [RubyGems.org](https://rubygems.org). Logstash [plugins](#glossary-plugin) are packaged as Ruby Gems. You can use the Logstash [plugin manager](#glossary-plugin-manager) to manage Logstash gems.
  </definition>
  <definition term="geo-point">
    A field type in Elasticsearch. A geo-point field accepts latitude-longitude pairs for storing point locations. The latitude-longitude format can be from a string, geohash, array, well-known text, or object. See [geo-point](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-point).
  </definition>
  <definition term="geo-shape">
    A field type in Elasticsearch. A geo-shape field accepts arbitrary geographic primitives, like polygons, lines, or rectangles (and more). You can populate a geo-shape field from GeoJSON or well-known text. See [geo-shape](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape).
  </definition>
  <definition term="GeoJSON">
    A format for representing geospatial data. GeoJSON is also a file-type, commonly used in the **Maps** application to upload a file of geospatial data. See [GeoJSON data](https://www.elastic.co/docs/explore-analyze/visualize/maps/indexing-geojson-data-tutorial).
  </definition>
  <definition term="graph">
    A data structure and visualization that shows interconnections between a set of entities. Each entity is represented by a node. Connections between nodes are represented by [edges](#glossary-edge). See [Graph](https://www.elastic.co/docs/explore-analyze/visualize/graph).
  </definition>
  <definition term="Grok Debugger">
    A tool for building and debugging grok patterns. Grok is good for parsing syslog, Apache, and other webserver logs. See [Debugging grok expressions](https://www.elastic.co/docs/explore-analyze/query-filter/tools/grok-debugger).
  </definition>
</definitions>


## H

<definitions>
  <definition term="hardware profile">
    In Elastic Cloud, a built-in [deployment template](#glossary-deployment-template) that supports a specific use case for the Elastic Stack, such as a compute optimized deployment that provides high vCPU for search-heavy use cases.
  </definition>
  <definition term="heat map">
    A layer type in the **Maps** application. Heat maps cluster locations to show higher (or lower) densities. Heat maps describe a visualization with color-coded cells or regions to analyze patterns across multiple dimensions. See [Heat map layer](https://www.elastic.co/docs/explore-analyze/visualize/maps/heatmap-layer).
  </definition>
  <definition term="hidden data stream or index">
    [Data stream](#glossary-data-stream) or [index](#glossary-index) excluded from most [index patterns](#glossary-index-pattern) by default. See [Hidden data streams and indices](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/api-conventions#multi-hidden).
  </definition>
  <definition term="host runner (runner)">
    In Elastic Cloud Enterprise, a local control agent that runs on all hosts, used to deploy local containers based on role definitions. Ensures that containers assigned to the host exist and are able to run, and creates or recreates the containers if necessary.
  </definition>
  <definition term="hot phase">
    First possible phase in the [index lifecycle](#glossary-index-lifecycle). In the hot phase, an [index](#glossary-index) is actively updated and queried. See [Index lifecycle](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management/index-lifecycle).
  </definition>
  <definition term="hot thread">
    A Java thread that has high CPU usage and executes for a longer than normal period of time.
  </definition>
  <definition term="hot tier">
    [Data tier](#glossary-data-tier) that contains [nodes](#glossary-node) that handle the [indexing](#glossary-index) load for time series data, such as logs or metrics. This tier holds your most recent, most frequently accessed data. See [Data tiers](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers).
  </definition>
</definitions>


## I

<definitions>
  <definition term="ID">
    Identifier for a [document](#glossary-document). Document IDs must be unique within an [index](#glossary-index). See the [`_id` field](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/mapping-id-field).
  </definition>
  <definition term="index lifecycle policy">
    Specifies how an [index](#glossary-index) moves between phases in the [index lifecycle](#glossary-index-lifecycle) and what actions to perform during each phase. See [Index lifecycle](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management/index-lifecycle).
  </definition>
  <definition term="index lifecycle">
    Five phases an [index](#glossary-index) can transition through: [hot](#glossary-hot-phase), [warm](#glossary-warm-phase), [cold](#glossary-cold-phase), [frozen](#glossary-frozen-phase), and [delete](#glossary-delete-phase). See [Index lifecycle](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management/index-lifecycle).
  </definition>
  <definition term="index pattern">
    In Elasticsearch, a string containing a wildcard (`*`) pattern that can match multiple [data streams](#glossary-data-stream), [indices](#glossary-index), or [aliases](#glossary-alias). See [Multi-target syntax](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/api-conventions).
  </definition>
  <definition term="index template">
    Automatically configures the [mappings](#glossary-mapping), [index settings](https://www.elastic.co/docs/reference/elasticsearch/index-settings), and [aliases](#glossary-alias) of new [indices](#glossary-index) that match its [index pattern](#glossary-index-pattern). You can also use index templates to create [data streams](#glossary-data-stream). See [Index templates](https://www.elastic.co/docs/manage-data/data-store/templates).
  </definition>
  <definition term="index">
    1. Collection of JSON [documents](#glossary-document). See [Documents and indices](https://www.elastic.co/docs/manage-data/data-store/index-basics).
    2. To add one or more JSON documents to Elasticsearch. This process is called indexing.
  </definition>
  <definition term="indexer">
    A Logstash instance that is tasked with interfacing with an Elasticsearch cluster in order to index [event](#glossary-event) data.
  </definition>
  <definition term="indicator index">
    Indices containing suspect field values in Elastic Security. [Indicator match rules](/docs/solutions/security/detect-and-alert/create-detection-rule#create-indicator-rule) use these indices to compare their field values with source event values contained in [Elastic Security indices](#glossary-elastic-security-indices).
  </definition>
  <definition term="inference aggregation">
    A pipeline aggregation that references a [trained model](#glossary-trained-model) in an aggregation to infer on the results field of the parent bucket aggregation. It enables you to use supervised machine learning at search time.
  </definition>
  <definition term="inference processor">
    A processor specified in an ingest pipeline that uses a [trained model](#glossary-trained-model) to infer against the data that is being ingested in the pipeline.
  </definition>
  <definition term="inference">
    A machine learning feature that enables you to use supervised learning processes – like classification, regression, or [natural language processing](#glossary-nlp) – in a continuous fashion by using [trained models](#glossary-trained-model) against incoming data.
  </definition>
  <definition term="influencer">
    Influencers are entities that might have contributed to an anomaly in a specific bucket in an anomaly detection job. For more information, see [Influencers](/docs/explore-analyze/machine-learning/anomaly-detection/ml-ad-run-jobs#ml-ad-influencers).
  </definition>
  <definition term="ingestion">
    The process of collecting and sending data from various data sources to Elasticsearch.
  </definition>
  <definition term="input plugin">
    A Logstash [plugin](#glossary-plugin) that reads [event](#glossary-event) data from a specific source. Input plugins are the first stage in the Logstash event processing [pipeline](#glossary-pipeline). Popular input plugins include file, syslog, redis, and beats.
  </definition>
  <definition term="instance configuration">
    In Elastic Cloud, enables the instances of the Elastic Stack to run on suitable hardware resources by filtering on [allocator tags](#glossary-allocator-tag). Used as building blocks for [deployment templates](#glossary-deployment-template).
  </definition>
  <definition term="instance type">
    In Elastic Cloud, categories for [instances](#glossary-instance) representing an Elastic feature or cluster node types, such as `master`, `ml` or `data`.
  </definition>
  <definition term="instance">
    A product from the Elastic Stack that is running in an Elastic Cloud deployment, such as an Elasticsearch node or a Kibana instance. When you choose more [availability zones](#glossary-zone), the system automatically creates more instances for you.
  </definition>
  <definition term="instrumentation">
    Extending application code to track where your application is spending time. Code is considered instrumented when it collects and reports this performance data to APM.
  </definition>
  <definition term="integration policy">
    An instance of an [integration](#glossary-integration) that is configured for a specific use case, such as collecting logs from a specific file.
  </definition>
  <definition term="integration">
    An easy way for external systems to connect to the Elastic Stack. Whether it's collecting data or protecting systems from security threats, integrations provide out-of-the-box assets to make setup easy—many with only a single click.
  </definition>
</definitions>


## J

<definitions>
  <definition term="job">
    Machine learning jobs contain the configuration information and metadata necessary to perform an analytics task. There are two types: [anomaly detection jobs](#glossary-anomaly-detection-job) and [data frame analytics jobs](#glossary-dataframe-job). See also [rollup job](#glossary-rollup-job).
  </definition>
</definitions>


## K

<definitions>
  <definition term="K8s">
    Shortened form (numeronym) of "Kubernetes" derived from replacing "ubernete" with "8".
  </definition>
  <definition term="Kibana privilege">
    Enable administrators to grant users read-only, read-write, or no access to individual features within [spaces](#glossary-space) in Kibana. See [Kibana privileges](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/kibana-privileges).
  </definition>
  <definition term="Kibana Query Language (KQL)">
    The default language for querying in Kibana. KQL provides support for scripted fields. See [Kibana Query Language](https://www.elastic.co/docs/explore-analyze/query-filter/languages/kql).
  </definition>
  <definition term="Kibana">
    A user interface that lets you visualize your Elasticsearch data and navigate the Elastic Stack.
  </definition>
</definitions>


## L

<definitions>
  <definition term="labs">
    An in-progress or experimental feature in **Canvas** or **Dashboard** that you can try out and provide feedback. When enabled, you'll see **Labs** in the toolbar.
  </definition>
  <definition term="leader index">
    Source [index](#glossary-index) for [cross-cluster replication](#glossary-ccr). A leader index exists on a [remote cluster](#glossary-remote-cluster) and is replicated to [follower indices](#glossary-follower-index). See [Cross-cluster replication](https://www.elastic.co/docs/deploy-manage/tools/cross-cluster-replication).
  </definition>
  <definition term="Lens">
    Enables you to build visualizations by dragging and dropping data fields. Lens makes makes smart visualization suggestions for your data, allowing you to switch between visualization types. See [Lens](https://www.elastic.co/docs/explore-analyze/dashboards).
  </definition>
  <definition term="local cluster">
    [Cluster](#glossary-cluster) that pulls data from a [remote cluster](#glossary-remote-cluster) in [cross-cluster search](#glossary-ccs) or [cross-cluster replication](#glossary-ccr). See [Remote clusters](https://www.elastic.co/docs/deploy-manage/remote-clusters/remote-clusters-self-managed).
  </definition>
  <definition term="Lucene query syntax">
    The query syntax for Kibana's legacy query language. The Lucene query syntax is available under the options menu in the query bar and from [Advanced Settings](#glossary-advanced-settings).
  </definition>
</definitions>


## M

<definitions>
  <definition term="machine learning node">
    A machine learning node is a node that has `xpack.ml.enabled` set to `true` and `ml` in `node.roles`. If you want to use machine learning features, there must be at least one machine learning node in your cluster. See [Machine learning nodes](https://www.elastic.co/docs/reference/elasticsearch/configuration-reference/node-settings#ml-node).
  </definition>
  <definition term="map">
    A representation of geographic data using symbols and labels. See [Maps](https://www.elastic.co/docs/explore-analyze/visualize/maps).
  </definition>
  <definition term="mapping">
    Defines how a [document](#glossary-document), its [fields](#glossary-field), and its metadata are stored in Elasticsearch. Similar to a schema definition. See [Mapping](https://www.elastic.co/docs/manage-data/data-store/mapping).
  </definition>
  <definition term="master node">
    Handles write requests for the cluster and publishes changes to other nodes in an ordered fashion. Each cluster has a single master node which is chosen automatically by the cluster and is replaced if the current master node fails. Also see [node](#glossary-node).
  </definition>
  <definition term="merge">
    Process of combining a [shard](#glossary-shard)'s smaller Lucene [segments](#glossary-segment) into a larger one. Elasticsearch manages merges automatically.
  </definition>
  <definition term="message broker">
    Also referred to as a *message buffer* or *message queue*, a message broker is external software (such as Redis, Kafka, or RabbitMQ) that stores messages from the Logstash shipper instance as an intermediate store, waiting to be processed by the Logstash indexer instance.
  </definition>
  <definition term="metric aggregation">
    An aggregation that calculates and tracks metrics for a set of documents.
  </definition>
  <definition term="module">
    Out-of-the-box configurations for common data sources to simplify the collection, parsing, and visualization of logs and metrics.
  </definition>
  <definition term="monitor">
    A network endpoint which is monitored to track the performance and availability of applications and services.
  </definition>
  <definition term="multi-field">
    A [field](#glossary-field) that's [mapped](#glossary-mapping) in multiple ways. See the [`fields` mapping parameter](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/multi-fields).
  </definition>
  <definition term="multifactor authentication (MFA)">
    A security process that requires you to provide two or more verification methods to gain access to web-based user interfaces.
  </definition>
</definitions>


## N

<definitions>
  <definition term="namespace">
    A user-configurable arbitrary data grouping, such as an environment (`dev`, `prod`, or `qa`), a team, or a strategic business unit.
  </definition>
  <definition term="natural language processing (NLP)">
    A machine learning feature that enables you to perform operations such as language identification, named entity recognition (NER), text classification, or text embedding. See [NLP overview](https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-overview).
  </definition>
  <definition term="no-op">
    In Elastic Cloud, the application of a rolling update on your deployment without actually applying any configuration changes. This type of update can be useful to resolve certain health warnings.
  </definition>
  <definition term="node">
    1. A single [Elasticsearch](#glossary-elasticsearch) server. One or more nodes can form a [cluster](#glossary-cluster). See [Clusters, nodes, and shards](https://www.elastic.co/docs/deploy-manage/production-guidance/elasticsearch-in-production-environments).
    2. In Elastic Cloud on Kubernetes, it can refer to either an [Elasticsearch Node](https://www.elastic.co/docs/reference/elasticsearch/configuration-reference/node-settings) or a [Kubernetes Node](https://kubernetes.io/docs/concepts/architecture/nodes/) depending on the context. ECK maps an Elasticsearch node to a Kubernetes Pod which can get scheduled onto any available Kubernetes node that can satisfy the [resource requirements](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s/manage-compute-resources) and [node constraints](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) defined in the [pod template](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s/customize-pods).
  </definition>
  <definition term="NodeSet">
    A set of Elasticsearch nodes that share the same Elasticsearch configuration and a Kubernetes Pod template. Multiple NodeSets can be defined in the Elasticsearch CRD to achieve a cluster topology consisting of groups of Elasticsearch nodes with different node roles, resource requirements and hardware configurations (Kubernetes node constraints).
  </definition>
</definitions>


## O

<definitions>
  <definition term="Observability">
    Unifying your logs, metrics, uptime data, and application traces to provide granular insights and context into the behavior of services running in your environments.
  </definition>
  <definition term="OpenShift">
    A Kubernetes [platform](https://www.openshift.com/) by RedHat.
  </definition>
  <definition term="operator">
    A design pattern in Kubernetes for [managing custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/). Elastic Cloud on Kubernetes implements the operator pattern to manage Elasticsearch, Kibana and APM Server resources on Kubernetes.
  </definition>
  <definition term="output plugin">
    A Logstash [plugin](#glossary-plugin) that writes [event](#glossary-event) data to a specific destination. Outputs are the final stage in the event [pipeline](#glossary-pipeline). Popular output plugins include elasticsearch, file, graphite, and statsd.
  </definition>
</definitions>


## P

<definitions>
  <definition term="Painless Lab">
    An interactive code editor that lets you test and debug Painless scripts in real-time. See [Painless Lab](https://www.elastic.co/docs/explore-analyze/scripting/painless-lab).
  </definition>
  <definition term="panel">
    A [dashboard](#glossary-dashboard) component that contains a query element or visualization, such as a chart, table, or list.
  </definition>
  <definition term="PDB">
    A [pod disruption budget](https://kubernetes.io/docs/reference/glossary/?all=true#term-pod-disruption-budget) in Elastic Cloud on Kubernetes.
  </definition>
  <definition term="pipeline">
    A term used to describe the flow of [events](#glossary-event) through the Logstash workflow. A pipeline typically consists of a series of input, filter, and output stages. [Input](#glossary-input-plugin) stages get data from a source and generate events, [filter](#glossary-filter-plugin) stages, which are optional, modify the event data, and [output](#glossary-output-plugin) stages write the data to a destination. Inputs and outputs support [codecs](#glossary-codec-plugin) that enable you to encode or decode the data as it enters or exits the pipeline without having to use a separate filter.
  </definition>
  <definition term="plan">
    Specifies the configuration and topology of an Elasticsearch or Kibana cluster, such as capacity, availability, and Elasticsearch version, for example. When changing a plan, the [constructor](#glossary-constructor) determines how to transform the existing cluster into the pending plan.
  </definition>
  <definition term="plugin manager">
    Accessed through the `bin/logstash-plugin` script, the plugin manager enables you to manage the lifecycle of [plugins](#glossary-plugin) in your Logstash deployment. You can install, remove, and upgrade plugins by using the plugin manager Command Line Interface (CLI).
  </definition>
  <definition term="plugin">
    A self-contained software package that implements one of the stages in the Logstash event processing [pipeline](#glossary-pipeline). The list of available plugins includes [input plugins](#glossary-input-plugin), [output plugins](#glossary-output-plugin), [codec plugins](#glossary-codec-plugin), and [filter plugins](#glossary-filter-plugin). The plugins are implemented as Ruby [gems](#glossary-gem) and hosted on [RubyGems.org](https://rubygems.org). You define the stages of an event processing [pipeline](#glossary-pipeline) by configuring plugins.
  </definition>
  <definition term="primary shard">
    Lucene instance containing some or all data for an [index](#glossary-index). When you index a [document](#glossary-document), Elasticsearch adds the document to primary shards before [replica shards](#glossary-replica-shard). See [Clusters, nodes, and shards](https://www.elastic.co/docs/deploy-manage/production-guidance/elasticsearch-in-production-environments).
  </definition>
  <definition term="proxy">
    A highly available, TLS-enabled proxy layer that routes user requests, mapping cluster IDs that are passed in request URLs for the container to the cluster nodes handling the user requests.
  </definition>
  <definition term="PVC">
    A [persistent volume claim](https://kubernetes.io/docs/reference/glossary/?all=true#term-persistent-volume-claim) in Elastic Cloud on Kubernetes.
  </definition>
</definitions>


## Q

<definitions>
  <definition term="QoS">
    Quality of service in Elastic Cloud on Kubernetes. When a Kubernetes cluster is under heavy load, the Kubernetes scheduler makes pod eviction decisions based on the [QoS class of individual pods](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/). [*Manage compute resources*](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s/manage-compute-resources) explains how to define QoS classes for Elasticsearch, Kibana and APM Server pods.
  </definition>
  <definition term="Query Profiler">
    A tool that enables you to inspect and analyze search queries to diagnose and debug poorly performing queries. See [Query Profiler](https://www.elastic.co/docs/explore-analyze/query-filter/tools/search-profiler).
  </definition>
  <definition term="query">
    Request for information about your data. You can think of a query as a question, written in a way Elasticsearch understands. See [Search your data](https://www.elastic.co/docs/solutions/search/querying-for-search).
  </definition>
</definitions>


## R

<definitions>
  <definition term="RBAC">
    Role-based Access Control. In Elastic Cloud on Kubernetes, it is a security mechanism in Kubernetes where access to cluster resources is restricted to principals having the appropriate role. Check [[https://kubernetes.io/docs/reference/access-authn-authz/rbac/](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) for more information.
  </definition>
  <definition term="Real user monitoring (RUM)">
    Performance monitoring, metrics, and error tracking of web applications.
  </definition>
  <definition term="recovery">
    Process of syncing a [replica shard](#glossary-replica-shard) from a [primary shard](#glossary-primary-shard). Upon completion, the replica shard is available for searches.
  </definition>
  <definition term="reindex">
    Copies documents from a source to a destination. The source and destination can be a [data stream](#glossary-data-stream), [index](#glossary-index), or [alias](#glossary-alias).
  </definition>
  <definition term="remote cluster">
    A separate [cluster](#glossary-cluster), often in a different data center or locale, that contains [indices](#glossary-index) that can be replicated or searched by the [local cluster](#glossary-local-cluster). The connection to a remote cluster is unidirectional. See [Remote clusters](https://www.elastic.co/docs/deploy-manage/remote-clusters/remote-clusters-self-managed).
  </definition>
  <definition term="replica shard">
    Copy of a [primary shard](#glossary-primary-shard). Replica shards can improve search performance and resiliency by distributing data across multiple [nodes](#glossary-node). See [Clusters, nodes, and shards](https://www.elastic.co/docs/deploy-manage/production-guidance/elasticsearch-in-production-environments).
  </definition>
  <definition term="roles token">
    Enables a host to join an existing Elastic Cloud Enterprise installation and grants permission to hosts to hold certain roles, such as the [allocator](#glossary-allocator) role. Used when installing Elastic Cloud Enterprise on additional hosts, a roles token helps secure Elastic Cloud Enterprise by making sure that only authorized hosts become part of the installation.
  </definition>
  <definition term="rollover">
    Creates a new write index when the current one reaches a certain size, number of docs, or age. A rollover can target a [data stream](#glossary-data-stream) or an [alias](#glossary-alias) with a write index.
  </definition>
  <definition term="rollup index">
    Special type of [index](#glossary-index) for storing historical data at reduced granularity. Documents are summarized and indexed into a rollup index by a [rollup job](#glossary-rollup-job). See [Rolling up historical data](https://www.elastic.co/docs/manage-data/lifecycle/rollup).
  </definition>
  <definition term="rollup job">
    Background task that runs continuously to summarize documents in an [index](#glossary-index) and index the summaries into a separate rollup index. The job configuration controls what data is rolled up and how often. See [Rolling up historical data](https://www.elastic.co/docs/manage-data/lifecycle/rollup).
  </definition>
  <definition term="rollup">
    Summarizes high-granularity data into a more compressed format to maintain access to historical data in a cost-effective way. See [Roll up your data](https://www.elastic.co/docs/manage-data/lifecycle/rollup).
  </definition>
  <definition term="routing">
    Process of sending and retrieving data from a specific [primary shard](#glossary-primary-shard). Elasticsearch uses a hashed routing value to choose this shard. You can provide a routing value in [indexing](#glossary-index) and search requests to take advantage of caching. See the [`_routing` field](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/mapping-routing-field).
  </definition>
  <definition term="rule">
    A set of [conditions](#glossary-condition), schedules, and [actions](#glossary-action) that enable notifications. See [Rules](#glossary-rules).
  </definition>
  <definition term="Rules">
    A comprehensive view of all your alerting rules. Enables you to access and manage rules for all Kibana apps from one place. See [Rules](https://www.elastic.co/docs/explore-analyze/alerting).
  </definition>
  <definition term="runner">
    A local control agent that runs on all hosts, used to deploy local containers based on role definitions. Ensures that containers assigned to it exist and are able to run, and creates or recreates the containers if necessary.
  </definition>
  <definition term="runtime field">
    [Field](#glossary-field) that is evaluated at query time. You access runtime fields from the search API like any other field, and Elasticsearch sees runtime fields no differently. See [Runtime fields](https://www.elastic.co/docs/manage-data/data-store/mapping/runtime-fields).
  </definition>
</definitions>


## S

<definitions>
  <definition term="saved object">
    A representation of a dashboard, visualization, map, data view, or Canvas workpad that can be stored and reloaded.
  </definition>
  <definition term="saved search">
    The query text, filters, and time filter that make up a search, saved for later retrieval and reuse.
  </definition>
  <definition term="scripted field">
    A field that computes data on the fly from the data in Elasticsearch indices. Scripted field data is shown in Discover and used in visualizations.
  </definition>
  <definition term="search session">
    A group of one or more queries that are executed asynchronously. The results of the session are stored for a period of time, so you can recall the query. Search sessions are user specific. From Elastic Stack 9.2, search sessions are called ["background searches"](#glossary-background-search).
  </definition>
  <definition term="search template">
    A stored search you can run with different variables. See [Search templates](https://www.elastic.co/docs/solutions/search/search-templates).
  </definition>
  <definition term="searchable snapshot index">
    [Index](#glossary-index) whose data is stored in a [snapshot](#glossary-snapshot). Searchable snapshot indices do not need [replica shards](#glossary-replica-shard) for resilience, since their data is reliably stored outside the cluster. See [searchable snapshots](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/searchable-snapshots).
  </definition>
  <definition term="searchable snapshot">
    [Snapshot](#glossary-snapshot) of an [index](#glossary-index) mounted as a [searchable snapshot index](#glossary-searchable-snapshot-index). You can search this index like a regular index. See [searchable snapshots](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/searchable-snapshots).
  </definition>
  <definition term="segment">
    Data file in a [shard](#glossary-shard)'s Lucene instance. Elasticsearch manages Lucene segments automatically.
  </definition>
  <definition term="services forwarder">
    Routes data internally in an Elastic Cloud Enterprise installation.
  </definition>
  <definition term="shard">
    Lucene instance containing some or all data for an [index](#glossary-index). Elasticsearch automatically creates and manages these Lucene instances. There are two types of shards: [primary](#glossary-primary-shard) and [replica](#glossary-replica-shard). See [Clusters, nodes, and shards](https://www.elastic.co/docs/deploy-manage/production-guidance/elasticsearch-in-production-environments).
  </definition>
  <definition term="shareable">
    A Canvas workpad that can be embedded on any webpage. Shareables enable you to display Canvas visualizations on internal wiki pages or public websites.
  </definition>
  <definition term="shipper">
    An instance of Logstash that send events to another instance of Logstash, or some other application.
  </definition>
  <definition term="shrink">
    Reduces the number of [primary shards](#glossary-primary-shard) in an index.
  </definition>
  <definition term="snapshot lifecycle policy">
    Specifies how frequently to perform automatic backups of a cluster and how long to retain the resulting [snapshots](#glossary-snapshot). See [Automate snapshots with SLM](/docs/deploy-manage/tools/snapshot-and-restore/create-snapshots#automate-snapshots-slm).
  </definition>
  <definition term="snapshot repository">
    Location where [snapshots](#glossary-snapshot) are stored. A snapshot repository can be a shared filesystem or a remote repository, such as Azure or Google Cloud Storage. See [Snapshot and restore](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore).
  </definition>
  <definition term="snapshot">
    Backup taken of a running [cluster](#glossary-cluster). You can take snapshots of the entire cluster or only specific [data streams](#glossary-data-stream) and [indices](#glossary-index). See [Snapshot and restore](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore).
  </definition>
  <definition term="solution">
    In Elastic Cloud, deployments with specialized [templates](#glossary-deployment-template) that are pre-configured with sensible defaults and settings for common use cases.
  </definition>
  <definition term="source field">
    Original JSON object provided during [indexing](#glossary-index). See the [`_source` field](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/mapping-source-field).
  </definition>
  <definition term="space">
    A place for organizing [dashboards](#glossary-dashboard), [visualizations](#glossary-visualization), and other [saved objects](#glossary-saved-object) by category. For example, you might have different spaces for each team, use case, or individual. See [Spaces](https://www.elastic.co/docs/deploy-manage/manage-spaces).
  </definition>
  <definition term="span">
    Information about the execution of a specific code path. [Spans](https://www.elastic.co/docs/solutions/observability/apm/spans) measure from the start to the end of an activity and can have a parent/child relationship with other spans.
  </definition>
  <definition term="split">
    Adds more [primary shards](#glossary-primary-shard) to an [index](#glossary-index).
  </definition>
  <definition term="stack rule">
    The general purpose rule types Kibana provides out of the box. Refer to [Stack rules](/docs/explore-analyze/alerting/alerts/rule-types#stack-rules).
  </definition>
  <definition term="standalone">
    This mode allows manual configuration and management of Elastic Agents locally on the systems where they are installed. See [Install standalone Elastic Agents](https://www.elastic.co/docs/reference/fleet/install-standalone-elastic-agent).
  </definition>
  <definition term="stunnel">
    Securely tunnels all traffic in an Elastic Cloud Enterprise installation.
  </definition>
  <definition term="system index">
    [Index](#glossary-index) containing configurations and other data used internally by the Elastic Stack. System index names start with a dot (`.`), such as `.security`. Do not directly access or change system indices.
  </definition>
</definitions>


## T

<definitions>
  <definition term="tag">
    A keyword or label that you assign to Kibana saved objects, such as dashboards and visualizations, so you can classify them in a way that is meaningful to you. Tags makes it easier for you to manage your content. See [Tags](https://www.elastic.co/docs/explore-analyze/find-and-organize/tags).
  </definition>
  <definition term="term join">
    A shared key that combines vector features with the results of an Elasticsearch terms aggregation. Term joins augment vector features with properties for data-driven styling and rich tooltip content in maps.
  </definition>
  <definition term="term">
    See [token](#glossary-token).
  </definition>
  <definition term="text">
    Unstructured content, such as a product description or log message. You typically [analyze](#glossary-analysis) text for better search. See [Text analysis](https://www.elastic.co/docs/manage-data/data-store/text-analysis).
  </definition>
  <definition term="time filter">
    A Kibana control that constrains the search results to a particular time period.
  </definition>
  <definition term="time series data stream">
    A type of [data stream](#glossary-data-stream) optimized for indexing metrics [time series data](#glossary-time-series-data). A TSDS allows for reduced storage size and for a sequence of metrics data points to be considered efficiently as a whole. See [Time series data stream](https://www.elastic.co/docs/manage-data/data-store/data-streams/time-series-data-stream-tsds).
  </definition>
  <definition term="time series data">
    A series of data points, such as logs, metrics and events, that is indexed in time order. Time series data can be indexed in a [data stream](#glossary-data-stream), where it can be accessed as a single named resource with the data stored across multiple backing indices. A [time series data stream](#glossary-time-series-data-stream) is optimized for indexing metrics data.
  </definition>
  <definition term="Timelion">
    A tool for building a time series visualization that analyzes data in time order. See [Timelion](https://www.elastic.co/docs/explore-analyze/dashboards).
  </definition>
  <definition term="token">
    A chunk of unstructured [text](#glossary-text) that's been optimized for search. In most cases, tokens are individual words. Tokens are also called terms. See [Text analysis](https://www.elastic.co/docs/manage-data/data-store/text-analysis).
  </definition>
  <definition term="tokenization">
    Process of breaking unstructured text down into smaller, searchable chunks called [tokens](#glossary-token). See [Tokenization](/docs/manage-data/data-store/text-analysis#tokenization).
  </definition>
  <definition term="trace">
    Defines the amount of time an application spends on a request. Traces are made up of a collection of transactions and spans that have a common root.
  </definition>
  <definition term="tracks">
    A layer type in the **Maps** application. This layer converts a series of point locations into a line, often representing a path or route.
  </definition>
  <definition term="trained model">
    A machine learning model that is trained and tested against a labeled data set and can be referenced in an ingest pipeline or in a pipeline aggregation to perform classification or regression analysis or [natural language processing](#glossary-nlp) on new data.
  </definition>
  <definition term="transaction">
    A special kind of [span](#glossary-span) that has additional attributes associated with it. [Transactions](https://www.elastic.co/docs/solutions/observability/apm/transactions) describe an event captured by an Elastic [APM agent](#glossary-apm-agent) instrumenting a service.
  </definition>
  <definition term="TSVB">
    A time series data visualizer that allows you to combine an infinite number of aggregations to display complex data. See [TSVB](https://www.elastic.co/docs/explore-analyze/dashboards).
  </definition>
</definitions>


## U

<definitions>
  <definition term="Upgrade Assistant">
    A tool that helps you prepare for an upgrade to the next major version of Elasticsearch. The assistant identifies the deprecated settings in your cluster and indices and guides you through resolving issues, including reindexing. See [Upgrade Assistant](https://www.elastic.co/docs/deploy-manage/upgrade/prepare-to-upgrade/upgrade-assistant).
  </definition>
  <definition term="Uptime">
    A metric of system reliability used to monitor the status of network endpoints through HTTP/S, TCP, and ICMP.
  </definition>
</definitions>


## V

<definitions>
  <definition term="vCPU">
    vCPU stands for virtual central processing unit. In Elastic Cloud, vCPUs are virtual compute units assigned to your nodes. The value is dependent on the size and hardware profile of the instance. The instance may be eligible for vCPU boosting depending on the size.
  </definition>
  <definition term="vector data">
    Points, lines, and polygons used to represent a map.
  </definition>
  <definition term="Vega">
    A declarative language used to create interactive visualizations. See [Vega](https://www.elastic.co/docs/explore-analyze/dashboards).
  </definition>
  <definition term="visualization">
    A graphical representation of query results in Kibana (for example, a histogram, line graph, pie chart, or heat map).
  </definition>
</definitions>


## W

<definitions>
  <definition term="warm phase">
    Second possible phase in the [index lifecycle](#glossary-index-lifecycle). In the warm phase, an [index](#glossary-index) is generally optimized for search and no longer updated. See [Index lifecycle](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management/index-lifecycle).
  </definition>
  <definition term="warm tier">
    [Data tier](#glossary-data-tier) that contains [nodes](#glossary-node) that hold time series data that is accessed less frequently and rarely needs to be updated. See [Data tiers](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers).
  </definition>
  <definition term="Watcher">
    The original suite of alerting features. See [Watcher](https://www.elastic.co/docs/explore-analyze/alerting/watcher).
  </definition>
  <definition term="Web Map Service (WMS)">
    A layer type in the **Maps** application. Add a WMS source to provide authoritative geographic context to your map. See the [OpenGIS Web Map Service](https://www.ogc.org/standards/wms).
  </definition>
  <definition term="worker">
    The filter thread model used by Logstash, where each worker receives an [event](#glossary-event) and applies all filters, in order, before emitting the event to the output queue. This allows scalability across CPUs because many filters are CPU intensive.
  </definition>
  <definition term="workpad">
    A workspace where you build presentations of your live data in [Canvas](#glossary-canvas). See [Create a workpad](https://www.elastic.co/docs/explore-analyze/visualize/canvas).
  </definition>
</definitions>


## X


## Y


## Z

<definitions>
  <definition term="ZooKeeper">
    A coordination service for distributed systems used by Elastic Cloud Enterprise to store the state of the installation. Responsible for discovery of hosts, resource allocation, leader election after failure and high priority notifications.
  </definition>
</definitions>
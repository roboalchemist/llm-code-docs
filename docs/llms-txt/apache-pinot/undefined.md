# Source: https://docs.pinot.apache.org/release-0.4.0/undefined.md

# Introduction

## What is Pinot?

Pinot is a real-time distributed OLAP datastore, built to deliver scalable real-time analytics with low latency. It can ingest from batch data sources (such as Hadoop HDFS, Amazon S3, Azure ADLS, Google Cloud Storage) as well as stream data sources (such as Apache Kafka).

Pinot was built by engineers at LinkedIn and Uber and is designed to scale up and out with no upper bound. Performance always remains constant based on the size of your cluster and an expected query per second (QPS) threshold.

{% hint style="info" %}
Join us in our Slack channel for questions, troubleshooting, and feedback. We'd love to hear from you. <https://communityinviter.com/apps/apache-pinot/apache-pinot>
{% endhint %}

![A modern OLAP platform for event-driven data warehousing](https://2688850955-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M69C48fK2BhCoou1REr%2F-M69DbDfcATcZOAgyX7k%2Fpinot-overview-graphic.png?alt=media\&token=3552722e-8d1d-4397-972e-a81917ced182)

## Get started

Our documentation is structured to let you quickly get to the content you need and is organized around the different concerns of users, operators, and developers. If you're new to Pinot and want to learn things by example, please take a look at our *getting started* section.

### Starter guides

{% content-ref url="basics/getting-started" %}
[getting-started](https://docs.pinot.apache.org/release-0.4.0/basics/getting-started)
{% endcontent-ref %}

To start importing data into Pinot, check out our guides on batch import and stream ingestion based on our [plugin architecture](https://docs.pinot.apache.org/release-0.4.0/plugins/plugin-architecture).

{% content-ref url="basics/data-import" %}
[data-import](https://docs.pinot.apache.org/release-0.4.0/basics/data-import)
{% endcontent-ref %}

### Query example

Pinot works very well for querying time series data with many dimensions and metrics over a vast unbounded space of records that scales linearly on a per node basis. Filters and aggregations are both easy and fast.

```sql
SELECT sum(clicks), sum(impressions) FROM AdAnalyticsTable
  WHERE 
       ((daysSinceEpoch >= 17849 AND daysSinceEpoch <= 17856)) AND 
       accountId IN (123456789)
  GROUP BY 
       daysSinceEpoch TOP 100
```

Pinot supports SQL for querying read-only data. Learn more about querying Pinot for time series data in our [PQL (Pinot Query Language)](https://docs.pinot.apache.org/release-0.4.0/users/user-guide-query/pinot-query-language) guide.

## Installation

Pinot may be deployed to and operated on a cloud provider or a local or virtual machine. You may get started either with a bare-metal installation or a Kubernetes one (either locally or in the cloud). To get immediately started with Pinot, check out these quick start guides for bootstrapping a Pinot cluster using Docker or Kubernetes.

### Standalone mode

{% content-ref url="basics/getting-started/running-pinot-locally" %}
[running-pinot-locally](https://docs.pinot.apache.org/release-0.4.0/basics/getting-started/running-pinot-locally)
{% endcontent-ref %}

{% content-ref url="basics/getting-started/running-pinot-in-docker" %}
[running-pinot-in-docker](https://docs.pinot.apache.org/release-0.4.0/basics/getting-started/running-pinot-in-docker)
{% endcontent-ref %}

### Cluster mode

{% content-ref url="basics/getting-started/kubernetes-quickstart" %}
[kubernetes-quickstart](https://docs.pinot.apache.org/release-0.4.0/basics/getting-started/kubernetes-quickstart)
{% endcontent-ref %}

{% content-ref url="basics/getting-started/advanced-pinot-setup" %}
[advanced-pinot-setup](https://docs.pinot.apache.org/release-0.4.0/basics/getting-started/advanced-pinot-setup)
{% endcontent-ref %}

## Learn

For a high-level overview that explains how Pinot works, please take a look at our basic concepts section.

{% content-ref url="basics/concepts" %}
[concepts](https://docs.pinot.apache.org/release-0.4.0/basics/concepts)
{% endcontent-ref %}

To understand the distributed systems architecture that explains Pinot's operating model, please take a look at our basic architecture section.

{% content-ref url="basics/architecture" %}
[architecture](https://docs.pinot.apache.org/release-0.4.0/basics/architecture)
{% endcontent-ref %}

## Overview

This section focuses on answering the most frequently asked questions for people exploring the newly evolving category of distributed OLAP engines. Pinot was created by authors at both Uber and LinkedIn and has been hardened and battle tested at the very highest of load and scale.

#### Is Pinot a data warehouse or a database?

While Pinot doesn't match the typical mold of a database product, it is best understood based on your role as either an analyst, data scientist, or application developer.

**Enterprise business intelligence**

For analysts and data scientists, Pinot is best viewed as a highly-scalable data platform for business intelligence. In this view, Pinot converges big data platforms with the traditional role of a data warehouse, making it a suitable replacement for analysis and reporting.

**Enterprise application development**

For application developers, Pinot is best viewed as an immutable aggregate store that sources events from streaming data sources, such as Kafka, and makes it available for query using SQL.

As is the case with a microservice architecture, data encapsulation ends up requiring each application to provision its own data store, as opposed to sharing one OLTP database for reads and writes. In this case, it becomes difficult to query the complete view of a domain because it becomes stored in many different databases. This is costly in terms of performance, since it requires joins across multiple microservices that expose their data over HTTP under a REST API. To prevent this, Pinot can be used to aggregate all of the data across a microservice architecture into one easily queryable view of the domain.

Pinot [tenants](https://docs.pinot.apache.org/release-0.4.0/basics/components/tenant) prevent any possibility of sharing ownership of database tables across microservice teams. Developers can create their own query models of data from multiple systems of record depending on their use case and needs. As with all aggregate stores, query models are eventually consistent and immutable.

### **Companies using Pinot**

| Company   | Notes                                                                                                                                                                                                                                                                                                                                                                      |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LinkedIn  | <p>Pinot originated at LinkedIn and it powers more 50+ user facing applications such as Who Viewed My Profile, Talent Analytics, Company Analytics, Ad Analytics and many more. Pinot also serves as the backend for to visualize and monitor 10,000+ business metrics.</p><p>Pinot runs on 1000+ nodes serving 100k+ queries while ingesting 1.5M+ events per second.</p> |
| Uber      | Pinot powers many internal and external dashboards as well as external site facing analytics applications like [UberEats Restaurant Analytics](https://eng.uber.com/restaurant-manager/).                                                                                                                                                                                  |
| Microsoft | Microsoft Teams uses Pinot for analytics on Teams product usage data.                                                                                                                                                                                                                                                                                                      |
| Weibo     | Weibo uses Pinot for realtime analytics on CDN & Weibo Video data to make business decisions, optimize service performance and improve user experience.                                                                                                                                                                                                                    |
| Factual   | Insight Product - <https://www.factual.com/products/insights/>                                                                                                                                                                                                                                                                                                             |

### Features

* A column-oriented database with various compression schemes such as Run Length, Fixed Bit Length
* Pluggable indexing technologies - Sorted Index, Bitmap Index, Inverted Index
* Ability to optimize query/execution plan based on query and segment metadata
* Near real time ingestion from streams and batch ingestion from Hadoop
* SQL-like language that supports selection, aggregation, filtering, group by, order by, distinct queries on data
* Support for multi-valued fields
* Horizontally scalable and fault-tolerant

### When should I use it?

Pinot is designed to execute OLAP queries with low latency. It is suited in contexts where fast analytics, such as aggregations, are needed on immutable data, possibly, with real-time data ingestion.

**User facing Analytics Products**

Pinot was originally built at LinkedIn to power rich interactive real-time analytic applications such as [Who Viewed Profile](https://www.linkedin.com/me/profile-views/urn:li:wvmp:summary/), [Company Analytics](https://www.linkedin.com/company/linkedin/insights/), [Talent Insights](https://business.linkedin.com/talent-solutions/talent-insights), and many more. [UberEats Restaurant Manager](https://eng.uber.com/restaurant-manager/) is another example of a customer facing Analytics App. At LinkedIn, Pinot powers 50+ user-facing products, ingesting ***millions of events per second*** and serving **100k+ queries per second** at millisecond latency.

**Real-time Dashboard for Business Metrics**

Pinot can be also be used to perform typical analytical operations such as **slice** and **dice**, **drill down**, **roll up**, and **pivot** on large scale multi-dimensional data. For instance, at LinkedIn, Pinot powers dashboards for thousands of business metrics. One can connect various BI tools such Superset, Tableau, or PowerBI to visualize data in Pinot.

Instructions to connect Pinot with Superset can found [here](https://docs.pinot.apache.org/release-0.4.0/integrations/superset).

**Anomaly Detection**

In addition to visualizing data in Pinot, one can run Machine Learning Algorithms to detect Anomalies on the data stored in Pinot. See [ThirdEye](https://docs.pinot.apache.org/release-0.4.0/integrations/thirdeye) for more information on how to use Pinot for Anomaly Detection and Root Cause Analysis.

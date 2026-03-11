# Source: https://docs.confluent.io/cloud/current/stream-governance/index.md

<a id="cloud-dg"></a>

# Stream Governance on Confluent Cloud

[Stream Governance](../_glossary.md#term-Stream-Governance) is built upon three key strategic pillars:

- [Stream Lineage](stream-lineage.md#cloud-stream-lineage) - Understand complex data relationships
  and uncover more insights with interactive, end-to-end maps of event streams.
- [Stream Catalog](stream-catalog.md#cloud-stream-catalog) - Increase collaboration and productivity
  with self-service data discovery that allows teams to classify, organize, and find the
  event streams they need.
- [Stream Quality](#cloud-stream-quality) - Deliver trusted, high-quality event streams
  to the business and maintain data integrity as services evolve.

To learn more about data governance, Stream Governance, and the strategies behind these new tools and products, see the brief introduction below.

## Demo: Overview of Stream Governance

This video demo shows how Confluent Stream Governance takes a fresh approach to data governance. Stream Governance not only enables data in motion,
but also gives you the real-time data governance tools built to help foster secure, compliant, and scalable collaboration and knowledge sharing necessary to become a real-time, event-centric business.

<iframe width="560" height="315" src="https://www.youtube.com/embed/2KNP1P9Wk-E" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Data governance

Data governance initiatives aim to manage the availability, integrity, and
security of data used across an organization. With the explosion in volume,
variety, and velocity of data powering the modern enterprise, itâs no surprise
that the management of that data has become paramount to the success of
companies across the globe. Data governance is now a mainstream, mandatory, and
critical force behind the âdata everywhereâ movement.

At its core, a data governance program consists of three key areas:

![icon-people](images/icon-people.png) The team that manages all aspects of your organizationâs data, with clearly defined roles and responsibilities.

![icon-processes](images/icon-processes.png) The processes and procedures for how data should be controlled, audited, secured, and monitored.

![icon-technology](images/icon-devices.png) The technology that enables people, and streamlines processes, with tools like standardization, monitoring,
collaboration, and reporting, just to name a few.

## Governance for Data in Motion

With the sharp rise of real-time data, the need for organizational governance
over data in motion is growing quickly. As investments into microservices
increase and data sources scale, it becomes more and more challenging for any
individual or team to understand or govern the full scope of streams flowing
across the business.

To enable a generation of event-centric enterprises, Confluent developed Stream
Governance: governance built for data in motion, allowing businesses to operate
around a central nervous system of real-time data.

With Confluentâs Stream Governance, companies can confidently share the power of
data in motion across the organization with a governance solution designed for
the intricacies of streaming data.

<a id="cloud-stream-quality"></a>

## Stream quality

Confluentâs stream quality tools enable teams to deliver a scalable supply of
trusted event streams throughout the business, enabling reliable delivery of
mission-critical applications, confident decision making, and a simplified
design for data standards. These tools set and control the data rules and
definitions by which the entire system operates. This determines what data gets
in and what data does not, all in the spirit of maintaining high data integrity.

- [Schema Registry](../sr/schemas-manage.md#sr-prv) allows teams to define and enforce universal
  data standards that enable scalable data compatibility while reducing operational
  complexity. Avro, JSON, and Protobuf serialization formats are supported.
- [Data Contracts and Data Quality Rules](../sr/fundamentals/data-contracts.md#sr-data-contracts)
  are supported in Schema Registry to expand on schemas and provide formal agreement
  between producers and consumers on the structure, evolution, and integrity constraints on data exchange.
  Data quality rules can specify the semantics of data fields, detail constraints on the data
  (such as requiring positive values for certain fields), describe the evolution and compatibility of schemas,
  and indicate data ownership.
- [Schema Validation](../sr/broker-side-schema-validation.md#cloud-schema-validation), enabled at the topic-level,
  ensures broker/registry coordination by verifying that schemas tied to incoming
  messages are both valid and assigned to the specific destination topic in order to publish.
- [Schema Linking](../sr/schema-linking.md#schema-linking) keeps schemas in sync across Schema Registry clusters.
  Optionally, use it in combination with [Geo-replication with Cluster Linking on Confluent Cloud](../multi-cloud/cluster-linking/index.md#cloud-cluster-linking) to keep both schemas and
  topic data in sync across Schema Registry and Kafka clusters.

<a id="dg-end-to-end-demo"></a>

## Demo

This video provides a real-world use case for Stream Governance, highlighting various aspects of stream catalog, Stream Lineage, data discovery, and data quality.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CTQmdLXtBWA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>&reg;

## Get started

To learn about Stream Governance packages and feature offerings, see [Manage Stream Governance Packages in Confluent Cloud](packages.md#stream-gov-packages).

To get started with Stream Governance, sign up for [Confluent Cloud](https://www.confluent.io/confluent-cloud/) and then try out the tutorials and
workflows in the sections below.

- [Stream Lineage](stream-lineage.md#cloud-stream-lineage), including [Stream Lineage first look](stream-lineage.md#stream-lineage-first-look)
  and [stream lineage tutorial](stream-lineage.md#stream-lineage-tutorial)
- [Stream Catalog](stream-catalog.md#cloud-stream-catalog), including [how to search for data and schemas](stream-catalog.md#data-discovery-search)
  and [how to create and use tags](stream-catalog.md#data-discovery-tagging)
- [Stream quality](#cloud-stream-quality), including guidelines on [working with schemas](../sr/schemas-manage.md#sr-prv),
  [using broker-side schema ID validation](../sr/broker-side-schema-validation.md#cloud-schema-validation), and [schema linking](../sr/schema-linking.md#schema-linking)
  to keep schemas in sync across Schema Registry clusters

## Related content

- Learn, Online Course: [Governing Data Streams](https://developer.confluent.io/learn-kafka/governing-data-streams/overview/)
- Podcast: [Building Real-Time Data Governance at Scale with Apache Kafka featuring Tushar Thole](https://developer.confluent.io/podcast/building-real-time-data-governance-at-scale-with-apache-kafka-ft-tushar-thole)
- Blog post: [Confluent Unlocks the Full Power of Event Streams with Stream Governance](https://www.confluent.io/blog/governing-data-with-confluent-stream-governance/)

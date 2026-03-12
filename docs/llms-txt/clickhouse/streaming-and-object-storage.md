# Source: https://clickhouse.ferndocs.com/cloud/reference/billing/clickpipes/streaming-and-object-storage.md

---
sidebar_label: Streaming and object storage
slug: /cloud/reference/billing/clickpipes/streaming-and-object-storage
title: ClickPipes for streaming and object storage
description: Overview of billing for streaming and object storage ClickPipes
doc_type: reference
keywords:

- billing
- clickpipes
- streaming pricing
- costs
- pricing

---

This section outlines the pricing model of ClickPipes for streaming and object storage.

## What does the ClickPipes pricing structure look like? [#what-does-the-clickpipes-pricing-structure-look-like]

It consists of two dimensions:

- **Compute**: Price **per unit per hour**.
  Compute represents the cost of running the ClickPipes replica pods whether they actively ingest data or not.
  It applies to all ClickPipes types.
- **Ingested data**: Price **per GB**.
  The ingested data rate applies to all streaming ClickPipes
  (Kafka, Confluent, Amazon MSK, Amazon Kinesis, Redpanda, WarpStream, Azure Event Hubs)
  for the data transferred via the replica pods. The ingested data size (GB) is charged based on bytes received from the source (uncompressed or compressed).

## What are ClickPipes replicas? [#what-are-clickpipes-replicas]

ClickPipes ingests data from remote data sources via a dedicated infrastructure
that runs and scales independently of the ClickHouse Cloud service.
For this reason, it uses dedicated compute replicas.

## What is the default number of replicas and their size? [#what-is-the-default-number-of-replicas-and-their-size]

Each ClickPipe defaults to 1 replica that is provided with 512 MiB of RAM and 0.125 vCPU (XS).
This corresponds to **0.0625** ClickHouse compute units (1 unit = 8 GiB RAM, 2 vCPUs).

## What are the ClickPipes public prices? [#what-are-the-clickpipes-public-prices]

- Compute: \$0.20 per unit per hour (\$0.0125 per replica per hour for the default replica size)
- Ingested data: \$0.04 per GB

The price for the Compute dimension depends on the **number** and **size** of replica(s) in a ClickPipe. The default replica size can be adjusted using vertical scaling, and each replica size is priced as follows:

| Replica Size               | Compute Units | RAM     | vCPU   | Price per Hour |
|----------------------------|---------------|---------|--------|----------------|
| Extra Small (XS) (default) | 0.0625        | 512 MiB | 0.125. | $0.0125        |
| Small (S)                  | 0.125         | 1 GiB   | 0.25   | $0.025         |
| Medium (M)                 | 0.25          | 2 GiB   | 0.5    | $0.05          |
| Large (L)                  | 0.5           | 4 GiB   | 1.0    | $0.10          |
| Extra Large (XL)           | 1.0           | 8 GiB   | 2.0    | $0.20          |

## How does it look in an illustrative example? [#how-does-it-look-in-an-illustrative-example]

The following examples assume a single M-sized replica, unless explicitly mentioned.

<table><thead>
  <tr>
    <th></th>
    <th>100 GB over 24h</th>
    <th>1 TB over 24h</th>
    <th>10 TB over 24h</th>
  </tr></thead>
<tbody>
  <tr>
    <td>Streaming ClickPipe</td>
    <td>(0.25 x 0.20 x 24) + (0.04 x 100) = \$5.20</td>
    <td>(0.25 x 0.20 x 24) + (0.04 x 1000) = \$41.20</td>
    <td>With 4 replicas: <br></br> (0.25 x 0.20 x 24 x 4) + (0.04 x 10000) = \$404.80</td>
  </tr>
  <tr>
    <td>Object Storage ClickPipe $^*$</td>
    <td>(0.25 x 0.20 x 24) = \$1.20</td>
    <td>(0.25 x 0.20 x 24) = \$1.20</td>
    <td>(0.25 x 0.20 x 24) = \$1.20</td>
  </tr>
</tbody>
</table>

$^1$ _Only ClickPipes compute for orchestration,
effective data transfer is assumed by the underlying Clickhouse Service_

## FAQ for streaming and object storage ClickPipes [#faq-streaming-and-object-storage]

<AccordionGroup>
<Accordion title="What are ClickPipes replicas?">
ClickPipes ingests data from remote data sources via a dedicated infrastructure
that runs and scales independently of the ClickHouse Cloud service.
For this reason, it uses dedicated compute replicas.
The diagrams below show a simplified architecture.

For streaming ClickPipes, ClickPipes replicas access the remote data sources (e.g., a Kafka broker),
pull the data, process and ingest it into the destination ClickHouse service.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d155c6de59e6df94e916fe13c09bcda3bc330469e3a2d13146e88cd201992310/images/cloud/manage/jan2025_faq/external_clickpipes_pricing_faq_1.png" alt="ClickPipes Replicas - Streaming ClickPipes"/>

In the case of object storage ClickPipes,
the ClickPipes replica orchestrates the data loading task
(identifying files to copy, maintaining the state, and moving partitions),
while the data is pulled directly from the ClickHouse service.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/36e0eb46d1b14b147733a5c033f5119f3ad7f011c9a51b234cec4e17b2fd1a0e/images/cloud/manage/jan2025_faq/external_clickpipes_pricing_faq_2.png" alt="ClickPipes Replicas - Object Storage ClickPipes"/>
</Accordion>
<Accordion title="What's the default number of replicas and their size?">
Each ClickPipe defaults to 1 replica that's provided with 2 GiB of RAM and 0.5 vCPU.
This corresponds to **0.25** ClickHouse compute units (1 unit = 8 GiB RAM, 2 vCPUs).
</Accordion>
<Accordion title="Can ClickPipes replicas be scaled?">
Yes, ClickPipes for streaming can be scaled both horizontally and vertically.
Horizontal scaling adds more replicas to increase throughput, while vertical scaling increases the resources (CPU and RAM) allocated to each replica to handle more intensive workloads.
This can be configured during ClickPipe creation, or at any other point under **Settings** -> **Advanced Settings** -> **Scaling**.
</Accordion>
<Accordion title="How many ClickPipes replicas do I need?">
It depends on the workload throughput and latency requirements.
We recommend starting with the default value of 1 replica, measuring your latency, and adding replicas if needed.
Keep in mind that for Kafka ClickPipes, you also have to scale the Kafka broker partitions accordingly.
The scaling controls are available under "settings" for each streaming ClickPipe.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/194aa9090bc57a5080d75aba0409903e88f3ff6e3868eff278b37084a63fa1ca/images/cloud/manage/jan2025_faq/external_clickpipes_pricing_faq_3.png" alt="ClickPipes Replicas - How many ClickPipes replicas do I need?"/>
</Accordion>
<Accordion title="What does the ClickPipes pricing structure look like?">
It consists of two dimensions:
- **Compute**: Price per unit per hour
  Compute represents the cost of running the ClickPipes replica pods whether they actively ingest data or not.
  It applies to all ClickPipes types.
- **Ingested data**: per GB pricing
  The ingested data rate applies to all streaming ClickPipes
  (Kafka, Confluent, Amazon MSK, Amazon Kinesis, Redpanda, WarpStream,
  Azure Event Hubs) for the data transferred via the replica pods.
  The ingested data size (GB) is charged based on bytes received from the source (uncompressed or compressed).
</Accordion>
<Accordion title="What are the ClickPipes public prices?">
- Compute: \$0.20 per unit per hour ($0.05 per replica per hour)
- Ingested data: $0.04 per GB
</Accordion>
<Accordion title="How does it look in an illustrative example?">
For example, ingesting 1 TB of data over 24 hours using the Kafka connector using a single replica (0.25 compute unit) costs:

$
(0.25 \times 0.20 \times 24) + (0.04 \times 1000) = \$41.2
$
<br/>

For object storage connectors (S3 and GCS),
only the ClickPipes compute cost is incurred since the ClickPipes pod is not processing data
but only orchestrating the transfer which is operated by the underlying ClickHouse service:

$
0.25 \times 0,20 \times 24 = \$1.2
$
</Accordion>
<Accordion title="How does ClickPipes pricing compare to the market?">
The philosophy behind ClickPipes pricing is
to cover the operating costs of the platform while offering an easy and reliable way to move data to ClickHouse Cloud.
From that angle, our market analysis revealed that we are positioned competitively.
</Accordion>
</AccordionGroup>

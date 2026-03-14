# Source: https://docs.snowflake.com/en/collaboration/use-auto-fulfillment-with-open-table-formats.md

# Using auto-fulfillment with open table formats

Cross-Cloud Auto-Fulfillment for listings enables you to share open table formats — including [Apache Iceberg™ tables](../user-guide/tables-iceberg.md) and Delta
Lake tables — with internal and external consumers across cloud providers and regions. The tables can be managed by Snowflake or any other
catalog provider. Cross-Cloud Auto-Fulfillment optimizes data transfer costs and ensures data availability across all regions, without
requiring you to maintain extract, transform, and load (ETL) jobs.

Cross-Cloud Auto-Fulfillment reads data directly from the external volume and replicates all data as a Snowflake-managed Iceberg table
within the target regions. For this process, providers are charged for the consumption of the Snowflake-managed data, including egress,
storage, and compute. Virtual Private Snowflake (VPS) rates for compute will only apply if you or your consumers are using VPS. Data
transfer is charged at the same replication rate listed in the serverless feature table in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

> **Note:**
>
> This feature is supported for private listings, public listings in the Snowflake Marketplace, and listings on the Internal Marketplace.

## Tutorials

Snowflake provides the following tutorial for creating an Iceberg table using SQL:
[Tutorial: Create your first Apache Iceberg™ table](../user-guide/tutorials/create-your-first-iceberg-table.md)

## Getting started with Cross-Cloud Auto-Fulfillment for Iceberg tables

[Tutorial: Create your first Apache Iceberg™ table](../user-guide/tutorials/create-your-first-iceberg-table.md) describes how to create an Iceberg table. After the table is created, you can
create a Snowflake listing that includes this table and then provide it to consumers across any region or cloud. Consumers can access the
listing, and Snowflake will manage the data egress, replication, and storage. For more information on how to create a listing, see [Create a
new listing](https://other-docs.snowflake.com/en/collaboration/provider-listings-creating-publishing).

## Accessing Iceberg tables as a consumer

As a consumer, you can access and query shared Iceberg tables. For more information, see [Access and install listings as a consumer](https://other-docs.snowflake.com/collaboration/consumer-listings-access). New
changes to the Iceberg will be synched from the provider account to your account based on your configured auto-fulfillment refresh
frequency. For more information, see [How auto-fulfillment works](provider-listings-auto-fulfillment.md).

## Limitations

Cross-Cloud Auto-Fulfillment for listings is subject to the following limitations:

* You cannot replicate CATALOG or any CATALOG-related information.
* Catalog-linked databases (CLDs) are not supported.
* You cannot access the secure share area created in consumer regions by Cross-Cloud Auto-Fulfillment.
* [Egress cost optimizer (ECO)](provider-listings-auto-fulfillment-eco.md) replication support isn’t available for
  individual files that are larger than 5 GB.
* The following objects are not supported:

  * Streams and dynamic tables on shared Iceberg tables.
  * Streams and dynamic tables on views with a shared Iceberg table base.
  * Streams and dynamic tables on shared views with Iceberg base tables.
  * V3 Iceberg tables.

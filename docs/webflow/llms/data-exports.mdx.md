# Source: https://developers.webflow.com/browser/data-exports.mdx

***

title: Data Exports
slug: data-exports
layout: overview
description: Export Webflow Analyze & Optimize data to your data warehouse
hidden: true
hide-toc: true
'og:title': 'Data Exports: Webflow Analyze & Optimize'
'og:description': >-
Export your Webflow Analyze & Optimize data to data warehouses like Snowflake,
BigQuery, and Redshift
subtitle: Export Webflow Analyze & Optimize data to your data warehouse
-----------------------------------------------------------------------

Data Exports lets you send your Webflow Analyze and Optimize data directly to your preferred data warehouse. Connect to popular destinations like Snowflake, Google BigQuery, Amazon Redshift, and more to centralize your analytics data for deeper analysis and reporting.

## What you can do with Data Exports

<CardGroup>
  <Card
    title="Connect to data warehouses"
    iconPosition="left"
    href="/browser/data-exports/destinations"
    iconSize="12"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CloudHosting.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CloudHosting.svg" alt="" className="light-icon" />
            </>
        }
  >
    Connect to Snowflake, BigQuery, Redshift, Databricks, and 18+ other destinations
  </Card>

  <Card
    title="Export Analyze data"
    iconPosition="left"
    href="/browser/data-exports/data-schema#analyze-data-models"
    iconSize="12"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/OptimizeUser.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/OptimizeUser.svg" alt="" className="light-icon" />
            </>
        }
  >
    Access page view and element click data
  </Card>

  <Card
    title="Export Optimize data"
    iconPosition="left"
    iconSize="12"
    href="/browser/data-exports/data-schema#optimize-data-models"
    icon={  
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Test.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Test.svg" alt="" className="light-icon" />
            </>
        }
  >
    Access variation viewed data for your optimizations
  </Card>
</CardGroup>

## Prerequisites

Before setting up Data Exports, ensure you have:

* A Webflow site with the **Analyze** and/or **Optimize** add-on and an eligible **Enterprise** plan
* Access to one of the [supported data destinations](/browser/data-exports/destinations)
* Administrative access to configure your data warehouse credentials

## How it works

<Steps>
  ### Choose your destination

  Select from 22+ supported data destinations, including OLAP data warehouses, OLTP databases, object storage, and more. See the full list in [Data destinations](/browser/data-exports/destinations).

  ### Configure the connection

  Follow the setup guide for your chosen destination to create the necessary credentials, users, and permissions. Each destination has specific configuration requirements.

  ### Start receiving data

  Webflow exports Analyze and Optimize data to your data warehouse as properly typed tables on a nightly basis.
</Steps>

## FAQs

<Accordion title="What data is included in the export?">
  The data included depends on your subscription. Analyze customers receive site analytics data like page views, and elements clicked. Optimize customers receive experiment data about variations viewed. Customers with both receive all available data. See [Data schema](/browser/data-exports/data-schema) for more details.

  <Info>
    **Historical data is not included**

    Only data from the established connection date going forward will be included in the daily exports.
  </Info>
</Accordion>

<Accordion title="How often is data exported?">
  Data is exported on a nightly basis (every 24 hours) to your configured destination.
</Accordion>

<Accordion title="What destinations are supported?">
  Data Exports supports 22+ destinations including Snowflake, Google BigQuery, Amazon Redshift, Databricks, PostgreSQL, MySQL, Amazon S3, Google Cloud Storage, and more. See [Data destinations](/browser/data-exports/destinations) for the complete list of supported destinations.
</Accordion>

# Source: https://fly.io/docs/mpg

Title: Managed Postgres

URL Source: https://fly.io/docs/mpg

Published Time: Thu, 26 Feb 2026 22:12:43 GMT

Markdown Content:
Managed Postgres · Fly Docs
===============

[Skip to content](https://fly.io/docs/mpg#main-content-start)

[](https://fly.io/)[](https://fly.io/docs/)

[**Need a Logo?** View Our Brand Assets](https://fly.io/docs/about/brand/)

Open main menu[](https://fly.io/)[](https://fly.io/docs/)

[Pricing](https://fly.io/pricing/)[Support](https://fly.io/docs/about/support/)

[Sign In](https://fly.io/app/sign-in/)[Sign Up](https://fly.io/app/sign-up/)

[Docs Index](https://fly.io/docs/)[Managed Postgres](https://fly.io/docs/mpg/)
*   [Managed Postgres Overview](https://fly.io/docs/mpg/)

Getting Started Toggle Getting Started section
*   [Create and Connect to a Managed Postgres Cluster](https://fly.io/docs/mpg/create-and-connect/)
*   [Cluster Configuration Options](https://fly.io/docs/mpg/configuration/)

Guides and Examples Toggle Guides and Examples section
*   [Phoenix with Managed Postgres](https://fly.io/docs/mpg/guides-examples/phoenix-guide/)

Management Toggle Management section
*   [Monitoring and Metrics](https://fly.io/docs/mpg/metrics/)
*   [Import data from another postgres cluster](https://fly.io/docs/mpg/import/)
*   [Supported Postgres Extensions](https://fly.io/docs/mpg/extensions/)

--- title: Managed Postgres layout: docs nav: mpg date: 2025-07-10 redirect_from: /docs/mpg/overview/ --- <figure class="flex justify-center"><img src="/static/images/Managed_Postgres.png" alt="Illustration by Annie Ruygt of a balloon doing a lot of tasks" class="w-full max-w-lg mx-auto"></figure> ## What is Managed Postgres? Fly.io's Managed Postgres is our fully-managed database service that handles all aspects of running production PostgreSQL databases where we take care of: - Automatic backups and recovery - High availability with automatic failover - Performance monitoring and metrics - Resource scaling (CPU, RAM, storage) - 24/7 support and incident response - Automatic encryption of data at rest and in transit ### What's included You'll be able to access: - A highly-available Postgres cluster within your Fly.io organization's [private network](/docs/networking/private-networking/) - Multiple databases and schemas on that cluster - Fly.io Support Portal to log tickets and get help - Any trusted extensions included in the [default Postgres 16 distribution](https://www.postgresql.org/docs/16/contrib.html) - The third party `pgvector` extension for vector similarity search - The third party `PostGIS` extension for adding geospatial data support, if enabled when provisioning your database ### What's not there yet At the moment, the following features are under development: - Security patches and version upgrades - Third Party Postgres extensions besides `pgvector` or `postGIS` - Customer-facing alerting - Database migration tools We're working on expanding these capabilities and will provide updates as they become available. ## Regions The current regions available for deploying Fly.io Managed Postgres are: - `ams` - Amsterdam, Netherlands - `fra` - Frankfurt, Germany - `gru` - São Paulo, Brazil - `iad` - Ashburn, Virginia, USA - `lax` - Los Angeles, California, USA - `lhr` - London, United Kingdom - `nrt` - Tokyo, Japan - `ord` - Chicago, Illinois, USA - `sin` - Singapore - `sjc` - San Jose, California, USA - `syd` - Sydney, Australia - `yyz` - Toronto, Canada We'll be rolling out more regions as soon as we can. Choose a region close to your application for optimal performance. ## Database Storage Managed Postgres storage features: - Maximum storage limit: 1 TB - Initial storage size: Up to 500 GB at creation - Storage is replicated across all nodes in your cluster - Storage growth is monitored and managed automatically ## Pricing The price of running Fly.io Managed Postgres depends on: - Your selected Managed Postgres Plan - The amount of storage your cluster has Your MPG plan determines the CPU and Memory configuration for your cluster. All plans include high availability, backups, and connection pooling. The current monthly plan pricing is: | Plan | CPU | Memory | Monthly Price | | --- | --- | --- | --- | | Basic | Shared-2x | 1GB | $38.00 | | Starter | Shared-2x | 2GB | $72.00| | Launch | Performance-2x| 8GB | $282.00 | | Scale | Performance-4x | 32GB | $962.00 | | Performance | Performance-8x | 64GB | $1,922.00 | Database storage is priced at **$0.28 per provisioned GB for a 30-day month**. For example, if you have 10GB of storage provisioned for your cluster, your monthly storage cost will be $2.80. Clusters created or deleted mid-month will have their pricing prorated accordingly. Starting February 2026, inter-region private network usage will be charged at the [same rate](/docs/about/pricing/#data-transfer-pricing) as Machines. It will also share the same free quota as existing private network usage. There will be no charges for transfer within the same region. 

[Docs](https://fly.io/docs/)Managed Postgres
Managed Postgres
================

![Image 1: Illustration by Annie Ruygt of a balloon doing a lot of tasks](https://fly.io/static/images/Managed_Postgres.png)
[](https://fly.io/docs/mpg#what-is-managed-postgres)What is Managed Postgres?
-----------------------------------------------------------------------------

Fly.io’s Managed Postgres is our fully-managed database service that handles all aspects of running production PostgreSQL databases where we take care of:

*   Automatic backups and recovery 
*   High availability with automatic failover 
*   Performance monitoring and metrics 
*   Resource scaling (CPU, RAM, storage) 
*   24/7 support and incident response 
*   Automatic encryption of data at rest and in transit 

### [](https://fly.io/docs/mpg#whats-included)What’s included

You’ll be able to access:

*   A highly-available Postgres cluster within your Fly.io organization’s [private network](https://fly.io/docs/networking/private-networking/)
*   Multiple databases and schemas on that cluster 
*   Fly.io Support Portal to log tickets and get help 
*   Any trusted extensions included in the [default Postgres 16 distribution](https://www.postgresql.org/docs/16/contrib.html)
*   The third party `pgvector` extension for vector similarity search 
*   The third party `PostGIS` extension for adding geospatial data support, if enabled when provisioning your database 

### [](https://fly.io/docs/mpg#whats-not-there-yet)What’s not there yet

At the moment, the following features are under development:

*   Security patches and version upgrades 
*   Third Party Postgres extensions besides `pgvector` or `postGIS`
*   Customer-facing alerting 
*   Database migration tools 

We’re working on expanding these capabilities and will provide updates as they become available.

[](https://fly.io/docs/mpg#regions)Regions
------------------------------------------

The current regions available for deploying Fly.io Managed Postgres are:

*   `ams` - Amsterdam, Netherlands 
*   `fra` - Frankfurt, Germany 
*   `gru` - São Paulo, Brazil 
*   `iad` - Ashburn, Virginia, USA 
*   `lax` - Los Angeles, California, USA 
*   `lhr` - London, United Kingdom 
*   `nrt` - Tokyo, Japan 
*   `ord` - Chicago, Illinois, USA 
*   `sin` - Singapore 
*   `sjc` - San Jose, California, USA 
*   `syd` - Sydney, Australia 
*   `yyz` - Toronto, Canada 

We’ll be rolling out more regions as soon as we can. Choose a region close to your application for optimal performance.

[](https://fly.io/docs/mpg#database-storage)Database Storage
------------------------------------------------------------

Managed Postgres storage features:

*   Maximum storage limit: 1 TB 
*   Initial storage size: Up to 500 GB at creation 
*   Storage is replicated across all nodes in your cluster 
*   Storage growth is monitored and managed automatically 

[](https://fly.io/docs/mpg#pricing)Pricing
------------------------------------------

The price of running Fly.io Managed Postgres depends on:

*   Your selected Managed Postgres Plan 
*   The amount of storage your cluster has 

Your MPG plan determines the CPU and Memory configuration for your cluster. All plans include high availability, backups, and connection pooling.

The current monthly plan pricing is:

Wrap text

| Plan | CPU | Memory | Monthly Price |
| --- | --- | --- | --- |
| Basic | Shared-2x | 1GB | $38.00 |
| Starter | Shared-2x | 2GB | $72.00 |
| Launch | Performance-2x | 8GB | $282.00 |
| Scale | Performance-4x | 32GB | $962.00 |
| Performance | Performance-8x | 64GB | $1,922.00 |

Database storage is priced at **$0.28 per provisioned GB for a 30-day month**. For example, if you have 10GB of storage provisioned for your cluster, your monthly storage cost will be $2.80.

Clusters created or deleted mid-month will have their pricing prorated accordingly.

Starting February 2026, inter-region private network usage will be charged at the [same rate](https://fly.io/docs/about/pricing/#data-transfer-pricing) as Machines. It will also share the same free quota as existing private network usage. There will be no charges for transfer within the same region.

Copy page as markdown or[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fmpg%2Findex.html.md)

[Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Managed+Postgres%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fmpg%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fmpg%2Findex.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Managed+Postgres%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/mpg/index.html.md)

[On this page](https://fly.io/docs/mpg#)
*   [What is Managed Postgres?](https://fly.io/docs/mpg#what-is-managed-postgres)
    *   [What’s included](https://fly.io/docs/mpg#whats-included)
    *   [What’s not there yet](https://fly.io/docs/mpg#whats-not-there-yet)

*   [Regions](https://fly.io/docs/mpg#regions)
*   [Database Storage](https://fly.io/docs/mpg#database-storage)
*   [Pricing](https://fly.io/docs/mpg#pricing)

Copy page as markdown[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fmpg%2Findex.html.md)

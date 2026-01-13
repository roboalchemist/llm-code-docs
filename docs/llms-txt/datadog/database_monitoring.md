# Source: https://docs.datadoghq.com/database_monitoring.md

---
title: Database Monitoring
description: Learn about Database Monitoring and get started
breadcrumbs: Docs > Database Monitoring
source_url: https://docs.datadoghq.com/index.html
---

# Database Monitoring

{% callout %}
##### Join an enablement webinar session

With Database Monitoring, learn how to quickly pinpoint costly and slow queries. Drill into precise execution details to address bottlenecks.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=Database)
{% /callout %}

Datadog Database Monitoring provides deep visibility into databases across all of your hosts. Dig into historical query performance metrics, explain plans, and host-level metrics all in one place, to understand the health and performance of your databases and troubleshoot issues as they arise.

## Getting started{% #getting-started %}

Datadog Database Monitoring supports self-hosted and managed cloud versions of **Postgres**, **MySQL**, **Oracle**, **SQL Server**, **MongoDB**, and **Amazon DocumentDB**. To get started with Datadog Database Monitoring, configure your database and install the Datadog Agent. For setup instructions, select your database technology:

### Postgres{% #postgres %}

- [Selfhosted](https://docs.datadoghq.com/database_monitoring/setup_postgres/selfhosted)
- [RDS](https://docs.datadoghq.com/database_monitoring/setup_postgres/rds)
- [Aurora](https://docs.datadoghq.com/database_monitoring/setup_postgres/aurora)
- [Google Cloud SQL](https://docs.datadoghq.com/database_monitoring/setup_postgres/gcsql)
- [Google Cloud SQL](https://docs.datadoghq.com/database_monitoring/setup_postgres/alloydb)
- [PostgreSQL](https://docs.datadoghq.com/database_monitoring/setup_postgres/azure)
- [PostgreSQL](https://docs.datadoghq.com/database_monitoring/setup_postgres/heroku)



### MySQL{% #mysql %}

- [Selfhosted](https://docs.datadoghq.com/database_monitoring/setup_mysql/selfhosted)
- [RDS](https://docs.datadoghq.com/database_monitoring/setup_mysql/rds)
- [Aurora](https://docs.datadoghq.com/database_monitoring/setup_mysql/aurora)
- [Google Cloud SQL](https://docs.datadoghq.com/database_monitoring/setup_mysql/gcsql)
- [MySQL](https://docs.datadoghq.com/database_monitoring/setup_mysql/azure)



### Oracle{% #oracle %}

- [Selfhosted](https://docs.datadoghq.com/database_monitoring/setup_oracle/selfhosted)
- [RDS](https://docs.datadoghq.com/database_monitoring/setup_oracle/rds)
- [RAC](https://docs.datadoghq.com/database_monitoring/setup_oracle/rac)
- [Exadata](https://docs.datadoghq.com/database_monitoring/setup_oracle/exadata)
- [Selfhosted](https://docs.datadoghq.com/database_monitoring/setup_oracle/autonomous_database)



### SQL Server{% #sql-server %}

- [Selfhosted](https://docs.datadoghq.com/database_monitoring/setup_sql_server/selfhosted)
- [RDS](https://docs.datadoghq.com/database_monitoring/setup_sql_server/rds)
- [Aurora](https://docs.datadoghq.com/database_monitoring/setup_sql_server/azure)
- [Google Cloud SQL](https://docs.datadoghq.com/database_monitoring/setup_sql_server/gcsql)



### MongoDB{% #mongodb %}

- [Self-hosted](https://docs.datadoghq.com/database_monitoring/setup_mongodb/selfhosted)
- [MongoDB Atlas](https://docs.datadoghq.com/database_monitoring/setup_mongodb/mongodbatlas)



### Amazon DocumentDB{% #amazon-documentdb %}

- [Amazon DocumentDB](https://docs.datadoghq.com/database_monitoring/setup_documentdb/amazon_documentdb)



## Explore Datadog Database Monitoring{% #explore-datadog-database-monitoring %}

Navigate to [Database Monitoring](https://app.datadoghq.com/databases) in Datadog.

### Dig into query performance metrics{% #dig-into-query-performance-metrics %}

The [Query Metrics view](https://docs.datadoghq.com/database_monitoring/query_metrics/) shows historical query performance for normalized queries. Visualize performance trends by infrastructure or custom tags such as datacenter availability zone, and set alerts for anomalies.

- Identify slow queries and which queries are consuming the most time.
- Show database-level metrics not captured by APM such as rows updated/returned.
- Filter and group queries by arbitrary dimensions such as team, user, cluster, and host.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm-query-metrics-2.2ef6dd60b331534effaa48eecfc19305.png?auto=format"
   alt="Database Monitoring" /%}

### Explore query samples{% #explore-query-samples %}

The [Query Samples view](https://docs.datadoghq.com/database_monitoring/query_samples/) helps you understand which queries are running at a given time. Compare each execution to the average performance of the query and related queries.

- Identify unusually slow but infrequent queries not captured by metrics.
- Find outliers in a query's execution time or execution cost.
- Attribute a specific query execution to a user, application, or client host.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm-query-sample-2.93171cf7c63bb3d848d793518b748152.png?auto=format"
   alt="Database Monitoring" /%}

### Understand before you run{% #understand-before-you-run %}

[Explain Plans](https://docs.datadoghq.com/database_monitoring/query_metrics/#explain-plans) help you understand how the database plans to execute your queries.

- Step through each operation to identify bottlenecks.
- Improve query efficiency and save on costly sequential scans on large tables.
- See how a query's plan changes over time.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm-explain-plan-3.22b2584abf740c5b16d63df99fe3e7c9.png?auto=format"
   alt="Database Monitoring" /%}

### Visualize everything on enriched dashboards{% #visualize-everything-on-enriched-dashboards %}

Quickly pinpoint problem areas by viewing database and system metrics together on enriched integration dashboards for both self-hosted and cloud-managed instances. Clone dashboards for customization and enhancement with your own custom metrics. Click the **Dashboards** link at the top of the Query Metrics and Query Samples pages to go to the Database Monitoring dashboards.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm-dashboard-postgres.9320a80bb33b7280060b8de43be16d55.png?auto=format"
   alt="Database Monitoring" /%}

### Optimize host health and performance{% #optimize-host-health-and-performance %}

On the [Databases page](https://app.datadoghq.com/databases), you can assess the health and activity of your database hosts. Sort and filter the list to prioritize hosts with triggered alerts, high query volume, and other criteria. Click on an individual host to view details such as its configuration, common blocking queries, and calling services. See [Exploring Database Hosts](https://docs.datadoghq.com/database_monitoring/database_hosts/) for details.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/databases-list.cfaff8755d54fa53e0430efdc1457aba.png?auto=format"
   alt="The Databases page in Datadog" /%}

### View optimization recommendations{% #view-optimization-recommendations %}

The [Recommendations page](https://docs.datadoghq.com/database_monitoring/recommendations/) highlights problems and optimization opportunities, helping you save time by prioritizing what's most important. Select a recommendation to view details, including a summary of the problem, as well as potential next steps to address the issue.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/recommendations-page.d994cc2e2cfa6b76d2b487b5fac5db8c.png?auto=format"
   alt="The Recommendations page in Datadog" /%}

## Further Reading{% #further-reading %}

{% callout %}
##### Try Monitoring a Postgres Database with Datadog DBM in the Learning Center

The Datadog Learning Center is full of hands-on courses to help you learn about this topic. Enroll at no cost to identify inefficiencies and optimize your Postgres database.

[ENROLL NOW](https://learn.datadoghq.com/courses/database-monitoring)
{% /callout %}

- [Improve database host and query performance with Database Monitoring Recommendations](https://www.datadoghq.com/blog/database-monitoring-recommendations/)
- [Monitor and visualize database performance](https://www.datadoghq.com/blog/database-performance-monitoring-datadog)
- [Monitor SQL Server and Azure managed databases with Datadog DBM](https://www.datadoghq.com/blog/sql-server-and-azure-managed-services-database-monitoring/)
- [Track and troubleshoot MongoDB performance with Datadog Database Monitoring](https://www.datadoghq.com/blog/mongodb-database-monitoring/)
- [How microservice architectures have shaped the usage of database technologies](https://www.datadoghq.com/blog/datadog-database-research/)
- [Data Collected](https://docs.datadoghq.com/database_monitoring/data_collected/)
- [Troubleshooting](https://docs.datadoghq.com/database_monitoring/troubleshooting/)
- [Join an interactive session to level up your Database Monitoring](https://dtdg.co/fe)

# Source: https://www.aptible.com/docs/how-to-guides/observability-guides/setup-newrelic-agent-database.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to collect database-specific metrics using the New Relic agent

> Learn how to collect database metrics using the New Relic agent on Aptible

## Overview

This guide provides instructions on how to use our sample repository to run the New Relic agent as an Aptible container and collect custom database metrics. The sample repository can be found at [Aptible's New Relic Metrics Example](https://github.com/aptible/newrelic-metrics-example/).

By following this guide, you will be able to deploy the New Relic agent alongside your database and collect database-specific metrics for monitoring and analysis.

## New Relic

The example repo demonstrates how to configure the New Relic Agent to monitor PostgreSQL databases hosted on Aptible and report custom metrics to your New Relic account. However, the Agent can also be configured to collect database-specific metrics for the following database types:

* [ElasticSearch](https://github.com/newrelic/nri-elasticsearch)
* [MongoDB](https://github.com/newrelic/nri-mongodb)
* [MySQL](https://github.com/newrelic/nri-mysql)
* [PostgreSQL](https://github.com/newrelic/nri-postgresql)
* [RabbitMQ](https://github.com/newrelic/nri-rabbitmq)
* [Redis](https://github.com/newrelic/nri-redisb)

The example repo already installs the packages for the above database types, so the configuration file would just need to be added for each specific database type needing to be monitored, based on using the example in the above New Relic repo links.

## Troubleshooting

* No metrics appearing in New Relic: Verify that your NEW\_RELIC\_LICENSE\_KEY is correct and that the agent is running. Use [aptible logs](/reference/aptible-cli/cli-commands/cli-logs) or a [Log Drain]() to inspect logs from the agent to see if there are any specific errors blocking delivery of metrics.
* Connection issues: Ensure that the database connection URL is accessible from the Aptible container. In Aptible's platform, the agent must be running in the same Stack as the Aptible database(s) being monitored.

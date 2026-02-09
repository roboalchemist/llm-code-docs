# Source: https://www.aptible.com/docs/how-to-guides/observability-guides/setup-datadog-apm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up Datadog APM

> Guide for setting up Datadog Application Performance Monitoring (APM) on your Aptible apps

## Overview

Datadog APM (Application Performance Monitoring) can be configured with Aptible to monitor and analyze the performance of Aptible apps and databases in real-time.

<AccordionGroup>
  <Accordion title="Setting Up the Datadog Agent">
    To use the Datadog APM on Aptible, you'll need to deploy the Datadog Agent as an App on Aptible, set a few configuration variables, and expose it through a HTTPS endpoint.

    ```shell  theme={null}
    aptible apps:create datadog-agent
    aptible config:set --app datadog-agent DD_API_KEY=foo DD_HOSTNAME=aptible
    aptible deploy --app datadog-agent --docker-image=datadog/agent:7
    aptible endpoints:https:create --app datadog-agent --default-domain cmd --internal
    ```

    The example above deploys the Datadog Agent v7 from Dockerhub, an endpoint with a default domain, and also sets two required configuration variables.

    * `DD_API_KEY` should be set to an [API Key](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys) associated with your Datadog Organization.
    * `DD_HOSTNAME` is a hostname identifier. Because Aptible does not grant containers permission to runtime information, you'll need explicitly set a hostname. While this can be anything, we recommend using this variable to help identify what the agent is monitoring.

    <Note>
      If you intend to use the Datadog APM for Database Monitoring, you'll need to make some adjustments to point the Datadog Agent at the database(s) you want to monitor. We go over these changes in the Setting Up Database Monitoring section below.
    </Note>
  </Accordion>

  <Accordion title="Setting Up Applications">
    To deliver data to Datadog, you'll need to instrument your application for tracing, as well as connect it to the Datadog Agent.

    Datadog provides a number of guides on how to set up your application for tracing. Follow the guide most relevant for your application to set up tracing.

    * [All Tracing Guides](https://docs.datadoghq.com/tracing/guide/)
    * [All Tracing Libraries](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/)
    * [Tutorial - Enabling Tracing for a Java Application and Datadog Agent in Containers](https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-containers/)
    * [Tutorial - Enabling Tracing for a Python Application and Datadog Agent in Containers](https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-containers/)
    * [Tutorial - Enabling Tracing for a Go Application and Datadog Agent in Containers](https://docs.datadoghq.com/tracing/guide/tutorial-enable-go-containers/)

    To connect to the Datadog Agent, set the `DD_TRACE_AGENT_URL` configuration variable for each App.

    ```shell  theme={null}
    aptible config:set --app yourapp DD_TRACE_AGENT_URL=https://app-42.on-aptible.com:443
    ```

    You'll want `DD_TRACE_AGENT_URL` to be set to the hostname of the endpoint you created, with `:443` appended to the end to specify the listening port 443.
  </Accordion>

  <Accordion title="Setting Up Databases for Metrics Collection">
    Datadog offers integrations for various databases, including integrations for Redis, PostgreSQL, and MySQL through the Datadog Agent.
    For each database you want to integrate with, you'll need to follow Datadog's specific integration guide to prepare the database.

    * [All Integrations](https://docs.datadoghq.com/integrations/)
    * [PostgreSQL Integration Guide](https://docs.datadoghq.com/integrations/postgres/?tab=host)
    * [Redis Integration Guide](https://docs.datadoghq.com/integrations/redisdb/?tab=host)
    * [MySQL Integration Guide](https://docs.datadoghq.com/integrations/mysql/?tab=host)

    In addition, you'll also need to adjust the Datadog Agent application deployed on Aptible to point at your databases. This involves creating a Dockerfile for the Datadog Agent and [Deploying with Git](https://www.aptible.com/docs/core-concepts/apps/deploying-apps/image/deploying-with-git/overview).
    How your Dockerfile looks will differ slightly depending on the database(s) you want to monitor but involves replacing the generic `$DATABASE_TYPE.d/conf.yaml` with one pointing at your database.

    For example, a Dockerfile pointing to a PostgreSQL database could look like this:

    ```Dockerfile  theme={null}
    FROM datadog/agent:7
    COPY postgres.yaml /conf.d/postgres.d/conf.yaml
    ```

    Where `postgres.yaml` is a file in your repository with information that points at the PostgreSQL database.

    You can find specifics on how to configure each database type in Datadog's integration documentation under the `Host` tab.

    * [PostgreSQL Configuration](https://docs.datadoghq.com/integrations/postgres/?tab=host#host)
    * [Redis Configuration](https://docs.datadoghq.com/integrations/redisdb/?tab=host#configuration)
    * [MySQL Configuration](https://docs.datadoghq.com/integrations/mysql/?tab=host#configuration)

    <Note>
      If you followed the instructions earlier and deployed with a Docker Image, you'll need to complete a few extra steps to swap back to git-based deployments. You can find those [instructions here](/how-to-guides/app-guides/deploying-docker-image-to-git)
    </Note>

    <Note>
      Depending on the type of Database you want to monitor, you may need to set additional configuration variables. Please refer to Datadog's documentation for specific instructions.
    </Note>
  </Accordion>
</AccordionGroup>

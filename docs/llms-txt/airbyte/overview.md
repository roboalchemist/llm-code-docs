# Source: https://docs.airbyte.com/platform/connector-development/connector-builder-ui/overview.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/connector-builder-ui/overview.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/connector-builder-ui/overview.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/connector-builder-ui/overview.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/connector-builder-ui/overview.md

# Connector Builder Intro

Copy Page

Connector Builder is a no-code tool that’s part of the Airbyte UI. It provides an intuitive user interface on top of the [low-code YAML format](https://docs.airbyte.com/connector-development/config-based/understanding-the-yaml-file/yaml-overview) and lets you develop a connector to use in data syncs without ever needing to leave your Airbyte workspace. Connector Builder offers the most straightforward method for building, contributing, and maintaining connectors.

## When should I use Connector Builder?[​](#when-should-i-use-connector-builder "Direct link to When should I use Connector Builder?")

First, check if the API you want to use has an available connector in the [catalog](/integrations/.md). If you find it there, you can use it as is. If the connector you're looking for doesn't already exist and you'd like to try creating your own implementation, the Connector Builder should be your first destination.

## Getting started[​](#getting-started "Direct link to Getting started")

The high-level process for using Connector Builder is as follows:

1. Access Connector Builder in the Airbyte web app by selecting "Builder" in the left-hand sidebar
2. Iterate on the connector by providing details for global configuration and user inputs, and streams
3. Once the connector is ready, publish it to your workspace, or contribute it to Airbyte catalog
4. Configure a Source based on the released connector
5. Use the Source in a connection to sync data

The concept pages in this section of the docs share more details related to the following topics: [authentication](/platform/1.6/connector-development/connector-builder-ui/authentication.md), [record processing](/platform/1.6/connector-development/connector-builder-ui/record-processing.md), [pagination](/platform/1.6/connector-development/connector-builder-ui/pagination.md), [incremental sync](/platform/1.6/connector-development/connector-builder-ui/incremental-sync.md), [partitioning](/platform/1.6/connector-development/connector-builder-ui/partitioning.md), and [error handling](/platform/1.6/connector-development/connector-builder-ui/error-handling.md).

tip

Do not hardcode things like API keys or passwords while configuring a connector in the builder. They will be used, but not saved, during development when you provide them as Testing Values. For use in production, these should be passed in as user inputs after publishing the connector to the workspace, when you configure a source using your connector.

Follow [the tutorial](/platform/1.6/connector-development/connector-builder-ui/tutorial.md) for an example of what this looks like in practice.

## Contributing the connector[​](#contributing-the-connector "Direct link to Contributing the connector")

If you'd like to share your connector with other Airbyte users, you can contribute it to Airbyte's GitHub repository right from the Builder.

1. Click "Publish" chevron -> "Contribute to Marketplace"
2. Fill out the form: add the connector description, and provide your GitHub PAT (Personal Access Token) to create a pull request
3. Click "Contribute" to submit the connector to the Airbyte catalog

Reviews typically take under a week.

You can also export the YAML manifest file for your connector and share it with others. The manifest file contains all the information about the connector, including the global configuration, streams, and user inputs.

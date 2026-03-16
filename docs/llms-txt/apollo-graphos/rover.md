# Source: https://www.apollographql.com/docs/rover.md

# Source: https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publishing/rover.md

# Source: https://www.apollographql.com/docs/graphos/connectors/tooling/rover.md

# Using Rover for Connectors Development

Rover is Apollo's command-line interface for developing graphs with Apollo GraphOS.
It serves as a primary tool for developers working with GraphQL schemas, including Connector-based development workflows.
This guide provides an overview of how to use Rover when developing with Apollo Connectors.

## Installation

The Rover CLI is available for Linux, Mac, and Windows.
To install or upgrade to the latest release of Rover:

```terminal
curl -sSL https://rover.apollo.dev/nix/latest | sh	
```

```terminal
iwr 'https://rover.apollo.dev/win/latest' | iex	
```

[See more installation methods.](https://www.apollographql.com/docs/rover/getting-started)

### Verifying installation with `rover --version`

After installation, you can verify Rover is correctly installed by running `rover --version` in your terminal, which will display the current version number.
For full use of all Connectors-related features, install v0.29.0 or later.

### Authentication with GraphOS using `rover config auth`

Before using Rover with GraphOS, you need to authenticate with GraphOS by running [`rover config auth`](https://www.apollographql.com/docs/rover/configuring#via-the-auth-command).
This interactive command guides you through obtaining and configuring your API key for GraphOS.

## Graph initialization

The [`rover init`](https://www.apollographql.com/docs/rover/commands/init) command creates a new graph in your current directory.
When prompted by the command, select the **Start with REST APIs** to set up a graph with all the necessary files for Connector development.

## Connector development

The [`rover dev`](https://www.apollographql.com/docs/rover/commands/dev) command runs a local instance of the GraphOS Router that can process your Connectors schemas.
This local environment lets you test your Connectors without deploying to production.
The `dev` command supports hot-reloading, automatically detecting changes to your Connector schema files and updating the running router.

To ensure `dev` works with schemas that include Connectors, ensure you include [`APOLLO_KEY` and `APOLLO_GRAPH_REF` environment variables](https://www.apollographql.com/docs/rover/configuring#with-an-environment-variable).

### Testing Connectors

When running `rover dev`, you can access Apollo Sandbox at `localhost:4000` to interactively test your Connector functionality.

This Sandbox lets you to test requests and see real-time responses from your REST API integrations.

You can also use the [`rover connector test`](https://www.apollographql.com/docs/graphos/connectors/testing) command to run tests using the Connectors Testing Framework.

## Schema publishing

Use [`rover subgraph publish`](https://www.apollographql.com/docs/rover/commands/subgraphs) to publish schemas to GraphOS. This makes your Connectors available in your graph for client usage.

## CI/CD integration

Rover can be integrated into continuous integration and deployment pipelines to automate Connector schema validation and publishing.
The [Rover docs](https://www.apollographql.com/docs/rover/ci-cd) provide specific integration guidance for GitHub Actions, CircleCI, Bitbucket Pipelines, and other popular CI systems.

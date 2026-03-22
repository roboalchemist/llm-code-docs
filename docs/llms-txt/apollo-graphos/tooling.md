# Source: https://www.apollographql.com/docs/graphos/connectors/tooling.md

# Connectors Development Workflow and Tooling

Apollo provides a complete toolkit for building with Apollo Connectors.
This article is an overview of those tools and the recommended workflow to get the most out of them.

## Setup

Two tools require installation, and should be installed in order:

1. The Rover CLI
2. An IDE extension

Some IDE extensions use Rover as a language server. Consult the [IDE extension article](https://www.apollographql.com/docs/graphos/connectors/tooling/ide-extensions) for setup instructions.

## Connectors development workflow

The general workflow for building Connectors is:

1. Edit your schema in your IDE
2. Test the changes in Apollo Sandbox
3. Use the **Connectors Debugger** in Sandbox to troubleshoot any issues
4. Use the [`test`](https://www.apollographql.com/docs/graphos/connectors/testing) and [`run`](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools#rover-connectors-run) commands in the Rover CLI to run unit tests and preview your Connector behavior.

Optionally, the Connectors Mapping Playground can help you get started or refine complex Connectors.

### Step 1. Editing in your IDE

The best way to author Connectors is using one of Apollo's official [IDE extensions](https://www.apollographql.com/docs/graphos/connectors/tooling/ide-extensions).
They provide real-time basic validations As you work and enhanced validations on-save.
These validations can catch many issues early on.

Save the file you're working on to get all validations.
Any errors that you see in the IDE will also prevent GraphOS Router from updating.

### Step 2. Testing with Sandbox

After edits, you should test changes locally to make sure everything is working as expected.
You can do this by [running `rover dev`](https://www.apollographql.com/docs/graphos/connectors/tooling/rover#connector-development) in your terminal.
This command starts a local instance of the GraphOS Router with recommended development settings, including Apollo Sandbox (at `http://localhost:4000`, by default).
In the Sandbox, you can send GraphQL operations to the router and check for the expected responses.

### Step 3. Troubleshooting

If anything is amiss, you can open the **Connectors Debugger** section to inspect the HTTP requests, responses, and
any errors encountered while processing them.

Refer to the [troubleshooting guide](https://www.apollographql.com/docs/graphos/connectors/troubleshooting) for additional debugging methods and common errors.

## The Connectors Mapping Playground

The [Connectors Mapping Playground](https://www.apollographql.com/connectors-mapping-playground/?referrer=docs-content) is a standalone website that allows you to experiment with Connectors and see results without actually running requests.
Using the playground can be quicker than cycling between your editor and Apollo Sandbox for complex Connectors. [Learn more about the playground.](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground)

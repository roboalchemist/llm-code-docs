# Source: https://docs.base44.com/developers/references/cli/commands/introduction.md

# Source: https://docs.base44.com/developers/app-code/overview/introduction.md

# Source: https://docs.base44.com/developers/backend/overview/introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Backend-as-a-service built with AI agents in mind

<Note>
  The Base44 backend service and the CLI are currently in beta. We're actively
  improving the platform and documentation based on user feedback. Share your
  thoughts and feature requests on our [GitHub Discussions page](https://github.com/orgs/base44/discussions).
</Note>

The Base44 backend service provides [everything you need](/developers/backend/overview/features) to build and deploy your applications. Get started with the following commands:

```bash  theme={null}
npm install -g base44@latest   # Install the CLI
base44 login                   # Authenticate
base44 create                  # Create a project
```

#### Build with AI

Projects created with the CLI are automatically configured with [Base44 skills](/developers/backend/overview/base44-skills). Just open your project in your preferred AI assistant and start building. You can also connect the [Base44 Docs MCP server](/developers/backend/overview/base44-docs-mcp) to give your AI tool direct access to this documentation.

#### Code it yourself

<CardGroup cols={2}>
  <Card title="Backend only quickstart" icon="server" href="/developers/backend/quickstart/templates/quickstart-backend-only">
    Create a backend-only project
  </Card>

  <Card title="React quickstart" icon="react" href="/developers/backend/quickstart/templates/quickstart-react-template">
    Create a full-stack project with React
  </Card>

  <Card title="Start from an existing Base44 app" icon="arrow-right-from-bracket" href="/developers/backend/overview/start-from-existing-app">
    Create a new project from an existing Base44 app
  </Card>

  <Card title="Example apps" icon="github" href="https://github.com/base44/apps-examples" arrow={false}>
    Learn from working examples and use them as starting points
  </Card>
</CardGroup>

#### Get oriented

To understand how this compares to Base44's app editor and whether it's right for you, see [Backend service basics](/developers/backend/overview/backend-service-basics).

## Learn more

* Explore the [features](/developers/backend/overview/features) included in the backend service.
* Learn about [project structure](/developers/backend/overview/project-structure) and configuration files.
* Read the [CLI command reference](/developers/references/cli/commands/introduction) for all available commands.
* Explore the [JavaScript SDK](/developers/references/sdk/getting-started/overview) documentation.


Built with [Mintlify](https://mintlify.com).
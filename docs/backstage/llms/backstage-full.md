# Backstage Documentation

Source: https://roadie.io/llms-full.txt

---

# Roadie - Internal Developer Portal built on Backstage

> Roadie is the most customizable Internal Developer Portal. With scorecards, self-service workflows, AI and actionable insights.

This file contains the full content of key pages for LLM consumption.
For a lighter index of all pages, see [/llms.txt](/llms.txt).

## Documentation

### [Authorization of the API](https://roadie.io/docs/api/authorization.md)

## Prerequisites

You need to have the "Roadie API Key Access" policy assigned to your user in Roadie to create an API token.

## Get an API token

- Go to Administration > Account
- Add a token description
- Click "Generate Token".

## To test the token

```shell
curl \
  -X GET \
  -H 'Accept: application/json' \
  -H "Authorization: bearer ${ROADIE_API_TOKEN}" \
  https://api.roadie.so/api/catalog/entities
```

For write operations using PUT, POST, or PATCH requests with a request body, we expect a JSON structure. You should modify your calls to include the `Content-Type` header.

```shell
curl \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: bearer ${ROADIE_API_TOKEN}" \
  -d '{ "key": "value" }'
  https://api.roadie.so/api/catalog/fragments
```

---

### [Entity Push API Tutorial](https://roadie.io/docs/api/entity-push-api.md)

## Introduction

In this tutorial we are going to show you how to ingest your organization's AWS accounts into your Roadie catalog as Resource entities. For this we will use Roadie's Entity Push API. You can check out the API docs [here](/docs/api/catalog/) in the Roadie Provider section.

This tutorial will hopefully serve as an example around how you might apply this same pattern to other cloud providers or other resources that you cannot currently manage with the providers available with Roadie out of the box.

## Authentication

First to be able to use the Roadie entity push API we will need to get an authentication token. You can generate your own token by going to the `Administration` -> `Account` (`/administration/account`) page. Here go to the `Roadie API Access` section. Give a name to your token and press the `GENERATE TOKEN` button.
Make sure you copy your token and put it in a secure place.
You can test out your token by hitting the api. For example:

```bash
curl \
  -X GET \
  -H 'Accept: application/json' \
  -H "Authorization: bearer ${ROADIE_API_TOKEN}" \
  https://api.roadie.so/api/catalog/entities
```

## Fetch your AWS accounts

Using the AWS CLI make sure you have it setup and configured. You can read more [here](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-welcome.html)

```bash
aws organizations list-accounts
```

<details>
<summary>Errors</summary>

If you encounter the following error make sure you have the proper permissions configured for yourself and check if you are using your correct AWS_PROFILE

`An error occurred (AccessDeniedException) when calling the ListAccounts operation: You don't have permissions to access this resource.`

</details>

This will result in a response like

```json
{
  "Accounts": [
    {
      "Arn": "arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111",
      "JoinedMethod": "INVITED",
      "JoinedTimestamp": 1481830215.45,
      "Id": "111111111111",
      "Name": "Master Account",
      "Email": "bill@example.com",
      "Status": "ACTIVE"
    },
    {
      "Arn": "arn:aws:organizations::111111111111:account/o-exampleorgid/222222222222",
      "JoinedMethod": "INVITED",
      "JoinedTimestamp": 1481835741.044,
      "Id": "222222222222",
      "Name": "Production Account",
      "Email": "alice@example.com",
      "Status": "ACTIVE"
    },
    {
      "Arn": "arn:aws:organizations::111111111111:account/o-exampleorgid/333333333333",
      "JoinedMethod": "INVITED",
      "JoinedTimestamp": 1481835795.536,
      "Id": "333333333333",
      "Name": "Development Account",
      "Email": "juan@example.com",
      "Status": "ACTIVE"
    },
    {
      "Arn": "arn:aws:organizations::111111111111:account/o-exampleorgid/444444444444",
      "JoinedMethod": "INVITED",
      "JoinedTimestamp": 1481835812.143,
      "Id": "444444444444",
      "Name": "Test Account",
      "Email": "anika@example.com",
      "Status": "ACTIVE"
    }
  ]
}
```

Now you can use either this list directly and send the data into the Roadie Catalog via your preferred way, using plain curl command or any programming language you prefer. In the next section I'll show you a full example with node.js.

### Listing the accounts and sending the entities to Roadie

- We will use the official AWS JavaScript SDK. Make sure you have it available in your system
- Make sure you have your `ROADIE_API_TOKEN` available in your shell
- Make sure you are authenticated towards your AWS.
- Make sure you are using your correct `AWS_PROFILE`

We are going to fetch the available AWS accounts and then pick the data we want to put in the Resource entities and finally send these into Roadie. We are going to use the `PUT /api/catalog/roadie-entities/sets/${setId}` endpoint. To use this we have to provide a set id, which should be something descriptive. This provides the ability to issue subsequent requests towards the same set id and it will update all of the entities provided in the request body. This performs a full mutation, every entity in the set will be replaced by the new incoming entities in the new requests.

If you would like to remove some of the entities provided in this set you will need to issue a new request without the entity you want to delete, so the whole set will be replaced by the new array of entities you send to Roadie.

```bash
npm i @aws-sdk/client-organizations
```

In this example I'll use the native `node:https` package, this can be substituted by your preferred way of making an http request. (axios, node-fetch, etc..)

```js
const https = require('node:https');
const { OrganizationsClient, ListAccountsCommand } = require('@aws-sdk/client-organizations');

const client = new OrganizationsClient();

const command = new ListAccountsCommand({});
const response = client.send(command);

response.then((r) => {
  const accounts = r.Accounts;

  if (!accounts) {
    throw new Error('No AWS Accounts found');
  }

  const templateResourceEntity = ({ name, arn }) => ({
    apiVersion: 'backstage.io/v1alpha1',
    kind: 'Resource',
    metadata: {
      name,
      description: 'AWS accounts',
      annotations: {
        'aws-account/arn': arn,
      },
    },
    spec: {
      owner: 'dx-team',
      type: 'aws-account',
    },
  });

  const entities = accounts.map((a) => templateResourceEntity({ name: a.Name, arn: a.Arn }));

  const body = JSON.stringify({ items: entities });
  const req = https.request(
    {
      hostname: 'api.roadie.so',
      port: 443,
      path: '/api/catalog/roadie-entities/sets/aws-accounts',
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(body),
        Authorization: `bearer ${process.env.ROADIE_API_TOKEN}`,
      },
    },
    (res) => {
      res.on('data', (chunk) => {
        console.log(chunk);
      });
    }
  );
  req.on('error', (e) => {
    console.log(e);
  });
  req.write(body);

  req.end();
});
```

You will see the following response body on a successful request:

```json
{
  "set": "aws-accounts",
  "items": [
    {
      "id": "cf71aba4-c2c5-4ba8-b274-c94c097d74be",
      "entity": {
        "kind": "Resource",
        "spec": { "type": "aws-account", "owner": "dx-team" },
        "metadata": {
          "name": "development",
          "annotations": {
            "update-me": "me",
            "aws-account/arn": "arn",
            "roadie.io/entity-set": "aws-accounts",
            "backstage.io/managed-by-location": "roadie-api:/api/catalog/roadie-entities/entities/by-ref/resource%3Adefault%2Fdevelopment",
            "backstage.io/managed-by-origin-location": "roadie-api:/api/catalog/roadie-entities/entities"
          },
          "description": "AWS accounts"
        },
        "apiVersion": "backstage.io/v1alpha1"
      },
      "entityRef": "resource:default/development",
      "rawData": {
        "kind": "Resource",
        "spec": { "type": "aws-account", "owner": "dx-team" },
        "metadata": {
          "name": "development",
          "annotations": {
            "update-me": "me",
            "aws-account/arn": "arn",
            "roadie.io/entity-set": "aws-accounts",
            "backstage.io/managed-by-location": "roadie-api:/api/catalog/roadie-entities/entities/by-ref/resource%3Adefault%2Fdevelopment",
            "backstage.io/managed-by-origin-location": "roadie-api:/api/catalog/roadie-entities/entities"
          },
          "description": "AWS accounts"
        },
        "apiVersion": "backstage.io/v1alpha1"
      },
      "set": "aws-accounts",
      "updatedBy": "user:default/guest",
      "source": "api-entity",
      "updatedAt": "2024-02-16T11:26:16.685+00:00"
    }
  ]
}
```

Go to your catalog page (`Catalog` -> `Resource`) and you will immedietly see these `Resource` entities in your catalog.

## Keep it syncing

To continuously update your catalog with the changes in your AWS accounts you will need to run this script on a schedule. I advise you to use your organization's best practice to run these scheduled jobs. Alternatively you can use the pull based `roadie-agent` library if you want Roadie to automatically schedule pulling these entities from your developed Roadie Agent service.

Regardless how it will run you will need to be sure that environment has the correct tokens to be able to fetch from your organization's AWS and to be able to push to your Roadie API. Do not forget to configure your `ROADIE_API_TOKEN` and your `AWS_PROFILE`.

---

### [Roadie API & MCP Servers](https://roadie.io/docs/api/overview.md)

## Overview

Roadie provides both a REST API and Model Context Protocol (MCP) servers to read and write information from a Roadie instance. These enable you to integrate Roadie with your existing tools, automate workflows, and build custom integrations.

## Roadie API

The Roadie API provides programmatic access to your Backstage catalog and other Roadie features. You can use it to automate catalog management, integrate with CI/CD pipelines, or build custom tooling.

Some uses of the API include:

- **Catalog management** - Create, update, and delete entities in your catalog from external systems
- **Entity sets** - Manage batches of entities idempotently, perfect for syncing resources from internal systems
- **Tech Insights** - Access fact data and scorecard results programmatically

To get started with the API, you'll need to [generate an API token](/docs/api/authorization/).

### API Base URL

```
https://api.roadie.so/api/
```

### Example: List catalog entities

```bash
curl \
  -X GET \
  -H 'Accept: application/json' \
  -H "Authorization: bearer ${ROADIE_API_TOKEN}" \
  https://api.roadie.so/api/catalog/entities
```

For more details, see the [API Authorization](/docs/api/authorization/) documentation and the specific API documentation for [Catalog](/docs/api/catalog), [Tech Insights](/docs/api/techinsights), [Templates](/docs/api/templates), and [Plugins](/docs/api/plugins).

## MCP Server(s)

You can also connect to your Roadie instance via an LLM client of your choice (provided it supports third party MCP servers). [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) enables AI assistants to interact with your Backstage catalog using structured data.

Some uses of the MCP servers include:

- **AI-powered catalog exploration** - Ask natural language questions about your software catalog and/or allow Agents to access rich metadata about your software.
- **Automated scaffolding** - find, validate, and execute scaffolder templates
- **Security and compliance insights** - Query vulnerability data, branch protection status, and compliance metrics
- **Documentation search** - Search and retrieve TechDocs content across your catalog
- **Catalog decoration** - Manage entity fragments and decorators via AI assistants

### Available MCP Servers

| Server                                                           | Description                                                           | Endpoint                                               |
| ---------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------ |
| [API Docs Query](/docs/api/roadie-mcp/api-docs-query/)           | Discover and retrieve API documentation and specifications            | `https://api.roadie.so/api/mcp/v1/api-docs-query`      |
| [Backend Config](/docs/api/roadie-mcp/backend-config/)           | Manage proxy settings and secrets                                     | `https://api.roadie.so/api/mcp/v1/backend-config`      |
| [Catalog Decorators](/docs/api/roadie-mcp/catalog-decorators/)   | Manage catalog entity decorators and fragments                        | `https://api.roadie.so/api/mcp/v1/catalog-decorators`  |
| [Rich Catalog Entity](/docs/api/roadie-mcp/rich-catalog-entity/) | Access catalog entity data, relationships, and documentation          | `https://api.roadie.so/api/mcp/v1/rich-catalog-entity` |
| [Scaffolder](/docs/api/roadie-mcp/scaffolder/)                   | Find, validate, and execute scaffolder templates                      | `https://api.roadie.so/api/mcp/v1/scaffolder-use`      |
| [Tech Insights Facts](/docs/api/roadie-mcp/tech-insights-facts/) | Access operational metrics, security data, and compliance information | `https://api.roadie.so/api/mcp/v1/tech-insights-facts` |

### Supported AI Tools

MCP servers work with popular AI development tools including:

- **VS Code with Copilot**
- **Cursor IDE**
- **Claude Desktop**

For detailed setup instructions, see the [Roadie MCP Getting Started](/docs/api/roadie-mcp/) documentation.

## Authentication

Both the REST API and MCP servers use the same authentication mechanism. You'll need to generate an API token from your Roadie instance:

1. Go to **Administration → Account**
2. Navigate to the **Roadie API Access** section
3. Add a token description and click **Generate Token**
4. Store the token securely

See [API Authorization](/docs/api/authorization/) for more details.

---

### [Roadie MCP AI Servers (Beta)](https://roadie.io/docs/api/roadie-mcp.md)

## Introduction

Roadie exposes a number of [Model Context Protocol Servers (MCP)](https://modelcontextprotocol.io/introduction) via our authenticated API that can provide AI tools like agents and LLMs with structured data to answer complex questions about your catalog and powerful workflow capabilities using the scaffolder.

## Available MCP Servers

Roadie currently provides six MCP servers that enable AI assistants to interact with your Backstage catalog:

- **[API Docs Query Server](api-docs-query)** - Discover and retrieve API documentation and specifications
  - https://api.roadie.so/api/mcp/v1/api-docs-query
- **[Backend Config Server](backend-config)** - Manage and query backend configuration including proxy settings and secrets
  - https://api.roadie.so/api/mcp/v1/backend-config
- **[Catalog Decorators Server](catalog-decorators)** - Manage catalog entity decorators and fragments
  - https://api.roadie.so/api/mcp/v1/catalog-decorators
- **[Rich Catalog Entity Server](rich-catalog-entity)** - Access catalog entity data, relationships, and documentation
  - https://api.roadie.so/api/mcp/v1/rich-catalog-entity
- **[Scaffolder Server](scaffolder)** - Find, validate, and execute Backstage scaffolder templates
  - https://api.roadie.so/api/mcp/v1/scaffolder-use
- **[Tech Insights Facts Server](tech-insights-facts)** - Access operational metrics, security data, and compliance information
  - https://api.roadie.so/api/mcp/v1/tech-insights-facts

## Prerequisites

- Roadie tenant with populated catalog
- Active Roadie API token
- AI assistant or MCP client configured to use Roadie's MCP servers

## Tool Integration Setup

### Setting up MCP Servers in Popular AI Tools

<details>
<summary><strong>VS Code with Copilot</strong></summary>

VS Code supports [MCP servers](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).

Here's how to configure Roadie's for use with Copilot:

#### Configure MCP Servers

Add the following configuration to your settings (`~/.vscode/mcp.json`):

```json
{
  "servers": {
    "roadie-api-docs": {
      "url": "https://api.roadie.so/api/mcp/v1/api-docs-query",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-backend-config": {
      "url": "https://api.roadie.so/api/mcp/v1/backend-config",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-catalog-decorators": {
      "url": "https://api.roadie.so/api/mcp/v1/catalog-decorators",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-scaffolder": {
      "url": "https://api.roadie.so/api/mcp/v1/scaffolder-use",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-catalog": {
      "url": "https://api.roadie.so/api/mcp/v1/rich-catalog-entity",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-insights": {
      "url": "https://api.roadie.so/api/mcp/v1/tech-insights-facts",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    }
  }
}
```

#### Get Your API Token

1. Log into your Roadie instance
2. Go to Settings → API Keys
3. Create a new API key with appropriate permissions
4. Replace `<roadie_api_token>` with your actual token

#### Check your Settings

- In settings, ensure `chat.mcp.enabled` is set to `enabled`.
- Occassionally your organisation will manage these settings (you will see something like "managed by organization" next to a given setting). If this is the case and `chat.mcp.enabled` is not set to enabled you will need to talk to whomever manages those settings.

#### Test the Integration

Open VS Code and try asking Copilot questions like:

- "What APIs are available for user management?"
- "Who owns the payment-service component?"
- "Create a fragment to add team ownership to the auth-service"

#### Skipping steps

- VSCode omits some information-only steps and/or auto-completes various actions our MCP tools request. That is due to a permissive interpretation of the protocols `readOnlyHint: true` flag, which is best practice to use on MCP servers [based on the protocol specification](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations). The flag represents non-destructive tools which only return information and do not alter the MCP clients environment. VSCode interprets `readOnlyHints` as default permissable to execute, whereas most other MCP clients require user consent or a flag to be set in config before they autocomplete.
- More information can be found here [https://code.visualstudio.com/updates/v1_100#\_mcp-tool-annotations](https://code.visualstudio.com/updates/v1_100#_mcp-tool-annotations)

</details>

<details>
<summary><strong>Cursor IDE</strong></summary>

Cursor supports MCP servers through its AI integration. Here's the setup:

#### Configure MCP Servers

Create or edit your Cursor MCP configuration file (`.cursor/mcp.json` in your project or home directory):

```json
{
  "mcpServers": {
    "roadie-api-docs": {
      "url": "https://api.roadie.so/api/mcp/v1/api-docs-query",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-backend-config": {
      "url": "https://api.roadie.so/api/mcp/v1/backend-config",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-catalog-decorators": {
      "url": "https://api.roadie.so/api/mcp/v1/catalog-decorators",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-scaffolder": {
      "url": "https://api.roadie.so/api/mcp/v1/scaffolder-use",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-catalog": {
      "url": "https://api.roadie.so/api/mcp/v1/rich-catalog-entity",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-insights": {
      "url": "https://api.roadie.so/api/mcp/v1/tech-insights-facts",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    }
  }
}
```

#### Restart Cursor

After configuring the MCP servers, restart Cursor to load the new configuration.

#### Test Integration

Use Cursor's AI chat to test the integration:

- "Show me security metrics for user-service"
- "What scaffolder templates are available?"
- "Find APIs related to payment processing"
- "List all fragments for the payment-service component"

</details>

<details>
<summary><strong>Claude Desktop (Anthropic)</strong></summary>

Claude Desktop supports MCP servers natively:

#### Configure MCP Servers

Edit your Claude Desktop configuration file (`~/.config/claude-desktop/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "roadie-api-docs": {
      "url": "https://api.roadie.so/api/mcp/v1/api-docs-query",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-backend-config": {
      "url": "https://api.roadie.so/api/mcp/v1/backend-config",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-catalog-decorators": {
      "url": "https://api.roadie.so/api/mcp/v1/catalog-decorators",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-scaffolder": {
      "url": "https://api.roadie.so/api/mcp/v1/scaffolder-use",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-catalog": {
      "url": "https://api.roadie.so/api/mcp/v1/rich-catalog-entity",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    },
    "roadie-insights": {
      "url": "https://api.roadie.so/api/mcp/v1/tech-insights-facts",
      "headers": {
        "Authorization": "Bearer <roadie_api_token>"
      }
    }
  }
}
```

#### Restart Claude Desktop

Restart the application to load the new MCP server configuration.

#### Test Functionality

Test with queries like:

- "What documentation exists for auth-service?"
- "Show me GitHub metrics for all payment services"
- "Add monitoring annotations to the user-service component"

</details>

### Authentication Setup

You will need an API token for your user to connect with these MCP servers. See [API Token docs here](/docs/api/authorization/). You may need an admin user to provide you with a Roadie API Token.

### Troubleshooting Setup

**Common Issues:**

1. **Authentication Errors**:

   - Verify your API token is correct and not expired
   - Check that the token has appropriate permissions

2. **Connection Failures**:

   - Verify network connectivity to your Roadie instance
   - Check that the MCP API endpoints are accessible

3. **Permission Denied**:

   - Review your API token permissions
   - Contact your Roadie administrator for access

4. **MCP Server Configuration Issues**:

   - Verify the URL format is correct: `https://api.roadie.so/api/mcp/v1/<server-name>`
   - Check that all required headers are included in the configuration
   - Ensure environment variables are properly set

5. **Global IDE Settings can Block MCP Server Access**:
   - Verify that access to remote authenticated MCP servers is enabled. For example, in VSCode the setting `chat.mcp.enabled` should be set to `enabled`.
   - Occassionally your organisation will manage these settings and if they are not enabled you will need to talk to your support team or whomever manages those settings. For example, in VSCode you will see something like "managed by organization".

## Best Practices

### API Discovery

- Start with broad search terms and refine based on results

### Template Execution

- Always validate inputs before execution to catch errors early
- Provide clear, descriptive names for generated projects

### Error Handling

- Check validation results before proceeding with template execution
- Monitor task status for long-running templates
- Review error messages for troubleshooting guidance
- Ensure proper permissions are in place before execution

## Support and Troubleshooting

### Common Issues

**Authentication Errors**

- Verify your Roadie API credentials are configured correctly
- Ensure your MCP client is properly authenticated

**Permission Denied**

- Check that you have the necessary permissions for catalog access and scaffolder execution
- Contact your Roadie administrator if you need additional permissions

**Template Execution Failures**

- Use `validate-template-values` to check inputs before execution
- Review template requirements and ensure all parameters are provided
- Check `get-scaffolder-task` for detailed error information

For additional support, please refer to the Roadie documentation or contact our support team.

---

### [API Docs Query Server](https://roadie.io/docs/api/roadie-mcp/api-docs-query.md)

## Introduction

The API Docs Query Server provides AI assistants with comprehensive access to your organization's API documentation and specifications stored in your Backstage catalog.

**Server Endpoint:** `https://api.roadie.so/api/mcp/v1/api-docs-query`

## Capabilities

- **API Discovery**: Search for APIs using natural language queries
- **Specification Retrieval**: Get complete OpenAPI, GraphQL, or AsyncAPI specifications
- **Intelligent Search**: Find APIs by domain, technology, or business context
- **Metadata Access**: Retrieve API descriptions, ownership, and categorization

## Available Tools

### Find API Specs

Search for available API specifications using a query string that supports partial matching across API names, descriptions, and metadata.

**Parameters:**

- `queryString` (string): Search term for finding API specs

**Example Usage:**

```json
{
  "queryString": "payment"
}
```

**Return Schema:**

```typescript
{
  results: {
    type: string,
    document: {
      kind: string,
      text: string,
      type: string,
      owner: string,
      title: string,
      keywords: string,
      location: string,
      lifecycle: string,
      namespace: string,
      componentType: string
    }
  }[]
}
```

This will return all APIs related to payments, including services like "payment-gateway", "payment-processor", or "billing-api".

### Retrieve API Spec

Get the complete specification for a specific API, including full OpenAPI/Swagger definitions, schemas, and endpoint documentation.

**Parameters:**

- `name` (string): API name
- `namespace` (string, optional): API namespace (defaults to "default")

**Example Usage:**

```json
{
  "name": "user-service-api",
  "namespace": "backend"
}
```

**Return Schema:**

```typescript
{
  entityRef: string,
  spec: string
}
```

#### Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities and API specifications

## Common Use Cases

### API Integration Planning

- Ask your AI assistant: "What payment APIs are available?"
- Get detailed endpoint information for integration planning
- Compare different APIs to choose the best fit

### Documentation Exploration

- "Show me the schema for creating a user account"
- "What authentication does the order API require?"
- "List all the endpoints in the inventory service"

### Development Assistance

- Generate client code from API specifications
- Create automated tests based on API schemas
- Validate API requests and responses

## Examples

### Example AI Conversation

**User:** "I need to integrate with our user management system"

**AI Response using MCP:**

1. Searches for user-related APIs using `find-api-specs`
2. Retrieves specifications for relevant APIs
3. Explains available endpoints, authentication, and schemas
4. Provides integration guidance and code examples

### Practical Usage

```json
// Finding payment-related APIs
{
  "tool": "find-api-specs",
  "arguments": {
    "queryString": "payment processing"
  }
}

// Getting complete specification
{
  "tool": "retrieve-api-spec",
  "arguments": {
    "name": "payment-gateway-api",
    "namespace": "payments"
  }
}
```

## Best Practices

- Start with broad search terms and refine based on results
- Use domain-specific language (e.g., "payment", "authentication", "notification")
- Check multiple namespaces if APIs aren't found in default
- Review complete specifications before starting integration

---

### [Backend Config Server](https://roadie.io/docs/api/roadie-mcp/backend-config.md)

## Introduction

The Backend Config Server provides specialized MCP tools for managing and querying backend configuration in Roadie. It focuses on administrative tasks like proxy configuration.

**Server Endpoint:** `https://api.roadie.so/api/mcp/v1/backend-config`

## Capabilities

- **Proxy Configuration Management**: List, create, and update proxy configurations for external service access
- **Secrets Management**: List available secrets that can be used in proxy configurations

## Available Tools

### Get Proxy Config List

Retrieve the current proxy configuration from the app-config plugin, including both custom proxy entries and default proxy entries.

**Parameters:**

- `random_string` (string): Dummy parameter for no-parameter tools

**Example Usage:**

```json
{
  "random_string": "dummy"
}
```

**Returns:** List of configured proxy routes including:

- Both custom proxy entries and default proxy entries
- Proxy paths, targets, and advanced settings like headers and methods

#### Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities
- **Backend config read** - Access to backend configuration

### Create Proxy Config

Create or update proxy entries in Roadie for secure access to external services from the Roadie backend using secrets stored in Roadie for authentication if necessary.

**Parameters:**

- `proxies` (array): Array of proxy configurations with path, target, and optional advanced settings

**Example Usage:**

```json
{
  "proxies": [
    {
      "path": "/github",
      "target": "https://api.github.com",
      "advancedSettings": {
        "headers": {
          "Authorization": "Bearer ${GITHUB_TOKEN}"
        },
        "allowedMethods": ["GET", "POST"]
      }
    }
  ]
}
```

**Proxy Configuration Schema:**

```typescript
{
  proxies: {
    path: string, // Path at which the proxy is mounted (must start with /)
    target: string, // Target URL for the proxy
    advancedSettings?: {
      allowedHeaders?: string[],
      allowedMethods?: string[],
      changeOrigin?: boolean,
      headers?: Record<string, string>,
      noHeaders?: boolean,
      noMethods?: boolean,
      pathRewrite?: Record<string, string>,
      target?: string
    }
  }[]
}
```

#### Required Permissions

- **Backend config write** - Permission to create and update backend configuration

### Get Secrets List

Retrieve the list of available secrets that can be used in proxy configurations and other backend integrations.

**Parameters:**

- `random_string` (string): Dummy parameter for no-parameter tools

**Example Usage:**

```json
{
  "random_string": "dummy"
}
```

**Returns:** List of available secrets including:

- Secret names that can be referenced in proxy configurations
- Masked secret values (showing only last 4 characters for security)
- Secret descriptions and usage information
- Current status (Available, Updating, or Not Set)
- Optional help URLs with additional information

**Return Schema:**

```typescript
{
  secrets: {
    name: string, // Secret name (e.g., "GITHUB_TOKEN")
    value: string, // Hidden value showing only last 4 characters
    description?: string, // Description of what the secret is for
    status: 'Available' | 'Updating' | 'Not Set', // Current status of the secret
    helpUrl?: string // Optional URL with help information for this secret
  }[]
}
```

#### Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities
- **Backend config read** - Access to backend configuration and secrets

## Common Use Cases

### Proxy Management

- "What backend proxies are configured in Roadie?"
- "Show me the proxy configuration for my custom plugin"
- "List all backend proxy endpoints in Roadie"

### Proxy Creation and Updates

- "Create a proxy for the GitHub API at /github with target https://api.github.com"
- "Add a proxy entry for my service at /my-service pointing to https://my-api.com"
- "Set up a proxy with custom headers for authentication"
- "Create multiple proxy entries for different external services"
- "Update the Snyk proxy to only allow GET methods"

### Service Integration

- "Add a proxy entry for Wiz security API"
- "Configure a proxy for our internal monitoring service"
- "Set up authenticated access to external documentation APIs"

### Secrets Management

- "What secrets are available for use in proxy configurations?"
- "List all available secrets in Roadie and their current status"
- "Show me which secrets are configured and which need to be set"
- "What authentication tokens can I use for my proxy setup?"
- "Which secrets are currently updating or not set?"
- "Show me help information for configuring specific secrets"

## Security Considerations

### Authentication and Secrets

- Proxy routes allow secure access to external services using secrets stored in Roadie
- Authentication headers can reference stored secrets using `${SECRET_NAME}` syntax
- Secrets are managed separately and securely in Roadie's secret management system

### Access Control

- **Method Restrictions**: Configure allowed HTTP methods for security
- **Header Control**: Specify allowed headers and custom authentication headers
- **Path Management**: Control routing and path rewriting for security

### Best Practices for Secrets

- Use `get-secrets-list` to discover available secrets and check their status before configuring proxies
- Verify secrets show "Available" status rather than "Not Set" or "Updating"
- Review masked values to confirm secrets contain expected data patterns
- Always reference secrets using the `${SECRET_NAME}` syntax rather than hardcoding values
- Utilize help URLs from the secrets list for service-specific configuration guidance
- Test secret authentication manually before deploying proxy configurations
- Regularly audit which secrets are being used in proxy configurations

## Example Workflows

### Setting Up External API Access

**User:** "I need to integrate with the Travis API from my custom plugin"

**AI Response using MCP:**

1. Uses `create-proxy-config` to set up a Travis API proxy
2. Configures authentication using stored Travis token
3. Sets appropriate method restrictions for security
4. Provides the proxy endpoint for plugin use

### Reviewing Current Configuration

**User:** "What external services do we currently have proxies for?"

**AI Response using MCP:**

1. Uses `get-proxy-config-list` to fetch all configured proxies
2. Analyzes proxy targets and paths
3. Identifies external services and their access patterns
4. Provides summary of current integrations

### Secrets Discovery and Configuration

**User:** "I want to set up a proxy for GitHub API but I'm not sure what authentication tokens are available"

**AI Response using MCP:**

1. Uses `get-secrets-list` to fetch all available secrets
2. Identifies GitHub-related secrets (e.g., `GITHUB_TOKEN`)
3. Checks secret status - whether they're Available, Updating, or Not Set
4. Shows masked values to confirm secrets are configured
5. Provides help URLs if available for additional setup guidance
6. Uses `create-proxy-config` to configure the proxy with the appropriate secret reference

## Advanced Configuration

### Headers and Authentication

```json
{
  "path": "/external-api",
  "target": "https://api.external-service.com",
  "advancedSettings": {
    "headers": {
      "Authorization": "Bearer ${EXTERNAL_API_TOKEN}",
      "Content-Type": "application/json"
    },
    "allowedMethods": ["GET", "POST"],
    "changeOrigin": true
  }
}
```

### Path Rewriting

```json
{
  "path": "/legacy-api",
  "target": "https://new-api.service.com",
  "advancedSettings": {
    "pathRewrite": {
      "^/legacy-api": "/v2/api"
    }
  }
}
```

## Troubleshooting

### Common Issues

1. **Authentication Failures**:

   - Verify secret names match exactly (case-sensitive)
   - Ensure secrets are properly configured in Roadie
   - Ensure secrets like tokens work by testing them
   - Check header formatting and syntax

2. **Connection Issues**:

   - Verify target URLs are accessible from Roadie's infrastructure
   - Check for network restrictions or firewall rules

3. **Method Restrictions**:

   - Review `allowedMethods` configuration
   - Ensure required HTTP methods are included
   - Check if `noMethods` is incorrectly set to true

4. **Path Issues**:

   - Verify proxy paths start with `/`
   - Check for path conflicts with existing routes
   - Review `pathRewrite` rules for correctness

5. **Secrets Issues**:
   - Use `get-secrets-list` to verify secret names, status, and availability
   - Check that secrets show "Available" status rather than "Not Set" or "Updating"
   - Review masked values to confirm secrets contain data
   - Ensure secrets are properly set in Roadie (see [Setting Secrets](/docs/details/setting-secrets/))
   - Check that secret references use the correct `${SECRET_NAME}` syntax
   - Use help URLs from the secrets list for service-specific setup guidance
   - Verify that secrets have the required permissions for the target service

---

### [Catalog Decorators Server](https://roadie.io/docs/api/roadie-mcp/catalog-decorators.md)

## Introduction

The Catalog Decorators Server provides MCP tools for managing catalog entity decorators/fragments in Roadie. It enables AI assistants to retrieve, create and update fragments that enhance catalog entities with additional metadata.

Fragments are partial entity data that are "decorated" onto an existing entity in the catalog to enrich its metadata.

**Server Endpoint:** `https://api.roadie.so/api/mcp/v1/catalog-decorators`

## Capabilities

- **Fragment Discovery**: List all entity fragments or fragments for a specific entity
- **Fragment Creation**: Create new fragments to decorate entities with additional metadata
- **Fragment Updates**: Add and change data in existing fragments for an entity
- **Entity Enhancement**: Add specifications, metadata, and other information to catalog entities

## Available Tools

### List Fragments

Retrieve a list of all entity fragments with optional filtering capabilities.

**Parameters:**

- `entityRef` (string, optional): Filter fragments for a specific entity
- `limit` (number, optional): Maximum number of results to return (default: 100)
- `offset` (number, optional): Pagination offset for results (default: 0)

**Example Usage:**

```json
{
  "entityRef": "component:default/user-service",
  "limit": 20,
  "offset": 0
}
```

**Alternative Usage (List All):**

```json
{
  "limit": 100
}
```

**Returns:** List of fragments including:

- Fragment identifiers and metadata
- Associated entity references
- Fragment content and specifications
- Creation and modification timestamps

**Return Schema:**

```typescript
{
  fragments: {
    id: string, // Fragment identifier
    entityRef: string, // Associated entity reference
    fragment: {
      metadata?: Record<string, any>, // Additional metadata
      spec?: Record<string, any>, // Specification data
      // Other fragment properties
    },
    createdAt: string, // Creation timestamp
    updatedAt?: string // Last modification timestamp
  }[],
  total: number, // Total number of fragments available
  hasMore: boolean // Whether more results are available
}
```

#### Required Permissions

- **Fragment entity read** - `roadie.entity-fragment.read` - Permission to view entity fragments

### Create Fragment

Create a new fragment to decorate a catalog entity with additional metadata and specifications.

**Parameters:**

- `entityRef` (string): Target entity reference to decorate
- `fragment` (object): Fragment data containing metadata and spec information

**Example Usage:**

```json
{
  "entityRef": "component:default/payment-service",
  "fragment": {
    "metadata": {
      "annotations": {
        "example.com/responsible-team": "payments-team",
        "example.com/deployment-strategy": "blue-green"
      },
      "labels": {
        "tier": "critical",
        "environment": "production"
      }
    },
    "spec": {
      "type": "something-new",
      "additionalConfig": {
        "monitoring": "enabled",
        "backup": "daily"
      }
    }
  }
}
```

**Fragment Schema:**

```typescript
{
  entityRef: string, // Target entity reference
  fragment: {
    metadata?: {
      annotations?: Record<string, string>, // Additional annotations
      labels?: Record<string, string>, // Additional labels
      tags?: string[], // Additional tags
      // Other metadata fields
    },
    spec?: Record<string, any>, // Custom specification data
  }
}
```

**Returns:** Created fragment information including:

- Fragment ID and entity reference
- Confirmation of applied decorations
- Any validation warnings or notes

#### Required Permissions

- **Fragment entity create** - `roadie.entity-fragment.create` - Permission to create and modify entity fragments

## Common Use Cases

### Fragment Discovery and Management

- "What fragments exist for the payment-service component?"
- "List all fragments in the system"
- "Find fragments that have been modified recently"

### Entity Enhancement

- "Update the decription of the user-service to say ..."
- "Add prometheus monitoring annotations to the user-service component"

### Bulk Operations and Analysis

- "Show me all fragments that modify descriptions"
- "List fragments that enhance entities with monitoring configurations"
- "Find all custom specifications added to payment-related services"

## Fragment Use Cases

### Adding Team Responsibility Information

```json
{
  "entityRef": "component:default/user-service",
  "fragment": {
    "metadata": {
      "annotations": {
        "roadie.io/responsible-team": "platform-team",
        "roadie.io/on-call-schedule": "https://pagerduty.com/schedules/platform"
      }
    }
  }
}
```

### Enhancing with Deployment Information

```json
{
  "entityRef": "resource:default/payment-gateway",
  "fragment": {
    "metadata": {
      "labels": {
        "deployment-strategy": "canary",
        "release-cycle": "weekly"
      }
    },
    "spec": {
      "deployment": {
        "replicas": 3,
        "strategy": "RollingUpdate"
      }
    }
  }
}
```

### Adding Monitoring and Observability

```json
{
  "entityRef": "api:default/orders-api",
  "fragment": {
    "metadata": {
      "annotations": {
        "datadog.com/dashboard": "https://app.datadoghq.com/dashboard/orders-api",
        "prometheus.io/scrape": "true"
      },
      "monitoring": {
        "alerts": ["high-error-rate", "high-latency"],
        "slos": [
          {
            "name": "availability",
            "target": 99.9
          }
        ]
      }
    },
    "spec": {}
  }
}
```

## Example Workflows

### Entity Enhancement Workflow

**User:** "I want to add team ownership information to all payment services"

**AI Response using MCP:**

1. Uses `list-fragments` to find existing fragments for payment services
2. Identifies services that need team ownership information
3. Uses `create-fragment` to add responsible team annotations
4. Provides summary of enhanced entities and their new metadata

### Fragment Audit and Discovery

**User:** "Show me all custom monitoring configurations added to our services"

**AI Response using MCP:**

1. Uses `list-fragments` to retrieve all fragments
2. Filters fragments containing monitoring-related specifications
3. Analyzes monitoring patterns and configurations
4. Provides summary of monitoring setups across services

### Systematic Entity Decoration

**User:** "Add deployment strategy labels to all components in the production namespace"

**AI Response using MCP:**

1. Uses entity search to find all production components
2. Uses `list-fragments` to check existing decorations
3. Uses `create-fragment` to add deployment strategy information
4. Confirms successful application and provides summary

## Best Practices

### Fragment Design

- **Specific Purpose**: Create fragments for specific enhancement purposes (monitoring, ownership, deployment info)
- **Update the source YAML file if possible**: Fragments allow easier updates to entity data and allow updates to entities not defined in YAML, but its always preferable to update the source entity of it comes from a YAML file in an SCM.

### Entity Reference Management

- **Precise References**: Use exact entity references (kind:namespace/name format)
- **Validation**: Verify target entities exist before creating fragments
- **Confirmation** Creating a fragment successfully does not mean it necessarily has been applied if there was an error. You can check if a Fragment was actually applied to an entity using the Get Entity MCP tool.

## Security Considerations

### Fragment Permissions

- Fragment mutations requires appropriate write permissions of `roadie.entity-fragment.create`

### Data Validation

- Fragment content is validated against entity schemas
- Malformed fragments are rejected with clear error messages

## Troubleshooting

### Common Issues

1. **Permission Errors**:

   - Verify you have the relevant `roadie.entity-fragment.<action>` permission
   - Ensure access to target entities before creating fragments

2. **Entity Reference Issues**:

   - Use exact entity reference format: `kind:namespace/name`
   - Verify target entities exist in the catalog
   - Check for typos in entity names or namespaces

3. **Validation Failures**:
   - Ensure fragment content follows expected schemas
   - Validate JSON structure and data types
   - Check that required fields are provided

---

### [Rich Catalog Entity Server](https://roadie.io/docs/api/roadie-mcp/rich-catalog-entity.md)

## Introduction

The Rich Catalog Entity Server provides AI assistants with comprehensive access to catalog entity data, relationships, and documentation from your Backstage instance.

**Server Endpoint:** `https://api.roadie.so/api/mcp/v1/rich-catalog-entity`

## Capabilities

- **Entity Information**: Get detailed metadata, ownership, lifecycle, and specifications
- **Relationship Mapping**: Discover dependencies, provides relationships, and entity connections
- **Documentation Access**: Search and retrieve TechDocs content associated with entities
- **Entity Discovery**: Search and find entities when exact names are unknown
- **Enhanced Error Handling**: Provides search suggestions when entities aren't found

## Available Tools

### Get Entity Info

Retrieve basic entity information including name, description, owner, lifecycle stage, and metadata.

**Parameters:**

- `entityRef` (string): Entity reference (e.g., "component:default/my-service")

**Example Usage:**

```json
{
  "entityRef": "component:default/user-service"
}
```

**Return Schema:**

```typescript
{
  name: string,
  title?: string,
  description?: string,
  owner?: string,
  lifecycle?: string,
  type?: string,
  tags?: string[],
  annotations?: Record<string, string>,
  labels?: Record<string, string>,
  links?: Record<string, any>[],
  namespace?: string,
  kind?: string
}
```

## Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities

### Get Entity Relationships

Discover entity relationships including dependencies, what the entity provides, and connected services.

**Parameters:**

- `entityRef` (string): Entity reference

**Example Usage:**

```json
{
  "entityRef": "component:default/payment-service"
}
```

**Return Schema:**

```typescript
{
  // Core relationships
  ownedBy?: string,
  owner?: string,
  system?: string,
  domain?: string,

  // Dependencies
  dependsOn: string[],
  dependencyOf: string[],

  // API relationships
  providesApis: string[],
  apiProvidedBy: string[],
  consumesApis: string[],

  // Hierarchical relationships
  partOf: string[],
  hasPart: string[],
  subcomponentOf?: string,
  subdomainOf?: string,

  // Group/User relationships
  memberOf: string[],
  members: string[],
  parent?: string,
  parentOf: string[],
  children: string[],
  childOf: string[],

  // Management relationships
  managedBy: string[],
  manages: string[]
}
```

## Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities

### Get TechDocs

Search and retrieve TechDocs documentation content for specific entities.

**Parameters:**

- `entityRef` (string): Entity reference
- `query` (string, optional): Search term within the documentation

**Example Usage:**

```json
{
  "entityRef": "component:default/auth-service",
  "query": "authentication flow"
}
```

**Return Schema:**

```typescript
{
  totalPages: number,
  pages: {
    title: string,
    content: string,
    path: string,
    htmlViewPath: string
  }[]
}
```

## Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities and their docs

### Search Entities

Discover and find entities when you don't know the exact entity name or want to explore available entities.

**Parameters:**

- `searchTerm` (string): Search term to find entities by name, title, or other attributes
- `kind` (string, optional): Filter by entity kind (e.g., "component", "api", "system")
- `namespace` (string, optional): Filter by specific namespace
- `limit` (number, optional): Maximum number of results to return (default: 10)

**Example Usage:**

```json
{
  "searchTerm": "payment",
  "kind": "component",
  "limit": 5
}
```

**Return Schema:**

```typescript
{
  totalFound: number,
  entities: {
    name: string,
    kind: string,
    namespace: string,
    title?: string,
    description?: string,
    owner?: string,
    lifecycle?: string,
    type?: string,
    tags?: string[],
    entityRef: string
  }[]
}
```

## Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities

### Search TechDocs

Search TechDocs documentation content across all entities in the catalog to find relevant information without knowing which specific entity contains it.

**Parameters:**

- `searchQuery` (string): Search query to find documentation content across all entities
- `pageLimit` (number, optional): Maximum number of results to return (default: 100)

**Example Usage:**

```json
{
  "searchQuery": "API design patterns",
  "pageLimit": 50
}
```

**Return Schema:**

```typescript
{
  totalResults: number,
  results: {
    pageTitle: string,
    content: string,
    path: string,
    htmlViewPath: string,
    entityRef: string,
    entityKind: string,
    entityNamespace: string,
    entityName: string
  }[]
}
```

**Usage Examples:**

- "Find documentation about API design patterns for my organisation"
- "What deployment patterns are used in my organisation"
- "How is Kubernetes used in my organisation? Are there any best practices?"
- "Search for security best practices in my organisation"
- "How are database migrations done in my organisation?"

**Key Benefits:**

- Discovers relevant documentation across entities you might not know about
- Useful when you don't know which specific entity contains the information
- Helps find patterns and best practices documented across multiple services
- Good for discovering related documentation in different teams/entities

## Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities and their documentation
- **TechDocs read** - Access to technical documentation

### User Group Listing

List users or groups and their relationships to understand organizational structure and team relationships.

**Parameters:**

- `entityType` (enum): Type of entities to list - "user" for User entities or "group" for Group entities
- `namespace` (string, optional): Optional filter by namespace. This is typically the SCM organisation, especially in the case of users and groups
- `limit` (number, optional): Maximum number of results to return (if not specified, returns all entities)

**Example Usage:**

```json
{
  "entityType": "user",
  "namespace": "platform",
  "limit": 50
}
```

**Return Schema:**

```typescript
{
  totalFound: number,
  entityType: string,
  entities: {
    entityRef: string,
    memberOf?: string[],
    type?: string,
    parent?: string,
    children?: string[],
    members?: string[]
  }[]
}
```

**Usage Examples:**

- "Which users are part of more than one group"
- "Are there any users not assigned to a group"
- "List all engineering team members"
- "Show me team hierarchies"
- "List users in the platform namespace"

**Key Benefits:**

- Shows team membership relationships (users in groups, group hierarchies)
- Provides organizational structure overview for answering team-related questions
- Returns minimal fields to reduce payload size and improve performance
- Helps understand team structure and user assignments

## Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities

## Common Use Cases

### Entity Exploration

- "Who owns the user-service component?"
- "What is the lifecycle stage of payment-api?"
- "Show me the description and metadata for auth-service"

### Dependency Analysis

- "What services does payment-service depend on?"
- "Which components use the user-api?"
- "Show me all the relationships for the auth-service"

### Documentation Discovery

- "What documentation exists for the payment-service?"
- "Search for authentication information in user-service docs"
- "Show me the getting started guide for inventory-api"

### Entity Discovery

- "Find entities related to payment processing"
- "Search for all user management services"
- "What APIs are available for authentication?"
- "Show me all components owned by the backend team"
- "Find systems in the platform namespace"

## Smart Entity Resolution

The Rich Catalog Entity Server includes intelligent entity resolution that makes it more user-friendly:

### How It Works

1. **Exact Match First**: Attempts to find the entity using the exact reference provided
2. **Fallback Search**: If exact match fails, searches for entities with matching names
3. **Type Prioritization**: Prefers Component entities, then falls back to other types (API, Resource, System)
4. **Namespace Awareness**: When a namespace is specified, prioritizes entities in that namespace

### Benefits

- **Flexible Queries**: Users don't need to know exact entity references
- **Natural Language**: Works with common entity names used in conversation
- **Context Awareness**: Understands common naming patterns and conventions
- **Enhanced Discovery**: When entities aren't found, provides intelligent search suggestions
- **Error Recovery**: Automatically suggests similar entities when exact matches fail

## Required Permissions

- **Catalog entity read (\*)** - Access to all catalog entities
- **TechDocs read** - Access to technical documentation (for TechDocs functionality)

## Example Workflows

### Entity Discovery Workflow

**User:** "I need to understand our payment infrastructure"

**AI Response using MCP:**

1. Uses `search-entities` to find all payment-related entities
2. Retrieves entity information for each discovered service
3. Maps relationships between payment components
4. Provides comprehensive overview of the payment ecosystem
5. Suggests related APIs and documentation for deeper exploration

### Dependency Analysis

**User:** "What does the user-service depend on?"

**AI Response using MCP:**

1. Uses `get-entity-relationships` to map all dependencies
2. Identifies direct and indirect dependencies
3. Explains the purpose of each dependency
4. Highlights potential impact of changes

## Best Practices

- Use search functionality when you don't know exact entity names
- Combine entity information with relationship data for comprehensive analysis
- Leverage TechDocs search to find specific documentation topics
- Use filters (kind, namespace) to narrow search results when needed

---

### [Scaffolder Server](https://roadie.io/docs/api/roadie-mcp/scaffolder.md)

## Introduction

The Scaffolder Server enables AI assistants to discover, validate, and execute Backstage scaffolder templates, automating project creation and code generation workflows.

**Server Endpoint:** `https://api.roadie.so/api/mcp/v1/scaffolder-use`

## Capabilities

- **Template Discovery**: Find available scaffolder templates using intelligent search
- **Template Inspection**: Get detailed template specifications and requirements
- **Input Validation**: Verify parameter values before template execution
- **Template Execution**: Run templates with proper error handling and monitoring
- **Status Monitoring**: Track execution progress and results

## Available Tools

### Find Scaffolder Templates

Search for available scaffolder templates using queries that match template names, descriptions, and tags.

**Parameters:**

- `queryString` (string): Search term for finding templates

**Example Usage:**

```json
{
  "queryString": "react frontend"
}
```

**Return Schema:**

```typescript
{
  results: {
    type: string,
    document: {
      kind: string,
      text: string,
      type: string,
      owner: string,
      title: string,
      keywords: string,
      location: string,
      lifecycle: string,
      namespace: string,
      componentType: string
    }
  }[]
}
```

## Required Permissions

- **Catalog entity read (\*)** - Access to catalog template entities

### Retrieve Scaffolder Template

Get detailed information about a specific template, including parameters, steps, and requirements.

**Parameters:**

- `name` (string): Template name
- `namespace` (string, optional): Template namespace (defaults to "default")

**Example Usage:**

```json
{
  "name": "microservice-template",
  "namespace": "platform"
}
```

**Return Schema:**

```typescript
{
  entityRef: string,
  spec: string
}
```

## Required Permissions

- **Catalog entity read (\*)** - Access to catalog template entities

### Validate Template Values

Check if your input values meet the template's parameter requirements before execution, preventing common errors.

**Parameters:**

- `templateRef` (string): Template reference (e.g., "template:default/my-template")
- `values` (object): Parameter values to validate

**Example Usage:**

```json
{
  "templateRef": "template:default/react-app",
  "values": {
    "name": "my-new-app",
    "description": "A React application",
    "owner": "team-frontend"
  }
}
```

**Return Schema:**

```typescript
{
  valid: boolean, // Whether the values are valid
  errors: string[], // List of validation errors
  schema: Record<string, any> // The template parameter schema
}
```

## Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities

### Run Scaffolder Template

Execute a scaffolder template with the provided values and optional secrets.

**Parameters:**

- `templateRef` (string): Template reference
- `values` (object): Required parameter values
- `secrets` (object, optional): Secrets needed by the template
- `skipValidation` (boolean, optional): Skip validation step

**Example Usage:**

```json
{
  "templateRef": "template:default/microservice",
  "values": {
    "name": "user-service",
    "description": "User management microservice",
    "owner": "backend-team",
    "database": "postgresql"
  },
  "secrets": {
    "github_token": "ghp_xxx"
  }
}
```

**Return Schema:**

```typescript
{
  id: string, // The created task ID
  taskUrl: string // URL to monitor the task
}
```

## Required Permissions

- **Scaffolder task create** - Allows the user to run scaffolder templates

### Get Scaffolder Task

Monitor the status and progress of template execution.

**Parameters:**

- `id` (string): Task ID returned from template execution

**Example Usage:**

```json
{
  "id": "abc123def456"
}
```

## Required Permissions

- **Scaffolder task read** - Allows a user to view scaffolder runs

## Common Use Cases

### Guided Project Creation

- "Create a new React application for the frontend team"
- "Set up a microservice with PostgreSQL database"
- "Generate a new API service with authentication"

### Template Exploration

- "What templates are available for Node.js services?"
- "Show me the requirements for the mobile app template"
- "What parameters does the library template need?"

### Automated Workflows

- Validate inputs before execution to prevent failures
- Execute templates with proper error handling
- Monitor progress and provide status updates

## Required Permissions

- **Catalog entity read (\*)** - Access to template definitions
- **Scaffolder execute** - Permission to run templates and create projects

## Example Workflows

### Basic Template Execution

1. **Find a template**: Use `find-scaffolder-templates` to discover available templates
2. **Inspect the template**: Use `retrieve-scaffolder-template` to understand requirements
3. **Validate inputs**: Use `validate-template-values` to ensure your values are correct
4. **Run the template**: Use `run-scaffolder-template` to execute
5. **Monitor progress**: Use `get-scaffolder-task` to check execution status

### AI-Guided Project Creation

**User:** "Create a new React frontend application"

**AI Response using MCP:**

1. Searches for React templates using `find-scaffolder-templates`
2. Shows available templates and their requirements
3. Guides user through providing necessary parameters
4. Validates inputs using `validate-template-values`
5. Executes template using `run-scaffolder-template`
6. Monitors progress and reports results

## Best Practices

- Always validate inputs before execution to catch errors early
- Provide clear, descriptive names for generated projects
- Include proper ownership and team information
- Use secrets parameter for sensitive information like tokens
- Monitor task status for long-running templates

## Security Considerations

- All operations require proper authentication tokens
- Template execution respects Roadie's permission model
- Task monitoring is limited to tasks you have access to

---

### [Tech Insights Facts Server](https://roadie.io/docs/api/roadie-mcp/tech-insights-facts.md)

## Introduction

The Tech Insights Facts Server provides AI assistants with access to operational metrics, compliance data, and insights from your Backstage Tech Insights configuration.

**Server Endpoint:** `https://api.roadie.so/api/mcp/v1/tech-insights-facts`

## Capabilities

- **Data Source Discovery**: Dynamically discover available Tech Insights data sources and their fact schemas
- **GitHub Metrics**: PR merge times, repository activity, contributor information, branch protection settings, code review policies
- **Security Metrics**: Vulnerability data from Snyk, Dependabot alerts, branch protection status
- **Monitoring Data**: PagerDuty incident metrics, mean time to resolve, Datadog SLO and monitor counts
- **Compliance Scoring**: Entity metadata completeness, ownership verification, TechDocs configuration
- **Repository Analysis**: File structure analysis, catalog status, codebase composition
- **Custom Facts**: Access any configured Tech Insights data source for specialized metrics
- **Bulk Operations**: Query facts across all entities from specific data sources with filtering

## Available Tools

### Get Data Source Discovery

Discovers available Tech Insights data sources and the fact data they provide.

**Parameters:**

- None required

**Example Usage:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-data-source-discovery",
      "arguments": {}
    },
    "id": 1
  }'
```

**Return Schema:**

```typescript
{
  dataSources: Array<{
    id: string,
    title: string,
    description?: string,
    cadence?: string,
    lifecycle?: any,
    createdAt?: string,
    updatedAt?: string,
    handlerDefinition?: {
      type: 'builtin' | string,
      config: {
        id: string,
        builtinId?: string
      }
    },
    timeout?: any,
    draft?: boolean,
    version?: string,
    entityFilter?: any,
    schema?: Record<string, {
      type: 'integer' | 'float' | 'string' | 'boolean' | 'datetime' | 'set' | 'object',
      description?: string,
      metadata?: {
        key?: string
      }
    }>
  }>,
  totalCount: number,
  builtinCount: number,
  customCount: number
}
```

**Workflow:**
This tool helps you understand what data sources are available and what facts they provide:

1. Call `get-data-source-discovery` to retrieve all available data sources
2. Receive a list of all data sources with their IDs, titles, descriptions, and fact schemas
3. Use the data source IDs to query specific facts using `get-entity-facts` or `get-all-entities-facts`

**Usage Examples:**

- "What data sources are available?"
- "What facts can I query about Rootly incidents?"
- "Show me the facts available for components in the catalog"
- "What is the average time to resolve for Rootly incidents on my-component?"

**Required Permissions:**

- **Catalog entity read (*)** - Access to catalog entities
- **Roadie Tech Insights Data Source Read** - Access to Tech Insights data

### Get Entity Facts

Gets Tech Insights facts for a specific data source and entity combination.

**Parameters:**

- `dataSourceId` (string): The ID of the data source to query facts from
- `name` (string): The name of the catalog entity
- `namespace` (string, optional): The entity namespace (defaults to "default")
- `kind` (string, optional): The entity kind (defaults to "component")

**Example Usage:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-entity-facts",
      "arguments": {
        "dataSourceId": "github-stats",
        "name": "user-service"
      }
    },
    "id": 1
  }'
```

**Example Usage with Full Parameters:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-entity-facts",
      "arguments": {
        "dataSourceId": "1234",
        "name": "payment-api",
        "namespace": "acmeinc",
        "kind": "api"
      }
    },
    "id": 1
  }'
```

**Return Schema:**

```typescript
{
  dataSourceId: string,
  dataSourceTitle?: string,
  entityRef: string,
  facts: Record<string, any>,
  timestamp?: string
}
```

**Workflow:**
Get facts for a specific entity from a data source:

1. First, use the data source discovery tool to find available data sources and their IDs
2. Call `get-entity-facts` with the data source ID and entity information
3. Receive all raw facts from that data source for the specified entity

**Usage Examples:**

- "Get all information available from Rootly about user-service"
- "What are the custom-security-check facts for payment-api?"
- "Show me all facts from data source '1234' for auth-service"
- "Fetch the techdocs facts for my-component"

**Key Benefits:**

- Dynamic fact retrieval for any configured data source
- Returns raw fact data with all available metrics
- Useful for exploratory analysis and custom integrations

**Required Permissions:**

- **Catalog entity read (*)** - Access to catalog entities
- **Roadie Tech Insights Data Source Read** - Access to Tech Insights data

### Get All Entities Facts

Get facts for all entities from a specific data source with optional filtering by kind and namespace (defaults to component entities).

**Parameters:**

- `dataSourceId` (string): The ID of the data source to query facts from
- `kind` (string, optional): Filter by entity kind (e.g., "component", "api"). **Defaults to "component".**
- `namespace` (string, optional): Filter by namespace (e.g., "default", "production")

**Example Usage:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-all-entities-facts",
      "arguments": {
        "dataSourceId": "7e6a974c-f0ec-473f-9cc1-21c2752780a0"
      }
    },
    "id": 1
  }'
```

**Example Usage with Filters:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-all-entities-facts",
      "arguments": {
        "dataSourceId": "7e6a974c-f0ec-473f-9cc1-21c2752780a0",
        "kind": "api",
        "namespace": "production"
      }
    },
    "id": 1
  }'
```

**Return Schema:**

```typescript
{
  dataSourceId: string,
  dataSourceTitle?: string,
  entities: Array<{
    entityRef: string,
    facts: Record<string, any>,
    timestamp?: string
  }>
}
```

**Workflow:**
Get facts for all entities from a specific data source:

1. First, use the data source discovery tool to find available data sources and their IDs
2. Call `get-all-entities-facts` with the data source ID
3. By default, returns only component entities (the most common use case)
4. Optionally override the kind filter or add namespace filtering
5. Receive facts for all matching entities tracked by that data source

**Available Filters:**

- **kind**: Filter by entity kind (e.g., "component", "api"). **Defaults to "component".**
- **namespace**: Filter by namespace (e.g., "default", "acmeinc")

**Usage Examples:**

- "Get all facts from data source 'github-stats'"
- "Get facts for all APIs from security metric data sources"
- "Show me all entities regardless of kind from github data source"
- "Get component facts in the acmeinc namespace"

**Note:**

- The default kind filter of "component" covers most use cases. To see all entity kinds, explicitly specify a different kind or omit the filter.

**Required Permissions:**

- **Catalog entity read (*)** - Access to catalog entities
- **Roadie Tech Insights Data Source Read** - Access to Tech Insights data

### Get GitHub Metrics

Retrieve GitHub-related metrics including pull request performance, repository activity, and contributor data.

**Parameters:**

- `name` (string): The name of the catalog entity
- `namespace` (string, optional): The entity namespace (defaults to "default")
- `kind` (string, optional): The entity kind (defaults to "component")

- `entityRef` (string): Entity reference

**Example Usage:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-github-metrics",
      "arguments": {
        "name": "user-service"
      }
    },
    "id": 1
  }'

```json
{
  "entityRef": "component:default/user-service"
}
```

**Return Schema:**

```typescript
{
  pullRequests: {
    total: number | 'unknown',
    merged: number | 'unknown',
    open: number | 'unknown',
    mergedPercentage: number | 'unknown',
    mergedLastMonth: number | 'unknown'
  },
  mergeTime: {
    avgHours: number | 'unknown',
    avgLastMonthHours: number | 'unknown',
    minHours: number | 'unknown',
    maxHours: number | 'unknown',
    minLastMonthHours: number | 'unknown',
    maxLastMonthHours: number | 'unknown'
  },
  issues: {
    total: number | 'unknown',
    open: number | 'unknown',
    closed: number | 'unknown',
    closedLastMonth: number | 'unknown'
  },
  latestMergedPR: {
    title: string | 'unknown',
    author: string | 'unknown'
  },
  collaboration: {
    languages: string[],
    collaborators: string[],
    collaboratorCount: number | 'unknown'
  },
  branchProtection: {
    enabled: boolean | 'unknown',
    enforceAdmins: boolean | 'unknown',
    allowDeletions: boolean | 'unknown',
    requiredLinearHistory: boolean | 'unknown',
    allowForcePushes: boolean | 'unknown',
    blockCreations: boolean | 'unknown',
    requiredSignatures: boolean | 'unknown'
  },
  codeReview: {
    dismissStaleReviews: boolean | 'unknown',
    requireCodeOwnerReviews: boolean | 'unknown',
    requireLastPushApproval: boolean | 'unknown',
    requiredApprovingReviewCount: number | 'unknown',
    strictRequiredStatusChecks: boolean | 'unknown',
    usesCodeowners: boolean | 'unknown',
    codeownersErrorCount: number | 'unknown',
    codeownersHasErrors: boolean | 'unknown'
  }
}
```

**Usage Examples:**

- "How long does it take to merge PRs for user-service?"
- "Show me GitHub metrics for payment-api"
- "What's the PR activity for auth-service?"

#### Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities
- **Roadie Tech Insights Data Source Read** - Access to Tech Insights data

### Get Security Metrics

Access security-related metrics from Snyk vulnerability scans and Dependabot alerts.

**Parameters:**

- `name` (string): The name of the catalog entity
- `namespace` (string, optional): The entity namespace (defaults to "default")
- `kind` (string, optional): The entity kind (defaults to "component")

- `entityRef` (string): Entity reference

**Example Usage:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-security-metrics",
      "arguments": {
        "name": "payment-service"
      }
    },
    "id": 1
  }'

```json
{
  "entityRef": "component:default/payment-service"
}
```

**Return Schema:**

```typescript
{
  snykIssues?: {
    total: number,
    critical: number,
    high: number,
    medium: number,
    low: number
  },
  dependabotAlerts?: {
    open: number,
    dismissed: number,
    fixed: number
  },
  branchProtection?: boolean
}
```

**Usage Examples:**

- "What security vulnerabilities does payment-service have?"
- "Are there any Dependabot alerts for user-service?"
- "Is branch protection enabled for auth-service?"

#### Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities
- **Roadie Tech Insights Data Source Read** - Access to Tech Insights data

### Get PagerDuty Metrics

Retrieve incident metrics and service configuration from PagerDuty integration.

**Parameters:**

- `name` (string): The name of the catalog entity
- `namespace` (string, optional): The entity namespace (defaults to "default")
- `kind` (string, optional): The entity kind (defaults to "component")

**Example Usage:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-pagerduty-metrics",
      "arguments": {
        "name": "auth-service"
      }
    },
    "id": 1
  }'

**Return Schema:**

```typescript
{
  incidentMetrics?: {
    totalIncidents: number,
    monthlyIncidents: number,
    quarterlyIncidents: number,
    meanTimeToResolve?: number,
    meanTimeToFirstAck?: number,
    upTimePercentage?: number
  },
  serviceInfo?: {
    hasEscalationPolicy: boolean,
    hasTeamsAssigned: boolean,
    hasDescription: boolean,
    alertCreationType?: string
  }
}
```

**Usage Examples:**

- "How many incidents does auth-service have?"
- "What's the MTTR for payment-service?"
- "Show me PagerDuty metrics for api:acmeinc/user-service"

#### Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities
- **Roadie Tech Insights Data Source Read** - Access to Tech Insights data

### Get Datadog Metrics

Access Service Level Objective (SLO) data and monitoring information from Datadog.

**Parameters:**

- `name` (string): The name of the catalog entity
- `namespace` (string, optional): The entity namespace (defaults to "default")
- `kind` (string, optional): The entity kind (defaults to "component")

**Example Usage:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-datadog-metrics",
      "arguments": {
        "name": "inventory-api"
      }
    },
    "id": 1
  }'

**Return Schema:**

```typescript
{
  sloCount: number,
  monitorCount: number
}
```

**Usage Examples:**

- "How many SLOs does inventory-api have?"
- "Show me Datadog metrics for payment-service"
- "What monitors are configured for auth-service?"

#### Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities
- **Roadie Tech Insights Data Source Read** - Access to Tech Insights data

### Get Entity Compliance

Evaluate entity metadata completeness and compliance with organizational standards.

**Parameters:**

- `name` (string): The name of the catalog entity
- `namespace` (string, optional): The entity namespace (defaults to "default")
- `kind` (string, optional): The entity kind (defaults to "component")

**Example Usage:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-entity-compliance",
      "arguments": {
        "name": "user-service"
      }
    },
    "id": 1
  }'

**Return Schema:**

```typescript
{
  metadata: {
    hasTitle: boolean | 'unknown',
    hasDescription: boolean | 'unknown',
    hasTags: boolean | 'unknown',
    hasOwner: boolean | 'unknown'
  },
  techdocs: {
    hasTechdocsRef: boolean | 'unknown'
  },
  ownership: {
    hasOwner: boolean | 'unknown',
    hasGroupOwner: boolean | 'unknown',
    hasRelationships: boolean | 'unknown'
  }
}
```

**Usage Examples:**

- "How complete is the metadata for user-service?"
- "Is payment-api properly documented?"
- "Does auth-service have proper ownership assigned?"

#### Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities
- **Roadie Tech Insights Data Source Read** - Access to Tech Insights data

### Get Repository Info

Analyze repository structure and catalog configuration status.

**Parameters:**

- `name` (string): The name of the catalog entity
- `namespace` (string, optional): The entity namespace (defaults to "default")

**Example Usage:**

```bash
curl -s -X POST https://api.roadie.so/api/mcp/v1/tech-insights-facts \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get-repository-info",
      "arguments": {
        "name": "payment-service"
      }
    },
    "id": 1
  }'

**Return Schema:**

```typescript
{
  filePaths: string[],
  totalFiles: number,
  inCatalog?: boolean,
  fileTypes: {
    docker: number,
    yaml: number,
    javascript: number,
    python: number,
    docs: number,
    config: number
  }
}
```

**Usage Examples:**

- "What files are in the payment-service repository?"
- "Is user-service properly cataloged?"
- "Show me the file structure for auth-service"

#### Required Permissions

- **Catalog entity read (\*)** - Access to catalog entities
- **Roadie Tech Insights Data Source Read** - Access to Tech Insights data

## Common Use Cases

### Performance Analysis

- "How long does it take to merge PRs for user-service?"
- "What's the incident rate for payment-service?"
- "Show me the SLO compliance for auth-api"

### Security Assessment

- "What security vulnerabilities does user-service have?"
- "Are there any Dependabot alerts for payment-service?"
- "What's the security posture of our inventory system?"

### Compliance Monitoring

- "How complete is the metadata for auth-service?"
- "Which services need better documentation?"
- "What's the compliance score for our payment components?"

### Operational Insights

- "Which services have the most incidents?"
- "What's the GitHub activity like for user-service?"
- "Show me the monitoring status for all payment services"

## Tech Insights Data Sources

The module automatically fetches data from all configured Tech Insights data sources, including:

- **GitHub Data Source**: PR metrics, repository info, collaborators, commit activity
- **Snyk Data Source**: Security vulnerability counts by severity level
- **Dependabot Data Source**: Dependency alert statistics and update metrics
- **PagerDuty Data Sources**: Incident metrics, MTTR, service configuration
- **Datadog Data Source**: SLO compliance, monitor counts, alert frequency
- **Repository Files**: File structure analysis, catalog-info.yaml status
- **Entity Metadata**: Completeness scores, required field compliance

## Example Workflows

### Security Assessment

**User:** "What's the security posture of our payment services?"

**AI Response using MCP:**

1. Uses `get-security-metrics` for all payment-related components
2. Aggregates vulnerability data across services
3. Identifies critical security issues requiring attention
4. Provides prioritized remediation recommendations

### Operational Review

**User:** "How are our services performing?"

**AI Response using MCP:**

1. Combines `get-github-metrics` with `get-pagerduty-metrics`
2. Analyzes development velocity and operational stability
3. Identifies services with concerning trends
4. Suggests areas for improvement

## Best Practices

- Combine multiple metrics for comprehensive service assessment
- Use compliance data to identify services needing attention
- Monitor trends over time rather than point-in-time snapshots
- Correlate security metrics with development activity

## Data Availability

Metric availability depends on your configured Tech Insights data sources. If a metric shows as unavailable, ensure the corresponding integration is properly configured in your Roadie instance.

---

### [Use custom renderer with your API entities](https://roadie.io/docs/catalog/custom-api-docs-renderers.md)

## Introduction

The API docs plugin supports user supplied renderers for API definitions. This page explains how you can configure such
a renderer in roadie.

## Prerequisites

- You must have custom plugins enabled for your tenant. Contact Roadie to enquire about this.

## Step 1: Write a custom renderer

A [custom API docs renderer](https://www.npmjs.com/package/@backstage/plugin-api-docs#custom-api-renderings) is a React
component which takes the API definition as a prop and renders it.

For example, the simplest custom renderer which just prefixes the definition would be something like this:

```typescript
import React from 'react';
import { Typography } from '@material-ui/core';

export const CustomApiDefinition = ({ definition }: { definition: string }) => (
  <Typography>Custom format: {definition}</Typography>
);
```

Ensure that the component is exported from the plugin:

```typescript
// src/index.ts
export { customApiDefinitionPlugin, CustomApiDefinition } from './plugin';
```

## Step 2: Configure your custom plugin

Navigate to the custom plugins page `/administration/custom-plugins` and click "Add new plugin". Then enter your plugin's
details.

- The plugin package should match the name in your plugin's package.json matching this convention `@<tenant-name>-roadie/<your plugin>`.
- The plugin name should be the name of the exported plugin variable (e.g. customApiDefinitionPlugin above)

Then click "Add Component" and set the type to ApiDocsWidget and the name to the name of the exported custom renderer
(e.g. CustomApiDefinition) and click "Save".

## Step 3: Publish your custom plugin

Read [the docs on custom plugins](/docs/custom-plugins/overview/) then build your package and publish to artifactory.

In a nutshell:

```
yarn tsc && yarn build && yarn version && yarn publish
```

## Step 4: Configure the renderer in settings

It is necessary to configure the type of entity the custom renderer applies to in settings at `/administration/settings/api-docs`.

First click "add item" then enter the custom renderer information.

- The type should match the `spec.type` field on API entities this should be used to render.
- The title is showed as the name of the format in the API docs card.
- The component is then specified and this should match the custom component registered in step #2
  (Caveat: it can take some time for a custom component to become available for use)

---

### [Custom Cards [beta]](https://roadie.io/docs/catalog/custom-cards.md)

## Introduction

Custom cards is a beta feature for generating UI components to be used within the Roadie IDP.

Custom cards can be created by Admins, entirely within the Roadie UI, for Entity pages or the Home Page to render data in whatever form you would like.

Each card is made up of:

- One or more Data Fetchers to grab data to populate the card from either internal Roadie APIs or proxies.
- Code to render the output of the returned data (MDX in this case)
- A set of Roadie components that help ensure the rendered card is in keeping with the rest of the user interface

## Creating a card

To create a card you can use the editor on either an Entity page using `CustomCard` or on the Home page using `CustomHomepageCard`.

The editor comprises of:

- Data fetcher configuration
- An editor so you can see the generated code
- A live preview of the rendered output
- And an AI agent to help generate and modify the cards themselves.

## Using the AI agent

An AI agent is available to both generate cards and to tweak generated output.

Simply articulate in natural language what you would like to do and the agent will make changes.

## Available components

The Custom Card has access to over 200 Roadie React components - `Table`, `Button` etc.

This allows visual uniformity of created custom cards and keeps the UI consistent.

The AI agent will automatically use these components, so there's no manual intervention required (unless you want to deviate from the components).

## Available context

Various contextual data objects are available in the Custom Cards.

### Users

Some user information is also available for use in the card. Logged in user and Backstage Identity information can be used either in the rendered output or in the API calls that the Data Fetchers make.

```
type UserInformation = {
  profile: ProfileInfo;
  displayName: string;
  userId?: string;
  identity?: BackstageUserIdentity;
};

type ProfileInfo = {
    email?: string;
    displayName?: string;
    picture?: string;
};

type BackstageUserIdentity = {
    userEntityRef: string;
    ownershipEntityRefs: string[];
};
```

For example, to retrieve a valid Backstage User Identity ref for a user could write something like `{props.user?.identity?.userEntityRef}` in the body of your card or `{{ user.identity.userEntityRef }}` as part of a templated Data Fetcher.

### Entities

Using the `/catalog` plugin, entity information can be accessed.

Several `/catalog` endpoints are available.

More info about the endpoints themselves can be found in [Backstage docs](https://backstage.io/docs/features/software-catalog/software-catalog-api/).

For example, if you wanted to pull information from the `/entities` Catalog API and use information about a user to retrieve only Group information pertinent to the logged in user, you could use the templated URL `/entities/by-query?filter=kind=Group,relations.hasMember={{ user.identity.userEntityRef }}`.

One potential output of that kind of card is something like this:

### Data from Proxies

Third party data is also available via configured proxies.

For example, data from PagerDuty could be accessed to retrieve data about an On Call rotation and parsed via a card. One potential output of that kind of card is something like this:

---

### [Customising your Catalog](https://roadie.io/docs/catalog/custom-views.md)

Admins can easily customise the tabs in the Catalog page to better fit your organisation's catalog data.

In Roadie, navigate to the Administration Settings page and in the Roadie Settings section select `Catalog`.

Here you can add new custom tabs that use filters to make a specific collection of catalog entities easy to access.

An example might be surfacing databases as a new tab, so you could create a new tab with the following filter assuming you have already added a database type to the correct entities:
e.g.
`{ kind: 'Resource', type: 'database' }`

You can then decide on the ordering of tabs and hide or show tabs.

NB: Consideration should be made around the number of tabs you want to expose to all users as having too many may actually make things harder to find. Catalog tab pages have extensive filtering options already which should mean that things are easy to search for withing a top level category, so you don't need a tab for everything. It is recommended to create tabs only for to top level domain objects or specific, organisation-wide categories.

---

### [Introduction](https://roadie.io/docs/catalog/decorating-components.md)

Decorators are an easy way to add links and annotations to Entities, without editing the YAML file that the Entity originates from.

Decorators are stored inside Roadie and available via the API.

## Decorating components

In order to access the decorator page, navigate to component page and select 'Decorate entity' from kebab menu at top right corner:

This will navigate you to the page where you can decorate your component with links and annotations, without a need to manually edit YAML files in your version control system. All of this is done via UI, in specifically designated sections.

A visual representation of the YAML structure of the component, is shown in Existing Entity section of the page.

Adding links is done via 'Add link' button in 'Links' section.

New link properties need to follow [link properties types](https://backstage.io/docs/features/software-catalog/descriptor-format#links-optional). Usually semantics of the type field are undefined, but we have added few predefined options you can select from a dropdown list.

Adding annotations is done via 'Add annotation' button in 'Annotations' section.

New annotation properties need to follow [annotation properties types](https://backstage.io/docs/features/software-catalog/descriptor-format#annotations-optional).

You will find all existing annotations used in components across the catalog in a dropdown list.

When you are happy with added annotations and/or links simply click 'Save' button and you will shortly see you changes.

**Please note:** all of the changes are kept and displayed in your Backstage instance, but YAML files in version control system remain intact.

---

### [Displaying Entity Metadata](https://roadie.io/docs/catalog/entity-metadata-card.md)

## Introduction

Roadie provides a card `EntityMetadataCard` which can be used to display any entity field in the catalog UI. This is particularly
useful where the entity spec contains custom fields.

## Configuration

- Firstly, determine which entity fields you wish to display.
- Add the `EntityMetadataCard` to a dashboard in the catalog UI. See [Instructions](/docs/getting-started/configure-ui/#updating-dashboards)
- Click the [add props](/docs/getting-started/configure-ui/#adding-props) icon and then click "New Row" under
  metadata. Select the field you wish to display and give it a display name.
  
- Repeat for any other fields you wish to display
  then click "Save" button and save the layout by clicking the save icon on the top right.

## Recent Blog Posts

### [The Context Engineering Glossary for Platform Engineers](https://roadie.io/blog/context-engineering-glossary.md)

Your team just wired an LLM into your Internal Developer Portal. The architecture review kicks off and someone asks whether you're doing RAG or agentic retrieval. Someone else flags context drift as a risk. A third person raises privilege leakage in the system prompt. You nod along, but the vocabulary is moving faster than the documentation.

This glossary defines every key term in the context engineering stack through the specific lens of platform engineering — Service Catalogs, TechDocs, golden paths, and on-call data — not abstract data science. Bookmark it, share it with your team, and use it as a reference before your next architecture decision.

This glossary focuses on context supply, not model training, fine-tuning, or prompt copywriting. Context engineering does not make models smarter — it determines what the model is allowed to know, when, and why. If an answer is wrong, the first place to look is rarely the model; it’s the data pipeline feeding it.

---

## Section 1: Context Fundamentals

### What Is Context Engineering?

Context engineering is the practice of curating, structuring, and retrieving the right infrastructure data so that an LLM can answer domain-specific questions accurately. The word choice matters: it's *engineering*, not prompting. Where prompt engineering focuses on the wording of individual queries, context engineering focuses on the entire information supply chain that feeds the model before it generates a word.

For platform teams, context engineering means deciding which fields from your `catalog-info.yaml` get indexed, how your TechDocs chunks get sized and tagged, and what real-time operational signals get injected at query time. A developer asking "Is the payments service production-ready?" gets a useful answer only if the lifecycle field from the Service Catalog was curated, indexed, and retrieved correctly. The LLM itself contributes maybe 20% of that answer's quality; context engineering accounts for the rest.

An LLM is a powerful reasoning engine with no institutional memory. Context engineering is how you give it one. In other words, context engineering is not about improving reasoning quality — it’s about constraining the information surface the model can reason over.

### What Is a Context Window?

The context window is the total number of tokens an LLM can process in a single request, covering the system prompt, retrieved documents, conversation history, and the generated response combined. [GPT-4o supports up to 128,000 tokens](https://platform.openai.com/docs/models/gpt-4o), and [Gemini 3.5 Pro pushes to 1 million tokens](https://deepmind.google/technologies/gemini/pro/). These numbers sound large until you picture a Service Catalog with 800 registered components, each with full metadata and linked TechDocs pages.

Stuffing everything into the context window is not a strategy. Irrelevant data degrades output quality, increases cost per query (models like [Claude charge per input token](https://www.anthropic.com/pricing)), and slows response time. The engineering discipline is in *selecting* the right 2,000 tokens out of 2,000,000 available, pulling only the service metadata relevant to the specific query, not the entire catalog.

Efficient context selection is where retrieval architecture pays for itself.

### What Is Grounding in LLMs?

Grounding anchors an LLM's response in verified, authoritative data sources rather than the model's pre-trained weights. Without grounding, a model answering "Who is the on-call engineer for the checkout service?" will either hallucinate a plausible name or admit it doesn't know. With grounding, the response comes from the live [PagerDuty](https://www.pagerduty.com/) schedule injected at query time.

In a platform engineering context, your Service Catalog is the primary grounding layer. When every answer the AI gives traces back to a specific entity in the catalog, with a citable source, you've achieved grounded output. Ungrounded AI assistants erode trust fast: one invented service name or wrong runbook link and developers stop using the tool. RAG is an architectural mechanism; grounding is the result. You can implement RAG without achieving grounding if the retrieved data isn’t authoritative or current.

---

## Section 2: Architecture and Retrieval Terms

### RAG (Retrieval-Augmented Generation)

[Retrieval-Augmented Generation (RAG)](https://arxiv.org/abs/2005.11401) is the architectural pattern where a system retrieves relevant documents from an external knowledge base before passing them to an LLM for response generation. The model doesn't rely on what it learned during training; it reads what you give it at runtime.

The flow for an IDP-backed assistant looks like this:

A developer asks: "How do I rotate credentials for the auth service?" The system encodes that query, searches TechDocs for credential rotation guides tagged to the auth service, pulls the service owner from the catalog, and injects both into the prompt. The LLM generates a specific, sourced answer, not a generic "here's how credential rotation works" response scraped from its training data.

RAG is the foundational pattern for any AI assistant built on top of an IDP. Every other term in this glossary relates to how well your RAG implementation performs.

### What Are Vector Embeddings?

A vector embedding is a numerical representation of text, typically a list of 768 to 3,072 floating-point numbers, that captures semantic meaning rather than just the words themselves. Two sentences that mean the same thing will have similar embeddings even if they share no words. "Service is deprecated" and "component has reached end-of-life" end up close together in embedding space; "deploy to production" and "YAML syntax error" end up far apart.

To build RAG for your IDP, every TechDocs page, every catalog entity description, and every relevant metadata field needs to be converted into an embedding and stored. When a developer submits a query, the query also gets embedded, and the system retrieves the stored documents whose embeddings are most similar. That's semantic search.

Generating and managing these embeddings is non-trivial. You need to pick an embedding model ([OpenAI's `text-embedding-3-large`](https://platform.openai.com/docs/guides/embeddings) or a self-hosted [Sentence Transformers](https://www.sbert.net/) variant), decide chunk sizes, handle incremental updates when docs change, and keep embeddings in sync with the underlying catalog. Roadie handles this entire pipeline automatically for TechDocs on your managed Backstage instance. You don't maintain a separate embedding job or manage model versions.

### What Is a Vector Database?

A vector database is a storage engine purpose-built for indexing and querying high-dimensional embedding vectors. It provides [Approximate Nearest Neighbor (ANN) search](https://en.wikipedia.org/wiki/Nearest_neighbor_search) at scale, which means it can find the 10 most semantically similar chunks from a corpus of 500,000 embeddings in under 100 milliseconds. Standard relational databases like PostgreSQL can store vectors (via [`pgvector`](https://github.com/pgvector/pgvector)), but dedicated systems like [Pinecone](https://www.pinecone.io/), [Weaviate](https://weaviate.io/), and [Qdrant](https://qdrant.tech/) are optimized for this workload.

For platform teams evaluating AI tooling, the vector database is an infrastructure dependency that often gets underestimated. It requires provisioning, access control, index tuning, and synchronization with your source catalog. When Roadie embeds your TechDocs, the vector storage layer is managed within the platform. You're not standing up a Qdrant cluster alongside your Backstage deployment.

### What Is Semantic Search?

Semantic search finds content based on meaning and intent, not keyword overlap. In an IDP context, it's the difference between a developer searching for "payment processor" and finding the `checkout-service`, `billing-api`, and `stripe-gateway` components — even though none of them are literally named "payment processor" — versus a keyword search that returns zero results because the exact string doesn't match any component name.

This matters especially for large catalogs and for developers who are new to the codebase. They don't know the internal naming conventions. They describe what they're looking for in plain English. Semantic search over vector embeddings bridges the delta between how developers think and how services are named.

On its own, semantic search is insufficient for an AI assistant — it retrieves candidates, but the Service Catalog determines which of those candidates are valid, owned, and safe to surface.

---

## Section 3: Platform Data Types (The Context Sources)

### Service Catalog Context

Service Catalog context is the structured metadata that lives in your `catalog-info.yaml` files and gets surfaced through the [Backstage catalog API](https://backstage.io/docs/features/software-catalog/). Fields like `owner`, `lifecycle`, `tier`, `tags`, `system`, and `dependsOn` are machine-readable facts that give an LLM the authority to answer structural questions.

"Who owns the recommendations engine?" gets answered from the `owner` field. "Is this service production-ready?" gets answered from the `lifecycle: production` tag. "What services would be affected if the user-profile API went down?" gets answered from dependency relationships in the catalog graph. This data is already structured, already maintained (or should be), and it's the highest-signal context source you have. Poor catalog hygiene directly degrades AI output quality.

### TechDocs Context

TechDocs context is unstructured markdown documentation that lives alongside your service code and gets rendered in [Backstage TechDocs](https://backstage.io/docs/features/techdocs/). It answers the "how" questions that structured catalog metadata can't: how to run the service locally, how to interpret a specific error code, how to onboard to the payments team's workflow.

When ingested into a RAG system, TechDocs pages get chunked (typically into 512-token segments with overlap), embedded, and indexed against their source entity. A developer asking "What does a 503 from the auth service usually mean?" should retrieve the relevant troubleshooting section from the auth service's TechDocs, not a generic HTTP guide. The specificity of the retrieval depends entirely on how well TechDocs are written and tagged. Vague documentation produces vague answers.

### Operational Context

Operational context is real-time data injected at query time rather than pre-indexed into a vector database. It includes current PagerDuty on-call schedules, [Kubernetes](https://kubernetes.io/) pod health and restart counts, recent [Argo CD](https://argo-cd.readthedocs.io/en/stable/) deployment status, open Jira incidents, and GitHub Actions build logs.

This data changes too fast for batch indexing to keep up. Instead, you pull it live via API calls triggered by the query itself. A developer asking "Why is checkout slow right now?" needs the current K8s resource utilization for the checkout pods, not the documentation about checkout's architecture. Mixing pre-indexed catalog and TechDocs context with real-time operational context is what separates a genuinely useful AI assistant from a documentation search engine.

Operational context informs decisions; it does not imply automated remediation unless explicitly authorized. Observing live state and acting on it are separate trust boundaries.

### Golden Path Context

Golden path context comes from your [Backstage Scaffolder](https://backstage.io/docs/features/software-templates/) templates, the opinionated, pre-approved patterns your platform team maintains for creating new services, adding CI/CD pipelines, or spinning up databases. This context feeds the AI's code generation and workflow guidance capabilities.

When a developer asks "How do I create a new Python microservice that follows our standards?" the answer shouldn't come from a generic tutorial. It should come from your actual Scaffolder template, including your team's specific conventions around naming, logging configuration, health check endpoints, and observability setup. Golden path context ensures that AI-assisted code generation produces output that passes your internal review standards on the first attempt.

---

## Section 4: Agentic Capabilities

### What Is Agentic Context Injection?

Agentic context injection is the dynamic process by which an AI system decides *which* data sources to query based on the intent of the user's question, rather than fetching a fixed set of context for every request. It's the difference between a system that always retrieves the top-10 catalog entries regardless of the question, and a system that recognizes "my build is failing" as a signal to pull CI/CD logs, not architecture documentation.

A well-designed agentic system routes queries through an intent classifier first. Questions about ownership route to the catalog API. Questions about procedures route to TechDocs embeddings. Questions about current system state trigger live operational data calls. This routing logic is itself a form of engineering. It determines response latency, token cost, and answer relevance simultaneously.

Without strict boundaries, agentic retrieval increases blast radius: every additional tool or data source expands what the system can surface or misuse. Intent routing must be auditable, deterministic, and permission-aware to be safe in production.

### Tool Use and Function Calling

[Function calling](https://platform.openai.com/docs/guides/function-calling) is the capability that allows an LLM to request the execution of a predefined function, a structured API call, rather than generating a text answer directly. The model outputs a JSON object specifying which function to call and with which parameters; your application executes the call and feeds the result back to the model.

For IDP AI assistants, function calling turns the LLM into an active participant in your platform's API surface. Instead of the model trying to recall what it knows about a service's on-call engineer, it calls `get_oncall_for_service(service_id="checkout")`, gets a live response from PagerDuty, and incorporates that response into its answer. Functions you'd expose typically include catalog entity lookup, TechDocs page retrieval, incident history queries, and deployment status checks. The LLM becomes a reasoning layer over your actual infrastructure data.

### What Is a System Prompt?

The system prompt is the foundational instruction block prepended to every conversation with the AI assistant. It defines the model's persona (a senior platform engineer, not a general assistant), its constraints ("only answer questions about services in this catalog"), its output format preferences, and its access permissions.

For a platform assistant, the system prompt is effectively a policy document. It specifies that the model should cite its sources, decline to speculate about services not in the catalog, and escalate ambiguous ownership questions to a human. A weak system prompt produces an assistant that will confidently make things up. A well-engineered system prompt is a first line of defense against the risks described in the next section. In practice, the system prompt is inseparable from access control. It should reflect the same RBAC assumptions as the IDP itself — otherwise the model’s behavior will drift from the platform’s security model.

---

## Section 5: Quality and Risk Definitions

### What Is LLM Hallucination?

Hallucination is when an LLM generates information that is factually incorrect but presented with full confidence. In a platform engineering context, hallucinations take a specific and damaging form: the model invents service names, fabricates runbook steps, cites non-existent on-call rotations, or describes API contracts that don't match the actual implementation.

The primary defense against hallucination is grounding (see above), combined with explicit system prompt instructions to cite sources. If the model's answer can't be traced to a specific catalog entity or TechDocs page, it shouldn't be trusted. Measuring hallucination rate by sampling model responses against the catalog is a useful quality metric for AI-enabled IDP rollouts.

### What Is Context Drift?

Context drift is the discrepancy between the data the AI has indexed and the actual current state of your infrastructure. A TechDocs page describing the old three-tier deployment model that your team migrated away from six months ago is a context drift problem. A catalog entry with a stale owner field pointing to a team that was reorganized is another.

Context drift is not a one-time fix. It's an ongoing operational concern. The mitigation is a combination of automated re-indexing (triggering embedding updates when `catalog-info.yaml` files change) and documentation standards that treat TechDocs as a first-class engineering artifact. An AI assistant is only as current as the data it reads. If your catalog hygiene is poor, context drift will silently produce incorrect answers with no obvious signal that something is wrong.

### What Is Context Poisoning?

Context poisoning occurs when low-quality, contradictory, or maliciously crafted documentation gets retrieved and influences the model's output. Two TechDocs pages for the same service that give conflicting deployment instructions will cause the model to blend them into a response that's confidently wrong. A poorly maintained runbook that describes a procedure deprecated two years ago is a context poisoning vector.

The solution is content governance: ownership requirements for every TechDocs page, last-reviewed timestamps surfaced in the catalog, and automated quality checks that flag documentation not updated in over 90 days. The AI doesn't discriminate between trusted and untrusted docs. The retrieval system surfaces whatever scores highest semantically. You own the quality of what gets indexed.

### What Is Context Overreach?

Context overreach happens when you inject too much data into the prompt, including irrelevant retrieved chunks that dilute the signal and confuse the model. A developer asking about the auth service's rate limits doesn't need context from the billing service's TechDocs, even if billing is a downstream dependency. Retrieving ten chunks when three would suffice increases token cost, slows the response, and statistically introduces off-topic content that nudges the model toward a less precise answer.

The fix is tighter retrieval: stricter similarity thresholds, metadata filtering (retrieve only docs tagged to the queried service), and re-ranker models that score retrieved chunks for relevance before they enter the prompt. Context budgeting, deciding in advance how many tokens each source type is allowed to consume, is a practical starting point.

### What Is Privilege Leakage in AI Systems?

Privilege leakage occurs when the AI assistant returns information about services, infrastructure, or documentation that the querying user shouldn't have access to, because the retrieval layer doesn't enforce the same [Role-Based Access Controls (RBAC)](https://backstage.io/docs/permissions/overview) as the IDP itself. A junior engineer asking a general question about "our database infrastructure" shouldn't receive details about the security team's secrets management service, even if that service's TechDocs scored highly in the semantic search results.

Preventing privilege leakage requires that your retrieval pipeline filters indexed documents by the user's Backstage permissions before returning results. It's not enough to apply RBAC at the catalog UI layer; the vector search results that feed the LLM must respect the same access policies. This is one of the most commonly overlooked security requirements in IDP AI implementations.

### What Are Implicit Trust Chains?

An implicit trust chain forms when a document retrieved as context itself references other documents — runbooks, architecture decision records, external wikis — that are outdated, incorrect, or not indexed by the retrieval system. The model reads the retrieved doc, which cites "the standard deployment procedure in the ops runbook," but the ops runbook lives in Confluence and isn't indexed. The model either ignores the reference, invents what it thinks the runbook says, or generates an incomplete answer.

Auditing your documentation for external references and either bringing those references into your indexed corpus or explicitly removing the links is a necessary part of context engineering. Every document in your retrieval index is implicitly vouching for everything it cites.

---

The pattern running through every definition in this glossary is simple: context engineering is now a core platform responsibility, not an AI feature bolted on at the edge. LLMs are capable of sophisticated reasoning, but they reason over whatever you give them. Platform teams that invest in clean catalogs, maintained TechDocs, and well-governed golden paths aren't just doing good hygiene. They're building the infrastructure that makes AI actually work.

---

### [Splitting TechDocs Out of Our Monolithic Backstage Deployment](https://roadie.io/blog/splitting-techdocs-out-of-our-monolithic-backstage-deployment.md)

At [Roadie](https://roadie.io/), we operate Backstage at a significant scale. Each customer receives a fully isolated, single-tenant Backstage deployment running in its own Kubernetes namespace. This architecture gives customers strong security boundaries, predictable isolation, and the freedom to customize their instance without affecting others.

But, this model also introduces some operational complexity. Architectural decisions that are harmless at a small scale can cause issues when every tenant is running their own Backstage stack. One such decision was how we deployed [TechDocs](https://backstage.io/docs/techdocs/generated-index/) as part of the same backend service as everything else.

In this article, we'll talk about why our original approach stopped scaling, how we redesigned it, and what improved when we split TechDocs out of the monolithic backend.

## Our Original Architecture

In our original setup, each Roadie tenant ran a complete Backstage application composed of all frontend and backend plugins bundled together. On the backend side, everything was executed within a single Node.js process.

This meant that for each customer, a dedicated Kubernetes namespace was created to ensure isolation, a single Backstage backend pod was deployed into that namespace, and all backend plugins like Catalog, Scaffolder, TechDocs, and Auth were loaded into the same backend service.

From an architectural standpoint, this resulted in a classic monolith. Every backend plugin shared the same runtime, memory space, CPU limits, and lifecycle. This design was simple to operate and reason about early on, and it served us well for a long time. But, as customer usage patterns evolved, issues began to appear.

## The Problem: Resource Contention

As more customers adopted TechDocs and began publishing larger documentation sites, we started receiving alerts that were difficult to explain at first glance.

These incidents typically involved brief periods during which the Backstage backend became unavailable, CPU usage exceeded configured limits, and Kubernetes restarted backend pods from resource exhaustion. What made this particularly challenging was that the failures were intermittent and tenant-specific. Many tenants were completely unaffected, while a handful experienced repeated disruptions, which made it harder to pinpoint the issue.

After analyzing metrics, logs, and pod-level behavior, a pattern emerged. In every affected case, the TechDocs backend plugin was consuming a disproportionate amount of CPU and memory.

### Why TechDocs Was the Culprit

We noticed that issues only occurred for tenants with particularly heavy TechDocs usage. This included large documentation sites with many pages and assets, repositories containing multiple documentation sets, and frequent rebuilds triggered by ongoing documentation updates.

This behavior is expected when you look at what TechDocs does under the hood. The backend is responsible for fetching documentation files, rendering Markdown content, and running documentation generators like MkDocs. These tasks are inherently resource-intensive, especially during large or frequent builds.

When TechDocs runs in the same process as the rest of the Backstage backend, resource spikes are not contained. CPU saturation or memory pressure caused by documentation builds directly impacts unrelated functionality, including catalog ingestion, scaffolder workflows, and authentication. The monolithic design of TechDocs became a liability.

## The Decision: Split TechDocs Out

To restore stability and regain operational control, we decided to extract TechDocs from the monolithic backend and deploy it as a separate Backstage backend application. The main reason for this was isolation. We wanted TechDocs to operate independently so that its workload characteristics would not interfere with the rest of the system. At the same time, we wanted to avoid breaking existing APIs or introducing fragile custom integrations.

Our TechDocs requirements were simple:

- It needed to be independently deployable so it could evolve on its own schedule.
- It needed to be discoverable by the core backend without hardcoded configuration.
- It needed to scale independently, based on documentation workload rather than overall backend traffic.

## The New Architecture

In the new design, each tenant runs two distinct Backstage backend services instead of one.

The first is the **core Backstage backend.** This service is responsible for handling catalog ingestion, Tech Insights, authentication, and other core APIs.

The second is a **dedicated TechDocs backend.** This service runs only the TechDocs-related functionality and handles documentation builds and rendering.

The two services communicate using Backstage’s built-in discovery mechanism.

## Results

### Cleaner Cluster Allocations

By running TechDocs in its own pod, we gained fine-grained control over its resource profile. CPU and memory limits are now explicitly tuned for documentation workloads, and scaling rules can be applied only where documentation usage justifies it.

This prevents overprovisioning the core backend while still allowing TechDocs to scale aggressively when needed.

### Improved Stability

Isolating TechDocs eliminated an entire class of failures. Documentation builds no longer put pressure on unrelated backend functionality. Catalog ingestion, scaffolder executions, authentication flows, and core API availability remain stable even during peak documentation activity.

For customers, this translates directly into fewer outages and a more predictable Backstage experience.

### Easier Debugging and Operations

From an operational perspective, separating TechDocs clarified boundaries. Resource spikes are now immediately attributable to the correct service. Logs are easier to interpret, and incidents can be diagnosed and mitigated quickly.

This separation also simplifies future tuning and capacity planning. With TechDocs isolated, we can reason about its resource usage independently from the rest of the backend and make decisions based on real workload characteristics rather than worst-case assumptions. CPU and memory requests can be adjusted specifically for documentation builds, and autoscaling policies can be tuned around build frequency, repository size, and peak documentation activity. This also makes forecasting easier: growth in documentation usage no longer forces us to overprovision the core backend. Instead, we can scale and optimize each service independently, reducing wasted capacity while maintaining predictable performance.

## What We Gained Overall

Splitting TechDocs out of the monolith forced us to formalize a clear boundary between core platform responsibilities and workload-specific plugins, which in turn improved how we think about backend composition overall. What started as a targeted stability fix turned out to have broader implications for how we structure the backend.

As a result, we now have a repeatable pattern for extracting heavy backend plugins into independent services when their resource profiles or failure modes warrant it. Backend deployments are slimmer, responsibilities are better defined, and each service can be sized and scaled according to the work it actually performs rather than the worst-case behavior of a single plugin. This makes the system easier to reason about both during normal operation and when something goes wrong.

## Takeaways

TechDocs was the most obvious candidate for separation due to its workload profile, but this architecture opens the door to further modularization where it makes sense. Backstage provides the primitives needed to support this kind of design. At scale, using them becomes less of an optimization and more of a requirement.

If you're running Backstage in a multi-tenant or high-scale environment and are seeing similar symptoms, it's worth examining your heaviest backend plugins and questioning whether they belong in the same process as the rest of Backstage.

---

### [Supercharge your GitLab setup with Roadie's Internal Developer Portal](https://roadie.io/blog/supercharge-your-gitlab-setup.md)

**[Roadie's SaaS Backstage platform](/) offers the deepest GitLab integration of any Internal Developer Portal**, solving "GitLab Sprawl," the challenge of navigating hundreds of repositories without a unified [software catalog](/product/catalog/), ownership model, or governance layer. GitLab itself acknowledges the gap: its own IDP category is officially "planned but not funded," with implementation pushed beyond 2025. For GitLab-centric organizations, Roadie provides a production-ready portal in hours rather than the 6 to 12 months required to self-host Backstage.

This guide covers every integration surface between Roadie and GitLab, from auto-discovery of catalog entities across hundreds of repos to CI/CD visualization, scaffolding new services, enforcing governance via scorecards, and securely connecting self-managed GitLab instances through the Roadie Broker.

## Set Up Roadie with GitLab: A Step-by-Step Guide

Connecting GitLab to Roadie takes about 30 minutes. You'll create a token, configure auto-discovery to populate your [Software Catalog](/product/catalog/), enable CI/CD visibility, and build your first [scaffolder template](/product/scaffolder/).

## Prerequisites

Before you start, make sure you have:

- Admin access to your Roadie instance (URL format: `https://<your-tenant>.roadie.so`)
- A GitLab account with permissions to create Personal Access Tokens
- Access to at least one GitLab group or project containing repositories.

## Step 1: Create and Configure Your GitLab Token

GitLab uses Personal Access Tokens to authenticate API requests. Roadie needs this token to read repositories, discover catalog entities, and interact with CI/CD pipelines.

Backstage needs a [GitLab API token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) for discovery and plugin data. Three token types exist, each with different trade-offs:

**Group Access Tokens** are the recommended choice for Backstage integrations. They create a bot user scoped to a specific group and all its projects, don't consume a GitLab license seat, and aren't tied to a human user (avoiding breakage when someone leaves the organization). They require GitLab Premium or Ultimate on SaaS. **Personal Access Tokens (PATs)** provide broader instance-wide access but inherit the creating user's permissions and break if that user is deactivated. **Project Access Tokens** are too narrow for discovery since you'd need one per repository.

The required scopes depend on the use case. For **read-only catalog discovery and CI/CD visualization**, `read_api` is sufficient. For **[scaffolder](https://roadie.io/product/scaffolder/) operations** that create repositories and merge requests, the full set of `api`, `read_repository`, and `write_repository` is needed. Roadie stores tokens securely in its secrets management UI at `https://<tenant>.roadie.so/administration/secrets`, backed by AWS Parameter Store with per-tenant KMS encryption, rather than requiring them in plaintext config files.

Once you have your token, you can enter it into [Roadie](/docs/details/setting-secrets/).

1. Log into your Roadie instance at `https://<your-tenant>.roadie.so`

2. Navigate to **Administration > Secrets** (direct URL: `https://<your-tenant>.roadie.so/administration/secrets`).

3. Find the secret named `GITLAB_TOKEN`

4. Click **Edit** and paste your GitLab token

5. Click **Save**

The secret update takes 2-3 minutes to propagate. You'll see the status indicator change from "Updating" to "Available" when it's ready.

## Configure Auto-Discovery: eliminate manual catalog registration at scale

The core of any Internal Developer Portal is the [software catalog](https://roadie.io/product/catalog/). Without auto-discovery, teams must manually register every service, an approach that collapses at hundreds of repositories. [Backstage's](https://backstage.io) `GitlabDiscoveryEntityProvider`, packaged in `@backstage/plugin-catalog-backend-module-gitlab`, crawls a GitLab instance, finds repositories containing a `catalog-info.yaml` file, and registers them automatically.

In self-hosted Backstage, this requires editing `app-config.yaml` directly:

```yaml
catalog:
  providers:
    gitlab:
      production:
        host: gitlab.com
        branch: main
        fallbackBranch: master
        skipForkedRepos: true
        includeArchivedRepos: false
        group: my-org                     # Scope to a specific group
        groupPattern:
          - '^platform-.*$'               # Regex: only groups starting with "platform-"
          - 'services'
        projectPattern: '[\s\S]*'         # Regex: match all projects (default)
        entityFilename: catalog-info.yaml
        excludeRepos:
          - my-org/deprecated-service
        schedule:
          frequency: { minutes: 30 }
          timeout: { minutes: 3 }
```

**Roadie replaces this YAML editing with a UI-based configuration** at `https://<tenant>.roadie.so/administration/settings/integrations/gitlab`. Admins add their GitLab instance URL, configure provider rules pointing to specific groups, and entities appear in the catalog within minutes.

The discovery provider supports powerful filtering through regex patterns. The `groupPattern` field accepts a list of regular expressions OR'd together to select which groups to scan. The `projectPattern` field applies a regex against each project's `path_with_namespace`. A legacy discovery processor also exists using wildcard URLs (`https://gitlab.com/group/subgroup/blob/*/catalog-info.yaml`, where `*` resolves to each repo's default branch), but the entity provider approach is the current recommended pattern.

For near-real-time updates, the provider supports **webhook-driven ingestion**, configure GitLab `push` webhooks to trigger incremental catalog refreshes instead of waiting for scheduled polls. Events can be received via HTTP endpoints, AWS SQS, Google Pub/Sub, or Kafka through `@backstage/plugin-events-backend-module-gitlab`.

To set up auto-discovery:

1. Navigate to **Administration > Integrations & Plugins > GitLab** (direct URL: `https://<your-tenant>.roadie.so/administration/settings/integrations/gitlab`)

2. In the **Host** field, enter your GitLab instance URL:
   - For GitLab.com: `gitlab.com`
   - For self-hosted: Your full domain (e.g., `gitlab.company.com`)

3. Leave **API Base URL** with the default vaule unless you're using a custom API endpoint

Now, you’ll need to add a discovery provider in Roadie. The discovery provider tells Roadie which GitLab groups or projects to scan for catalog files.

1. In the same GitLab integration page, scroll to **Configure GitLab Discovery**

2. Click **Add Provider Configuration**

3. Configure the provider. At the very least, you’ll need to enter your group name. You can also add filters to refine discovery. For example, you can add a [project pattern](/docs/catalog/location-management/#gitlab-autodiscovery).

4. Click **Save**

The discovery process runs every hour by default. To trigger an immediate scan, you can refresh the catalog or wait for the next scheduled run.

For Roadie to link catalog entities to GitLab data, you need to add GitLab-specific annotations to your `catalog-info.yaml` files.

Add one of these annotations to your entity metadata:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: my-service
  annotations:
    # Option 1: Use project ID (found in Settings > General in GitLab)
    gitlab.com/project-id: '12345'

    # Option 2: Use project slug (group/project format)
    # gitlab.com/project-slug: 'acme-corp/my-service'

    # Option 3: For self-hosted GitLab instances
    # gitlab.com/instance: 'gitlab.company.com'
```

The project ID is the most reliable option. You can find it in your GitLab project under **Settings > General** at the top of the page.

Now, auto-discovery should be enabled, and your catalog will be populated with projects from GitLab.

## CI/CD visibility and contextual linking to GitLab

Once entities are cataloged, the `@immobiliarelabs/backstage-plugin-gitlab` provides rich GitLab data directly on each component's page in Backstage. This plugin reads the `gitlab.com/project-slug` or `gitlab.com/project-id` annotation and calls the GitLab API via a backend proxy to surface:

- **Pipeline status table** showing the last 20 builds with status (success/failed/running/pending), direct links to the GitLab pipeline URL, and execution time
- **Merge requests table** with open and recently merged MRs, linking directly to GitLab
- **MR statistics** for review velocity insights
- **Contributors/people card**, language breakdown, releases, code coverage, and rendered README

The plugin supports both cloud-hosted `gitlab.com` and self-managed GitLab instances (configured via the `gitlab.com/instance` annotation). Multiple GitLab instances can be configured simultaneously in Roadie, useful for organizations running both cloud and on-premise deployments or undergoing migrations between the two.

The GitLab plugin should already be installed in your Roadie instance, but you need to add it to your component layouts.

1. Navigate to any component in your catalog

2. Click the **gear icon** (⚙️) in the top right corner

3. Click the **plus icon** (+) to add a new card

4. Select **GitLab** from the plugin list:
   - **EntityGitlabPeopleCard**: Shows contributors and languages
   - **EntityGitlabPipelinesTable**: Shows recent pipeline runs
   - **EntityGitlabMergeRequestStatsCard**: Shows MR stats
   - **EntityGitlabMergeRequestsTable**: Shows MRs
   - **EntityGitlabReadmeCard**: Shows Readme
   - **EntityGitlabLanguageCard**: Shows repository languages
   - **EntityGitlabReleasesCard**: Shows recent releases

5. Drag the cards to arrange them in your preferred order

6. Click **Save** to apply the layout.

If you want consolidated GitLab data:

1. Click the **plus icon** (+) next to the existing tabs

2. Select **EntityGitlabContent**

3. Name the tab (e.g., "GitLab")

4. Click **Save**

This creates a comprehensive GitLab view with all available cards on one page.

## Step 4: Create Your First Scaffolder Template

[Software Templates](https://roadie.io/product/scaffolder/) in Backstage, powered by the Scaffolder plugin, let developers create new projects through forms that execute predefined actions.

Create a new file in one of your GitLab repositories at `templates/basic-service.yaml`:

```yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: gitlab-basic-service
  title: Create a New Service (GitLab)
  description: Creates a new service repository in GitLab with a standard structure
spec:
  owner: user:default/<your-user>
  type: service

  parameters:
    - title: Service Information
      required:
        - name
        - owner
        - description
      properties:
        name:
          title: Service Name
          type: string
          description: Unique name for your service (lowercase, hyphens only)
          pattern: '^[a-z0-9-]+$'
        description:
          title: Description
          type: string
          description: What does this service do?
        owner:
          title: Owner
          type: string
          description: User that owns this service
          ui:field: OwnerPicker
          ui:options:
            catalogFilter:
              kind: [Group, User]

    - title: GitLab Configuration
      required:
        - repoUrl
      properties:
        repoUrl:
          title: Repository Location
          type: string
          ui:field: RepoUrlPicker
          ui:options:
            allowedHosts:
              - gitlab.com
            allowedOwners:
              - <your-group>

  steps:
    - id: fetch-base
      name: Fetch Base Template
      action: fetch:template
      input:
        url: https://gitlab.com/<your-group>/<your-repo>/-/tree/master/skeleton
        values:
          name: ${{ parameters.name }}
          description: ${{ parameters.description }}
          owner: ${{ parameters.owner }}
          repoUrl: ${{ parameters.repoUrl }}

    - id: publish
      name: Publish to GitLab
      action: publish:gitlab
      input:
        repoUrl: ${{ parameters.repoUrl }}
        defaultBranch: main

    - id: register
      name: Register Component
      action: catalog:register
      input:
        repoContentsUrl: ${{ steps.publish.output.repoContentsUrl }}
        catalogInfoPath: '/catalog-info.yaml'

  output:
    links:
      - title: Repository
        url: ${{ steps.publish.output.remoteUrl }}
      - title: Open in Catalog
        icon: catalog
        entityRef: ${{ steps.register.output.entityRef }}
```

### Create the Template Skeleton

In the same repository, create a `skeleton` directory with your template files:

**skeleton/catalog-info.yaml:**

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: ${{ values.name }}
  description: ${{ values.description }}
  annotations:
    gitlab.com/project-slug: ${{ values.repoUrl | parseRepoUrl | pick('owner') }}/${{ values.name }}
spec:
  type: service
  lifecycle: experimental
  owner: ${{ values.owner }}
```

**skeleton/README.md:**

```markdown
# ${{ values.name }}

${{ values.description }}

## Getting Started

[Add your setup instructions here]

## Owner

Maintained by: ${{ values.owner }}
```

**skeleton/.gitignore:**

```
node_modules/
.env
dist/
```

### Register the Template

1. Create a `catalog-info.yaml` in your templates repository:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Location
metadata:
  name: templates
  description: Scaffolder templates for our organization
spec:
  type: url
  targets:
    - https://gitlab.com/<your-group>/<your-repo>/-/blob/main/templates/basic-service.yaml
```

1. Register this location in Roadie:
   - Navigate to **Catalog > Import**
   - Paste the URL to your `catalog-info.yaml`
   - Click **Analyze**, then **Import**

If auto-discovery is configured for your templates repository, Roadie finds and registers them automatically.

### Test Your Template

1. Navigate to **Templates** in your Roadie instance

2. Find your template: "Create a New Service (GitLab)"

3. Click **Run** and fill out the form:
   - Service Name: `test-service`
   - Description: `A test service to verify template functionality`
   - Owner: Select an owner from the dropdown
   - Repository Location: Provide a name for the repository

4. Click **Review** to see a summary of what will be created

5. Click **Create** to execute the template

The scaffolder will:

- Generate files from your skeleton directory
- Create a new GitLab repository
- Push the generated code
- Register the component in your Roadie catalog

You'll see a link to the new repository and the catalog entry when complete.

### Add GitLab-Specific Actions

Roadie supports [several GitLab-specific scaffolder actions](https://roadie.io/backstage/scaffolder-actions/) beyond basic repository creation:

**Create a merge request:**

```yaml
- id: create-mr
  name: Create Merge Request
  action: publish:gitlab:merge-request
  input:
    repoUrl: gitlab.com?owner=acme-corp&repo=my-service
    title: 'feat: Initial service setup'
    description: 'Automated setup via scaffolder'
    branchName: feature/initial-setup
    targetBranch: main
```

**Add project variables:**

```yaml
- id: add-variables
  name: Add CI/CD Variables
  action: gitlab:projectVariable:create
  input:
    repoUrl: gitlab.com?owner=acme-corp&repo=my-service
    key: API_KEY
    value: ${{ parameters.apiKey }}
    masked: true
    variableType: env_var
```

**Trigger a pipeline:**

```yaml
- id: trigger-pipeline
  name: Trigger Initial Pipeline
  action: gitlab:pipeline:trigger
  input:
    repoUrl: gitlab.com?owner=acme-corp&repo=my-service
    branch: main
```

## Tech Insights enables governance at scale through GitLab API data

[Tech Insights](https://roadie.io/product/tech-insights/) transforms ad-hoc governance (manual audits, spreadsheets of compliance) into continuous, automated checks surfaced directly in the developer portal. The system works through three layers: **data sources** (fact retrievers that call APIs), **checks** (boolean logic evaluating facts), and **scorecards** (collections of checks targeting entity subsets).

For GitLab integrations, common governance questions answered through the API include:

| Governance Check | GitLab API Endpoint | Data Type |
|------------------|---------------------|-----------|
| Repository has CODEOWNERS | `GET /projects/:id/repository/files/CODEOWNERS` | `boolean` |
| Default branch protected | `GET /projects/:id/protected_branches` | `boolean` |
| CI configuration exists | `GET /projects/:id/repository/files/.gitlab-ci.yml` | `boolean` |
| MR approval rules configured | `GET /projects/:id/approval_rules` | `boolean` |
| Project description set | `GET /projects/:id` → `description` field | `boolean` |
| Open vulnerability count | `GET /projects/:id/vulnerability_findings` | `number` |

Roadie's managed [Tech Insights](https://roadie.io/docs/tech-insights/introduction/) provides **100+ built-in data source types** and a UI for [defining checks and scorecards](https://roadie.io/docs/tech-insights/add-check/) without writing code. Scorecards can target entity subsets (e.g., "all production services must have CODEOWNERS and branch protection") and surface results as team-level rollups, historical trends, and operational review dashboards. The `read_api` scope is sufficient for all fact collection.

## Connecting Self-Managed GitLab (On-Prem)

Organizations running **self-managed GitLab behind a firewall** face a connectivity challenge: how does a SaaS portal reach an internal GitLab instance without exposing it to the internet? [Roadie's Broker](https://roadie.io/docs/integrations/broker/), based on Snyk's open-source broker, solves this with **outbound-only connections**.

The architecture consists of two components. The **Broker Client** is a Node.js application deployed inside the customer's infrastructure (via Docker, Helm chart, or npm CLI). It initiates an outbound WebSocket connection to the **Broker Server**, a tenant-specific endpoint hosted in Roadie's infrastructure. All traffic flows through this tunnel, Roadie never initiates inbound connections, and **no firewall ports need to be opened**.

Security is enforced through multiple layers. An `accept.json` configuration file on the client side provides **allowlist-based access control**, by default, Roadie has zero access to any internal APIs. Only explicitly permitted URL patterns and HTTP methods are proxied. Authentication tokens for internal GitLab remain in the customer's infrastructure and are never transmitted to Roadie. Additionally, the Broker Server restricts connections to customer-specified **IP CIDR ranges**, and all access is logged for audit.

A minimal Broker Client deployment for self-managed GitLab:

```bash
docker run \
  --env BROKER_TOKEN=gitlab-integration \
  --env BROKER_SERVER_URL=https://<tenant>.broker.roadie.so \
  -v $(pwd)/accept.json:/service/accept.json \
  roadiehq/broker
```

The corresponding `accept.json` restricts access to only the GitLab API paths Backstage needs:

```json
{
  "private": [
    {
      "//": "GitLab API access for catalog discovery and plugins",
      "method": "GET",
      "path": "/api/v4/*",
      "origin": "${GITLAB_INTERNAL_URL}",
      "auth": {
        "scheme": "token",
        "token": "${GITLAB_INTERNAL_TOKEN}"
      }
    }
  ],
  "public": [
    { "method": "GET", "path": "/healthcheck" }
  ]
}
```

Broker configuration is managed through Roadie's admin UI at `https://<tenant>.roadie.so/administration/settings/integrations/broker`, where admins set CIDR ranges and broker tokens.

## How Roadie compares to the alternatives for GitLab shops

**GitLab's native capabilities leave a significant gap.** GitLab offers CI/CD pipelines, project templates, and compliance frameworks, but no unified service catalog, no scorecard-based governance, no [docs-as-code portal](https://roadie.io/product/documentation/), and no cross-tool aggregation surface. GitLab's Service Desk is an ITSM ticketing system for external users, not a developer portal. GitLab's own [direction page](https://about.gitlab.com/direction/) explicitly identifies Backstage and Port as competitive solutions, tacitly acknowledging the gap it cannot fill until at least 2026.

**[Self-hosted Backstage](https://roadie.io/blog/the-true-cost-of-self-hosting-backstage/)** provides the same plugin ecosystem but demands a dedicated team for maintenance, upgrades, infrastructure management, and plugin curation. Real-world experience confirms that organizations routinely spend months reaching production and still struggle with adoption at scale. Roadie eliminates this burden: automatic monthly upgrades, pre-configured plugins (75+), no-code UI customization, and enterprise features like [RBAC](https://roadie.io/product/access-control/), usage analytics, and OpenSearch-powered catalog search that don't exist in open-source Backstage.

**Proprietary portals** (Cortex at ~\$65/user/month, Port with a free tier up to 15 users then $40/seat/month) offer polished UIs and built-in engineering intelligence, but carry significant lock-in risk with proprietary data models. Cortex provides strong DORA metrics and maturity scorecards but has no community plugin ecosystem and no TechDocs equivalent. Port offers maximum flexibility through custom "Blueprints" but lacks native documentation features and treats GitLab primarily as an action backend rather than a deep data source. Neither matches the depth of Backstage's GitLab plugin ecosystem, which includes discovery, org sync, CI/CD visualization, scaffolding, pipeline triggers, code owners display, MR statistics, and coverage reporting across **six actively maintained packages**.

Roadie sits at the intersection: the open-source extensibility and [GitLab integration](https://roadie.io/docs/integrations/gitlab/) depth of Backstage, with the operational simplicity of a managed SaaS, at roughly one-third the per-user cost of Cortex.

## Common pitfalls and production-hardening advice

Several failure modes recur in GitLab + Backstage deployments at scale. **Token expiration** is the most common, GitLab tokens expire silently (default max 365 days, extendable to 400 in GitLab 17.6+), causing catalog updates to stop without clear errors. Automate rotation via the GitLab API's `POST /groups/:id/access_tokens/:token_id/rotate` endpoint. **Entity naming collisions** break ingestion when two repos use identical `metadata.name` values; standardize naming conventions early and enforce them through scaffolder templates. **Quoted numeric IDs** trip up YAML parsing, `gitlab.com/project-id: '4521'` must be quoted, or YAML interprets it as a number and the annotation match fails.

For discovery at scale (500+ repos), **scope discovery to specific groups** rather than scanning the entire instance to reduce API calls, and **deploy webhook-driven updates** to eliminate polling overhead. Use [Software Templates](https://roadie.io/product/scaffolder/) to generate correct `catalog-info.yaml` files for new projects from day one, preventing the catalog drift that occurs when teams must retroactively add metadata to existing repos. Treat `catalog-info.yaml` as code, reviewed via merge requests, enforced by CI validation, and owned by the service team.

## Conclusion

The combination of Roadie and GitLab addresses a gap that GitLab itself won't fill until 2026 at the earliest. **Auto-discovery with regex-based group and project filtering** eliminates the manual registration burden across hundreds of repos. **[Scaffolder actions](https://roadie.io/backstage/scaffolder-actions/)** specific to GitLab automate project creation with built-in guardrails, CI configuration, branch protection, and catalog registration happen in a single self-service workflow. **[Tech Insights scorecards](https://roadie.io/product/tech-insights/)** transform governance from periodic audits into continuous, visible compliance tracking. And the **[Broker architecture](https://roadie.io/docs/integrations/broker/)** extends all of this to self-managed GitLab instances without any firewall changes, using outbound-only connections with allowlist-based access control.

The key technical insight is that [Backstage's](https://backstage.io) GitLab integration ecosystem is uniquely deep, six actively maintained packages covering discovery, org sync, CI/CD visualization, pipeline triggers, and scaffolding. [Roadie](https://roadie.io) wraps this ecosystem in a managed layer that eliminates the 3,12 engineer operational burden of self-hosting, adds enterprise features absent from open-source Backstage ([RBAC](https://roadie.io/product/access-control/), scorecards, no-code layout editing, AI capabilities), and avoids the proprietary lock-in of alternatives like Cortex and Port. For GitLab-centric organizations, it represents the fastest path from repository sprawl to a governed, self-service developer platform.

## Next Steps

Now that you understand how Roadie integrates with GitLab, here are practical next steps to get started:

- **[Start a free trial](https://roadie.io/free-trial/)** to connect your GitLab instance and see auto-discovery in action within minutes
- **[Explore the GitLab integration documentation](https://roadie.io/docs/integrations/gitlab/)** for detailed configuration instructions and advanced patterns
- **[Learn how to model your software catalog](https://roadie.io/docs/catalog/modeling-entities/)** to represent your system architecture properly with components, APIs, and dependencies
- **[Create your first Software Template](https://roadie.io/docs/scaffolder/writing-templates/)** to standardize how teams create new GitLab projects with pre-configured CI/CD and governance
- **[Set up Tech Insights checks](https://roadie.io/docs/tech-insights/add-check/)** to monitor engineering standards like CODEOWNERS files and branch protection across your GitLab repositories
- **[Review customer success stories](https://roadie.io/case-studies/)** from other organizations using Roadie with GitLab to accelerate their platform engineering initiatives

---

### [Backstage Microservices Strategies: Taming Sprawl with a Service Catalog](https://roadie.io/blog/backstage-microservices-strategies.md)

When a 3 AM incident cascades through your 400-microservice architecture, the critical question isn't what's broken, it's who owns it. Without a centralized system of record, organizations inevitably accumulate "zombie services" - undocumented, unmaintained code that nobody claims until it fails catastrophically. [Backstage](https://roadie.io/backstage-spotify/), the CNCF-incubated developer portal created by Spotify, has emerged as the definitive solution for taming this complexity, streamlining incident response and drastically cutting the time required to onboard new engineers.

The stakes are substantial: the friction caused by tool sprawl and context switching acts as a massive tax on engineering velocity. For organizations with 50+ engineers already committed to microservices, the question isn't whether to implement a service catalog, it's how to do it effectively before complexity overwhelms capacity.

## The hidden cost of microservices at scale

Modern engineering organizations force developers to juggle a dizzying array of monitoring, CI/CD, and cloud infrastructure tools. This fragmentation forces constant context switching, breaking flow state and burning valuable engineering hours every week. When Expedia Group surveyed their [5,000+ developers managing 20,000 microservices](https://roadie.io/case-studies/expedia-group-backstage-mvp/), documentation discoverability emerged as their primary pain point - engineers were spending more time finding information than building features.

The ownership problem compounds over time. Without a system of record, teams accumulate what practitioners call "microservice graveyards", entire clusters of services where the original owners have departed and no one wants responsibility. At Spotify before Backstage, engineers described their workflow as ["rumor-driven development"](https://qeunit.com/blog/quality-engineering-productivity-at-spotify/), the only way to discover how something worked was asking colleagues who might remember.

Incident response suffers most acutely. FireHydrant's analysis of 50,000+ incidents found that when services have clear ownership attached, [mean time to resolution drops by 36%](https://firehydrant.com/blog/learn-from-50-000-incidents-with-the-first-incident-benchmark-report/). Motability was able to reduce the creation of new services [from 2 - 3 days to minutes](https://roadie.io/case-studies/motability-operations-case-study-a-modern-idp/) after implementing service catalog tooling that eliminated the "who owns this?" question during outages. The pattern is consistent: visibility into ownership and dependencies transforms incident response from frantic Slack archaeology into systematic problem-solving.

## Backstage as your microservices operating system

Backstage functions as an [internal developer portal](https://roadie.io/backstage-spotify/), a unified interface that aggregates service metadata, documentation, and operational tooling into a single searchable surface. Created by Spotify in 2016 and open-sourced in 2020, it now manages their 2,000+ backend services and 4,000+ data pipelines with contributions from over 60 internal teams. The CNCF accepted it as an Incubating project in March 2022, signaling enterprise-grade maturity. Created by Spotify in 2016 and open-sourced in 2020, it now manages their **[2,000+ backend services and 4,000+ data pipelines](https://backstage.io/blog/2020/03/16/announcing-backstage/)** with contributions from **over 60 internal teams**. The CNCF **[accepted it as an Incubating project](https://www.cncf.io/blog/2022/03/15/backstage-project-joins-the-cncf-incubator/)** in March 2022, signaling enterprise-grade maturity.

The [Software Catalog](https://roadie.io/product/catalog/) forms the foundation. Every service, API, library, and infrastructure resource gets registered with a `catalog-info.yaml` file that lives alongside the code:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: payments-service
  description: Handles payment processing for all checkout flows
  annotations:
    # Links this service to its PagerDuty on-call schedule
    pagerduty.com/service-id: P123ABC
    # Connects to the GitHub repository
    github.com/project-slug: acme/payments-service
spec:
  type: service
  lifecycle: production
  # Defines team ownership - answers "who owns this?"
  owner: payments-team
  # Groups service into larger business domain
  system: checkout
  # Declares what APIs this service provides
  providesApis:
    - payments-api
  # Declares dependencies on other resources
  dependsOn:
    - resource:default/payments-db
```

This declarative approach ensures metadata lives with code and flows through standard git workflows. The **owner** field answers the 3 AM question definitively. The **dependsOn** and **providesApis** fields create a navigable dependency graph. Annotations connect the service to operational tooling, PagerDuty, CI/CD pipelines, monitoring dashboards, creating what Backstage calls a "single pane of glass."

The [System Model](https://roadie.io/docs/catalog/modeling-entities/) introduces organizational hierarchy: **Domains** (business areas like Payments or Search) contain **Systems** (collections of components that form a product capability), which contain **Components** (individual services) and **APIs** (interface boundaries). This taxonomy maps directly to how engineering organizations structure teams and ownership, making catalog navigation intuitive rather than arbitrary.

## Golden Paths eliminate the copy-paste tax

Before Backstage, creating a new service at Spotify took [14 days of configuration, pipeline setup, and documentation. Afterward: less than 5 minutes](https://engineering.atspotify.com/2020/08/how-we-improved-developer-productivity-for-our-devops-teams). The difference is the **[Scaffolder](https://roadie.io/product/scaffolder/)**, Backstage's templating system that implements what Spotify calls ["Golden Paths"](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem).

A Golden Path is an opinionated, supported path to building something, a backend service, a data pipeline, a React application. Rather than starting from a copy-pasted template that's already drifted from current standards, engineers use Software Templates that generate services with current CI/CD configuration, security scanning, logging, and observability pre-wired:

```yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: spring-boot-service
  title: Spring Boot Microservice
  description: Create a production-ready Spring Boot service with CI/CD
spec:
  owner: platform-team
  type: service
  # Parameters define the form users fill out
  parameters:
    - title: Service Details
      required:
        - name
        - owner
      properties:
        name:
          type: string
          title: Service Name
          description: Lowercase with hyphens (e.g., user-auth-service)
        owner:
          type: string
          title: Owner
          description: Team that will own this service
          ui:field: OwnerPicker
  # Steps define what actions to execute
  steps:
    # Step 1: Fetch the template skeleton from a repository
    - id: template
      name: Fetch Template
      action: fetch:template
      input:
        url: ./skeleton
        values:
          name: ${{ parameters.name }}
          owner: ${{ parameters.owner }}

    # Step 2: Publish to GitHub and create repository
    - id: publish
      name: Publish to GitHub
      action: publish:github
      input:
        repoUrl: github.com?repo=${{ parameters.name }}&owner=acme
        description: ${{ parameters.description }}

    # Step 3: Register in Backstage catalog automatically
    - id: register
      name: Register Component
      action: catalog:register
      input:
        catalogInfoPath: /catalog-info.yaml
```

The philosophy matters: Golden Paths are **recommended, not mandated**. Engineers can deviate, but they lose platform team support. This balances standardization with autonomy, the platform provides the easy path, but doesn't constrain innovation. Spotify maintains [six Golden Paths](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem) spanning backend, frontend, data engineering, machine learning, and web development, each optimized for their specific discipline.

The productivity impact extends beyond service creation. Spotify measured new engineer [time to 10th pull request, dropping from 60+ days to 20 days](https://engineering.atspotify.com/2021/09/how-backstage-made-our-developers-more-effective-and-how-it-can-help-yours-too) after Backstage deployment. When every service follows consistent patterns, understanding one means understanding all.

## Dependency visualization reveals blast radius

The [Catalog Graph plugin](https://roadie.io/backstage/plugins/catalog-graph/) transforms the static catalog into an interactive dependency map. When planning an API deprecation or infrastructure migration, engineers can trace exactly which services consume an endpoint and who owns them. During incidents, the graph shows upstream dependencies that might be causing failures and downstream services that might be affected.

*Example dependency graph showing blast radius when payments-service changes*

Relationships are defined explicitly in [catalog metadata](https://roadie.io/docs/catalog/modeling-entities/) using `dependsOn`, `providesApis`, and `consumesApis` fields. Backstage automatically generates inverse relationships, if Service A declares it consumes API B, API B's page shows Service A as a consumer. This bidirectional visibility makes deprecation planning systematic: filter by API, identify all consumers, contact those teams, and track migration progress.

The blast radius analysis capability transforms change management. Before deploying infrastructure changes, engineers visualize what breaks if a database becomes unavailable or an API endpoint goes down. Migration wave planning becomes data-driven, identify server clusters where dependency chains can be broken cleanly, then sequence the migration accordingly.

## Tech Insights gamifies production readiness

Catalog completeness means nothing if the metadata is wrong. **[Tech Insights](https://roadie.io/product/tech-insights/)** (called Scorecards in some implementations) provides automated fact-checking that validates services against production readiness standards. The system operates on two concepts: **Facts** (data points collected from various sources) and **Checks** (rules that evaluate facts).

Common checks include [PagerDuty integration](https://roadie.io/backstage/plugins/pagerduty/) verification (ensuring on-call is configured), deprecated library detection, Node.js version compliance, and documentation completeness. Each check runs on a configurable schedule and produces a compliance score visible on service pages:

```yaml
# Example Tech Insights check configuration
techInsights:
  factChecker:
    checks:
      productionReadiness:
        type: json-rules-engine
        name: Production Readiness
        description: Ensures services meet production standards
        # Define which facts to collect
        factIds:
          - entityOwnershipFactRetriever
          - techdocsFactRetriever
          - pagerdutyFactRetriever
        # Define the rule logic
        rule:
          conditions:
            all:
              # Check 1: Must have a group owner (not individual)
              - fact: hasGroupOwner
                operator: equal
                value: true
              # Check 2: Must have TechDocs documentation
              - fact: hasTechDocs
                operator: equal
                value: true
              # Check 3: Must have PagerDuty integration
              - fact: hasPagerDuty
                operator: equal
                value: true
```

[Dexcom used automated checks](https://roadie.io/case-studies/dexcom-automating-catalog-completeness-backstage/) to drive catalog completeness from 60% to over 95%. [Baillie Gifford](https://roadie.io/blog/backstage-gets-quality-and-compliance-scorecards-with-roadie/), operating in the regulated financial services sector, uses scorecards to track security tool adoption across 250 developers, generating compliance reports that previously required days of manual assembly.

The gamification effect drives adoption organically. When teams see leaderboards showing their scorecard performance relative to peers, competitive dynamics motivate improvement without mandates. Engineering leaders report this ["soft governance" approach](https://roadie.io/blog/improving-and-measuring-developer-experience-with-backstage/) achieves better compliance than top-down enforcement while preserving team autonomy.

## Integration creates the unified dashboard

Backstage's plugin architecture enables what engineers call the **"single pane of glass"**, consolidated visibility across the entire operational stack. Over [200 plugins](https://roadie.io/backstage/plugins/) provide native integrations with common tooling.

The **[Kubernetes plugin](https://roadie.io/backstage/plugins/kubernetes/)** displays deployment status, pod health, and resource metrics directly on service pages. Engineers see crash logs aggregated from all pods, health indicators, and links to deeper investigation tools, without leaving Backstage or requiring kubectl access. The **[PagerDuty plugin](https://roadie.io/backstage/plugins/pagerduty/)** shows active incidents, on-call schedules, and allows triggering new incidents from service context. **[GitHub Actions](https://roadie.io/backstage/plugins/github-actions/)**, **[CircleCI](https://roadie.io/backstage/plugins/circle-ci/)**, and **[Jenkins](https://roadie.io/backstage/plugins/jenkins/)** plugins display build status, deployment history, and failure details.

API management uses the same catalog model. OpenAPI, AsyncAPI, and GraphQL specifications register as API entities with full interactive documentation, consumer/provider relationships, and lifecycle management. When API version 2 launches, teams identify v1 consumers directly from the catalog and coordinate deprecation timelines.

The integration pattern is consistent: annotate catalog entities with tool-specific identifiers, and plugins fetch relevant data on page load. A properly configured service page shows ownership, dependencies, [documentation](https://roadie.io/product/documentation/), build status, deployment health, active incidents, and on-call, everything needed to understand and operate the service from a single URL.

## Choosing between self-hosted and managed options

Self-hosted Backstage offers unlimited customization but demands significant investment: typically [2-3 dedicated FTEs](https://roadie.io/blog/backstage-how-much-does-it-really-cost/) with TypeScript/React expertise for initial buildout and ongoing maintenance. Organizations like [Paddle](https://roadie.io/case-studies/from-self-hosted-backstage-to-roadie/) ran self-hosted Backstage for four years before migrating to managed alternatives when the maintenance burden conflicted with driving adoption.

**[Roadie](https://roadie.io)** provides managed Backstage at approximately $20/user/month with same-day setup, [200+ pre-configured plugins](https://roadie.io/backstage/plugins/), and enterprise features like [RBAC](https://roadie.io/product/access-control/) included. The tradeoff is reduced customization compared to self-hosted, though standard catalog formats mean organizations can migrate later if needs evolve.

Proprietary alternatives like Cortex ($65-69/user/month), OpsLevel, and Port offer differentiated approaches. Cortex emphasizes AI-powered service discovery and executive reporting. OpsLevel prioritizes fast deployment, 30-45 days typical, with automated catalog maintenance. Port offers maximum customization through a no-code builder but requires significant configuration investment.

For organizations with 50-100 engineers, managed solutions typically deliver faster time-to-value. Above 500 engineers with dedicated platform teams, self-hosted Backstage becomes economically viable if TypeScript expertise exists. Regulated industries should evaluate on-premises options alongside [Roadie's self-hosted offering](https://roadie.io/blog/roadie-local-self-hosted-backstage-ready-in-minutes/).

## Starting your service catalog journey

Successful implementations follow a consistent pattern: start with the **[software catalog](https://roadie.io/product/catalog/)** before adding complexity. Import users and teams first so ownership fields work immediately. Choose early-adopter teams willing to contribute catalog metadata, then expand systematically. Platform teams at Expedia [put 850+ engineers through Backstage-based bootcamp](https://roadie.io/blog/3-strategies-for-a-complete-software-catalog/#:~:text=Expedia%20Group%20put%20850%2B%20engineers%20through%20their%20Backstage%20based%20bootcamp%20in%202022.) in their first year, treating adoption as a change management initiative rather than a technology deployment.

Catalog completeness matters more than feature breadth initially. Contentful [achieved 90% metadata coverage within one year](https://roadie.io/case-studies/maintaining-velocity-through-hypergrowth-contentful/) by making Scaffolder the default service creation path, new services entered the catalog automatically, while existing services received incremental metadata through team contributions.

Measure what matters: **time to 10th PR** for onboarding velocity, **MTTR** for incident response improvement, and **catalog completeness** for adoption tracking. [Spotify's Pia Nilsson captured the business case succinctly](https://engineering.atspotify.com/2021/09/how-backstage-made-our-developers-more-effective-and-how-it-can-help-yours-too): "If you have numbers like that in your organization, it's easy to get buy-in for investments in developer experience."

The microservices complexity that created the 3 AM ownership problem also created the opportunity for systematic improvement. Backstage provides the framework; your implementation provides the value. Organizations that treat their [service catalog](https://roadie.io/docs/catalog/modeling-entities/) as a product, with dedicated ownership, user feedback loops, and continuous improvement, consistently report the productivity gains that justify investment. Those that deploy and forget find another unused tool in an already crowded landscape.

The choice isn't whether complexity will be managed, it's whether you'll manage it systematically before it manages you.

## Next Steps

Ready to implement Backstage in your organization? Here are resources to help you get started:

- **[Explore Roadie's Catalog](https://roadie.io/product/catalog/)** - See how Roadie's managed Backstage platform can help you organize your microservices architecture with automated discoverability and ownership tracking.

- **[Learn About the Scaffolder](https://roadie.io/product/scaffolder/)** - Discover how Software Templates and Golden Paths can standardize service creation and reduce onboarding time from weeks to minutes.

- **[Read Implementation Case Studies](https://roadie.io/case-studies/)** - Learn from companies like Expedia Group, Dexcom, and Contentful who have successfully deployed Backstage at scale.

- **[Compare Deployment Options](https://roadie.io/blog/the-true-cost-of-self-hosting-backstage/)** - Download the whitepaper comparing managed versus self-hosted Backstage to determine the best approach for your organization.

- **[Book a Demo](https://roadie.io/request-demo/)** - See Roadie in action. Request a personalized demo to discover how managed Backstage can tame your microservices sprawl with same-day setup and enterprise-grade security.

---

### [Creating Backstage EntityProviders at Runtime](https://roadie.io/blog/creating-backstage-entityproviders-at-runtime.md)

Backstage's catalog is the heart of your developer portal. EntityProviders are the mechanism by which data flows into it—they connect to external systems, fetch entity data, and push it to the catalog.

Typically, EntityProviders are registered at application startup via the `catalogProcessingExtensionPoint`. Once the backend initializes, the set of providers is fixed. But what happens when you need to dynamically create new sources of catalog data without redeploying?

Consider these scenarios:

- A multi-tenant platform where each tenant needs isolated entity management
- User-defined integrations that pull data from custom sources
- Dynamic data pipelines that generate catalog entities on-demand
- Self-service onboarding where teams register their own data sources

Backstage doesn't natively support registering EntityProviders after startup. This post explains how to solve this with a provider pooling pattern.

## The Challenge

The `EntityProviderConnection` that allows emitting entities is established once at startup when providers are registered. After initialization, you cannot add new providers—any attempt to call `addEntityProvider` after the catalog has started will fail.

## The Solution: Provider Pooling

Instead of fighting Backstage's architecture, work with it. The key insight: register a pool of providers at startup, then dynamically assign them to consumers at runtime.

```
┌─────────────────────────────────────────────────────────────┐
│                    Backend Startup                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  1. Create pool of N idle EntityProviders            │   │
│  │  2. Register all with catalogProcessingExtensionPoint│   │
│  │  3. Restore any persisted assignments from database  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                  ProviderRegistryService                    │
│  ┌────────────────────────────────────────────────────┐     │
│  │  getProviderFor(id) → assigns idle provider        │     │
│  │  releaseProvider(id) → clears entities, returns    │     │
│  └────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
    Consumer A            Consumer B            Consumer C
    (provider-0)          (provider-1)          (provider-2)
```

## The Pooled EntityProvider

Extend the standard `EntityProvider` with assignment tracking and the ability to clear entities:

```typescript
interface PooledEntityProvider extends EntityProvider {
  assignTo(id: string): void;
  clearAssignment(): void;
  clearEntities(): Promise<void>;
  updateEntities(entities: Entity[]): Promise<void>;
}
```

The key method is `clearEntities`—emitting an empty full mutation removes all entities that provider previously managed:

```typescript
async clearEntities(): Promise<void> {
  await this.connection?.applyMutation({
    type: 'full',
    entities: [],
  });
}
```

## The Registry Service

The registry manages the pool, handling assignment and release:

```typescript
interface ProviderRegistryService {
  getProviderFor(id: string): Promise<PooledEntityProvider>;
  releaseProvider(id: string): Promise<void>;
  getAllProviders(): PooledEntityProvider[];
}
```

When a consumer requests a provider, the registry either returns an existing assignment or finds an available provider from the pool and persists the new assignment.

When a provider is released, the registry clears its entities, removes the assignment, and returns it to the pool.

## Catalog Registration

Register all pooled providers at startup via a backend module:

```typescript
const providerRegistryCatalogModule = createBackendModule({
  pluginId: 'catalog',
  moduleId: 'provider-registry',
  register(module) {
    module.registerInit({
      deps: {
        catalog: catalogProcessingExtensionPoint,
        registry: providerRegistryServiceRef,
      },
      async init({ catalog, registry }) {
        for (const provider of registry.getAllProviders()) {
          catalog.addEntityProvider(provider);
        }
      },
    });
  },
});
```

## Persistence

Store assignments in a database table so they survive restarts. This ensures the same consumer gets the same provider ID, maintaining entity ownership continuity.

## Usage

```typescript
// Acquire a provider
const provider = await registry.getProviderFor('my-integration-123');

// Emit entities
await provider.updateEntities(entities);

// When done, release (clears entities and returns provider to pool)
await registry.releaseProvider('my-integration-123');
```

## Trade-offs

- **Memory overhead** — Pre-allocated providers consume memory, though instances are lightweight
- **Fixed capacity** — Pool exhaustion causes failures; size appropriately for your workload
- **Provider ID stability** — Assignments must persist to maintain entity ownership across restarts

## Conclusion

By pre-registering a pool of EntityProviders and dynamically assigning them at runtime, you can achieve flexible, dynamic entity management without modifying Backstage's core architecture. This pattern works for multi-tenancy, user-defined integrations, or any scenario requiring runtime control over catalog data sources.

---

### [The True Cost of Self-Hosting Backstage: A Build vs. Buy Analysis for Engineering Leaders](https://roadie.io/blog/the-true-cost-of-self-hosting-backstage.md)

Your platform team is fielding 30 Slack messages a day. "Who owns the payment service?" "How do I get an S3 bucket?" "Does virus scanning exist in our environment?"

Someone suggests [Backstage](https://roadie.io/backstage-spotify/). You look at the README, see it's open source, and think you'll just spin it up.

Six months later, you've burned through your platform team's roadmap, your [catalog](https://roadie.io/product/catalog/) is half-populated, and developers are still opening JIRA tickets for everything.

At my previous company, we built an internal developer portal from scratch. The bill ran into the millions. [That experience taught me](https://roadie.io/blog/from-a-spreadsheet-and-a-usd2m-bill-why-we-built-roadie/) that every engineering organization over 100 people eventually needs this infrastructure. But it also showed me how expensive it is to build and maintain. Even with AI coding agents to help with development, there’s a thousand small decisions to make about business logic.

Now, as CEO of Roadie, I talk to engineering leaders every week who are making this build vs. buy decision. Most underestimate what self-hosting Backstage actually costs. Not just in dollars, but in team capacity and time to value.

Here's what the decision really looks like.

## The Problem You're Actually Solving

The developer portal problem starts small. You're managing 50 services across 30 teams. Someone asks which services depend on the auth API. You don't have a good answer.

Another team needs virus scanning. You think it exists somewhere, but you're not sure.

So you make a spreadsheet. Service name, owner, what it does. Problem solved.

This works for about three weeks. Then nobody updates the spreadsheet. It's out of date. People stop trusting it.

This is the discoverability problem. At 10 engineers, you just shout across the office. At 100+ engineers, that breaks down completely. You need a [software catalog](https://roadie.io/product/catalog/) that actually stays current.

But discoverability is just the first problem. You also hit:

**The self-service bottleneck**: A mobile developer needs an S3 bucket. They don't know Terraform. They open a JIRA ticket. Your platform team gets to it in two weeks. The developer either waits or bypasses your platform entirely and creates shadow IT.

**The governance gap**: Your security team needs to verify every service has proper on-call setup. Your compliance team wants to check access controls. You need automated checks against your entire software catalog, not manual audits.

These three problems drive every developer portal evaluation. The question isn't whether you need a solution. The question is whether you build it or buy it.

## What Backstage Actually Gives You

[Backstage](https://roadie.io/backstage-spotify/) is not a developer portal. It's a framework for building one.

This distinction matters. When Spotify open sourced Backstage in 2020, they released their toolkit for building developer portals, not a turnkey product. You get a collection of TypeScript libraries and React components. You have to assemble them into something useful.

This creates immediate friction for most platform teams:

**You need TypeScript expertise**. Most platform teams work in Go, Python, and YAML. Web development is a different skillset than infrastructure engineering. You either hire TypeScript developers or retrain your existing team.

**You're building, not configuring**. Out of the box, Backstage gives you basic catalog functionality. It doesn't give you [role-based access control](https://roadie.io/product/access-control/). It doesn't give you production-grade search (it runs on Postgres full-text search). It doesn't give you most enterprise features. You build those.

**You're maintaining a web application**. Backstage releases a new version every couple of weeks. Each upgrade can break your plugins. Each new integration requires custom TypeScript code. This is ongoing work, not a one-time project.

## The Real Cost: Team Capacity

When we surveyed the Backstage community this year, organizations that reported being happy with their self-hosted deployment had at least three dedicated engineers. Some teams were as large as 12 people.

Let me translate that into budget terms. Three mid-level engineers cost around \$450,000 per year in salary, benefits, and overhead. That's the minimum for a successful deployment.

But the real cost is what those engineers aren't doing.

**Time to production: 6-12 months**. You're not launching next sprint. You're building the catalog model, integrating CI/CD tools, setting up authentication, configuring plugins, and training teams. The organizations we talk to consistently report 6-12 months before they had something teams would actually use.

**Opportunity cost**. Those three engineers aren't improving your CI/CD pipeline. They're not hardening security. They're not building platform capabilities that differentiate your business. They're maintaining a developer portal.

**Missing features you have to build**. Need [RBAC](https://roadie.io/product/access-control/) so your security services aren't visible to everyone? You're building that. Want better search? You're integrating Elasticsearch. Want [API documentation](https://roadie.io/product/documentation/)? You're configuring and maintaining that integration.

[The actual costs break down](https://roadie.io/blog/backstage-how-much-does-it-really-cost/) into several categories:

- 3 engineers minimum at \$150k loaded cost each = \$450,000/year
- 9 months to production at 60% team efficiency = ~\$200,000 in delayed value
- Ongoing maintenance and feature development
- TypeScript training or new hires

First year total exceeds \$800,000. Every year after that is still \$450,000 minimum, assuming no team growth.

And you still haven't built all the features you need.

## When Building Makes Sense

Self-hosting Backstage gives you something valuable: control.

If you have unique requirements that no vendor can handle, being able to modify every line of code matters. If you're integrating with complex legacy systems, having full access to the source code can be critical.

You also get the Backstage ecosystem. The community is active. New [plugins](https://roadie.io/backstage/plugins/) appear regularly. If you need an integration with a specific tool, someone in the community might have already built it.

Some engineering leaders prefer ownership for critical infrastructure. They don't want vendor dependencies. They want the source code running in their environment.

These are legitimate reasons to self-host. But they need to justify the cost.

**Build if:**

- You have genuinely unique requirements no vendor can handle
- You already have a team with TypeScript expertise who wants to own this
- You're large enough (500+ engineers) that control benefits outweigh costs
- You have specific security requirements that mandate on-premises deployment
- Your platform team has capacity to spare

**Don't build if:**

- Your platform team is already stretched thin
- You want to launch in weeks, not months
- You need enterprise features without building them
- You'd rather focus engineering resources on your actual platform

The key question: What do you want your platform team working on? If the answer is "building platform capabilities that make our engineering organization more effective," you probably shouldn't be maintaining a developer portal.

## The Managed Alternative

When we built [Roadie](https://roadie.io/), the goal was straightforward: give you Backstage without the team overhead.

Here's what that means:

**Day one deployment**. You connect your GitHub organization. Your services start populating. No six-month buildout. No TypeScript work. You're [configuring, not coding](https://roadie.io/docs/getting-started/overview/).

**Enterprise features included**. [RBAC](https://roadie.io/product/access-control/), production-grade search, authentication integrations. The pieces you'd have to build yourself are already there, built from feedback across hundreds of deployments.

**Automatic upgrades**. When Backstage releases a new version, we test it, validate it, and roll it out. You don't manage the upgrade cycle. You don't deal with breaking changes.

**No TypeScript team required**. You use a web UI to configure Backstage. Your platform team stays focused on platform work.

The financial calculation is simple. Managed Backstage costs a fraction of a three-engineer team. But the more important comparison is what your platform team accomplishes.

Would you rather have three engineers maintaining Backstage, or three engineers improving your CI/CD pipeline and building platform capabilities?

## The Hybrid Approach

This is Roadie's actual positioning: the hybrid model.

Proprietary developer portals lock you into their data model. If they don't support your integration, you're stuck. If they sunset a feature, you adapt. You have no control.

Self-hosted Backstage gives you control but requires a dedicated team and significant TypeScript expertise.

[Managed Backstage](https://roadie.io/backstage-comparison/) sits in the middle:

- The flexibility of Backstage's open source ecosystem
- Day-one usability and enterprise features
- No team overhead, no TypeScript requirement, no year-long buildout

You're not locked into a proprietary platform. If you decide you want to self-host later, you can. The catalog format is standard Backstage. Your [plugins](https://roadie.io/backstage/plugins/) are standard Backstage.

But you also don't need to staff a team just to keep the portal running.

## The Path Few Consider

Most engineering leaders frame this as "self-host Backstage vs. buy a proprietary portal." But there's a third option: start managed, migrate to self-hosted later if needed.

You can validate that Backstage solves your problems without burning six months and half your platform team's capacity. Get your [catalog](https://roadie.io/docs/getting-started/model-software/) populated. Get teams using it. Prove the value.

Then, if you decide you need more control, migrate to self-hosted. The data model is identical. The plugins are the same. You're not locked in.

Several of our [customers](https://roadie.io/case-studies/) took exactly this path in reverse. They self-hosted Backstage, realized it was consuming their platform team, and [migrated to Roadie](https://roadie.io/case-studies/why-celonis-switched-from-selfhosted-backstage-to-roadie/) to free up those engineers for higher-value work.

## Making the Decision

Here's the framework I use when talking to engineering leaders:

**Start with team capacity**. Can your platform team absorb a year-long project plus ongoing maintenance? If not, you're not really choosing to build. You're choosing to delay.

**Calculate opportunity cost**. What else could three engineers accomplish in a year? New CI/CD capabilities? Better security tooling? Improved developer experience? Is maintaining a developer portal more valuable than those alternatives?

**Consider your timeline**. Do you need this solved in weeks or months? If you need it fast, you're buying. If you have a year to spare, you might build.

**Evaluate your requirements**. Do you have genuinely unique needs, or do you just need a software catalog with good search, RBAC, and common integrations? Most organizations overestimate how unique their requirements actually are.

**Think about your team's preferences**. Does your platform team want to work on TypeScript and React components, or do they want to work on platform capabilities? Forcing engineers to maintain infrastructure they don't want to maintain leads to burnout and turnover.

The honest answer for most organizations under 500 engineers is that building doesn't make financial sense. You can get Backstage with all the ecosystem benefits for a fraction of the cost, with immediate deployment, and without tying up your platform team.

## What This Really Comes Down To

The question isn't whether you need a developer portal. If you're managing 50+ services across 30+ teams, you probably do.

The question is whether building and maintaining that portal is the best use of your platform engineering resources.

For most engineering leaders, the answer is no. Your platform team should be [improving your platform](https://roadie.io/blog/what-to-think-about-when-youre-thinking-about-an-idp/), not maintaining a web application.

That's why Roadie exists. You get Backstage without the team overhead. You get the open source ecosystem without the TypeScript requirement. You get day-one deployment without the year-long buildout.

And your platform team gets to focus on the work that actually differentiates your business.

The build vs. buy decision isn't really about cost. It's about what you want your team working on. Choose accordingly.

## Next Steps

If you're evaluating Backstage for your organization, here are concrete next steps to help you move forward:

**Explore Backstage capabilities**: Review our [comprehensive guide to Backstage](https://roadie.io/backstage-spotify/) to understand what's possible with the platform and how organizations are using it today.

**See how others decided**: Read [case studies from engineering teams](https://roadie.io/case-studies/) who've made the build vs. buy decision. Learn from [Celonis's experience migrating from self-hosted to managed](https://roadie.io/case-studies/why-celonis-switched-from-selfhosted-backstage-to-roadie/) and how [Contentful maintained velocity through hypergrowth](https://roadie.io/case-studies/maintaining-velocity-through-hypergrowth-contentful/).

**Understand the full cost picture**: Dive deeper into [the complete cost breakdown of self-hosting Backstage](https://roadie.io/blog/backstage-how-much-does-it-really-cost/) to validate your budget estimates.

**Try it yourself**: [Request a demo](https://roadie.io/request-demo/) to see how managed Backstage works, or [start a free trial](https://roadie.io/free-trial/) to experience Roadie firsthand and get your catalog populated in hours, not months.

**Compare your options**: Review [Backstage alternatives and approaches](https://roadie.io/blog/backstage-alternatives/) to ensure you're making an informed decision about your developer portal strategy.

---

### [Self-Hosting Backstage: The Real To-Do List](https://roadie.io/blog/self-hosting-backstage-the-real-to-do-list.md)

Considering Backstage? Great! Want to self-host it? Sure - lots of organizations do. In fact, in the [State of Backstage 2025 survey](https://roadie.io/blog/the-2025-state-of-backstage-report/), 91% said they self-host, versus 9% on managed platforms. Just because loads of people do it doesn’t mean it’s easy, though. The real question is what it takes to run Backstage as a production platform once you have thousands of engineers, hundreds of teams, and a catalog that keeps growing. The gap between “we stood it up” and “engineers rely on it every day” is where most of the cost and complexity lives.

We’ve spent the last five years running Backstage in production across dozens of organizations, and building the missing pieces that make it reliable at scale: performance work, background job isolation, governance and scorecards, RBAC, search, TechDocs operations, plugin maintenance, and the unglamorous reality of constant upgrades. If you want to know what’s the real cost and effort involved in standing up a Backstage instance, we’re uniquely positioned to tell you.

This post is a roadmap of that work. If you only have a minute, the table below is the executive summary detailing what will probably need to be done. Think of it as your ultimate to-do list for self-hosting Backstage.

And as always, many of these learnings and insights are captured in this year’s [State of Backstage Report](https://roadie.io/blog/the-2025-state-of-backstage-report/), where you can hear firsthand from self-hosted users around their Backstage journey.

## Executive summary

*Some assumptions about these numbers:*

- You’re aiming for a production-grade portal, not a demo.
- You expect meaningful adoption across the organization, not a niche tool used by one team.
- You’ll run a non-trivial plugin surface (CI, SCM, cloud, observability, security, incident tooling).
- Effort is shown as engineering weeks, where one engineering week equals 5 working days of one engineer, and roughly 40 hours.
- Obviously ranges here vary by organizational complexity, catalog size, and how strict your governance/security requirements are.

| **Initiative** | What you’re building | Effort (engineering weeks) |
| --- | --- | --- |
| Performance and scalability | Server-side catalog pagination, worker isolation, stability profiling, general optimization, scaffolder scaling | 16-24 weeks (plus ongoing maintenance). This depends substantially on the size of your catalog - this will be on the higher side for larger catalogs with 50,000+ entities |
| Catalog customization and data modeling | Configurable catalog UI, decorators/fragments to enrich without PRs, custom kinds/schema, refresh triggers, completeness tracking | 18-30 weeks depending on just how much customization is necessary to meet your requirements. Plus ongoing time required for maintenance |
| Search | Operate a real search backend (OpenSearch), indexers and relevance tuning, UX refinements, AI search tie-in | 8-12 weeks for search, plus another 8-12 weeks for AI search if you want a real assistant experience |
| Plugins and integrations | Ongoing plugin lifecycle, auth quirks, API drift, version compatibility | 0.5 to 2 weeks per plugin to productionize (auth, permissions, UI polish, support), plus a few hours per upgrade cycle |
| Tech Insights and scorecards | Facts ingestion, rule engine, no-code builder UI, built-in checks library, aggregation/history/reporting | ~100 weeks (roughly 6 months for a team of 4 engineers) to build Tech Insights |
| RBAC, security and governance | Role mapping, policy engine, admin UI, token issuance/revocation tied to RBAC | ~50 weeks (6 months for a team of 2 engineers) to build RBAC |
| TechDocs operations | Hybrid build modes, webhooks/rebuilds, curated MkDocs environment, performance tuning | 2 weeks for initial setup, ongoing maintenance to address any issues |
| Developer experience polish | Catalog UI QoL, homepage improvements, admin UX | Ongoing commitment that can very easily be a full-time job for a platform engineer |
| AI and MCP | AI assistant over catalog/docs, embeddings/vector store, permission-aware retrieval, MCP servers | 12- 24 weeks, with a significant ongoing investment to continually implement and improve |
| Upgrades and release engineering | Test suites across plugin surface, staged rollouts, triage and rollback processes | Ongoing investment of a few hours a week, with significant  effort of 5 - 20 engineering days around major Backstage releases |

The rest of this post breaks down each initiative, why it exists, what tends to go wrong in real usage, and the type of engineering work required to make it solid. If you’re a platform engineer, treat it like a checklist. If you’re an engineering leader, treat it like a way to pressure-test the real cost and opportunity cost of self-hosting.

## 1. Performance and scalability: keeping Backstage fast at 200k entities

Backstage starts out fast enough. It becomes difficult to keep it performant and responsive at scale.

Once you have tens or hundreds of thousands of entities, TechDocs for most services, scorecards, search indexing, CI integrations and so on, the default architecture begins to strain. With several customers with north of 200,000 entities in their catalogs, this is where we had to invest heavily.

Some of the larger pieces you should plan for:

### Server side catalog pagination

Vanilla Backstage loads the full result set for catalog pages, then filters on the frontend. That is fine for a few hundred entities. At hundreds of thousands, it become very slow.

We rewired the catalog list to use server side pagination and filtering. That meant changing how queries are constructed, how counts are calculated, and how the UI behaves when it only has a slice of the data. The result is dramatically lower load times for big catalogs. Reproducing that means touching both backend and frontend, and being ready to debug subtle performance and UX regressions when filters combine in unexpected ways.

Factor on at least 200 engineering hours to implement server side catalog pagination. This accounts for a backend refactor, restructuring the frontend table, compatibility handling for pagination edge cases, and API shape changes.

*Catalog pagination becomes an absolute necessity as the size of the catalog increases*

### Background job isolation

In open source Backstage, long running tasks often share a process with the user facing API. TechDocs builds, scaffolder jobs, scorecard computations, data ingestions and so on can all compete with login and catalog requests.

We pulled the heavy backend work out into separate worker containers. That improves stability and reduces resource contention, but it also means you now have to design and operate a small distributed system: one set of pods serving interactive traffic, another running asynchronous jobs, plus the plumbing to schedule, observe, and scale those workers safely.

Effort wise, a reasonable baseline is one to two days for the Backstage specific configuration and app construction, plus at least a few more days for the infrastructure work. All told, expect a small team to spend a week or two on this.

### Deep stability work

On the way to running multi tenant Backstage, we have spent a lot of time on the unglamorous work: memory leaks, readiness probes that misreport their status, and so on. Examples include fixing global arrays that never stopped growing, ensuring in memory caches actually drop expired items, and tuning Kubernetes probes so that pods are only marked ready when they really are.

*Tenant performance is meticulously logged and continually optimized*

These are the bugs that only show up after weeks of production traffic. If you self host, you need to plan for that kind of ongoing investigation with profiling, heap dumps and careful rollouts.

Factor in at least a couple of engineering weeks time off the bat to ensuring all your infrastructure is properly profiled and optimized, and several hours per month of monitoring to ensure everything is running smoothly.  

### Scaffolder scalability: popularity changes the problem

The Backstage Scaffolder is easy to run when usage is low, but once it becomes the default way engineers create services and automate workflows, it turns into a workflow you need to manage. Scaling isn’t just “add more pods” - it’s making sure you can absorb bursts without the rest of Backstage slowing down, separating template execution from other traffic, and having enough visibility to support it day to day with an understanding what’s running, what’s queued, what’s stuck, what’s failing, and why.

*The Scaffolder as a production workflow engine*

### Preloading, caching and endless optimizations, frontend and back

On the frontend we made numerous changes to how Backstage handles content. This includes optimizing API calls, ruthlessly culling what is loaded, and optimizing how we serve static content such as TechDocs.

In the backend we added visibility and controls around the job scheduler, because once your tooling grows and you’ve got multiple ingestion refreshes, scorecard jobs and TechDocs builds, it is easy to end up with invisible backlogs that impact performance.

*Roadie’s scheduler view showing background jobs across the instance*

None of these changes is individually complex, but together they form the difference between “Backstage mostly works” and “Backstage feels fast even on a Monday morning with thousands of users.”

It’s challenging to reliably estimate this effort; but even at the lower end for a smaller catalog expect to sink multiple months worth of engineering effort into optimization for Backstage. For us, obviously with multiple Enterprise customers that makes sense to invest the time - for an individual team it’s a challenging cost-benefit discussion to make work.

## 2. Catalog customization and data modeling

Backstage’s catalog is designed to be endless flexible and extensible, but in practice organizations quickly run into the limits of pure YAML in git.

Over time we have had to turn the catalog into something that behaves more like a product, both in terms of how it’s populated, and how it’s used and consumed by users and services.

### Custom columns, tabs and views

Platform teams want to surface critical metadata directly in the catalog table: criticality, lifecycle, tier, compliance score, owner health, and so on. We built configurable catalog columns that can display arbitrary metadata, numeric scales, links and even scorecard results, along with the ability for users to save filtered views as tabs.

Replicating this means building a more dynamic catalog UI and a way to define, persist and share those views. The alternative is endless “export to CSV and slice in a spreadsheet” workflows, which ultimately defeat the purpose of an IDP.

This was one of the most useful features we’ve built for Roadie, and there’s hundreds of hours of engineering effort behind the work.

*Custom tabs in action -  a must have for the more mature catalog*

### Decorators and “glue of truth”

Real organizations almost never have a single source of truth. Teams want to combine data from git, SSO, HR systems, cloud providers and ad hoc spreadsheets.

We built the Decorator as an entity decorator, and the Fragments API, which allow extra metadata to be stored in Roadie’s database and merged into entities at runtime, without changing the YAML. That is the foundation for things like business ownership, cost centre tags, custom maturity ratings, and so on. The Decorator works in the UI, while the Fragments API achieves the same thing programmatically.

*Skip the YAML - decorate entities with metadata from within the Backstage UI*

If you self host, you will need your own answer for how to enrich entities from multiple systems without forcing every change through a pull request. What we’ve learned from experience is that trying to batch annotate entities via organization-wide PRs is unlikely to succeed, hence, empowering the platform teams to decorate these entities at the IDP level. Factor on at least two  months of engineering investment to make the data model changes, build the logic and UI elements.

### Repositories, products and custom kinds

Very quickly people want to catalogue more than just “services.” They want to represent repositories, shared libraries, products, data models, infrastructure resources and more.

We have added new kinds such as Repository and Product, plus guidance and tooling for extending the entity model safely. Doing this yourself means working with Backstage’s schema system, updating layouts and cards, and then thinking about how all of this will be queried and shown in search.

These are some of the more foundational and impactful changes, and are in the Backstage scheme of things, on the simpler side. Factor on 40-60 hours for the changes to the data model schema and building the custom processor.

*Richer kinds unlock richer relationships: the catalog graph is one way to visualize how services, repos, and products connect*

### Instant updates and completeness tracking

The catalog is a living thing, and it’s important it stays fresh. As usage grows, you will want more control over how your catalog is refreshed, in an idempotent way, from your underlying systems. We use webhooks and APIs from SCM systems to trigger catalog refreshes in near real time, and we track catalog completeness using scorecards that measure ownership, labels and other metadata.

A self hosted team will need some equivalent if you want to trust the catalog as a real time view of your software. Factor on a month or more to get this done.

## 3. Search: how people can actually find things

Search is one of the most visible parts of a developer portal. If it feels off, people give up quickly. Open source Backstage has gradually improved search, but we found that large organizations quickly needed more than the out-of-the-box search experience.

### A real search engine

We moved to OpenSearch for search, with analyzers that handle mixed case names, hyphenation, and partial matches. For example, engineers can type part of a service name, or a fragment of an API route, and still find what they need. This is not the case for out-of-the-box self-hosted Backstage.

That work required running and maintaining a search cluster, setting up indexers, and designing relevance rules. It also meant a pass over search UX, so that results are presented in a way people can actually work with. This can take anywhere from 2-3 months depending on the level of customization required.

### AI search

A recently addition, but a critical one - we now make available our MCP tooling to a built-in AI assistant in the Roadie UI. This allows engineers to ask natural language questions about their catalog and have the answers displayed in Roadie. A step change from regular search, and a similar order of magnitude in terms of engineering effort. The real investment here was in the addition of MCP tooling, but factor on a couple of weeks at least here.

*AI search uses the same MCP tooling to expose a richer, conversational search experience*

## 4. Plugins and integrations: owning the long tail

Backstage’s plugin model is its greatest strength and one of its sharper edges.

Most large organisations end up using a long list of plugins: Argo CD, AWS, Azure DevOps, GitLab, Jira, Datadog, Sentry, SonarQube, security scanners, incident tools and more. Each of those brings its own authentication quirks, rate limits, API changes and version compatibility issues.

Over the last five years we have:

- Maintained and updated dozens of plugins when Backstage core moved forward or vendor APIs changed
- Built new plugins such as AWS resource ingestion, Wiz security integration, LaunchDarkly enhancements, Shortcut integration and more
- Created a secure connectivity pattern with Snyk using an open source broker to reach on prem systems without opening inbound access

If you choose to self host, the integrations you rely on today will keep evolving. The work is less about “install plugin X once” and more about “own a small product surface for each plugin indefinitely.”

That is not a reason to avoid self hosting, but it is a cost you should be explicit about.

## 5. Tech Insights and scorecards: turning Backstage into a governance tool

Most organizations adopting Backstage eventually want more than a catalog. They want to use it to drive standards: security adoption, SLO coverage, migration progress, documentation quality, and so on.

Open source Tech Insights gives you some primitives, but it expects you to write a lot of the logic and UI yourself. We turned that into a full product, and it was a six-month engineering lift from a fairly substantially sized engineering team. Factor on at least the same for your own efforts to make Tech Insights into a fully-featured product. Here’s what we’ve built:

### A no code scorecard builder

Platform teams can define checks and scorecards in a UI. Under the hood, data is pulled from SCMs, CI, security tools and other sources, stored as facts, and evaluated regularly. We ship a large library of built in checks so that people do not start from a blank page.

### Aggregation, history and reporting

Results are rolled up by team and group, graphed over time, and shown either on a dedicated Scorecards section, and/or directly on entity pages and in the catalog. That lets you answer questions like “which team is lagging on SAST adoption” or “how has our documentation coverage changed over the last quarter.”

To replicate this yourself you will need to implement three things: a data ingestion layer, a rule engine, and a UI that surfaces all of it in Backstage. It is very doable, but it is also a multi month engineering effort.

*Tech Insights scorecards in action, turning standards into automated checks across your entire software catalog*

## 6. RBAC, security and governance: controlling who can do what

Once you have real adoption, permissions move from “nice to have” to “non negotiable.”

Backstage’s permission framework is flexible, but it does not ship with a full RBAC system out of the box. Building a full RBAC product (roles, admin UI, policy engine, tokens) is typically a six month effort for a small two-person team. We had to build:

### Fine grained roles and permission policies

We support custom roles, mapping from identity provider groups to roles, and a policy engine that can express rules like “owners of a service can edit it, others can only view” or “only this group can run these templates.” That is exposed through an admin UI rather than code.

### API tokens and service accounts

To allow automation and external tools such as MCP clients, we added API token support tied into the same permission system. That means designing token issuance and revocation flows, and making sure tokens are not a back door around your RBAC rules.

## 7. TechDocs: documentation without the pain

Docs like code is one of Backstage’s most attractive features, but it can be surprisingly hard to operate in anger.

Problems tend to show up over time: builds that are slow or flaky, large monorepos that generate huge docs sites, Markdown features that people expect but are not configured, and so on.

We addressed this with:

### Hybrid build modes

Teams can choose between on demand builds or CI based publishing to a shared bucket. For large or frequently accessed docs, CI publishing gives much better performance.

### Autodiscovery and webhooks

When a docs folder changes in git, webhooks trigger a rebuild in the background so that by the time someone opens the page, the new version is already there.

### A curated MkDocs environment

We ship a standard set of MkDocs plugins and extensions for diagrams, tabs, admonitions and monorepos. That saves teams from having to build their own MkDocs image and solve the compatibility problems that come with it.

None of this is conceptually complex, but if you skip it you can easily end up with TechDocs that are slow, unreliable, or underused.

*TechDocs pages rendered in Backstage, powered by MkDocs and a build pipeline running behind the scenes*

## 8. Developer experience improvements

Developers judge a portal by how it feels in day to day use.

A lot of our work has been on the small things: catalog table layout, sticky filters, configurable columns, a useful homepage, sensible defaults for layouts, certified templates, better error messages, and an admin area that is navigable when you have dozens of integrations.

On top of that we are experimenting with new ways to let teams extend the UI quickly, such as MDX based homepage cards that can fetch and present data without building a full plugin. The direction here is to give engineers “power tools” so they can shape the portal around their workflows.

If you self host, this is the kind of work that rarely makes it onto a roadmap, but that strongly influences whether people actually enjoy using Backstage.

*Homepage cards - a quick and easy way to expose information from internal and external APIs in Roadie*

## 9. AI and MCP: the next layer

Finally, there is AI.

We touched on this under search - having an AI assistant that can answer questions about your documentation and catalog, and we have implemented Model Context Protocol servers so that external AI tools can safely talk to Roadie’s APIs. That allows agents in editors to discover templates, understand APIs and query scorecards, all through Backstage as a system of record.

You do not need AI on day one of a self hosted journey. It is, however, part of where the ecosystem is going. If you want Backstage to be a first class participant in your AI tooling, you will likely need to invest in similar capabilities: embeddings, vector storage, permission aware retrieval, and APIs tailored for LLM clients.

## 10. Saving the best for last - upgrades

If there is one topic that consistently surprises teams adopting Backstage, it is the upgrade burden.

Standing up Backstage for the first time is the easy part. Keeping it running, stable, secure, and compatible with the fast-moving upstream project is where the long-term work lives. Backstage releases frequently. Plugins evolve independently. Breaking changes land often and sometimes without much warning. And because Backstage is a framework rather than a product, the blast radius of every change is potentially wide.

### **Backstage moves fast**

Backstage core typically publishes new releases every few weeks. These releases regularly include:

- Deprecations or removals of catalog processors or entity fields
- Changes to authentication flows and permission boundaries
- Scaffolder API changes
- Search backend rewrites
- Plugin architecture changes (backend plugin framework migration, for example)

If you fall behind, the upgrade path compounds. A one-version bump is manageable. A six-month gap can become a multi-week project.

### **Plugins evolve at their own cadence**

Each plugin (Datadog, Argo, GitHub, Jira, TechDocs, API Docs, AWS, Azure, Wiz, LaunchDarkly, and dozens more) sits on top of Backstage but is not coordinated with it. They evolve independently, and breaking changes in one can cascade across your installation.

A self-hosted team effectively ends up with a plugin garden, each with its own update cycle, bug behavior, API quirks, and upstream issues.

### **The systems we had to build to keep this sustainable**

After years of running Backstage in production, we realized that upgrades needed as much engineering investment as performance or catalog work. We ended up building test suites that run Roadie’s full plugin surface against new Backstage versions before anything reaches customers. This catches breakages early and reliably.

We also never upgrade every tenant or environment at once. Rollouts happen gradually, with internal test tenants and rollback paths if something unexpected happens.

When something does break (and it often does) we have documented processes for diagnosing plugin failures, dependency mismatches, deprecations, and migration regressions, and clear steps for rolling forward or back safely. There’s also the experience that comes from having done this for years across multiple versions - hard won experience that allows our team to quickly triage and resolve highly-specific Backstage issues.

These systems collectively represent hundreds of hours of engineering time. They exist because without them, upgrades would regularly break real customer portals.

### **The hidden cost: this work never ends**

This is the part people most often underestimate. Upgrades are not a one-time project. They are ongoing rent  Every new Backstage release, every new plugin version, every upstream API deprecation requires attention.

Self-hosting teams often start enthusiastically, then gradually slow down as the backlog of breaking changes grows. Eventually they end up frozen on an old version, unable to upgrade without major intervention.

### **Why this matters for your roadmap**

If you plan to self-host Backstage, you need to view upgrades as a primary, recurring body of work, not a background task. The cost lives in:

- Testing every combination of plugins and Backstage core on every upgrade
- Managing breaking changes across dozens of moving parts
- Keeping your team aware of upstream changes and migration guides
- Avoiding drift so upgrades remain tractable
- Making sure your internal plugins and catalog processors don’t fall behind
- Ensuring that upgrades don’t take down developer workflows

This is not a warning; it’s a reality. Many teams can absolutely do this. But you should plan for it with eyes open. If there is one lesson from the [State of Backstage](https://roadie.io/blog/the-2025-state-of-backstage-report/) report, it is this: upgrades are the number one pain point for self-hosters. Not performance. Not TechDocs. Not plugins. Upgrades.

## Bringing it together: a realistic roadmap

Taken together, the list above is long. That is the point.

Self hosting Backstage is not simply about standing up a Node process and pointing it at your git repos. It is about:

- Operating a complex web application with many background jobs and external dependencies
- Owning a growing set of plugins and integrations and keeping them healthy
- Deciding how you will model your organisation and software, and then enforcing and evolving that model (we provide extensive engagement and support here through a structured onboarding and ongoing Customer Success motion)
- Providing governance through scorecards and permissions, not slide decks and spreadsheets
- Smoothing the user experience enough that engineers actually want to use the portal
- Keeping up with upstream Backstage changes and broader trends such as AI
- Upgrades. Friction around keeping your Backstage instance up-to-date with the upstream upgrades is a major, major source of pain for self-hosters.

None of this is impossible. Many of our customers could build a lot of it themselves, or did, before migrating to Roadie. Hundreds or thousands of organizations are successfully hosting their own Backstage implementations.

The question is not “can you,” but “which pieces do you want to own, and how much time do you want to commit.” Every engineering hour spent on an upgrade, or an enhancement already offered by Roadie is an hour not spent on improving developer experience, or custom plugins that unlock real value for your internal users. It’s a question of opportunity cost.

Roadie is far more than a hosted wrapper for Backstage - we offer production-grade infrastructure and enhancements that address fundamental gaps in security, governance, performance and developer experience that organizations that want to self-host would inevitably need to replicate.

If you decide to continue your journey on self hosted Backstage, we hope this roadmap helps you plan that work with eyes open. And if you prefer to have someone else carry this complexity for you, that is the role Roadie continues to play: a production grade distribution of Backstage, shaped by years of learning across many organizations. Feel free to [request a demo](https://roadie.io/request-demo/) anytime.

---

### [The Three Big Problems Every Platform Engineering Team Must Solve](https://roadie.io/blog/the-three-big-problems-every-platform-engineering-team-must-solve.md)

I learned about platform engineering the hard way. At Workday, I was an infrastructure product manager building what was essentially a private AWS inside the company. We had virtualization platforms, logging systems, monitoring systems, the works.

Everything worked fine when we had 10 or 20 services. Then we hit 50. That's when people started asking questions we couldn't answer: What is all this stuff? Who owns which service? If something breaks at 2 AM, who do we call? How do we know everything is secure?

We tried a spreadsheet. It lasted about three months before it became hopelessly out of date. So we built a UI from scratch to list services, show where they were running, and let people create new services without going through us for everything.

That was 10 years ago. Today, this problem has a name, [internal developer portal](https://roadie.io/backstage-spotify/), and there's an entire market built around solving it. But after talking to hundreds of platform teams, I've found they all struggle with the same three fundamental problems.

## Problem 1: The Discoverability Crisis

The discoverability problem shows up when your organization crosses a threshold. At 10 engineers, everyone knows what everyone else is working on. At 100+ engineers, it's chaos.

Here's what this looks like: Your security team builds a virus scanning service. Your mobile developers need to scan files for viruses, but they don't know this service exists. In an enterprise, they can't just sign up for some random SaaS tool because of compliance requirements. So they open a Slack thread, ask around, wait for responses, schedule a meeting, and maybe get an answer in a week.

Meanwhile, your platform team is getting bombarded: "Do we have an API for X?" "Who owns service Y?" "Which services depend on this database?"

The discoverability problem has three common variations:

**Documentation sprawl**: Teams scatter docs across Confluence, GitHub wikis, Google Docs, and Notion. No one can find anything. You need to centralize documentation in a [software catalog](https://roadie.io/product/catalog/) where people can actually discover it.

**Dependency mapping**: You need to understand which services depend on each other. When you're planning to upgrade a database, you need to know what breaks. Without a dependency graph, you're operating blind.

**API discovery**: Different teams build APIs, but there's no central place to see what exists, what they do, or how to use them. You need a searchable catalog of API specs.

This problem scales exponentially. We don't work with companies under 50 engineers because they don't face this yet. Most of our customers have 100+ engineers. At that scale, you can't just shout across the office anymore.

## Problem 2: The Self-Service Bottleneck

Your platform team becomes a bottleneck. Developers want to get things done without opening a JIRA ticket and waiting days for someone to configure their network rules or provision an S3 bucket.

At most organizations, you're waiting days for basic requests. This creates two problems:

First, developers get frustrated and stop being productive. They're blocked on simple tasks that should take five minutes.

Second, they bypass your platform entirely. This is shadow IT. A mobile developer who doesn't know Terraform just goes into the AWS console and clicks "Create S3 Bucket" because they can't wait. Now you have untracked infrastructure that's not in your Terraform state, doesn't follow your naming conventions, and might not meet your security requirements.

The self-service problem shows up in two main ways:

**Project creation**: A developer wants to start a new service on your platform. They need a repo, CI/CD pipeline, monitoring, logging, and all your platform integrations. If they configure this manually, they'll get it wrong. You want to give them a template that sets everything up correctly in five minutes, a ["golden path"](https://roadie.io/product/scaffolder/).

**Infrastructure requests**: A developer needs an S3 bucket, a database, or network rules configured. They don't know Terraform and shouldn't have to learn it. You want to let them fill out a form that opens a templated pull request against your Terraform repository. Someone reviews it, merges it, and the infrastructure gets created. The request is tracked, the developer doesn't need specialized knowledge, and you maintain control.

Self-service doesn't mean "let developers do whatever they want." It means giving them fast, easy ways to do things the right way. You're creating guardrails, not removing them.

## Problem 3: The Governance Gap

You have hundreds of services running on your platform. You need to know they're secure, reliable, and following your best practices. But you have no single place to check.

Here's a concrete example: You use [Incident.io](https://incident.io/) for incident management. Every service should be registered in Incident.io with an on-call person assigned. How do you verify this? You could manually check each service, but that's impossible at scale. You could send a Slack message asking people to audit their services, but half won't respond.

The governance problem shows up in several ways:

**Security compliance**: You need to verify that all services are scanning dependencies for vulnerabilities, using approved authentication methods, and following your security policies. Without automated checks, you're relying on self-reporting.

**Reliability standards**: You need to know which services have proper monitoring, alerting, and on-call rotations. When an outage happens, you need to immediately know who to call.

**Best practices enforcement**: Your platform team has defined standards, code review requirements, test coverage thresholds, documentation expectations. You need to see which teams are falling behind so you can work with them to improve.

The governance problem is about visibility rolled up across your org chart. You want to ask: "Show me the director of engineering who has the most services failing our security checks." Then you can work with that director to improve things.

Some teams also want [DORA metrics](https://dora.dev/) (deployment frequency, lead time, change failure rate, mean time to recovery) visible in one place. This is harder than it sounds. One of the DORA metrics is deployment frequency, the more you deploy, the smaller your changes are, the less likely they cause issues. But what counts as a "deployment" when different teams use Argo CD, Netlify, and five other deployment tools? Some normalization has to happen before you can just look at a DORA metric. Teams aren't necessarily there yet, and they're expecting a bit of magic that isn't that simple.

The same applies to defining what counts as a "service." That's a hard question to answer, and it's one of the most important challenges when trying to get any developer portal working in your organization.

## Why This is Hard to Solve

These three problems, discoverability, self-service, and governance, all stem from the same root cause: you have a lot of software, and you need organized metadata about it.

At Workday, we spent a lot of money building a custom solution. When I left in 2020, I talked to other companies and found they'd all built similar things.

The problem is that building this from scratch takes a year and requires a dedicated team to maintain. You're essentially building a product inside your company.

In 2020, [Spotify open sourced Backstage](https://backstage.io/), which gave the world a framework for building developer portals. But Backstage isn't a ready-to-use portal, it's a set of TypeScript libraries you use to build your own portal. This creates new problems:

**Language barrier**: Platform teams typically work in Go, Python, or YAML. They don't know TypeScript, which is a web development language.

**Build time**: Because you're building from libraries, not deploying a container, it takes six months to a year to get Backstage into production.

**Team requirements**: We surveyed the Backstage community and found that teams who report being happy with self-hosted Backstage have at least three dedicated engineers. Large deployments have 12+ engineers working on Backstage full-time.

**Missing features**: Backstage doesn't include basic features like [role-based access control](https://roadie.io/product/access-control/) out of the box. The search runs on PostgreSQL full-text search, which is okay but not as good as Elasticsearch. Your search won't be great unless you manage an Elasticsearch cluster as well as your Backstage instance.

Getting Backstage takes a year and a team of five people. That's why the internal developer portal market exists.

## How Companies Choose Solutions

When people come to us, they're typically in one of three situations:

**They already have Backstage**: Someone stood it up at some point and people are using it. They're realizing it's a lot of effort and they don't want to staff that team of five people.

**They want Backstage specifically**: They want a developer portal, like the idea of Backstage, and don't want to be locked into a proprietary data model. They want to customize their solution because they have legacy tools they need to integrate. But they don't want to staff the team around it.

**They just want a developer portal**: They don't care if it's Backstage or not. In this case, it's more competitive between proprietary solutions and Backstage-based options.

For the first two groups, they're doing a [build versus buy evaluation](https://roadie.io/blog/backstage-how-much-does-it-really-cost/): how much will it cost us to build and maintain this versus how much will it cost to buy a managed solution?

For the third group, it's more of a feature comparison and proof-of-concept scoring across vendors.

## What You Actually Need

Solving these three problems requires a few key capabilities:

**A software catalog**: Your source of truth for what software exists, who owns it, and how it's configured. The catalog needs to integrate with your existing tools, your repos, your CI/CD, your cloud providers, so it stays up to date automatically.

**Self-service actions**: Your developers need a UI for common tasks that generates the right pull requests, kicks off the right workflows, and follows your standards. This keeps them moving fast without bypassing your platform.

**Automated scoring**: You need [automated checks](https://roadie.io/product/tech-insights/) that run against everything in your catalog and tell you what's not meeting your standards. This gives you the visibility to work with teams on improvements.

**Easy onboarding**: Getting services into the catalog can't require each team to manually register everything. You need [automated ingestion](https://roadie.io/docs/getting-started/autodiscovery/) that pulls metadata from your existing systems. This is table stakes, but it's an area where Backstage is weak compared to proprietary competitors.

The challenge is that every organization has a slightly different definition of what counts as a "service" or a "deployment" or a "team." You need a solution that's flexible enough to adapt to your organization while being opinionated enough to actually work.

## The Path Forward

These three problems, discoverability, self-service, and governance, get worse as your engineering organization grows. If you're at 100 engineers now, imagine what happens at 200 or 500. The chaos compounds.

You're not the first platform team to face these problems. Every company with more than 50 engineers hits them eventually. Software catalogs, self-service automation, and governance scoring aren't experimental anymore.

The decision you need to make is whether to [build or buy](https://roadie.io/backstage-comparison/). Building gives you complete control but requires significant investment. Buying gets you there faster but means accepting someone else's opinions about how things should work.

Whatever path you choose, the problems won't solve themselves. Your platform team is already overwhelmed with questions, your developers are already frustrated with bottlenecks, and your managers can't answer basic questions about what's running in production.

These problems only get worse with time. The earlier you address them, the easier they are to solve.

## Next Steps

If you're ready to address these platform engineering challenges, here are some practical next steps to consider:

**Evaluate Backstage for your organization**: Learn more about [what Backstage is and how it works](https://roadie.io/backstage-spotify/) to understand if it's the right foundation for your developer portal needs.

**See a developer portal in action**: [Request a demo of Roadie](https://roadie.io/request-demo/) to see how a managed Backstage solution can solve your discoverability, self-service, and governance problems without the overhead of building and maintaining it yourself.

**Calculate your total cost of ownership**: Use our guide on [how much Backstage really costs](https://roadie.io/blog/backstage-how-much-does-it-really-cost/) to compare the build versus buy decision for your specific situation.

**Learn from teams who've solved these problems**: Read our [case studies](https://roadie.io/case-studies/) to see how companies like Contentful, Celonis, and others tackled similar platform engineering challenges.

**Start with a free trial**: If you're ready to experiment, [try Roadie free](https://roadie.io/free-trial/) to get hands-on experience with a fully managed developer portal built on Backstage.

---

### [Platform Engineering in 2026: Why DIY Is Dead](https://roadie.io/blog/platform-engineering-in-2026-why-diy-is-dead.md)

The software industry loves a good pendulum swing. For decades, we watched as centralized IT teams controlled every aspect of infrastructure, then witnessed the dramatic DevOps revolution that pushed that responsibility directly onto developers. Now, as organizations grapple with the consequences of both extremes, Platform Engineering is being touted as the discipline that finally gets the balance right.

[Gartner forecasts](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering) that by 2026, 80% of large software engineering organizations will establish platform teams as internal providers of reusable services, components, and tools for application delivery, up from 45% in 2022. The [CNCF Backstage project](https://www.cncf.io/blog/2024/11/15/internal-developer-platforms-at-scale-with-the-certified-backstage-associate-cba-certification/) now boasts [over 3,400 adopters](https://thenewstack.io/five-years-in-backstage-is-just-getting-started/) worldwide. What started as a bunch of internal teams hacking together their own tools has turned into a mature discipline with established best practices, dedicated conferences, and a rapidly consolidating technology landscape.

For VPs of Engineering and Platform Engineering leads who have moved beyond the "why do we need this" phase, the question now is: **how do we mature this practice without getting stuck in endless portal maintenance?**

## The Evolution of Platform Engineering

To understand where we are going, we must briefly understand how we got here. We have moved from the "Ticket Queue" era (where centralized IT provided stability but strangled velocity) to the "DevOps Revolution," where developers gained speed but drowned in infrastructure complexity.

Platform Engineering represents the synthesis of these two extremes. It centralizes complexity without removing autonomy. Platform teams build and maintain the underlying infrastructure, but they expose it through self-service interfaces. This allows developers to move quickly without needing to master every implementation detail, effectively treating the platform as a product with developers as customers.

## From Infrastructure to Interfaces

Early platform engineering efforts focused heavily on infrastructure primitives. Teams invested enormous energy in standardizing [Kubernetes deployments](https://roadie.io/docs/integrations/kubernetes/), building CI/CD pipelines, and creating Infrastructure as Code templates. These were necessary foundations, but they were not sufficient for driving developer adoption.

The modern Platform Engineering conversation has shifted decisively toward Developer Experience. The infrastructure layer still matters, but what sets teams apart is how they present that infrastructure to developers. That's why Internal Developer Portals (IDPs) have become popular.

## The Rise of the IDP

An IDP is the storefront of your platform. It gives developers a unified interface to discover services, access documentation, spin up new projects from templates, and view their deployments. Without this interface layer, even the most sophisticated platform remains opaque and underutilized.

While various tools exist, the market has overwhelmingly converged on a single standard. [Recent analysis](https://newsletter.getdx.com/p/backstage-and-the-developer-portal-market) indicates Backstage holds approximately 89% market share among organizations that have adopted an IDP. Originally developed by Spotify and now a CNCF project, it has moved from early experimentation to essential infrastructure.

This dominance is reflected in the project's momentum. Backstage now boasts [over 270 public adopters](https://www.cncf.io/blog/2024/11/15/internal-developer-platforms-at-scale-with-the-certified-backstage-associate-cba-certification/), including global brands like LinkedIn, CVS Health, and Vodafone. It was also the [top CNCF project by end-user commits](https://backstage.io/blog/2024/12/18/backstage-wrapped-2024/) and the fourth most contributed-to CNCF project in 2024, trailing only infrastructure giants like Kubernetes, OpenTelemetry, and Argo.

## Platform as a Product: From Philosophy to Practice

The shift to "Platform as a Product" marks a critical maturity point in Platform Engineering. Instead of mandating tools, modern platform teams treat developers as customers, using a competitive dynamic to force a relentless focus on value delivery.

This approach manifests in two concrete practices:

### Golden Paths

Rather than offering infinite flexibility, platform teams curate Golden Paths, opinionated, well-supported pathways for common tasks. These paths come with excellent documentation, proven templates, and integrated tooling. Developers can deviate when necessary, but the "Golden Path" represents the path of least resistance and highest support.

### Measuring Success

Success measurement has fundamentally changed. Uptime is no longer the only metric that matters. Leading teams now track impact using:

- **Adoption rates:** Are developers voluntarily choosing the platform?
- **Time-to-hello-world:** How fast can a new engineer deploy code?
- **DORA metrics:** Tracking deployment frequency and lead time for changes.
- **Satisfaction scores:** Using frameworks like SPACE to measure developer sentiment.

For example, [Spotify reported](https://backstage.io/docs/overview/adopting/) that their time-to-tenth-pull-request metric for new developers dropped by 55% after deploying Backstage.

## The Tooling Landscape: Consolidation and Standardization

The Platform Engineering technology stack has matured into defined categories. The infrastructure stack is well-defined: cloud providers (AWS, GCP, Azure) at the bottom, Kubernetes for orchestration, and Terraform for Infrastructure as Code. Increasingly, Backstage or a commercial derivative serves as the interface layer on top. [Gartner's Hype Cycle for Platform Engineering](https://www.gartner.com/en/documents/6586902) now tracks dozens of technologies across this stack, reflecting the maturity of the space.

This consolidation is creating a dilemma for the interface layer: Build vs. Buy. Organizations must choose between self-hosting Backstage, purchasing a commercial offering, or using a managed Backstage solution.

Self-hosting Backstage provides maximum flexibility but comes with significant costs. [Industry observers report](https://platformengineering.org/blog/platform-engineering-predictions-for-2025) common pitfalls including:

- **Long time-to-value:** Teams often spend 6-12 months on setup, with complex implementations extending to 18+ months.
- **Maintenance burden:** The plugin architecture requires continuous maintenance, and breaking changes in recent releases have created upgrade challenges.
- **Low adoption:** [Organizations outside of Spotify struggle with adoption](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/), with average internal rates hovering around 10%—often because teams burn out on maintenance before delivering features developers actually want.

This is not a failing of Backstage itself, but rather a reflection of the reality that [building and maintaining a production-quality developer portal](https://roadie.io/blog/from-day-0-to-day-2-a-guide-to-planning-and-implementing-backstage/) requires dedicated ongoing investment. Many organizations discover that maintaining the portal consumes so much of their platform team's capacity that they never get to building the unique platform capabilities that would actually differentiate their developer experience.

Commercial and managed offerings address this challenge. [Several alternatives exist](https://roadie.io/blog/backstage-alternatives/) in the IDP market, each with different approaches and strengths:

- Solutions like [Roadie](https://roadie.io/) provide Backstage as a service, eliminating the operational overhead while preserving the extensibility and ecosystem compatibility that make Backstage attractive.
- [Red Hat Developer Hub](https://www.redhat.com/en/about/press-releases/red-hat-accelerates-internal-developer-portal-adoption-latest-version-red-hat-developer-hub) offers an enterprise-grade alternative for organizations already invested in the Red Hat ecosystem.
- Platforms like Port, Cortex, and OpsLevel provide different architectural approaches to the IDP challenge, while Humanitec focuses on platform orchestration.

These approaches allow platform teams to skip directly from concept to value delivery, focusing their energy on the platform logic and Golden Paths that are unique to their organization rather than on maintaining commodity infrastructure.

## The Future: AI and the Intelligent Platform

The integration of AI into IDPs is the next frontier for Platform Engineering. [Gartner predicts](https://www.gartner.com/en/newsroom/press-releases/2025-07-01-gartner-identifies-the-top-strategic-trends-in-software-engineering-for-2025-and-beyond) that by 2028, 90% of enterprise software engineers will use AI code assistants, up from less than 14% in early 2024. The role of developers is shifting from implementation to orchestration, focusing on problem-solving and system design. Early implementations are already showing promising results, and the trajectory suggests fundamental changes to how developers interact with their platforms.

### Model Context Protocol

The [Model Context Protocol (MCP)](https://roadie.io/blog/announcing-the-roadie-mcp/), introduced by Anthropic and rapidly gaining adoption, provides a standardized approach for connecting AI systems with data sources and tools. Platform teams are beginning to expose their capabilities through MCP servers, enabling developers to interact with their platforms using natural language through AI assistants. Rather than navigating a web interface to provision a new service, a developer can simply describe what they need in conversation with an AI agent that understands the organization's platform capabilities.

### Agentic AI

[Agentic AI](https://roadie.io/blog/ai-is-showing-up-in-developer-portals/) takes this further. Instead of passively waiting for developer requests, intelligent platform agents can proactively identify issues, suggest optimizations, and implement routine fixes autonomously. This shifts the platform team's role from building tools to defining the rules and organizational knowledge that enable these agents to operate safely.

These capabilities are not speculative. Organizations are already deploying AI-powered observability that automatically analyzes logs and flags anomalies before they impact production. [Scaffolding workflows](https://roadie.io/product/scaffolder/) are becoming increasingly intelligent, generating not just boilerplate code but production-ready configurations tailored to the specific context. Documentation is being synthesized and queried through natural language interfaces rather than searched manually.

### The Prerequisites for AI-Powered Platforms

The platform teams who will thrive in this environment are those who have already built strong foundational platforms. AI agents need reliable, well-documented APIs to interact with. They need accurate [software catalogs](https://roadie.io/product/catalog/) to understand system relationships. They need established Golden Paths that encode organizational best practices. Organizations that have invested in mature Internal Developer Portals have the infrastructure in place to adopt AI capabilities rapidly.

## The End of DIY

Platform Engineering is entering its "boring" phase, and this is exactly what success looks like. The fundamental patterns are established, and the technology choices are converging.

The teams achieving the best outcomes have recognized that maintaining commodity infrastructure is not a competitive advantage. They buy or use managed solutions for the interface layer, freeing their platform engineers to focus on the unique Golden Paths and integrations that actually differentiate their developer experience.

Building a developer portal is not the same as building a platform. The portal is the interface; the platform is the substance behind it. Organizations that conflate the two often find themselves with impressive storefronts and empty shelves. The path forward is to source the interface from a specialist and focus your energy on the substance.

## Next Steps

If you're ready to move from concept to implementation, here are concrete next steps you can take:

**Evaluate Your Build vs. Buy Decision:** Before committing significant engineering resources to building and maintaining your own Backstage instance, consider the [true cost of self-hosting](https://roadie.io/blog/backstage-how-much-does-it-really-cost/). Understanding the full scope of ongoing maintenance, upgrades, and support requirements will help you make an informed decision.

**Start with a Software Catalog:** The foundation of any successful Internal Developer Portal is a comprehensive [software catalog](https://roadie.io/product/catalog/). Begin by modeling your existing services, APIs, and resources. Learn about [effective strategies for creating a complete catalog](https://roadie.io/blog/3-strategies-for-a-complete-software-catalog/) to ensure discoverability across your organization.

**Implement Self-Service Templates:** Reduce friction and standardize best practices by deploying [software templates](https://roadie.io/product/scaffolder/) that encode your Golden Paths. This accelerates onboarding and ensures consistency across your engineering organization.

**Define Engineering Standards with Tech Insights:** Move beyond anecdotal evidence and establish [measurable engineering standards](https://roadie.io/blog/how-to-define-engineering-standards/) using data-driven scorecards. This helps you track compliance, identify gaps, and demonstrate continuous improvement.

**Plan Your Adoption Strategy:** Technical implementation is only half the battle. Develop a comprehensive [adoption strategy](https://roadie.io/blog/the-adoption-journey-initiatives-and-strategies/) that addresses organizational change management, stakeholder engagement, and measuring success metrics that matter to your leadership team.

**Explore Managed Backstage Options:** If you want to skip the lengthy setup and ongoing maintenance burden, [try Roadie](https://roadie.io/free-trial/) to get a production-ready Backstage instance deployed in minutes rather than months, allowing your team to focus on building unique platform capabilities instead of maintaining infrastructure.

**Stop building the tool and start building the platform. Get a production-ready Backstage instance today with [Roadie](https://roadie.io/request-demo/).**

---

### [7 Best Developer Portals for Enterprise Engineering Teams](https://roadie.io/blog/7-best-developer-portals-for-enterprise-engineering-teams.md)

Your platform team built an internal developer portal. Or maybe you bought one. Either way, you spent $2 million and a year of engineering time. Sound familiar?

Here's the uncomfortable truth about [internal developer portals](https://roadie.io/blog/developer-portals-are-a-superpower/) in 2025: the market has fundamentally matured, and the old "build versus buy" calculus no longer applies. Companies that chose self-hosted Backstage discovered that "free and open-source" means 3-12 dedicated engineers. Organizations that bought proprietary platforms found themselves locked into data models they can't migrate away from. And those who picked the wrong solution are now facing a painful rip-and-replace.

The IDP landscape has evolved into three distinct approaches, each with radically different total cost of ownership:

- **Build**: Self-hosted Backstage installations offering maximum flexibility at the cost of $1M+ annual operational overhead.
- **Buy**: Proprietary SaaS platforms like Cortex and Port with polished interfaces but permanent vendor lock-in.
- **Hybrid**: Managed Backstage solutions delivering open-source ecosystem benefits without the engineering tax.

This guide evaluates the seven platforms that enterprise engineering leaders are actually deploying at scale, focusing on the strategic tradeoffs that matter three years after your initial decision, when you discover whether you made the right choice.

## What Makes a Great Enterprise Developer Portal?

Before diving into specific platforms, let's establish the evaluation criteria that separate enterprise-ready IDPs from tools that work well in demos but fail in production.

### Ecosystem and Extensibility

Can the platform integrate with your entire toolchain, or are you limited to what the vendor supports? At enterprise scale, you're likely using 50+ different tools across CI/CD, monitoring, security, and cloud infrastructure. The difference between supporting 20 integrations versus 250+ becomes critical when half your value comes from having everything in one place.

### Vendor Lock-In Risk

If you decide to move away from the platform in two years, what happens to your data model? Open-source-based solutions like [Backstage](https://roadie.io/backstage-spotify/) use standardized YAML entity definitions that you can export and migrate. Proprietary platforms often use custom data models that trap your organizational knowledge inside their systems.

### Maintenance Overhead

Does running the platform require a dedicated team, or can your existing platform engineers manage it alongside their other responsibilities? Self-hosted solutions can consume 3-5 full-time engineers just for maintenance, upgrades, and troubleshooting. This is what we call the "TypeScript tax," the hidden cost of maintaining frontend infrastructure that most DevOps teams aren't equipped to handle.

### Enterprise Readiness

Does the platform provide [role-based access control](https://roadie.io/product/access-control/) (RBAC), single sign-on (SSO), and SOC2 compliance out of the box, or do you need to build these capabilities yourself? For regulated industries or companies with strict security requirements, these aren't nice-to-haves, they're table stakes.

### Day 2 Operations

Look beyond the initial setup. How difficult is it to upgrade the platform when breaking changes occur? How do you handle search infrastructure at scale? What happens when you need to migrate to a new backend system? The platforms that look easiest on day one often become maintenance nightmares on day 700.

---

## 1. Roadie: The Backstage Platform for Enterprises

**Category**: Hybrid (Managed Backstage)

**Best For**: Teams that want Backstage's ecosystem without the operational burden

[Roadie](https://roadie.io/) delivers the full power of Spotify's open-source [Backstage platform](https://roadie.io/backstage-spotify/) as a managed SaaS service. This hybrid approach gives you access to the entire Backstage ecosystem, 211 [open-source Backstage plugins](https://roadie.io/backstage/plugins/), standardized data models, and active open-source development, while eliminating the maintenance overhead that typically requires 3+ dedicated engineers.

The platform handles all infrastructure concerns: hosting, security patches, database management, enterprise-grade search, and complex upgrades like the [New Backend System migration](https://roadie.io/blog/migrating-to-backstages-new-backend-a-step-by-step-guide/) that challenged self-hosted installations throughout 2024. Your team focuses on configuring integrations and building workflows, not on TypeScript debugging or React component updates.

**Key Features**:

- Minimal-maintenance Backstage platform with automated upgrades
- Access to entire open-source plugin ecosystem (211 plugins, 82 supported out-of-the-box)
- Built-in [Tech Insights](https://roadie.io/product/tech-insights/) for scorecards and engineering standards (paid add-on)
- Enterprise [RBAC](https://roadie.io/product/access-control/) (basic RBAC in Teams plan, custom RBAC in Growth plan)
- No vendor lock-in, data model is standard Backstage YAML

**Pros**:

- **No TypeScript Tax**: Platform engineering teams can focus on platform capabilities rather than [maintaining TypeScript and React frontends](https://roadie.io/blog/backstage-how-much-does-it-really-cost/).
- **Open Ecosystem**: Any [Backstage plugin](https://roadie.io/backstage/plugins/) works, including community-developed integrations.
- **Automatic Migrations**: Complex upgrades like the New Backend System transition happen automatically.
- **Faster Time-to-Value**: Most customers [see value within weeks](https://roadie.io/blog/from-day-0-to-day-2-a-guide-to-planning-and-implementing-backstage/), not months.
- **Standard Data Model**: Your [catalog definitions](https://roadie.io/docs/catalog/modeling-entities/) are portable YAML files, not proprietary formats.

**Cons**:

- **Backstage UI Constraints**: Less drag-and-drop flexibility compared to tools like Port, though more structured.
- **Requires SaaS Comfort**: While Roadie offers secure connectivity options (like the [Roadie Broker](https://roadie.io/docs/integrations/broker/)) for on-premises resources, it is primarily a hosted service.

**Pricing**: Teams plan starts at $24/developer/month with a 50-seat minimum (50-150 developers). Growth plan pricing is custom with a 100-seat minimum (100+ developers). Only active contributors to your source control management (SCM) incur costs, non-coding team members like product managers and leadership can access for free. Tech Insights is an optional paid add-on. [View pricing details](https://roadie.io/pricing/).

## 2. Cortex: The Engineering Metrics Specialist

**Category**: Proprietary SaaS

**Best For**: Organizations obsessed with service maturity scorecards and reliability metrics

[Cortex](https://www.cortex.io/) offers a polished, opinionated developer portal focused heavily on measuring and improving service quality through scorecards and engineering metrics. The platform excels at gamifying service ownership with detailed maturity models, SLO tracking, and automated scoring based on engineering best practices using Bronze/Silver/Gold levels and point-based systems.

The UI feels modern and intuitive, particularly for teams familiar with SaaS tools like Datadog or PagerDuty. Cortex's scorecard system is more sophisticated than most alternatives, offering fine-grained control over scoring criteria with flexible rule definitions and excellent visualization of engineering standards compliance across your organization.

**Key Features**:

- Advanced scorecard system with customizable rubrics using Bronze/Silver/Gold levels and point-based scoring
- Strong reliability engineering focus (SLOs, incidents, on-call)
- Polished, modern UI optimized for service discovery
- AI-powered features including Ownership Prediction and Velocity Dashboard for DORA metrics
- 60+ out-of-the-box integrations with major monitoring and development tools

**Pros**:

- **Scorecard Sophistication**: Best-in-class service maturity tracking with Bronze/Silver/Gold level visualization and detailed point-based scoring.
- **Beautiful UI**: Modern design that impresses stakeholders.
- **Strong Reliability Focus**: Excellent for teams prioritizing SRE practices.
- **Fast Initial Setup**: Can get basic catalog running quickly.
- **AI Integration**: New AI features for ownership prediction and metrics analysis.

**Cons**:

- **High Price Point**: Known for being expensive at enterprise scale, especially compared to Backstage-based alternatives.
- **Proprietary Lock-In**: Data model is Cortex-specific, making migration difficult.
- **Limited Ecosystem**: Rely on Cortex to build integrations, can't leverage community plugins.
- **Scaffolding Limitations**: Template/workflow capabilities lag behind [Backstage's Software Templates](https://roadie.io/product/scaffolder/).

**Pricing**: Not publicly disclosed; requires signing up for a demo to receive pricing information. However, the [Forrester Total Economic Impact study](https://tei.forrester.com/go/Cortex/IDP/?lang=en-us) from July 2024 lists pricing at approximately $65/user/month at scale. Multiple tiers available (Engineering Intelligence, Accelerate, Full IDP, Site License) with features scaling from basic catalog and scorecards to full platform capabilities with AI-powered features. [Request pricing](https://www.cortex.io/pricing).

## 3. Port: The No-Code Builder's Platform

**Category**: Proprietary SaaS

**Best For**: Teams that need to model non-standard assets or want maximum UI customization

[Port](https://www.port.io/) takes a radically different approach: instead of providing an opinionated developer portal, it gives you building blocks to create your own. The platform's "no-code" interface lets you define custom data models (called Blueprints) for any asset type, not just services and APIs, but also environments, IoT devices, or cloud resources.

This flexibility makes Port uniquely suited for organizations with complex, non-standard infrastructure that doesn't fit typical service catalog patterns. You can build custom views, define relationships between any entity types, and create workflows that match your exact processes. Port has recently rebranded as an "Agentic Internal Developer Portal" with enhanced AI capabilities.

**Key Features**:

- Fully customizable data models and UI views via Blueprints
- No-code interface for defining entities and relationships
- Strong visualization capabilities for complex systems
- Self-service actions using Cookiecutter templates
- 50+ integrations including DORA metrics tracking
- AI agent capabilities and Engineering360 dashboard

**Pros**:

- **Ultimate Flexibility**: Model anything your organization needs, not just traditional services.
- **Custom Views**: Build exactly the interface your teams need.
- **Good for Complex Infrastructure**: Excellent for multi-cloud, hybrid environments with diverse asset types.
- **Visual Workflow Builder**: Create automation without writing code.

**Cons**:

- **Blank Slate Problem**: Maximum flexibility means you build everything from scratch; less out-of-the-box value.
- **Proprietary Ecosystem**: Cannot leverage the Backstage open-source plugin ecosystem, though the Ocean Framework provides extensibility through data integrations and workflow automation.
- **Weaker Documentation Features**: While it supports Markdown, it lacks the full [TechDocs](https://roadie.io/docs/getting-started/technical-documentation/) build pipeline and search capabilities found in Backstage.
- **Steeper Learning Curve**: Teams need time to master the data modeling concepts.

**Pricing**: Free tier available (up to 15 seats, 10,000 entities). Startup tier at $30/developer/month. Enterprise tier available with premium features including SSO, advanced RBAC, ISO 27001 and SOC2 Type 2 certifications, and dedicated support. [View pricing details](https://www.port.io/pricing).

## 4. OpsLevel: The Service Maturity Tracker

**Category**: Proprietary SaaS

**Best For**: Teams focused primarily on service ownership and maturity tracking

[OpsLevel](https://www.opslevel.com/) started as a service maturity and ownership tool before evolving into a broader developer portal. This heritage shows in its excellent service ownership features and straightforward approach to tracking engineering standards compliance through its "Rubric" system with Bronze/Silver/Gold levels, plus separate Scorecards for team-specific standards.

The platform offers the fastest time-to-initial-value for basic service cataloging, with typical deployments completing in 30-45 days. You can have a working catalog with ownership information and basic checks running within hours. However, this simplicity comes at the cost of extensibility, OpsLevel's feature set is more constrained than platforms built on extensible architectures. Recent additions include AI-powered features for check generation and catalog enrichment.

**Key Features**:

- Fast setup for basic service catalog (typical 30-45 day deployment)
- Strong focus on service ownership and maturity rubrics
- Good integration with CI/CD systems for automated checks (60+ integrations)
- AI-generated checks and AI-enriched catalog
- Package version inventories for SBOM visibility
- Clean, straightforward UI

**Pros**:

- **Quickest Setup**: Get a basic catalog running faster than any alternative.
- **Service Ownership Focus**: Excellent for clarifying who owns what.
- **Maturity Rubrics**: Good built-in templates for measuring service quality.
- **Intuitive Interface**: Less complex than more feature-rich platforms.
- **AI Integration**: New AI features streamline catalog management.

**Cons**:

- **Limited Extensibility**: Can't add community plugins or build custom integrations easily.
- **Rigid UI**: Less flexible than Port or Backstage for customization.
- **Narrower Feature Set**: Primarily focused on cataloging and checks, less emphasis on docs or scaffolding.
- **Proprietary Lock-In**: Migration path unclear if you outgrow the platform.

**Pricing**: Not publicly disclosed, pricing based on team size with custom quotes. Per-developer pricing model with volume discounts available. Includes SOC2 Type 2 compliance and SAML-based SSO. Pricing customizable based on needs including self-hosted options and support levels. [Request pricing](https://www.opslevel.com/pricing).

## 5. Atlassian Compass: The Jira Companion

**Category**: Proprietary SaaS

**Best For**: Organizations deeply invested in the Atlassian ecosystem

If your company runs on Jira, Bitbucket, and Confluence, [Compass](https://www.atlassian.com/software/compass) offers the most seamless native integration you'll find. The platform leverages Atlassian's identity system, pulls in data from other Atlassian products automatically, and feels like a natural extension of your existing toolchain.

Compass provides automated service health monitoring, tracking metrics from integrated tools and surfacing problems before they escalate. For teams already paying for Atlassian products, Compass represents an incremental cost with minimal integration effort. The platform has scorecards with a new "Maturity Levels" feature added in 2025.

**Important Note**: Atlassian deprecated the Templates/scaffolding feature on December 1, 2025. This represents a significant capability reduction for teams requiring self-service service creation.

**Key Features**:

- Native integration with Jira, Bitbucket, Confluence, and Opsgenie
- Automated service health monitoring
- Component tracking with Atlassian-native data models
- Integrated incident management through Opsgenie
- Scorecards with Maturity Levels feature
- Built on Atlassian Forge with GraphQL APIs for extensibility

**Pros**:

- **Atlassian Integration**: Unbeatable if you use Jira for everything.
- **Familiar UX**: Feels consistent with other Atlassian products.
- **Automated Health Monitoring**: Good automated health checks.
- **Standalone or Bundled**: Available as standalone product or with some enterprise packages.

**Cons**:

- **The Atlassian Trap**: Struggles with non-Atlassian tools like [GitHub](https://roadie.io/docs/integrations/github-discovery/), [GitLab](https://roadie.io/docs/integrations/gitlab/), or CircleCI.
- **Scaffolding Removed**: Templates feature deprecated December 1, 2025, no longer available for service creation.
- **Proprietary Ecosystem**: Can't extend with community plugins.
- **Not a Full IDP**: More of a service catalog with add-ons than a complete platform interface.

**Pricing**: Free tier available (3 full users, unlimited basic users). Standard tier at $8/user/month includes basic features. Premium tier at $25/user/month includes IP Allowlisting, advanced integrations, 99.9% uptime SLA, and premium support. Discounted rates available for teams above 101 users. Compass is a standalone product with separate billing from other Atlassian tools. [View pricing details](https://www.atlassian.com/software/compass/pricing).

## 6. Backstage (Self-Hosted)

**Category**: Open Source (Self-Hosted)

**Best For**: Large enterprises with dedicated platform engineering teams and specific compliance requirements

Spotify's [Backstage](https://backstage.io/) is the industry-standard open-source developer portal framework. It powers IDPs at Spotify, American Airlines, Pinterest, and thousands of other organizations. The platform offers ultimate flexibility: you own the code, control the infrastructure, and can customize anything.

But this flexibility comes with significant operational costs. Self-hosting Backstage requires 3-5 dedicated engineers to manage infrastructure, handle upgrades, maintain search systems, and keep up with the rapidly evolving codebase. Roadie's survey of the Backstage community found that users reporting satisfaction with self-hosted deployments had at least three engineers dedicated full-time, with some companies staffing teams of 12 people just for Backstage. Breaking changes occur regularly with monthly releases, and major migrations like the [New Backend System](https://roadie.io/blog/migrating-to-backstages-new-backend-a-step-by-step-guide/) transition that completed in 2024 consumed months of engineering time for self-hosted teams.

For perspective on the true cost of building similar developer portals, [Zalando invested over $4 million](https://roadie.io/blog/backstage-how-much-does-it-really-cost/) across four years developing their internal platform before open-sourcing their work as part of Backstage.

**Key Features**:

- Fully open-source with Apache 2.0 license
- 250+ [community plugins](https://roadie.io/backstage/plugins/) covering every major tool
- Extensible architecture for [custom plugins](https://roadie.io/docs/custom-plugins/overview/) and integrations
- Active community and regular monthly releases
- CNCF Incubating project with strong enterprise adoption

**Pros**:

- **Ultimate Control**: You own everything and can customize without limits.
- **No License Costs**: Free to download and use.
- **Massive Ecosystem**: Largest community and plugin library (250+ plugins).
- **No Vendor Dependency**: Run anywhere, modify anything.
- **Industry Standard**: Backed by CNCF and major enterprises.

**Cons**:

- **Operational Overhead**: Requires 3-5 FTE engineers minimum for successful deployments, some teams reach 12 FTEs.
- **The TypeScript Tax**: Most DevOps teams lack frontend skills for React/TypeScript customization.
- **Upgrade Complexity**: Monthly breaking changes and major migrations (like New Backend System) require significant engineering investment.
- **Day 2 Operational Burden**: You manage databases, search infrastructure (Elasticsearch), monitoring, and security patches.
- **Hidden Costs**: The real cost when factoring in engineering time, opportunity cost, and infrastructure can reach millions of dollars. At typical senior platform engineer compensation ($250K/year fully loaded), 3-5 engineers cost $750K-$1.25M annually, plus infrastructure costs ($12K-$24K/year). TCO typically exceeds $2M+ over three years when including engineering time and opportunity cost.

**Pricing**: Free (open source under Apache 2.0 license). However, total cost of ownership includes 3-5 engineer salaries ($750K-$1.25M+ annually at senior platform engineer compensation of $250K/year fully loaded) plus infrastructure costs ($12K-$24K+ annually for hosting, databases, and search infrastructure). TCO typically exceeds $2M+ over three years when factoring in engineering time, opportunity cost, and infrastructure.

## 7. Configure8: The Universal Catalog Platform

**Category**: Proprietary SaaS

**Best For**: Organizations prioritizing discovery and cost analytics

[Configure8](https://configure8-io.webflow.io/) positions itself as a "universal catalog" that can ingest and relate data from virtually any source. The platform emphasizes discovery features, helping teams understand what they have and how it's interconnected. It also offers strong cloud cost integration, surfacing spending data alongside technical resources.

While Configure8 has solid core features including 30+ integrations and workflow-based Self-Serve Actions, its smaller market presence and proprietary nature make it a riskier choice than platforms with larger ecosystems or open-source foundations.

**Key Features**:

- Universal catalog supporting diverse asset types
- Strong discovery and search capabilities
- Cloud cost analytics integration
- Relationship mapping across resources
- Workflow-based Self-Serve Actions
- Available as SaaS or on-premises deployment

**Pros**:

- **Comprehensive Discovery**: Good at helping teams understand what exists.
- **Cost Integration**: Unique focus on cloud spending alongside technical resources.
- **Multi-Source Ingestion**: Can pull data from many systems.
- **Deployment Flexibility**: Offers both SaaS and on-prem options.

**Cons**:

- **Smaller Ecosystem**: Less community support and fewer integrations (30+) than larger platforms.
- **Proprietary Lock-In**: Data model is Configure8-specific.
- **Limited Track Record**: Fewer public case studies and enterprise deployments than alternatives.
- **Market Position Uncertainty**: Smaller player in a competitive market.

**Pricing**: Free tier available (up to 10 users for scorecards). Paid tiers available with SOC2 certification and RBAC features. Enterprise pricing available with additional features and volume discounts. Available as both SaaS and on-premises deployment. Contact Configure8 for detailed pricing information. [View pricing page](https://configure8-io.webflow.io/pricing).

## Comparison: At a Glance

| Platform | Foundation | Maintenance | Ecosystem Size | Lock-In Risk | Enterprise Features |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Roadie** | Open Source (Backstage) | Minimal (Managed) | 211 plugins | Low (standard YAML) | RBAC, SSO, SOC2 Day 1 |
| **Cortex** | Proprietary | Minimal (SaaS) | 60+ integrations | High (proprietary) | Strong |
| **Port** | Proprietary | Minimal (SaaS) | 50+ integrations | High (proprietary) | Good |
| **OpsLevel** | Proprietary | Minimal (SaaS) | 60+ integrations | High (proprietary) | Basic |
| **Compass** | Proprietary | Minimal (SaaS) | Atlassian-centric | High (proprietary) | Good (if Atlassian) |
| **Backstage** | Open Source | High (3-12 engineers) | 250+ plugins | None | DIY |
| **Configure8** | Proprietary | Minimal (SaaS) | 30+ integrations | High (proprietary) | Moderate |

## How to Choose the Right Developer Portal

The right IDP depends on your organization's constraints, technical culture, and platform engineering maturity:

- **Choose Self-Hosted Backstage if** you have a team of 10+ platform engineers, unlimited budget, and specific requirements that absolutely cannot be met by managed solutions. You're willing to invest significant engineering time in maintenance and customization for maximum control. Be prepared for 3-12 dedicated engineers and $2M+ total cost of ownership over three years.
- **Choose Cortex or Port if** you value polished UI above all else, don't mind proprietary lock-in, and want specific workflow capabilities their platforms emphasize. Budget for potentially higher costs at scale (~$65/user/month for Cortex, ~$30+/user/month for Port enterprise tiers).
- **Choose OpsLevel if** you need a basic service catalog immediately and your primary use case is [tracking ownership](https://roadie.io/docs/catalog/ownership/) and maturity, not building complex workflows or maintaining extensive documentation.
- **Choose Compass if** you live entirely in the Atlassian ecosystem and can accept its limitations with non-Atlassian tools. Note that scaffolding/templates were deprecated December 1, 2025. The integration efficiency may outweigh the platform's constraints if you're already in the Atlassian ecosystem.
- **Choose Roadie if** you want the industry standard (Backstage) with its entire ecosystem and community support, but you value your engineers' time too much to spend it on infrastructure maintenance. It's the "golden path" for enterprises that want modern platform capabilities without the platform tax or the $2M+ cost of building from scratch.

The key question isn't which platform has the most features, it's which platform lets your engineers focus on building platform capabilities instead of maintaining platform infrastructure. At the 150+ engineer scale where IDPs become critical, that distinction determines whether your portal becomes a force multiplier or just another thing to maintain, potentially at a cost exceeding $2M over three years if you go the self-hosted route.

## Next Steps

Ready to implement a developer portal for your organization? Here are some practical next steps to guide your journey:

**Evaluate Roadie with a Free Trial**: Experience the power of managed Backstage firsthand. [Start your free trial](https://roadie.io/free-trial/) to explore Roadie's features, integrations, and see how quickly you can get value without the operational overhead.

**Learn from Customer Success Stories**: See how other enterprise teams have successfully implemented developer portals. Read our [case studies](https://roadie.io/case-studies/) to understand real-world adoption strategies, challenges overcome, and measurable results achieved.

**Dive Deeper into Backstage**: If you're new to Backstage or want to understand its capabilities better, explore our comprehensive [guide to Backstage](https://roadie.io/backstage-spotify/) and learn why it's become the industry standard for developer portals.

**Plan Your Implementation**: Moving from evaluation to production requires careful planning. Our guide on [planning and implementing Backstage from Day 0 to Day 2](https://roadie.io/blog/from-day-0-to-day-2-a-guide-to-planning-and-implementing-backstage/) provides a roadmap for successful adoption.

**Compare Your Options**: Still weighing self-hosted versus managed solutions? Read our detailed [comparison of managed vs. self-hosted Backstage](https://roadie.io/backstage-comparison/) to understand the true total cost of ownership.

**Schedule a Demo**: See Roadie in action with your specific use cases. [Request a personalized demo](https://roadie.io/request-demo/) to discuss your requirements, explore integrations, and understand how Roadie can accelerate your platform engineering initiatives.

## Case Studies

### [Motability Operations: Building a Modern Developer Platform with Roadie](https://roadie.io/case-studies/motability-operations-case-study-a-modern-idp.md)

When Motability Operations (MO) began its internal developer portal journey in early 2024, it wasn’t just about adopting a new tool, it was about taking control of a sprawling and opaque software ecosystem.

Since then, MO has transformed how its engineers discover, manage, and standardize their services. Roadie’s hosted Backstage platform has become the backbone of that effort, with MO’s recent source code management (SCM) migration serving as both a milestone and a catalyst for deeper platform maturity.

We sat down with Jose Carlos (JC) Monteiro, Technical Principal, and Charles Illingworth, Engineering Manager, who lead MO’s Developer Experience (DevEx) team, to get the full story of their IDP journey, how they navigated an SCM migration as a chunky side quest, and some of the lessons learned along the way.

### The Original Challenge: Visibility, Ownership, and Consistency

What was the impetus for MO considering an IDP? Prior to exploring the IDP space and ultimately adopting Roadie, MO underwent a major cloud migration from AWS London to Ireland and upgraded its OpenShift infrastructure in the process. These initiatives exposed a glaring problem: nobody had a reliable, up-to-date picture of what software the company ran, who owned it, or how it was configured.

As JC recalls: “We were trying to keep up with Excel spreadsheets. ‘What is this workload, who owns it, what is it for’, but it was always out of date. It was just too messy and too much work.”

Realising that they needed a solution, the team experimented with running open-source Backstage on their own infrastructure, but maintaining plugins and updates was error-prone and costly. It quickly became clear that self-hosting would pull the DevEx team away from delivering value to developers and into managing Backstage itself.

Other options like Atlassian Compass and Red Hat Developer Hub were briefly considered, but Roadie stood out as the only solution that let MO focus on building a great developer experience without having to run and maintain the platform themselves. Roadie’s fully-managed SaaS model removed operational overhead, while features like Tech Insights and the Scaffolder worked out of the box, with expert support when needed.

### The Roadie Approach: Catalog + Scaffolder + Insights

The initial draw for MO was Roadie’s software catalog and Tech Insights, but the Scaffolder quickly became the workhorse of their developer platform. At first seen as a “nice to have,” it rapidly evolved into a core part of day-to-day workflows.

JC reflects: “We quickly realised there’s a lot of boilerplate work we were asking our engineers to do: CI/CD configuration, setting up repos. We thought, imagine if we had a simple UI where after filling a form, it does all the boilerplate.”

The Scaffolder has become so widely adopted within MO, that as Charles comments: “Even junior developers can create a new microservice without needing a more seasoned developer who knows how all the pipelines work.”

Today, MO estimates that around 90% of new services are created using Roadie templates. What used to take 2-3 days of manual setup now takes minutes. This has sped up delivery and reduced frustration, while embedding consistent patterns across teams.

### An SCM Migration That Moved More Than Code

At around the same time MO was rolling out its internal developer portal with Roadie, the team faced a major technical challenge: migrating from one SCM provider to another. Their existing SCM had been in place for years and had served them well, but as their needs evolved, so did their requirements around automation, scalability, and developer experience.

“Our previous SCM had been reliable and had worked well,” JC explained. “But as our platform ambitions grew, we started running into some limitations. The new provider aligned better with the direction we were heading, both technically and in terms of the broader ecosystem.”

With the decision made, the migration itself was a significant lift. In spite of the scope - upwards of 20 teams and close on 500 repositories - it quickly became clear that the real challenge wasn’t the SCM switch in itself - it was everything around it. Once again the migration exposed inconsistent CI/CD pipelines, missing ownership metadata, and some fragmented standards across teams. What began as an infrastructure upgrade turned into a forcing function for broader platform maturity.

Rather than manage this manually, MO leaned heavily on Roadie and the Scaffolder in particular. Migration templates were designed to require proper metadata; every repo had to include a catalog-info.yaml file and define ownership before it could be migrated. This had a powerful side effect: it seeded the catalog with missing components and enforced consistency across services.

Teams were also able to self-serve their migrations on their own timeline, and those that didn’t need to be migrated could be archived, again, with a purpose-built Scaffolder template. Even MO’s shared Jenkins pipeline library was upgraded as part of the process, bringing improved functionality to teams that had previously been running older versions.

“Some teams were able to migrate 20-30 repos in a day,” Charles noted. “Doing that manually would have been weeks, if not a month of elapsed time, and even then, there’d be no guarantee the right standards had been applied.”

By embedding platform hygiene, ownership, and automation directly into the migration, MO emerged on the other side not just with a new SCM but with a cleaner, more visible, and more governable developer platform.

### Results: Faster Delivery, Better Onboarding, Clearer Ownership

The combination of Roadie’s catalog, Scaffolder, and Tech Insights has delivered tangible benefits to JC, Charles, and the team at MO:

- **Speed**: Creating new services now takes minutes instead of days.
- **Scale**: 90% of new services use Roadie templates.
- **Consistency**: Templates and Tech Insights enforce standards.
- **Ownership**: Every repo had to declare its owner during migration.
- **Onboarding**: New hires can quickly discover who owns what.

As JC observes: “It’s been very important not only for those of us who’ve been here a while, but also for helping onboard new people. They can quickly find information in Roadie - it was a nice surprise for them.”

### Lessons Learned: Start with the Catalog

Looking back, JC and Charles agree on one thing: don’t skip ahead. While it’s tempting to jump straight into features like scorecards or scaffolder templates, those tools only work if the catalog is in good shape.

“Having to set up our services in Roadie forced us to answer some tough questions, even before the migration,” Charles recalled. ‘Who owns this? What does it do? Which system is it part of?’ We didn’t always have the answers.”

The software catalog is foundational. If it’s incomplete or inaccurate, downstream tools like Tech Insights and the Scaffolder may not deliver full value. Their advice to other teams? Prioritize building a strong, structured catalog first, standardizing ownership, adding missing components, and aligning on naming, before layering on automation and governance. As JC puts it: “I highly recommend that anyone new to Roadie spend the time up front refining the catalog. It makes everything else downstream more powerful.”

### Looking Ahead

For MO, choosing a managed platform like Roadie both accelerated time-to-value and meant their platform team could focus on what really matters: building great tools for developers, not maintaining infrastructure.

Having successfully used Roadie to turn a daunting SCM migration into a springboard for a more standardized developer platform, MO is now planning a comprehensive data model review to scale and improve its catalog structure. The journey isn’t over, but the foundation is in place. MO now has the tools, structure, and visibility to keep evolving their platform with confidence.

Thinking of switching to managed Backstage? See how Roadie can help: book a demo, contact us at sales@roadie.io, or check out our [Backstage comparison guide](https://roadie.io/backstage-comparison/).

---

### [Maintenance to Momentum: Why Celonis Made the Switch from Self-Hosted Backstage to Roadie](https://roadie.io/case-studies/why-celonis-switched-from-selfhosted-backstage-to-roadie.md)

## **About Celonis**

[Celonis](https://www.celonis.com/) is the global leader in Process Mining, helping organizations identify inefficiencies and optimize operations across finance, supply chain, customer service, and beyond. With over 3,000 employees, more than 20 offices worldwide and 1,500 enterprise customers, Celonis powers process excellence for more than 30% of the Fortune Global 500.

## **Celonis’ OSS Backstage Era**

Internally, Celonis brings the same performance-driven mindset to its engineering operations, investing in tools that help teams move fast, operate safely, and scale with confidence. That mindset is what led them to adopt open source Backstage in 2022: a flexible, extensible platform that offered a centralized view of their software ecosystem, clear ownership, and a framework for codifying engineering standards into daily workflows.

The initial goal was to build a unified internal developer portal that could drive consistency and visibility across teams. And in the early days, Backstage certainly delivered, improving discoverability and reducing reliance on tribal knowledge.

According to Andreas Bayer, VP System Engineering at Celonis:

> A few of the early wins were consolidating documentation scattered across GitHub, Confluence, and Google Docs into one place, and improving discoverability. As the company grew, Backstage also helped address service ownership: previously, everyone knew which team owned what, but that model broke down as we scaled. Having a central catalog helped resolve that.
>

But over time, the limitations of maintaining Backstage internally began to surface.

> A team of 3 FTEs is not able to deliver a sufficiently useful portal based on OSS Backstage. There are obvious pieces like Tech Insights, but also many little things that add up to a much better user experience - things that would take weeks to build and are hard to prioritize over bigger features. The maintenance overhead is just too high.
>

Keeping up with backend upgrades was one of the biggest drags on velocity. As Andreas described it, it became a constant trade-off: invest time in upgrades or in feature development. Every hour spent keeping Backstage alive was an hour not spent improving the developer experience.

> It was always a choice between building new features and falling behind on maintenance, or staying up to date but delivering little value to users. That’s not sustainable.
>

According to data collected for Roadie’s 2025 State of Backstage Report, 70 percent of companies that are ‘very happy’ with Backstage dedicate *at least* 3 full-time engineers to maintaining it. For teams that can’t justify such a level of investment, maintaining a production-grade experience becomes a game of trade-offs.

The tipping point came gradually. Over time, the team noticed that the very features sitting on their internal backlog were already being shipped by other platforms like Roadie: Scorecards, catalog UX improvements, integrations - they were constantly being outpaced.

> We saw vendors shipping features we’d always wanted to build but never got to. The final nudge came when we wanted to double down on scorecards and readiness checks. Building and wiring up the Tech Insights stack ourselves was so time-consuming - then we looked at Roadie and realized, wait, it’s already there. No engineering lift required.
>

## **Making the Case for Roadie**

That’s when Celonis began to seriously evaluate Roadie. Unlike a from-scratch rebuild or a major migration project, Roadie offered a natural next step for an existing Backstage adopter: a fully-managed Backstage platform that could give the Celonis team everything they needed, without the overhead.

Roadie *is* Backstage, just with the batteries already included. The compatibility was crucial: Celonis could reuse their existing catalog-info.yaml files, extensions, and the knowledge and patterns they had already established. They got continuity, without the cost of ongoing maintenance.

> One of the biggest draws was that Roadie is deeply involved in the Backstage ecosystem: we’d seen Roadie’s contributions to ArgoCD plugins and other parts of the platform. That gave us a lot of confidence in their technical approach and commitment.
>

Beyond compatibility, Roadie gave Celonis:

- A developer portal that was polished, fast, and production-ready; no weeks-long sprints just to improve search, navigation, or quality of life features
- A fully integrated Tech Insights platform, letting them build scorecards and enforce standards from day one
- Powerful customization options like agent-based ingestion and the Fragments API to support more advanced use cases
- Freedom to focus on value, not infrastructure - Roadie took on the burden of plugin upkeep, upgrade stability, performance tuning, and support.

> All the usual pain points - plugins breaking, authentication weirdness, long CI cycles, slow page loads, they just go away. It’s not just a hosted Backstage - it’s a managed solution that lets us focus on what actually matters to our engineers.
>

## **Migration: From Evaluation to Execution**

Celonis engaged Roadie through a Proof of Value (PoV) evaluation, giving them the chance to test capabilities, validate integrations, and work closely with Roadie’s support and solutions engineering teams.

Following a successful PoV, the decision was made to fully migrate off their self-hosted instance. Thanks to the shared Backstage foundation, much of the transition was seamless. Existing entity definitions, scorecards, and metadata were immediately portable. Within two weeks, the production migration was complete.

> Hooking up our existing catalog files just worked. But the real wow moment came when the team realized how easy it was to write new scorecard checks. People who had struggled with the old system were like, ‘wait, that’s it? No dev containers? No plugin juggling? It just works!’
>

Most of the effort went into trimming internal customizations: choosing what to keep, what to drop, and what to rethink now that Roadie offered native alternatives. As Andreas puts it, the migration was as much a cleanup opportunity as it was a platform shift:

> It helped us revisit old decisions and remove customizations that weren’t as useful as we originally thought. The technical migration was easy - most of the work was organizational.
>

## **What’s Next**

Now that the migration is complete, Celonis is focused on scaling the value of their developer portal.

The priorities include:

- Expanding Tech Insights usage, including custom filters and compliance labels unique to their requirements
- Lifecycle gating to ensure services meet quality thresholds before going live
- Sorting, filtering, and custom columns to help platform and security teams prioritize risk
- Future plans for automated remediations, Slack notifications, and Scaffolder-driven workflows.

Celonis is now also rebuilding their scaffolder strategy with the goal of making service creation fully self-service, from repo setup to monitoring and documentation. Longer term, they’re exploring how templates can streamline squad registration and ownership updates in line with their org model.

## **Advice to Other Teams**

When asked if Celonis would recommend other teams who are self-hosting Backstage to consider switching to Roadie, Andreas was emphatic:

> It’s definitely worth switching. With Roadie, you get to spend your time thinking about what’s valuable for your users - not worrying about Backstage internals or upgrade mechanics.
>

Thinking of switching to managed Backstage? See how Roadie can help: book a [demo](/request-demo/?referringPathname=homepage) or check out our [Backstage comparison guide](/backstage-comparison/).

---

### [Dexcom: Automating Backstage Catalog Completeness with Roadie](https://roadie.io/case-studies/dexcom-automating-catalog-completeness-backstage.md)

When [Dexcom](https://www.dexcom.com/) set out to improve the completeness of their software catalog in Backstage, they weren’t just solving a technical problem – they were tackling one of the most persistent blockers to platform maturity. Like many organizations, Dexcom had a sprawling GitHub organization with hundreds of repositories, but not all were onboarded into Backstage. That made it difficult to understand software ownership, run meaningful checks, or drive improvements at scale. After a concerted push, catalog completeness improved from 60% to over 95%, bringing nearly all of their IT repos into view.

## From manual overhead to intelligent automation

At the center of this transformation has been Natalie Brooks, a platform engineer at Dexcom, who took a hands-on approach to solving the problem. Working within the IT organization within Dexcom, Natalie found herself repeatedly chasing down ownership info and trying to figure out which IT teams were responsible for long-abandoned or unclear repositories. The existing process was frustrating, unsustainable and didn’t scale.

Rather than relying on individual engineers to create and populate catalog-info.yaml files for the various repositories, Natalie wrote a Python script to automate catalog ingestion. The script pulled data from the GitHub API to surface repo metadata – contributors, admins, last committers, and more. It opened each repo in the browser so she could make a quick visual judgment when needed. She created a simple interactive flow in the terminal where she could select the most likely owner, set lifecycle and system metadata, and confirm the description. If none was provided, the script defaulted to using the repo name.

Once the input was validated, the script would generate a catalog-info.yaml using a simple template and inject it directly into the repo. It committed the file straight to the default branch, with CI actions disabled to avoid triggering unnecessary pipelines.

> It was either herd cats or automate it,” she said. “I was going into every single repo trying to copy-paste the same info or track people down. I figured I could either do this a hundred times, or make it easy on myself and do it once, well.

The results came quickly: what started as a side project led to a systematic onboarding of nearly every repo in the IT org within a matter of weeks.

## A top-down approach to onboarding

Rather than waiting for individual teams to take action, Dexcom took a [top-down approach](https://roadie.io/blog/the-adoption-journey-initiatives-and-strategies/#expand-and-land), a strategy that echoes guidance shared in Roadie’s adoption journey framework. However, the change wasn’t done without due consideration of including the broader organization – Natalie posted a banner in GitHub alerting teams to the incoming catalog-info.yaml files, with a clear note that they wouldn’t affect production code. She coordinated the rollout carefully, using her internal ownership of the GitHub org to make changes without disruption.

The result: catalog completeness surged past 95%, giving Dexcom a clear, organization-wide view of their software landscape and unlocking the full potential of their developer portal.

## Preventing drift with the Scaffolder

To prevent regressions, Dexcom now enforces repo creation through Roadie’s Scaffolder. Repositories can no longer be created through GitHub directly. Instead, every new repo creation must be done via a software template that requires users to define ownership, resource type, and lifecycle up front, all of which is captured in an appropriate catalog-info.yaml. This ensures all new projects are compliant from day one – no more retroactive fixes.

## Unlocking governance with Tech Insights

Dexcom had already been using Tech Insights to track software standards across the organization, but the dramatic improvement in catalog completeness has made those checks far more meaningful. With nearly every repository onboarded, scorecards now provide a full and fair view of team-by-team performance.

KPIs like repo safety and hygiene are reported directly to leadership, and team-level reporting has introduced a new level of accountability.

> If a team shows up in a KPI meeting because they’re dragging down our safety score, that drives change,” said Natalie. “And the best part is they go into Roadie to fix it.

## Building a foundation for automation and improvement

Dexcom is now turning their focus to remediation. Natalie plans to create scaffolder templates that help teams fix issues automatically, like enabling branch protection or adding READMEs, to further improve standards across the org.

By combining catalog automation, template enforcement, and governance via Tech Insights, Dexcom has created a platform strategy that’s scalable, measurable, and deeply pragmatic. It didn’t require mass buy-in upfront. Just a smart script, some well-placed nudges, and a strong desire to remove friction from the developer experience.

## Learn more

- [Roadie Tech Insights](/docs/tech-insights/introduction/)
- [Roadie Scaffolder Templates](/docs/scaffolder/writing-templates/)
- [Get a Roadie demo](/request-demo/)

---

### [Improving software standards with Roadie](https://roadie.io/case-studies/improving-software-standards-with-roadie.md)

[Uplight](https://uplight.com/ "Uplight") is a clean energy technology company that creates, deploys, manages and monetizes energy resources at scale to improve grid reliability, reduce costs, and accelerate decarbonization.

Uplight is dedicated to improving the way they develop software to meet that mission, which in turn means they’re highly engaged with software catalogs and scorecards, and how the combination of the two can be used to drive sought-after improvements.

I met with Doug Ramirez, Principal Architect at Uplight, and Shaw Atkinson, Senior Principal SRE, to discuss how they’ve used Roadie to capture and model a diverse set of software teams and components, then set about the task of improving software standards using scorecards.

## Building a software catalog in a complex business

Engineers and architects at Uplight think a lot about how to document, standardise and improve the software they write. Uplight has grown rapidly since its founding in 2019, and any company which embarks on such a journey needs a powerful muscle for folding in new technology and capabilities into an existing stack.

### Pulling available levers to gain traction

The initial rationale for working with Roadie was to help the team manage its technology stack through a software catalog: consistently maintaining ownership attribution, standardisation, and transparency of information and folding new units into the wider Uplight technical community.

Driving adoption took time and focus, but the reward was a complete catalog. As Doug puts it, “we went through a big push to make everybody merge in catalog-info.yaml files and to GitHub for detection by Roadie with some helpful context”. That initial surge, as Shaw adds, has now created a virtuous feedback loop: the catalog in Roadie just “solves issues before they arise - it gives the visibility to engineering teams that they could be missing” and that’s a big enough benefit that it’s pushed adoption up towards 100%.

## Defining software standards

Once everything is visible and transparently available in a software catalog, Platform and architecture teams have the opportunity to drive up standards and standardisation of software development.

To do that you need to put a stake in the ground and define some standards.

### Asking the right questions

Uplight started to ask questions like:

- What are our standards of what a service is, what a component is etc?
- What does it mean to be 'production ready'?
- How can we verify those standards so we’re not relying on manual reporting?
- And ultimately, how can we surface all this data to teams and leadership?

To answer those questions, the team at Uplight looked back on past examples of standardisation, especially their checklists, to start to pull disparate threads together into a single cohesive set of software standards.

“We adapted some of our existing checklists on production readiness, service deployment checklists, service account governance derived through infra etc, but we had to do the groundwork” said Doug.

### Forming a software standards document

The end product was a set of 10 categories of software standards that will feel familiar to other businesses:

- Security
- Logging
- Monitoring
- etc.

With individual line-items against each one to pinpoint concrete steps by which to measure those areas of a given piece of software.

Uplight focused on the simplicity of their standards rather than dictating how and by what means engineering teams should fix individual tasks. As Doug puts it, “when you’re building these things you think about a check engine light on the dashboard - it means you should go take a look, it suggests some aspect of the checklist not being met,” rather than specifying a solution.

## Implementing automated checks in Roadie

To help automate these standards, Uplight uses the Roadie Tech Insights plugin inside Roadie to build checks and scorecards, then run checks against those standards several times a day.

As Shaw highlights, “If a VP asked a very simple question about our infrastructure or code standards a year ago I wouldn’t be able to answer it without some digging. Now, even for a check or data we don’t yet have in Roadie it’s fifteen minutes. I add a Tech Insights Data Source, run it for a bit, then send them the link.”

### Starting simple

Uplight started the process of automating these standards as simply as they could.

“There were a lot of checks that we didn’t know how to bring the info up and make it available. So step one for us was looking for annotation - rather than looking at the code or CICD platform to determine deployment strategy. We looked at documentation and annotation first.

This was a “Fantastic first step. It started the conversation. We have a lot of repos, people aren’t always focused on legacy services, stuff gets lost in march of time etc. and now teams have the information they need to be effective at their fingertips,” said Shaw.

These productive discussions allowed Product, Engineering and non-technical teams to share a common language around standards improvement and start to shift behaviour.

### Then focusing on the social side of standardisation

“Our goal with scorecards is when we give teams ownership of something in the catalog they can kind of look at each one of these scorecards and decide which one is more most critical to them and then start work to address that category, get that percentage up.”

Embedding standards takes time but Uplight are investing the time and energy in thinking about the social elements of standardisation and standards improvement as much as the technical implementation of creating checks and scorecards within Roadie.

### Increasing the complexity of checks

Software standards that check documentation are one thing, but automating the process by which every piece of software an organisation creates is evaluated against that software is a different challenge.

As Shaw puts it, “we threw a lot of checks into Tech Insights, a whole bunch of people got their feet wet and so when we came back to it we could streamline and review. Now we don’t point at documentation, we point to implementation.”

That includes things like checking DataDog directly for SLOs, for example, rather than relying on documentation of service standards.

### The Social side of rolling out standards

“Our goal with scorecards is when we give teams ownership of something in the catalog they can kind of look at each one of these scorecards and decide which one is more most critical to them and then start work to address that category, get that percentage up”.

Embedding standards takes time but Uplight are investing the time and energy in thinking about the social elements of standardisation and standards improvement as much as the technical implementation of creating checks and scorecards within Roadie.

## And what's next for Uplight?

In a word: ***campaigns***.

“Previously we ran these campaigns very loosely on Slack and with running lists and spreadsheets,” said Doug. Tech Insights tightened up these campaigns and removed the spreadsheets, but it didn’t remove all manual effort.

Currently, Uplight focus the attention on a subset of scorecards each month. This makes it easier to rollout and ensures that teams don’t get overwhelmed if they see a lot of new information in the scorecards.

Of the ten different categories of service delivery maturity that are now embedded into Uplight’s scorecards, only one or two are seen as the priority at any given time. These campaigns focus attention on the top priorities for the wider business and allow a simplicity of communication with teams.

“We started first with a ‘General’ scorecard. It focused on ownership, codeowner files, is there a GitHub slug, etc. It was effectively housekeeping.” That helped engineering teams build a mental model of what a campaign was going to be, what they needed to do, and what good looked like.

Next up came SLO reporting. Then architectural diagramming and documentation. Sometimes a campaign isn’t a full scorecard, it is a subset of checks from a given scorecard, or a few checks across different areas. This flexibility means that teams can understand a campaign is what the rest of Uplight is prioritising at that moment.

“We keep running campaigns at the rate of two or three per quarter to keep pushing up standards” said Doug.

### Manual Campaigns

Tech Insights helps here, but it currently doesn’t capture the totality of a campaign. To build an appropriate campaign, the Uplight team identifies what materials (golden paths, runbooks, tooling, supporting teams, etc) are missing and gather and prepare all that information before a campaign is announced. Then they use Tech Insights to measure adoption and offer assistance where needed.

The aspiration is greater than that though. Uplight wants to automate as much as possible and use Tech Insights more to drive the conversation, not just report progress.

As Doug puts it:

> “We want to put a scorecard front and center on everybody's access to the catalog and say 'This is the campaign. Work on these scorecard checks’ then put the data for that campaign in front of engineering managers and make leaderboards where teams can see how they can leverage knowledge from other teams to accelerate their adoption".

### Tech Insights Campaigns

Taking inspiration and feedback from Uplight, we’ll shortly be introducing functionality so that other customers can use Tech Insight insights in the same way that Uplight are.
Doug put it simply a few weeks ago:

> “Everything on your roadmap we will use, but if I could vote with *Roadie Bucks* I’d put my money on full campaigns inside Roadie.”

So that’s what we’re building.

An early version of *Roadie Tech Insights Campaigns* will be released this year. Roadie customers will be able to select a set of scorecards and checks, allocate a date and time, push those particular standards out to teams via cards on the homepage and entity pages, and monitor the ongoing campaign in a dashboard. External notifications to email and Slack for a Campaign will also be coming soon.

---

### [Growing and Governing an Internal Developer Portal in a Regulated business](https://roadie.io/case-studies/growing-and-governing-an-internal-developer-portal-in-a-regulated-business.md)

[Baillie Gifford & Co](https://www.bailliegifford.com/en/global/all-users/ "Baillie Gifford") is an independent investment management firm founded in Edinburgh in 1908. They invest in game-changing companies and other assets that can sustain growth and remain resilient in a changing world for decades to come.

I met with Chris Hawkins, Lead Software Architect at Baillie Gifford, to discuss how they’ve implemented Roadie and the lessons they’ve learnt while rolling it out across the organisation.

## Regulated businesses and the need for an IDP

Operating in a [highly regulated industry](https://www.bailliegifford.com/en/uk/individual-investors/legal-and-regulatory/#:~:text=Baillie%20Gifford%20Investment%20Management%20(Europe)%20Ltd%20(BGE)%20is,perform%20Individual%20Portfolio%20Management%20activities. "Baillie Gifford Regulatory Information") means discipline and clear lines of ownership are necessary when developing software at scale.

Regulators arrive with frightening regularity in such industries and important functions like Compliance, Security, Legal and Regulatory have requirements of what and how development teams need to demonstrate their compliance.

Auditing helps, but only partially. An annual external audit and periodic ISO audits, along with frequent internal audits, examine Software Development Lifecycle (SDLC) processes can demonstrate compliance but when they do find issues it is all retrospective. This is useful information, but suboptimal. Baillie Gifford wanted and needed to be on the front-foot, finding and resolving issues before the auditors told them something was wrong.

This need to demonstrate a steady hand on the tiller led Baillie Gifford to explore software catalogs and internal developer portals long before Backstage or Roadie existed. Back in the mid-2010s they were experimenting with portfolio management solutions and the last generation of IT catalogs in an effort to index the software they were building. Those efforts often involved individuals logging into the portal to keep things up to date, so quickly went stale after an initial surge of enthusiasm.

## Finding Backstage and moving to Roadie

According to Chris, Backstage’s focus on providing a developer portal which delivered values for development teams was the key shift. It was the thing that could enable their dream of a full and rich software catalog.

> “Backstage is a software catalog disguised as a Dev Portal and YAML is a better incentive to keep things up to date. That makes a huge difference.”

The desire to find a software catalog that worked for developers eventually paid off when the team discovered Backstage. “We had a call with Gartner about Internal Developer Portals - they said Backstage, OpsLevel, Cortex are the main players”.

Exploration of all three followed, and the team at Baillie Gifford soon found their way to Roadie. Roadie was GitHub-only at the time, while Baillie Gifford use Azure DevOps. Keen to get going, Chris and the team pursued a quick Proof of Concept to spin up a self-hosted Backstage instance to kick the tires on Backstage while Roadie integrated new providers to pull information from [Azure DevOps](https://roadie.io/docs/integrations/azure-devops/ "Azure DevOps Roadie Docs") and support their stack.

A few weeks later Baillie Gifford had a Roadie instance to start building upon.

## Filling in the Catalog

Baillie Gifford started simply - with a mass import of all the software they could find in their internal RBAC rules. As Chris puts it, 'we just grabbed everything that development teams own. We also have some third party stuff that we wanted to represent in the catalog like Microsoft Graph, but there’s a fuzzy line. Our Internal Audit and Information Assurance teams were pushing for 'get as much as possible in'.”

That resulted in a big tidying exercise.

> “People were assigned as owners and we focused on the Systems list. We said 'is that correct?', and if so we then moved on to Components, then Resources etc.”

## Driving adoption

### Tech Insights

The [Roadie Tech Insights](https://roadie.io/docs/tech-insights/introduction/ "Roadie Tech Insights") plugin proved useful in tracking the import and quality of data in the catalog, which drove further improvements. The team at Baillie Gifford have a Roadie Component Onboarding check.

> “We had comms to say 'you need to be doing this now', and we used that scorecard to show people what to do; set a soft deadline ' by the end of X we would like to see these improvements'.

Next came a focus on Rollups (a Tech Insights feature that allow you to look team-by-team at check and scorecard results). According to Chris, that information “helped us engage with a specific area to help move the dial.” Teams who needed to take action could see at a glance what they needed to do and where they were in comparison with their peers. A quick meeting with Tech Insights up on a screen was all that was required - adoption soon followed.

### Communications

Senior stakeholders also got involved. “We made sure the messaging was always also coming from the manager for a given area or some senior person - they communicate on our behalf as better visibility of what they are ultimately responsible for clearly benefits them”.

### Grassroots enthusiasm for TechDocs and the Scaffolder

Some areas of Roadie have seen unexpected growth, without prompting by the central team. [TechDocs](https://backstage.io/docs/features/techdocs/ "TechDocs") and [Scaffolder templates](https://backstage.io/docs/features/software-templates/ "Backstage Scaffolder Templates") are two such areas.

 “TechDocs is an area we struggled at first with but now it's blown up. It really took off - 304 docs in there now and it’s really proving useful”.

They’ve also now started to explore Scaffolder Templates in greater depth. This isn’t an initiative from Chris and the team at all. “Another team is running with that. They think it’s useful and we want to make more of it.”

## Hitting the limit of a centralised model

That shift brings new problems, like how do you help govern and constrain inputs when they’re growing organically. Chris and team ended up writing an Roadie onboarding guide for new joiners to Baillie Gifford to nudge teams in thinking through what they were doing. Even this has its limits: no central team can keep their eye on everything while also promoting free expression within the platform.

This shift from central direct and control is emblematic of the tipping point that many Backstage and Roadie adopters reach where the usage of the platform grows in unpredictable and undirected ways once a critical mass of useful information is in the catalog.

### Moving from centralised control to a decentralised ownership

With all pistons firing the initial catalog was soon complete and Baillie Gifford were well on their way to having a thriving Internal Developer Portal.

Chris and the team at Baillie Gifford had up to this point been driving the deployment of Roadie themselves. They had hunches about what would be useful and followed through, but they knew it would be the development teams that would now drive the endeavour forward.

Now that the building blocks were in place, they decided to move from a centralised model of control to a decentralised ‘working group’ model.

This is part of a wider attempt to encourage ‘Engagement Through Governance’.
While it is helpful to foster the growth of Roadie as an IDP within Baillie Gifford, this is about genuine ownership of the tools that teams use. As Chris puts, it’s about “giving developer teams a greater say in how Roadie is run.”

“The group involved is still relatively small, but we have now established the Roadie Working Group who now manage the catalog. At the moment it’s just representatives from 4-5 of our most active engineering teams, but we plan to grow it time”

Decentralised control is the answer so far to how to strike a balance between responsible usage of the catalog and expressive freedom for adding information that is useful. It is one of the key ways Baillie Gifford are keeping their Roadie instance healthy and sustainable for the future.

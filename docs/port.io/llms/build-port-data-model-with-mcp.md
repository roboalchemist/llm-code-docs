# Source: https://docs.port.io/guides/all/build-port-data-model-with-mcp.md

# Build your software catalog with MCP

Use Port's MCP (Model Context Protocol) server to build and manage your software catalog through natural language conversations with AI. This guide shows you how to create blueprints, populate entities and define relations by describing what you need in plain English.

Instead of manually configuring JSON schemas or clicking through UI forms, you can have conversations with your AI assistant to build your catalog iteratively, getting instant feedback and making adjustments on the fly.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* **Bootstrap new catalogs**: Describe your architecture and let AI create the initial blueprint structure.
* **Populate entities**: Ask AI to create services, teams, or environments based on your requirements.
* **Define relations**: Explain how components connect and let AI configure the relationships.
* **Set up actions**: Describe workflows you want to enable and have AI create self-service actions.
* **Create scorecards**: Explain quality standards and let AI build evaluation rules.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes you have:

* A basic understanding of [blueprints](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md) and [relations](/build-your-software-catalog/customize-integrations/configure-data-model/relate-blueprints/.md).
* Port's MCP server configured in your [IDE](/ai-interfaces/port-mcp-server/overview-and-installation.md?mcp-setup=cursor).

Permissions

MCP operations use the permissions of the authenticated user. Only users with appropriate access (typically admins) can create or modify blueprints, entities, and other catalog components.

## Create blueprints with AI[â](#create-blueprints-with-ai "Direct link to Create blueprints with AI")

Port's MCP server provides tools like `list_blueprints` and `upsert_blueprint` that enable AI agents to build your catalog through natural language conversations. You can describe what you need, and the AI will generate the appropriate JSON schema and create it in Port.

### Start with a simple description

Describe the blueprint you want to create in natural language. The AI will interpret your requirements and generate the appropriate schema.

**Example conversation:**

*"Create a microservice blueprint with properties for programming language, repository URL, and deployment status"*

The AI will use the MCP `upsert_blueprint` tool to generate and create the blueprint:

**Screenshot example (click to expand)**

![](/img/guides/MCPCreateBlueprint.png)

Iterative refinement

After creating a blueprint, you can refine it by asking follow-up questions like "Add a team property" or "Change the status enum to include 'maintenance'".

### Create multiple related blueprints

You can describe an entire architecture and let AI create multiple blueprints at once:

**Example conversation:**

*"Create blueprints for libraries, packages, and dependencies. Libraries should have properties for programming language and license type. Packages should have version and publish date properties. Dependencies should connect packages to libraries they depend on."*

The AI will:

1. Create the library blueprint with appropriate properties.
2. Create the package blueprint.
3. Create the dependency blueprint with relations to both package and library.
4. Configure the relationships between them.

* MCP server input
* Port output

![](/img/guides/MCPCreateBlueprintMultiple.png)

![](/img/guides/MCPCreateBlueprintMultiple2.png)

### Add computed properties

Describe aggregations and calculations you need, and AI will configure them:

**Example conversations:**

*"Add an aggregation property to the service blueprint that counts the number of open incidents from PagerDuty"*

* MCP server input
* Port output

![](/img/guides/MCPAggregationPropertyAddition.png)

![](/img/guides/MCPAggregationPropertyAdditionPort.png)

*"Add a calculation property that combines the service name and version into a display title"*

* MCP server input
* Port output

![](/img/guides/MCPCalculationPropertyAddition.png)

![](/img/guides/MCPCalculationPropertyAdditionPort.png)

The AI will add the appropriate `aggregationProperties` or `calculationProperties` section with the correct structure.

## Populate entities with AI[â](#populate-entities-with-ai "Direct link to Populate entities with AI")

Once you have blueprints, use AI to create entities. The MCP server provides the `upsert_entity` tool that works through natural language to create or update entities.

### Create individual entities

Describe the entity you want to create:

**Example conversation:**

*"Create a service called order-api with Python as the language, status active, and assign it to the platform team"*

* MCP server input
* Port output

![](/img/guides/MCPCreateEntity.png)

![](/img/guides/MCPCreateEntityPort.png)

### Bulk entity creation

You can describe multiple entities and let AI create them all:

**Example conversation:**

*"Create three services: payment-api (Node.js, active, payments team), user-service (Python, active, identity team), and notification-service (Go, experimental, platform team)"*

The AI will create all three entities with the correct properties and team assignments.

* MCP server input
* Port output

![](/img/guides/MCPCreateEntityMultiple.png)

![](/img/guides/MCPCreateEntityMultiplePortOutput.png)

### Update existing entities

Modify entities by describing the changes:

**Example conversation:**

*"Change the status of notification-service to active and update its description to include SMS and email capabilities"*

* MCP server input
* Port output

![](/img/guides/MCPCreateEntityUpdate.png)

![](/img/guides/MCPCreateEntityUpdatePort.png)

## Define relations with AI[â](#define-relations-with-ai "Direct link to Define relations with AI")

Relations connect entities in your catalog. AI can help you understand existing relations and create new ones based on your architecture.

### Query existing relations

Ask AI about how entities are connected:

**Example conversation:**

*"What services depend on the payment-database?"*

The AI uses `list_entities` with the `relatedTo` operator to traverse relationships and answer your question.

![](/img/guides/MCPQueryRelations.png)

### Update blueprint relations

Add new relations by describing them:

**Example conversation:**

*"Update the service blueprint to include a relation to databases. Services should be able to connect to multiple databases."*

The AI will use `upsert_blueprint` to add the relation configuration.

![](/img/guides/MCPUpdateBlueprintRelations.png)

## Best practices for AI-driven catalog building[â](#best-practices-for-ai-driven-catalog-building "Direct link to Best practices for AI-driven catalog building")

When using AI to build your catalog, follow these practices to get the best results:

### Be specific in your requests

The more detail you provide, the better AI can configure your catalog:

* **Good**: *"Create a service blueprint with properties for language (enum: Python, Node.js, Go), status (enum: active, deprecated), and a markdown description field"*
* **Less effective**: *"Create a service blueprint"*

### Iterate incrementally

Build your catalog in steps, refining as you go:

1. Start with basic blueprints and a few properties.
2. Add more properties and relations based on your needs.
3. Create entities to test the structure.
4. Adjust based on what works.

### Use consistent naming

Ask AI to follow consistent naming patterns across blueprints:

*"Use the same property name 'owning\_team' for team ownership across all blueprints"*

### Validate and review

After AI creates components, review them in the Port UI:

* Check that enums have the right values.
* Verify relations point to the correct blueprints.
* Test actions in a non-production environment first.

## Querying and managing your catalog[â](#querying-and-managing-your-catalog "Direct link to Querying and managing your catalog")

Once your catalog is built, use natural language to query and manage it:

* *"Show me all services owned by the platform team"*
* *"Give me a summary of services by deployment status"*

For more query examples and capabilities, see the [MCP server documentation](/ai-interfaces/port-mcp-server/available-tools.md).

## Related documentation[â](#related-documentation "Direct link to Related documentation")

* [Port MCP server overview](/ai-interfaces/port-mcp-server/overview-and-installation.md) - Installation and configuration for your IDE.
* [Available MCP tools](/ai-interfaces/port-mcp-server/available-tools.md) - Complete reference for all MCP tools and their capabilities.
* [Set up blueprints](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md) - Detailed blueprint configuration reference.

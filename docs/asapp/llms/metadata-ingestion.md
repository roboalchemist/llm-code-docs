# Source: https://docs.asapp.com/reporting/metadata-ingestion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metadata Ingestion API

> Learn how to send metadata via Metadata Ingestion API.

Customers with AI Services implementations use ASAPP's Metadata Ingestion API to send key attributes about conversations, customers, and agents. Developers can join metadata with AI Service output data to sort and filter reports and analyses using attributes important to your business.

<Note>
  Metadata Ingestion API is not accessible by default. Reach out to your ASAPP account contact to ensure it is enabled for your implementation.
</Note>

## Before You Begin

ASAPP provides an AI Services [Developer Portal](/getting-started/developers). Within the portal, developers can:

* Access relevant API documentation (e.g., OpenAPI reference schemas)
* Access API keys for authorization
* Manage user accounts and apps

In order to use ASAPP's APIs, all apps must be registered through the portal. Once registered, each app will be provided unique API keys for ongoing use.

<Tip>
  Visit the [Get Started](/getting-started/developers) page on the Developer Portal for instructions on creating a developer account, managing teams and apps, and setup for using AI Service APIs.
</Tip>

## Endpoints

The Metadata Ingestion endpoints are used to send information about agents, conversations, and customers. Metadata can be sent for a single entity (e.g., one agent) or for multiple entities at once (e.g., several hundred agents) in a batch format.

### Agent

The OpenAPI specification for each agent endpoint shows the types of metadata the API accepts. Examples include information about lines of business, groups, locations, supervisors, languages spoken, vendor, job role, and email.

The endpoints also accept custom-defined `attributes` in key-value pairs if no existing field in the schema suits the type of metadata you wish to upload.

* [`POST /metadata-ingestion/v1/single-agent-metadata`](/apis/metadata/add-an-agent-metadata)
  * Use this endpoint to add metadata for a single agent.

* [`POST /metadata-ingestion/v1/many-agent-metadata`](/apis/metadata/add-multiple-agent-metadata)
  * Use this endpoint to add metadata for a batch of agents all at once.

### Conversation

The OpenAPI specification for each conversation endpoint shows the types of metadata the API accepts. Examples include unique identifiers, lines of business, group and subdivision identifiers, routing codes, associated campaigns and business rules, browser and device information.

The endpoints also accept custom-defined `attributes` in key-value pairs if no existing field in the schema suits the type of metadata you wish to upload.

* [`POST /metadata-ingestion/v1/single-convo-metadata`](/apis/metadata/add-a-conversation-metadata)
  * Use this endpoint to add metadata for a single conversation.

* [`POST /metadata-ingestion/v1/many-convo-metadata`](/apis/metadata/add-multiple-conversation-metadata)
  * Use this endpoint to add metadata for a batch of conversations all at once.

### Customer

The OpenAPI specification for each customer endpoint shows the types of metadata the API accepts. Examples include unique identifiers, statuses, contact details, and location information.

The endpoints also accept custom-defined `attributes` in key-value pairs if no existing field in the schema suits the type of metadata you wish to upload.

* [`POST /metadata-ingestion/v1/single-customer-metadata`](/apis/metadata/add-a-customer-metadata)
  * Use this endpoint to add metadata for a single customer.

* [`POST /metadata-ingestion/v1/many-customer-metadata`](/apis/metadata/add-multiple-customer-metadata)
  * Use this endpoint to add metadata for a batch of customers all at once.

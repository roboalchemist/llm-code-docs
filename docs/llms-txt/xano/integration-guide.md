# Source: https://docs.xano.com/integration/integration-guide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Partner Integration Guide

> Learn how to integrate with Xano through programmatic backend building or by embedding your product into the Xano ecosystem.

We're thankful that you're considering integrating with Xano, and your user base will be as well. Xano offers a scalable, secure backend platform at the forefront of building visually, with code, with AI, or all three. We provide different ways to integrate, depending on your use case.

<CardGroup cols={2}>
  <Card title="I want my users to build a backend from my platform or service" icon="hammer-brush" href="#building-in-xano-from-your-platform-or-service">
    You can allow your users to build a backend from your platform or service by using the Metadata API or Xano MCP server.
  </Card>

  <Card title="I want my users to utilize my platform or service from within Xano" icon="share-nodes" href="#integrating-your-product-into-xano">
    You can allow your users to utilize your platform or service from within Xano by building a snippet or action that they can import into their Xano workspaces.
  </Card>
</CardGroup>

***

## Building in Xano from your platform or service

Xano provides a robust set of APIs that enable you to programmatically build a backend. This is done through the **Metadata API**, which gives you access to every aspect of the Xano system — from creating and managing database tables to building APIs, Reusable Functions, Tasks, and more. It's a great way to allow your users to, for example, build a backend for their app or website without leaving your platform.

The Metadata API has a significant number of endpoints available to you depending on what actions you want to offer to your users, and all they have to do is provide their own Metadata API access token from their Xano account. All of our users can generate these tokens and they do not require a paid plan to do so.

All of the features available through the Metadata API are also available through the Xano MCP server, which allows you to leverage AI agents and tool calls on your user's behalf.

<Card title="Metadata API Docs" icon="webhook" horizontal href="https://docs.xano.com/xano-features/metadata-api">
  Check out the full Metadata API docs
</Card>

<Card title="Xano MCP Server Docs" icon="robot" horizontal href="https://docs.xano.com/ai-tools/xano-mcp-server">
  Check out the full Xano MCP server docs
</Card>

## Integrating Your Product into Xano

In Xano, users can build an entire backend from scratch; this includes a database, logic for APIs, AI Agents, and more. If your service has REST or GraphQL API endpoints available, you can easily offer them to Xano users to utilize in their backend builds.

<Tip>
  You don't actually need to do anything here -- Xano users can call any external API they want already. The advantage to following this guide is all about visibility and control over the experience, enabling you to expand your reach to the Xano base in new ways, and making it much easier for them to use your service.
</Tip>

We have two different ways to integrate your product into Xano:

* **Actions**<br />
  Actions are a way to offer your service as a dependency-free function that Xano users can use in their backend builds. Dependency free just means that there are no database tables or other more complex additions; it's just the logic that's necessary.<br /><br />Actions can be built into Action Packages, allowing you to offer them as a single entity that can be installed into a Xano workspace while containing multiple separate Actions.<br /><br />

  This option is best for simple services that can be represented with nothing other than API calls. Users can try your Actions without even signing into Xano, which can get them to see the value of your platform or service faster.

  <Card title="Learn more about Actions and start building" icon="block-brick" horizontal href="/xano-actions/what-are-actions" />

* **Snippets**<br />
  Snippets are similar to Actions, but are more robust in that they can contain multiple APIs, AI Agents, database tables; anything that can be built in Xano can be included in a Snippet.<br /><br />

  This option is best if your service shines when it's integrated into a larger backend, or if you have a lot of complex logic that you want to offer to Xano users.

  <Card title="Learn more about Snippets and start building" icon="scissors" horizontal href="/xano-features/snippets" />


Built with [Mintlify](https://mintlify.com).
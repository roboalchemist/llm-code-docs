# Source: https://docs.xano.com/ai-tools/mcp-builder.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Builder

<Check>
  #### **Not looking for MCP, and just want to build chatbots or connect to your favorite AI models, like ChatGPT?**

  **Check out this resource instead:** [Chatbots](/building-backend-features/chatbots)
</Check>

<Info>
  **Quick Summary**

  **MCP** stands for Model Context Protocol, and is essentially a standardized way for AI models (also referred to as Large Language Models, or LLMs) to interact with other services.

  Think about the typical flow every time you interact with an AI. You, the **user**, utilize a **client**, like ChatGPT, to send instructions or ask questions to an **LLM**. The client is responsible for taking your input and transforming it into a way that the LLM you're interacting with can understand.

  With MCP in the mix, clients are able to take your input, and instruct an LLM on how to interact with *other* services and tools, like your Xano database, for example. Each separate task that is exposed to the client via the MCP standard is called a **tool**.

  Xano's **MCP Builder** feature allows you to build tools just like you build any other function stack and expose them to any client that supports the MCP standard, opening up the opportunity to build for AI, using the power of visual development in Xano.
</Info>

<CardGroup cols={2}>
  <Card icon="youtube" color="#bf0000" href="https://youtu.be/VQGjbBBY96s" img="/images/70212fa8-image.jpeg">
    **Introduction to MCP**
  </Card>

  <Card icon="youtube" color="#bf0000" href="https://youtu.be/5-K4nCW1YHE" img="/images/d15b18c8-image.jpeg">
    **Build an MCP Server in 10min or Less**
  </Card>

  <Card icon="youtube" color="#bf0000" href="https://youtu.be/5k6VcKu0AJU" img="/images/cbf3184d-image.jpeg">
    **MCP Tools and Functions**
  </Card>

  <Card icon="youtube" color="#bf0000" href="https://youtu.be/5M6Qx6-rcbo" img="/images/01921a63-image.jpeg">
    **Building an MCP Server & Client**
  </Card>
</CardGroup>

## Introduction to building MCP Servers in Xano

MCP stands for **Model Context Protocol**.

At its core, MCP is a standardized framework that enables seamless communication and interaction between AI models (especially Large Language Models, or LLMs) and external services. Think of it as a universal language and set of rules that allows AI models to go beyond their internal knowledge and capabilities by intelligently leveraging external data sources, tools, and functionalities.

Traditionally, interacting with external services from an AI model required complex and often proprietary integrations built into specific clients. MCP simplifies this by providing a consistent and structured way for client applications to describe available tools and instruct AI models on how to use them. This includes defining the tool's purpose, its input parameters, and how the AI model can expect to receive results.

## Why would I build MCP Servers in Xano?

Building MCP Servers in Xano offers a fundamental shift in how you integrate AI capabilities into your applications. Instead of being limited to building traditional REST APIs for standard web or mobile interactions, Xano's MCP Builder empowers you to create **AI-native functionalities**.

You can build function stacks in Xano specifically designed to be used by AI models. This means that you can create tools for your AI to:

* Retrieve specific data from your Xano database based on natural language queries

  <Frame><img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/da1ee881-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=ad3ba2b6ac793c9cf6227bba4713d70c" alt="" width="1444" height="366" data-path="images/da1ee881-image.jpeg" /></Frame>

* Perform complex data manipulations and calculations triggered by AI insights

  <Frame><img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b92c676d-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=430061dfefeb390ed42d1fbefacc1267" alt="" width="1444" height="366" data-path="images/b92c676d-image.jpeg" /></Frame>

* Write data back to your Xano database based on AI-driven decisions or user requests interpreted by the AI

  <Frame><img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/167802fb-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=8a92cee5ba975118bd09a751d3327bca" alt="" width="1444" height="366" data-path="images/167802fb-image.jpeg" /></Frame>

* Interact with other external APIs and services through your Xano function stacks, orchestrated by the AI

* Interact with your own APIs and services you've already built in Xano through the AI

## What's supported with Xano's MCP Builder?

We have built our current MCP support using the SSE transport method. Only tools are available at this time.

You can use any available function we have today in your MCP servers.

As MCP is an evolving protocol, we aim to continue to expand the functionality as it develops. If you are utilizing MCP in Xano and have any feedback or questions, please reach out to our support team.

## Getting Started with MCP Builder

### First, create an MCP Server.

To build MCP servers in Xano, we'll first need to create a server that will house some tools.

<Steps>
  <Step title="From the left-hand navigation menu, click AI Tools" />

  <Step title="Click + Add MCP Server to create your first MCP server" />

  <Step title="Fill out the necessary information">
    * **Name** - Give your server a name that clearly indicates its purpose.

    * **Description** - This is an internal field just for you to expand on the
      purpose of the MCP server.

    * **Allow Connections** - Choose whether or not to allow connections to this MCP server

    * **Add Tag** - Tag your MCP servers for easier search throughout your Xano workspace.

    * **MCP Instructions** - These instructions are what your clients will look at to understand the purpose of the MCP server. Markdown format is recommended for easy readability for your LLMs and clients. These instructions apply to the server as a whole, and are not used for individual tool instructions.
  </Step>
</Steps>

### After you've created a server, add some tools.

#### What is a tool?

Tools are essentially individual actions that your MCP server can perform, such as querying a database, adding new records, or calling an external API. You'll build tools just like you build any other function stack.

#### Tool Types

You'll select your tool type when connecting a tool to your MCP server, after it's been created.

<Card title="Tool" icon="hammer" horizontal>
  A tool is an action that your MCP server can perform. Each tool has its own set of logic that defines its behavior, such as querying a database, adding new records, or calling an external API.
</Card>

<Card title="Resource" icon="page" horizontal>
  Resources allow servers to share data that provides context to language models, such as files, database schemas, or application-specific information. Each resource is uniquely identified by a URI.
</Card>

From your MCP server, click the <span class="ui-bubble">⋮</span> icon next to the tool you want to change the type on, and select <span class="ui-bubble"><Icon icon="gear" />Connection Settings</span>. From there, you can change the tool type. For resource tools, make sure to specify a URI, which is what clients will use to reference the resource.

<Tip>Use the Resource tool type as part of building apps to run right inside of ChatGPT.<br /><br /><iframe width="560" height="315" src="https://www.youtube.com/embed/KjPMTeMuaeQ?si=Dw7ezTvkLe8OC-gI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen /></Tip>

### Using Existing Function Stacks as Tools

<Steps>
  <Step title="In the existing function stack, click the ⋮ settings icon in the upper-right corner and click Use As AI Tool" />

  <Step title="Choose the MCP Server you'd like to add the tool to, and give it a name. This name is what the command will be, so make sure it's understandable" />

  <Step title="Navigate to your MCP Server and check for the newly created tool">
    Xano will not make a copy of your existing function stack; instead, it will use a Run Endpoint function and call that API internally. This is ideal so you only have to maintain one function stack.

    <Frame caption="A tool created from an existing API endpoint">
            <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5d3f516b-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=8ff4d5282229416c6d9a733fcdb38c13" alt="" width="1987" height="1124" data-path="images/5d3f516b-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Adjust the settings for your newly created tool and add instructions">
    Instructions are important to have so the AI models and clients interacting with this tool understand how to use it.
  </Step>
</Steps>

### Creating Tools from Scratch

<Steps>
  <Step title="In your MCP Server, click + Add Tool" />

  <Step title="Fill out the required information">
    * **Name**
      * Give your tool a recognizable name. This is also the command that will be used to execute your tool.
    * **Description**
      * This is an internal-only field just for you to describe the purpose of the tool.
    * **Allow Connections**
      * Enable or disable connection to this specific tool
    * **Add Tag**
      * Tag your tools for easier search across your Xano workspace
    * **Authentication**
      * Determine if this tool requires an authentication token
    * **Tool Instructions**
      * These instructions are what your clients will use to understand how to send requests to the tool, and what the expected result will be. Markdown format is recommended.
  </Step>

  <Step title="Build your tool's function stack">
    If you haven't already, make sure you're familiar with Xano's [visual builder](/the-function-stack/building-with-visual-development).

    We also have some specific functions that may be useful to you when building tools that allow you to interact with existing function stacks.

    [MCP Functions](/ai-tools/mcp-builder/mcp-functions)
  </Step>

  <Step title="When you're ready, publish your changes" />
</Steps>

## MCP Authentication

<Warning>
  ## **Before you continue**

  It's important to understand that MCP is an evolving protocol. Authentication methods and best practices are in flux and may change. The best course of action right now for per-user authentication is to build a custom client that can authenticate your users.
</Warning>

Your MCP tools can have authentication enabled. The method of authentication is a bearer token, similar to the secure APIs you're already building in Xano. You'll include a valid token inside of your client's configuration (if you're using a ready-made client such as Claude Desktop or Cursor), and it will send that token along with your requests.

If you are building a publicly available application with its own user base, and need to make sure that your tools work across your set of users and separates data properly, you'll need to serve your own client that can handle dynamic authentication.

Our end-to-end MCP Server tutorial walks you through one example of building your own server and client, both using Xano.

<Frame>
  <iframe width="1000" height="500" src="https://www.youtube.com/embed/5M6Qx6-rcbo" title="Build an MCP Server and Client with Xano" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

## MCP Variables

When working with data as part of an MCP tool function stack, you have access to two special variables.

#### token

The Token variable contains a token that is passed as part of the connection URL. This token can be used for building custom authentication, or any other purpose that you see fit.

`https://your-xano-instance.xano.io/x2/mcp/67Dx5RNL/``token_here``/sse`

#### params

You can also pass URL parameters as a part of your connection URL, such as `?beta=true`

`https://yourxano.stage.xano.io/x2/mcp/67Dx5RNL/token_here/sse``?beta=true¶m=here`

You can use the URL parameters in your tool function stacks to determine the behavior of the tool(s).

## Hint

Use the token and / or params in combination with [Triggers](/building/logic/triggers/mcp-servers) for building powerful and complex MCP logic.

## Connecting to your MCP Server

Now that you've built an MCP server and added some tools to it, you can connect with your client of choice. Choose from the list below for a quick getting started guide.

If you're new to MCP servers, we recommend starting with Cursor.

#### [ Cursor](/ai-tools/mcp-builder/connecting-clients#cursor)

#### [ Claude Desktop](/ai-tools/mcp-builder/connecting-clients#claudedesktop)

***

## Best Practices & FAQs

There are some best practices when building tools that we recommend following for the best experience.

1. [**\*\***&#x55;se enum inputs wherever possible\*\*\*\*\*\*](/the-database/database-basics/field-types#enum) so the AI model understands what options are available for your inputs.
2. Use **clear naming conventions** and instructions.
3. **Try to find a balance when writing instructions** between being clear and descriptive, but also concise. Reducing the amount of tokens sent to an AI model will reduce token cost, improve speed, and improve responses.
4. **Use error handling with clear error messages**. If an AI model fails to use a tool, clear error messages will allow it to retry the tool successfully.

* **What are the benefits of using MCP?**
  * **Standardization:** MCP provides a common way for different applications and LLMs to interact, reducing the need for custom integrations.
  * **Interoperability:** MCP enables different LLMs and applications to work together more easily.
  * **Flexibility:** MCP allows developers to connect LLMs to a wide range of external resources.
  * **Efficiency:** MCP streamlines the process of building AI agents and applications.
* **Is MCP tied to a specific LLM or platform?**
  * No, MCP is designed to be an open and vendor-neutral protocol, allowing it to be used with various LLMs and platforms.
* **How does MCP relate to APIs?**
  * While APIs provide access to specific functions, MCP provides a standardized way for LLMs to discover and use those functions in a context-aware manner.
* **What is the role of "context" in MCP?**
  * Context is crucial in MCP. It provides the LLM with the necessary information about the user's request, the available tools, and the overall environment, enabling the LLM to make more informed decisions.
* **How is security handled in MCP?**
  * MCP emphasizes secure communication between clients and servers. Mechanisms like authentication, authorization, and secure data transfer are important considerations in MCP implementations.
* **Can I build multiple MCP servers?**
  * Yes, in Xano you can build multiple MCP servers and they can all have their own tools available.


Built with [Mintlify](https://mintlify.com).
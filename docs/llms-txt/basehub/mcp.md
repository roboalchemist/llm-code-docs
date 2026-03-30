# MCP

> You can use your agent tools provided by our MCP server and connect it to your favorite apps, like Claude and Cursor.

The MCP (Model Context Protocol) integration enables AI agents to interact directly with your BaseHub repository through a comprehensive set of tools. From creating and updating content blocks to managing assets and automating workflows, you can build functional websites, migrate hardcoded content, and set up forms—all through natural language prompts with your favorite AI tools.

info:

“MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.”

[More on Anthropic →](https://modelcontextprotocol.io/introduction)

## How to integrate

### Prerequsities

To use the BaseHub MCP, you should have [Cursor](https://cursor.com/) installed in your machine before integrating it.

### Go to “Connect” tab in your dashboard

![](https://assets.basehub.com/7b31fb4b/14d99cd919c63be1e7e3cb3adc872eb8/screenshot-2025-07-14-at-11.50.37-am.png?width=3840&quality=90&format=auto)

Developers -> Connect to your app -> Add to Cursor

### Click on “Add to Cursor”

The flow will ask you to open the “Cursor” app. After opening, it will show this config form.

![](https://assets.basehub.com/7b31fb4b/bb499c7d7575a766256cee3ab6386e6e/screenshot-2025-07-14-at-11.59.59-am.png?width=3840&quality=90&format=auto)

The default name always includes your repository name. This enables having multiple MCP Servers targeting different repositories.

### Finish your set-up

Rename the MCP server if you need and click “Install”. You’re ready to start building with Cursor + BaseHub. NOTE: Make sure to use Agent mode to let Cursor use BaseHub tools.

note:

In the background, this button adds the BaseHub MCP server URL to your Cursor config with a special BaseHub MCP Token that is linked to your user in BaseHub. This token gives read and write access to the LLM and saves the current ref where the LLM will work (`main` by default).

To set it up in Claude desktop, you should copy and paste the BaseHub MCP token by yourself.

## Available tools

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Tool Name

Description

`query_content`

Query the BaseHub repository content. Use this as you need to get content created by the user, or specific IDs for subsequent content changes.

`create_blocks`

Create one or more BaseHub blocks (with possible nested children).

`update_blocks`

Update existing blocks in BaseHub.

`delete_blocks`

Delete one or more BaseHub blocks in a single transaction. Only requires the block ID.

`commit`

Create a new commit in BaseHub, publishing all draft changes.

`merge_branch`

Merge a BaseHub branch into another branch.

`create_branch`

Create a new branch based on an existing branch in BaseHub. The new branch will be created from the specified base branch and optionally checked out.

`checkout_branch`

Checkout (switch to) a specific branch in BaseHub. NOTE: This changes the current working branch to the specified branch name for the Agent using the MCP, not for the user.

`get_current_ref`

Get the current BaseHub branch that the LLM is using.

`list_branches`

List all branches in the current BaseHub repository.

`get_upload_url`

Returns a signed URL where the LLM can upload assets to BaseHub.

`get_content_structure`

Retrieve the structure of the current BaseHub repository in XML format and possible block types.

`get_example_content_structure`

Get an XML representation of the structure of one of BaseHub example repos. This serves as inspiration on how to create structures in BaseHub.

`get_query_guidelines`

A helper tool that tells the LLM how to structure queries.

`get_mutation_guidelines`

A helper tool that tells the LLM how to structure mutations.

`search_developer_docs`

Search the BaseHub developer docs.

`get_token`

Get the repository read/write tokens.

## Use cases

### Start from scratch, create a fresh new website.

You can have a functional website in minutes with a good prompt and the help of BaseHub tools.

### Un-hardcode an existing piece of content from your site.

Incrementally implementing your content into the CMS has never been easier, push hardcoded content into BaseHub with just one prompt.

### Upload local images/videos/3D-models to your CMS.

The MCP supports asset uploading and lets the LLM know which steps to take to easily upload local files to BaseHub CDN

### Set up a newsletter form (or any kind of form) without writing a single line of code.

Simplify your integrations with LLMs work and BaseHub API transaction capabilities.
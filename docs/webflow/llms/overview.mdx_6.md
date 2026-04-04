# Source: https://developers.webflow.com/mcp/reference/overview.mdx

***

title: Webflow MCP server
description: Webflow's MCP server and AI tools for building with Webflow APIs
-----------------------------------------------------------------------------

<Frame>
  <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/307e7d3ea1afcd433f7d946be876f1e4f1bd55a6ad1b8d320b66d69b2bd611ab/products/assets/images/mcp_hero.png" alt="MCP Hero Image" />
</Frame>

The Model Context Protocol (MCP) server connects your AI tools directly to your Webflow projects. Prompt an AI agent to update designs, manage site data, and work with the CMS from your preferred AI environment.

For developers using AI-powered tools like [Claude Code](https://github.com/anthropics/claude-code), [Claude Desktop](https://claude.ai/download), [Cursor](https://www.cursor.com/), or [Windsurf](https://codeium.com/windsurf), the MCP server enhances an agent's understanding of your Webflow projects. It's built on Webflow's APIs, exposing them as tools your AI agent can use to create elements, styles, and variables on the canvas, as well as manage collections, custom code, assets, and other site data.

<Callout intent="success">
  **Why use the MCP server?**

  Skip writing API calls and managing authentication. Just describe what you want in natural language, and your AI agent handles the implementation using Webflow's Data and Designer APIs.
</Callout>

## What you can do

<Tabs>
  <Tab title="Build and design">
    Use Designer API tools to create and modify visual elements on the canvas:

    * **Create layouts**: Build responsive sections, containers, and grids with proper breakpoint configurations
    * **Style elements**: Apply classes, modify CSS properties, and manage design variables
    * **Build components**: Create reusable component definitions
    * **Design systems**: Set up color schemes, typography scales, and spacing systems
  </Tab>

  <Tab title="Manage content">
    Use Data API tools to work with your site's content and assets:

    * **CMS operations**: Create collections, define fields, and manage items with bulk updates
    * **Asset management**: Organize folders and optimize file sizes
    * **SEO optimization**: Update meta titles, descriptions, and Open Graph tags across pages
    * **Content auditing**: Scan for broken links, missing alt text, and outdated information

    <Accordion title="Example: Standardize collection fields">
      ```
      Ensure all items in my collection have featured images, complete descriptions,
      and SEO metadata. Add placeholder content where fields are empty.
      ```

      Your AI agent will:

      1. Fetch the collection schema and all items
      2. Identify items with missing featured images, descriptions, or meta tags
      3. Generate appropriate placeholder content based on existing item data
      4. Update items with the new content
      5. Generate a report showing what was added or updated
    </Accordion>
  </Tab>

  <Tab title="Automate workflows">
    Combine multiple tools to create sophisticated automation workflows:

    * **Content analysis**: Review blog posts, identify trends, and suggest new topics with SEO keywords
    * **Style refactoring**: Migrate legacy styles to design variables and modern breakpoint configurations
    * **Quality assurance**: Run automated checks for accessibility, performance, and SEO best practices
    * **Cross-site management**: Apply consistent changes across multiple Webflow projects

    <Accordion title="Example: Site-wide quality audit">
      ```
      Audit my site for broken links, missing alt text, and incomplete meta descriptions,
      then fix what you can automatically
      ```

      Your AI agent will:

      1. Scan all pages and CMS items for common issues
      2. Check internal and external links for broken references
      3. Identify images without alt text
      4. Find pages missing SEO metadata
      5. Automatically fix issues where possible
      6. Generate a detailed report with recommendations
    </Accordion>
  </Tab>
</Tabs>

## Try the beta improvements

We're testing significant improvements to the MCP server with better performance and developer experience. Sign up to get early access to the beta version.

<Callout intent="info">
  **What's new in beta:**

  * **Consolidated tools**: Simplified tool structure with fewer, more powerful tools
  * **Batch operations**: Update multiple items, pages, or elements in a single call
  * **Better performance**: Faster response times and optimized data transfer
  * **Faster calls**: Reduced latency for all API operations

  Plus: Priority support and direct feedback channel to the team
</Callout>

<WebflowForm />

## Get started

<Cards>
  <Card
    title="Install the MCP server"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/CircleArrowDown.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/CircleArrowDown.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/reference/getting-started"
  >
    Set up the Webflow MCP server in Claude Desktop, Cursor, or Windsurf with OAuth authentication.
  </Card>

  <Card
    title="Explore the prompt library"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Ai.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Ai.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/examples"
  >
    Browse ready-to-use prompts for image optimization, SEO audits, style refactoring, and more.
  </Card>

  <Card
    title="Review available tools"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/ToolNut.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/ToolNut.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/reference/how-it-works#available-tools"
  >
    See the complete list of Data API and Designer API tools you can use with your AI agent.
  </Card>

  <Card
    title="Learn how it works"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Resources.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Resources.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/reference/how-it-works"
  >
    Understand the architecture, authentication, and how the MCP server connects to Webflow's APIs.
  </Card>
</Cards>

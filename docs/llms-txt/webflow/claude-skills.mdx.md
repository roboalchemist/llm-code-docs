# Source: https://developers.webflow.com/mcp/reference/claude-skills.mdx

***

title: Claude skills
description: >-
Production-ready agent skills for Claude Code that work with the Webflow MCP
server
'og:title': Claude skills for Webflow MCP
'og:description': >-
Production-ready agent skills for content management, site optimization, and
safe publishing
'og:image':
type: fileId
value: 'https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/e2b355e4e186e25dd361fd84efedbd522eb9582bf092bd77c2c82fd32d571d0a/assets/images/claude-skills.jpg'
--------------------------------------------------

Claude skills are pre-built agent capabilities that help you accomplish common Webflow tasks through natural language. They work alongside the Webflow MCP server to provide specialized workflows for content management, site optimization, and safe publishing.

<Callout intent="info">
  **Prerequisites**

  Claude skills require both:

  * **Claude Code** - The official CLI tool from Anthropic
  * **Webflow MCP server** - Installed and configured in Claude Code

  If you haven't set up the MCP server yet, see the [getting started guide](/mcp/reference/getting-started).
</Callout>

## What are Claude skills?

Skills are specialized agent workflows that combine multiple MCP tools to accomplish specific tasks. Instead of manually orchestrating tool calls, you describe what you want and the skill handles the implementation details.

For example, rather than:

1. Manually fetching collection schemas
2. Reading each item individually
3. Validating field requirements
4. Updating items one by one

You can use the `bulk-cms-update` skill with a prompt like:

```
Update all blog posts to add a default featured image where missing
```

The skill automatically handles validation, generates a preview of changes, and asks for confirmation before applying updates.

## Available skills

<Tabs>
  <Tab title="Content management">
    ### Bulk CMS update

    Create or update multiple CMS items in a Webflow collection with validation and diff preview. Use when adding multiple blog posts, products, or updating fields across many items.

    **Example prompts:**

    ```
    Add 2 blog posts about Webflow MCP and update the first blog to say "Top" instead of "Best"
    ```

    ```
    Update all product prices by increasing them 10%
    ```

    ### CMS collection setup

    Create a new CMS collection in Webflow with specified fields and relationships. Use when setting up blog posts, products, team members, portfolios, or other content types with custom fields.

    **Example prompts:**

    ```
    Create a team members collection with name, bio, photo, and role fields
    ```

    ```
    Set up a products collection with pricing, categories, and related items
    ```

    ### CMS best practices

    Expert guidance on Webflow CMS architecture and best practices. Use when planning collections, setting up relationships, optimizing content structure, or troubleshooting CMS issues.

    **Example prompts:**

    ```
    I'm building a recipe site. How should I structure the CMS?
    ```

    ```
    My collection list is slow with 500+ items. How do I optimize?
    ```
  </Tab>

  <Tab title="Site health & optimization">
    ### Site audit

    Comprehensive audit of a Webflow site including pages, CMS collections, health scoring, and actionable insights. Use for site analysis, migration planning, or understanding site structure.

    **Example prompts:**

    ```
    Give me a complete inventory of my site
    ```

    ```
    Audit my site and show me the top issues to fix
    ```

    ### Asset audit

    Analyze assets on a Webflow site for SEO optimization. Identifies assets missing alt text and assets with non-SEO-friendly names, then generates and applies improvements.

    **Example prompts:**

    ```
    Run an asset audit on my site
    ```

    ```
    Find all images without alt text and add descriptive alt text
    ```

    ### Link checker

    Find and fix broken or insecure links across an entire site, including CMS content, to improve SEO and user experience. Audits HTTP/HTTPS issues and validates all internal and external links.

    **Example prompts:**

    ```
    Run a complete link check on my site and fix any issues
    ```

    ```
    Check all links in my blog posts
    ```
  </Tab>

  <Tab title="Publishing & code">
    ### Safe publish

    Publish a Webflow site with a plan-confirm-publish workflow. Shows what changed since last publish, runs pre-publish checks, and requires explicit confirmation before going live.

    **Example prompts:**

    ```
    Publish my site
    ```

    ```
    Show me what changed and publish if it looks good
    ```

    ### Custom code management

    Add, review, or remove inline custom scripts on a Webflow site (up to 10,000 chars). Use for analytics, tracking pixels, chat widgets, or any custom JavaScript.

    **Example prompts:**

    ```
    Add Google Analytics tracking to my site
    ```

    ```
    Review all custom code and remove any unused scripts
    ```
  </Tab>
</Tabs>

## Installation

<Steps>
  <Step title="Install via Claude Code marketplace">
    Use the Claude Code plugin system to install from the marketplace:

    ```bash
    # Add the marketplace
    claude plugin marketplace add webflow/webflow-skills

    # Install the plugin
    claude plugin install webflow-skills@webflow-skills
    ```

    After installation, restart Claude Code. Skills will be automatically invoked when relevant to your task.
  </Step>

  <Step title="Or install from local repository">
    Clone and install the repository directly:

    ```bash
    # Clone the repository
    git clone git@github.com:webflow/webflow-skills.git ~/webflow-skills

    # Install the plugin
    claude plugin install ~/webflow-skills
    ```
  </Step>

  <Step title="Verify installation">
    Open Claude Code and try a skill-related prompt:

    ```
    Audit my Webflow site for common issues
    ```

    If the `site-audit` skill is working, Claude Code will automatically invoke it and run a comprehensive health check.
  </Step>
</Steps>

## Updating skills

Keep your skills up to date to get the latest features and improvements:

```bash
# Update the marketplace index
claude plugin marketplace update

# Update the plugin
claude plugin update webflow-skills@webflow-skills
```

Or use the interactive plugin manager:

```bash
/plugin
```

## How skills work with MCP

Skills are implemented using the [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) open format. They work as specialized workflows that:

1. **Detect relevant tasks** - Skills activate automatically when your prompt matches their use case
2. **Orchestrate MCP tools** - Each skill combines multiple Webflow MCP tools in specific sequences
3. **Provide guardrails** - Skills include validation, error handling, and confirmation steps
4. **Return structured results** - You get clear summaries, previews, and actionable recommendations

The skills layer on top of the MCP server without requiring any changes to your MCP configuration. They simply make common workflows easier by packaging best practices into reusable patterns.

## Resources

<Cards>
  <Card
    title="View on GitHub"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Code.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Code.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="https://github.com/webflow/webflow-skills"
  >
    Explore the source code, contribute improvements, or report issues.
  </Card>

  <Card
    title="Prompt library"
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
    Browse example prompts that work with skills and the MCP server.
  </Card>

  <Card
    title="Getting started"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/ToolNut.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/ToolNut.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/reference/getting-started"
  >
    Learn how to set up and configure the Webflow MCP server.
  </Card>
</Cards>

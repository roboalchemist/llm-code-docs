# Source: https://docs.replit.com/tutorials/mcp-in-3.md

# Learn about MCP in 3 minutes

> Learn how to use Model Context Protocol (MCP) to give AI models access to tools, data sources, and real-world capabilities in just 3 minutes.

export const AuthorCard = ({img = "https://replit.com/cdn-cgi/image/width=256,quality=80,format=auto/https://storage.googleapis.com/replit/images/1730840970400_e885f16578bbbb227adbfeb7b979be34.jpeg", href = "https://youtube.com/@mattpalmer", name = "Matt Palmer", role = "Head of Developer Relations"}) => {
  return <a href={href} target="_blank" className="card block not-prose font-normal group relative my-2 ring-2 ring-transparent rounded-xl bg-white/50 dark:bg-codeblock/50 border border-gray-100 shadow-md dark:shadow-none shadow-gray-300/10 dark:border-gray-800/50 overflow-hidden cursor-pointer hover:!border-primary dark:hover:!border-primary-light">
      <div className="flex items-center gap-2 p-4">
        <div className="flex-shrink-0">
          <img src={img} alt={name} className="w-12 h-12 rounded-full object-cover" />
        </div>
        <div className="flex-grow">
          <h3 className="text-base font-semibold mb-0.5 text-inherit">{name}</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400 m-0">{role}</p>
        </div>
      </div>
    </a>;
};

<AuthorCard />

## Why AI models need MCP to connect with the real world

AI models like Claude and GPT are powerful but limited to what they were trained on. Without access to external tools and data sources, they can't:

* Access up-to-date information
* Interact with external systems
* Perform actions in the real world
* Work with your private data

## What MCP does: The universal connector for AI apps

Model Context Protocol (MCP) solves this by creating a universal way for AI to connect to tools and data sources - similar to how USB-C standardized device connections.

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/mcp.avif?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=fa8ad7a48e8e22fef036f6ef9c804536" data-og-width="1920" width="1920" data-og-height="1055" height="1055" data-path="images/tutorials/mcp.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/mcp.avif?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=20c309b5600a5e2e9a7af02f93542829 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/mcp.avif?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=494b1d2b1f3bf129299234a998e146b4 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/mcp.avif?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=138f74db5475550536469c66657aece5 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/mcp.avif?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=815c6f666f97669e1a4c92f470d7f085 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/mcp.avif?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=75be696bcba42da44eb501c6f673f33e 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/mcp.avif?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=cebc01d79208ff1ddfe41ed601440d81 2500w" />
</Frame>

MCP is a standardized protocol that allows AI models to:

* Access specialized tools and APIs
* Work with private data sources
* Perform actions in the real world
* Connect to other systems seamlessly

## How MCP works: Understanding the key components

The MCP architecture has three main components:

1. **The Client Side**: AI models like Claude or applications that need to access external tools
2. **The Communication Layer**: The protocol itself that standardizes how requests and responses are formatted
3. **The Server Side**: Programs that provide access to tools, data sources, and specialized capabilities

<AccordionGroup>
  <Accordion title="What's an MCP client?">
    An MCP client is something like Claude or a command-line interface that connects to a large language model (LLM). It's the device that needs to plug into external tools or data sources.

    Examples of MCP clients:

    * Claude in the browser
    * Command-line interfaces for AI
    * Custom applications built with AI SDKs
  </Accordion>

  <Accordion title="What's an MCP server?">
    An MCP server provides tools and capabilities to AI models. Think of it like giving AI a set of specialized tools to solve problems.

    Examples of what MCP servers enable:

    * Accessing specific data sources to answer questions
    * Connecting AI to APIs so it can go online
    * Enabling video summarization or transcript fetching
    * Writing files to your computer
    * Making calculations or running code
  </Accordion>
</AccordionGroup>

## MCP capabilities that extend AI functionality

MCP provides several key features that make it powerful for AI applications:

* **Resources**: Share data and content with AI models
* **Tools**: Let AI models perform actions through your services
* **Prompts**: Create reusable templates for consistent AI interactions
* **Sampling**: Allow your services to request information from AI models
* **Transports**: Connect clients and servers efficiently

## Try MCP yourself: Build an AI tool in minutes

<Frame>
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/zyDm-MJgDOA" title="Mastering MCP: The Ultimate Guide to AI Connectivity" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

<Steps>
  <Step title="Set up an MCP environment">
    Replit provides Templates that let you experiment with MCP without installing anything. These Templates include all the necessary components to connect AI models to useful tools.

    To get started quickly:

    1. Remix this template: [Learn about MCP](https://replit.com/@matt/Learn-about-MCP?v=1\&utm_source=matt\&utm_medium=blog\&utm_campaign=mcp-in-3)
    2. Wait for the environment to load completely
    3. You'll have a ready-to-use MCP setup with no configuration needed
  </Step>

  <Step title="Run a practical example">
    A simple demonstration shows how MCP enables AI to:

    1. Fetch a YouTube video using just a URL
    2. Get the content or transcript of that video
    3. Write a summary to a file on your system

    Try this command in our MCP Template:

    ```bash  theme={null}
    llm "Summarize this video https://youtu.be/1qxOcsj1TAg and write the summary to summary.txt"
    ```

    This demonstrates how MCP gives AI models abilities they wouldn't normally have.
  </Step>

  <Step title="Customize for your needs">
    Once you understand the basics, you can connect MCP servers to your own data sources or create custom tools that your AI can use to solve specific problems.
  </Step>
</Steps>

## Real-world applications you can build with MCP

MCP enables a wide range of powerful AI applications:

* **Customer service systems** that can access company databases to answer specific questions
* **Research assistants** that can search and summarize content from multiple sources
* **Productivity tools** that can interact with your files and applications
* **Content creation tools** that can access media libraries and publishing platforms

## Benefits of using MCP for your AI projects

MCP offers three key benefits:

* Ready-to-use integrations your AI can connect to immediately
* The ability to switch between different AI providers without rewriting your connections
* Security features that keep your sensitive data protected

This is transformative for developers building AI applications and for users who want AI that can do more than just generate text.

<Note>
  MCP is an emerging standard with growing support across the AI ecosystem. More tools and integrations are being added regularly.
</Note>

## Next steps: Go further with MCP development

<AccordionGroup>
  <Accordion title="Explore more MCP examples">
    * Check out Templates on Replit to experiment without installing anything
    * Look through the MCP protocol documentation to understand how it works
    * Join the MCP community to see what others are building
  </Accordion>

  <Accordion title="Build your own MCP server">
    * Create custom tools that connect to your data sources
    * Develop specialized capabilities for your AI applications
    * Share your MCP servers with the community
  </Accordion>

  <Accordion title="Resources">
    * [MCP Protocol Documentation](https://modelcontextprotocol.io)
    * [Anthropic MCP Starter](https://github.com/anthropics/mcp-starter)
    * [Everything you need to know about MCP](https://blog.replit.com/everything-you-need-to-know-about-mcp)
  </Accordion>
</AccordionGroup>

MCP might sound technical, but the concept is simple—it's about giving AI models access to tools and data through a standardized connection. This expands what AI can accomplish and makes building powerful AI applications more accessible to everyone.

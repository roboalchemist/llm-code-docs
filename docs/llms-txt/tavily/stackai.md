# Source: https://docs.tavily.com/documentation/integrations/stackai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# StackAI

> Using Tavily in StackAI to enhance your AI workflows with real-time web data.

## Introduction

Integrate [Tavily with StackAI](https://www.stack-ai.com/integrations/tavily) to enhance your AI workflows with real-time web data. With this integration, you can easily fetch and utilize live web content in your StackAI workflows.

<Frame>
  <img src="https://mintcdn.com/tavilyai/Y-5Alnz1le_K5S9f/images/stack_ai.gif?s=4caccb1ee81f9020296ce70cbbbd600c" alt="stackai" data-og-width="1280" width="1280" data-og-height="712" height="712" data-path="images/stack_ai.gif" data-optimize="true" data-opv="3" />
</Frame>

## How to set up Tavily with StackAI

<AccordionGroup>
  <Accordion title="Step 1: Log in to StackAI">
    <p>
      <a href="https://stack-ai.com/">Log in</a> to your StackAI account or
      self-hosted instance.
    </p>
  </Accordion>

  <Accordion title="Step 2: Create a New Workflow">
    <p>Create a new workflow or choose one of the available templates.</p>
  </Accordion>

  <Accordion title="Step 3: Add Tavily to Your Workflow">
    <p>**Option 1: Add Tavily as a Node**</p>

    <ul>
      <li>
        Search for "Tavily" under the **Apps** section in the left sidebar.
      </li>

      <li>Drag and drop the "Tavily" app into your canvas.</li>
    </ul>

    <p>**Option 2: Add Tavily as a Tool to an AI Agent**</p>

    <ul>
      <li>
        Choose between "Search", "Crawl", "Extract" or "Map" tool based on your
        needs.
      </li>
    </ul>

    **Configure the Tavily Node or Tool:**

    <ul>
      <li>
        In the Connect Tavily section, create a new connection by entering a
        connection name and your [Tavily API key](https://app.tavily.com/home).
      </li>
    </ul>

    **Configuring parameters:**
    <p>**For Search:**</p>

    <ul>
      <li>
        Enter your search <code>query</code> (can be manually entered or
        populated from another node's output)
      </li>

      <li>
        Select a <code>topic</code> ("general" or "news")
      </li>

      <li>Choose whether to include raw content or generate an answer</li>
      <li>Specify Maximum Search Results to return</li>
      <li>Set search depth and other optional parameters</li>
    </ul>

    <p>**For Extract:**</p>

    <ul>
      <li>
        Enter the URL(s) to extract content from (can be a single URL or
        multiple URLs from another node's output)
      </li>

      <li>Choose Extract Depth ("basic" or "advanced")</li>
      <li>Specify the output format ("markdown" or "text")</li>
    </ul>

    <p>**For Crawl:**</p>

    <ul>
      <li>Enter the **Root URL** to crawl</li>
      <li>Set the crawl instructions to guide the crawler</li>
      <li>Set the Limit on the number of pages to crawl</li>
    </ul>

    <p>**For Map:**</p>

    <ul>
      <li>Enter the **Root URL** to begin the mapping</li>
      <li>Set the map instructions to guide the mapping process</li>
      <li>Set the mapping depth to control how deep the mapping goes</li>
    </ul>

    <p>**Test:** Run the node to verify your configuration.</p>
  </Accordion>

  <Accordion title="Step 4: Process and Use Tavily Results">
    <p>Utilize the search, crawl, extract, or map results in your workflow:</p>

    <ul>
      <li>Process data through additional nodes</li>
      <li>Send information to your CRM, database, or email</li>
      <li>Generate reports or notifications</li>
      <li>Feed data into AI models for further processing</li>
    </ul>
  </Accordion>
</AccordionGroup>

## Use cases for Tavily in StackAI

Leverage Tavily's capabilities to create powerful automated workflows:

* **Job Search Automation**: Find and summarize new job postings, then send results to your inbox
* **Competitive Intelligence**: Automatically gather and analyze competitor information
* **Market Research**: Track industry trends and market developments
* **Content Curation**: Collect and organize relevant content for your business
* **Lead Enrichment**: Enhance lead data with real-time information
* **News Monitoring**: Stay updated with the latest developments in your field

## Detailed example - AI News Summary

Here's an example workflow that uses Tavily to search for the latest articles on "AI advancements" and sends a summary to your email:

<AccordionGroup>
  <Accordion title="Workflow Steps">
    <ol>
      <li>**Trigger:** Schedule the workflow to run daily</li>
      <li>**AI Agent:** Add an AI agent node to your workflow</li>

      <li>
        **Search:** The AI agent uses Tavily to find recent articles on “AI
        advancements”
      </li>

      <li>
        **Summarize:** The AI agent summarizes the most important news and
        trends
      </li>

      <li>
        **Delivery:** Send the summarized briefing via Email, Slack, or another
        integration
      </li>
    </ol>
  </Accordion>
</AccordionGroup>

## Best practices

To optimize your Tavily integration in StackAI:

* Tightly constrain Tavily queries to specific intent, time range, and domains to avoid noisy retrieval.
* Force concise, structured outputs (bullets/JSON with only required fields) to reduce tokens and parsing errors.

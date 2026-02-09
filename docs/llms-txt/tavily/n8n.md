# Source: https://docs.tavily.com/documentation/integrations/n8n.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# n8n

> Tavily is now available for no-code integration through n8n.

## Introduction

Integrate Tavily with n8n to enhance your workflows with real-time web search and content extraction—without writing code. With Tavily's powerful search and extraction capabilities, you can seamlessly integrate up-to-date online information into your n8n automations.

<Frame>
  <img src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/n8n.gif?s=bb9a9ca58010f04981df615e09d52971" alt="n8n" data-og-width="1108" width="1108" data-og-height="720" height="720" data-path="images/n8n.gif" data-optimize="true" data-opv="3" />
</Frame>

## How to set up Tavily with n8n

<AccordionGroup>
  <Accordion title="Step 1: Log in to n8n">
    <p><a href="https://n8n.io/">Log in</a> to your n8n account or self-hosted instance.</p>
  </Accordion>

  <Accordion title="Step 2: Create a New Workflow">
    <p>Create a new workflow and select a trigger node to start your automation.</p>
  </Accordion>

  <Accordion title="Step 3: Add Tavily to Your Workflow">
    <div>
      <p>
        <strong>Option 1: Add Tavily as a Node</strong><br />
        In the node library, search for <strong>Tavily</strong>. Add it to your workflow and choose between <strong>Search</strong> or <strong>Extract</strong> actions.
      </p>

      <p>
        <strong>Option 2: Add Tavily as a Tool to an AI Agent</strong><br />
        If you are building an AI agent workflow, you can add Tavily as a tool to your agent. This allows your agent to use Tavily for web search or content extraction as part of its reasoning process.
      </p>

      <p><strong>Connection:</strong> Connect your Tavily account by entering your <a href="https://app.tavily.com/home">Tavily API key</a>.</p>
      <p><strong>Configuration:</strong> Set up your parameters:</p>
      <p><strong>For Search:</strong></p>

      <ul>
        <li>Enter your search <code>query</code> (can be manually entered or populated from another node's output)</li>
        <li>Select a <code>topic</code> ("general" or "news")</li>
        <li>Choose whether to include raw content or generate an answer</li>
        <li>Specify domains to include or exclude</li>
        <li>Set search depth and other optional parameters</li>
      </ul>

      <p><strong>For Extract:</strong></p>

      <ul>
        <li>Enter the URL(s) to extract content from (can be a single URL or multiple URLs from another node's output)</li>
        <li>Choose extraction type ("basic" or "advanced")</li>
      </ul>

      <p><strong>Test:</strong> Run a test to verify your configuration.</p>
    </div>
  </Accordion>

  <Accordion title="Step 4: Process and Use Tavily Results">
    <div>
      <p>Utilize the search or extraction results in your workflow:</p>

      <ul>
        <li>Process data through additional nodes</li>
        <li>Send information to your CRM, database, or email</li>
        <li>Generate reports or notifications</li>
        <li>Feed data into AI models for further processing</li>
      </ul>
    </div>
  </Accordion>
</AccordionGroup>

## Use cases for Tavily in n8n

Leverage Tavily's capabilities to create powerful automated workflows:

* **Job Search Automation**: Find and summarize new job postings, then send results to your inbox
* **Competitive Intelligence**: Automatically gather and analyze competitor information
* **Market Research**: Track industry trends and market developments
* **Content Curation**: Collect and organize relevant content for your business
* **Lead Enrichment**: Enhance lead data with real-time information
* **News Monitoring**: Stay updated with the latest developments in your field

## Detailed example – Automated job search

Create an automated workflow that uses an AI agent with Tavily as a tool for web search to find new "Software Engineering Intern Roles" on the web, summarizes the results, and sends them to your email.

<Accordion title="Workflow Steps">
  <ol>
    <li><strong>Trigger:</strong> Schedule the workflow to run daily or weekly</li>
    <li><strong>AI Agent:</strong> Add an AI agent node to your workflow</li>
    <li><strong>Add Tavily as a Tool:</strong> In the AI agent configuration, add Tavily as a tool for web search</li>
    <li><strong>Search:</strong> The AI agent uses Tavily to find new "Software Engineering Intern Roles"</li>
    <li><strong>Summarize:</strong> The AI agent summarizes the search results using its LLM capabilities</li>
    <li><strong>Email:</strong> Use the Email node to send the summarized results to your inbox</li>
  </ol>
</Accordion>

## Best practices

To optimize your Tavily integration in n8n:

* Use the SplitInBatches node to process multiple search results efficiently
* Use filters to process only relevant results
* Use the Merge node to combine multiple search results

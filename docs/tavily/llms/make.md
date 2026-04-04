# Source: https://docs.tavily.com/documentation/integrations/make.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Make

> Tavily is now available for no-code integration through Make.

## Introduction

Integrate [Tavily with Make](https://www.make.com/en/integrations/tavily) to enhance your business processes without writing a single line of code. With Tavily's powerful search and content extraction capabilities, you can seamlessly integrate real-time online information into your Make workflows and automations.

<Frame>
  <img src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/make-tavily.gif?s=8c21f3b24b94f8648447746c67f92be6" alt="Make-Tavily" data-og-width="1060" width="1060" data-og-height="720" height="720" data-path="images/make-tavily.gif" data-optimize="true" data-opv="3" />
</Frame>

## How to set up Tavily with Make

<AccordionGroup>
  <Accordion title="Step 1: Log in to Make">
    <p><a href="https://www.make.com/en/login">Log in</a> to your Make account.</p>
  </Accordion>

  <Accordion title="Step 2: Create a New Scenario">
    <p>Create a new scenario and select a trigger module that will start your workflow.</p>
  </Accordion>

  <Accordion title="Step 3: Add Tavily as an Action Module">
    <div>
      <p>Add Tavily as an action module in your scenario and choose between **Perform a Search** or **Extract Raw Content**:</p>

      <p><strong>Connection:</strong> Connect your Tavily account by entering your [Tavily API key](https://app.tavily.com/home).</p>

      <p><strong>Configuration:</strong> Set up your parameters:</p>

      <p><strong>For Search:</strong></p>

      <ul>
        <li>Enter your search `query` (can be manually entered or populated from another module's output)</li>
        <li>Select a `topic` (`general` or `news`)</li>
        <li>Choose whether to include raw content or generate an answer</li>
        <li>Specify domains to include or exclude</li>
        <li>Set search depth and other optional parameters</li>
      </ul>

      <p><strong>For Extract:</strong></p>

      <ul>
        <li>Enter the URL(s) to extract content from (can be a single URL or multiple URLs from another module's output)</li>
        <li>Choose extraction type (`basic` or `advanced`)</li>
      </ul>

      <p><strong>Test:</strong> Run a test to verify your configuration.</p>
    </div>
  </Accordion>

  <Accordion title="Step 4: Process and Use Tavily Results">
    <div>
      <p>Utilize the search results in your workflow:</p>

      <ul>
        <li>Process data through additional modules</li>
        <li>Send information to your CRM or database</li>
        <li>Generate reports or notifications</li>
        <li>Feed data into AI models for further processing</li>
      </ul>
    </div>
  </Accordion>
</AccordionGroup>

## Use cases for Tavily in Make

Leverage Tavily's capabilities to create powerful automated workflows:

* **Competitive Intelligence**: Automatically gather and analyze competitor information
* **Market Research**: Track industry trends and market developments
* **Content Curation**: Collect and organize relevant content for your business
* **Lead Enrichment**: Enhance lead data with real-time information
* **News Monitoring**: Stay updated with the latest developments in your field

## Detailed example - automated market research

Create an automated workflow that performs market research and delivers insights to your team.

<Accordion title="Workflow Steps">
  <ol>
    <li><strong>Trigger:</strong> Schedule the scenario to run daily or weekly</li>
    <li><strong>Generate Search Queries:</strong> Use an AI module to create relevant search queries</li>
    <li><strong>Execute Searches:</strong> Use Tavily to perform multiple searches with the generated queries</li>
    <li><strong>Process Results:</strong> Filter and organize the search results</li>
    <li><strong>Generate Report:</strong> Use an AI module to create a comprehensive report</li>
    <li><strong>Deliver Insights:</strong> Send the report via email or to your team's communication platform</li>
  </ol>
</Accordion>

## Best practices

To optimize your Tavily integration in Make:

* Use the Iterator module to process multiple search results efficiently
* Use filters to process only relevant results
* Use the Aggregator module to combine multiple search results

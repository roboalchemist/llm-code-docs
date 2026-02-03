# Source: https://docs.tavily.com/documentation/integrations/tines.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tines

> Integrate Tavily with Tines for automated, no-code intelligence workflows.

## Introduction

Integrate [Tavily with Tines](https://www.tines.com/docs/credentials/connect-flows/tavily/) to enhance your automation workflows with powerful web search and content extraction capabilities. Tines' no-code platform makes it easy to incorporate Tavily's real-time search and data extraction features into your stories, enabling you to build powerful automation workflows without writing code.

## How to set up Tavily with Tines

<AccordionGroup>
  <Accordion title="Step 1: Log in to Tines">
    <p><a href="https://www.tines.com/">Log in</a> to your Tines account.</p>
  </Accordion>

  <Accordion title="Step 2: Create or Open a Story">
    <p>Create a new story or open an existing one where you want to add Tavily.</p>
  </Accordion>

  <Accordion title="Step 3: Add a Tavily Action">
    <div>
      <p>Follow these steps to add a Tavily action to your story:</p>

      <ol>
        <li>Navigate to the Templates section.</li>
        <li>Search for "Tavily" in the search bar.</li>
        <li>Drag the Tavily action into your story.</li>
        <li>Select a template between "Extract Web Content" and "Search the Web" based on your use case.</li>
        <li>Click on the Tavily connection to set up new credentials.</li>
        <li>Enter your Tavily API key in the provided field.</li>
      </ol>
    </div>
  </Accordion>

  <Accordion title="Step 4: Process and Use Tavily Results">
    <div>
      <p>Use Tines built-in actions to process Tavily's response:</p>

      <ul>
        <li>Parse and filter search results</li>
        <li>Enrich alerts or tickets with real-time intelligence</li>
        <li>Trigger notifications or follow-up actions based on findings</li>
      </ul>
    </div>
  </Accordion>
</AccordionGroup>

## Use cases for Tavily in Tines

* **Workbench Integration**: Connect Tavily to Tines Workbench (AI-powered chat interface) to enable real-time web search and content extraction directly in your conversations
* **Market & News Monitoring**: Track industry trends or breaking news relevant to your organization
* **Lead & Entity Enrichment**: Pull real-time data on companies, people, or technologies
* **Content Extraction**: Extract and analyze web content for deeper investigations

## Example Use Cases

<AccordionGroup>
  <Accordion title="Enrich new Airtable company records using Tavily search">
    <p>
      Enrich a company when it is added to an Airtable database. Receive a webhook notification when a new record is added and fill out the remaining fields with web searches powered by Tavily.<br />
      See the <a href="https://www.tines.com/library/stories/1312477/?name=enrich-new-airtable-company-records-using-tavily-searches" target="_blank">full story</a> on Tines' library.
    </p>
  </Accordion>

  <Accordion title="Search the internet with Tavily via Slack">
    <p>
      Search the internet using Tavily in response to a Slack slash command. Summarize the results and post them in a Slack thread, including source links. Users can click on the links to access more detailed information from the original sources.<br />
      See the <a href="https://www.tines.com/library/stories/1312847/?name=search-the-internet-with-tavily-via-slack" target="_blank">full story</a> on Tines' library.
    </p>
  </Accordion>
</AccordionGroup>

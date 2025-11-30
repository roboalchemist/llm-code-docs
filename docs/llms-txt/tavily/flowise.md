# Source: https://docs.tavily.com/documentation/integrations/flowise.md

# FlowiseAI

> Tavily is now available for integration through Flowise.

## Introduction

Integrate [Tavily with FlowiseAI](https://docs.flowiseai.com/integrations/langchain/tools/tavily-ai) to enhance your AI workflows with powerful web search capabilities. Flowise provides a no-code platform for building AI applications, and the Tavily integration offers real-time, accurate search results tailored for LLMs and RAG (Retrieval-Augmented Generation) systems.

Set up Tavily in Flowise to create chatflows or agent flows that can automate research, track news, or feed relevant data into your connected applications.

## How to set up Tavily with Flowise

Follow these steps to integrate Tavily with Flowise:

<AccordionGroup>
  <Accordion title="Step 1: Log in to Flowise">
    <div>[Login](https://flowiseai.com/) to your Flowise account.</div>
  </Accordion>

  <Accordion title="Step 2: Create a New Flow">
    <div>
      <p>Create a new flow in Flowise:</p>

      <ol>
        <li>Click "Create New Flow"</li>
        <li>Select either "Chat Flow" or "Agent Flow" as the type</li>
        <li>Name your flow (e.g., "Research Assistant")</li>
      </ol>
    </div>
  </Accordion>

  <Accordion title="Step 3: Add Tavily Node">
    <div>
      <p>Add the Tavily node to your flow:</p>

      <p><strong>For Chat Flow:</strong></p>

      <ol>
        <li>Click on the (+) button</li>
        <li>Navigate to <strong>LangChain > Tools > Tavily API</strong></li>
        <li>Drag the Tavily node into your flow</li>
      </ol>

      <p><strong>For Agent Flow:</strong></p>

      <ol>
        <li>Click on the (+) button</li>
        <li>Navigate to <strong>Tools > Tavily API</strong></li>
        <li>Drag the Tavily node into your flow</li>
      </ol>
    </div>
  </Accordion>

  <Accordion title="Step 4: Configure Tavily Node">
    <div>
      <p>Configure the Tavily node with your credentials and parameters:</p>

      <ol>
        <li>Enter your Tavily API key in the credentials section</li>

        <li>
          Configure additional parameters, for example:

          <ul>
            <li><strong>Search Depth:</strong> Choose between 'basic' or 'advanced'</li>
            <li><strong>Max Results:</strong> Set the number of results to return</li>
            <li><strong>Include Domains:</strong> Specify domains to include in search</li>
            <li><strong>Exclude Domains:</strong> Specify domains to exclude from search</li>
          </ul>
        </li>
      </ol>
    </div>
  </Accordion>

  <Accordion title="Step 5: Connect Nodes">
    <div>
      <p>Connect the Tavily node to other nodes in your flow:</p>

      <ol>
        <li>Connect to any node that accepts tool inputs</li>
        <li>Connect to an LLM node for query processing</li>
        <li>Connect to a Response node to format results</li>
      </ol>
    </div>
  </Accordion>
</AccordionGroup>

## Using Tavily in Flowise

Tavily can be utilized in various Flowise application types:

### Chatflow Applications

Flowise's Chatflow applications support Tavily tool node. This node allows you to automate tasks such as research, content curation, and real-time data integration into your workflows.

### Agent Applications

In Agent applications, you can integrate the Tavily tool to access web data in real time. Use this to:

* Retrieve structured and relevant search results
* Extract raw content for further processing
* Provide accurate, context-aware answers to user queries

<img src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/flowise-tavily.png?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=25e21b93e92b99d765eb7c0c4aba06c5" alt="Flowise Tavily Integration" width="400" height="300" data-og-width="926" data-og-height="1008" data-path="images/flowise-tavily.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/flowise-tavily.png?w=280&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=2baa34742d39bb8a29dc13e1c5658d81 280w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/flowise-tavily.png?w=560&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=827771e8502ad22a89cff1e564a8c550 560w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/flowise-tavily.png?w=840&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=9f6f8a85bac404c02610bd789fdfc20f 840w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/flowise-tavily.png?w=1100&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=238ad15bdd3a95a6134f2c4c44016179 1100w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/flowise-tavily.png?w=1650&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=92dce9d3f2d73ae75dce1592ec87950b 1650w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/flowise-tavily.png?w=2500&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=267b7f82ffcc878c31c8e607b834fc8b 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.tavily.com/llms.txt
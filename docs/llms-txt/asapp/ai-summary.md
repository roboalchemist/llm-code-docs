# Source: https://docs.asapp.com/ai-productivity/ai-summary.md

# AI Summary

> Use AI Summary to extract insights and data from your conversations

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autosummary/autosummary-home.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=41404b27ee171ec96677536583dea078" data-og-width="1408" width="1408" data-og-height="594" height="594" data-path="images/autosummary/autosummary-home.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autosummary/autosummary-home.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=b3118ff2877ac9cbcaaf95a28c7d6cf2 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autosummary/autosummary-home.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=3b509528dcdcc19bda26a309ea87f8c2 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autosummary/autosummary-home.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=1d3a9c04315ca023de3614e18eca75fa 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autosummary/autosummary-home.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=8ee2267bf81851ffdc3c383ce0e23106 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autosummary/autosummary-home.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=2a39c18ab02524f335b21e00db713926 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autosummary/autosummary-home.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=f983abbb69b7f3918722fbf65488892e 2500w" />
</Frame>

AI Summary provides a set of APIs to enable you to extract insights from the wealth of data generated when your agents talk to your customers.

AI Summary insights are powered by ASAPP's Generative AI (LLMs). Organizations use these insights to identify custom data, intents, topics, entities, sentiment drivers, and other structured data from every voice or chat (message) interaction between a customer and an agent.

AI Summary can be customized to your specific use cases such as workflows optimizations, trade confirmations, compliance monitoring and quality assurance etc.

## Insights and Data

With AI Summary, you can extract the following information:

| Insight                                                            | Description                                                                                                                                                                                                                                                                                                                                            | This enables you to                                                                                                                                                                                                                                                              |
| :----------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Free text summary](/ai-productivity/ai-summary/free-text-summary) | Generates a concise text summary of each conversation                                                                                                                                                                                                                                                                                                  | <ul><li>Reduces average handle time by eliminating post-call summarization.</li><li>Improves customer experience by allowing agents to focus on customers.</li></ul>                                                                                                             |
| [Intents](/ai-productivity/ai-summary/intent)                      | Identifies the topic-level categorization of the customer's primary issue or question                                                                                                                                                                                                                                                                  | <ul><li>Optimizes operations by analyzing contact reasons.</li><li>Improves customer experience through better conversation routing.​</li></ul>                                                                                                                                  |
| [Structured Data](/ai-productivity/ai-summary/structured-data)     | Extract specific, customizable data points from a conversation:​<ul><li>Question: Answers to predefined queries (e.g., "Was the customer issue resolved?", "Did the agent follow the script?")</li><li>Entities: Key information said in the conversation such as claim numbers, account details, approval dates, monetary amount, and more.</li></ul> | <ul><li>Automates data collection for analytics and reporting.</li><li> Facilitates compliance monitoring and quality assurance</li><li>Enables rapid population of CRMs and other business tools</li><li>Supports data-driven decision making and process improvement</li></ul> |

## Customizable

AI Summary is designed to be highly customizable to meet your specific business needs:

* **Free Text Summaries and Intents**: Train these features on your historical conversation data for optimal performance.
* **Structured Data**:
  * **Questions**: You have full control over the questions asked. Define any yes/no questions relevant to your business processes or compliance needs.
  * **Entities**: Configure the system to extract specific data points that matter most to your organization.

This level of customization ensures that AI Summary provides precisely the insights you need for your unique use cases.

## Implementation

AI Summary requires conversation transcripts to evaluate. You have multiple methods available to provide transcripts:

* API (Real-Time): Use the conversation API to upload conversations. This approach is addressed in the Getting Started.
* [AI Transcribe (speech-to-text service)](/ai-productivity/ai-transcribe): Use ASAPP's AI Transcribe  to transcribe your phone calls.
* [Salesforce plugin (for free text summaries only)](/ai-productivity/ai-summary/salesforce-plugin): If using Salesforce Chat, install our plugin to automatically handle the API interactions. Only free text summary supported.

<Card title="Getting Started" href="autosummary/getting-started" horizontal="true" icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.82 3H19C20.1 3 21 3.9 21 5V19C21 20.1 20.1 21 19 21H5C4.86 21 4.73 20.99 4.6 20.97C4.21 20.89 3.86 20.69 3.59 20.42C3.41 20.23 3.26 20.02 3.16 19.78C3.06 19.54 3 19.27 3 19V5C3 4.72 3.06 4.46 3.16 4.23C3.26 3.99 3.41 3.77 3.59 3.59C3.86 3.32 4.21 3.12 4.6 3.04C4.73 3.01 4.86 3 5 3H9.18H14.82ZM17 7H7V9H17V7ZM7 11H17V13H7V11ZM7 15H14V17H7V15ZM5 19H19V5H5V19Z" fill="#8056B0"/></svg>}> Learn how to start using AI Summary</Card>

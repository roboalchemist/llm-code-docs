# Source: https://docs.asapp.com/ai-productivity/ai-compose.md

# AI Compose

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autocompose/autocompose-home.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=cee9fe320b1776f90d2c5742e322eda3" data-og-width="1408" width="1408" data-og-height="594" height="594" data-path="images/autocompose/autocompose-home.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autocompose/autocompose-home.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=d6eabf4cb53b0f89bb134a4110dc875f 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autocompose/autocompose-home.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=a3051a57babea9dad3405415496971eb 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autocompose/autocompose-home.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=25167dee223503d1a0ee1ccce7eb6ff9 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autocompose/autocompose-home.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=8c9dd4f429981b9a6d2a0511ec5631de 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autocompose/autocompose-home.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=45cbb525c2766fb719f192e574b12bd7 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/autocompose/autocompose-home.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=eeba04790089c1124b769f997b92c687 2500w" />
</Frame>

ASAPP AI Compose helps agents compose the best response to customers, using machine learning techniques to suggest complete responses, partial sentences, key phrases and spelling fixes in real-time based on both the context of the conversation and past agent behavior.

## Features

AI Compose provides the following features:

| Feature                  | Description                                                                                                               |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| **Autosuggest**          | Provides up to three suggestions that appear in a suggestion drawer above the typing field before the agent begins typing |
| **Autocomplete**         | Provides up to three suggestions that appear in a suggestion drawer above the typing field after the agent begins typing  |
| **Phrase autocomplete**  | Provides in-line phrase suggestions that appear while an agent is typing                                                  |
| **Response quicksearch** | Allows in-line search of global and custom responses                                                                      |
| **Fluency correction**   | Applies automatic grammar corrections that an agent can undo                                                              |
| **Profanity blocking**   | Prevents an agent from sending a message containing profanity to the customer                                             |
| **Custom response list** | Enables management of an individual agent's custom responses in a simple library interface                                |
| **Global response list** | Enables management of global responses in a simple tooling interface                                                      |

## How it works

AI Compose takes in a live feed of your agent's conversations, and then using our various AI models, returns a list of changes or suggested responses based on the state of conversation and currently typed message.

1. Provide Conversation data via Conversation API.
2. In your Agent Application, call the AI Compose APIs to retrieve the list of changes or suggested responses.
3. Show the potential changes or responses to your Agent for them to incorporate.

This streamlines your agent's efficiency while still allowing agents to review changes, ensuring only the highest quality of responses are sent to your customers.

AI Compose has the following technical components:

| Component              | Description                                                                                                                          |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| **Autosuggest model**  | LLM Retrained by ASAPP with agent usage data                                                                                         |
| **Data Storage**       | A storage for historical conversations, global response lists and agent historical feature usage that are used for weekly retraining |
| **Conversation API**\* | An API for creating and updating conversations and conversation data                                                                 |

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efcbb75b-b38e-3cc1-4f44-1630dbe3c68b.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=11aff522949940bc1ab8369aa5849d73" data-og-width="1986" width="1986" data-og-height="1091" height="1091" data-path="image/uuid-efcbb75b-b38e-3cc1-4f44-1630dbe3c68b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efcbb75b-b38e-3cc1-4f44-1630dbe3c68b.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=9f411a0fda2f59605038821b7f57fe95 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efcbb75b-b38e-3cc1-4f44-1630dbe3c68b.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=4d5c6574b0bcf9ca000baadef4a7a576 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efcbb75b-b38e-3cc1-4f44-1630dbe3c68b.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=79139f71020f62ea35426edda76e794f 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efcbb75b-b38e-3cc1-4f44-1630dbe3c68b.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=2fe0ed4bf042aa57673d62f0871ea4f9 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efcbb75b-b38e-3cc1-4f44-1630dbe3c68b.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=39a3f8a9aa36e3af9bd31845a0ecf76e 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efcbb75b-b38e-3cc1-4f44-1630dbe3c68b.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=1f6a4bbea65aeb855605b27d7eaffa17 2500w" />
</Frame>

## Get Started

Integrate AI Compose into your applications and upscale your agent response rates.

### Integrate AI Compose

AI Compose is available both as an integration into leading messaging applications and as an API for custom-built messaging interfaces.

For technical instructions on how to implement the service for each approach, refer to the deployment guides below:

<Card title="AI Compose API" href="/ai-productivity/ai-compose/deploying-ai-compose-api">Learn more on the use of AI Compose API</Card>
<Card title="AI Compose for LivePerson" href="/ai-productivity/ai-compose/deploying-ai-compose-for-liveperson">Deploy AI Compose via LivePerson</Card>
<Card title="AI Compose for Salesforce" href="/ai-productivity/ai-compose/deploying-ai-compose-for-salesforce">Deploy AI Compose on your Salesforce solution</Card>

### Use AI Compose

For a functional breakdown and walkthrough of effective use cases and configurations, refer to the guides below:

<Card title="AI Compose Product Guide" href="/ai-productivity/ai-compose/product-guide">Learn more on the use of AI Compose</Card>
<Card title="AI Compose Tooling Guide" href="/ai-productivity/ai-compose/ai-compose-tooling-guide">Check the tooling options for AI Compose</Card>

### Feature Releases

<Card title="AI Compose Feature Releases" href="/ai-productivity/ai-compose/feature-releases">Visit the feature releases for new additions to AI Compose functionality</Card>

<Note>
  Product and Deployment Guides will be updated as new features become available in production.
</Note>

## Enhance AI Compose

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=e15f17e7467349a953d5de50b1a6deba" data-og-width="2002" width="2002" data-og-height="669" height="669" data-path="image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=83b1175647b735ab613d63d404023943 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=8894af02ee5ec88b5d28c05d4e2c5f0f 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=00832e5efa5a70c81708c39fae1b8711 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=737555976e74a97d853a82a19027faed 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6a565b9d628512b097143ef27e37ba60 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6267bcd225d2f1331bbcf41ff4193e65 2500w" />
</Frame>

ASAPP AI Summary is a recommended pairing with AI Compose, generating conversation summaries of key events for 100% of customer interactions.

Note-taking and disposition questions take call time and agent focus, both of which can have a negative impact on agent performance. Removing summarization tasks from agents through automation can keep agents focused on messaging with customers and yield higher summary data coverage than manual agent notes.

<CardGroup>
  <Card title="AI Summary" href="/ai-productivity/ai-summary">Head to AI Summary Overview to learn more.</Card>
  <Card title="AI Summary on ASAPP.com" href="https://www.asapp.com/products/ai-services/autosummary/">Learn more about AI Summary on ASAPP.com</Card>
</CardGroup>

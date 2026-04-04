# Reprocess a document.
Source: https://docs.mistral.ai/api/#tag/libraries_documents_reprocess_v1

post /v1/libraries/{library_id}/documents/{document_id}/reprocess

[Agents & Conversations]
Source: https://docs.mistral.ai/docs/agents/agents_and_conversations

### Objects

We introduce three new main objects that our API makes use of:
- **Agents**: A set of pre-selected values to augment model abilities, such as tools, instructions, and completion parameters.
- **Conversation**: A history of interactions, past events and entries with an assistant, such as messages and tool executions, Conversations can be started by an Agent or a Model.
- **Entry**: An action that can be created by the user or an assistant. It brings a more flexible and expressive representation of interactions between a user and one or multiple assistants. This allows for more control over describing events.

*You can also leverage all the features of Agents and Conversations without the need to create an Agent. This means you can query our API without creating an Agent, from using the built-in Conversations features to the built-in Connectors.*

To find all details visit our [Agents](https://docs.mistral.ai/api/#tag/beta.agents) and [Conversations](https://docs.mistral.ai/api/#tag/beta.conversations) API spec.

## Agent Creation

When creating an Agent, there are multiple parameters and values that need to be set in advance. These are:
- `model`: The model your agent will use among our available models for chat completion.
- `description`: The agent description, related to the task it must accomplish or the use case at stake.
- `name`: The name of your agent.
- `instructions` *optional*: The main instructions of the agent, also known as the system prompt. This must accurately describe the main task of your agent.
- `tools` *optional*: A list of tools the model can make use of. There are currently different `types` of tools:
  - `function`: User-defined tools, with similar usage to the standard function calling used with chat completion.
  - `web_search`/`web_search_premium`: Our built-in tool for web search.
  - `code_interpreter`: Our built-in tool for code execution.
  - `image_generation`: Our built-in tool for image generation.
  - `document_library`: Our built-in RAG tool for knowledge grounding and search on custom data.
- `completion_args` *optional*: Standard chat completion sampler arguments. All chat completion arguments are accepted.

### Creating an Agent
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key)

simple_agent = client.beta.agents.create(
    model="mistral-medium-2505",
    description="A simple Agent with persistent state.",
    name="Simple Agent"
)
```
When creating an agent, you will receive an Agent object with an agent ID. You can then use that ID to have conversations.

Here is an example of a Web Search Agent using our built-in tool:
```py
websearch_agent = client.beta.agents.create(
    model="mistral-medium-2505",
    description="Agent able to search information over the web, such as news, weather, sport results...",
    name="Websearch Agent",
    instructions="You have the ability to perform web searches with `web_search` to find up-to-date information.",
    tools=[{"type": "web_search"}],
    completion_args={
        "temperature": 0.3,
        "top_p": 0.95,
    }
)
```

You can find more information [here](../connectors/websearch).
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript


dotenv.config();

const apiKey = process.env.MISTRAL_API_KEY;

const client = new Mistral({ apiKey: apiKey });

async function main() {
  let websearchAgent = await client.beta.agents.create({
    model: "mistral-medium-latest",
    name: "WebSearch Agent",
    instructions: "Use your websearch abilities when answering requests you don't know.",
    description: "Agent able to fetch new information on the web.",
    tools: [{ type: "web_search" }],
  });
}
```

  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/agents" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "model": "mistral-medium-latest",
     "name": "Simple Agent",
     "description": "A simple Agent with persistent state."
  }'
```

  </TabItem>
</Tabs>

<details>
    <summary><b>JSON Output</b></summary>

```json
{
  "model": "mistral-medium-2505",
  "name": "Simple Agent",
  "id": "ag_0684fe0e0b98773e8000323fc71a3986",
  "version": 0,
  "created_at": "2025-06-16T09:16:16.726715Z",
  "updated_at": "2025-06-16T09:16:16.726718Z",
  "instructions": null,
  "tools": [],
  "completion_args": {
    "stop": null,
    "presence_penalty": null,
    "frequency_penalty": null,
    "temperature": 0.3,
    "top_p": null,
    "max_tokens": null,
    "random_seed": null,
    "prediction": null,
    "response_format": null,
    "tool_choice": "auto"
  },
  "description": "A simple Agent with persistent state.",
  "handoffs": null,
  "object": "agent"
}
```
</details>

### Updating an Agent

After creation, you can update the Agent with new settings if needed. The arguments are the same as those used when creating an Agent.  
The result is a new `version` of the Agent with the new settings, you can this way have the previous and new versions available.

#### Create a new Version
Create a new `version` of the Agent, will be used by default.
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py
simple_agent = client.beta.agents.update(
    agent_id=simple_agent.id, 
    description="An edited simple agent.",
    completion_args={
        "temperature": 0.3,
        "top_p": 0.95,
    }
)
```

  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
websearchAgent = await client.beta.agents.update({
    agentId: websearchAgent.id, 
    agentUpdateRequest: {
        completionArgs: {
            temperature: 0.3,
            topP: 0.95,
        },
        description: "An edited simple agent."
    },
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/agents/<agent_id>" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "completion_args": {
       "temperature": 0.3,
       "top_p": 0.95
     },
     "description": "An edited simple agent."
  }'
```

  </TabItem>
</Tabs>

<details>
    <summary><b>JSON Output</b></summary>

```json
{
  "model": "mistral-medium-2505",
  "name": "Simple Agent",
  "id": "ag_0684fe0e0b98773e8000323fc71a3986",
  "version": 1,
  "created_at": "2025-06-16T09:16:16.726715Z",
  "updated_at": "2025-06-16T09:17:19.872254Z",
  "instructions": null,
  "tools": [],
  "completion_args": {
    "stop": null,
    "presence_penalty": null,
    "frequency_penalty": null,
    "temperature": 0.3,
    "top_p": 0.95,
    "max_tokens": null,
    "random_seed": null,
    "prediction": null,
    "response_format": null,
    "tool_choice": "auto"
  },
  "description": "An edited simple agent.",
  "handoffs": null,
  "object": "agent"
}
```
</details>

#### Change Version
Change manually the version of the Agent.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py
simple_agent = client.beta.agents.update_version(
    agent_id=simple_agent.id, 
    version=0
)
```

  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
websearchAgent = await client.beta.agents.updateVersion({
    agentId: websearchAgent.id, 
    version: 0
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/agents/<agent_id>/version" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "version": 0
  }'
```

  </TabItem>
</Tabs>

<details>
    <summary><b>JSON Output</b></summary>

```json
{
  "model": "mistral-medium-2505",
  "name": "Simple Agent",
  "id": "ag_0684fe0e0b98773e8000323fc71a3986",
  "version": 0,
  "created_at": "2025-06-16T09:16:16.726715Z",
  "updated_at": "2025-06-16T09:18:04.624549Z",
  "instructions": null,
  "tools": [],
  "completion_args": {
    "stop": null,
    "presence_penalty": null,
    "frequency_penalty": null,
    "temperature": 0.3,
    "top_p": null,
    "max_tokens": null,
    "random_seed": null,
    "prediction": null,
    "response_format": null,
    "tool_choice": "auto"
  },
  "description": "A simple Agent with persistent state.",
  "handoffs": null,
  "object": "agent"
}
```
</details>

## Conversations

Once your agent is created, you can **start** conversations at any point while keeping the same conversation persistent. You first start a conversation by providing:
- `agent_id`: The ID of the agent, created during the Agent creation.
- `inputs`: The message to start the conversation with. It can be either a string with the first user message or question, or the history of messages.  

Creating a Conversation will return a conversation ID.

To **continue** the conversation and append the exchanges as you go, you provide two values:
- `conversation_id`: The ID created during the conversation start or append that maps to the internally stored conversation history.
- `inputs`: The next message or reply. It can be either a string or a list of messages.  

A new Conversation ID is provided at each append.

You can also **opt out** from the automatic storing with `store=False`; this will make the new history not being stored on our cloud.  

We also provide the parameter `handoff_execution`, which currently has two modes: `server` or `client`.
- `server`: Runs the handoff as expected internally on our cloud servers; this is the default setting.
- `client`: When a handoff is triggered, a response is provided directly to the user, enabling them to handle the handoff with control.  

For more information regarding handoffs visit [this section](../agents/handoffs).

### Starting a Conversation
<Tabs groupId="code">
  <TabItem value="python" label="python" default>
  
```py
response = client.beta.conversations.start(
    agent_id=simple_agent.id,
    inputs="Who is Albert Einstein?",
    #store=False
)
```
or...
```py
response = client.beta.conversations.start(
    agent_id=simple_agent.id,
    inputs=[{"role": "user", "content": "Who is Albert Einstein?"}],
    #store=False
)
```
Both options are equivalent.

Without an Agent, querying Conversations could look like so:
```py
response = client.beta.conversations.start(
    model="mistral-medium-latest",
    inputs=[{"role": "user", "content": "Who is Albert Einstein?"}],
    #store=False
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
let conversation = await client.beta.conversations.start({
      agentId: websearchAgent.id,
      inputs:"Who is Albert Einstein?",
      //store:false
});
```
or...
```typescript
let conversationMultipleEntries = await client.beta.conversations.start({
    agentId: websearchAgent.id,
    inputs:[{role: "user", content:"Who is Albert Einstein?"}],
    //store:false
});
```
Both options are equivalent.

Without an Agent, querying Conversations could look like so:
```typescript
let conversationMultipleEntries = await client.beta.conversations.start({
    model: "mistral-medium-latest",
    inputs:[{role: "user", content:"Who is Albert Einstein?"}],
    //store:false
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/conversations" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "inputs": "Who is Albert Einstein?",
     "stream": false,
     "agent_id": "<agent_id>"
  }'
```
or
```bash
curl --location "https://api.mistral.ai/v1/conversations" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "inputs": [
       {
         "role": "user",
         "content": "Who is Albert Einstein?",
         "object": "entry",
         "type": "message.input"
       }
     ],
     "stream": false,
     "agent_id": "<agent_id>"
  }'
```
  </TabItem>
</Tabs>

<details>
    <summary><b>JSON Output</b></summary>

```json
{
  "conversation_id": "conv_0684fe18cbc57ba6800065acdd2b6c85",
  "outputs": [
    {
      "content": "Albert Einstein was a German-born theoretical physicist who is widely regarded as one of the most influential scientists of the 20th century. He is best known for developing the theory of relativity, which revolutionized our understanding of space, time, and energy. Einstein's work also made significant contributions to the development of quantum mechanics and statistical mechanics.\n\nSome of his most notable achievements include:\n\n1. **Special Theory of Relativity (1905)**: This theory introduced the idea that the laws of physics are the same for all non-accelerating observers and that the speed of light in a vacuum is constant, regardless of the observer's motion.\n\n2. **General Theory of Relativity (1915)**: This theory extended the principles of special relativity to include gravity, describing it as a property of the geometry of space and time.\n\n3. **Mass-Energy Equivalence (E=mc²)**: This famous equation from his special theory of relativity shows that mass and energy are interchangeable.\n\n4. **Photoelectric Effect**: Einstein's explanation of the photoelectric effect, which suggested that light could be described as discrete packets of energy (quanta or photons), was a pivotal step in the development of quantum theory.\n\nEinstein was awarded the Nobel Prize in Physics in 1921 for his explanation of the photoelectric effect. He was also known for his humanitarian efforts and his advocacy for civil rights and peace. Einstein emigrated to the United States in the 1930s to escape the rise of the Nazi regime in Germany and became a professor at the Institute for Advanced Study in Princeton, New Jersey, where he spent the remainder of his career.\n\nEinstein's work continues to influence modern physics and our understanding of the universe. He passed away on April 18, 1955.",
      "object": "entry",
      "type": "message.output",
      "created_at": "2025-06-16T09:19:09.031905Z",
      "completed_at": "2025-06-16T09:19:15.138424Z",
      "id": "msg_0684fe18d08278058000efa70b28fa5a",
      "agent_id": "ag_0684fe0e0b98773e8000323fc71a3986",
      "model": "mistral-medium-2505",
      "role": "assistant"
    }
  ],
  "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 370,
    "total_tokens": 378,
    "connector_tokens": null,
    "connectors": null
  },
  "object": "conversation.response"
}
```
</details>

### Continue a Conversation
You can continue the conversation; the history is stored when using the correct conversation ID.
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py 
response = client.beta.conversations.append(
    conversation_id=response.conversation_id,
    inputs="Translate to French."
)
```

  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
conversation = await client.beta.conversations.append({
    conversationId: conversation.conversationId,
    conversationAppendRequest:
    {
        inputs:[{role: "user", content:"Who is Albert Einstein?"}],
        completionArgs: {
            temperature: 0.3,
            topP: 0.95,
        }
    },
    //store:false
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/conversations/<conv_id>" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "inputs": "Translate to French.",
     "stream": false,
     "store": true,
     "handoff_execution": "server"
  }'
```
  </TabItem>
</Tabs>

<details>
    <summary><b>JSON Output</b></summary>

```json
{
  "conversation_id": "conv_0684fe18cbc57ba6800065acdd2b6c85",
  "outputs": [
    {
      "content": "Albert Einstein était un physicien théoricien né en Allemagne, largement considéré comme l'un des scientifiques les plus influents du 20ᵉ siècle. Il est surtout connu pour avoir développé la théorie de la relativité, qui a révolutionné notre compréhension de l'espace, du temps et de l'énergie. Les travaux d'Einstein ont également apporté des contributions significatives au développement de la mécanique quantique et de la mécanique statistique.\n\nParmi ses réalisations les plus notables, on peut citer :\n\n1. **Théorie de la relativité restreinte (1905)** : Cette théorie a introduit l'idée que les lois de la physique sont les mêmes pour tous les observateurs non accélérés et que la vitesse de la lumière dans le vide est constante, indépendamment du mouvement de l'observateur.\n\n2. **Théorie de la relativité générale (1915)** : Cette théorie a étendu les principes de la relativité restreinte pour inclure la gravité, la décrivant comme une propriété de la géométrie de l'espace et du temps.\n\n3. **Équivalence masse-énergie (E=mc²)** : Cette équation célèbre de sa théorie de la relativité restreinte montre que la masse et l'énergie sont interchangeables.\n\n4. **Effet photoélectrique** : L'explication d'Einstein de l'effet photoélectrique, qui suggérait que la lumière pouvait être décrite comme des paquets discrets d'énergie (quanta ou photons), a été une étape décisive dans le développement de la théorie quantique.\n\nEinstein a reçu le prix Nobel de physique en 1921 pour son explication de l'effet photoélectrique. Il était également connu pour ses efforts humanitaires et son engagement en faveur des droits civiques et de la paix. Einstein a émigré aux États-Unis dans les années 1930 pour échapper à la montée du régime nazi en Allemagne et est devenu professeur à l'Institut d'études avancées de Princeton, dans le New Jersey, où il a passé le reste de sa carrière.\n\nLes travaux d'Einstein continuent d'influencer la physique moderne et notre compréhension de l'univers. Il est décédé le 18 avril 1955.",
      "object": "entry",
      "type": "message.output",
      "created_at": "2025-06-16T09:19:56.901953Z",
      "completed_at": "2025-06-16T09:20:03.257737Z",
      "id": "msg_0684fe1bce6e72bc8000f89d886633fe",
      "agent_id": "ag_0684fe0e0b98773e8000323fc71a3986",
      "model": "mistral-medium-2505",
      "role": "assistant"
    }
  ],
  "usage": {
    "prompt_tokens": 384,
    "completion_tokens": 471,
    "total_tokens": 855,
    "connector_tokens": null,
    "connectors": null
  },
  "object": "conversation.response"
}
```
</details>

### Retrieve Conversations
You can retrieve conversations; both all available already created and the details of each.

Retrieve conversations available:
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py 
conversations_list = client.beta.conversations.list(
    page=0, page_size=100
)
```

  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
let conversationList = await client.beta.conversations.list({
    page: 0,
    pageSize: 100
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/conversations?page=0&page_size=100" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```

  </TabItem>
</Tabs>

<details>
    <summary><b>JSON Output</b></summary>

```json
[
  {
    "id": "conv_0684fe18cbc57ba6800065acdd2b6c85",
    "created_at": "2025-06-16T09:19:08.735790Z",
    "updated_at": "2025-06-16T09:20:03.273654Z",
    "agent_id": "ag_0684fe0e0b98773e8000323fc71a3986",
    "name": null,
    "description": null,
    "object": "conversation"
  },
  {
    "id": "conv_0684fd306df172f2800051d4f82d4a8b",
    "created_at": "2025-06-16T08:17:10.871401Z",
    "updated_at": "2025-06-16T08:17:10.871402Z",
    "model": "mistral-medium-2505",
    "instructions": "check if it has tool calls",
    "tools": [],
    "completion_args": {
      "stop": null,
      "presence_penalty": null,
      "frequency_penalty": null,
      "temperature": 0.0,
      "top_p": null,
      "max_tokens": 1000,
      "random_seed": null,
      "prediction": null,
      "response_format": null,
      "tool_choice": "auto"
    },
    "name": null,
    "description": null,
    "object": "conversation"
  },
  ...
  {
    "id": "conv_0684fd176fba7a4880001e21144b6a00",
    "created_at": "2025-06-16T08:10:30.983084Z",
    "updated_at": "2025-06-16T08:10:30.983085Z",
    "model": "mistral-medium-2505",
    "instructions": "check if it has tool calls",
    "tools": [],
    "completion_args": {
      "stop": null,
      "presence_penalty": null,
      "frequency_penalty": null,
      "temperature": 0.3,
      "top_p": null,
      "max_tokens": null,
      "random_seed": null,
      "prediction": null,
      "response_format": null,
      "tool_choice": "auto"
    },
    "name": null,
    "description": null,
    "object": "conversation"
  },
  {
    "id": "conv_0684fd151a46729580002ff86353ebcb",
    "created_at": "2025-06-16T08:09:53.642147Z",
    "updated_at": "2025-06-16T08:09:53.642148Z",
    "model": "mistral-medium-2505",
    "instructions": "check if it has tool calls",
    "tools": [],
    "completion_args": {
      "stop": null,
      "presence_penalty": null,
      "frequency_penalty": null,
      "temperature": 0.0,
      "top_p": null,
      "max_tokens": 1000,
      "random_seed": null,
      "prediction": null,
      "response_format": {
        "type": "json_schema",
        "json_schema": null
      },
      "tool_choice": "auto"
    },
    "name": null,
    "description": null,
    "object": "conversation"
  },
  ...
  {
    "id": "conv_0684efea24637995800022373f1405cb",
    "created_at": "2025-06-15T17:10:58.274332Z",
    "updated_at": "2025-06-15T17:10:58.274334Z",
    "agent_id": "ag_0684efea22ed758e80008aae99df024c",
    "name": null,
    "description": null,
    "object": "conversation"
  },
  {
    "id": "conv_0684efe3c5b47aeb80005bbb300bf035",
    "created_at": "2025-06-15T17:09:16.356633Z",
    "updated_at": "2025-06-15T17:09:16.356635Z",
    "agent_id": "ag_0684efe3c42a72a680000054f1de6c9d",
    "name": null,
    "description": null,
    "object": "conversation"
  },
  {
    "id": "conv_0684efe0d72577578000bb81a96730ce",
    "created_at": "2025-06-15T17:08:29.446662Z",
    "updated_at": "2025-06-15T17:08:29.446664Z",
    "agent_id": "ag_0684efe0d5bb780e800001065cfbc60c",
    "name": null,
    "description": null,
    "object": "conversation"
  },
  ...
  {
    "id": "conv_0684efcc3e1975818000c45ea5de559d",
    "created_at": "2025-06-15T17:02:59.881204Z",
    "updated_at": "2025-06-15T17:02:59.881205Z",
    "agent_id": "ag_0684efcc3ccf76078000ac2c6fa89efc",
    "name": null,
    "description": null,
    "object": "conversation"
  },
]
```
</details>


Retrieve details from a specific conversation:
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py 
conversation = client.beta.conversations.get(
    conversation_id=response.conversation_id
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
let conversation = await client.beta.conversations.get({
    conversationId: conversation.conversationId
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/conversations/<conv_id>" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```

  </TabItem>
</Tabs>

<details>
    <summary><b>JSON Output</b></summary>

```json
{
  "id": "conv_0684fe18cbc57ba6800065acdd2b6c85",
  "created_at": "2025-06-16T09:19:08.735790Z",
  "updated_at": "2025-06-16T09:20:03.273654Z",
  "agent_id": "ag_0684fe0e0b98773e8000323fc71a3986",
  "name": null,
  "description": null,
  "object": "conversation"
}
```
</details>

Retrieve entries and history from a specific conversation:
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py 
conversation = client.beta.conversations.get_history(
    conversation_id=response.conversation_id
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
let conversationHistory = await client.beta.conversations.getHistory({
    conversationId: conversation.conversationId
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/conversations/<conv_id>/history" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```

  </TabItem>
</Tabs>

<details>
    <summary><b>JSON Output</b></summary>

```json
{
  "conversation_id": "conv_0684fe18cbc57ba6800065acdd2b6c85",
  "entries": [
    {
      "role": "user",
      "content": "Who is Albert Einstein?",
      "object": "entry",
      "type": "message.input",
      "created_at": "2025-06-16T09:19:08.734315Z",
      "completed_at": null,
      "id": "msg_0684fe18cbbf7c358000e14357aedf41"
    },
    {
      "content": "Albert Einstein was a German-born theoretical physicist who is widely regarded as one of the most influential scientists of the 20th century. He is best known for developing the theory of relativity, which revolutionized our understanding of space, time, and energy. Einstein's work also made significant contributions to the development of quantum mechanics and statistical mechanics.\n\nSome of his most notable achievements include:\n\n1. **Special Theory of Relativity (1905)**: This theory introduced the idea that the laws of physics are the same for all non-accelerating observers and that the speed of light in a vacuum is constant, regardless of the observer's motion.\n\n2. **General Theory of Relativity (1915)**: This theory extended the principles of special relativity to include gravity, describing it as a property of the geometry of space and time.\n\n3. **Mass-Energy Equivalence (E=mc²)**: This famous equation from his special theory of relativity shows that mass and energy are interchangeable.\n\n4. **Photoelectric Effect**: Einstein's explanation of the photoelectric effect, which suggested that light could be described as discrete packets of energy (quanta or photons), was a pivotal step in the development of quantum theory.\n\nEinstein was awarded the Nobel Prize in Physics in 1921 for his explanation of the photoelectric effect. He was also known for his humanitarian efforts and his advocacy for civil rights and peace. Einstein emigrated to the United States in the 1930s to escape the rise of the Nazi regime in Germany and became a professor at the Institute for Advanced Study in Princeton, New Jersey, where he spent the remainder of his career.\n\nEinstein's work continues to influence modern physics and our understanding of the universe. He passed away on April 18, 1955.",
      "object": "entry",
      "type": "message.output",
      "created_at": "2025-06-16T09:19:09.031905Z",
      "completed_at": null,
      "id": "msg_0684fe18d08278058000efa70b28fa5a",
      "agent_id": "ag_0684fe0e0b98773e8000323fc71a3986",
      "model": "mistral-medium-2505",
      "role": "assistant"
    },
    {
      "role": "user",
      "content": "Translate to French.",
      "object": "entry",
      "type": "message.input",
      "created_at": "2025-06-16T09:19:56.563908Z",
      "completed_at": null,
      "id": "msg_0684fe1bc9057cbe8000753468b64f7d"
    },
    {
      "content": "Albert Einstein était un physicien théoricien né en Allemagne, largement considéré comme l'un des scientifiques les plus influents du 20ᵉ siècle. Il est surtout connu pour avoir développé la théorie de la relativité, qui a révolutionné notre compréhension de l'espace, du temps et de l'énergie. Les travaux d'Einstein ont également apporté des contributions significatives au développement de la mécanique quantique et de la mécanique statistique.\n\nParmi ses réalisations les plus notables, on peut citer :\n\n1. **Théorie de la relativité restreinte (1905)** : Cette théorie a introduit l'idée que les lois de la physique sont les mêmes pour tous les observateurs non accélérés et que la vitesse de la lumière dans le vide est constante, indépendamment du mouvement de l'observateur.\n\n2. **Théorie de la relativité générale (1915)** : Cette théorie a étendu les principes de la relativité restreinte pour inclure la gravité, la décrivant comme une propriété de la géométrie de l'espace et du temps.\n\n3. **Équivalence masse-énergie (E=mc²)** : Cette équation célèbre de sa théorie de la relativité restreinte montre que la masse et l'énergie sont interchangeables.\n\n4. **Effet photoélectrique** : L'explication d'Einstein de l'effet photoélectrique, qui suggérait que la lumière pouvait être décrite comme des paquets discrets d'énergie (quanta ou photons), a été une étape décisive dans le développement de la théorie quantique.\n\nEinstein a reçu le prix Nobel de physique en 1921 pour son explication de l'effet photoélectrique. Il était également connu pour ses efforts humanitaires et son engagement en faveur des droits civiques et de la paix. Einstein a émigré aux États-Unis dans les années 1930 pour échapper à la montée du régime nazi en Allemagne et est devenu professeur à l'Institut d'études avancées de Princeton, dans le New Jersey, où il a passé le reste de sa carrière.\n\nLes travaux d'Einstein continuent d'influencer la physique moderne et notre compréhension de l'univers. Il est décédé le 18 avril 1955.",
      "object": "entry",
      "type": "message.output",
      "created_at": "2025-06-16T09:19:56.901953Z",
      "completed_at": null,
      "id": "msg_0684fe1bce6e72bc8000f89d886633fe",
      "agent_id": "ag_0684fe0e0b98773e8000323fc71a3986",
      "model": "mistral-medium-2505",
      "role": "assistant"
    }
  ],
  "object": "conversation.history"
}
```
</details>

Retrieve all messages from a specific conversation:
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py 
conversation = client.beta.conversations.get_messages(
    conversation_id=response.conversation_id
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
let conversationMessages = await client.beta.conversations.getMessages({
    conversationId: conversation.conversationId,
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/conversations/<conv_id>/messages" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```

  </TabItem>
</Tabs>

<details>
    <summary><b>JSON Output</b></summary>

```json
{
  "conversation_id": "conv_0684fe18cbc57ba6800065acdd2b6c85",
  "messages": [
    {
      "role": "user",
      "content": "Who is Albert Einstein?",
      "object": "entry",
      "type": "message.input",
      "created_at": "2025-06-16T09:19:08.734315Z",
      "completed_at": null,
      "id": "msg_0684fe18cbbf7c358000e14357aedf41"
    },
    {
      "content": "Albert Einstein was a German-born theoretical physicist who is widely regarded as one of the most influential scientists of the 20th century. He is best known for developing the theory of relativity, which revolutionized our understanding of space, time, and energy. Einstein's work also made significant contributions to the development of quantum mechanics and statistical mechanics.\n\nSome of his most notable achievements include:\n\n1. **Special Theory of Relativity (1905)**: This theory introduced the idea that the laws of physics are the same for all non-accelerating observers and that the speed of light in a vacuum is constant, regardless of the observer's motion.\n\n2. **General Theory of Relativity (1915)**: This theory extended the principles of special relativity to include gravity, describing it as a property of the geometry of space and time.\n\n3. **Mass-Energy Equivalence (E=mc²)**: This famous equation from his special theory of relativity shows that mass and energy are interchangeable.\n\n4. **Photoelectric Effect**: Einstein's explanation of the photoelectric effect, which suggested that light could be described as discrete packets of energy (quanta or photons), was a pivotal step in the development of quantum theory.\n\nEinstein was awarded the Nobel Prize in Physics in 1921 for his explanation of the photoelectric effect. He was also known for his humanitarian efforts and his advocacy for civil rights and peace. Einstein emigrated to the United States in the 1930s to escape the rise of the Nazi regime in Germany and became a professor at the Institute for Advanced Study in Princeton, New Jersey, where he spent the remainder of his career.\n\nEinstein's work continues to influence modern physics and our understanding of the universe. He passed away on April 18, 1955.",
      "object": "entry",
      "type": "message.output",
      "created_at": "2025-06-16T09:19:09.031905Z",
      "completed_at": null,
      "id": "msg_0684fe18d08278058000efa70b28fa5a",
      "agent_id": "ag_0684fe0e0b98773e8000323fc71a3986",
      "model": "mistral-medium-2505",
      "role": "assistant"
    },
    {
      "role": "user",
      "content": "Translate to French.",
      "object": "entry",
      "type": "message.input",
      "created_at": "2025-06-16T09:19:56.563908Z",
      "completed_at": null,
      "id": "msg_0684fe1bc9057cbe8000753468b64f7d"
    },
    {
      "content": "Albert Einstein était un physicien théoricien né en Allemagne, largement considéré comme l'un des scientifiques les plus influents du 20ᵉ siècle. Il est surtout connu pour avoir développé la théorie de la relativité, qui a révolutionné notre compréhension de l'espace, du temps et de l'énergie. Les travaux d'Einstein ont également apporté des contributions significatives au développement de la mécanique quantique et de la mécanique statistique.\n\nParmi ses réalisations les plus notables, on peut citer :\n\n1. **Théorie de la relativité restreinte (1905)** : Cette théorie a introduit l'idée que les lois de la physique sont les mêmes pour tous les observateurs non accélérés et que la vitesse de la lumière dans le vide est constante, indépendamment du mouvement de l'observateur.\n\n2. **Théorie de la relativité générale (1915)** : Cette théorie a étendu les principes de la relativité restreinte pour inclure la gravité, la décrivant comme une propriété de la géométrie de l'espace et du temps.\n\n3. **Équivalence masse-énergie (E=mc²)** : Cette équation célèbre de sa théorie de la relativité restreinte montre que la masse et l'énergie sont interchangeables.\n\n4. **Effet photoélectrique** : L'explication d'Einstein de l'effet photoélectrique, qui suggérait que la lumière pouvait être décrite comme des paquets discrets d'énergie (quanta ou photons), a été une étape décisive dans le développement de la théorie quantique.\n\nEinstein a reçu le prix Nobel de physique en 1921 pour son explication de l'effet photoélectrique. Il était également connu pour ses efforts humanitaires et son engagement en faveur des droits civiques et de la paix. Einstein a émigré aux États-Unis dans les années 1930 pour échapper à la montée du régime nazi en Allemagne et est devenu professeur à l'Institut d'études avancées de Princeton, dans le New Jersey, où il a passé le reste de sa carrière.\n\nLes travaux d'Einstein continuent d'influencer la physique moderne et notre compréhension de l'univers. Il est décédé le 18 avril 1955.",
      "object": "entry",
      "type": "message.output",
      "created_at": "2025-06-16T09:19:56.901953Z",
      "completed_at": null,
      "id": "msg_0684fe1bce6e72bc8000f89d886633fe",
      "agent_id": "ag_0684fe0e0b98773e8000323fc71a3986",
      "model": "mistral-medium-2505",
      "role": "assistant"
    }
  ],
  "object": "conversation.messages"
}
```
</details>

### Restart Conversation

You can continue a conversation from any given entry from the history of entries:
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py 
conversation = client.beta.conversations.restart(
    conversation_id=response.conversation_id,
    from_entry_id="msg_0684fe18d08278058000efa70b28fa5a",
    inputs="Translate to Portuguese."
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
let newConversation = await client.beta.conversations.restart({
    conversationId: conversation.conversationId,
    conversationRestartRequest: {
        inputs: "Translate to portuguese.",
        fromEntryId: conversationMessages.messages[conversationMessages.messages.length - 1 ].id?.toString() || ''
    }
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/conversations/<conv_id>/restart" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "from_entry_id": "<entry_id>",
     "inputs": "Translate to Portuguese.",
     "stream": false,
     "store": true,
     "handoff_execution": "server"
  }'
```
  </TabItem>
</Tabs>

<details>
    <summary><b>JSON Output</b></summary>

```json
{
  "conversation_id": "conv_0684fe409c757d4580000514e0c851ad",
  "outputs": [
    {
      "content": "Claro! Aqui está a tradução para o português:\n\n---\n\nAlbert Einstein foi um físico teórico nascido na Alemanha, amplamente considerado um dos cientistas mais influentes do século XX. Ele é mais conhecido por desenvolver a teoria da relatividade, que revolucionou nossa compreensão do espaço, tempo e energia. O trabalho de Einstein também contribuiu significativamente para o desenvolvimento da mecânica quântica e da mecânica estatística.\n\nAlgumas de suas realizações mais notáveis incluem:\n\n1. **Teoria da Relatividade Especial (1905)**: Esta teoria introduziu a ideia de que as leis da física são as mesmas para todos os observadores não acelerados e que a velocidade da luz no vácuo é constante, independentemente do movimento do observador.\n\n2. **Teoria da Relatividade Geral (1915)**: Esta teoria estendeu os princípios da relatividade especial para incluir a gravidade, descrevendo-a como uma propriedade da geometria do espaço e do tempo.\n\n3. **Equivalência Massa-Energia (E=mc²)**: Esta famosa equação de sua teoria da relatividade especial mostra que massa e energia são intercambiáveis.\n\n4. **Efeito Fotoelétrico**: A explicação de Einstein para o efeito fotoelétrico, que sugeria que a luz poderia ser descrita como pacotes discretos de energia (quanta ou fótons), foi um passo crucial no desenvolvimento da teoria quântica.\n\nEinstein foi agraciado com o Prêmio Nobel de Física em 1921 por sua explicação do efeito fotoelétrico. Ele também era conhecido por seus esforços humanitários e por sua defesa dos direitos civis e da paz. Einstein emigrou para os Estados Unidos na década de 1930 para escapar do regime nazista na Alemanha e tornou-se professor no Instituto de Estudos Avançados em Princeton, Nova Jersey, onde passou o restante de sua carreira.\n\nO trabalho de Einstein continua a influenciar a física moderna e nossa compreensão do universo. Ele faleceu em 18 de abril de 1955.\n\n---\n\nSe precisar de mais alguma coisa, é só avisar!",
      "object": "entry",
      "type": "message.output",
      "created_at": "2025-06-16T09:29:45.954701Z",
      "completed_at": "2025-06-16T09:29:56.369588Z",
      "id": "msg_0684fe409f46733d8000e40522f8ceea",
      "agent_id": "ag_0684fe0e0b98773e8000323fc71a3986",
      "model": "mistral-medium-2505",
      "role": "assistant"
    }
  ],
  "usage": {
    "prompt_tokens": 384,
    "completion_tokens": 461,
    "total_tokens": 845,
    "connector_tokens": null,
    "connectors": null
  },
  "object": "conversation.response"
}
```
</details>

**Note**: You can only restart conversations on which you used the `append()` method at least once.

### Streaming Output
You can also stream the outputs, both when starting a conversation, continuing or restarting a previous one.
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

#### Start
```py
response = client.beta.conversations.start_stream(
    agent_id=websearch_agent.id,
    inputs="Who is Albert Einstein?"
)
```
#### Continue
```py
response = client.beta.conversations.append_stream(
    conversation_id=response.conversation_id,
    inputs="Translate to French."
)
```
#### Restart
```py
response = client.beta.conversations.restart_stream(
    conversation_id=response.conversation_id,
    from_entry_id="msg_0684fe18d08278058000efa70b28fa5a",
    inputs="Translate to Portuguese."
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

#### Start
```typescript
let stream = await client.beta.conversations.startStream({
    agentId: websearchAgent.id,
    inputs: "Who is albert Enstein?"
});
```
#### Continue
```typescript
let stream = await client.beta.conversations.appendStream({
    conversationId: conversation.conversationId,
    conversationAppendStreamRequest: {
        inputs: "Who is albert Enstein?"
    }
});
```
#### Restart
```typescript
let stream = await client.beta.conversations.restartStream({
    conversationId: conversation.conversationId,
    conversationRestartStreamRequest: {
        fromEntryId: conversationMessages.messages[conversationMessages.messages.length - 1 ].id?.toString() || '',
        inputs: "Who is albert Enstein?"
    }
});
```

For each streaming operation, you should use the following snippet of code:
```typescript
for await (const chunk of stream) {
    // The operation you want to make. In this example, we only choose to display each incoming streamed object.
    console.log(chunk);
}
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/conversations" \
     --header 'Content-Type: application/json' \
     --header 'Accept: text/event-stream' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "inputs": "Who is Albert Einstein?",
     "stream": true,
     "agent_id": "ag_06811008e6e07cb48000fd3f133e1771"
  }'
```
  </TabItem>
</Tabs>

When streaming, you will have specific indexes for specific content types during a stream. These include:
- `conversation.response.started`: The start of a conversation response.
- `conversation.response.done`: The response is done and finished.
- `conversation.response.error`: An error occurred.
- `message.output.delta`: Chunk of content, usually tokens corresponding to the model reply.
- `tool.execution.started`: A tool execution has started.
- `tool.execution.done`: A tool has finished executing.
- `agent.handoff.started`: The handoff to a different agent has started.
- `agent.handoff.done`: The handoff was concluded.
- `function.call.delta`: Chunk of content, usually tokens corresponding to the function tool call.

<details>
    <summary><b>Example</b></summary>

```
event: conversation.response.started
data: {"type":"conversation.response.started","conversation_id":"conv_067f2a98c1a773678000ce73a36b785a"}

event: tool.execution.started
data: {"type":"tool.execution.started","output_index":0,"id":"tool_exec_067f2a98ca357c8b8000ea212104b290","name":"web_search"}

event: tool.execution.done
data: {"type":"tool.execution.done","output_index":0,"id":"tool_exec_067f2a98ca357c8b8000ea212104b290","name":"web_search"}

event: message.output.delta
data: {"type":"message.output.delta","output_index":1,"id":"msg_067f2a9925d674ea8000e63c68ae0474","content_index":0,"model":"mistral-medium-2505","agent_id":"ag_067f2a39ddd67bf68000fa921bc0c25d","role":"assistant","content":"The"}

event: message.output.delta
data: {"type":"message.output.delta","output_index":1,"id":"msg_067f2a9925d674ea8000e63c68ae0474","content_index":0,"model":"mistral-medium-2505","agent_id":"ag_067f2a39ddd67bf68000fa921bc0c25d","role":"assistant","content":" last"}

event: message.output.delta
data: {"type":"message.output.delta","output_index":1,"id":"msg_067f2a9925d674ea8000e63c68ae0474","content_index":0,"model":"mistral-medium-2505","agent_id":"ag_067f2a39ddd67bf68000fa921bc0c25d","role":"assistant","content":" European"}

event: message.output.delta
data: {"type":"message.output.delta","output_index":1,"id":"msg_067f2a9925d674ea8000e63c68ae0474","content_index":0,"model":"mistral-medium-2505","agent_id":"ag_067f2a39ddd67bf68000fa921bc0c25d","role":"assistant","content":" Football"}

...

event: message.output.delta
data: {"type":"message.output.delta","output_index":1,"id":"msg_067f2a9925d674ea8000e63c68ae0474","content_index":2,"model":"mistral-medium-2505","agent_id":"ag_067f2a39ddd67bf68000fa921bc0c25d","role":"assistant","content":" tournament"}

event: message.output.delta
data: {"type":"message.output.delta","output_index":1,"id":"msg_067f2a9925d674ea8000e63c68ae0474","content_index":2,"model":"mistral-medium-2505","agent_id":"ag_067f2a39ddd67bf68000fa921bc0c25d","role":"assistant","content":"."}

event: conversation.response.done
data: {"type":"conversation.response.done","usage":{"prompt_tokens":18709,"total_tokens":18892,"completion_tokens":183}}
```
</details>


[Agents Function Calling]
Source: https://docs.mistral.ai/docs/agents/agents_function_calling

The core of an agent relies on its tool usage capabilities, enabling it to use and call tools and workflows depending on the task it must accomplish.

Built into our API, we provide [connector](../connectors/connectors) tools such as `websearch`, `code_interpreter`, `image_generation` and `document_library`. However, you can also use standard function tool calling by defining a JSON schema for your function.

You can also leverage our MCP Orchestration to implement local Function Calling, visit our [Local MCP docs](../mcp/#step-4-register-mcp-client) for further details.

For more information regarding function calling, we recommend to visit our [function calling docs](../../capabilities/function_calling).

### Creating an Agent with Function Calling

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

We need to define our function that we want our model to call when needed, in this case, the function is a dummy for demonstration purposes.

```py
from typing import Dict

def get_european_central_bank_interest_rate(date: str) -> Dict[str, str]:
    """
    Retrieve the real interest rate of the European Central Bank for a given date.

    Parameters:
    - date (str): The date for which to retrieve the interest rate in the format YYYY-MM-DD.

    Returns:
    - dict: A dictionary containing the date and the corresponding interest rate.
    """
    # This is a mock implementation. In a real scenario, you would fetch this data from an API or database.
    # For demonstration, let's assume the interest rate is fixed at 2.5% for any date.
    interest_rate = "2.5%"

    return {
        "date": date,
        "interest_rate": interest_rate
    }
```

Once defined, we provide a Shema corresponding to the same function.

```py
ecb_interest_rate_agent = client.beta.agents.create(
    model="mistral-medium-2505",
    description="Can find the current interest rate of the European central bank",
    name="ecb-interest-rate-agent",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_european_central_bank_interest_rate",
                "description": "Retrieve the real interest rate of European central bank.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                        },
                    },
                    "required": [
                        "date",
                    ]
                },
            },
        },
    ],
)
```

  </TabItem>

  <TabItem value="typescript" label="typescript">


We need to define our function that we want our model to call when needed, in this case, the function is a dummy for demonstration purposes.

```typescript
async function getEuropeanentralBankInterestRate(date: str){
    /*
    Retrieve the real interest rate of the European Central Bank for a given date.

    Parameters:
    - date (str): The date for which to retrieve the interest rate in the format YYYY-MM-DD.

    Returns:
    - dict: A dictionary containing the date and the corresponding interest rate.
    */
    // This is a mock implementation. In a real scenario, you would fetch this data from an API or database.
    // For demonstration, let's assume the interest rate is fixed at 2.5% for any date.
    let interestRate = "2.5%";

    return {
        date: date,
        interestRate: interestRate
    }
}
```

Once defined, we provide a Shema corresponding to the same function.


```typescript
let ecbInterestRateAgent = await client.beta.agents.create({
    model:"mistral-medium-2505",
    description:"Can find the current interest rate of the European central bank",
    name:"ecb-interest-rate-agent",
    tools:[
        {
            type: "function",
            function: {
                name: "getEuropeanCentralBankInterestRate",
                description: "Retrieve the real interest rate of European central bank.",
                parameters: {
                    type: "object",
                    properties: {
                        date: {
                            type: "string",
                        },
                    },
                    required: [
                        "date",
                    ]
                },
            },
        },
    ],
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/agents" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "model": "mistral-medium-2505",
     "name": "ecb-interest-rate-agent",
     "description": "Can find the current interest rate of the European central bank",
     "instructions": "You can provide interest rate and information regarding the European central bank.",
     "tools": [
         {
             "function": {
                 "name": "get_european_central_bank_interest_rate",
                 "parameters": {
                     "type": "object",
                     "properties": {
                         "date": {
                             "type": "string"
                         }
                     },
                     "required": ["date"]
                 },
                 "description": "Retrieve the real interest rate of European central bank."
             },
             "type": "function"
         }
     ]
 }'

```
  </TabItem>
</Tabs>

<details>
    <summary><b>Output</b></summary>

```json
{
  "model": "mistral-medium-2505",
  "name": "ecb-interest-rate-agent",
  "description": "Can find the current interest rate of the European central bank",
  "id": "ag_06835a34f2c476518000c372a505c2c4",
  "version": 0,
  "created_at": "2025-05-27T11:34:39.175924Z",
  "updated_at": "2025-05-27T11:34:39.175926Z",
  "instructions": "You can provide interest rate and information regarding the European central bank.",
  "tools": [
    {
      "function": {
        "name": "get_european_central_bank_interest_rate",
        "parameters": {
          "type": "object",
          "properties": {
            "date": {
              "type": "string"
            }
          },
          "required": [
            "date"
          ]
        },
        "description": "Retrieve the real interest rate of European central bank.",
        "strict": false
      },
      "type": "function"
    }
  ],
  "completion_args": {
    "stop": null,
    "presence_penalty": null,
    "frequency_penalty": null,
    "temperature": 0.3,
    "top_p": null,
    "max_tokens": null,
    "random_seed": null,
    "prediction": null,
    "response_format": null,
    "tool_choice": "auto"
  },
  "handoffs": null,
  "object": "agent"
}
```
</details>

### Using an Agent with Function Calling

<Tabs groupId="code">
  <TabItem value="python" label="python" default>
Then, to use it, we start a conversation or continue a previously existing one.

```py
response = client.beta.conversations.start(
    agent_id=ecb_interest_rate_agent.id,
    inputs=[{"role": "user", "content": "Whats the current 2025 real interest rate?"}]
)
```

<details>
    <summary><b>Output</b></summary>

```json
{
  "conversation_id": "conv_06835a34f58773bd8000f46c0d11e42c",
  "outputs": [
    {
      "tool_call_id": "6TI17yZkV",
      "name": "get_european_central_bank_interest_rate",
      "arguments": "{\"date\": \"2024-06-06\"}",
      "object": "entry",
      "type": "function.call",
      "created_at": "2025-05-27T11:34:39.610632Z",
      "completed_at": null,
      "id": "fc_06835a34f9c47fc88000e0370a295774"
    }
  ],
  "usage": {
    "prompt_tokens": 91,
    "completion_tokens": 29,
    "total_tokens": 120,
    "connector_tokens": null,
    "connectors": null
  },
  "object": "conversation.response"
}

```
</details>

The model will output either an answer, or a function call, we need to detect and return the result of the expected function.


```py
from mistralai import FunctionResultEntry


if response.outputs[-1].type == "function.call" and response.outputs[-1].name == "get_european_central_bank_interest_rate":

    # Running our function
    function_result = json.dumps(get_european_central_bank_interest_rate(**json.loads(response.outputs[-1].arguments)))

    # Providing the result to our Agent
    user_function_calling_entry = FunctionResultEntry(
        tool_call_id=response.outputs[-1].tool_call_id,
        result=function_result,
    )

    # Retrieving the final response
    response = client.beta.conversations.append(
        conversation_id=response.conversation_id,
        inputs=[user_function_calling_entry]
    )
    print(response.outputs[-1])
else:

    # In case the model did not call our function
    print(response.outputs[-1])
```
  </TabItem>


  <TabItem value="typescript" label="typescript">
Then, to use it, we start a conversation or continue a previously existing one.

```typescript
let response = await client.beta.conversations.start({
    agentId: (await ecbInterestRateAgent).id,
    inputs:[{role: "user", content: "Whats the current 2025 real interest rate?"}]
});
```

<details>
    <summary><b>Output</b></summary>

```json
{
  "conversation_id": "conv_06835a34f58773bd8000f46c0d11e42c",
  "outputs": [
    {
      "tool_call_id": "6TI17yZkV",
      "name": "get_european_central_bank_interest_rate",
      "arguments": "{\"date\": \"2024-06-06\"}",
      "object": "entry",
      "type": "function.call",
      "created_at": "2025-05-27T11:34:39.610632Z",
      "completed_at": null,
      "id": "fc_06835a34f9c47fc88000e0370a295774"
    }
  ],
  "usage": {
    "prompt_tokens": 91,
    "completion_tokens": 29,
    "total_tokens": 120,
    "connector_tokens": null,
    "connectors": null
  },
  "object": "conversation.response"
}

```
</details>

The model will output either an answer, or a function call, we need to detect and return the result of the expected function.

First, let's add the following imports:
```typescript

```

Then, we check whether or not a function call was triggered:

```typescript
let output = response.outputs[response.outputs.length - 1];

if (output.type === "function.call" && output.name === "getEuropeanCentralBankInterestRate") {
    const args = output.arguments as unknown as string;
    const parsedArgs = JSON.parse(args);
    const date = parsedArgs.date;

    const functionResult = JSON.stringify(await getEuropeanCentralBankInterestRate(date));

    const toolCallId = output.toolCallId;

    const userFunctionCallingEntry: FunctionResultEntry = {
        toolCallId: toolCallId,
        result: functionResult,
    };

    response = await client.beta.conversations.append({
        conversationId: response.conversationId,
        conversationAppendRequest:{
            inputs: [userFunctionCallingEntry]
        }
    });

    const finalEntry = response.outputs[response.outputs.length - 1];
    const finalMessageOutputEntry = finalEntry as MessageOutputEntry;
    console.log(finalMessageOutputEntry);
} else {
    console.log(output);
}
```
  </TabItem>

  <TabItem value="curl" label="curl">

For starting a conversation:
```bash
curl --location "https://api.mistral.ai/v1/conversations" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "inputs": [
         {
             "role": "user",
             "content": "Whats the current 2025 real interest rate?",
             "object": "entry",
             "type": "message.input"
         }
     ],
     "stream": false,
     "agent_id": "<agent_id>"
 }'
```

For continuing a conversation:
```bash
curl --location "https://api.mistral.ai/v1/conversations/<conv_id>" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "inputs": [
         {
             "tool_call_id": "6TI17yZkV",
             "result": "{\"date\": \"2024-06-06\", \"interest_rate\": \"2.5%\"}",
             "object": "entry",
             "type": "function.result"
         }
     ],
     "stream": false,
     "store": true,
     "handoff_execution": "server"
 }'
```
  </TabItem>
</Tabs>

<details>
    <summary><b>Output</b></summary>
    
```json
{
  "content": "The current interest rate as of June 6, 2024, is 2.5%. This information is relevant for understanding the economic conditions in 2025.",
  "object": "entry",
  "type": "message.output",
  "created_at": "2025-05-27T11:34:40.142767Z",
  "completed_at": "2025-05-27T11:34:40.801117Z",
  "id": "msg_06835a35024879bc80005b1bf9ab0f12",
  "agent_id": "ag_06835a34f2c476518000c372a505c2c4",
  "model": "mistral-medium-2505",
  "role": "assistant"
}
```
</details>


[Agents Introduction]
Source: https://docs.mistral.ai/docs/agents/agents_introduction

## What are AI agents?

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/agent_overview.png"
    alt="agent_introduction"
    width="600"
    style={{ borderRadius: '15px' }}
  />
</div>

AI agents are autonomous systems powered by large language models (LLMs) that, given high-level instructions, can plan, use tools, carry out processing steps, and take actions to achieve specific goals. These agents leverage advanced natural language processing capabilities to understand and execute complex tasks efficiently and can even collaborate with each other to achieve more sophisticated outcomes.

Our Agents and Conversations API allows developers to build such agents, leveraging multiple features such as:
- Multiple mutlimodal models available, **text and vision models**.
- **Persistent state** across conversations.
- Ability to have conversations with **base models**, **a single agent**, and **multiple agents**.
- Built-in connector tools for **code execution**, **web search**, **image generation** and **document library** out of the box.
- **Handoff capability** to use different agents as part of a workflow, allowing agents to call other agents.
- Features supported via our chat completions endpoint are also supported, such as:
  - **Structured Outputs**
  - **Document Understanding**
  - **Tool Usage**
  - **Citations**

## More Information
- [Agents & Conversations](../agents_basics): Basic explanations and code snippets around our Agents and Conversations API.
- [Connectors](../connectors/connectors): Make your tools accessible directly to any Agents.
  - [Websearch](../connectors/websearch): In-depth explanation of our web search built-in connector tool.
  - [Code Interpreter](../connectors/code_interpreter): In-depth explanation of our code interpreter for code execution built-in connector tool.
  - [Image Generation](../connectors/image_generation): In-depth explanation of our image generation built-in connector tool.
  - [Document Library (Beta)](../connectors/document_library): A RAG built-in connector enabling Agents to access a library of documents.
- [MCP](../mcp): How to use [MCP](../../capabilities/function_calling) (Model Context Protocol) servers with Agents.
- [Function Calling](../function_calling): How to use [Function calling](../../capabilities/function_calling) with Agents.
- [Handoffs](../handoffs): Relay tasks and use other agents as tools in agentic workflows.

## Cookbooks
For more information and guides on how to use our Agents, we have the following cookbooks:
- [Github Agent](https://github.com/mistralai/cookbook/tree/main/mistral/agents/agents_api/github_agent)
- [Linear Tickets](https://github.com/mistralai/cookbook/tree/main/mistral/agents/agents_api/prd_linear_ticket)
- [Financial Analyst](https://github.com/mistralai/cookbook/tree/main/mistral/agents/agents_api/financial_analyst)
- [Travel Assistant](https://github.com/mistralai/cookbook/tree/main/mistral/agents/agents_api/travel_assistant)
- [Food Diet Companion](https://github.com/mistralai/cookbook/tree/main/mistral/agents/agents_api/food_diet_companion)

## FAQ

- **Which models are supported?**

  Currently, only `mistral-medium-latest` and `mistral-large-latest` are supported, but we will soon enable it for more models.


[Code Interpreter]
Source: https://docs.mistral.ai/docs/agents/connectors/code_interpreter

Code Interpreter adds the capability to safely execute code in an isolated container, this built-in [connector](../connectors) tool allows Agents to run code at any point on demand, practical to draw graphs, data analysis, mathematical operations, code validation, and much more.

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/code_interpreter_connector.png"
    alt="code_interpreter_graph"
    width="400"
    style={{ borderRadius: '15px' }}
  />
</div>

## Create a Code Interpreter Agent
You can create an agent with access to our code interpreter by providing it as one of the tools.  
Note that you can still add more tools to the agent, the model is free to run code or not on demand.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py
code_agent = client.beta.agents.create(
    model="mistral-medium-2505",
    name="Coding Agent",
    description="Agent used to execute code using the interpreter tool.",
    instructions="Use the code interpreter tool when you have to run code.",
    tools=[{"type": "code_interpreter"}],
    completion_args={
        "temperature": 0.3,
        "top_p": 0.95,
    }
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
const codeAgent = await client.beta.agents.create({
    model: "mistral-medium-latest",
    name: "Coding Agent",
    instructions: "Use the code interpreter tool when you have to run code.",
    description: "Agent used to execute code using the interpreter tool.",
    tools: [{ type: "code_interpreter" }],
    completionArgs:{
        temperature: 0.3,
        topP: 0.95,
    }
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/agents" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "model": "mistral-medium-2505",
     "name": "Coding Agent",
     "description": "Agent used to execute code using the interpreter tool.",
     "instructions": "Use the code interpreter tool when you have to run code.",
     "tools": [
       {
         "type": "code_interpreter"
       }
     ],
     "completion_args": {
       "temperature": 0.3,
       "top_p": 0.95
     }
  }'
```
  </TabItem>
</Tabs>

<details>
    <summary><b>Output</b></summary>

```json
{
  "model": "mistral-medium-2505",
  "name": "Coding Agent",
  "description": "Agent used to execute code using the interpreter tool.",
  "id": "ag_06830595b7ea7e70800087c4ec8a74e7",
  "version": 0,
  "created_at": "2025-05-23T11:17:47.497956Z",
  "updated_at": "2025-05-23T11:17:47.497959Z",
  "instructions": "Use the code interpreter tool when you have to run code.",
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  "completion_args": {
    "stop": null,
    "presence_penalty": null,
    "frequency_penalty": null,
    "temperature": 0.3,
    "top_p": 0.95,
    "max_tokens": null,
    "random_seed": null,
    "prediction": null,
    "response_format": null,
    "tool_choice": "auto"
  },
  "handoffs": null,
  "object": "agent"
}

```
</details>

As for other agents, when creating one you will receive an agent id corresponding to the created agent that you can use to start a conversation.

## How it works

### Conversations with Code Interpreter
Now that we have our coding agent ready, we can at any point make use of it to run code.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py
response = client.beta.conversations.start(
    agent_id=code_agent.id,
    inputs="Run a fibonacci function for the first 20 values."
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
let conversation = await client.beta.conversations.start({
    agentId: codeAgent.id,
    inputs:"Run a fibonacci function for the first 20 values.",
    //store:false
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/conversations" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "inputs": "Run a fibonacci function for the first 20 values.",
     "stream": false,
     "agent_id": "<agent_id>"
  }'
```
  </TabItem>
</Tabs>

For explanation purposes, lets take a look at the output in a readable JSON format.
```json
{
  "conversation_id": "conv_06835b9dc0c7749180001958779d13c5",
  "outputs": [
    {
      "content": "Sure, I can help with that. Here's a simple Python function to generate the first 20 Fibonacci numbers.",
      "object": "entry",
      "type": "message.output",
      "created_at": "2025-05-27T13:10:52.208822Z",
      "completed_at": "2025-05-27T13:10:52.470589Z",
      "id": "msg_06835b9dc35772be800073298138bacc",
      "agent_id": "ag_06835b9dbded7f39800034281a63e4f0",
      "model": "mistral-medium-2505",
      "role": "assistant"
    },
    {
      "name": "code_interpreter",
      "object": "entry",
      "type": "tool.execution",
      "created_at": "2025-05-27T13:10:52.561656Z",
      "completed_at": "2025-05-27T13:10:54.431304Z",
      "id": "tool_exec_06835b9dc8fc763880004b7aa94286d8",
      "info": {
        "code": "def fibonacci(n):\n    fib_sequence = [0, 1]\n    for i in range(2, n):\n        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])\n    return fib_sequence[:n]\n\nfibonacci_20 = fibonacci(20)\nfibonacci_20",
        "code_output": "[0,\n 1,\n 1,\n 2,\n 3,\n 5,\n 8,\n 13,\n 21,\n 34,\n 55,\n 89,\n 144,\n 233,\n 377,\n 610,\n 987,\n 1597,\n 2584,\n 4181]\n"
      }
    },
    {
      "content": "The first 20 values of the Fibonacci sequence are:\n\n[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]",
      "object": "entry",
      "type": "message.output",
      "created_at": "2025-05-27T13:10:54.517935Z",
      "completed_at": "2025-05-27T13:10:55.314698Z",
      "id": "msg_06835b9de84974fa8000f1a97be62f2e",
      "agent_id": "ag_06835b9dbded7f39800034281a63e4f0",
      "model": "mistral-medium-2505",
      "role": "assistant"
    }
  ],
  "usage": {
    "prompt_tokens": 95,
    "completion_tokens": 209,
    "total_tokens": 399,
    "connector_tokens": 95,
    "connectors": {
      "code_interpreter": 1
    }
  },
  "object": "conversation.response"
}
```

### Explanation of the Outputs 
There are 3 main entries in the `outputs` of our request:  

- **`message.output`**: This entry corresponds to the initial response from the assistant, indicating that it can help generate the first 20 Fibonacci numbers.

- **`tool.execution`**: This entry corresponds to the execution of the code interpreter tool. It includes metadata about the execution, such as:
  - `name`: The name of the tool, which in this case is `code_interpreter`.
  - `object`: The type of object, which is `entry`.
  - `type`: The type of entry, which is `tool.execution`.
  - `created_at` and `completed_at`: Timestamps indicating when the tool execution started and finished.
  - `id`: A unique identifier for the tool execution.
  - `info`: This section contains additional information specific to the tool execution. For the `code_interpreter` tool, the `info` section includes:
    - `code`: The actual code that was executed. In this example, it contains a Python function `fibonacci(n)` that generates the first `n` numbers in the Fibonacci sequence and a call to this function to get the first 20 Fibonacci numbers.
    - `code_output`: The output of the executed code, which is the list of the first 20 Fibonacci numbers.

- **`message.output`**: This entry corresponds to the final response from the assistant, providing the first 20 values of the Fibonacci sequence.


[Connectors Overview]
Source: https://docs.mistral.ai/docs/agents/connectors/connectors_overview

Connectors are tools that Agents can call at any given point. They are deployed and ready for the agents to leverage to answer questions on demand.  

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/connectors_graph.png"
    alt="connectors_graph"
    width="800"
    style={{ borderRadius: '15px' }}
  />
</div>

They are also available for users to use them directly via Conversations without the Agent creation step!

## General Usage
<Tabs groupId="code">
  <TabItem value="python" label="python" default>
You can either create an Agent with the desired tools:

```py
agent = client.beta.agents.create(
    model="<model>",
    name="<name_of_the_agent>",
    description="<description>",
    instructions="<instructions_or_system_prompt>",
    tools=[<list_of_tools>]
)
```

Or call our conversations API directly:

```py
response = client.beta.conversations.start(
    model="<model>",
    inputs=[<messages_or_question>],
    tools=[<list_of_tools>],
    # store=False
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">
    
You can either create an Agent with the desired tools:

```typescript
agent = client.beta.agents.create({
    model:"<model>",
    name:"<name_of_the_agent>",
    description:"<description>",
    instructions:"<instructions_or_system_prompt>",
    tools:[<list_of_tools>]
});
```

Or call our conversations API directly:

```typescript
response = client.beta.conversations.start({
    model:"<model>",
    inputs:[<messages_or_question>],
    tools:[<list_of_tools>],
    // store:False
});
```
  </TabItem>

  <TabItem value="curl" label="curl">
You can either create an Agent with the desired tools:

```bash
curl --location "https://api.mistral.ai/v1/agents" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "model": "<model>",
     "name": "<name_of_the_agent>",
     "description": "<description>",
     "instructions": "<instructions_or_system_prompt>",
     "tools": [<list_of_tools>]
  }'
```

Or call our conversations API directly:

```bash
curl --location "https://api.mistral.ai/v1/conversations" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
     "model": "<model>",
     "inputs": [<messages_or_question>],
     "tools": [<list_of_tools>]
  }'
```
  </TabItem>
</Tabs>

Currently, our API has 4 built-in Connector tools, here you can find how to use them in details:
- [Websearch](../websearch)
- [Code Interpreter](../code_interpreter)
- [Image Generation](../image_generation)
- [Document Library](../document_library)


[Document Library]
Source: https://docs.mistral.ai/docs/agents/connectors/document_library

Document Library is a built-in [connector](../connectors) tool that enables agents to access documents from Mistral Cloud.

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/document_library_connector.png"
    alt="document_library_graph"
    width="400"
    style={{ borderRadius: '15px' }}
  />
</div>

It is a built-in RAG capability that enhances your agents' knowledge with the data you have uploaded.

## Manage Libraries

You can manage your libraries using the Mistral AI API, we recommend taking a look at the [API spec](https://docs.mistral.ai/api/#tag/beta.libraries.documents) for the details. Below are some examples of how to interact with libraries and documents.

### Listing Libraries

You can list your existing libraries and their documents.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
libraries = client.beta.libraries.list().data
for library in libraries:
    print(library.name, f"with {library.nb_documents} documents.")
```

  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
let libraries = await client.beta.libraries.list();

for (const library of libraries.data)
{
    console.log(`${library.name} with ${library.nbDocuments} documents`);
}
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/libraries" \
     --header "Accept: application/json" \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>
</Tabs>

<details>
    <summary><b>Output</b></summary>

```
X's Library with 152 documents.
My new API library with 1 documents.
Mistral Documentation with 81 documents.
Y's PDFs  with 21 documents.
Papers with 2 documents.
```
</details>

### Listing Documents in a Library

To list documents in a specific library:

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
if len(libraries) == 0:
    print("No libraries found.")
else:
    doc_list = client.beta.libraries.documents.list(library_id=libraries[0].id).data
    for doc in doc_list:
        print(f"{doc.name}: {doc.extension} with {doc.number_of_pages} pages.")
        print(f"{doc.summary}")
```

 </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
if (libraries.data.length === 0) 
{
    console.log("No libraries found.");
} 
else 
{
  const docList = await client.beta.libraries.documents.list({ 
      libraryId: libraries.data[0].id 
  });
  for (const doc of docList.data) 
  {
      console.log(`${doc.name}: ${doc.extension} with ${doc.numberOfPages} pages.`);
      console.log(`${doc.summary}`);
  }
}
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/libraries/<library_id>/documents?page_size=100&page=0&sort_by=created_at&sort_order=desc" \
     --header "Accept: application/json" \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>
</Tabs>

You can list and search documents in a library if required.

### Creating a New Library

You can create and manage new document libraries directly via our API.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
new_library = client.beta.libraries.create(name="Mistral Models", description="A simple library with information about Mistral models.")
```

 </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
const newLibrary = await client.beta.libraries.create({
    name: "Mistral Models",
    description: "A simple library with information about Mistral models."
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/libraries" \
     --header "Accept: application/json" \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --header "Content-Type: application/json" \
     --data '{
      "name": "Mistral Models",
      "description": "A simple library with information about Mistral models."
     }'
```
  </TabItem>
</Tabs>

<details>
    <summary><b>Contents</b></summary>

```json
{
  "id": "0197f425-5e85-7353-b8e7-e8b974b9c613",
  "name": "Mistral Models",
  "created_at": "2025-07-10T11:42:59.230268Z",
  "updated_at": "2025-07-10T11:42:59.230268Z",
  "owner_id": "6340e568-a546-4c41-9dee-1fbeb80493e1",
  "owner_type": "Workspace",
  "total_size": 0,
  "nb_documents": 0,
  "chunk_size": null,
  "emoji": null,
  "description": "A simple library with information about Mistral models.",
  "generated_name": null,
  "generated_description": null,
  "explicit_user_members_count": null,
  "explicit_workspace_members_count": null,
  "org_sharing_role": null
}
```
</details>

When generated, the library will contain different kinds of information. This information is updated and generated when files are added. Specifically, `generated_name` and `generated_description` will be constantly updated and kept up to date.

### Listing Documents in a New Library

Each library, has a set of documents that belongs to it.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
doc_list = client.beta.libraries.documents.list(library_id=new_library.id).data
for doc in doc_list:
    print(f"{doc.name}: {doc.extension} with {doc.number_of_pages} pages.")
    print(f"{doc.summary}")
```

 </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
const docList = await client.beta.libraries.documents.list({ libraryId: newLibrary.id });
for (const doc of docList.data) {
    console.log(`${doc.name}: ${doc.extension} with ${doc.numberOfPages} pages.`);
    console.log(`${doc.summary}`);
}
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/libraries/<library_id>/documents?page_size=100&page=0&sort_by=created_at&sort_order=desc" \
     --header "Accept: application/json" \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>
</Tabs>

At first, a new library will not have any documents inside.

### Uploading a Document

You can upload and remove documents from a library.

#### Upload
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
from mistralai.models import File
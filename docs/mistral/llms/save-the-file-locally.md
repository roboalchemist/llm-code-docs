# Save the file locally
with open(f"image_generated.png", "wb") as file:
    file.write(file_bytes)
```

**Generated Image:**
<div style={{ textAlign: 'center' }}>
  <img
    src="/img/agent_generated.png"
    alt="generated_image"
    width="600"
    style={{ borderRadius: '15px' }}
  />
</div>


A full code snippet to download all generated images from a response could look like so:
```py
from mistralai.models import ToolFileChunk

for i, chunk in enumerate(response.outputs[-1].content):
    # Check if chunk corresponds to a ToolFileChunk
    if isinstance(chunk, ToolFileChunk):

      # Download using the ToolFileChunk ID
      file_bytes = client.files.download(file_id=chunk.file_id).read()

      # Save the file locally
      with open(f"image_generated_{i}.png", "wb") as file:
          file.write(file_bytes)
```

  </TabItem>

  <TabItem value="typescript" label="typescript">
Add the following imports:

```typescript


```

Function used to save your image:

```typescript
async function saveStreamToFile(stream: ReadableStream<Uint8Array>, filePath: string): Promise<void> {
    const reader = stream.getReader();
    const writableStream = fs.createWriteStream(filePath);

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        writableStream.write(Buffer.from(value));
    }

    writableStream.end();
}
```

Conversation content retrieval, and call the `saveStreamToFile` function.
```typescript
const entry = conversation.outputs[conversation.outputs.length - 1];
const messageOutputEntry = entry as MessageOutputEntry;

const chunk = messageOutputEntry.content[1];
if (typeof(chunk) != "string" && 'fileId' in chunk) {
    const fileChunk = chunk as ToolFileChunk;
    const fileStream = await client.files.download({ fileId: fileChunk.fileId });
    await saveStreamToFile(fileStream, `image_generated.png`);
}
```

**Generated Image:**
<div style={{ textAlign: 'center' }}>
  <img
    src="/img/agent_generated.png"
    alt="generated_image"
    width="600"
    style={{ borderRadius: '15px' }}
  />
</div>


A full code snippet to download all generated images from a response could look like so:<br></br>


```typescript
async function processFileChunks(conversation: ConversationResponse) {
    const entry = conversation.outputs[conversation.outputs.length - 1];
    const messageOutputEntry = entry as MessageOutputEntry;
    for (let i = 0; i < messageOutputEntry.content.length; i++) {
        const chunk = messageOutputEntry.content[i];
        if (typeof(chunk) != "string" && 'fileId' in chunk) {
            const fileChunk = chunk as ToolFileChunk;
            const fileStream = await client.files.download({ fileId: fileChunk.fileId });
            await saveStreamToFile(fileStream, `image_generated_${i}.png`);
        }
    }
}
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/files/<file_id>/content" \
     --header 'Accept: application/octet-stream' \
     --header 'Accept-Encoding: gzip, deflate, zstd' \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>
</Tabs>


[Websearch]
Source: https://docs.mistral.ai/docs/agents/connectors/websearch

Websearch is the capability to browse the web in search of information, this tool does not only fix the limitations of models of not being up to date due to their training data, but also allows them to actually retrieve recent information or access specific websites.

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/websearch_connector.png"
    alt="websearch_graph"
    width="400"
    style={{ borderRadius: '15px' }}
  />
</div>

Our built-in [connector](../connectors) tool for websearch allows any of our models to access the web at any point to search websites and sources for relevant information to answer the given query, but also open provided URLs from the user.

There are two versions:
- `web_search`: A simple web search tool that enables access to a search engine.
- `web_search_premium`: A more complex web search tool that enables access to both a search engine and to news articles via integrated news provider verification.

## Create a Websearch Agent
You can create an agent with access to websearch by providing it as one of the tools.  
Note that you can still add more tools to the agent, the model is free to search the web or not on demand.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

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
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
const websearchAgent = await client.beta.agents.create({
  model: "mistral-medium-latest",
  name: "WebSearch Agent",
  instructions: "Use your websearch abilities when answering requests you don't know.",
  description: "Agent able to fetch new information on the web.",
  tools: [{ type: "web_search" }],
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
     "name": "Websearch Agent",
     "description": "Agent able to search information over the web, such as news, weather, sport results...",
     "instructions": "You have the ability to perform web searches with `web_search` to find up-to-date information.",
     "tools": [
       {
         "type": "web_search"
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
  "name": "Websearch Agent",
  "description": "Agent able to search information over the web, such as news, weather, sport results...",
  "id": "ag_06835b734cc47dec8000b5f8f860b672",
  "version": 0,
  "created_at": "2025-05-27T12:59:32.803403Z",
  "updated_at": "2025-05-27T12:59:32.803405Z",
  "instructions": "You have the ability to perform web searches with `web_search` to find up-to-date information.",
  "tools": [
    {
      "type": "web_search"
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
Now that we have our websearch agent ready, we can at any point make use of it to ask it questions about recent events.

### Conversations with Websearch

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py
response = client.beta.conversations.start(
    agent_id=websearch_agent.id,
    inputs="Who won the last European Football cup?"
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">
  
```typescript
let conversation = await client.beta.conversations.start({
      agentId: agent.id,
      inputs:"Who is Albert Einstein?",
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
     "inputs": "Who won the last European Football cup?",
     "stream": false,
     "agent_id": "<agent_id>"
  }'
```
  </TabItem>
</Tabs>

For explanation purposes, lets take a look at the output in a readable JSON format.

```json
{
  "conversation_id": "conv_06835b734f2776bb80008fa7a309bf5a",
  "outputs": [
    {
      "type": "tool.execution",
      "name": "web_search",
      "object": "entry",
      "created_at": "2025-05-27T12:59:33.171501Z",
      "completed_at": "2025-05-27T12:59:34.828228Z",
      "id": "tool_exec_06835b7352be74d38000b3523a0cce2e"
    },
    {
      "type": "message.output",
      "content": [
        {
          "type": "text",
          "text": "The last winner of the European Football Cup was Spain, who won the UEFA Euro 2024 by defeating England 2-1 in the final"
        },
        {
          "type": "tool_reference",
          "tool": "web_search",
          "title": "UEFA Euro Winners List from 1960 to today - MARCA in English",
          "url": "https://www.marca.com/en/football/uefa-euro/winners.html",
          "source": "brave"
        },
        {
          "type": "tool_reference",
          "tool": "web_search",
          "title": "UEFA Euro winners: Know the champions - full list",
          "url": "https://www.olympics.com/en/news/uefa-european-championships-euro-winners-list-champions",
          "source": "brave"
        },
        {
          "type": "tool_reference",
          "tool": "web_search",
          "title": "Full list of UEFA European Championship winners",
          "url": "https://www.givemesport.com/football-european-championship-winners/",
          "source": "brave"
        },
        {
          "type": "text",
          "text": "."
        }
      ],
      "object": "entry",
      "created_at": "2025-05-27T12:59:35.457474Z",
      "completed_at": "2025-05-27T12:59:36.156233Z",
      "id": "msg_06835b7377517a3680009b05207112ce",
      "agent_id": "ag_06835b734cc47dec8000b5f8f860b672",
      "model": "mistral-medium-2505",
      "role": "assistant"
    }
  ],
  "usage": {
    "prompt_tokens": 188,
    "completion_tokens": 55,
    "total_tokens": 7355,
    "connector_tokens": 7112,
    "connectors": {
      "web_search": 1
    }
  },
  "object": "conversation.response"
}
```

### Explanation of the Outputs

- **`tool.execution`**: This entry corresponds to the execution of the web search tool. It includes metadata about the execution, such as:
  - `name`: The name of the tool, which in this case is `web_search`.
  - `object`: The type of object, which is `entry`.
  - `type`: The type of entry, which is `tool.execution`.
  - `created_at` and `completed_at`: Timestamps indicating when the tool execution started and finished.
  - `id`: A unique identifier for the tool execution.

- **`message.output`**: This entry corresponds to the generated answer from our agent. It includes metadata about the message, such as:
  - `content`: The actual content of the message, which in this case is a list of chunks. These chunks correspond to the text chunks, the actual message response of the model, interleaved with reference chunks. These reference chunks are used for citations during Retrieval-Augmented Generation (RAG) related tool usages. In this case, it provides the source of the information it just answered with, which is extremely useful for web search. This allows for transparent feedback on where the model got its response from for each section and fact answered with. The `content` section includes:
    - `type`: The type of chunk, which can be `text` or `tool_reference`.
    - `text`: The actual text content of the message.
    - `tool`: The name of the tool used for the reference, which in this case is `web_search`.
    - `title`: The title of the reference source.
    - `url`: The URL of the reference source.
    - `source`: The source of the reference.
  - `object`: The type of object, which is `entry`.
  - `type`: The type of entry, which is `message.output`.
  - `created_at` and `completed_at`: Timestamps indicating when the message was created and completed.
  - `id`: A unique identifier for the message.
  - `agent_id`: A unique identifier for the agent that generated the message.
  - `model`: The model used to generate the message, which in this case is `mistral-medium-2505`.
  - `role`: The role of the message, which is `assistant`.

Another tool that pro-actively uses references is the document library beta connector, feel free to take a look [here](../document_library).   
For more information regarding the use of citations, you can find more [here](../../../capabilities/citations).


[Agents Handoffs]
Source: https://docs.mistral.ai/docs/agents/handoffs

When creating and using Agents, often with access to specific tools, there are moments where it is desired to call other Agents mid-action. To elaborate and engineer workflows for diverse tasks that you may want automated, this ability to give Agents tasks or hand over a conversation to other agents is called **Handoffs**.

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/handoffs.png"
    alt="handoffs_graph"
    width="800"
    style={{ borderRadius: '15px' }}
  />
</div>

## Create an Agentic Workflow

When creating a workflow powered by Handoffs, we first need to create all the Agents that our workflow will use.
There is no limit to how many chained Handoffs a workflow can have. You are free to create multiple Agents using diverse tools, models and handoffs, and orchestrate your own workflow using these Agents.

### Create Multiple Agents

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/multiple_agents_handoffs.png"
    alt="handoffs_graph"
    width="600"
    style={{ borderRadius: '15px' }}
  />
</div>

First things first, let's create diverse Agents with multiple tasks and capabilities.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py
from mistralai import CompletionArgs, ResponseFormat, JSONSchema
from pydantic import BaseModel

class CalcResult(BaseModel):
    reasoning: str
    result: str
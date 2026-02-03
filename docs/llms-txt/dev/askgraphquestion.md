# Source: https://dev.writer.com/blueprints/askgraphquestion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ask graph question

Asks a natural language question using one or more knowledge graphs and puts the result into a state variable.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=44644671f3d1b17ba0292b08f36188a9" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/ask-graph-question-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0cb7e041cb4e460993f759f10b015b58 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1ac4507f6c29142d42dac114545cc57a 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=4970a1878899da33786dc48262a7378d 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c678167c27a0ea43a2d1b7cab1c4a244 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=a206ad5daedda14037a094a4339dd650 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0bfa82fbf5d709da797c925638faaf2c 2500w" />

## Overview

The **Ask graph question** block queries one or more Writer Knowledge Graphs to find relevant information and generate answers based on the stored data. Use it to create AI applications that can reference and retrieve information from your uploaded documents and structured data.

You can specify the question, the list of Knowledge Graphs to search, whether to use streaming or subqueries, and a state variable to store the answer in. The block searches through the Knowledge Graphs and returns a relevant response.

## Common use cases

* Building question-answering systems based on company documents
* Creating AI assistants that reference specific knowledge bases
* Creating compliance verification tools that check against policy documents
* Building research assistants that analyze academic papers or reports

## How it works

1. **Question**: Enter the natural language question you want to ask about the stored data.
2. **Graph Ids**: Specify one or more Knowledge Graphs to query from a list of available Graphs.
3. **Link Variable**: The name of the variable that stores the answer in the agent's state.
4. **Use streaming**: Choose whether to stream the answer as it is generated. If you choose `yes`, the answer will be streamed to the UI as it is generated. If you choose `no`, the answer will be generated and then returned to the agent once it is complete.
5. **Use subqueries**: Enable to allow the LLM to ask follow-up questions to the Knowledge Graph for improved answers.

The block searches the selected Knowledge Graph or Graphs for relevant information and generates an answer based on the stored documents and data.

## Examples

### Employee policy assistant

This example shows a complete workflow where employees can ask questions about company policies and receive accurate, up-to-date information.

**Interface:**

1. **Text input** → Employee submits a question and the text input stores it in a state variable called `question`
2. **Button** → Employee clicks a button to submit the question to the agent
3. **Text** → Employee sees the answer stored in the `policy_answer` state variable in a text block

**Blueprint Flow:**

1. **UI Trigger** → Employee submits policy question through form
2. **Ask graph question** → Searches company knowledge base
3. **Text generation** → Formats the answer for the employee with additional context
4. **Set state** → Stores response for display

**Block Configuration:**

* **Graph Ids:** `["Company Policies", "Employee Handbook"]`
* **Question:** `@{question}` (set from a text input in the UI)
* **Link Variable:** `policy_answer`
* **Use streaming:** `yes`
* **Use subqueries:** `yes`

This workflow ensures employees receive accurate, up-to-date policy information directly from company documents.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block-example.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7d1c89ee4021c8bca59f6508022f1cf4" alt="" data-og-width="2406" width="2406" data-og-height="1434" height="1434" data-path="images/agent-builder/blueprints/ask-graph-question-block-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block-example.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=4279f56b9f715812fc722598e8b2bf08 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block-example.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1a1e12af6be66abccbdc9f40029a7658 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block-example.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=9d2b0a48049e868c7021a3e6a7f88e9c 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block-example.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6cc94fd0648b39d32ec9fdecfc842e0c 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block-example.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=8ca054d280fb70d882e8b5d922c76356 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ask-graph-question-block-example.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b768ac87f3cdd7528604bc695541b756 2500w" />

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Question</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>The natural language question to ask.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Use streaming</td>
      <td>Boolean</td>
      <td>-</td>

      <td>
        <code>yes</code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Link Variable</td>
      <td>Binding</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>Set the variable here and use it across your agent.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Graph Ids</td>
      <td>Graph Ids</td>
      <td>-</td>

      <td>
        <code>""</code>
      </td>

      <td>IDs of the graphs to query.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Use subqueries</td>
      <td>Boolean</td>
      <td>-</td>

      <td>
        <code>yes</code>
      </td>

      <td>Enables LLM to ask follow-up questions to the knowledge graph. This improves answers, but may be slower.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>Successfully streamed the answer.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>There was an error answering the question.</td>
    </tr>
  </tbody>
</table>

The **Ask graph question** block stores the answer to the question in a state variable that you set in the `Link Variable` field. Access the output by referencing the state variable you defined, or use the `@{result}` variable in the next block.

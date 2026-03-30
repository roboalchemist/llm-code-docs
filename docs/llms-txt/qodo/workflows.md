# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/workflows.md

# Workflows

Workflows are [**custom agents**](https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/what-is-an-agent) that can run directly in the IDE. They are single-task executors, triggered to perform a specific job step by step.

Workflows allow you to define agent behaviors, instructions, and tools, but with a visual interface integrated into your development environment.

Use workflows to automate workflows, define reusable processes, and interact with Qodo’s powerful [Agentic Tools](https://docs.qodo.ai/qodo-documentation/qodo-gen/tools-mcps/agentic-tools-mcps). All without leaving your editor.

***

## Getting Started

### How to Use Workflows

To use a workflow, call it with its applicable slash command.&#x20;

In the chatbox in the bottom of the Qodo panel, type / followed by the required workflow's name.

For example:

```
/my-workflow-name
```

Once run, the workflows executes a single, focused job and then exits. It does **not** maintain ongoing context or remain active after completing its task.

You can either create a new workflow or [use Qodo's ready-to-use default workflows](https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/workflows/available-workflows).

***

### Create a New Workflow

In order to create a new agent:

1. Type `/` in the chat input, or click the `/` button, to open the workflow menu.
2. Select `Create new workflow` in the workflow menu, then hit enter.
3. The workflow creation panel will open.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FJdHVHQcd7ByTDsxcmgAN%2FScreenshot%202025-08-18%20at%2014.32.54.png?alt=media&#x26;token=5ec35771-b971-4384-90a9-7c16fa9bc569" alt="" width="510"><figcaption></figcaption></figure>

4. **Name** your workflow (e.g., `review_agent`)
5. **Steps:** Enter natural language instructions for your agent to follow, step-by-step. For example:\
   \&#xNAN;*"1. Review my code changes.*\
   &#x20;*2. Identify potential issues such as anti-patterns, missing error handling, or      excessive complexity.*\
   &#x20;*3. Provide a summary of the findings with recommended improvements.*"
6. **MCP Tools:** From the list, Choose which **MCP tools** the agent should have access to (e.g., `filesystem`, `github`, `shell`).
7. **Preferable model**: From the list, choose a preferable AI model for your workflow to use.
8. **Description**: Add a description for your agent, explaining what it does.
9. Click the **Save** button.

Your newly created workflow is ready to run immediately.

In the chatbox in the bottom of the Qodo panel, type `/` followed by the workflow's name.

### Sharing and reusing workflows

Qodo makes it easy to collaborate by letting you share and reuse custom workflows across your team.

#### **Share Button**

Click the share button in a workflow's configuration page to share your workflow (click on the menu button on the top right, then choose **Share .toml**).

This allows you to export the workflow's configuration [as a `.toml` file](https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/workflows/agent-toml-file), so others can easily import and use it in their environment.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FoT2lmyJ2EzASFMwIHgQH%2FScreenshot%202025-08-18%20at%2014.37.34.png?alt=media&#x26;token=a310adcc-ed23-4bd3-9dcb-8d96d46c0545" alt="" width="177"><figcaption></figcaption></figure>

#### **Edit workflow**

Click the edit button next to a workflow's name to edit its configuration.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FX9yRPjFEccv3j2itzfyK%2FScreenshot%202025-08-18%20at%2014.39.39.png?alt=media&#x26;token=4a808ee8-d6ef-4938-b244-5fc6ce454b64" alt="" width="340"><figcaption></figcaption></figure>

#### **Import workflow from File**

From the workflow menu, choose to upload a `.toml` file to import an existing workflow into Qodo. [Learn more about agent `.toml` file](https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/workflows/agent-toml-file).

This makes it simple to standardize useful tools across your organization, or share helpful setups with teammates.

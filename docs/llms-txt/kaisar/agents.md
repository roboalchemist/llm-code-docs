# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/agents.md

# Agents

Manage AI agents, their configurations, and monitoring.

![Agents List View](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-1558d06e4adc193fa9ae11aef8d89fbe5b8079c0%2Fagents_list_view.png?alt=media)

## Overview

Agents are autonomous AI entities configured to perform specific tasks. This section allows you to manage their lifecycle, monitor their performance, and configure their behaviors.

**Dashboard Summary**:

* **Total Agents**: Total number of agents configured
* **Active**: Number of agents currently active
* **Error**: Number of agents in error state

## Agents List

The agents table displays:

* **Agent**: Name and description (e.g., "Claude Assistant", "Code Reviewer")
* **Type**: AI Provider (e.g., CLAUDE, OPENAI, CUSTOM)
* **Status**: Current state (Active, Error, Maintenance, Busy, Inactive)
* **Environment**: Runtime environment (e.g., x64 @ 8 GB)
* **Last Heartbeat**: Time since last signal
* **Created**: Creation date
* **Actions**: Edit, Delete, etc.

## Creating an Agent

Navigate to **Organization** → **Agents** → Click **+ Create**

![Create Agent Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-8151018e31691777167e95947de087ade45b0e8f%2Fagent_create_form.png?alt=media)

### Basic Information

**Agent Name**\* (Required)

* A unique name to identify this agent
* Example: `Claude Assistant`

**Agent Type**\* (Required)

* Select the AI provider for this agent
* Options: `Claude (Anthropic)`, `OpenAI`, `Custom`

**Description**\* (Required)

* Brief description of what this agent does

**Workspace Path**\* (Required)

* File system path where agent files are stored
* Example: `/workspace/agents/claude-assistant`

### System Prompt

**System Prompt**\* (Required)

* Instructions that define the agent's behavior and personality
* Example: "You are a helpful AI assistant. Always be professional and accurate."

### Configuration

**Model**

* Model identifier (e.g., `claude-3-sonnet`, `gpt-4-turbo`)

**Temperature**

* Controls randomness (0 = deterministic, 1 = creative)

**Max Tokens**

* Maximum response length in tokens

**Anthropic API Version** / **OpenAI Organization**

* Provider-specific settings

**Custom API Endpoint**

* Full URL to your custom AI endpoint (if applicable)

### Environment

* Configure runtime environment variables and resources

### Actions

* **Cancel**: Discard changes
* **Create Agent**: Submit and create the agent

## Viewing Agent Details

To view detailed information about an agent:

1. Navigate to **Organization** → **Agents**
2. Click on an agent from the list
3. View details in the modal dialog

![View Agent](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-4b8c13a64d21e5161c964f330b7e237e8ac15f49%2Fagent_view_details.png?alt=media)

**Details Panel**:

* **Basic Information**: Name, Type, Description, Workspace Path
* **System Prompt**: View the current system prompt
* **Configuration**: View model settings
* **Environment**: View environment settings

## Editing an Agent

To update an agent's configuration:

1. Open agent details
2. Click **Edit** button (or select Edit from list actions)
3. Modify editable fields in the Edit Agent modal

![Edit Agent](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-b37a664c49222480429875a07c70993afbff68ef%2Fagent_edit_form.png?alt=media)

4. Click **Update Agent** to save changes

**Editable Fields**:

* ✅ Basic Information (Name, Description, Workspace Path)
* ✅ System Prompt
* ✅ Configuration (Model, Temperature, etc.)
* ✅ Environment

## Best Practices

* **Specific Prompts**: Write clear, specific system prompts to guide agent behavior
* **Resource Allocation**: Monitor environment usage and adjust resources as needed
* **Error Monitoring**: Check "Error" status agents immediately to resolve issues
* **Version Control**: Keep track of changes to system prompts and configurations

## Next Steps

* Configure [Platform Connections](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/platform-connections) for your agents
* Set up [Tools](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/tools) for your agents to use
* Monitor agent activity in [Analytics](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/analytics)

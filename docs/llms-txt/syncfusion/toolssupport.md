# Source: https://docs.syncfusion.com/code-studio/reference/configure-properties/toolssupport.md

# Tools Support

## Overview

The Tools Support feature in Syncfusion Code Studio empowers developers to perform specific actions within the development environment, such as creating folders, reading files, searching within files, and interacting with browsers. This guide provides a step-by-step approach to use the built-in tools, enabling you to streamline your development workflow and automate tasks efficiently with simple prompts.

## Purpose

The tools are designed to automate and simplify common development tasks, allowing you to focus on writing code. Key purposes include:

### 1. File Management
- Create new files or edit existing ones.
- Perform bulk search-and-replace operations.
- Organize project structures efficiently.

### 2. Terminal Integration
- Run CLI commands like npm install or yarn start.
- Install dependencies or launch development servers.
- Automate build and deployment processes.

### 3. Code Insights
- Identify and fix bugs with AI-driven suggestions.
- Refactor code for better performance or readability.
- Generate inline documentation automatically.

### 4. Web and Browser Tools
- Perform web searches to fetch relevant resources.
- Automate browser tasks like testing or scraping.

## Types of Tools

Syncfusion Code Studio provides a suite of tools to streamline your workflow.You can use two types of tools in chat
 
### 1. Built-In Tools

-	Built-in tools are automatically available in chat.
-	They cover common development tasks and are optimized for working within your workspace.
-	No installation or configuration is required â they are ready to use as soon as you start.

### 2. MCP Tools

-	Model Context Protocol (MCP) is an open standard that enables AI models to use external tools and services through a unified interface.
-	MCP servers provide tools that you can add to Syncfusion Code Studio to extend chat with additional capabilities.
-	To use MCP tools, you must install and configure MCP servers first.
-	MCP servers can run locally on your machine or be hosted remotely.

<img src="../reference-images/tools1.png" alt="Tools" >

### Toolset Overview

Below is a list of some tools and their descriptions for reference

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Tool Name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>agent</td>
      <td>Delegate tasks to other agent.</td>
    </tr>
    <tr>
      <td>codestudio</td>
      <td>Use Code Studio features</td>
    </tr>
    <tr>
      <td>edit</td>
      <td>Edit files in your workspace</td>
    </tr>
    <tr>
      <td>execute</td>
      <td>Execute code and applications on your machine.</td>
    </tr>
    <tr>
      <td>read</td>
      <td>Read files in your workspace</td>
    </tr>
    <tr>
      <td>search</td>
      <td>Search files in your workspace</td>
    </tr>
    <tr>
      <td>todo</td>
      <td>Manage and track todo items for task planning</td>
    </tr>
    <tr>
      <td>web</td>
      <td>Fetch information from the web</td>
    </tr>
  </tbody>
</table>

## How to Enable Tools for Chat

Before you can use tools in chat, you need to enable them in the **Chat view**. Tools can be enabled or disabled on a per-request basis using the **tools picker**. 

> **Note:** Select the agent after that tool picker is visible in the chat. Select only the tools that are relevant to your prompt to improve results.

### How to access the tools picker

**Step 1** : Click the Syncfusion Code Studio icon. The chat window is displayed.

<img src="../reference-images/tools2.png" alt="Tools" >

**Step 2**: Select the Agent in the chat window.

**Step 3** : Click the Configure Tools button in the chat input field. The tools are displayed.

<img src="../reference-images/tools3.png" alt="Tools" >

> **Note:** Must select the Agent to access the configuration tools.

**Step 4** : Select or deselect tools to control which ones are available for the current request.

<img src="../reference-images/tools4.png" alt="Tools" >

**ð¡Tip** : Use the search box to quickly filter the list of tools.

## How to use tools in your prompts

You can explicitly reference tools in your prompts by typing **#** followed by the **tool name**. This is useful when you want to ensure that a specific tool is used. Type **#** in the chat input field to see a list of available tools.

<img src="../reference-images/tools5.png" alt="Tools" >

**Example of a tool reference:**

<img src="../reference-images/tools6.png" alt="Tools" >

## Tools Approval

When using agents, the agent automatically determines which tools to use from the enabled set based on your prompt and the context of your request. The agent autonomously selects and invokes the relevant tools needed to accomplish the task.

Some tools require your approval before they can run. This is a security measure because tools may perform actions that modify files, change your environment, or attempt prompt injection attacks through malicious output.

<img src="../reference-images/tools7.png" alt="Tools" >

> **Note:** Always review tool parameters carefully before approving, especially for tools that modify files, run commands, or access external services.


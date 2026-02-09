# Source: https://docs.agent.ai/actions/add_to_list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Add to List

## Overview

The "Add to List" action lets you add items to an existing list variable. This allows you to collect multiple entries or build up data over time within your workflow.

### Use Cases

* **Data Aggregation**: Collect multiple responses or items into a single list

* **Iterative Storage**: Track user selections or actions throughout a workflow

* **Building Collections**: Create lists of related items step by step

* **Dynamic Lists**: Add user-provided items to predefined lists

## Configuration Fields

### Input Text

* **Description**: Enter the text to append to the list.

* **Example**:  Enter what you want to add to the list

  1. Can be a fixed value: "Sample item"

  2. Or a variable: \{\{first\_task}}

  3. Or another list: \{\{additional\_tasks}}

* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the updated list.

* **Example**: "task\_list" or "user\_choices."

* **Validation**: Only letters, numbers, and underscores (\_) are allowed.

* **Required**: Yes

## **Example: Example Agent for Adding and Using Lists**

See this [simple Task Organizer Agent](https://agent.ai/agent/lists-agent-example). It collects an initial task, creates a list with it, then gathers additional tasks and adds them to the list. The complete list is then passed to an AI for analysis.&#x20;

# Source: https://docs.agent.ai/actions/get_user_knowledge_base_and_files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get User KBs and Files

## Overview

The "Get User Knowledge Base and Files" action retrieves information from user-selected knowledge bases and uploaded files to support decision-making within the workflow.

### Use Cases

* **Content Search**: Allow users to select a knowledge base to search from.
* **Resource Management**: Link workflows to specific user-uploaded files.

## Configuration Fields

### User Prompt

* **Description**: Provide a prompt for users to select a knowledge base.
* **Example**: "Choose the knowledge base to search from."
* **Required**: Yes

### Required?

* **Description**: Mark as required if selecting a knowledge base is essential for the workflow.
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the knowledge base ID.
* **Example**: "selected\_kb" or "kb\_source."
* **Validation**:
  * Only letters, numbers, and underscores (\_) are allowed.
  * No spaces, special characters, or dashes.
  * **Regex**: `^[a-zA-Z0-9_]+$`
* **Hint**: This variable will be used to reference the knowledge base in subsequent steps.
* **Required**: Yes

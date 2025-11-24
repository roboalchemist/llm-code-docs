# Source: https://docs.agent.ai/actions/get_user_list.md

# Get User List

## Overview

The "Get User List" action collects a list of items entered by users and splits them based on a specified delimiter or newline.

### Use Cases

* **Batch Data Input**: Gather a list of email addresses or item names.
* **Bulk Selection**: Allow users to input multiple options in one field.

## Configuration Fields

### User Prompt

* **Description**: Write a clear prompt to guide users on what information is required.
* **Example**: "Enter the list of email addresses separated by commas."
* **Required**: Yes

### List Delimiter (leave blank for newline)

* **Description**: Specify the character that separates the list items.
* **Example**: Use a comma (,) for "item1,item2,item3" or leave blank for newlines.
* **Required**: No

### Required?

* **Description**: Mark this checkbox if this input is mandatory.
* **Example**: Enable if a response is essential to proceed in the workflow.
* **Required**: No

### Output Variable Name

* **Description**: Assign a unique variable name for the input value.
* **Example**: "email\_list" or "item\_names."
* **Validation**:
  * Only letters, numbers, and underscores (\_) are allowed.
  * No spaces, special characters, or dashes.
  * **Regex**: `^[a-zA-Z0-9_]+$`
* **Hint**: This variable will be used to reference the list in subsequent steps.
* **Required**: Yes

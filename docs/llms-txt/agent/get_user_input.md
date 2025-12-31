# Source: https://docs.agent.ai/actions/get_user_input.md

# Get User Input

## Overview

The "Get User Input" action allows you to capture dynamic responses from users, such as text, numbers, URLs, and dropdown selections. This action is essential for workflows that require specific input from users to proceed.

### Use Cases

* **Survey Form**: Collect user preferences or feedback.
* **Authentication**: Prompt for email addresses or verification codes.
* **Customized Workflow**: Ask users to select options to determine the next steps.

## Configuration Fields

### Input Type

* **Description**: Choose the type of input you want to capture from the user.
* **Options**:
  * **Text**: Open-ended text input.
  * **Number**: Numeric input only.
  * **Yes/No**: Binary selection.
  * **Textarea**: Multi-line text input.
  * **URL**: Input limited to URLs.
  * **Website Domain**: Input limited to domains.
  * **Dropdown (single)**: Single selection from a dropdown.
  * **Dropdown (multiple)**: Multiple selections from a dropdown.
  * **Multi-Item Selector**: Allows selecting multiple items.
  * **Multi-Item Selector (Table View)**: Allows selecting multiple items in a table view.
  * **Radio Select (single)**: Single selection using radio buttons.
  * **HubSpot Portal**: Select a portal.
  * **HubSpot Company**: Select a company.
  * **Knowledge Base**: Select a knowledge base.
* **Hint**: Select the appropriate input type based on your data collection needs. For example, use "Text" for open-ended input or "Yes/No" for binary responses.
* **Required**: Yes

### User Prompt

* **Description**: Write a clear prompt to guide users on what information is required.
* **Example**: "Please enter your email address" or "Select your preferred contact method."
* **Required**: Yes

### Default Value

* **Description**: Provide a default response that appears automatically in the input field.
* **Example**: "[example@domain.com](mailto:example@domain.com)" for an email field.
* **Hint**: Use this field to pre-fill common or expected responses to simplify input for users.
* **Required**: No

### Required?

* **Description**: Mark this checkbox if this input is mandatory.
* **Example**: Enable if a response is essential to proceed in the workflow.
* **Required**: No

### Output Variable Name

* **Description**: Assign a unique variable name for the input value.
* **Example**: "user\_email" or "preferred\_contact."
* **Validation**:
  * Only letters, numbers, and underscores (\_) are allowed.
  * No spaces, special characters, or dashes.
  * **Regex**: `^[a-zA-Z0-9_]+$`
* **Hint**: This variable will be used to reference the input value in subsequent steps.
* **Required**: Yes

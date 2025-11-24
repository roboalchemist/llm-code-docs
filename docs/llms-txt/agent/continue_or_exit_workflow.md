# Source: https://docs.agent.ai/actions/continue_or_exit_workflow.md

# Continue or Exit Workflow

## Overview

Evaluate conditions to decide whether to continue or exit the workflow, providing control over the process flow.

### Use Cases

* **Conditional Completion**: End a workflow if certain criteria are met.
* **Dynamic Navigation**: Determine the next step in the workflow based on user input or data.

## Configuration Fields

### Condition Logic

* **Description**: Define the condition logic using Jinja template syntax.
* **Example**: "if user\_age > 18" or "agent\_control = 'exit'."
* **Required**: Yes

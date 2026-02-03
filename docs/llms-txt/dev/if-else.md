# Source: https://dev.writer.com/blueprints/if-else.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# If-Else

Evaluate custom Python code and redirect to 'true' or 'false' branch. Useful for conditional logic.

<img src="https://mintcdn.com/writer/AUM2TsZWJvQTGd3c/images/agent-builder/blueprints/if-else-block.png?fit=max&auto=format&n=AUM2TsZWJvQTGd3c&q=85&s=f9e8df709ca05a6147f4eb92d6ffa288" alt="" data-og-width="2294" width="2294" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/if-else-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/AUM2TsZWJvQTGd3c/images/agent-builder/blueprints/if-else-block.png?w=280&fit=max&auto=format&n=AUM2TsZWJvQTGd3c&q=85&s=b29a8f70526d6ee6183245d18c1e6a9c 280w, https://mintcdn.com/writer/AUM2TsZWJvQTGd3c/images/agent-builder/blueprints/if-else-block.png?w=560&fit=max&auto=format&n=AUM2TsZWJvQTGd3c&q=85&s=6e0cfc05536ba9487539a8055833661b 560w, https://mintcdn.com/writer/AUM2TsZWJvQTGd3c/images/agent-builder/blueprints/if-else-block.png?w=840&fit=max&auto=format&n=AUM2TsZWJvQTGd3c&q=85&s=959c3be96dc9ff38f342afdec2dadbe3 840w, https://mintcdn.com/writer/AUM2TsZWJvQTGd3c/images/agent-builder/blueprints/if-else-block.png?w=1100&fit=max&auto=format&n=AUM2TsZWJvQTGd3c&q=85&s=bb13ba02c50e53e4ead60b8d92bebae9 1100w, https://mintcdn.com/writer/AUM2TsZWJvQTGd3c/images/agent-builder/blueprints/if-else-block.png?w=1650&fit=max&auto=format&n=AUM2TsZWJvQTGd3c&q=85&s=47221fcd41dbc009eb152637f0c75040 1650w, https://mintcdn.com/writer/AUM2TsZWJvQTGd3c/images/agent-builder/blueprints/if-else-block.png?w=2500&fit=max&auto=format&n=AUM2TsZWJvQTGd3c&q=85&s=609a409ad1f5918926f6a2029d52ef0a 2500w" />

## Overview

The **If-Else** block evaluates a Python expression and routes workflow execution to either a **True** or **False** branch based on the result. Use it to create conditional logic in your blueprints, enabling different actions based on data conditions.

The expression must be a single Python expression that evaluates to a Boolean value. You can use variables, comparison operators, logical operators, and built-in Python functions in your expression.

## Common use cases

* Validating user input before processing
* Checking if data meets specific criteria
* Routing workflows based on configuration settings
* Implementing business rules and decision logic
* Verifying API responses or data availability

## How it works

1. **Expression**: Enter a Python expression that evaluates to `True` or `False`. The expression must be a single expression, not multiple statements.
2. **Evaluation**: The block evaluates the expression using the Python interpreter.
3. **Routing**: Based on the result:
   * If the expression evaluates to `True`, the workflow continues to the **True** branch
   * If the expression evaluates to `False`, the workflow continues to the **False** branch
   * If an error occurs during evaluation, the workflow continues to the **Error** branch

The block has access to [state variables](/agent-builder/state), [execution environment variables](/agent-builder/execution-environment), and standard Python operations.

### Expression examples

<CodeGroup>
  ```python Comparing values theme={null}
  state["age"] >= 18
  ```

  ```python Checking data presence theme={null}
  "email" in state and state["email"]
  ```

  ```python Multiple conditions theme={null}
  state["score"] > 80 and state["completed"] == True
  ```

  ```python Type checking theme={null}
  isinstance(payload, dict) and "user_id" in payload
  ```

  ```python String operations theme={null}
  state.get("status", "").lower() == "approved"
  ```
</CodeGroup>

## Examples

### Data quality validation

This example shows how to validate API response data before processing it further in the workflow.

**Blueprint Flow:**

1. **HTTP Request** → Fetches data from external API
2. **If-Else** → Validates response contains required fields
   3a. **True branch → Text generation** → Processes valid data
   3b. **False branch → Log message** → Records validation failure

**Block Configuration:**

* **Expression:** `isinstance(result, dict) and "data" in result and len(result["data"]) > 0`

This workflow ensures data quality before processing, preventing errors downstream.

### Score-based routing

This example demonstrates routing users to different workflows based on their performance score.

**Blueprint Flow:**

1. **UI Trigger** → User completes assessment
2. **Python code** → Calculates total score
3. **If-Else** → Checks if score meets passing threshold
   4a. **True branch → Text generation** → Generates certificate
   4b. **False branch → Text generation** → Generates improvement recommendations

**Block Configuration:**

* **Expression:** `state["total_score"] >= state["passing_threshold"]`

This workflow provides personalized responses based on user performance metrics.

<Tip>
  **Choosing the right block:**

  * **Use If-Else** for rule-based logic with exact conditions: numeric comparisons (`age >= 18`), data validation (`"email" in state`), checking Boolean flags, or evaluating structured data. Best when you know the exact criteria to evaluate.

  * **Use [Classification](/blueprints/classification)** for content-based routing: categorizing text by topic, sentiment, or intent. Best when you need AI to understand natural language meaning and route to multiple categories (for example, classifying support tickets as "Technical", "Billing", or "General").

  * **Use [Python code](/blueprints/pythoncode)** before If-Else for complex logic: when you need multiple statements, loops, or calculations before the conditional check. Store the result in state, then reference it in the If-Else expression.

  **Expression requirement:** The If-Else block accepts only a single Python expression that evaluates to a Boolean value, not multiple statements.
</Tip>

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
      <td>Expression</td>
      <td>Eval</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>The expression to be evaluated. Must be a single expression (no statements).</td>

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
      <td>True</td>
      <td>-</td>
      <td>success</td>
      <td>The event handler execution for True.</td>
    </tr>

    <tr>
      <td>False</td>
      <td>-</td>
      <td>success</td>
      <td>The event handler execution for False.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>The expression evaluation failed.</td>
    </tr>
  </tbody>
</table>

# Source: https://dev.writer.com/blueprints/pythoncode.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Python code

Runs custom Python code. Useful for logic not covered by existing blocks.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-code-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0e036182b28e067fbb66aa61b0c1a234" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/python-code-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-code-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c40908b77a2e4b23a4db43edf7bda0f0 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-code-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=4daf1507746d13adbd6310c8c8111c1d 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-code-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=40e6c064f3e1b43674e282e92f5110df 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-code-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=29f1f9d99ed61493e5a3df096471cb7a 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-code-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=91f52c2c1f9fb1d55a48cb4371e222ca 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-code-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=89e5dbb984b7b941cb5c521bf9461864 2500w" />

## Overview

The Python code block allows you to write Python code to extend your blueprint's functionality. Use it to perform custom data processing, calculations, API integrations, or any other logic that requires Python programming capabilities.

## Common use cases

* Custom data processing and transformations
* Complex calculations and mathematical operations
* API integrations with external services
* File manipulation and data parsing

## How it works

1. **Code execution**: Write Python code in the block's code editor.
2. **Variable access**: Access [state variables](/agent-builder/state), [environment variables](/agent-builder/execution-environment), and [preinstalled libraries](/agent-builder/python-libraries).
3. **Output generation**: Use `set_output()` to return values to subsequent blocks.
4. **Error handling**: Handle exceptions and provide meaningful error messages. If an error occurs, access the error message in the next block using `@{message}`.
5. **Error exit condition**: Raise an `Exception` to trigger the **Error** exit condition and route to error handling blocks.

The block provides a full Python environment with access to [state variables](/agent-builder/state), [execution environment variables](/agent-builder/execution-environment), and [preinstalled libraries](/agent-builder/python-libraries).

## Examples

### Calculate average from list

This example shows how to return a value from the Python code block. It calculates the average of a list of numbers and returns the result to the next block by using the `set_output` function.

**Blueprint flow:**

1. **UI Trigger** → User provides list of numbers
2. **Python code** → Calculates average of numbers
3. **Set state** → Stores result in state variable

```python  theme={null}
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

average = calculate_mean(state["numbers"])
set_output(average)
```

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-block-example.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0622225769970e6d301f15bf65a07014" alt="" data-og-width="2352" width="2352" data-og-height="1086" height="1086" data-path="images/agent-builder/blueprints/python-block-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-block-example.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=5a6cbfedfa31d2c64c09dcc63ec7a66a 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-block-example.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=456db592e3942f5efb3312c1bb144481 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-block-example.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f95463d5f045651586c89a4a075ec9d7 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-block-example.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7948f94765a9de8cccd4901b5e033ffe 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-block-example.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=290b659aae36422fbf66e92d6140d9ca 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/python-block-example.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=31cf9cf882da337b8c4c6efe6c53c197 2500w" />

### Error handling with exceptions

You can trigger the **Error** exit condition by raising an `Exception` in your Python code. This allows you to route to error handling blocks when specific conditions are met.

**Example:**

```python  theme={null}
# Validate user input and raise exception if invalid
user_age = state.get("age", 0)

if user_age < 0 or user_age > 120:
    raise Exception("Invalid age: Age must be between 0 and 120")

if not state.get("email"):
    raise Exception("Missing required field: Email address")

# Process valid data
set_output({"status": "valid", "age": user_age})
```

When an `Exception` occurs, the Python code block exits with the **Error** condition, allowing you to route to error handling blocks in your blueprint. You can access the error message in the next block by referencing the `@{message}` variable.

## Available variables and libraries

Python code block can access the following global variables and libraries:

* [State variables](/agent-builder/state)
* [Execution environment variables](/agent-builder/execution-environment)
* [Preinstalled Python libraries](/agent-builder/python-libraries)
* Functions you've defined in your `main.py` file

### Return values from the Python code block

To return a value from a Python code block and store it in the `result` execution environment variable, you must use the `set_output` function.

Anything that runs in the block but is not returned in the `set_output` function does not get passed to the next block.

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
      <td>Code</td>
      <td>Code</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>The code to be executed.</td>

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
      <td>The code executed successfully.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>There was an error executing the code.</td>
    </tr>
  </tbody>
</table>

Access the output of a **Python code** block using the `@{result}` variable in the block that follows it in a blueprint. The output contains whatever value was passed to the `set_output()` function.

Access the error message of a **Python code** block using the `@{message}` variable in the block that follows it in a blueprint. The error message contains whatever value was passed to the `raise Exception` function.

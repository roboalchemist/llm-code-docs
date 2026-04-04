# Source: https://docs.agent.ai/actions/serverless_function.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Serverless Function

## Overview

Serverless Functions allow your agents to execute custom code in the cloud without managing infrastructure. This powerful capability enables complex operations and integrations beyond what standard actions can provide.

### Use Cases

* **Custom Logic Implementation**: Execute specialized code for unique business requirements
* **External System Integration**: Connect with third-party services and APIs
* **Advanced Data Processing**: Perform complex calculations and transformations
* **Extended Functionality**: Add capabilities not available in standard Agent.ai actions

<iframe width="560" height="315" src="https://www.youtube.com/embed/n5nTAzKGy18?si=6iUG3xZu3ekwG3GU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## **How Serverless Functions Work**

Serverless Functions in Agent.ai:

1. Run in AWS Lambda (fully managed by Agent.ai)
2. Support Python and Node.js
3. Automatically deploy when you save the action
4. Generate a REST API endpoint for programmatic access

## Creating a Serverless Function

1. In the Actions tab, click "Add action"
2. Select the "Workflow & Logic" category
3. Choose "Call Serverless Function"

## Configuration Fields

### Language

* **Description**: Select the programming language for the serverless function.
* **Options**: Python, Node
* **Required**: Yes

### Serverless Code

* **Description**: Write your custom code.
* **Example**: Python or Node script performing custom logic.
* **Required**: Yes

### Serverless API URL

* **Description**: Provide the API URL for the deployed serverless function.
* **Required**: Yes (auto-generated upon deployment)

### Output Variable Name

* **Description**: Assign a variable name to store the result of the serverless function.
* **Example**: "function\_result" or "api\_response."
* **Validation**: Only letters, numbers, and underscores (`_`) are allowed.
* **Required**: Yes

### Deploy and Save

1. Click "Save"
2. After successful deployment, the serverless action can be used

### Using Function Results

The function's output is stored in your specified variable name. You can access specific data points using dot notation, for example:

* `{{variable_name.message}}`
* `{{variable_name.input}}`

## Accessing Agent Variables

When your agent runs a serverless function, any context variables created earlier in the workflow are passed into your function as part of the event object.

Understanding how to access these variables is key to using serverless functions effectively.

<iframe width="560" height="315" src="https://www.youtube.com/embed/bGnCZpjKJWw?si=oeyi6XDsFcW-sTOl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Inspecting the Event Structure

To inspect the data being passed to your function, you can set up a basic debug function. This is helpful for confirming that your agent variables are available and structured as expected.

```python  theme={null}
import json

def execute(event, context):
    debug_info = {
        "received_event": json.dumps(event),
        "received_context": str(context)
    }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "debug_info": debug_info
        })
    }
```

Running your agent with this code will return the full contents of the event and context objects. In most cases, the information you’ll want is located here:

`event['body']['context']`

This nested context object contains your agent's variables—such as out\_topic, out\_summary, and others defined earlier in your workflow.

### Accessing Variables in Your Code

Once you understand the structure, you can write your function to access specific values like this:

```python  theme={null}
import json

def execute(event, context):
    body = event.get('body', {})
    agent_context = body.get('context', {})

    topic = agent_context.get('out_topic')
    summary = agent_context.get('out_summary')

    result = f"The topic is {topic} and the summary is {summary}"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }
```

You can now use these variables to power more complex logic in your serverless functions.

### Notes on Debugging

* Use the `return` statement to pass debugging information back to the agent UI. `print()` statements will only appear in AWS logs.
* The context panel in [Agent.ai](http://Agent.ai) shows the variables currently available to your serverless function—this can help confirm what’s being passed in.
* If your function isn’t behaving as expected, start by confirming that the data is structured as described above.

## Example: Serverless Function Agent

See [this simple Message Analysis Agent](https://agent.ai/agent/serverless-function-example) that demonstrates how to use Serverless Functions:

1. **Step 1**: Get user input text message
2. **Step 2**: Call a serverless function that analyzes:
   * Word count
   * Character count
   * Sentiment (positive/negative/neutral)
3. **Step 3**: Display the results in a formatted output

This sample agent shows how Serverless Functions can extend your agent's capabilities with custom logic that would be difficult to implement using standard actions alone.

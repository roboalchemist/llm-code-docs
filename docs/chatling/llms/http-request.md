# Source: https://docs.chatling.ai/chatbot/builder/blocks/action/http-request.md

# Source: https://docs.chatling.ai/ai-agent/actions/http-request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# HTTP Request

The HTTP Request action allows the AI Agent to connect to external APIs and services during the chat and perform an action.

The Agent can collect the needed inputs from the user, pull values from chat history, or use saved contact data—then send the request and use the result to respond or take the next step.

## Configuration

### `Action Name`

A short, specific identifier that tells the Agent what this action does (e.g. check\_order\_status, create\_support\_ticket).

### `When to Use`

A detailed description of what the action does and when it must be used.

When applicable, you can specify one or more of the following:

* **Positive cues/phrases**: Example utterances and keywords that signal this action (include a few variations).
* **Preconditions**: What must be true before running.
* **Do not use when**: Explicit exclusions to avoid false triggers.

### `Frequency`

Specify how often the Agent can invoke this action to avoid overusing it, e.g `Once per chat` or `Whenever applicable`.

### `Input parameters`

Define the parameters the Agent must gather before sending the request. The Agent can capture these from user input, existing chat context, or saved contact data.

For each parameter, you can specify the following:

* **Name**: The name of the parameter. Must start with a letter and contain only letters, numbers, and underscores.
* **Description** (optional): A description of the parameter to indicate what it is and if applicable, the formatting rules and min/max length.
* **Save to variable** (optional): The variable where the data can be saved. Applicable when you want to use the data in the HTTP request's parameters, such as URL, body, headers, etc.

### `Request`

Configure how the HTTP call is made.

* **Method**: GET, POST, PUT, PATCH, DELETE
* **URL**: Enter the request URL, such as an API endpoint.
* **Query Params** (optional): Key-value pairs appended to the URL.
* **Body** (optional): The request payload which can be passed as form data, form URL encoded, or raw JSON.
* **Headers** (optional): Data to be sent as the headers of the request, such as Content-Type and Authorization.

### `Test Request`

Run a live test with sample input values to confirm that it's working.

The request must succeed before the action can be created. A request is considered successful if it returns a 2xx status code and a valid JSON response.

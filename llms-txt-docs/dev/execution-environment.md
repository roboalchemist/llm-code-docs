# Source: https://dev.writer.com/agent-builder/execution-environment.md

# Using data from previous blocks

> Pass data between blocks in Agent Builder blueprints. Access state variables, secrets, and results from preceding blocks with execution environment.

Agents can pass data between blocks in the blueprint and the UI to create dynamic workflows. Each block operates with a set of variables in its execution environment.

The execution environment includes the agent's [state variables](/agent-builder/state) and [secrets](/agent-builder/secrets), along with the results and inputs from the preceding blocks in the blueprint. You can access variables from the execution environment in the blueprint and in custom code.

The most common use case for the execution environment is to access the result of the preceding block. Each blueprint block that runs passes its result to the next block in the blueprint, which you can access with the `@{result}` variable in the following block.

The execution environment is specific to each block in the blueprint and changes based on the block's inputs, outputs, and state.

This document includes:

* [An explanation of the execution environment](#execution-environment-explained)
* [A table of variables available in the execution environment](#variables-available-to-each-block)
* [Examples of how to access variables in the execution environment](#access-execution-environment-variables)

## Execution environment explained

Think of an execution environment like a toolbox that a block can access while it's running. This toolbox contains useful information that your agent needs to do its job, like remembering information from earlier steps or accessing important values you've saved. Blocks can add, remove, and update variables in the execution environment as they run.

Most of the information in the toolbox is primarily useful for internal use, debugging, and advanced use cases, but `@{result}` is particularly important for you as you build workflows.

Whenever a block finishes running, it adds its result to the execution environment. This result is then available to the next block in the blueprint so it can act on it.

<img src="https://mintcdn.com/writer/AfqfjP6jBmTFWZzr/images/agent-builder/execution-environment.png?fit=max&auto=format&n=AfqfjP6jBmTFWZzr&q=85&s=92ecc2e4f23d2c055261917c3a229b4f" alt="" data-og-width="2781" width="2781" data-og-height="879" height="879" data-path="images/agent-builder/execution-environment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/AfqfjP6jBmTFWZzr/images/agent-builder/execution-environment.png?w=280&fit=max&auto=format&n=AfqfjP6jBmTFWZzr&q=85&s=18641488b5ff70f60874bbd0b68ef79c 280w, https://mintcdn.com/writer/AfqfjP6jBmTFWZzr/images/agent-builder/execution-environment.png?w=560&fit=max&auto=format&n=AfqfjP6jBmTFWZzr&q=85&s=3d99193fea9f7056eb6309105ca969d9 560w, https://mintcdn.com/writer/AfqfjP6jBmTFWZzr/images/agent-builder/execution-environment.png?w=840&fit=max&auto=format&n=AfqfjP6jBmTFWZzr&q=85&s=42078254c8f8660273f2daff8f7fd9a5 840w, https://mintcdn.com/writer/AfqfjP6jBmTFWZzr/images/agent-builder/execution-environment.png?w=1100&fit=max&auto=format&n=AfqfjP6jBmTFWZzr&q=85&s=1c821542a1686ccbbe519027dd4807db 1100w, https://mintcdn.com/writer/AfqfjP6jBmTFWZzr/images/agent-builder/execution-environment.png?w=1650&fit=max&auto=format&n=AfqfjP6jBmTFWZzr&q=85&s=5dd9f454fb3fe58de32338324997aba0 1650w, https://mintcdn.com/writer/AfqfjP6jBmTFWZzr/images/agent-builder/execution-environment.png?w=2500&fit=max&auto=format&n=AfqfjP6jBmTFWZzr&q=85&s=51392ae3e3b86b26d5d49233fad00cf0 2500w" />

### Example from a blueprint

Consider the following section of a blueprint that generates text based on a specific prompt. It shows two connected blocks:

* A **Text generation** block that generates text based on a specific prompt
* A **Set state** block that sets a state variable with the results of the **Text generation** block

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-example.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4560c3db84629182529e4440fcb8b0af" alt="" data-og-width="1503" width="1503" data-og-height="670" height="670" data-path="images/agent-builder/execution-environment-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-example.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=99faea70c5ad70ff6d10342388afc98b 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-example.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=b8b76e47feefa7adc4431d18af3e4ca1 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-example.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5e1341daa9f2be2c4705f99b4790439e 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-example.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=23ed9a467ba7ee40b2ab3692ca980e36 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-example.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4ddcf22bc20875720041e1dd61210fa3 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-example.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=b0ad54ea15799a8f7f3bbd0304e58341 2500w" />

* The **Text generation** block uses the state variable `product` to access information that the user input via the UI. It then generates text based on that information.
* The **Set state** block's execution environment includes the `result` variable from the **Text generation** block, which is the summary of the file. It sets a state variable with that result so that the UI can display the summary.

## Variables available to each block

The following table shows the variables that are available to each block in the execution environment. Not all variables are available in all blocks; for example, the `api_calls` variable is only available when the block makes an API call.

Many of these variables are primarily useful for internal use, debugging, and advanced use cases. However, the `result` variable is particularly useful for building workflows.

| Variable         | Type          | Description                                                                                                                                                                                                                                       | Example                                                                                                                      |
| ---------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `api_calls`      | `array[dict]` | Any Writer API calls that the agent made at this block, including the request and the response. For example, API calls from a **Text generation** block to the Writer [chat completions](/api-reference/completion-api/chat-completion) endpoint. | `[{'request': {'method': 'POST', ...}, 'response': {'status_code': 200, ...}}]`                                              |
| `call_stack`     | `dict`        | The call stack of the agent. The key is the index of the block in the call stack and the value is the block ID.                                                                                                                                   | `{0: "123abc", 1: "456def"}`                                                                                                 |
| `context`        | `dict`        | The ID of the block that triggered the blueprint execution and the event that triggered it.                                                                                                                                                       | `{'target': '123abc', 'event': 'wf-click'}`                                                                                  |
| `httpx_requests` | `array[dict]` | Any HTTP requests that the agent made at this block, including the request and the response.                                                                                                                                                      | `[{'request': {'method': 'POST', ...}, 'response': {'status_code': 200, ...}}]`                                              |
| `item`           | Any           | An individual item in a **For-each** block loop. The type of the item varies based on the values provided to the **For-each** block. For a dictionary, this is the value of the item. For a list, this is the item itself.                        | `file123`                                                                                                                    |
| `itemId`         | `str`         | The ID of the individual item in a **For-each** block loop. For a list, this is its index in the loop, starting at 0. For a dictionary, this is the key of the item.                                                                              | `0`                                                                                                                          |
| `message`        | `str`         | The error message if a block failed with an error.                                                                                                                                                                                                | `"Invalid input: age must be a number"`                                                                                      |
| `result`         | varies        | The result of the preceding block. The type of the result varies based on the block.                                                                                                                                                              | `Thank you so much for your wonderful review! We're thrilled to hear that you've found the perfect tailored blazer with us.` |
| `results`        | `dict`        | The full list of results from all blocks in the blueprint. It's a dictionary where the key is the block ID and the value is the result of the block. If the block hasn't run yet, the value is `null`.                                            | `{'123abc': 'Thank you so much...', '456def': '%Generating response...', '789ghi': null}`                                    |
| `session`        | `dict`        | Session information, such as the session ID, cookies, headers, and user information.                                                                                                                                                              | `{'id': '123', 'cookies': {...}, 'headers': {...}, 'userInfo': {}}`                                                          |
| `state`          | `dict`        | The agent's [state variables](/agent-builder/state).                                                                                                                                                                                              | `{'user_name': 'John', 'persona': 'sales'}`                                                                                  |
| `target`         | `str`         | The ID of the next block to run.                                                                                                                                                                                                                  | `'123abc'`                                                                                                                   |
| `ui`             | `object`      | The UI of the agent as a WriterUIManager object. This is a Python object that allows you to interact with the UI of the agent via custom code.                                                                                                    |                                                                                                                              |

## Access execution environment variables

### In blueprint blocks

You can read the execution environment variables in blueprint blocks using `@{variable_name}` syntax. For example, `@{result}` accesses the result of the preceding block.

This example shows a **Set state** block that uses the `@{result}` variable to access the result of the preceding block. The block sets a state variable `message` with the string `Result: ` and the output of the preceding block.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d50c641d8693637dab3352efc66a46af" alt="" data-og-width="2854" width="2854" data-og-height="1704" height="1704" data-path="images/agent-builder/execution-environment-set-state-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=fd750aba913556a2590665f2bdcd82b2 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=0136e42ba6cee0a90d700ae6a90af9f3 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e4562255cdcc968a6082c51f0f168b53 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=36584b922faf6ef688a505cad293f2b3 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9d304ba8506a4e94faf6e209ee600ec4 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=1e6640cf6ee1817eccc7e48067cbb270 2500w" />

#### Nested variable syntax

You can access nested variables in blueprint blocks using dot notation. For example, `@{result.0.id}` accesses the `id` field of the first result of the preceding block.

This example shows a **Set state** block to set a `file_id` state variable from an **Add files to Writer Cloud** block. It uses `@{result.0.id}` to access the `id` field of the first item in the result of the preceding block.

Here is the what the `result` variable looks like in the execution environment. It's possible to add multiple files to Writer Cloud, so the `result` variable from this block is an array of dictionaries. The `0` index accesses the first item in the array.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-result-variable.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d598d08eee8fa476772cb9cda39c5a2a" alt="" data-og-width="800" width="800" data-og-height="314" height="314" data-path="images/agent-builder/execution-environment-result-variable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-result-variable.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=823197df66fe120a62e5d70c007c243c 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-result-variable.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=be6660ab209235be65b6f45727cfea89 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-result-variable.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7f6cc4d3c9453d80936c7195c1c83ce1 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-result-variable.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c775d0619bb3eaf58c131ce3eed7d392 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-result-variable.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=22acc80a9c388ce65a8e7387a20d1030 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-result-variable.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5e4b112b70a01ff5c8fc8a2bd4296a38 2500w" />

The **Set state** block uses `@{result.0.id}` to access the `id` field of the first item in the result of the preceding block.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block-nested.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7127d3a3645fd151eb80f1f28cecd074" alt="" data-og-width="1922" width="1922" data-og-height="1104" height="1104" data-path="images/agent-builder/execution-environment-set-state-block-nested.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block-nested.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=47a6857dfac795ea95fb06106f27db29 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block-nested.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d02639eee8c72e5010e03fd1b1c56401 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block-nested.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=651ff630403185bdbc22df8b10aaff14 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block-nested.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=0c7bf492cbdcebab644f793d669b2320 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block-nested.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=42aa91054063af11f24f2868de9ffaae 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-set-state-block-nested.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9009efb060dd77984c72be2925019e26 2500w" />

### In custom Python code

You can access the execution environment variables in custom Python code directly as variables.

For example, this Python block in the blueprint accesses the output of the preceding block and prepends the string `Result: ` to it. It then sets state variable `message` with the final result.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-python-block.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e30328aac1475d3a866dda2c5035777e" alt="" data-og-width="2644" width="2644" data-og-height="1108" height="1108" data-path="images/agent-builder/execution-environment-python-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-python-block.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d40ed26bb41e1bf419cb0679935bd9e1 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-python-block.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=52210c02059d266a827eb2c06d0dfc81 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-python-block.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d5d7a5041f98a1510d9be3be99851dda 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-python-block.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d2529f22c879875d15fabf741e2813a2 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-python-block.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=236f564205d7891d4c6a802bd25f85b8 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/execution-environment-python-block.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=dd0c72fa27dd4a8cf00d86816167c91a 2500w" />

#### Environment variables

Your `WRITER_API_KEY` is also available when you run custom Python code. It's available as an environment variable (as opposed to an execution environment variable), so you can access it using `os.getenv('WRITER_API_KEY')`.

```python  theme={null}
import os

api_key = os.getenv('WRITER_API_KEY')
```

<feedback />

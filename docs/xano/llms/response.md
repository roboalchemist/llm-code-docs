# Source: https://docs.xano.com/building/logic/core-components/response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Response

> Anything that is returned when the logic is complete

The response is what the logic will return when it's executed. It can be a value, a message, a JSON object; almost anything you want. Responses can be returned from a variable, or manually defined in the response itself.

Not all primitives support responses; see below.

| Primitive       | Supports Response | Notes                                                                                                                   |
| --------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| API             | Yes               | Returns the JSON object defined in the response block                                                                   |
| AI Agent        | No                | Your agent will return messages to the user, but you don't directly define the response like other primitives           |
| Trigger         | Yes               | Returns the JSON object defined in the response block                                                                   |
| Background Task | No                | No responses are supported                                                                                              |
| Custom Function | Yes               | Returns the JSON object defined in the response block                                                                   |
| Middleware      | Yes               | Returns the JSON object defined in the response block                                                                   |
| AI Tool         | Yes               | Returns the JSON object defined in the response block                                                                   |
| MCP Server      | No                | Your tools will deliver messages back to the MCP client, but you don't directly define a response like other primitives |

## Adding a Response

Responses will usually come from a variable of some kind, but you can also manually define a static value, or use filters to create a combination of both.

When building visually, Xano will automatically add a response of the first variable in the stack. For example, if you start by adding a Query All Records function, Xano will make sure that the response is the output of that function.

Responses can be returned as `self`, meaning that it is not nested in another object.

```json lines icon="code" Example of a self response theme={null}
{
  "id": 1,
  "created_at": 1760368044972,
  "name": "Erin Porter",
  "email": "mei.payne@google.com"
}
```

You can also return each response as its own nested object.

```json lines icon="code" Example of a nested response theme={null}
{
  "user": {
    "id": 1,
    "created_at": 1760368044972,
    "name": "Erin Porter",
    "email": "mei.payne@google.com"
  }
}
```

<Tabs>
  <Tab title="Visually: Canvas View" icon="share-nodes">
    Find your response block and choose **Add a Response**.
    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/4xy0p5vdU3hAE_8U/images/response-20251013-135205.png?fit=max&auto=format&n=4xy0p5vdU3hAE_8U&q=85&s=090c4c42458039aad138aa0404d3520b" alt="response-20251013-135205" width="985" height="623" data-path="images/response-20251013-135205.png" /></Frame>

    Give your response a name, and choose whether you want to return it as `self` or nested under another value.
    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/4xy0p5vdU3hAE_8U/images/response-20251013-135552.png?fit=max&auto=format&n=4xy0p5vdU3hAE_8U&q=85&s=fe1271f41f8ed053bf5ac206e2891841" alt="response-20251013-135552" width="431" height="487" data-path="images/response-20251013-135552.png" /></Frame>
  </Tab>

  <Tab title="Visually: Function Stack" icon="stack">
    Find your response block and choose **Add a Response**.
    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/4xy0p5vdU3hAE_8U/images/response-20251013-135651.png?fit=max&auto=format&n=4xy0p5vdU3hAE_8U&q=85&s=e1e32429eb927ea4f0b6fae12f126f14" alt="response-20251013-135651" width="1321" height="1113" data-path="images/response-20251013-135651.png" /></Frame>

    Give your response a name, and choose whether you want to return it as `self` or nested under another value.
    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/4xy0p5vdU3hAE_8U/images/response-20251013-135552.png?fit=max&auto=format&n=4xy0p5vdU3hAE_8U&q=85&s=fe1271f41f8ed053bf5ac206e2891841" alt="response-20251013-135552" width="431" height="487" data-path="images/response-20251013-135552.png" /></Frame>
  </Tab>

  <Tab title="XanoScript" icon="code">
    The response block is placed towards the end of the primitive, after the logic and before any additional settings.

    ```javascript lines icon="code" Example of a response in XanoScript theme={null}
      response {
        value = {user: $model}
      }
    ```

    To return a self response, forgo the object and keep only the `value` assignment.

    ```javascript lines icon="code" Example of a self response in XanoScript theme={null}
      response {
        value = $model
      }
    ```
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).
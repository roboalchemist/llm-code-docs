# Source: https://www.traceloop.com/docs/api-reference/tracing/whitelist_user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Enable logging of prompts and responses

By default, all prompts and responses are logged.
If you want to disable this behavior by following [this guide](/openllmetry/privacy/traces),
you can selectively enable it for some of your users with this API.

## Request Body

<ParamField body="associationPropertyAllowList" type="Associated Property Object">
  The list of association properties (like `{userId: "123"}`) that will be allowed to be logged.
</ParamField>

Example:

```json  theme={null}
{
  "associationPropertyAllowList": [
    {
      "userId": "123"
    }
  ]
}
```

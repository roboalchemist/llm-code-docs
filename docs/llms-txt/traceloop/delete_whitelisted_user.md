# Source: https://www.traceloop.com/docs/api-reference/tracing/delete_whitelisted_user.md

# Disable logging of prompts and responses for specific users

By default, all prompts and responses are logged.
If you've disabled this behavior by following [this guide](/openllmetry/privacy/traces),
and then [selectively enabled it for some of your users](/api-reference/tracing/whitelist_user) then you
can use this API to disable it for previously enabled ones.

## Request Body

<ParamField body="associationProperty" type="Associated Property Object">
  A single association property (like `{userId: "123"}`) that was previously allowed to be logged.
</ParamField>

Example:

```json  theme={null}
{
  "associationProperty": {
    "userId": "123"
  }
}
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt
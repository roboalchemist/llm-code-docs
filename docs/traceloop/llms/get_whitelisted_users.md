# Source: https://www.traceloop.com/docs/api-reference/tracing/get_whitelisted_users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get identifiers of users that are allowed to be logged

By default, all prompts and responses are logged.
If you've disabled this behavior by following [this guide](/openllmetry/privacy/traces),
and then [selectively enabled it for some of your users](/api-reference/tracing/whitelist_user) then you
can use this API to view which users you've enabled.

## Response

<ResponseField name="associationPropertyAllowList" type="JSON">
  The list of users that are allowed to be logged. Listed using their
  association properties.
</ResponseField>

```json  theme={null}
{
  "associationPropertyAllowList": [
    {
      "userId": "123"
    },
    {
      "userId": "456",
      "chatId": "abc"
    }
  ]
}
```

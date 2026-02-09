# Source: https://docs.lunary.ai/docs/integrations/javascript/serverless.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Serverless

Usage with serverless functions.

When using lunary with Serverless/Lambda functions, you need to make sure that you flush the queue at the end of each function otherwise the data may not be side.

```js  theme={null}
import lunary from 'lunary'

async function handler(event, context) {
  // do something

  // your function logic...

  // flush the queue (make sure to await)

  await lunary.flush()

  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'Hello World' })
  }
}
```

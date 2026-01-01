# Source: https://docs.lunary.ai/docs/integrations/javascript/serverless.md

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


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt
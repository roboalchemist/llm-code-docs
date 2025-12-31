# Source: https://resend.com/docs/send-with-redwoodjs.md

# Send emails with RedwoodJS

> Learn how to send your first email using Redwood.js and the Resend Node.js SDK.

### Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

### 1. Install

Get the Resend Node.js SDK.

<CodeGroup>
  ```bash yarn theme={null}
  yarn workspace api add resend
  ```
</CodeGroup>

### 2. Send email using HTML

```bash  theme={null}
yarn rw g function send
```

The easiest way to send an email is by using the `html` parameter.

```ts api/src/functions/send/send.ts theme={null}
import { Resend } from 'resend';
import type { APIGatewayEvent, Context } from 'aws-lambda';

const resend = new Resend('re_xxxxxxxxx');

export const handler = async (event: APIGatewayEvent, context: Context) => {
  const { data, error } = await resend.emails.send({
    from: 'Acme <onboarding@resend.dev>',
    to: ['delivered@resend.dev'],
    subject: 'hello world',
    html: '<strong>it works!</strong>',
  });

  if (error) {
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error }),
    };
  }

  return {
    statusCode: 200,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ data }),
  };
};
```

### 3. Try it yourself

<Card title="Redwood.js Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-redwoodjs-example">
  See the full source code.
</Card>

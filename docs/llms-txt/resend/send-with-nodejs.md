# Source: https://resend.com/docs/send-with-nodejs.md

# Send emails with Node.js

> Learn how to send your first email using the Resend Node.js SDK.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

Get the Resend Node.js SDK.

<CodeGroup>
  ```bash npm theme={null}
  npm install resend
  ```

  ```bash yarn theme={null}
  yarn add resend
  ```

  ```bash pnpm theme={null}
  pnpm add resend
  ```
</CodeGroup>

## 2. Send email using HTML

The easiest way to send an email is by using the `html` parameter.

```js server.ts theme={null}
import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

(async function () {
  const { data, error } = await resend.emails.send({
    from: 'Acme <onboarding@resend.dev>',
    to: ['delivered@resend.dev'],
    subject: 'Hello World',
    html: '<strong>It works!</strong>',
  });

  if (error) {
    return console.error({ error });
  }

  console.log({ data });
})();
```

## 3. Try it yourself

<Card title="Node.js Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-node-example">
  See the full source code.
</Card>

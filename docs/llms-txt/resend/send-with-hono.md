# Source: https://resend.com/docs/send-with-hono.md

# Send emails with Hono

> Learn how to send your first email using Hono and the Resend Node.js SDK.

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

## 2. Create an email template

Start by creating your email template on `emails/email-template.tsx`.

```tsx emails/email-template.tsx theme={null}
import * as React from 'react';

interface EmailTemplateProps {
  firstName: string;
}

export function EmailTemplate({ firstName }: EmailTemplateProps) {
  return (
    <div>
      <h1>Welcome, {firstName}!</h1>
    </div>
  );
}
```

To use JSX/TSX with Hono, we need to modify the `tsconfig.json`.

```json tsconfig.json theme={null}
{
  "compilerOptions": {
    "jsx": "react-jsx",
    "jsxImportSource": "react"
  }
}
```

## 3. Send email using React

Create a new file `index.tsx` and send your first email.

```ts index.tsx theme={null}
import { Hono } from 'hono';
import { Resend } from 'resend';
import { EmailTemplate } from './emails/email-template';

const app = new Hono();
const resend = new Resend('re_xxxxxxxxx');

app.get('/', async (c) => {
  const { data, error } = await resend.emails.send({
    from: 'Acme <onboarding@resend.dev>',
    to: ['delivered@resend.dev'],
    subject: 'hello world',
    react: <EmailTemplate firstName="John" />,
  });

  if (error) {
    return c.json(error, 400);
  }

  return c.json(data);
});

export default app;
```

## 4. Try it yourself

<Card title="Hono Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-hono-example">
  See the full source code.
</Card>

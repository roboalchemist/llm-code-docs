# Source: https://resend.com/docs/send-with-bun.md

# Send emails with Bun

> Learn how to send your first email using Bun and the Resend Node.js SDK.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

Get the Resend Node.js SDK.

```bash  theme={null}
bun install resend
```

## 2. Create an email template

Start by creating your email template on `email-template.tsx`.

```tsx email-template.tsx theme={null}
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

## 3. Send email using React

Create a new file `index.tsx` and send your first email.

```tsx index.tsx theme={null}
import { Resend } from 'resend';
import { EmailTemplate } from './email-template';

const resend = new Resend(process.env.RESEND_API_KEY);

const server = Bun.serve({
  port: 3000,
  async fetch() {
    const { data, error } = await resend.emails.send({
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: 'Hello World',
      react: EmailTemplate({ firstName: 'Vitor' }),
    });

    if (error) {
      return new Response(JSON.stringify({ error }));
    }

    return new Response(JSON.stringify({ data }));
  },
});

console.log(`Listening on http://localhost:${server.port} ...`);
```

Start the local server by running `bun index.tsx` and navigate to `http://localhost:3000`.

## 3. Try it yourself

<Card title="Bun Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-bun-example">
  See the full source code.
</Card>

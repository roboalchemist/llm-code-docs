# Source: https://resend.com/docs/send-with-bun.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Bun

> Learn how to send your first email using Bun and the Resend Node.js SDK.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

Get the Resend Node.js SDK.

```bash  theme={"theme":{"light":"github-light","dark":"vesper"}}
bun install resend
```

## 2. Create an email template

Start by creating your email template on `email-template.tsx`.

```tsx email-template.tsx theme={"theme":{"light":"github-light","dark":"vesper"}}
import * as React from 'react';

interface EmailTemplateProps {
  firstName: string;
}

export const EmailTemplate = ({ firstName }: EmailTemplateProps) => (
  <div>
    <h1>Welcome, {firstName}!</h1>
  </div>
);
```

## 3. Send email using React

Create a new file `index.tsx` and send your first email.

```tsx index.tsx theme={"theme":{"light":"github-light","dark":"vesper"}}
import { Resend } from 'resend';
import { EmailTemplate } from './email-template';

const resend = new Resend(process.env.RESEND_API_KEY);

const server = Bun.serve({
  port: 3000,
  async fetch() {
    const data = await resend.emails.send({
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: 'Hello World',
      react: EmailTemplate({ firstName: 'Vitor' }),
    });

    return new Response(JSON.stringify(data));
  },
});

console.log(`Listening on http://localhost:${server.port} ...`);
```

Start the local server by running `bun index.tsx` and navigate to `http://localhost:3000`.

## 3. Try it yourself

<Card title="Bun Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-bun-example">
  See the full source code.
</Card>

# Source: https://resend.com/docs/send-with-cloudflare-workers.md

# Send emails with Cloudflare Workers

> Learn how to send your first email using Cloudflare Workers.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)
* Have a Cloudflare worker with a bundling setup
  * Recommended to be bootstrapped with `npm create cloudflare`

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

Start by creating your email template on `src/emails/email-template.tsx`:

```tsx src/emails/email-template.tsx theme={null}
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

export default EmailTemplate;
```

## 3. Send the email using React and the SDK

Change the file extension of the worker's main file to `tsx` and modify your configurations.

After that, you can send your email using the `react` parameter:

```tsx src/index.tsx theme={null}
import { Resend } from 'resend';
import { EmailTemplate } from './emails/email-template';

export default {
  async fetch(request, env, context): Promise<Response> {
    const resend = new Resend('re_xxxxxxxxx');

    const data = await resend.emails.send({
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: 'hello world',
      react: <EmailTemplate firstName="John" />,
    });

    return Response.json(data);
  },
} satisfies ExportedHandler<Env, ExecutionContext>;
```

## 4. Deploy and send email

Run `wrangler deploy` and wait for it to finish. Once it's done, it will
give you a URL to try out, like `https://my-worker.your_name.workers.dev`,
that you can open and verify that your email has been sent.

## 5. Try it yourself

<Card title="Cloudflare Workers Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-cloudflare-workers-example">
  See the full source code.
</Card>

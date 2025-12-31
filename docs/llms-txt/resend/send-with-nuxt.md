# Source: https://resend.com/docs/send-with-nuxt.md

# Send emails with Nuxt

> Learn how to send your first email using Nuxt and the Resend Node.js SDK.

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

Create a [Server Route](https://nuxt.com/docs/guide/directory-structure/server) under `server/api/send.ts`.

The easiest way to send an email is by using the `html` parameter.

<CodeGroup>
  ```ts server/api/send.ts theme={null}
  import { Resend } from 'resend';

  const resend = new Resend(process.env.RESEND_API_KEY);

  export default defineEventHandler(async () => {
    try {
      const data = await resend.emails.send({
        from: 'Acme <onboarding@resend.dev>',
        to: ['delivered@resend.dev'],
        subject: 'Hello world',
        html: '<strong>It works!</strong>',
      });

      return data;
    } catch (error) {
      return { error };
    }
  });
  ```
</CodeGroup>

## 3. Try it yourself

<Card title="Nuxt Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-nuxt-example">
  See the full source code.
</Card>

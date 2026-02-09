# Source: https://resend.com/docs/send-with-nuxt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Nuxt

> Learn how to send your first email using Nuxt and the Resend Node.js SDK.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

Get the Resend Node.js SDK.

<CodeGroup>
  ```bash npm theme={"theme":{"light":"github-light","dark":"vesper"}}
  npm install resend
  ```

  ```bash yarn theme={"theme":{"light":"github-light","dark":"vesper"}}
  yarn add resend
  ```

  ```bash pnpm theme={"theme":{"light":"github-light","dark":"vesper"}}
  pnpm add resend
  ```

  ```bash bun theme={"theme":{"light":"github-light","dark":"vesper"}}
  bun add resend
  ```
</CodeGroup>

## 2. Send email using HTML

Create a [Server Route](https://nuxt.com/docs/guide/directory-structure/server) under `server/api/send.ts`.

The easiest way to send an email is by using the `html` parameter.

<CodeGroup>
  ```ts server/api/send.ts theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend(process.env.RESEND_API_KEY);

  export default defineEventHandler(async () => {
    const response = await resend.emails.send({
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: 'Hello world',
      html: '<strong>It works!</strong>',
    });

    if (response.error) {
      throw createError({
        statusCode: 500,
        message: 'Error sending email',
      });
    }

    return response;
  });
  ```
</CodeGroup>

## 3. Try it yourself

<Card title="Nuxt Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-nuxt-example">
  See the full source code.
</Card>

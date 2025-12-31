# Source: https://resend.com/docs/send-with-sveltekit.md

# Send emails with SvelteKit

> Learn how to send your first email using SvelteKit and the Resend Node.js SDK.

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

Create a [+server API route](https://svelte.dev/docs/kit/routing#server) under `src/routes/send/+server.ts`.

The easiest way to send an email is by using the `html` parameter.

<CodeGroup>
  ```ts src/routes/send/+server.ts theme={null}
  import { Resend } from 'resend';
  import { RESEND_API_KEY } from '$env/static/private'; // define in your .env file

  const resend = new Resend(RESEND_API_KEY);

  export async function POST() {
    try {
      const { data, error } = await resend.emails.send({
        from: 'Acme <onboarding@resend.dev>',
        to: ['delivered@resend.dev'],
        subject: 'Hello world',
        html: '<p>Hello world</p>',
      });

      if (error) {
        return Response.json({ error }, { status: 500 });
      }

      return Response.json({ data });
    } catch (error) {
      return Response.json({ error }, { status: 500 });
    }
  }
  ```
</CodeGroup>

## 3. Try it yourself

<CardGroup>
  <Card title="SvelteKit Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-svelte-kit-example">
    See the full source code.
  </Card>
</CardGroup>

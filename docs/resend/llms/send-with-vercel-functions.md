# Source: https://resend.com/docs/send-with-vercel-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Vercel Functions

> Learn how to send your first email using Vercel Functions.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

Make sure you have the latest version of the [Vercel CLI](https://vercel.com/docs/cli#installing-vercel-cli) installed.

## 1. Install dependencies

Install the Resend SDK:

```bash  theme={"theme":{"light":"github-light","dark":"vesper"}}
npm install resend
```

## 2. Set up environment variables

Add your Resend API key to your environment variables:

```bash .env.local theme={"theme":{"light":"github-light","dark":"vesper"}}
RESEND_API_KEY=re_xxxxxxxxx
```

## 3. Create a Next.js function

Create a route file under `app/api/send/route.ts` if you're using the [App Router](https://nextjs.org/docs/app/building-your-application/routing/router-handlers).

```ts route.ts theme={"theme":{"light":"github-light","dark":"vesper"}}
import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

export async function POST() {
  const response = await resend.emails.send({
    from: 'Acme <onboarding@resend.dev>',
    to: ['delivered@resend.dev'],
    subject: 'hello world',
    html: '<strong>it works!</strong>',
  });

  return Response.json(response, {
    status: response.error ? 500 : 200,
  });
}
```

## 4. Send email locally

Run function locally:

```bash  theme={"theme":{"light":"github-light","dark":"vesper"}}
npm run dev
```

Open the endpoint URL to send an email: `http://localhost:3000/api/send`

## 5. Send email in production

Deploy function to Vercel:

```bash  theme={"theme":{"light":"github-light","dark":"vesper"}}
vercel
```

Make sure to add your `RESEND_API_KEY` environment variable in your Vercel project settings.

Open the endpoint URL to send an email: `https://your-project.vercel.app/api/send`

## 6. Try it yourself

<Card title="Vercel Functions Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-vercel-functions-example">
  See the full source code.
</Card>

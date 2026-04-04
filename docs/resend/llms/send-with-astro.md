# Source: https://resend.com/docs/send-with-astro.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Astro

> Learn how to send your first email using Astro, Resend, and Node.js.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

If you prefer to watch a video, check out our video walkthrough below.

<YouTube id="OzDg4QPmmac" />

## 1. Install

Install Resend for Node.js.

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

## 2. Install an SSR adapter

Because Astro builds a static site by default, [install an SSR adapter](https://docs.astro.build/en/guides/server-side-rendering/) to enable on-demand rendering of routes.

## 3. Add your API key

[Create an API key](https://resend.com/api-keys) in Resend and add it to your `.env` file to keep your API key secret.

```ini .env theme={"theme":{"light":"github-light","dark":"vesper"}}
RESEND_API_KEY="re_xxxxxxxxx"
```

## 4. Send email using HTML

Create an [Astro Action](https://docs.astro.build/en/guides/actions/) under `actions/index.ts`.

The easiest way to send an email is with the `html` parameter.

<CodeGroup>
  ```ts src/actions/index.ts theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { ActionError, defineAction } from 'astro:actions';
  import { Resend } from 'resend';

  const resend = new Resend(import.meta.env.RESEND_API_KEY);

  export const server = {
    send: defineAction({
      accept: 'form',
      handler: async () => {
        const { data, error } = await resend.emails.send({
          from: 'Acme <onboarding@resend.dev>',
          to: ['delivered@resend.dev'],
          subject: 'Hello world',
          html: '<strong>It works!</strong>',
        });

        if (error) {
          throw new ActionError({
            code: 'BAD_REQUEST',
            message: error.message,
          });
        }

        return data;
      },
    }),
  };
  ```
</CodeGroup>

Call the `send` action from any frontmatter route, script, or component.

## 5. Try it yourself

<Card title="Astro Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-astro-example">
  See the full source code.
</Card>

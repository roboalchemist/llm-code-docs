# Source: https://resend.com/docs/send-with-express.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Express

> Learn how to send your first email using Express and the Resend Node.js SDK.

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

The easiest way to send an email is by using the `html` parameter.

```js server.ts theme={"theme":{"light":"github-light","dark":"vesper"}}
import express, { Request, Response } from "express";
import { Resend } from "resend";

const app = express();
const resend = new Resend("re_xxxxxxxxx");

app.get("/", async (req: Request, res: Response) => {
  const { data, error } = await resend.emails.send({
    from: "Acme <onboarding@resend.dev>",
    to: ["delivered@resend.dev"],
    subject: "hello world",
    html: "<strong>it works!</strong>",
  });

  if (error) {
    return res.status(400).json({ error });
  }

  res.status(200).json({ data });
});

app.listen(3000, () => {
  console.log("Listening on http://localhost:3000");
});
```

## 3. Try it yourself

<Card title="Express Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-express-example">
  See the full source code.
</Card>

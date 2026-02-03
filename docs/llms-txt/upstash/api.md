# Source: https://upstash.com/docs/workflow/basics/context/api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# context.api

In addition to `context.call`, you can also make third‑party requests using the `context.api` namespace.

This namespace provides built‑in integrations for **OpenAI**, **Anthropic**, and **Resend**, allowing you to make requests in a **type‑safe** manner.

<CodeGroup>
  ```typescript OpenAI theme={"system"}
  const { status, body } = await context.api.openai.call("Call OpenAI", {
    token: "<OPENAI_API_KEY>",
    operation: "chat.completions.create",
    body: {
      model: "gpt-4o",
      messages: [
        {
          role: "system",
          content: "Assistant says 'hello!'",
        },
        { role: "user", content: "User shouts back 'hi!'" },
      ],
    },
  });
  ```

  ```typescript Anthropic theme={"system"}
  const { status, body } = await context.api.anthropic.call(
    "Call Anthropic",
    {
      token: "<ANTHROPIC_API_KEY>",
      operation: "messages.create",
      body: {
        model: "claude-3-5-sonnet-20241022",
        max_tokens: 1024,
        messages: [
            {"role": "user", "content": "Hello, world"}
        ]
      },
    }
  );
  ```

  ```typescript Resend theme={"system"}
  const { status, body } = await context.api.resend.call("Call Resend", {
    token: "<RESEND_API_KEY>",
    body: {
      from: "Acme <onboarding@resend.dev>",
      to: ["delivered@resend.dev"],
      subject: "Hello World",
      html: "<p>It works!</p>",
    },
    headers: {
      "content-type": "application/json",
    },
  });
  ```
</CodeGroup>

We'll continue adding more integrations over time. If you'd like to see a specific integration, feel free to contribute to the SDK or contact us with your suggestion.

For detailed guides on usage and configuration, see the [Integrations section](/workflow/integrations/openai).

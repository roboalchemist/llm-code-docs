# Source: https://resend.com/docs/send-with-elixir.md

# Send emails with Elixir

> Learn how to send your first email using the Resend Elixir SDK.

<Info>
  This guides utilizes an [open source
  library](https://github.com/elixir-saas/resend-elixir) contributed by a
  community member. It's not developed, maintained, or supported by Resend
  directly.
</Info>

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

Install by adding `resend` to your list of dependencies in `mix.exs`:

<CodeGroup>
  ```elixir mix.exs theme={null}
  def deps do
    [
      {:resend, "~> 0.4.0"}
    ]
  end
  ```
</CodeGroup>

## 2. Send email using HTML

The easiest way to send an email is by using the `html` parameter.

```elixir send.exs theme={null}
client = Resend.client(api_key: System.get_env("RESEND_API_KEY"))

Resend.Emails.send(client, %{
  from: "Acme <onboarding@resend.dev>",
  to: ["delivered@resend.dev"],
  subject: "hello world",
  html: "<strong>it works!</strong>"
})
```

## 3. Try it yourself

<Card title="Elixir Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-elixir-example">
  See the full source code.
</Card>

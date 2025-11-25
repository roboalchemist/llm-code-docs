# Source: https://resend.com/docs/send-with-phoenix.md

# Send emails with Phoenix

> Learn how to send your first email using Phoenix and the Resend Elixir SDK.

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

## 2. Send email using Swoosh

This library includes a Swoosh adapter to make using Resend with a new Phoenix project as easy as possible. All you have to do is configure your Mailer:

```elixir  theme={null}
config :my_app, MyApp.Mailer,
  adapter: Resend.Swoosh.Adapter,
  api_key: System.fetch_env!("RESEND_API_KEY")
```

If you're configuring your app for production, configure your adapter in `prod.exs`, and your API key from the environment in `runtime.exs`:

<CodeGroup>
  ```elixir prod.exs theme={null}
  config :my_app, MyApp.Mailer, adapter: Resend.Swoosh.Adapter
  ```

  ```elixir runtime.exs theme={null}
  config :my_app, MyApp.Mailer, api_key: "re_xxxxxxxxx"
  ```
</CodeGroup>

## 3. Try it yourself

<Card title="Phoenix Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-phoenix-example">
  See the full source code.
</Card>

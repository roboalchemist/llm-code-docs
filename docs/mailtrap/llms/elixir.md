# Source: https://docs.mailtrap.io/guides/sdk/elixir.md

# Elixir

<a href="https://github.com/mailtrap/mailtrap-elixir" class="button primary">Mailtrap Elixir SDK on GitHub</a>

## Overview

Mailtrap can be integrated with Elixir apps and projects for email sending.

## Email API/SMTP for Elixir

### SDK integration

The [Mailtrap Elixir SDK](https://github.com/mailtrap/mailtrap-elixir) brings functional programming elegance to email sending with full support for Elixir's concurrent and fault-tolerant features. The SDK supports:

* Transactional email sending
* Sandbox testing
* Account management
* OTP-compliant design
* Pattern matching for responses
* Pipe-friendly API

{% hint style="info" %}
Check the repo for Bamboo adaptor examples.
{% endhint %}

### Installation

Add the SDK to your `mix.exs` dependencies:

{% code title="mix.exs" %}

```elixir
def deps do
  [
    {:mailtrap, "~> 1.0"}
  ]
end
```

{% endcode %}

Then run:

{% code title="Terminal" %}

```bash
mix deps.get
```

{% endcode %}

### Minimal Example

Here's a minimal example to send your first email:

{% code title="send\_email.exs" %}

```elixir
client = Mailtrap.Sending.client("PASTE TOKEN HERE")
email = (%Mailtrap.Email{}
  |> Mailtrap.Email.put_from({"From name", "from@example.com"})
  |> Mailtrap.Email.put_to({"Recepient", "recepient@example.com"})
  |> Mailtrap.Email.put_subject("Hi there")
  |> Mailtrap.Email.put_text("General Kenobi"))
Mailtrap.Sending.send(client, email)
```

{% endcode %}

{% hint style="info" %}
Get your API token from your Mailtrap account under **Settings → API Tokens**.
{% endhint %}

### SMTP integration

To integrate SMTP with your Elixir app, navigate to the Integrations tab and copy-paste the credentials.

{% hint style="info" %}
SMTP integration is compatible with any Elixir framework or library that sends emails via SMTP.
{% endhint %}

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-94c0ecea77d970fd6fc53b31a09b6e75d5d93bf6%2Fmailtrap-elixir-integration-smtp-credentials.png?alt=media" alt="" width="563"></div>

Read more about SMTP integration [here](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/smtp-integration).

### RESTful API integration

To integrate Mailtrap using RESTful API, simply copy/paste the API endpoint and API Token into the configuration file of the Elixir framework or library that supports HTTP requests. For more details, refer to the [API documentation](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/5tjdeg9545058-mailtrap-api).

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-5983dc9b0a4866158ef212833d340402b11a8999%2Fmailtrap-elixir-integration-api-credentials.png?alt=media" alt="" width="563"></div>

Read more about API integration in the [here](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/api-integration).

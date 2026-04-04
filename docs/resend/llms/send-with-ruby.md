# Source: https://resend.com/docs/send-with-ruby.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Ruby

> Learn how to send your first email using the Resend Ruby SDK.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

Get the Resend Ruby SDK.

<CodeGroup>
  ```bash RubyGems theme={"theme":{"light":"github-light","dark":"vesper"}}
  gem install resend
  ```

  ```bash Gemfile theme={"theme":{"light":"github-light","dark":"vesper"}}
  gem 'resend'
  ```
</CodeGroup>

## 2. Send email using HTML

The easiest way to send an email is by using the `html` parameter.

```rb index.rb theme={"theme":{"light":"github-light","dark":"vesper"}}
require "resend"

Resend.api_key = "re_xxxxxxxxx"

params = {
  "from": "Acme <onboarding@resend.dev>",
  "to": ["delivered@resend.dev"],
  "subject": "hello world",
  "html": "<strong>it works!</strong>"
}

sent = Resend::Emails.send(params)
puts sent
```

## 3. Try it yourself

<Card title="Ruby Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-ruby-example">
  See the full source code.
</Card>

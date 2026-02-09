# Source: https://resend.com/docs/send-with-sinatra.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Sinatra

> Learn how to send your first email using Sinatra and the Resend Ruby SDK.

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
require "sinatra"
require "resend"

set :port, 5000
set :bind, "0.0.0.0"

Resend.api_key = ENV["RESEND_API_KEY"]

get "/" do

  content_type :json

  params = {
    from: 'Acme <onboarding@resend.dev>',
    to: ['delivered@resend.dev'],
    subject: 'hello world',
    html: '<strong>it works!</strong>',
  }

  Resend::Emails.send(params).to_hash.to_json
end
```

## 3. Try it yourself

<Card title="Sinatra Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-sinatra-example">
  See the full source code.
</Card>

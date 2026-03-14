# Source: https://docs.mailtrap.io/guides/sdk/ruby.md

# Ruby

<a href="https://github.com/mailtrap/mailtrap-ruby" class="button primary">Mailtrap Ruby SDK on GitHub</a>

### Overview

Mailtrap can be integrated with Ruby apps and projects for email sending.

### Email API/SMTP for Ruby

#### SDK integration

> The Mailtrap Ruby SDK has been significantly expanded. It now covers the full Mailtrap feature set — from batch sending and sandbox testing to contact management, templates, and more.

The [Mailtrap Ruby SDK](https://github.com/mailtrap/mailtrap-ruby) provides an idiomatic Ruby interface for sending transactional and bulk emails. The SDK supports:

* Transactional email sending
* Batch email sending
* Template management
* [ActionMailer](https://github.com/mailtrap/mailtrap-ruby/blob/main/examples/action_mailer.rb) integration for Rails applications
* Comprehensive error handling
* Sandbox email sending and messages CRUD
* Contacts management
* Inboxes and Projects management
* Account management

### Installation

Add the SDK to your Gemfile:

{% code title="Gemfile" %}

```ruby
gem 'mailtrap'
```

{% endcode %}

Then run:

{% code title="Terminal" %}

```bash
bundle install
```

{% endcode %}

### Minimal Example Ruby on Rails (Actionmailer)

{% code title="config/environments/production.rb" %}

```ruby
# place this code in config/environments/production.rb:
config.action_mailer.delivery_method = :mailtrap

# then set the MAILTRAP_API_KEY environment variable
# using your hosting solution.
```

{% endcode %}

### Minimal Example Ruby

Here's a minimal example to send your first email:

{% code title="send\_email.rb" %}

```ruby
require 'mailtrap'

client = Mailtrap::Client.new(api_key: 'your-api-token')

mail = Mailtrap::Mail::FromTemplate.new(
  from: { email: 'hello@example.com', name: 'Mailtrap Test' },
  to: [{ email: 'recipient@example.com' }],
  template_uuid: 'template-uuid',
  template_variables: {
    'user_name' => 'John Doe'
  }
)

# Or send a simple email
mail = {
  from: { email: 'hello@example.com', name: 'Mailtrap Test' },
  to: [{ email: 'recipient@example.com' }],
  subject: 'Hello from Mailtrap!',
  text: 'Welcome to Mailtrap Email Sending!',
  html: '<p>Welcome to <strong>Mailtrap</strong> Email Sending!</p>'
}

response = client.send(mail)
puts response
```

{% endcode %}

{% hint style="info" %}
Get your API token from your Mailtrap account under **Settings → API Tokens**.
{% endhint %}

#### SMTP integration

To integrate SMTP with your Ruby app, navigate to the **Integrations** tab, choose either Ruby on Rails or Ruby Net/SMTP, and copy-paste the credentials or ready-made code snippets.

{% hint style="info" %}
SMTP integration is compatible with any Ruby framework or library that sends emails via SMTP.
{% endhint %}

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-ed5503382dbd3f653071b9c201d0c46bfc995edd%2Fmailtrap-ruby-smtp-integration.png?alt=media" alt=""></div>

Read more about SMTP integration in the [Email API/SMTP - SMTP Integration](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/smtp-integration) article.

#### RESTful API integration

To integrate Mailtrap using RESTful API, use the configuration available among **Code samples** under the API section.

API integration can be used with any Ruby framework or library that supports HTTP requests. For more details, refer to the [API documentation](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/5tjdeg9545058-mailtrap-api).

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-acd4781ccf6ec684b874579011626232a81837f6%2Fmailtrap-ruby-api-integration.png?alt=media" alt=""></div>

Read more about API integration in the [Email API/SMTP - API Integration](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/api-integration) article.

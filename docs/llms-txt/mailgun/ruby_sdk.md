# Source: https://documentation.mailgun.com/docs/mailgun/sdk/ruby_sdk.md

# Ruby

a
img

    Official Mailgun Ruby Gem On Github

This is the Mailgun Ruby Library. This library contains methods for easily interacting
with the Mailgun API.
Below are examples to get you started. For additional examples, please see our repository on GitHub.

Happy Coding!

Installation

Via RubyGems


```ruby
gem install mailgun-ruby
```

Gemfile:


```ruby
gem 'mailgun-ruby', '~>1.2.14'
```

Usage

Here's a simple example on how to send an email. As always, please consult the repository readme for full details.


```ruby
require 'mailgun-ruby'

# First, instantiate the Mailgun Client with your API key
mg_client = Mailgun::Client.new 'MAILGUN_API_KEY'

# Define your message parameters
message_params =  { from: 'bob@sending_domain.com',
                    to:   'sally@example.com',
                    subject: 'The Ruby SDK is awesome!',
                    text:    'It is really easy to send a message!'
                  }

# Send your message through the client
mg_client.send_message 'sending_domain.com', message_params
```
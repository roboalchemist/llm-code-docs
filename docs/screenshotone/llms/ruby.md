# Source: https://screenshotone.com/docs/code-examples/ruby/

# Ruby SDK and Code Examples

import Alert from "@/components/Alert.astro";

<Alert>
    If you have any questions, please, reach out at `support@screenshotone.com`.
</Alert>

<Alert>
    Massive thanks and rays of goodness to [Gustavo
    Garcia](https://twitter.com/theluctus) from
    [Dailytics](https://dailytics.com/) for providing the fully-featured
    high-quality Ruby SDK.
</Alert>

### Installation

Update your Gemfile:

```
gem 'screenshotone'
```

Then execute:

```shell
bundle install
```

### Usage

Don't forget to [sign up](https://dash.screenshotone.com/sign-up) to get access and secret keys.

Generate a screenshot URL without executing the request. Or download the screenshot. It is up to you:

```ruby
# If you don't need to add a signature
client = ScreenshotOne::Client.new('my_access_key')

# If you do need to add a signature
client = ScreenshotOne::Client.new('my_access_key', 'my_secret_key')

# You can set any available option, in a camel_case format, for example:
options = ScreenshotOne::TakeOptions.new(url: 'https://example.com').
            full_page(true).
            delay(2).
            geolocation_latitude(48.857648).
            geolocation_longitude(2.294677).
            geolocation_accuracy(50)

# Verify all the parameters are valid (we will validate the parameters that should be
# numeric, booleans or that accept only certain values)
options.valid?
=> true

# To simply get the final url:
client.generate_take_url(options)
=> "https://api.screenshotone.com/take?url=https%3A%2F%2Fexample.com..."

# To actually get the image (the response body of a request to the previous url)
client.take(options)
=> "\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF\..."
```


Check out [other SDKs and code examples](/docs/code-examples/).
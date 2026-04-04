# Source: https://configcat.com/docs/sdk-reference/ruby.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/ruby.md

# OpenFeature Provider for Ruby

Copy page

[![Build Status](https://github.com/configcat/openfeature-ruby/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/configcat/openfeature-ruby/actions/workflows/ci.yml) [![Gem Version](https://badge.fury.io/rb/configcat-openfeature-provider.svg?icon=si%3Arubygems)](https://badge.fury.io/rb/configcat-openfeature-provider)

[ConfigCat OpenFeature Provider for Ruby on GitHub](https://github.com/configcat/openfeature-ruby)

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install the provider[​](#1-install-the-provider "Direct link to 1. Install the provider")

```bash
gem install configcat-openfeature-provider

```

### 2. Initialize the provider[​](#2-initialize-the-provider "Direct link to 2. Initialize the provider")

The initializer of `ConfigCat::OpenFeature::Provider` takes the SDK key and an optional `ConfigCat::ConfigCatOptions` argument containing the additional configuration options for the [ConfigCat Ruby SDK](https://configcat.com/docs/sdk-reference/ruby.md#creating-the-configcat-client):

```ruby
require "configcat-openfeature-provider"

# Configure the OpenFeature API with the ConfigCat provider.
OpenFeature::SDK.configure do |config|
  config.set_provider(ConfigCat::OpenFeature::Provider.new(
    sdk_key: "<YOUR-CONFIGCAT-SDK-KEY>",
    # Build options for the ConfigCat SDK.
    options: ConfigCat::ConfigCatOptions.new(
      polling_mode: ConfigCat::PollingMode.auto_poll
    )))
end

# Create a client.
client = OpenFeature::SDK.build_client

```

For more information about all the configuration options, see the [Ruby SDK documentation](https://configcat.com/docs/sdk-reference/ruby.md#creating-the-configcat-client).

### 3. Evaluate your feature flag[​](#3-evaluate-your-feature-flag "Direct link to 3. Evaluate your feature flag")

```ruby
is_awesome_feature_enabled = client.fetch_boolean_value(
  flag_key: "isAwesomeFeatureEnabled",
  default_value: false
)
if is_awesome_feature_enabled
    do_the_new_thing
else
    do_the_old_thing
end

```

## Evaluation Context[​](#evaluation-context "Direct link to Evaluation Context")

An [evaluation context](https://openfeature.dev/docs/reference/concepts/evaluation-context) in the OpenFeature specification is a container for arbitrary contextual data that can be used as a basis for feature flag evaluation. The ConfigCat provider translates these evaluation contexts to ConfigCat [User Objects](https://configcat.com/docs/sdk-reference/ruby.md#user-object).

The following table shows how the different context attributes are mapped to User Object attributes.

| Evaluation context | User Object  | Required |
| ------------------ | ------------ | -------- |
| `targeting_key`    | `identifier` | ☑        |
| `Email`            | `email`      |          |
| `Country`          | `country`    |          |
| Any other          | `custom`     |          |

To evaluate feature flags for a context, use the [OpenFeature Evaluation API](https://openfeature.dev/docs/reference/concepts/evaluation-api/):

```ruby
context = OpenFeature::SDK::EvaluationContext.new(
    OpenFeature::SDK::EvaluationContext::TARGETING_KEY => "#SOME-USER-ID#",
    "Email" => "configcat@example.com",
    "Country" => "CountryID",
    "Rating" => 4.5,
    "RegisteredAt" => DateTime.iso8601("2023-11-22T12:34:56+00:00"),
    "Roles" => [ "Role1", "Role2" ]
)

is_awesome_feature_enabled = client.fetch_boolean_value(
  flag_key: "isAwesomeFeatureEnabled",
  default_value: false,
  evaluation_context: context
)

```

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [Sample Ruby APP](https://github.com/configcat/openfeature-ruby/tree/main/samples/provider-sample)
* [ConfigCat OpenFeature Provider's repository on GitHub](https://github.com/configcat/openfeature-ruby)
* [ConfigCat OpenFeature Provider in RubyGems](https://rubygems.org/gems/configcat-openfeature-provider)

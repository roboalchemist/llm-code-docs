---
---
title: Set Up Profiling
description: "Learn how to enable profiling in your app if it is not already set up."
---

## Enable Profiling using StackProf

StackProf profiling beta is available starting in SDK version `5.9.0`.

We use the [`stackprof` gem](https://github.com/tmm1/stackprof) to collect profiles for Ruby.

First add `stackprof` to your `Gemfile` and make sure it is loaded before `sentry-ruby`.

```ruby
# Gemfile

gem 'stackprof'
gem 'sentry-ruby'
```

Then, make sure both `traces_sample_rate` and `profiles_sample_rate` are set and non-zero in your Sentry initializer.

```ruby
# config/initializers/sentry.rb

Sentry.init do |config|
  config.dsn = "___PUBLIC_DSN___"
  config.traces_sample_rate = 1.0
  config.profiles_sample_rate = 1.0
end
```

The  setting is _relative_ to the  setting.

For Profiling to work, you have to first enable Sentry’s tracing via `traces_sample_rate` (like in the example above). Read our tracing setup documentation to learn how to configure sampling. If you set your sample rate to 1.0, all transactions will be captured.

## Enable Profiling using Vernier

Vernier profiling beta is available starting in SDK version `5.21.0`.

Vernier requires Ruby 3.2.1+

You can have much better profiles if you're using multi-threaded servers like Puma now by leveraging Vernier.

First, add `vernier` to your `Gemfile` and make sure it is loaded before `sentry-ruby`.

```ruby
# Gemfile

gem 'vernier'
gem 'sentry-ruby'
```

Then, set a `profiles_sample_rate` and the new `profiler_class` configuration in your sentry initializer to use the new profiler.

```ruby
# config/initializers/sentry.rb

Sentry.init do |config|
  config.dsn = "___PUBLIC_DSN___"
  config.profiles_sample_rate = 1.0
  config.traces_sample_rate = 1.0
  config.profiler_class = Sentry::Vernier::Profiler
end
```

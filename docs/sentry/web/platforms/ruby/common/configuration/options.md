---
---
title: Options
description: "Learn more about how the SDK can be configured via options. These are being passed to the init function and therefore set when the SDK is first initialized."
---

## Available Options

## Core Options

Options that can be read from an environment variable (`SENTRY_DSN`, `SENTRY_ENVIRONMENT`, `SENTRY_RELEASE`) will be read automatically.

The DSN tells the SDK where to send events. If this value isn't provided, the SDK will try to read it from the `SENTRY_DSN` environment variable. If that variable doesn't exist, the SDK won't send any events.

Learn more about [DSN utilization](/product/sentry-basics/dsn-explainer/#dsn-utilization).

This turns debug mode on or off. When enabled, SDK errors will be logged with backtrace.
If you want more output, use `config.sdk_logger.level`. `debug` only works for attaching backtraces to the messages.

The logger used by Sentry. The default for Rails is `Rails.logger`, otherwise it's `Sentry::Logger`. Make sure to change the logger level if you need debug output. **We don't recommend doing this in production unless absolutely necessary.**

```ruby
config.sdk_logger = Sentry::Logger.new(STDOUT)
config.sdk_logger.level = ::Logger::DEBUG # defaults to INFO
```

Lets you track your application version in Sentry.

We intelligently guess the release in the following order of preference:

- The `SENTRY_RELEASE` environment variable
- Commit SHA of the last commit (git)
- Reading from the `REVISION` file in the app root (used by Capistrano)
- Heroku’s dyno metadata via the `HEROKU_SLUG_COMMIT` environment variable (must have been enabled via Heroku Labs)

Configures the sample rate for error events, in the range of `0.0` to `1.0`. The default is `1.0`, which means that 100% of error events will be sent. If set to `0.1`, only 10% of error events will be sent.

```ruby
# send 50% of events
config.sample_rate = 0.5
```

This lets you attach diagnostic client reports about dropped events to an existing envelope max once every 30s. If you don't want to send this data, opt-out by setting:

```ruby
config.send_client_reports = false
```

If this flag is enabled, [certain personally identifiable information (PII)](/platforms/ruby/data-management/data-collected/) is added to Sentry events.

If you enable this option, be sure to manually remove what you don't want to send using our features for managing [_Sensitive Data_](../../data-management/sensitive-data/).

A boolean to decide whether to send module (dependency) information to Sentry.

```ruby
# if you don't want to send all the dependency info
config.send_modules = false
```

Whether to capture local variables from the raised exceptions frame.

Track sessions in request/response cycles automatically.

The maximum number of breadcrumbs the SDK could hold.

```ruby
config.max_breadcrumbs = 30
```

Sentry supports different breadcrumbs loggers in the Ruby SDK:

- `:sentry_logger` - A general breadcrumbs logger for all Ruby applications.
- `:http_logger` - Captures requests made with the standard `net/http` library.
- `:redis_logger` - Captures breadcrumbs from redis operations.
- `:active_support_logger` - Built on top of [ActiveSupport instrumentation](https://guides.rubyonrails.org/active_support_instrumentation.html) and provides many Rails-specific information.

And you can enable them with the `breadcrumbs_logger` option:

```ruby
config.breadcrumbs_logger = [:active_support_logger]
config.breadcrumbs_logger = [:active_support_logger, :http_logger]
```

" defaultValue="[]">

Logger names to exclude from breadcrumbs.

How many lines to display before/after the line where issue occurs.

You may provide your own `LineCache` for matching paths with source files to populate `context_lines`. This may be useful if you need to get source code from places other than the disk.

Sets the environment. This string is freeform and not set by default. A release can be associated with more than one environment so that you can separate them in the UI (think `staging` vs `prod` or similar).

Sentry automatically sets the current environment from the environment variables: `SENTRY_CURRENT_ENV`, `SENTRY_ENVIRONMENT`, `RAILS_ENV`, `RACK_ENV` in that order and defaults to `development`.

By default, events will be sent to Sentry in all environments. If you don't want to send events in a specific environment, you can unset the `SENTRY_DSN` variable in that environment.

You can also set up Sentry to only run in certain environments by configuring the `enabled_environments` list. For example, to only run Sentry in production:

```ruby
config.enabled_environments = %w[production]
```

You can use this option to stop getting notifications about certain exceptions. In the example below, the exceptions Rails uses to generate 404 responses will be suppressed.

```ruby
config.excluded_exceptions += ['ActionController::RoutingError', 'ActiveRecord::RecordNotFound']
```

You can find the list of exceptions that are excluded by default in `Sentry::Configuration::IGNORE_DEFAULT`. It is suggested that you append to these defaults rather than overwrite them with `=`.

Inspect an incoming exception's causes when determining whether or not that exception should be excluded. This option works together with `excluded_exceptions`.

```ruby
config.inspect_exception_causes_for_exclusion = true
```

Some of our integrations work via patches that need to be enabled. Use this option to control which patches are loaded when the SDK is initialized.

The list of all available patches is: `[:http, :redis, :puma, :graphql, :faraday]`.

```ruby
# enable :faraday patch
config.enabled_patches << :faraday

# disable :puma patch
config.enabled_patches.delete(:puma)
```

Project directory root for `in_app` detection. Set to `Rails.root` for Rails applications.

Directories to be recognized as `in_app` in backtrace frames.

Whether to strip the load path while constructing the backtrace frame filename.

Determine whether to ignore exceptions caused by rake integrations.

" defaultValue='["REMOTE_ADDR", "SERVER_NAME", "SERVER_PORT"]'>

Array of rack env parameters to be included in the event sent to sentry.

This option can be used to supply a server name sent in the event payload.

If running on Heroku, it is set to `ENV["DYNO"]` otherwise set to `Socket.gethostname`.

These trusted proxies will be skipped when the SDK computes the user's ip address and `sentry-rails` will automatically inject the value of `Rails.application.config.action_dispatch.trusted_proxies` to this option.

```ruby
config.trusted_proxies = ["2.2.2.2"]
```

## Tracing Options

A number between `0` and `1` that determines the percentage of total transaction that will be sent to Sentry (with 0 representing 0% and 1, 100%). This will apply equally to all transactions created in the app. Either this or `traces_sampler` must be defined to enable tracing.

If `traces_sample_rate` is set to 0, no new traces will be created. However, if you have another service (for example a JS frontend) that makes requests to your service and has trace information, those traces will be continued and transactions will be sent to Sentry.

To disable all tracing, you'll need to set `traces_sample_rate = nil`. Once this is done, no new traces will be started and no incoming traces will be continued.

A lambda or proc that's responsible for determining the chance that a given transaction has of being sent to Sentry (from 0-100%). It will automatically be passed information about the transaction and the context in which it's being created, and must return a number between `0` (0% chance of being sent) and `1` (100% chance of being sent).

It can also be used for filtering transactions, by returning 0 for those that are of no interest. Either this or `traces_sample_rate` must be defined to enable tracing.

A boolean that controls whether a new monitor thread will be spawned to perform health checks on the SDK. If the system is unhealthy, the SDK will keep halving the `traces_sample_rate` set by you in 10 second intervals until recovery. This downsampling helps ensure that the system stays stable and reduces SDK overhead under high load.

">

An optional property that controls which downstream services receive tracing data, in the form of a `sentry-trace` and a `baggage` header attached to any outgoing HTTP requests.

The option may contain an array of strings or regex against which the URLs of outgoing requests are matched.
If one of the entries in the list matches the URL of an outgoing request, trace headers will be attached to that request.
String entries don't have to be full matches, (meaning the URL of a request is matched when it _contains_ a string provided through the option).

By default, trace headers are attached to every outgoing request from the instrumented client.

By default, Sentry injects `sentry-trace` and `baggage` headers to outgoing requests made with `Net::HTTP` to connect traces between services. You can disable this behavior with:

```ruby
config.propagate_traces = false
```

" defaultValue="[(301..303), (305..399), (401..404)]">

An optional property that disables tracing for HTTP requests with certain status codes.

Requests are not traced if the status code is contained in the provided list.

```ruby
config.trace_ignore_status_codes = [404, (502..511)]
```

The instrumenter to use, `:sentry` or `:otel` for [use with OpenTelemetry](../../tracing/instrumentation/opentelemetry).

## Hooks

The below options can be used to hook the SDK in various ways and customize how events are being reported.

Provides a lambda or proc that's called with a message or error event object, and can return a modified event object, or `nil` to skip reporting the event. This can be used, for instance, for manual PII stripping before sending.

By the time `before_send` is executed, all scope data has already been applied to the event. Further modification of the scope won't have any effect.

Provides a lambda or proc that's called with a transaction event object, and can return a modified transaction event object, or `nil` to skip reporting the event. One way this might be used is for manual PII stripping before sending.

Provides a lambda or proc that's called with an SDK-specific log object, and can return a modified log object, or `nil` to skip reporting the log. This can be used to filter logs before they are sent to Sentry.

Provides a lambda or proc that's called with a check-in event object, and can return a modified check-in event object, or `nil` to skip reporting the event.

If you want to clean up the backtrace of an exception before it's sent to Sentry, you can specify a callback with `backtrace_cleanup_callback`, for example:

```ruby
config.backtrace_cleanup_callback = lambda do |backtrace|
  Rails.backtrace_cleaner.clean(backtrace)
end
```

This function is called with a breadcrumb object before the breadcrumb is added to the scope. When `nil` is returned from the function, the breadcrumb is dropped. To pass the breadcrumb through, return the first argument, which contains the breadcrumb object.
The callback typically gets a second argument (called a "hint") which contains the original object from which the breadcrumb was created to further customize what the breadcrumb should look like.

## Transport Options

Sentry will send events in a non-blocking way with its own background worker. By default, the worker holds a thread pool that has [the number of available processors](https://ruby-concurrency.github.io/concurrent-ruby/master/Concurrent.html#available_processor_count-class_method) threads. But you can override it as follows:

```ruby
config.background_worker_threads = 5
```

Or if you want to send events synchronously, set the value to 0:

```ruby
config.background_worker_threads = 0
```

The maximum queue size for the background worker. Jobs will be rejected above this limit.

By default, the SDK uses the `Sentry::HTTPTransport` class for sending events to Sentry, which should work for the majority of users. But if you want to use your own Transport class, you can change it with this option:

```ruby
config.transport.transport_class = MyTransportClass
```

It would generally be advisable to derive your custom transport class from `Sentry::HTTPTransport` and just override the necessary logic.

Setup a proxy to use to connect to Sentry. This option is respected by the default `Sentry::HTTPTransport` class. You can set `config.transport.proxy` with as a `String` containing a proxy URI, or a `URI` object, or a `Hash` containing `uri`, `user` and `password` keys.

```ruby
Sentry.init do |config|
  # ...

  # Provide proxy config as a String
  config.transport.proxy = "http://user:password@proxyhost.net:8080"

  # Or a URI
  config.transport.proxy = URI("http://user:password@proxyhost.net:8080")

  # Or a Hash
  config.transport.proxy = {
    uri: "http://proxyhost.net:8080",
    user: "user",
    password: "password"
  }
end
```

Whether to also capture events and traces into [Spotlight](https://spotlightjs.com/setup/other/).

If you set this to true, Sentry will send events and traces to the local Sidecar proxy at `http://localhost:8969/stream`.

If you want to use a different Sidecar proxy address, set this to String with the proxy URL.

## Cron Options

How long (in minutes) after the expected checkin time we will wait until we consider the checkin to have been missed.

```ruby
config.cron.default_checkin_margin = 5
```

How long (in minutes) is the checkin allowed to be `in_progress` before it is considered failed.

```ruby
config.cron.default_max_runtime = 30
```

Database style timezone string for checkins.

```ruby
config.cron.default_timezone = "America/New_York"
```

## Profiler Options

A number between `0` and `1`, controlling the percentage chance a given sampled transaction will be profiled. (`0` represents 0% while `1` represents 100%.) Applies equally to all profiles created in the app. This is relative to the tracing sample rate - e.g. `0.5` means 50% of sampled transactions will be profiled.

Interval in microseconds at which the profiler will collect samples.

The default is 101 Hz. Note that the 101 is intentional to avoid **lockstep sampling**.

The profiler to use for collecting profiles.

Set to `Sentry::Vernier::Profiler` when using `vernier` and `Sentry::Profiler` when using `stackprof`.

See [the Profiling documentation](../../profiling) for setup instructions.


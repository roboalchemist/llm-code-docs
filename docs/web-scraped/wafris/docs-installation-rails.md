# Source: https://wafris.org/docs/installation/rails/

Title: Rails

URL Source: https://wafris.org/docs/installation/rails/

Markdown Content:
[](https://wafris.org/docs/installation/rails/#installation-summary) Installation Summary
-----------------------------------------------------------------------------------------

To add a Wafris Web Application Firewall to your application:

1. Install the `wafris` gem
2. Set the `WAFRIS_API_KEY` environment variable on your server

Note: Signing up at [hub.wafris.org](https://hub.wafris.org/) will provide you with both an API key and detailed instructions for configuring your Rails application. If you’d prefer not to centrally track requests and set rules, you can use the WAF in “local mode” without an API key.

[](https://wafris.org/docs/installation/rails/#how-it-works) How it works
-------------------------------------------------------------------------

The Wafris Ruby client is a gem that installs a Rack middleware into your Rails/Sinatra/Rack application filtering requests based on your created rules.

At startup and periodically, the gem will send a request to the Wafris API to get the latest rules and apply them to the requests.

[](https://wafris.org/docs/installation/rails/#requirements) Requirements
-------------------------------------------------------------------------

* Rails 5+
* Ruby 2.5+

[](https://wafris.org/docs/installation/rails/#gem-installation) Gem installation
---------------------------------------------------------------------------------

### [](https://wafris.org/docs/installation/rails/#add-the-gem-to-your-gemfile) Add the gem to your Gemfile

```
# Gemfile
gem 'wafris', group: :production
```

We would recommend running Wafris on any internet exposed application (staging, qa, production, etc).

[](https://wafris.org/docs/installation/rails/#configuration-setting) Configuration Setting
-------------------------------------------------------------------------------------------

Wafris configuration settings (including the API key) can be set either as environment variables or via the creation of the `config/initializers/wafris.rb` file.

Environment variables will take precedence over initializer settings.

[](https://wafris.org/docs/installation/rails/#environment-variables) Environment Variables
-------------------------------------------------------------------------------------------

### [](https://wafris.org/docs/installation/rails/#api-key---required) API Key - Required

### [](https://wafris.org/docs/installation/rails/#wafris_api_key)`WAFRIS_API_KEY`

This environment variable is required to enable the Wafris Web Application Firewall. It is used to authenticate your application with the Wafris service. If not set, the firewall will be disabled.

### [](https://wafris.org/docs/installation/rails/#db-file-path-location---optional) DB FILE PATH LOCATION - Optional

### [](https://wafris.org/docs/installation/rails/#wafris_db_file_path)`WAFRIS_DB_FILE_PATH`

This environment variable specifies the path where the Wafris database file will be stored. If not set, it defaults to `./tmp/wafris`.

Ensure that the db_file_path exists This code ensures that the specified database file path exists. If it does not exist, it will be created.

### [](https://wafris.org/docs/installation/rails/#db-file-name---for-local) DB FILE NAME - For local

### [](https://wafris.org/docs/installation/rails/#wafris_db_file_name)`WAFRIS_DB_FILE_NAME`

This environment variable specifies the name of the Wafris database file. If not set, it defaults to `wafris.db`.

### [](https://wafris.org/docs/installation/rails/#wafris_downsync_custom_rules_interval)`WAFRIS_DOWNSYNC_CUSTOM_RULES_INTERVAL`

This environment variable sets the interval in seconds for how often custom rules are checked. If not set, it defaults to 60 seconds (1 minute).

### [](https://wafris.org/docs/installation/rails/#wafris_downsync_data_subscriptions_interval)`WAFRIS_DOWNSYNC_DATA_SUBSCRIPTIONS_INTERVAL`

This environment variable sets the interval in seconds for how often data subscriptions are checked. If not set, it defaults to 86400 seconds (1 day).

### [](https://wafris.org/docs/installation/rails/#wafris_downsync_url)`WAFRIS_DOWNSYNC_URL`

This environment variable sets the URL used for downsync operations. If not set, it defaults to `https://distributor.wafris.org/v2/downsync`.

### [](https://wafris.org/docs/installation/rails/#wafris_upsync_url)`WAFRIS_UPSYNC_URL`

This environment variable sets the URL used for upsync operations. If not set, it defaults to `https://collector.wafris.org/v2/upsync`.

### [](https://wafris.org/docs/installation/rails/#wafris_upsync_interval)`WAFRIS_UPSYNC_INTERVAL`

This environment variable sets the interval in seconds for how often upsync operations are performed. If not set, it defaults to 10 seconds.

### [](https://wafris.org/docs/installation/rails/#wafris_upsync_queue_limit)`WAFRIS_UPSYNC_QUEUE_LIMIT`

This environment variable sets the limit for the number of queued upsync requests. If not set, it defaults to 250.

### [](https://wafris.org/docs/installation/rails/#wafris_max_body_size_mb)`WAFRIS_MAX_BODY_SIZE_MB`

This environment variable sets the maximum body size in megabytes for requests. If not set or set to a value less than or equal to 0, it defaults to 10 megabytes.

* * *

# Source: https://wafris.org/docs/configuration/

Title: Configuration

URL Source: https://wafris.org/docs/configuration/

Markdown Content:
[](https://wafris.org/docs/configuration/#environment-variables-documentation) Environment Variables Documentation
------------------------------------------------------------------------------------------------------------------

Each individual Wafris client can be configured via it’s native configuration commands (ex: the Rails client and a config/initializers/wafris.rb file).

[](https://wafris.org/docs/configuration/#configuration-precedence) Configuration Precedence
--------------------------------------------------------------------------------------------

Environment variables take precedence over configuration files. The assumption is that you may specify a global configuration and then override it for a specific environment.

An example would be that you’d like to deploy Wafris to protect all of your production environments, but the logging messes with your CI output. So in your test environment you’d set the environment variable to disable logging.

[](https://wafris.org/docs/configuration/#environment-variables) Environment Variables
--------------------------------------------------------------------------------------

### [](https://wafris.org/docs/configuration/#wafris_api_key) WAFRIS_API_KEY

* **Purpose:** Specifies the API key for Wafris.
* **Default Value:** None
* **Why set it:** You need to set this variable if you want to use Wafris with an API key. This is required for authentication and authorization.
* **Why not set it:** If you’re not using Wafris with an API key, you can leave this variable unset.

### [](https://wafris.org/docs/configuration/#wafris_db_file_path) WAFRIS_DB_FILE_PATH

* **Purpose:** Specifies the file path for the Wafris database.
* **Default Value:** (varies by client), but typically a well known temp directory for the framwork or runtime.
* **Why set it:** You might want to set this variable if you need to change the default location of the Wafris database file. If you’re on a platform that only has ephemeral storage and that resets often (like AWS Lambda) you may want to set this to a more persistent location.

### [](https://wafris.org/docs/configuration/#wafris_db_file_name) WAFRIS_DB_FILE_NAME

* **Purpose:** Specifies the name of the Wafris database file.
* **Default Value:** ‘wafris.db’
* **Why set it:** Setting this enables the Wafris client in standalone instead of managed mode (the default).

In standalone mode, the Wafris client will use the rules database file that you’ve provided instead of one synced from [Wafris Hub](https://hub.wafris.org/).

In managed mode, the Wafris client will sync the rules database file from [Wafris Hub](https://hub.wafris.org/) to the location specified by the WAFRIS_DB_FILE_PATH environment variable.

For more on operational modes, see the [Operational Modes](https://wafris.org/docs/concepts/operational_modes/) page.

### [](https://wafris.org/docs/configuration/#wafris_downsync_custom_rules_interval) WAFRIS_DOWNSYNC_CUSTOM_RULES_INTERVAL

* **Purpose:** Specifies the interval in seconds for checking custom rules during downsync.
* **Default Value:** 10
* **Why set it:** You might want to set this variable if you need to adjust the frequency of custom rule checks.
* **Why not set it:** If you’re happy with the default interval, you don’t need to set this variable.

### [](https://wafris.org/docs/configuration/#wafris_downsync_data_subscriptions_interval) WAFRIS_DOWNSYNC_DATA_SUBSCRIPTIONS_INTERVAL

* **Purpose:** Specifies the interval in seconds for checking data subscriptions during downsync.
* **Default Value:** 86400 (1 day)
* **Why set it:** You might want to set this variable if you need to adjust the frequency of data subscription checks.
* **Why not set it:** If you’re happy with the default interval, you don’t need to set this variable.

### [](https://wafris.org/docs/configuration/#wafris_downsync_url) WAFRIS_DOWNSYNC_URL

* **Purpose:** Specifies the URL for downsync operations.
* **Default Value:** ‘https://distributor.wafris.org/v2/downsync’
* **Why set it:** You might want to set this variable if you need to use a different downsync URL.
* **Why not set it:** If you’re happy with the default URL, you don’t need to set this variable.

### [](https://wafris.org/docs/configuration/#wafris_upsync_url) WAFRIS_UPSYNC_URL

* **Purpose:** Specifies the URL for upsync operations.
* **Default Value:** ‘https://collector.wafris.org/v2/upsync’
* **Why set it:** You might want to set this variable if you need to use a different upsync URL.
* **Why not set it:** If you’re happy with the default URL, you don’t need to set this variable.

### [](https://wafris.org/docs/configuration/#wafris_upsync_interval) WAFRIS_UPSYNC_INTERVAL

* **Purpose:** Specifies the interval in seconds for upsync operations.
* **Default Value:** 10
* **Why set it:** You might want to set this variable if you need to adjust the frequency of upsync operations.
* **Why not set it:** If you’re happy with the default interval, you don’t need to set this variable.

### [](https://wafris.org/docs/configuration/#wafris_upsync_queue_limit) WAFRIS_UPSYNC_QUEUE_LIMIT

* **Purpose:** Specifies the limit for the upsync queue.
* **Default Value:** 250
* **Why set it:** You might want to set this variable if you need to adjust the upsync queue limit.
* **Why not set it:** If you’re happy with the default limit, you don’t need to set this variable.

### [](https://wafris.org/docs/configuration/#wafris_max_body_size_mb) WAFRIS_MAX_BODY_SIZE_MB

* **Purpose:** Specifies the maximum body size in megabytes for requests.
* **Default Value:** 10
* **Why set it:** You might want to set this variable if you need to adjust the maximum body size for requests.
* **Why not set it:** If you’re happy with the default size, you don’t need to set this variable.

* * *

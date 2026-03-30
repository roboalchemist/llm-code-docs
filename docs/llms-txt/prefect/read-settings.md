# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/admin/read-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Settings

> Get the current Prefect REST API settings.

Secret setting values will be obfuscated.



## OpenAPI

````yaml get /admin/settings
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /admin/settings:
    get:
      tags:
        - Admin
      summary: Read Settings
      description: |-
        Get the current Prefect REST API settings.

        Secret setting values will be obfuscated.
      operationId: read_settings_admin_settings_get
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Settings'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Settings:
      properties:
        home:
          type: string
          format: path
          title: Home
          description: The path to the Prefect home directory. Defaults to ~/.prefect
          default: ~/.prefect
          supported_environment_variables:
            - PREFECT_HOME
        profiles_path:
          type: string
          format: path
          title: Profiles Path
          description: >-
            The path to a profiles configuration file. Supports \$PREFECT_HOME
            templating. Defaults to \$PREFECT_HOME/profiles.toml.
          supported_environment_variables:
            - PREFECT_PROFILES_PATH
        debug_mode:
          type: boolean
          title: Debug Mode
          description: >-
            If True, enables debug mode which may provide additional logging and
            debugging features.
          default: false
          supported_environment_variables:
            - PREFECT_DEBUG_MODE
        api:
          $ref: '#/components/schemas/APISettings'
          supported_environment_variables: []
        cli:
          $ref: '#/components/schemas/CLISettings'
          supported_environment_variables: []
        client:
          $ref: '#/components/schemas/ClientSettings'
          supported_environment_variables: []
        cloud:
          $ref: '#/components/schemas/CloudSettings'
          supported_environment_variables: []
        deployments:
          $ref: '#/components/schemas/DeploymentsSettings'
          supported_environment_variables: []
        experiments:
          $ref: '#/components/schemas/ExperimentsSettings'
          description: Settings for controlling experimental features
          supported_environment_variables: []
        flows:
          $ref: '#/components/schemas/FlowsSettings'
          supported_environment_variables: []
        internal:
          $ref: '#/components/schemas/InternalSettings'
          description: Settings for internal Prefect machinery
          supported_environment_variables: []
        logging:
          $ref: '#/components/schemas/LoggingSettings'
          supported_environment_variables: []
        results:
          $ref: '#/components/schemas/ResultsSettings'
          supported_environment_variables: []
        runner:
          $ref: '#/components/schemas/RunnerSettings'
          supported_environment_variables: []
        server:
          $ref: '#/components/schemas/ServerSettings'
          supported_environment_variables: []
        tasks:
          $ref: '#/components/schemas/TasksSettings'
          description: Settings for controlling task behavior
          supported_environment_variables: []
        testing:
          $ref: '#/components/schemas/TestingSettings'
          description: Settings used during testing
          supported_environment_variables: []
        worker:
          $ref: '#/components/schemas/WorkerSettings'
          description: Settings for controlling worker behavior
          supported_environment_variables: []
        ui_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Ui Url
          description: >-
            The URL of the Prefect UI. If not set, the client will attempt to
            infer it.
          supported_environment_variables:
            - PREFECT_UI_URL
        silence_api_url_misconfiguration:
          type: boolean
          title: Silence Api Url Misconfiguration
          description: |2-

                    If `True`, disable the warning when a user accidentally misconfigure its `PREFECT_API_URL`
                    Sometimes when a user manually set `PREFECT_API_URL` to a custom url,reverse-proxy for example,
                    we would like to silence this warning so we will set it to `FALSE`.
                    
          default: false
          supported_environment_variables:
            - PREFECT_SILENCE_API_URL_MISCONFIGURATION
      type: object
      title: Settings
      description: |-
        Settings for Prefect using Pydantic settings.

        See https://docs.pydantic.dev/latest/concepts/pydantic_settings
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    APISettings:
      properties:
        url:
          anyOf:
            - type: string
            - type: 'null'
          title: Url
          description: >-
            The URL of the Prefect API. If not set, the client will attempt to
            infer it.
          supported_environment_variables:
            - PREFECT_API_URL
        auth_string:
          anyOf:
            - type: string
              format: password
              writeOnly: true
            - type: 'null'
          title: Auth String
          description: >-
            The auth string used for basic authentication with a self-hosted
            Prefect API. Should be kept secret.
          supported_environment_variables:
            - PREFECT_API_AUTH_STRING
        key:
          anyOf:
            - type: string
              format: password
              writeOnly: true
            - type: 'null'
          title: Key
          description: >-
            The API key used for authentication with the Prefect API. Should be
            kept secret.
          supported_environment_variables:
            - PREFECT_API_KEY
        tls_insecure_skip_verify:
          type: boolean
          title: Tls Insecure Skip Verify
          description: >-
            If `True`, disables SSL checking to allow insecure requests. Setting
            to False is recommended only during development. For example, when
            using self-signed certificates.
          default: false
          supported_environment_variables:
            - PREFECT_API_TLS_INSECURE_SKIP_VERIFY
        ssl_cert_file:
          anyOf:
            - type: string
            - type: 'null'
          title: Ssl Cert File
          description: >-
            This configuration settings option specifies the path to an SSL
            certificate file.
          supported_environment_variables:
            - PREFECT_API_SSL_CERT_FILE
        enable_http2:
          type: boolean
          title: Enable Http2
          description: >-
            If true, enable support for HTTP/2 for communicating with an API. If
            the API does not support HTTP/2, this will have no effect and
            connections will be made via HTTP/1.1.
          default: false
          supported_environment_variables:
            - PREFECT_API_ENABLE_HTTP2
        request_timeout:
          type: number
          title: Request Timeout
          description: The default timeout for requests to the API
          default: 60
          supported_environment_variables:
            - PREFECT_API_REQUEST_TIMEOUT
      type: object
      title: APISettings
      description: Settings for interacting with the Prefect API
    CLISettings:
      properties:
        colors:
          type: boolean
          title: Colors
          description: >-
            If True, use colors in CLI output. If `False`, output will not
            include colors codes.
          default: true
          supported_environment_variables:
            - PREFECT_CLI_COLORS
        prompt:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Prompt
          description: >-
            If `True`, use interactive prompts in CLI commands. If `False`, no
            interactive prompts will be used. If `None`, the value will be
            dynamically determined based on the presence of an
            interactive-enabled terminal.
          supported_environment_variables:
            - PREFECT_CLI_PROMPT
        wrap_lines:
          type: boolean
          title: Wrap Lines
          description: >-
            If `True`, wrap text by inserting new lines in long lines in CLI
            output. If `False`, output will not be wrapped.
          default: true
          supported_environment_variables:
            - PREFECT_CLI_WRAP_LINES
      type: object
      title: CLISettings
      description: Settings for controlling CLI behavior
    ClientSettings:
      properties:
        max_retries:
          type: integer
          minimum: 0
          title: Max Retries
          description: |2-

                    The maximum number of retries to perform on failed HTTP requests.
                    Defaults to 5. Set to 0 to disable retries.
                    See `PREFECT_CLIENT_RETRY_EXTRA_CODES` for details on which HTTP status codes are
                    retried.
                    
          default: 5
          supported_environment_variables:
            - PREFECT_CLIENT_MAX_RETRIES
        retry_jitter_factor:
          type: number
          minimum: 0
          title: Retry Jitter Factor
          description: |2-

                    A value greater than or equal to zero to control the amount of jitter added to retried
                    client requests. Higher values introduce larger amounts of jitter.
                    Set to 0 to disable jitter. See `clamped_poisson_interval` for details on the how jitter
                    can affect retry lengths.
                    
          default: 0.2
          supported_environment_variables:
            - PREFECT_CLIENT_RETRY_JITTER_FACTOR
        retry_extra_codes:
          anyOf:
            - type: string
            - type: integer
              maximum: 599
              minimum: 100
            - items:
                type: integer
                maximum: 599
                minimum: 100
              type: array
              uniqueItems: true
            - type: 'null'
          title: Retry Extra Codes
          description: |2-

                    A list of extra HTTP status codes to retry on. Defaults to an empty list.
                    429, 502 and 503 are always retried. Please note that not all routes are idempotent and retrying
                    may result in unexpected behavior.
                    
          examples:
            - 404,429,503
            - '429'
            - - 404
              - 429
              - 503
          supported_environment_variables:
            - PREFECT_CLIENT_RETRY_EXTRA_CODES
        csrf_support_enabled:
          type: boolean
          title: Csrf Support Enabled
          description: |2-

                    Determines if CSRF token handling is active in the Prefect client for API
                    requests.

                    When enabled (`True`), the client automatically manages CSRF tokens by
                    retrieving, storing, and including them in applicable state-changing requests
                    
          default: true
          supported_environment_variables:
            - PREFECT_CLIENT_CSRF_SUPPORT_ENABLED
        custom_headers:
          additionalProperties:
            type: string
          type: object
          title: Custom Headers
          description: |2-

                    Custom HTTP headers to include with every API request to the Prefect server.
                    Headers are specified as key-value pairs. Note that headers like 'User-Agent'
                    and CSRF-related headers are managed by Prefect and cannot be overridden.
                    
          examples:
            - X-Custom-Header: value
            - Authorization: Bearer token
          supported_environment_variables:
            - PREFECT_CLIENT_CUSTOM_HEADERS
        metrics:
          $ref: '#/components/schemas/ClientMetricsSettings'
          supported_environment_variables: []
      type: object
      title: ClientSettings
      description: Settings for controlling API client behavior
    CloudSettings:
      properties:
        api_url:
          type: string
          title: Api Url
          description: >-
            API URL for Prefect Cloud. Used for authentication with Prefect
            Cloud.
          default: https://api.prefect.cloud/api
          supported_environment_variables:
            - PREFECT_CLOUD_API_URL
        enable_orchestration_telemetry:
          type: boolean
          title: Enable Orchestration Telemetry
          description: Whether or not to enable orchestration telemetry.
          default: true
          supported_environment_variables:
            - PREFECT_CLOUD_ENABLE_ORCHESTRATION_TELEMETRY
        max_log_size:
          type: integer
          title: Max Log Size
          description: >-
            Maximum size in characters for a single log when sending logs to
            Prefect Cloud.
          default: 25000
          supported_environment_variables:
            - PREFECT_CLOUD_MAX_LOG_SIZE
        ui_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Ui Url
          description: >-
            The URL of the Prefect Cloud UI. If not set, the client will attempt
            to infer it.
          supported_environment_variables:
            - PREFECT_CLOUD_UI_URL
      type: object
      title: CloudSettings
      description: Settings for interacting with Prefect Cloud
    DeploymentsSettings:
      properties:
        default_work_pool_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Default Work Pool Name
          description: The default work pool to use when creating deployments.
          supported_environment_variables:
            - PREFECT_DEPLOYMENTS_DEFAULT_WORK_POOL_NAME
            - PREFECT_DEFAULT_WORK_POOL_NAME
        default_docker_build_namespace:
          anyOf:
            - type: string
            - type: 'null'
          title: Default Docker Build Namespace
          description: The default Docker namespace to use when building images.
          examples:
            - my-dockerhub-registry
            - 4999999999999.dkr.ecr.us-east-2.amazonaws.com/my-ecr-repo
          supported_environment_variables:
            - PREFECT_DEPLOYMENTS_DEFAULT_DOCKER_BUILD_NAMESPACE
            - PREFECT_DEFAULT_DOCKER_BUILD_NAMESPACE
      type: object
      title: DeploymentsSettings
      description: Settings for configuring deployments defaults
    ExperimentsSettings:
      properties:
        warn:
          type: boolean
          title: Warn
          description: If `True`, warn on usage of experimental features.
          default: true
          supported_environment_variables:
            - PREFECT_EXPERIMENTS_WARN
            - PREFECT_EXPERIMENTAL_WARN
        plugins:
          $ref: '#/components/schemas/PluginsSettings'
          description: Settings for the experimental plugin system
          supported_environment_variables: []
      type: object
      title: ExperimentsSettings
      description: Settings for configuring experimental features
    FlowsSettings:
      properties:
        heartbeat_frequency:
          anyOf:
            - type: integer
              minimum: 30
            - type: 'null'
          title: Heartbeat Frequency
          description: >-
            Number of seconds between flow run heartbeats. Heartbeats are used
            to detect crashed flow runs.
          supported_environment_variables:
            - PREFECT_FLOWS_HEARTBEAT_FREQUENCY
            - PREFECT_RUNNER_HEARTBEAT_FREQUENCY
        default_retries:
          type: integer
          minimum: 0
          title: Default Retries
          description: This value sets the default number of retries for all flows.
          default: 0
          supported_environment_variables:
            - PREFECT_FLOWS_DEFAULT_RETRIES
            - PREFECT_FLOW_DEFAULT_RETRIES
        default_retry_delay_seconds:
          anyOf:
            - type: integer
            - type: number
            - items:
                type: number
              type: array
          title: Default Retry Delay Seconds
          description: This value sets the default retry delay seconds for all flows.
          default: 0
          supported_environment_variables:
            - PREFECT_FLOWS_DEFAULT_RETRY_DELAY_SECONDS
            - PREFECT_FLOW_DEFAULT_RETRY_DELAY_SECONDS
      type: object
      title: FlowsSettings
      description: Settings for controlling flow behavior
    InternalSettings:
      properties:
        logging_level:
          type: string
          enum:
            - DEBUG
            - INFO
            - WARNING
            - ERROR
            - CRITICAL
          title: Logging Level
          description: The default logging level for Prefect's internal machinery loggers.
          default: ERROR
          supported_environment_variables:
            - PREFECT_INTERNAL_LOGGING_LEVEL
            - PREFECT_LOGGING_INTERNAL_LEVEL
      type: object
      title: InternalSettings
    LoggingSettings:
      properties:
        level:
          type: string
          enum:
            - DEBUG
            - INFO
            - WARNING
            - ERROR
            - CRITICAL
          title: Level
          description: The default logging level for Prefect loggers.
          default: INFO
          supported_environment_variables:
            - PREFECT_LOGGING_LEVEL
        config_path:
          type: string
          format: path
          title: Config Path
          description: >-
            A path to a logging configuration file. Defaults to
            $PREFECT_HOME/logging.yml
          supported_environment_variables:
            - PREFECT_LOGGING_CONFIG_PATH
            - PREFECT_LOGGING_SETTINGS_PATH
        extra_loggers:
          anyOf:
            - type: string
            - items:
                type: string
              type: array
            - type: 'null'
          title: Extra Loggers
          description: Additional loggers to attach to Prefect logging at runtime.
          supported_environment_variables:
            - PREFECT_LOGGING_EXTRA_LOGGERS
        log_prints:
          type: boolean
          title: Log Prints
          description: >-
            If `True`, `print` statements in flows and tasks will be redirected
            to the Prefect logger for the given run.
          default: false
          supported_environment_variables:
            - PREFECT_LOGGING_LOG_PRINTS
        colors:
          type: boolean
          title: Colors
          description: >-
            If `True`, use colors in CLI output. If `False`, output will not
            include colors codes.
          default: true
          supported_environment_variables:
            - PREFECT_LOGGING_COLORS
        markup:
          type: boolean
          title: Markup
          description: |2-

                    Whether to interpret strings wrapped in square brackets as a style.
                    This allows styles to be conveniently added to log messages, e.g.
                    `[red]This is a red message.[/red]`. However, the downside is, if enabled,
                    strings that contain square brackets may be inaccurately interpreted and
                    lead to incomplete output, e.g.
                    `[red]This is a red message.[/red]` may be interpreted as
                    `[red]This is a red message.[/red]`.
                    
          default: false
          supported_environment_variables:
            - PREFECT_LOGGING_MARKUP
        to_api:
          $ref: '#/components/schemas/LoggingToAPISettings'
          supported_environment_variables: []
      type: object
      title: LoggingSettings
      description: Settings for controlling logging behavior
    ResultsSettings:
      properties:
        default_serializer:
          type: string
          title: Default Serializer
          description: The default serializer to use when not otherwise specified.
          default: pickle
          supported_environment_variables:
            - PREFECT_RESULTS_DEFAULT_SERIALIZER
        persist_by_default:
          type: boolean
          title: Persist By Default
          description: >-
            The default setting for persisting results when not otherwise
            specified.
          default: false
          supported_environment_variables:
            - PREFECT_RESULTS_PERSIST_BY_DEFAULT
        default_storage_block:
          anyOf:
            - type: string
            - type: 'null'
          title: Default Storage Block
          description: >-
            The `block-type/block-document` slug of a block to use as the
            default result storage.
          supported_environment_variables:
            - PREFECT_RESULTS_DEFAULT_STORAGE_BLOCK
            - PREFECT_DEFAULT_RESULT_STORAGE_BLOCK
        local_storage_path:
          type: string
          format: path
          title: Local Storage Path
          description: >-
            The default location for locally persisted results. Defaults to
            $PREFECT_HOME/storage.
          supported_environment_variables:
            - PREFECT_RESULTS_LOCAL_STORAGE_PATH
            - PREFECT_LOCAL_STORAGE_PATH
      type: object
      title: ResultsSettings
      description: Settings for controlling result storage behavior
    RunnerSettings:
      properties:
        process_limit:
          type: integer
          title: Process Limit
          description: Maximum number of processes a runner will execute in parallel.
          default: 5
          supported_environment_variables:
            - PREFECT_RUNNER_PROCESS_LIMIT
        poll_frequency:
          type: integer
          title: Poll Frequency
          description: >-
            Number of seconds a runner should wait between queries for scheduled
            work.
          default: 10
          supported_environment_variables:
            - PREFECT_RUNNER_POLL_FREQUENCY
        crash_on_cancellation_failure:
          type: boolean
          title: Crash On Cancellation Failure
          description: >-
            Whether to crash flow runs and shut down the runner when
            cancellation observing fails. When enabled, if both websocket and
            polling mechanisms for detecting cancellation events fail, all
            in-flight flow runs will be marked as crashed and the runner will
            shut down. When disabled (default), the runner will log an error but
            continue executing flow runs.
          default: false
          supported_environment_variables:
            - PREFECT_RUNNER_CRASH_ON_CANCELLATION_FAILURE
        server:
          $ref: '#/components/schemas/RunnerServerSettings'
          supported_environment_variables: []
      type: object
      title: RunnerSettings
      description: Settings for controlling runner behavior
    ServerSettings:
      properties:
        logging_level:
          type: string
          enum:
            - DEBUG
            - INFO
            - WARNING
            - ERROR
            - CRITICAL
          title: Logging Level
          description: The default logging level for the Prefect API server.
          default: WARNING
          supported_environment_variables:
            - PREFECT_SERVER_LOGGING_LEVEL
            - PREFECT_LOGGING_SERVER_LEVEL
        analytics_enabled:
          type: boolean
          title: Analytics Enabled
          description: |2-

                    When enabled, Prefect sends anonymous data (e.g. count of flow runs, package version)
                    on server startup to help us improve our product.
                    
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_ANALYTICS_ENABLED
        metrics_enabled:
          type: boolean
          title: Metrics Enabled
          description: Whether or not to enable Prometheus metrics in the API.
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_METRICS_ENABLED
            - PREFECT_API_ENABLE_METRICS
        log_retryable_errors:
          type: boolean
          title: Log Retryable Errors
          description: If `True`, log retryable errors in the API and it's services.
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_LOG_RETRYABLE_ERRORS
            - PREFECT_API_LOG_RETRYABLE_ERRORS
        register_blocks_on_start:
          type: boolean
          title: Register Blocks On Start
          description: >-
            If set, any block types that have been imported will be registered
            with the backend on application startup. If not set, block types
            must be manually registered.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_REGISTER_BLOCKS_ON_START
            - PREFECT_API_BLOCKS_REGISTER_ON_START
        memoize_block_auto_registration:
          type: boolean
          title: Memoize Block Auto Registration
          description: Controls whether or not block auto-registration on start
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_MEMOIZE_BLOCK_AUTO_REGISTRATION
            - PREFECT_MEMOIZE_BLOCK_AUTO_REGISTRATION
        memo_store_path:
          type: string
          format: path
          title: Memo Store Path
          description: >-
            Path to the memo store file. Defaults to
            $PREFECT_HOME/memo_store.toml
          supported_environment_variables:
            - PREFECT_SERVER_MEMO_STORE_PATH
            - PREFECT_MEMO_STORE_PATH
        deployment_schedule_max_scheduled_runs:
          type: integer
          title: Deployment Schedule Max Scheduled Runs
          description: The maximum number of scheduled runs to create for a deployment.
          default: 50
          supported_environment_variables:
            - PREFECT_SERVER_DEPLOYMENT_SCHEDULE_MAX_SCHEDULED_RUNS
            - PREFECT_DEPLOYMENT_SCHEDULE_MAX_SCHEDULED_RUNS
        api:
          $ref: '#/components/schemas/ServerAPISettings'
          supported_environment_variables: []
        concurrency:
          $ref: '#/components/schemas/ServerConcurrencySettings'
          description: Settings for controlling server-side concurrency limit handling
          supported_environment_variables: []
        database:
          $ref: '#/components/schemas/ServerDatabaseSettings'
          supported_environment_variables: []
        deployments:
          $ref: '#/components/schemas/ServerDeploymentsSettings'
          description: Settings for controlling server deployments behavior
          supported_environment_variables: []
        docket:
          $ref: '#/components/schemas/ServerDocketSettings'
          description: Settings for controlling server Docket behavior
          supported_environment_variables: []
        ephemeral:
          $ref: '#/components/schemas/ServerEphemeralSettings'
          supported_environment_variables: []
        events:
          $ref: '#/components/schemas/ServerEventsSettings'
          description: Settings for controlling server events behavior
          supported_environment_variables: []
        flow_run_graph:
          $ref: '#/components/schemas/ServerFlowRunGraphSettings'
          description: Settings for controlling flow run graph behavior
          supported_environment_variables: []
        logs:
          $ref: '#/components/schemas/ServerLogsSettings'
          description: Settings for controlling server logs behavior
          supported_environment_variables: []
        services:
          $ref: '#/components/schemas/ServerServicesSettings'
          description: Settings for controlling server services behavior
          supported_environment_variables: []
        tasks:
          $ref: '#/components/schemas/ServerTasksSettings'
          description: Settings for controlling server tasks behavior
          supported_environment_variables: []
        ui:
          $ref: '#/components/schemas/ServerUISettings'
          description: Settings for controlling server UI behavior
          supported_environment_variables: []
      type: object
      title: ServerSettings
      description: Settings for controlling server behavior
    TasksSettings:
      properties:
        refresh_cache:
          type: boolean
          title: Refresh Cache
          description: >-
            If `True`, enables a refresh of cached results: re-executing the
            task will refresh the cached results.
          default: false
          supported_environment_variables:
            - PREFECT_TASKS_REFRESH_CACHE
        default_no_cache:
          type: boolean
          title: Default No Cache
          description: If `True`, sets the default cache policy on all tasks to `NO_CACHE`.
          default: false
          supported_environment_variables:
            - PREFECT_TASKS_DEFAULT_NO_CACHE
        disable_caching:
          type: boolean
          title: Disable Caching
          description: If `True`, disables caching on all tasks regardless of cache policy.
          default: false
          supported_environment_variables:
            - PREFECT_TASKS_DISABLE_CACHING
        default_retries:
          type: integer
          minimum: 0
          title: Default Retries
          description: This value sets the default number of retries for all tasks.
          default: 0
          supported_environment_variables:
            - PREFECT_TASKS_DEFAULT_RETRIES
            - PREFECT_TASK_DEFAULT_RETRIES
        default_retry_delay_seconds:
          anyOf:
            - type: string
            - type: integer
            - type: number
            - items:
                type: number
              type: array
            - type: 'null'
          title: Default Retry Delay Seconds
          description: This value sets the default retry delay seconds for all tasks.
          default: 0
          supported_environment_variables:
            - PREFECT_TASKS_DEFAULT_RETRY_DELAY_SECONDS
            - PREFECT_TASK_DEFAULT_RETRY_DELAY_SECONDS
        default_persist_result:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Default Persist Result
          description: >-
            If `True`, results will be persisted by default for all tasks. Set
            to `False` to disable persistence by default. Note that setting to
            `False` will override the behavior set by a parent flow or task.
          supported_environment_variables:
            - PREFECT_TASKS_DEFAULT_PERSIST_RESULT
        runner:
          $ref: '#/components/schemas/TasksRunnerSettings'
          description: Settings for controlling task runner behavior
          supported_environment_variables: []
        scheduling:
          $ref: '#/components/schemas/TasksSchedulingSettings'
          description: Settings for controlling client-side task scheduling behavior
          supported_environment_variables: []
      type: object
      title: TasksSettings
    TestingSettings:
      properties:
        test_mode:
          type: boolean
          title: Test Mode
          description: >-
            If `True`, places the API in test mode. This may modify behavior to
            facilitate testing.
          default: false
          supported_environment_variables:
            - PREFECT_TESTING_TEST_MODE
            - PREFECT_TEST_MODE
        unit_test_mode:
          type: boolean
          title: Unit Test Mode
          description: >-
            This setting only exists to facilitate unit testing. If `True`, code
            is executing in a unit test context. Defaults to `False`.
          default: false
          supported_environment_variables:
            - PREFECT_TESTING_UNIT_TEST_MODE
            - PREFECT_UNIT_TEST_MODE
        unit_test_loop_debug:
          type: boolean
          title: Unit Test Loop Debug
          description: If `True` turns on debug mode for the unit testing event loop.
          default: true
          supported_environment_variables:
            - PREFECT_TESTING_UNIT_TEST_LOOP_DEBUG
            - PREFECT_UNIT_TEST_LOOP_DEBUG
        test_setting:
          anyOf:
            - {}
            - type: 'null'
          title: Test Setting
          description: >-
            This setting only exists to facilitate unit testing. If in test
            mode, this setting will return its value. Otherwise, it returns
            `None`.
          default: FOO
          supported_environment_variables:
            - PREFECT_TESTING_TEST_SETTING
            - PREFECT_TEST_SETTING
      type: object
      title: TestingSettings
    WorkerSettings:
      properties:
        debug_mode:
          type: boolean
          title: Debug Mode
          description: >-
            If True, enables debug mode for the worker only. Unlike
            PREFECT_DEBUG_MODE, this setting does not propagate to flow runs
            executed by the worker.
          default: false
          supported_environment_variables:
            - PREFECT_WORKER_DEBUG_MODE
        heartbeat_seconds:
          type: number
          title: Heartbeat Seconds
          description: Number of seconds a worker should wait between sending a heartbeat.
          default: 30
          supported_environment_variables:
            - PREFECT_WORKER_HEARTBEAT_SECONDS
        query_seconds:
          type: number
          title: Query Seconds
          description: >-
            Number of seconds a worker should wait between queries for scheduled
            work.
          default: 10
          supported_environment_variables:
            - PREFECT_WORKER_QUERY_SECONDS
        prefetch_seconds:
          type: number
          title: Prefetch Seconds
          description: >-
            The number of seconds into the future a worker should query for
            scheduled work.
          default: 10
          supported_environment_variables:
            - PREFECT_WORKER_PREFETCH_SECONDS
        enable_cancellation:
          type: boolean
          title: Enable Cancellation
          description: >-
            Enable worker-side flow run cancellation for pending flow runs. When
            enabled, the worker will terminate infrastructure for flow runs that
            are cancelled while still in PENDING state (before the runner
            starts).
          default: false
          supported_environment_variables:
            - PREFECT_WORKER_ENABLE_CANCELLATION
        cancellation_poll_seconds:
          type: number
          title: Cancellation Poll Seconds
          description: >-
            Number of seconds between polls for cancelling flow runs. Used as a
            fallback when the WebSocket connection for real-time cancellation
            events is unavailable.
          default: 120
          supported_environment_variables:
            - PREFECT_WORKER_CANCELLATION_POLL_SECONDS
        webserver:
          $ref: '#/components/schemas/WorkerWebserverSettings'
          description: Settings for a worker's webserver
          supported_environment_variables: []
      type: object
      title: WorkerSettings
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    ClientMetricsSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: Whether or not to enable Prometheus metrics in the client.
          default: false
          supported_environment_variables:
            - PREFECT_CLIENT_METRICS_ENABLED
            - PREFECT_CLIENT_ENABLE_METRICS
        port:
          type: integer
          title: Port
          description: The port to expose the client Prometheus metrics on.
          default: 4201
          supported_environment_variables:
            - PREFECT_CLIENT_METRICS_PORT
      type: object
      title: ClientMetricsSettings
      description: Settings for controlling metrics reporting from the client
    PluginsSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: Enable the experimental plugin system.
          default: false
          supported_environment_variables:
            - PREFECT_EXPERIMENTS_PLUGINS_ENABLED
        allow:
          anyOf:
            - items:
                type: string
              type: array
              uniqueItems: true
            - type: 'null'
          title: Allow
          description: >-
            Comma-separated list of plugin names to allow. If set, only these
            plugins will be loaded.
          supported_environment_variables:
            - PREFECT_EXPERIMENTS_PLUGINS_ALLOW
        deny:
          anyOf:
            - items:
                type: string
              type: array
              uniqueItems: true
            - type: 'null'
          title: Deny
          description: >-
            Comma-separated list of plugin names to deny. These plugins will not
            be loaded.
          supported_environment_variables:
            - PREFECT_EXPERIMENTS_PLUGINS_DENY
        setup_timeout_seconds:
          type: number
          title: Setup Timeout Seconds
          description: >-
            Maximum time in seconds for all plugins to complete their setup
            hooks.
          default: 20
          supported_environment_variables:
            - PREFECT_EXPERIMENTS_PLUGINS_SETUP_TIMEOUT_SECONDS
        strict:
          type: boolean
          title: Strict
          description: If True, exit if a required plugin fails during setup.
          default: false
          supported_environment_variables:
            - PREFECT_EXPERIMENTS_PLUGINS_STRICT
        safe_mode:
          type: boolean
          title: Safe Mode
          description: >-
            If True, load plugins but do not execute their hooks. Useful for
            testing.
          default: false
          supported_environment_variables:
            - PREFECT_EXPERIMENTS_PLUGINS_SAFE_MODE
      type: object
      title: PluginsSettings
      description: Settings for configuring the experimental plugin system
    LoggingToAPISettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: If `True`, logs will be sent to the API.
          default: true
          supported_environment_variables:
            - PREFECT_LOGGING_TO_API_ENABLED
        batch_interval:
          type: number
          title: Batch Interval
          description: The number of seconds between batched writes of logs to the API.
          default: 2
          supported_environment_variables:
            - PREFECT_LOGGING_TO_API_BATCH_INTERVAL
        batch_size:
          type: integer
          title: Batch Size
          description: The number of logs to batch before sending to the API.
          default: 4000000
          supported_environment_variables:
            - PREFECT_LOGGING_TO_API_BATCH_SIZE
        max_log_size:
          type: integer
          title: Max Log Size
          description: >-
            The maximum size in characters for a single log. When connected to
            Prefect Cloud, this value is capped at `PREFECT_CLOUD_MAX_LOG_SIZE`
            (default 25,000).
          default: 1000000
          supported_environment_variables:
            - PREFECT_LOGGING_TO_API_MAX_LOG_SIZE
        when_missing_flow:
          type: string
          enum:
            - warn
            - error
            - ignore
          title: When Missing Flow
          description: |2-

                    Controls the behavior when loggers attempt to send logs to the API handler from outside of a flow.
                    
                    All logs sent to the API must be associated with a flow run. The API log handler can
                    only be used outside of a flow by manually providing a flow run identifier. Logs
                    that are not associated with a flow run will not be sent to the API. This setting can
                    be used to determine if a warning or error is displayed when the identifier is missing.

                    The following options are available:

                    - "warn": Log a warning message.
                    - "error": Raise an error.
                    - "ignore": Do not log a warning message or raise an error.
                    
          default: warn
          supported_environment_variables:
            - PREFECT_LOGGING_TO_API_WHEN_MISSING_FLOW
      type: object
      title: LoggingToAPISettings
      description: Settings for controlling logging to the API
    RunnerServerSettings:
      properties:
        enable:
          type: boolean
          title: Enable
          description: Whether or not to enable the runner's webserver.
          default: false
          supported_environment_variables:
            - PREFECT_RUNNER_SERVER_ENABLE
        host:
          type: string
          title: Host
          description: The host address the runner's webserver should bind to.
          default: localhost
          supported_environment_variables:
            - PREFECT_RUNNER_SERVER_HOST
        port:
          type: integer
          title: Port
          description: The port the runner's webserver should bind to.
          default: 8080
          supported_environment_variables:
            - PREFECT_RUNNER_SERVER_PORT
        log_level:
          type: string
          enum:
            - DEBUG
            - INFO
            - WARNING
            - ERROR
            - CRITICAL
          title: Log Level
          description: The log level of the runner's webserver.
          default: ERROR
          supported_environment_variables:
            - PREFECT_RUNNER_SERVER_LOG_LEVEL
        missed_polls_tolerance:
          type: integer
          title: Missed Polls Tolerance
          description: >-
            Number of missed polls before a runner is considered unhealthy by
            its webserver.
          default: 2
          supported_environment_variables:
            - PREFECT_RUNNER_SERVER_MISSED_POLLS_TOLERANCE
      type: object
      title: RunnerServerSettings
      description: Settings for controlling runner server behavior
    ServerAPISettings:
      properties:
        auth_string:
          anyOf:
            - type: string
              format: password
              writeOnly: true
            - type: 'null'
          title: Auth String
          description: >-
            A string to use for basic authentication with the API in the form
            'user:password'.
          supported_environment_variables:
            - PREFECT_SERVER_API_AUTH_STRING
        host:
          type: string
          title: Host
          description: The API's host address (defaults to `127.0.0.1`).
          default: 127.0.0.1
          supported_environment_variables:
            - PREFECT_SERVER_API_HOST
        port:
          type: integer
          title: Port
          description: The API's port address (defaults to `4200`).
          default: 4200
          supported_environment_variables:
            - PREFECT_SERVER_API_PORT
        base_path:
          anyOf:
            - type: string
            - type: 'null'
          title: Base Path
          description: The base URL path to serve the API under.
          examples:
            - /v2/api
          supported_environment_variables:
            - PREFECT_SERVER_API_BASE_PATH
        default_limit:
          type: integer
          title: Default Limit
          description: >-
            The default limit applied to queries that can return multiple
            objects, such as `POST /flow_runs/filter`.
          default: 200
          supported_environment_variables:
            - PREFECT_SERVER_API_DEFAULT_LIMIT
            - PREFECT_API_DEFAULT_LIMIT
        keepalive_timeout:
          type: integer
          title: Keepalive Timeout
          description: |2-

                    The API's keep alive timeout (defaults to `5`).
                    Refer to https://www.uvicorn.org/settings/#timeouts for details.

                    When the API is hosted behind a load balancer, you may want to set this to a value
                    greater than the load balancer's idle timeout.

                    Note this setting only applies when calling `prefect server start`; if hosting the
                    API with another tool you will need to configure this there instead.
                    
          default: 5
          supported_environment_variables:
            - PREFECT_SERVER_API_KEEPALIVE_TIMEOUT
        csrf_protection_enabled:
          type: boolean
          title: Csrf Protection Enabled
          description: |2-

                    Controls the activation of CSRF protection for the Prefect server API.

                    When enabled (`True`), the server enforces CSRF validation checks on incoming
                    state-changing requests (POST, PUT, PATCH, DELETE), requiring a valid CSRF
                    token to be included in the request headers or body. This adds a layer of
                    security by preventing unauthorized or malicious sites from making requests on
                    behalf of authenticated users.

                    It is recommended to enable this setting in production environments where the
                    API is exposed to web clients to safeguard against CSRF attacks.

                    Note: Enabling this setting requires corresponding support in the client for
                    CSRF token management. See PREFECT_CLIENT_CSRF_SUPPORT_ENABLED for more.
                    
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_API_CSRF_PROTECTION_ENABLED
            - PREFECT_SERVER_CSRF_PROTECTION_ENABLED
        csrf_token_expiration:
          type: string
          format: duration
          title: Csrf Token Expiration
          description: |2-

                    Specifies the duration for which a CSRF token remains valid after being issued
                    by the server.

                    The default expiration time is set to 1 hour, which offers a reasonable
                    compromise. Adjust this setting based on your specific security requirements
                    and usage patterns.
                    
          default: PT1H
          supported_environment_variables:
            - PREFECT_SERVER_API_CSRF_TOKEN_EXPIRATION
            - PREFECT_SERVER_CSRF_TOKEN_EXPIRATION
        cors_allowed_origins:
          type: string
          title: Cors Allowed Origins
          description: |2-

                    A comma-separated list of origins that are authorized to make cross-origin requests to the API.

                    By default, this is set to `*`, which allows requests from all origins.
                    
          default: '*'
          supported_environment_variables:
            - PREFECT_SERVER_API_CORS_ALLOWED_ORIGINS
            - PREFECT_SERVER_CORS_ALLOWED_ORIGINS
        cors_allowed_methods:
          type: string
          title: Cors Allowed Methods
          description: |2-

                    A comma-separated list of methods that are authorized to make cross-origin requests to the API.

                    By default, this is set to `*`, which allows requests from all methods.
                    
          default: '*'
          supported_environment_variables:
            - PREFECT_SERVER_API_CORS_ALLOWED_METHODS
            - PREFECT_SERVER_CORS_ALLOWED_METHODS
        cors_allowed_headers:
          type: string
          title: Cors Allowed Headers
          description: |2-

                    A comma-separated list of headers that are authorized to make cross-origin requests to the API.

                    By default, this is set to `*`, which allows requests from all headers.
                    
          default: '*'
          supported_environment_variables:
            - PREFECT_SERVER_API_CORS_ALLOWED_HEADERS
            - PREFECT_SERVER_CORS_ALLOWED_HEADERS
      type: object
      title: ServerAPISettings
      description: Settings for controlling API server behavior
    ServerConcurrencySettings:
      properties:
        lease_storage:
          type: string
          title: Lease Storage
          description: The module to use for storing concurrency limit leases.
          default: prefect.server.concurrency.lease_storage.memory
          supported_environment_variables:
            - PREFECT_SERVER_CONCURRENCY_LEASE_STORAGE
        initial_deployment_lease_duration:
          type: number
          maximum: 3600
          minimum: 30
          title: Initial Deployment Lease Duration
          description: Initial duration for deployment concurrency lease in seconds.
          default: 300
          supported_environment_variables:
            - PREFECT_SERVER_CONCURRENCY_INITIAL_DEPLOYMENT_LEASE_DURATION
        maximum_concurrency_slot_wait_seconds:
          type: number
          minimum: 0
          title: Maximum Concurrency Slot Wait Seconds
          description: >-
            The maximum number of seconds to wait before retrying when a
            concurrency slot cannot be acquired.
          default: 30
          supported_environment_variables:
            - PREFECT_SERVER_CONCURRENCY_MAXIMUM_CONCURRENCY_SLOT_WAIT_SECONDS
      type: object
      title: ServerConcurrencySettings
    ServerDatabaseSettings:
      properties:
        sqlalchemy:
          $ref: '#/components/schemas/SQLAlchemySettings'
          description: Settings for controlling SQLAlchemy behavior
          supported_environment_variables: []
        connection_url:
          anyOf:
            - type: string
              format: password
              writeOnly: true
            - type: 'null'
          title: Connection Url
          description: |2-

                    A database connection URL in a SQLAlchemy-compatible
                    format. Prefect currently supports SQLite and Postgres. Note that all
                    Prefect database engines must use an async driver - for SQLite, use
                    `sqlite+aiosqlite` and for Postgres use `postgresql+asyncpg`.

                    SQLite in-memory databases can be used by providing the url
                    `sqlite+aiosqlite:///file::memory:?cache=shared&uri=true&check_same_thread=false`,
                    which will allow the database to be accessed by multiple threads. Note
                    that in-memory databases can not be accessed from multiple processes and
                    should only be used for simple tests.
                    
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_CONNECTION_URL
            - PREFECT_API_DATABASE_CONNECTION_URL
        driver:
          anyOf:
            - type: string
              enum:
                - postgresql+asyncpg
                - sqlite+aiosqlite
            - type: 'null'
          title: Driver
          description: >-
            The database driver to use when connecting to the database. If not
            set, the driver will be inferred from the connection URL.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_DRIVER
            - PREFECT_API_DATABASE_DRIVER
        host:
          anyOf:
            - type: string
            - type: 'null'
          title: Host
          description: The database server host.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_HOST
            - PREFECT_API_DATABASE_HOST
        port:
          anyOf:
            - type: integer
            - type: 'null'
          title: Port
          description: The database server port.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_PORT
            - PREFECT_API_DATABASE_PORT
        user:
          anyOf:
            - type: string
            - type: 'null'
          title: User
          description: The user to use when connecting to the database.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_USER
            - PREFECT_API_DATABASE_USER
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
          description: >-
            The name of the Prefect database on the remote server, or the path
            to the database file for SQLite.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_NAME
            - PREFECT_API_DATABASE_NAME
        password:
          anyOf:
            - type: string
              format: password
              writeOnly: true
            - type: 'null'
          title: Password
          description: >-
            The password to use when connecting to the database. Should be kept
            secret.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_PASSWORD
            - PREFECT_API_DATABASE_PASSWORD
        echo:
          type: boolean
          title: Echo
          description: >-
            If `True`, SQLAlchemy will log all SQL issued to the database.
            Defaults to `False`.
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_ECHO
            - PREFECT_API_DATABASE_ECHO
        migrate_on_start:
          type: boolean
          title: Migrate On Start
          description: If `True`, the database will be migrated on application startup.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_MIGRATE_ON_START
            - PREFECT_API_DATABASE_MIGRATE_ON_START
        timeout:
          anyOf:
            - type: number
            - type: 'null'
          title: Timeout
          description: >-
            A statement timeout, in seconds, applied to all database
            interactions made by the Prefect backend. Defaults to 10 seconds.
          default: 10
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_TIMEOUT
            - PREFECT_API_DATABASE_TIMEOUT
        connection_timeout:
          anyOf:
            - type: number
            - type: 'null'
          title: Connection Timeout
          description: >-
            A connection timeout, in seconds, applied to database connections.
            Defaults to `5`.
          default: 5
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_CONNECTION_TIMEOUT
            - PREFECT_API_DATABASE_CONNECTION_TIMEOUT
      type: object
      title: ServerDatabaseSettings
      description: Settings for controlling server database behavior
    ServerDeploymentsSettings:
      properties:
        concurrency_slot_wait_seconds:
          type: number
          minimum: 0
          title: Concurrency Slot Wait Seconds
          description: >-
            The number of seconds to wait before retrying when a deployment flow
            run cannot secure a concurrency slot from the server.
          default: 30
          supported_environment_variables:
            - PREFECT_SERVER_DEPLOYMENTS_CONCURRENCY_SLOT_WAIT_SECONDS
            - PREFECT_DEPLOYMENT_CONCURRENCY_SLOT_WAIT_SECONDS
      type: object
      title: ServerDeploymentsSettings
    ServerDocketSettings:
      properties:
        name:
          type: string
          title: Name
          description: The name of the Docket instance.
          default: prefect-server
          supported_environment_variables:
            - PREFECT_SERVER_DOCKET_NAME
        url:
          type: string
          title: Url
          description: The URL of the Redis server to use for Docket.
          default: memory://
          supported_environment_variables:
            - PREFECT_SERVER_DOCKET_URL
      type: object
      title: ServerDocketSettings
      description: Settings for controlling Docket behavior
    ServerEphemeralSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: |2-

                    Controls whether or not a subprocess server can be started when no API URL is provided.
                    
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_EPHEMERAL_ENABLED
            - PREFECT_SERVER_ALLOW_EPHEMERAL_MODE
        startup_timeout_seconds:
          type: integer
          title: Startup Timeout Seconds
          description: |2-

                    The number of seconds to wait for the server to start when ephemeral mode is enabled.
                    Defaults to `20`.
                    
          default: 20
          supported_environment_variables:
            - PREFECT_SERVER_EPHEMERAL_STARTUP_TIMEOUT_SECONDS
      type: object
      title: ServerEphemeralSettings
      description: Settings for controlling ephemeral server behavior
    ServerEventsSettings:
      properties:
        stream_out_enabled:
          type: boolean
          title: Stream Out Enabled
          description: Whether or not to stream events out to the API via websockets.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_STREAM_OUT_ENABLED
            - PREFECT_API_EVENTS_STREAM_OUT_ENABLED
        related_resource_cache_ttl:
          type: string
          format: duration
          title: Related Resource Cache Ttl
          description: The number of seconds to cache related resources for in the API.
          default: PT5M
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_RELATED_RESOURCE_CACHE_TTL
            - PREFECT_API_EVENTS_RELATED_RESOURCE_CACHE_TTL
        maximum_labels_per_resource:
          type: integer
          title: Maximum Labels Per Resource
          description: The maximum number of labels a resource may have.
          default: 500
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_MAXIMUM_LABELS_PER_RESOURCE
            - PREFECT_EVENTS_MAXIMUM_LABELS_PER_RESOURCE
        maximum_related_resources:
          type: integer
          title: Maximum Related Resources
          description: The maximum number of related resources an Event may have.
          default: 100
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_MAXIMUM_RELATED_RESOURCES
            - PREFECT_EVENTS_MAXIMUM_RELATED_RESOURCES
        maximum_size_bytes:
          type: integer
          title: Maximum Size Bytes
          description: The maximum size of an Event when serialized to JSON
          default: 1500000
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_MAXIMUM_SIZE_BYTES
            - PREFECT_EVENTS_MAXIMUM_SIZE_BYTES
        expired_bucket_buffer:
          type: string
          format: duration
          title: Expired Bucket Buffer
          description: The amount of time to retain expired automation buckets
          default: PT1M
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_EXPIRED_BUCKET_BUFFER
            - PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER
        proactive_granularity:
          type: string
          format: duration
          title: Proactive Granularity
          description: How frequently proactive automations are evaluated
          default: PT5S
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_PROACTIVE_GRANULARITY
            - PREFECT_EVENTS_PROACTIVE_GRANULARITY
        retention_period:
          type: string
          format: duration
          title: Retention Period
          description: The amount of time to retain events in the database.
          default: P7D
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_RETENTION_PERIOD
            - PREFECT_EVENTS_RETENTION_PERIOD
        maximum_websocket_backfill:
          type: string
          format: duration
          title: Maximum Websocket Backfill
          description: >-
            The maximum range to look back for backfilling events for a
            websocket subscriber.
          default: PT15M
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_MAXIMUM_WEBSOCKET_BACKFILL
            - PREFECT_EVENTS_MAXIMUM_WEBSOCKET_BACKFILL
        websocket_backfill_page_size:
          type: integer
          exclusiveMinimum: 0
          title: Websocket Backfill Page Size
          description: >-
            The page size for the queries to backfill events for websocket
            subscribers.
          default: 250
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_WEBSOCKET_BACKFILL_PAGE_SIZE
            - PREFECT_EVENTS_WEBSOCKET_BACKFILL_PAGE_SIZE
        messaging_broker:
          type: string
          title: Messaging Broker
          description: >-
            Which message broker implementation to use for the messaging system,
            should point to a module that exports a Publisher and Consumer
            class.
          default: prefect.server.utilities.messaging.memory
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_MESSAGING_BROKER
            - PREFECT_MESSAGING_BROKER
        messaging_cache:
          type: string
          title: Messaging Cache
          description: >-
            Which cache implementation to use for the events system. Should
            point to a module that exports a Cache class.
          default: prefect.server.utilities.messaging.memory
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_MESSAGING_CACHE
            - PREFECT_MESSAGING_CACHE
        causal_ordering:
          type: string
          title: Causal Ordering
          description: >-
            Which causal ordering implementation to use for the events system.
            Should point to a module that exports a CausalOrdering class.
          default: prefect.server.events.ordering.memory
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_CAUSAL_ORDERING
        maximum_event_name_length:
          type: integer
          exclusiveMinimum: 0
          title: Maximum Event Name Length
          description: The maximum length of an event name.
          default: 1024
          supported_environment_variables:
            - PREFECT_SERVER_EVENTS_MAXIMUM_EVENT_NAME_LENGTH
      type: object
      title: ServerEventsSettings
      description: Settings for controlling behavior of the events subsystem
    ServerFlowRunGraphSettings:
      properties:
        max_nodes:
          type: integer
          title: Max Nodes
          description: The maximum size of a flow run graph on the v2 API
          default: 10000
          supported_environment_variables:
            - PREFECT_SERVER_FLOW_RUN_GRAPH_MAX_NODES
            - PREFECT_API_MAX_FLOW_RUN_GRAPH_NODES
        max_artifacts:
          type: integer
          title: Max Artifacts
          description: >-
            The maximum number of artifacts to show on a flow run graph on the
            v2 API
          default: 10000
          supported_environment_variables:
            - PREFECT_SERVER_FLOW_RUN_GRAPH_MAX_ARTIFACTS
            - PREFECT_API_MAX_FLOW_RUN_GRAPH_ARTIFACTS
      type: object
      title: ServerFlowRunGraphSettings
      description: Settings for controlling behavior of the flow run graph
    ServerLogsSettings:
      properties:
        stream_out_enabled:
          type: boolean
          title: Stream Out Enabled
          description: Whether or not to stream logs out to the API via websockets.
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_LOGS_STREAM_OUT_ENABLED
        stream_publishing_enabled:
          type: boolean
          title: Stream Publishing Enabled
          description: Whether or not to publish logs to the streaming system.
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_LOGS_STREAM_PUBLISHING_ENABLED
      type: object
      title: ServerLogsSettings
      description: Settings for controlling behavior of the logs subsystem
    ServerServicesSettings:
      properties:
        cancellation_cleanup:
          $ref: '#/components/schemas/ServerServicesCancellationCleanupSettings'
          supported_environment_variables: []
        db_vacuum:
          $ref: '#/components/schemas/ServerServicesDBVacuumSettings'
          supported_environment_variables: []
        event_persister:
          $ref: '#/components/schemas/ServerServicesEventPersisterSettings'
          supported_environment_variables: []
        event_logger:
          $ref: '#/components/schemas/ServerServicesEventLoggerSettings'
          supported_environment_variables: []
        foreman:
          $ref: '#/components/schemas/ServerServicesForemanSettings'
          supported_environment_variables: []
        late_runs:
          $ref: '#/components/schemas/ServerServicesLateRunsSettings'
          supported_environment_variables: []
        scheduler:
          $ref: '#/components/schemas/ServerServicesSchedulerSettings'
          supported_environment_variables: []
        pause_expirations:
          $ref: '#/components/schemas/ServerServicesPauseExpirationsSettings'
          supported_environment_variables: []
        repossessor:
          $ref: '#/components/schemas/ServerServicesRepossessorSettings'
          supported_environment_variables: []
        task_run_recorder:
          $ref: '#/components/schemas/ServerServicesTaskRunRecorderSettings'
          supported_environment_variables: []
        triggers:
          $ref: '#/components/schemas/ServerServicesTriggersSettings'
          supported_environment_variables: []
      type: object
      title: ServerServicesSettings
      description: Settings for controlling server services
    ServerTasksSettings:
      properties:
        tag_concurrency_slot_wait_seconds:
          type: number
          minimum: 0
          title: Tag Concurrency Slot Wait Seconds
          description: >-
            The number of seconds to wait before retrying when a task run cannot
            secure a concurrency slot from the server.
          default: 30
          supported_environment_variables:
            - PREFECT_SERVER_TASKS_TAG_CONCURRENCY_SLOT_WAIT_SECONDS
            - PREFECT_TASK_RUN_TAG_CONCURRENCY_SLOT_WAIT_SECONDS
        max_cache_key_length:
          type: integer
          title: Max Cache Key Length
          description: The maximum number of characters allowed for a task run cache key.
          default: 2000
          supported_environment_variables:
            - PREFECT_SERVER_TASKS_MAX_CACHE_KEY_LENGTH
            - PREFECT_API_TASK_CACHE_KEY_MAX_LENGTH
        scheduling:
          $ref: '#/components/schemas/ServerTasksSchedulingSettings'
          supported_environment_variables: []
      type: object
      title: ServerTasksSettings
      description: Settings for controlling server-side behavior related to tasks
    ServerUISettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: Whether or not to serve the Prefect UI.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_UI_ENABLED
            - PREFECT_UI_ENABLED
        v2_enabled:
          type: boolean
          title: V2 Enabled
          description: >-
            Whether to serve the experimental V2 UI instead of the default V1
            UI.
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_UI_V2_ENABLED
        api_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Api Url
          description: >-
            The connection url for communication from the UI to the API.
            Defaults to `PREFECT_API_URL` if set. Otherwise, the default URL is
            generated from `PREFECT_SERVER_API_HOST` and
            `PREFECT_SERVER_API_PORT`.
          supported_environment_variables:
            - PREFECT_SERVER_UI_API_URL
            - PREFECT_UI_API_URL
        serve_base:
          type: string
          title: Serve Base
          description: The base URL path to serve the Prefect UI from.
          default: /
          supported_environment_variables:
            - PREFECT_SERVER_UI_SERVE_BASE
            - PREFECT_UI_SERVE_BASE
        static_directory:
          anyOf:
            - type: string
            - type: 'null'
          title: Static Directory
          description: >-
            The directory to serve static files from. This should be used when
            running into permissions issues when attempting to serve the UI from
            the default directory (for example when running in a Docker
            container).
          supported_environment_variables:
            - PREFECT_SERVER_UI_STATIC_DIRECTORY
            - PREFECT_UI_STATIC_DIRECTORY
        show_promotional_content:
          type: boolean
          title: Show Promotional Content
          description: >-
            Whether or not to display promotional content in the UI, including
            upgrade prompts and marketing banners.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_UI_SHOW_PROMOTIONAL_CONTENT
      type: object
      title: ServerUISettings
    TasksRunnerSettings:
      properties:
        thread_pool_max_workers:
          anyOf:
            - type: integer
              exclusiveMinimum: 0
            - type: 'null'
          title: Thread Pool Max Workers
          description: The maximum number of workers for ThreadPoolTaskRunner.
          supported_environment_variables:
            - PREFECT_TASKS_RUNNER_THREAD_POOL_MAX_WORKERS
            - PREFECT_TASK_RUNNER_THREAD_POOL_MAX_WORKERS
        process_pool_max_workers:
          anyOf:
            - type: integer
              exclusiveMinimum: 0
            - type: 'null'
          title: Process Pool Max Workers
          description: The maximum number of workers for ProcessPoolTaskRunner.
          supported_environment_variables:
            - PREFECT_TASKS_RUNNER_PROCESS_POOL_MAX_WORKERS
      type: object
      title: TasksRunnerSettings
    TasksSchedulingSettings:
      properties:
        default_storage_block:
          anyOf:
            - type: string
            - type: 'null'
          title: Default Storage Block
          description: >-
            The `block-type/block-document` slug of a block to use as the
            default storage for autonomous tasks.
          supported_environment_variables:
            - PREFECT_TASKS_SCHEDULING_DEFAULT_STORAGE_BLOCK
            - PREFECT_TASK_SCHEDULING_DEFAULT_STORAGE_BLOCK
        delete_failed_submissions:
          type: boolean
          title: Delete Failed Submissions
          description: Whether or not to delete failed task submissions from the database.
          default: true
          supported_environment_variables:
            - PREFECT_TASKS_SCHEDULING_DELETE_FAILED_SUBMISSIONS
            - PREFECT_TASK_SCHEDULING_DELETE_FAILED_SUBMISSIONS
      type: object
      title: TasksSchedulingSettings
    WorkerWebserverSettings:
      properties:
        host:
          type: string
          title: Host
          description: The host address the worker's webserver should bind to.
          default: 0.0.0.0
          supported_environment_variables:
            - PREFECT_WORKER_WEBSERVER_HOST
        port:
          type: integer
          title: Port
          description: The port the worker's webserver should bind to.
          default: 8080
          supported_environment_variables:
            - PREFECT_WORKER_WEBSERVER_PORT
      type: object
      title: WorkerWebserverSettings
    SQLAlchemySettings:
      properties:
        connect_args:
          $ref: '#/components/schemas/SQLAlchemyConnectArgsSettings'
          description: Settings for controlling SQLAlchemy connection behavior
          supported_environment_variables: []
        pool_size:
          type: integer
          title: Pool Size
          description: >-
            Controls connection pool size of database connection pools from the
            Prefect backend.
          default: 5
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_POOL_SIZE
            - PREFECT_SQLALCHEMY_POOL_SIZE
        pool_recycle:
          type: integer
          title: Pool Recycle
          description: >-
            This setting causes the pool to recycle connections after the given
            number of seconds has passed; set it to -1 to avoid recycling
            entirely.
          default: 3600
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_POOL_RECYCLE
        pool_timeout:
          anyOf:
            - type: number
            - type: 'null'
          title: Pool Timeout
          description: >-
            Number of seconds to wait before giving up on getting a connection
            from the pool. Defaults to 30 seconds.
          default: 30
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_POOL_TIMEOUT
        max_overflow:
          type: integer
          title: Max Overflow
          description: >-
            Controls maximum overflow of the connection pool. To prevent
            overflow, set to -1.
          default: 10
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_MAX_OVERFLOW
            - PREFECT_SQLALCHEMY_MAX_OVERFLOW
      type: object
      title: SQLAlchemySettings
      description: >-
        Settings for controlling SQLAlchemy behavior; note that these settings
        only take effect when

        using a PostgreSQL database.
    ServerServicesCancellationCleanupSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Whether or not to start the cancellation cleanup service in the
            server application.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_CANCELLATION_CLEANUP_ENABLED
            - PREFECT_API_SERVICES_CANCELLATION_CLEANUP_ENABLED
        loop_seconds:
          type: number
          title: Loop Seconds
          description: >-
            The cancellation cleanup service will look for non-terminal tasks
            and subflows this often. Defaults to `20`.
          default: 20
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_CANCELLATION_CLEANUP_LOOP_SECONDS
            - PREFECT_API_SERVICES_CANCELLATION_CLEANUP_LOOP_SECONDS
      type: object
      title: ServerServicesCancellationCleanupSettings
      description: Settings for controlling the cancellation cleanup service
    ServerServicesDBVacuumSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Whether or not to start the database vacuum service in the server
            application. Disabled by default because it permanently deletes
            data.
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_DB_VACUUM_ENABLED
        loop_seconds:
          type: number
          exclusiveMinimum: 0
          title: Loop Seconds
          description: >-
            The database vacuum service will run this often, in seconds.
            Defaults to `3600` (1 hour).
          default: 3600
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_DB_VACUUM_LOOP_SECONDS
        retention_period:
          type: string
          format: duration
          title: Retention Period
          description: >-
            How old a flow run must be (based on end_time) before it is eligible
            for deletion. Accepts seconds. Minimum 1 hour. Defaults to 90 days.
          default: P90D
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_DB_VACUUM_RETENTION_PERIOD
        batch_size:
          type: integer
          exclusiveMinimum: 0
          title: Batch Size
          description: >-
            The number of records to delete per database transaction. Defaults
            to `200`.
          default: 200
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_DB_VACUUM_BATCH_SIZE
      type: object
      title: ServerServicesDBVacuumSettings
      description: Settings for controlling the database vacuum service
    ServerServicesEventPersisterSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Whether or not to start the event persister service in the server
            application.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_EVENT_PERSISTER_ENABLED
            - PREFECT_API_SERVICES_EVENT_PERSISTER_ENABLED
        batch_size:
          type: integer
          exclusiveMinimum: 0
          title: Batch Size
          description: >-
            The number of events the event persister will attempt to insert in
            one batch.
          default: 20
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_EVENT_PERSISTER_BATCH_SIZE
            - PREFECT_API_SERVICES_EVENT_PERSISTER_BATCH_SIZE
        read_batch_size:
          type: integer
          exclusiveMinimum: 0
          title: Read Batch Size
          description: >-
            The number of events the event persister will attempt to read from
            the message broker in one batch.
          default: 1
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_EVENT_PERSISTER_READ_BATCH_SIZE
            - PREFECT_API_SERVICES_EVENT_PERSISTER_READ_BATCH_SIZE
        flush_interval:
          type: number
          exclusiveMinimum: 0
          title: Flush Interval
          description: >-
            The maximum number of seconds between flushes of the event
            persister.
          default: 5
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_EVENT_PERSISTER_FLUSH_INTERVAL
            - PREFECT_API_SERVICES_EVENT_PERSISTER_FLUSH_INTERVAL
        batch_size_delete:
          type: integer
          exclusiveMinimum: 0
          title: Batch Size Delete
          description: >-
            The number of expired events and event resources the event persister
            will attempt to delete in one batch.
          default: 10000
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_EVENT_PERSISTER_BATCH_SIZE_DELETE
        queue_max_size:
          type: integer
          exclusiveMinimum: 0
          title: Queue Max Size
          description: >-
            The maximum number of events that can be queued in memory for
            persistence. When the queue is full, new events will be dropped.
          default: 50000
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_EVENT_PERSISTER_QUEUE_MAX_SIZE
        max_flush_retries:
          type: integer
          exclusiveMinimum: 0
          title: Max Flush Retries
          description: >-
            The maximum number of consecutive flush failures before events are
            dropped instead of being re-queued.
          default: 5
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_EVENT_PERSISTER_MAX_FLUSH_RETRIES
      type: object
      title: ServerServicesEventPersisterSettings
      description: Settings for controlling the event persister service
    ServerServicesEventLoggerSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Whether or not to start the event logger service in the server
            application.
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_EVENT_LOGGER_ENABLED
            - PREFECT_API_SERVICES_EVENT_LOGGER_ENABLED
      type: object
      title: ServerServicesEventLoggerSettings
      description: Settings for controlling the event logger service
    ServerServicesForemanSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Whether or not to start the foreman service in the server
            application.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_FOREMAN_ENABLED
            - PREFECT_API_SERVICES_FOREMAN_ENABLED
        loop_seconds:
          type: number
          title: Loop Seconds
          description: >-
            The foreman service will check for offline workers this often.
            Defaults to `15`.
          default: 15
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_FOREMAN_LOOP_SECONDS
            - PREFECT_API_SERVICES_FOREMAN_LOOP_SECONDS
        inactivity_heartbeat_multiple:
          type: integer
          title: Inactivity Heartbeat Multiple
          description: |2-

                    The number of heartbeats that must be missed before a worker is marked as offline. Defaults to `3`.
                    
          default: 3
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_FOREMAN_INACTIVITY_HEARTBEAT_MULTIPLE
            - PREFECT_API_SERVICES_FOREMAN_INACTIVITY_HEARTBEAT_MULTIPLE
        fallback_heartbeat_interval_seconds:
          type: integer
          title: Fallback Heartbeat Interval Seconds
          description: |2-

                    The number of seconds to use for online/offline evaluation if a worker's heartbeat
                    interval is not set. Defaults to `30`.
                    
          default: 30
          supported_environment_variables:
            - >-
              PREFECT_SERVER_SERVICES_FOREMAN_FALLBACK_HEARTBEAT_INTERVAL_SECONDS
            - PREFECT_API_SERVICES_FOREMAN_FALLBACK_HEARTBEAT_INTERVAL_SECONDS
        deployment_last_polled_timeout_seconds:
          type: integer
          title: Deployment Last Polled Timeout Seconds
          description: |2-

                    The number of seconds before a deployment is marked as not ready if it has not been
                    polled. Defaults to `60`.
                    
          default: 60
          supported_environment_variables:
            - >-
              PREFECT_SERVER_SERVICES_FOREMAN_DEPLOYMENT_LAST_POLLED_TIMEOUT_SECONDS
            - >-
              PREFECT_API_SERVICES_FOREMAN_DEPLOYMENT_LAST_POLLED_TIMEOUT_SECONDS
        work_queue_last_polled_timeout_seconds:
          type: integer
          title: Work Queue Last Polled Timeout Seconds
          description: |2-

                    The number of seconds before a work queue is marked as not ready if it has not been
                    polled. Defaults to `60`.
                    
          default: 60
          supported_environment_variables:
            - >-
              PREFECT_SERVER_SERVICES_FOREMAN_WORK_QUEUE_LAST_POLLED_TIMEOUT_SECONDS
            - >-
              PREFECT_API_SERVICES_FOREMAN_WORK_QUEUE_LAST_POLLED_TIMEOUT_SECONDS
      type: object
      title: ServerServicesForemanSettings
      description: Settings for controlling the foreman service
    ServerServicesLateRunsSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Whether or not to start the late runs service in the server
            application.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_LATE_RUNS_ENABLED
            - PREFECT_API_SERVICES_LATE_RUNS_ENABLED
        loop_seconds:
          type: number
          title: Loop Seconds
          description: |2-

                    The late runs service will look for runs to mark as late this often. Defaults to `5`.
                    
          default: 5
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_LATE_RUNS_LOOP_SECONDS
            - PREFECT_API_SERVICES_LATE_RUNS_LOOP_SECONDS
        after_seconds:
          type: string
          format: duration
          title: After Seconds
          description: |2-

                    The late runs service will mark runs as late after they have exceeded their scheduled start time by this many seconds. Defaults to `5` seconds.
                    
          default: PT15S
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_LATE_RUNS_AFTER_SECONDS
            - PREFECT_API_SERVICES_LATE_RUNS_AFTER_SECONDS
      type: object
      title: ServerServicesLateRunsSettings
      description: Settings for controlling the late runs service
    ServerServicesSchedulerSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Whether or not to start the scheduler service in the server
            application.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_SCHEDULER_ENABLED
            - PREFECT_API_SERVICES_SCHEDULER_ENABLED
        loop_seconds:
          type: number
          title: Loop Seconds
          description: |2-

                    The scheduler loop interval, in seconds. This determines
                    how often the scheduler will attempt to schedule new flow runs, but has no
                    impact on how quickly either flow runs or task runs are actually executed.
                    Defaults to `60`.
                    
          default: 60
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_SCHEDULER_LOOP_SECONDS
            - PREFECT_API_SERVICES_SCHEDULER_LOOP_SECONDS
        deployment_batch_size:
          type: integer
          title: Deployment Batch Size
          description: |2-

                    The number of deployments the scheduler will attempt to
                    schedule in a single batch. If there are more deployments than the batch
                    size, the scheduler immediately attempts to schedule the next batch; it
                    does not sleep for `scheduler_loop_seconds` until it has visited every
                    deployment once. Defaults to `100`.
                    
          default: 100
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_SCHEDULER_DEPLOYMENT_BATCH_SIZE
            - PREFECT_API_SERVICES_SCHEDULER_DEPLOYMENT_BATCH_SIZE
        max_runs:
          type: integer
          title: Max Runs
          description: |2-

                    The scheduler will attempt to schedule up to this many
                    auto-scheduled runs in the future. Note that runs may have fewer than
                    this many scheduled runs, depending on the value of
                    `scheduler_max_scheduled_time`.  Defaults to `100`.
                    
          default: 100
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_SCHEDULER_MAX_RUNS
            - PREFECT_API_SERVICES_SCHEDULER_MAX_RUNS
        min_runs:
          type: integer
          title: Min Runs
          description: |2-

                    The scheduler will attempt to schedule at least this many
                    auto-scheduled runs in the future. Note that runs may have more than
                    this many scheduled runs, depending on the value of
                    `scheduler_min_scheduled_time`.  Defaults to `3`.
                    
          default: 3
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_SCHEDULER_MIN_RUNS
            - PREFECT_API_SERVICES_SCHEDULER_MIN_RUNS
        max_scheduled_time:
          type: string
          format: duration
          title: Max Scheduled Time
          description: |2-

                    The scheduler will create new runs up to this far in the
                    future. Note that this setting will take precedence over
                    `scheduler_max_runs`: if a flow runs once a month and
                    `scheduler_max_scheduled_time` is three months, then only three runs will be
                    scheduled. Defaults to 100 days (`8640000` seconds).
                    
          default: P100D
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_SCHEDULER_MAX_SCHEDULED_TIME
            - PREFECT_API_SERVICES_SCHEDULER_MAX_SCHEDULED_TIME
        min_scheduled_time:
          type: string
          format: duration
          title: Min Scheduled Time
          description: |2-

                    The scheduler will create new runs at least this far in the
                    future. Note that this setting will take precedence over `scheduler_min_runs`:
                    if a flow runs every hour and `scheduler_min_scheduled_time` is three hours,
                    then three runs will be scheduled even if `scheduler_min_runs` is 1. Defaults to
                    
          default: PT1H
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_SCHEDULER_MIN_SCHEDULED_TIME
            - PREFECT_API_SERVICES_SCHEDULER_MIN_SCHEDULED_TIME
        insert_batch_size:
          type: integer
          title: Insert Batch Size
          description: |2-

                    The number of runs the scheduler will attempt to insert in a single batch.
                    Defaults to `500`.
                    
          default: 500
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_SCHEDULER_INSERT_BATCH_SIZE
            - PREFECT_API_SERVICES_SCHEDULER_INSERT_BATCH_SIZE
        recent_deployments_loop_seconds:
          type: number
          title: Recent Deployments Loop Seconds
          description: |2-

                    The number of seconds the recent deployments scheduler will wait between checking for recently updated deployments. Defaults to `5`.
                    
          default: 5
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_SCHEDULER_RECENT_DEPLOYMENTS_LOOP_SECONDS
      type: object
      title: ServerServicesSchedulerSettings
      description: Settings for controlling the scheduler service
    ServerServicesPauseExpirationsSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: |2-

                    Whether or not to start the paused flow run expiration service in the server
                    application. If disabled, paused flows that have timed out will remain in a Paused state
                    until a resume attempt.
                    
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_PAUSE_EXPIRATIONS_ENABLED
            - PREFECT_API_SERVICES_PAUSE_EXPIRATIONS_ENABLED
        loop_seconds:
          type: number
          title: Loop Seconds
          description: |2-

                    The pause expiration service will look for runs to mark as failed this often. Defaults to `5`.
                    
          default: 5
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_PAUSE_EXPIRATIONS_LOOP_SECONDS
            - PREFECT_API_SERVICES_PAUSE_EXPIRATIONS_LOOP_SECONDS
      type: object
      title: ServerServicesPauseExpirationsSettings
      description: Settings for controlling the pause expiration service
    ServerServicesRepossessorSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Whether or not to start the repossessor service in the server
            application.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_REPOSSESSOR_ENABLED
        loop_seconds:
          type: number
          title: Loop Seconds
          description: >-
            The repossessor service will look for expired leases this often.
            Defaults to `15`.
          default: 15
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_REPOSSESSOR_LOOP_SECONDS
      type: object
      title: ServerServicesRepossessorSettings
      description: Settings for controlling the repossessor service
    ServerServicesTaskRunRecorderSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Whether or not to start the task run recorder service in the server
            application.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_TASK_RUN_RECORDER_ENABLED
            - PREFECT_API_SERVICES_TASK_RUN_RECORDER_ENABLED
        read_batch_size:
          type: integer
          exclusiveMinimum: 0
          title: Read Batch Size
          description: >-
            The number of task runs the task run recorder will attempt to read
            from the message broker in one batch.
          default: 1
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_TASK_RUN_RECORDER_READ_BATCH_SIZE
        batch_size:
          type: integer
          exclusiveMinimum: 0
          title: Batch Size
          description: >-
            The number of task runs the task run recorder will attempt to insert
            in one batch.
          default: 1
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_TASK_RUN_RECORDER_BATCH_SIZE
        flush_interval:
          type: number
          exclusiveMinimum: 0
          title: Flush Interval
          description: >-
            The maximum number of seconds between flushes of the task run
            recorder.
          default: 5
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_TASK_RUN_RECORDER_FLUSH_INTERVAL
      type: object
      title: ServerServicesTaskRunRecorderSettings
      description: Settings for controlling the task run recorder service
    ServerServicesTriggersSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Whether or not to start the triggers service in the server
            application.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_TRIGGERS_ENABLED
            - PREFECT_API_SERVICES_TRIGGERS_ENABLED
        read_batch_size:
          type: integer
          exclusiveMinimum: 0
          title: Read Batch Size
          description: >-
            The number of events the triggers service will attempt to read from
            the message broker in one batch.
          default: 1
          supported_environment_variables:
            - PREFECT_SERVER_SERVICES_TRIGGERS_READ_BATCH_SIZE
        pg_notify_reconnect_interval_seconds:
          type: integer
          title: Pg Notify Reconnect Interval Seconds
          description: |2-

                    The number of seconds to wait before reconnecting to the PostgreSQL NOTIFY/LISTEN 
                    connection after an error. Only used when using PostgreSQL as the database.
                    Defaults to `10`.
                    
          default: 10
          supported_environment_variables:
            - >-
              PREFECT_SERVER_SERVICES_TRIGGERS_PG_NOTIFY_RECONNECT_INTERVAL_SECONDS
        pg_notify_heartbeat_interval_seconds:
          type: integer
          title: Pg Notify Heartbeat Interval Seconds
          description: |2-

                    The number of seconds between heartbeat checks for the PostgreSQL NOTIFY/LISTEN 
                    connection to ensure it's still alive. Only used when using PostgreSQL as the database.
                    Defaults to `5`.
                    
          default: 5
          supported_environment_variables:
            - >-
              PREFECT_SERVER_SERVICES_TRIGGERS_PG_NOTIFY_HEARTBEAT_INTERVAL_SECONDS
      type: object
      title: ServerServicesTriggersSettings
      description: Settings for controlling the triggers service
    ServerTasksSchedulingSettings:
      properties:
        max_scheduled_queue_size:
          type: integer
          title: Max Scheduled Queue Size
          description: The maximum number of scheduled tasks to queue for submission.
          default: 1000
          supported_environment_variables:
            - PREFECT_SERVER_TASKS_SCHEDULING_MAX_SCHEDULED_QUEUE_SIZE
            - PREFECT_TASK_SCHEDULING_MAX_SCHEDULED_QUEUE_SIZE
        max_retry_queue_size:
          type: integer
          title: Max Retry Queue Size
          description: The maximum number of retries to queue for submission.
          default: 100
          supported_environment_variables:
            - PREFECT_SERVER_TASKS_SCHEDULING_MAX_RETRY_QUEUE_SIZE
            - PREFECT_TASK_SCHEDULING_MAX_RETRY_QUEUE_SIZE
        pending_task_timeout:
          type: string
          format: duration
          title: Pending Task Timeout
          description: >-
            How long before a PENDING task are made available to another task
            worker.
          default: PT0S
          supported_environment_variables:
            - PREFECT_SERVER_TASKS_SCHEDULING_PENDING_TASK_TIMEOUT
            - PREFECT_TASK_SCHEDULING_PENDING_TASK_TIMEOUT
      type: object
      title: ServerTasksSchedulingSettings
      description: Settings for controlling server-side behavior related to task scheduling
    SQLAlchemyConnectArgsSettings:
      properties:
        application_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Application Name
          description: >-
            Controls the application_name field for connections opened from the
            connection pool when using a PostgreSQL database with the Prefect
            backend.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_CONNECT_ARGS_APPLICATION_NAME
        search_path:
          anyOf:
            - type: string
            - type: 'null'
          title: Search Path
          description: >-
            PostgreSQL schema name to set in search_path when using a PostgreSQL
            database with the Prefect backend. Note: The public schema should be
            included in the search path (e.g. 'myschema, public') to ensure that
            pg_trgm and other extensions remain available.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_CONNECT_ARGS_SEARCH_PATH
        statement_cache_size:
          anyOf:
            - type: integer
            - type: 'null'
          title: Statement Cache Size
          description: >-
            Controls statement cache size for PostgreSQL connections. Setting
            this to 0 is required when using PgBouncer in transaction mode.
            Defaults to None.
          supported_environment_variables:
            - >-
              PREFECT_SERVER_DATABASE_SQLALCHEMY_CONNECT_ARGS_STATEMENT_CACHE_SIZE
        prepared_statement_cache_size:
          anyOf:
            - type: integer
            - type: 'null'
          title: Prepared Statement Cache Size
          description: >-
            Controls the size of the statement cache for PostgreSQL connections.
            When set to 0, statement caching is disabled. Defaults to None to
            use SQLAlchemy's default behavior.
          supported_environment_variables:
            - >-
              PREFECT_SERVER_DATABASE_SQLALCHEMY_CONNECT_ARGS_PREPARED_STATEMENT_CACHE_SIZE
        tls:
          $ref: '#/components/schemas/SQLAlchemyTLSSettings'
          description: Settings for controlling SQLAlchemy mTLS behavior
          supported_environment_variables: []
      type: object
      title: SQLAlchemyConnectArgsSettings
      description: >-
        Settings for controlling SQLAlchemy connection behavior; note that these
        settings only take effect when

        using a PostgreSQL database.
    SQLAlchemyTLSSettings:
      properties:
        enabled:
          type: boolean
          title: Enabled
          description: >-
            Controls whether connected to mTLS enabled PostgreSQL when using a
            PostgreSQL database with the Prefect backend.
          default: false
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_CONNECT_ARGS_TLS_ENABLED
        ca_file:
          anyOf:
            - type: string
            - type: 'null'
          title: Ca File
          description: >-
            This configuration settings option specifies the path to PostgreSQL
            client certificate authority file.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_CONNECT_ARGS_TLS_CA_FILE
        cert_file:
          anyOf:
            - type: string
            - type: 'null'
          title: Cert File
          description: >-
            This configuration settings option specifies the path to PostgreSQL
            client certificate file.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_CONNECT_ARGS_TLS_CERT_FILE
        key_file:
          anyOf:
            - type: string
            - type: 'null'
          title: Key File
          description: >-
            This configuration settings option specifies the path to PostgreSQL
            client key file.
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_CONNECT_ARGS_TLS_KEY_FILE
        check_hostname:
          type: boolean
          title: Check Hostname
          description: >-
            This configuration settings option specifies whether to verify
            PostgreSQL server hostname.
          default: true
          supported_environment_variables:
            - PREFECT_SERVER_DATABASE_SQLALCHEMY_CONNECT_ARGS_TLS_CHECK_HOSTNAME
      type: object
      title: SQLAlchemyTLSSettings
      description: |-
        Settings for controlling SQLAlchemy mTLS context when
        using a PostgreSQL database.

````

Built with [Mintlify](https://mintlify.com).
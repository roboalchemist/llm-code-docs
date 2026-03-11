# Source: https://tyk.io/docs/api-reference/configuration/retrieve-current-configuration-status.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve current configuration status

> Returns the current configuration status of the system. You can optionally filter for a specific configuration field.

**Example curl commands:**

Get full configuration:

```bash
curl -X GET \
http://localhost:8181/config \
-H 'X-Tyk-Authorization: your-secret-key'
```

Get specific configuration field:

```bash
curl -X GET \
'http://localhost:8181/config?field=storage.host' \
-H 'X-Tyk-Authorization: your-secret-key'
```

## OpenAPI

````yaml swagger/5.8/mdcb-swagger.yml get /config
openapi: 3.0.0
info:
  contact:
    email: support@tyk.io
    name: Tyk Technologies
    url: https://tyk.io/contact
  version: 1.0.0
  title: MDCB Data Planes and Diagnostics API
  description: >
    This API provides operations for monitoring Data Planes connected to MDCB
    and accessing diagnostic data.  It includes endpoints for retrieving
    connected data plane details, performing health checks,  and accessing Go's
    built-in pprof diagnostics for advanced performance profiling.
servers:
  - url: https://{tenant}
    variables:
      tenant:
        default: localhost:8181
        description: Your MDCB host
security:
  - api_key: []
tags:
  - name: Data Planes
    description: Operations related to data plane management and information
  - name: Health
    description: Endpoints for checking system health and status
  - name: Debug
    description: Diagnostic and profiling endpoints
  - name: Configuration
    description: Configuration and environment variable management
paths:
  /config:
    get:
      tags:
        - Configuration
      summary: Retrieve current configuration status
      description: >
        Returns the current configuration status of the system. You can
        optionally filter for a specific configuration field.


        **Example curl commands:**


        Get full configuration:

        ```bash

        curl -X GET \

        http://localhost:8181/config \

        -H 'X-Tyk-Authorization: your-secret-key'

        ```


        Get specific configuration field:

        ```bash

        curl -X GET \

        'http://localhost:8181/config?field=storage.host' \

        -H 'X-Tyk-Authorization: your-secret-key'

        ```
      operationId: configGet
      parameters:
        - in: header
          name: X-Tyk-Authorization
          description: Secret value set in sink.conf
          required: true
          schema:
            type: string
          example: your-secret-key
        - in: query
          name: field
          description: Optional configuration field name to filter by
          required: false
          schema:
            type: string
          example: storage.host
      responses:
        '200':
          description: Successful retrieval of the current configuration.
          content:
            application/json:
              schema:
                type: object
                properties:
                  type:
                    type: string
                    enum:
                      - full
                      - single
                discriminator:
                  propertyName: type
                allOf:
                  - $ref: '#/components/schemas/ConfigStatus'
                  - $ref: '#/components/schemas/EnvVariable'
              examples:
                full_config:
                  summary: Full configuration
                  value:
                    type: full
                    listen_port: 9090
                    healthcheck_port: 8180
                    http_port: 8180
                    enable_http_profiler: false
                    server_options:
                      use_ssl: false
                      certificate:
                        cert_file: ./server.crt
                        key_file: ./server.key
                      min_version: 0
                      ssl_ciphers: null
                      ssl_certificates: null
                    http_server_options:
                      use_ssl: false
                      certificate:
                        cert_file: ''
                        key_file: ''
                      min_version: 0
                      ssl_ciphers: null
                      ssl_certificates: null
                    security:
                      private_certificate_encoding_secret: ''
                      enable_http_secure_endpoints: true
                      secret: ''
                    storage:
                      type: redis
                      host: localhost
                      port: 6379
                      master_name: ''
                      sentinel_password: ''
                      username: ''
                      password: ''
                      database: 0
                      optimisation_max_idle: 0
                      optimisation_max_active: 0
                      enable_cluster: false
                      hosts: null
                      addrs: null
                      redis_use_ssl: false
                      redis_ssl_insecure_skip_verify: false
                      debug: false
                      timeout: 0
                      use_ssl: false
                      ssl_insecure_skip_verify: false
                      ca_file: ''
                      cert_file: ''
                      key_file: ''
                      max_version: ''
                      min_version: ''
                    analytics:
                      type: mongo
                      connection_string: ''
                      table_sharding: false
                      batch_size: 0
                      postgres:
                        prefer_simple_protocol: false
                      mysql:
                        default_string_size: 0
                        disable_datetime_precision: false
                        dont_support_rename_index: false
                        dont_support_rename_column: false
                        skip_initialize_with_version: false
                      mongo_url: ''
                      mongo_use_ssl: false
                      mongo_ssl_insecure_skip_verify: false
                      mongo_ssl_allow_invalid_hostnames: false
                      mongo_ssl_ca_file: ''
                      mongo_ssl_pem_keyfile: ''
                      mongo_session_consistency: ''
                      mongo_batch_size: 0
                      driver: mongo-go
                      mongo_direct_connection: false
                    hash_keys: true
                    session_timeout: 0
                    forward_analytics_to_pump: false
                    enable_multiple_analytics_keys: false
                    dont_store_selective: false
                    dont_store_aggregate: false
                    org_session_expiration: 60
                    org_session_cleanup: 60
                    license: ''
                    aggregates_ignore_tags: null
                    track_all_paths: false
                    store_analytics_per_minute: false
                    ignore_tag_prefix_list: null
                    threshold_len_tag_list: 1000
                    omit_analytics_index_creation: false
                    enable_separate_analytics_store: false
                    analytics_storage:
                      type: ''
                      host: ''
                      port: 0
                      master_name: ''
                      sentinel_password: ''
                      username: ''
                      password: ''
                      database: 0
                      optimisation_max_idle: 0
                      optimisation_max_active: 0
                      enable_cluster: false
                      hosts: null
                      addrs: null
                      redis_use_ssl: false
                      redis_ssl_insecure_skip_verify: false
                      debug: false
                      timeout: 0
                      use_ssl: false
                      ssl_insecure_skip_verify: false
                      ca_file: ''
                      cert_file: ''
                      key_file: ''
                      max_version: ''
                      min_version: ''
                    log_level: info
                    enable_key_logging: false
                    sync_worker_config:
                      enabled: true
                      hash_keys: true
                      max_batch_size: 1000
                      time_between_batches: 3
                      max_workers: 1000
                      warmup_time: 0
                      group_key_ttl: 30
                    enable_ownership: false
                single_field:
                  summary: Single configuration field (filtered by query parameter)
                  value:
                    type: single
                    config_field: sync_worker_config.warmup_time
                    env: TYK_MDCB_SYNCWORKERCONFIG_WARMUPTIME
                    value: '0'
                    obfuscated: false
        '400':
          description: Field not found in configuration.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: field not found
        '401':
          description: Forbidden access due to invalid or missing administrative key.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    ConfigStatus:
      type: object
      properties:
        listen_port:
          type: integer
          example: 9090
        healthcheck_port:
          type: integer
          example: 8180
        http_port:
          type: integer
          example: 8180
        enable_http_profiler:
          type: boolean
          example: false
        server_options:
          type: object
          properties:
            use_ssl:
              type: boolean
              example: false
            certificate:
              type: object
              properties:
                cert_file:
                  type: string
                  example: ./server.crt
                key_file:
                  type: string
                  example: ./server.key
            min_version:
              type: integer
              example: 0
            ssl_ciphers:
              type: string
              nullable: true
            ssl_certificates:
              type: string
              nullable: true
        http_server_options:
          type: object
          properties:
            use_ssl:
              type: boolean
              example: false
            certificate:
              type: object
              properties:
                cert_file:
                  type: string
                  example: ''
                key_file:
                  type: string
                  example: ''
            min_version:
              type: integer
              example: 0
            ssl_ciphers:
              type: string
              nullable: true
            ssl_certificates:
              type: string
              nullable: true
        security:
          type: object
          properties:
            private_certificate_encoding_secret:
              type: string
              example: ''
            enable_http_secure_endpoints:
              type: boolean
              example: true
            secret:
              type: string
              example: ''
        storage:
          type: object
          properties:
            type:
              type: string
              example: redis
            host:
              type: string
              example: localhost
            port:
              type: integer
              example: 6379
            master_name:
              type: string
              example: ''
            sentinel_password:
              type: string
              example: ''
            username:
              type: string
              example: ''
            password:
              type: string
              example: ''
            database:
              type: integer
              example: 0
            optimisation_max_idle:
              type: integer
              example: 0
            optimisation_max_active:
              type: integer
              example: 0
            enable_cluster:
              type: boolean
              example: false
            hosts:
              type: string
              nullable: true
            addrs:
              type: string
              nullable: true
            redis_use_ssl:
              type: boolean
              example: false
            redis_ssl_insecure_skip_verify:
              type: boolean
              example: false
            debug:
              type: boolean
              example: false
            timeout:
              type: integer
              example: 0
            use_ssl:
              type: boolean
              example: false
            ssl_insecure_skip_verify:
              type: boolean
              example: false
            ca_file:
              type: string
              example: ''
            cert_file:
              type: string
              example: ''
            key_file:
              type: string
              example: ''
            max_version:
              type: string
              example: ''
            min_version:
              type: string
              example: ''
        analytics:
          type: object
          properties:
            type:
              type: string
              example: mongo
            connection_string:
              type: string
              example: ''
            table_sharding:
              type: boolean
              example: false
            batch_size:
              type: integer
              example: 0
            postgres:
              type: object
              properties:
                prefer_simple_protocol:
                  type: boolean
                  example: false
            mysql:
              type: object
              properties:
                default_string_size:
                  type: integer
                  example: 0
                disable_datetime_precision:
                  type: boolean
                  example: false
                dont_support_rename_index:
                  type: boolean
                  example: false
                dont_support_rename_column:
                  type: boolean
                  example: false
                skip_initialize_with_version:
                  type: boolean
                  example: false
            mongo_url:
              type: string
              example: ''
            mongo_use_ssl:
              type: boolean
              example: false
            mongo_ssl_insecure_skip_verify:
              type: boolean
              example: false
            mongo_ssl_allow_invalid_hostnames:
              type: boolean
              example: false
            mongo_ssl_ca_file:
              type: string
              example: ''
            mongo_ssl_pem_keyfile:
              type: string
              example: ''
            mongo_session_consistency:
              type: string
              example: ''
            mongo_batch_size:
              type: integer
              example: 0
            driver:
              type: string
              example: mongo-go
            mongo_direct_connection:
              type: boolean
              example: false
        hash_keys:
          type: boolean
          example: true
        session_timeout:
          type: integer
          example: 0
        forward_analytics_to_pump:
          type: boolean
          example: false
        enable_multiple_analytics_keys:
          type: boolean
          example: false
        dont_store_selective:
          type: boolean
          example: false
        dont_store_aggregate:
          type: boolean
          example: false
        org_session_expiration:
          type: integer
          example: 60
        org_session_cleanup:
          type: integer
          example: 60
        license:
          type: string
          example: ''
        aggregates_ignore_tags:
          type: string
          nullable: true
        track_all_paths:
          type: boolean
          example: false
        store_analytics_per_minute:
          type: boolean
          example: false
        ignore_tag_prefix_list:
          type: string
          nullable: true
        threshold_len_tag_list:
          type: integer
          example: 1000
        omit_analytics_index_creation:
          type: boolean
          example: false
        enable_separate_analytics_store:
          type: boolean
          example: false
        analytics_storage:
          type: object
          properties:
            type:
              type: string
              example: ''
            host:
              type: string
              example: ''
            port:
              type: integer
              example: 0
            master_name:
              type: string
              example: ''
            sentinel_password:
              type: string
              example: ''
            username:
              type: string
              example: ''
            password:
              type: string
              example: ''
            database:
              type: integer
              example: 0
            optimisation_max_idle:
              type: integer
              example: 0
            optimisation_max_active:
              type: integer
              example: 0
            enable_cluster:
              type: boolean
              example: false
            hosts:
              type: string
              nullable: true
            addrs:
              type: string
              nullable: true
            redis_use_ssl:
              type: boolean
              example: false
            redis_ssl_insecure_skip_verify:
              type: boolean
              example: false
            debug:
              type: boolean
              example: false
            timeout:
              type: integer
              example: 0
            use_ssl:
              type: boolean
              example: false
            ssl_insecure_skip_verify:
              type: boolean
              example: false
            ca_file:
              type: string
              example: ''
            cert_file:
              type: string
              example: ''
            key_file:
              type: string
              example: ''
            max_version:
              type: string
              example: ''
            min_version:
              type: string
              example: ''
        log_level:
          type: string
          example: info
        enable_key_logging:
          type: boolean
          example: false
        sync_worker_config:
          type: object
          properties:
            enabled:
              type: boolean
              example: true
            hash_keys:
              type: boolean
              example: true
            max_batch_size:
              type: integer
              example: 1000
            time_between_batches:
              type: integer
              example: 3
            max_workers:
              type: integer
              example: 1000
            warmup_time:
              type: integer
              example: 0
            group_key_ttl:
              type: integer
              example: 30
        enable_ownership:
          type: boolean
          example: false
    EnvVariable:
      type: object
      properties:
        config_field:
          type: string
          example: sync_worker_config.warmup_time
        env:
          type: string
          example: TYK_MDCB_SYNCWORKERCONFIG_WARMUPTIME
        value:
          type: string
          example: '0'
        obfuscated:
          type: boolean
          example: false
    Error:
      type: object
      properties:
        error:
          type: string
          example: Attempted administrative access with invalid or missing key!
  securitySchemes:
    api_key:
      in: header
      name: X-Tyk-Authorization
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).

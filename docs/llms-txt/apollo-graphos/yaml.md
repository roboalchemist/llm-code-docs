# Source: https://www.apollographql.com/docs/graphos/routing/configuration/yaml.md

# Router YAML Configuration Reference

This reference covers the YAML configuration file properties for configuring an Apollo Router.

## YAML configuration properties

The router can be configured by a YAML configuration file. This file enables you to declaratively configure various runtime properties of your router's behavior.

At startup, you set the config file for your router by providing its path with the [`--config`](https://www.apollographql.com/docs/graphos/routing/configuration/yaml.md#-c----config) option:

```bash
./router --config router.yaml
```

Enable your text editor to validate the format and content of your router YAML configuration file by [configuring it with the router's configuration schema](https://www.apollographql.com/docs/graphos/routing/configuration/cli#configuration-schema-for-ide-validation).

## Example YAML with all properties

Expand the code block to view an example YAML config file containing all properties.

```yaml
apq:
  enabled: true
  router:
    cache:
      in_memory:
        limit: 1
      redis:
        namespace: example_namespace
        password: example_password
        pool_size: 1
        required_to_start: false
        reset_ttl: true
        timeout: null
        tls:
          certificate_authorities: null
          client_authentication:
            certificate_chain: example_certificate_chain
            key: example_key
        ttl: null
        urls:
          - http://example.com/urls_item
        username: example_username
  subgraph:
    all:
      enabled: false
    subgraphs: {}
authentication:
  connector:
    sources: {}
  router:
    jwt:
      header_name: authorization
      header_value_prefix: Bearer
      ignore_other_prefixes: false
      jwks:
        - algorithms: null
          headers:
            - name: example_name
              value: example_value
          issuer: example_issuer
          poll_interval:
            secs: 60
            nanos: 0
          url: http://service.example.com/url
      on_error: Continue
      sources:
        - name: authorization
          type: header
          value_prefix: Bearer
  subgraph:
    all:
      aws_sig_v4:
        hardcoded:
          access_key_id: example_access_key_id
          assume_role:
            external_id: example_external_id
            role_arn: example_role_arn
            session_name: example_session_name
          region: example_region
          secret_access_key: example_secret_access_key
          service_name: example_service_name
    subgraphs: {}
authorization:
  directives:
    dry_run: false
    enabled: true
    errors:
      log: true
      response: errors
    reject_unauthorized: false
  require_authentication: false
batching:
  enabled: false
  maximum_size: null
  mode: batch_http_link
  subgraph:
    all:
      enabled: false
    subgraphs: {}
connectors:
  debug_extensions: false
  expose_sources_in_context: false
  max_requests_per_operation_per_source: null
  sources: {}
  subgraphs: {}
coprocessor:
  client:
    dns_resolution_strategy: ipv4_only
    experimental_http2: enable
  execution:
    request:
      body: false
      context: false
      headers: false
      method: false
      query_plan: false
      sdl: false
    response:
      body: false
      context: false
      headers: false
      sdl: false
      status_code: false
  router:
    request:
      body: false
      condition:
        eq:
          - false
          - false
      context: false
      headers: false
      method: false
      path: false
      sdl: false
    response:
      body: false
      condition:
        eq:
          - false
          - false
      context: false
      headers: false
      sdl: false
      status_code: false
  subgraph:
    all:
      request:
        body: false
        condition:
          eq:
            - false
            - false
        context: false
        headers: false
        method: false
        service_name: false
        subgraph_request_id: false
        uri: false
      response:
        body: false
        condition:
          eq:
            - false
            - false
        context: false
        headers: false
        service_name: false
        status_code: false
        subgraph_request_id: false
  supergraph:
    request:
      body: false
      condition:
        eq:
          - false
          - false
      context: false
      headers: false
      method: false
      sdl: false
    response:
      body: false
      condition:
        eq:
          - false
          - false
      context: false
      headers: false
      sdl: false
      status_code: false
  timeout:
    secs: 1
    nanos: 0
  url: http://service.example.com/url
cors:
  allow_any_origin: false
  allow_credentials: false
  allow_headers: []
  expose_headers: null
  match_origins: null
  max_age: null
  methods:
    - GET
    - POST
    - OPTIONS
  policies:
    - origins: [https://studio.apollographql.com]
csrf:
  required_headers:
    - x-apollo-operation-name
    - apollo-require-preflight
  unsafe_disabled: false
demand_control:
  enabled: false
  mode: measure
  strategy:
    static_estimated:
      list_size: 0
      max: 0.0
      actual_cost_mode: by_subgraph
experimental_chaos:
  force_reload: null
experimental_hoist_orphan_errors:
  all:
    enabled: false
  subgraphs: {}
experimental_type_conditioned_fetching: false
fleet_detector: {}
forbid_mutations: false
headers:
  all:
    request:
      - insert:
          name: example_name
          value: example_value
  subgraphs: {}
health_check:
  enabled: true
  listen: example_listen
  path: /health
  readiness:
    allowed: 100
    interval:
      sampling: 0s
      unready: null
homepage:
  enabled: true
  graph_ref: null
include_subgraph_errors:
  all: false
  subgraphs: {}
license_enforcement: {}
limits:
  http1_max_request_buf_size: null
  http1_max_request_headers: null
  http_max_request_bytes: 2000000
  introspection_max_depth: true
  max_aliases: null
  max_depth: null
  max_height: null
  max_root_fields: null
  parser_max_recursion: 500
  parser_max_tokens: 15000
  warn_only: false
override_subgraph_url: {}
persisted_queries:
  enabled: false
  experimental_prewarm_query_plan_cache:
    on_reload: true
    on_startup: false
  hot_reload: false
  local_manifests: null
  log_unknown: false
  safelist:
    enabled: false
    require_id: false
plugins: unknown_type_plugins
preview_entity_cache:
  enabled: false
  expose_keys_in_context: false
  invalidation:
    concurrent_requests: 10
    listen: example_listen
    path: example_path
    scan_count: 1000
  metrics:
    enabled: false
    separate_per_type: false
    ttl: 30s
  subgraph:
    all:
      enabled: true
      invalidation:
        enabled: false
        shared_key: ""
      private_id: null
      redis:
        namespace: example_namespace
        password: example_password
        pool_size: 1
        required_to_start: false
        reset_ttl: true
        timeout: null
        tls:
          certificate_authorities: null
          client_authentication:
            certificate_chain: example_certificate_chain
            key: example_key
        ttl: null
        urls:
          - http://example.com/urls_item
        username: example_username
      ttl: 30s
    subgraphs: {}
preview_file_uploads:
  enabled: false
  protocols:
    multipart:
      enabled: true
      limits:
        max_file_size: example_max_file_size
        max_files: 0
      mode: stream
progressive_override: {}
rhai:
  main: example_main
  scripts: example_scripts
sandbox:
  enabled: false
subscription:
  enable_deduplication: true
  enabled: true
  max_opened_subscriptions: null
  mode:
    callback:
      heartbeat_interval: disabled
      listen: example_listen
      path: example_path
      public_url: http://service.example.com/public_url
      subgraphs: []
    passthrough:
      all:
        heartbeat_interval: disabled
        path: null
        protocol: graphql_ws
      subgraphs: {}
  queue_capacity: null
supergraph:
  defer_support: true
  early_cancel: false
  experimental_log_on_broken_pipe: false
  generate_query_fragments: true
  introspection: false
  listen: example_listen
  path: /
  redact_query_validation_errors: false
  query_planning:
    cache:
      in_memory:
        limit: 1
      redis:
        namespace: example_namespace
        password: example_password
        pool_size: 1
        required_to_start: false
        reset_ttl: true
        timeout: null
        tls:
          certificate_authorities: null
          client_authentication:
            certificate_chain: example_certificate_chain
            key: example_key
        ttl:
          secs: 2592000
          nanos: 0
        urls:
          - http://example.com/urls_item
        username: example_username
    experimental_paths_limit: null
    experimental_plans_limit: null
    experimental_reuse_query_plans: false
    warmed_up_queries: null
  strict_variable_validation: enforce
telemetry:
  apollo:
    batch_processor:
      max_concurrent_exports: 1
      max_export_batch_size: 512
      max_export_timeout:
        secs: 30
        nanos: 0
      max_queue_size: 2048
      scheduled_delay:
        secs: 5
        nanos: 0
    buffer_size: 10000
    client_name_header: apollographql-client-name
    client_version_header: apollographql-client-version
    endpoint: https://usage-reporting.api.apollographql.com/api/ingress/traces
    errors:
      preview_extended_error_metrics: disabled
      subgraph:
        all:
          redact: true
          redaction_policy: strict
          send: true
        subgraphs: {}
    experimental_local_field_metrics: false
    experimental_otlp_endpoint: https://usage-reporting.api.apollographql.com/
    experimental_otlp_tracing_protocol: grpc
    field_level_instrumentation_sampler: 0.0
    metrics_reference_mode: extended
    otlp_tracing_sampler: 0.0
    send_headers:
      only:
        - example_only_item
    send_variable_values:
      only:
        - example_only_item
    signature_normalization_algorithm: legacy
  exporters:
    logging:
      common:
        resource: {}
        service_name: null
        service_namespace: null
      stdout:
        enabled: true
        format:
          json:
            display_current_span: false
            display_filename: false
            display_level: true
            display_line_number: false
            display_resource: true
            display_span_id: true
            display_span_list: true
            display_target: true
            display_thread_id: false
            display_thread_name: false
            display_timestamp: true
            display_trace_id: hexadecimal
            span_attributes: []
        rate_limit:
          capacity: 1
          enabled: false
          interval:
            secs: 1
            nanos: 0
        tty_format:
          json:
            display_current_span: false
            display_filename: false
            display_level: true
            display_line_number: false
            display_resource: true
            display_span_id: true
            display_span_list: true
            display_target: true
            display_thread_id: false
            display_thread_name: false
            display_timestamp: true
            display_trace_id: hexadecimal
            span_attributes: []
    metrics:
      common:
        buckets:
          - 0.001
          - 0.005
          - 0.015
          - 0.05
          - 0.1
          - 0.2
          - 0.3
          - 0.4
          - 0.5
          - 1.0
          - 5.0
          - 10.0
        resource: {}
        service_name: null
        service_namespace: null
        views:
          - aggregation:
              histogram:
                buckets:
                  - 0.0
            allowed_attribute_keys:
              - example_allowed_attribute_keys_item
            description: example_description
            name: example_name
            unit: example_unit
      otlp:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            secs: 30
            nanos: 0
          max_queue_size: 2048
          scheduled_delay:
            secs: 5
            nanos: 0
        enabled: false
        endpoint: example_endpoint
        grpc:
          ca: null
          cert: null
          domain_name: null
          key: null
          metadata: {}
        http:
          headers: {}
        protocol: grpc
        temporality: cumulative
      prometheus:
        enabled: false
        listen: example_listen
        path: /metrics
    tracing:
      common:
        max_attributes_per_event: 128
        max_attributes_per_link: 128
        max_attributes_per_span: 128
        max_events_per_span: 128
        max_links_per_span: 128
        parent_based_sampler: true
        preview_datadog_agent_sampling: null
        resource: {}
        sampler: 0.0
        service_name: null
        service_namespace: null
      datadog:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            secs: 30
            nanos: 0
          max_queue_size: 2048
          scheduled_delay:
            secs: 5
            nanos: 0
        enable_span_mapping: true
        enabled: false
        endpoint: example_endpoint
        fixed_span_names: true
        resource_mapping: {}
        span_metrics:
          parse_query: true
          connect: true
          execution: true
          http_request: true
          request: true
          query_planning: true
          connect_request: true
          subgraph: true
          router: true
          supergraph: true
          subgraph_request: true
      experimental_response_trace_id:
        enabled: false
        format: hexadecimal
        header_name: example_header_name
      otlp:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            secs: 30
            nanos: 0
          max_queue_size: 2048
          scheduled_delay:
            secs: 5
            nanos: 0
        enabled: false
        endpoint: example_endpoint
        grpc:
          ca: null
          cert: null
          domain_name: null
          key: null
          metadata: {}
        http:
          headers: {}
        protocol: grpc
        temporality: cumulative
      propagation:
        aws_xray: false
        baggage: false
        datadog: false
        jaeger: false
        request:
          format: hexadecimal
          header_name: example_header_name
        trace_context: false
        zipkin: false
      zipkin:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            secs: 30
            nanos: 0
          max_queue_size: 2048
          scheduled_delay:
            secs: 5
            nanos: 0
        enabled: false
        endpoint: example_endpoint
  instrumentation:
    events:
      connector:
        error:
          condition:
            eq:
              - false
              - false
          level: info
        request:
          condition:
            eq:
              - false
              - false
          level: info
        response:
          condition:
            eq:
              - false
              - false
          level: info
      router:
        error:
          condition:
            eq:
              - false
              - false
          level: info
        request:
          condition:
            eq:
              - false
              - false
          level: info
        response:
          condition:
            eq:
              - false
              - false
          level: info
      subgraph:
        error:
          condition:
            eq:
              - false
              - false
          level: info
        request:
          condition:
            eq:
              - false
              - false
          level: info
        response:
          condition:
            eq:
              - false
              - false
          level: info
      supergraph:
        error:
          condition:
            eq:
              - false
              - false
          level: info
        request:
          condition:
            eq:
              - false
              - false
          level: info
        response:
          condition:
            eq:
              - false
              - false
          level: info
    instruments:
      cache:
        apollo.router.operations.entity.cache:
          attributes:
            graphql.type.name:
              alias: example_alias
      connector:
        http.client.request.body.size:
          attributes:
            connector.http.method:
              alias: example_alias
            connector.source.name:
              alias: example_alias
            connector.url.template:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.request.duration:
          attributes:
            connector.http.method:
              alias: example_alias
            connector.source.name:
              alias: example_alias
            connector.url.template:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.response.body.size:
          attributes:
            connector.http.method:
              alias: example_alias
            connector.source.name:
              alias: example_alias
            connector.url.template:
              alias: example_alias
            subgraph.name:
              alias: example_alias
      default_requirement_level: none
      graphql:
        field.execution:
          attributes:
            graphql.field.name:
              alias: example_alias
            graphql.field.type:
              alias: example_alias
            graphql.list.length:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.type.name:
              alias: example_alias
        list.length:
          attributes:
            graphql.field.name:
              alias: example_alias
            graphql.field.type:
              alias: example_alias
            graphql.list.length:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.type.name:
              alias: example_alias
      router:
        http.server.active_requests:
          attributes:
            http.request.method: false
            server.address: false
            server.port: false
            url.scheme: false
        http.server.request.body.size:
          attributes:
            baggage: null
            dd.trace_id:
              alias: example_alias
            error.type:
              alias: example_alias
            http.request.body.size:
              alias: example_alias
            http.request.method:
              alias: example_alias
            http.response.body.size:
              alias: example_alias
            http.response.status_code:
              alias: example_alias
            http.route:
              alias: example_alias
            network.local.address:
              alias: example_alias
            network.local.port:
              alias: example_alias
            network.peer.address:
              alias: example_alias
            network.peer.port:
              alias: example_alias
            network.protocol.name:
              alias: example_alias
            network.protocol.version:
              alias: example_alias
            network.transport:
              alias: example_alias
            network.type:
              alias: example_alias
            server.address:
              alias: example_alias
            server.port:
              alias: example_alias
            trace_id:
              alias: example_alias
            url.path:
              alias: example_alias
            url.query:
              alias: example_alias
            url.scheme:
              alias: example_alias
            user_agent.original:
              alias: example_alias
        http.server.request.duration:
          attributes:
            baggage: null
            dd.trace_id:
              alias: example_alias
            error.type:
              alias: example_alias
            http.request.body.size:
              alias: example_alias
            http.request.method:
              alias: example_alias
            http.response.body.size:
              alias: example_alias
            http.response.status_code:
              alias: example_alias
            http.route:
              alias: example_alias
            network.local.address:
              alias: example_alias
            network.local.port:
              alias: example_alias
            network.peer.address:
              alias: example_alias
            network.peer.port:
              alias: example_alias
            network.protocol.name:
              alias: example_alias
            network.protocol.version:
              alias: example_alias
            network.transport:
              alias: example_alias
            network.type:
              alias: example_alias
            server.address:
              alias: example_alias
            server.port:
              alias: example_alias
            trace_id:
              alias: example_alias
            url.path:
              alias: example_alias
            url.query:
              alias: example_alias
            url.scheme:
              alias: example_alias
            user_agent.original:
              alias: example_alias
        http.server.response.body.size:
          attributes:
            baggage: null
            dd.trace_id:
              alias: example_alias
            error.type:
              alias: example_alias
            http.request.body.size:
              alias: example_alias
            http.request.method:
              alias: example_alias
            http.response.body.size:
              alias: example_alias
            http.response.status_code:
              alias: example_alias
            http.route:
              alias: example_alias
            network.local.address:
              alias: example_alias
            network.local.port:
              alias: example_alias
            network.peer.address:
              alias: example_alias
            network.peer.port:
              alias: example_alias
            network.protocol.name:
              alias: example_alias
            network.protocol.version:
              alias: example_alias
            network.transport:
              alias: example_alias
            network.type:
              alias: example_alias
            server.address:
              alias: example_alias
            server.port:
              alias: example_alias
            trace_id:
              alias: example_alias
            url.path:
              alias: example_alias
            url.query:
              alias: example_alias
            url.scheme:
              alias: example_alias
            user_agent.original:
              alias: example_alias
      subgraph:
        http.client.request.body.size:
          attributes:
            http.request.resend_count:
              alias: example_alias
            subgraph.graphql.document:
              alias: example_alias
            subgraph.graphql.operation.name:
              alias: example_alias
            subgraph.graphql.operation.type:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.request.duration:
          attributes:
            http.request.resend_count:
              alias: example_alias
            subgraph.graphql.document:
              alias: example_alias
            subgraph.graphql.operation.name:
              alias: example_alias
            subgraph.graphql.operation.type:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.response.body.size:
          attributes:
            http.request.resend_count:
              alias: example_alias
            subgraph.graphql.document:
              alias: example_alias
            subgraph.graphql.operation.name:
              alias: example_alias
            subgraph.graphql.operation.type:
              alias: example_alias
            subgraph.name:
              alias: example_alias
      supergraph:
        cost.actual:
          attributes:
            cost.actual:
              alias: example_alias
            cost.delta:
              alias: example_alias
            cost.estimated:
              alias: example_alias
            cost.result:
              alias: example_alias
            graphql.document:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.operation.type:
              alias: example_alias
        cost.delta:
          attributes:
            cost.actual:
              alias: example_alias
            cost.delta:
              alias: example_alias
            cost.estimated:
              alias: example_alias
            cost.result:
              alias: example_alias
            graphql.document:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.operation.type:
              alias: example_alias
        cost.estimated:
          attributes:
            cost.actual:
              alias: example_alias
            cost.delta:
              alias: example_alias
            cost.estimated:
              alias: example_alias
            cost.result:
              alias: example_alias
            graphql.document:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.operation.type:
              alias: example_alias
    spans:
      connector:
        attributes:
          connector.http.method:
            alias: example_alias
          connector.source.name:
            alias: example_alias
          connector.url.template:
            alias: example_alias
          subgraph.name:
            alias: example_alias
      default_attribute_requirement_level: none
      mode: deprecated
      router:
        attributes:
          baggage: null
          dd.trace_id:
            alias: example_alias
          error.type:
            alias: example_alias
          http.request.body.size:
            alias: example_alias
          http.request.method:
            alias: example_alias
          http.response.body.size:
            alias: example_alias
          http.response.status_code:
            alias: example_alias
          http.route:
            alias: example_alias
          network.local.address:
            alias: example_alias
          network.local.port:
            alias: example_alias
          network.peer.address:
            alias: example_alias
          network.peer.port:
            alias: example_alias
          network.protocol.name:
            alias: example_alias
          network.protocol.version:
            alias: example_alias
          network.transport:
            alias: example_alias
          network.type:
            alias: example_alias
          server.address:
            alias: example_alias
          server.port:
            alias: example_alias
          trace_id:
            alias: example_alias
          url.path:
            alias: example_alias
          url.query:
            alias: example_alias
          url.scheme:
            alias: example_alias
          user_agent.original:
            alias: example_alias
      subgraph:
        attributes:
          http.request.resend_count:
            alias: example_alias
          subgraph.graphql.document:
            alias: example_alias
          subgraph.graphql.operation.name:
            alias: example_alias
          subgraph.graphql.operation.type:
            alias: example_alias
          subgraph.name:
            alias: example_alias
      supergraph:
        attributes:
          cost.actual:
            alias: example_alias
          cost.delta:
            alias: example_alias
          cost.estimated:
            alias: example_alias
          cost.result:
            alias: example_alias
          graphql.document:
            alias: example_alias
          graphql.operation.name:
            alias: example_alias
          graphql.operation.type:
            alias: example_alias
tls:
  connector:
    all:
      certificate_authorities: null
      client_authentication:
        certificate_chain: example_certificate_chain
        key: example_key
    sources: {}
  subgraph:
    all:
      certificate_authorities: null
      client_authentication:
        certificate_chain: example_certificate_chain
        key: example_key
    subgraphs: {}
  supergraph:
    certificate: example_certificate
    certificate_chain: example_certificate_chain
    key: example_key
traffic_shaping:
  all:
    compression: gzip
    deduplicate_query: false
    dns_resolution_strategy: ipv4_only
    experimental_http2: enable
    global_rate_limit:
      capacity: 1
      interval: 30s
    timeout: null
  connector:
    all:
      compression: gzip
      dns_resolution_strategy: ipv4_only
      experimental_http2: enable
      global_rate_limit:
        capacity: 1
        interval: 30s
      timeout: null
    sources: {}
  deduplicate_variables: null
  router:
    concurrency_limit: 0
    global_rate_limit:
      capacity: 1
      interval: 30s
    timeout: null
  subgraphs: {}
```

## Properties

***

### `apq`

```yaml title=apq
apq:
  enabled: true
  router:
    cache:
      in_memory:
        limit: 1
      redis:
        namespace: example_namespace
        password: example_password
        pool_size: 1
        required_to_start: false
        reset_ttl: true
        timeout: null
        tls:
          certificate_authorities: null
          client_authentication:
            certificate_chain: example_certificate_chain
            key: example_key
        ttl: null
        urls:
        - http://example.com/urls_item
        username: example_username
  subgraph:
    all:
      enabled: false
    subgraphs: {}
```

Learn more in [Automatic Persisted Queries](https://www.apollographql.com/docs/graphos/routing/operations/apq).

***

### `authentication`

```yaml title=authentication
authentication:
  connector:
    sources: {}
  router:
    jwt:
      header_name: authorization
      header_value_prefix: Bearer
      ignore_other_prefixes: false
      jwks:
      - algorithms: null
        headers:
        - name: example_name
          value: example_value
        issuer: example_issuer
        poll_interval:
          nanos: 0
          secs: 60
        url: http://service.example.com/url
      on_error: Continue
      sources:
      - name: authorization
        type: header
        value_prefix: Bearer
  subgraph:
    all:
      aws_sig_v4:
        hardcoded:
          access_key_id: example_access_key_id
          assume_role:
            external_id: example_external_id
            role_arn: example_role_arn
            session_name: example_session_name
          region: example_region
          secret_access_key: example_secret_access_key
          service_name: example_service_name
    subgraphs: {}
```

* To learn about JWT authentication, go to [JWT authentication in the GraphOS Router](https://www.apollographql.com/docs/router/configuration/authn-jwt).

* To learn about subgraph authentication with AWS SigV4, go to a [subgraph authentication configuration example](https://www.apollographql.com/docs/router/configuration/authn-subgraph/#configuration-example).

***

### `authorization`

```yaml title=authorization
authorization:
  directives:
    dry_run: false
    enabled: true
    errors:
      log: true
      response: errors
    reject_unauthorized: false
  require_authentication: false
```

* To configure authorization directives, see [Authorization directives](https://www.apollographql.com/docs/router/configuration/authorization/#authorization-directives).

* To configure the authorization plugin, see [Configuration options](https://www.apollographql.com/docs/router/configuration/authorization/#configuration-options).

***

### `batching`

```yaml title=batching
batching:
  enabled: false
  maximum_size: null
  mode: batch_http_link
  subgraph:
    all:
      enabled: false
    subgraphs: {}
```

Learn more in [query batching](https://www.apollographql.com/docs/router/executing-operations/query-batching).

***

### `connectors`

```yaml title=connectors
connectors:
  debug_extensions: false
  expose_sources_in_context: false
  max_requests_per_operation_per_source: null
  sources: {}
  subgraphs: {}
```

Learn more in [Working with router for Apollo Connectors](https://www.apollographql.com/docs/graphos/connectors/router).

***

### `coprocessor`

```yaml title=coprocessor
coprocessor:
  client:
    dns_resolution_strategy: ipv4_only
    experimental_http2: enable
  connector:
    all:
      request:
        body: false
        condition:
          eq:
          - false
          - false
        context: false
        headers: false
        method: false
        service_name: false
        uri: false
      response:
        body: false
        condition:
          eq:
          - false
          - false
        context: false
        headers: false
        service_name: false
        status_code: false
  execution:
    request:
      body: false
      context: false
      headers: false
      method: false
      query_plan: false
      sdl: false
    response:
      body: false
      context: false
      headers: false
      sdl: false
      status_code: false
  router:
    request:
      body: false
      condition:
        eq:
        - false
        - false
      context: false
      headers: false
      method: false
      path: false
      sdl: false
    response:
      body: false
      condition:
        eq:
        - false
        - false
      context: false
      headers: false
      sdl: false
      status_code: false
  subgraph:
    all:
      request:
        body: false
        condition:
          eq:
          - false
          - false
        context: false
        headers: false
        method: false
        service_name: false
        subgraph_request_id: false
        uri: false
      response:
        body: false
        condition:
          eq:
          - false
          - false
        context: false
        headers: false
        service_name: false
        status_code: false
        subgraph_request_id: false
  supergraph:
    request:
      body: false
      condition:
        eq:
        - false
        - false
      context: false
      headers: false
      method: false
      sdl: false
    response:
      body: false
      condition:
        eq:
        - false
        - false
      context: false
      headers: false
      sdl: false
      status_code: false
  timeout:
    nanos: 0
    secs: 1
  url: http://service.example.com/url
```

Learn more in [External coprocessing in the GraphOS Router](https://www.apollographql.com/docs/router/customizations/coprocessor/).

***

### `cors`

```yaml title=cors
cors:
  allow_any_origin: false
  allow_credentials: false
  allow_headers: []
  expose_headers: null
  max_age: null
  methods:
  - GET
  - POST
  - OPTIONS
  policies:
  - origins:
    - https://studio.apollographql.com
    - https://myapp.com
    allow_credentials: false
    allow_headers: []
    expose_headers: []
    private_network_access:
      access_id:
    # methods not specified - uses global defaults [GET, POST, OPTIONS]
  - origins:
    - https://restricted.com
    methods: []  # Explicitly no methods allowed
  - origins:
    - https://api.example.com
    match_origins:
    - "^https://.*\\.example\\.com$"
    allow_headers:
    - content-type
    - authorization
    methods:
    - GET
    - POST
    private_network_access:
      access_id: "01:23:45:67:89:0A"
      access_name: "mega-corp device"
    # Specific methods override global defaults
```

By default, the router only allows GraphOS Studio to initiate browser connections to it. If your supergraph serves data to other browser-based applications, you need to update its Cross-Origin Resource Sharing (CORS) configuration.

Learn more in [CORS](https://www.apollographql.com/docs/graphos/routing/security/cors).

***

### `csrf`

```yaml title=csrf
csrf:
  required_headers:
  - x-apollo-operation-name
  - apollo-require-preflight
  unsafe_disabled: false
```

Learn more in [CSRF prevention in the router](https://www.apollographql.com/docs/router/configuration/csrf).

***

### `demand_control`

```yaml title=demand_control
demand_control:
  enabled: false
  mode: measure
  strategy:
    static_estimated:
      list_size: 0
      max: 0.0
      actual_cost_mode: by_subgraph
      subgraph:
        all:
          list_size: 0
          max: 0.0
        subgraphs: {}
```

With demand control, the router analyzes the cost of operations and rejects requests with operations that exceed customizable cost limits.

Learn more in [Demand Control](https://www.apollographql.com/docs/router/executing-operations/demand-control)

***

### `experimental_chaos`

```yaml title=experimental_chaos
experimental_chaos:
  force_reload: null
```

***

### `experimental_hoist_orphan_errors`

```yaml title=experimental_hoist_orphan_errors
experimental_hoist_orphan_errors:
  all:
    enabled: false
  subgraphs: {}
```

When the entity-resolution process for a subgraph returns errors that apply to multiple entities in a list, the router defaults to propagating each error to every matching entity path. That results in a multiplicative increase in the size of the returned error array.

The `experimental_hoist_orphan_errors` option changes that behavior on a per-subgraph basis. When enabled, the router attaches each orphaned subgraph error to a single parent path instead of duplicating the error across every entity path, which can significantly reduce the number of errors in the response.

The `experimental_hoist_orphan_errors` option isn't compliant with the GraphQL spec. The option changes how errors are associated with paths in the response, compared to the behavior described in the [GraphQL specification](https://spec.graphql.org/). Only use the feature for your subgraphs when the reduction in error volume is more desirable than strict compliance.

To target a specific subgraph:

```yaml title=router.yaml
experimental_hoist_orphan_errors:
  subgraphs:
    my_subgraph:
      enabled: true
```

To target all subgraphs:

```yaml title=router.yaml
experimental_hoist_orphan_errors:
  all:
    enabled: true
```

To target all subgraphs except one:

```yaml title=router.yaml
experimental_hoist_orphan_errors:
  all:
    enabled: true
  subgraphs:
    spec_compliant_one:
      enabled: false
```

Per-subgraph settings override `all`.

Although the `experimental_hoist_orphan_errors` option can reduce the number of propagated errors, the option doesn't limit the total number of errors. If a subgraph returns a large number of errors, the router still processes all of them. For subgraphs that are likely to produce an unbounded number of errors, consider additional mitigation strategies at the subgraph level.

***

### `experimental_type_conditioned_fetching`

```yaml title=experimental_type_conditioned_fetching
experimental_type_conditioned_fetching: false
```

***

### `fleet_detector`

```yaml title=fleet_detector
fleet_detector: {}
```

***

### `forbid_mutations`

```yaml title=forbid_mutations
forbid_mutations: false
```

***

### `headers`

```yaml title=headers
headers:
  all:
    request:
    - insert:
        name: example_name
        value: example_value
  subgraphs: {}
```

Learn more in [Sending HTTP headers to subgraphs](https://www.apollographql.com/docs/graphos/routing/header-propagation/).

***

### `health_check`

```yaml title=health_check
health_check:
  enabled: true
  listen: example_listen
  path: /health
  readiness:
    allowed: 100
    interval:
      sampling: 0s
      unready: null
```

Learn more in [Health Checks](https://www.apollographql.com/docs/graphos/routing/self-hosted/health-checks).

***

### `homepage`

```yaml title=homepage
homepage:
  enabled: true
  graph_ref: null
```

The router can serve a landing page to browsers that visit its endpoint path (`supergraph.path`):

* A basic landing page that displays an example query `curl` command (default)

  ```yaml title=router.yaml
  # This is the default behavior. You don't need to include this config.
  homepage:
    enabled: true
  ```

* *No* landing page

  ```yaml title=router.yaml
  homepage:
    enabled: false
  ```

* Sending users to Apollo Explorer

  ```yaml title=router.yaml
  homepage:
    graph_ref: my-org-graph@production
  ```

  When you specify a `graph_ref`, the router's landing page includes an option for users to redirect to Apollo Explorer. Users can check a box that will remember their preference and automatically redirect them to Explorer on subsequent visits.

  The `graph_ref` value should match the format `organization-name@variant-name`, which is the same format used with the `APOLLO_GRAPH_REF` environment variable. Note that the router does not automatically use the value from the `APOLLO_GRAPH_REF` environment variable for this setting - you must explicitly set `graph_ref` in your YAML configuration even if you're already using the environment variable.

***

### `include_subgraph_errors`

```yaml title=include_subgraph_errors
include_subgraph_errors:
  all: false
  subgraphs: {}
```

***

### `license_enforcement`

```yaml title=license_enforcement
license_enforcement: {}
```

***

### `limits`

```yaml title=limits
limits:
  http1_max_request_buf_size: null
  http1_max_request_headers: null
  http_max_request_bytes: 2000000
  introspection_max_depth: true
  max_aliases: null
  max_depth: null
  max_height: null
  max_root_fields: null
  parser_max_recursion: 500
  parser_max_tokens: 15000
  warn_only: false
```

Learn more in [Request Limits](https://www.apollographql.com/docs/graphos/routing/security/request-limits).

***

### `override_subgraph_url`

```yaml title=override_subgraph_url
override_subgraph_url: {}
```

By default, the router obtains the routing URL for each of your subgraphs from the composed supergraph schema you provide it. In most cases, no additional configuration is required. The URL can use HTTP and HTTPS for network access to subgraph, or have the following shape for Unix sockets usage: `unix:///path/to/subgraph.sock`

Unix socket paths should be absolute (starting with `/`). The URL format is `unix://` followed by the absolute path, resulting in three slashes: `unix:///var/run/subgraph.sock`.

Because `.sock` is not required as a file extension, the router cannot determine if a path is appended to the base URL. Specify a custom HTTP path using the `path` query parameter:

```yaml
override_subgraph_url:
  my_subgraph: "unix:///tmp/subgraph.sock?path=/graphql/v1"
```

This configuration also applies to subgraph URLs defined in your supergraph schema (using the `url` argument of the `@join__graph` directive).

However, if you *do* need to override a particular subgraph's routing URL (for example, to handle changing network topography), you can do so with the `override_subgraph_url` option:

```yaml
override_subgraph_url:
  organizations: http://localhost:8080
  accounts: "${env.ACCOUNTS_SUBGRAPH_HOST_URL}"
```

In this example, the `organizations` subgraph URL is overridden to point to `http://localhost:8080`, and the `accounts` subgraph URL is overridden to point to a new URL using [variable expansion](https://www.apollographql.com/docs/graphos/routing/configuration/yaml.md#variable-expansion). The URL specified in the supergraph schema is ignored.

Any subgraphs that are *omitted* from `override_subgraph_url` continue to use the routing URL specified in the supergraph schema.

If you need to override the subgraph URL at runtime on a per-request basis, you can use [request customizations](https://www.apollographql.com/docs/router/customizations/overview/#request-path) in the `SubgraphService` layer.

### `persisted_queries`

```yaml title=persisted_queries
persisted_queries:
  enabled: false
  experimental_prewarm_query_plan_cache:
    on_reload: true
    on_startup: false
  hot_reload: false
  local_manifests: null
  log_unknown: false
  safelist:
    enabled: false
    require_id: false
```

You can enhance your graph's security with GraphOS Router by maintaining a persisted query list (PQL), an operation safelist made by your first-party apps. As opposed to automatic persisted queries (APQ) where operations are automatically cached, operations must be preregistered to the PQL. Once configured, the router checks incoming requests against the PQL.

Learn more about [safelisting with persisted queries](https://www.apollographql.com/docs/graphos/platform/security/persisted-queries).

***

### `plugins`

```yaml title=plugins
plugins: unknown_type_plugins
```

You can customize the router's behavior with [plugins](https://www.apollographql.com/docs/router/customizations/overview). Each plugin can have its own section in the configuration file with arbitrary values:

```yaml title=example-plugin-router.yaml
plugins:
  example.plugin:
    var1: "hello"
    var2: 1
```

Learn more in [Native Plugins for router](https://www.apollographql.com/docs/graphos/routing/customization/native-plugins).

***

### `preview_entity_cache`

```yaml title=preview_entity_cache
preview_entity_cache:
  enabled: false
  expose_keys_in_context: false
  invalidation:
    concurrent_requests: 10
    listen: example_listen
    path: example_path
    scan_count: 1000
  metrics:
    enabled: false
    separate_per_type: false
    ttl: 30s
  subgraph:
    all:
      enabled: true
      invalidation:
        enabled: false
        shared_key: ''
      private_id: null
      redis:
        namespace: example_namespace
        password: example_password
        pool_size: 1
        required_to_start: false
        reset_ttl: true
        timeout: null
        tls:
          certificate_authorities: null
          client_authentication:
            certificate_chain: example_certificate_chain
            key: example_key
        ttl: null
        urls:
        - http://example.com/urls_item
        username: example_username
      ttl: 30s
    subgraphs: {}
```

When using Redis as the cache backend, the router emits additional Redis-specific metrics to help monitor cache performance:

* **Connection metrics**: Track Redis connection establishment and health
* **Command metrics**: Monitor Redis command execution, queue length, and redelivery counts
* **Performance metrics**: Measure average latency, network latency, and request/response sizes
* **Operational metrics**: Help identify connection issues, network problems, or performance bottlenecks

These metrics use the `kind` attribute to distinguish between different Redis cache uses (e.g., `entity`). For the complete list of Redis metrics and their descriptions, see the [Redis Cache metrics documentation](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/standard-instruments/#redis-cache).

For new projects, Apollo recommends using [Response Caching](https://www.apollographql.com/docs/graphos/routing/performance/caching/response-caching/overview) instead.

Learn more in [Entity Caching](https://www.apollographql.com/docs/graphos/routing/v1/performance/caching/entity).

***

### `response_cache`

```yaml title=response_cache.router.yaml
response_cache:
  enabled: false
  debug: false
  private_queries_buffer_size: 2048
  invalidation:
    listen: 127.0.0.1:4000
    path: /invalidation
  subgraph:
    all:
      enabled: true
      ttl: 30s
      private_id: null
      redis:
        urls:
        - redis://127.0.0.1:6379
        username: example_username
        password: example_password
        fetch_timeout: 150ms
        insert_timeout: 500ms
        invalidate_timeout: 1s
        maintenance_timeout: 500ms
        namespace: example_namespace
        tls:
          certificate_authorities: null
          client_authentication:
            certificate_chain: example_certificate_chain
            key: example_key
        required_to_start: false
        pool_size: 5
        metrics_interval: 1s
      invalidation:
        enabled: false
        shared_key: ''
    subgraphs: {}
```

When using Redis as the cache backend, the router emits additional Redis-specific metrics to help monitor cache performance:

* **Connection metrics**: Track Redis connection establishment and health
* **Command metrics**: Monitor Redis command execution, queue length, and redelivery counts
* **Performance metrics**: Measure average latency, network latency, and request/response sizes
* **Operational metrics**: Help identify connection issues, network problems, or performance bottlenecks

These metrics use the `kind` attribute to distinguish between different Redis cache uses (e.g., `response`). For the complete list of Redis metrics and their descriptions, see the [Redis Cache metrics documentation](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/standard-instruments/#redis-cache).

Learn more in [Response Caching](https://www.apollographql.com/docs/graphos/routing/performance/caching/response-caching/overview).

***

### `preview_file_uploads`

```yaml title=preview_file_uploads
preview_file_uploads:
  enabled: false
  protocols:
    multipart:
      enabled: true
      limits:
        max_file_size: example_max_file_size
        max_files: 0
      mode: stream
```

Learn more in [File Uploads](https://www.apollographql.com/docs/graphos/routing/operations/file-upload).

***

### `rhai`

```yaml title=rhai
rhai:
  main: example_main
  scripts: example_scripts
```

Learn more in [Rhai customization for router](https://www.apollographql.com/docs/graphos/routing/customization/rhai).

***

### `sandbox`

```yaml title=sandbox
sandbox:
  enabled: false
```

[Apollo Sandbox](https://www.apollographql.com/docs/graphos/explorer/sandbox) is a GraphQL development environment. It runs a graph via introspection queries on the router's supergrpah schema, and it provides an IDE for making queries to the graph.

Running Sandbox in router requires configuring `sandbox.enabled`, `supergraph.instrospection`, and `homepage.enabled`:

```yaml title=router.yaml
sandbox:
  enabled: true

# Sandbox uses introspection to obtain your router's schema.
supergraph:
  introspection: true

# Sandbox requires the default landing page to be disabled.
homepage:
  enabled: false
```

**Do not enable Sandbox in production.** Sandbox requires enabling introspection, which is strongly discouraged in production environments.

Learn more in [Apollo Sandbox](https://www.apollographql.com/docs/graphos/platform/sandbox).

***

### `server`

```yaml title=server
server:
  http:
    header_read_timeout: 30s
    tls_handshake_timeout: 30s
```

#### Header Read Timeout

The header read timeout is the amount of time the Router will wait to receive the complete request headers from a client before timing out. It applies both when the connection is fully idle and when a request has been started but sending the headers has not been completed.

By default, the header read timeout is set to 10 seconds. A longer timeout can be configured using the `server.http.header_read_timeout` configuration option.

#### TLS handshake timeout

The TLS handshake timeout determines how long the router waits to complete a TLS handshake with a client.

The default timeout is ten seconds. You can configure the `server.http.tls_handshake_timeout` option to change this duration.

***

### `subscription`

```yaml title=subscription
subscription:
  enable_deduplication: true
  enabled: true
  max_opened_subscriptions: null
  mode:
    callback:
      heartbeat_interval: disabled
      listen: example_listen
      path: example_path
      public_url: http://service.example.com/public_url
      subgraphs: []
    passthrough:
      all:
        heartbeat_interval: disabled
        path: null
        protocol: graphql_ws
      subgraphs: {}
  queue_capacity: null
```

Learn more in [Subscriptions](https://www.apollographql.com/docs/graphos/routing/operations/subscriptions).

***

### `supergraph`

```yaml title=supergraph
supergraph:
  defer_support: true
  early_cancel: false
  experimental_log_on_broken_pipe: false
  generate_query_fragments: true
  introspection: false
  listen: example_listen
  path: /
  redact_query_validation_errors: false
  query_planning:
    cache:
      in_memory:
        limit: 1
      redis:
        namespace: example_namespace
        password: example_password
        pool_size: 1
        required_to_start: false
        reset_ttl: true
        timeout: null
        tls:
          certificate_authorities: null
          client_authentication:
            certificate_chain: example_certificate_chain
            key: example_key
        ttl:
          nanos: 0
          secs: 2592000
        urls:
        - http://example.com/urls_item
        username: example_username
    experimental_paths_limit: null
    experimental_plans_limit: null
    experimental_reuse_query_plans: false
    warmed_up_queries: null
  strict_variable_validation: enforce
```

#### Supergraph listen address

As the gateway and single endpoint to your supergraph, an Apollo Router has a socket address and port that it listens for client requests. This listen address is configurable in YAML as `supergraph.listen`.

By default, the router starts an HTTP server that listens on `127.0.0.1:4000`. You can specify a different address by setting `supergraph.listen` for IPv4, IPv6, or Unix sockets.

##### IPv4

```yaml title=router.yaml
supergraph:
  # The socket address and port to listen on (default: 127.0.0.1:400)
  listen: 127.0.0.1:4000
```

##### IPv6

```yaml title=router.yaml
supergraph:
  # The socket address and port to listen on. (default: [::1]:4000)
  # Note that this must be quoted to avoid interpretation as an array in YAML.
  listen: "[::1]:4000"
```

##### Unix socket

```yaml title=router_unix.yaml
supergraph:
  # Absolute path to a Unix socket
  listen: /tmp/router.sock
```

Listening on a Unix socket is not supported on Windows.

#### Supergraph endpoint path

The path of the HTTP endpoint of the supergraph that the router runs is configured by `supergraph.path`.

By default, the router starts an HTTP server that exposes a `POST`/`GET` endpoint at path `/`.

```yaml title=router.yaml
supergraph:
  # The path for GraphQL execution
  # (Defaults to /)
  path: /graphql
```

The path must start with `/`.

A path can contain parameters and wildcards:

* `/{parameter}` matches a single segment. For example:

  * `/abc/{my_param}/def` matches `/abc/1/def` and `/abc/whatever/def`, but it doesn't match `/abc/1/2/def` or `/abc/def`

* `/{*parameter}` matches all segments in the rest of a path. For example:
  * `/abc/{*wildcard}` matches `/abc/1/def` and `/abc/w/h/a/t/e/v/e/r`, but it doesn't match `/abc/` or `/not_abc_at_all`

- Both parameters and wildcards require a name, even though you can’t use those names anywhere.

- The router doesn't support wildcards in the *middle* of a path (e.g., `/{*wild}/graphql`). Instead, use a path parameter (e.g., `/{parameter}/graphql`).

#### Introspection

In GraphQL, introspection queries are used during development to learn about a GraphQL API's schema. The router can resolve introspection queries, based on the configuration of `supergraph.introspection`.

By default, the router doesn't resolve introspection queries.

To enable introspection queries during development, set the `supergraph.introspection` flag:

```yaml title=router.yaml
# Do not enable introspection in production!
supergraph:
  introspection: true
```

##### Introspection recursion limit

The [schema-introspection schema](https://spec.graphql.org/draft/#sec-Schema-Introspection.Schema-Introspection-Schema) is recursive: a client can query the fields of the types of some other fields, and so on arbitrarily deep. This can produce responses that grow much faster than the size of the request.

To prevent this, the router is configured by default to not execute introspection queries that nest list fields that are too deep, instead returning an error. The criteria matches `MaxIntrospectionDepthRule` in graphql-js, and it may change in future versions.

In case the router rejects legitimate queries, you can disable the limit by setting the `limits.introspection_max_depth` flag:

```yaml title=router.yaml
# Do not enable introspection in production!
supergraph:
  introspection: true
limits:
  introspection_max_depth: false
```

#### Redacting query validation errors

Query validation errors might reveal information about your schema structure, such as field names, types, and required arguments. Although this is not typically a significant security concern (especially with persisted queries), you can redact these error details in production environments.

Apollo Router returns detailed validation error messages by default. To redact validation errors and return a generic error message, set the `supergraph.redact_query_validation_errors` flag:

```yaml title=router.yaml
supergraph:
  redact_query_validation_errors: true
```

When you enable this setting, Apollo Router replaces query validation errors with a single generic error:

```json
{
  "message": "invalid query",
  "extensions": {
    "code": "UNKNOWN_ERROR"
  }
}
```

Enabling this option will make debugging more difficult, as clients won't receive specific information about what's wrong with their queries. Consider enabling it only in production environments where schema details should remain private.

#### Early cancel

Up until [Apollo Router Core v1.43.1](https://github.com/apollographql/router/releases/tag/v1.43.1), when the client closed the connection without waiting for the response, the entire request was cancelled and did not go through the entire pipeline. Since this causes issues with request monitoring, the router introduced a new behavior in 1.43.1. Now, the entire pipeline is executed if the request is detected as cancelled, but subgraph requests are not actually done. The response will be reported with the `499` status code, but not actually sent to the client.

To go back to the previous behavior of immediately cancelling the request, the following configuration can be used for `supergraph.early_cancel`:

```yaml
supergraph:
  early_cancel: true
```

Additionally, since v1.43.1, the router can show a log when it detects that the client canceled the request. This log can be activated with:

```yaml title=router.yaml
supergraph:
  experimental_log_on_broken_pipe: true
```

#### Connection shutdown timeout

When the Router schema or configuration updates all connections must be closed for resources to be freed.
To ensure that long-lived connections do not hang on to resources, a maximum graceful shutdown timeout can be configured with `supergraph.connection_shutdown_timeout`:

```yaml title=router.yaml
supergraph:
  connection_shutdown_timeout: 60s
```

The default value is 60 seconds.

Note that if `early_cancel` is `false` (default), then requests in progress will still hold onto pipeline resources.
In that case, traffic shaping request timeouts should be used to prevent long-running requests:

```yaml title=router.yaml
traffic_shaping:
  router:
    timeout: 60s
```

#### Automatic fragment generation

By default, the router compresses subgraph requests by generating fragment definitions based on the shape of the subgraph operation. In many cases this significantly reduces the size of the query sent to subgraphs.

Opt out of this behavior by specifying `supergraph.generate_query_fragments`:

```yaml
supergraph:
  generate_query_fragments: false
```

#### Variable validation modes

By default, the router validates input variables strictly. It validates each input object value against its type definition, and any unknown fields result in a request error.

```yaml
supergraph:
  strict_variable_validation: enforce
```

If your implementation requires unknown fields on a defined type, you can opt out of stricter validation by specifying `strict_variable_validation: measure`.
In this case, the router will not error when encountering unknown fields, but will log the field for reference.

***

### `telemetry`

```yaml title=telemetry
telemetry:
  apollo:
    tracing:
      batch_processor:
        max_export_timeout: 30s
        scheduled_delay: 5s
        max_export_batch_size: 512
        max_concurrent_exports: 1
        max_queue_size: 2048
    metrics:
      otlp:
        batch_processor:
          scheduled_delay: 5s
          max_export_timeout: 30s
      usage_reports:
        batch_processor:
          max_export_timeout: 30s
          scheduled_delay: 5s
          max_queue_size: 2048
    buffer_size: 10000
    client_name_header: apollographql-client-name
    client_version_header: apollographql-client-version
    endpoint: https://usage-reporting.api.apollographql.com/api/ingress/traces
    errors:
      preview_extended_error_metrics: disabled
      subgraph:
        all:
          redact: true
          redaction_policy: strict
          send: true
        subgraphs: {}
    experimental_local_field_metrics: false
    experimental_otlp_endpoint: https://usage-reporting.api.apollographql.com/
    experimental_otlp_tracing_protocol: grpc
    field_level_instrumentation_sampler: 0.0
    metrics_reference_mode: extended
    otlp_tracing_sampler: 0.0
    send_headers:
      only:
      - example_only_item
    send_variable_values:
      only:
      - example_only_item
    signature_normalization_algorithm: enhanced
  exporters:
    logging:
      common:
        resource: {}
        service_name: null
        service_namespace: null
      stdout:
        enabled: true
        format:
          json:
            display_current_span: false
            display_filename: false
            display_level: true
            display_line_number: false
            display_resource: true
            display_span_id: true
            display_span_list: true
            display_target: true
            display_thread_id: false
            display_thread_name: false
            display_timestamp: true
            display_trace_id: hexadecimal
            span_attributes: []
        rate_limit:
          capacity: 1
          enabled: false
          interval:
            nanos: 0
            secs: 1
        tty_format:
          json:
            display_current_span: false
            display_filename: false
            display_level: true
            display_line_number: false
            display_resource: true
            display_span_id: true
            display_span_list: true
            display_target: true
            display_thread_id: false
            display_thread_name: false
            display_timestamp: true
            display_trace_id: hexadecimal
            span_attributes: []
    metrics:
      common:
        buckets:
        - 0.001
        - 0.005
        - 0.015
        - 0.05
        - 0.1
        - 0.2
        - 0.3
        - 0.4
        - 0.5
        - 1.0
        - 5.0
        - 10.0
        resource: {}
        service_name: null
        service_namespace: null
        views:
        - aggregation:
            histogram:
              buckets:
              - 0.0
          allowed_attribute_keys:
          - example_allowed_attribute_keys_item
          description: example_description
          name: example_name
          rename: example_rename
          unit: example_unit
      otlp:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            nanos: 0
            secs: 30
          max_queue_size: 2048
          scheduled_delay:
            nanos: 0
            secs: 5
        enabled: false
        endpoint: example_endpoint
        grpc:
          ca: null
          cert: null
          domain_name: null
          key: null
          metadata: {}
        http:
          headers: {}
        protocol: grpc
        temporality: cumulative
      prometheus:
        enabled: false
        listen: example_listen
        path: /metrics
    tracing:
      common:
        max_attributes_per_event: 128
        max_attributes_per_link: 128
        max_attributes_per_span: 128
        max_events_per_span: 128
        max_links_per_span: 128
        parent_based_sampler: true
        preview_datadog_agent_sampling: null
        resource: {}
        sampler: 0.0
        service_name: null
        service_namespace: null
      datadog:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            nanos: 0
            secs: 30
          max_queue_size: 2048
          scheduled_delay:
            nanos: 0
            secs: 5
        enable_span_mapping: true
        enabled: false
        endpoint: example_endpoint
        fixed_span_names: true
        resource_mapping: {}
        span_metrics:
          connect: true
          connect_request: true
          execution: true
          http_request: true
          parse_query: true
          query_planning: true
          request: true
          router: true
          subgraph: true
          subgraph_request: true
          supergraph: true
      experimental_response_trace_id:
        enabled: false
        format: hexadecimal
        header_name: example_header_name
      otlp:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            nanos: 0
            secs: 30
          max_queue_size: 2048
          scheduled_delay:
            nanos: 0
            secs: 5
        enabled: false
        endpoint: example_endpoint
        grpc:
          ca: null
          cert: null
          domain_name: null
          key: null
          metadata: {}
        http:
          headers: {}
        protocol: grpc
        temporality: cumulative
      propagation:
        aws_xray: false
        baggage: false
        datadog: false
        jaeger: false
        request:
          format: hexadecimal
          header_name: example_header_name
        trace_context: false
        zipkin: false
      zipkin:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            nanos: 0
            secs: 30
          max_queue_size: 2048
          scheduled_delay:
            nanos: 0
            secs: 5
        enabled: false
        endpoint: example_endpoint
  instrumentation:
    events:
      connector:
        error:
          condition:
            eq:
            - false
            - false
          level: info
        request:
          condition:
            eq:
            - false
            - false
          level: info
        response:
          condition:
            eq:
            - false
            - false
          level: info
      router:
        error:
          condition:
            eq:
            - false
            - false
          level: info
        request:
          condition:
            eq:
            - false
            - false
          level: info
        response:
          condition:
            eq:
            - false
            - false
          level: info
      subgraph:
        error:
          condition:
            eq:
            - false
            - false
          level: info
        request:
          condition:
            eq:
            - false
            - false
          level: info
        response:
          condition:
            eq:
            - false
            - false
          level: info
      supergraph:
        error:
          condition:
            eq:
            - false
            - false
          level: info
        request:
          condition:
            eq:
            - false
            - false
          level: info
        response:
          condition:
            eq:
            - false
            - false
          level: info
    instruments:
      cache:
        apollo.router.operations.entity.cache:
          attributes:
            graphql.type.name:
              alias: example_alias
      connector:
        http.client.request.body.size:
          attributes:
            connector.http.method:
              alias: example_alias
            connector.source.name:
              alias: example_alias
            connector.url.template:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.request.duration:
          attributes:
            connector.http.method:
              alias: example_alias
            connector.source.name:
              alias: example_alias
            connector.url.template:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.response.body.size:
          attributes:
            connector.http.method:
              alias: example_alias
            connector.source.name:
              alias: example_alias
            connector.url.template:
              alias: example_alias
            subgraph.name:
              alias: example_alias
      default_requirement_level: none
      graphql:
        field.execution:
          attributes:
            graphql.field.name:
              alias: example_alias
            graphql.field.type:
              alias: example_alias
            graphql.list.length:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.type.name:
              alias: example_alias
        list.length:
          attributes:
            graphql.field.name:
              alias: example_alias
            graphql.field.type:
              alias: example_alias
            graphql.list.length:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.type.name:
              alias: example_alias
      router:
        http.server.active_requests:
          attributes:
            http.request.method: false
            server.address: false
            server.port: false
            url.scheme: false
        http.server.request.body.size:
          attributes:
            baggage: null
            dd.trace_id:
              alias: example_alias
            error.type:
              alias: example_alias
            http.request.body.size:
              alias: example_alias
            http.request.method:
              alias: example_alias
            http.response.body.size:
              alias: example_alias
            http.response.status_code:
              alias: example_alias
            http.route:
              alias: example_alias
            network.local.address:
              alias: example_alias
            network.local.port:
              alias: example_alias
            network.peer.address:
              alias: example_alias
            network.peer.port:
              alias: example_alias
            network.protocol.name:
              alias: example_alias
            network.protocol.version:
              alias: example_alias
            network.transport:
              alias: example_alias
            network.type:
              alias: example_alias
            server.address:
              alias: example_alias
            server.port:
              alias: example_alias
            trace_id:
              alias: example_alias
            url.path:
              alias: example_alias
            url.query:
              alias: example_alias
            url.scheme:
              alias: example_alias
            user_agent.original:
              alias: example_alias
        http.server.request.duration:
          attributes:
            baggage: null
            dd.trace_id:
              alias: example_alias
            error.type:
              alias: example_alias
            http.request.body.size:
              alias: example_alias
            http.request.method:
              alias: example_alias
            http.response.body.size:
              alias: example_alias
            http.response.status_code:
              alias: example_alias
            http.route:
              alias: example_alias
            network.local.address:
              alias: example_alias
            network.local.port:
              alias: example_alias
            network.peer.address:
              alias: example_alias
            network.peer.port:
              alias: example_alias
            network.protocol.name:
              alias: example_alias
            network.protocol.version:
              alias: example_alias
            network.transport:
              alias: example_alias
            network.type:
              alias: example_alias
            server.address:
              alias: example_alias
            server.port:
              alias: example_alias
            trace_id:
              alias: example_alias
            url.path:
              alias: example_alias
            url.query:
              alias: example_alias
            url.scheme:
              alias: example_alias
            user_agent.original:
              alias: example_alias
        http.server.response.body.size:
          attributes:
            baggage: null
            dd.trace_id:
              alias: example_alias
            error.type:
              alias: example_alias
            http.request.body.size:
              alias: example_alias
            http.request.method:
              alias: example_alias
            http.response.body.size:
              alias: example_alias
            http.response.status_code:
              alias: example_alias
            http.route:
              alias: example_alias
            network.local.address:
              alias: example_alias
            network.local.port:
              alias: example_alias
            network.peer.address:
              alias: example_alias
            network.peer.port:
              alias: example_alias
            network.protocol.name:
              alias: example_alias
            network.protocol.version:
              alias: example_alias
            network.transport:
              alias: example_alias
            network.type:
              alias: example_alias
            server.address:
              alias: example_alias
            server.port:
              alias: example_alias
            trace_id:
              alias: example_alias
            url.path:
              alias: example_alias
            url.query:
              alias: example_alias
            url.scheme:
              alias: example_alias
            user_agent.original:
              alias: example_alias
      subgraph:
        http.client.request.body.size:
          attributes:
            http.request.resend_count:
              alias: example_alias
            subgraph.graphql.document:
              alias: example_alias
            subgraph.graphql.operation.name:
              alias: example_alias
            subgraph.graphql.operation.type:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.request.duration:
          attributes:
            http.request.resend_count:
              alias: example_alias
            subgraph.graphql.document:
              alias: example_alias
            subgraph.graphql.operation.name:
              alias: example_alias
            subgraph.graphql.operation.type:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.response.body.size:
          attributes:
            http.request.resend_count:
              alias: example_alias
            subgraph.graphql.document:
              alias: example_alias
            subgraph.graphql.operation.name:
              alias: example_alias
            subgraph.graphql.operation.type:
              alias: example_alias
            subgraph.name:
              alias: example_alias
      supergraph:
        cost.actual:
          attributes:
            cost.actual:
              alias: example_alias
            cost.delta:
              alias: example_alias
            cost.estimated:
              alias: example_alias
            cost.result:
              alias: example_alias
            graphql.document:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.operation.type:
              alias: example_alias
        cost.delta:
          attributes:
            cost.actual:
              alias: example_alias
            cost.delta:
              alias: example_alias
            cost.estimated:
              alias: example_alias
            cost.result:
              alias: example_alias
            graphql.document:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.operation.type:
              alias: example_alias
        cost.estimated:
          attributes:
            cost.actual:
              alias: example_alias
            cost.delta:
              alias: example_alias
            cost.estimated:
              alias: example_alias
            cost.result:
              alias: example_alias
            graphql.document:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.operation.type:
              alias: example_alias
    spans:
      connector:
        attributes:
          connector.http.method:
            alias: example_alias
          connector.source.name:
            alias: example_alias
          connector.url.template:
            alias: example_alias
          subgraph.name:
            alias: example_alias
      default_attribute_requirement_level: none
      mode: deprecated
      router:
        attributes:
          baggage: null
          dd.trace_id:
            alias: example_alias
          error.type:
            alias: example_alias
          http.request.body.size:
            alias: example_alias
          http.request.method:
            alias: example_alias
          http.response.body.size:
            alias: example_alias
          http.response.status_code:
            alias: example_alias
          http.route:
            alias: example_alias
          network.local.address:
            alias: example_alias
          network.local.port:
            alias: example_alias
          network.peer.address:
            alias: example_alias
          network.peer.port:
            alias: example_alias
          network.protocol.name:
            alias: example_alias
          network.protocol.version:
            alias: example_alias
          network.transport:
            alias: example_alias
          network.type:
            alias: example_alias
          server.address:
            alias: example_alias
          server.port:
            alias: example_alias
          trace_id:
            alias: example_alias
          url.path:
            alias: example_alias
          url.query:
            alias: example_alias
          url.scheme:
            alias: example_alias
          user_agent.original:
            alias: example_alias
      subgraph:
        attributes:
          http.request.resend_count:
            alias: example_alias
          subgraph.graphql.document:
            alias: example_alias
          subgraph.graphql.operation.name:
            alias: example_alias
          subgraph.graphql.operation.type:
            alias: example_alias
          subgraph.name:
            alias: example_alias
      supergraph:
        attributes:
          cost.actual:
            alias: example_alias
          cost.delta:
            alias: example_alias
          cost.estimated:
            alias: example_alias
          cost.result:
            alias: example_alias
          graphql.document:
            alias: example_alias
          graphql.operation.name:
            alias: example_alias
          graphql.operation.type:
            alias: example_alias
```

```yaml title=telemetry
telemetry:
  apollo:
    batch_processor:
      max_concurrent_exports: 1
      max_export_batch_size: 512
      max_export_timeout:
        nanos: 0
        secs: 30
      max_queue_size: 2048
      scheduled_delay:
        nanos: 0
        secs: 5
    buffer_size: 10000
    client_name_header: apollographql-client-name
    client_version_header: apollographql-client-version
    endpoint: https://usage-reporting.api.apollographql.com/api/ingress/traces
    errors:
      preview_extended_error_metrics: disabled
      subgraph:
        all:
          redact: true
          redaction_policy: strict
          send: true
        subgraphs: {}
    experimental_local_field_metrics: false
    experimental_otlp_endpoint: https://usage-reporting.api.apollographql.com/
    experimental_otlp_tracing_protocol: grpc
    field_level_instrumentation_sampler: 0.0
    metrics_reference_mode: extended
    otlp_tracing_sampler: 0.0
    send_headers:
      only:
      - example_only_item
    send_variable_values:
      only:
      - example_only_item
    signature_normalization_algorithm: enhanced
  exporters:
    logging:
      common:
        resource: {}
        service_name: null
        service_namespace: null
      stdout:
        enabled: true
        format:
          json:
            display_current_span: false
            display_filename: false
            display_level: true
            display_line_number: false
            display_resource: true
            display_span_id: true
            display_span_list: true
            display_target: true
            display_thread_id: false
            display_thread_name: false
            display_timestamp: true
            display_trace_id: hexadecimal
            span_attributes: []
        rate_limit:
          capacity: 1
          enabled: false
          interval:
            nanos: 0
            secs: 1
        tty_format:
          json:
            display_current_span: false
            display_filename: false
            display_level: true
            display_line_number: false
            display_resource: true
            display_span_id: true
            display_span_list: true
            display_target: true
            display_thread_id: false
            display_thread_name: false
            display_timestamp: true
            display_trace_id: hexadecimal
            span_attributes: []
    metrics:
      common:
        buckets:
        - 0.001
        - 0.005
        - 0.015
        - 0.05
        - 0.1
        - 0.2
        - 0.3
        - 0.4
        - 0.5
        - 1.0
        - 5.0
        - 10.0
        resource: {}
        service_name: null
        service_namespace: null
        views:
        - aggregation:
            histogram:
              buckets:
              - 0.0
          allowed_attribute_keys:
          - example_allowed_attribute_keys_item
          description: example_description
          name: example_name
          unit: example_unit
      otlp:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            nanos: 0
            secs: 30
          max_queue_size: 2048
          scheduled_delay:
            nanos: 0
            secs: 5
        enabled: false
        endpoint: example_endpoint
        grpc:
          ca: null
          cert: null
          domain_name: null
          key: null
          metadata: {}
        http:
          headers: {}
        protocol: grpc
        temporality: cumulative
      prometheus:
        enabled: false
        listen: example_listen
        path: /metrics
    tracing:
      common:
        max_attributes_per_event: 128
        max_attributes_per_link: 128
        max_attributes_per_span: 128
        max_events_per_span: 128
        max_links_per_span: 128
        parent_based_sampler: true
        preview_datadog_agent_sampling: null
        resource: {}
        sampler: 0.0
        service_name: null
        service_namespace: null
      datadog:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            nanos: 0
            secs: 30
          max_queue_size: 2048
          scheduled_delay:
            nanos: 0
            secs: 5
        enable_span_mapping: true
        enabled: false
        endpoint: example_endpoint
        fixed_span_names: true
        resource_mapping: {}
        span_metrics:
          connect: true
          connect_request: true
          execution: true
          http_request: true
          parse_query: true
          query_planning: true
          request: true
          router: true
          subgraph: true
          subgraph_request: true
          supergraph: true
      experimental_response_trace_id:
        enabled: false
        format: hexadecimal
        header_name: example_header_name
      otlp:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            nanos: 0
            secs: 30
          max_queue_size: 2048
          scheduled_delay:
            nanos: 0
            secs: 5
        enabled: false
        endpoint: example_endpoint
        grpc:
          ca: null
          cert: null
          domain_name: null
          key: null
          metadata: {}
        http:
          headers: {}
        protocol: grpc
        temporality: cumulative
      propagation:
        aws_xray: false
        baggage: false
        datadog: false
        jaeger: false
        request:
          format: hexadecimal
          header_name: example_header_name
        trace_context: false
        zipkin: false
      zipkin:
        batch_processor:
          max_concurrent_exports: 1
          max_export_batch_size: 512
          max_export_timeout:
            nanos: 0
            secs: 30
          max_queue_size: 2048
          scheduled_delay:
            nanos: 0
            secs: 5
        enabled: false
        endpoint: example_endpoint
  instrumentation:
    events:
      connector:
        error:
          condition:
            eq:
            - false
            - false
          level: info
        request:
          condition:
            eq:
            - false
            - false
          level: info
        response:
          condition:
            eq:
            - false
            - false
          level: info
      router:
        error:
          condition:
            eq:
            - false
            - false
          level: info
        request:
          condition:
            eq:
            - false
            - false
          level: info
        response:
          condition:
            eq:
            - false
            - false
          level: info
      subgraph:
        error:
          condition:
            eq:
            - false
            - false
          level: info
        request:
          condition:
            eq:
            - false
            - false
          level: info
        response:
          condition:
            eq:
            - false
            - false
          level: info
      supergraph:
        error:
          condition:
            eq:
            - false
            - false
          level: info
        request:
          condition:
            eq:
            - false
            - false
          level: info
        response:
          condition:
            eq:
            - false
            - false
          level: info
    instruments:
      cache:
        apollo.router.operations.entity.cache:
          attributes:
            graphql.type.name:
              alias: example_alias
      connector:
        http.client.request.body.size:
          attributes:
            connector.http.method:
              alias: example_alias
            connector.source.name:
              alias: example_alias
            connector.url.template:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.request.duration:
          attributes:
            connector.http.method:
              alias: example_alias
            connector.source.name:
              alias: example_alias
            connector.url.template:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.response.body.size:
          attributes:
            connector.http.method:
              alias: example_alias
            connector.source.name:
              alias: example_alias
            connector.url.template:
              alias: example_alias
            subgraph.name:
              alias: example_alias
      default_requirement_level: none
      graphql:
        field.execution:
          attributes:
            graphql.field.name:
              alias: example_alias
            graphql.field.type:
              alias: example_alias
            graphql.list.length:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.type.name:
              alias: example_alias
        list.length:
          attributes:
            graphql.field.name:
              alias: example_alias
            graphql.field.type:
              alias: example_alias
            graphql.list.length:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.type.name:
              alias: example_alias
      router:
        http.server.active_requests:
          attributes:
            http.request.method: false
            server.address: false
            server.port: false
            url.scheme: false
        http.server.request.body.size:
          attributes:
            baggage: null
            dd.trace_id:
              alias: example_alias
            error.type:
              alias: example_alias
            http.request.body.size:
              alias: example_alias
            http.request.method:
              alias: example_alias
            http.response.body.size:
              alias: example_alias
            http.response.status_code:
              alias: example_alias
            http.route:
              alias: example_alias
            network.local.address:
              alias: example_alias
            network.local.port:
              alias: example_alias
            network.peer.address:
              alias: example_alias
            network.peer.port:
              alias: example_alias
            network.protocol.name:
              alias: example_alias
            network.protocol.version:
              alias: example_alias
            network.transport:
              alias: example_alias
            network.type:
              alias: example_alias
            server.address:
              alias: example_alias
            server.port:
              alias: example_alias
            trace_id:
              alias: example_alias
            url.path:
              alias: example_alias
            url.query:
              alias: example_alias
            url.scheme:
              alias: example_alias
            user_agent.original:
              alias: example_alias
        http.server.request.duration:
          attributes:
            baggage: null
            dd.trace_id:
              alias: example_alias
            error.type:
              alias: example_alias
            http.request.body.size:
              alias: example_alias
            http.request.method:
              alias: example_alias
            http.response.body.size:
              alias: example_alias
            http.response.status_code:
              alias: example_alias
            http.route:
              alias: example_alias
            network.local.address:
              alias: example_alias
            network.local.port:
              alias: example_alias
            network.peer.address:
              alias: example_alias
            network.peer.port:
              alias: example_alias
            network.protocol.name:
              alias: example_alias
            network.protocol.version:
              alias: example_alias
            network.transport:
              alias: example_alias
            network.type:
              alias: example_alias
            server.address:
              alias: example_alias
            server.port:
              alias: example_alias
            trace_id:
              alias: example_alias
            url.path:
              alias: example_alias
            url.query:
              alias: example_alias
            url.scheme:
              alias: example_alias
            user_agent.original:
              alias: example_alias
        http.server.response.body.size:
          attributes:
            baggage: null
            dd.trace_id:
              alias: example_alias
            error.type:
              alias: example_alias
            http.request.body.size:
              alias: example_alias
            http.request.method:
              alias: example_alias
            http.response.body.size:
              alias: example_alias
            http.response.status_code:
              alias: example_alias
            http.route:
              alias: example_alias
            network.local.address:
              alias: example_alias
            network.local.port:
              alias: example_alias
            network.peer.address:
              alias: example_alias
            network.peer.port:
              alias: example_alias
            network.protocol.name:
              alias: example_alias
            network.protocol.version:
              alias: example_alias
            network.transport:
              alias: example_alias
            network.type:
              alias: example_alias
            server.address:
              alias: example_alias
            server.port:
              alias: example_alias
            trace_id:
              alias: example_alias
            url.path:
              alias: example_alias
            url.query:
              alias: example_alias
            url.scheme:
              alias: example_alias
            user_agent.original:
              alias: example_alias
      subgraph:
        http.client.request.body.size:
          attributes:
            http.request.resend_count:
              alias: example_alias
            subgraph.graphql.document:
              alias: example_alias
            subgraph.graphql.operation.name:
              alias: example_alias
            subgraph.graphql.operation.type:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.request.duration:
          attributes:
            http.request.resend_count:
              alias: example_alias
            subgraph.graphql.document:
              alias: example_alias
            subgraph.graphql.operation.name:
              alias: example_alias
            subgraph.graphql.operation.type:
              alias: example_alias
            subgraph.name:
              alias: example_alias
        http.client.response.body.size:
          attributes:
            http.request.resend_count:
              alias: example_alias
            subgraph.graphql.document:
              alias: example_alias
            subgraph.graphql.operation.name:
              alias: example_alias
            subgraph.graphql.operation.type:
              alias: example_alias
            subgraph.name:
              alias: example_alias
      supergraph:
        cost.actual:
          attributes:
            cost.actual:
              alias: example_alias
            cost.delta:
              alias: example_alias
            cost.estimated:
              alias: example_alias
            cost.result:
              alias: example_alias
            graphql.document:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.operation.type:
              alias: example_alias
        cost.delta:
          attributes:
            cost.actual:
              alias: example_alias
            cost.delta:
              alias: example_alias
            cost.estimated:
              alias: example_alias
            cost.result:
              alias: example_alias
            graphql.document:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.operation.type:
              alias: example_alias
        cost.estimated:
          attributes:
            cost.actual:
              alias: example_alias
            cost.delta:
              alias: example_alias
            cost.estimated:
              alias: example_alias
            cost.result:
              alias: example_alias
            graphql.document:
              alias: example_alias
            graphql.operation.name:
              alias: example_alias
            graphql.operation.type:
              alias: example_alias
    spans:
      connector:
        attributes:
          connector.http.method:
            alias: example_alias
          connector.source.name:
            alias: example_alias
          connector.url.template:
            alias: example_alias
          subgraph.name:
            alias: example_alias
      default_attribute_requirement_level: none
      mode: deprecated
      router:
        attributes:
          baggage: null
          dd.trace_id:
            alias: example_alias
          error.type:
            alias: example_alias
          http.request.body.size:
            alias: example_alias
          http.request.method:
            alias: example_alias
          http.response.body.size:
            alias: example_alias
          http.response.status_code:
            alias: example_alias
          http.route:
            alias: example_alias
          network.local.address:
            alias: example_alias
          network.local.port:
            alias: example_alias
          network.peer.address:
            alias: example_alias
          network.peer.port:
            alias: example_alias
          network.protocol.name:
            alias: example_alias
          network.protocol.version:
            alias: example_alias
          network.transport:
            alias: example_alias
          network.type:
            alias: example_alias
          server.address:
            alias: example_alias
          server.port:
            alias: example_alias
          trace_id:
            alias: example_alias
          url.path:
            alias: example_alias
          url.query:
            alias: example_alias
          url.scheme:
            alias: example_alias
          user_agent.original:
            alias: example_alias
      subgraph:
        attributes:
          http.request.resend_count:
            alias: example_alias
          subgraph.graphql.document:
            alias: example_alias
          subgraph.graphql.operation.name:
            alias: example_alias
          subgraph.graphql.operation.type:
            alias: example_alias
          subgraph.name:
            alias: example_alias
      supergraph:
        attributes:
          cost.actual:
            alias: example_alias
          cost.delta:
            alias: example_alias
          cost.estimated:
            alias: example_alias
          cost.result:
            alias: example_alias
          graphql.document:
            alias: example_alias
          graphql.operation.name:
            alias: example_alias
          graphql.operation.type:
            alias: example_alias
```

#### Enhanced operation signature normalization

The router supports enhanced operation signature normalization in the following versions:

* [General availability](https://www.apollographql.com/docs/resources/product-launch-stages/#general-availability) in v1.54.0 and later
* [Experimental](https://www.apollographql.com/docs/resources/product-launch-stages/#experimental-features) in v1.49.0 to v1.53.0

Apollo's legacy operation signature algorithm removes information about certain fields, such as input objects and aliases.
This removal means some operations may have the same normalized signature though they are distinct operations.

Enhanced normalization incorporates [input types](https://www.apollographql.com/docs/graphos/routing/configuration/yaml.md#input-types) and [aliases](https://www.apollographql.com/docs/graphos/routing/configuration/yaml.md#aliases) in signature generation.
It also includes other improvements that make it more likely that two operations that only vary slightly have the same signature.

Configure enhanced operation signature normalization in `router.yaml` with the `telemetry.apollo.signature_normalization_algorithm` option:

```yaml title=router.yaml
telemetry:
  apollo:
    signature_normalization_algorithm: enhanced # Default is legacy
```

Once you enable this configuration, operations with enhanced signatures might appear with different operation IDs than they did previously in GraphOS Studio.

##### Input types

Enhanced signatures include input object type shapes, while still redacting any actual values.
Legacy signatures [replace input object type with `{}`](https://www.apollographql.com/docs/graphos/metrics/operation-signatures/#1-transform-in-line-argument-values).

Given the following example operation:

```graphql
query InlineInputTypeQuery {
  inputTypeQuery(
    input: {
      inputString: "foo"
      inputInt: 42
      inputBoolean: null
      nestedType: { someFloat: 4.2 }
      enumInput: SOME_VALUE_1
      nestedTypeList: [{ someFloat: 4.2, someNullableFloat: null }]
      listInput: [1, 2, 3]
    }
  ) {
    enumResponse
  }
}
```

The legacy normalization algorithm generates the following signature:

```graphql
query InlineInputTypeQuery {
  inputTypeQuery(input: {}) {
    enumResponse
  }
}
```

The enhanced normalization algorithm generates the following signature:

```graphql
query InlineInputTypeQuery {
  inputTypeQuery(
    input: {
      inputString: ""
      inputInt: 0
      inputBoolean: null
      nestedType: { someFloat: 0 }
      enumInput: SOME_VALUE_1
      nestedTypeList: [{ someFloat: 0, someNullableFloat: null }]
      listInput: []
    }
  ) {
    enumResponse
  }
}
```

##### Aliases

Enhanced signatures include any field aliases used in an operation.
Legacy signatures [remove aliases completely](https://www.apollographql.com/docs/graphos/metrics/operation-signatures/#field-aliases), meaning the signature may be invalid if the same field was used with multiple aliases.

Given the following example operation:

```graphql
query AliasedQuery {
  noInputQuery {
    interfaceAlias1: interfaceResponse {
      sharedField
    }
    interfaceAlias2: interfaceResponse {
      ... on InterfaceImplementation1 {
        implementation1Field
      }
      ... on InterfaceImplementation2 {
        implementation2Field
      }
    }
    inputFieldAlias1: objectTypeWithInputField(boolInput: true) {
      stringField
    }
    inputFieldAlias2: objectTypeWithInputField(boolInput: false) {
      intField
    }
  }
}
```

The legacy normalization algorithm generates the following signature:

```graphql
query AliasedQuery {
  noInputQuery {
    interfaceResponse {
      sharedField
    }
    interfaceResponse {
      ... on InterfaceImplementation1 {
        implementation1Field
      }
      ... on InterfaceImplementation2 {
        implementation2Field
      }
    }
    objectTypeWithInputField(boolInput: true) {
      stringField
    }
    objectTypeWithInputField(boolInput: false) {
      intField
    }
  }
}
```

The enhanced normalization algorithm generates the following signature:

```graphql
query AliasedQuery {
  noInputQuery {
    interfaceAlias1: interfaceResponse {
      sharedField
    }
    interfaceAlias2: interfaceResponse {
      ... on InterfaceImplementation1 {
        implementation1Field
      }
      ... on InterfaceImplementation2 {
        implementation2Field
      }
    }
    inputFieldAlias1: objectTypeWithInputField(boolInput: true) {
      stringField
    }
    inputFieldAlias2: objectTypeWithInputField(boolInput: false) {
      intField
    }
  }
}
```

#### Extended reference reporting

The router supports extended reference reporting in the following versions:

* [General availability](https://www.apollographql.com/docs/resources/product-launch-stages/#general-availability) in v1.54.0 and later
* [Experimental](https://www.apollographql.com/docs/resources/product-launch-stages/#experimental-features) in v1.50.0 to v1.53.0

You can configure the router to report enum and input object references for enhanced insights and operation checks.
Apollo's legacy reference reporting doesn't include data about enum values and input object fields, meaning you can't view enum and input object field usage in GraphOS Studio.
Legacy reporting can also cause [inaccurate operation checks](https://www.apollographql.com/docs/graphos/routing/configuration/yaml.md#enhanced-operation-checks).

Configure extended reference reporting in `router.yaml` with the `telemetry.apollo.metrics_reference_mode` option like so:

```yaml title=router.yaml
telemetry:
  apollo:
    metrics_reference_mode: extended # Default is legacy
```

#### Extended error reporting

The router supports extended error reporting in the following versions:

* [Preview](https://www.apollographql.com/docs/resources/product-launch-stages/#preview) in v2.1.2 and later
* [Experimental](https://www.apollographql.com/docs/resources/product-launch-stages/#experimental-features) in v2.0.0

You can configure the router to report extended error information for improved diagnostics.
Apollo's legacy error reporting doesn't include the service or error code, meaning you can't easily attribute errors to their root cause in GraphOS Studio.

Configure extended reference reporting in `router.yaml` with the `telemetry.apollo.errors.preview_extended_error_metrics` option like so:

```yaml title=router.yaml
telemetry:
  apollo:
    errors:
      preview_extended_error_metrics: enabled # Default is disabled
```

[Learn more.](https://www.apollographql.com/docs/graphos/routing/graphos-reporting#errors)

##### Configuration effect timing

Once you configure extended reference reporting, you can view enum value and input field usage alongside object [field usage in GraphOS Studio](https://www.apollographql.com/docs/graphos/metrics/field-usage) for all subsequent operations.

Configuring extended reference reporting automatically turns on [enhanced operation checks](https://www.apollographql.com/docs/graphos/routing/configuration/yaml.md#enhanced-operation-checks), though you won't see an immediate change in your operations check behavior.

This delay is because operation checks rely on historical operation data.
To ensure sufficient data to distinguish between genuinely unused values and those simply not reported in legacy data, enhanced checks require some operations with extended reference reporting turned on.

##### Enhanced operation checks

Thanks to extended reference reporting, operation checks can more accurately flag issues for changes to enum values and input object fields. See the comparison table below for differences between standard operation checks based on legacy reference reporting and enhanced checks based on extended reference reporting.

Standard Check Behavior
(Legacy reference reporting)

Enhanced Check Behavior
(Extended reference reporting)

###### Enum value removal

Removing any enum values is considered a breaking change if any operations use the enum.
Removing enum values is only a breaking change if historical operations use the specific enum value(s) that were removed.

###### Default argument changes for input object fields

Changing or removing a default argument is generally considered a breaking change, but changing or removing default values for input object fields isn't.

Changing or removing default values for input object fields is considered a breaking change.

You can [configure checks to ignore default values changes](https://www.apollographql.com/docs/graphos/platform/schema-management/checks#ignored-conditions-settings).

###### Nullable input object field removal

Removing a nullable input object field is always considered a breaking change.
Removing a nullable input object field is only considered a breaking change if the nullable field is present in historical operations. If the nullable field is always omitted in historical operations, its removal isn't considered a breaking change.

###### Changing nullable input object fields to non-nullable

Changing a nullable input object field to non-nullable is considered a breaking change.
Changing a nullable input object field to non-nullable is only considered a breaking change if the field had a null value in historical operations. If the field was always a non-null value in historical operations, changing it to non-nullable isn't considered a breaking change.

You won't see an immediate change in checks behavior when you first turn on extended reference reporting.
[Learn more.](https://www.apollographql.com/docs/graphos/routing/configuration/yaml.md#configuration-effect-timing)

***

### `tls`

```yaml title=tls
tls:
  connector:
    all:
      certificate_authorities: null
      client_authentication:
        certificate_chain: example_certificate_chain
        key: example_key
    sources: {}
  subgraph:
    all:
      certificate_authorities: null
      client_authentication:
        certificate_chain: example_certificate_chain
        key: example_key
    subgraphs: {}
  supergraph:
    certificate: example_certificate
    certificate_chain: example_certificate_chain
    key: example_key
```

Learn more in [TLS for the router](https://www.apollographql.com/docs/graphos/routing/security/tls).

***

### `traffic_shaping`

```yaml title=traffic_shaping
traffic_shaping:
  all:
    compression: gzip
    deduplicate_query: false
    dns_resolution_strategy: ipv4_only
    experimental_http2: enable
    global_rate_limit:
      capacity: 1
      interval: 30s
    timeout: null
  connector:
    all:
      compression: gzip
      dns_resolution_strategy: ipv4_only
      experimental_http2: enable
      global_rate_limit:
        capacity: 1
        interval: 30s
      timeout: null
    sources: {}
  deduplicate_variables: null
  router:
    concurrency_limit: 0
    global_rate_limit:
      capacity: 1
      interval: 30s
    timeout: null
  subgraphs: {}
```

Learn more in [Traffic Shaping](https://www.apollographql.com/docs/graphos/routing/performance/traffic-shaping).

***

## YAML configuration utilities

### Variable expansion

You can reference variables directly in your YAML config file. This is useful for referencing secrets without including them in the file.

Currently, the router supports expansion of environment variables and file paths. Corresponding variables are prefixed with `env.` and `file.`, respectively.

The router uses Unix-style expansion. Here are some examples:

* `${env.ENV_VAR_NAME}` expands to the value of environment variable `ENV_VAR_NAME`.
* `${env.ENV_VAR_NAME:-some_default}` expands to the value of environment variable `ENV_VAR_NAME`, or falls back to the value `some_default` if the environment variable is not defined.
* `${file.a.txt}` expands to the contents of the file `a.txt`.
* `${file.a.txt:-some_default}` expands to the contents of the file `a.txt`, or falls back to the value `some_default` if the file does not exist.

Variable expansions are valid only for YAML *values*, not keys.

### Reusing configurations with YAML aliases

You can reuse parts of your configuration file in multiple places using standard YAML aliasing syntax:

```yaml title=router.yaml
headers:
  subgraphs:
    products:
      request:
        - insert: &insert_custom_header
            name: "custom-header"
            value: "something"
    reviews:
      request:
        - insert: *insert_custom_header
```

Here, the `name` and `value` entries under `&insert_custom_header` are reused under `*insert_custom_header`.

### Escaping special characters

To include a literal `$` character, double it as `$$`. The router converts each `$$` to a single `$`:

* Config value: `prefix$$suffix`
* Result: `prefix$suffix`

## Related topics

* [Checklist for configuring the router for production](https://www.apollographql.com/docs/technotes/TN0008-production-readiness-checklist/#apollo-router)

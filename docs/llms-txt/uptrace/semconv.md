# Source: https://uptrace.dev/raw/opentelemetry/semconv.md

# Source: https://uptrace.dev/raw/features/querying/semconv.md

# OpenTelemetry semantic attributes convention

> Understand the OpenTelemetry semantic conventions Uptrace normalizes, including version specific renames and attribute aliases.

## What are semantic attributes?

OpenTelemetry [semantic attribute conventions](/opentelemetry/semconv) are standardized naming and value specifications for telemetry data attributes across traces, metrics, and logs. These conventions ensure consistency and interoperability when instrumenting applications and services.

Attributes use dot-notation namespacing (e.g., `http.method`, `db.connection_string`) and follow consistent naming patterns. The conventions specify not only attribute names but also their expected values, data types, and appropriate usage contexts.

To maintain compatibility with other tools like Prometheus and Tempo, Uptrace replaces dots with underscores in attribute names. For example, `service.name` becomes `service_name`.

## Evolution

The semantic conventions are actively maintained and [versioned](https://github.com/open-telemetry/semantic-conventions/releases) separately from the OpenTelemetry specification. They continue to expand to cover new technologies, protocols, and use cases while maintaining backward compatibility where possible.

To simplify migration between different versions, Uptrace allows you to select your desired semantic convention version on the Project Settings page. Once selected, Uptrace automatically renames certain attributes to follow the chosen convention. For example, it will rename `deployment_environment` to `deployment_environment_name`.

Uptrace does not modify existing rules to avoid breaking current queries, but we welcome suggestions for changes to include in the next supported version.

### v1.33.0

<table>
<thead>
  <tr>
    <th>
      Normalized attr name
    </th>
    
    <th>
      Candidates
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      deployment_environment_name
    </td>
    
    <td>
      deployment_environment, environment, env
    </td>
  </tr>
  
  <tr>
    <td>
      service_name
    </td>
    
    <td>
      service, appname, application_name, fly_app_name
    </td>
  </tr>
  
  <tr>
    <td>
      host_name
    </td>
    
    <td>
      hostname, host_hostname, host
    </td>
  </tr>
  
  <tr>
    <td>
      db_namespace
    </td>
    
    <td>
      db_name, db_cassandra_keyspace, db_hbase_namespace, dbname
    </td>
  </tr>
  
  <tr>
    <td>
      db_system_name
    </td>
    
    <td>
      db_system, db_type, db_dbms
    </td>
  </tr>
  
  <tr>
    <td>
      db_collection_name
    </td>
    
    <td>
      db_sql_table
    </td>
  </tr>
  
  <tr>
    <td>
      db_operation_name
    </td>
    
    <td>
      db_operation
    </td>
  </tr>
  
  <tr>
    <td>
      db_query_text
    </td>
    
    <td>
      db_statement
    </td>
  </tr>
  
  <tr>
    <td>
      http_request_method
    </td>
    
    <td>
      http_method, request_method, method
    </td>
  </tr>
  
  <tr>
    <td>
      http_route
    </td>
    
    <td>
      http_server_route, route
    </td>
  </tr>
  
  <tr>
    <td>
      log_severity
    </td>
    
    <td>
      severity, error_severity, log_level, level
    </td>
  </tr>
  
  <tr>
    <td>
      log_source
    </td>
    
    <td>
      source_type, facility
    </td>
  </tr>
  
  <tr>
    <td>
      log_file_path
    </td>
    
    <td>
      log_filepath, log_file
    </td>
  </tr>
  
  <tr>
    <td>
      code_function_name
    </td>
    
    <td>
      code_function
    </td>
  </tr>
  
  <tr>
    <td>
      code_file_path
    </td>
    
    <td>
      code_filepath
    </td>
  </tr>
  
  <tr>
    <td>
      code_line_number
    </td>
    
    <td>
      code_lineno
    </td>
  </tr>
  
  <tr>
    <td>
      process_pid
    </td>
    
    <td>
      procid, pid
    </td>
  </tr>
  
  <tr>
    <td>
      server_address
    </td>
    
    <td>
      net_host_name, http_server_name, http_host
    </td>
  </tr>
  
  <tr>
    <td>
      client_address
    </td>
    
    <td>
      http_client_ip, net_peer_name, ip
    </td>
  </tr>
  
  <tr>
    <td>
      messaging_message_id
    </td>
    
    <td>
      message_id, msgid
    </td>
  </tr>
  
  <tr>
    <td>
      grouping_fingerprint
    </td>
    
    <td>
      log_fingerprint, exception_fingerprint
    </td>
  </tr>
</tbody>
</table>

### v1.25.0

<table>
<thead>
  <tr>
    <th>
      Normalized attr name
    </th>
    
    <th>
      Candidates
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      deployment_environment
    </td>
    
    <td>
      deployment_environment_name, environment, env
    </td>
  </tr>
  
  <tr>
    <td>
      service_name
    </td>
    
    <td>
      service, appname, application_name, fly_app_name
    </td>
  </tr>
  
  <tr>
    <td>
      host_name
    </td>
    
    <td>
      hostname, host_hostname, host
    </td>
  </tr>
  
  <tr>
    <td>
      enduser_id
    </td>
    
    <td>
      user_id, user_identifier, user
    </td>
  </tr>
  
  <tr>
    <td>
      db_name
    </td>
    
    <td>
      db_cassandra_keyspace, db_hbase_namespace, dbname
    </td>
  </tr>
  
  <tr>
    <td>
      db_system
    </td>
    
    <td>
      db_type, db_dbms
    </td>
  </tr>
  
  <tr>
    <td>
      http_request_method
    </td>
    
    <td>
      http_method, request_method, method
    </td>
  </tr>
  
  <tr>
    <td>
      http_route
    </td>
    
    <td>
      http_server_route, route
    </td>
  </tr>
  
  <tr>
    <td>
      http_response_status_code
    </td>
    
    <td>
      http_status_code
    </td>
  </tr>
  
  <tr>
    <td>
      http_request_body_size
    </td>
    
    <td>
      http_request_content_length
    </td>
  </tr>
  
  <tr>
    <td>
      http_response_body_size
    </td>
    
    <td>
      http_response_content_length
    </td>
  </tr>
  
  <tr>
    <td>
      log_severity
    </td>
    
    <td>
      severity, error_severity, log_level, level
    </td>
  </tr>
  
  <tr>
    <td>
      log_source
    </td>
    
    <td>
      source_type, facility
    </td>
  </tr>
  
  <tr>
    <td>
      log_file_path
    </td>
    
    <td>
      log_filepath, log_file
    </td>
  </tr>
  
  <tr>
    <td>
      cloud_region
    </td>
    
    <td>
      fly_region
    </td>
  </tr>
  
  <tr>
    <td>
      cloud_resource_id
    </td>
    
    <td>
      faas_id
    </td>
  </tr>
  
  <tr>
    <td>
      cloud_availability_zone
    </td>
    
    <td>
      cloud_zone
    </td>
  </tr>
  
  <tr>
    <td>
      process_pid
    </td>
    
    <td>
      procid, pid
    </td>
  </tr>
  
  <tr>
    <td>
      url_scheme
    </td>
    
    <td>
      http_scheme
    </td>
  </tr>
  
  <tr>
    <td>
      url_full
    </td>
    
    <td>
      http_url
    </td>
  </tr>
  
  <tr>
    <td>
      url_path
    </td>
    
    <td>
      http_target, request
    </td>
  </tr>
  
  <tr>
    <td>
      faas_invocation_id
    </td>
    
    <td>
      faas_execution
    </td>
  </tr>
  
  <tr>
    <td>
      user_agent_original
    </td>
    
    <td>
      http_user_agent, browser_user_agent, user_agent
    </td>
  </tr>
  
  <tr>
    <td>
      network_protocol_name
    </td>
    
    <td>
      net_app_protocol_name, messaging_protocol, http_flavor
    </td>
  </tr>
  
  <tr>
    <td>
      network_protocol_version
    </td>
    
    <td>
      net_app_protocol_version, messaging_protocol_version
    </td>
  </tr>
  
  <tr>
    <td>
      network_transport
    </td>
    
    <td>
      net_transport
    </td>
  </tr>
  
  <tr>
    <td>
      server_address
    </td>
    
    <td>
      net_host_name, http_server_name, http_host
    </td>
  </tr>
  
  <tr>
    <td>
      server_port
    </td>
    
    <td>
      net_host_port
    </td>
  </tr>
  
  <tr>
    <td>
      server_socket_domain
    </td>
    
    <td>
      net_sock_peer_name
    </td>
  </tr>
  
  <tr>
    <td>
      server_socket_address
    </td>
    
    <td>
      net_host_ip, net_sock_host_addr
    </td>
  </tr>
  
  <tr>
    <td>
      server_socket_port
    </td>
    
    <td>
      net_host_port, net_sock_host_port
    </td>
  </tr>
  
  <tr>
    <td>
      client_address
    </td>
    
    <td>
      http_client_ip, net_peer_name, ip
    </td>
  </tr>
  
  <tr>
    <td>
      client_socket_address
    </td>
    
    <td>
      net_peer_ip, net_sock_peer_addr
    </td>
  </tr>
  
  <tr>
    <td>
      client_socket_port
    </td>
    
    <td>
      net_peer_port, net_sock_peer_port
    </td>
  </tr>
  
  <tr>
    <td>
      messaging_destination_name
    </td>
    
    <td>
      messaging_destination
    </td>
  </tr>
  
  <tr>
    <td>
      messaging_destination_kind
    </td>
    
    <td>
      messaging_destination_kind
    </td>
  </tr>
  
  <tr>
    <td>
      messaging_message_id
    </td>
    
    <td>
      message_id, msgid
    </td>
  </tr>
  
  <tr>
    <td>
      messaging_message_type
    </td>
    
    <td>
      message_type
    </td>
  </tr>
  
  <tr>
    <td>
      messaging_message_payload_size_bytes
    </td>
    
    <td>
      message_uncompressed_size
    </td>
  </tr>
  
  <tr>
    <td>
      grouping_fingerprint
    </td>
    
    <td>
      log_fingerprint, exception_fingerprint
    </td>
  </tr>
</tbody>
</table>

## Indexed attributes

To store data, Uptrace uses ClickHouse, a columnar database that stores data in columns rather than rows. This means that instead of storing all data for a single record together, each column is stored separately.

To improve query performance, Uptrace places some attributes into separate columns. However, Uptrace cannot place all attributes into separate columns because it doesn't know the complete list of attributes in advance, and this list can become very large with thousands of attributes.

<table>
<thead>
  <tr>
    <th>
      Attribute
    </th>
    
    <th>
      Spans
    </th>
    
    <th>
      Logs
    </th>
    
    <th>
      Events
    </th>
    
    <th>
      Preaggregated
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      deployment_environment
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
  </tr>
  
  <tr>
    <td>
      service_namespace
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
  </tr>
  
  <tr>
    <td>
      service_name
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
  </tr>
  
  <tr>
    <td>
      service_version
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
  </tr>
  
  <tr>
    <td>
      host_name
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
  </tr>
  
  <tr>
    <td>
      telemetry_sdk_name
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      telemetry_sdk_language
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      telemetry_sdk_version
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      telemetry_auto_version
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      otel_library_name
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      otel_library_version
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      client_address
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      client_socket_address
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      client_socket_port
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      db_system
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      db_name
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      db_sql_table
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      db_statement
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      db_operation
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      process_pid
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      process_command
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      process_runtime_name
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      process_runtime_version
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      process_runtime_description
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      log_severity
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      log_file_path
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      log_file_name
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      log_iostream
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      log_source
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      exception_type
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      exception_message
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      messaging_message_id
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      messaging_message_type
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      messaging_message_payload_size_bytes
    </td>
    
    <td>
      
    </td>
    
    <td>
      
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

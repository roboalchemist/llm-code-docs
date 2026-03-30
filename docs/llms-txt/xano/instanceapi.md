# Source: https://docs.xano.com/xano-features/metadata-api/instanceapi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Xano Metadata API (Instances)

> Endpoints for browsing and managing instances via the Metadata API.

# Overview

The **Instance endpoints** allow you to **browse**, **inspect**, and **retrieve metadata** for your Xano instances.\
All endpoints use **Bearer access tokens** for authentication.

**Base URL:** Your base URL is the URL of your Xano instance.

***

# API Endpoints

## Authentication

<CardGroup cols={2}>
  <Card title="Retrieve information about the authenticated user including ID, name, and email address" icon="user" href="/xano-features/metadata-api/instance_api/retrieve_information_about_the_authenticated_user_including_id_name_and_email_address">
    Returns the authenticated user's basic account information
  </Card>

  <Card title="Retrieve all accessible workspaces for the authenticated user" icon="user" href="/xano-features/metadata-api/instance_api/retrieve_all_accessible_workspaces_for_the_authenticated_user">
    Returns all workspaces accessible to the authenticated user
  </Card>
</CardGroup>

## Workspace Management

<CardGroup cols={2}>
  <Card title="Retrieve detailed information about a specific workspace" icon="building" href="/xano-features/metadata-api/instance_api/retrieve_detailed_information_about_a_specific_workspace">
    Returns detailed information about a specific workspace
  </Card>

  <Card title="Retrieve all branches in a workspace" icon="building" href="/xano-features/metadata-api/instance_api/retrieve_all_branches_in_a_workspace">
    Returns all branches in a workspace
  </Card>

  <Card title="Delete a workspace branch cannot delete the default branch or currently live branch" icon="building" href="/xano-features/metadata-api/instance_api/delete_a_workspace_branch_cannot_delete_the_default_branch_or_currently_live_branch">
    Deletes a workspace branch (cannot delete default or live branch)
  </Card>

  <Card title="Retrieve all external data sources for a workspace" icon="building" href="/xano-features/metadata-api/instance_api/retrieve_all_external_data_sources_for_a_workspace">
    Returns all external data sources for a workspace
  </Card>

  <Card title="Create a new external data source with custom label and color" icon="building" href="/xano-features/metadata-api/instance_api/create_a_new_external_data_source_with_custom_label_and_color">
    Creates a new external data source with custom label and color
  </Card>

  <Card title="Update an existing data sources label and color properties" icon="building" href="/xano-features/metadata-api/instance_api/update_an_existing_data_sources_label_and_color_properties">
    Updates an existing data source's label and color properties
  </Card>

  <Card title="Delete a data source permanently this action cannot be undone" icon="building" href="/xano-features/metadata-api/instance_api/delete_a_data_source_permanently_this_action_cannot_be_undone">
    Deletes a data source permanently (cannot be undone)
  </Card>

  <Card title="Export complete workspace data and configuration as an archive" icon="building" href="/xano-features/metadata-api/instance_api/export_complete_workspace_data_and_configuration_as_an_archive">
    Exports complete workspace data and configuration as an archive
  </Card>

  <Card title="Export database table schemas and branch configuration as a file" icon="building" href="/xano-features/metadata-api/instance_api/export_database_table_schemas_and_branch_configuration_as_a_file">
    Exports database table schemas and branch configuration as a file
  </Card>

  <Card title="Import database schema into a new branch with optional deployment" icon="building" href="/xano-features/metadata-api/instance_api/import_database_schema_into_a_new_branch_with_optional_deployment">
    Imports database schema into a new branch with optional deployment
  </Card>

  <Card title="Replace workspace content and configuration with imported archive" icon="building" href="/xano-features/metadata-api/instance_api/replace_workspace_content_and_configuration_with_imported_archive">
    Replaces workspace content and configuration with imported archive
  </Card>

  <Card title="Upload files to workspace" icon="building" href="/xano-features/metadata-api/instance_api/upload_files_to_workspace">
    Uploads files to workspace
  </Card>

  <Card title="Retrieve workspace files with optional search filtering and pagination" icon="building" href="/xano-features/metadata-api/instance_api/retrieve_workspace_files_with_optional_search_filtering_and_pagination">
    Returns workspace files with optional search filtering and pagination
  </Card>

  <Card title="Delete a file permanently this action cannot be undone" icon="building" href="/xano-features/metadata-api/instance_api/delete_a_file_permanently_this_action_cannot_be_undone">
    Deletes a file permanently (cannot be undone)
  </Card>

  <Card title="Delete multiple files permanently this action cannot be undone" icon="building" href="/xano-features/metadata-api/instance_api/delete_multiple_files_permanently_this_action_cannot_be_undone">
    Deletes multiple files permanently (cannot be undone)
  </Card>

  <Card title="Update workspace tables autocomplete" icon="building" href="/xano-features/metadata-api/instance_api/update_workspace_tables_autocomplete">
    Updates workspace tables autocomplete
  </Card>

  <Card title="Update workspace table" icon="building" href="/xano-features/metadata-api/instance_api/update_workspace_table">
    Updates workspace table
  </Card>
</CardGroup>

## API Groups & Endpoints

<CardGroup cols={2}>
  <Card title="Create a new API group in a workspace include name description and optional tags" icon="api" href="/xano-features/metadata-api/instance_api/create_a_new_api_group_in_a_workspace_include_name_description_and_optional_tags">
    Creates a new API group in a workspace with name, description and optional tags
  </Card>

  <Card title="Retrieve a list of API groups inside of a workspace use the optional filtering and sorting parameters for more granular returns" icon="api" href="/xano-features/metadata-api/instance_api/retrieve_a_list_of_api_groups_inside_of_a_workspace_use_the_optional_filtering_and_sorting_parameters_for_more_granular_returns">
    Returns a list of API groups in a workspace with optional filtering and sorting
  </Card>

  <Card title="Get detailed information for a specific API group returns complete metadata and configuration" icon="api" href="/xano-features/metadata-api/instance_api/get_detailed_information_for_a_specific_api_group_returns_complete_metadata_and_configuration">
    Returns detailed information for a specific API group
  </Card>

  <Card title="Update an existing API group modify name description documentation settings or tags" icon="api" href="/xano-features/metadata-api/instance_api/update_an_existing_api_group_modify_name_description_documentation_settings_or_tags">
    Updates an existing API group settings
  </Card>

  <Card title="Delete an API group and all its endpoints this action cannot be undone" icon="api" href="/xano-features/metadata-api/instance_api/delete_an_api_group_and_all_its_endpoints_this_action_cannot_be_undone">
    Deletes an API group and all its endpoints (cannot be undone)
  </Card>

  <Card title="Get the OpenAPI specification for an API group returns the complete Swagger JSON for all endpoints" icon="api" href="/xano-features/metadata-api/instance_api/get_the_openapi_specification_for_an_api_group_returns_the_complete_swagger_json_for_all_endpoints">
    Returns the complete OpenAPI specification for an API group
  </Card>

  <Card title="Update security settings for an API group configure access permissions and authentication requirements" icon="api" href="/xano-features/metadata-api/instance_api/update_security_settings_for_an_api_group_configure_access_permissions_and_authentication_requirements">
    Updates security settings for an API group
  </Card>

  <Card title="Create a new API endpoint" icon="api" href="/xano-features/metadata-api/instance_api/create_a_new_api_endpoint_using_xanoscript">
    Creates a new API endpoint
  </Card>

  <Card title="Retrieve all API endpoints in a group with optional filtering and pagination" icon="api" href="/xano-features/metadata-api/instance_api/retrieve_all_api_endpoints_in_a_group_with_optional_filtering_and_pagination">
    Returns all API endpoints in a group with optional filtering and pagination
  </Card>

  <Card title="Retrieve a specific API endpoint by ID" icon="api" href="/xano-features/metadata-api/instance_api/retrieve_a_specific_api_endpoint_by_id">
    Returns a specific API endpoint by ID
  </Card>

  <Card title="Update API endpoint code settings and authentication rules" icon="api" href="/xano-features/metadata-api/instance_api/update_api_endpoint_code_settings_and_authentication_rules">
    Updates API endpoint code settings and authentication rules
  </Card>

  <Card title="Update API endpoint security configuration and access controls" icon="api" href="/xano-features/metadata-api/instance_api/update_api_endpoint_security_configuration_and_access_controls">
    Updates API endpoint security configuration and access controls
  </Card>

  <Card title="Generate OpenAPI specification for a specific API endpoint" icon="api" href="/xano-features/metadata-api/instance_api/generate_openapi_specification_for_a_specific_api_endpoint">
    Generates OpenAPI specification for a specific API endpoint
  </Card>

  <Card title="Delete an API endpoint permanently this action cannot be undone" icon="api" href="/xano-features/metadata-api/instance_api/delete_an_api_endpoint_permanently_this_action_cannot_be_undone">
    Deletes an API endpoint permanently (cannot be undone)
  </Card>

  <Card title="Configure table security rules by assigning an API group GUID or removing restrictions" icon="api" href="/xano-features/metadata-api/instance_api/configure_table_security_rules_by_assigning_an_api_group_guid_or_removing_restrictions">
    Configures table security rules by assigning an API group GUID
  </Card>
</CardGroup>

## Functions

<CardGroup cols={2}>
  <Card title="Create a new function" icon="code" href="/xano-features/metadata-api/instance_api/create_a_new_function_using_xanoscript">
    Creates a new function
  </Card>

  <Card title="Retrieve all functions in a workspace with optional filtering and pagination" icon="code" href="/xano-features/metadata-api/instance_api/retrieve_all_functions_in_a_workspace_with_optional_filtering_and_pagination">
    Returns all functions in a workspace with optional filtering and pagination
  </Card>

  <Card title="Retrieve a specific function by ID" icon="code" href="/xano-features/metadata-api/instance_api/retrieve_a_specific_function_by_id">
    Returns a specific function by ID
  </Card>

  <Card title="Update function code metadata and caching settings" icon="code" href="/xano-features/metadata-api/instance_api/update_function_code_metadata_and_caching_settings">
    Updates function code metadata and caching settings
  </Card>

  <Card title="Update function security configuration and access controls" icon="code" href="/xano-features/metadata-api/instance_api/update_function_security_configuration_and_access_controls">
    Updates function security configuration and access controls
  </Card>

  <Card title="Delete a function permanently this action cannot be undone" icon="code" href="/xano-features/metadata-api/instance_api/delete_a_function_permanently_this_action_cannot_be_undone">
    Deletes a function permanently (cannot be undone)
  </Card>

  <Card title="Retrieve API function request history with optional filtering and pagination" icon="code" href="/xano-features/metadata-api/instance_api/retrieve_api_function_request_history_with_optional_filtering_and_pagination">
    Returns API function request history with optional filtering and pagination
  </Card>

  <Card title="Search function request history using advanced filters and custom sorting options" icon="code" href="/xano-features/metadata-api/instance_api/search_function_request_history_using_advanced_filters_and_custom_sorting_options">
    Searches function request history using advanced filters and custom sorting
  </Card>
</CardGroup>

## Tables & Schema

<CardGroup cols={2}>
  <Card title="Create a new database table with optional schema definition" icon="database" href="/xano-features/metadata-api/instance_api/create_a_new_database_table_with_optional_schema_definition">
    Creates a new database table with optional schema definition
  </Card>

  <Card title="Retrieve all tables in a workspace with optional filtering and pagination" icon="database" href="/xano-features/metadata-api/instance_api/retrieve_all_tables_in_a_workspace_with_optional_filtering_and_pagination">
    Returns all tables in a workspace with optional filtering and pagination
  </Card>

  <Card title="Retrieve detailed information for a specific table" icon="database" href="/xano-features/metadata-api/instance_api/retrieve_detailed_information_for_a_specific_table">
    Returns detailed information for a specific table
  </Card>

  <Card title="Update table properties including name description tags and authentication settings" icon="database" href="/xano-features/metadata-api/instance_api/update_table_properties_including_name_description_tags_and_authentication_settings">
    Updates table properties including name, description, tags and authentication settings
  </Card>

  <Card title="Delete a database table and all its data permanently" icon="database" href="/xano-features/metadata-api/instance_api/delete_a_database_table_and_all_its_data_permanently">
    Deletes a database table and all its data permanently
  </Card>

  <Card title="Retrieve the complete schema definition for a database table" icon="database" href="/xano-features/metadata-api/instance_api/retrieve_the_complete_schema_definition_for_a_database_table">
    Returns the complete schema definition for a database table
  </Card>

  <Card title="Replace the entire schema definition for a database table" icon="database" href="/xano-features/metadata-api/instance_api/replace_the_entire_schema_definition_for_a_database_table">
    Replaces the entire schema definition for a database table
  </Card>

  <Card title="Retrieve details for a specific column in a tables schema" icon="database" href="/xano-features/metadata-api/instance_api/retrieve_details_for_a_specific_column_in_a_tables_schema">
    Returns details for a specific column in a table's schema
  </Card>

  <Card title="Rename a column in a tables schema" icon="database" href="/xano-features/metadata-api/instance_api/rename_a_column_in_a_tables_schema">
    Renames a column in a table's schema
  </Card>

  <Card title="Delete a column from a tables schema this action cannot be undone" icon="database" href="/xano-features/metadata-api/instance_api/delete_a_column_from_a_tables_schema_this_action_cannot_be_undone">
    Deletes a column from a table's schema (cannot be undone)
  </Card>

  <Card title="Retrieve all indexes for a database table" icon="database" href="/xano-features/metadata-api/instance_api/retrieve_all_indexes_for_a_database_table">
    Returns all indexes for a database table
  </Card>

  <Card title="Replace all indexes for a database table with new index configuration" icon="database" href="/xano-features/metadata-api/instance_api/replace_all_indexes_for_a_database_table_with_new_index_configuration">
    Replaces all indexes for a database table with new index configuration
  </Card>

  <Card title="Delete a specific table index this action cannot be undone" icon="database" href="/xano-features/metadata-api/instance_api/delete_a_specific_table_index_this_action_cannot_be_undone">
    Deletes a specific table index (cannot be undone)
  </Card>

  <Card title="Delete all records from the table and optionally reset the primary key" icon="database" href="/xano-features/metadata-api/instance_api/delete_all_records_from_the_table_and_optionally_reset_the_primary_key">
    Deletes all records from the table and optionally resets the primary key
  </Card>
</CardGroup>

## Table Content

<CardGroup cols={2}>
  <Card title="Create a new record in the table" icon="table" href="/xano-features/metadata-api/instance_api/create_a_new_record_in_the_table">
    Creates a new record in the table
  </Card>

  <Card title="Create multiple records in a single batch operation" icon="table" href="/xano-features/metadata-api/instance_api/create_multiple_records_in_a_single_batch_operation">
    Creates multiple records in a single batch operation
  </Card>

  <Card title="Retrieve paginated records from a table" icon="table" href="/xano-features/metadata-api/instance_api/retrieve_paginated_records_from_a_table">
    Returns paginated records from a table
  </Card>

  <Card title="Retrieve a specific record by ID" icon="table" href="/xano-features/metadata-api/instance_api/retrieve_a_specific_record_by_id">
    Returns a specific record by ID
  </Card>

  <Card title="Update a specific record by ID" icon="table" href="/xano-features/metadata-api/instance_api/update_a_specific_record_by_id">
    Updates a specific record by ID
  </Card>

  <Card title="Update multiple records in a single batch operation" icon="table" href="/xano-features/metadata-api/instance_api/update_multiple_records_in_a_single_batch_operation">
    Updates multiple records in a single batch operation
  </Card>

  <Card title="Update all records matching specified search criteria" icon="table" href="/xano-features/metadata-api/instance_api/update_all_records_matching_specified_search_criteria">
    Updates all records matching specified search criteria
  </Card>

  <Card title="Delete a specific record by ID" icon="table" href="/xano-features/metadata-api/instance_api/delete_a_specific_record_by_id">
    Deletes a specific record by ID
  </Card>

  <Card title="Delete multiple records by their IDs in a single operation" icon="table" href="/xano-features/metadata-api/instance_api/delete_multiple_records_by_their_ids_in_a_single_operation">
    Deletes multiple records by their IDs in a single operation
  </Card>

  <Card title="Delete all records matching specified search criteria" icon="table" href="/xano-features/metadata-api/instance_api/delete_all_records_matching_specified_search_criteria">
    Deletes all records matching specified search criteria
  </Card>

  <Card title="Search table records with advanced filtering and sorting options" icon="table" href="/xano-features/metadata-api/instance_api/search_table_records_with_advanced_filtering_and_sorting_options">
    Searches table records with advanced filtering and sorting options
  </Card>
</CardGroup>

## Tasks

<CardGroup cols={2}>
  <Card title="Create a new scheduled task" icon="clock" href="/xano-features/metadata-api/instance_api/create_a_new_scheduled_task_using_xanoscript">
    Creates a new scheduled task
  </Card>

  <Card title="Retrieve all scheduled tasks in a workspace with optional filtering and pagination" icon="clock" href="/xano-features/metadata-api/instance_api/retrieve_all_scheduled_tasks_in_a_workspace_with_optional_filtering_and_pagination">
    Returns all scheduled tasks in a workspace with optional filtering and pagination
  </Card>

  <Card title="Retrieve a specific scheduled task by ID" icon="clock" href="/xano-features/metadata-api/instance_api/retrieve_a_specific_scheduled_task_by_id">
    Returns a specific scheduled task by ID
  </Card>

  <Card title="Update task code schedule settings and activation status" icon="clock" href="/xano-features/metadata-api/instance_api/update_task_code_schedule_settings_and_activation_status">
    Updates task code, schedule settings and activation status
  </Card>

  <Card title="Update scheduled task security configuration and access controls" icon="clock" href="/xano-features/metadata-api/instance_api/update_scheduled_task_security_configuration_and_access_controls">
    Updates scheduled task security configuration and access controls
  </Card>

  <Card title="Delete a scheduled task permanently this action cannot be undone" icon="clock" href="/xano-features/metadata-api/instance_api/delete_a_scheduled_task_permanently_this_action_cannot_be_undone">
    Deletes a scheduled task permanently (cannot be undone)
  </Card>

  <Card title="Retrieve task request history with optional filtering and pagination" icon="clock" href="/xano-features/metadata-api/instance_api/retrieve_task_request_history_with_optional_filtering_and_pagination">
    Returns task request history with optional filtering and pagination
  </Card>

  <Card title="Search task request history using advanced filters and custom sorting options" icon="clock" href="/xano-features/metadata-api/instance_api/search_task_request_history_using_advanced_filters_and_custom_sorting_options">
    Searches task request history using advanced filters and custom sorting
  </Card>
</CardGroup>

## Real-time

<CardGroup cols={2}>
  <Card title="Retrieve real-time operational metrics and connection details" icon="zap" href="/xano-features/metadata-api/instance_api/retrieve_real-time_operational_metrics_and_connection_details">
    Returns real-time operational metrics and connection details
  </Card>

  <Card title="Update real-time settings and connection configuration" icon="zap" href="/xano-features/metadata-api/instance_api/update_real-time_settings_and_connection_configuration">
    Updates real-time settings and connection configuration
  </Card>
</CardGroup>

## Audit & History

<CardGroup cols={2}>
  <Card title="Browse audit logs across all workspaces" icon="search" href="/xano-features/metadata-api/instance_api/browse_audit_logs_across_all_workspaces">
    Returns audit logs across all workspaces
  </Card>

  <Card title="Search audit logs across all workspaces with support for complex filtering and sorting" icon="search" href="/xano-features/metadata-api/instance_api/search_audit_logs_across_all_workspaces_with_support_for_complex_filtering_and_sorting">
    Searches audit logs across all workspaces with complex filtering and sorting
  </Card>

  <Card title="Retrieve workspace audit logs with pagination support" icon="search" href="/xano-features/metadata-api/instance_api/retrieve_workspace_audit_logs_with_pagination_support">
    Returns workspace audit logs with pagination support
  </Card>

  <Card title="Search audit logs using advanced filters and custom sorting options" icon="search" href="/xano-features/metadata-api/instance_api/search_audit_logs_using_advanced_filters_and_custom_sorting_options">
    Searches audit logs using advanced filters and custom sorting
  </Card>

  <Card title="Retrieve API request history with optional filtering and pagination" icon="search" href="/xano-features/metadata-api/instance_api/retrieve_api_request_history_with_optional_filtering_and_pagination">
    Returns API request history with optional filtering and pagination
  </Card>

  <Card title="Search API request history using advanced filters and custom sorting options" icon="search" href="/xano-features/metadata-api/instance_api/search_api_request_history_using_advanced_filters_and_custom_sorting_options">
    Searches API request history using advanced filters and custom sorting
  </Card>

  <Card title="Retrieve middleware request history with optional filtering and pagination" icon="search" href="/xano-features/metadata-api/instance_api/retrieve_middleware_request_history_with_optional_filtering_and_pagination">
    Returns middleware request history with optional filtering and pagination
  </Card>

  <Card title="Search middleware request history using advanced filters and custom sorting options" icon="search" href="/xano-features/metadata-api/instance_api/search_middleware_request_history_using_advanced_filters_and_custom_sorting_options">
    Searches middleware request history using advanced filters and custom sorting
  </Card>

  <Card title="Retrieve tool request history with optional filtering and pagination" icon="search" href="/xano-features/metadata-api/instance_api/retrieve_tool_request_history_with_optional_filtering_and_pagination">
    Returns tool request history with optional filtering and pagination
  </Card>

  <Card title="Search tool request history using advanced filters and custom sorting options" icon="search" href="/xano-features/metadata-api/instance_api/search_tool_request_history_using_advanced_filters_and_custom_sorting_options">
    Searches tool request history using advanced filters and custom sorting
  </Card>

  <Card title="Retrieve trigger request history with optional filtering and pagination" icon="search" href="/xano-features/metadata-api/instance_api/retrieve_trigger_request_history_with_optional_filtering_and_pagination">
    Returns trigger request history with optional filtering and pagination
  </Card>

  <Card title="Search trigger request history using advanced filters and custom sorting options" icon="search" href="/xano-features/metadata-api/instance_api/search_trigger_request_history_using_advanced_filters_and_custom_sorting_options">
    Searches trigger request history using advanced filters and custom sorting
  </Card>
</CardGroup>

***

# Common errors

* **400** — Input Error. Check the request payload for issues.
* **401** — Unauthorized.
* **403** — Access denied. Additional privileges are needed.
* **404** — Not Found.
* **429** — Rate Limited.
* **500** — Unexpected error.

***

# Changelog

* **v0.0.1** — Initial beta endpoints for listing and retrieving instances.


Built with [Mintlify](https://mintlify.com).
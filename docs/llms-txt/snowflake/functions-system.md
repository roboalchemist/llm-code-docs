# Source: https://docs.snowflake.com/en/sql-reference/functions-system.md

# System functions

Snowflake provides the following types of system functions:

* Control functions that allow you to execute actions in the system (e.g. aborting a query).
* Information functions that return information about the system (e.g. calculating the clustering depth of a table).
* Information functions that return information about queries (e.g. information about EXPLAIN plans).

Many of these system functions have the prefix `SYSTEM$` (e.g. `SYSTEM$TYPEOF`). For the system functions that use
this prefix, you must specify the prefix when calling the function. For example:

```sqlexample
SELECT SYSTEM$TYPEOF('a');
```

| Function Name | Notes |
| --- | --- |
| **Control** |  |
| [SYSTEM$ABORT_SESSION](functions/system_abort_session.md) |  |
| [SYSTEM$ABORT_TRANSACTION](functions/system_abort_transaction.md) |  |
| [SYSTEM$ACTIVATE_CMK_INFO](functions/system_activate_cmk_info.md) |  |
| [SYSTEM$ACTIVATE_CMK_INFO_POSTGRES](functions/system_activate_cmk_info_postgres.md) |  |
| [SYSTEM$ADD_EVENT (for Snowflake Scripting)](functions/system_add_event.md) |  |
| [SYSTEM$ADD_REFERENCE](functions/system_add_reference.md) |  |
| [SYSTEM$AUTHORIZE_PRIVATELINK](functions/system_authorize_privatelink.md) |  |
| [SYSTEM$AUTHORIZE_STAGE_PRIVATELINK_ACCESS](functions/system_authorize_stage_privatelink_access.md) |  |
| [SYSTEM$BEGIN_DEBUG_APPLICATION](functions/system_begin_debug_application.md) |  |
| [SYSTEM$BLOCK_INTERNAL_STAGES_PUBLIC_ACCESS](functions/system_block_internal_stages_public_access.md) |  |
| [SYSTEM$CANCEL_ALL_QUERIES](functions/system_cancel_all_queries.md) |  |
| [SYSTEM$CANCEL_QUERY](functions/system_cancel_query.md) |  |
| [SYSTEM$CLEANUP_DATABASE_ROLE_GRANTS](functions/system_cleanup_database_role_grants.md) |  |
| [SYSTEM$COMMIT_MOVE_ORGANIZATION_ACCOUNT](functions/system_commit_move_organization_account.md) |  |
| [SYSTEM$CONVERT_PIPES_SQS_TO_SNS](functions/system_convert_pipes_sqs_to_sns.md) |  |
| [SYSTEM$CREATE_BILLING_EVENT](functions/system_create_billing_event.md) |  |
| [SYSTEM$CREATE_BILLING_EVENTS](functions/system_create_billing_events.md) |  |
| [SYSTEM$DEACTIVATE_CMK_INFO](functions/system_deactivate_cmk_info.md) |  |
| [SYSTEM$DEPROVISION_PRIVATELINK_ENDPOINT](functions/system_deprovision_privatelink_endpoint.md) |  |
| [SYSTEM$DEPROVISION_PRIVATELINK_ENDPOINT_TSS](functions/system_deprovision_privatelink_endpoint_tss.md) |  |
| [SYSTEM$DEREGISTER_CMK_INFO](functions/system_deregister_cmk_info.md) |  |
| [SYSTEM$DEREGISTER_CMK_INFO_POSTGRES](functions/system_deregister_cmk_info_postgres.md) |  |
| [SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE](functions/system_disable_behavior_change_bundle.md) |  |
| [SYSTEM$DISABLE_DATABASE_REPLICATION](functions/system_disable_database_replication.md) |  |
| [SYSTEM$DISABLE_GLOBAL_DATA_SHARING_FOR_ACCOUNT](functions/system_disable_global_data_sharing_for_account.md) |  |
| [SYSTEM$DISABLE_PREVIEW_ACCESS](functions/system_disable_preview_access.md) |  |
| [SYSTEM$DISABLE_PRIVATELINK_ACCESS_ONLY](functions/system_disable_privatelink_access_only.md) |  |
| [SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE](functions/system_enable_behavior_change_bundle.md) |  |
| [SYSTEM$ENABLE_GLOBAL_DATA_SHARING_FOR_ACCOUNT](functions/system_enable_global_data_sharing_for_account.md) |  |
| [SYSTEM$ENABLE_PREVIEW_ACCESS](functions/system_enable_preview_access.md) |  |
| [SYSTEM$END_DEBUG_APPLICATION](functions/system_end_debug_application.md) |  |
| [SYSTEM$ENFORCE_PRIVATELINK_ACCESS_ONLY](functions/system_enforce_privatelink_access_only.md) |  |
| [SYSTEM$FINISH_OAUTH_FLOW](functions/system_finish_oauth_flow.md) |  |
| [SYSTEM$GLOBAL_ACCOUNT_SET_PARAMETER](functions/system_global_account_set_parameter.md) |  |
| [SYSTEM$INITIATE_MOVE_ORGANIZATION_ACCOUNT](functions/system_initiate_move_organization_account.md) |  |
| [SYSTEM$LINK_ACCOUNT_OBJECTS_BY_NAME](functions/system_link_account_objects_by_name.md) |  |
| [SYSTEM$LINK_ORGANIZATION_USER](functions/system_link_organization_user.md) |  |
| [SYSTEM$LINK_ORGANIZATION_USER_GROUP](functions/system_link_organization_user_group.md) |  |
| [SYSTEM$MIGRATE_SAML_IDP_REGISTRATION](functions/system_migrate_saml_idp_registration.md) |  |
| [SYSTEM$OPT_IN_INTERNAL_STAGE_NETWORK_LOGS](functions/system_opt_in_internal_stage_network_logs.md) |  |
| [SYSTEM$OPT_OUT_INTERNAL_STAGE_NETWORK_LOGS](functions/system_opt_out_internal_stage_network_logs.md) |  |
| [SYSTEM$OPT_OUT_MALICIOUS_IP_PROTECTION_BY_CATEGORY](functions/system_opt_out_malicious_ip_protection_by_category.md) |  |
| [SYSTEM$PIPE_FORCE_RESUME](functions/system_pipe_force_resume.md) |  |
| [SYSTEM$PIPE_REBINDING_WITH_NOTIFICATION_CHANNEL](functions/system_pipe_rebinding_with_notification_channel.md) |  |
| [SYSTEM$PROVISION_PRIVATELINK_ENDPOINT](functions/system_provision_privatelink_endpoint.md) |  |
| [SYSTEM$PROVISION_PRIVATELINK_ENDPOINT_TSS](functions/system_provision_privatelink_endpoint_tss.md) |  |
| [SYSTEM$REGISTER_CMK_INFO](functions/system_register_cmk_info.md) |  |
| [SYSTEM$REGISTER_CMK_INFO_POSTGRES](functions/system_register_cmk_info_postgres.md) |  |
| [SYSTEM$REGISTER_PRIVATELINK_ENDPOINT](functions/system_register_privatelink_endpoint.md) |  |
| [SYSTEM$REMOVE_ALL_REFERENCES](functions/system_remove_all_references.md) |  |
| [SYSTEM$REMOVE_REFERENCE](functions/system_remove_reference.md) |  |
| [SYSTEM$RESTORE_PRIVATELINK_ENDPOINT](functions/system_restore_privatelink_endpoint.md) |  |
| [SYSTEM$RESTORE_PRIVATELINK_ENDPOINT_TSS](functions/system_restore_privatelink_endpoint_tss.md) |  |
| [SYSTEM$REVOKE_PRIVATELINK](functions/system_revoke_privatelink.md) |  |
| [SYSTEM$REVOKE_STAGE_PRIVATELINK_ACCESS](functions/system_revoke_stage_privatelink_access.md) |  |
| [SYSTEM$SCHEDULE_ASYNC_REPLICATION_GROUP_REFRESH](functions/system_schedule_async_replication_group_refresh.md) |  |
| [SYSTEM$SEND_NOTIFICATIONS_TO_CATALOG](functions/system_send_notifications_to_catalog.md) |  |
| [SYSTEM$SET_APPLICATION_RESTRICTED_FEATURE_ACCESS](functions/system_set_application_restricted_feature_access.md) |  |
| [SYSTEM$SET_CATALOG_INTEGRATION](functions/system_set_catalog_integration.md) |  |
| [SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](functions/system_set_default_columns_override_for_show_command.md) |  |
| [SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](functions/system_set_default_columns_override_for_system_object.md) |  |
| [SYSTEM$SET_EVENT_SHARING_ACCOUNT_FOR_REGION](functions/system_set_event_sharing_account_for_region.md) |  |
| [SYSTEM$SET_PRIVATELINK_ENDPOINT_HOSTNAME](functions/system_set_privatelink_endpoint_hostname.md) |  |
| [SYSTEM$SET_REFERENCE](functions/system_set_reference.md) |  |
| [SYSTEM$SET_ROW_TIMESTAMP_ON_ALL_SUPPORTED_TABLES](functions/system_set_row_timestamp_on_all_supported_tables.md) |  |
| [SYSTEM$SNOWPIPE_STREAMING_UPDATE_CHANNEL_OFFSET_TOKEN](functions/system_snowpipe_streaming_update_channel_offset_token.md) |  |
| [SYSTEM$START_OAUTH_FLOW](functions/system_start_oauth_flow.md) |  |
| [SYSTEM$START_USER_EMAIL_VERIFICATION](functions/system_start_user_email_verification.md) |  |
| [SYSTEM$TASK_DEPENDENTS_ENABLE](functions/system_task_dependents_enable.md) |  |
| [SYSTEM$TRIGGER_LISTING_REFRESH](functions/system_trigger_listing_refresh.md) |  |
| [SYSTEM$UNBLOCK_INTERNAL_STAGES_PUBLIC_ACCESS](functions/system_unblock_internal_stages_public_access.md) |  |
| [SYSTEM$UNLINK_ORGANIZATION_USER](functions/system_unlink_organization_user.md) |  |
| [SYSTEM$UNLINK_ORGANIZATION_USER_GROUP](functions/system_unlink_organization_user_group.md) |  |
| [SYSTEM$UNREGISTER_PRIVATELINK_ENDPOINT](functions/system_unregister_privatelink_endpoint.md) |  |
| [SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](functions/system_unset_default_columns_override_for_show_command.md) |  |
| [SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](functions/system_unset_default_columns_override_for_system_object.md) |  |
| [SYSTEM$UNSET_EVENT_SHARING_ACCOUNT_FOR_REGION](functions/system_unset_event_sharing_account_for_region.md) |  |
| [SYSTEM$USER_TASK_CANCEL_ONGOING_EXECUTIONS](functions/system_user_task_cancel_ongoing_executions.md) |  |
| [SYSTEM$WAIT](functions/system_wait.md) |  |
| **Information** |  |
| [EXTRACT_SEMANTIC_CATEGORIES](functions/extract_semantic_categories.md) |  |
| [GET_ANACONDA_PACKAGES_REPODATA](functions/get_anaconda_packages_repodata.md) |  |
| [SHOW_PYTHON_PACKAGES_DEPENDENCIES](functions/show_python_packages_dependencies.md) |  |
| [SYSTEM$ALLOWLIST](functions/system_allowlist.md) |  |
| [SYSTEM$ALLOWLIST_PRIVATELINK](functions/system_allowlist_privatelink.md) |  |
| [SYSTEM$APP_COMPATIBILITY_CHECK](functions/system_app_compatibility_check.md) |  |
| [SYSTEM$APPLICATION_GET_LOG_LEVEL](functions/system_application_get_log_level.md) |  |
| [SYSTEM$APPLICATION_GET_METRIC_LEVEL](functions/system_application_get_metric_level.md) |  |
| [SYSTEM$APPLICATION_GET_TRACE_LEVEL](functions/system_application_get_trace_level.md) |  |
| [SYSTEM$AUTO_REFRESH_STATUS](functions/system_auto_refresh_status.md) |  |
| [SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS](functions/system_behavior_change_bundle_status.md) |  |
| [SYSTEM$CATALOG_LINK_STATUS](functions/system_catalog_link_status.md) |  |
| [SYSTEM$CLIENT_VERSION_INFO](functions/system_client_version_info.md) |  |
| [SYSTEM$CLIENT_VULNERABILITY_INFO](functions/system_client_vulnerability_info.md) |  |
| [SYSTEM$CLUSTERING_DEPTH](functions/system_clustering_depth.md) |  |
| [SYSTEM$CLUSTERING_INFORMATION](functions/system_clustering_information.md) |  |
| [SYSTEM$CLUSTERING_RATIO](functions/system_clustering_ratio.md) | Deprecated; use the other clustering functions instead. |
| [SYSTEM$CURRENT_USER_TASK_NAME](functions/system_current_user_task_name.md) |  |
| [SYSTEM$DATA_METRIC_SCAN](functions/system_data_metric_scan.md) |  |
| [SYSTEM$DATABASE_REFRESH_HISTORY](functions/system_database_refresh_history.md) | Deprecated; use [DATABASE_REFRESH_HISTORY](functions/database_refresh_history.md) instead. |
| [SYSTEM$DATABASE_REFRESH_PROGRESS , SYSTEM$DATABASE_REFRESH_PROGRESS_BY_JOB](functions/system_database_refresh_progress.md) | Deprecated; use [DATABASE_REFRESH_PROGRESS , DATABASE_REFRESH_PROGRESS_BY_JOB](functions/database_refresh_progress.md) instead. |
| [SYSTEM$DECODE_PAT](functions/system_decode_pat.md) |  |
| [SYSTEM$DESC_ICEBERG_ACCESS_IDENTITY](functions/system_desc_iceberg_access_identity.md) |  |
| [SYSTEM$ESTIMATE_AUTOMATIC_CLUSTERING_COSTS](functions/system_estimate_automatic_clustering_costs.md) |  |
| [SYSTEM$ESTIMATE_SEARCH_OPTIMIZATION_COSTS](functions/system_estimate_search_optimization_costs.md) |  |
| [SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS](functions/system_evaluate_data_quality_expectations.md) |  |
| [SYSTEM$EXPORT_TDS_FROM_SEMANTIC_VIEW](functions/system_export_tds_from_semantic_view.md) |  |
| [SYSTEM$EXTERNAL_TABLE_PIPE_STATUS](functions/system_external_table_pipe_status.md) |  |
| [SYSTEM$GENERATE_SAML_CSR](functions/system_generate_saml_csr.md) |  |
| [SYSTEM$GENERATE_SCIM_ACCESS_TOKEN](functions/system_generate_scim_access_token.md) |  |
| [SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES](functions/system_get_all_default_columns_overrides.md) |  |
| [SYSTEM$GET_ALL_REFERENCES](functions/system_get_all_references.md) |  |
| [SYSTEM$GET_AWS_SNS_IAM_POLICY](functions/system_get_aws_sns_iam_policy.md) |  |
| [SYSTEM$GET_CATALOG_LINKED_DATABASE_CONFIG](functions/system_get_catalog_linked_database_config.md) |  |
| [SYSTEM$GET_CLASSIFICATION_RESULT](functions/system_get_classification_result.md) |  |
| [SYSTEM$GET_CMK_AKV_CONSENT_URL](functions/system_get_cmk_akv_consent_url.md) |  |
| [SYSTEM$GET_CMK_CONFIG](functions/system_get_cmk_config.md) |  |
| [SYSTEM$GET_CMK_CONFIG_POSTGRES](functions/system_get_cmk_config_postgres.md) |  |
| [SYSTEM$GET_CMK_INFO](functions/system_get_cmk_info.md) |  |
| [SYSTEM$GET_CMK_INFO_POSTGRES](functions/system_get_cmk_info_postgres.md) |  |
| [SYSTEM$GET_CMK_KMS_KEY_POLICY](functions/system_get_cmk_kms_key_policy.md) |  |
| [SYSTEM$GET_COMPUTE_POOL_PENDING_MAINTENANCE](functions/system_get_compute_pool_pending_maintenance.md) |  |
| [SYSTEM$GET_DBT_LOG](functions/system_get_dbt_log.md) |  |
| [SYSTEM$GET_DEBUG_STATUS](functions/system_get_debug_status.md) |  |
| [SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](functions/system_get_default_columns_override_for_show_command.md) |  |
| [SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](functions/system_get_default_columns_override_for_system_object.md) |  |
| [SYSTEM$GET_DIRECTORY_TABLE_STATUS](functions/system_get_directory_table_status.md) |  |
| [SYSTEM$GET_GCP_KMS_CMK_GRANT_ACCESS_CMD](functions/system_get_gcp_kms_cmk_grant_access_cmd.md) |  |
| [SYSTEM$GET_HASH_FOR_APPLICATION](functions/system_get_hash_for_application.md) |  |
| [SYSTEM$GET_ICEBERG_TABLE_INFORMATION](functions/system_get_iceberg_table_information.md) |  |
| [SYSTEM$GET_INSTANCE_FAMILY_PLACEMENT_GROUPS](functions/system_get_instance_family_placement_groups.md) |  |
| [SYSTEM$GET_LOGIN_FAILURE_DETAILS](functions/system_get_login_failure_details.md) |  |
| [SYSTEM$GET_PREDECESSOR_RETURN_VALUE](functions/system_get_predecessor_return_value.md) |  |
| [SYSTEM$GET_PREVIEW_ACCESS_STATUS](functions/system_get_preview_access_status.md) |  |
| [SYSTEM$GET_PRIVATELINK](functions/system_get_privatelink.md) |  |
| [SYSTEM$GET_PRIVATELINK_AUTHORIZED_ENDPOINTS](functions/system_get_privatelink_authorized_endpoints.md) |  |
| [SYSTEM$GET_PRIVATELINK_CONFIG](functions/system_get_privatelink_config.md) |  |
| [SYSTEM$GET_PRIVATELINK_ENDPOINTS_INFO](functions/system_get_privatelink_endpoints_info.md) |  |
| [SYSTEM$GET_PRIVATELINK_ENDPOINT_REGISTRATIONS](functions/system_get_privatelink_endpoint_registrations.md) |  |
| [SYSTEM$GET_PURCHASE_ATTRIBUTES](functions/system_get_purchase_attributes.md) |  |
| [SYSTEM$GET_REFERENCED_OBJECT_ID_HASH](functions/system_get_referenced_object_id_hash.md) |  |
| [SYSTEM$GET_SERVICE_DNS_DOMAIN](functions/system_get_service_dns_domain.md) |  |
| [SYSTEM$GET_SERVICE_LOGS](functions/system_get_service_logs.md) |  |
| [SYSTEM$GET_SERVICE_STATUS — Deprecated](functions/system_get_service_status.md) | Deprecated; use the [SHOW SERVICE CONTAINERS IN SERVICE](sql/show-service-containers-in-service.md) command instead. |
| [SYSTEM$GET_SNOWFLAKE_EGRESS_IP_RANGES](functions/system_get_snowflake_egress_ip_ranges.md) |  |
| [SYSTEM$GET_SNOWFLAKE_PLATFORM_INFO](functions/system_get_snowflake_platform_info.md) |  |
| [SYSTEM$GET_TAG](functions/system_get_tag.md) |  |
| [SYSTEM$GET_TAG_ALLOWED_VALUES](functions/system_get_tag_allowed_values.md) |  |
| [SYSTEM$GET_TAG_ON_CURRENT_COLUMN](functions/system_get_tag_on_current_column.md) |  |
| [SYSTEM$GET_TAG_ON_CURRENT_TABLE](functions/system_get_tag_on_current_table.md) |  |
| [SYSTEM$GET_TASK_GRAPH_CONFIG](functions/system_get_task_graph_config.md) |  |
| [SYSTEM$HOLD_PRIVILEGE_ON_ACCOUNT](functions/system_hold_privilege_on_account.md) |  |
| [SYSTEM$INTERNAL_STAGES_PUBLIC_ACCESS_STATUS](functions/system_internal_stages_public_access_status.md) |  |
| [SYSTEM$IS_APPLICATION_ALL_MANDATORY_TELEMETRY_EVENT_DEFINITIONS_ENABLED](functions/system_is_application_all_mandatory_telemetry_event_definitions_enabled.md) |  |
| [SYSTEM$IS_APPLICATION_AUTHORIZED_FOR_TELEMETRY_EVENT_SHARING](functions/system_is_application_authorized_for_telemetry_event_sharing.md) |  |
| [SYSTEM$IS_APPLICATION_INSTALLED_FROM_SAME_ACCOUNT](functions/system_is_application_installed_from_same_account.md) |  |
| [SYSTEM$IS_APPLICATION_SHARING_EVENTS_WITH_PROVIDER](functions/system_is_application_sharing_events_with_provider.md) |  |
| [SYSTEM$IS_GLOBAL_DATA_SHARING_ENABLED_FOR_ACCOUNT](functions/system_is_global_data_sharing_enabled_for_account.md) |  |
| [SYSTEM$IS_LISTING_PURCHASED](functions/system_is_listing_purchased.md) |  |
| [SYSTEM$IS_LISTING_TRIAL](functions/system_is_listing_trial.md) |  |
| [SYSTEM$LAST_CHANGE_COMMIT_TIME](functions/system_last_change_commit_time.md) |  |
| [SYSTEM$LIST_APPLICATION_RESTRICTED_FEATURES](functions/system_list_application_restricted_features.md) |  |
| [SYSTEM$LIST_ICEBERG_TABLES_FROM_CATALOG](functions/system_list_iceberg_tables_from_catalog.md) |  |
| [SYSTEM$LIST_NAMESPACES_FROM_CATALOG](functions/system_list_namespaces_from_catalog.md) |  |
| [SYSTEM$LOCATE_DBT_ARCHIVE](functions/system_locate_dbt_archive.md) |  |
| [SYSTEM$LOCATE_DBT_ARTIFACTS](functions/system_locate_dbt_artifacts.md) |  |
| [SYSTEM$LOG, SYSTEM$LOG_<level> (for Snowflake Scripting)](functions/system_log.md) |  |
| [SYSTEM$PIPE_STATUS](functions/system_pipe_status.md) |  |
| [SYSTEM$QUERY_REFERENCE](functions/system_query_reference.md) |  |
| [SYSTEM$READ_YAML_FROM_SEMANTIC_VIEW](functions/system_read_yaml_from_semantic_view.md) |  |
| [SYSTEM$REFERENCE](functions/system_reference.md) |  |
| [SYSTEM$REGISTRY_LIST_IMAGES](functions/system_registry_list_images.md) | Deprecated; use the [SHOW IMAGES IN IMAGE REPOSITORY](sql/show-images-in-image-repository.md) command instead. |
| [SYSTEM$REPORT_HEALTH_STATUS](functions/system_report_health_status.md) |  |
| [SYSTEM$SAP_BDC_LIST_SHARES](functions/system_sap_bdc_list_shares.md) |  |
| [SYSTEM$SET_RETURN_VALUE](functions/system_set_return_value.md) |  |
| [SYSTEM$SET_SPAN_ATTRIBUTES (for Snowflake Scripting)](functions/system_set_span_attributes.md) |  |
| [SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES](functions/system_show_active_behavior_change_bundles.md) |  |
| [SYSTEM$SHOW_BUDGETS_FOR_RESOURCE](functions/system_show_budgets_for_resource.md) |  |
| [SYSTEM$SHOW_BUDGETS_IN_ACCOUNT](functions/system_show_budgets_in_account.md) |  |
| [SYSTEM$SHOW_EVENT_SHARING_ACCOUNTS](functions/system_show_event_sharing_accounts.md) |  |
| [SYSTEM$SHOW_MOVE_ORGANIZATION_ACCOUNT_STATUS](functions/system_show_move_organization_account_status.md) |  |
| [SYSTEM$SHOW_OAUTH_CLIENT_SECRETS](functions/system_show_oauth_client_secrets.md) |  |
| [SYSTEM$SHOW_SENSITIVE_DATA_MONITORED_ENTITIES](functions/system_show_sensitive_data_monitored_entities.md) |  |
| [SYSTEM$STREAM_BACKLOG](functions/system_stream_backlog.md) | This function is a [table function](functions-table.md). |
| [SYSTEM$STREAM_GET_TABLE_TIMESTAMP](functions/system_stream_get_table_timestamp.md) |  |
| [SYSTEM$STREAM_HAS_DATA](functions/system_stream_has_data.md) |  |
| [SYSTEM$SUPPORTED_DBT_VERSIONS](functions/system_supported_dbt_versions.md) |  |
| [SYSTEM$TASK_RUNTIME_INFO](functions/system_task_runtime_info.md) |  |
| [SYSTEM$TYPEOF](functions/system_typeof.md) |  |
| [SYSTEM$VALIDATE_STORAGE_INTEGRATION](functions/system_validate_storage_integration.md) |  |
| [SYSTEM$VERIFY_CATALOG_INTEGRATION](functions/system_verify_catalog_integration.md) |  |
| [SYSTEM$VERIFY_CMK_INFO](functions/system_verify_cmk_info.md) |  |
| [SYSTEM$VERIFY_CMK_INFO_POSTGRES](functions/system_verify_cmk_info_postgres.md) |  |
| [SYSTEM$VERIFY_EXTERNAL_OAUTH_TOKEN](functions/system_verify_ext_oauth_token.md) |  |
| [SYSTEM$VERIFY_EXTERNAL_VOLUME](functions/system_verify_external_volume.md) |  |
| [SYSTEM$WHITELIST](functions/system_whitelist.md) | Deprecated; use [SYSTEM$ALLOWLIST](functions/system_allowlist.md) instead. |
| [SYSTEM$WAIT_FOR_SERVICES](functions/system_wait_for_services.md) |  |
| [SYSTEM$WHITELIST_PRIVATELINK](functions/system_whitelist_privatelink.md) | Deprecated; use [SYSTEM$ALLOWLIST_PRIVATELINK](functions/system_allowlist_privatelink.md) instead. |
| **Query Information** |  |
| [EXPLAIN_JSON](functions/explain_json.md) |  |
| [GET_QUERY_OPERATOR_STATS](functions/get_query_operator_stats.md) |  |
| [GET_PYTHON_PROFILER_OUTPUT (SNOWFLAKE.CORE)](functions/get_python_profiler_output.md) |  |
| [SYSTEM$ESTIMATE_QUERY_ACCELERATION](functions/system_estimate_query_acceleration.md) |  |
| [SYSTEM$EXPLAIN_PLAN_JSON](functions/system_explain_plan_json.md) |  |
| [SYSTEM$EXPLAIN_JSON_TO_TEXT](functions/system_explain_json_to_text.md) |  |
| [SYSTEM$GET_RESULTSET_STATUS](functions/system_get_resultset_status.md) |  |

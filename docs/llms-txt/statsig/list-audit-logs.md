# Source: https://docs.statsig.com/api-reference/audit-logs/list-audit-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Audit Logs



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/audit_logs
openapi: 3.0.0
info:
  title: Console API
  description: >-
    The "Console API" is the CRUD API for performing the actions offered on
    console.statsig.com without needing to go through the web UI.

    If you have any feature requests, drop on in to our [slack
    channel](https://www.statsig.com/slack) and let us know.

    <br /><br />

    <b>Authorization</b>

    <br />

    All requests must include the **STATSIG-API-KEY** field in the header. The
    value should be a **Console API Key** which can be created in the Project
    Settings on
    [console.statsig.com/api_keys](https://console.statsig.com/api_keys)

    <br /><br />

    <b>Rate Limiting</b>

    <br />

    Requests to the Console API are limited to <code>~ 100reqs / 10secs and ~
    900reqs / 15 mins</code>.

    <br /><br />

    <b>Keyboard Search</b>

    <br />

    Use <code>Ctrl/Cmd + K</code> to search for specific endpoints.
  version: 20240601.0.0
  contact: {}
servers:
  - url: https://statsigapi.net
security: []
tags: []
paths:
  /console/v1/audit_logs:
    get:
      tags:
        - Audit Logs
      summary: List Audit Logs
      parameters:
        - name: id
          required: false
          in: query
          schema:
            type: string
        - name: sortKey
          required: false
          in: query
          schema:
            type: string
            enum:
              - id
              - name
              - changeLog
              - actionType
              - date
              - time
              - updatedBy
              - updatedByUserID
        - name: sortOrder
          required: false
          in: query
          schema:
            type: string
            enum:
              - asc
              - desc
        - name: latestID
          required: false
          in: query
          schema:
            type: string
        - name: tags
          required: false
          in: query
          schema:
            oneOf:
              - type: string
              - type: array
                items:
                  type: string
        - name: actionType
          required: false
          in: query
          schema:
            type: string
            enum:
              - cancel_mex_query
              - bulk_add_remove_configs_from_tag
              - create_paired_experiment
              - delete_dashboard_subscription
              - update_dashboard_subscriptions
              - add_dashboard_page
              - generate_dashboard_screenshot_url
              - delete_echidna_table_config
              - update_default_company_metrics
              - rate_sidekick_message
              - rename_offline_aa_report
              - rate_investigation_response
              - set_ai_dataset_global
              - set_ai_scheduled_runs
              - load_power_analysis_results_whn
              - create_offline_aa_report
              - set_warehouse_metadata_indexing_enabled
              - update_primary_attached_report
              - delete_ai_eval
              - delete_ai_dataset
              - upsert_traces_tag
              - create_traces_tag
              - upsert_traces_metadata
              - delete_ai_eval_run
              - create_ai_eval_run
              - create_ai_eval
              - refresh_warehouse_explorer_table_info
              - edit_experiment_scheduled_start
              - edit_ai_config_agent_version
              - update_ai_dataset
              - upload_ai_config_dataset_csv
              - resalt_experiment
              - run_eval_from_traces
              - edit_ai_config_auto_eval_state
              - edit_ai_config_eval_settings
              - update_grader_advisor_cache
              - edit_ai_playground
              - save_ai_playground_results
              - delete_ai_config
              - set_suggest_cure_covariates
              - edit_ai_playground_setup
              - start_ai_config_version_evaluation_job
              - start_ai_playground_completion_job
              - stop_ai_config_version_evaluation_job
              - clone_ai_config
              - edit_ai_config_version
              - delete_ai_config_version
              - delete_ai_config_versions
              - clone_ai_config_version
              - ai_config_create
              - create_ai_config_experiment
              - ai_playground_create
              - create_ai_dataset
              - create_ai_config_version
              - upsert_ai_config_version
              - create_ai_config_eval_grader
              - edit_ai_config_eval_grader
              - delete_ai_config_eval_grader
              - set_enable_id_resolution_toggle
              - dynamic_config_create
              - dynamic_config_template_create
              - dynamic_config_update_owners
              - gate_overrides_update
              - gate_template_create
              - gate_create
              - gate_update
              - set_user_sampling_rate_for_gate
              - gate_update_owners
              - update_store_0_100_exposures
              - update_gate_analytics_enabled
              - update_gate_display_name
              - release_pipeline_create
              - release_pipeline_update
              - release_pipeline_delete
              - update_config_release_pipeline
              - release_pipeline_trigger_create
              - release_pipeline_trigger_paused
              - release_pipeline_trigger_unpaused
              - release_pipeline_trigger_approved
              - release_pipeline_trigger_aborted
              - release_pipeline_trigger_phase_skipped
              - apply_experiment_review
              - extend_experiment_pulse_end_date
              - restart_experiment_pulse
              - autotune_experiment_create
              - autotune_experiment_delete
              - autotune_experiment_snapshot_delete
              - autotune_experiment_edit
              - autotune_experiment_update_target_apps
              - autotune_experiment_update_pulse_paused
              - autotune_overrides_edit
              - autotune_reviews_on
              - experiment_data_report_delete
              - offline_aa_report_delete
              - experiment_discussion_post_create
              - experiment_discussion_post_delete
              - experiment_abandon
              - experiment_pause_assignment
              - experiment_stopped
              - experiment_review_accept
              - experiment_review_reject
              - experiment_template_create
              - update_template_decision_framework
              - remove_template_decision_framework
              - experiment_create
              - experiment_review_create
              - experiment_delete
              - experiment_review_delete
              - experiment_review_update_team
              - experiment_snapshot_delete
              - experiment_group_disable
              - experiment_description_edit
              - experiment_display_name_edit
              - experiment_edit
              - experiment_overrides_edit
              - hypothesis_edit
              - key_experiment_metrics_edit
              - experiment_advanced_settings_edit
              - experiment_decision_make
              - experiment_restart
              - experiment_restart_as_new
              - experiment_rollout
              - experiment_schedule_rollout
              - experiment_reviews_on
              - experiment_start
              - schedule_experiment_start
              - experiment_follow_toggle
              - experiment_allowed_reviewers_update
              - experiment_review_info_update
              - update_experiment_enabled_non_prod_environments
              - archive_experiment
              - unarchive_experiment
              - experiment_update_owners
              - update_echidna_subtype
              - setup_stratified_sampling
              - experiment_update_target_apps
              - experiment_update_subdimension_filter
              - experiment_review_update_overrides
              - experiment_review_update_owners
              - experiment_update_decision_note
              - experiment_update_summary_sections
              - unattach_experiment_to_power_analysis_report
              - attach_experiment_to_power_analysis_report
              - pin_chart_to_summary
              - set_geotest_design
              - delete_geotest_design
              - create_geotest_design
              - experiment_assigned_to_layer
              - holdout_create
              - holdout_delete
              - holdout_layer_parameter_values_update
              - holdout_update
              - holdout_update_owners
              - metric_edit_definition
              - metric_edit_description
              - metric_add_tag
              - metric_remove_tag
              - schedule_delete_metric
              - schedule_archive_metric
              - update_metric_is_permanent
              - update_metric_is_verified
              - metric_reviews_on
              - metric_disable_reviews_locally
              - custom_metric_definition_edit
              - custom_metric_definition_create
              - custom_metric_definition_delete
              - custom_metric_update_owners
              - tag_metrics_bulk
              - tag_create
              - tag_delete
              - tag_edit
              - segment_create
              - segment_update_owners
              - layer_update_owners
              - layer_review_commit
              - layer_review_accept
              - layer_parameter_add
              - layer_create
              - layer_review_create
              - layer_review_delete
              - layer_delete
              - layer_snapshot_delete
              - layer_description_edit
              - layer_edit
              - layer_overrides_edit
              - layer_parameters_edit
              - layer_review_reject
              - layer_allowed_reviewers_update
              - layer_review_info_update
              - layer_update_target_apps
              - delete_layer_parameter
              - update_layer_parameter
              - config_review_accept
              - config_review_commit
              - config_review_create
              - config_delete
              - config_review_delete
              - config_reviews_disable
              - config_review_reject
              - config_resalt
              - config_revert
              - config_require_reviews
              - config_state_toggle
              - config_allowed_reviewers_update
              - config_conditions_update
              - config_default_value_update
              - config_description_update
              - config_display_name_update
              - config_environments_update
              - config_review_info_update
              - config_review_update
              - config_review_required_update
              - config_add_tag
              - config_edit_tags
              - config_remove_tag
              - config_monitoring_metrics_update
              - config_edit_target_apps
              - update_config_analytics_enabled
              - set_self_approvals_blocked
              - release_pipeline_completed
              - release_pipeline_waiting_for_review
              - pin_dashboard_for_company
              - add_dashboard_widget
              - create_dashboard
              - delete_dashboard_widget
              - edit_dashboard_widget
              - delete_dashboard
              - edit_dashboard_description
              - edit_dashboard_name
              - restore_dashboard
              - update_dashboard_widgets_from_generated_tags
              - dashboard_update_owners
              - update_dashboard_settings
              - create_topline_alert
              - update_topline_alert
              - delete_topline_alert
              - topline_alert_update_owners
              - active_user_definition_update
              - company_create
              - company_metric_management_update
              - metric_allowed_reviewers_update
              - metric_review_commit
              - metric_review_create
              - metric_review_info_update
              - set_metric_directionality
              - set_metric_default_impact_multiplier
              - custom_metric_edit
              - custom_metric_name_edit
              - custom_metric_review_accept
              - custom_metric_review_delete
              - custom_metric_review_reject
              - delete_metric
              - archive_metric
              - unarchive_metric
              - cancel_delete_metric
              - cancel_archive_metric
              - edit_guardrail_metric_alert
              - create_guardrail_metric_alert
              - delete_guardrail_metric_alert
              - resolve_guardrail_metric_alert
              - unsnooze_guardrail_metric_alert
              - update_echidna_metric_loading_window
              - update_metric_review_required
              - layer_reviews_on
              - delete_tag
              - ID_list_update
              - update_gate_is_permanent
              - set_config_auto_archive_state
              - load_echidna_metric
              - batch_load_echidna_topline_impact
              - load_echidna_metric_async_batch
              - update_server_sdk_configuration_rollback
              - company_ID_type_add
              - update_echidna_source_review_required
              - AWS_marketplace_account_delete
              - batch_cancel_company_invites
              - batch_user_role_update
              - company_basic_info_edit
              - company_delete
              - company_email_domain_config_delete
              - company_environments_edit
              - add_geo_type
              - delete_geo_type
              - company_ID_type_delete
              - company_ID_type_edit
              - company_invite_access_update
              - update_entities_require_teams
              - update_company_user_store_enabled
              - company_member_remove
              - company_metric_delete
              - company_snapshot_delete
              - config_id_type_update
              - config_update_owners
              - create_customer_app
              - edit_target_app
              - delete_target_app
              - source_allowed_reviewers_update
              - create_echidna_assignment_source
              - create_echidna_entity_property_source
              - create_echidna_metric_source
              - create_echidna_data_quality_checks
              - create_echidna_source_review
              - accept_echidna_source_review
              - commit_echidna_source_review
              - reject_echidna_source_review
              - update_echidna_source_review
              - delete_echidna_source_review
              - create_power_analysis_gate_query
              - create_power_analysis_custom_query
              - custom_pulse_query_create
              - custom_pulse_query_delete
              - custom_pulse_query_name_edit
              - custom_query_toggle_favorite
              - custom_sankey_delete
              - delete_echidna_assignment_source
              - delete_echidna_entity_property_source
              - delete_echidna_metric_source
              - delete_payment_method
              - tag_update_owners
              - modify_override_config
              - modify_overrides
              - remove_override_config
              - scheduled_custom_pulse_query_create
              - integration_delete
              - integration_create
              - integration_requested
              - integration_update
              - scheduled_pulse_custom_query_delete
              - scheduled_pulse_query_name_edit
              - user_data_load
              - organization_member_remove
              - shared_report_link_upsert
              - scheduled_pulse_rollups_update
              - OIDC_configuration_delete
              - project_review_group_delete
              - SSO_disable
              - project_description_edit
              - project_owner_set
              - user_role_update
              - OIDC_configuration_upsert
              - payment_entitlements_upsert
              - project_review_group_upsert
              - project_review_group_remove
              - update_team_settings
              - update_team_admins
              - update_team_name
              - update_team_description
              - update_team
              - shared_report_link_delete
              - experiment_data_report_rename
              - experiment_data_report_update_parameters
              - event_dimension_update
              - integration_set_enabled
              - integration_update_disabled_events
              - integration_update_outgoing_config
              - integration_update_rate_limits
              - integration_upsert
              - ingestion_source_delete
              - tag_configs_bulk
              - org_api_key_create
              - set_personal_api_key_access
              - sdk_key_create
              - sdk_key_rotate
              - sdk_key_deactivate
              - sdk_key_delete
              - secret_key_regenerate
              - sdk_key_update_description
              - set_api_share_key_access
              - set_plan_type
              - generate_integration_webhook_secret
              - set_default_payment_method
              - set_user_sampling_rate
              - sdk_key_update_environments
              - upsert_trigger_integration
              - delete_trigger_integration
              - dismiss_runaway_entity
              - update_echidna_metric_source
              - update_echidna_metric_source_name
              - update_echidna_metric_tag_or_description
              - update_echidna_assignment_source
              - update_echidna_assignment_source_name
              - update_echidna_assignment_source_loading_window
              - update_echidna_entity_property_source
              - update_echidna_entity_property_source_name
              - update_echidna_source_owner
              - update_precommit_hook
              - load_echidna_pulse
              - load_echidna_autotune_pulse
              - load_echidna_assignment_source
              - set_echidna_schedule_hour
              - echidna_drop_tables
              - upsert_user_role
              - delete_user_role
              - sdk_key_update_target_app
              - set_gate_analytics_enabled_by_default
              - set_dynamic_config_analytics_enabled_by_default
              - set_gate_analytics_0_100_exposures_enabled
              - update_bv3_subscription
              - upsert_experiment_settings
              - upsert_gate_settings
              - sdk_key_update_scopes
              - user_login
              - param_store_create
              - param_store_update
              - set_bv3_plan_type
              - set_echidna_project_pulse_schedule
              - set_echidna_project_metric_schedule
              - set_company_default_user_role
              - set_company_session_replay_sampling_rate
              - set_company_session_replay_settings
              - cancel_echidna_dag
              - set_require_target_app_for_new_entity
              - set_default_target_apps_for_new_entity
              - add_segments_of_interest_property
              - delete_segments_of_interest_property
              - add_srm_debugger_custom_dimension
              - delete_srm_debugger_custom_dimension
              - param_store_delete
              - setup_external_opt_in
              - param_store_update_owners
              - create_statsig_proxy
              - update_echidna_assignment_source_is_verified
              - update_echidna_metric_source_is_verified
              - update_echidna_entity_property_source_is_verified
              - update_echidna_source_is_verified
              - set_automated_bot_removals
              - pulse_results_export
              - update_company_auto_capture_settings
              - update_company_experiment_exclusion_segment
              - set_stop_new_assignment_toggle
              - set_stop_experiment_enabled
              - update_company_remove_default_gates_setting
              - set_whn_results_export_setting
              - update_experiment_quality_score_settings
              - update_experiment_salt
              - update_precommit_webhook_key
              - set_whn_table_ttls
              - set_id_resolution_inferred_id
              - set_id_resolution_labeled_id
              - add_session_recordings_to_playlist
              - delete_session_recordings_from_playlist
              - delete_session_replay_playlist
              - backfill_metric_results
              - cancel_metric_backfills
              - archive_org_project
              - update_ai_assistance_enabled
              - update_ai_business_context
              - update_experiment_ai_settings
              - update_experiment_ai_advisor_settings
              - update_ai_config_ai_advisor_settings
              - upsert_ai_config_eval_groups
              - edit_ai_config_targeting_rules
              - upsert_user_store_client_targeting_properties
              - set_ai_config_baseline_version
              - verify_dashboard
              - set_first_exposure_user_store_default
              - scheduled_rollout_template_create
              - scheduled_rollout_template_update
              - scheduled_rollout_template_delete
              - set_ai_provider_api_keys
              - experiment_schedule_allocation_change
              - experiment_rollout_allocation_change
              - gate_stale_status_update
              - rollout_plan_create
              - rollout_plan_update
              - rollout_plan_delete
              - update_experiment_quality_score_criteria
        - name: actionTypes
          required: false
          in: query
          schema:
            type: array
            items:
              type: string
              enum:
                - cancel_mex_query
                - bulk_add_remove_configs_from_tag
                - create_paired_experiment
                - delete_dashboard_subscription
                - update_dashboard_subscriptions
                - add_dashboard_page
                - generate_dashboard_screenshot_url
                - delete_echidna_table_config
                - update_default_company_metrics
                - rate_sidekick_message
                - rename_offline_aa_report
                - rate_investigation_response
                - set_ai_dataset_global
                - set_ai_scheduled_runs
                - load_power_analysis_results_whn
                - create_offline_aa_report
                - set_warehouse_metadata_indexing_enabled
                - update_primary_attached_report
                - delete_ai_eval
                - delete_ai_dataset
                - upsert_traces_tag
                - create_traces_tag
                - upsert_traces_metadata
                - delete_ai_eval_run
                - create_ai_eval_run
                - create_ai_eval
                - refresh_warehouse_explorer_table_info
                - edit_experiment_scheduled_start
                - edit_ai_config_agent_version
                - update_ai_dataset
                - upload_ai_config_dataset_csv
                - resalt_experiment
                - run_eval_from_traces
                - edit_ai_config_auto_eval_state
                - edit_ai_config_eval_settings
                - update_grader_advisor_cache
                - edit_ai_playground
                - save_ai_playground_results
                - delete_ai_config
                - set_suggest_cure_covariates
                - edit_ai_playground_setup
                - start_ai_config_version_evaluation_job
                - start_ai_playground_completion_job
                - stop_ai_config_version_evaluation_job
                - clone_ai_config
                - edit_ai_config_version
                - delete_ai_config_version
                - delete_ai_config_versions
                - clone_ai_config_version
                - ai_config_create
                - create_ai_config_experiment
                - ai_playground_create
                - create_ai_dataset
                - create_ai_config_version
                - upsert_ai_config_version
                - create_ai_config_eval_grader
                - edit_ai_config_eval_grader
                - delete_ai_config_eval_grader
                - set_enable_id_resolution_toggle
                - dynamic_config_create
                - dynamic_config_template_create
                - dynamic_config_update_owners
                - gate_overrides_update
                - gate_template_create
                - gate_create
                - gate_update
                - set_user_sampling_rate_for_gate
                - gate_update_owners
                - update_store_0_100_exposures
                - update_gate_analytics_enabled
                - update_gate_display_name
                - release_pipeline_create
                - release_pipeline_update
                - release_pipeline_delete
                - update_config_release_pipeline
                - release_pipeline_trigger_create
                - release_pipeline_trigger_paused
                - release_pipeline_trigger_unpaused
                - release_pipeline_trigger_approved
                - release_pipeline_trigger_aborted
                - release_pipeline_trigger_phase_skipped
                - apply_experiment_review
                - extend_experiment_pulse_end_date
                - restart_experiment_pulse
                - autotune_experiment_create
                - autotune_experiment_delete
                - autotune_experiment_snapshot_delete
                - autotune_experiment_edit
                - autotune_experiment_update_target_apps
                - autotune_experiment_update_pulse_paused
                - autotune_overrides_edit
                - autotune_reviews_on
                - experiment_data_report_delete
                - offline_aa_report_delete
                - experiment_discussion_post_create
                - experiment_discussion_post_delete
                - experiment_abandon
                - experiment_pause_assignment
                - experiment_stopped
                - experiment_review_accept
                - experiment_review_reject
                - experiment_template_create
                - update_template_decision_framework
                - remove_template_decision_framework
                - experiment_create
                - experiment_review_create
                - experiment_delete
                - experiment_review_delete
                - experiment_review_update_team
                - experiment_snapshot_delete
                - experiment_group_disable
                - experiment_description_edit
                - experiment_display_name_edit
                - experiment_edit
                - experiment_overrides_edit
                - hypothesis_edit
                - key_experiment_metrics_edit
                - experiment_advanced_settings_edit
                - experiment_decision_make
                - experiment_restart
                - experiment_restart_as_new
                - experiment_rollout
                - experiment_schedule_rollout
                - experiment_reviews_on
                - experiment_start
                - schedule_experiment_start
                - experiment_follow_toggle
                - experiment_allowed_reviewers_update
                - experiment_review_info_update
                - update_experiment_enabled_non_prod_environments
                - archive_experiment
                - unarchive_experiment
                - experiment_update_owners
                - update_echidna_subtype
                - setup_stratified_sampling
                - experiment_update_target_apps
                - experiment_update_subdimension_filter
                - experiment_review_update_overrides
                - experiment_review_update_owners
                - experiment_update_decision_note
                - experiment_update_summary_sections
                - unattach_experiment_to_power_analysis_report
                - attach_experiment_to_power_analysis_report
                - pin_chart_to_summary
                - set_geotest_design
                - delete_geotest_design
                - create_geotest_design
                - experiment_assigned_to_layer
                - holdout_create
                - holdout_delete
                - holdout_layer_parameter_values_update
                - holdout_update
                - holdout_update_owners
                - metric_edit_definition
                - metric_edit_description
                - metric_add_tag
                - metric_remove_tag
                - schedule_delete_metric
                - schedule_archive_metric
                - update_metric_is_permanent
                - update_metric_is_verified
                - metric_reviews_on
                - metric_disable_reviews_locally
                - custom_metric_definition_edit
                - custom_metric_definition_create
                - custom_metric_definition_delete
                - custom_metric_update_owners
                - tag_metrics_bulk
                - tag_create
                - tag_delete
                - tag_edit
                - segment_create
                - segment_update_owners
                - layer_update_owners
                - layer_review_commit
                - layer_review_accept
                - layer_parameter_add
                - layer_create
                - layer_review_create
                - layer_review_delete
                - layer_delete
                - layer_snapshot_delete
                - layer_description_edit
                - layer_edit
                - layer_overrides_edit
                - layer_parameters_edit
                - layer_review_reject
                - layer_allowed_reviewers_update
                - layer_review_info_update
                - layer_update_target_apps
                - delete_layer_parameter
                - update_layer_parameter
                - config_review_accept
                - config_review_commit
                - config_review_create
                - config_delete
                - config_review_delete
                - config_reviews_disable
                - config_review_reject
                - config_resalt
                - config_revert
                - config_require_reviews
                - config_state_toggle
                - config_allowed_reviewers_update
                - config_conditions_update
                - config_default_value_update
                - config_description_update
                - config_display_name_update
                - config_environments_update
                - config_review_info_update
                - config_review_update
                - config_review_required_update
                - config_add_tag
                - config_edit_tags
                - config_remove_tag
                - config_monitoring_metrics_update
                - config_edit_target_apps
                - update_config_analytics_enabled
                - set_self_approvals_blocked
                - release_pipeline_completed
                - release_pipeline_waiting_for_review
                - pin_dashboard_for_company
                - add_dashboard_widget
                - create_dashboard
                - delete_dashboard_widget
                - edit_dashboard_widget
                - delete_dashboard
                - edit_dashboard_description
                - edit_dashboard_name
                - restore_dashboard
                - update_dashboard_widgets_from_generated_tags
                - dashboard_update_owners
                - update_dashboard_settings
                - create_topline_alert
                - update_topline_alert
                - delete_topline_alert
                - topline_alert_update_owners
                - active_user_definition_update
                - company_create
                - company_metric_management_update
                - metric_allowed_reviewers_update
                - metric_review_commit
                - metric_review_create
                - metric_review_info_update
                - set_metric_directionality
                - set_metric_default_impact_multiplier
                - custom_metric_edit
                - custom_metric_name_edit
                - custom_metric_review_accept
                - custom_metric_review_delete
                - custom_metric_review_reject
                - delete_metric
                - archive_metric
                - unarchive_metric
                - cancel_delete_metric
                - cancel_archive_metric
                - edit_guardrail_metric_alert
                - create_guardrail_metric_alert
                - delete_guardrail_metric_alert
                - resolve_guardrail_metric_alert
                - unsnooze_guardrail_metric_alert
                - update_echidna_metric_loading_window
                - update_metric_review_required
                - layer_reviews_on
                - delete_tag
                - ID_list_update
                - update_gate_is_permanent
                - set_config_auto_archive_state
                - load_echidna_metric
                - batch_load_echidna_topline_impact
                - load_echidna_metric_async_batch
                - update_server_sdk_configuration_rollback
                - company_ID_type_add
                - update_echidna_source_review_required
                - AWS_marketplace_account_delete
                - batch_cancel_company_invites
                - batch_user_role_update
                - company_basic_info_edit
                - company_delete
                - company_email_domain_config_delete
                - company_environments_edit
                - add_geo_type
                - delete_geo_type
                - company_ID_type_delete
                - company_ID_type_edit
                - company_invite_access_update
                - update_entities_require_teams
                - update_company_user_store_enabled
                - company_member_remove
                - company_metric_delete
                - company_snapshot_delete
                - config_id_type_update
                - config_update_owners
                - create_customer_app
                - edit_target_app
                - delete_target_app
                - source_allowed_reviewers_update
                - create_echidna_assignment_source
                - create_echidna_entity_property_source
                - create_echidna_metric_source
                - create_echidna_data_quality_checks
                - create_echidna_source_review
                - accept_echidna_source_review
                - commit_echidna_source_review
                - reject_echidna_source_review
                - update_echidna_source_review
                - delete_echidna_source_review
                - create_power_analysis_gate_query
                - create_power_analysis_custom_query
                - custom_pulse_query_create
                - custom_pulse_query_delete
                - custom_pulse_query_name_edit
                - custom_query_toggle_favorite
                - custom_sankey_delete
                - delete_echidna_assignment_source
                - delete_echidna_entity_property_source
                - delete_echidna_metric_source
                - delete_payment_method
                - tag_update_owners
                - modify_override_config
                - modify_overrides
                - remove_override_config
                - scheduled_custom_pulse_query_create
                - integration_delete
                - integration_create
                - integration_requested
                - integration_update
                - scheduled_pulse_custom_query_delete
                - scheduled_pulse_query_name_edit
                - user_data_load
                - organization_member_remove
                - shared_report_link_upsert
                - scheduled_pulse_rollups_update
                - OIDC_configuration_delete
                - project_review_group_delete
                - SSO_disable
                - project_description_edit
                - project_owner_set
                - user_role_update
                - OIDC_configuration_upsert
                - payment_entitlements_upsert
                - project_review_group_upsert
                - project_review_group_remove
                - update_team_settings
                - update_team_admins
                - update_team_name
                - update_team_description
                - update_team
                - shared_report_link_delete
                - experiment_data_report_rename
                - experiment_data_report_update_parameters
                - event_dimension_update
                - integration_set_enabled
                - integration_update_disabled_events
                - integration_update_outgoing_config
                - integration_update_rate_limits
                - integration_upsert
                - ingestion_source_delete
                - tag_configs_bulk
                - org_api_key_create
                - set_personal_api_key_access
                - sdk_key_create
                - sdk_key_rotate
                - sdk_key_deactivate
                - sdk_key_delete
                - secret_key_regenerate
                - sdk_key_update_description
                - set_api_share_key_access
                - set_plan_type
                - generate_integration_webhook_secret
                - set_default_payment_method
                - set_user_sampling_rate
                - sdk_key_update_environments
                - upsert_trigger_integration
                - delete_trigger_integration
                - dismiss_runaway_entity
                - update_echidna_metric_source
                - update_echidna_metric_source_name
                - update_echidna_metric_tag_or_description
                - update_echidna_assignment_source
                - update_echidna_assignment_source_name
                - update_echidna_assignment_source_loading_window
                - update_echidna_entity_property_source
                - update_echidna_entity_property_source_name
                - update_echidna_source_owner
                - update_precommit_hook
                - load_echidna_pulse
                - load_echidna_autotune_pulse
                - load_echidna_assignment_source
                - set_echidna_schedule_hour
                - echidna_drop_tables
                - upsert_user_role
                - delete_user_role
                - sdk_key_update_target_app
                - set_gate_analytics_enabled_by_default
                - set_dynamic_config_analytics_enabled_by_default
                - set_gate_analytics_0_100_exposures_enabled
                - update_bv3_subscription
                - upsert_experiment_settings
                - upsert_gate_settings
                - sdk_key_update_scopes
                - user_login
                - param_store_create
                - param_store_update
                - set_bv3_plan_type
                - set_echidna_project_pulse_schedule
                - set_echidna_project_metric_schedule
                - set_company_default_user_role
                - set_company_session_replay_sampling_rate
                - set_company_session_replay_settings
                - cancel_echidna_dag
                - set_require_target_app_for_new_entity
                - set_default_target_apps_for_new_entity
                - add_segments_of_interest_property
                - delete_segments_of_interest_property
                - add_srm_debugger_custom_dimension
                - delete_srm_debugger_custom_dimension
                - param_store_delete
                - setup_external_opt_in
                - param_store_update_owners
                - create_statsig_proxy
                - update_echidna_assignment_source_is_verified
                - update_echidna_metric_source_is_verified
                - update_echidna_entity_property_source_is_verified
                - update_echidna_source_is_verified
                - set_automated_bot_removals
                - pulse_results_export
                - update_company_auto_capture_settings
                - update_company_experiment_exclusion_segment
                - set_stop_new_assignment_toggle
                - set_stop_experiment_enabled
                - update_company_remove_default_gates_setting
                - set_whn_results_export_setting
                - update_experiment_quality_score_settings
                - update_experiment_salt
                - update_precommit_webhook_key
                - set_whn_table_ttls
                - set_id_resolution_inferred_id
                - set_id_resolution_labeled_id
                - add_session_recordings_to_playlist
                - delete_session_recordings_from_playlist
                - delete_session_replay_playlist
                - backfill_metric_results
                - cancel_metric_backfills
                - archive_org_project
                - update_ai_assistance_enabled
                - update_ai_business_context
                - update_experiment_ai_settings
                - update_experiment_ai_advisor_settings
                - update_ai_config_ai_advisor_settings
                - upsert_ai_config_eval_groups
                - edit_ai_config_targeting_rules
                - upsert_user_store_client_targeting_properties
                - set_ai_config_baseline_version
                - verify_dashboard
                - set_first_exposure_user_store_default
                - scheduled_rollout_template_create
                - scheduled_rollout_template_update
                - scheduled_rollout_template_delete
                - set_ai_provider_api_keys
                - experiment_schedule_allocation_change
                - experiment_rollout_allocation_change
                - gate_stale_status_update
                - rollout_plan_create
                - rollout_plan_update
                - rollout_plan_delete
                - update_experiment_quality_score_criteria
        - name: startDate
          required: false
          in: query
          description: Expected valid date in the form of YYYY-MM-DD
          schema:
            example: '2024-01-01'
            type: string
        - name: endDate
          required: false
          in: query
          description: Expected valid date in the form of YYYY-MM-DD
          schema:
            example: '2024-01-01'
            type: string
        - name: limit
          required: false
          in: query
          description: Results per page
          schema:
            example: 10
            oneOf:
              - type: string
              - type: number
            type: integer
        - name: page
          required: false
          in: query
          description: Page number
          schema:
            example: 1
            oneOf:
              - type: string
              - type: number
            type: integer
      responses:
        '200':
          description: Audit logs listed successfully.
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/AuditLogDto'
                example:
                  message: Audit logs listed successfully.
                  data:
                    - id: 25KPZcLjTY7AS1uZdBolPZ
                      name: test_gate_1
                      changeLog: Created Gate
                      actionType: gate_create
                      date: Mon Sep 26 2022
                      time: 23:46:14 GMT+0000 (Coordinated Universal Time)
                      updatedBy: Jane Doe
                      updatedByUserID: 4eoDlYj7svJixZfDsYSn
                      changes:
                        rules:
                          new:
                            - groupName: test
                              percentagePass: 100
                              conditionJSON:
                                - conditionType: 1
                                  operator: 0
                                  value:
                                    - '1'
                                  extraConfig: {}
                              returnValueJSON: 'true'
                              id: BfGswoMDcsZ4y9Le1d9O
                              salt: 8df8n90p-d9bj-1l23-c9bl-1m022n9bzps8
                              environment: production
                              rollouts: []
                              enabledEnvironments:
                                - development
                                - staging
                                - production
                          old:
                            - groupName: test
                              percentagePass: 100
                              conditionJSON:
                                - conditionType: 1
                                  operator: 0
                                  value:
                                    - '1'
                                  extraConfig: {}
                              returnValueJSON: 'true'
                              id: BfGswoMDcsZ4y9Le1d9O
                              salt: 8df8n90p-d9bj-1l23-c9bl-1m022n9bzps8
                              environment: production
                              rollouts: []
                              enabledEnvironments:
                                - development
                                - staging
                    - id: 19LZJaPtCM4GT1sUbWlqVC
                      name: check_employee
                      changeLog: Removed Tag from Config
                      actionType: config_remove_tag
                      date: Mon Sep 26 2022
                      time: 21:25:22 GMT+0000 (Coordinated Universal Time)
                      updatedBy: John Doe
                      updatedByUserID: fd7dWH15Ddncvl3xhVLH
                      changes: {}
                    - id: 76LGVrItCR9WE1iDfNmpHT
                      name: check_employee
                      changeLog: Removed Tag from Config
                      actionType: config_remove_tag
                      date: Mon Sep 26 2022
                      time: 21:25:18 GMT+0000 (Coordinated Universal Time)
                      updatedBy: John Doe
                      updatedByUserID: fd7dWH15Ddncvl3xhVLH
                      changes: {}
                  pagination:
                    itemsPerPage: 3
                    pageNumber: 2
                    totalItems: 829
                    nextPage: statsigapi.net/console/v1/audit_logs?page=3&limit=3
                    previousPage: statsigapi.net/console/v1/audit_logs?page=1&limit=3
                    all: statsigapi.net/console/v1/audit_logs
              example:
                message: Audit logs listed successfully.
                data:
                  - id: 25KPZcLjTY7AS1uZdBolPZ
                    name: test_gate_1
                    changeLog: Created Gate
                    actionType: gate_create
                    date: Mon Sep 26 2022
                    time: 23:46:14 GMT+0000 (Coordinated Universal Time)
                    updatedBy: Jane Doe
                    updatedByUserID: 4eoDlYj7svJixZfDsYSn
                    changes:
                      rules:
                        new:
                          - groupName: test
                            percentagePass: 100
                            conditionJSON:
                              - conditionType: 1
                                operator: 0
                                value:
                                  - '1'
                                extraConfig: {}
                            returnValueJSON: 'true'
                            id: BfGswoMDcsZ4y9Le1d9O
                            salt: 8df8n90p-d9bj-1l23-c9bl-1m022n9bzps8
                            environment: production
                            rollouts: []
                            enabledEnvironments:
                              - development
                              - staging
                              - production
                        old:
                          - groupName: test
                            percentagePass: 100
                            conditionJSON:
                              - conditionType: 1
                                operator: 0
                                value:
                                  - '1'
                                extraConfig: {}
                            returnValueJSON: 'true'
                            id: BfGswoMDcsZ4y9Le1d9O
                            salt: 8df8n90p-d9bj-1l23-c9bl-1m022n9bzps8
                            environment: production
                            rollouts: []
                            enabledEnvironments:
                              - development
                              - staging
                  - id: 19LZJaPtCM4GT1sUbWlqVC
                    name: check_employee
                    changeLog: Removed Tag from Config
                    actionType: config_remove_tag
                    date: Mon Sep 26 2022
                    time: 21:25:22 GMT+0000 (Coordinated Universal Time)
                    updatedBy: John Doe
                    updatedByUserID: fd7dWH15Ddncvl3xhVLH
                    changes: {}
                  - id: 76LGVrItCR9WE1iDfNmpHT
                    name: check_employee
                    changeLog: Removed Tag from Config
                    actionType: config_remove_tag
                    date: Mon Sep 26 2022
                    time: 21:25:18 GMT+0000 (Coordinated Universal Time)
                    updatedBy: John Doe
                    updatedByUserID: fd7dWH15Ddncvl3xhVLH
                    changes: {}
                pagination:
                  itemsPerPage: 3
                  pageNumber: 2
                  totalItems: 829
                  nextPage: statsigapi.net/console/v1/audit_logs?page=3&limit=3
                  previousPage: statsigapi.net/console/v1/audit_logs?page=1&limit=3
                  all: statsigapi.net/console/v1/audit_logs
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    PaginationResponseWithMessage:
      type: object
      properties:
        message:
          type: string
          description: A simple string explaining the result of the operation.
        data:
          description: Array of results returned by pagination limit.
          type: array
          items:
            type: object
        pagination:
          description: Pagination metadata for checking if there is next page for example.
          allOf:
            - $ref: '#/components/schemas/PaginationResponseMetadataDto'
      required:
        - message
        - data
        - pagination
    AuditLogDto:
      type: object
      properties:
        id:
          type: string
          example: abc123
          description: id of the audit log
        name:
          type: string
          example: Gate View
          description: name of the audit log
        changeLog:
          type: string
          example: Edited Gate View
          description: change log of the audit log
        actionType:
          type: object
        date:
          type: string
        time:
          type: string
        updatedBy:
          type: string
        updatedByUserID:
          type: string
        modifierEmail:
          type: object
        changes:
          type: object
        tags:
          type: array
          items:
            type: string
        targetAppIDs:
          type: array
          items:
            type: string
      required:
        - id
        - name
        - changeLog
        - actionType
        - date
        - time
        - updatedBy
        - updatedByUserID
        - modifierEmail
        - changes
        - tags
    PaginationResponseMetadataDto:
      type: object
      properties:
        itemsPerPage:
          type: number
          format: double
        pageNumber:
          type: number
          format: double
        nextPage:
          type: string
          nullable: true
        previousPage:
          type: string
          nullable: true
        totalItems:
          type: number
          format: double
        all:
          type: string
      required:
        - itemsPerPage
        - pageNumber
        - nextPage
        - previousPage
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).
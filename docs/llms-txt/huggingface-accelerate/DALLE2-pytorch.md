# Source: https://github.com/lucidrains/DALLE2-pytorch







<!DOCTYPE html>
<html
  lang="en"
  
  data-color-mode="auto" data-light-theme="light" data-dark-theme="dark"
  data-a11y-animated-images="system" data-a11y-link-underlines="true"
  
  >




  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
  <link rel="preconnect" href="https://avatars.githubusercontent.com">

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light-0c8222dcd7a4f9b7.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light_high_contrast-51c0c6e0c085cc0f.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark-fc6eec18532c3ae0.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark_high_contrast-96d7b2bab5a6ae4e.css" /><link data-color-theme="light" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light-0c8222dcd7a4f9b7.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-51c0c6e0c085cc0f.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-4dd12c5689d6b012.css" /><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-dfa0c9e22ba6ba2b.css" /><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-9fd9c8859395d1a8.css" /><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-9c32304a2a8ac631.css" /><link data-color-theme="dark" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark-fc6eec18532c3ae0.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-96d7b2bab5a6ae4e.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-0c6ca283d4d35cea.css" /><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-2dc46b4919fae81e.css" /><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-271332ec9362e8d3.css" /><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-eb5bb84e91d6d553.css" /><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-f3aa862f2ac7ead2.css" /><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-206b6b93f856629b.css" />

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-primitives-10bf9dd67e3d70bd.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-0fcd9af82350aeda.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-0bd78641c0a1f3e0.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/github-c94ab8d1f22049a8.css" />
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/repository-6ec84ae2261fecf8.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-2d31826944fd3be8.css" />

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["actions_custom_images_storage_billing_ui_visibility","actions_image_version_event","actions_service_container_command","alternate_user_config_repo","arianotify_comprehensive_migration","batch_suggested_changes","billing_discount_threshold_notification","code_scanning_all_branch_query","code_scanning_dfa_degraded_experience_notice","codespaces_prebuild_region_target_update","coding_agent_model_selection","coding_agent_model_selection_all_skus","comment_viewer_copy_raw_markdown","contentful_primer_code_blocks","copilot_agent_image_upload","copilot_agent_snippy","copilot_api_agentic_issue_marshal_yaml","copilot_ask_mode_dropdown","copilot_chat_attach_multiple_images","copilot_chat_clear_model_selection_for_default_change","copilot_chat_enable_tool_call_logs","copilot_chat_explain_error_user_model","copilot_chat_file_redirect","copilot_chat_input_commands","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_code_review_batch_apply_suggestions","copilot_coding_agent_task_response","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_hide_in_dotcom_chat","copilot_extensions_removal_on_marketplace","copilot_features_sql_server_logo","copilot_features_zed_logo","copilot_file_block_ref_matching","copilot_ftp_hyperspace_upgrade_prompt","copilot_icebreakers_experiment_dashboard","copilot_icebreakers_experiment_hyperspace","copilot_immersive_code_block_transition_wrap","copilot_immersive_embedded","copilot_immersive_embedded_mode","copilot_immersive_file_block_transition_open","copilot_immersive_file_preview_keep_mounted","copilot_immersive_job_result_preview","copilot_immersive_layout_routes","copilot_immersive_structured_model_picker","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_mc_cli_resume_any_users_task","copilot_mission_control_always_send_integration_id","copilot_mission_control_cli_resume_with_task_id","copilot_mission_control_decoupled_mode","copilot_mission_control_decoupled_mode_agent_tooltip","copilot_mission_control_initial_data_spinner","copilot_mission_control_scroll_to_bottom_button","copilot_mission_control_task_alive_updates","copilot_org_policy_page_focus_mode","copilot_redirect_header_button_to_agents","copilot_resource_panel","copilot_scroll_preview_tabs","copilot_share_active_subthread","copilot_spaces_ga","copilot_spaces_individual_policies_ga","copilot_spaces_pagination","copilot_spark_empty_state","copilot_spark_handle_nil_friendly_name","copilot_swe_agent_hide_model_picker_if_only_auto","copilot_swe_agent_pr_comment_model_picker","copilot_swe_agent_use_subagents","copilot_task_api_github_rest_style","copilot_unconfigured_is_inherited","copilot_usage_metrics_ga","copilot_workbench_slim_line_top_tabs","custom_instructions_file_references","custom_properties_consolidate_default_value_input","dashboard_add_updated_desc","dashboard_indexeddb_caching","dashboard_lists_max_age_filter","dashboard_universe_2025_feedback_dialog","flex_cta_groups_mvp","global_nav_react","hyperspace_2025_logged_out_batch_1","hyperspace_2025_logged_out_batch_2","hyperspace_2025_logged_out_batch_3","ipm_global_transactional_message_agents","ipm_global_transactional_message_copilot","ipm_global_transactional_message_issues","ipm_global_transactional_message_prs","ipm_global_transactional_message_repos","ipm_global_transactional_message_spaces","issue_cca_modal_open","issue_cca_visualization","issue_fields_global_search","issue_fields_visibility_indicator","issue_fields_visibility_settings","issues_dashboard_inp_optimization","issues_diff_based_label_updates","issues_expanded_file_types","issues_index_semantic_search","issues_lazy_load_comment_box_suggestions","issues_react_bots_timeline_pagination","issues_react_chrome_container_query_fix","issues_react_prohibit_title_fallback","issues_search_type_gql","landing_pages_ninetailed","landing_pages_web_vitals_tracking","lifecycle_label_name_updates","marketing_pages_search_explore_provider","memex_default_issue_create_repository","memex_live_update_hovercard","memex_mwl_filter_field_delimiter","memex_remove_deprecated_type_issue","merge_status_header_feedback","mission_control_retry_on_401","oauth_authorize_clickjacking_protection","open_agent_session_in_vscode_insiders","open_agent_session_in_vscode_stable","primer_react_css_has_selector_perf","primer_react_spinner_synchronize_animations","prs_conversations_react","prx_merge_status_button_alt_logic","pulls_sidebar_update","sample_network_conn_type","secret_scanning_pattern_alerts_link","session_logs_ungroup_reasoning_text","site_features_copilot_universe","site_homepage_collaborate_video","spark_prompt_secret_scanning","spark_server_connection_status","suppress_automated_browser_vitals","viewscreen_sandbox","webp_support","workbench_store_readonly"],"copilotApiOverrideUrl":"https://api.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/high-contrast-cookie-fed1d93364101384.js"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/wp-runtime-535e2541d53f87b0.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/fetch-utilities-78a4114cfa572239.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/85924-e131bec5f99667e1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/28839-734cb6d8a7150172.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/34646-edd5528648c197b1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/environment-51c0968cf21c176d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/runtime-helpers-3bb6f7d6b7a2f531.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2966-f6796bfd155feae1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/96232-69d46a31854353d4.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/41013-7a6deee6d6ff15eb.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/51210-3abb7238871a5b29.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/64247-7de91c52a8aca0eb.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81683-1370179bf9bdc0f0.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/46740-6606b1026a237412.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/53102-f34caec7b425fe9f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/github-elements-32fbe2698fc2a4f0.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/element-registry-2c7c75ef125262db.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-core-2e47687b4310af0f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-lib-a4cf89fce9a1300a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/7053-fe40037405b8998b.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/79039-2565b539a6ebc09b.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/61110-93cf7706e5dc8bfa.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2887-47ac9a4b8862e6bf.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/26533-4df1172b25427069.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/45695-0f7265ae0cee4917.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/86483-92f38323ee870655.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/86659-ee83bc63b54d5ea9.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/60481-19fcf1c5670a41f1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/46287-a173e8d4423a732c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2498-7a413c8209222158.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/61025-40fd5e83cbe4bc66.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/89627-fbbd31c43d83e10c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/49029-32f138b26aa15ad8.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/99328-5e06da57c4622e21.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-71b614800b479109.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/react-core.d14f70276c05a07b.module.css" />
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/4244-d5dcb589fae0ecbf.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/notifications-global-206312e9c9776c21.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/19262-313c6e4aa6bc1abc.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/13284-8b9feeae4ba8bcad.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/19930-d7474e22a5e73a83.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/codespaces-2f877186c025b44c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/42890-dc8a427d0e01e2ea.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/70206-3ba10f6524cc3c66.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/repositories-eeaddac13075ea91.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/34140-bd56b738d77cb446.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/code-menu-34c67a8e6616ccae.js" defer="defer"></script>
  
  <script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/primer-react-72d2ec7521017972.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/octicons-react-a181826f33dcd4d8.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/87376-216370dc132be7e5.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/37869-a873e81f0fcb98e2.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/68751-fe5cb40b5547c377.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/7463-f34e26efc84a7578.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/15272-00d6ef52b0f88c77.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/32769-329cba91f224b6ee.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/46148-0e40187c0246d203.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/91498-c4157c3b474acdfa.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/50938-5b5d5a0255a1f741.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/97519-def3535ce684b22d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/60350-a2a4baae8ada6147.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/24844-58b030e66defd270.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/63991-125a5c660965e63e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/73022-ba0350cffceb8489.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/59852-ef8d9f97624f514a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/3624-6fb548159c275124.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/66231-1e6cc99727940110.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/36600-b3024c97643f0102.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/33684-8c0b5018276812ee.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/18222-498ac30c45b2263a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/96755-8619cf5f811a4353.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/4916-50f2539dc1c5e1ee.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/24787-791cfb59d6b5d03c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/17363-9d3b6dc38025c8e2.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/1097-b805267515cb2087.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/13333-2a2decebccdb5c1f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/5289-399a52981b09bfae.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/62653-b5fad92fb3c5b665.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/54990-adbf64c5251a4ce5.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/20343-336c13a95643eb69.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/9371-07f06acb4933225b.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/49972-40a4b0a31a6433a6.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/87332-2185f20c984174a1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/21384-517aaa5f8010485d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/50110-4385e3caef0c7e52.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/26497-3db8876731818fda.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/66205-ba8d8f244a4626e9.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/45106-197ebc11e66a756f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/61454-b09ac3d8eaae2866.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/code-view-118e0c52ef8863e2.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a2f41fc3ac05567f.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/87332.293e1121826dd022.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/66205.7991bcdd0cea0dd2.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/61454.a9540430471e8db9.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-view.6a2db30287623770.module.css" />

  <script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/75999-af2e3ea53e208314.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/42656-94271233114fb826.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/notifications-subscriptions-menu-2037df81bb0fb115.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a2f41fc3ac05567f.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/notifications-subscriptions-menu.d14124df928c0132.module.css" />


  <title>GitHub - lucidrains/DALLE2-pytorch: Implementation of DALL-E 2, OpenAI&#39;s updated text-to-image synthesis neural network,  in Pytorch · GitHub</title>



  <meta name="route-pattern" content="/:user_id/:repository" data-turbo-transient>
  <meta name="route-controller" content="files" data-turbo-transient>
  <meta name="route-action" content="disambiguate" data-turbo-transient>
  <meta name="fetch-nonce" content="v2:2794b2bc-e069-7a37-3ae9-05ff3bb3b6f8">

    
  <meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb">


  <meta name="request-id" content="9A31:3B2C47:634197:64A86D:69CF3819" data-pjax-transient="true"/><meta name="html-safe-nonce" content="3fec6907d5ca69e855997d63912d7eef04e82da35bc3952fefcad16c65bff9ef" data-pjax-transient="true"/><meta name="visitor-payload" content="eyJyZWZlcnJlciI6IiIsInJlcXVlc3RfaWQiOiI5QTMxOjNCMkM0Nzo2MzQxOTc6NjRBODZEOjY5Q0YzODE5IiwidmlzaXRvcl9pZCI6IjQ1ODA0MTIyMDI5NTE4NTAwMDkiLCJyZWdpb25fZWRnZSI6InNlYSIsInJlZ2lvbl9yZW5kZXIiOiJzZWEifQ==" data-pjax-transient="true"/><meta name="visitor-hmac" content="5d6cae13e110ebebbebc02a805c02632d81da58a295ab82980dc317a64851435" data-pjax-transient="true"/>


    <meta name="hovercard-subject-tag" content="repository:478823173" data-turbo-transient>


  <meta name="github-keyboard-shortcuts" content="repository,copilot" data-turbo-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-turbo-transient>
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" />





  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;" data-turbo-transient="true" />

  




    <meta name="user-login" content="">

  

    <meta name="viewport" content="width=device-width">

    

      <meta name="description" content="Implementation of DALL-E 2, OpenAI&#39;s updated text-to-image synthesis neural network,  in Pytorch - lucidrains/DALLE2-pytorch">

      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">

    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/lucidrains/DALLE2-pytorch" />

      <meta name="twitter:image" content="https://opengraph.githubassets.com/086136b868bed862a16a6e5d5ce449b77a1864f7f1348f2c117b6a7da805f4da/lucidrains/DALLE2-pytorch" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="GitHub - lucidrains/DALLE2-pytorch: Implementation of DALL-E 2, OpenAI&#39;s updated text-to-image synthesis neural network,  in Pytorch" /><meta name="twitter:description" content="Implementation of DALL-E 2, OpenAI&#39;s updated text-to-image synthesis neural network,  in Pytorch - lucidrains/DALLE2-pytorch" />
  <meta property="og:image" content="https://opengraph.githubassets.com/086136b868bed862a16a6e5d5ce449b77a1864f7f1348f2c117b6a7da805f4da/lucidrains/DALLE2-pytorch" /><meta property="og:image:alt" content="Implementation of DALL-E 2, OpenAI&#39;s updated text-to-image synthesis neural network,  in Pytorch - lucidrains/DALLE2-pytorch" /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="GitHub - lucidrains/DALLE2-pytorch: Implementation of DALL-E 2, OpenAI&#39;s updated text-to-image synthesis neural network,  in Pytorch" /><meta property="og:url" content="https://github.com/lucidrains/DALLE2-pytorch" /><meta property="og:description" content="Implementation of DALL-E 2, OpenAI&#39;s updated text-to-image synthesis neural network,  in Pytorch - lucidrains/DALLE2-pytorch" />
  




      <meta name="hostname" content="github.com">



        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="054bece0cc73f4e58bd37a50ea11775db0ea1cc2ed8316bfe9df2d6680f6e202" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="568c098497d98702bac1642a2a853732a047a6ced28eabd3e15d50041a890235" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="20fcfbab4ff75c6eb07df12ea46a99278a956a46f28b2d7e4e7233e3a2a3251e" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="c1fdd7a494e593945bace0638d7b9b4f48b42270f0b51aec4c7da7d5c9e3e30d" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient>

    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/lucidrains/DALLE2-pytorch git https://github.com/lucidrains/DALLE2-pytorch.git">

  <meta name="octolytics-dimension-user_id" content="108653" /><meta name="octolytics-dimension-user_login" content="lucidrains" /><meta name="octolytics-dimension-repository_id" content="478823173" /><meta name="octolytics-dimension-repository_nwo" content="lucidrains/DALLE2-pytorch" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="478823173" /><meta name="octolytics-dimension-repository_network_root_nwo" content="lucidrains/DALLE2-pytorch" />



    

    <meta name="turbo-body-classes" content="logged-out env-production page-responsive">
  <meta name="disable-turbo" content="false">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="release" content="2f925ec0ea72e035ff4a4941945074baa1619e04">
  <meta name="ui-target" content="full">

  <link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg" data-base-href="https://github.githubassets.com/favicons/favicon">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark" />


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-responsive" style="word-wrap: break-word;" >
    <div data-turbo-body class="logged-out env-production page-responsive" style="word-wrap: break-word;" >
      <div id="__primerPortalRoot__" role="region" style="z-index: 1000; position: absolute; width: 100%;" data-turbo-permanent></div>
      

    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="#start-of-content" data-skip-target-assigned="false" class="px-2 tmp-py-4 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a2f41fc3ac05567f.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/keyboard-shortcuts-dialog.f581ff34f52b4167.module.css" />

<react-partial
  partial-name="keyboard-shortcuts-dialog"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>





      

          

              
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/46752-46c707717fcbe6a9.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/sessions-540a49da117bf56f.js" defer="defer"></script>

<style>
  /* Override primer focus outline color for marketing header dropdown links for better contrast */
  [data-color-mode="light"] .HeaderMenu-dropdown-link:focus-visible,
  [data-color-mode="light"] .HeaderMenu-trailing-link a:focus-visible {
    outline-color: var(--color-accent-fg);
  }
</style>

<header class="HeaderMktg header-logged-out js-details-container js-header Details f4 tmp-py-3" role="banner" data-is-top="true" data-color-mode=auto data-light-theme=light data-dark-theme=dark>
  <h2 class="sr-only">Navigation Menu</h2>

  <button type="button" class="HeaderMktg-backdrop d-lg-none border-0 position-fixed top-0 left-0 width-full height-full js-details-target" aria-label="Toggle navigation">
    <span class="d-none">Toggle navigation</span>
  </button>

  <div class="d-flex flex-column flex-lg-row flex-items-center tmp-px-3 tmp-px-md-4 tmp-px-lg-5 height-full position-relative z-1">
    <div class="d-flex flex-justify-between flex-items-center width-full width-lg-auto">
      <div class="flex-1">
        <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="js-details-target js-nav-padding-recalculate js-header-menu-toggle Button--link Button--medium Button d-lg-none color-fg-inherit p-1 tmp-p-1">  <span class="Button-content">
    <span class="Button-label"><div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div></span>
  </span>
</button>
      </div>

      <a class="tmp-mr-lg-3 color-fg-inherit flex-order-2 js-prevent-focus-on-mobile-nav"
        href="/"
        aria-label="Homepage"
        data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Logomark;ref_loc:Header&quot;}">
        <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M10.226 17.284c-2.965-.36-5.054-2.493-5.054-5.256 0-1.123.404-2.336 1.078-3.144-.292-.741-.247-2.314.09-2.965.898-.112 2.111.36 2.83 1.01.853-.269 1.752-.404 2.853-.404 1.1 0 1.999.135 2.807.382.696-.629 1.932-1.1 2.83-.988.315.606.36 2.179.067 2.942.72.854 1.101 2 1.101 3.167 0 2.763-2.089 4.852-5.098 5.234.763.494 1.28 1.572 1.28 2.807v2.336c0 .674.561 1.056 1.235.786 4.066-1.55 7.255-5.615 7.255-10.646C23.5 6.188 18.334 1 11.978 1 5.62 1 .5 6.188.5 12.545c0 4.986 3.167 9.12 7.435 10.669.606.225 1.19-.18 1.19-.786V20.63a2.9 2.9 0 0 1-1.078.224c-1.483 0-2.359-.808-2.987-2.313-.247-.607-.517-.966-1.034-1.033-.27-.023-.359-.135-.359-.27 0-.27.45-.471.898-.471.652 0 1.213.404 1.797 1.235.45.651.921.943 1.483.943.561 0 .92-.202 1.437-.719.382-.381.674-.718.944-.943"></path>
</svg>
      </a>

      <div class="d-flex flex-1 flex-order-2 text-right d-lg-none gap-2 flex-justify-end">
          <a
            href="/login?return_to=https%3A%2F%2Fgithub.com%2Flucidrains%2FDALLE2-pytorch"
            class="HeaderMenu-link HeaderMenu-button d-inline-flex f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit js-prevent-focus-on-mobile-nav"
            data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/lucidrains/DALLE2-pytorch&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="650aa3efe04f23a14f2dd95f8c13893e1b873f19a023cf4532ae67f980847a60"
            data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to Sign in&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}"
          >
            Sign in
          </a>
              <div class="AppHeader-appearanceSettings">
    <react-partial-anchor>
      <button data-target="react-partial-anchor.anchor" id="icon-button-5ee4f96f-d29c-4954-bfc0-d4d84a0d7007" aria-labelledby="tooltip-7ba5d6b5-b5d1-4502-91a1-8cbf1d0802ec" type="button" disabled="disabled" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium AppHeader-button HeaderMenu-link border cursor-wait">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sliders Button-visual">
    <path d="M15 2.75a.75.75 0 0 1-.75.75h-4a.75.75 0 0 1 0-1.5h4a.75.75 0 0 1 .75.75Zm-8.5.75v1.25a.75.75 0 0 0 1.5 0v-4a.75.75 0 0 0-1.5 0V2H1.75a.75.75 0 0 0 0 1.5H6.5Zm1.25 5.25a.75.75 0 0 0 0-1.5h-6a.75.75 0 0 0 0 1.5h6ZM15 8a.75.75 0 0 1-.75.75H11.5V10a.75.75 0 1 1-1.5 0V6a.75.75 0 0 1 1.5 0v1.25h2.75A.75.75 0 0 1 15 8Zm-9 5.25v-2a.75.75 0 0 0-1.5 0v1.25H1.75a.75.75 0 0 0 0 1.5H4.5v1.25a.75.75 0 0 0 1.5 0v-2Zm9 0a.75.75 0 0 1-.75.75h-6a.75.75 0 0 1 0-1.5h6a.75.75 0 0 1 .75.75Z"></path>
</svg>
</button><tool-tip id="tooltip-7ba5d6b5-b5d1-4502-91a1-8cbf1d0802ec" for="icon-button-5ee4f96f-d29c-4954-bfc0-d4d84a0d7007" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Appearance settings</tool-tip>

      <template data-target="react-partial-anchor.template">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a2f41fc3ac05567f.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/appearance-settings.6f14ff9973550c9e.module.css" />

<react-partial
  partial-name="appearance-settings"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>


      </template>
    </react-partial-anchor>
  </div>

      </div>
    </div>


    <div class="HeaderMenu js-header-menu height-fit position-lg-relative d-lg-flex flex-column flex-auto top-0">
      <div class="HeaderMenu-wrapper d-flex flex-column flex-self-start flex-lg-row flex-auto rounded rounded-lg-0">
            <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a2f41fc3ac05567f.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/marketing-navigation.5b4138cab2f44179.module.css" />

<react-partial
  partial-name="marketing-navigation"
  data-ssr="true"
  data-attempted-ssr="true"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"should_use_dotcom_links":true}}</script>
  <div data-target="react-partial.reactRoot"><nav class="MarketingNavigation-module__nav__W0KYY" aria-label="Global"><ul class="MarketingNavigation-module__list__tFbMb"><li><div class="NavDropdown-module__container__l2YeI js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button__PEHWX js-details-target" aria-expanded="false">Platform<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">AI CODE CREATION</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/features/copilot" data-analytics-event="{&quot;action&quot;:&quot;github_copilot&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_copilot_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Copilot</span><span class="NavLink-module__subtitle__X4gkW">Write better code with AI</span></div></a></li><li><a href="https://github.com/features/spark" data-analytics-event="{&quot;action&quot;:&quot;github_spark&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_spark_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-sparkle-fill NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.296 1.924c.24-.656 1.168-.656 1.408 0l.717 1.958a11.25 11.25 0 0 0 6.697 6.697l1.958.717c.657.24.657 1.168 0 1.408l-1.958.717a11.25 11.25 0 0 0-6.697 6.697l-.717 1.958c-.24.657-1.168.657-1.408 0l-.717-1.958a11.25 11.25 0 0 0-6.697-6.697l-1.958-.717c-.656-.24-.656-1.168 0-1.408l1.958-.717a11.25 11.25 0 0 0 6.697-6.697l.717-1.958Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Spark</span><span class="NavLink-module__subtitle__X4gkW">Build and deploy intelligent apps</span></div></a></li><li><a href="https://github.com/features/models" data-analytics-event="{&quot;action&quot;:&quot;github_models&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_models_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-ai-model NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M19.375 8.5a3.25 3.25 0 1 1-3.163 4h-3a3.252 3.252 0 0 1-4.443 2.509L7.214 17.76a3.25 3.25 0 1 1-1.342-.674l1.672-2.957A3.238 3.238 0 0 1 6.75 12c0-.907.371-1.727.97-2.316L6.117 6.846A3.253 3.253 0 0 1 1.875 3.75a3.25 3.25 0 1 1 5.526 2.32l1.603 2.836A3.25 3.25 0 0 1 13.093 11h3.119a3.252 3.252 0 0 1 3.163-2.5ZM10 10.25a1.75 1.75 0 1 0-.001 3.499A1.75 1.75 0 0 0 10 10.25ZM5.125 2a1.75 1.75 0 1 0 0 3.5 1.75 1.75 0 0 0 0-3.5Zm12.5 9.75a1.75 1.75 0 1 0 3.5 0 1.75 1.75 0 0 0-3.5 0Zm-14.25 8.5a1.75 1.75 0 1 0 3.501-.001 1.75 1.75 0 0 0-3.501.001Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Models</span><span class="NavLink-module__subtitle__X4gkW">Manage and compare prompts</span></div></a></li><li><a href="https://github.com/mcp" data-analytics-event="{&quot;action&quot;:&quot;mcp_registry&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;mcp_registry_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-mcp NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.795 1.694a4.287 4.287 0 0 1 6.061 0 4.28 4.28 0 0 1 1.181 3.819 4.282 4.282 0 0 1 3.819 1.181 4.287 4.287 0 0 1 0 6.061l-6.793 6.793a.249.249 0 0 0 0 .353l2.617 2.618a.75.75 0 1 1-1.061 1.061l-2.617-2.618a1.75 1.75 0 0 1 0-2.475l6.793-6.793a2.785 2.785 0 1 0-3.939-3.939l-5.9 5.9a.734.734 0 0 1-.249.165.749.749 0 0 1-.812-1.225l5.9-5.901a2.785 2.785 0 1 0-3.939-3.939L2.931 10.68A.75.75 0 1 1 1.87 9.619l7.925-7.925Z"></path><path d="M12.42 4.069a.752.752 0 0 1 1.061 0 .752.752 0 0 1 0 1.061L7.33 11.28a2.788 2.788 0 0 0 0 3.94 2.788 2.788 0 0 0 3.94 0l6.15-6.151a.752.752 0 0 1 1.061 0 .752.752 0 0 1 0 1.061l-6.151 6.15a4.285 4.285 0 1 1-6.06-6.06l6.15-6.151Z"></path></svg><span class="NavLink-module__title__Q7t0p">MCP Registry<sup class="NavLink-module__label__bil7n">New</sup></span><span class="NavLink-module__subtitle__X4gkW">Integrate external tools</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">DEVELOPER WORKFLOWS</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/features/actions" data-analytics-event="{&quot;action&quot;:&quot;actions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;actions_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-workflow NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 3a2 2 0 0 1 2-2h6.5a2 2 0 0 1 2 2v6.5a2 2 0 0 1-2 2H7v4.063C7 16.355 7.644 17 8.438 17H12.5v-2.5a2 2 0 0 1 2-2H21a2 2 0 0 1 2 2V21a2 2 0 0 1-2 2h-6.5a2 2 0 0 1-2-2v-2.5H8.437A2.939 2.939 0 0 1 5.5 15.562V11.5H3a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v6.5a.5.5 0 0 0 .5.5h6.5a.5.5 0 0 0 .5-.5V3a.5.5 0 0 0-.5-.5ZM14.5 14a.5.5 0 0 0-.5.5V21a.5.5 0 0 0 .5.5H21a.5.5 0 0 0 .5-.5v-6.5a.5.5 0 0 0-.5-.5Z"></path></svg><span class="NavLink-module__title__Q7t0p">Actions</span><span class="NavLink-module__subtitle__X4gkW">Automate any workflow</span></div></a></li><li><a href="https://github.com/features/codespaces" data-analytics-event="{&quot;action&quot;:&quot;codespaces&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;codespaces_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-codespaces NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.5 3.75C3.5 2.784 4.284 2 5.25 2h13.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 18.75 13H5.25a1.75 1.75 0 0 1-1.75-1.75Zm-2 12c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v4a1.75 1.75 0 0 1-1.75 1.75H3.25a1.75 1.75 0 0 1-1.75-1.75ZM5.25 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h13.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Zm-2 12a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h17.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25Z"></path><path d="M10 17.75a.75.75 0 0 1 .75-.75h6.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path></svg><span class="NavLink-module__title__Q7t0p">Codespaces</span><span class="NavLink-module__subtitle__X4gkW">Instant dev environments</span></div></a></li><li><a href="https://github.com/features/issues" data-analytics-event="{&quot;action&quot;:&quot;issues&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;issues_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M12 1c6.075 0 11 4.925 11 11s-4.925 11-11 11S1 18.075 1 12 5.925 1 12 1ZM2.5 12a9.5 9.5 0 0 0 9.5 9.5 9.5 9.5 0 0 0 9.5-9.5A9.5 9.5 0 0 0 12 2.5 9.5 9.5 0 0 0 2.5 12Zm9.5 2a2 2 0 1 1-.001-3.999A2 2 0 0 1 12 14Z"></path></svg><span class="NavLink-module__title__Q7t0p">Issues</span><span class="NavLink-module__subtitle__X4gkW">Plan and track work</span></div></a></li><li><a href="https://github.com/features/code-review" data-analytics-event="{&quot;action&quot;:&quot;code_review&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;code_review_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-code NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M15.22 4.97a.75.75 0 0 1 1.06 0l6.5 6.5a.75.75 0 0 1 0 1.06l-6.5 6.5a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L21.19 12l-5.97-5.97a.75.75 0 0 1 0-1.06Zm-6.44 0a.75.75 0 0 1 0 1.06L2.81 12l5.97 5.97a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-6.5-6.5a.75.75 0 0 1 0-1.06l6.5-6.5a.75.75 0 0 1 1.06 0Z"></path></svg><span class="NavLink-module__title__Q7t0p">Code Review</span><span class="NavLink-module__subtitle__X4gkW">Manage code changes</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">APPLICATION SECURITY</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/security/advanced-security" data-analytics-event="{&quot;action&quot;:&quot;github_advanced_security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_advanced_security_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-shield-check NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Advanced Security</span><span class="NavLink-module__subtitle__X4gkW">Find and fix vulnerabilities</span></div></a></li><li><a href="https://github.com/security/advanced-security/code-security" data-analytics-event="{&quot;action&quot;:&quot;code_security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;code_security_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-code-square NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.3 8.24a.75.75 0 0 1-.04 1.06L7.352 12l2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M2 3.75C2 2.784 2.784 2 3.75 2h16.5c.966 0 1.75.784 1.75 1.75v16.5A1.75 1.75 0 0 1 20.25 22H3.75A1.75 1.75 0 0 1 2 20.25Zm1.75-.25a.25.25 0 0 0-.25.25v16.5c0 .138.112.25.25.25h16.5a.25.25 0 0 0 .25-.25V3.75a.25.25 0 0 0-.25-.25Z"></path></svg><span class="NavLink-module__title__Q7t0p">Code security</span><span class="NavLink-module__subtitle__X4gkW">Secure your code as you build</span></div></a></li><li><a href="https://github.com/security/advanced-security/secret-protection" data-analytics-event="{&quot;action&quot;:&quot;secret_protection&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;secret_protection_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-lock NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6 9V7.25C6 3.845 8.503 1 12 1s6 2.845 6 6.25V9h.5a2.5 2.5 0 0 1 2.5 2.5v8a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 19.5v-8A2.5 2.5 0 0 1 5.5 9Zm-1.5 2.5v8a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1v-8a1 1 0 0 0-1-1h-13a1 1 0 0 0-1 1Zm3-4.25V9h9V7.25c0-2.67-1.922-4.75-4.5-4.75-2.578 0-4.5 2.08-4.5 4.75Z"></path></svg><span class="NavLink-module__title__Q7t0p">Secret protection</span><span class="NavLink-module__subtitle__X4gkW">Stop leaks before they start</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ NavGroup-module__hasSeparator__FnMrN"><span class="NavGroup-module__title__Wzxz2">EXPLORE</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/why-github" data-analytics-event="{&quot;action&quot;:&quot;why_github&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;why_github_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Why GitHub</span></a></li><li><a href="https://docs.github.com" data-analytics-event="{&quot;action&quot;:&quot;documentation&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;documentation_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Documentation</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.blog" data-analytics-event="{&quot;action&quot;:&quot;blog&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;blog_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Blog</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.blog/changelog" data-analytics-event="{&quot;action&quot;:&quot;changelog&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;changelog_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Changelog</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.com/marketplace" data-analytics-event="{&quot;action&quot;:&quot;marketplace&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;marketplace_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Marketplace</span></a></li></ul></div></li></ul><div class="NavDropdown-module__trailingLinkContainer__VgJGL"><a href="https://github.com/features" data-analytics-event="{&quot;action&quot;:&quot;view_all_features&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_features_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all features</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></div></div></div></li><li><div class="NavDropdown-module__container__l2YeI js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button__PEHWX js-details-target" aria-expanded="false">Solutions<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">BY COMPANY SIZE</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/enterprise" data-analytics-event="{&quot;action&quot;:&quot;enterprises&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;enterprises_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Enterprises</span></a></li><li><a href="https://github.com/team" data-analytics-event="{&quot;action&quot;:&quot;small_and_medium_teams&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;small_and_medium_teams_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Small and medium teams</span></a></li><li><a href="https://github.com/enterprise/startups" data-analytics-event="{&quot;action&quot;:&quot;startups&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;startups_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Startups</span></a></li><li><a href="https://github.com/solutions/industry/nonprofits" data-analytics-event="{&quot;action&quot;:&quot;nonprofits&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;nonprofits_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Nonprofits</span></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">BY USE CASE</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/solutions/use-case/app-modernization" data-analytics-event="{&quot;action&quot;:&quot;app_modernization&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;app_modernization_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">App Modernization</span></a></li><li><a href="https://github.com/solutions/use-case/devsecops" data-analytics-event="{&quot;action&quot;:&quot;devsecops&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;devsecops_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">DevSecOps</span></a></li><li><a href="https://github.com/solutions/use-case/devops" data-analytics-event="{&quot;action&quot;:&quot;devops&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;devops_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">DevOps</span></a></li><li><a href="https://github.com/solutions/use-case/ci-cd" data-analytics-event="{&quot;action&quot;:&quot;ci/cd&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;ci/cd_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">CI/CD</span></a></li><li><a href="https://github.com/solutions/use-case" data-analytics-event="{&quot;action&quot;:&quot;view_all_use_cases&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_use_cases_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all use cases</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">BY INDUSTRY</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/solutions/industry/healthcare" data-analytics-event="{&quot;action&quot;:&quot;healthcare&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;healthcare_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Healthcare</span></a></li><li><a href="https://github.com/solutions/industry/financial-services" data-analytics-event="{&quot;action&quot;:&quot;financial_services&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;financial_services_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Financial services</span></a></li><li><a href="https://github.com/solutions/industry/manufacturing" data-analytics-event="{&quot;action&quot;:&quot;manufacturing&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;manufacturing_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Manufacturing</span></a></li><li><a href="https://github.com/solutions/industry/government" data-analytics-event="{&quot;action&quot;:&quot;government&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;government_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Government</span></a></li><li><a href="https://github.com/solutions/industry" data-analytics-event="{&quot;action&quot;:&quot;view_all_industries&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_industries_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all industries</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></li></ul></div></li></ul><div class="NavDropdown-module__trailingLinkContainer__VgJGL"><a href="https://github.com/solutions" data-analytics-event="{&quot;action&quot;:&quot;view_all_solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_solutions_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all solutions</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></div></div></div></li><li><div class="NavDropdown-module__container__l2YeI js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button__PEHWX js-details-target" aria-expanded="false">Resources<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">EXPLORE BY TOPIC</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/resources/articles?topic=ai" data-analytics-event="{&quot;action&quot;:&quot;ai&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;ai_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">AI</span></a></li><li><a href="https://github.com/resources/articles?topic=software-development" data-analytics-event="{&quot;action&quot;:&quot;software_development&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;software_development_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Software Development</span></a></li><li><a href="https://github.com/resources/articles?topic=devops" data-analytics-event="{&quot;action&quot;:&quot;devops&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;devops_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">DevOps</span></a></li><li><a href="https://github.com/resources/articles?topic=security" data-analytics-event="{&quot;action&quot;:&quot;security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;security_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Security</span></a></li><li><a href="https://github.com/resources/articles" data-analytics-event="{&quot;action&quot;:&quot;view_all_topics&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_topics_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all topics</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">EXPLORE BY TYPE</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/customer-stories" data-analytics-event="{&quot;action&quot;:&quot;customer_stories&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;customer_stories_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Customer stories</span></a></li><li><a href="https://github.com/resources/events" data-analytics-event="{&quot;action&quot;:&quot;events__webinars&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;events__webinars_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Events &amp; webinars</span></a></li><li><a href="https://github.com/resources/whitepapers" data-analytics-event="{&quot;action&quot;:&quot;ebooks__reports&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;ebooks__reports_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Ebooks &amp; reports</span></a></li><li><a href="https://github.com/solutions/executive-insights" data-analytics-event="{&quot;action&quot;:&quot;business_insights&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;business_insights_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Business insights</span></a></li><li><a href="https://skills.github.com" data-analytics-event="{&quot;action&quot;:&quot;github_skills&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_skills_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">GitHub Skills</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">SUPPORT &amp; SERVICES</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://docs.github.com" data-analytics-event="{&quot;action&quot;:&quot;documentation&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;documentation_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Documentation</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://support.github.com" data-analytics-event="{&quot;action&quot;:&quot;customer_support&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;customer_support_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Customer support</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.com/orgs/community/discussions" data-analytics-event="{&quot;action&quot;:&quot;community_forum&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;community_forum_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Community forum</span></a></li><li><a href="https://github.com/trust-center" data-analytics-event="{&quot;action&quot;:&quot;trust_center&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;trust_center_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Trust center</span></a></li><li><a href="https://github.com/partners" data-analytics-event="{&quot;action&quot;:&quot;partners&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;partners_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Partners</span></a></li></ul></div></li></ul><div class="NavDropdown-module__trailingLinkContainer__VgJGL"><a href="https://github.com/resources" data-analytics-event="{&quot;action&quot;:&quot;view_all_resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_resources_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all resources</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></div></div></div></li><li><div class="NavDropdown-module__container__l2YeI js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button__PEHWX js-details-target" aria-expanded="false">Open Source<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">COMMUNITY</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/sponsors" data-analytics-event="{&quot;action&quot;:&quot;github_sponsors&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_sponsors_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-sponsor-tiers NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M16.004 1.25C18.311 1.25 20 3.128 20 5.75c0 2.292-1.23 4.464-3.295 6.485-.481.47-.98.909-1.482 1.31l.265 1.32 1.375 7.5a.75.75 0 0 1-.982.844l-3.512-1.207a.75.75 0 0 0-.488 0L8.37 23.209a.75.75 0 0 1-.982-.844l1.378-7.512.261-1.309c-.5-.4-1-.838-1.481-1.31C5.479 10.215 4.25 8.043 4.25 5.75c0-2.622 1.689-4.5 3.996-4.5 1.55 0 2.947.752 3.832 1.967l.047.067.047-.067a4.726 4.726 0 0 1 3.612-1.962l.22-.005ZM13.89 14.531c-.418.285-.828.542-1.218.77l-.18.103a.75.75 0 0 1-.734 0l-.071-.04-.46-.272c-.282-.173-.573-.36-.868-.562l-.121.605-1.145 6.239 2.3-.79a2.248 2.248 0 0 1 1.284-.054l.18.053 2.299.79-1.141-6.226-.125-.616ZM16.004 2.75c-1.464 0-2.731.983-3.159 2.459-.209.721-1.231.721-1.44 0-.428-1.476-1.695-2.459-3.16-2.459-1.44 0-2.495 1.173-2.495 3 0 1.811 1.039 3.647 2.844 5.412a19.624 19.624 0 0 0 3.734 2.84l-.019-.011-.184-.111.147-.088a19.81 19.81 0 0 0 3.015-2.278l.37-.352C17.46 9.397 18.5 7.561 18.5 5.75c0-1.827-1.055-3-2.496-3Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Sponsors</span><span class="NavLink-module__subtitle__X4gkW">Fund open source developers</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">PROGRAMS</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://securitylab.github.com" data-analytics-event="{&quot;action&quot;:&quot;security_lab&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;security_lab_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Security Lab</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://maintainers.github.com" data-analytics-event="{&quot;action&quot;:&quot;maintainer_community&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;maintainer_community_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Maintainer Community</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.com/accelerator" data-analytics-event="{&quot;action&quot;:&quot;accelerator&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;accelerator_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Accelerator</span></a></li><li><a href="https://stars.github.com" data-analytics-event="{&quot;action&quot;:&quot;github_stars&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_stars_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">GitHub Stars</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://archiveprogram.github.com" data-analytics-event="{&quot;action&quot;:&quot;archive_program&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;archive_program_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Archive Program</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">REPOSITORIES</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/topics" data-analytics-event="{&quot;action&quot;:&quot;topics&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;topics_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Topics</span></a></li><li><a href="https://github.com/trending" data-analytics-event="{&quot;action&quot;:&quot;trending&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;trending_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Trending</span></a></li><li><a href="https://github.com/collections" data-analytics-event="{&quot;action&quot;:&quot;collections&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;collections_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Collections</span></a></li></ul></div></li></ul></div></div></li><li><div class="NavDropdown-module__container__l2YeI js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button__PEHWX js-details-target" aria-expanded="false">Enterprise<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">ENTERPRISE SOLUTIONS</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/enterprise" data-analytics-event="{&quot;action&quot;:&quot;enterprise_platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;enterprise_platform_link_enterprise_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-stack NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.063 1.456a1.749 1.749 0 0 1 1.874 0l8.383 5.316a1.751 1.751 0 0 1 0 2.956l-8.383 5.316a1.749 1.749 0 0 1-1.874 0L2.68 9.728a1.751 1.751 0 0 1 0-2.956Zm1.071 1.267a.25.25 0 0 0-.268 0L3.483 8.039a.25.25 0 0 0 0 .422l8.383 5.316a.25.25 0 0 0 .268 0l8.383-5.316a.25.25 0 0 0 0-.422Z"></path><path d="M1.867 12.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path><path d="M1.867 16.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path></svg><span class="NavLink-module__title__Q7t0p">Enterprise platform</span><span class="NavLink-module__subtitle__X4gkW">AI-powered developer platform</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">AVAILABLE ADD-ONS</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/security/advanced-security" data-analytics-event="{&quot;action&quot;:&quot;github_advanced_security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_advanced_security_link_enterprise_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-shield-check NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Advanced Security</span><span class="NavLink-module__subtitle__X4gkW">Enterprise-grade security features</span></div></a></li><li><a href="https://github.com/features/copilot/copilot-business" data-analytics-event="{&quot;action&quot;:&quot;copilot_for_business&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;copilot_for_business_link_enterprise_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path></svg><span class="NavLink-module__title__Q7t0p">Copilot for Business</span><span class="NavLink-module__subtitle__X4gkW">Enterprise-grade AI features</span></div></a></li><li><a href="https://github.com/premium-support" data-analytics-event="{&quot;action&quot;:&quot;premium_support&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;premium_support_link_enterprise_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-comment-discussion NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path></svg><span class="NavLink-module__title__Q7t0p">Premium Support</span><span class="NavLink-module__subtitle__X4gkW">Enterprise-grade 24/7 support</span></div></a></li></ul></div></li></ul></div></div></li><li><a href="https://github.com/pricing" data-analytics-event="{&quot;action&quot;:&quot;pricing&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;pricing&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;pricing_link_pricing_navbar&quot;}" class="NavLink-module__link__EG3d4 MarketingNavigation-module__navLink__hUomM"><span class="NavLink-module__title__Q7t0p">Pricing</span></a></li></ul></nav><script type="application/json" id="__PRIMER_DATA__R_0___">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>



        <div class="d-flex flex-column flex-lg-row width-full flex-justify-end flex-lg-items-center text-center tmp-mt-3 tmp-mt-lg-0 text-lg-left tmp-ml-lg-3">
                


<qbsearch-input class="search-input" data-scope="repo:lucidrains/DALLE2-pytorch" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="I_nHv5wwkDD3DIXGbT2Ga3YZAJh975Q9ttrqGHaAqQpr2HY4R2PUKHFN82HxDBhDJPNv6O04pk72ktrbFD2Mag" data-max-custom-scopes="10" data-header-redesign-enabled="false" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="lucidrains/DALLE2-pytorch" data-current-org="" data-current-owner="lucidrains" data-logged-in="false" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-retain-scroll-position="true">
  <div
    class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center tmp-mr-4 rounded"
    data-action="click:qbsearch-input#searchInputContainerClicked"
  >
      <button
        type="button"
        class="header-search-button placeholder  input-button form-control d-flex flex-1 flex-self-stretch flex-items-center no-wrap width-full py-0 pl-2 pr-0 text-left border-0 box-shadow-none"
        data-target="qbsearch-input.inputButton"
        aria-label="Search or jump to…"
        aria-haspopup="dialog"
        placeholder="Search or jump to..."
        data-hotkey=s,/
        autocapitalize="off"
        data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;searchbar&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;input&quot;,&quot;label&quot;:&quot;searchbar_input_global_navbar&quot;}"
        data-action="click:qbsearch-input#handleExpand"
      >
        <div class="mr-2 color-fg-muted">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <span class="flex-1" data-target="qbsearch-input.inputButtonText">Search or jump to...</span>
          <div class="d-flex" data-target="qbsearch-input.hotkeyIndicator">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="20" aria-hidden="true" class="mr-1"><path fill="none" stroke="#979A9C" opacity=".4" d="M3.5.5h12c1.7 0 3 1.3 3 3v13c0 1.7-1.3 3-3 3h-12c-1.7 0-3-1.3-3-3v-13c0-1.7 1.3-3 3-3z"></path><path fill="#979A9C" d="M11.8 6L8 15.1h-.9L10.8 6h1z"></path></svg>
          </div>
      </button>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay>
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-large Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-fixed width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container"
          style="border-radius: 12px;"
          data-target="qbsearch-input.queryBuilderContainer"
          hidden
        >
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="query-builder-test-form" action="" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div
        class="QueryBuilder-StyledInput width-fit "
        data-target="query-builder.styledInput"
      >
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div
            aria-hidden="true"
            class="QueryBuilder-StyledInputContent"
            data-target="query-builder.styledInputContent"
          ></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-8e28b114-3b1e-404e-9f3c-ecd3dac31c04" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" />
          </div>
        </div>
          <span data-target="query-builder.clearButton" hidden>
            <span class="sr-only" id="query-builder-test-clear">Clear</span>
            <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-action="
                  click:query-builder#clear
                  focus:query-builder#clearButtonFocus
                  blur:query-builder#clearButtonBlur
                " variant="small" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 tmp-mr-1 px-2 tmp-px-2 py-0 tmp-py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

          </span>
      </div>
      <template id="search-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
</template>

<template id="code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</template>

<template id="file-code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-code">
    <path d="M4 1.75C4 .784 4.784 0 5.75 0h5.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v8.586A1.75 1.75 0 0 1 14.25 15h-9a.75.75 0 0 1 0-1.5h9a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 10 4.25V1.5H5.75a.25.25 0 0 0-.25.25v2.5a.75.75 0 0 1-1.5 0Zm1.72 4.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.47-1.47-1.47-1.47a.75.75 0 0 1 0-1.06ZM3.28 7.78 1.81 9.25l1.47 1.47a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Zm8.22-6.218V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path>
</svg>
</template>

<template id="history-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-history">
    <path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path>
</svg>
</template>

<template id="repo-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
</template>

<template id="bookmark-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bookmark">
    <path d="M3 2.75C3 1.784 3.784 1 4.75 1h6.5c.966 0 1.75.784 1.75 1.75v11.5a.75.75 0 0 1-1.227.579L8 11.722l-3.773 3.107A.751.751 0 0 1 3 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v9.91l3.023-2.489a.75.75 0 0 1 .954 0l3.023 2.49V2.75a.25.25 0 0 0-.25-.25Z"></path>
</svg>
</template>

<template id="plus-circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus-circle">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm7.25-3.25v2.5h2.5a.75.75 0 0 1 0 1.5h-2.5v2.5a.75.75 0 0 1-1.5 0v-2.5h-2.5a.75.75 0 0 1 0-1.5h2.5v-2.5a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</template>

<template id="circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
</template>

<template id="trash-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-trash">
    <path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path>
</svg>
</template>

<template id="team-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
</template>

<template id="project-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
</template>

<template id="pencil-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pencil">
    <path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path>
</svg>
</template>

<template id="copilot-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</template>

<template id="copilot-error-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot-error">
    <path d="M16 11.24c0 .112-.072.274-.21.467L13 9.688V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-.198 0-.388-.009-.571-.029L6.833 5.226a4.01 4.01 0 0 0 .17-.782c.117-.935-.037-1.395-.241-1.614-.193-.206-.637-.413-1.682-.297-.683.076-1.115.231-1.395.415l-1.257-.91c.579-.564 1.413-.877 2.485-.996 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095Zm-5.083-8.707c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Zm2.511 11.074c-1.393.776-3.272 1.428-5.43 1.428-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.18-.455-.241-.963-.252-1.475L.31 4.107A.747.747 0 0 1 0 3.509V3.49a.748.748 0 0 1 .625-.73c.156-.026.306.047.435.139l14.667 10.578a.592.592 0 0 1 .227.264.752.752 0 0 1 .046.249v.022a.75.75 0 0 1-1.19.596Zm-1.367-.991L5.635 7.964a5.128 5.128 0 0 1-.889.073c-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433 1.539 0 3.089-.505 4.063-.934Z"></path>
</svg>
</template>

<template id="workflow-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-workflow">
    <path d="M0 1.75C0 .784.784 0 1.75 0h3.5C6.216 0 7 .784 7 1.75v3.5A1.75 1.75 0 0 1 5.25 7H4v4a1 1 0 0 0 1 1h4v-1.25C9 9.784 9.784 9 10.75 9h3.5c.966 0 1.75.784 1.75 1.75v3.5A1.75 1.75 0 0 1 14.25 16h-3.5A1.75 1.75 0 0 1 9 14.25v-.75H5A2.5 2.5 0 0 1 2.5 11V7h-.75A1.75 1.75 0 0 1 0 5.25Zm1.75-.25a.25.25 0 0 0-.25.25v3.5c0 .138.112.25.25.25h3.5a.25.25 0 0 0 .25-.25v-3.5a.25.25 0 0 0-.25-.25Zm9 9a.25.25 0 0 0-.25.25v3.5c0 .138.112.25.25.25h3.5a.25.25 0 0 0 .25-.25v-3.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
</template>

<template id="book-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
</template>

<template id="code-review-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-review">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 13H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 14.543V13H1.75A1.75 1.75 0 0 1 0 11.25v-8.5C0 1.784.784 1 1.75 1ZM1.5 2.75v8.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Zm5.28 1.72a.75.75 0 0 1 0 1.06L5.31 7l1.47 1.47a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-2-2a.75.75 0 0 1 0-1.06l2-2a.75.75 0 0 1 1.06 0Zm2.44 0a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L10.69 7 9.22 5.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</template>

<template id="codespaces-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
</template>

<template id="comment-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment">
    <path d="M1 2.75C1 1.784 1.784 1 2.75 1h10.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 13.25 12H9.06l-2.573 2.573A1.458 1.458 0 0 1 4 13.543V12H2.75A1.75 1.75 0 0 1 1 10.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h4.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
</template>

<template id="comment-discussion-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</template>

<template id="organization-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-organization">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</template>

<template id="rocket-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-rocket">
    <path d="M14.064 0h.186C15.216 0 16 .784 16 1.75v.186a8.752 8.752 0 0 1-2.564 6.186l-.458.459c-.314.314-.641.616-.979.904v3.207c0 .608-.315 1.172-.833 1.49l-2.774 1.707a.749.749 0 0 1-1.11-.418l-.954-3.102a1.214 1.214 0 0 1-.145-.125L3.754 9.816a1.218 1.218 0 0 1-.124-.145L.528 8.717a.749.749 0 0 1-.418-1.11l1.71-2.774A1.748 1.748 0 0 1 3.31 4h3.204c.288-.338.59-.665.904-.979l.459-.458A8.749 8.749 0 0 1 14.064 0ZM8.938 3.623h-.002l-.458.458c-.76.76-1.437 1.598-2.02 2.5l-1.5 2.317 2.143 2.143 2.317-1.5c.902-.583 1.74-1.26 2.499-2.02l.459-.458a7.25 7.25 0 0 0 2.123-5.127V1.75a.25.25 0 0 0-.25-.25h-.186a7.249 7.249 0 0 0-5.125 2.123ZM3.56 14.56c-.732.732-2.334 1.045-3.005 1.148a.234.234 0 0 1-.201-.064.234.234 0 0 1-.064-.201c.103-.671.416-2.273 1.15-3.003a1.502 1.502 0 1 1 2.12 2.12Zm6.94-3.935c-.088.06-.177.118-.266.175l-2.35 1.521.548 1.783 1.949-1.2a.25.25 0 0 0 .119-.213ZM3.678 8.116 5.2 5.766c.058-.09.117-.178.176-.266H3.309a.25.25 0 0 0-.213.119l-1.2 1.95ZM12 5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
</template>

<template id="shield-check-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield-check">
    <path d="m8.533.133 5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667l5.25-1.68a1.748 1.748 0 0 1 1.066 0Zm-.61 1.429.001.001-5.25 1.68a.251.251 0 0 0-.174.237V7c0 1.36.275 2.666 1.057 3.859.784 1.194 2.121 2.342 4.366 3.298a.196.196 0 0 0 .154 0c2.245-.957 3.582-2.103 4.366-3.297C13.225 9.666 13.5 8.358 13.5 7V3.48a.25.25 0 0 0-.174-.238l-5.25-1.68a.25.25 0 0 0-.153 0ZM11.28 6.28l-3.5 3.5a.75.75 0 0 1-1.06 0l-1.5-1.5a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l.97.97 2.97-2.97a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
</template>

<template id="heart-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heart">
    <path d="m8 14.25.345.666a.75.75 0 0 1-.69 0l-.008-.004-.018-.01a7.152 7.152 0 0 1-.31-.17 22.055 22.055 0 0 1-3.434-2.414C2.045 10.731 0 8.35 0 5.5 0 2.836 2.086 1 4.25 1 5.797 1 7.153 1.802 8 3.02 8.847 1.802 10.203 1 11.75 1 13.914 1 16 2.836 16 5.5c0 2.85-2.045 5.231-3.885 6.818a22.066 22.066 0 0 1-3.744 2.584l-.018.01-.006.003h-.002ZM4.25 2.5c-1.336 0-2.75 1.164-2.75 3 0 2.15 1.58 4.144 3.365 5.682A20.58 20.58 0 0 0 8 13.393a20.58 20.58 0 0 0 3.135-2.211C12.92 9.644 14.5 7.65 14.5 5.5c0-1.836-1.414-3-2.75-3-1.373 0-2.609.986-3.029 2.456a.749.749 0 0 1-1.442 0C6.859 3.486 5.623 2.5 4.25 2.5Z"></path>
</svg>
</template>

<template id="server-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-server">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v4c0 .372-.116.717-.314 1 .198.283.314.628.314 1v4a1.75 1.75 0 0 1-1.75 1.75H1.75A1.75 1.75 0 0 1 0 12.75v-4c0-.358.109-.707.314-1a1.739 1.739 0 0 1-.314-1v-4C0 1.784.784 1 1.75 1ZM1.5 2.75v4c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Zm.25 5.75a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25ZM7 4.75A.75.75 0 0 1 7.75 4h4.5a.75.75 0 0 1 0 1.5h-4.5A.75.75 0 0 1 7 4.75ZM7.75 10h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1 0-1.5ZM3 4.75A.75.75 0 0 1 3.75 4h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 4.75ZM3.75 10h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</template>

<template id="globe-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-globe">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM5.78 8.75a9.64 9.64 0 0 0 1.363 4.177c.255.426.542.832.857 1.215.245-.296.551-.705.857-1.215A9.64 9.64 0 0 0 10.22 8.75Zm4.44-1.5a9.64 9.64 0 0 0-1.363-4.177c-.307-.51-.612-.919-.857-1.215a9.927 9.927 0 0 0-.857 1.215A9.64 9.64 0 0 0 5.78 7.25Zm-5.944 1.5H1.543a6.507 6.507 0 0 0 4.666 5.5c-.123-.181-.24-.365-.352-.552-.715-1.192-1.437-2.874-1.581-4.948Zm-2.733-1.5h2.733c.144-2.074.866-3.756 1.58-4.948.12-.197.237-.381.353-.552a6.507 6.507 0 0 0-4.666 5.5Zm10.181 1.5c-.144 2.074-.866 3.756-1.58 4.948-.12.197-.237.381-.353.552a6.507 6.507 0 0 0 4.666-5.5Zm2.733-1.5a6.507 6.507 0 0 0-4.666-5.5c.123.181.24.365.353.552.714 1.192 1.436 2.874 1.58 4.948Z"></path>
</svg>
</template>

<template id="issue-opened-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</template>

<template id="device-mobile-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-device-mobile">
    <path d="M3.75 0h8.5C13.216 0 14 .784 14 1.75v12.5A1.75 1.75 0 0 1 12.25 16h-8.5A1.75 1.75 0 0 1 2 14.25V1.75C2 .784 2.784 0 3.75 0ZM3.5 1.75v12.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM8 13a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
</template>

<template id="package-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-package">
    <path d="m8.878.392 5.25 3.045c.54.314.872.89.872 1.514v6.098a1.75 1.75 0 0 1-.872 1.514l-5.25 3.045a1.75 1.75 0 0 1-1.756 0l-5.25-3.045A1.75 1.75 0 0 1 1 11.049V4.951c0-.624.332-1.201.872-1.514L7.122.392a1.75 1.75 0 0 1 1.756 0ZM7.875 1.69l-4.63 2.685L8 7.133l4.755-2.758-4.63-2.685a.248.248 0 0 0-.25 0ZM2.5 5.677v5.372c0 .09.047.171.125.216l4.625 2.683V8.432Zm6.25 8.271 4.625-2.683a.25.25 0 0 0 .125-.216V5.677L8.75 8.432Z"></path>
</svg>
</template>

<template id="credit-card-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-credit-card">
    <path d="M10.75 9a.75.75 0 0 0 0 1.5h1.5a.75.75 0 0 0 0-1.5h-1.5Z"></path><path d="M0 3.75C0 2.784.784 2 1.75 2h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14H1.75A1.75 1.75 0 0 1 0 12.25ZM14.5 6.5h-13v5.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Zm0-2.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25V5h13Z"></path>
</svg>
</template>

<template id="play-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
</template>

<template id="gift-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
</template>

<template id="code-square-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-square">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
</template>

<template id="device-desktop-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-device-desktop">
    <path d="M14.25 1c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 14.25 12h-3.727c.099 1.041.52 1.872 1.292 2.757A.752.752 0 0 1 11.25 16h-6.5a.75.75 0 0 1-.565-1.243c.772-.885 1.192-1.716 1.292-2.757H1.75A1.75 1.75 0 0 1 0 10.25v-7.5C0 1.784.784 1 1.75 1ZM1.75 2.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25ZM9.018 12H6.982a5.72 5.72 0 0 1-.765 2.5h3.566a5.72 5.72 0 0 1-.765-2.5Z"></path>
</svg>
</template>

        <div class="position-relative">
                        <ul
              role="listbox"
              class="ActionListWrap QueryBuilder-ListWrap"
              aria-label="Suggestions"
              data-action="
                combobox-commit:query-builder#comboboxCommit
                mousedown:query-builder#resultsMousedown
              "
              data-target="query-builder.resultsList"
              data-persist-list=false
              id="query-builder-test-results"
              tabindex="-1"
            ></ul>

        </div>
      <div class="FormControl-inlineValidation" id="validation-8e28b114-3b1e-404e-9f3c-ecd3dac31c04" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only"></div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted tmp-px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2 tmp-ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="code-search-feedback-form" data-turbo="false" action="/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="gn6c1EyCTRZ+ul5B5/FvnkP8l/WqyI9IvFaKscCMHDjazx8gvRfEqSkvFhbiOYZutjcSImckcCzWhTbD4iouCg==" />
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="custom-scopes-dialog-form" data-turbo="false" action="/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="wDbAJ8F5yf8B181sYgZX3Q80uJHgh1eq14+YCSgPy3TThbv4AP09zzBq5+VXq6yNRiN6lD/kRgaADwL3yf/r5Q==" />
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required>
              <input
                type="text"
                name="custom_scope_name"
                id="custom_scope_name"
                data-target="custom-scopes.customScopesNameField"
                class="form-control"
                autocomplete="off"
                placeholder="github-ruby"
                required
                maxlength="50">
              <input type="hidden" data-csrf="true" value="QBlsmL+ZP/sBJaJ2ELYjD7B8jxdaw1WVGKSEtNJt1hQ3v4/Jg4pPJlWBYS8e/IEc8eoVzHUvndCmwXLmmORQ5g==" />
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input
              type="text"
              name="custom_scope_query"
              id="custom_scope_query"
              data-target="custom-scopes.customScopesQueryField"
              class="form-control"
              autocomplete="off"
              placeholder="(repo:mona/a OR repo:mona/b) AND lang:python"
              required
              maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>


            <div class="position-relative HeaderMenu-link-wrap d-lg-inline-block">
              <a
                href="/login?return_to=https%3A%2F%2Fgithub.com%2Flucidrains%2FDALLE2-pytorch"
                class="HeaderMenu-link HeaderMenu-link--sign-in HeaderMenu-button flex-shrink-0 no-underline d-none d-lg-inline-flex border border-lg-0 rounded px-2 py-1"
                style="margin-left: 12px;"
                data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/lucidrains/DALLE2-pytorch&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="650aa3efe04f23a14f2dd95f8c13893e1b873f19a023cf4532ae67f980847a60"
                data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}"
              >
                Sign in
              </a>
            </div>

              <a href="/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&amp;source=header-repo&amp;source_repo=lucidrains%2FDALLE2-pytorch"
                class="HeaderMenu-link HeaderMenu-link--sign-up HeaderMenu-button flex-shrink-0 d-flex d-lg-inline-flex no-underline border color-border-default rounded px-2 py-1"
                data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/lucidrains/DALLE2-pytorch&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="650aa3efe04f23a14f2dd95f8c13893e1b873f19a023cf4532ae67f980847a60"
                data-analytics-event="{&quot;category&quot;:&quot;Sign up&quot;,&quot;action&quot;:&quot;click to sign up for account&quot;,&quot;label&quot;:&quot;ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;;ref_cta:Sign up;ref_loc:header logged out&quot;}"
              >
                Sign up
              </a>

                <div class="AppHeader-appearanceSettings">
    <react-partial-anchor>
      <button data-target="react-partial-anchor.anchor" id="icon-button-ca444e73-4fca-422a-be29-28f3859140f8" aria-labelledby="tooltip-512f8742-b319-44d9-ac06-8faf0aa512eb" type="button" disabled="disabled" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium AppHeader-button HeaderMenu-link border cursor-wait">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sliders Button-visual">
    <path d="M15 2.75a.75.75 0 0 1-.75.75h-4a.75.75 0 0 1 0-1.5h4a.75.75 0 0 1 .75.75Zm-8.5.75v1.25a.75.75 0 0 0 1.5 0v-4a.75.75 0 0 0-1.5 0V2H1.75a.75.75 0 0 0 0 1.5H6.5Zm1.25 5.25a.75.75 0 0 0 0-1.5h-6a.75.75 0 0 0 0 1.5h6ZM15 8a.75.75 0 0 1-.75.75H11.5V10a.75.75 0 1 1-1.5 0V6a.75.75 0 0 1 1.5 0v1.25h2.75A.75.75 0 0 1 15 8Zm-9 5.25v-2a.75.75 0 0 0-1.5 0v1.25H1.75a.75.75 0 0 0 0 1.5H4.5v1.25a.75.75 0 0 0 1.5 0v-2Zm9 0a.75.75 0 0 1-.75.75h-6a.75.75 0 0 1 0-1.5h6a.75.75 0 0 1 .75.75Z"></path>
</svg>
</button><tool-tip id="tooltip-512f8742-b319-44d9-ac06-8faf0aa512eb" for="icon-button-ca444e73-4fca-422a-be29-28f3859140f8" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Appearance settings</tool-tip>

      <template data-target="react-partial-anchor.template">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a2f41fc3ac05567f.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/appearance-settings.6f14ff9973550c9e.module.css" />

<react-partial
  partial-name="appearance-settings"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>


      </template>
    </react-partial-anchor>
  </div>

          <button type="button" class="sr-only js-header-menu-focus-trap d-block d-lg-none">Resetting focus</button>
        </div>
      </div>
    </div>
  </div>
</header>

      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden>You switched accounts on another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>

    <button id="icon-button-fa8f9321-ef72-4d00-8d7d-05729aa7d5f1" aria-labelledby="tooltip-938cd933-9f27-4224-8477-2c40093642fd" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-938cd933-9f27-4224-8477-2c40093642fd" for="icon-button-fa8f9321-ef72-4d00-8d7d-05729aa7d5f1" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Dismiss alert</tool-tip>


  
</div>
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace>




  <template class="js-flash-template">
    
<div class="flash flash-full   {{ className }}">
  <div >
    <button autofocus class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    <div aria-atomic="true" role="alert" class="js-flash-alert">
      
      <div>{{ message }}</div>

    </div>
  </div>
</div>
  </template>
</div>


    






  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
    data-project-hovercards-enabled
  >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" >
      
      






  

  <div id="repository-container-header"  class="tmp-pt-3 hide-full-screen" style="background-color: var(--page-header-bgColor, var(--color-page-header-bg));" data-turbo-replace>

      <div class="d-flex flex-nowrap flex-justify-end tmp-mb-3  tmp-px-3 tmp-px-lg-5" style="gap: 1rem;">

        <div class="flex-auto min-width-0 width-fit">
            
  <div class=" d-flex flex-wrap flex-items-center wb-break-word f3 text-normal">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo color-fg-muted mr-2 tmp-mr-2">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
    
    <span class="author flex-self-stretch" itemprop="author">
      <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/lucidrains/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/lucidrains">
        lucidrains
</a>    </span>
    <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
    <strong itemprop="name" class="mr-2 flex-self-stretch">
      <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/lucidrains/DALLE2-pytorch">DALLE2-pytorch</a>
    </strong>

    <span></span><span class="Label Label--secondary v-align-middle mr-1">Public</span>
  </div>


        </div>

        <div id="repository-details-container" class="flex-shrink-0" data-turbo-replace style="max-width: 70%;">
            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
    
        <li>
          <include-fragment src="/lucidrains/DALLE2-pytorch/sponsor_button" data-nonce="v2:2794b2bc-e069-7a37-3ae9-05ff3bb3b6f8" data-view-component="true">
  
  <div data-show-on-forbidden-error hidden>
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true" class="blankslate-description">        <p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="" aria-label="Please reload this page">Please reload this page</a>.</p>
</p>

</div>  </div>
</div>  </div>
</include-fragment>
        </li>

      

  <li>
            <a href="/login?return_to=%2Flucidrains%2FDALLE2-pytorch" rel="nofollow" id="repository-details-watch-button" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/lucidrains/DALLE2-pytorch&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="c7ec121dd12b2f2a4cc11737f34c39f191fcc7b794a5b8e9d2d7f7be918fa904" aria-label="You must be signed in to change notification settings" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2 tmp-mr-2">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>Notifications
</a>    <tool-tip id="tooltip-58b43ba2-4b43-4003-b47d-a14e5d651463" for="repository-details-watch-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">You must be signed in to change notification settings</tool-tip>

  </li>

  <li>
          <a icon="repo-forked" id="fork-button" href="/login?return_to=%2Flucidrains%2FDALLE2-pytorch" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:478823173,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/lucidrains/DALLE2-pytorch&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="a51c01ce07117492ce3ce28bd2e2612adaf2193df466e25e74446d10aeb58864" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2 tmp-mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>Fork
    <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="1,084" data-view-component="true" class="Counter">1.1k</span>
</a>
  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <a href="/login?return_to=%2Flucidrains%2FDALLE2-pytorch" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:478823173,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/lucidrains/DALLE2-pytorch&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="abd2ec4325048ce85a0f9d3a8bd22a734e59fcfcc8cd692009c23a8880f0729c" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-sw btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2 tmp-mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>          <span id="repo-stars-counter-star" aria-label="11324 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="11,324" data-view-component="true" class="Counter js-social-count">11.3k</span>
</a></div>
  </li>

</ul>

        </div>
      </div>

        <div id="responsive-meta-container" data-turbo-replace>
</div>


          <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 tmp-px-3 px-md-4 tmp-px-md-4 px-lg-5 tmp-px-lg-5">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="/lucidrains/DALLE2-pytorch" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /lucidrains/DALLE2-pytorch" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-command-id="repositories:go-to-code" data-react-nav="code-view" data-react-nav-anchor="code-view-repo-link" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" aria-current="page" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="/lucidrains/DALLE2-pytorch/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /lucidrains/DALLE2-pytorch/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-command-id="repositories:go-to-issues" data-react-nav="issues-react" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="68" data-view-component="true" class="Counter">68</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/lucidrains/DALLE2-pytorch/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /lucidrains/DALLE2-pytorch/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-command-id="repositories:go-to-pull-requests" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="5" data-view-component="true" class="Counter">5</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="discussions-tab" href="/lucidrains/DALLE2-pytorch/discussions" data-tab-item="i3discussions-tab" data-selected-links="repo_discussions /lucidrains/DALLE2-pytorch/discussions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g g" data-command-id="repositories:go-to-discussions" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Discussions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        <span data-content="Discussions">Discussions</span>
          <span id="discussions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/lucidrains/DALLE2-pytorch/actions" data-tab-item="i4actions-tab" data-selected-links="repo_actions /lucidrains/DALLE2-pytorch/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-command-id="repositories:go-to-actions" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="/lucidrains/DALLE2-pytorch/projects" data-tab-item="i5projects-tab" data-selected-links="repo_projects new_repo_project repo_project /lucidrains/DALLE2-pytorch/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-command-id="repositories:go-to-projects" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-and-quality-tab" href="/lucidrains/DALLE2-pytorch/security" data-tab-item="i6security-and-quality-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /lucidrains/DALLE2-pytorch/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-command-id="repositories:go-to-security" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security and quality&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security and quality">Security and quality</span>
          <span id="security-and-quality-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="/lucidrains/DALLE2-pytorch/pulse" data-tab-item="i7insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /lucidrains/DALLE2-pytorch/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-command-id="repositories:go-to-insights" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 tmp-pr-3 pr-md-4 tmp-pr-md-4 pr-lg-5 tmp-pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true">
  <focus-group direction="vertical" mnemonics retain>
    <button id="action-menu-21439364-5ac1-4b5a-8554-8a46410c3ae1-button" popovertarget="action-menu-21439364-5ac1-4b5a-8554-8a46410c3ae1-overlay" aria-controls="action-menu-21439364-5ac1-4b5a-8554-8a46410c3ae1-list" aria-haspopup="true" aria-labelledby="tooltip-50766d9a-f455-405a-9c92-6f623c2fa151" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-50766d9a-f455-405a-9c92-6f623c2fa151" for="action-menu-21439364-5ac1-4b5a-8554-8a46410c3ae1-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-21439364-5ac1-4b5a-8554-8a46410c3ae1-overlay" anchor="action-menu-21439364-5ac1-4b5a-8554-8a46410c3ae1-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list>
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-21439364-5ac1-4b5a-8554-8a46410c3ae1-button" id="action-menu-21439364-5ac1-4b5a-8554-8a46410c3ae1-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="hidden" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-6bf2d313-0018-4943-a063-d689924069a1" href="/lucidrains/DALLE2-pytorch" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-4a15c1f9-11ad-4636-8c65-064f34c1cf66" href="/lucidrains/DALLE2-pytorch/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-f5cc405b-539f-430c-b8cd-8f72b64fa404" href="/lucidrains/DALLE2-pytorch/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i3discussions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-b051f152-1b1a-415f-b2fb-651fe50aff42" href="/lucidrains/DALLE2-pytorch/discussions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i4actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-0bb101a7-8723-4fe5-b7fe-3154f0c96efa" href="/lucidrains/DALLE2-pytorch/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i5projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-d8a04c48-a47a-4868-8b9f-decd8b65c132" href="/lucidrains/DALLE2-pytorch/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i6security-and-quality-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-82632c6e-21cd-4863-a74d-ee708bcc0211" href="/lucidrains/DALLE2-pytorch/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security and quality
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i7insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-a25650f4-6547-44b3-a67d-72f8d6e7e2bd" href="/lucidrains/DALLE2-pytorch/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>

  </div>
  



<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content " >
    



    
      
    








<react-app
  app-name="code-view"
  initial-path="/lucidrains/DALLE2-pytorch"
  style="display: block; min-height: calc(100vh - 64px);"
  data-attempted-ssr="true"
  data-ssr="true"
  data-lazy="false"
  data-alternate="false"
  data-data-router-enabled="true"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"codeViewRepoRoute":{"path":"/","refInfo":{"name":"main","listCacheKey":"v0:1697688176.0","canEdit":false,"refType":"branch","currentOid":"680dfc4d93b70f9ab23c814a22ca18017a738ef6"},"tree":{"items":[{"name":".github","path":".github","contentType":"directory"},{"name":"configs","path":"configs","contentType":"directory"},{"name":"dalle2_pytorch","path":"dalle2_pytorch","contentType":"directory"},{"name":"samples","path":"samples","contentType":"directory"},{"name":"test_data","path":"test_data","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"LICENSE","path":"LICENSE","contentType":"file"},{"name":"MANIFEST.in","path":"MANIFEST.in","contentType":"file"},{"name":"Makefile","path":"Makefile","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"dalle2.png","path":"dalle2.png","contentType":"file"},{"name":"prior.md","path":"prior.md","contentType":"file"},{"name":"setup.py","path":"setup.py","contentType":"file"},{"name":"train_decoder.py","path":"train_decoder.py","contentType":"file"},{"name":"train_diffusion_prior.py","path":"train_diffusion_prior.py","contentType":"file"}],"totalCount":15,"templateDirectorySuggestionUrl":null,"readme":null,"showBranchInfobar":false},"userNameDisplayConfiguration":null,"treeExpanded":false,"symbolsExpanded":false,"copilotSWEAgentEnabled":false,"isOverview":true,"overview":{"banners":{"shouldRecommendReadme":false,"isPersonalRepo":false,"showUseActionBanner":false,"actionSlug":null,"actionId":null,"showProtectBranchBanner":false,"transactionalMessageBanner":null,"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_repo","releasePath":"/lucidrains/DALLE2-pytorch/releases/new?marketplace=true","showPublishActionBanner":false},"interactionLimitBanner":null,"showInvitationBanner":false,"inviterName":null,"actionsMigrationBannerInfo":{"releaseTags":[],"showImmutableActionsMigrationBanner":false,"initialMigrationStatus":null}},"codeButton":{"contactPath":"/contact","isEnterprise":false,"local":{"protocolInfo":{"httpAvailable":true,"sshAvailable":null,"httpUrl":"https://github.com/lucidrains/DALLE2-pytorch.git","showCloneWarning":null,"sshUrl":null,"sshCertificatesRequired":null,"sshCertificatesAvailable":null,"ghCliUrl":"gh repo clone lucidrains/DALLE2-pytorch","defaultProtocol":"http","newSshKeyUrl":"/settings/ssh/new","setProtocolPath":"/users/set_protocol"},"platformInfo":{"cloneUrl":"https://desktop.github.com","showVisualStudioCloneButton":false,"visualStudioCloneUrl":"https://windows.github.com","showXcodeCloneButton":false,"xcodeCloneUrl":"xcode://clone?repo=https%3A%2F%2Fgithub.com%2Flucidrains%2FDALLE2-pytorch","zipballUrl":"/lucidrains/DALLE2-pytorch/archive/refs/heads/main.zip"}},"newCodespacePath":"/codespaces/new?hide_repo_select=true\u0026repo=478823173"},"popovers":{"rename":null,"renamedParentRepo":null},"commitCount":"602","overviewFiles":[{"displayName":"README.md","repoName":"DALLE2-pytorch","refName":"main","path":"README.md","preferredFileType":"readme","tabName":"README","richText":"\u003carticle class=\"markdown-body entry-content container-lg\" itemprop=\"text\"\u003e\u003cp dir=\"auto\"\u003e\u003ca target=\"_blank\" rel=\"noopener noreferrer\" href=\"/lucidrains/DALLE2-pytorch/blob/main/dalle2.png\"\u003e\u003cimg src=\"/lucidrains/DALLE2-pytorch/raw/main/dalle2.png\" width=\"450px\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDALL-E 2 - Pytorch\u003c/h2\u003e\u003ca id=\"user-content-dall-e-2---pytorch\" class=\"anchor\" aria-label=\"Permalink: DALL-E 2 - Pytorch\" href=\"#dall-e-2---pytorch\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eImplementation of \u003ca href=\"https://openai.com/dall-e-2/\" rel=\"nofollow\"\u003eDALL-E 2\u003c/a\u003e, OpenAI's updated text-to-image synthesis neural network, in Pytorch.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca href=\"https://youtu.be/RJwPN4qNi_Y?t=555\" rel=\"nofollow\"\u003eYannic Kilcher summary\u003c/a\u003e | \u003ca href=\"https://www.youtube.com/watch?v=F1X4fHzF4mQ\" rel=\"nofollow\"\u003eAssemblyAI explainer\u003c/a\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThe main novelty seems to be an extra layer of indirection with the prior network (whether it is an autoregressive transformer or a diffusion network), which predicts an image embedding based on the text embedding from CLIP. Specifically, this repository will only build out the diffusion prior network, as it is the best performing variant (but which incidentally involves a causal transformer as the denoising network 😂)\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThis model is SOTA for text-to-image for now.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003ePlease join \u003ca href=\"https://discord.gg/xBPBXfcFHd\" rel=\"nofollow\"\u003e\u003cimg alt=\"Join us on Discord\" src=\"https://camo.githubusercontent.com/6df2255d075e0356a86a3db06dda295fda5ee305948a6eb9f76786703c110b1e/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3832333831333135393539323030313533373f636f6c6f723d353836354632266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465\" data-canonical-src=\"https://img.shields.io/discord/823813159592001537?color=5865F2\u0026amp;logo=discord\u0026amp;logoColor=white\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e if you are interested in helping out with the replication with the \u003ca href=\"https://laion.ai/\" rel=\"nofollow\"\u003eLAION\u003c/a\u003e community | \u003ca href=\"https://www.youtube.com/watch?v=AIOE1l1W0Tw\" rel=\"nofollow\"\u003eYannic Interview\u003c/a\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eAs of 5/23/22, it is no longer SOTA. SOTA will be \u003ca href=\"https://github.com/lucidrains/imagen-pytorch\"\u003ehere\u003c/a\u003e. Jax versions as well as text-to-video project will be shifted towards the Imagen architecture, as it is way simpler.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eStatus\u003c/h2\u003e\u003ca id=\"user-content-status\" class=\"anchor\" aria-label=\"Permalink: Status\" href=\"#status\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eA research group has used the code in this repository to train a functional diffusion prior for their CLIP generations. Will share their work once they release their preprint. This, and \u003ca href=\"https://github.com/crowsonkb\"\u003eKatherine's\u003c/a\u003e own experiments, validate OpenAI's finding that the extra prior increases variety of generations.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eDecoder is now verified working for unconditional generation on my experimental setup for Oxford flowers. 2 researchers have also confirmed Decoder is working for them.\u003c/p\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp dir=\"auto\"\u003e\u003ca target=\"_blank\" rel=\"noopener noreferrer\" href=\"/lucidrains/DALLE2-pytorch/blob/main/samples/oxford.png\"\u003e\u003cimg src=\"/lucidrains/DALLE2-pytorch/raw/main/samples/oxford.png\" width=\"450px\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eongoing at 21k steps\u003c/em\u003e\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003e\u003ca href=\"https://twitter.com/Buntworthy/status/1529475416775434240?t=0GEge3Kr9I36cjcUVCQUTg\" rel=\"nofollow\"\u003eJustin Pinkney\u003c/a\u003e successfully trained the diffusion prior in the repository for his CLIP to Stylegan2 text-to-image application\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003e\u003ca href=\"https://github.com/rom1504\"\u003eRomain\u003c/a\u003e has scaled up training to 800 GPUs with the available scripts without any issues\u003c/p\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003ePre-Trained Models\u003c/h2\u003e\u003ca id=\"user-content-pre-trained-models\" class=\"anchor\" aria-label=\"Permalink: Pre-Trained Models\" href=\"#pre-trained-models\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eLAION is training prior models. Checkpoints are available on \u003ca href=\"https://huggingface.co/zenglishuci/conditioned-prior\" rel=\"nofollow\"\u003e🤗huggingface\u003c/a\u003e and the training statistics are available on \u003ca href=\"https://wandb.ai/nousr_laion/conditioned-prior/reports/LAION-DALLE2-PyTorch-Prior--VmlldzoyMDI2OTIx\" rel=\"nofollow\"\u003e🐝WANDB\u003c/a\u003e.\u003c/li\u003e\n\u003cli\u003eDecoder - \u003ca href=\"https://wandb.ai/veldrovive/dalle2_train_decoder/runs/jkrtg0so?workspace=user-veldrovive\" rel=\"nofollow\"\u003eIn-progress test run\u003c/a\u003e 🚧\u003c/li\u003e\n\u003cli\u003eDecoder - \u003ca href=\"https://wandb.ai/veldrovive/dalle2_train_decoder/runs/3d5rytsa?workspace=\" rel=\"nofollow\"\u003eAnother test run with sparse attention\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003eDALL-E 2 🚧 - \u003ca href=\"https://github.com/LAION-AI/dalle2-laion\"\u003eDALL-E 2 Laion repository\u003c/a\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eAppreciation\u003c/h2\u003e\u003ca id=\"user-content-appreciation\" class=\"anchor\" aria-label=\"Permalink: Appreciation\" href=\"#appreciation\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThis library would not have gotten to this working state without the help of\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/nousr\"\u003eZion\u003c/a\u003e for the distributed training code for the diffusion prior\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/Veldrovive\"\u003eAidan\u003c/a\u003e for the distributed training code for the decoder as well as the dataloaders\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/krish240574\"\u003eKumar\u003c/a\u003e for working on the initial diffusion training script\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/rom1504\"\u003eRomain\u003c/a\u003e for the pull request reviews and project management\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/Ciaohe\"\u003eHe Cao\u003c/a\u003e and \u003ca href=\"https://github.com/xiankgx\"\u003exiankgx\u003c/a\u003e for the Q\u0026amp;A and for identifying of critical bugs\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/marunine\"\u003eMarunine\u003c/a\u003e for identifying issues with resizing of the low resolution conditioner, when training the upsampler, in addition to various other bug fixes\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/malumadev\"\u003eMalumaDev\u003c/a\u003e for proposing the use of pixel shuffle upsampler for fixing checkboard artifacts\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/crowsonkb\"\u003eKatherine\u003c/a\u003e for her advice\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://stability.ai/\" rel=\"nofollow\"\u003eStability AI\u003c/a\u003e for the generous sponsorship\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://huggingface.co\" rel=\"nofollow\"\u003e🤗 Huggingface\u003c/a\u003e and in particular \u003ca href=\"https://github.com/sgugger\"\u003eSylvain\u003c/a\u003e for the \u003ca href=\"https://github.com/huggingface/accelerate\"\u003eAccelerate\u003c/a\u003e library\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/arogozhnikov\"\u003eAlex\u003c/a\u003e for \u003ca href=\"https://github.com/arogozhnikov/einops\"\u003eeinops\u003c/a\u003e, indispensable tool for tensor manipulation\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp dir=\"auto\"\u003e... and many others. Thank you! 🙏\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eInstall\u003c/h2\u003e\u003ca id=\"user-content-install\" class=\"anchor\" aria-label=\"Permalink: Install\" href=\"#install\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"$ pip install dalle2-pytorch\"\u003e\u003cpre\u003e$ pip install dalle2-pytorch\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eUsage\u003c/h2\u003e\u003ca id=\"user-content-usage\" class=\"anchor\" aria-label=\"Permalink: Usage\" href=\"#usage\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eTo train DALLE-2 is a 3 step process, with the training of CLIP being the most important\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eTo train CLIP, you can either use \u003ca href=\"https://github.com/lucidrains/x-clip\"\u003ex-clip\u003c/a\u003e package, or join the LAION discord, where a lot of replication efforts are already \u003ca href=\"https://github.com/mlfoundations/open_clip\"\u003eunderway\u003c/a\u003e.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThis repository will demonstrate integration with \u003ccode\u003ex-clip\u003c/code\u003e for starters\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import CLIP\n\nclip = CLIP(\n    dim_text = 512,\n    dim_image = 512,\n    dim_latent = 512,\n    num_text_tokens = 49408,\n    text_enc_depth = 1,\n    text_seq_len = 256,\n    text_heads = 8,\n    visual_enc_depth = 1,\n    visual_image_size = 256,\n    visual_patch_size = 32,\n    visual_heads = 8,\n    use_all_token_embeds = True,            # whether to use fine-grained contrastive learning (FILIP)\n    decoupled_contrastive_learning = True,  # use decoupled contrastive learning (DCL) objective function, removing positive pairs from the denominator of the InfoNCE loss (CLOOB + DCL)\n    extra_latent_projection = True,         # whether to use separate projections for text-to-image vs image-to-text comparisons (CLOOB)\n    use_visual_ssl = True,                  # whether to do self supervised learning on images\n    visual_ssl_type = 'simclr',             # can be either 'simclr' or 'simsiam', depending on using DeCLIP or SLIP\n    use_mlm = False,                        # use masked language learning (MLM) on text (DeCLIP)\n    text_ssl_loss_weight = 0.05,            # weight for text MLM loss\n    image_ssl_loss_weight = 0.05            # weight for image self-supervised learning loss\n).cuda()\n\n# mock data\n\ntext = torch.randint(0, 49408, (4, 256)).cuda()\nimages = torch.randn(4, 3, 256, 256).cuda()\n\n# train\n\nloss = clip(\n    text,\n    images,\n    return_loss = True              # needs to be set to True to return contrastive loss\n)\n\nloss.backward()\n\n# do the above with as many texts and images as possible in a loop\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eCLIP\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eCLIP\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim_text\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_latent\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003enum_text_tokens\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_seq_len\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_image_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_patch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003euse_all_token_embeds\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,            \u003cspan class=\"pl-c\"\u003e# whether to use fine-grained contrastive learning (FILIP)\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003edecoupled_contrastive_learning\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,  \u003cspan class=\"pl-c\"\u003e# use decoupled contrastive learning (DCL) objective function, removing positive pairs from the denominator of the InfoNCE loss (CLOOB + DCL)\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eextra_latent_projection\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,         \u003cspan class=\"pl-c\"\u003e# whether to use separate projections for text-to-image vs image-to-text comparisons (CLOOB)\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003euse_visual_ssl\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,                  \u003cspan class=\"pl-c\"\u003e# whether to do self supervised learning on images\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003evisual_ssl_type\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'simclr'\u003c/span\u003e,             \u003cspan class=\"pl-c\"\u003e# can be either 'simclr' or 'simsiam', depending on using DeCLIP or SLIP\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003euse_mlm\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e,                        \u003cspan class=\"pl-c\"\u003e# use masked language learning (MLM) on text (DeCLIP)\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003etext_ssl_loss_weight\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.05\u003c/span\u003e,            \u003cspan class=\"pl-c\"\u003e# weight for text MLM loss\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eimage_ssl_loss_weight\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.05\u003c/span\u003e            \u003cspan class=\"pl-c\"\u003e# weight for image self-supervised learning loss\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock data\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandint\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e, (\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e)).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# train\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eclip\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003ereturn_loss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e              \u003cspan class=\"pl-c\"\u003e# needs to be set to True to return contrastive loss\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do the above with as many texts and images as possible in a loop\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThen, you will need to train the decoder, which learns to generate images based on the image embedding coming from the trained CLIP above\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import Unet, Decoder, CLIP\n\n# trained clip from step 1\n\nclip = CLIP(\n    dim_text = 512,\n    dim_image = 512,\n    dim_latent = 512,\n    num_text_tokens = 49408,\n    text_enc_depth = 1,\n    text_seq_len = 256,\n    text_heads = 8,\n    visual_enc_depth = 1,\n    visual_image_size = 256,\n    visual_patch_size = 32,\n    visual_heads = 8\n).cuda()\n\n# unet for the decoder\n\nunet = Unet(\n    dim = 128,\n    image_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    dim_mults=(1, 2, 4, 8)\n).cuda()\n\n# decoder, which contains the unet and clip\n\ndecoder = Decoder(\n    unet = unet,\n    clip = clip,\n    timesteps = 100,\n    image_cond_drop_prob = 0.1,\n    text_cond_drop_prob = 0.5\n).cuda()\n\n# mock images (get a lot of this)\n\nimages = torch.randn(4, 3, 256, 256).cuda()\n\n# feed images into decoder\n\nloss = decoder(images)\nloss.backward()\n\n# do the above for many many many many steps\n# then it will learn to generate images based on the CLIP image embeddings\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eUnet\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoder\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eCLIP\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# trained clip from step 1\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eCLIP\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim_text\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_latent\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003enum_text_tokens\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_seq_len\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_image_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_patch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# unet for the decoder\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e)\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# decoder, which contains the unet and clip\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDecoder\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e100\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock images (get a lot of this)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# feed images into decoder\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e)\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do the above for many many many many steps\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# then it will learn to generate images based on the CLIP image embeddings\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eFinally, the main contribution of the paper. The repository offers the diffusion prior network. It takes the CLIP text embeddings and tries to generate the CLIP image embeddings. Again, you will need the trained CLIP from the first step\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import DiffusionPriorNetwork, DiffusionPrior, CLIP\n\n# get trained CLIP from step one\n\nclip = CLIP(\n    dim_text = 512,\n    dim_image = 512,\n    dim_latent = 512,\n    num_text_tokens = 49408,\n    text_enc_depth = 6,\n    text_seq_len = 256,\n    text_heads = 8,\n    visual_enc_depth = 6,\n    visual_image_size = 256,\n    visual_patch_size = 32,\n    visual_heads = 8,\n).cuda()\n\n# setup prior network, which contains an autoregressive transformer\n\nprior_network = DiffusionPriorNetwork(\n    dim = 512,\n    depth = 6,\n    dim_head = 64,\n    heads = 8\n).cuda()\n\n# diffusion prior network, which contains the CLIP and network (with transformer) above\n\ndiffusion_prior = DiffusionPrior(\n    net = prior_network,\n    clip = clip,\n    timesteps = 100,\n    cond_drop_prob = 0.2\n).cuda()\n\n# mock data\n\ntext = torch.randint(0, 49408, (4, 256)).cuda()\nimages = torch.randn(4, 3, 256, 256).cuda()\n\n# feed text and images into diffusion prior network\n\nloss = diffusion_prior(text, images)\nloss.backward()\n\n# do the above for many many many steps\n# now the diffusion prior can generate image embeddings from the text embeddings\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDiffusionPriorNetwork\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDiffusionPrior\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eCLIP\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# get trained CLIP from step one\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eCLIP\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim_text\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_latent\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003enum_text_tokens\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_seq_len\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_image_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_patch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# setup prior network, which contains an autoregressive transformer\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPriorNetwork\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edepth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_head\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e64\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eheads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# diffusion prior network, which contains the CLIP and network (with transformer) above\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPrior\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003enet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e100\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.2\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock data\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandint\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e, (\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e)).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# feed text and images into diffusion prior network\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ediffusion_prior\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e)\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do the above for many many many steps\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# now the diffusion prior can generate image embeddings from the text embeddings\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eIn the paper, they actually used a \u003ca href=\"https://cascaded-diffusion.github.io/\" rel=\"nofollow\"\u003erecently discovered technique\u003c/a\u003e, from \u003ca href=\"http://www.jonathanho.me/\" rel=\"nofollow\"\u003eJonathan Ho\u003c/a\u003e himself (original author of DDPMs, the core technique used in DALL-E v2) for high resolution image synthesis.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThis can easily be used within this framework as so\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import Unet, Decoder, CLIP\n\n# trained clip from step 1\n\nclip = CLIP(\n    dim_text = 512,\n    dim_image = 512,\n    dim_latent = 512,\n    num_text_tokens = 49408,\n    text_enc_depth = 6,\n    text_seq_len = 256,\n    text_heads = 8,\n    visual_enc_depth = 6,\n    visual_image_size = 256,\n    visual_patch_size = 32,\n    visual_heads = 8\n).cuda()\n\n# 2 unets for the decoder (a la cascading DDPM)\n\nunet1 = Unet(\n    dim = 32,\n    image_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    dim_mults = (1, 2, 4, 8)\n).cuda()\n\nunet2 = Unet(\n    dim = 32,\n    image_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    dim_mults = (1, 2, 4, 8, 16)\n).cuda()\n\n# decoder, which contains the unet(s) and clip\n\ndecoder = Decoder(\n    clip = clip,\n    unet = (unet1, unet2),            # insert both unets in order of low resolution to highest resolution (you can have as many stages as you want here)\n    image_sizes = (256, 512),         # resolutions, 256 for first unet, 512 for second. these must be unique and in ascending order (matches with the unets passed in)\n    timesteps = 1000,\n    image_cond_drop_prob = 0.1,\n    text_cond_drop_prob = 0.5\n).cuda()\n\n# mock images (get a lot of this)\n\nimages = torch.randn(4, 3, 512, 512).cuda()\n\n# feed images into decoder, specifying which unet you want to train\n# each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme\n\nloss = decoder(images, unet_number = 1)\nloss.backward()\n\nloss = decoder(images, unet_number = 2)\nloss.backward()\n\n# do the above for many steps for both unets\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eUnet\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoder\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eCLIP\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# trained clip from step 1\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eCLIP\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim_text\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_latent\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003enum_text_tokens\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_seq_len\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_image_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_patch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# 2 unets for the decoder (a la cascading DDPM)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e)\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e)\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# decoder, which contains the unet(s) and clip\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDecoder\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e),            \u003cspan class=\"pl-c\"\u003e# insert both unets in order of low resolution to highest resolution (you can have as many stages as you want here)\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eimage_sizes\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e),         \u003cspan class=\"pl-c\"\u003e# resolutions, 256 for first unet, 512 for second. these must be unique and in ascending order (matches with the unets passed in)\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1000\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock images (get a lot of this)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# feed images into decoder, specifying which unet you want to train\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e)\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e)\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do the above for many steps for both unets\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eFinally, to generate the DALL-E2 images from text. Insert the trained \u003ccode\u003eDiffusionPrior\u003c/code\u003e as well as the \u003ccode\u003eDecoder\u003c/code\u003e (which wraps \u003ccode\u003eCLIP\u003c/code\u003e, the causal transformer, and unet(s))\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"from dalle2_pytorch import DALLE2\n\ndalle2 = DALLE2(\n    prior = diffusion_prior,\n    decoder = decoder\n)\n\n# send the text as a string if you want to use the simple tokenizer from DALLE v1\n# or you can do it as token ids, if you have your own tokenizer\n\ntexts = ['glistening morning dew on a flower petal']\nimages = dalle2(texts) # (1, 3, 256, 256)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDALLE2\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003edalle2\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDALLE2\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eprior\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-c\"\u003e# send the text as a string if you want to use the simple tokenizer from DALLE v1\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# or you can do it as token ids, if you have your own tokenizer\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003etexts\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e [\u003cspan class=\"pl-s\"\u003e'glistening morning dew on a flower petal'\u003c/span\u003e]\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edalle2\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003etexts\u003c/span\u003e) \u003cspan class=\"pl-c\"\u003e# (1, 3, 256, 256)\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThat's it!\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eLet's see the whole script below\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import DALLE2, DiffusionPriorNetwork, DiffusionPrior, Unet, Decoder, CLIP\n\nclip = CLIP(\n    dim_text = 512,\n    dim_image = 512,\n    dim_latent = 512,\n    num_text_tokens = 49408,\n    text_enc_depth = 6,\n    text_seq_len = 256,\n    text_heads = 8,\n    visual_enc_depth = 6,\n    visual_image_size = 256,\n    visual_patch_size = 32,\n    visual_heads = 8\n).cuda()\n\n# mock data\n\ntext = torch.randint(0, 49408, (4, 256)).cuda()\nimages = torch.randn(4, 3, 256, 256).cuda()\n\n# train\n\nloss = clip(\n    text,\n    images,\n    return_loss = True\n)\n\nloss.backward()\n\n# do above for many steps ...\n\n# prior networks (with transformer)\n\nprior_network = DiffusionPriorNetwork(\n    dim = 512,\n    depth = 6,\n    dim_head = 64,\n    heads = 8\n).cuda()\n\ndiffusion_prior = DiffusionPrior(\n    net = prior_network,\n    clip = clip,\n    timesteps = 1000,\n    sample_timesteps = 64,\n    cond_drop_prob = 0.2\n).cuda()\n\nloss = diffusion_prior(text, images)\nloss.backward()\n\n# do above for many steps ...\n\n# decoder (with unet)\n\nunet1 = Unet(\n    dim = 128,\n    image_embed_dim = 512,\n    text_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    dim_mults=(1, 2, 4, 8),\n    cond_on_text_encodings = True    # set to True for any unets that need to be conditioned on text encodings\n).cuda()\n\nunet2 = Unet(\n    dim = 16,\n    image_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    dim_mults = (1, 2, 4, 8, 16)\n).cuda()\n\ndecoder = Decoder(\n    unet = (unet1, unet2),\n    image_sizes = (128, 256),\n    clip = clip,\n    timesteps = 100,\n    image_cond_drop_prob = 0.1,\n    text_cond_drop_prob = 0.5\n).cuda()\n\nfor unet_number in (1, 2):\n    loss = decoder(images, text = text, unet_number = unet_number) # this can optionally be decoder(images, text) if you wish to condition on the text encodings as well, though it was hinted in the paper it didn't do much\n    loss.backward()\n\n# do above for many steps\n\ndalle2 = DALLE2(\n    prior = diffusion_prior,\n    decoder = decoder\n)\n\nimages = dalle2(\n    ['cute puppy chasing after a squirrel'],\n    cond_scale = 2. # classifier free guidance strength (\u0026gt; 1 would strengthen the condition)\n)\n\n# save your image (in this example, of size 256x256)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDALLE2\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDiffusionPriorNetwork\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDiffusionPrior\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eUnet\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoder\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eCLIP\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eCLIP\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim_text\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_latent\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003enum_text_tokens\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_seq_len\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_image_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_patch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock data\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandint\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e, (\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e)).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# train\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eclip\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003ereturn_loss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do above for many steps ...\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# prior networks (with transformer)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPriorNetwork\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edepth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_head\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e64\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eheads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPrior\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003enet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1000\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003esample_timesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e64\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.2\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ediffusion_prior\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e)\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do above for many steps ...\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# decoder (with unet)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003econd_on_text_encodings\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e    \u003cspan class=\"pl-c\"\u003e# set to True for any unets that need to be conditioned on text encodings\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e)\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDecoder\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003eimage_sizes\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e100\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ein\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e):\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e) \u003cspan class=\"pl-c\"\u003e# this can optionally be decoder(images, text) if you wish to condition on the text encodings as well, though it was hinted in the paper it didn't do much\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do above for many steps\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003edalle2\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDALLE2\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eprior\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edalle2\u003c/span\u003e(\n    [\u003cspan class=\"pl-s\"\u003e'cute puppy chasing after a squirrel'\u003c/span\u003e],\n    \u003cspan class=\"pl-s1\"\u003econd_scale\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e2.\u003c/span\u003e \u003cspan class=\"pl-c\"\u003e# classifier free guidance strength (\u0026gt; 1 would strengthen the condition)\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-c\"\u003e# save your image (in this example, of size 256x256)\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eEverything in this readme should run without error\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eYou can also train the decoder on images of greater than the size (say 512x512) at which CLIP was trained (256x256). The images will be resized to CLIP image resolution for the image embeddings\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eFor the layperson, no worries, training will all be automated into a CLI tool, at least for small scale training.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eTraining on Preprocessed CLIP Embeddings\u003c/h2\u003e\u003ca id=\"user-content-training-on-preprocessed-clip-embeddings\" class=\"anchor\" aria-label=\"Permalink: Training on Preprocessed CLIP Embeddings\" href=\"#training-on-preprocessed-clip-embeddings\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eIt is likely, when scaling up, that you would first preprocess your images and text into corresponding embeddings before training the prior network. You can do so easily by simply passing in \u003ccode\u003eimage_embed\u003c/code\u003e, \u003ccode\u003etext_embed\u003c/code\u003e, and optionally \u003ccode\u003etext_encodings\u003c/code\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eWorking example below\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import DiffusionPriorNetwork, DiffusionPrior, CLIP\n\n# get trained CLIP from step one\n\nclip = CLIP(\n    dim_text = 512,\n    dim_image = 512,\n    dim_latent = 512,\n    num_text_tokens = 49408,\n    text_enc_depth = 6,\n    text_seq_len = 256,\n    text_heads = 8,\n    visual_enc_depth = 6,\n    visual_image_size = 256,\n    visual_patch_size = 32,\n    visual_heads = 8,\n).cuda()\n\n# setup prior network, which contains an autoregressive transformer\n\nprior_network = DiffusionPriorNetwork(\n    dim = 512,\n    depth = 6,\n    dim_head = 64,\n    heads = 8\n).cuda()\n\n# diffusion prior network, which contains the CLIP and network (with transformer) above\n\ndiffusion_prior = DiffusionPrior(\n    net = prior_network,\n    clip = clip,\n    timesteps = 100,\n    cond_drop_prob = 0.2,\n    condition_on_text_encodings = False  # this probably should be true, but just to get Laion started\n).cuda()\n\n# mock data\n\ntext = torch.randint(0, 49408, (4, 256)).cuda()\nimages = torch.randn(4, 3, 256, 256).cuda()\n\n# precompute the text and image embeddings\n# here using the diffusion prior class, but could be done with CLIP alone\n\nclip_image_embeds = diffusion_prior.clip.embed_image(images).image_embed\nclip_text_embeds = diffusion_prior.clip.embed_text(text).text_embed\n\n# feed text and images into diffusion prior network\n\nloss = diffusion_prior(\n    text_embed = clip_text_embeds,\n    image_embed = clip_image_embeds\n)\n\nloss.backward()\n\n# do the above for many many many steps\n# now the diffusion prior can generate image embeddings from the text embeddings\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDiffusionPriorNetwork\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDiffusionPrior\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eCLIP\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# get trained CLIP from step one\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eCLIP\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim_text\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_latent\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003enum_text_tokens\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_seq_len\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_image_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_patch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# setup prior network, which contains an autoregressive transformer\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPriorNetwork\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edepth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_head\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e64\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eheads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# diffusion prior network, which contains the CLIP and network (with transformer) above\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPrior\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003enet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e100\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.2\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econdition_on_text_encodings\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e  \u003cspan class=\"pl-c\"\u003e# this probably should be true, but just to get Laion started\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock data\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandint\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e, (\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e)).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# precompute the text and image embeddings\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# here using the diffusion prior class, but could be done with CLIP alone\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip_image_embeds\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eclip\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eembed_image\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003eimage_embed\u003c/span\u003e\n\u003cspan class=\"pl-s1\"\u003eclip_text_embeds\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eclip\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eembed_text\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003etext_embed\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# feed text and images into diffusion prior network\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ediffusion_prior\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003etext_embed\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip_text_embeds\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip_image_embeds\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do the above for many many many steps\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# now the diffusion prior can generate image embeddings from the text embeddings\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eYou can also completely go \u003ccode\u003eCLIP\u003c/code\u003e-less, in which case you will need to pass in the \u003ccode\u003eimage_embed_dim\u003c/code\u003e into the \u003ccode\u003eDiffusionPrior\u003c/code\u003e on initialization\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import DiffusionPriorNetwork, DiffusionPrior\n\n# setup prior network, which contains an autoregressive transformer\n\nprior_network = DiffusionPriorNetwork(\n    dim = 512,\n    depth = 6,\n    dim_head = 64,\n    heads = 8\n).cuda()\n\n# diffusion prior network, which contains the CLIP and network (with transformer) above\n\ndiffusion_prior = DiffusionPrior(\n    net = prior_network,\n    image_embed_dim = 512,               # this needs to be set\n    timesteps = 100,\n    cond_drop_prob = 0.2,\n    condition_on_text_encodings = False  # this probably should be true, but just to get Laion started\n).cuda()\n\n# mock data\n\ntext = torch.randint(0, 49408, (4, 256)).cuda()\nimages = torch.randn(4, 3, 256, 256).cuda()\n\n# precompute the text and image embeddings\n# here using the diffusion prior class, but could be done with CLIP alone\n\nclip_image_embeds = torch.randn(4, 512).cuda()\nclip_text_embeds = torch.randn(4, 512).cuda()\n\n# feed text and images into diffusion prior network\n\nloss = diffusion_prior(\n    text_embed = clip_text_embeds,\n    image_embed = clip_image_embeds\n)\n\nloss.backward()\n\n# do the above for many many many steps\n# now the diffusion prior can generate image embeddings from the text embeddings\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDiffusionPriorNetwork\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDiffusionPrior\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# setup prior network, which contains an autoregressive transformer\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPriorNetwork\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edepth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_head\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e64\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eheads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# diffusion prior network, which contains the CLIP and network (with transformer) above\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPrior\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003enet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,               \u003cspan class=\"pl-c\"\u003e# this needs to be set\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e100\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.2\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econdition_on_text_encodings\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e  \u003cspan class=\"pl-c\"\u003e# this probably should be true, but just to get Laion started\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock data\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandint\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e, (\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e)).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# precompute the text and image embeddings\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# here using the diffusion prior class, but could be done with CLIP alone\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip_image_embeds\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eclip_text_embeds\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# feed text and images into diffusion prior network\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ediffusion_prior\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003etext_embed\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip_text_embeds\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip_image_embeds\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do the above for many many many steps\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# now the diffusion prior can generate image embeddings from the text embeddings\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eOpenAI CLIP\u003c/h2\u003e\u003ca id=\"user-content-openai-clip\" class=\"anchor\" aria-label=\"Permalink: OpenAI CLIP\" href=\"#openai-clip\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eAlthough there is the possibility they are using an unreleased, more powerful CLIP, you can use one of the released ones, if you do not wish to train your own CLIP from scratch. This will also allow the community to more quickly validate the conclusions of the paper.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eTo use a pretrained OpenAI CLIP, simply import \u003ccode\u003eOpenAIClipAdapter\u003c/code\u003e and pass it into the \u003ccode\u003eDiffusionPrior\u003c/code\u003e or \u003ccode\u003eDecoder\u003c/code\u003e like so\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import DALLE2, DiffusionPriorNetwork, DiffusionPrior, Unet, Decoder, OpenAIClipAdapter\n\n# openai pretrained clip - defaults to ViT-B/32\n\nclip = OpenAIClipAdapter()\n\n# mock data\n\ntext = torch.randint(0, 49408, (4, 256)).cuda()\nimages = torch.randn(4, 3, 256, 256).cuda()\n\n# prior networks (with transformer)\n\nprior_network = DiffusionPriorNetwork(\n    dim = 512,\n    depth = 6,\n    dim_head = 64,\n    heads = 8\n).cuda()\n\ndiffusion_prior = DiffusionPrior(\n    net = prior_network,\n    clip = clip,\n    timesteps = 100,\n    cond_drop_prob = 0.2\n).cuda()\n\nloss = diffusion_prior(text, images)\nloss.backward()\n\n# do above for many steps ...\n\n# decoder (with unet)\n\nunet1 = Unet(\n    dim = 128,\n    image_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    dim_mults=(1, 2, 4, 8),\n    text_embed_dim = 512,\n    cond_on_text_encodings = True  # set to True for any unets that need to be conditioned on text encodings (ex. first unet in cascade)\n).cuda()\n\nunet2 = Unet(\n    dim = 16,\n    image_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    dim_mults = (1, 2, 4, 8, 16)\n).cuda()\n\ndecoder = Decoder(\n    unet = (unet1, unet2),\n    image_sizes = (128, 256),\n    clip = clip,\n    timesteps = 1000,\n    sample_timesteps = (250, 27),\n    image_cond_drop_prob = 0.1,\n    text_cond_drop_prob = 0.5\n).cuda()\n\nfor unet_number in (1, 2):\n    loss = decoder(images, text = text, unet_number = unet_number) # this can optionally be decoder(images, text) if you wish to condition on the text encodings as well, though it was hinted in the paper it didn't do much\n    loss.backward()\n\n# do above for many steps\n\ndalle2 = DALLE2(\n    prior = diffusion_prior,\n    decoder = decoder\n)\n\nimages = dalle2(\n    ['a butterfly trying to escape a tornado'],\n    cond_scale = 2. # classifier free guidance strength (\u0026gt; 1 would strengthen the condition)\n)\n\n# save your image (in this example, of size 256x256)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDALLE2\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDiffusionPriorNetwork\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDiffusionPrior\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eUnet\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoder\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eOpenAIClipAdapter\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# openai pretrained clip - defaults to ViT-B/32\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eOpenAIClipAdapter\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock data\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandint\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e, (\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e)).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# prior networks (with transformer)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPriorNetwork\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edepth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_head\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e64\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eheads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPrior\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003enet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e100\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.2\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ediffusion_prior\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e)\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do above for many steps ...\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# decoder (with unet)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003etext_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_on_text_encodings\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e  \u003cspan class=\"pl-c\"\u003e# set to True for any unets that need to be conditioned on text encodings (ex. first unet in cascade)\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e)\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDecoder\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003eimage_sizes\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1000\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003esample_timesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e250\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e27\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003eimage_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ein\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e):\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e) \u003cspan class=\"pl-c\"\u003e# this can optionally be decoder(images, text) if you wish to condition on the text encodings as well, though it was hinted in the paper it didn't do much\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do above for many steps\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003edalle2\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDALLE2\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eprior\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edalle2\u003c/span\u003e(\n    [\u003cspan class=\"pl-s\"\u003e'a butterfly trying to escape a tornado'\u003c/span\u003e],\n    \u003cspan class=\"pl-s1\"\u003econd_scale\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e2.\u003c/span\u003e \u003cspan class=\"pl-c\"\u003e# classifier free guidance strength (\u0026gt; 1 would strengthen the condition)\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-c\"\u003e# save your image (in this example, of size 256x256)\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eAlternatively, you can also use \u003ca href=\"https://github.com/mlfoundations/open_clip\"\u003eOpen Clip\u003c/a\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"$ pip install open-clip-torch\"\u003e\u003cpre\u003e$ pip install open-clip-torch\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eEx. using the \u003ca href=\"https://laion.ai/blog/large-openclip/\" rel=\"nofollow\"\u003eSOTA Open Clip\u003c/a\u003e model trained by \u003ca href=\"https://github.com/rom1504\"\u003eRomain\u003c/a\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"from dalle2_pytorch import OpenClipAdapter\n\nclip = OpenClipAdapter('ViT-H/14')\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eOpenClipAdapter\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eOpenClipAdapter\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e'ViT-H/14'\u003c/span\u003e)\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eNow you'll just have to worry about training the Prior and the Decoder!\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eInpainting\u003c/h2\u003e\u003ca id=\"user-content-inpainting\" class=\"anchor\" aria-label=\"Permalink: Inpainting\" href=\"#inpainting\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eInpainting is also built into the \u003ccode\u003eDecoder\u003c/code\u003e. You simply have to pass in the \u003ccode\u003einpaint_image\u003c/code\u003e and \u003ccode\u003einpaint_mask\u003c/code\u003e (boolean tensor where \u003ccode\u003eTrue\u003c/code\u003e indicates which regions of the inpaint image to keep)\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThis repository uses the formulation put forth by \u003ca href=\"https://arxiv.org/abs/2201.09865\" rel=\"nofollow\"\u003eLugmayr et al. in Repaint\u003c/a\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import Unet, Decoder, CLIP\n\n# trained clip from step 1\n\nclip = CLIP(\n    dim_text = 512,\n    dim_image = 512,\n    dim_latent = 512,\n    num_text_tokens = 49408,\n    text_enc_depth = 6,\n    text_seq_len = 256,\n    text_heads = 8,\n    visual_enc_depth = 6,\n    visual_image_size = 256,\n    visual_patch_size = 32,\n    visual_heads = 8\n).cuda()\n\n# 2 unets for the decoder (a la cascading DDPM)\n\nunet = Unet(\n    dim = 16,\n    image_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    dim_mults = (1, 1, 1, 1)\n).cuda()\n\n\n# decoder, which contains the unet(s) and clip\n\ndecoder = Decoder(\n    clip = clip,\n    unet = (unet,),               # insert both unets in order of low resolution to highest resolution (you can have as many stages as you want here)\n    image_sizes = (256,),         # resolutions, 256 for first unet, 512 for second. these must be unique and in ascending order (matches with the unets passed in)\n    timesteps = 1000,\n    image_cond_drop_prob = 0.1,\n    text_cond_drop_prob = 0.5\n).cuda()\n\n# mock images (get a lot of this)\n\nimages = torch.randn(4, 3, 256, 256).cuda()\n\n# feed images into decoder, specifying which unet you want to train\n# each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme\n\nloss = decoder(images, unet_number = 1)\nloss.backward()\n\n# do the above for many steps for both unets\n\nmock_image_embed = torch.randn(1, 512).cuda()\n\n# then to do inpainting\n\ninpaint_image = torch.randn(1, 3, 256, 256).cuda()      # (batch, channels, height, width)\ninpaint_mask = torch.ones(1, 256, 256).bool().cuda()    # (batch, height, width)\n\ninpainted_images = decoder.sample(\n    image_embed = mock_image_embed,\n    inpaint_image = inpaint_image,    # just pass in the inpaint image\n    inpaint_mask = inpaint_mask       # and the mask\n)\n\ninpainted_images.shape # (1, 3, 256, 256)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eUnet\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoder\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eCLIP\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# trained clip from step 1\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eCLIP\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim_text\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_latent\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003enum_text_tokens\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_seq_len\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_image_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_patch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# 2 unets for the decoder (a la cascading DDPM)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e)\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\n\u003cspan class=\"pl-c\"\u003e# decoder, which contains the unet(s) and clip\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDecoder\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e,),               \u003cspan class=\"pl-c\"\u003e# insert both unets in order of low resolution to highest resolution (you can have as many stages as you want here)\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eimage_sizes\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,),         \u003cspan class=\"pl-c\"\u003e# resolutions, 256 for first unet, 512 for second. these must be unique and in ascending order (matches with the unets passed in)\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1000\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock images (get a lot of this)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# feed images into decoder, specifying which unet you want to train\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e)\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do the above for many steps for both unets\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003emock_image_embed\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# then to do inpainting\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003einpaint_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()      \u003cspan class=\"pl-c\"\u003e# (batch, channels, height, width)\u003c/span\u003e\n\u003cspan class=\"pl-s1\"\u003einpaint_mask\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eones\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ebool\u003c/span\u003e().\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()    \u003cspan class=\"pl-c\"\u003e# (batch, height, width)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003einpainted_images\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003esample\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eimage_embed\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003emock_image_embed\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003einpaint_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003einpaint_image\u003c/span\u003e,    \u003cspan class=\"pl-c\"\u003e# just pass in the inpaint image\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003einpaint_mask\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003einpaint_mask\u003c/span\u003e       \u003cspan class=\"pl-c\"\u003e# and the mask\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-s1\"\u003einpainted_images\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eshape\u003c/span\u003e \u003cspan class=\"pl-c\"\u003e# (1, 3, 256, 256)\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eExperimental\u003c/h2\u003e\u003ca id=\"user-content-experimental\" class=\"anchor\" aria-label=\"Permalink: Experimental\" href=\"#experimental\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDALL-E2 with Latent Diffusion\u003c/h3\u003e\u003ca id=\"user-content-dall-e2-with-latent-diffusion\" class=\"anchor\" aria-label=\"Permalink: DALL-E2 with Latent Diffusion\" href=\"#dall-e2-with-latent-diffusion\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThis repository decides to take the next step and offer DALL-E v2 combined with \u003ca href=\"https://huggingface.co/spaces/multimodalart/latentdiffusion\" rel=\"nofollow\"\u003elatent diffusion\u003c/a\u003e, from Rombach et al.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eYou can use it as follows. Latent diffusion can be limited to just the first U-Net in the cascade, or to any number you wish.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThe repository also comes equipped with all the necessary settings to recreate \u003ccode\u003eViT-VQGan\u003c/code\u003e from the \u003ca href=\"https://arxiv.org/abs/2110.04627\" rel=\"nofollow\"\u003eImproved VQGans\u003c/a\u003e paper. Furthermore, the \u003ca href=\"https://github.com/lucidrains/vector-quantize-pytorch\"\u003evector quantization\u003c/a\u003e library also comes equipped to do \u003ca href=\"https://arxiv.org/abs/2203.01941\" rel=\"nofollow\"\u003eresidual or multi-headed quantization\u003c/a\u003e, which I believe will give an even further boost in performance to the autoencoder.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import Unet, Decoder, CLIP, VQGanVAE\n\n# trained clip from step 1\n\nclip = CLIP(\n    dim_text = 512,\n    dim_image = 512,\n    dim_latent = 512,\n    num_text_tokens = 49408,\n    text_enc_depth = 1,\n    text_seq_len = 256,\n    text_heads = 8,\n    visual_enc_depth = 1,\n    visual_image_size = 256,\n    visual_patch_size = 32,\n    visual_heads = 8\n)\n\n# 3 unets for the decoder (a la cascading DDPM)\n\n# first two unets are doing latent diffusion\n# vqgan-vae must be trained beforehand\n\nvae1 = VQGanVAE(\n    dim = 32,\n    image_size = 256,\n    layers = 3,\n    layer_mults = (1, 2, 4)\n)\n\nvae2 = VQGanVAE(\n    dim = 32,\n    image_size = 512,\n    layers = 3,\n    layer_mults = (1, 2, 4)\n)\n\nunet1 = Unet(\n    dim = 32,\n    image_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    sparse_attn = True,\n    sparse_attn_window = 2,\n    dim_mults = (1, 2, 4, 8)\n)\n\nunet2 = Unet(\n    dim = 32,\n    image_embed_dim = 512,\n    channels = 3,\n    dim_mults = (1, 2, 4, 8, 16),\n    cond_on_image_embeds = True,\n    cond_on_text_encodings = False\n)\n\nunet3 = Unet(\n    dim = 32,\n    image_embed_dim = 512,\n    channels = 3,\n    dim_mults = (1, 2, 4, 8, 16),\n    cond_on_image_embeds = True,\n    cond_on_text_encodings = False,\n    attend_at_middle = False\n)\n\n# decoder, which contains the unet(s) and clip\n\ndecoder = Decoder(\n    clip = clip,\n    vae = (vae1, vae2),                # latent diffusion for unet1 (vae1) and unet2 (vae2), but not for the last unet3\n    unet = (unet1, unet2, unet3),      # insert unets in order of low resolution to highest resolution (you can have as many stages as you want here)\n    image_sizes = (256, 512, 1024),    # resolutions, 256 for first unet, 512 for second, 1024 for third\n    timesteps = 100,\n    image_cond_drop_prob = 0.1,\n    text_cond_drop_prob = 0.5\n).cuda()\n\n# mock images (get a lot of this)\n\nimages = torch.randn(1, 3, 1024, 1024).cuda()\n\n# feed images into decoder, specifying which unet you want to train\n# each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme\n\nwith decoder.one_unet_in_gpu(1):\n    loss = decoder(images, unet_number = 1)\n    loss.backward()\n\nwith decoder.one_unet_in_gpu(2):\n    loss = decoder(images, unet_number = 2)\n    loss.backward()\n\nwith decoder.one_unet_in_gpu(3):\n    loss = decoder(images, unet_number = 3)\n    loss.backward()\n\n# do the above for many steps for both unets\n\n# then it will learn to generate images based on the CLIP image embeddings\n\n# chaining the unets from lowest resolution to highest resolution (thus cascading)\n\nmock_image_embed = torch.randn(1, 512).cuda()\nimages = decoder.sample(mock_image_embed) # (1, 3, 1024, 1024)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eUnet\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoder\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eCLIP\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eVQGanVAE\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# trained clip from step 1\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eCLIP\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim_text\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_latent\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003enum_text_tokens\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_seq_len\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_image_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_patch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-c\"\u003e# 3 unets for the decoder (a la cascading DDPM)\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# first two unets are doing latent diffusion\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# vqgan-vae must be trained beforehand\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003evae1\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eVQGanVAE\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003elayers\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003elayer_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e)\n)\n\n\u003cspan class=\"pl-s1\"\u003evae2\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eVQGanVAE\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003elayers\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003elayer_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e)\n)\n\n\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003esparse_attn\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003esparse_attn_window\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e)\n)\n\n\u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003econd_on_image_embeds\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_on_text_encodings\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-s1\"\u003eunet3\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003econd_on_image_embeds\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_on_text_encodings\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eattend_at_middle\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-c\"\u003e# decoder, which contains the unet(s) and clip\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDecoder\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evae\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-s1\"\u003evae1\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003evae2\u003c/span\u003e),                \u003cspan class=\"pl-c\"\u003e# latent diffusion for unet1 (vae1) and unet2 (vae2), but not for the last unet3\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet3\u003c/span\u003e),      \u003cspan class=\"pl-c\"\u003e# insert unets in order of low resolution to highest resolution (you can have as many stages as you want here)\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eimage_sizes\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e1024\u003c/span\u003e),    \u003cspan class=\"pl-c\"\u003e# resolutions, 256 for first unet, 512 for second, 1024 for third\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e100\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.1\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_cond_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock images (get a lot of this)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e1024\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e1024\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# feed images into decoder, specifying which unet you want to train\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eone_unet_in_gpu\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e):\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e)\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eone_unet_in_gpu\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e):\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e)\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eone_unet_in_gpu\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e):\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e)\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebackward\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# do the above for many steps for both unets\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# then it will learn to generate images based on the CLIP image embeddings\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# chaining the unets from lowest resolution to highest resolution (thus cascading)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003emock_image_embed\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003esample\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003emock_image_embed\u003c/span\u003e) \u003cspan class=\"pl-c\"\u003e# (1, 3, 1024, 1024)\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eTraining wrapper\u003c/h2\u003e\u003ca id=\"user-content-training-wrapper\" class=\"anchor\" aria-label=\"Permalink: Training wrapper\" href=\"#training-wrapper\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDecoder Training\u003c/h3\u003e\u003ca id=\"user-content-decoder-training\" class=\"anchor\" aria-label=\"Permalink: Decoder Training\" href=\"#decoder-training\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eTraining the \u003ccode\u003eDecoder\u003c/code\u003e may be confusing, as one needs to keep track of an optimizer for each of the \u003ccode\u003eUnet\u003c/code\u003e(s) separately. Each \u003ccode\u003eUnet\u003c/code\u003e will also need its own corresponding exponential moving average. The \u003ccode\u003eDecoderTrainer\u003c/code\u003e hopes to make this simple, as shown below\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import DALLE2, Unet, Decoder, CLIP, DecoderTrainer\n\nclip = CLIP(\n    dim_text = 512,\n    dim_image = 512,\n    dim_latent = 512,\n    num_text_tokens = 49408,\n    text_enc_depth = 6,\n    text_seq_len = 256,\n    text_heads = 8,\n    visual_enc_depth = 6,\n    visual_image_size = 256,\n    visual_patch_size = 32,\n    visual_heads = 8\n).cuda()\n\n# mock data\n\ntext = torch.randint(0, 49408, (32, 256)).cuda()\nimages = torch.randn(32, 3, 256, 256).cuda()\n\n# decoder (with unet)\n\nunet1 = Unet(\n    dim = 128,\n    image_embed_dim = 512,\n    text_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    dim_mults=(1, 2, 4, 8),\n    cond_on_text_encodings = True,\n).cuda()\n\nunet2 = Unet(\n    dim = 16,\n    image_embed_dim = 512,\n    cond_dim = 128,\n    channels = 3,\n    dim_mults = (1, 2, 4, 8, 16),\n).cuda()\n\ndecoder = Decoder(\n    unet = (unet1, unet2),\n    image_sizes = (128, 256),\n    clip = clip,\n    timesteps = 1000\n).cuda()\n\ndecoder_trainer = DecoderTrainer(\n    decoder,\n    lr = 3e-4,\n    wd = 1e-2,\n    ema_beta = 0.99,\n    ema_update_after_step = 1000,\n    ema_update_every = 10,\n)\n\nfor unet_number in (1, 2):\n    loss = decoder_trainer(\n        images,\n        text = text,\n        unet_number = unet_number, # which unet to train on\n        max_batch_size = 4         # gradient accumulation - this sets the maximum batch size in which to do forward and backwards pass - for this example 32 / 4 == 8 times\n    )\n\n    decoder_trainer.update(unet_number) # update the specific unet as well as its exponential moving average\n\n# after much training\n# you can sample from the exponentially moving averaged unets as so\n\nmock_image_embed = torch.randn(32, 512).cuda()\nimages = decoder_trainer.sample(image_embed = mock_image_embed, text = text) # (4, 3, 256, 256)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDALLE2\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eUnet\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoder\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eCLIP\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoderTrainer\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eCLIP\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim_text\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_latent\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003enum_text_tokens\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_seq_len\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_image_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_patch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock data\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandint\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e, (\u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e)).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# decoder (with unet)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003econd_on_text_encodings\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eimage_embed_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_dim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003echannels\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e),\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDecoder\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003eimage_sizes\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1000\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003edecoder_trainer\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDecoderTrainer\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003elr\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3e-4\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003ewd\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1e-2\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eema_beta\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.99\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eema_update_after_step\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1000\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eema_update_every\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e10\u003c/span\u003e,\n)\n\n\u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ein\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e):\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder_trainer\u003c/span\u003e(\n        \u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e,\n        \u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e,\n        \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e, \u003cspan class=\"pl-c\"\u003e# which unet to train on\u003c/span\u003e\n        \u003cspan class=\"pl-s1\"\u003emax_batch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e         \u003cspan class=\"pl-c\"\u003e# gradient accumulation - this sets the maximum batch size in which to do forward and backwards pass - for this example 32 / 4 == 8 times\u003c/span\u003e\n    )\n\n    \u003cspan class=\"pl-s1\"\u003edecoder_trainer\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eupdate\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e) \u003cspan class=\"pl-c\"\u003e# update the specific unet as well as its exponential moving average\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# after much training\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# you can sample from the exponentially moving averaged unets as so\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003emock_image_embed\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edecoder_trainer\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003esample\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimage_embed\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003emock_image_embed\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e) \u003cspan class=\"pl-c\"\u003e# (4, 3, 256, 256)\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDiffusion Prior Training\u003c/h3\u003e\u003ca id=\"user-content-diffusion-prior-training\" class=\"anchor\" aria-label=\"Permalink: Diffusion Prior Training\" href=\"#diffusion-prior-training\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eSimilarly, one can use the \u003ccode\u003eDiffusionPriorTrainer\u003c/code\u003e to automatically instantiate and keep track of an exponential moving averaged prior.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import DALLE2, DiffusionPriorNetwork, DiffusionPrior, DiffusionPriorTrainer, Unet, Decoder, CLIP\n\nclip = CLIP(\n    dim_text = 512,\n    dim_image = 512,\n    dim_latent = 512,\n    num_text_tokens = 49408,\n    text_enc_depth = 6,\n    text_seq_len = 256,\n    text_heads = 8,\n    visual_enc_depth = 6,\n    visual_image_size = 256,\n    visual_patch_size = 32,\n    visual_heads = 8\n).cuda()\n\n# mock data\n\ntext = torch.randint(0, 49408, (512, 256)).cuda()\nimages = torch.randn(512, 3, 256, 256).cuda()\n\n# prior networks (with transformer)\n\nprior_network = DiffusionPriorNetwork(\n    dim = 512,\n    depth = 6,\n    dim_head = 64,\n    heads = 8\n).cuda()\n\ndiffusion_prior = DiffusionPrior(\n    net = prior_network,\n    clip = clip,\n    timesteps = 100,\n    cond_drop_prob = 0.2\n).cuda()\n\ndiffusion_prior_trainer = DiffusionPriorTrainer(\n    diffusion_prior,\n    lr = 3e-4,\n    wd = 1e-2,\n    ema_beta = 0.99,\n    ema_update_after_step = 1000,\n    ema_update_every = 10,\n)\n\nloss = diffusion_prior_trainer(text, images, max_batch_size = 4)\ndiffusion_prior_trainer.update()  # this will update the optimizer as well as the exponential moving averaged diffusion prior\n\n# after much of the above three lines in a loop\n# you can sample from the exponential moving average of the diffusion prior identically to how you do so for DiffusionPrior\n\nimage_embeds = diffusion_prior_trainer.sample(text, max_batch_size = 4) # (512, 512) - exponential moving averaged image embeddings\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDALLE2\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDiffusionPriorNetwork\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDiffusionPrior\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDiffusionPriorTrainer\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eUnet\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoder\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eCLIP\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eCLIP\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim_text\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_image\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_latent\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003enum_text_tokens\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_seq_len\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etext_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_enc_depth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_image_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_patch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003evisual_heads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# mock data\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandint\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e49408\u003c/span\u003e, (\u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e)).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# prior networks (with transformer)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPriorNetwork\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edepth\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_head\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e64\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eheads\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPrior\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003enet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eprior_network\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclip\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e100\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003econd_drop_prob\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.2\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003ediffusion_prior_trainer\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDiffusionPriorTrainer\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003ediffusion_prior\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003elr\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3e-4\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003ewd\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1e-2\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eema_beta\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.99\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eema_update_after_step\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1000\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eema_update_every\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e10\u003c/span\u003e,\n)\n\n\u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ediffusion_prior_trainer\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003emax_batch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e)\n\u003cspan class=\"pl-s1\"\u003ediffusion_prior_trainer\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eupdate\u003c/span\u003e()  \u003cspan class=\"pl-c\"\u003e# this will update the optimizer as well as the exponential moving averaged diffusion prior\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# after much of the above three lines in a loop\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# you can sample from the exponential moving average of the diffusion prior identically to how you do so for DiffusionPrior\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eimage_embeds\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ediffusion_prior_trainer\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003esample\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003etext\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003emax_batch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e) \u003cspan class=\"pl-c\"\u003e# (512, 512) - exponential moving averaged image embeddings\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eBonus\u003c/h2\u003e\u003ca id=\"user-content-bonus\" class=\"anchor\" aria-label=\"Permalink: Bonus\" href=\"#bonus\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eUnconditional Training\u003c/h3\u003e\u003ca id=\"user-content-unconditional-training\" class=\"anchor\" aria-label=\"Permalink: Unconditional Training\" href=\"#unconditional-training\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThe repository also contains the means to train unconditional DDPM model, or even cascading DDPMs. You simply have to set \u003ccode\u003eunconditional = True\u003c/code\u003e in the \u003ccode\u003eDecoder\u003c/code\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eex.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import torch\nfrom dalle2_pytorch import Unet, Decoder, DecoderTrainer\n\n# unet for the cascading ddpm\n\nunet1 = Unet(\n    dim = 128,\n    dim_mults=(1, 2, 4, 8)\n).cuda()\n\nunet2 = Unet(\n    dim = 32,\n    dim_mults = (1, 2, 4, 8, 16)\n).cuda()\n\n# decoder, which contains the unets\n\ndecoder = Decoder(\n    unet = (unet1, unet2),\n    image_sizes = (256, 512),  # first unet up to 256px, then second to 512px\n    timesteps = 1000,\n    unconditional = True\n).cuda()\n\n# decoder trainer\n\ndecoder_trainer = DecoderTrainer(decoder)\n\n# images (get a lot of this)\n\nimages = torch.randn(1, 3, 512, 512).cuda()\n\n# feed images into decoder\n\nfor i in (1, 2):\n    loss = decoder_trainer(images, unet_number = i)\n    decoder_trainer.update(unet_number = i)\n\n# do the above for many many many many images\n# then it will learn to generate images\n\nimages = decoder_trainer.sample(batch_size = 36, max_batch_size = 4) # (36, 3, 512, 512)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eUnet\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoder\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDecoderTrainer\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# unet for the cascading ddpm\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e128\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e)\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eUnet\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003edim\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003edim_mults\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e16\u003c/span\u003e)\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# decoder, which contains the unets\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDecoder\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eunet\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-s1\"\u003eunet1\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet2\u003c/span\u003e),\n    \u003cspan class=\"pl-s1\"\u003eimage_sizes\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e256\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e),  \u003cspan class=\"pl-c\"\u003e# first unet up to 256px, then second to 512px\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003etimesteps\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1000\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eunconditional\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e\n).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# decoder trainer\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003edecoder_trainer\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eDecoderTrainer\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003edecoder\u003c/span\u003e)\n\n\u003cspan class=\"pl-c\"\u003e# images (get a lot of this)\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etorch\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erandn\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e512\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003ecuda\u003c/span\u003e()\n\n\u003cspan class=\"pl-c\"\u003e# feed images into decoder\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ei\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ein\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e):\n    \u003cspan class=\"pl-s1\"\u003eloss\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edecoder_trainer\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ei\u003c/span\u003e)\n    \u003cspan class=\"pl-s1\"\u003edecoder_trainer\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eupdate\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eunet_number\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ei\u003c/span\u003e)\n\n\u003cspan class=\"pl-c\"\u003e# do the above for many many many many images\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e# then it will learn to generate images\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eimages\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edecoder_trainer\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003esample\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003ebatch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e36\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003emax_batch_size\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e) \u003cspan class=\"pl-c\"\u003e# (36, 3, 512, 512)\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDataloaders\u003c/h2\u003e\u003ca id=\"user-content-dataloaders\" class=\"anchor\" aria-label=\"Permalink: Dataloaders\" href=\"#dataloaders\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDecoder Dataloaders\u003c/h3\u003e\u003ca id=\"user-content-decoder-dataloaders\" class=\"anchor\" aria-label=\"Permalink: Decoder Dataloaders\" href=\"#decoder-dataloaders\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eIn order to make loading data simple and efficient, we include some general dataloaders that can be used to train portions of the network.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDecoder: Image Embedding Dataset\u003c/h4\u003e\u003ca id=\"user-content-decoder-image-embedding-dataset\" class=\"anchor\" aria-label=\"Permalink: Decoder: Image Embedding Dataset\" href=\"#decoder-image-embedding-dataset\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWhen training the decoder (and up samplers if training together) in isolation, you will need to load images and corresponding image embeddings. This dataset can read two similar types of datasets. First, it can read a \u003ca href=\"https://github.com/webdataset/webdataset\"\u003ewebdataset\u003c/a\u003e that contains \u003ccode\u003e.jpg\u003c/code\u003e and \u003ccode\u003e.npy\u003c/code\u003e files in the \u003ccode\u003e.tar\u003c/code\u003es that contain the images and associated image embeddings respectively. Alternatively, you can also specify a source for the embeddings outside of the webdataset. In this case, the path to the embeddings should contain \u003ccode\u003e.npy\u003c/code\u003e files with the same shard numbers as the webdataset and there should be a correspondence between the filename of the \u003ccode\u003e.jpg\u003c/code\u003e and the index of the embedding in the \u003ccode\u003e.npy\u003c/code\u003e. So, for example, \u003ccode\u003e0001.tar\u003c/code\u003e from the webdataset with image \u003ccode\u003e00010509.jpg\u003c/code\u003e (the first 4 digits are the shard number and the last 4 are the index) in it should be paralleled by a \u003ccode\u003eimg_emb_0001.npy\u003c/code\u003e which contains a NumPy array with the embedding at index 509.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eGenerating a dataset of this type:\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eUse \u003ca href=\"https://github.com/rom1504/img2dataset\"\u003eimg2dataset\u003c/a\u003e to generate a webdataset.\u003c/li\u003e\n\u003cli\u003eUse \u003ca href=\"https://github.com/rom1504/clip-retrieval\"\u003eclip-retrieval\u003c/a\u003e to convert the images to embeddings.\u003c/li\u003e\n\u003cli\u003eUse \u003ca href=\"https://github.com/Veldrovive/embedding-dataset-reordering\"\u003eembedding-dataset-reordering\u003c/a\u003e to reorder the embeddings into the expected format.\u003c/li\u003e\n\u003c/ol\u003e\n\u003cp dir=\"auto\"\u003eUsage:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"from dalle2_pytorch.dataloaders import ImageEmbeddingDataset, create_image_embedding_dataloader\n\n# Create a dataloader directly.\ndataloader = create_image_embedding_dataloader(\n    tar_url=\u0026quot;/path/or/url/to/webdataset/{0000..9999}.tar\u0026quot;, # Uses bracket expanding notation. This specifies to read all tars from 0000.tar to 9999.tar\n    embeddings_url=\u0026quot;path/or/url/to/embeddings/folder\u0026quot;,     # Included if .npy files are not in webdataset. Left out or set to None otherwise\n    num_workers=4,\n    batch_size=32,\n    shard_width=4,                                         # If a file in the webdataset shard 3 is named 0003039.jpg, we know the shard width is 4 and the last three digits are the index\n    shuffle_num=200,                                       # Does a shuffle of the data with a buffer size of 200\n    shuffle_shards=True,                                   # Shuffle the order the shards are read in\n    resample_shards=False,                                 # Sample shards with replacement. If true, an epoch will be infinite unless stopped manually\n)\nfor img, emb in dataloader:\n    print(img.shape)  # torch.Size([32, 3, 256, 256])\n    print(emb[\u0026quot;img\u0026quot;].shape)  # torch.Size([32, 512])\n    # Train decoder only as shown above\n\n# Or create a dataset without a loader so you can configure it manually\ndataset = ImageEmbeddingDataset(\n    urls=\u0026quot;/path/or/url/to/webdataset/{0000..9999}.tar\u0026quot;,\n    embedding_folder_url=\u0026quot;path/or/url/to/embeddings/folder\u0026quot;,\n    shard_width=4,\n    shuffle_shards=True,\n    resample=False\n)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edalle2_pytorch\u003c/span\u003e.\u003cspan class=\"pl-s1\"\u003edataloaders\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eImageEmbeddingDataset\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003ecreate_image_embedding_dataloader\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# Create a dataloader directly.\u003c/span\u003e\n\u003cspan class=\"pl-s1\"\u003edataloader\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ecreate_image_embedding_dataloader\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003etar_url\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"/path/or/url/to/webdataset/{0000..9999}.tar\"\u003c/span\u003e, \u003cspan class=\"pl-c\"\u003e# Uses bracket expanding notation. This specifies to read all tars from 0000.tar to 9999.tar\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eembeddings_url\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"path/or/url/to/embeddings/folder\"\u003c/span\u003e,     \u003cspan class=\"pl-c\"\u003e# Included if .npy files are not in webdataset. Left out or set to None otherwise\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003enum_workers\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003ebatch_size\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e32\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eshard_width\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e,                                         \u003cspan class=\"pl-c\"\u003e# If a file in the webdataset shard 3 is named 0003039.jpg, we know the shard width is 4 and the last three digits are the index\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eshuffle_num\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e200\u003c/span\u003e,                                       \u003cspan class=\"pl-c\"\u003e# Does a shuffle of the data with a buffer size of 200\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eshuffle_shards\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,                                   \u003cspan class=\"pl-c\"\u003e# Shuffle the order the shards are read in\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003eresample_shards\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e,                                 \u003cspan class=\"pl-c\"\u003e# Sample shards with replacement. If true, an epoch will be infinite unless stopped manually\u003c/span\u003e\n)\n\u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eimg\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eemb\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ein\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edataloader\u003c/span\u003e:\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eimg\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eshape\u003c/span\u003e)  \u003cspan class=\"pl-c\"\u003e# torch.Size([32, 3, 256, 256])\u003c/span\u003e\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eemb\u003c/span\u003e[\u003cspan class=\"pl-s\"\u003e\"img\"\u003c/span\u003e].\u003cspan class=\"pl-c1\"\u003eshape\u003c/span\u003e)  \u003cspan class=\"pl-c\"\u003e# torch.Size([32, 512])\u003c/span\u003e\n    \u003cspan class=\"pl-c\"\u003e# Train decoder only as shown above\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# Or create a dataset without a loader so you can configure it manually\u003c/span\u003e\n\u003cspan class=\"pl-s1\"\u003edataset\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eImageEmbeddingDataset\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eurls\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"/path/or/url/to/webdataset/{0000..9999}.tar\"\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eembedding_folder_url\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"path/or/url/to/embeddings/folder\"\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eshard_width\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eshuffle_shards\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003eresample\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e\n)\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eScripts\u003c/h3\u003e\u003ca id=\"user-content-scripts\" class=\"anchor\" aria-label=\"Permalink: Scripts\" href=\"#scripts\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e\u003ccode\u003etrain_diffusion_prior.py\u003c/code\u003e\u003c/h4\u003e\u003ca id=\"user-content-train_diffusion_priorpy\" class=\"anchor\" aria-label=\"Permalink: train_diffusion_prior.py\" href=\"#train_diffusion_priorpy\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eFor detailed information on training the diffusion prior, please refer to the \u003ca href=\"/lucidrains/DALLE2-pytorch/blob/main/prior.md\"\u003ededicated readme\u003c/a\u003e\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eTodo\u003c/h2\u003e\u003ca id=\"user-content-todo\" class=\"anchor\" aria-label=\"Permalink: Todo\" href=\"#todo\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul class=\"contains-task-list\"\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e finish off gaussian diffusion class for latent embedding - allow for prediction of epsilon\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e add what was proposed in the paper, where DDPM objective for image latent embedding predicts x0 directly (reread vq-diffusion paper and get caught up on that line of work)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e make sure it works end to end to produce an output tensor, taking a single gradient step\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e augment unet so that it can also be conditioned on text encodings (although in paper they hinted this didn't make much a difference)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e figure out all the current bag of tricks needed to make DDPMs great (starting with the blur trick mentioned in paper)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e build the cascading ddpm by having Decoder class manage multiple unets at different resolutions\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e add efficient attention in unet\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e be able to finely customize what to condition on (text, image embed) for specific unet in the cascade (super resolution ddpms near the end may not need too much conditioning)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e offload unets not being trained on to CPU for memory efficiency (for training each resolution unets separately)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e build out latent diffusion architecture, with the vq-reg variant (vqgan-vae), make it completely optional and compatible with cascading ddpms\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e for decoder, allow ability to customize objective (predict epsilon vs x0), in case latent diffusion does better with prediction of x0\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e use attention-based upsampling \u003ca href=\"https://arxiv.org/abs/2112.11435\" rel=\"nofollow\"\u003ehttps://arxiv.org/abs/2112.11435\u003c/a\u003e\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e use inheritance just this once for sharing logic between decoder and prior network ddpms\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e bring in vit-vqgan \u003ca href=\"https://arxiv.org/abs/2110.04627\" rel=\"nofollow\"\u003ehttps://arxiv.org/abs/2110.04627\u003c/a\u003e for the latent diffusion\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e abstract interface for CLIP adapter class, so other CLIPs can be brought in\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e take care of mixed precision as well as gradient accumulation within decoder trainer\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e just take care of the training for the decoder in a wrapper class, as each unet in the cascade will need its own optimizer\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e bring in tools to train vqgan-vae\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e add convnext backbone for vqgan-vae (in addition to vit [vit-vqgan] + resnet)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e make sure DDPMs can be run with traditional resnet blocks (but leave convnext as an option for experimentation)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e make sure for the latter unets in the cascade, one can train on crops for learning super resolution (constrain the unet to be only convolutions in that case, or allow conv-like attention with rel pos bias)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e offer setting in diffusion prior to split time and image embeddings into multiple tokens, configurable, for more surface area during attention\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e make sure resnet hyperparameters can be configurable across unet depth (groups and expansion factor)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e pull logic for training diffusion prior into a class DiffusionPriorTrainer, for eventual script based + CLI based training\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e make sure the cascading ddpm in the repository can be trained unconditionally, offer a one-line CLI tool for training on a folder of images\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e bring in cross-scale embedding from iclr paper \u003ca href=\"https://github.com/lucidrains/vit-pytorch/blob/main/vit_pytorch/crossformer.py#L14\"\u003ehttps://github.com/lucidrains/vit-pytorch/blob/main/vit_pytorch/crossformer.py#L14\u003c/a\u003e\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e cross embed layers for downsampling, as an option\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e use an experimental tracker agnostic setup, as done \u003ca href=\"https://github.com/lucidrains/tf-bind-transformer#simple-trainer-class-for-fine-tuning\"\u003ehere\u003c/a\u003e\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e use pydantic for config drive training\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e for both diffusion prior and decoder, all exponential moving averaged models needs to be saved and restored as well (as well as the step number)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e offer save / load methods on the trainer classes to automatically take care of state dicts for scalers / optimizers / saving versions and checking for breaking changes\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e allow for creation of diffusion prior model off pydantic config classes - consider the same for tracker configs\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e bring in skip-layer excitations (from lightweight gan paper) to see if it helps for either decoder of unet or vqgan-vae training (doesnt work well)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e test out grid attention in cascading ddpm locally, decide whether to keep or remove \u003ca href=\"https://arxiv.org/abs/2204.01697\" rel=\"nofollow\"\u003ehttps://arxiv.org/abs/2204.01697\u003c/a\u003e (keeping, seems to be fine)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e allow for unet to be able to condition non-cross attention style as well\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e speed up inference, read up on papers (ddim)\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e add inpainting ability using resampler from repaint paper \u003ca href=\"https://arxiv.org/abs/2201.09865\" rel=\"nofollow\"\u003ehttps://arxiv.org/abs/2201.09865\u003c/a\u003e\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Completed task\" checked=\"\"\u003e add the final combination of upsample feature maps, used in unet squared, seems to have an effect in local experiments\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Incomplete task\"\u003e consider elucidated dalle2 \u003ca href=\"https://arxiv.org/abs/2206.00364\" rel=\"nofollow\"\u003ehttps://arxiv.org/abs/2206.00364\u003c/a\u003e\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Incomplete task\"\u003e add simple outpainting, text-guided 2x size the image for starters\u003c/li\u003e\n\u003cli class=\"task-list-item\"\u003e\u003cinput type=\"checkbox\" id=\"\" disabled=\"\" class=\"task-list-item-checkbox\" aria-label=\"Incomplete task\"\u003e interface out the vqgan-vae so a pretrained one can be pulled off the shelf to validate latent diffusion + DALL-E2\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eCitations\u003c/h2\u003e\u003ca id=\"user-content-citations\" class=\"anchor\" aria-label=\"Permalink: Citations\" href=\"#citations\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@misc{ramesh2022,\n    title   = {Hierarchical Text-Conditional Image Generation with CLIP Latents}, \n    author  = {Aditya Ramesh et al},\n    year    = {2022}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@misc\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eramesh2022\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eHierarchical Text-Conditional Image Generation with CLIP Latents\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e, \n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eAditya Ramesh et al\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2022\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@misc{crowson2022,\n    author  = {Katherine Crowson},\n    url     = {https://twitter.com/rivershavewings}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@misc\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003ecrowson2022\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eKatherine Crowson\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eurl\u003c/span\u003e     = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003ehttps://twitter.com/rivershavewings\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@misc{rombach2021highresolution,\n    title   = {High-Resolution Image Synthesis with Latent Diffusion Models}, \n    author  = {Robin Rombach and Andreas Blattmann and Dominik Lorenz and Patrick Esser and Björn Ommer},\n    year    = {2021},\n    eprint  = {2112.10752},\n    archivePrefix = {arXiv},\n    primaryClass = {cs.CV}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@misc\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003erombach2021highresolution\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eHigh-Resolution Image Synthesis with Latent Diffusion Models\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e, \n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eRobin Rombach and Andreas Blattmann and Dominik Lorenz and Patrick Esser and Björn Ommer\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2021\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eeprint\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2112.10752\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003earchivePrefix\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003earXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eprimaryClass\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003ecs.CV\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{shen2019efficient,\n    author  = {Zhuoran Shen and Mingyuan Zhang and Haiyu Zhao and Shuai Yi and Hongsheng Li},\n    title   = {Efficient Attention: Attention with Linear Complexities},\n    journal = {CoRR},\n    year    = {2018},\n    url     = {http://arxiv.org/abs/1812.01243},\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eshen2019efficient\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eZhuoran Shen and Mingyuan Zhang and Haiyu Zhao and Shuai Yi and Hongsheng Li\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eEfficient Attention: Attention with Linear Complexities\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eCoRR\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2018\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eurl\u003c/span\u003e     = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003ehttp://arxiv.org/abs/1812.01243\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{Yu2021VectorquantizedIM,\n    title   = {Vector-quantized Image Modeling with Improved VQGAN},\n    author  = {Jiahui Yu and Xin Li and Jing Yu Koh and Han Zhang and Ruoming Pang and James Qin and Alexander Ku and Yuanzhong Xu and Jason Baldridge and Yonghui Wu},\n    journal = {ArXiv},\n    year    = {2021},\n    volume  = {abs/2110.04627}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eYu2021VectorquantizedIM\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eVector-quantized Image Modeling with Improved VQGAN\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eJiahui Yu and Xin Li and Jing Yu Koh and Han Zhang and Ruoming Pang and James Qin and Alexander Ku and Yuanzhong Xu and Jason Baldridge and Yonghui Wu\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eArXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2021\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003evolume\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eabs/2110.04627\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{Shleifer2021NormFormerIT,\n    title   = {NormFormer: Improved Transformer Pretraining with Extra Normalization},\n    author  = {Sam Shleifer and Jason Weston and Myle Ott},\n    journal = {ArXiv},\n    year    = {2021},\n    volume  = {abs/2110.09456}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eShleifer2021NormFormerIT\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eNormFormer: Improved Transformer Pretraining with Extra Normalization\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eSam Shleifer and Jason Weston and Myle Ott\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eArXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2021\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003evolume\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eabs/2110.09456\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{Yu2022CoCaCC,\n    title   = {CoCa: Contrastive Captioners are Image-Text Foundation Models},\n    author  = {Jiahui Yu and Zirui Wang and Vijay Vasudevan and Legg Yeung and Mojtaba Seyedhosseini and Yonghui Wu},\n    journal = {ArXiv},\n    year    = {2022},\n    volume  = {abs/2205.01917}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eYu2022CoCaCC\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eCoCa: Contrastive Captioners are Image-Text Foundation Models\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eJiahui Yu and Zirui Wang and Vijay Vasudevan and Legg Yeung and Mojtaba Seyedhosseini and Yonghui Wu\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eArXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2022\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003evolume\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eabs/2205.01917\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@misc{wang2021crossformer,\n    title   = {CrossFormer: A Versatile Vision Transformer Hinging on Cross-scale Attention},\n    author  = {Wenxiao Wang and Lu Yao and Long Chen and Binbin Lin and Deng Cai and Xiaofei He and Wei Liu},\n    year    = {2021},\n    eprint  = {2108.00154},\n    archivePrefix = {arXiv},\n    primaryClass = {cs.CV}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@misc\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003ewang2021crossformer\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eCrossFormer: A Versatile Vision Transformer Hinging on Cross-scale Attention\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eWenxiao Wang and Lu Yao and Long Chen and Binbin Lin and Deng Cai and Xiaofei He and Wei Liu\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2021\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eeprint\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2108.00154\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003earchivePrefix\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003earXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eprimaryClass\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003ecs.CV\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{ho2021cascaded,\n    title   = {Cascaded Diffusion Models for High Fidelity Image Generation},\n    author  = {Ho, Jonathan and Saharia, Chitwan and Chan, William and Fleet, David J and Norouzi, Mohammad and Salimans, Tim},\n    journal = {arXiv preprint arXiv:2106.15282},\n    year    = {2021}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eho2021cascaded\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eCascaded Diffusion Models for High Fidelity Image Generation\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eHo, Jonathan and Saharia, Chitwan and Chan, William and Fleet, David J and Norouzi, Mohammad and Salimans, Tim\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003earXiv preprint arXiv:2106.15282\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2021\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@misc{Saharia2022,\n    title   = {Imagen: unprecedented photorealism × deep level of language understanding},\n    author  = {Chitwan Saharia*, William Chan*, Saurabh Saxena†, Lala Li†, Jay Whang†, Emily Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi, Rapha Gontijo Lopes, Tim Salimans, Jonathan Ho†, David Fleet†, Mohammad Norouzi*},\n    year    = {2022}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@misc\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eSaharia2022\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eImagen: unprecedented photorealism × deep level of language understanding\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eChitwan Saharia*, William Chan*, Saurabh Saxena†, Lala Li†, Jay Whang†, Emily Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi, Rapha Gontijo Lopes, Tim Salimans, Jonathan Ho†, David Fleet†, Mohammad Norouzi*\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2022\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{Choi2022PerceptionPT,\n    title   = {Perception Prioritized Training of Diffusion Models},\n    author  = {Jooyoung Choi and Jungbeom Lee and Chaehun Shin and Sungwon Kim and Hyunwoo J. Kim and Sung-Hoon Yoon},\n    journal = {ArXiv},\n    year    = {2022},\n    volume  = {abs/2204.00227}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eChoi2022PerceptionPT\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003ePerception Prioritized Training of Diffusion Models\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eJooyoung Choi and Jungbeom Lee and Chaehun Shin and Sungwon Kim and Hyunwoo J. Kim and Sung-Hoon Yoon\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eArXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2022\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003evolume\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eabs/2204.00227\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{Saharia2021PaletteID,\n    title   = {Palette: Image-to-Image Diffusion Models},\n    author  = {Chitwan Saharia and William Chan and Huiwen Chang and Chris A. Lee and Jonathan Ho and Tim Salimans and David J. Fleet and Mohammad Norouzi},\n    journal = {ArXiv},\n    year    = {2021},\n    volume  = {abs/2111.05826}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eSaharia2021PaletteID\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003ePalette: Image-to-Image Diffusion Models\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eChitwan Saharia and William Chan and Huiwen Chang and Chris A. Lee and Jonathan Ho and Tim Salimans and David J. Fleet and Mohammad Norouzi\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eArXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2021\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003evolume\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eabs/2111.05826\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{Lugmayr2022RePaintIU,\n    title   = {RePaint: Inpainting using Denoising Diffusion Probabilistic Models},\n    author  = {Andreas Lugmayr and Martin Danelljan and Andr{\\'e}s Romero and Fisher Yu and Radu Timofte and Luc Van Gool},\n    journal = {ArXiv},\n    year    = {2022},\n    volume  = {abs/2201.09865}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eLugmayr2022RePaintIU\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eRePaint: Inpainting using Denoising Diffusion Probabilistic Models\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eAndreas Lugmayr and Martin Danelljan and Andr{\\'e}s Romero and Fisher Yu and Radu Timofte and Luc Van Gool\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eArXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2022\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003evolume\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eabs/2201.09865\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@misc{chen2022analog,\n    title   = {Analog Bits: Generating Discrete Data using Diffusion Models with Self-Conditioning},\n    author  = {Ting Chen and Ruixiang Zhang and Geoffrey Hinton},\n    year    = {2022},\n    eprint  = {2208.04202},\n    archivePrefix = {arXiv},\n    primaryClass = {cs.CV}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@misc\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003echen2022analog\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eAnalog Bits: Generating Discrete Data using Diffusion Models with Self-Conditioning\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eTing Chen and Ruixiang Zhang and Geoffrey Hinton\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2022\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eeprint\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2208.04202\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003earchivePrefix\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003earXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eprimaryClass\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003ecs.CV\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{Qiao2019WeightS,\n    title   = {Weight Standardization},\n    author  = {Siyuan Qiao and Huiyu Wang and Chenxi Liu and Wei Shen and Alan Loddon Yuille},\n    journal = {ArXiv},\n    year    = {2019},\n    volume  = {abs/1903.10520}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eQiao2019WeightS\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eWeight Standardization\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eSiyuan Qiao and Huiyu Wang and Chenxi Liu and Wei Shen and Alan Loddon Yuille\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eArXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2019\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003evolume\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eabs/1903.10520\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@inproceedings{rogozhnikov2022einops,\n    title   = {Einops: Clear and Reliable Tensor Manipulations with Einstein-like Notation},\n    author  = {Alex Rogozhnikov},\n    booktitle = {International Conference on Learning Representations},\n    year    = {2022},\n    url     = {https://openreview.net/forum?id=oapKSVM2bcj}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@inproceedings\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003erogozhnikov2022einops\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eEinops: Clear and Reliable Tensor Manipulations with Einstein-like Notation\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eAlex Rogozhnikov\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ebooktitle\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eInternational Conference on Learning Representations\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2022\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eurl\u003c/span\u003e     = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003ehttps://openreview.net/forum?id=oapKSVM2bcj\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{Sunkara2022NoMS,\n    title   = {No More Strided Convolutions or Pooling: A New CNN Building Block for Low-Resolution Images and Small Objects},\n    author  = {Raja Sunkara and Tie Luo},\n    journal = {ArXiv},\n    year    = {2022},\n    volume  = {abs/2208.03641}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eSunkara2022NoMS\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eNo More Strided Convolutions or Pooling: A New CNN Building Block for Low-Resolution Images and Small Objects\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eRaja Sunkara and Tie Luo\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eArXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2022\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003evolume\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eabs/2208.03641\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-text-bibtex notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"@article{Salimans2022ProgressiveDF,\n    title   = {Progressive Distillation for Fast Sampling of Diffusion Models},\n    author  = {Tim Salimans and Jonathan Ho},\n    journal = {ArXiv},\n    year    = {2022},\n    volume  = {abs/2202.00512}\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003e@article\u003c/span\u003e{\u003cspan class=\"pl-en\"\u003eSalimans2022ProgressiveDF\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003etitle\u003c/span\u003e   = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eProgressive Distillation for Fast Sampling of Diffusion Models\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eauthor\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eTim Salimans and Jonathan Ho\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003ejournal\u003c/span\u003e = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eArXiv\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003eyear\u003c/span\u003e    = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003e2022\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-s\"\u003evolume\u003c/span\u003e  = \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e{\u003c/span\u003eabs/2202.00512\u003cspan class=\"pl-pds\"\u003e}\u003c/span\u003e\u003c/span\u003e\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eCreating noise from data is easy; creating data from noise is generative modeling.\u003c/em\u003e - \u003ca href=\"https://arxiv.org/abs/2011.13456\" rel=\"nofollow\"\u003eYang Song's paper\u003c/a\u003e\u003c/p\u003e\n\u003c/article\u003e","loaded":true,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":[{"level":2,"text":"DALL-E 2 - Pytorch","anchor":"dall-e-2---pytorch","htmlText":"DALL-E 2 - Pytorch"},{"level":2,"text":"Status","anchor":"status","htmlText":"Status"},{"level":2,"text":"Pre-Trained Models","anchor":"pre-trained-models","htmlText":"Pre-Trained Models"},{"level":2,"text":"Appreciation","anchor":"appreciation","htmlText":"Appreciation"},{"level":2,"text":"Install","anchor":"install","htmlText":"Install"},{"level":2,"text":"Usage","anchor":"usage","htmlText":"Usage"},{"level":2,"text":"Training on Preprocessed CLIP Embeddings","anchor":"training-on-preprocessed-clip-embeddings","htmlText":"Training on Preprocessed CLIP Embeddings"},{"level":2,"text":"OpenAI CLIP","anchor":"openai-clip","htmlText":"OpenAI CLIP"},{"level":2,"text":"Inpainting","anchor":"inpainting","htmlText":"Inpainting"},{"level":2,"text":"Experimental","anchor":"experimental","htmlText":"Experimental"},{"level":3,"text":"DALL-E2 with Latent Diffusion","anchor":"dall-e2-with-latent-diffusion","htmlText":"DALL-E2 with Latent Diffusion"},{"level":2,"text":"Training wrapper","anchor":"training-wrapper","htmlText":"Training wrapper"},{"level":3,"text":"Decoder Training","anchor":"decoder-training","htmlText":"Decoder Training"},{"level":3,"text":"Diffusion Prior Training","anchor":"diffusion-prior-training","htmlText":"Diffusion Prior Training"},{"level":2,"text":"Bonus","anchor":"bonus","htmlText":"Bonus"},{"level":3,"text":"Unconditional Training","anchor":"unconditional-training","htmlText":"Unconditional Training"},{"level":2,"text":"Dataloaders","anchor":"dataloaders","htmlText":"Dataloaders"},{"level":3,"text":"Decoder Dataloaders","anchor":"decoder-dataloaders","htmlText":"Decoder Dataloaders"},{"level":4,"text":"Decoder: Image Embedding Dataset","anchor":"decoder-image-embedding-dataset","htmlText":"Decoder: Image Embedding Dataset"},{"level":3,"text":"Scripts","anchor":"scripts","htmlText":"Scripts"},{"level":4,"text":"train_diffusion_prior.py","anchor":"train_diffusion_priorpy","htmlText":"train_diffusion_prior.py"},{"level":2,"text":"Todo","anchor":"todo","htmlText":"Todo"},{"level":2,"text":"Citations","anchor":"citations","htmlText":"Citations"}],"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Flucidrains%2FDALLE2-pytorch"}},{"displayName":"LICENSE","repoName":"DALLE2-pytorch","refName":"main","path":"LICENSE","preferredFileType":"license","tabName":"MIT","richText":null,"loaded":false,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":null,"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Flucidrains%2FDALLE2-pytorch"}}],"overviewFilesProcessingTime":0,"copilotSWEAgentEnabled":false}},"codeViewLayoutRoute":{"repo":{"id":478823173,"defaultBranch":"main","name":"DALLE2-pytorch","ownerLogin":"lucidrains","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2022-04-07T04:14:08.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/108653?v=4","public":true,"private":false,"isOrgOwned":false},"currentUser":null,"uploadToken":"GX9Fjvz77E9yvMANo_j3M-zo9jHFJAoeQT7wDnNvXfov24EAlEp3ZRbZLRiqmut_wuTy326s5ZvoMMxkUAHV7g","allShortcutsEnabled":false,"treeExpanded":true,"path":"/","symbolsExpanded":false,"refInfo":{"name":"main","listCacheKey":"v0:1697688176.0","canEdit":false,"currentOid":"680dfc4d93b70f9ab23c814a22ca18017a738ef6"},"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-4e5d7136862a2a48.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-4c35b25d88167fef.js","githubDevUrl":null},"csrf_tokens":{"/lucidrains/DALLE2-pytorch/branches":{"post":"9pJMg7jCm3aJf4Cr_aJDRMnyVx5Nmu_Q5l6m7zldlqc-SD6xUBJbhO1-YLNt0Qr1T9lo4VczFmSXhxEUzgsVqg"}}},"title":"GitHub - lucidrains/DALLE2-pytorch: Implementation of DALL-E 2, OpenAI's updated text-to-image synthesis neural network,  in Pytorch","appPayload":{},"meta":{"title":"GitHub - lucidrains/DALLE2-pytorch: Implementation of DALL-E 2, OpenAI's updated text-to-image synthesis neural network,  in Pytorch"}}</script>
  <div data-target="react-app.reactRoot"><meta name="github-code-view-meta-stats" id="github-code-view-meta-stats" data-hydrostats="publish"/> <!-- --> <a hidden="" id="code-view-repo-link" href="/lucidrains/DALLE2-pytorch" data-discover="true"></a> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><div><div style="--spacing:var(--spacing-none)" class="prc-PageLayout-PageLayoutRoot--KH-d"><div class="prc-PageLayout-PageLayoutWrapper-2BhU2" data-width="full"><div class="prc-PageLayout-PageLayoutContent-BneH9"><div class="prc-PageLayout-ContentWrapper-gR9eG" data-is-hidden-narrow="false"><div class="prc-PageLayout-Content-xWL-A" data-width="full" style="--spacing:var(--spacing-none)"><div class="SharedPageLayout-module__content__IwGAp" data-selector="repos-split-pane-content" tabindex="0"><div style="--spacing:var(--spacing-none)" class="prc-PageLayout-PageLayoutRoot--KH-d container-xl"><div class="prc-PageLayout-PageLayoutWrapper-2BhU2" data-width="full"><header data-hidden="false" class="prc-PageLayout-Header-0of-R tmp-px-3 tmp-px-lg-5" style="--spacing:var(--spacing-none)"><div class="prc-PageLayout-HeaderContent-gdFfN" style="--spacing:var(--spacing-none)"><rails-partial data-partial-name="codeViewRepoRoute.Header" class="RailsPartial-module__d-contents__G5m4w">




<h1 class='sr-only'>lucidrains/DALLE2-pytorch</h1>


<input type="hidden" data-csrf="true" value="/Fcwi5mvi9etIvtdUCrCndvBxHagC1E+0NdAiJCQ9xyDAIFS5BTXrE0qkUAgDYps6EXHAwXopx6mNHX1VpLnag==" />
</rails-partial></div><div class="prc-PageLayout-HorizontalDivider-JLVqp prc-PageLayout-HeaderHorizontalDivider-odAHl" data-variant="none" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div></header><div class="prc-PageLayout-PageLayoutContent-BneH9"><div class="prc-PageLayout-ContentWrapper-gR9eG" data-is-hidden="false"><div class="prc-PageLayout-Content-xWL-A" data-width="large" style="--spacing:var(--spacing-condensed)"><div class="OverviewContent-module__Box__PF75K tmp-pl-lg-3 mt-0"><div class="OverviewHeader-module__Box__cC1RH"></div><div class="OverviewContent-module__Box_1__MPS0U"><div class="OverviewContent-module__Box_2__Di8Pb"><div class="OverviewContent-module__Box_3__wzlJx"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" style="min-width:0" aria-label="main branch" data-testid="anchor-button" data-icv-name="Switch branches/tags" class="prc-Button-ButtonBase-9n-Xk overview-ref-selector width-full RefSelectorAnchoredOverlay-module__RefSelectorOverlayBtn__a3WK3" data-loading="false" data-size="medium" data-variant="default" id="ref-picker-repos-header-ref-selector"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayContainer__yaf4p"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayHeader__XtXRG"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="ref-selector-button-text-container RefSelectorAnchoredOverlay-module__RefSelectorBtnTextContainer__Di3rk"><span class="RefSelectorAnchoredOverlay-module__RefSelectorText__w_fmP"> <!-- -->main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-testid="ref-selector-hotkey-button" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="OverviewContent-module__Box_4__qf73o"><a type="button" href="/lucidrains/DALLE2-pytorch/branches" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button___Uotu" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Branches</span></span></a><a type="button" href="/lucidrains/DALLE2-pytorch/tags" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button___Uotu" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-tag" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Tags</span></span></a></div><div class="OverviewContent-module__Box_5__Zc3i7"><a type="button" aria-label="Go to Branches page" href="/lucidrains/DALLE2-pytorch/branches" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button_1__vmS6D" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></a><a type="button" aria-label="Go to Tags page" href="/lucidrains/DALLE2-pytorch/tags" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button_1__vmS6D" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible"><svg aria-hidden="true" focusable="false" class="octicon octicon-tag" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path></svg></a></div></div><div class="OverviewContent-module__Box_6__Y_Yb_"><div class="OverviewContent-module__Box_7__JuRXo"><div class="OverviewContent-module__Box_8__UZCZh"><!--$!--><template></template><!--/$--></div><div class="OverviewContent-module__Box_9__bqMPw"><button type="button" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Go to file</span></span></button></div></div><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-size="medium" data-variant="primary" id="_R_3idajal1d_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-code hide-sm" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Code</span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><div class="OverviewContent-module__Box_10__mGSb4"><button data-component="IconButton" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_R_3sidajal1d_" id="_R_4idajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_R_3sidajal1d_">Open more actions menu</span></div></div></div><div class="OverviewContent-module__Box_11__F19kY"><div data-hpc="true"><button hidden="" data-testid="focus-next-element-button" data-hotkey="j"></button><button hidden="" data-testid="focus-previous-element-button" data-hotkey="k"></button><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="folders-and-files">Folders and files</h2><table class="Table-module__Box__HZKiQ" aria-labelledby="folders-and-files"><thead class="DirectoryContent-module__OverviewHeaderRow__hOrKy Table-module__Box_1__VacXC"><tr class="Table-module__Box_2__PBp9s"><th colSpan="2" class="DirectoryContent-module__Box__iC_5e"><span class="text-bold">Name</span></th><th colSpan="1" class="DirectoryContent-module__Box_1__fuSBO"><span class="text-bold">Name</span></th><th class="hide-sm"><div class="width-fit prc-Truncate-Truncate-2G1eo" data-inline="true" title="Last commit message" style="--truncate-max-width:125px"><span class="text-bold">Last commit message</span></div></th><th colSpan="1" class="DirectoryContent-module__Box_2__Ccrx7"><div class="width-fit prc-Truncate-Truncate-2G1eo" data-inline="true" title="Last commit date" style="--truncate-max-width:125px"><span class="text-bold">Last commit date</span></div></th></tr></thead><tbody><tr class="DirectoryContent-module__Box_3__gl6dE"><td colSpan="3" class="bgColor-muted p-1 rounded-top-2"><div class="LatestCommit-module__Box__B25ZT"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">Latest commit</h2><div style="width:120px" class="Skeleton Skeleton--text" data-testid="loading"> </div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">History</h2><a href="/lucidrains/DALLE2-pytorch/commits/main/" class="prc-Button-ButtonBase-9n-Xk d-none d-lg-flex LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="fgColor-default">602 Commits</span></span></span></a><div class="d-sm-none"></div><div class="d-flex d-lg-none"><a aria-label="View commit history for this file." href="/lucidrains/DALLE2-pytorch/commits/main/" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby="_R_9d9kcdajal1d_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" role="tooltip" aria-hidden="true" id="_R_9d9kcdajal1d_">602 Commits</span></div></div></div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-0"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".github" aria-label=".github, (Directory)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/tree/main/.github" data-discover="true">.github</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".github" aria-label=".github, (Directory)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/tree/main/.github" data-discover="true">.github</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-1"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="configs" aria-label="configs, (Directory)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/tree/main/configs" data-discover="true">configs</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="configs" aria-label="configs, (Directory)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/tree/main/configs" data-discover="true">configs</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-2"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="dalle2_pytorch" aria-label="dalle2_pytorch, (Directory)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/tree/main/dalle2_pytorch" data-discover="true">dalle2_pytorch</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="dalle2_pytorch" aria-label="dalle2_pytorch, (Directory)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/tree/main/dalle2_pytorch" data-discover="true">dalle2_pytorch</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-3"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="samples" aria-label="samples, (Directory)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/tree/main/samples" data-discover="true">samples</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="samples" aria-label="samples, (Directory)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/tree/main/samples" data-discover="true">samples</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-4"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="test_data" aria-label="test_data, (Directory)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/tree/main/test_data" data-discover="true">test_data</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="test_data" aria-label="test_data, (Directory)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/tree/main/test_data" data-discover="true">test_data</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-5"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".gitignore" aria-label=".gitignore, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/.gitignore" data-discover="true">.gitignore</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".gitignore" aria-label=".gitignore, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/.gitignore" data-discover="true">.gitignore</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-6"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="LICENSE" aria-label="LICENSE, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/LICENSE" data-discover="true">LICENSE</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="LICENSE" aria-label="LICENSE, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/LICENSE" data-discover="true">LICENSE</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-7"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="MANIFEST.in" aria-label="MANIFEST.in, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/MANIFEST.in" data-discover="true">MANIFEST.in</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="MANIFEST.in" aria-label="MANIFEST.in, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/MANIFEST.in" data-discover="true">MANIFEST.in</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-8"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="Makefile" aria-label="Makefile, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/Makefile" data-discover="true">Makefile</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="Makefile" aria-label="Makefile, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/Makefile" data-discover="true">Makefile</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-9"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="README.md" aria-label="README.md, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/README.md" data-discover="true">README.md</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="README.md" aria-label="README.md, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/README.md" data-discover="true">README.md</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-10"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="dalle2.png" aria-label="dalle2.png, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/dalle2.png" data-discover="true">dalle2.png</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="dalle2.png" aria-label="dalle2.png, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/dalle2.png" data-discover="true">dalle2.png</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-11"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="prior.md" aria-label="prior.md, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/prior.md" data-discover="true">prior.md</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="prior.md" aria-label="prior.md, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/prior.md" data-discover="true">prior.md</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-12"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="setup.py" aria-label="setup.py, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/setup.py" data-discover="true">setup.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="setup.py" aria-label="setup.py, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/setup.py" data-discover="true">setup.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-13"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="train_decoder.py" aria-label="train_decoder.py, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/train_decoder.py" data-discover="true">train_decoder.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="train_decoder.py" aria-label="train_decoder.py, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/train_decoder.py" data-discover="true">train_decoder.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-14"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="train_diffusion_prior.py" aria-label="train_diffusion_prior.py, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/train_diffusion_prior.py" data-discover="true">train_diffusion_prior.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="train_diffusion_prior.py" aria-label="train_diffusion_prior.py, (File)" class="Link--primary" href="/lucidrains/DALLE2-pytorch/blob/main/train_diffusion_prior.py" data-discover="true">train_diffusion_prior.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="react-directory-commit-age"><div class="Skeleton Skeleton--text"> </div></div></td></tr><tr class="show-for-mobile DirectoryContent-module__Box_4__RhIsE" data-testid="view-all-files-row"><td colSpan="3" class="DirectoryContent-module__Box_5__GaE8N"><div><button class="prc-Link-Link-9ZwDx">View all files</button></div></td></tr></tbody></table></div><div class="OverviewRepoFiles-module__Box_1__OXeac"><div class="OverviewRepoFiles-module__Box_2__zsLGk"><div itemScope="" itemType="https://schema.org/abstract" class="OverviewRepoFiles-module__Box_3__bBU1C"><h2 class="prc-src-InternalVisuallyHidden-2YaI6">Repository files navigation</h2><nav class="prc-components-UnderlineWrapper-eT-Yj OverviewRepoFiles-module__UnderlineNav__QbWWv" aria-label="Repository files" data-variant="inset" data-overflow-measured="false"><ul class="prc-components-UnderlineItemList-xKlKC" role="list"><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="#" aria-current="page" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-book" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path></svg></span><span data-component="text" data-content="README">README</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="#" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-law" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8.75.75V2h.985c.304 0 .603.08.867.231l1.29.736c.038.022.08.033.124.033h2.234a.75.75 0 0 1 0 1.5h-.427l2.111 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.006.005-.01.01-.045.04c-.21.176-.441.327-.686.45C14.556 10.78 13.88 11 13 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L12.178 4.5h-.162c-.305 0-.604-.079-.868-.231l-1.29-.736a.245.245 0 0 0-.124-.033H8.75V13h2.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1 0-1.5h2.5V3.5h-.984a.245.245 0 0 0-.124.033l-1.289.737c-.265.15-.564.23-.869.23h-.162l2.112 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.016.015-.045.04c-.21.176-.441.327-.686.45C4.556 10.78 3.88 11 3 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L2.178 4.5H1.75a.75.75 0 0 1 0-1.5h2.234a.249.249 0 0 0 .125-.033l1.288-.737c.265-.15.564-.23.869-.23h.984V.75a.75.75 0 0 1 1.5 0Zm2.945 8.477c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327Zm-10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327Z"></path></svg></span><span data-component="text" data-content="MIT license">MIT license</span></a></li></ul></nav><button type="button" aria-label="Outline" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk OverviewRepoFiles-module__ActionMenu_Button__OKDYV" data-loading="false" data-size="medium" data-variant="invisible" id="_R_dkdajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-list-unordered" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg></button></div><div class="js-snippet-clipboard-copy-unpositioned DirectoryRichtextContent-module__SharedMarkdownContent__hHXUL" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><p dir="auto"><a target="_blank" rel="noopener noreferrer" href="/lucidrains/DALLE2-pytorch/blob/main/dalle2.png"><img src="/lucidrains/DALLE2-pytorch/raw/main/dalle2.png" width="450px" style="max-width: 100%;"></a></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">DALL-E 2 - Pytorch</h2><a id="user-content-dall-e-2---pytorch" class="anchor" aria-label="Permalink: DALL-E 2 - Pytorch" href="#dall-e-2---pytorch"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Implementation of <a href="https://openai.com/dall-e-2/" rel="nofollow">DALL-E 2</a>, OpenAI's updated text-to-image synthesis neural network, in Pytorch.</p>
<p dir="auto"><a href="https://youtu.be/RJwPN4qNi_Y?t=555" rel="nofollow">Yannic Kilcher summary</a> | <a href="https://www.youtube.com/watch?v=F1X4fHzF4mQ" rel="nofollow">AssemblyAI explainer</a></p>
<p dir="auto">The main novelty seems to be an extra layer of indirection with the prior network (whether it is an autoregressive transformer or a diffusion network), which predicts an image embedding based on the text embedding from CLIP. Specifically, this repository will only build out the diffusion prior network, as it is the best performing variant (but which incidentally involves a causal transformer as the denoising network 😂)</p>
<p dir="auto">This model is SOTA for text-to-image for now.</p>
<p dir="auto">Please join <a href="https://discord.gg/xBPBXfcFHd" rel="nofollow"><img alt="Join us on Discord" src="https://camo.githubusercontent.com/6df2255d075e0356a86a3db06dda295fda5ee305948a6eb9f76786703c110b1e/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3832333831333135393539323030313533373f636f6c6f723d353836354632266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/discord/823813159592001537?color=5865F2&amp;logo=discord&amp;logoColor=white" style="max-width: 100%;"></a> if you are interested in helping out with the replication with the <a href="https://laion.ai/" rel="nofollow">LAION</a> community | <a href="https://www.youtube.com/watch?v=AIOE1l1W0Tw" rel="nofollow">Yannic Interview</a></p>
<p dir="auto">As of 5/23/22, it is no longer SOTA. SOTA will be <a href="https://github.com/lucidrains/imagen-pytorch">here</a>. Jax versions as well as text-to-video project will be shifted towards the Imagen architecture, as it is way simpler.</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Status</h2><a id="user-content-status" class="anchor" aria-label="Permalink: Status" href="#status"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li>
<p dir="auto">A research group has used the code in this repository to train a functional diffusion prior for their CLIP generations. Will share their work once they release their preprint. This, and <a href="https://github.com/crowsonkb">Katherine's</a> own experiments, validate OpenAI's finding that the extra prior increases variety of generations.</p>
</li>
<li>
<p dir="auto">Decoder is now verified working for unconditional generation on my experimental setup for Oxford flowers. 2 researchers have also confirmed Decoder is working for them.</p>
</li>
</ul>
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="/lucidrains/DALLE2-pytorch/blob/main/samples/oxford.png"><img src="/lucidrains/DALLE2-pytorch/raw/main/samples/oxford.png" width="450px" style="max-width: 100%;"></a></p>
<p dir="auto"><em>ongoing at 21k steps</em></p>
<ul dir="auto">
<li>
<p dir="auto"><a href="https://twitter.com/Buntworthy/status/1529475416775434240?t=0GEge3Kr9I36cjcUVCQUTg" rel="nofollow">Justin Pinkney</a> successfully trained the diffusion prior in the repository for his CLIP to Stylegan2 text-to-image application</p>
</li>
<li>
<p dir="auto"><a href="https://github.com/rom1504">Romain</a> has scaled up training to 800 GPUs with the available scripts without any issues</p>
</li>
</ul>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Pre-Trained Models</h2><a id="user-content-pre-trained-models" class="anchor" aria-label="Permalink: Pre-Trained Models" href="#pre-trained-models"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li>LAION is training prior models. Checkpoints are available on <a href="https://huggingface.co/zenglishuci/conditioned-prior" rel="nofollow">🤗huggingface</a> and the training statistics are available on <a href="https://wandb.ai/nousr_laion/conditioned-prior/reports/LAION-DALLE2-PyTorch-Prior--VmlldzoyMDI2OTIx" rel="nofollow">🐝WANDB</a>.</li>
<li>Decoder - <a href="https://wandb.ai/veldrovive/dalle2_train_decoder/runs/jkrtg0so?workspace=user-veldrovive" rel="nofollow">In-progress test run</a> 🚧</li>
<li>Decoder - <a href="https://wandb.ai/veldrovive/dalle2_train_decoder/runs/3d5rytsa?workspace=" rel="nofollow">Another test run with sparse attention</a></li>
<li>DALL-E 2 🚧 - <a href="https://github.com/LAION-AI/dalle2-laion">DALL-E 2 Laion repository</a></li>
</ul>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Appreciation</h2><a id="user-content-appreciation" class="anchor" aria-label="Permalink: Appreciation" href="#appreciation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">This library would not have gotten to this working state without the help of</p>
<ul dir="auto">
<li><a href="https://github.com/nousr">Zion</a> for the distributed training code for the diffusion prior</li>
<li><a href="https://github.com/Veldrovive">Aidan</a> for the distributed training code for the decoder as well as the dataloaders</li>
<li><a href="https://github.com/krish240574">Kumar</a> for working on the initial diffusion training script</li>
<li><a href="https://github.com/rom1504">Romain</a> for the pull request reviews and project management</li>
<li><a href="https://github.com/Ciaohe">He Cao</a> and <a href="https://github.com/xiankgx">xiankgx</a> for the Q&amp;A and for identifying of critical bugs</li>
<li><a href="https://github.com/marunine">Marunine</a> for identifying issues with resizing of the low resolution conditioner, when training the upsampler, in addition to various other bug fixes</li>
<li><a href="https://github.com/malumadev">MalumaDev</a> for proposing the use of pixel shuffle upsampler for fixing checkboard artifacts</li>
<li><a href="https://github.com/crowsonkb">Katherine</a> for her advice</li>
<li><a href="https://stability.ai/" rel="nofollow">Stability AI</a> for the generous sponsorship</li>
<li><a href="https://huggingface.co" rel="nofollow">🤗 Huggingface</a> and in particular <a href="https://github.com/sgugger">Sylvain</a> for the <a href="https://github.com/huggingface/accelerate">Accelerate</a> library</li>
<li><a href="https://github.com/arogozhnikov">Alex</a> for <a href="https://github.com/arogozhnikov/einops">einops</a>, indispensable tool for tensor manipulation</li>
</ul>
<p dir="auto">... and many others. Thank you! 🙏</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Install</h2><a id="user-content-install" class="anchor" aria-label="Permalink: Install" href="#install"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="$ pip install dalle2-pytorch"><pre>$ pip install dalle2-pytorch</pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Usage</h2><a id="user-content-usage" class="anchor" aria-label="Permalink: Usage" href="#usage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">To train DALLE-2 is a 3 step process, with the training of CLIP being the most important</p>
<p dir="auto">To train CLIP, you can either use <a href="https://github.com/lucidrains/x-clip">x-clip</a> package, or join the LAION discord, where a lot of replication efforts are already <a href="https://github.com/mlfoundations/open_clip">underway</a>.</p>
<p dir="auto">This repository will demonstrate integration with <code>x-clip</code> for starters</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import CLIP

clip = CLIP(
    dim_text = 512,
    dim_image = 512,
    dim_latent = 512,
    num_text_tokens = 49408,
    text_enc_depth = 1,
    text_seq_len = 256,
    text_heads = 8,
    visual_enc_depth = 1,
    visual_image_size = 256,
    visual_patch_size = 32,
    visual_heads = 8,
    use_all_token_embeds = True,            # whether to use fine-grained contrastive learning (FILIP)
    decoupled_contrastive_learning = True,  # use decoupled contrastive learning (DCL) objective function, removing positive pairs from the denominator of the InfoNCE loss (CLOOB + DCL)
    extra_latent_projection = True,         # whether to use separate projections for text-to-image vs image-to-text comparisons (CLOOB)
    use_visual_ssl = True,                  # whether to do self supervised learning on images
    visual_ssl_type = 'simclr',             # can be either 'simclr' or 'simsiam', depending on using DeCLIP or SLIP
    use_mlm = False,                        # use masked language learning (MLM) on text (DeCLIP)
    text_ssl_loss_weight = 0.05,            # weight for text MLM loss
    image_ssl_loss_weight = 0.05            # weight for image self-supervised learning loss
).cuda()

# mock data

text = torch.randint(0, 49408, (4, 256)).cuda()
images = torch.randn(4, 3, 256, 256).cuda()

# train

loss = clip(
    text,
    images,
    return_loss = True              # needs to be set to True to return contrastive loss
)

loss.backward()

# do the above with as many texts and images as possible in a loop"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-c1">CLIP</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">CLIP</span>(
    <span class="pl-s1">dim_text</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_image</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_latent</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">num_text_tokens</span> <span class="pl-c1">=</span> <span class="pl-c1">49408</span>,
    <span class="pl-s1">text_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>,
    <span class="pl-s1">text_seq_len</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">text_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">visual_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>,
    <span class="pl-s1">visual_image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">visual_patch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">visual_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">use_all_token_embeds</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>,            <span class="pl-c"># whether to use fine-grained contrastive learning (FILIP)</span>
    <span class="pl-s1">decoupled_contrastive_learning</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>,  <span class="pl-c"># use decoupled contrastive learning (DCL) objective function, removing positive pairs from the denominator of the InfoNCE loss (CLOOB + DCL)</span>
    <span class="pl-s1">extra_latent_projection</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>,         <span class="pl-c"># whether to use separate projections for text-to-image vs image-to-text comparisons (CLOOB)</span>
    <span class="pl-s1">use_visual_ssl</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>,                  <span class="pl-c"># whether to do self supervised learning on images</span>
    <span class="pl-s1">visual_ssl_type</span> <span class="pl-c1">=</span> <span class="pl-s">'simclr'</span>,             <span class="pl-c"># can be either 'simclr' or 'simsiam', depending on using DeCLIP or SLIP</span>
    <span class="pl-s1">use_mlm</span> <span class="pl-c1">=</span> <span class="pl-c1">False</span>,                        <span class="pl-c"># use masked language learning (MLM) on text (DeCLIP)</span>
    <span class="pl-s1">text_ssl_loss_weight</span> <span class="pl-c1">=</span> <span class="pl-c1">0.05</span>,            <span class="pl-c"># weight for text MLM loss</span>
    <span class="pl-s1">image_ssl_loss_weight</span> <span class="pl-c1">=</span> <span class="pl-c1">0.05</span>            <span class="pl-c"># weight for image self-supervised learning loss</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock data</span>

<span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randint</span>(<span class="pl-c1">0</span>, <span class="pl-c1">49408</span>, (<span class="pl-c1">4</span>, <span class="pl-c1">256</span>)).<span class="pl-c1">cuda</span>()
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># train</span>

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">clip</span>(
    <span class="pl-s1">text</span>,
    <span class="pl-s1">images</span>,
    <span class="pl-s1">return_loss</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>              <span class="pl-c"># needs to be set to True to return contrastive loss</span>
)

<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do the above with as many texts and images as possible in a loop</span></pre></div>
<p dir="auto">Then, you will need to train the decoder, which learns to generate images based on the image embedding coming from the trained CLIP above</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import Unet, Decoder, CLIP

# trained clip from step 1

clip = CLIP(
    dim_text = 512,
    dim_image = 512,
    dim_latent = 512,
    num_text_tokens = 49408,
    text_enc_depth = 1,
    text_seq_len = 256,
    text_heads = 8,
    visual_enc_depth = 1,
    visual_image_size = 256,
    visual_patch_size = 32,
    visual_heads = 8
).cuda()

# unet for the decoder

unet = Unet(
    dim = 128,
    image_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    dim_mults=(1, 2, 4, 8)
).cuda()

# decoder, which contains the unet and clip

decoder = Decoder(
    unet = unet,
    clip = clip,
    timesteps = 100,
    image_cond_drop_prob = 0.1,
    text_cond_drop_prob = 0.5
).cuda()

# mock images (get a lot of this)

images = torch.randn(4, 3, 256, 256).cuda()

# feed images into decoder

loss = decoder(images)
loss.backward()

# do the above for many many many many steps
# then it will learn to generate images based on the CLIP image embeddings"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">Unet</span>, <span class="pl-v">Decoder</span>, <span class="pl-c1">CLIP</span>

<span class="pl-c"># trained clip from step 1</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">CLIP</span>(
    <span class="pl-s1">dim_text</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_image</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_latent</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">num_text_tokens</span> <span class="pl-c1">=</span> <span class="pl-c1">49408</span>,
    <span class="pl-s1">text_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>,
    <span class="pl-s1">text_seq_len</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">text_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">visual_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>,
    <span class="pl-s1">visual_image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">visual_patch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">visual_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># unet for the decoder</span>

<span class="pl-s1">unet</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span><span class="pl-c1">=</span>(<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>)
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># decoder, which contains the unet and clip</span>

<span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-en">Decoder</span>(
    <span class="pl-s1">unet</span> <span class="pl-c1">=</span> <span class="pl-s1">unet</span>,
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">100</span>,
    <span class="pl-s1">image_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.1</span>,
    <span class="pl-s1">text_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.5</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock images (get a lot of this)</span>

<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># feed images into decoder</span>

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder</span>(<span class="pl-s1">images</span>)
<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do the above for many many many many steps</span>
<span class="pl-c"># then it will learn to generate images based on the CLIP image embeddings</span></pre></div>
<p dir="auto">Finally, the main contribution of the paper. The repository offers the diffusion prior network. It takes the CLIP text embeddings and tries to generate the CLIP image embeddings. Again, you will need the trained CLIP from the first step</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import DiffusionPriorNetwork, DiffusionPrior, CLIP

# get trained CLIP from step one

clip = CLIP(
    dim_text = 512,
    dim_image = 512,
    dim_latent = 512,
    num_text_tokens = 49408,
    text_enc_depth = 6,
    text_seq_len = 256,
    text_heads = 8,
    visual_enc_depth = 6,
    visual_image_size = 256,
    visual_patch_size = 32,
    visual_heads = 8,
).cuda()

# setup prior network, which contains an autoregressive transformer

prior_network = DiffusionPriorNetwork(
    dim = 512,
    depth = 6,
    dim_head = 64,
    heads = 8
).cuda()

# diffusion prior network, which contains the CLIP and network (with transformer) above

diffusion_prior = DiffusionPrior(
    net = prior_network,
    clip = clip,
    timesteps = 100,
    cond_drop_prob = 0.2
).cuda()

# mock data

text = torch.randint(0, 49408, (4, 256)).cuda()
images = torch.randn(4, 3, 256, 256).cuda()

# feed text and images into diffusion prior network

loss = diffusion_prior(text, images)
loss.backward()

# do the above for many many many steps
# now the diffusion prior can generate image embeddings from the text embeddings"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">DiffusionPriorNetwork</span>, <span class="pl-v">DiffusionPrior</span>, <span class="pl-c1">CLIP</span>

<span class="pl-c"># get trained CLIP from step one</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">CLIP</span>(
    <span class="pl-s1">dim_text</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_image</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_latent</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">num_text_tokens</span> <span class="pl-c1">=</span> <span class="pl-c1">49408</span>,
    <span class="pl-s1">text_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">text_seq_len</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">text_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">visual_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">visual_image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">visual_patch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">visual_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># setup prior network, which contains an autoregressive transformer</span>

<span class="pl-s1">prior_network</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPriorNetwork</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">dim_head</span> <span class="pl-c1">=</span> <span class="pl-c1">64</span>,
    <span class="pl-s1">heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># diffusion prior network, which contains the CLIP and network (with transformer) above</span>

<span class="pl-s1">diffusion_prior</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPrior</span>(
    <span class="pl-s1">net</span> <span class="pl-c1">=</span> <span class="pl-s1">prior_network</span>,
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">100</span>,
    <span class="pl-s1">cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.2</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock data</span>

<span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randint</span>(<span class="pl-c1">0</span>, <span class="pl-c1">49408</span>, (<span class="pl-c1">4</span>, <span class="pl-c1">256</span>)).<span class="pl-c1">cuda</span>()
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># feed text and images into diffusion prior network</span>

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">diffusion_prior</span>(<span class="pl-s1">text</span>, <span class="pl-s1">images</span>)
<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do the above for many many many steps</span>
<span class="pl-c"># now the diffusion prior can generate image embeddings from the text embeddings</span></pre></div>
<p dir="auto">In the paper, they actually used a <a href="https://cascaded-diffusion.github.io/" rel="nofollow">recently discovered technique</a>, from <a href="http://www.jonathanho.me/" rel="nofollow">Jonathan Ho</a> himself (original author of DDPMs, the core technique used in DALL-E v2) for high resolution image synthesis.</p>
<p dir="auto">This can easily be used within this framework as so</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import Unet, Decoder, CLIP

# trained clip from step 1

clip = CLIP(
    dim_text = 512,
    dim_image = 512,
    dim_latent = 512,
    num_text_tokens = 49408,
    text_enc_depth = 6,
    text_seq_len = 256,
    text_heads = 8,
    visual_enc_depth = 6,
    visual_image_size = 256,
    visual_patch_size = 32,
    visual_heads = 8
).cuda()

# 2 unets for the decoder (a la cascading DDPM)

unet1 = Unet(
    dim = 32,
    image_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    dim_mults = (1, 2, 4, 8)
).cuda()

unet2 = Unet(
    dim = 32,
    image_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    dim_mults = (1, 2, 4, 8, 16)
).cuda()

# decoder, which contains the unet(s) and clip

decoder = Decoder(
    clip = clip,
    unet = (unet1, unet2),            # insert both unets in order of low resolution to highest resolution (you can have as many stages as you want here)
    image_sizes = (256, 512),         # resolutions, 256 for first unet, 512 for second. these must be unique and in ascending order (matches with the unets passed in)
    timesteps = 1000,
    image_cond_drop_prob = 0.1,
    text_cond_drop_prob = 0.5
).cuda()

# mock images (get a lot of this)

images = torch.randn(4, 3, 512, 512).cuda()

# feed images into decoder, specifying which unet you want to train
# each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme

loss = decoder(images, unet_number = 1)
loss.backward()

loss = decoder(images, unet_number = 2)
loss.backward()

# do the above for many steps for both unets"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">Unet</span>, <span class="pl-v">Decoder</span>, <span class="pl-c1">CLIP</span>

<span class="pl-c"># trained clip from step 1</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">CLIP</span>(
    <span class="pl-s1">dim_text</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_image</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_latent</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">num_text_tokens</span> <span class="pl-c1">=</span> <span class="pl-c1">49408</span>,
    <span class="pl-s1">text_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">text_seq_len</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">text_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">visual_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">visual_image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">visual_patch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">visual_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># 2 unets for the decoder (a la cascading DDPM)</span>

<span class="pl-s1">unet1</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>)
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">unet2</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>, <span class="pl-c1">16</span>)
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># decoder, which contains the unet(s) and clip</span>

<span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-en">Decoder</span>(
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">unet</span> <span class="pl-c1">=</span> (<span class="pl-s1">unet1</span>, <span class="pl-s1">unet2</span>),            <span class="pl-c"># insert both unets in order of low resolution to highest resolution (you can have as many stages as you want here)</span>
    <span class="pl-s1">image_sizes</span> <span class="pl-c1">=</span> (<span class="pl-c1">256</span>, <span class="pl-c1">512</span>),         <span class="pl-c"># resolutions, 256 for first unet, 512 for second. these must be unique and in ascending order (matches with the unets passed in)</span>
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span>,
    <span class="pl-s1">image_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.1</span>,
    <span class="pl-s1">text_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.5</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock images (get a lot of this)</span>

<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">3</span>, <span class="pl-c1">512</span>, <span class="pl-c1">512</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># feed images into decoder, specifying which unet you want to train</span>
<span class="pl-c"># each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme</span>

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder</span>(<span class="pl-s1">images</span>, <span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>)
<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder</span>(<span class="pl-s1">images</span>, <span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-c1">2</span>)
<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do the above for many steps for both unets</span></pre></div>
<p dir="auto">Finally, to generate the DALL-E2 images from text. Insert the trained <code>DiffusionPrior</code> as well as the <code>Decoder</code> (which wraps <code>CLIP</code>, the causal transformer, and unet(s))</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="from dalle2_pytorch import DALLE2

dalle2 = DALLE2(
    prior = diffusion_prior,
    decoder = decoder
)

# send the text as a string if you want to use the simple tokenizer from DALLE v1
# or you can do it as token ids, if you have your own tokenizer

texts = ['glistening morning dew on a flower petal']
images = dalle2(texts) # (1, 3, 256, 256)"><pre><span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">DALLE2</span>

<span class="pl-s1">dalle2</span> <span class="pl-c1">=</span> <span class="pl-en">DALLE2</span>(
    <span class="pl-s1">prior</span> <span class="pl-c1">=</span> <span class="pl-s1">diffusion_prior</span>,
    <span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-s1">decoder</span>
)

<span class="pl-c"># send the text as a string if you want to use the simple tokenizer from DALLE v1</span>
<span class="pl-c"># or you can do it as token ids, if you have your own tokenizer</span>

<span class="pl-s1">texts</span> <span class="pl-c1">=</span> [<span class="pl-s">'glistening morning dew on a flower petal'</span>]
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-en">dalle2</span>(<span class="pl-s1">texts</span>) <span class="pl-c"># (1, 3, 256, 256)</span></pre></div>
<p dir="auto">That's it!</p>
<p dir="auto">Let's see the whole script below</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import DALLE2, DiffusionPriorNetwork, DiffusionPrior, Unet, Decoder, CLIP

clip = CLIP(
    dim_text = 512,
    dim_image = 512,
    dim_latent = 512,
    num_text_tokens = 49408,
    text_enc_depth = 6,
    text_seq_len = 256,
    text_heads = 8,
    visual_enc_depth = 6,
    visual_image_size = 256,
    visual_patch_size = 32,
    visual_heads = 8
).cuda()

# mock data

text = torch.randint(0, 49408, (4, 256)).cuda()
images = torch.randn(4, 3, 256, 256).cuda()

# train

loss = clip(
    text,
    images,
    return_loss = True
)

loss.backward()

# do above for many steps ...

# prior networks (with transformer)

prior_network = DiffusionPriorNetwork(
    dim = 512,
    depth = 6,
    dim_head = 64,
    heads = 8
).cuda()

diffusion_prior = DiffusionPrior(
    net = prior_network,
    clip = clip,
    timesteps = 1000,
    sample_timesteps = 64,
    cond_drop_prob = 0.2
).cuda()

loss = diffusion_prior(text, images)
loss.backward()

# do above for many steps ...

# decoder (with unet)

unet1 = Unet(
    dim = 128,
    image_embed_dim = 512,
    text_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    dim_mults=(1, 2, 4, 8),
    cond_on_text_encodings = True    # set to True for any unets that need to be conditioned on text encodings
).cuda()

unet2 = Unet(
    dim = 16,
    image_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    dim_mults = (1, 2, 4, 8, 16)
).cuda()

decoder = Decoder(
    unet = (unet1, unet2),
    image_sizes = (128, 256),
    clip = clip,
    timesteps = 100,
    image_cond_drop_prob = 0.1,
    text_cond_drop_prob = 0.5
).cuda()

for unet_number in (1, 2):
    loss = decoder(images, text = text, unet_number = unet_number) # this can optionally be decoder(images, text) if you wish to condition on the text encodings as well, though it was hinted in the paper it didn't do much
    loss.backward()

# do above for many steps

dalle2 = DALLE2(
    prior = diffusion_prior,
    decoder = decoder
)

images = dalle2(
    ['cute puppy chasing after a squirrel'],
    cond_scale = 2. # classifier free guidance strength (&gt; 1 would strengthen the condition)
)

# save your image (in this example, of size 256x256)"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">DALLE2</span>, <span class="pl-v">DiffusionPriorNetwork</span>, <span class="pl-v">DiffusionPrior</span>, <span class="pl-v">Unet</span>, <span class="pl-v">Decoder</span>, <span class="pl-c1">CLIP</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">CLIP</span>(
    <span class="pl-s1">dim_text</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_image</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_latent</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">num_text_tokens</span> <span class="pl-c1">=</span> <span class="pl-c1">49408</span>,
    <span class="pl-s1">text_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">text_seq_len</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">text_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">visual_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">visual_image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">visual_patch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">visual_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock data</span>

<span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randint</span>(<span class="pl-c1">0</span>, <span class="pl-c1">49408</span>, (<span class="pl-c1">4</span>, <span class="pl-c1">256</span>)).<span class="pl-c1">cuda</span>()
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># train</span>

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">clip</span>(
    <span class="pl-s1">text</span>,
    <span class="pl-s1">images</span>,
    <span class="pl-s1">return_loss</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>
)

<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do above for many steps ...</span>

<span class="pl-c"># prior networks (with transformer)</span>

<span class="pl-s1">prior_network</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPriorNetwork</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">dim_head</span> <span class="pl-c1">=</span> <span class="pl-c1">64</span>,
    <span class="pl-s1">heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">diffusion_prior</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPrior</span>(
    <span class="pl-s1">net</span> <span class="pl-c1">=</span> <span class="pl-s1">prior_network</span>,
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span>,
    <span class="pl-s1">sample_timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">64</span>,
    <span class="pl-s1">cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.2</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">diffusion_prior</span>(<span class="pl-s1">text</span>, <span class="pl-s1">images</span>)
<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do above for many steps ...</span>

<span class="pl-c"># decoder (with unet)</span>

<span class="pl-s1">unet1</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">text_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span><span class="pl-c1">=</span>(<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>),
    <span class="pl-s1">cond_on_text_encodings</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>    <span class="pl-c"># set to True for any unets that need to be conditioned on text encodings</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">unet2</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">16</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>, <span class="pl-c1">16</span>)
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-en">Decoder</span>(
    <span class="pl-s1">unet</span> <span class="pl-c1">=</span> (<span class="pl-s1">unet1</span>, <span class="pl-s1">unet2</span>),
    <span class="pl-s1">image_sizes</span> <span class="pl-c1">=</span> (<span class="pl-c1">128</span>, <span class="pl-c1">256</span>),
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">100</span>,
    <span class="pl-s1">image_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.1</span>,
    <span class="pl-s1">text_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.5</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-k">for</span> <span class="pl-s1">unet_number</span> <span class="pl-c1">in</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>):
    <span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder</span>(<span class="pl-s1">images</span>, <span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">text</span>, <span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-s1">unet_number</span>) <span class="pl-c"># this can optionally be decoder(images, text) if you wish to condition on the text encodings as well, though it was hinted in the paper it didn't do much</span>
    <span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do above for many steps</span>

<span class="pl-s1">dalle2</span> <span class="pl-c1">=</span> <span class="pl-en">DALLE2</span>(
    <span class="pl-s1">prior</span> <span class="pl-c1">=</span> <span class="pl-s1">diffusion_prior</span>,
    <span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-s1">decoder</span>
)

<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-en">dalle2</span>(
    [<span class="pl-s">'cute puppy chasing after a squirrel'</span>],
    <span class="pl-s1">cond_scale</span> <span class="pl-c1">=</span> <span class="pl-c1">2.</span> <span class="pl-c"># classifier free guidance strength (&gt; 1 would strengthen the condition)</span>
)

<span class="pl-c"># save your image (in this example, of size 256x256)</span></pre></div>
<p dir="auto">Everything in this readme should run without error</p>
<p dir="auto">You can also train the decoder on images of greater than the size (say 512x512) at which CLIP was trained (256x256). The images will be resized to CLIP image resolution for the image embeddings</p>
<p dir="auto">For the layperson, no worries, training will all be automated into a CLI tool, at least for small scale training.</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Training on Preprocessed CLIP Embeddings</h2><a id="user-content-training-on-preprocessed-clip-embeddings" class="anchor" aria-label="Permalink: Training on Preprocessed CLIP Embeddings" href="#training-on-preprocessed-clip-embeddings"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">It is likely, when scaling up, that you would first preprocess your images and text into corresponding embeddings before training the prior network. You can do so easily by simply passing in <code>image_embed</code>, <code>text_embed</code>, and optionally <code>text_encodings</code></p>
<p dir="auto">Working example below</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import DiffusionPriorNetwork, DiffusionPrior, CLIP

# get trained CLIP from step one

clip = CLIP(
    dim_text = 512,
    dim_image = 512,
    dim_latent = 512,
    num_text_tokens = 49408,
    text_enc_depth = 6,
    text_seq_len = 256,
    text_heads = 8,
    visual_enc_depth = 6,
    visual_image_size = 256,
    visual_patch_size = 32,
    visual_heads = 8,
).cuda()

# setup prior network, which contains an autoregressive transformer

prior_network = DiffusionPriorNetwork(
    dim = 512,
    depth = 6,
    dim_head = 64,
    heads = 8
).cuda()

# diffusion prior network, which contains the CLIP and network (with transformer) above

diffusion_prior = DiffusionPrior(
    net = prior_network,
    clip = clip,
    timesteps = 100,
    cond_drop_prob = 0.2,
    condition_on_text_encodings = False  # this probably should be true, but just to get Laion started
).cuda()

# mock data

text = torch.randint(0, 49408, (4, 256)).cuda()
images = torch.randn(4, 3, 256, 256).cuda()

# precompute the text and image embeddings
# here using the diffusion prior class, but could be done with CLIP alone

clip_image_embeds = diffusion_prior.clip.embed_image(images).image_embed
clip_text_embeds = diffusion_prior.clip.embed_text(text).text_embed

# feed text and images into diffusion prior network

loss = diffusion_prior(
    text_embed = clip_text_embeds,
    image_embed = clip_image_embeds
)

loss.backward()

# do the above for many many many steps
# now the diffusion prior can generate image embeddings from the text embeddings"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">DiffusionPriorNetwork</span>, <span class="pl-v">DiffusionPrior</span>, <span class="pl-c1">CLIP</span>

<span class="pl-c"># get trained CLIP from step one</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">CLIP</span>(
    <span class="pl-s1">dim_text</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_image</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_latent</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">num_text_tokens</span> <span class="pl-c1">=</span> <span class="pl-c1">49408</span>,
    <span class="pl-s1">text_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">text_seq_len</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">text_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">visual_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">visual_image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">visual_patch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">visual_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># setup prior network, which contains an autoregressive transformer</span>

<span class="pl-s1">prior_network</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPriorNetwork</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">dim_head</span> <span class="pl-c1">=</span> <span class="pl-c1">64</span>,
    <span class="pl-s1">heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># diffusion prior network, which contains the CLIP and network (with transformer) above</span>

<span class="pl-s1">diffusion_prior</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPrior</span>(
    <span class="pl-s1">net</span> <span class="pl-c1">=</span> <span class="pl-s1">prior_network</span>,
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">100</span>,
    <span class="pl-s1">cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.2</span>,
    <span class="pl-s1">condition_on_text_encodings</span> <span class="pl-c1">=</span> <span class="pl-c1">False</span>  <span class="pl-c"># this probably should be true, but just to get Laion started</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock data</span>

<span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randint</span>(<span class="pl-c1">0</span>, <span class="pl-c1">49408</span>, (<span class="pl-c1">4</span>, <span class="pl-c1">256</span>)).<span class="pl-c1">cuda</span>()
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># precompute the text and image embeddings</span>
<span class="pl-c"># here using the diffusion prior class, but could be done with CLIP alone</span>

<span class="pl-s1">clip_image_embeds</span> <span class="pl-c1">=</span> <span class="pl-s1">diffusion_prior</span>.<span class="pl-c1">clip</span>.<span class="pl-c1">embed_image</span>(<span class="pl-s1">images</span>).<span class="pl-c1">image_embed</span>
<span class="pl-s1">clip_text_embeds</span> <span class="pl-c1">=</span> <span class="pl-s1">diffusion_prior</span>.<span class="pl-c1">clip</span>.<span class="pl-c1">embed_text</span>(<span class="pl-s1">text</span>).<span class="pl-c1">text_embed</span>

<span class="pl-c"># feed text and images into diffusion prior network</span>

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">diffusion_prior</span>(
    <span class="pl-s1">text_embed</span> <span class="pl-c1">=</span> <span class="pl-s1">clip_text_embeds</span>,
    <span class="pl-s1">image_embed</span> <span class="pl-c1">=</span> <span class="pl-s1">clip_image_embeds</span>
)

<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do the above for many many many steps</span>
<span class="pl-c"># now the diffusion prior can generate image embeddings from the text embeddings</span></pre></div>
<p dir="auto">You can also completely go <code>CLIP</code>-less, in which case you will need to pass in the <code>image_embed_dim</code> into the <code>DiffusionPrior</code> on initialization</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import DiffusionPriorNetwork, DiffusionPrior

# setup prior network, which contains an autoregressive transformer

prior_network = DiffusionPriorNetwork(
    dim = 512,
    depth = 6,
    dim_head = 64,
    heads = 8
).cuda()

# diffusion prior network, which contains the CLIP and network (with transformer) above

diffusion_prior = DiffusionPrior(
    net = prior_network,
    image_embed_dim = 512,               # this needs to be set
    timesteps = 100,
    cond_drop_prob = 0.2,
    condition_on_text_encodings = False  # this probably should be true, but just to get Laion started
).cuda()

# mock data

text = torch.randint(0, 49408, (4, 256)).cuda()
images = torch.randn(4, 3, 256, 256).cuda()

# precompute the text and image embeddings
# here using the diffusion prior class, but could be done with CLIP alone

clip_image_embeds = torch.randn(4, 512).cuda()
clip_text_embeds = torch.randn(4, 512).cuda()

# feed text and images into diffusion prior network

loss = diffusion_prior(
    text_embed = clip_text_embeds,
    image_embed = clip_image_embeds
)

loss.backward()

# do the above for many many many steps
# now the diffusion prior can generate image embeddings from the text embeddings"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">DiffusionPriorNetwork</span>, <span class="pl-v">DiffusionPrior</span>

<span class="pl-c"># setup prior network, which contains an autoregressive transformer</span>

<span class="pl-s1">prior_network</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPriorNetwork</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">dim_head</span> <span class="pl-c1">=</span> <span class="pl-c1">64</span>,
    <span class="pl-s1">heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># diffusion prior network, which contains the CLIP and network (with transformer) above</span>

<span class="pl-s1">diffusion_prior</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPrior</span>(
    <span class="pl-s1">net</span> <span class="pl-c1">=</span> <span class="pl-s1">prior_network</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,               <span class="pl-c"># this needs to be set</span>
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">100</span>,
    <span class="pl-s1">cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.2</span>,
    <span class="pl-s1">condition_on_text_encodings</span> <span class="pl-c1">=</span> <span class="pl-c1">False</span>  <span class="pl-c"># this probably should be true, but just to get Laion started</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock data</span>

<span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randint</span>(<span class="pl-c1">0</span>, <span class="pl-c1">49408</span>, (<span class="pl-c1">4</span>, <span class="pl-c1">256</span>)).<span class="pl-c1">cuda</span>()
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># precompute the text and image embeddings</span>
<span class="pl-c"># here using the diffusion prior class, but could be done with CLIP alone</span>

<span class="pl-s1">clip_image_embeds</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">512</span>).<span class="pl-c1">cuda</span>()
<span class="pl-s1">clip_text_embeds</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">512</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># feed text and images into diffusion prior network</span>

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">diffusion_prior</span>(
    <span class="pl-s1">text_embed</span> <span class="pl-c1">=</span> <span class="pl-s1">clip_text_embeds</span>,
    <span class="pl-s1">image_embed</span> <span class="pl-c1">=</span> <span class="pl-s1">clip_image_embeds</span>
)

<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do the above for many many many steps</span>
<span class="pl-c"># now the diffusion prior can generate image embeddings from the text embeddings</span></pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">OpenAI CLIP</h2><a id="user-content-openai-clip" class="anchor" aria-label="Permalink: OpenAI CLIP" href="#openai-clip"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Although there is the possibility they are using an unreleased, more powerful CLIP, you can use one of the released ones, if you do not wish to train your own CLIP from scratch. This will also allow the community to more quickly validate the conclusions of the paper.</p>
<p dir="auto">To use a pretrained OpenAI CLIP, simply import <code>OpenAIClipAdapter</code> and pass it into the <code>DiffusionPrior</code> or <code>Decoder</code> like so</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import DALLE2, DiffusionPriorNetwork, DiffusionPrior, Unet, Decoder, OpenAIClipAdapter

# openai pretrained clip - defaults to ViT-B/32

clip = OpenAIClipAdapter()

# mock data

text = torch.randint(0, 49408, (4, 256)).cuda()
images = torch.randn(4, 3, 256, 256).cuda()

# prior networks (with transformer)

prior_network = DiffusionPriorNetwork(
    dim = 512,
    depth = 6,
    dim_head = 64,
    heads = 8
).cuda()

diffusion_prior = DiffusionPrior(
    net = prior_network,
    clip = clip,
    timesteps = 100,
    cond_drop_prob = 0.2
).cuda()

loss = diffusion_prior(text, images)
loss.backward()

# do above for many steps ...

# decoder (with unet)

unet1 = Unet(
    dim = 128,
    image_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    dim_mults=(1, 2, 4, 8),
    text_embed_dim = 512,
    cond_on_text_encodings = True  # set to True for any unets that need to be conditioned on text encodings (ex. first unet in cascade)
).cuda()

unet2 = Unet(
    dim = 16,
    image_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    dim_mults = (1, 2, 4, 8, 16)
).cuda()

decoder = Decoder(
    unet = (unet1, unet2),
    image_sizes = (128, 256),
    clip = clip,
    timesteps = 1000,
    sample_timesteps = (250, 27),
    image_cond_drop_prob = 0.1,
    text_cond_drop_prob = 0.5
).cuda()

for unet_number in (1, 2):
    loss = decoder(images, text = text, unet_number = unet_number) # this can optionally be decoder(images, text) if you wish to condition on the text encodings as well, though it was hinted in the paper it didn't do much
    loss.backward()

# do above for many steps

dalle2 = DALLE2(
    prior = diffusion_prior,
    decoder = decoder
)

images = dalle2(
    ['a butterfly trying to escape a tornado'],
    cond_scale = 2. # classifier free guidance strength (&gt; 1 would strengthen the condition)
)

# save your image (in this example, of size 256x256)"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">DALLE2</span>, <span class="pl-v">DiffusionPriorNetwork</span>, <span class="pl-v">DiffusionPrior</span>, <span class="pl-v">Unet</span>, <span class="pl-v">Decoder</span>, <span class="pl-v">OpenAIClipAdapter</span>

<span class="pl-c"># openai pretrained clip - defaults to ViT-B/32</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">OpenAIClipAdapter</span>()

<span class="pl-c"># mock data</span>

<span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randint</span>(<span class="pl-c1">0</span>, <span class="pl-c1">49408</span>, (<span class="pl-c1">4</span>, <span class="pl-c1">256</span>)).<span class="pl-c1">cuda</span>()
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># prior networks (with transformer)</span>

<span class="pl-s1">prior_network</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPriorNetwork</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">dim_head</span> <span class="pl-c1">=</span> <span class="pl-c1">64</span>,
    <span class="pl-s1">heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">diffusion_prior</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPrior</span>(
    <span class="pl-s1">net</span> <span class="pl-c1">=</span> <span class="pl-s1">prior_network</span>,
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">100</span>,
    <span class="pl-s1">cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.2</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">diffusion_prior</span>(<span class="pl-s1">text</span>, <span class="pl-s1">images</span>)
<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do above for many steps ...</span>

<span class="pl-c"># decoder (with unet)</span>

<span class="pl-s1">unet1</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span><span class="pl-c1">=</span>(<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>),
    <span class="pl-s1">text_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_on_text_encodings</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>  <span class="pl-c"># set to True for any unets that need to be conditioned on text encodings (ex. first unet in cascade)</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">unet2</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">16</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>, <span class="pl-c1">16</span>)
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-en">Decoder</span>(
    <span class="pl-s1">unet</span> <span class="pl-c1">=</span> (<span class="pl-s1">unet1</span>, <span class="pl-s1">unet2</span>),
    <span class="pl-s1">image_sizes</span> <span class="pl-c1">=</span> (<span class="pl-c1">128</span>, <span class="pl-c1">256</span>),
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span>,
    <span class="pl-s1">sample_timesteps</span> <span class="pl-c1">=</span> (<span class="pl-c1">250</span>, <span class="pl-c1">27</span>),
    <span class="pl-s1">image_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.1</span>,
    <span class="pl-s1">text_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.5</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-k">for</span> <span class="pl-s1">unet_number</span> <span class="pl-c1">in</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>):
    <span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder</span>(<span class="pl-s1">images</span>, <span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">text</span>, <span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-s1">unet_number</span>) <span class="pl-c"># this can optionally be decoder(images, text) if you wish to condition on the text encodings as well, though it was hinted in the paper it didn't do much</span>
    <span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do above for many steps</span>

<span class="pl-s1">dalle2</span> <span class="pl-c1">=</span> <span class="pl-en">DALLE2</span>(
    <span class="pl-s1">prior</span> <span class="pl-c1">=</span> <span class="pl-s1">diffusion_prior</span>,
    <span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-s1">decoder</span>
)

<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-en">dalle2</span>(
    [<span class="pl-s">'a butterfly trying to escape a tornado'</span>],
    <span class="pl-s1">cond_scale</span> <span class="pl-c1">=</span> <span class="pl-c1">2.</span> <span class="pl-c"># classifier free guidance strength (&gt; 1 would strengthen the condition)</span>
)

<span class="pl-c"># save your image (in this example, of size 256x256)</span></pre></div>
<p dir="auto">Alternatively, you can also use <a href="https://github.com/mlfoundations/open_clip">Open Clip</a></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="$ pip install open-clip-torch"><pre>$ pip install open-clip-torch</pre></div>
<p dir="auto">Ex. using the <a href="https://laion.ai/blog/large-openclip/" rel="nofollow">SOTA Open Clip</a> model trained by <a href="https://github.com/rom1504">Romain</a></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="from dalle2_pytorch import OpenClipAdapter

clip = OpenClipAdapter('ViT-H/14')"><pre><span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">OpenClipAdapter</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">OpenClipAdapter</span>(<span class="pl-s">'ViT-H/14'</span>)</pre></div>
<p dir="auto">Now you'll just have to worry about training the Prior and the Decoder!</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Inpainting</h2><a id="user-content-inpainting" class="anchor" aria-label="Permalink: Inpainting" href="#inpainting"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Inpainting is also built into the <code>Decoder</code>. You simply have to pass in the <code>inpaint_image</code> and <code>inpaint_mask</code> (boolean tensor where <code>True</code> indicates which regions of the inpaint image to keep)</p>
<p dir="auto">This repository uses the formulation put forth by <a href="https://arxiv.org/abs/2201.09865" rel="nofollow">Lugmayr et al. in Repaint</a></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import Unet, Decoder, CLIP

# trained clip from step 1

clip = CLIP(
    dim_text = 512,
    dim_image = 512,
    dim_latent = 512,
    num_text_tokens = 49408,
    text_enc_depth = 6,
    text_seq_len = 256,
    text_heads = 8,
    visual_enc_depth = 6,
    visual_image_size = 256,
    visual_patch_size = 32,
    visual_heads = 8
).cuda()

# 2 unets for the decoder (a la cascading DDPM)

unet = Unet(
    dim = 16,
    image_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    dim_mults = (1, 1, 1, 1)
).cuda()


# decoder, which contains the unet(s) and clip

decoder = Decoder(
    clip = clip,
    unet = (unet,),               # insert both unets in order of low resolution to highest resolution (you can have as many stages as you want here)
    image_sizes = (256,),         # resolutions, 256 for first unet, 512 for second. these must be unique and in ascending order (matches with the unets passed in)
    timesteps = 1000,
    image_cond_drop_prob = 0.1,
    text_cond_drop_prob = 0.5
).cuda()

# mock images (get a lot of this)

images = torch.randn(4, 3, 256, 256).cuda()

# feed images into decoder, specifying which unet you want to train
# each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme

loss = decoder(images, unet_number = 1)
loss.backward()

# do the above for many steps for both unets

mock_image_embed = torch.randn(1, 512).cuda()

# then to do inpainting

inpaint_image = torch.randn(1, 3, 256, 256).cuda()      # (batch, channels, height, width)
inpaint_mask = torch.ones(1, 256, 256).bool().cuda()    # (batch, height, width)

inpainted_images = decoder.sample(
    image_embed = mock_image_embed,
    inpaint_image = inpaint_image,    # just pass in the inpaint image
    inpaint_mask = inpaint_mask       # and the mask
)

inpainted_images.shape # (1, 3, 256, 256)"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">Unet</span>, <span class="pl-v">Decoder</span>, <span class="pl-c1">CLIP</span>

<span class="pl-c"># trained clip from step 1</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">CLIP</span>(
    <span class="pl-s1">dim_text</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_image</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_latent</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">num_text_tokens</span> <span class="pl-c1">=</span> <span class="pl-c1">49408</span>,
    <span class="pl-s1">text_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">text_seq_len</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">text_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">visual_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">visual_image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">visual_patch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">visual_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># 2 unets for the decoder (a la cascading DDPM)</span>

<span class="pl-s1">unet</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">16</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">1</span>, <span class="pl-c1">1</span>, <span class="pl-c1">1</span>)
).<span class="pl-c1">cuda</span>()


<span class="pl-c"># decoder, which contains the unet(s) and clip</span>

<span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-en">Decoder</span>(
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">unet</span> <span class="pl-c1">=</span> (<span class="pl-s1">unet</span>,),               <span class="pl-c"># insert both unets in order of low resolution to highest resolution (you can have as many stages as you want here)</span>
    <span class="pl-s1">image_sizes</span> <span class="pl-c1">=</span> (<span class="pl-c1">256</span>,),         <span class="pl-c"># resolutions, 256 for first unet, 512 for second. these must be unique and in ascending order (matches with the unets passed in)</span>
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span>,
    <span class="pl-s1">image_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.1</span>,
    <span class="pl-s1">text_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.5</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock images (get a lot of this)</span>

<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">4</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># feed images into decoder, specifying which unet you want to train</span>
<span class="pl-c"># each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme</span>

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder</span>(<span class="pl-s1">images</span>, <span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>)
<span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do the above for many steps for both unets</span>

<span class="pl-s1">mock_image_embed</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">1</span>, <span class="pl-c1">512</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># then to do inpainting</span>

<span class="pl-s1">inpaint_image</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">1</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()      <span class="pl-c"># (batch, channels, height, width)</span>
<span class="pl-s1">inpaint_mask</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">ones</span>(<span class="pl-c1">1</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">bool</span>().<span class="pl-c1">cuda</span>()    <span class="pl-c"># (batch, height, width)</span>

<span class="pl-s1">inpainted_images</span> <span class="pl-c1">=</span> <span class="pl-s1">decoder</span>.<span class="pl-c1">sample</span>(
    <span class="pl-s1">image_embed</span> <span class="pl-c1">=</span> <span class="pl-s1">mock_image_embed</span>,
    <span class="pl-s1">inpaint_image</span> <span class="pl-c1">=</span> <span class="pl-s1">inpaint_image</span>,    <span class="pl-c"># just pass in the inpaint image</span>
    <span class="pl-s1">inpaint_mask</span> <span class="pl-c1">=</span> <span class="pl-s1">inpaint_mask</span>       <span class="pl-c"># and the mask</span>
)

<span class="pl-s1">inpainted_images</span>.<span class="pl-c1">shape</span> <span class="pl-c"># (1, 3, 256, 256)</span></pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Experimental</h2><a id="user-content-experimental" class="anchor" aria-label="Permalink: Experimental" href="#experimental"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">DALL-E2 with Latent Diffusion</h3><a id="user-content-dall-e2-with-latent-diffusion" class="anchor" aria-label="Permalink: DALL-E2 with Latent Diffusion" href="#dall-e2-with-latent-diffusion"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">This repository decides to take the next step and offer DALL-E v2 combined with <a href="https://huggingface.co/spaces/multimodalart/latentdiffusion" rel="nofollow">latent diffusion</a>, from Rombach et al.</p>
<p dir="auto">You can use it as follows. Latent diffusion can be limited to just the first U-Net in the cascade, or to any number you wish.</p>
<p dir="auto">The repository also comes equipped with all the necessary settings to recreate <code>ViT-VQGan</code> from the <a href="https://arxiv.org/abs/2110.04627" rel="nofollow">Improved VQGans</a> paper. Furthermore, the <a href="https://github.com/lucidrains/vector-quantize-pytorch">vector quantization</a> library also comes equipped to do <a href="https://arxiv.org/abs/2203.01941" rel="nofollow">residual or multi-headed quantization</a>, which I believe will give an even further boost in performance to the autoencoder.</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import Unet, Decoder, CLIP, VQGanVAE

# trained clip from step 1

clip = CLIP(
    dim_text = 512,
    dim_image = 512,
    dim_latent = 512,
    num_text_tokens = 49408,
    text_enc_depth = 1,
    text_seq_len = 256,
    text_heads = 8,
    visual_enc_depth = 1,
    visual_image_size = 256,
    visual_patch_size = 32,
    visual_heads = 8
)

# 3 unets for the decoder (a la cascading DDPM)

# first two unets are doing latent diffusion
# vqgan-vae must be trained beforehand

vae1 = VQGanVAE(
    dim = 32,
    image_size = 256,
    layers = 3,
    layer_mults = (1, 2, 4)
)

vae2 = VQGanVAE(
    dim = 32,
    image_size = 512,
    layers = 3,
    layer_mults = (1, 2, 4)
)

unet1 = Unet(
    dim = 32,
    image_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    sparse_attn = True,
    sparse_attn_window = 2,
    dim_mults = (1, 2, 4, 8)
)

unet2 = Unet(
    dim = 32,
    image_embed_dim = 512,
    channels = 3,
    dim_mults = (1, 2, 4, 8, 16),
    cond_on_image_embeds = True,
    cond_on_text_encodings = False
)

unet3 = Unet(
    dim = 32,
    image_embed_dim = 512,
    channels = 3,
    dim_mults = (1, 2, 4, 8, 16),
    cond_on_image_embeds = True,
    cond_on_text_encodings = False,
    attend_at_middle = False
)

# decoder, which contains the unet(s) and clip

decoder = Decoder(
    clip = clip,
    vae = (vae1, vae2),                # latent diffusion for unet1 (vae1) and unet2 (vae2), but not for the last unet3
    unet = (unet1, unet2, unet3),      # insert unets in order of low resolution to highest resolution (you can have as many stages as you want here)
    image_sizes = (256, 512, 1024),    # resolutions, 256 for first unet, 512 for second, 1024 for third
    timesteps = 100,
    image_cond_drop_prob = 0.1,
    text_cond_drop_prob = 0.5
).cuda()

# mock images (get a lot of this)

images = torch.randn(1, 3, 1024, 1024).cuda()

# feed images into decoder, specifying which unet you want to train
# each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme

with decoder.one_unet_in_gpu(1):
    loss = decoder(images, unet_number = 1)
    loss.backward()

with decoder.one_unet_in_gpu(2):
    loss = decoder(images, unet_number = 2)
    loss.backward()

with decoder.one_unet_in_gpu(3):
    loss = decoder(images, unet_number = 3)
    loss.backward()

# do the above for many steps for both unets

# then it will learn to generate images based on the CLIP image embeddings

# chaining the unets from lowest resolution to highest resolution (thus cascading)

mock_image_embed = torch.randn(1, 512).cuda()
images = decoder.sample(mock_image_embed) # (1, 3, 1024, 1024)"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">Unet</span>, <span class="pl-v">Decoder</span>, <span class="pl-c1">CLIP</span>, <span class="pl-v">VQGanVAE</span>

<span class="pl-c"># trained clip from step 1</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">CLIP</span>(
    <span class="pl-s1">dim_text</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_image</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_latent</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">num_text_tokens</span> <span class="pl-c1">=</span> <span class="pl-c1">49408</span>,
    <span class="pl-s1">text_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>,
    <span class="pl-s1">text_seq_len</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">text_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">visual_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>,
    <span class="pl-s1">visual_image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">visual_patch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">visual_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
)

<span class="pl-c"># 3 unets for the decoder (a la cascading DDPM)</span>

<span class="pl-c"># first two unets are doing latent diffusion</span>
<span class="pl-c"># vqgan-vae must be trained beforehand</span>

<span class="pl-s1">vae1</span> <span class="pl-c1">=</span> <span class="pl-en">VQGanVAE</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">layers</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">layer_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>)
)

<span class="pl-s1">vae2</span> <span class="pl-c1">=</span> <span class="pl-en">VQGanVAE</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">layers</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">layer_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>)
)

<span class="pl-s1">unet1</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">sparse_attn</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>,
    <span class="pl-s1">sparse_attn_window</span> <span class="pl-c1">=</span> <span class="pl-c1">2</span>,
    <span class="pl-s1">dim_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>)
)

<span class="pl-s1">unet2</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>, <span class="pl-c1">16</span>),
    <span class="pl-s1">cond_on_image_embeds</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>,
    <span class="pl-s1">cond_on_text_encodings</span> <span class="pl-c1">=</span> <span class="pl-c1">False</span>
)

<span class="pl-s1">unet3</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>, <span class="pl-c1">16</span>),
    <span class="pl-s1">cond_on_image_embeds</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>,
    <span class="pl-s1">cond_on_text_encodings</span> <span class="pl-c1">=</span> <span class="pl-c1">False</span>,
    <span class="pl-s1">attend_at_middle</span> <span class="pl-c1">=</span> <span class="pl-c1">False</span>
)

<span class="pl-c"># decoder, which contains the unet(s) and clip</span>

<span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-en">Decoder</span>(
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">vae</span> <span class="pl-c1">=</span> (<span class="pl-s1">vae1</span>, <span class="pl-s1">vae2</span>),                <span class="pl-c"># latent diffusion for unet1 (vae1) and unet2 (vae2), but not for the last unet3</span>
    <span class="pl-s1">unet</span> <span class="pl-c1">=</span> (<span class="pl-s1">unet1</span>, <span class="pl-s1">unet2</span>, <span class="pl-s1">unet3</span>),      <span class="pl-c"># insert unets in order of low resolution to highest resolution (you can have as many stages as you want here)</span>
    <span class="pl-s1">image_sizes</span> <span class="pl-c1">=</span> (<span class="pl-c1">256</span>, <span class="pl-c1">512</span>, <span class="pl-c1">1024</span>),    <span class="pl-c"># resolutions, 256 for first unet, 512 for second, 1024 for third</span>
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">100</span>,
    <span class="pl-s1">image_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.1</span>,
    <span class="pl-s1">text_cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.5</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock images (get a lot of this)</span>

<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">1</span>, <span class="pl-c1">3</span>, <span class="pl-c1">1024</span>, <span class="pl-c1">1024</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># feed images into decoder, specifying which unet you want to train</span>
<span class="pl-c"># each unet can be trained separately, which is one of the benefits of the cascading DDPM scheme</span>

<span class="pl-k">with</span> <span class="pl-s1">decoder</span>.<span class="pl-c1">one_unet_in_gpu</span>(<span class="pl-c1">1</span>):
    <span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder</span>(<span class="pl-s1">images</span>, <span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>)
    <span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-k">with</span> <span class="pl-s1">decoder</span>.<span class="pl-c1">one_unet_in_gpu</span>(<span class="pl-c1">2</span>):
    <span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder</span>(<span class="pl-s1">images</span>, <span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-c1">2</span>)
    <span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-k">with</span> <span class="pl-s1">decoder</span>.<span class="pl-c1">one_unet_in_gpu</span>(<span class="pl-c1">3</span>):
    <span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder</span>(<span class="pl-s1">images</span>, <span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>)
    <span class="pl-s1">loss</span>.<span class="pl-c1">backward</span>()

<span class="pl-c"># do the above for many steps for both unets</span>

<span class="pl-c"># then it will learn to generate images based on the CLIP image embeddings</span>

<span class="pl-c"># chaining the unets from lowest resolution to highest resolution (thus cascading)</span>

<span class="pl-s1">mock_image_embed</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">1</span>, <span class="pl-c1">512</span>).<span class="pl-c1">cuda</span>()
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">decoder</span>.<span class="pl-c1">sample</span>(<span class="pl-s1">mock_image_embed</span>) <span class="pl-c"># (1, 3, 1024, 1024)</span></pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Training wrapper</h2><a id="user-content-training-wrapper" class="anchor" aria-label="Permalink: Training wrapper" href="#training-wrapper"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Decoder Training</h3><a id="user-content-decoder-training" class="anchor" aria-label="Permalink: Decoder Training" href="#decoder-training"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Training the <code>Decoder</code> may be confusing, as one needs to keep track of an optimizer for each of the <code>Unet</code>(s) separately. Each <code>Unet</code> will also need its own corresponding exponential moving average. The <code>DecoderTrainer</code> hopes to make this simple, as shown below</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import DALLE2, Unet, Decoder, CLIP, DecoderTrainer

clip = CLIP(
    dim_text = 512,
    dim_image = 512,
    dim_latent = 512,
    num_text_tokens = 49408,
    text_enc_depth = 6,
    text_seq_len = 256,
    text_heads = 8,
    visual_enc_depth = 6,
    visual_image_size = 256,
    visual_patch_size = 32,
    visual_heads = 8
).cuda()

# mock data

text = torch.randint(0, 49408, (32, 256)).cuda()
images = torch.randn(32, 3, 256, 256).cuda()

# decoder (with unet)

unet1 = Unet(
    dim = 128,
    image_embed_dim = 512,
    text_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    dim_mults=(1, 2, 4, 8),
    cond_on_text_encodings = True,
).cuda()

unet2 = Unet(
    dim = 16,
    image_embed_dim = 512,
    cond_dim = 128,
    channels = 3,
    dim_mults = (1, 2, 4, 8, 16),
).cuda()

decoder = Decoder(
    unet = (unet1, unet2),
    image_sizes = (128, 256),
    clip = clip,
    timesteps = 1000
).cuda()

decoder_trainer = DecoderTrainer(
    decoder,
    lr = 3e-4,
    wd = 1e-2,
    ema_beta = 0.99,
    ema_update_after_step = 1000,
    ema_update_every = 10,
)

for unet_number in (1, 2):
    loss = decoder_trainer(
        images,
        text = text,
        unet_number = unet_number, # which unet to train on
        max_batch_size = 4         # gradient accumulation - this sets the maximum batch size in which to do forward and backwards pass - for this example 32 / 4 == 8 times
    )

    decoder_trainer.update(unet_number) # update the specific unet as well as its exponential moving average

# after much training
# you can sample from the exponentially moving averaged unets as so

mock_image_embed = torch.randn(32, 512).cuda()
images = decoder_trainer.sample(image_embed = mock_image_embed, text = text) # (4, 3, 256, 256)"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">DALLE2</span>, <span class="pl-v">Unet</span>, <span class="pl-v">Decoder</span>, <span class="pl-c1">CLIP</span>, <span class="pl-v">DecoderTrainer</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">CLIP</span>(
    <span class="pl-s1">dim_text</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_image</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_latent</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">num_text_tokens</span> <span class="pl-c1">=</span> <span class="pl-c1">49408</span>,
    <span class="pl-s1">text_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">text_seq_len</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">text_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">visual_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">visual_image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">visual_patch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">visual_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock data</span>

<span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randint</span>(<span class="pl-c1">0</span>, <span class="pl-c1">49408</span>, (<span class="pl-c1">32</span>, <span class="pl-c1">256</span>)).<span class="pl-c1">cuda</span>()
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">32</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># decoder (with unet)</span>

<span class="pl-s1">unet1</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">text_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span><span class="pl-c1">=</span>(<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>),
    <span class="pl-s1">cond_on_text_encodings</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>,
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">unet2</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">16</span>,
    <span class="pl-s1">image_embed_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">cond_dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">channels</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>,
    <span class="pl-s1">dim_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>, <span class="pl-c1">16</span>),
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-en">Decoder</span>(
    <span class="pl-s1">unet</span> <span class="pl-c1">=</span> (<span class="pl-s1">unet1</span>, <span class="pl-s1">unet2</span>),
    <span class="pl-s1">image_sizes</span> <span class="pl-c1">=</span> (<span class="pl-c1">128</span>, <span class="pl-c1">256</span>),
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">decoder_trainer</span> <span class="pl-c1">=</span> <span class="pl-en">DecoderTrainer</span>(
    <span class="pl-s1">decoder</span>,
    <span class="pl-s1">lr</span> <span class="pl-c1">=</span> <span class="pl-c1">3e-4</span>,
    <span class="pl-s1">wd</span> <span class="pl-c1">=</span> <span class="pl-c1">1e-2</span>,
    <span class="pl-s1">ema_beta</span> <span class="pl-c1">=</span> <span class="pl-c1">0.99</span>,
    <span class="pl-s1">ema_update_after_step</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span>,
    <span class="pl-s1">ema_update_every</span> <span class="pl-c1">=</span> <span class="pl-c1">10</span>,
)

<span class="pl-k">for</span> <span class="pl-s1">unet_number</span> <span class="pl-c1">in</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>):
    <span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder_trainer</span>(
        <span class="pl-s1">images</span>,
        <span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">text</span>,
        <span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-s1">unet_number</span>, <span class="pl-c"># which unet to train on</span>
        <span class="pl-s1">max_batch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">4</span>         <span class="pl-c"># gradient accumulation - this sets the maximum batch size in which to do forward and backwards pass - for this example 32 / 4 == 8 times</span>
    )

    <span class="pl-s1">decoder_trainer</span>.<span class="pl-c1">update</span>(<span class="pl-s1">unet_number</span>) <span class="pl-c"># update the specific unet as well as its exponential moving average</span>

<span class="pl-c"># after much training</span>
<span class="pl-c"># you can sample from the exponentially moving averaged unets as so</span>

<span class="pl-s1">mock_image_embed</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">32</span>, <span class="pl-c1">512</span>).<span class="pl-c1">cuda</span>()
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">decoder_trainer</span>.<span class="pl-c1">sample</span>(<span class="pl-s1">image_embed</span> <span class="pl-c1">=</span> <span class="pl-s1">mock_image_embed</span>, <span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">text</span>) <span class="pl-c"># (4, 3, 256, 256)</span></pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Diffusion Prior Training</h3><a id="user-content-diffusion-prior-training" class="anchor" aria-label="Permalink: Diffusion Prior Training" href="#diffusion-prior-training"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Similarly, one can use the <code>DiffusionPriorTrainer</code> to automatically instantiate and keep track of an exponential moving averaged prior.</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import DALLE2, DiffusionPriorNetwork, DiffusionPrior, DiffusionPriorTrainer, Unet, Decoder, CLIP

clip = CLIP(
    dim_text = 512,
    dim_image = 512,
    dim_latent = 512,
    num_text_tokens = 49408,
    text_enc_depth = 6,
    text_seq_len = 256,
    text_heads = 8,
    visual_enc_depth = 6,
    visual_image_size = 256,
    visual_patch_size = 32,
    visual_heads = 8
).cuda()

# mock data

text = torch.randint(0, 49408, (512, 256)).cuda()
images = torch.randn(512, 3, 256, 256).cuda()

# prior networks (with transformer)

prior_network = DiffusionPriorNetwork(
    dim = 512,
    depth = 6,
    dim_head = 64,
    heads = 8
).cuda()

diffusion_prior = DiffusionPrior(
    net = prior_network,
    clip = clip,
    timesteps = 100,
    cond_drop_prob = 0.2
).cuda()

diffusion_prior_trainer = DiffusionPriorTrainer(
    diffusion_prior,
    lr = 3e-4,
    wd = 1e-2,
    ema_beta = 0.99,
    ema_update_after_step = 1000,
    ema_update_every = 10,
)

loss = diffusion_prior_trainer(text, images, max_batch_size = 4)
diffusion_prior_trainer.update()  # this will update the optimizer as well as the exponential moving averaged diffusion prior

# after much of the above three lines in a loop
# you can sample from the exponential moving average of the diffusion prior identically to how you do so for DiffusionPrior

image_embeds = diffusion_prior_trainer.sample(text, max_batch_size = 4) # (512, 512) - exponential moving averaged image embeddings"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">DALLE2</span>, <span class="pl-v">DiffusionPriorNetwork</span>, <span class="pl-v">DiffusionPrior</span>, <span class="pl-v">DiffusionPriorTrainer</span>, <span class="pl-v">Unet</span>, <span class="pl-v">Decoder</span>, <span class="pl-c1">CLIP</span>

<span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-en">CLIP</span>(
    <span class="pl-s1">dim_text</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_image</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">dim_latent</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">num_text_tokens</span> <span class="pl-c1">=</span> <span class="pl-c1">49408</span>,
    <span class="pl-s1">text_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">text_seq_len</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">text_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>,
    <span class="pl-s1">visual_enc_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">visual_image_size</span> <span class="pl-c1">=</span> <span class="pl-c1">256</span>,
    <span class="pl-s1">visual_patch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">visual_heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># mock data</span>

<span class="pl-s1">text</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randint</span>(<span class="pl-c1">0</span>, <span class="pl-c1">49408</span>, (<span class="pl-c1">512</span>, <span class="pl-c1">256</span>)).<span class="pl-c1">cuda</span>()
<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">512</span>, <span class="pl-c1">3</span>, <span class="pl-c1">256</span>, <span class="pl-c1">256</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># prior networks (with transformer)</span>

<span class="pl-s1">prior_network</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPriorNetwork</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">512</span>,
    <span class="pl-s1">depth</span> <span class="pl-c1">=</span> <span class="pl-c1">6</span>,
    <span class="pl-s1">dim_head</span> <span class="pl-c1">=</span> <span class="pl-c1">64</span>,
    <span class="pl-s1">heads</span> <span class="pl-c1">=</span> <span class="pl-c1">8</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">diffusion_prior</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPrior</span>(
    <span class="pl-s1">net</span> <span class="pl-c1">=</span> <span class="pl-s1">prior_network</span>,
    <span class="pl-s1">clip</span> <span class="pl-c1">=</span> <span class="pl-s1">clip</span>,
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">100</span>,
    <span class="pl-s1">cond_drop_prob</span> <span class="pl-c1">=</span> <span class="pl-c1">0.2</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">diffusion_prior_trainer</span> <span class="pl-c1">=</span> <span class="pl-en">DiffusionPriorTrainer</span>(
    <span class="pl-s1">diffusion_prior</span>,
    <span class="pl-s1">lr</span> <span class="pl-c1">=</span> <span class="pl-c1">3e-4</span>,
    <span class="pl-s1">wd</span> <span class="pl-c1">=</span> <span class="pl-c1">1e-2</span>,
    <span class="pl-s1">ema_beta</span> <span class="pl-c1">=</span> <span class="pl-c1">0.99</span>,
    <span class="pl-s1">ema_update_after_step</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span>,
    <span class="pl-s1">ema_update_every</span> <span class="pl-c1">=</span> <span class="pl-c1">10</span>,
)

<span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">diffusion_prior_trainer</span>(<span class="pl-s1">text</span>, <span class="pl-s1">images</span>, <span class="pl-s1">max_batch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">4</span>)
<span class="pl-s1">diffusion_prior_trainer</span>.<span class="pl-c1">update</span>()  <span class="pl-c"># this will update the optimizer as well as the exponential moving averaged diffusion prior</span>

<span class="pl-c"># after much of the above three lines in a loop</span>
<span class="pl-c"># you can sample from the exponential moving average of the diffusion prior identically to how you do so for DiffusionPrior</span>

<span class="pl-s1">image_embeds</span> <span class="pl-c1">=</span> <span class="pl-s1">diffusion_prior_trainer</span>.<span class="pl-c1">sample</span>(<span class="pl-s1">text</span>, <span class="pl-s1">max_batch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">4</span>) <span class="pl-c"># (512, 512) - exponential moving averaged image embeddings</span></pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Bonus</h2><a id="user-content-bonus" class="anchor" aria-label="Permalink: Bonus" href="#bonus"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Unconditional Training</h3><a id="user-content-unconditional-training" class="anchor" aria-label="Permalink: Unconditional Training" href="#unconditional-training"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">The repository also contains the means to train unconditional DDPM model, or even cascading DDPMs. You simply have to set <code>unconditional = True</code> in the <code>Decoder</code></p>
<p dir="auto">ex.</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import torch
from dalle2_pytorch import Unet, Decoder, DecoderTrainer

# unet for the cascading ddpm

unet1 = Unet(
    dim = 128,
    dim_mults=(1, 2, 4, 8)
).cuda()

unet2 = Unet(
    dim = 32,
    dim_mults = (1, 2, 4, 8, 16)
).cuda()

# decoder, which contains the unets

decoder = Decoder(
    unet = (unet1, unet2),
    image_sizes = (256, 512),  # first unet up to 256px, then second to 512px
    timesteps = 1000,
    unconditional = True
).cuda()

# decoder trainer

decoder_trainer = DecoderTrainer(decoder)

# images (get a lot of this)

images = torch.randn(1, 3, 512, 512).cuda()

# feed images into decoder

for i in (1, 2):
    loss = decoder_trainer(images, unet_number = i)
    decoder_trainer.update(unet_number = i)

# do the above for many many many many images
# then it will learn to generate images

images = decoder_trainer.sample(batch_size = 36, max_batch_size = 4) # (36, 3, 512, 512)"><pre><span class="pl-k">import</span> <span class="pl-s1">torch</span>
<span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span> <span class="pl-k">import</span> <span class="pl-v">Unet</span>, <span class="pl-v">Decoder</span>, <span class="pl-v">DecoderTrainer</span>

<span class="pl-c"># unet for the cascading ddpm</span>

<span class="pl-s1">unet1</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">128</span>,
    <span class="pl-s1">dim_mults</span><span class="pl-c1">=</span>(<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>)
).<span class="pl-c1">cuda</span>()

<span class="pl-s1">unet2</span> <span class="pl-c1">=</span> <span class="pl-en">Unet</span>(
    <span class="pl-s1">dim</span> <span class="pl-c1">=</span> <span class="pl-c1">32</span>,
    <span class="pl-s1">dim_mults</span> <span class="pl-c1">=</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">8</span>, <span class="pl-c1">16</span>)
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># decoder, which contains the unets</span>

<span class="pl-s1">decoder</span> <span class="pl-c1">=</span> <span class="pl-en">Decoder</span>(
    <span class="pl-s1">unet</span> <span class="pl-c1">=</span> (<span class="pl-s1">unet1</span>, <span class="pl-s1">unet2</span>),
    <span class="pl-s1">image_sizes</span> <span class="pl-c1">=</span> (<span class="pl-c1">256</span>, <span class="pl-c1">512</span>),  <span class="pl-c"># first unet up to 256px, then second to 512px</span>
    <span class="pl-s1">timesteps</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span>,
    <span class="pl-s1">unconditional</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>
).<span class="pl-c1">cuda</span>()

<span class="pl-c"># decoder trainer</span>

<span class="pl-s1">decoder_trainer</span> <span class="pl-c1">=</span> <span class="pl-en">DecoderTrainer</span>(<span class="pl-s1">decoder</span>)

<span class="pl-c"># images (get a lot of this)</span>

<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">torch</span>.<span class="pl-c1">randn</span>(<span class="pl-c1">1</span>, <span class="pl-c1">3</span>, <span class="pl-c1">512</span>, <span class="pl-c1">512</span>).<span class="pl-c1">cuda</span>()

<span class="pl-c"># feed images into decoder</span>

<span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>):
    <span class="pl-s1">loss</span> <span class="pl-c1">=</span> <span class="pl-en">decoder_trainer</span>(<span class="pl-s1">images</span>, <span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-s1">i</span>)
    <span class="pl-s1">decoder_trainer</span>.<span class="pl-c1">update</span>(<span class="pl-s1">unet_number</span> <span class="pl-c1">=</span> <span class="pl-s1">i</span>)

<span class="pl-c"># do the above for many many many many images</span>
<span class="pl-c"># then it will learn to generate images</span>

<span class="pl-s1">images</span> <span class="pl-c1">=</span> <span class="pl-s1">decoder_trainer</span>.<span class="pl-c1">sample</span>(<span class="pl-s1">batch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">36</span>, <span class="pl-s1">max_batch_size</span> <span class="pl-c1">=</span> <span class="pl-c1">4</span>) <span class="pl-c"># (36, 3, 512, 512)</span></pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Dataloaders</h2><a id="user-content-dataloaders" class="anchor" aria-label="Permalink: Dataloaders" href="#dataloaders"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Decoder Dataloaders</h3><a id="user-content-decoder-dataloaders" class="anchor" aria-label="Permalink: Decoder Dataloaders" href="#decoder-dataloaders"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">In order to make loading data simple and efficient, we include some general dataloaders that can be used to train portions of the network.</p>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Decoder: Image Embedding Dataset</h4><a id="user-content-decoder-image-embedding-dataset" class="anchor" aria-label="Permalink: Decoder: Image Embedding Dataset" href="#decoder-image-embedding-dataset"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">When training the decoder (and up samplers if training together) in isolation, you will need to load images and corresponding image embeddings. This dataset can read two similar types of datasets. First, it can read a <a href="https://github.com/webdataset/webdataset">webdataset</a> that contains <code>.jpg</code> and <code>.npy</code> files in the <code>.tar</code>s that contain the images and associated image embeddings respectively. Alternatively, you can also specify a source for the embeddings outside of the webdataset. In this case, the path to the embeddings should contain <code>.npy</code> files with the same shard numbers as the webdataset and there should be a correspondence between the filename of the <code>.jpg</code> and the index of the embedding in the <code>.npy</code>. So, for example, <code>0001.tar</code> from the webdataset with image <code>00010509.jpg</code> (the first 4 digits are the shard number and the last 4 are the index) in it should be paralleled by a <code>img_emb_0001.npy</code> which contains a NumPy array with the embedding at index 509.</p>
<p dir="auto">Generating a dataset of this type:</p>
<ol dir="auto">
<li>Use <a href="https://github.com/rom1504/img2dataset">img2dataset</a> to generate a webdataset.</li>
<li>Use <a href="https://github.com/rom1504/clip-retrieval">clip-retrieval</a> to convert the images to embeddings.</li>
<li>Use <a href="https://github.com/Veldrovive/embedding-dataset-reordering">embedding-dataset-reordering</a> to reorder the embeddings into the expected format.</li>
</ol>
<p dir="auto">Usage:</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="from dalle2_pytorch.dataloaders import ImageEmbeddingDataset, create_image_embedding_dataloader

# Create a dataloader directly.
dataloader = create_image_embedding_dataloader(
    tar_url=&quot;/path/or/url/to/webdataset/{0000..9999}.tar&quot;, # Uses bracket expanding notation. This specifies to read all tars from 0000.tar to 9999.tar
    embeddings_url=&quot;path/or/url/to/embeddings/folder&quot;,     # Included if .npy files are not in webdataset. Left out or set to None otherwise
    num_workers=4,
    batch_size=32,
    shard_width=4,                                         # If a file in the webdataset shard 3 is named 0003039.jpg, we know the shard width is 4 and the last three digits are the index
    shuffle_num=200,                                       # Does a shuffle of the data with a buffer size of 200
    shuffle_shards=True,                                   # Shuffle the order the shards are read in
    resample_shards=False,                                 # Sample shards with replacement. If true, an epoch will be infinite unless stopped manually
)
for img, emb in dataloader:
    print(img.shape)  # torch.Size([32, 3, 256, 256])
    print(emb[&quot;img&quot;].shape)  # torch.Size([32, 512])
    # Train decoder only as shown above

# Or create a dataset without a loader so you can configure it manually
dataset = ImageEmbeddingDataset(
    urls=&quot;/path/or/url/to/webdataset/{0000..9999}.tar&quot;,
    embedding_folder_url=&quot;path/or/url/to/embeddings/folder&quot;,
    shard_width=4,
    shuffle_shards=True,
    resample=False
)"><pre><span class="pl-k">from</span> <span class="pl-s1">dalle2_pytorch</span>.<span class="pl-s1">dataloaders</span> <span class="pl-k">import</span> <span class="pl-v">ImageEmbeddingDataset</span>, <span class="pl-s1">create_image_embedding_dataloader</span>

<span class="pl-c"># Create a dataloader directly.</span>
<span class="pl-s1">dataloader</span> <span class="pl-c1">=</span> <span class="pl-en">create_image_embedding_dataloader</span>(
    <span class="pl-s1">tar_url</span><span class="pl-c1">=</span><span class="pl-s">"/path/or/url/to/webdataset/{0000..9999}.tar"</span>, <span class="pl-c"># Uses bracket expanding notation. This specifies to read all tars from 0000.tar to 9999.tar</span>
    <span class="pl-s1">embeddings_url</span><span class="pl-c1">=</span><span class="pl-s">"path/or/url/to/embeddings/folder"</span>,     <span class="pl-c"># Included if .npy files are not in webdataset. Left out or set to None otherwise</span>
    <span class="pl-s1">num_workers</span><span class="pl-c1">=</span><span class="pl-c1">4</span>,
    <span class="pl-s1">batch_size</span><span class="pl-c1">=</span><span class="pl-c1">32</span>,
    <span class="pl-s1">shard_width</span><span class="pl-c1">=</span><span class="pl-c1">4</span>,                                         <span class="pl-c"># If a file in the webdataset shard 3 is named 0003039.jpg, we know the shard width is 4 and the last three digits are the index</span>
    <span class="pl-s1">shuffle_num</span><span class="pl-c1">=</span><span class="pl-c1">200</span>,                                       <span class="pl-c"># Does a shuffle of the data with a buffer size of 200</span>
    <span class="pl-s1">shuffle_shards</span><span class="pl-c1">=</span><span class="pl-c1">True</span>,                                   <span class="pl-c"># Shuffle the order the shards are read in</span>
    <span class="pl-s1">resample_shards</span><span class="pl-c1">=</span><span class="pl-c1">False</span>,                                 <span class="pl-c"># Sample shards with replacement. If true, an epoch will be infinite unless stopped manually</span>
)
<span class="pl-k">for</span> <span class="pl-s1">img</span>, <span class="pl-s1">emb</span> <span class="pl-c1">in</span> <span class="pl-s1">dataloader</span>:
    <span class="pl-en">print</span>(<span class="pl-s1">img</span>.<span class="pl-c1">shape</span>)  <span class="pl-c"># torch.Size([32, 3, 256, 256])</span>
    <span class="pl-en">print</span>(<span class="pl-s1">emb</span>[<span class="pl-s">"img"</span>].<span class="pl-c1">shape</span>)  <span class="pl-c"># torch.Size([32, 512])</span>
    <span class="pl-c"># Train decoder only as shown above</span>

<span class="pl-c"># Or create a dataset without a loader so you can configure it manually</span>
<span class="pl-s1">dataset</span> <span class="pl-c1">=</span> <span class="pl-en">ImageEmbeddingDataset</span>(
    <span class="pl-s1">urls</span><span class="pl-c1">=</span><span class="pl-s">"/path/or/url/to/webdataset/{0000..9999}.tar"</span>,
    <span class="pl-s1">embedding_folder_url</span><span class="pl-c1">=</span><span class="pl-s">"path/or/url/to/embeddings/folder"</span>,
    <span class="pl-s1">shard_width</span><span class="pl-c1">=</span><span class="pl-c1">4</span>,
    <span class="pl-s1">shuffle_shards</span><span class="pl-c1">=</span><span class="pl-c1">True</span>,
    <span class="pl-s1">resample</span><span class="pl-c1">=</span><span class="pl-c1">False</span>
)</pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Scripts</h3><a id="user-content-scripts" class="anchor" aria-label="Permalink: Scripts" href="#scripts"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto"><code>train_diffusion_prior.py</code></h4><a id="user-content-train_diffusion_priorpy" class="anchor" aria-label="Permalink: train_diffusion_prior.py" href="#train_diffusion_priorpy"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">For detailed information on training the diffusion prior, please refer to the <a href="/lucidrains/DALLE2-pytorch/blob/main/prior.md">dedicated readme</a></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Todo</h2><a id="user-content-todo" class="anchor" aria-label="Permalink: Todo" href="#todo"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> finish off gaussian diffusion class for latent embedding - allow for prediction of epsilon</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> add what was proposed in the paper, where DDPM objective for image latent embedding predicts x0 directly (reread vq-diffusion paper and get caught up on that line of work)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> make sure it works end to end to produce an output tensor, taking a single gradient step</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> augment unet so that it can also be conditioned on text encodings (although in paper they hinted this didn't make much a difference)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> figure out all the current bag of tricks needed to make DDPMs great (starting with the blur trick mentioned in paper)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> build the cascading ddpm by having Decoder class manage multiple unets at different resolutions</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> add efficient attention in unet</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> be able to finely customize what to condition on (text, image embed) for specific unet in the cascade (super resolution ddpms near the end may not need too much conditioning)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> offload unets not being trained on to CPU for memory efficiency (for training each resolution unets separately)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> build out latent diffusion architecture, with the vq-reg variant (vqgan-vae), make it completely optional and compatible with cascading ddpms</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> for decoder, allow ability to customize objective (predict epsilon vs x0), in case latent diffusion does better with prediction of x0</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> use attention-based upsampling <a href="https://arxiv.org/abs/2112.11435" rel="nofollow">https://arxiv.org/abs/2112.11435</a></li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> use inheritance just this once for sharing logic between decoder and prior network ddpms</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> bring in vit-vqgan <a href="https://arxiv.org/abs/2110.04627" rel="nofollow">https://arxiv.org/abs/2110.04627</a> for the latent diffusion</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> abstract interface for CLIP adapter class, so other CLIPs can be brought in</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> take care of mixed precision as well as gradient accumulation within decoder trainer</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> just take care of the training for the decoder in a wrapper class, as each unet in the cascade will need its own optimizer</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> bring in tools to train vqgan-vae</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> add convnext backbone for vqgan-vae (in addition to vit [vit-vqgan] + resnet)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> make sure DDPMs can be run with traditional resnet blocks (but leave convnext as an option for experimentation)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> make sure for the latter unets in the cascade, one can train on crops for learning super resolution (constrain the unet to be only convolutions in that case, or allow conv-like attention with rel pos bias)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> offer setting in diffusion prior to split time and image embeddings into multiple tokens, configurable, for more surface area during attention</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> make sure resnet hyperparameters can be configurable across unet depth (groups and expansion factor)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> pull logic for training diffusion prior into a class DiffusionPriorTrainer, for eventual script based + CLI based training</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> make sure the cascading ddpm in the repository can be trained unconditionally, offer a one-line CLI tool for training on a folder of images</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> bring in cross-scale embedding from iclr paper <a href="https://github.com/lucidrains/vit-pytorch/blob/main/vit_pytorch/crossformer.py#L14">https://github.com/lucidrains/vit-pytorch/blob/main/vit_pytorch/crossformer.py#L14</a></li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> cross embed layers for downsampling, as an option</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> use an experimental tracker agnostic setup, as done <a href="https://github.com/lucidrains/tf-bind-transformer#simple-trainer-class-for-fine-tuning">here</a></li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> use pydantic for config drive training</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> for both diffusion prior and decoder, all exponential moving averaged models needs to be saved and restored as well (as well as the step number)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> offer save / load methods on the trainer classes to automatically take care of state dicts for scalers / optimizers / saving versions and checking for breaking changes</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> allow for creation of diffusion prior model off pydantic config classes - consider the same for tracker configs</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> bring in skip-layer excitations (from lightweight gan paper) to see if it helps for either decoder of unet or vqgan-vae training (doesnt work well)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> test out grid attention in cascading ddpm locally, decide whether to keep or remove <a href="https://arxiv.org/abs/2204.01697" rel="nofollow">https://arxiv.org/abs/2204.01697</a> (keeping, seems to be fine)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> allow for unet to be able to condition non-cross attention style as well</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> speed up inference, read up on papers (ddim)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> add inpainting ability using resampler from repaint paper <a href="https://arxiv.org/abs/2201.09865" rel="nofollow">https://arxiv.org/abs/2201.09865</a></li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Completed task" checked=""> add the final combination of upsample feature maps, used in unet squared, seems to have an effect in local experiments</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> consider elucidated dalle2 <a href="https://arxiv.org/abs/2206.00364" rel="nofollow">https://arxiv.org/abs/2206.00364</a></li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> add simple outpainting, text-guided 2x size the image for starters</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> interface out the vqgan-vae so a pretrained one can be pulled off the shelf to validate latent diffusion + DALL-E2</li>
</ul>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Citations</h2><a id="user-content-citations" class="anchor" aria-label="Permalink: Citations" href="#citations"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@misc{ramesh2022,
    title   = {Hierarchical Text-Conditional Image Generation with CLIP Latents}, 
    author  = {Aditya Ramesh et al},
    year    = {2022}
}"><pre><span class="pl-k">@misc</span>{<span class="pl-en">ramesh2022</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Hierarchical Text-Conditional Image Generation with CLIP Latents<span class="pl-pds">}</span></span>, 
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Aditya Ramesh et al<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2022<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@misc{crowson2022,
    author  = {Katherine Crowson},
    url     = {https://twitter.com/rivershavewings}
}"><pre><span class="pl-k">@misc</span>{<span class="pl-en">crowson2022</span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Katherine Crowson<span class="pl-pds">}</span></span>,
    <span class="pl-s">url</span>     = <span class="pl-s"><span class="pl-pds">{</span>https://twitter.com/rivershavewings<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@misc{rombach2021highresolution,
    title   = {High-Resolution Image Synthesis with Latent Diffusion Models}, 
    author  = {Robin Rombach and Andreas Blattmann and Dominik Lorenz and Patrick Esser and Björn Ommer},
    year    = {2021},
    eprint  = {2112.10752},
    archivePrefix = {arXiv},
    primaryClass = {cs.CV}
}"><pre><span class="pl-k">@misc</span>{<span class="pl-en">rombach2021highresolution</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>High-Resolution Image Synthesis with Latent Diffusion Models<span class="pl-pds">}</span></span>, 
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Robin Rombach and Andreas Blattmann and Dominik Lorenz and Patrick Esser and Björn Ommer<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2021<span class="pl-pds">}</span></span>,
    <span class="pl-s">eprint</span>  = <span class="pl-s"><span class="pl-pds">{</span>2112.10752<span class="pl-pds">}</span></span>,
    <span class="pl-s">archivePrefix</span> = <span class="pl-s"><span class="pl-pds">{</span>arXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">primaryClass</span> = <span class="pl-s"><span class="pl-pds">{</span>cs.CV<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{shen2019efficient,
    author  = {Zhuoran Shen and Mingyuan Zhang and Haiyu Zhao and Shuai Yi and Hongsheng Li},
    title   = {Efficient Attention: Attention with Linear Complexities},
    journal = {CoRR},
    year    = {2018},
    url     = {http://arxiv.org/abs/1812.01243},
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">shen2019efficient</span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Zhuoran Shen and Mingyuan Zhang and Haiyu Zhao and Shuai Yi and Hongsheng Li<span class="pl-pds">}</span></span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Efficient Attention: Attention with Linear Complexities<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>CoRR<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2018<span class="pl-pds">}</span></span>,
    <span class="pl-s">url</span>     = <span class="pl-s"><span class="pl-pds">{</span>http://arxiv.org/abs/1812.01243<span class="pl-pds">}</span></span>,
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{Yu2021VectorquantizedIM,
    title   = {Vector-quantized Image Modeling with Improved VQGAN},
    author  = {Jiahui Yu and Xin Li and Jing Yu Koh and Han Zhang and Ruoming Pang and James Qin and Alexander Ku and Yuanzhong Xu and Jason Baldridge and Yonghui Wu},
    journal = {ArXiv},
    year    = {2021},
    volume  = {abs/2110.04627}
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">Yu2021VectorquantizedIM</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Vector-quantized Image Modeling with Improved VQGAN<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Jiahui Yu and Xin Li and Jing Yu Koh and Han Zhang and Ruoming Pang and James Qin and Alexander Ku and Yuanzhong Xu and Jason Baldridge and Yonghui Wu<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>ArXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2021<span class="pl-pds">}</span></span>,
    <span class="pl-s">volume</span>  = <span class="pl-s"><span class="pl-pds">{</span>abs/2110.04627<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{Shleifer2021NormFormerIT,
    title   = {NormFormer: Improved Transformer Pretraining with Extra Normalization},
    author  = {Sam Shleifer and Jason Weston and Myle Ott},
    journal = {ArXiv},
    year    = {2021},
    volume  = {abs/2110.09456}
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">Shleifer2021NormFormerIT</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>NormFormer: Improved Transformer Pretraining with Extra Normalization<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Sam Shleifer and Jason Weston and Myle Ott<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>ArXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2021<span class="pl-pds">}</span></span>,
    <span class="pl-s">volume</span>  = <span class="pl-s"><span class="pl-pds">{</span>abs/2110.09456<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{Yu2022CoCaCC,
    title   = {CoCa: Contrastive Captioners are Image-Text Foundation Models},
    author  = {Jiahui Yu and Zirui Wang and Vijay Vasudevan and Legg Yeung and Mojtaba Seyedhosseini and Yonghui Wu},
    journal = {ArXiv},
    year    = {2022},
    volume  = {abs/2205.01917}
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">Yu2022CoCaCC</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>CoCa: Contrastive Captioners are Image-Text Foundation Models<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Jiahui Yu and Zirui Wang and Vijay Vasudevan and Legg Yeung and Mojtaba Seyedhosseini and Yonghui Wu<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>ArXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2022<span class="pl-pds">}</span></span>,
    <span class="pl-s">volume</span>  = <span class="pl-s"><span class="pl-pds">{</span>abs/2205.01917<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@misc{wang2021crossformer,
    title   = {CrossFormer: A Versatile Vision Transformer Hinging on Cross-scale Attention},
    author  = {Wenxiao Wang and Lu Yao and Long Chen and Binbin Lin and Deng Cai and Xiaofei He and Wei Liu},
    year    = {2021},
    eprint  = {2108.00154},
    archivePrefix = {arXiv},
    primaryClass = {cs.CV}
}"><pre><span class="pl-k">@misc</span>{<span class="pl-en">wang2021crossformer</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>CrossFormer: A Versatile Vision Transformer Hinging on Cross-scale Attention<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Wenxiao Wang and Lu Yao and Long Chen and Binbin Lin and Deng Cai and Xiaofei He and Wei Liu<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2021<span class="pl-pds">}</span></span>,
    <span class="pl-s">eprint</span>  = <span class="pl-s"><span class="pl-pds">{</span>2108.00154<span class="pl-pds">}</span></span>,
    <span class="pl-s">archivePrefix</span> = <span class="pl-s"><span class="pl-pds">{</span>arXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">primaryClass</span> = <span class="pl-s"><span class="pl-pds">{</span>cs.CV<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{ho2021cascaded,
    title   = {Cascaded Diffusion Models for High Fidelity Image Generation},
    author  = {Ho, Jonathan and Saharia, Chitwan and Chan, William and Fleet, David J and Norouzi, Mohammad and Salimans, Tim},
    journal = {arXiv preprint arXiv:2106.15282},
    year    = {2021}
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">ho2021cascaded</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Cascaded Diffusion Models for High Fidelity Image Generation<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Ho, Jonathan and Saharia, Chitwan and Chan, William and Fleet, David J and Norouzi, Mohammad and Salimans, Tim<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>arXiv preprint arXiv:2106.15282<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2021<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@misc{Saharia2022,
    title   = {Imagen: unprecedented photorealism × deep level of language understanding},
    author  = {Chitwan Saharia*, William Chan*, Saurabh Saxena†, Lala Li†, Jay Whang†, Emily Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi, Rapha Gontijo Lopes, Tim Salimans, Jonathan Ho†, David Fleet†, Mohammad Norouzi*},
    year    = {2022}
}"><pre><span class="pl-k">@misc</span>{<span class="pl-en">Saharia2022</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Imagen: unprecedented photorealism × deep level of language understanding<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Chitwan Saharia*, William Chan*, Saurabh Saxena†, Lala Li†, Jay Whang†, Emily Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi, Rapha Gontijo Lopes, Tim Salimans, Jonathan Ho†, David Fleet†, Mohammad Norouzi*<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2022<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{Choi2022PerceptionPT,
    title   = {Perception Prioritized Training of Diffusion Models},
    author  = {Jooyoung Choi and Jungbeom Lee and Chaehun Shin and Sungwon Kim and Hyunwoo J. Kim and Sung-Hoon Yoon},
    journal = {ArXiv},
    year    = {2022},
    volume  = {abs/2204.00227}
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">Choi2022PerceptionPT</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Perception Prioritized Training of Diffusion Models<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Jooyoung Choi and Jungbeom Lee and Chaehun Shin and Sungwon Kim and Hyunwoo J. Kim and Sung-Hoon Yoon<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>ArXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2022<span class="pl-pds">}</span></span>,
    <span class="pl-s">volume</span>  = <span class="pl-s"><span class="pl-pds">{</span>abs/2204.00227<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{Saharia2021PaletteID,
    title   = {Palette: Image-to-Image Diffusion Models},
    author  = {Chitwan Saharia and William Chan and Huiwen Chang and Chris A. Lee and Jonathan Ho and Tim Salimans and David J. Fleet and Mohammad Norouzi},
    journal = {ArXiv},
    year    = {2021},
    volume  = {abs/2111.05826}
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">Saharia2021PaletteID</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Palette: Image-to-Image Diffusion Models<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Chitwan Saharia and William Chan and Huiwen Chang and Chris A. Lee and Jonathan Ho and Tim Salimans and David J. Fleet and Mohammad Norouzi<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>ArXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2021<span class="pl-pds">}</span></span>,
    <span class="pl-s">volume</span>  = <span class="pl-s"><span class="pl-pds">{</span>abs/2111.05826<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{Lugmayr2022RePaintIU,
    title   = {RePaint: Inpainting using Denoising Diffusion Probabilistic Models},
    author  = {Andreas Lugmayr and Martin Danelljan and Andr{\'e}s Romero and Fisher Yu and Radu Timofte and Luc Van Gool},
    journal = {ArXiv},
    year    = {2022},
    volume  = {abs/2201.09865}
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">Lugmayr2022RePaintIU</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>RePaint: Inpainting using Denoising Diffusion Probabilistic Models<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Andreas Lugmayr and Martin Danelljan and Andr{\'e}s Romero and Fisher Yu and Radu Timofte and Luc Van Gool<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>ArXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2022<span class="pl-pds">}</span></span>,
    <span class="pl-s">volume</span>  = <span class="pl-s"><span class="pl-pds">{</span>abs/2201.09865<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@misc{chen2022analog,
    title   = {Analog Bits: Generating Discrete Data using Diffusion Models with Self-Conditioning},
    author  = {Ting Chen and Ruixiang Zhang and Geoffrey Hinton},
    year    = {2022},
    eprint  = {2208.04202},
    archivePrefix = {arXiv},
    primaryClass = {cs.CV}
}"><pre><span class="pl-k">@misc</span>{<span class="pl-en">chen2022analog</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Analog Bits: Generating Discrete Data using Diffusion Models with Self-Conditioning<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Ting Chen and Ruixiang Zhang and Geoffrey Hinton<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2022<span class="pl-pds">}</span></span>,
    <span class="pl-s">eprint</span>  = <span class="pl-s"><span class="pl-pds">{</span>2208.04202<span class="pl-pds">}</span></span>,
    <span class="pl-s">archivePrefix</span> = <span class="pl-s"><span class="pl-pds">{</span>arXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">primaryClass</span> = <span class="pl-s"><span class="pl-pds">{</span>cs.CV<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{Qiao2019WeightS,
    title   = {Weight Standardization},
    author  = {Siyuan Qiao and Huiyu Wang and Chenxi Liu and Wei Shen and Alan Loddon Yuille},
    journal = {ArXiv},
    year    = {2019},
    volume  = {abs/1903.10520}
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">Qiao2019WeightS</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Weight Standardization<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Siyuan Qiao and Huiyu Wang and Chenxi Liu and Wei Shen and Alan Loddon Yuille<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>ArXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2019<span class="pl-pds">}</span></span>,
    <span class="pl-s">volume</span>  = <span class="pl-s"><span class="pl-pds">{</span>abs/1903.10520<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@inproceedings{rogozhnikov2022einops,
    title   = {Einops: Clear and Reliable Tensor Manipulations with Einstein-like Notation},
    author  = {Alex Rogozhnikov},
    booktitle = {International Conference on Learning Representations},
    year    = {2022},
    url     = {https://openreview.net/forum?id=oapKSVM2bcj}
}"><pre><span class="pl-k">@inproceedings</span>{<span class="pl-en">rogozhnikov2022einops</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Einops: Clear and Reliable Tensor Manipulations with Einstein-like Notation<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Alex Rogozhnikov<span class="pl-pds">}</span></span>,
    <span class="pl-s">booktitle</span> = <span class="pl-s"><span class="pl-pds">{</span>International Conference on Learning Representations<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2022<span class="pl-pds">}</span></span>,
    <span class="pl-s">url</span>     = <span class="pl-s"><span class="pl-pds">{</span>https://openreview.net/forum?id=oapKSVM2bcj<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{Sunkara2022NoMS,
    title   = {No More Strided Convolutions or Pooling: A New CNN Building Block for Low-Resolution Images and Small Objects},
    author  = {Raja Sunkara and Tie Luo},
    journal = {ArXiv},
    year    = {2022},
    volume  = {abs/2208.03641}
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">Sunkara2022NoMS</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>No More Strided Convolutions or Pooling: A New CNN Building Block for Low-Resolution Images and Small Objects<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Raja Sunkara and Tie Luo<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>ArXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2022<span class="pl-pds">}</span></span>,
    <span class="pl-s">volume</span>  = <span class="pl-s"><span class="pl-pds">{</span>abs/2208.03641<span class="pl-pds">}</span></span>
}</pre></div>
<div class="highlight highlight-text-bibtex notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="@article{Salimans2022ProgressiveDF,
    title   = {Progressive Distillation for Fast Sampling of Diffusion Models},
    author  = {Tim Salimans and Jonathan Ho},
    journal = {ArXiv},
    year    = {2022},
    volume  = {abs/2202.00512}
}"><pre><span class="pl-k">@article</span>{<span class="pl-en">Salimans2022ProgressiveDF</span>,
    <span class="pl-s">title</span>   = <span class="pl-s"><span class="pl-pds">{</span>Progressive Distillation for Fast Sampling of Diffusion Models<span class="pl-pds">}</span></span>,
    <span class="pl-s">author</span>  = <span class="pl-s"><span class="pl-pds">{</span>Tim Salimans and Jonathan Ho<span class="pl-pds">}</span></span>,
    <span class="pl-s">journal</span> = <span class="pl-s"><span class="pl-pds">{</span>ArXiv<span class="pl-pds">}</span></span>,
    <span class="pl-s">year</span>    = <span class="pl-s"><span class="pl-pds">{</span>2022<span class="pl-pds">}</span></span>,
    <span class="pl-s">volume</span>  = <span class="pl-s"><span class="pl-pds">{</span>abs/2202.00512<span class="pl-pds">}</span></span>
}</pre></div>
<p dir="auto"><em>Creating noise from data is easy; creating data from noise is generative modeling.</em> - <a href="https://arxiv.org/abs/2011.13456" rel="nofollow">Yang Song's paper</a></p>
</article></div></div></div></div></div></div></div><div class="prc-PageLayout-PaneWrapper-pHPop pr-2" style="--offset-header:0px;--spacing-row:var(--spacing-none);--spacing-column:var(--spacing-none)" data-is-hidden="false" data-position="end"><div class="prc-PageLayout-HorizontalDivider-JLVqp prc-PageLayout-PaneHorizontalDivider-9tbnE" data-variant-narrow="none" data-variant-regular="none" data-position="end" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div><div class="prc-PageLayout-Pane-AyzHK" style="--spacing:var(--spacing-normal);--pane-min-width:256px;--pane-max-width:calc(100vw - var(--pane-max-width-diff));--pane-width-size:var(--pane-width-large);--pane-width:320px"><rails-partial data-partial-name="codeViewRepoRoute.Sidebar" class="RailsPartial-module__d-contents__G5m4w">

<div class="BorderGrid ">
  <div class="BorderGrid-row">
    <div class="BorderGrid-cell">
      <div class="hide-sm hide-md">
  <h2 class="tmp-mb-3 h4">About</h2>

      <p class="f4 tmp-my-3">
        Implementation of DALL-E 2, OpenAI's updated text-to-image synthesis neural network, in Pytorch
      </p>

    <h3 class="sr-only">Topics</h3>
    <div class="tmp-my-3">
        <div class="f6">
      <a href="/topics/deep-learning" title="Topic: deep-learning" data-view-component="true" class="topic-tag topic-tag-link">
  deep-learning
</a>
      <a href="/topics/artificial-intelligence" title="Topic: artificial-intelligence" data-view-component="true" class="topic-tag topic-tag-link">
  artificial-intelligence
</a>
      <a href="/topics/text-to-image" title="Topic: text-to-image" data-view-component="true" class="topic-tag topic-tag-link">
  text-to-image
</a>
  </div>

    </div>

    <h3 class="sr-only">Resources</h3>
    <div class="mt-2">
      <a class="Link--muted" data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:readme&quot;}" href="#readme-ov-file">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book mr-2 tmp-mr-2">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        Readme
</a>    </div>

  
    <h3 class="sr-only">License</h3>
  <div class="mt-2">
    <a href="#MIT-1-ov-file"
      class="Link--muted"
      
      data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:license&quot;}"
    >
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-law mr-1 mr-sm-1 mr-md-2 mr-lg-2">
    <path d="M8.75.75V2h.985c.304 0 .603.08.867.231l1.29.736c.038.022.08.033.124.033h2.234a.75.75 0 0 1 0 1.5h-.427l2.111 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.006.005-.01.01-.045.04c-.21.176-.441.327-.686.45C14.556 10.78 13.88 11 13 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L12.178 4.5h-.162c-.305 0-.604-.079-.868-.231l-1.29-.736a.245.245 0 0 0-.124-.033H8.75V13h2.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1 0-1.5h2.5V3.5h-.984a.245.245 0 0 0-.124.033l-1.289.737c-.265.15-.564.23-.869.23h-.162l2.112 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.016.015-.045.04c-.21.176-.441.327-.686.45C4.556 10.78 3.88 11 3 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L2.178 4.5H1.75a.75.75 0 0 1 0-1.5h2.234a.249.249 0 0 0 .125-.033l1.288-.737c.265-.15.564-.23.869-.23h.984V.75a.75.75 0 0 1 1.5 0Zm2.945 8.477c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327Zm-10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327Z"></path>
</svg>
     MIT license
    </a>
  </div>






  <include-fragment src="/lucidrains/DALLE2-pytorch/hovercards/citation/sidebar_partial?tree_name=main" data-nonce="v2:2794b2bc-e069-7a37-3ae9-05ff3bb3b6f8" data-view-component="true">
  

  <div data-show-on-forbidden-error hidden>
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true" class="blankslate-description">        <p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="" aria-label="Please reload this page">Please reload this page</a>.</p>
</p>

</div>  </div>
</div>  </div>
</include-fragment>
    <div class="mt-2">
      <a href="/lucidrains/DALLE2-pytorch/activity" data-view-component="true" class="Link Link--muted"><svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pulse mr-2 tmp-mr-2">
    <path d="M6 2c.306 0 .582.187.696.471L10 10.731l1.304-3.26A.751.751 0 0 1 12 7h3.25a.75.75 0 0 1 0 1.5h-2.742l-1.812 4.528a.751.751 0 0 1-1.392 0L6 4.77 4.696 8.03A.75.75 0 0 1 4 8.5H.75a.75.75 0 0 1 0-1.5h2.742l1.812-4.529A.751.751 0 0 1 6 2Z"></path>
</svg>
        <span class="color-fg-muted">Activity</span></a>    </div>


    <h3 class="sr-only">Stars</h3>
    <div class="mt-2">
      <a href="/lucidrains/DALLE2-pytorch/stargazers" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-2 tmp-mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        <strong>11.3k</strong>
        stars</a>    </div>

    <h3 class="sr-only">Watchers</h3>
    <div class="mt-2">
      <a href="/lucidrains/DALLE2-pytorch/watchers" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye mr-2 tmp-mr-2">
    <path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path>
</svg>
        <strong>119</strong>
        watching</a>    </div>

    <h3 class="sr-only">Forks</h3>
    <div class="mt-2">
      <a href="/lucidrains/DALLE2-pytorch/forks" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2 tmp-mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
        <strong>1.1k</strong>
        forks</a>    </div>


    <div class="mt-2">
      <a class="Link--muted" href="/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Flucidrains%2FDALLE2-pytorch&amp;report=lucidrains+%28user%29">
          Report repository
</a>    </div>
</div>

    </div>
  </div>

  
      <div class="BorderGrid-row">
        <div class="BorderGrid-cell">
          <h2 class="h4 tmp-mb-3" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
  <a href="/lucidrains/DALLE2-pytorch/releases" data-view-component="true" class="Link--primary no-underline Link">Releases
      <span title="346" data-view-component="true" class="Counter">346</span></a></h2>

  <a class="Link--primary d-flex no-underline" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/lucidrains/DALLE2-pytorch/releases/tag/1.15.6">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tag flex-shrink-0 mt-1 tmp-mt-1 color-fg-success">
    <path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path>
</svg>
    <div class="ml-2 min-width-0">
      <div class="d-flex">
        <span class="css-truncate css-truncate-target text-bold mr-2" style="max-width: none;">1.15.6</span>
        <span title="Label: Latest" data-view-component="true" class="Label Label--success flex-shrink-0">
          Latest
</span>      </div>
      <div class="text-small color-fg-muted"><relative-time datetime="2023-10-19T04:02:56Z" class="no-wrap">Oct 19, 2023</relative-time></div>
    </div>
</a>    <div data-view-component="true" class="tmp-mt-3">
      <a text="small" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/lucidrains/DALLE2-pytorch/releases" data-view-component="true" class="Link">+ 345 releases</a></div>
        </div>
      </div>

  
      <div class="BorderGrid-row">
        <div class="BorderGrid-cell">
          
<h2 class="h4 tmp-mb-3">Sponsor this project</h2>
<include-fragment aria-busy="true" aria-label="Loading sponsorable links" src="/lucidrains/DALLE2-pytorch/sponsors_list?block_button=false&amp;current_repository=DALLE2-pytorch" data-nonce="v2:2794b2bc-e069-7a37-3ae9-05ff3bb3b6f8" data-view-component="true">
  
        <ul class="list-style-none">
            <li class="mb-2 d-flex">
              <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
              <div class="Skeleton Skeleton--text flex-1 flex-self-center f4">&nbsp;</div>
            </li>
            <li class="mb-2 d-flex">
              <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
              <div class="Skeleton Skeleton--text flex-1 flex-self-center f4">&nbsp;</div>
            </li>
        </ul>

  <div data-show-on-forbidden-error hidden>
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true" class="blankslate-description">        <p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="" aria-label="Please reload this page">Please reload this page</a>.</p>
</p>

</div>  </div>
</div>  </div>
</include-fragment>  <div class="text-small tmp-mt-3">
    <a href="/sponsors">Learn more about GitHub Sponsors</a>
  </div>

        </div>
      </div>

  
  
      <div class="BorderGrid-row">
        <div class="BorderGrid-cell">
          
<include-fragment aria-busy="true" aria-label="Loading latest packages" src="/lucidrains/DALLE2-pytorch/packages_list?current_repository=DALLE2-pytorch" data-nonce="v2:2794b2bc-e069-7a37-3ae9-05ff3bb3b6f8" data-view-component="true">
  
  <h2 class="h4 tmp-mb-3">
  <a href="/users/lucidrains/packages?repo_name=DALLE2-pytorch" data-view-component="true" class="Link--primary no-underline Link d-flex flex-items-center">Packages
      <span title="0" hidden="hidden" data-view-component="true" class="Counter ml-1 tmp-ml-1">0</span></a></h2>


      <div class="mb-2 d-flex flex-items-center">
        <div class="Skeleton mr-2" style="width:20px;height:20px;"></div>
        <div class="Skeleton Skeleton--text flex-auto">&nbsp;</div>
      </div>
      <div class="mb-2 d-flex flex-items-center">
        <div class="Skeleton mr-2" style="width:20px;height:20px;"></div>
        <div class="Skeleton Skeleton--text flex-auto">&nbsp;</div>
      </div>
      <div class="mb-2 d-flex flex-items-center">
        <div class="Skeleton mr-2" style="width:20px;height:20px;"></div>
        <div class="Skeleton Skeleton--text flex-auto">&nbsp;</div>
      </div>



  <div data-show-on-forbidden-error hidden>
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true" class="blankslate-description">        <p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="" aria-label="Please reload this page">Please reload this page</a>.</p>
</p>

</div>  </div>
</div>  </div>
</include-fragment>
        </div>
      </div>

  
      <div class="BorderGrid-row" hidden>
        <div class="BorderGrid-cell">
          <include-fragment src="/lucidrains/DALLE2-pytorch/used_by_list" accept="text/fragment+html" data-nonce="v2:2794b2bc-e069-7a37-3ae9-05ff3bb3b6f8" data-view-component="true">
  

  <div data-show-on-forbidden-error hidden>
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true" class="blankslate-description">        <p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="" aria-label="Please reload this page">Please reload this page</a>.</p>
</p>

</div>  </div>
</div>  </div>
</include-fragment>
        </div>
      </div>

  
    <div class="BorderGrid-row">
      <div class="BorderGrid-cell">
        <include-fragment aria-busy="true" aria-label="Loading contributors" src="/lucidrains/DALLE2-pytorch/contributors_list?current_repository=DALLE2-pytorch&amp;deferred=true" data-nonce="v2:2794b2bc-e069-7a37-3ae9-05ff3bb3b6f8" data-view-component="true">
  
  <h2 class="h4 tmp-mb-3">
    <a href="/lucidrains/DALLE2-pytorch/graphs/contributors" data-view-component="true" class="Link--primary no-underline Link d-flex flex-items-center">Contributors</a>  </h2>

  <ul class="list-style-none d-flex flex-wrap mb-n2">
      <li class="mb-2">
        <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
      </li>
      <li class="mb-2">
        <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
      </li>
      <li class="mb-2">
        <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
      </li>
  </ul>

  <div data-show-on-forbidden-error hidden>
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true" class="blankslate-description">        <p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="" aria-label="Please reload this page">Please reload this page</a>.</p>
</p>

</div>  </div>
</div>  </div>
</include-fragment>
      </div>
    </div>

  
      <div class="BorderGrid-row">
        <div class="BorderGrid-cell">
          <h2 class="h4 tmp-mb-3">Languages</h2>
<div class="mb-2">
  <span data-view-component="true" class="Progress">
    <span style="background-color:#3572A5 !important;;width: 100.0%;" itemprop="keywords" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
</span></div>
<ul class="list-style-none">
    <li class="d-inline">
        <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small tmp-mr-3" href="/lucidrains/DALLE2-pytorch/search?l=python"  data-ga-click="Repository, language stats search click, location:repo overview">
          <svg style="color:#3572A5;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2 tmp-mr-2">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
          <span class="color-fg-default text-bold mr-1">Python</span>
          <span>100.0%</span>
        </a>
    </li>
</ul>

        </div>
      </div>

  
  </div>
</rails-partial></div><div class="prc-PageLayout-VerticalDivider-9QRmK prc-PageLayout-PaneVerticalDivider-le57g" data-variant-narrow="none" data-variant-regular="none" data-position="end" style="--spacing:var(--spacing-none)"></div></div></div></div></div></div></div></div></div></div></div><div class="ScrollMarksContainer-module__scrollMarksContainer__Eu7uU" id="find-result-marks-container"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA__R_1___">{"resolvedServerColorMode":"day"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer tmp-pt-7 tmp-pb-6 f6 color-fg-muted color-border-subtle p-responsive" role="contentinfo" >
  <h2 class='sr-only'>Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="GitHub Homepage" class="footer-octicon mr-2" href="https://github.com">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M10.226 17.284c-2.965-.36-5.054-2.493-5.054-5.256 0-1.123.404-2.336 1.078-3.144-.292-.741-.247-2.314.09-2.965.898-.112 2.111.36 2.83 1.01.853-.269 1.752-.404 2.853-.404 1.1 0 1.999.135 2.807.382.696-.629 1.932-1.1 2.83-.988.315.606.36 2.179.067 2.942.72.854 1.101 2 1.101 3.167 0 2.763-2.089 4.852-5.098 5.234.763.494 1.28 1.572 1.28 2.807v2.336c0 .674.561 1.056 1.235.786 4.066-1.55 7.255-5.615 7.255-10.646C23.5 6.188 18.334 1 11.978 1 5.62 1 .5 6.188.5 12.545c0 4.986 3.167 9.12 7.435 10.669.606.225 1.19-.18 1.19-.786V20.63a2.9 2.9 0 0 1-1.078.224c-1.483 0-2.359-.808-2.987-2.313-.247-.607-.517-.966-1.034-1.033-.27-.023-.359-.135-.359-.27 0-.27.45-.471.898-.471.652 0 1.213.404 1.797 1.235.45.651.921.943 1.483.943.561 0 .92-.202 1.437-.719.382-.381.674-.718.944-.943"></path>
</svg>
</a>
      <span>
        &copy; 2026 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">


          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to community&quot;,&quot;label&quot;:&quot;text:community&quot;}" href="https://github.community/" data-view-component="true" class="Link--secondary Link">Community</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2" >
  <cookie-consent-link>
    <button
      type="button"
      class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent"
      data-action="click:cookie-consent-link#showConsentManagement"
      data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}"
    >
       Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link>
    <button
      type="button"
      class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent text-left"
      data-action="click:cookie-consent-link#showConsentManagement"
      data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}"
    >
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999"
      data-locale="en"
      data-initial-cookie-consent-allowed=""
      data-cookie-consent-required="false"
    ></ghcc-consent>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden>
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default color-fg-default hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
      </button>
      <div class="octocat-spinner tmp-my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;">
  </div>
</div>

    <template id="snippet-clipboard-copy-button">
  <div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2 tmp-m-2">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2 tmp-m-2">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>
<template id="snippet-clipboard-copy-button-unpositioned">
  <div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>




    </div>
    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true" ></div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  </body>
</html>


# Source: https://docs.together.ai/python-library.md







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

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-primitives-6da842159062d25e.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-9e07ff8eaaaff3a3.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-87aa887446e37f5c.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/github-6e7c458caf1e80bb.css" />
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/repository-6784600ba556c086.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-0eb15370f045c7e0.css" />

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["a11y_status_checks_ruleset","actions_custom_images_public_preview_visibility","actions_custom_images_storage_billing_ui_visibility","actions_image_version_event","agent_session_retry_fetch_capi_on_401","alternate_user_config_repo","arianotify_comprehensive_migration","batch_suggested_changes","cache_issue_labels","codespaces_prebuild_region_target_update","coding_agent_model_selection","coding_agent_model_selection_all_skus","contentful_primer_code_blocks","copilot_3p_agent_hovercards","copilot_agent_snippy","copilot_agent_task_list_v2","copilot_agent_tasks_btn_code_nav","copilot_agent_tasks_btn_code_view","copilot_agent_tasks_btn_code_view_lines","copilot_agent_tasks_btn_repo","copilot_api_agentic_issue_marshal_yaml","copilot_ask_mode_dropdown","copilot_chat_attach_multiple_images","copilot_chat_clear_model_selection_for_default_change","copilot_chat_enable_tool_call_logs","copilot_chat_file_redirect","copilot_chat_input_commands","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_repository_picker","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_cli_install_cta","copilot_code_review_batch_apply_suggestions","copilot_coding_agent_task_response","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_hide_in_dotcom_chat","copilot_extensions_removal_on_marketplace","copilot_features_sql_server_logo","copilot_features_zed_logo","copilot_file_block_ref_matching","copilot_ftp_hyperspace_upgrade_prompt","copilot_icebreakers_experiment_dashboard","copilot_icebreakers_experiment_hyperspace","copilot_immersive_embedded","copilot_immersive_job_result_preview","copilot_immersive_layout_routes","copilot_immersive_structured_model_picker","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_mc_cli_resume_any_users_task","copilot_mission_control_always_send_integration_id","copilot_mission_control_task_alive_updates","copilot_mission_control_use_task_name","copilot_org_policy_page_focus_mode","copilot_redirect_header_button_to_agents","copilot_resource_panel","copilot_scroll_preview_tabs","copilot_share_active_subthread","copilot_spaces_ga","copilot_spaces_individual_policies_ga","copilot_spaces_pagination","copilot_spark_empty_state","copilot_spark_handle_nil_friendly_name","copilot_swe_agent_hide_model_picker_if_only_auto","copilot_swe_agent_pr_comment_model_picker","copilot_swe_agent_use_subagents","copilot_task_api_github_rest_style","copilot_unconfigured_is_inherited","copilot_usage_metrics_ga","copilot_workbench_slim_line_top_tabs","custom_instructions_file_references","custom_properties_consolidate_default_value_input","dashboard_lists_max_age_filter","dashboard_universe_2025_feedback_dialog","disable_soft_navigate_turbo_visit","flex_cta_groups_mvp","global_account_switch_dialog_lazy_load","global_agents_menu_lazy_load","global_create_menu_lazy_load","global_nav_menu_lazy_load","global_nav_react","global_user_menu_lazy_load","hyperspace_2025_logged_out_batch_1","hyperspace_2025_logged_out_batch_2","hyperspace_2025_logged_out_batch_3","initial_per_page_pagination_updates","ipm_global_transactional_message_agents","ipm_global_transactional_message_copilot","ipm_global_transactional_message_issues","ipm_global_transactional_message_prs","ipm_global_transactional_message_repos","ipm_global_transactional_message_spaces","issue_fields_global_search","issue_fields_timeline_events","issues_cca_assign_actor_with_agent","issues_dashboard_inp_optimization","issues_dashboard_semantic_search","issues_diff_based_label_updates","issues_expanded_file_types","issues_index_semantic_search","issues_lazy_load_comment_box_suggestions","issues_react_auto_retry_on_error","issues_react_bots_timeline_pagination","issues_react_chrome_container_query_fix","issues_react_hot_cache","issues_react_low_quality_comment_warning","issues_react_prohibit_title_fallback","issues_react_safari_scroll_preservation","issues_react_use_turbo_for_cross_repo_navigation","issues_service_worker","landing_pages_ninetailed","landing_pages_web_vitals_tracking","lifecycle_label_name_updates","marketing_pages_search_explore_provider","memex_default_issue_create_repository","memex_grouped_by_edit_route","memex_live_update_hovercard","memex_mwl_filter_field_delimiter","merge_status_header_feedback","mission_control_retry_on_401","mission_control_use_body_html","notifications_menu_defer_labels","oauth_authorize_clickjacking_protection","open_agent_session_in_vscode_insiders","open_agent_session_in_vscode_stable","primer_react_css_has_selector_perf","primer_react_spinner_synchronize_animations","prs_conversations_react","prx_merge_status_button_alt_logic","ruleset_deletion_confirmation","sample_network_conn_type","session_logs_ungroup_reasoning_text","site_calculator_actions_2025","site_features_copilot_universe","site_homepage_collaborate_video","spark_prompt_secret_scanning","spark_server_connection_status","suppress_automated_browser_vitals","suppress_non_representative_vitals","viewscreen_sandbox","webp_support","workbench_store_readonly"],"copilotApiOverrideUrl":"https://api.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/high-contrast-cookie-fed1d93364101384.js"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/wp-runtime-170150a692ee9e91.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/28839-734cb6d8a7150172.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/85924-e131bec5f99667e1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/34646-e68f26aaba7f2b0d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/environment-990d83f9bff5b0e9.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/runtime-helpers-3bb6f7d6b7a2f531.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2966-f6796bfd155feae1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/96232-c2cf4a34762f0169.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/41013-7a6deee6d6ff15eb.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/51210-3abb7238871a5b29.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/24387-bc06b4d78bbcd753.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81683-1370179bf9bdc0f0.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/46740-6606b1026a237412.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81751-2c06efb98b9460b1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/github-elements-21691d9353073fe5.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/element-registry-377dc04b8b45b524.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-core-017b3a88b81253a9.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-lib-a4cf89fce9a1300a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/29434-47789cf97f381365.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/79039-2565b539a6ebc09b.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/61110-93cf7706e5dc8bfa.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2887-47ac9a4b8862e6bf.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/26533-2961d590db2a09c3.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/62249-6514db80cf0cc26f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/54195-ca6526f3483e6a6c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/62988-af4811a8532026f8.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/60481-3c7a0fd2336c8106.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/46287-7b500b5354119a88.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2498-7a413c8209222158.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/61075-6d5c1005b38602d6.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/89627-fc3955a85261a02a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/49029-6c429c0e1bbd1e79.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/99328-5e06da57c4622e21.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-7320c3a05a5a8a94.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/react-core.36c3e8b046fb98c7.module.css" />
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/38302-841b0fa97d5950a1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/notifications-global-3413132b6df94f22.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/19262-313c6e4aa6bc1abc.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/32225-0f598a4a1b50cbd4.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/19930-d7474e22a5e73a83.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/codespaces-f5257279c46939d1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/3064-ee1625cf0fbcd858.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/89756-4280abf10da82907.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/99291-6f4866190d0539e5.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/repositories-cb23fff88a2ee8dc.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/34140-bd56b738d77cb446.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/code-menu-34c67a8e6616ccae.js" defer="defer"></script>
  
  <script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/primer-react-827130267d5df3a7.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/octicons-react-6e60bcde38f313de.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/17383-e0b14a829f4de8f1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/68751-fe5cb40b5547c377.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/7463-f34e26efc84a7578.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/15272-00d6ef52b0f88c77.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/32769-329cba91f224b6ee.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/99849-920965235c8ccd0b.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/21122-b3cc5a80945950fe.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/18549-7bd99002ba6af757.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/26557-b8109a166e44c543.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/63991-125a5c660965e63e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/15696-4d46221fddf8f5d2.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/36600-03045adfc5db235d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/66231-e6e39ee93d5d7dba.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/18222-498ac30c45b2263a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/4916-50f2539dc1c5e1ee.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/24787-791cfb59d6b5d03c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/7053-f4bd13214a8bd433.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/17363-e3dd517653b6b9ee.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/95553-f433ba6b36620468.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/34253-adcd4826f66bae4a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/11969-66d44a3037bfb35f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/38227-47594c6970d0b3c2.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/73061-c1057d89c6936e56.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/78683-1f6705f22b21537a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/49972-94c3370fcc3392bd.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/89979-62f8b2fb979df318.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/54709-f80e3a81a32ec27b.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/96306-1f603f3f74fb4d72.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/26497-2bdad8556e409811.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/76936-23e0bc4ddc75cbd8.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2758-4d759125d32a5bed.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/43690-bfbe902f6d657a99.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/code-view-0096c1776f9073c3.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a7c2947c416ec834.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/54709.a5727bcd62ae2219.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/76936.46b8dd328c52f5e0.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/43690.12df5a0fc912c5fa.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-view.2416418ea64a53d6.module.css" />

  <script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/75999-8b712b86e441ee4c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/86065-133936570df95481.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/33684-3f07b96816e44898.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/5289-ff89f2d234909a49.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/16643-84e61880ec91a86e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/notifications-subscriptions-menu-7b04277e360f2edb.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a7c2947c416ec834.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/notifications-subscriptions-menu.3497bc82ea580c5f.module.css" />


  <title>GitHub - togethercomputer/together-py · GitHub</title>



  <meta name="route-pattern" content="/:user_id/:repository" data-turbo-transient>
  <meta name="route-controller" content="files" data-turbo-transient>
  <meta name="route-action" content="disambiguate" data-turbo-transient>
  <meta name="fetch-nonce" content="v2:cb0ba074-d866-cbc2-1501-de97be737629">

    
  <meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb">


  <meta name="request-id" content="DAE2:1D0E8D:3022CE6:308C1D7:69B1EBAE" data-pjax-transient="true"/><meta name="html-safe-nonce" content="9486402914bb07f3854a170df8dde19ecd5451d0918f6b043d4b581d49308702" data-pjax-transient="true"/><meta name="visitor-payload" content="eyJyZWZlcnJlciI6IiIsInJlcXVlc3RfaWQiOiJEQUUyOjFEMEU4RDozMDIyQ0U2OjMwOEMxRDc6NjlCMUVCQUUiLCJ2aXNpdG9yX2lkIjoiODczNzExNjc0OTI3NTcyMDYyMiIsInJlZ2lvbl9lZGdlIjoic2VhIiwicmVnaW9uX3JlbmRlciI6InNlYSJ9" data-pjax-transient="true"/><meta name="visitor-hmac" content="b92abd32c3d5970d826019e0848ce52c327a0f53a98ac71e53c06c32569c50a0" data-pjax-transient="true"/>


    <meta name="hovercard-subject-tag" content="repository:798597405" data-turbo-transient>


  <meta name="github-keyboard-shortcuts" content="repository,copilot" data-turbo-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-turbo-transient>
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" />





  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;" data-turbo-transient="true" />

  




    <meta name="user-login" content="">

  

    <meta name="viewport" content="width=device-width">

    

      <meta name="description" content="Contribute to togethercomputer/together-py development by creating an account on GitHub.">

      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">

    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/togethercomputer/together-py" />

      <meta name="twitter:image" content="https://opengraph.githubassets.com/7da3de62204d12ad53334900392200e285f9119b06d7e6691bbf693d52014ddf/togethercomputer/together-py" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="GitHub - togethercomputer/together-py" /><meta name="twitter:description" content="Contribute to togethercomputer/together-py development by creating an account on GitHub." />
  <meta property="og:image" content="https://opengraph.githubassets.com/7da3de62204d12ad53334900392200e285f9119b06d7e6691bbf693d52014ddf/togethercomputer/together-py" /><meta property="og:image:alt" content="Contribute to togethercomputer/together-py development by creating an account on GitHub." /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="GitHub - togethercomputer/together-py" /><meta property="og:url" content="https://github.com/togethercomputer/together-py" /><meta property="og:description" content="Contribute to togethercomputer/together-py development by creating an account on GitHub." />
  




      <meta name="hostname" content="github.com">



        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="48fa4b9ec5f46ad465f20fab2b215efca3de382caa60e03070e82e48616e6767" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="568c098497d98702bac1642a2a853732a047a6ced28eabd3e15d50041a890235" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="29efb9e0d90eec5f00934d16427f39c7d64ef9893cd48ec5de0eea0e48234ad7" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="61b09dd1922a5e823a5044a867560e20c9df6340a0a9081714b76007f1f86af1" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient>

    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/togethercomputer/together-py git https://github.com/togethercomputer/together-py.git">

  <meta name="octolytics-dimension-user_id" content="109101822" /><meta name="octolytics-dimension-user_login" content="togethercomputer" /><meta name="octolytics-dimension-repository_id" content="798597405" /><meta name="octolytics-dimension-repository_nwo" content="togethercomputer/together-py" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="798597405" /><meta name="octolytics-dimension-repository_network_root_nwo" content="togethercomputer/together-py" />



    

    <meta name="turbo-body-classes" content="logged-out env-production page-responsive">
  <meta name="disable-turbo" content="false">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="release" content="0e3a431ea2be3a1bee18cfc32e180968f2e7380f">
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
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a7c2947c416ec834.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/keyboard-shortcuts-dialog.24804fee9fc98092.module.css" />

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
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/93308-c21d6ff736807846.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/sessions-e5a020fb258986c3.js" defer="defer"></script>

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
        <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="js-details-target js-nav-padding-recalculate js-header-menu-toggle Button--link Button--medium Button d-lg-none color-fg-inherit p-1">  <span class="Button-content">
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
    <path d="M10.303 16.652c-2.837-.344-4.835-2.385-4.835-5.028 0-1.074.387-2.235 1.031-3.008-.279-.709-.236-2.214.086-2.837.86-.107 2.02.344 2.708.967.816-.258 1.676-.386 2.728-.386 1.053 0 1.913.128 2.686.365.666-.602 1.848-1.053 2.708-.946.3.581.344 2.085.064 2.815.688.817 1.053 1.913 1.053 3.03 0 2.643-1.998 4.641-4.877 5.006.73.473 1.224 1.504 1.224 2.686v2.235c0 .644.537 1.01 1.182.752 3.889-1.483 6.94-5.372 6.94-10.185 0-6.081-4.942-11.044-11.022-11.044-6.081 0-10.98 4.963-10.98 11.044a10.84 10.84 0 0 0 7.112 10.206c.58.215 1.139-.172 1.139-.752v-1.719a2.768 2.768 0 0 1-1.032.215c-1.418 0-2.256-.773-2.857-2.213-.237-.58-.495-.924-.989-.988-.258-.022-.344-.129-.344-.258 0-.258.43-.451.86-.451.623 0 1.16.386 1.719 1.181.43.623.881.903 1.418.903.537 0 .881-.194 1.375-.688.365-.365.645-.687.903-.902Z"></path>
</svg>
      </a>

      <div class="d-flex flex-1 flex-order-2 text-right d-lg-none gap-2 flex-justify-end">
          <a
            href="/login?return_to=https%3A%2F%2Fgithub.com%2Ftogethercomputer%2Ftogether-py"
            class="HeaderMenu-link HeaderMenu-button d-inline-flex f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit js-prevent-focus-on-mobile-nav"
            data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/togethercomputer/together-py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="6f375c3f7cbd4df859df52b05863d4e82de64712156d77809baff31d58d49483"
            data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to Sign in&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}"
          >
            Sign in
          </a>
              <div class="AppHeader-appearanceSettings">
    <react-partial-anchor>
      <button data-target="react-partial-anchor.anchor" id="icon-button-20173381-ea54-444e-947a-f76b3bb50b46" aria-labelledby="tooltip-e403288d-a3d1-47eb-9fae-83d163f986d7" type="button" disabled="disabled" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium AppHeader-button HeaderMenu-link border cursor-wait">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sliders Button-visual">
    <path d="M15 2.75a.75.75 0 0 1-.75.75h-4a.75.75 0 0 1 0-1.5h4a.75.75 0 0 1 .75.75Zm-8.5.75v1.25a.75.75 0 0 0 1.5 0v-4a.75.75 0 0 0-1.5 0V2H1.75a.75.75 0 0 0 0 1.5H6.5Zm1.25 5.25a.75.75 0 0 0 0-1.5h-6a.75.75 0 0 0 0 1.5h6ZM15 8a.75.75 0 0 1-.75.75H11.5V10a.75.75 0 1 1-1.5 0V6a.75.75 0 0 1 1.5 0v1.25h2.75A.75.75 0 0 1 15 8Zm-9 5.25v-2a.75.75 0 0 0-1.5 0v1.25H1.75a.75.75 0 0 0 0 1.5H4.5v1.25a.75.75 0 0 0 1.5 0v-2Zm9 0a.75.75 0 0 1-.75.75h-6a.75.75 0 0 1 0-1.5h6a.75.75 0 0 1 .75.75Z"></path>
</svg>
</button><tool-tip id="tooltip-e403288d-a3d1-47eb-9fae-83d163f986d7" for="icon-button-20173381-ea54-444e-947a-f76b3bb50b46" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Appearance settings</tool-tip>

      <template data-target="react-partial-anchor.template">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a7c2947c416ec834.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/appearance-settings.437ba0a52997e5dd.module.css" />

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
            <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a7c2947c416ec834.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/marketing-navigation.081eee98a5812e77.module.css" />

<react-partial
  partial-name="marketing-navigation"
  data-ssr="true"
  data-attempted-ssr="true"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"should_use_dotcom_links":true}}</script>
  <div data-target="react-partial.reactRoot"><nav class="MarketingNavigation-module__nav__W0KYY" aria-label="Global"><ul class="MarketingNavigation-module__list__tFbMb"><li><div class="NavDropdown-module__container__l2YeI js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button__PEHWX js-details-target" aria-expanded="false">Platform<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">AI CODE CREATION</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/features/copilot" data-analytics-event="{&quot;action&quot;:&quot;github_copilot&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_copilot_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Copilot</span><span class="NavLink-module__subtitle__X4gkW">Write better code with AI</span></div></a></li><li><a href="https://github.com/features/spark" data-analytics-event="{&quot;action&quot;:&quot;github_spark&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_spark_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-sparkle-fill NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.296 1.924c.24-.656 1.168-.656 1.408 0l.717 1.958a11.25 11.25 0 0 0 6.697 6.697l1.958.717c.657.24.657 1.168 0 1.408l-1.958.717a11.25 11.25 0 0 0-6.697 6.697l-.717 1.958c-.24.657-1.168.657-1.408 0l-.717-1.958a11.25 11.25 0 0 0-6.697-6.697l-1.958-.717c-.656-.24-.656-1.168 0-1.408l1.958-.717a11.25 11.25 0 0 0 6.697-6.697l.717-1.958Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Spark</span><span class="NavLink-module__subtitle__X4gkW">Build and deploy intelligent apps</span></div></a></li><li><a href="https://github.com/features/models" data-analytics-event="{&quot;action&quot;:&quot;github_models&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_models_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-ai-model NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M19.375 8.5a3.25 3.25 0 1 1-3.163 4h-3a3.252 3.252 0 0 1-4.443 2.509L7.214 17.76a3.25 3.25 0 1 1-1.342-.674l1.672-2.957A3.238 3.238 0 0 1 6.75 12c0-.907.371-1.727.97-2.316L6.117 6.846A3.253 3.253 0 0 1 1.875 3.75a3.25 3.25 0 1 1 5.526 2.32l1.603 2.836A3.25 3.25 0 0 1 13.093 11h3.119a3.252 3.252 0 0 1 3.163-2.5ZM10 10.25a1.75 1.75 0 1 0-.001 3.499A1.75 1.75 0 0 0 10 10.25ZM5.125 2a1.75 1.75 0 1 0 0 3.5 1.75 1.75 0 0 0 0-3.5Zm12.5 9.75a1.75 1.75 0 1 0 3.5 0 1.75 1.75 0 0 0-3.5 0Zm-14.25 8.5a1.75 1.75 0 1 0 3.501-.001 1.75 1.75 0 0 0-3.501.001Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Models</span><span class="NavLink-module__subtitle__X4gkW">Manage and compare prompts</span></div></a></li><li><a href="https://github.com/mcp" data-analytics-event="{&quot;action&quot;:&quot;mcp_registry&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;mcp_registry_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-mcp NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.795 1.694a4.287 4.287 0 0 1 6.061 0 4.28 4.28 0 0 1 1.181 3.819 4.282 4.282 0 0 1 3.819 1.181 4.287 4.287 0 0 1 0 6.061l-6.793 6.793a.249.249 0 0 0 0 .353l2.617 2.618a.75.75 0 1 1-1.061 1.061l-2.617-2.618a1.75 1.75 0 0 1 0-2.475l6.793-6.793a2.785 2.785 0 1 0-3.939-3.939l-5.9 5.9a.734.734 0 0 1-.249.165.749.749 0 0 1-.812-1.225l5.9-5.901a2.785 2.785 0 1 0-3.939-3.939L2.931 10.68A.75.75 0 1 1 1.87 9.619l7.925-7.925Z"></path><path d="M12.42 4.069a.752.752 0 0 1 1.061 0 .752.752 0 0 1 0 1.061L7.33 11.28a2.788 2.788 0 0 0 0 3.94 2.788 2.788 0 0 0 3.94 0l6.15-6.151a.752.752 0 0 1 1.061 0 .752.752 0 0 1 0 1.061l-6.151 6.15a4.285 4.285 0 1 1-6.06-6.06l6.15-6.151Z"></path></svg><span class="NavLink-module__title__Q7t0p">MCP Registry<sup class="NavLink-module__label__bil7n">New</sup></span><span class="NavLink-module__subtitle__X4gkW">Integrate external tools</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">DEVELOPER WORKFLOWS</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/features/actions" data-analytics-event="{&quot;action&quot;:&quot;actions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;actions_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-workflow NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 3a2 2 0 0 1 2-2h6.5a2 2 0 0 1 2 2v6.5a2 2 0 0 1-2 2H7v4.063C7 16.355 7.644 17 8.438 17H12.5v-2.5a2 2 0 0 1 2-2H21a2 2 0 0 1 2 2V21a2 2 0 0 1-2 2h-6.5a2 2 0 0 1-2-2v-2.5H8.437A2.939 2.939 0 0 1 5.5 15.562V11.5H3a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v6.5a.5.5 0 0 0 .5.5h6.5a.5.5 0 0 0 .5-.5V3a.5.5 0 0 0-.5-.5ZM14.5 14a.5.5 0 0 0-.5.5V21a.5.5 0 0 0 .5.5H21a.5.5 0 0 0 .5-.5v-6.5a.5.5 0 0 0-.5-.5Z"></path></svg><span class="NavLink-module__title__Q7t0p">Actions</span><span class="NavLink-module__subtitle__X4gkW">Automate any workflow</span></div></a></li><li><a href="https://github.com/features/codespaces" data-analytics-event="{&quot;action&quot;:&quot;codespaces&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;codespaces_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-codespaces NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.5 3.75C3.5 2.784 4.284 2 5.25 2h13.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 18.75 13H5.25a1.75 1.75 0 0 1-1.75-1.75Zm-2 12c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v4a1.75 1.75 0 0 1-1.75 1.75H3.25a1.75 1.75 0 0 1-1.75-1.75ZM5.25 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h13.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Zm-2 12a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h17.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25Z"></path><path d="M10 17.75a.75.75 0 0 1 .75-.75h6.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path></svg><span class="NavLink-module__title__Q7t0p">Codespaces</span><span class="NavLink-module__subtitle__X4gkW">Instant dev environments</span></div></a></li><li><a href="https://github.com/features/issues" data-analytics-event="{&quot;action&quot;:&quot;issues&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;issues_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M12 1c6.075 0 11 4.925 11 11s-4.925 11-11 11S1 18.075 1 12 5.925 1 12 1ZM2.5 12a9.5 9.5 0 0 0 9.5 9.5 9.5 9.5 0 0 0 9.5-9.5A9.5 9.5 0 0 0 12 2.5 9.5 9.5 0 0 0 2.5 12Zm9.5 2a2 2 0 1 1-.001-3.999A2 2 0 0 1 12 14Z"></path></svg><span class="NavLink-module__title__Q7t0p">Issues</span><span class="NavLink-module__subtitle__X4gkW">Plan and track work</span></div></a></li><li><a href="https://github.com/features/code-review" data-analytics-event="{&quot;action&quot;:&quot;code_review&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;code_review_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-code NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M15.22 4.97a.75.75 0 0 1 1.06 0l6.5 6.5a.75.75 0 0 1 0 1.06l-6.5 6.5a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L21.19 12l-5.97-5.97a.75.75 0 0 1 0-1.06Zm-6.44 0a.75.75 0 0 1 0 1.06L2.81 12l5.97 5.97a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-6.5-6.5a.75.75 0 0 1 0-1.06l6.5-6.5a.75.75 0 0 1 1.06 0Z"></path></svg><span class="NavLink-module__title__Q7t0p">Code Review</span><span class="NavLink-module__subtitle__X4gkW">Manage code changes</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">APPLICATION SECURITY</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/security/advanced-security" data-analytics-event="{&quot;action&quot;:&quot;github_advanced_security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_advanced_security_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-shield-check NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Advanced Security</span><span class="NavLink-module__subtitle__X4gkW">Find and fix vulnerabilities</span></div></a></li><li><a href="https://github.com/security/advanced-security/code-security" data-analytics-event="{&quot;action&quot;:&quot;code_security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;code_security_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-code-square NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.3 8.24a.75.75 0 0 1-.04 1.06L7.352 12l2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M2 3.75C2 2.784 2.784 2 3.75 2h16.5c.966 0 1.75.784 1.75 1.75v16.5A1.75 1.75 0 0 1 20.25 22H3.75A1.75 1.75 0 0 1 2 20.25Zm1.75-.25a.25.25 0 0 0-.25.25v16.5c0 .138.112.25.25.25h16.5a.25.25 0 0 0 .25-.25V3.75a.25.25 0 0 0-.25-.25Z"></path></svg><span class="NavLink-module__title__Q7t0p">Code security</span><span class="NavLink-module__subtitle__X4gkW">Secure your code as you build</span></div></a></li><li><a href="https://github.com/security/advanced-security/secret-protection" data-analytics-event="{&quot;action&quot;:&quot;secret_protection&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;secret_protection_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-lock NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6 9V7.25C6 3.845 8.503 1 12 1s6 2.845 6 6.25V9h.5a2.5 2.5 0 0 1 2.5 2.5v8a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 19.5v-8A2.5 2.5 0 0 1 5.5 9Zm-1.5 2.5v8a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1v-8a1 1 0 0 0-1-1h-13a1 1 0 0 0-1 1Zm3-4.25V9h9V7.25c0-2.67-1.922-4.75-4.5-4.75-2.578 0-4.5 2.08-4.5 4.75Z"></path></svg><span class="NavLink-module__title__Q7t0p">Secret protection</span><span class="NavLink-module__subtitle__X4gkW">Stop leaks before they start</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ NavGroup-module__hasSeparator__FnMrN"><span class="NavGroup-module__title__Wzxz2">EXPLORE</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/why-github" data-analytics-event="{&quot;action&quot;:&quot;why_github&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;why_github_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Why GitHub</span></a></li><li><a href="https://docs.github.com" data-analytics-event="{&quot;action&quot;:&quot;documentation&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;documentation_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Documentation</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.blog" data-analytics-event="{&quot;action&quot;:&quot;blog&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;blog_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Blog</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.blog/changelog" data-analytics-event="{&quot;action&quot;:&quot;changelog&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;changelog_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Changelog</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.com/marketplace" data-analytics-event="{&quot;action&quot;:&quot;marketplace&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;marketplace_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Marketplace</span></a></li></ul></div></li></ul><div class="NavDropdown-module__trailingLinkContainer__VgJGL"><a href="https://github.com/features" data-analytics-event="{&quot;action&quot;:&quot;view_all_features&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_features_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all features</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></div></div></div></li><li><div class="NavDropdown-module__container__l2YeI js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button__PEHWX js-details-target" aria-expanded="false">Solutions<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">BY COMPANY SIZE</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/enterprise" data-analytics-event="{&quot;action&quot;:&quot;enterprises&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;enterprises_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Enterprises</span></a></li><li><a href="https://github.com/team" data-analytics-event="{&quot;action&quot;:&quot;small_and_medium_teams&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;small_and_medium_teams_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Small and medium teams</span></a></li><li><a href="https://github.com/enterprise/startups" data-analytics-event="{&quot;action&quot;:&quot;startups&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;startups_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Startups</span></a></li><li><a href="https://github.com/solutions/industry/nonprofits" data-analytics-event="{&quot;action&quot;:&quot;nonprofits&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;nonprofits_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Nonprofits</span></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">BY USE CASE</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/solutions/use-case/app-modernization" data-analytics-event="{&quot;action&quot;:&quot;app_modernization&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;app_modernization_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">App Modernization</span></a></li><li><a href="https://github.com/solutions/use-case/devsecops" data-analytics-event="{&quot;action&quot;:&quot;devsecops&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;devsecops_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">DevSecOps</span></a></li><li><a href="https://github.com/solutions/use-case/devops" data-analytics-event="{&quot;action&quot;:&quot;devops&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;devops_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">DevOps</span></a></li><li><a href="https://github.com/solutions/use-case/ci-cd" data-analytics-event="{&quot;action&quot;:&quot;ci/cd&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;ci/cd_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">CI/CD</span></a></li><li><a href="https://github.com/solutions/use-case" data-analytics-event="{&quot;action&quot;:&quot;view_all_use_cases&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_use_cases_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all use cases</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">BY INDUSTRY</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/solutions/industry/healthcare" data-analytics-event="{&quot;action&quot;:&quot;healthcare&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;healthcare_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Healthcare</span></a></li><li><a href="https://github.com/solutions/industry/financial-services" data-analytics-event="{&quot;action&quot;:&quot;financial_services&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;financial_services_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Financial services</span></a></li><li><a href="https://github.com/solutions/industry/manufacturing" data-analytics-event="{&quot;action&quot;:&quot;manufacturing&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;manufacturing_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Manufacturing</span></a></li><li><a href="https://github.com/solutions/industry/government" data-analytics-event="{&quot;action&quot;:&quot;government&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;government_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Government</span></a></li><li><a href="https://github.com/solutions/industry" data-analytics-event="{&quot;action&quot;:&quot;view_all_industries&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_industries_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all industries</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></li></ul></div></li></ul><div class="NavDropdown-module__trailingLinkContainer__VgJGL"><a href="https://github.com/solutions" data-analytics-event="{&quot;action&quot;:&quot;view_all_solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_solutions_link_solutions_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all solutions</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></div></div></div></li><li><div class="NavDropdown-module__container__l2YeI js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button__PEHWX js-details-target" aria-expanded="false">Resources<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">EXPLORE BY TOPIC</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/resources/articles?topic=ai" data-analytics-event="{&quot;action&quot;:&quot;ai&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;ai_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">AI</span></a></li><li><a href="https://github.com/resources/articles?topic=software-development" data-analytics-event="{&quot;action&quot;:&quot;software_development&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;software_development_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Software Development</span></a></li><li><a href="https://github.com/resources/articles?topic=devops" data-analytics-event="{&quot;action&quot;:&quot;devops&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;devops_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">DevOps</span></a></li><li><a href="https://github.com/resources/articles?topic=security" data-analytics-event="{&quot;action&quot;:&quot;security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;security_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Security</span></a></li><li><a href="https://github.com/resources/articles" data-analytics-event="{&quot;action&quot;:&quot;view_all_topics&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_topics_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all topics</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">EXPLORE BY TYPE</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/customer-stories" data-analytics-event="{&quot;action&quot;:&quot;customer_stories&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;customer_stories_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Customer stories</span></a></li><li><a href="https://github.com/resources/events" data-analytics-event="{&quot;action&quot;:&quot;events__webinars&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;events__webinars_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Events &amp; webinars</span></a></li><li><a href="https://github.com/resources/whitepapers" data-analytics-event="{&quot;action&quot;:&quot;ebooks__reports&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;ebooks__reports_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Ebooks &amp; reports</span></a></li><li><a href="https://github.com/solutions/executive-insights" data-analytics-event="{&quot;action&quot;:&quot;business_insights&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;business_insights_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Business insights</span></a></li><li><a href="https://skills.github.com" data-analytics-event="{&quot;action&quot;:&quot;github_skills&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_skills_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">GitHub Skills</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">SUPPORT &amp; SERVICES</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://docs.github.com" data-analytics-event="{&quot;action&quot;:&quot;documentation&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;documentation_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Documentation</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://support.github.com" data-analytics-event="{&quot;action&quot;:&quot;customer_support&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;customer_support_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Customer support</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.com/orgs/community/discussions" data-analytics-event="{&quot;action&quot;:&quot;community_forum&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;community_forum_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Community forum</span></a></li><li><a href="https://github.com/trust-center" data-analytics-event="{&quot;action&quot;:&quot;trust_center&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;trust_center_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Trust center</span></a></li><li><a href="https://github.com/partners" data-analytics-event="{&quot;action&quot;:&quot;partners&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;partners_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Partners</span></a></li></ul></div></li></ul><div class="NavDropdown-module__trailingLinkContainer__VgJGL"><a href="https://github.com/resources" data-analytics-event="{&quot;action&quot;:&quot;view_all_resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_resources_link_resources_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">View all resources</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon__amekg" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></div></div></div></li><li><div class="NavDropdown-module__container__l2YeI js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button__PEHWX js-details-target" aria-expanded="false">Open Source<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">COMMUNITY</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/sponsors" data-analytics-event="{&quot;action&quot;:&quot;github_sponsors&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_sponsors_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-sponsor-tiers NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M16.004 1.25C18.311 1.25 20 3.128 20 5.75c0 2.292-1.23 4.464-3.295 6.485-.481.47-.98.909-1.482 1.31l.265 1.32 1.375 7.5a.75.75 0 0 1-.982.844l-3.512-1.207a.75.75 0 0 0-.488 0L8.37 23.209a.75.75 0 0 1-.982-.844l1.378-7.512.261-1.309c-.5-.4-1-.838-1.481-1.31C5.479 10.215 4.25 8.043 4.25 5.75c0-2.622 1.689-4.5 3.996-4.5 1.55 0 2.947.752 3.832 1.967l.047.067.047-.067a4.726 4.726 0 0 1 3.612-1.962l.22-.005ZM13.89 14.531c-.418.285-.828.542-1.218.77l-.18.103a.75.75 0 0 1-.734 0l-.071-.04-.46-.272c-.282-.173-.573-.36-.868-.562l-.121.605-1.145 6.239 2.3-.79a2.248 2.248 0 0 1 1.284-.054l.18.053 2.299.79-1.141-6.226-.125-.616ZM16.004 2.75c-1.464 0-2.731.983-3.159 2.459-.209.721-1.231.721-1.44 0-.428-1.476-1.695-2.459-3.16-2.459-1.44 0-2.495 1.173-2.495 3 0 1.811 1.039 3.647 2.844 5.412a19.624 19.624 0 0 0 3.734 2.84l-.019-.011-.184-.111.147-.088a19.81 19.81 0 0 0 3.015-2.278l.37-.352C17.46 9.397 18.5 7.561 18.5 5.75c0-1.827-1.055-3-2.496-3Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Sponsors</span><span class="NavLink-module__subtitle__X4gkW">Fund open source developers</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">PROGRAMS</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://securitylab.github.com" data-analytics-event="{&quot;action&quot;:&quot;security_lab&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;security_lab_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Security Lab</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://maintainers.github.com" data-analytics-event="{&quot;action&quot;:&quot;maintainer_community&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;maintainer_community_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Maintainer Community</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.com/accelerator" data-analytics-event="{&quot;action&quot;:&quot;accelerator&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;accelerator_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Accelerator</span></a></li><li><a href="https://archiveprogram.github.com" data-analytics-event="{&quot;action&quot;:&quot;archive_program&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;archive_program_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4" target="_blank" rel="noreferrer"><span class="NavLink-module__title__Q7t0p">Archive Program</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon__eWIry" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">REPOSITORIES</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/topics" data-analytics-event="{&quot;action&quot;:&quot;topics&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;topics_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Topics</span></a></li><li><a href="https://github.com/trending" data-analytics-event="{&quot;action&quot;:&quot;trending&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;trending_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Trending</span></a></li><li><a href="https://github.com/collections" data-analytics-event="{&quot;action&quot;:&quot;collections&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;collections_link_open_source_navbar&quot;}" class="NavLink-module__link__EG3d4"><span class="NavLink-module__title__Q7t0p">Collections</span></a></li></ul></div></li></ul></div></div></li><li><div class="NavDropdown-module__container__l2YeI js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button__PEHWX js-details-target" aria-expanded="false">Enterprise<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">ENTERPRISE SOLUTIONS</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/enterprise" data-analytics-event="{&quot;action&quot;:&quot;enterprise_platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;enterprise_platform_link_enterprise_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-stack NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.063 1.456a1.749 1.749 0 0 1 1.874 0l8.383 5.316a1.751 1.751 0 0 1 0 2.956l-8.383 5.316a1.749 1.749 0 0 1-1.874 0L2.68 9.728a1.751 1.751 0 0 1 0-2.956Zm1.071 1.267a.25.25 0 0 0-.268 0L3.483 8.039a.25.25 0 0 0 0 .422l8.383 5.316a.25.25 0 0 0 .268 0l8.383-5.316a.25.25 0 0 0 0-.422Z"></path><path d="M1.867 12.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path><path d="M1.867 16.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path></svg><span class="NavLink-module__title__Q7t0p">Enterprise platform</span><span class="NavLink-module__subtitle__X4gkW">AI-powered developer platform</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2">AVAILABLE ADD-ONS</span><ul class="NavGroup-module__list__UCOFy"><li><a href="https://github.com/security/advanced-security" data-analytics-event="{&quot;action&quot;:&quot;github_advanced_security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_advanced_security_link_enterprise_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-shield-check NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Advanced Security</span><span class="NavLink-module__subtitle__X4gkW">Enterprise-grade security features</span></div></a></li><li><a href="https://github.com/features/copilot/copilot-business" data-analytics-event="{&quot;action&quot;:&quot;copilot_for_business&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;copilot_for_business_link_enterprise_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path></svg><span class="NavLink-module__title__Q7t0p">Copilot for Business</span><span class="NavLink-module__subtitle__X4gkW">Enterprise-grade AI features</span></div></a></li><li><a href="https://github.com/premium-support" data-analytics-event="{&quot;action&quot;:&quot;premium_support&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;premium_support_link_enterprise_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg aria-hidden="true" focusable="false" class="octicon octicon-comment-discussion NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path></svg><span class="NavLink-module__title__Q7t0p">Premium Support</span><span class="NavLink-module__subtitle__X4gkW">Enterprise-grade 24/7 support</span></div></a></li></ul></div></li></ul></div></div></li><li><a href="https://github.com/pricing" data-analytics-event="{&quot;action&quot;:&quot;pricing&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;pricing&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;pricing_link_pricing_navbar&quot;}" class="NavLink-module__link__EG3d4 MarketingNavigation-module__navLink__hUomM"><span class="NavLink-module__title__Q7t0p">Pricing</span></a></li></ul></nav><script type="application/json" id="__PRIMER_DATA__R_0___">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>



        <div class="d-flex flex-column flex-lg-row width-full flex-justify-end flex-lg-items-center text-center tmp-mt-3 tmp-mt-lg-0 text-lg-left tmp-ml-lg-3">
                


<qbsearch-input class="search-input" data-scope="repo:togethercomputer/together-py" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="huyq0EMWG3DBaqssDG69oW8a0vkk_o-saPcCMJcxypHMk_SViDnt-RzeNHhdkm3vYDI89fESjZuRZxAoLDdyHA" data-max-custom-scopes="10" data-header-redesign-enabled="false" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="togethercomputer/together-py" data-current-org="togethercomputer" data-current-owner="" data-logged-in="false" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-retain-scroll-position="true">
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
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-c2a57731-8e57-4519-a7f6-02f2c4d40feb" data-target="query-builder.input" data-action="
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
                " variant="small" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
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
      <div class="FormControl-inlineValidation" id="validation-c2a57731-8e57-4519-a7f6-02f2c4d40feb" hidden="hidden">
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
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
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
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="code-search-feedback-form" data-turbo="false" action="/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="XH4Hq4TEud3JM+LSZHk5C9Ole3RBsTgzaWC8I5DjZAQvRUJKoSMz7S4g+xT0+QAuqbeqOz8q4yu2aB1u1hF6fQ==" />
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
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="custom-scopes-dialog-form" data-turbo="false" action="/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="XEFQkUPPnaHwcGr8/UwBlNUvy9WBxV0TahF0UHbkfQc2g5IQkFDp/sUdVE0rs0ikqLdvdElytIcA83ETpQSwFw==" />
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
              <input type="hidden" data-csrf="true" value="zl/ivssF0B6iJwvPq43U6klj7e9igj2tLmiq9z4XGI8NsK4QO7uhJDDLmXVfkqz9ANJRxyuRdGxbI2O0n05iUA==" />
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
                href="/login?return_to=https%3A%2F%2Fgithub.com%2Ftogethercomputer%2Ftogether-py"
                class="HeaderMenu-link HeaderMenu-link--sign-in HeaderMenu-button flex-shrink-0 no-underline d-none d-lg-inline-flex border border-lg-0 rounded px-2 py-1"
                style="margin-left: 12px;"
                data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/togethercomputer/together-py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="6f375c3f7cbd4df859df52b05863d4e82de64712156d77809baff31d58d49483"
                data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}"
              >
                Sign in
              </a>
            </div>

              <a href="/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&amp;source=header-repo&amp;source_repo=togethercomputer%2Ftogether-py"
                class="HeaderMenu-link HeaderMenu-link--sign-up HeaderMenu-button flex-shrink-0 d-flex d-lg-inline-flex no-underline border color-border-default rounded px-2 py-1"
                data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/togethercomputer/together-py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="6f375c3f7cbd4df859df52b05863d4e82de64712156d77809baff31d58d49483"
                data-analytics-event="{&quot;category&quot;:&quot;Sign up&quot;,&quot;action&quot;:&quot;click to sign up for account&quot;,&quot;label&quot;:&quot;ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;;ref_cta:Sign up;ref_loc:header logged out&quot;}"
              >
                Sign up
              </a>

                <div class="AppHeader-appearanceSettings">
    <react-partial-anchor>
      <button data-target="react-partial-anchor.anchor" id="icon-button-78955a1f-0e1a-4692-9f08-65b47e9f11c8" aria-labelledby="tooltip-bd6820fd-c9f5-4eaa-b05e-a3450e3ea081" type="button" disabled="disabled" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium AppHeader-button HeaderMenu-link border cursor-wait">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sliders Button-visual">
    <path d="M15 2.75a.75.75 0 0 1-.75.75h-4a.75.75 0 0 1 0-1.5h4a.75.75 0 0 1 .75.75Zm-8.5.75v1.25a.75.75 0 0 0 1.5 0v-4a.75.75 0 0 0-1.5 0V2H1.75a.75.75 0 0 0 0 1.5H6.5Zm1.25 5.25a.75.75 0 0 0 0-1.5h-6a.75.75 0 0 0 0 1.5h6ZM15 8a.75.75 0 0 1-.75.75H11.5V10a.75.75 0 1 1-1.5 0V6a.75.75 0 0 1 1.5 0v1.25h2.75A.75.75 0 0 1 15 8Zm-9 5.25v-2a.75.75 0 0 0-1.5 0v1.25H1.75a.75.75 0 0 0 0 1.5H4.5v1.25a.75.75 0 0 0 1.5 0v-2Zm9 0a.75.75 0 0 1-.75.75h-6a.75.75 0 0 1 0-1.5h6a.75.75 0 0 1 .75.75Z"></path>
</svg>
</button><tool-tip id="tooltip-bd6820fd-c9f5-4eaa-b05e-a3450e3ea081" for="icon-button-78955a1f-0e1a-4692-9f08-65b47e9f11c8" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Appearance settings</tool-tip>

      <template data-target="react-partial-anchor.template">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.a7c2947c416ec834.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/appearance-settings.437ba0a52997e5dd.module.css" />

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

    <button id="icon-button-9a206048-d8f6-41b8-95e7-a052d1e67df2" aria-labelledby="tooltip-294d1913-2d6b-4d62-b288-f5b958c39bee" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-294d1913-2d6b-4d62-b288-f5b958c39bee" for="icon-button-9a206048-d8f6-41b8-95e7-a052d1e67df2" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Dismiss alert</tool-tip>


  
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
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo color-fg-muted mr-2">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
    
    <span class="author flex-self-stretch" itemprop="author">
      <a class="url fn" rel="author" data-hovercard-type="organization" data-hovercard-url="/orgs/togethercomputer/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/togethercomputer">
        togethercomputer
</a>    </span>
    <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
    <strong itemprop="name" class="mr-2 flex-self-stretch">
      <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/togethercomputer/together-py">together-py</a>
    </strong>

    <span></span><span class="Label Label--secondary v-align-middle mr-1">Public</span>
  </div>


        </div>

        <div id="repository-details-container" class="flex-shrink-0" data-turbo-replace style="max-width: 70%;">
            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
    
      

  <li>
            <a href="/login?return_to=%2Ftogethercomputer%2Ftogether-py" rel="nofollow" id="repository-details-watch-button" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/togethercomputer/together-py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="e2b8b8c22c3349ffae1fead61101a567e29668c21a1a5a7a4a735eeee64f3d43" aria-label="You must be signed in to change notification settings" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>Notifications
</a>    <tool-tip id="tooltip-8cced3a3-1f4e-4441-abb6-bb4a4c60c8e8" for="repository-details-watch-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">You must be signed in to change notification settings</tool-tip>

  </li>

  <li>
          <a icon="repo-forked" id="fork-button" href="/login?return_to=%2Ftogethercomputer%2Ftogether-py" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:798597405,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/togethercomputer/together-py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="a50cda87c23d84d31cb3365eb20aa9fcc2706dffd27be82a8498ea4bd76aa556" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>Fork
    <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="0" data-view-component="true" class="Counter">0</span>
</a>
  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <a href="/login?return_to=%2Ftogethercomputer%2Ftogether-py" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:798597405,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/togethercomputer/together-py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="53cfbd5757f7a91d9882c4ef7c18bd4119c3e75886829ebf7104775cf4d635f9" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-sw btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>          <span id="repo-stars-counter-star" aria-label="7 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="7" data-view-component="true" class="Counter js-social-count">7</span>
</a></div>
  </li>

</ul>

        </div>
      </div>

        <div id="responsive-meta-container" data-turbo-replace>
</div>


          <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="/togethercomputer/together-py" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /togethercomputer/together-py" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-command-id="repositories:go-to-code" data-react-nav="code-view" data-react-nav-anchor="code-view-repo-link" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" aria-current="page" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="/togethercomputer/together-py/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /togethercomputer/together-py/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-command-id="repositories:go-to-issues" data-react-nav="issues-react" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/togethercomputer/together-py/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /togethercomputer/together-py/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-command-id="repositories:go-to-pull-requests" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="5" data-view-component="true" class="Counter">5</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/togethercomputer/together-py/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /togethercomputer/together-py/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-command-id="repositories:go-to-actions" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="/togethercomputer/together-py/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /togethercomputer/together-py/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-command-id="repositories:go-to-projects" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="/togethercomputer/together-py/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /togethercomputer/together-py/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-command-id="repositories:go-to-security" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          <span id="security-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="/togethercomputer/together-py/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /togethercomputer/together-py/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-command-id="repositories:go-to-insights" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true">
  <focus-group direction="vertical" mnemonics retain>
    <button id="action-menu-80dd44e4-6429-4699-85e4-aa3e7b9bade3-button" popovertarget="action-menu-80dd44e4-6429-4699-85e4-aa3e7b9bade3-overlay" aria-controls="action-menu-80dd44e4-6429-4699-85e4-aa3e7b9bade3-list" aria-haspopup="true" aria-labelledby="tooltip-f2b4401f-99b7-48be-ab7a-63a84ec18b75" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-f2b4401f-99b7-48be-ab7a-63a84ec18b75" for="action-menu-80dd44e4-6429-4699-85e4-aa3e7b9bade3-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-80dd44e4-6429-4699-85e4-aa3e7b9bade3-overlay" anchor="action-menu-80dd44e4-6429-4699-85e4-aa3e7b9bade3-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list>
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-80dd44e4-6429-4699-85e4-aa3e7b9bade3-button" id="action-menu-80dd44e4-6429-4699-85e4-aa3e7b9bade3-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="hidden" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-94b0f029-d087-4fc7-a17e-1c0867be81b0" href="/togethercomputer/together-py" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-f3934a5a-80be-4c29-b2f3-0bb9322ac604" href="/togethercomputer/together-py/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-463af68f-b010-461f-b610-18f4828b522a" href="/togethercomputer/together-py/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
        <li hidden="hidden" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-3ced7e05-452a-4ff8-9bbf-de430c9123fd" href="/togethercomputer/together-py/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
        <li hidden="hidden" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-6cdff0dc-0b87-41d7-b831-32a2a457335a" href="/togethercomputer/together-py/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
        <li hidden="hidden" data-menu-item="i5security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-7b95c52d-eb1b-4fca-ad92-e7eddd9f5bac" href="/togethercomputer/together-py/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i6insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-12b2450d-f078-49c4-b32f-ba42b239e90a" href="/togethercomputer/together-py/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
  initial-path="/togethercomputer/together-py"
  style="display: block; min-height: calc(100vh - 64px);"
  data-attempted-ssr="true"
  data-ssr="true"
  data-lazy="false"
  data-alternate="false"
  data-data-router-enabled="true"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"codeViewRepoRoute":{"path":"/","refInfo":{"name":"main","listCacheKey":"v0:1773255036.0","canEdit":false,"refType":"branch","currentOid":"f80a2b05ec9c5d917a5a327ac002e44dddd96b84"},"tree":{"items":[{"name":".devcontainer","path":".devcontainer","contentType":"directory"},{"name":".github/workflows","path":".github/workflows","contentType":"directory","hasSimplifiedPath":true},{"name":".vscode","path":".vscode","contentType":"directory"},{"name":"bin","path":"bin","contentType":"directory"},{"name":"examples","path":"examples","contentType":"directory"},{"name":"scripts","path":"scripts","contentType":"directory"},{"name":"src/together","path":"src/together","contentType":"directory","hasSimplifiedPath":true},{"name":"tests","path":"tests","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":".python-version","path":".python-version","contentType":"file"},{"name":".release-please-manifest.json","path":".release-please-manifest.json","contentType":"file"},{"name":".stats.yml","path":".stats.yml","contentType":"file"},{"name":"Brewfile","path":"Brewfile","contentType":"file"},{"name":"CHANGELOG.md","path":"CHANGELOG.md","contentType":"file"},{"name":"CONTRIBUTING.md","path":"CONTRIBUTING.md","contentType":"file"},{"name":"LICENSE","path":"LICENSE","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"SECURITY.md","path":"SECURITY.md","contentType":"file"},{"name":"api.md","path":"api.md","contentType":"file"},{"name":"pyproject.toml","path":"pyproject.toml","contentType":"file"},{"name":"release-please-config.json","path":"release-please-config.json","contentType":"file"},{"name":"requirements-dev.lock","path":"requirements-dev.lock","contentType":"file"},{"name":"uv.lock","path":"uv.lock","contentType":"file"}],"totalCount":23,"templateDirectorySuggestionUrl":null,"readme":null,"showBranchInfobar":false},"userNameDisplayConfiguration":"handle","treeExpanded":false,"symbolsExpanded":false,"copilotSWEAgentEnabled":false,"isOverview":true,"overview":{"banners":{"shouldRecommendReadme":false,"isPersonalRepo":false,"showUseActionBanner":false,"actionSlug":null,"actionId":null,"showProtectBranchBanner":false,"transactionalMessageBanner":null,"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_repo","releasePath":"/togethercomputer/together-py/releases/new?marketplace=true","showPublishActionBanner":false},"interactionLimitBanner":null,"showInvitationBanner":false,"inviterName":null,"actionsMigrationBannerInfo":{"releaseTags":[],"showImmutableActionsMigrationBanner":false,"initialMigrationStatus":null}},"codeButton":{"contactPath":"/contact","isEnterprise":false,"local":{"protocolInfo":{"httpAvailable":true,"sshAvailable":null,"httpUrl":"https://github.com/togethercomputer/together-py.git","showCloneWarning":null,"sshUrl":null,"sshCertificatesRequired":null,"sshCertificatesAvailable":null,"ghCliUrl":"gh repo clone togethercomputer/together-py","defaultProtocol":"http","newSshKeyUrl":"/settings/ssh/new","setProtocolPath":"/users/set_protocol"},"platformInfo":{"cloneUrl":"https://desktop.github.com","showVisualStudioCloneButton":false,"visualStudioCloneUrl":"https://windows.github.com","showXcodeCloneButton":false,"xcodeCloneUrl":"xcode://clone?repo=https%3A%2F%2Fgithub.com%2Ftogethercomputer%2Ftogether-py","zipballUrl":"/togethercomputer/together-py/archive/refs/heads/main.zip"}},"newCodespacePath":"/codespaces/new?hide_repo_select=true\u0026repo=798597405"},"popovers":{"rename":null,"renamedParentRepo":null},"commitCount":"509","overviewFiles":[{"displayName":"README.md","repoName":"together-py","refName":"main","path":"README.md","preferredFileType":"readme","tabName":"README","richText":"\u003carticle class=\"markdown-body entry-content container-lg\" itemprop=\"text\"\u003e\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch1 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eTogether Python API library\u003c/h1\u003e\u003ca id=\"user-content-together-python-api-library\" class=\"anchor\" aria-label=\"Permalink: Together Python API library\" href=\"#together-python-api-library\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\n\u003cp dir=\"auto\"\u003e\u003ca href=\"https://pypi.org/project/together/\" rel=\"nofollow\"\u003e\u003cimg src=\"https://camo.githubusercontent.com/d91235b9694c1546c6b0fac18a791e6d8d3b8958c0049f3fe504ecf52c83226c/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f746f6765746865722e7376673f6c6162656c3d7079706925323028737461626c6529\" alt=\"PyPI version\" data-canonical-src=\"https://img.shields.io/pypi/v/together.svg?label=pypi%20(stable)\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThe Together Python library provides convenient access to the Together REST API from any Python 3.9+\napplication. The library includes type definitions for all request params and response fields,\nand offers both synchronous and asynchronous clients powered by \u003ca href=\"https://github.com/encode/httpx\"\u003ehttpx\u003c/a\u003e.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eIt is generated with \u003ca href=\"https://www.stainless.com/\" rel=\"nofollow\"\u003eStainless\u003c/a\u003e.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDocumentation\u003c/h2\u003e\u003ca id=\"user-content-documentation\" class=\"anchor\" aria-label=\"Permalink: Documentation\" href=\"#documentation\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThe REST API documentation can be found on \u003ca href=\"https://docs.together.ai/\" rel=\"nofollow\"\u003edocs.together.ai\u003c/a\u003e. The full API of this library can be found in \u003ca href=\"/togethercomputer/together-py/blob/main/api.md\"\u003eapi.md\u003c/a\u003e.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eInstallation\u003c/h2\u003e\u003ca id=\"user-content-installation\" class=\"anchor\" aria-label=\"Permalink: Installation\" href=\"#installation\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"pip install together\"\u003e\u003cpre\u003epip install together\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"uv add together\"\u003e\u003cpre\u003euv add together\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eUsage\u003c/h2\u003e\u003ca id=\"user-content-usage\" class=\"anchor\" aria-label=\"Permalink: Usage\" href=\"#usage\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThe full API of this library can be found in \u003ca href=\"/togethercomputer/together-py/blob/main/api.md\"\u003eapi.md\u003c/a\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import os\nfrom together import Together\n\nclient = Together(\n    api_key=os.environ.get(\u0026quot;TOGETHER_API_KEY\u0026quot;),  # This is the default and can be omitted\n)\n\nchat_completion = client.chat.completions.create(\n    messages=[\n        {\n            \u0026quot;role\u0026quot;: \u0026quot;user\u0026quot;,\n            \u0026quot;content\u0026quot;: \u0026quot;Say this is a test!\u0026quot;,\n        }\n    ],\n    model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n)\nprint(chat_completion.choices)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eos\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eTogether\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eTogether\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eapi_key\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eos\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eenviron\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eget\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e\"TOGETHER_API_KEY\"\u003c/span\u003e),  \u003cspan class=\"pl-c\"\u003e# This is the default and can be omitted\u003c/span\u003e\n)\n\n\u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[\n        {\n            \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"user\"\u003c/span\u003e,\n            \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"Say this is a test!\"\u003c/span\u003e,\n        }\n    ],\n    \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n)\n\u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echoices\u003c/span\u003e)\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWhile you can provide an \u003ccode\u003eapi_key\u003c/code\u003e keyword argument,\nwe recommend using \u003ca href=\"https://pypi.org/project/python-dotenv/\" rel=\"nofollow\"\u003epython-dotenv\u003c/a\u003e\nto add \u003ccode\u003eTOGETHER_API_KEY=\"My API Key\"\u003c/code\u003e to your \u003ccode\u003e.env\u003c/code\u003e file\nso that your API Key is not stored in source control.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eAsync usage\u003c/h2\u003e\u003ca id=\"user-content-async-usage\" class=\"anchor\" aria-label=\"Permalink: Async usage\" href=\"#async-usage\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eSimply import \u003ccode\u003eAsyncTogether\u003c/code\u003e instead of \u003ccode\u003eTogether\u003c/code\u003e and use \u003ccode\u003eawait\u003c/code\u003e with each API call:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import os\nimport asyncio\nfrom together import AsyncTogether\n\nclient = AsyncTogether(\n    api_key=os.environ.get(\u0026quot;TOGETHER_API_KEY\u0026quot;),  # This is the default and can be omitted\n)\n\n\nasync def main() -\u0026gt; None:\n    chat_completion = await client.chat.completions.create(\n        messages=[\n            {\n                \u0026quot;role\u0026quot;: \u0026quot;user\u0026quot;,\n                \u0026quot;content\u0026quot;: \u0026quot;Say this is a test!\u0026quot;,\n            }\n        ],\n        model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n    )\n    print(chat_completion.choices)\n\n\nasyncio.run(main())\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eos\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003easyncio\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eAsyncTogether\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eAsyncTogether\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003eapi_key\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eos\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eenviron\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eget\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e\"TOGETHER_API_KEY\"\u003c/span\u003e),  \u003cspan class=\"pl-c\"\u003e# This is the default and can be omitted\u003c/span\u003e\n)\n\n\n\u003cspan class=\"pl-k\"\u003easync\u003c/span\u003e \u003cspan class=\"pl-k\"\u003edef\u003c/span\u003e \u003cspan class=\"pl-en\"\u003emain\u003c/span\u003e() \u003cspan class=\"pl-c1\"\u003e-\u0026gt;\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e:\n    \u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n        \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[\n            {\n                \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"user\"\u003c/span\u003e,\n                \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"Say this is a test!\"\u003c/span\u003e,\n            }\n        ],\n        \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n    )\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echoices\u003c/span\u003e)\n\n\n\u003cspan class=\"pl-s1\"\u003easyncio\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erun\u003c/span\u003e(\u003cspan class=\"pl-en\"\u003emain\u003c/span\u003e())\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eFunctionality between the synchronous and asynchronous clients is otherwise identical.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eWith aiohttp\u003c/h3\u003e\u003ca id=\"user-content-with-aiohttp\" class=\"anchor\" aria-label=\"Permalink: With aiohttp\" href=\"#with-aiohttp\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eBy default, the async client uses \u003ccode\u003ehttpx\u003c/code\u003e for HTTP requests. However, for improved concurrency performance you may also use \u003ccode\u003eaiohttp\u003c/code\u003e as the HTTP backend.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eYou can enable this by installing \u003ccode\u003eaiohttp\u003c/code\u003e:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# install from PyPI\npip install '--pre together[aiohttp]'\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e install from PyPI\u003c/span\u003e\npip install \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e--pre together[aiohttp]\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThen you can enable it by instantiating the client with \u003ccode\u003ehttp_client=DefaultAioHttpClient()\u003c/code\u003e:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import os\nimport asyncio\nfrom together import DefaultAioHttpClient\nfrom together import AsyncTogether\n\n\nasync def main() -\u0026gt; None:\n    async with AsyncTogether(\n        api_key=os.environ.get(\u0026quot;TOGETHER_API_KEY\u0026quot;),  # This is the default and can be omitted\n        http_client=DefaultAioHttpClient(),\n    ) as client:\n        chat_completion = await client.chat.completions.create(\n            messages=[\n                {\n                    \u0026quot;role\u0026quot;: \u0026quot;user\u0026quot;,\n                    \u0026quot;content\u0026quot;: \u0026quot;Say this is a test!\u0026quot;,\n                }\n            ],\n            model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n        )\n        print(chat_completion.choices)\n\n\nasyncio.run(main())\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eos\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003easyncio\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDefaultAioHttpClient\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eAsyncTogether\u003c/span\u003e\n\n\n\u003cspan class=\"pl-k\"\u003easync\u003c/span\u003e \u003cspan class=\"pl-k\"\u003edef\u003c/span\u003e \u003cspan class=\"pl-en\"\u003emain\u003c/span\u003e() \u003cspan class=\"pl-c1\"\u003e-\u0026gt;\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e:\n    \u003cspan class=\"pl-k\"\u003easync\u003c/span\u003e \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eAsyncTogether\u003c/span\u003e(\n        \u003cspan class=\"pl-s1\"\u003eapi_key\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eos\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eenviron\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eget\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e\"TOGETHER_API_KEY\"\u003c/span\u003e),  \u003cspan class=\"pl-c\"\u003e# This is the default and can be omitted\u003c/span\u003e\n        \u003cspan class=\"pl-s1\"\u003ehttp_client\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eDefaultAioHttpClient\u003c/span\u003e(),\n    ) \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e:\n        \u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n            \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[\n                {\n                    \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"user\"\u003c/span\u003e,\n                    \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"Say this is a test!\"\u003c/span\u003e,\n                }\n            ],\n            \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n        )\n        \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echoices\u003c/span\u003e)\n\n\n\u003cspan class=\"pl-s1\"\u003easyncio\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003erun\u003c/span\u003e(\u003cspan class=\"pl-en\"\u003emain\u003c/span\u003e())\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eStreaming responses\u003c/h2\u003e\u003ca id=\"user-content-streaming-responses\" class=\"anchor\" aria-label=\"Permalink: Streaming responses\" href=\"#streaming-responses\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWe provide support for streaming responses using Server Side Events (SSE).\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"from together import Together\n\nclient = Together()\n\nstream = client.chat.completions.create(\n    messages=[\n        {\n            \u0026quot;role\u0026quot;: \u0026quot;user\u0026quot;,\n            \u0026quot;content\u0026quot;: \u0026quot;Say this is a test!\u0026quot;,\n        }\n    ],\n    model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n    stream=True,\n)\nfor chat_completion in stream:\n    print(chat_completion.choices)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eTogether\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eTogether\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003estream\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[\n        {\n            \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"user\"\u003c/span\u003e,\n            \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"Say this is a test!\"\u003c/span\u003e,\n        }\n    ],\n    \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003estream\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,\n)\n\u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ein\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003estream\u003c/span\u003e:\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echoices\u003c/span\u003e)\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThe async client uses the exact same interface.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"from together import AsyncTogether\n\nclient = AsyncTogether()\n\nstream = await client.chat.completions.create(\n    messages=[\n        {\n            \u0026quot;role\u0026quot;: \u0026quot;user\u0026quot;,\n            \u0026quot;content\u0026quot;: \u0026quot;Say this is a test!\u0026quot;,\n        }\n    ],\n    model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n    stream=True,\n)\nasync for chat_completion in stream:\n    print(chat_completion.choices)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eAsyncTogether\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eAsyncTogether\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003estream\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[\n        {\n            \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"user\"\u003c/span\u003e,\n            \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"Say this is a test!\"\u003c/span\u003e,\n        }\n    ],\n    \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003estream\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e,\n)\n\u003cspan class=\"pl-k\"\u003easync\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ein\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003estream\u003c/span\u003e:\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echoices\u003c/span\u003e)\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eUsing types\u003c/h2\u003e\u003ca id=\"user-content-using-types\" class=\"anchor\" aria-label=\"Permalink: Using types\" href=\"#using-types\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eNested request parameters are \u003ca href=\"https://docs.python.org/3/library/typing.html#typing.TypedDict\" rel=\"nofollow\"\u003eTypedDicts\u003c/a\u003e. Responses are \u003ca href=\"https://docs.pydantic.dev\" rel=\"nofollow\"\u003ePydantic models\u003c/a\u003e which also provide helper methods for things like:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eSerializing back into JSON, \u003ccode\u003emodel.to_json()\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003eConverting to a dictionary, \u003ccode\u003emodel.to_dict()\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp dir=\"auto\"\u003eTyped requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set \u003ccode\u003epython.analysis.typeCheckingMode\u003c/code\u003e to \u003ccode\u003ebasic\u003c/code\u003e.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eNested params\u003c/h2\u003e\u003ca id=\"user-content-nested-params\" class=\"anchor\" aria-label=\"Permalink: Nested params\" href=\"#nested-params\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eNested parameters are dictionaries, typed using \u003ccode\u003eTypedDict\u003c/code\u003e, for example:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"from together import Together\n\nclient = Together()\n\nchat_completion = client.chat.completions.create(\n    messages=[\n        {\n            \u0026quot;content\u0026quot;: \u0026quot;content\u0026quot;,\n            \u0026quot;role\u0026quot;: \u0026quot;system\u0026quot;,\n        }\n    ],\n    model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n    reasoning={},\n)\nprint(chat_completion.reasoning)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eTogether\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eTogether\u003c/span\u003e()\n\n\u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[\n        {\n            \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e,\n            \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"system\"\u003c/span\u003e,\n        }\n    ],\n    \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003ereasoning\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e{},\n)\n\u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003echat_completion\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ereasoning\u003c/span\u003e)\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThe async client uses the exact same interface. If you pass a \u003ca href=\"https://docs.python.org/3/library/os.html#os.PathLike\" rel=\"nofollow\"\u003e\u003ccode\u003ePathLike\u003c/code\u003e\u003c/a\u003e instance, the file contents will be read asynchronously automatically.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eHandling errors\u003c/h2\u003e\u003ca id=\"user-content-handling-errors\" class=\"anchor\" aria-label=\"Permalink: Handling errors\" href=\"#handling-errors\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWhen the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of \u003ccode\u003etogether.APIConnectionError\u003c/code\u003e is raised.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eWhen the API returns a non-success status code (that is, 4xx or 5xx\nresponse), a subclass of \u003ccode\u003etogether.APIStatusError\u003c/code\u003e is raised, containing \u003ccode\u003estatus_code\u003c/code\u003e and \u003ccode\u003eresponse\u003c/code\u003e properties.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eAll errors inherit from \u003ccode\u003etogether.APIError\u003c/code\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import together\nfrom together import Together\n\nclient = Together()\n\ntry:\n    client.chat.completions.create(\n        messages=[\n            {\n                \u0026quot;role\u0026quot;: \u0026quot;user\u0026quot;,\n                \u0026quot;content\u0026quot;: \u0026quot;Say this is a test\u0026quot;,\n            }\n        ],\n        model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n    )\nexcept together.APIConnectionError as e:\n    print(\u0026quot;The server could not be reached\u0026quot;)\n    print(e.__cause__)  # an underlying Exception, likely raised within httpx.\nexcept together.RateLimitError as e:\n    print(\u0026quot;A 429 status code was received; we should back off a bit.\u0026quot;)\nexcept together.APIStatusError as e:\n    print(\u0026quot;Another non-200-range status code was received\u0026quot;)\n    print(e.status_code)\n    print(e.response)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eTogether\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eTogether\u003c/span\u003e()\n\n\u003cspan class=\"pl-k\"\u003etry\u003c/span\u003e:\n    \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n        \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[\n            {\n                \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"user\"\u003c/span\u003e,\n                \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"Say this is a test\"\u003c/span\u003e,\n            }\n        ],\n        \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n    )\n\u003cspan class=\"pl-k\"\u003eexcept\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eAPIConnectionError\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ee\u003c/span\u003e:\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e\"The server could not be reached\"\u003c/span\u003e)\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003ee\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003e__cause__\u003c/span\u003e)  \u003cspan class=\"pl-c\"\u003e# an underlying Exception, likely raised within httpx.\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eexcept\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eRateLimitError\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ee\u003c/span\u003e:\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e\"A 429 status code was received; we should back off a bit.\"\u003c/span\u003e)\n\u003cspan class=\"pl-k\"\u003eexcept\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eAPIStatusError\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ee\u003c/span\u003e:\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e\"Another non-200-range status code was received\"\u003c/span\u003e)\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003ee\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003estatus_code\u003c/span\u003e)\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003ee\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eresponse\u003c/span\u003e)\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eError codes are as follows:\u003c/p\u003e\n\u003cmarkdown-accessiblity-table\u003e\u003ctable\u003e\n\u003cthead\u003e\n\u003ctr\u003e\n\u003cth\u003eStatus Code\u003c/th\u003e\n\u003cth\u003eError Type\u003c/th\u003e\n\u003c/tr\u003e\n\u003c/thead\u003e\n\u003ctbody\u003e\n\u003ctr\u003e\n\u003ctd\u003e400\u003c/td\u003e\n\u003ctd\u003e\u003ccode\u003eBadRequestError\u003c/code\u003e\u003c/td\u003e\n\u003c/tr\u003e\n\u003ctr\u003e\n\u003ctd\u003e401\u003c/td\u003e\n\u003ctd\u003e\u003ccode\u003eAuthenticationError\u003c/code\u003e\u003c/td\u003e\n\u003c/tr\u003e\n\u003ctr\u003e\n\u003ctd\u003e403\u003c/td\u003e\n\u003ctd\u003e\u003ccode\u003ePermissionDeniedError\u003c/code\u003e\u003c/td\u003e\n\u003c/tr\u003e\n\u003ctr\u003e\n\u003ctd\u003e404\u003c/td\u003e\n\u003ctd\u003e\u003ccode\u003eNotFoundError\u003c/code\u003e\u003c/td\u003e\n\u003c/tr\u003e\n\u003ctr\u003e\n\u003ctd\u003e422\u003c/td\u003e\n\u003ctd\u003e\u003ccode\u003eUnprocessableEntityError\u003c/code\u003e\u003c/td\u003e\n\u003c/tr\u003e\n\u003ctr\u003e\n\u003ctd\u003e429\u003c/td\u003e\n\u003ctd\u003e\u003ccode\u003eRateLimitError\u003c/code\u003e\u003c/td\u003e\n\u003c/tr\u003e\n\u003ctr\u003e\n\u003ctd\u003e\u0026gt;=500\u003c/td\u003e\n\u003ctd\u003e\u003ccode\u003eInternalServerError\u003c/code\u003e\u003c/td\u003e\n\u003c/tr\u003e\n\u003ctr\u003e\n\u003ctd\u003eN/A\u003c/td\u003e\n\u003ctd\u003e\u003ccode\u003eAPIConnectionError\u003c/code\u003e\u003c/td\u003e\n\u003c/tr\u003e\n\u003c/tbody\u003e\n\u003c/table\u003e\u003c/markdown-accessiblity-table\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eRetries\u003c/h3\u003e\u003ca id=\"user-content-retries\" class=\"anchor\" aria-label=\"Permalink: Retries\" href=\"#retries\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eCertain errors are automatically retried 2 times by default, with a short exponential backoff.\nConnection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,\n429 Rate Limit, and \u0026gt;=500 Internal errors are all retried by default.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eYou can use the \u003ccode\u003emax_retries\u003c/code\u003e option to configure or disable retry settings:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"from together import Together\n\n# Configure the default for all requests:\nclient = Together(\n    # default is 2\n    max_retries=0,\n)\n\n# Or, configure per-request:\nclient.with_options(max_retries=5).chat.completions.create(\n    messages=[\n        {\n            \u0026quot;role\u0026quot;: \u0026quot;user\u0026quot;,\n            \u0026quot;content\u0026quot;: \u0026quot;Say this is a test\u0026quot;,\n        }\n    ],\n    model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eTogether\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# Configure the default for all requests:\u003c/span\u003e\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eTogether\u003c/span\u003e(\n    \u003cspan class=\"pl-c\"\u003e# default is 2\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003emax_retries\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e,\n)\n\n\u003cspan class=\"pl-c\"\u003e# Or, configure per-request:\u003c/span\u003e\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ewith_options\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003emax_retries\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e5\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[\n        {\n            \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"user\"\u003c/span\u003e,\n            \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"Say this is a test\"\u003c/span\u003e,\n        }\n    ],\n    \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n)\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eTimeouts\u003c/h3\u003e\u003ca id=\"user-content-timeouts\" class=\"anchor\" aria-label=\"Permalink: Timeouts\" href=\"#timeouts\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eBy default requests time out after 1 minute. You can configure this with a \u003ccode\u003etimeout\u003c/code\u003e option,\nwhich accepts a float or an \u003ca href=\"https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration\" rel=\"nofollow\"\u003e\u003ccode\u003ehttpx.Timeout\u003c/code\u003e\u003c/a\u003e object:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"from together import Together\n\n# Configure the default for all requests:\nclient = Together(\n    # 20 seconds (default is 1 minute)\n    timeout=20.0,\n)\n\n# More granular control:\nclient = Together(\n    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),\n)\n\n# Override per-request:\nclient.with_options(timeout=5.0).chat.completions.create(\n    messages=[\n        {\n            \u0026quot;role\u0026quot;: \u0026quot;user\u0026quot;,\n            \u0026quot;content\u0026quot;: \u0026quot;Say this is a test\u0026quot;,\n        }\n    ],\n    model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eTogether\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e# Configure the default for all requests:\u003c/span\u003e\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eTogether\u003c/span\u003e(\n    \u003cspan class=\"pl-c\"\u003e# 20 seconds (default is 1 minute)\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003etimeout\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e20.0\u003c/span\u003e,\n)\n\n\u003cspan class=\"pl-c\"\u003e# More granular control:\u003c/span\u003e\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eTogether\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003etimeout\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ehttpx\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eTimeout\u003c/span\u003e(\u003cspan class=\"pl-c1\"\u003e60.0\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003eread\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e5.0\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003ewrite\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e10.0\u003c/span\u003e, \u003cspan class=\"pl-s1\"\u003econnect\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e2.0\u003c/span\u003e),\n)\n\n\u003cspan class=\"pl-c\"\u003e# Override per-request:\u003c/span\u003e\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ewith_options\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003etimeout\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e5.0\u003c/span\u003e).\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[\n        {\n            \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"user\"\u003c/span\u003e,\n            \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"Say this is a test\"\u003c/span\u003e,\n        }\n    ],\n    \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n)\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eOn timeout, an \u003ccode\u003eAPITimeoutError\u003c/code\u003e is thrown.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eNote that requests that time out are \u003ca href=\"#retries\"\u003eretried twice by default\u003c/a\u003e.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eAdvanced\u003c/h2\u003e\u003ca id=\"user-content-advanced\" class=\"anchor\" aria-label=\"Permalink: Advanced\" href=\"#advanced\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eLogging\u003c/h3\u003e\u003ca id=\"user-content-logging\" class=\"anchor\" aria-label=\"Permalink: Logging\" href=\"#logging\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWe use the standard library \u003ca href=\"https://docs.python.org/3/library/logging.html\" rel=\"nofollow\"\u003e\u003ccode\u003elogging\u003c/code\u003e\u003c/a\u003e module.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eYou can enable logging by setting the environment variable \u003ccode\u003eTOGETHER_LOG\u003c/code\u003e to \u003ccode\u003einfo\u003c/code\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"$ export TOGETHER_LOG=info\"\u003e\u003cpre\u003e$ \u003cspan class=\"pl-k\"\u003eexport\u003c/span\u003e TOGETHER_LOG=info\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eOr to \u003ccode\u003edebug\u003c/code\u003e for more verbose logging.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eHow to tell whether \u003ccode\u003eNone\u003c/code\u003e means \u003ccode\u003enull\u003c/code\u003e or missing\u003c/h3\u003e\u003ca id=\"user-content-how-to-tell-whether-none-means-null-or-missing\" class=\"anchor\" aria-label=\"Permalink: How to tell whether None means null or missing\" href=\"#how-to-tell-whether-none-means-null-or-missing\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eIn an API response, a field may be explicitly \u003ccode\u003enull\u003c/code\u003e, or missing entirely; in either case, its value is \u003ccode\u003eNone\u003c/code\u003e in this library. You can differentiate the two cases with \u003ccode\u003e.model_fields_set\u003c/code\u003e:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"if response.my_field is None:\n  if 'my_field' not in response.model_fields_set:\n    print('Got json like {}, without a \u0026quot;my_field\u0026quot; key present at all.')\n  else:\n    print('Got json like {\u0026quot;my_field\u0026quot;: null}.')\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eresponse\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003emy_field\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eis\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e:\n  \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'my_field'\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e\u003cspan class=\"pl-c1\"\u003enot\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ein\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eresponse\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003emodel_fields_set\u003c/span\u003e:\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e'Got json like {}, without a \"my_field\" key present at all.'\u003c/span\u003e)\n  \u003cspan class=\"pl-k\"\u003eelse\u003c/span\u003e:\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e'Got json like {\"my_field\": null}.'\u003c/span\u003e)\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eAccessing raw response data (e.g. headers)\u003c/h3\u003e\u003ca id=\"user-content-accessing-raw-response-data-eg-headers\" class=\"anchor\" aria-label=\"Permalink: Accessing raw response data (e.g. headers)\" href=\"#accessing-raw-response-data-eg-headers\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThe \"raw\" Response object can be accessed by prefixing \u003ccode\u003e.with_raw_response.\u003c/code\u003e to any HTTP method call, e.g.,\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"from together import Together\n\nclient = Together()\nresponse = client.chat.completions.with_raw_response.create(\n    messages=[{\n        \u0026quot;role\u0026quot;: \u0026quot;user\u0026quot;,\n        \u0026quot;content\u0026quot;: \u0026quot;Say this is a test\u0026quot;,\n    }],\n    model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n)\nprint(response.headers.get('X-My-Header'))\n\ncompletion = response.parse()  # get the object that `chat.completions.create()` would have returned\nprint(completion.choices)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eTogether\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eTogether\u003c/span\u003e()\n\u003cspan class=\"pl-s1\"\u003eresponse\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ewith_raw_response\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[{\n        \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"user\"\u003c/span\u003e,\n        \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"Say this is a test\"\u003c/span\u003e,\n    }],\n    \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n)\n\u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eresponse\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eget\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e'X-My-Header'\u003c/span\u003e))\n\n\u003cspan class=\"pl-s1\"\u003ecompletion\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eresponse\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eparse\u003c/span\u003e()  \u003cspan class=\"pl-c\"\u003e# get the object that `chat.completions.create()` would have returned\u003c/span\u003e\n\u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003ecompletion\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echoices\u003c/span\u003e)\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThese methods return an \u003ca href=\"https://github.com/togethercomputer/together-py/tree/main/src/together/_response.py\"\u003e\u003ccode\u003eAPIResponse\u003c/code\u003e\u003c/a\u003e object.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThe async client returns an \u003ca href=\"https://github.com/togethercomputer/together-py/tree/main/src/together/_response.py\"\u003e\u003ccode\u003eAsyncAPIResponse\u003c/code\u003e\u003c/a\u003e with the same structure, the only difference being \u003ccode\u003eawait\u003c/code\u003eable methods for reading the response content.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e\u003ccode\u003e.with_streaming_response\u003c/code\u003e\u003c/h4\u003e\u003ca id=\"user-content-with_streaming_response\" class=\"anchor\" aria-label=\"Permalink: .with_streaming_response\" href=\"#with_streaming_response\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThe above interface eagerly reads the full response body when you make the request, which may not always be what you want.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eTo stream the response body, use \u003ccode\u003e.with_streaming_response\u003c/code\u003e instead, which requires a context manager and only reads the response body once you call \u003ccode\u003e.read()\u003c/code\u003e, \u003ccode\u003e.text()\u003c/code\u003e, \u003ccode\u003e.json()\u003c/code\u003e, \u003ccode\u003e.iter_bytes()\u003c/code\u003e, \u003ccode\u003e.iter_text()\u003c/code\u003e, \u003ccode\u003e.iter_lines()\u003c/code\u003e or \u003ccode\u003e.parse()\u003c/code\u003e. In the async client, these are async methods.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"with client.chat.completions.with_streaming_response.create(\n    messages=[\n        {\n            \u0026quot;role\u0026quot;: \u0026quot;user\u0026quot;,\n            \u0026quot;content\u0026quot;: \u0026quot;Say this is a test\u0026quot;,\n        }\n    ],\n    model=\u0026quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\u0026quot;,\n) as response:\n    print(response.headers.get(\u0026quot;X-My-Header\u0026quot;))\n\n    for line in response.iter_lines():\n        print(line)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ewith_streaming_response\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate\u003c/span\u003e(\n    \u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e[\n        {\n            \u003cspan class=\"pl-s\"\u003e\"role\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"user\"\u003c/span\u003e,\n            \u003cspan class=\"pl-s\"\u003e\"content\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\"Say this is a test\"\u003c/span\u003e,\n        }\n    ],\n    \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo\"\u003c/span\u003e,\n) \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eresponse\u003c/span\u003e:\n    \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eresponse\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eget\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e\"X-My-Header\"\u003c/span\u003e))\n\n    \u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eline\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ein\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eresponse\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eiter_lines\u003c/span\u003e():\n        \u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eline\u003c/span\u003e)\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThe context manager is required so that the response will reliably be closed.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eMaking custom/undocumented requests\u003c/h3\u003e\u003ca id=\"user-content-making-customundocumented-requests\" class=\"anchor\" aria-label=\"Permalink: Making custom/undocumented requests\" href=\"#making-customundocumented-requests\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThis library is typed for convenient access to the documented API.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eIf you need to access undocumented endpoints, params, or response properties, the library can still be used.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eUndocumented endpoints\u003c/h4\u003e\u003ca id=\"user-content-undocumented-endpoints\" class=\"anchor\" aria-label=\"Permalink: Undocumented endpoints\" href=\"#undocumented-endpoints\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eTo make requests to undocumented endpoints, you can make requests using \u003ccode\u003eclient.get\u003c/code\u003e, \u003ccode\u003eclient.post\u003c/code\u003e, and other\nhttp verbs. Options on the client will be respected (such as retries) when making this request.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import httpx\n\nresponse = client.post(\n    \u0026quot;/foo\u0026quot;,\n    cast_to=httpx.Response,\n    body={\u0026quot;my_param\u0026quot;: True},\n)\n\nprint(response.headers.get(\u0026quot;x-foo\u0026quot;))\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ehttpx\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eresponse\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003epost\u003c/span\u003e(\n    \u003cspan class=\"pl-s\"\u003e\"/foo\"\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003ecast_to\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ehttpx\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eResponse\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003ebody\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e{\u003cspan class=\"pl-s\"\u003e\"my_param\"\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e},\n)\n\n\u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003eresponse\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eget\u003c/span\u003e(\u003cspan class=\"pl-s\"\u003e\"x-foo\"\u003c/span\u003e))\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eUndocumented request params\u003c/h4\u003e\u003ca id=\"user-content-undocumented-request-params\" class=\"anchor\" aria-label=\"Permalink: Undocumented request params\" href=\"#undocumented-request-params\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eIf you want to explicitly send an extra param, you can do so with the \u003ccode\u003eextra_query\u003c/code\u003e, \u003ccode\u003eextra_body\u003c/code\u003e, and \u003ccode\u003eextra_headers\u003c/code\u003e request\noptions.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eUndocumented response properties\u003c/h4\u003e\u003ca id=\"user-content-undocumented-response-properties\" class=\"anchor\" aria-label=\"Permalink: Undocumented response properties\" href=\"#undocumented-response-properties\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eTo access undocumented response properties, you can access the extra fields like \u003ccode\u003eresponse.unknown_prop\u003c/code\u003e. You\ncan also get all the extra fields on the Pydantic model as a dict with\n\u003ca href=\"https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra\" rel=\"nofollow\"\u003e\u003ccode\u003eresponse.model_extra\u003c/code\u003e\u003c/a\u003e.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eConfiguring the HTTP client\u003c/h3\u003e\u003ca id=\"user-content-configuring-the-http-client\" class=\"anchor\" aria-label=\"Permalink: Configuring the HTTP client\" href=\"#configuring-the-http-client\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eYou can directly override the \u003ca href=\"https://www.python-httpx.org/api/#client\" rel=\"nofollow\"\u003ehttpx client\u003c/a\u003e to customize it for your use case, including:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eSupport for \u003ca href=\"https://www.python-httpx.org/advanced/proxies/\" rel=\"nofollow\"\u003eproxies\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003eCustom \u003ca href=\"https://www.python-httpx.org/advanced/transports/\" rel=\"nofollow\"\u003etransports\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003eAdditional \u003ca href=\"https://www.python-httpx.org/advanced/clients/\" rel=\"nofollow\"\u003eadvanced\u003c/a\u003e functionality\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import httpx\nfrom together import Together, DefaultHttpxClient\n\nclient = Together(\n    # Or use the `TOGETHER_BASE_URL` env var\n    base_url=\u0026quot;http://my.test.server.example.com:8083\u0026quot;,\n    http_client=DefaultHttpxClient(\n        proxy=\u0026quot;http://my.test.proxy.example.com\u0026quot;,\n        transport=httpx.HTTPTransport(local_address=\u0026quot;0.0.0.0\u0026quot;),\n    ),\n)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ehttpx\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eTogether\u003c/span\u003e, \u003cspan class=\"pl-v\"\u003eDefaultHttpxClient\u003c/span\u003e\n\n\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eTogether\u003c/span\u003e(\n    \u003cspan class=\"pl-c\"\u003e# Or use the `TOGETHER_BASE_URL` env var\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003ebase_url\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"http://my.test.server.example.com:8083\"\u003c/span\u003e,\n    \u003cspan class=\"pl-s1\"\u003ehttp_client\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eDefaultHttpxClient\u003c/span\u003e(\n        \u003cspan class=\"pl-s1\"\u003eproxy\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"http://my.test.proxy.example.com\"\u003c/span\u003e,\n        \u003cspan class=\"pl-s1\"\u003etransport\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ehttpx\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eHTTPTransport\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003elocal_address\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"0.0.0.0\"\u003c/span\u003e),\n    ),\n)\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eYou can also customize the client on a per-request basis by using \u003ccode\u003ewith_options()\u003c/code\u003e:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"client.with_options(http_client=DefaultHttpxClient(...))\"\u003e\u003cpre\u003e\u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ewith_options\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003ehttp_client\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eDefaultHttpxClient\u003c/span\u003e(...))\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eManaging HTTP resources\u003c/h3\u003e\u003ca id=\"user-content-managing-http-resources\" class=\"anchor\" aria-label=\"Permalink: Managing HTTP resources\" href=\"#managing-http-resources\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eBy default the library closes underlying HTTP connections whenever the client is \u003ca href=\"https://docs.python.org/3/reference/datamodel.html#object.__del__\" rel=\"nofollow\"\u003egarbage collected\u003c/a\u003e. You can manually close the client using the \u003ccode\u003e.close()\u003c/code\u003e method if desired, or with a context manager that closes when exiting.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"from together import Together\n\nwith Together() as client:\n  # make requests here\n  ...\n\n# HTTP client is now closed\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eTogether\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eTogether\u003c/span\u003e() \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eclient\u003c/span\u003e:\n  \u003cspan class=\"pl-c\"\u003e# make requests here\u003c/span\u003e\n  ...\n\n\u003cspan class=\"pl-c\"\u003e# HTTP client is now closed\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eUsage – CLI\u003c/h2\u003e\u003ca id=\"user-content-usage--cli\" class=\"anchor\" aria-label=\"Permalink: Usage – CLI\" href=\"#usage--cli\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eFiles\u003c/h3\u003e\u003ca id=\"user-content-files\" class=\"anchor\" aria-label=\"Permalink: Files\" href=\"#files\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether files --help\n\n# Check file\ntogether files check example.jsonl\n\n# Upload file\ntogether files upload example.jsonl\n\n# List files\ntogether files list\n\n# Retrieve file metadata\ntogether files retrieve file-6f50f9d1-5b95-416c-9040-0799b2b4b894\n\n# Retrieve file content\ntogether files retrieve-content file-6f50f9d1-5b95-416c-9040-0799b2b4b894\n\n# Delete remote file\ntogether files delete file-6f50f9d1-5b95-416c-9040-0799b2b4b894\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether files --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Check file\u003c/span\u003e\ntogether files check example.jsonl\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Upload file\u003c/span\u003e\ntogether files upload example.jsonl\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List files\u003c/span\u003e\ntogether files list\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Retrieve file metadata\u003c/span\u003e\ntogether files retrieve file-6f50f9d1-5b95-416c-9040-0799b2b4b894\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Retrieve file content\u003c/span\u003e\ntogether files retrieve-content file-6f50f9d1-5b95-416c-9040-0799b2b4b894\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Delete remote file\u003c/span\u003e\ntogether files delete file-6f50f9d1-5b95-416c-9040-0799b2b4b894\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eFine-tuning\u003c/h3\u003e\u003ca id=\"user-content-fine-tuning\" class=\"anchor\" aria-label=\"Permalink: Fine-tuning\" href=\"#fine-tuning\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether fine-tuning --help\n\n# Create fine-tune job\ntogether fine-tuning create \\\n  --model togethercomputer/llama-2-7b-chat \\\n  --training-file file-711d8724-b3e3-4ae2-b516-94841958117d\n\n# List fine-tune jobs\ntogether fine-tuning list\n\n# Retrieve fine-tune job details\ntogether fine-tuning retrieve ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n# List fine-tune job events\ntogether fine-tuning list-events ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n# Cancel running job\ntogether fine-tuning cancel ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n# Download fine-tuned model weights\ntogether fine-tuning download ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether fine-tuning --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Create fine-tune job\u003c/span\u003e\ntogether fine-tuning create \\\n  --model togethercomputer/llama-2-7b-chat \\\n  --training-file file-711d8724-b3e3-4ae2-b516-94841958117d\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List fine-tune jobs\u003c/span\u003e\ntogether fine-tuning list\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Retrieve fine-tune job details\u003c/span\u003e\ntogether fine-tuning retrieve ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List fine-tune job events\u003c/span\u003e\ntogether fine-tuning list-events ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Cancel running job\u003c/span\u003e\ntogether fine-tuning cancel ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Download fine-tuned model weights\u003c/span\u003e\ntogether fine-tuning download ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eModels\u003c/h3\u003e\u003ca id=\"user-content-models\" class=\"anchor\" aria-label=\"Permalink: Models\" href=\"#models\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether models --help\n\n# List models\ntogether models list\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether models --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List models\u003c/span\u003e\ntogether models list\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eVersioning\u003c/h2\u003e\u003ca id=\"user-content-versioning\" class=\"anchor\" aria-label=\"Permalink: Versioning\" href=\"#versioning\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThis package generally follows \u003ca href=\"https://semver.org/spec/v2.0.0.html\" rel=\"nofollow\"\u003eSemVer\u003c/a\u003e conventions, though certain backwards-incompatible changes may be released as minor versions:\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eChanges that only affect static types, without breaking runtime behavior.\u003c/li\u003e\n\u003cli\u003eChanges to library internals which are technically public but not intended or documented for external use. \u003cem\u003e(Please open a GitHub issue to let us know if you are relying on such internals.)\u003c/em\u003e\u003c/li\u003e\n\u003cli\u003eChanges that we do not expect to impact the vast majority of users in practice.\u003c/li\u003e\n\u003c/ol\u003e\n\u003cp dir=\"auto\"\u003eWe take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eWe are keen for your feedback; please open an \u003ca href=\"https://www.github.com/togethercomputer/together-py/issues\"\u003eissue\u003c/a\u003e with questions, bugs, or suggestions.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDetermining the installed version\u003c/h3\u003e\u003ca id=\"user-content-determining-the-installed-version\" class=\"anchor\" aria-label=\"Permalink: Determining the installed version\" href=\"#determining-the-installed-version\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eIf you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eYou can determine the version that is being used at runtime with:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-python notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import together\nprint(together.__version__)\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e\n\u003cspan class=\"pl-en\"\u003eprint\u003c/span\u003e(\u003cspan class=\"pl-s1\"\u003etogether\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003e__version__\u003c/span\u003e)\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eRequirements\u003c/h2\u003e\u003ca id=\"user-content-requirements\" class=\"anchor\" aria-label=\"Permalink: Requirements\" href=\"#requirements\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003ePython 3.9 or higher.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eUsage – CLI\u003c/h2\u003e\u003ca id=\"user-content-usage--cli-1\" class=\"anchor\" aria-label=\"Permalink: Usage – CLI\" href=\"#usage--cli-1\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eFiles\u003c/h3\u003e\u003ca id=\"user-content-files-1\" class=\"anchor\" aria-label=\"Permalink: Files\" href=\"#files-1\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether files --help\n\n# Check file\ntogether files check example.jsonl\n\n# Upload file\ntogether files upload example.jsonl\n\n# List files\ntogether files list\n\n# Retrieve file metadata\ntogether files retrieve file-6f50f9d1-5b95-416c-9040-0799b2b4b894\n\n# Retrieve file content\ntogether files retrieve-content file-6f50f9d1-5b95-416c-9040-0799b2b4b894\n\n# Delete remote file\ntogether files delete file-6f50f9d1-5b95-416c-9040-0799b2b4b894\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether files --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Check file\u003c/span\u003e\ntogether files check example.jsonl\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Upload file\u003c/span\u003e\ntogether files upload example.jsonl\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List files\u003c/span\u003e\ntogether files list\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Retrieve file metadata\u003c/span\u003e\ntogether files retrieve file-6f50f9d1-5b95-416c-9040-0799b2b4b894\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Retrieve file content\u003c/span\u003e\ntogether files retrieve-content file-6f50f9d1-5b95-416c-9040-0799b2b4b894\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Delete remote file\u003c/span\u003e\ntogether files delete file-6f50f9d1-5b95-416c-9040-0799b2b4b894\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eFine-tuning\u003c/h3\u003e\u003ca id=\"user-content-fine-tuning-1\" class=\"anchor\" aria-label=\"Permalink: Fine-tuning\" href=\"#fine-tuning-1\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether fine-tuning --help\n\n# Create fine-tune job\ntogether fine-tuning create \\\n  --model togethercomputer/llama-2-7b-chat \\\n  --training-file file-711d8724-b3e3-4ae2-b516-94841958117d\n\n# List fine-tune jobs\ntogether fine-tuning list\n\n# Retrieve fine-tune job details\ntogether fine-tuning retrieve ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n# List fine-tune job events\ntogether fine-tuning list-events ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n# List fine-tune checkpoints\ntogether fine-tuning list-checkpoints ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n# Cancel running job\ntogether fine-tuning cancel ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n# Download fine-tuned model weights\ntogether fine-tuning download ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n# Delete fine-tuned model weights\ntogether fine-tuning delete ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether fine-tuning --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Create fine-tune job\u003c/span\u003e\ntogether fine-tuning create \\\n  --model togethercomputer/llama-2-7b-chat \\\n  --training-file file-711d8724-b3e3-4ae2-b516-94841958117d\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List fine-tune jobs\u003c/span\u003e\ntogether fine-tuning list\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Retrieve fine-tune job details\u003c/span\u003e\ntogether fine-tuning retrieve ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List fine-tune job events\u003c/span\u003e\ntogether fine-tuning list-events ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List fine-tune checkpoints\u003c/span\u003e\ntogether fine-tuning list-checkpoints ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Cancel running job\u003c/span\u003e\ntogether fine-tuning cancel ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Download fine-tuned model weights\u003c/span\u003e\ntogether fine-tuning download ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Delete fine-tuned model weights\u003c/span\u003e\ntogether fine-tuning delete ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eModels\u003c/h3\u003e\u003ca id=\"user-content-models-1\" class=\"anchor\" aria-label=\"Permalink: Models\" href=\"#models-1\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether models --help\n\n# List models\ntogether models list\n\n# Upload a model\ntogether models upload --model-name my-org/my-model --model-source s3-or-hugging-face\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether models --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List models\u003c/span\u003e\ntogether models list\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Upload a model\u003c/span\u003e\ntogether models upload --model-name my-org/my-model --model-source s3-or-hugging-face\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eClusters\u003c/h3\u003e\u003ca id=\"user-content-clusters\" class=\"anchor\" aria-label=\"Permalink: Clusters\" href=\"#clusters\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether beta clusters --help\n\n# Create a cluster\ntogether beta clusters create\n\n# List clusters\ntogether beta clusters list\n\n# Retrieve cluster details\ntogether beta clusters retrieve [cluster-id]\n\n# Update a cluster\ntogether beta clusters update [cluster-id]\n\n# Retrieve Together cluster configuration options such as regions, gpu types and drivers available\ntogether beta clusters list-regions\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether beta clusters --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Create a cluster\u003c/span\u003e\ntogether beta clusters create\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List clusters\u003c/span\u003e\ntogether beta clusters list\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Retrieve cluster details\u003c/span\u003e\ntogether beta clusters retrieve [cluster-id]\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Update a cluster\u003c/span\u003e\ntogether beta clusters update [cluster-id]\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Retrieve Together cluster configuration options such as regions, gpu types and drivers available\u003c/span\u003e\ntogether beta clusters list-regions\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch5 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eCluster Storage\u003c/h5\u003e\u003ca id=\"user-content-cluster-storage\" class=\"anchor\" aria-label=\"Permalink: Cluster Storage\" href=\"#cluster-storage\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether beta clusters storage --help\n\n# Create cluster storage volume\ntogether beta clusters storage create\n\n# List storage volumes\ntogether beta clusters storage list\n\n# Retrieve storage volume\ntogether beta clusters storage retrieve [storage-id]\n\n# Delete storage volume\ntogether beta clusters storage delete [storage-id]\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether beta clusters storage --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Create cluster storage volume\u003c/span\u003e\ntogether beta clusters storage create\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List storage volumes\u003c/span\u003e\ntogether beta clusters storage list\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Retrieve storage volume\u003c/span\u003e\ntogether beta clusters storage retrieve [storage-id]\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Delete storage volume\u003c/span\u003e\ntogether beta clusters storage delete [storage-id]\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eJig (Container Deployments)\u003c/h3\u003e\u003ca id=\"user-content-jig-container-deployments\" class=\"anchor\" aria-label=\"Permalink: Jig (Container Deployments)\" href=\"#jig-container-deployments\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether beta jig --help\n\n# Initialize jig configuration (creates pyproject.toml)\ntogether beta jig init\n\n# Generate Dockerfile from config\ntogether beta jig dockerfile\n\n# Build container image\ntogether beta jig build\ntogether beta jig build --tag v1.0 --warmup\n\n# Push image to registry\ntogether beta jig push\ntogether beta jig push --tag v1.0\n\n# Deploy model (builds, pushes, and deploys)\ntogether beta jig deploy\ntogether beta jig deploy --build-only\ntogether beta jig deploy --image existing-image:tag\n\n# Get deployment status\ntogether beta jig status\n\n# Get deployment endpoint URL\ntogether beta jig endpoint\n\n# View deployment logs\ntogether beta jig logs\ntogether beta jig logs --follow\n\n# Destroy deployment\ntogether beta jig destroy\n\n# Get queue metrics\ntogether beta jig queue-status\n\n# List all deployments\ntogether beta jig list\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether beta jig --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Initialize jig configuration (creates pyproject.toml)\u003c/span\u003e\ntogether beta jig init\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Generate Dockerfile from config\u003c/span\u003e\ntogether beta jig dockerfile\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Build container image\u003c/span\u003e\ntogether beta jig build\ntogether beta jig build --tag v1.0 --warmup\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Push image to registry\u003c/span\u003e\ntogether beta jig push\ntogether beta jig push --tag v1.0\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Deploy model (builds, pushes, and deploys)\u003c/span\u003e\ntogether beta jig deploy\ntogether beta jig deploy --build-only\ntogether beta jig deploy --image existing-image:tag\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Get deployment status\u003c/span\u003e\ntogether beta jig status\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Get deployment endpoint URL\u003c/span\u003e\ntogether beta jig endpoint\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e View deployment logs\u003c/span\u003e\ntogether beta jig logs\ntogether beta jig logs --follow\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Destroy deployment\u003c/span\u003e\ntogether beta jig destroy\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Get queue metrics\u003c/span\u003e\ntogether beta jig queue-status\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List all deployments\u003c/span\u003e\ntogether beta jig list\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch5 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eJig Secrets\u003c/h5\u003e\u003ca id=\"user-content-jig-secrets\" class=\"anchor\" aria-label=\"Permalink: Jig Secrets\" href=\"#jig-secrets\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether beta jig secrets --help\n\n# Set a secret (creates or updates)\ntogether beta jig secrets set --name MY_SECRET --value \u0026quot;secret-value\u0026quot;\n\n# Remove a secret from local state\ntogether beta jig secrets unset --name MY_SECRET\n\n# List all secrets with sync status\ntogether beta jig secrets list\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether beta jig secrets --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Set a secret (creates or updates)\u003c/span\u003e\ntogether beta jig secrets \u003cspan class=\"pl-c1\"\u003eset\u003c/span\u003e --name MY_SECRET --value \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003esecret-value\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Remove a secret from local state\u003c/span\u003e\ntogether beta jig secrets \u003cspan class=\"pl-c1\"\u003eunset\u003c/span\u003e --name MY_SECRET\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List all secrets with sync status\u003c/span\u003e\ntogether beta jig secrets list\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch5 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eJig Volumes\u003c/h5\u003e\u003ca id=\"user-content-jig-volumes\" class=\"anchor\" aria-label=\"Permalink: Jig Volumes\" href=\"#jig-volumes\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"# Help\ntogether beta jig volumes --help\n\n# Create a volume and upload files from directory\ntogether beta jig volumes create --name my-volume --source ./data\n\n# Update a volume with new files\ntogether beta jig volumes update --name my-volume --source ./data\n\n# Set volume mount path for deployment\ntogether beta jig volumes set --name my-volume --mount-path /app/data\n\n# Remove volume from deployment config (does not delete remote volume)\ntogether beta jig volumes unset --name my-volume\n\n# Delete a volume\ntogether beta jig volumes delete --name my-volume\n\n# Describe a volume\ntogether beta jig volumes describe --name my-volume\n\n# List all volumes\ntogether beta jig volumes list\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Help\u003c/span\u003e\ntogether beta jig volumes --help\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Create a volume and upload files from directory\u003c/span\u003e\ntogether beta jig volumes create --name my-volume --source ./data\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Update a volume with new files\u003c/span\u003e\ntogether beta jig volumes update --name my-volume --source ./data\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Set volume mount path for deployment\u003c/span\u003e\ntogether beta jig volumes \u003cspan class=\"pl-c1\"\u003eset\u003c/span\u003e --name my-volume --mount-path /app/data\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Remove volume from deployment config (does not delete remote volume)\u003c/span\u003e\ntogether beta jig volumes \u003cspan class=\"pl-c1\"\u003eunset\u003c/span\u003e --name my-volume\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Delete a volume\u003c/span\u003e\ntogether beta jig volumes delete --name my-volume\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Describe a volume\u003c/span\u003e\ntogether beta jig volumes describe --name my-volume\n\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e List all volumes\u003c/span\u003e\ntogether beta jig volumes list\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eContributing\u003c/h2\u003e\u003ca id=\"user-content-contributing\" class=\"anchor\" aria-label=\"Permalink: Contributing\" href=\"#contributing\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eSee \u003ca href=\"/togethercomputer/together-py/blob/main/CONTRIBUTING.md\"\u003ethe contributing documentation\u003c/a\u003e.\u003c/p\u003e\n\u003c/article\u003e","loaded":true,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":[{"level":1,"text":"Together Python API library","anchor":"together-python-api-library","htmlText":"Together Python API library"},{"level":2,"text":"Documentation","anchor":"documentation","htmlText":"Documentation"},{"level":2,"text":"Installation","anchor":"installation","htmlText":"Installation"},{"level":2,"text":"Usage","anchor":"usage","htmlText":"Usage"},{"level":2,"text":"Async usage","anchor":"async-usage","htmlText":"Async usage"},{"level":3,"text":"With aiohttp","anchor":"with-aiohttp","htmlText":"With aiohttp"},{"level":2,"text":"Streaming responses","anchor":"streaming-responses","htmlText":"Streaming responses"},{"level":2,"text":"Using types","anchor":"using-types","htmlText":"Using types"},{"level":2,"text":"Nested params","anchor":"nested-params","htmlText":"Nested params"},{"level":2,"text":"Handling errors","anchor":"handling-errors","htmlText":"Handling errors"},{"level":3,"text":"Retries","anchor":"retries","htmlText":"Retries"},{"level":3,"text":"Timeouts","anchor":"timeouts","htmlText":"Timeouts"},{"level":2,"text":"Advanced","anchor":"advanced","htmlText":"Advanced"},{"level":3,"text":"Logging","anchor":"logging","htmlText":"Logging"},{"level":3,"text":"How to tell whether None means null or missing","anchor":"how-to-tell-whether-none-means-null-or-missing","htmlText":"How to tell whether None means null or missing"},{"level":3,"text":"Accessing raw response data (e.g. headers)","anchor":"accessing-raw-response-data-eg-headers","htmlText":"Accessing raw response data (e.g. headers)"},{"level":4,"text":".with_streaming_response","anchor":"with_streaming_response","htmlText":".with_streaming_response"},{"level":3,"text":"Making custom/undocumented requests","anchor":"making-customundocumented-requests","htmlText":"Making custom/undocumented requests"},{"level":4,"text":"Undocumented endpoints","anchor":"undocumented-endpoints","htmlText":"Undocumented endpoints"},{"level":4,"text":"Undocumented request params","anchor":"undocumented-request-params","htmlText":"Undocumented request params"},{"level":4,"text":"Undocumented response properties","anchor":"undocumented-response-properties","htmlText":"Undocumented response properties"},{"level":3,"text":"Configuring the HTTP client","anchor":"configuring-the-http-client","htmlText":"Configuring the HTTP client"},{"level":3,"text":"Managing HTTP resources","anchor":"managing-http-resources","htmlText":"Managing HTTP resources"},{"level":2,"text":"Usage – CLI","anchor":"usage--cli","htmlText":"Usage – CLI"},{"level":3,"text":"Files","anchor":"files","htmlText":"Files"},{"level":3,"text":"Fine-tuning","anchor":"fine-tuning","htmlText":"Fine-tuning"},{"level":3,"text":"Models","anchor":"models","htmlText":"Models"},{"level":2,"text":"Versioning","anchor":"versioning","htmlText":"Versioning"},{"level":3,"text":"Determining the installed version","anchor":"determining-the-installed-version","htmlText":"Determining the installed version"},{"level":2,"text":"Requirements","anchor":"requirements","htmlText":"Requirements"},{"level":2,"text":"Usage – CLI","anchor":"usage--cli-1","htmlText":"Usage – CLI"},{"level":3,"text":"Files","anchor":"files-1","htmlText":"Files"},{"level":3,"text":"Fine-tuning","anchor":"fine-tuning-1","htmlText":"Fine-tuning"},{"level":3,"text":"Models","anchor":"models-1","htmlText":"Models"},{"level":3,"text":"Clusters","anchor":"clusters","htmlText":"Clusters"},{"level":5,"text":"Cluster Storage","anchor":"cluster-storage","htmlText":"Cluster Storage"},{"level":3,"text":"Jig (Container Deployments)","anchor":"jig-container-deployments","htmlText":"Jig (Container Deployments)"},{"level":5,"text":"Jig Secrets","anchor":"jig-secrets","htmlText":"Jig Secrets"},{"level":5,"text":"Jig Volumes","anchor":"jig-volumes","htmlText":"Jig Volumes"},{"level":2,"text":"Contributing","anchor":"contributing","htmlText":"Contributing"}],"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Ftogethercomputer%2Ftogether-py"}},{"displayName":"CONTRIBUTING.md","repoName":"together-py","refName":"main","path":"CONTRIBUTING.md","preferredFileType":"contributing","tabName":"Contributing","richText":null,"loaded":false,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":null,"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Ftogethercomputer%2Ftogether-py"}},{"displayName":"LICENSE","repoName":"together-py","refName":"main","path":"LICENSE","preferredFileType":"license","tabName":"Apache-2.0","richText":null,"loaded":false,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":null,"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Ftogethercomputer%2Ftogether-py"}},{"displayName":"SECURITY.md","repoName":"together-py","refName":"main","path":"SECURITY.md","preferredFileType":"security","tabName":"Security","richText":null,"loaded":false,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":null,"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Ftogethercomputer%2Ftogether-py"}}],"overviewFilesProcessingTime":0,"copilotSWEAgentEnabled":false}},"codeViewLayoutRoute":{"repo":{"id":798597405,"defaultBranch":"main","name":"together-py","ownerLogin":"togethercomputer","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2024-05-10T05:10:26.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/109101822?v=4","public":true,"private":false,"isOrgOwned":true},"currentUser":null,"uploadToken":"ltAcvWyA-p2M-0SQr9vze5qX7OMP7XiMdbN2vMBJZ7UGKHrntSvnMHgFieknqoXIeXo0ycD7IiBVy3EYQPg3Ww","allShortcutsEnabled":false,"treeExpanded":true,"path":"/","symbolsExpanded":false,"refInfo":{"name":"main","listCacheKey":"v0:1773255036.0","canEdit":false,"currentOid":"f80a2b05ec9c5d917a5a327ac002e44dddd96b84"},"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-4e5d7136862a2a48.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-4c35b25d88167fef.js","githubDevUrl":null},"csrf_tokens":{"/togethercomputer/together-py/branches":{"post":"LS8HQnwaMDcUNoD04wWKi1d-Ws11SUsHub8D9908FmHBXNY3ocin0R2-6OHgAKqzvAqeC0J-yCSZD1WmtvUY6w"}}},"title":"GitHub - togethercomputer/together-py","appPayload":{},"meta":{"title":"GitHub - togethercomputer/together-py"}}</script>
  <div data-target="react-app.reactRoot"><meta name="github-code-view-meta-stats" id="github-code-view-meta-stats" data-hydrostats="publish"/> <!-- --> <a hidden="" id="code-view-repo-link" href="/togethercomputer/together-py" data-discover="true"></a> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><div><div style="--spacing:var(--spacing-none)" class="prc-PageLayout-PageLayoutRoot--KH-d"><div class="prc-PageLayout-PageLayoutWrapper-2BhU2" data-width="full"><div class="prc-PageLayout-PageLayoutContent-BneH9"><div class="prc-PageLayout-ContentWrapper-gR9eG" data-is-hidden-narrow="false"><div class="prc-PageLayout-Content-xWL-A" data-width="full" style="--spacing:var(--spacing-none)"><div class="SharedPageLayout-module__content__IwGAp" data-selector="repos-split-pane-content" tabindex="0"><div style="--spacing:var(--spacing-none)" class="prc-PageLayout-PageLayoutRoot--KH-d container-xl"><div class="prc-PageLayout-PageLayoutWrapper-2BhU2" data-width="full"><header data-hidden="false" class="prc-PageLayout-Header-0of-R tmp-px-3 tmp-px-lg-5" style="--spacing:var(--spacing-none)"><div class="prc-PageLayout-HeaderContent-gdFfN" style="--spacing:var(--spacing-none)"><rails-partial data-partial-name="codeViewRepoRoute.Header" class="RailsPartial-module__d-contents__G5m4w">




<h1 class='sr-only'>togethercomputer/together-py</h1>


<input type="hidden" data-csrf="true" value="HQYtFgAemHYhTZdJgiUdriVxxfp2MJYIfPj1RUgQ5RPrTt9HzWknPX7O1752RuC/DhfT/l2IM3rV2DF5g+7QTw==" />
</rails-partial></div><div class="prc-PageLayout-HorizontalDivider-JLVqp prc-PageLayout-HeaderHorizontalDivider-odAHl" data-variant="none" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div></header><div class="prc-PageLayout-PageLayoutContent-BneH9"><div class="prc-PageLayout-ContentWrapper-gR9eG" data-is-hidden="false"><div class="prc-PageLayout-Content-xWL-A" data-width="large" style="--spacing:var(--spacing-condensed)"><div class="OverviewContent-module__Box__PF75K tmp-pl-lg-3 mt-0"><div class="OverviewHeader-module__Box__cC1RH"></div><div class="OverviewContent-module__Box_1__MPS0U"><div class="OverviewContent-module__Box_2__Di8Pb"><div class="OverviewContent-module__Box_3__wzlJx"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" style="min-width:0" aria-label="main branch" data-testid="anchor-button" data-icv-name="Switch branches/tags" class="prc-Button-ButtonBase-9n-Xk overview-ref-selector width-full RefSelectorAnchoredOverlay-module__RefSelectorOverlayBtn__a3WK3" data-loading="false" data-size="medium" data-variant="default" id="ref-picker-repos-header-ref-selector"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayContainer__yaf4p"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayHeader__XtXRG"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="ref-selector-button-text-container RefSelectorAnchoredOverlay-module__RefSelectorBtnTextContainer__Di3rk"><span class="RefSelectorAnchoredOverlay-module__RefSelectorText__w_fmP"> <!-- -->main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-testid="ref-selector-hotkey-button" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="OverviewContent-module__Box_4__qf73o"><a type="button" href="/togethercomputer/together-py/branches" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button___Uotu" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Branches</span></span></a><a type="button" href="/togethercomputer/together-py/tags" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button___Uotu" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-tag" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Tags</span></span></a></div><div class="OverviewContent-module__Box_5__Zc3i7"><a type="button" aria-label="Go to Branches page" href="/togethercomputer/together-py/branches" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button_1__vmS6D" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></a><a type="button" aria-label="Go to Tags page" href="/togethercomputer/together-py/tags" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button_1__vmS6D" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible"><svg aria-hidden="true" focusable="false" class="octicon octicon-tag" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path></svg></a></div></div><div class="OverviewContent-module__Box_6__Y_Yb_"><div class="OverviewContent-module__Box_7__JuRXo"><div class="OverviewContent-module__Box_8__UZCZh"><!--$!--><template></template><!--/$--></div><div class="OverviewContent-module__Box_9__bqMPw"><button type="button" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Go to file</span></span></button></div></div><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-size="medium" data-variant="primary" id="_R_3idajal1d_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-code hide-sm" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Code</span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><div class="OverviewContent-module__Box_10__mGSb4"><button data-component="IconButton" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_R_3sidajal1d_" id="_R_4idajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_R_3sidajal1d_">Open more actions menu</span></div></div></div><div class="OverviewContent-module__Box_11__F19kY"><div data-hpc="true"><button hidden="" data-testid="focus-next-element-button" data-hotkey="j"></button><button hidden="" data-testid="focus-previous-element-button" data-hotkey="k"></button><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="folders-and-files">Folders and files</h2><table class="Table-module__Box__HZKiQ" aria-labelledby="folders-and-files"><thead class="DirectoryContent-module__OverviewHeaderRow__hOrKy Table-module__Box_1__VacXC"><tr class="Table-module__Box_2__PBp9s"><th colSpan="2" class="DirectoryContent-module__Box__iC_5e"><span class="text-bold">Name</span></th><th colSpan="1" class="DirectoryContent-module__Box_1__fuSBO"><span class="text-bold">Name</span></th><th class="hide-sm"><div class="width-fit prc-Truncate-Truncate-2G1eo" data-inline="true" title="Last commit message" style="--truncate-max-width:125px"><span class="text-bold">Last commit message</span></div></th><th colSpan="1" class="DirectoryContent-module__Box_2__Ccrx7"><div class="width-fit prc-Truncate-Truncate-2G1eo" data-inline="true" title="Last commit date" style="--truncate-max-width:125px"><span class="text-bold">Last commit date</span></div></th></tr></thead><tbody><tr class="DirectoryContent-module__Box_3__gl6dE"><td colSpan="3" class="bgColor-muted p-1 rounded-top-2"><div class="LatestCommit-module__Box__B25ZT"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">Latest commit</h2><div style="width:120px" class="Skeleton Skeleton--text" data-testid="loading"> </div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">History</h2><a href="/togethercomputer/together-py/commits/main/" class="prc-Button-ButtonBase-9n-Xk d-none d-lg-flex LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="fgColor-default">509 Commits</span></span></span></a><div class="d-sm-none"></div><div class="d-flex d-lg-none"><a aria-label="View commit history for this file." href="/togethercomputer/together-py/commits/main/" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby="_R_9d9kcdajal1d_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" role="tooltip" aria-hidden="true" id="_R_9d9kcdajal1d_">509 Commits</span></div></div></div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-0"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".devcontainer" aria-label=".devcontainer, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/.devcontainer" data-discover="true">.devcontainer</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".devcontainer" aria-label=".devcontainer, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/.devcontainer" data-discover="true">.devcontainer</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-1"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="This path skips through empty directories" aria-label=".github/workflows, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/.github/workflows" data-discover="true"><span class="react-directory-default-color" data-testid="path-name-segment">.github/</span><span class="" data-testid="path-name-segment">workflows</span></a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="This path skips through empty directories" aria-label=".github/workflows, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/.github/workflows" data-discover="true"><span class="react-directory-default-color" data-testid="path-name-segment">.github/</span><span class="" data-testid="path-name-segment">workflows</span></a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-2"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".vscode" aria-label=".vscode, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/.vscode" data-discover="true">.vscode</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".vscode" aria-label=".vscode, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/.vscode" data-discover="true">.vscode</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-3"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="bin" aria-label="bin, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/bin" data-discover="true">bin</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="bin" aria-label="bin, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/bin" data-discover="true">bin</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-4"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="examples" aria-label="examples, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/examples" data-discover="true">examples</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="examples" aria-label="examples, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/examples" data-discover="true">examples</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-5"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="scripts" aria-label="scripts, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/scripts" data-discover="true">scripts</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="scripts" aria-label="scripts, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/scripts" data-discover="true">scripts</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-6"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="This path skips through empty directories" aria-label="src/together, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/src/together" data-discover="true"><span class="react-directory-default-color" data-testid="path-name-segment">src/</span><span class="" data-testid="path-name-segment">together</span></a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="This path skips through empty directories" aria-label="src/together, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/src/together" data-discover="true"><span class="react-directory-default-color" data-testid="path-name-segment">src/</span><span class="" data-testid="path-name-segment">together</span></a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-7"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="tests" aria-label="tests, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/tests" data-discover="true">tests</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="tests" aria-label="tests, (Directory)" class="Link--primary" href="/togethercomputer/together-py/tree/main/tests" data-discover="true">tests</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-8"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".gitignore" aria-label=".gitignore, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/.gitignore" data-discover="true">.gitignore</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".gitignore" aria-label=".gitignore, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/.gitignore" data-discover="true">.gitignore</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-9"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".python-version" aria-label=".python-version, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/.python-version" data-discover="true">.python-version</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".python-version" aria-label=".python-version, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/.python-version" data-discover="true">.python-version</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-10"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".release-please-manifest.json" aria-label=".release-please-manifest.json, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/.release-please-manifest.json" data-discover="true">.release-please-manifest.json</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".release-please-manifest.json" aria-label=".release-please-manifest.json, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/.release-please-manifest.json" data-discover="true">.release-please-manifest.json</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-11"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".stats.yml" aria-label=".stats.yml, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/.stats.yml" data-discover="true">.stats.yml</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".stats.yml" aria-label=".stats.yml, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/.stats.yml" data-discover="true">.stats.yml</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-12"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="Brewfile" aria-label="Brewfile, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/Brewfile" data-discover="true">Brewfile</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="Brewfile" aria-label="Brewfile, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/Brewfile" data-discover="true">Brewfile</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-13"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="CHANGELOG.md" aria-label="CHANGELOG.md, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/CHANGELOG.md" data-discover="true">CHANGELOG.md</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="CHANGELOG.md" aria-label="CHANGELOG.md, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/CHANGELOG.md" data-discover="true">CHANGELOG.md</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-14"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="CONTRIBUTING.md" aria-label="CONTRIBUTING.md, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/CONTRIBUTING.md" data-discover="true">CONTRIBUTING.md</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="CONTRIBUTING.md" aria-label="CONTRIBUTING.md, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/CONTRIBUTING.md" data-discover="true">CONTRIBUTING.md</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-15"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="LICENSE" aria-label="LICENSE, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/LICENSE" data-discover="true">LICENSE</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="LICENSE" aria-label="LICENSE, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/LICENSE" data-discover="true">LICENSE</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-16"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="README.md" aria-label="README.md, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/README.md" data-discover="true">README.md</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="README.md" aria-label="README.md, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/README.md" data-discover="true">README.md</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-17"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="SECURITY.md" aria-label="SECURITY.md, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/SECURITY.md" data-discover="true">SECURITY.md</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="SECURITY.md" aria-label="SECURITY.md, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/SECURITY.md" data-discover="true">SECURITY.md</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-18"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="api.md" aria-label="api.md, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/api.md" data-discover="true">api.md</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="api.md" aria-label="api.md, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/api.md" data-discover="true">api.md</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-19"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="pyproject.toml" aria-label="pyproject.toml, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/pyproject.toml" data-discover="true">pyproject.toml</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="pyproject.toml" aria-label="pyproject.toml, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/pyproject.toml" data-discover="true">pyproject.toml</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-20"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="release-please-config.json" aria-label="release-please-config.json, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/release-please-config.json" data-discover="true">release-please-config.json</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="release-please-config.json" aria-label="release-please-config.json, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/release-please-config.json" data-discover="true">release-please-config.json</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-21"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="requirements-dev.lock" aria-label="requirements-dev.lock, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/requirements-dev.lock" data-discover="true">requirements-dev.lock</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="requirements-dev.lock" aria-label="requirements-dev.lock, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/requirements-dev.lock" data-discover="true">requirements-dev.lock</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-22"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="uv.lock" aria-label="uv.lock, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/uv.lock" data-discover="true">uv.lock</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="uv.lock" aria-label="uv.lock, (File)" class="Link--primary" href="/togethercomputer/together-py/blob/main/uv.lock" data-discover="true">uv.lock</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="show-for-mobile DirectoryContent-module__Box_4__RhIsE" data-testid="view-all-files-row"><td colSpan="3" class="DirectoryContent-module__Box_5__GaE8N"><div><button class="prc-Link-Link-9ZwDx">View all files</button></div></td></tr></tbody></table></div><div class="OverviewRepoFiles-module__Box_1__OXeac"><div class="OverviewRepoFiles-module__Box_2__zsLGk"><div itemScope="" itemType="https://schema.org/abstract" class="OverviewRepoFiles-module__Box_3__bBU1C"><h2 class="prc-src-InternalVisuallyHidden-2YaI6">Repository files navigation</h2><nav class="prc-components-UnderlineWrapper-eT-Yj OverviewRepoFiles-module__UnderlineNav__QbWWv" aria-label="Repository files" data-variant="inset" data-overflow-measured="false"><ul class="prc-components-UnderlineItemList-xKlKC" role="list"><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="#" aria-current="page" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-book" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path></svg></span><span data-component="text" data-content="README">README</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="#" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-people" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path></svg></span><span data-component="text" data-content="Contributing">Contributing</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="#" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-law" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8.75.75V2h.985c.304 0 .603.08.867.231l1.29.736c.038.022.08.033.124.033h2.234a.75.75 0 0 1 0 1.5h-.427l2.111 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.006.005-.01.01-.045.04c-.21.176-.441.327-.686.45C14.556 10.78 13.88 11 13 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L12.178 4.5h-.162c-.305 0-.604-.079-.868-.231l-1.29-.736a.245.245 0 0 0-.124-.033H8.75V13h2.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1 0-1.5h2.5V3.5h-.984a.245.245 0 0 0-.124.033l-1.289.737c-.265.15-.564.23-.869.23h-.162l2.112 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.016.015-.045.04c-.21.176-.441.327-.686.45C4.556 10.78 3.88 11 3 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L2.178 4.5H1.75a.75.75 0 0 1 0-1.5h2.234a.249.249 0 0 0 .125-.033l1.288-.737c.265-.15.564-.23.869-.23h.984V.75a.75.75 0 0 1 1.5 0Zm2.945 8.477c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327Zm-10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327Z"></path></svg></span><span data-component="text" data-content="Apache-2.0 license">Apache-2.0 license</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="#" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-law" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8.75.75V2h.985c.304 0 .603.08.867.231l1.29.736c.038.022.08.033.124.033h2.234a.75.75 0 0 1 0 1.5h-.427l2.111 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.006.005-.01.01-.045.04c-.21.176-.441.327-.686.45C14.556 10.78 13.88 11 13 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L12.178 4.5h-.162c-.305 0-.604-.079-.868-.231l-1.29-.736a.245.245 0 0 0-.124-.033H8.75V13h2.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1 0-1.5h2.5V3.5h-.984a.245.245 0 0 0-.124.033l-1.289.737c-.265.15-.564.23-.869.23h-.162l2.112 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.016.015-.045.04c-.21.176-.441.327-.686.45C4.556 10.78 3.88 11 3 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L2.178 4.5H1.75a.75.75 0 0 1 0-1.5h2.234a.249.249 0 0 0 .125-.033l1.288-.737c.265-.15.564-.23.869-.23h.984V.75a.75.75 0 0 1 1.5 0Zm2.945 8.477c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327Zm-10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327Z"></path></svg></span><span data-component="text" data-content="Security">Security</span></a></li></ul></nav><button type="button" aria-label="Outline" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk OverviewRepoFiles-module__ActionMenu_Button__OKDYV" data-loading="false" data-size="medium" data-variant="invisible" id="_R_dkdajal1d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-list-unordered" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg></button></div><div class="Box-sc-62in7e-0 js-snippet-clipboard-copy-unpositioned DirectoryRichtextContent-module__SharedMarkdownContent__hHXUL" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><div class="markdown-heading" dir="auto"><h1 tabindex="-1" class="heading-element" dir="auto">Together Python API library</h1><a id="user-content-together-python-api-library" class="anchor" aria-label="Permalink: Together Python API library" href="#together-python-api-library"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>

<p dir="auto"><a href="https://pypi.org/project/together/" rel="nofollow"><img src="https://camo.githubusercontent.com/d91235b9694c1546c6b0fac18a791e6d8d3b8958c0049f3fe504ecf52c83226c/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f746f6765746865722e7376673f6c6162656c3d7079706925323028737461626c6529" alt="PyPI version" data-canonical-src="https://img.shields.io/pypi/v/together.svg?label=pypi%20(stable)" style="max-width: 100%;"></a></p>
<p dir="auto">The Together Python library provides convenient access to the Together REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by <a href="https://github.com/encode/httpx">httpx</a>.</p>
<p dir="auto">It is generated with <a href="https://www.stainless.com/" rel="nofollow">Stainless</a>.</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Documentation</h2><a id="user-content-documentation" class="anchor" aria-label="Permalink: Documentation" href="#documentation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">The REST API documentation can be found on <a href="https://docs.together.ai/" rel="nofollow">docs.together.ai</a>. The full API of this library can be found in <a href="/togethercomputer/together-py/blob/main/api.md">api.md</a>.</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Installation</h2><a id="user-content-installation" class="anchor" aria-label="Permalink: Installation" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="pip install together"><pre>pip install together</pre></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="uv add together"><pre>uv add together</pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Usage</h2><a id="user-content-usage" class="anchor" aria-label="Permalink: Usage" href="#usage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">The full API of this library can be found in <a href="/togethercomputer/together-py/blob/main/api.md">api.md</a>.</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import os
from together import Together

client = Together(
    api_key=os.environ.get(&quot;TOGETHER_API_KEY&quot;),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            &quot;role&quot;: &quot;user&quot;,
            &quot;content&quot;: &quot;Say this is a test!&quot;,
        }
    ],
    model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
)
print(chat_completion.choices)"><pre><span class="pl-k">import</span> <span class="pl-s1">os</span>
<span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">Together</span>

<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">Together</span>(
    <span class="pl-s1">api_key</span><span class="pl-c1">=</span><span class="pl-s1">os</span>.<span class="pl-c1">environ</span>.<span class="pl-c1">get</span>(<span class="pl-s">"TOGETHER_API_KEY"</span>),  <span class="pl-c"># This is the default and can be omitted</span>
)

<span class="pl-s1">chat_completion</span> <span class="pl-c1">=</span> <span class="pl-s1">client</span>.<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">create</span>(
    <span class="pl-s1">messages</span><span class="pl-c1">=</span>[
        {
            <span class="pl-s">"role"</span>: <span class="pl-s">"user"</span>,
            <span class="pl-s">"content"</span>: <span class="pl-s">"Say this is a test!"</span>,
        }
    ],
    <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
)
<span class="pl-en">print</span>(<span class="pl-s1">chat_completion</span>.<span class="pl-c1">choices</span>)</pre></div>
<p dir="auto">While you can provide an <code>api_key</code> keyword argument,
we recommend using <a href="https://pypi.org/project/python-dotenv/" rel="nofollow">python-dotenv</a>
to add <code>TOGETHER_API_KEY="My API Key"</code> to your <code>.env</code> file
so that your API Key is not stored in source control.</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Async usage</h2><a id="user-content-async-usage" class="anchor" aria-label="Permalink: Async usage" href="#async-usage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Simply import <code>AsyncTogether</code> instead of <code>Together</code> and use <code>await</code> with each API call:</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import os
import asyncio
from together import AsyncTogether

client = AsyncTogether(
    api_key=os.environ.get(&quot;TOGETHER_API_KEY&quot;),  # This is the default and can be omitted
)


async def main() -&gt; None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                &quot;role&quot;: &quot;user&quot;,
                &quot;content&quot;: &quot;Say this is a test!&quot;,
            }
        ],
        model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
    )
    print(chat_completion.choices)


asyncio.run(main())"><pre><span class="pl-k">import</span> <span class="pl-s1">os</span>
<span class="pl-k">import</span> <span class="pl-s1">asyncio</span>
<span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">AsyncTogether</span>

<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">AsyncTogether</span>(
    <span class="pl-s1">api_key</span><span class="pl-c1">=</span><span class="pl-s1">os</span>.<span class="pl-c1">environ</span>.<span class="pl-c1">get</span>(<span class="pl-s">"TOGETHER_API_KEY"</span>),  <span class="pl-c"># This is the default and can be omitted</span>
)


<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">main</span>() <span class="pl-c1">-&gt;</span> <span class="pl-c1">None</span>:
    <span class="pl-s1">chat_completion</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">client</span>.<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">create</span>(
        <span class="pl-s1">messages</span><span class="pl-c1">=</span>[
            {
                <span class="pl-s">"role"</span>: <span class="pl-s">"user"</span>,
                <span class="pl-s">"content"</span>: <span class="pl-s">"Say this is a test!"</span>,
            }
        ],
        <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
    )
    <span class="pl-en">print</span>(<span class="pl-s1">chat_completion</span>.<span class="pl-c1">choices</span>)


<span class="pl-s1">asyncio</span>.<span class="pl-c1">run</span>(<span class="pl-en">main</span>())</pre></div>
<p dir="auto">Functionality between the synchronous and asynchronous clients is otherwise identical.</p>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">With aiohttp</h3><a id="user-content-with-aiohttp" class="anchor" aria-label="Permalink: With aiohttp" href="#with-aiohttp"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">By default, the async client uses <code>httpx</code> for HTTP requests. However, for improved concurrency performance you may also use <code>aiohttp</code> as the HTTP backend.</p>
<p dir="auto">You can enable this by installing <code>aiohttp</code>:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# install from PyPI
pip install '--pre together[aiohttp]'"><pre><span class="pl-c"><span class="pl-c">#</span> install from PyPI</span>
pip install <span class="pl-s"><span class="pl-pds">'</span>--pre together[aiohttp]<span class="pl-pds">'</span></span></pre></div>
<p dir="auto">Then you can enable it by instantiating the client with <code>http_client=DefaultAioHttpClient()</code>:</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import os
import asyncio
from together import DefaultAioHttpClient
from together import AsyncTogether


async def main() -&gt; None:
    async with AsyncTogether(
        api_key=os.environ.get(&quot;TOGETHER_API_KEY&quot;),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as client:
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    &quot;role&quot;: &quot;user&quot;,
                    &quot;content&quot;: &quot;Say this is a test!&quot;,
                }
            ],
            model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
        )
        print(chat_completion.choices)


asyncio.run(main())"><pre><span class="pl-k">import</span> <span class="pl-s1">os</span>
<span class="pl-k">import</span> <span class="pl-s1">asyncio</span>
<span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">DefaultAioHttpClient</span>
<span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">AsyncTogether</span>


<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">main</span>() <span class="pl-c1">-&gt;</span> <span class="pl-c1">None</span>:
    <span class="pl-k">async</span> <span class="pl-k">with</span> <span class="pl-en">AsyncTogether</span>(
        <span class="pl-s1">api_key</span><span class="pl-c1">=</span><span class="pl-s1">os</span>.<span class="pl-c1">environ</span>.<span class="pl-c1">get</span>(<span class="pl-s">"TOGETHER_API_KEY"</span>),  <span class="pl-c"># This is the default and can be omitted</span>
        <span class="pl-s1">http_client</span><span class="pl-c1">=</span><span class="pl-en">DefaultAioHttpClient</span>(),
    ) <span class="pl-k">as</span> <span class="pl-s1">client</span>:
        <span class="pl-s1">chat_completion</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">client</span>.<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">create</span>(
            <span class="pl-s1">messages</span><span class="pl-c1">=</span>[
                {
                    <span class="pl-s">"role"</span>: <span class="pl-s">"user"</span>,
                    <span class="pl-s">"content"</span>: <span class="pl-s">"Say this is a test!"</span>,
                }
            ],
            <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
        )
        <span class="pl-en">print</span>(<span class="pl-s1">chat_completion</span>.<span class="pl-c1">choices</span>)


<span class="pl-s1">asyncio</span>.<span class="pl-c1">run</span>(<span class="pl-en">main</span>())</pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Streaming responses</h2><a id="user-content-streaming-responses" class="anchor" aria-label="Permalink: Streaming responses" href="#streaming-responses"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">We provide support for streaming responses using Server Side Events (SSE).</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="from together import Together

client = Together()

stream = client.chat.completions.create(
    messages=[
        {
            &quot;role&quot;: &quot;user&quot;,
            &quot;content&quot;: &quot;Say this is a test!&quot;,
        }
    ],
    model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
    stream=True,
)
for chat_completion in stream:
    print(chat_completion.choices)"><pre><span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">Together</span>

<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">Together</span>()

<span class="pl-s1">stream</span> <span class="pl-c1">=</span> <span class="pl-s1">client</span>.<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">create</span>(
    <span class="pl-s1">messages</span><span class="pl-c1">=</span>[
        {
            <span class="pl-s">"role"</span>: <span class="pl-s">"user"</span>,
            <span class="pl-s">"content"</span>: <span class="pl-s">"Say this is a test!"</span>,
        }
    ],
    <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
    <span class="pl-s1">stream</span><span class="pl-c1">=</span><span class="pl-c1">True</span>,
)
<span class="pl-k">for</span> <span class="pl-s1">chat_completion</span> <span class="pl-c1">in</span> <span class="pl-s1">stream</span>:
    <span class="pl-en">print</span>(<span class="pl-s1">chat_completion</span>.<span class="pl-c1">choices</span>)</pre></div>
<p dir="auto">The async client uses the exact same interface.</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="from together import AsyncTogether

client = AsyncTogether()

stream = await client.chat.completions.create(
    messages=[
        {
            &quot;role&quot;: &quot;user&quot;,
            &quot;content&quot;: &quot;Say this is a test!&quot;,
        }
    ],
    model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
    stream=True,
)
async for chat_completion in stream:
    print(chat_completion.choices)"><pre><span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">AsyncTogether</span>

<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">AsyncTogether</span>()

<span class="pl-s1">stream</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">client</span>.<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">create</span>(
    <span class="pl-s1">messages</span><span class="pl-c1">=</span>[
        {
            <span class="pl-s">"role"</span>: <span class="pl-s">"user"</span>,
            <span class="pl-s">"content"</span>: <span class="pl-s">"Say this is a test!"</span>,
        }
    ],
    <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
    <span class="pl-s1">stream</span><span class="pl-c1">=</span><span class="pl-c1">True</span>,
)
<span class="pl-k">async</span> <span class="pl-k">for</span> <span class="pl-s1">chat_completion</span> <span class="pl-c1">in</span> <span class="pl-s1">stream</span>:
    <span class="pl-en">print</span>(<span class="pl-s1">chat_completion</span>.<span class="pl-c1">choices</span>)</pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Using types</h2><a id="user-content-using-types" class="anchor" aria-label="Permalink: Using types" href="#using-types"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Nested request parameters are <a href="https://docs.python.org/3/library/typing.html#typing.TypedDict" rel="nofollow">TypedDicts</a>. Responses are <a href="https://docs.pydantic.dev" rel="nofollow">Pydantic models</a> which also provide helper methods for things like:</p>
<ul dir="auto">
<li>Serializing back into JSON, <code>model.to_json()</code></li>
<li>Converting to a dictionary, <code>model.to_dict()</code></li>
</ul>
<p dir="auto">Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set <code>python.analysis.typeCheckingMode</code> to <code>basic</code>.</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Nested params</h2><a id="user-content-nested-params" class="anchor" aria-label="Permalink: Nested params" href="#nested-params"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Nested parameters are dictionaries, typed using <code>TypedDict</code>, for example:</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="from together import Together

client = Together()

chat_completion = client.chat.completions.create(
    messages=[
        {
            &quot;content&quot;: &quot;content&quot;,
            &quot;role&quot;: &quot;system&quot;,
        }
    ],
    model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
    reasoning={},
)
print(chat_completion.reasoning)"><pre><span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">Together</span>

<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">Together</span>()

<span class="pl-s1">chat_completion</span> <span class="pl-c1">=</span> <span class="pl-s1">client</span>.<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">create</span>(
    <span class="pl-s1">messages</span><span class="pl-c1">=</span>[
        {
            <span class="pl-s">"content"</span>: <span class="pl-s">"content"</span>,
            <span class="pl-s">"role"</span>: <span class="pl-s">"system"</span>,
        }
    ],
    <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
    <span class="pl-s1">reasoning</span><span class="pl-c1">=</span>{},
)
<span class="pl-en">print</span>(<span class="pl-s1">chat_completion</span>.<span class="pl-c1">reasoning</span>)</pre></div>
<p dir="auto">The async client uses the exact same interface. If you pass a <a href="https://docs.python.org/3/library/os.html#os.PathLike" rel="nofollow"><code>PathLike</code></a> instance, the file contents will be read asynchronously automatically.</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Handling errors</h2><a id="user-content-handling-errors" class="anchor" aria-label="Permalink: Handling errors" href="#handling-errors"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of <code>together.APIConnectionError</code> is raised.</p>
<p dir="auto">When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of <code>together.APIStatusError</code> is raised, containing <code>status_code</code> and <code>response</code> properties.</p>
<p dir="auto">All errors inherit from <code>together.APIError</code>.</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import together
from together import Together

client = Together()

try:
    client.chat.completions.create(
        messages=[
            {
                &quot;role&quot;: &quot;user&quot;,
                &quot;content&quot;: &quot;Say this is a test&quot;,
            }
        ],
        model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
    )
except together.APIConnectionError as e:
    print(&quot;The server could not be reached&quot;)
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except together.RateLimitError as e:
    print(&quot;A 429 status code was received; we should back off a bit.&quot;)
except together.APIStatusError as e:
    print(&quot;Another non-200-range status code was received&quot;)
    print(e.status_code)
    print(e.response)"><pre><span class="pl-k">import</span> <span class="pl-s1">together</span>
<span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">Together</span>

<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">Together</span>()

<span class="pl-k">try</span>:
    <span class="pl-s1">client</span>.<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">create</span>(
        <span class="pl-s1">messages</span><span class="pl-c1">=</span>[
            {
                <span class="pl-s">"role"</span>: <span class="pl-s">"user"</span>,
                <span class="pl-s">"content"</span>: <span class="pl-s">"Say this is a test"</span>,
            }
        ],
        <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
    )
<span class="pl-k">except</span> <span class="pl-s1">together</span>.<span class="pl-c1">APIConnectionError</span> <span class="pl-k">as</span> <span class="pl-s1">e</span>:
    <span class="pl-en">print</span>(<span class="pl-s">"The server could not be reached"</span>)
    <span class="pl-en">print</span>(<span class="pl-s1">e</span>.<span class="pl-c1">__cause__</span>)  <span class="pl-c"># an underlying Exception, likely raised within httpx.</span>
<span class="pl-k">except</span> <span class="pl-s1">together</span>.<span class="pl-c1">RateLimitError</span> <span class="pl-k">as</span> <span class="pl-s1">e</span>:
    <span class="pl-en">print</span>(<span class="pl-s">"A 429 status code was received; we should back off a bit."</span>)
<span class="pl-k">except</span> <span class="pl-s1">together</span>.<span class="pl-c1">APIStatusError</span> <span class="pl-k">as</span> <span class="pl-s1">e</span>:
    <span class="pl-en">print</span>(<span class="pl-s">"Another non-200-range status code was received"</span>)
    <span class="pl-en">print</span>(<span class="pl-s1">e</span>.<span class="pl-c1">status_code</span>)
    <span class="pl-en">print</span>(<span class="pl-s1">e</span>.<span class="pl-c1">response</span>)</pre></div>
<p dir="auto">Error codes are as follows:</p>
<markdown-accessiblity-table><table>
<thead>
<tr>
<th>Status Code</th>
<th>Error Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>400</td>
<td><code>BadRequestError</code></td>
</tr>
<tr>
<td>401</td>
<td><code>AuthenticationError</code></td>
</tr>
<tr>
<td>403</td>
<td><code>PermissionDeniedError</code></td>
</tr>
<tr>
<td>404</td>
<td><code>NotFoundError</code></td>
</tr>
<tr>
<td>422</td>
<td><code>UnprocessableEntityError</code></td>
</tr>
<tr>
<td>429</td>
<td><code>RateLimitError</code></td>
</tr>
<tr>
<td>&gt;=500</td>
<td><code>InternalServerError</code></td>
</tr>
<tr>
<td>N/A</td>
<td><code>APIConnectionError</code></td>
</tr>
</tbody>
</table></markdown-accessiblity-table>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Retries</h3><a id="user-content-retries" class="anchor" aria-label="Permalink: Retries" href="#retries"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and &gt;=500 Internal errors are all retried by default.</p>
<p dir="auto">You can use the <code>max_retries</code> option to configure or disable retry settings:</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="from together import Together

# Configure the default for all requests:
client = Together(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).chat.completions.create(
    messages=[
        {
            &quot;role&quot;: &quot;user&quot;,
            &quot;content&quot;: &quot;Say this is a test&quot;,
        }
    ],
    model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
)"><pre><span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">Together</span>

<span class="pl-c"># Configure the default for all requests:</span>
<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">Together</span>(
    <span class="pl-c"># default is 2</span>
    <span class="pl-s1">max_retries</span><span class="pl-c1">=</span><span class="pl-c1">0</span>,
)

<span class="pl-c"># Or, configure per-request:</span>
<span class="pl-s1">client</span>.<span class="pl-c1">with_options</span>(<span class="pl-s1">max_retries</span><span class="pl-c1">=</span><span class="pl-c1">5</span>).<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">create</span>(
    <span class="pl-s1">messages</span><span class="pl-c1">=</span>[
        {
            <span class="pl-s">"role"</span>: <span class="pl-s">"user"</span>,
            <span class="pl-s">"content"</span>: <span class="pl-s">"Say this is a test"</span>,
        }
    ],
    <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
)</pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Timeouts</h3><a id="user-content-timeouts" class="anchor" aria-label="Permalink: Timeouts" href="#timeouts"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">By default requests time out after 1 minute. You can configure this with a <code>timeout</code> option,
which accepts a float or an <a href="https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration" rel="nofollow"><code>httpx.Timeout</code></a> object:</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="from together import Together

# Configure the default for all requests:
client = Together(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Together(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).chat.completions.create(
    messages=[
        {
            &quot;role&quot;: &quot;user&quot;,
            &quot;content&quot;: &quot;Say this is a test&quot;,
        }
    ],
    model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
)"><pre><span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">Together</span>

<span class="pl-c"># Configure the default for all requests:</span>
<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">Together</span>(
    <span class="pl-c"># 20 seconds (default is 1 minute)</span>
    <span class="pl-s1">timeout</span><span class="pl-c1">=</span><span class="pl-c1">20.0</span>,
)

<span class="pl-c"># More granular control:</span>
<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">Together</span>(
    <span class="pl-s1">timeout</span><span class="pl-c1">=</span><span class="pl-s1">httpx</span>.<span class="pl-c1">Timeout</span>(<span class="pl-c1">60.0</span>, <span class="pl-s1">read</span><span class="pl-c1">=</span><span class="pl-c1">5.0</span>, <span class="pl-s1">write</span><span class="pl-c1">=</span><span class="pl-c1">10.0</span>, <span class="pl-s1">connect</span><span class="pl-c1">=</span><span class="pl-c1">2.0</span>),
)

<span class="pl-c"># Override per-request:</span>
<span class="pl-s1">client</span>.<span class="pl-c1">with_options</span>(<span class="pl-s1">timeout</span><span class="pl-c1">=</span><span class="pl-c1">5.0</span>).<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">create</span>(
    <span class="pl-s1">messages</span><span class="pl-c1">=</span>[
        {
            <span class="pl-s">"role"</span>: <span class="pl-s">"user"</span>,
            <span class="pl-s">"content"</span>: <span class="pl-s">"Say this is a test"</span>,
        }
    ],
    <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
)</pre></div>
<p dir="auto">On timeout, an <code>APITimeoutError</code> is thrown.</p>
<p dir="auto">Note that requests that time out are <a href="#retries">retried twice by default</a>.</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Advanced</h2><a id="user-content-advanced" class="anchor" aria-label="Permalink: Advanced" href="#advanced"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Logging</h3><a id="user-content-logging" class="anchor" aria-label="Permalink: Logging" href="#logging"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">We use the standard library <a href="https://docs.python.org/3/library/logging.html" rel="nofollow"><code>logging</code></a> module.</p>
<p dir="auto">You can enable logging by setting the environment variable <code>TOGETHER_LOG</code> to <code>info</code>.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="$ export TOGETHER_LOG=info"><pre>$ <span class="pl-k">export</span> TOGETHER_LOG=info</pre></div>
<p dir="auto">Or to <code>debug</code> for more verbose logging.</p>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">How to tell whether <code>None</code> means <code>null</code> or missing</h3><a id="user-content-how-to-tell-whether-none-means-null-or-missing" class="anchor" aria-label="Permalink: How to tell whether None means null or missing" href="#how-to-tell-whether-none-means-null-or-missing"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">In an API response, a field may be explicitly <code>null</code>, or missing entirely; in either case, its value is <code>None</code> in this library. You can differentiate the two cases with <code>.model_fields_set</code>:</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a &quot;my_field&quot; key present at all.')
  else:
    print('Got json like {&quot;my_field&quot;: null}.')"><pre><span class="pl-k">if</span> <span class="pl-s1">response</span>.<span class="pl-c1">my_field</span> <span class="pl-c1">is</span> <span class="pl-c1">None</span>:
  <span class="pl-k">if</span> <span class="pl-s">'my_field'</span> <span class="pl-c1"><span class="pl-c1">not</span> <span class="pl-c1">in</span></span> <span class="pl-s1">response</span>.<span class="pl-c1">model_fields_set</span>:
    <span class="pl-en">print</span>(<span class="pl-s">'Got json like {}, without a "my_field" key present at all.'</span>)
  <span class="pl-k">else</span>:
    <span class="pl-en">print</span>(<span class="pl-s">'Got json like {"my_field": null}.'</span>)</pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Accessing raw response data (e.g. headers)</h3><a id="user-content-accessing-raw-response-data-eg-headers" class="anchor" aria-label="Permalink: Accessing raw response data (e.g. headers)" href="#accessing-raw-response-data-eg-headers"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">The "raw" Response object can be accessed by prefixing <code>.with_raw_response.</code> to any HTTP method call, e.g.,</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="from together import Together

client = Together()
response = client.chat.completions.with_raw_response.create(
    messages=[{
        &quot;role&quot;: &quot;user&quot;,
        &quot;content&quot;: &quot;Say this is a test&quot;,
    }],
    model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion.choices)"><pre><span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">Together</span>

<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">Together</span>()
<span class="pl-s1">response</span> <span class="pl-c1">=</span> <span class="pl-s1">client</span>.<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">with_raw_response</span>.<span class="pl-c1">create</span>(
    <span class="pl-s1">messages</span><span class="pl-c1">=</span>[{
        <span class="pl-s">"role"</span>: <span class="pl-s">"user"</span>,
        <span class="pl-s">"content"</span>: <span class="pl-s">"Say this is a test"</span>,
    }],
    <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
)
<span class="pl-en">print</span>(<span class="pl-s1">response</span>.<span class="pl-c1">headers</span>.<span class="pl-c1">get</span>(<span class="pl-s">'X-My-Header'</span>))

<span class="pl-s1">completion</span> <span class="pl-c1">=</span> <span class="pl-s1">response</span>.<span class="pl-c1">parse</span>()  <span class="pl-c"># get the object that `chat.completions.create()` would have returned</span>
<span class="pl-en">print</span>(<span class="pl-s1">completion</span>.<span class="pl-c1">choices</span>)</pre></div>
<p dir="auto">These methods return an <a href="https://github.com/togethercomputer/together-py/tree/main/src/together/_response.py"><code>APIResponse</code></a> object.</p>
<p dir="auto">The async client returns an <a href="https://github.com/togethercomputer/together-py/tree/main/src/together/_response.py"><code>AsyncAPIResponse</code></a> with the same structure, the only difference being <code>await</code>able methods for reading the response content.</p>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto"><code>.with_streaming_response</code></h4><a id="user-content-with_streaming_response" class="anchor" aria-label="Permalink: .with_streaming_response" href="#with_streaming_response"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">The above interface eagerly reads the full response body when you make the request, which may not always be what you want.</p>
<p dir="auto">To stream the response body, use <code>.with_streaming_response</code> instead, which requires a context manager and only reads the response body once you call <code>.read()</code>, <code>.text()</code>, <code>.json()</code>, <code>.iter_bytes()</code>, <code>.iter_text()</code>, <code>.iter_lines()</code> or <code>.parse()</code>. In the async client, these are async methods.</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="with client.chat.completions.with_streaming_response.create(
    messages=[
        {
            &quot;role&quot;: &quot;user&quot;,
            &quot;content&quot;: &quot;Say this is a test&quot;,
        }
    ],
    model=&quot;meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo&quot;,
) as response:
    print(response.headers.get(&quot;X-My-Header&quot;))

    for line in response.iter_lines():
        print(line)"><pre><span class="pl-k">with</span> <span class="pl-s1">client</span>.<span class="pl-c1">chat</span>.<span class="pl-c1">completions</span>.<span class="pl-c1">with_streaming_response</span>.<span class="pl-c1">create</span>(
    <span class="pl-s1">messages</span><span class="pl-c1">=</span>[
        {
            <span class="pl-s">"role"</span>: <span class="pl-s">"user"</span>,
            <span class="pl-s">"content"</span>: <span class="pl-s">"Say this is a test"</span>,
        }
    ],
    <span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"</span>,
) <span class="pl-k">as</span> <span class="pl-s1">response</span>:
    <span class="pl-en">print</span>(<span class="pl-s1">response</span>.<span class="pl-c1">headers</span>.<span class="pl-c1">get</span>(<span class="pl-s">"X-My-Header"</span>))

    <span class="pl-k">for</span> <span class="pl-s1">line</span> <span class="pl-c1">in</span> <span class="pl-s1">response</span>.<span class="pl-c1">iter_lines</span>():
        <span class="pl-en">print</span>(<span class="pl-s1">line</span>)</pre></div>
<p dir="auto">The context manager is required so that the response will reliably be closed.</p>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Making custom/undocumented requests</h3><a id="user-content-making-customundocumented-requests" class="anchor" aria-label="Permalink: Making custom/undocumented requests" href="#making-customundocumented-requests"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">This library is typed for convenient access to the documented API.</p>
<p dir="auto">If you need to access undocumented endpoints, params, or response properties, the library can still be used.</p>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Undocumented endpoints</h4><a id="user-content-undocumented-endpoints" class="anchor" aria-label="Permalink: Undocumented endpoints" href="#undocumented-endpoints"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">To make requests to undocumented endpoints, you can make requests using <code>client.get</code>, <code>client.post</code>, and other
http verbs. Options on the client will be respected (such as retries) when making this request.</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import httpx

response = client.post(
    &quot;/foo&quot;,
    cast_to=httpx.Response,
    body={&quot;my_param&quot;: True},
)

print(response.headers.get(&quot;x-foo&quot;))"><pre><span class="pl-k">import</span> <span class="pl-s1">httpx</span>

<span class="pl-s1">response</span> <span class="pl-c1">=</span> <span class="pl-s1">client</span>.<span class="pl-c1">post</span>(
    <span class="pl-s">"/foo"</span>,
    <span class="pl-s1">cast_to</span><span class="pl-c1">=</span><span class="pl-s1">httpx</span>.<span class="pl-c1">Response</span>,
    <span class="pl-s1">body</span><span class="pl-c1">=</span>{<span class="pl-s">"my_param"</span>: <span class="pl-c1">True</span>},
)

<span class="pl-en">print</span>(<span class="pl-s1">response</span>.<span class="pl-c1">headers</span>.<span class="pl-c1">get</span>(<span class="pl-s">"x-foo"</span>))</pre></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Undocumented request params</h4><a id="user-content-undocumented-request-params" class="anchor" aria-label="Permalink: Undocumented request params" href="#undocumented-request-params"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">If you want to explicitly send an extra param, you can do so with the <code>extra_query</code>, <code>extra_body</code>, and <code>extra_headers</code> request
options.</p>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Undocumented response properties</h4><a id="user-content-undocumented-response-properties" class="anchor" aria-label="Permalink: Undocumented response properties" href="#undocumented-response-properties"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">To access undocumented response properties, you can access the extra fields like <code>response.unknown_prop</code>. You
can also get all the extra fields on the Pydantic model as a dict with
<a href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra" rel="nofollow"><code>response.model_extra</code></a>.</p>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Configuring the HTTP client</h3><a id="user-content-configuring-the-http-client" class="anchor" aria-label="Permalink: Configuring the HTTP client" href="#configuring-the-http-client"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">You can directly override the <a href="https://www.python-httpx.org/api/#client" rel="nofollow">httpx client</a> to customize it for your use case, including:</p>
<ul dir="auto">
<li>Support for <a href="https://www.python-httpx.org/advanced/proxies/" rel="nofollow">proxies</a></li>
<li>Custom <a href="https://www.python-httpx.org/advanced/transports/" rel="nofollow">transports</a></li>
<li>Additional <a href="https://www.python-httpx.org/advanced/clients/" rel="nofollow">advanced</a> functionality</li>
</ul>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import httpx
from together import Together, DefaultHttpxClient

client = Together(
    # Or use the `TOGETHER_BASE_URL` env var
    base_url=&quot;http://my.test.server.example.com:8083&quot;,
    http_client=DefaultHttpxClient(
        proxy=&quot;http://my.test.proxy.example.com&quot;,
        transport=httpx.HTTPTransport(local_address=&quot;0.0.0.0&quot;),
    ),
)"><pre><span class="pl-k">import</span> <span class="pl-s1">httpx</span>
<span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">Together</span>, <span class="pl-v">DefaultHttpxClient</span>

<span class="pl-s1">client</span> <span class="pl-c1">=</span> <span class="pl-en">Together</span>(
    <span class="pl-c"># Or use the `TOGETHER_BASE_URL` env var</span>
    <span class="pl-s1">base_url</span><span class="pl-c1">=</span><span class="pl-s">"http://my.test.server.example.com:8083"</span>,
    <span class="pl-s1">http_client</span><span class="pl-c1">=</span><span class="pl-en">DefaultHttpxClient</span>(
        <span class="pl-s1">proxy</span><span class="pl-c1">=</span><span class="pl-s">"http://my.test.proxy.example.com"</span>,
        <span class="pl-s1">transport</span><span class="pl-c1">=</span><span class="pl-s1">httpx</span>.<span class="pl-c1">HTTPTransport</span>(<span class="pl-s1">local_address</span><span class="pl-c1">=</span><span class="pl-s">"0.0.0.0"</span>),
    ),
)</pre></div>
<p dir="auto">You can also customize the client on a per-request basis by using <code>with_options()</code>:</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="client.with_options(http_client=DefaultHttpxClient(...))"><pre><span class="pl-s1">client</span>.<span class="pl-c1">with_options</span>(<span class="pl-s1">http_client</span><span class="pl-c1">=</span><span class="pl-en">DefaultHttpxClient</span>(...))</pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Managing HTTP resources</h3><a id="user-content-managing-http-resources" class="anchor" aria-label="Permalink: Managing HTTP resources" href="#managing-http-resources"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">By default the library closes underlying HTTP connections whenever the client is <a href="https://docs.python.org/3/reference/datamodel.html#object.__del__" rel="nofollow">garbage collected</a>. You can manually close the client using the <code>.close()</code> method if desired, or with a context manager that closes when exiting.</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="from together import Together

with Together() as client:
  # make requests here
  ...

# HTTP client is now closed"><pre><span class="pl-k">from</span> <span class="pl-s1">together</span> <span class="pl-k">import</span> <span class="pl-v">Together</span>

<span class="pl-k">with</span> <span class="pl-en">Together</span>() <span class="pl-k">as</span> <span class="pl-s1">client</span>:
  <span class="pl-c"># make requests here</span>
  ...

<span class="pl-c"># HTTP client is now closed</span></pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Usage – CLI</h2><a id="user-content-usage--cli" class="anchor" aria-label="Permalink: Usage – CLI" href="#usage--cli"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Files</h3><a id="user-content-files" class="anchor" aria-label="Permalink: Files" href="#files"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together files --help

# Check file
together files check example.jsonl

# Upload file
together files upload example.jsonl

# List files
together files list

# Retrieve file metadata
together files retrieve file-6f50f9d1-5b95-416c-9040-0799b2b4b894

# Retrieve file content
together files retrieve-content file-6f50f9d1-5b95-416c-9040-0799b2b4b894

# Delete remote file
together files delete file-6f50f9d1-5b95-416c-9040-0799b2b4b894"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together files --help

<span class="pl-c"><span class="pl-c">#</span> Check file</span>
together files check example.jsonl

<span class="pl-c"><span class="pl-c">#</span> Upload file</span>
together files upload example.jsonl

<span class="pl-c"><span class="pl-c">#</span> List files</span>
together files list

<span class="pl-c"><span class="pl-c">#</span> Retrieve file metadata</span>
together files retrieve file-6f50f9d1-5b95-416c-9040-0799b2b4b894

<span class="pl-c"><span class="pl-c">#</span> Retrieve file content</span>
together files retrieve-content file-6f50f9d1-5b95-416c-9040-0799b2b4b894

<span class="pl-c"><span class="pl-c">#</span> Delete remote file</span>
together files delete file-6f50f9d1-5b95-416c-9040-0799b2b4b894</pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Fine-tuning</h3><a id="user-content-fine-tuning" class="anchor" aria-label="Permalink: Fine-tuning" href="#fine-tuning"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together fine-tuning --help

# Create fine-tune job
together fine-tuning create \
  --model togethercomputer/llama-2-7b-chat \
  --training-file file-711d8724-b3e3-4ae2-b516-94841958117d

# List fine-tune jobs
together fine-tuning list

# Retrieve fine-tune job details
together fine-tuning retrieve ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

# List fine-tune job events
together fine-tuning list-events ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

# Cancel running job
together fine-tuning cancel ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

# Download fine-tuned model weights
together fine-tuning download ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together fine-tuning --help

<span class="pl-c"><span class="pl-c">#</span> Create fine-tune job</span>
together fine-tuning create \
  --model togethercomputer/llama-2-7b-chat \
  --training-file file-711d8724-b3e3-4ae2-b516-94841958117d

<span class="pl-c"><span class="pl-c">#</span> List fine-tune jobs</span>
together fine-tuning list

<span class="pl-c"><span class="pl-c">#</span> Retrieve fine-tune job details</span>
together fine-tuning retrieve ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

<span class="pl-c"><span class="pl-c">#</span> List fine-tune job events</span>
together fine-tuning list-events ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

<span class="pl-c"><span class="pl-c">#</span> Cancel running job</span>
together fine-tuning cancel ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

<span class="pl-c"><span class="pl-c">#</span> Download fine-tuned model weights</span>
together fine-tuning download ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b</pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Models</h3><a id="user-content-models" class="anchor" aria-label="Permalink: Models" href="#models"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together models --help

# List models
together models list"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together models --help

<span class="pl-c"><span class="pl-c">#</span> List models</span>
together models list</pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Versioning</h2><a id="user-content-versioning" class="anchor" aria-label="Permalink: Versioning" href="#versioning"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">This package generally follows <a href="https://semver.org/spec/v2.0.0.html" rel="nofollow">SemVer</a> conventions, though certain backwards-incompatible changes may be released as minor versions:</p>
<ol dir="auto">
<li>Changes that only affect static types, without breaking runtime behavior.</li>
<li>Changes to library internals which are technically public but not intended or documented for external use. <em>(Please open a GitHub issue to let us know if you are relying on such internals.)</em></li>
<li>Changes that we do not expect to impact the vast majority of users in practice.</li>
</ol>
<p dir="auto">We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.</p>
<p dir="auto">We are keen for your feedback; please open an <a href="https://www.github.com/togethercomputer/together-py/issues">issue</a> with questions, bugs, or suggestions.</p>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Determining the installed version</h3><a id="user-content-determining-the-installed-version" class="anchor" aria-label="Permalink: Determining the installed version" href="#determining-the-installed-version"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.</p>
<p dir="auto">You can determine the version that is being used at runtime with:</p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import together
print(together.__version__)"><pre><span class="pl-k">import</span> <span class="pl-s1">together</span>
<span class="pl-en">print</span>(<span class="pl-s1">together</span>.<span class="pl-c1">__version__</span>)</pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Requirements</h2><a id="user-content-requirements" class="anchor" aria-label="Permalink: Requirements" href="#requirements"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Python 3.9 or higher.</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Usage – CLI</h2><a id="user-content-usage--cli-1" class="anchor" aria-label="Permalink: Usage – CLI" href="#usage--cli-1"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Files</h3><a id="user-content-files-1" class="anchor" aria-label="Permalink: Files" href="#files-1"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together files --help

# Check file
together files check example.jsonl

# Upload file
together files upload example.jsonl

# List files
together files list

# Retrieve file metadata
together files retrieve file-6f50f9d1-5b95-416c-9040-0799b2b4b894

# Retrieve file content
together files retrieve-content file-6f50f9d1-5b95-416c-9040-0799b2b4b894

# Delete remote file
together files delete file-6f50f9d1-5b95-416c-9040-0799b2b4b894"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together files --help

<span class="pl-c"><span class="pl-c">#</span> Check file</span>
together files check example.jsonl

<span class="pl-c"><span class="pl-c">#</span> Upload file</span>
together files upload example.jsonl

<span class="pl-c"><span class="pl-c">#</span> List files</span>
together files list

<span class="pl-c"><span class="pl-c">#</span> Retrieve file metadata</span>
together files retrieve file-6f50f9d1-5b95-416c-9040-0799b2b4b894

<span class="pl-c"><span class="pl-c">#</span> Retrieve file content</span>
together files retrieve-content file-6f50f9d1-5b95-416c-9040-0799b2b4b894

<span class="pl-c"><span class="pl-c">#</span> Delete remote file</span>
together files delete file-6f50f9d1-5b95-416c-9040-0799b2b4b894</pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Fine-tuning</h3><a id="user-content-fine-tuning-1" class="anchor" aria-label="Permalink: Fine-tuning" href="#fine-tuning-1"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together fine-tuning --help

# Create fine-tune job
together fine-tuning create \
  --model togethercomputer/llama-2-7b-chat \
  --training-file file-711d8724-b3e3-4ae2-b516-94841958117d

# List fine-tune jobs
together fine-tuning list

# Retrieve fine-tune job details
together fine-tuning retrieve ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

# List fine-tune job events
together fine-tuning list-events ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

# List fine-tune checkpoints
together fine-tuning list-checkpoints ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

# Cancel running job
together fine-tuning cancel ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

# Download fine-tuned model weights
together fine-tuning download ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

# Delete fine-tuned model weights
together fine-tuning delete ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together fine-tuning --help

<span class="pl-c"><span class="pl-c">#</span> Create fine-tune job</span>
together fine-tuning create \
  --model togethercomputer/llama-2-7b-chat \
  --training-file file-711d8724-b3e3-4ae2-b516-94841958117d

<span class="pl-c"><span class="pl-c">#</span> List fine-tune jobs</span>
together fine-tuning list

<span class="pl-c"><span class="pl-c">#</span> Retrieve fine-tune job details</span>
together fine-tuning retrieve ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

<span class="pl-c"><span class="pl-c">#</span> List fine-tune job events</span>
together fine-tuning list-events ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

<span class="pl-c"><span class="pl-c">#</span> List fine-tune checkpoints</span>
together fine-tuning list-checkpoints ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

<span class="pl-c"><span class="pl-c">#</span> Cancel running job</span>
together fine-tuning cancel ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

<span class="pl-c"><span class="pl-c">#</span> Download fine-tuned model weights</span>
together fine-tuning download ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b

<span class="pl-c"><span class="pl-c">#</span> Delete fine-tuned model weights</span>
together fine-tuning delete ft-c66a5c18-1d6d-43c9-94bd-32d756425b4b</pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Models</h3><a id="user-content-models-1" class="anchor" aria-label="Permalink: Models" href="#models-1"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together models --help

# List models
together models list

# Upload a model
together models upload --model-name my-org/my-model --model-source s3-or-hugging-face"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together models --help

<span class="pl-c"><span class="pl-c">#</span> List models</span>
together models list

<span class="pl-c"><span class="pl-c">#</span> Upload a model</span>
together models upload --model-name my-org/my-model --model-source s3-or-hugging-face</pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Clusters</h3><a id="user-content-clusters" class="anchor" aria-label="Permalink: Clusters" href="#clusters"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together beta clusters --help

# Create a cluster
together beta clusters create

# List clusters
together beta clusters list

# Retrieve cluster details
together beta clusters retrieve [cluster-id]

# Update a cluster
together beta clusters update [cluster-id]

# Retrieve Together cluster configuration options such as regions, gpu types and drivers available
together beta clusters list-regions"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together beta clusters --help

<span class="pl-c"><span class="pl-c">#</span> Create a cluster</span>
together beta clusters create

<span class="pl-c"><span class="pl-c">#</span> List clusters</span>
together beta clusters list

<span class="pl-c"><span class="pl-c">#</span> Retrieve cluster details</span>
together beta clusters retrieve [cluster-id]

<span class="pl-c"><span class="pl-c">#</span> Update a cluster</span>
together beta clusters update [cluster-id]

<span class="pl-c"><span class="pl-c">#</span> Retrieve Together cluster configuration options such as regions, gpu types and drivers available</span>
together beta clusters list-regions</pre></div>
<div class="markdown-heading" dir="auto"><h5 tabindex="-1" class="heading-element" dir="auto">Cluster Storage</h5><a id="user-content-cluster-storage" class="anchor" aria-label="Permalink: Cluster Storage" href="#cluster-storage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together beta clusters storage --help

# Create cluster storage volume
together beta clusters storage create

# List storage volumes
together beta clusters storage list

# Retrieve storage volume
together beta clusters storage retrieve [storage-id]

# Delete storage volume
together beta clusters storage delete [storage-id]"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together beta clusters storage --help

<span class="pl-c"><span class="pl-c">#</span> Create cluster storage volume</span>
together beta clusters storage create

<span class="pl-c"><span class="pl-c">#</span> List storage volumes</span>
together beta clusters storage list

<span class="pl-c"><span class="pl-c">#</span> Retrieve storage volume</span>
together beta clusters storage retrieve [storage-id]

<span class="pl-c"><span class="pl-c">#</span> Delete storage volume</span>
together beta clusters storage delete [storage-id]</pre></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Jig (Container Deployments)</h3><a id="user-content-jig-container-deployments" class="anchor" aria-label="Permalink: Jig (Container Deployments)" href="#jig-container-deployments"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together beta jig --help

# Initialize jig configuration (creates pyproject.toml)
together beta jig init

# Generate Dockerfile from config
together beta jig dockerfile

# Build container image
together beta jig build
together beta jig build --tag v1.0 --warmup

# Push image to registry
together beta jig push
together beta jig push --tag v1.0

# Deploy model (builds, pushes, and deploys)
together beta jig deploy
together beta jig deploy --build-only
together beta jig deploy --image existing-image:tag

# Get deployment status
together beta jig status

# Get deployment endpoint URL
together beta jig endpoint

# View deployment logs
together beta jig logs
together beta jig logs --follow

# Destroy deployment
together beta jig destroy

# Get queue metrics
together beta jig queue-status

# List all deployments
together beta jig list"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together beta jig --help

<span class="pl-c"><span class="pl-c">#</span> Initialize jig configuration (creates pyproject.toml)</span>
together beta jig init

<span class="pl-c"><span class="pl-c">#</span> Generate Dockerfile from config</span>
together beta jig dockerfile

<span class="pl-c"><span class="pl-c">#</span> Build container image</span>
together beta jig build
together beta jig build --tag v1.0 --warmup

<span class="pl-c"><span class="pl-c">#</span> Push image to registry</span>
together beta jig push
together beta jig push --tag v1.0

<span class="pl-c"><span class="pl-c">#</span> Deploy model (builds, pushes, and deploys)</span>
together beta jig deploy
together beta jig deploy --build-only
together beta jig deploy --image existing-image:tag

<span class="pl-c"><span class="pl-c">#</span> Get deployment status</span>
together beta jig status

<span class="pl-c"><span class="pl-c">#</span> Get deployment endpoint URL</span>
together beta jig endpoint

<span class="pl-c"><span class="pl-c">#</span> View deployment logs</span>
together beta jig logs
together beta jig logs --follow

<span class="pl-c"><span class="pl-c">#</span> Destroy deployment</span>
together beta jig destroy

<span class="pl-c"><span class="pl-c">#</span> Get queue metrics</span>
together beta jig queue-status

<span class="pl-c"><span class="pl-c">#</span> List all deployments</span>
together beta jig list</pre></div>
<div class="markdown-heading" dir="auto"><h5 tabindex="-1" class="heading-element" dir="auto">Jig Secrets</h5><a id="user-content-jig-secrets" class="anchor" aria-label="Permalink: Jig Secrets" href="#jig-secrets"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together beta jig secrets --help

# Set a secret (creates or updates)
together beta jig secrets set --name MY_SECRET --value &quot;secret-value&quot;

# Remove a secret from local state
together beta jig secrets unset --name MY_SECRET

# List all secrets with sync status
together beta jig secrets list"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together beta jig secrets --help

<span class="pl-c"><span class="pl-c">#</span> Set a secret (creates or updates)</span>
together beta jig secrets <span class="pl-c1">set</span> --name MY_SECRET --value <span class="pl-s"><span class="pl-pds">"</span>secret-value<span class="pl-pds">"</span></span>

<span class="pl-c"><span class="pl-c">#</span> Remove a secret from local state</span>
together beta jig secrets <span class="pl-c1">unset</span> --name MY_SECRET

<span class="pl-c"><span class="pl-c">#</span> List all secrets with sync status</span>
together beta jig secrets list</pre></div>
<div class="markdown-heading" dir="auto"><h5 tabindex="-1" class="heading-element" dir="auto">Jig Volumes</h5><a id="user-content-jig-volumes" class="anchor" aria-label="Permalink: Jig Volumes" href="#jig-volumes"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="# Help
together beta jig volumes --help

# Create a volume and upload files from directory
together beta jig volumes create --name my-volume --source ./data

# Update a volume with new files
together beta jig volumes update --name my-volume --source ./data

# Set volume mount path for deployment
together beta jig volumes set --name my-volume --mount-path /app/data

# Remove volume from deployment config (does not delete remote volume)
together beta jig volumes unset --name my-volume

# Delete a volume
together beta jig volumes delete --name my-volume

# Describe a volume
together beta jig volumes describe --name my-volume

# List all volumes
together beta jig volumes list"><pre><span class="pl-c"><span class="pl-c">#</span> Help</span>
together beta jig volumes --help

<span class="pl-c"><span class="pl-c">#</span> Create a volume and upload files from directory</span>
together beta jig volumes create --name my-volume --source ./data

<span class="pl-c"><span class="pl-c">#</span> Update a volume with new files</span>
together beta jig volumes update --name my-volume --source ./data

<span class="pl-c"><span class="pl-c">#</span> Set volume mount path for deployment</span>
together beta jig volumes <span class="pl-c1">set</span> --name my-volume --mount-path /app/data

<span class="pl-c"><span class="pl-c">#</span> Remove volume from deployment config (does not delete remote volume)</span>
together beta jig volumes <span class="pl-c1">unset</span> --name my-volume

<span class="pl-c"><span class="pl-c">#</span> Delete a volume</span>
together beta jig volumes delete --name my-volume

<span class="pl-c"><span class="pl-c">#</span> Describe a volume</span>
together beta jig volumes describe --name my-volume

<span class="pl-c"><span class="pl-c">#</span> List all volumes</span>
together beta jig volumes list</pre></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Contributing</h2><a id="user-content-contributing" class="anchor" aria-label="Permalink: Contributing" href="#contributing"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">See <a href="/togethercomputer/together-py/blob/main/CONTRIBUTING.md">the contributing documentation</a>.</p>
</article></div></div></div></div></div></div></div><div class="prc-PageLayout-PaneWrapper-pHPop pr-2" style="--offset-header:0px;--spacing-row:var(--spacing-none);--spacing-column:var(--spacing-none)" data-is-hidden="false" data-position="end"><div class="prc-PageLayout-HorizontalDivider-JLVqp prc-PageLayout-PaneHorizontalDivider-9tbnE" data-variant-narrow="none" data-variant-regular="none" data-position="end" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div><div class="prc-PageLayout-Pane-AyzHK" style="--spacing:var(--spacing-normal);--pane-min-width:256px;--pane-max-width:calc(100vw - var(--pane-max-width-diff));--pane-width-size:var(--pane-width-large);--pane-width:320px"><rails-partial data-partial-name="codeViewRepoRoute.Sidebar" class="RailsPartial-module__d-contents__G5m4w">

<div class="BorderGrid ">
  <div class="BorderGrid-row">
    <div class="BorderGrid-cell">
      <div class="hide-sm hide-md">
  <h2 class="tmp-mb-3 h4">About</h2>

      <div class="f4 tmp-my-3 color-fg-muted text-italic">
        No description, website, or topics provided.
      </div>


    <h3 class="sr-only">Resources</h3>
    <div class="mt-2">
      <a class="Link--muted" data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:readme&quot;}" href="#readme-ov-file">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book mr-2">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        Readme
</a>    </div>

  
    <h3 class="sr-only">License</h3>
  <div class="mt-2">
    <a href="#Apache-2.0-1-ov-file"
      class="Link--muted"
      
      data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:license&quot;}"
    >
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-law mr-1 mr-sm-1 mr-md-2 mr-lg-2">
    <path d="M8.75.75V2h.985c.304 0 .603.08.867.231l1.29.736c.038.022.08.033.124.033h2.234a.75.75 0 0 1 0 1.5h-.427l2.111 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.006.005-.01.01-.045.04c-.21.176-.441.327-.686.45C14.556 10.78 13.88 11 13 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L12.178 4.5h-.162c-.305 0-.604-.079-.868-.231l-1.29-.736a.245.245 0 0 0-.124-.033H8.75V13h2.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1 0-1.5h2.5V3.5h-.984a.245.245 0 0 0-.124.033l-1.289.737c-.265.15-.564.23-.869.23h-.162l2.112 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.016.015-.045.04c-.21.176-.441.327-.686.45C4.556 10.78 3.88 11 3 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L2.178 4.5H1.75a.75.75 0 0 1 0-1.5h2.234a.249.249 0 0 0 .125-.033l1.288-.737c.265-.15.564-.23.869-.23h.984V.75a.75.75 0 0 1 1.5 0Zm2.945 8.477c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327Zm-10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327Z"></path>
</svg>
     Apache-2.0 license
    </a>
  </div>




    <h3 class="sr-only">Contributing</h3>
    <div class="mt-2">
      <a href="#contributing-ov-file"
        class="Link--muted"
        
        data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:contributing&quot;}"
      >
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people mr-2">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
        Contributing
      </a>
    </div>

    <h3 class="sr-only">Security policy</h3>
    <div class="mt-2">
      <a href="#security-ov-file"
        class="Link--muted"
        
        data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:security policy&quot;}"
      >
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-law mr-2">
    <path d="M8.75.75V2h.985c.304 0 .603.08.867.231l1.29.736c.038.022.08.033.124.033h2.234a.75.75 0 0 1 0 1.5h-.427l2.111 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.006.005-.01.01-.045.04c-.21.176-.441.327-.686.45C14.556 10.78 13.88 11 13 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L12.178 4.5h-.162c-.305 0-.604-.079-.868-.231l-1.29-.736a.245.245 0 0 0-.124-.033H8.75V13h2.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1 0-1.5h2.5V3.5h-.984a.245.245 0 0 0-.124.033l-1.289.737c-.265.15-.564.23-.869.23h-.162l2.112 4.692a.75.75 0 0 1-.154.838l-.53-.53.529.531-.001.002-.002.002-.006.006-.016.015-.045.04c-.21.176-.441.327-.686.45C4.556 10.78 3.88 11 3 11a4.498 4.498 0 0 1-2.023-.454 3.544 3.544 0 0 1-.686-.45l-.045-.04-.016-.015-.006-.006-.004-.004v-.001a.75.75 0 0 1-.154-.838L2.178 4.5H1.75a.75.75 0 0 1 0-1.5h2.234a.249.249 0 0 0 .125-.033l1.288-.737c.265-.15.564-.23.869-.23h.984V.75a.75.75 0 0 1 1.5 0Zm2.945 8.477c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327Zm-10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327Z"></path>
</svg>
        Security policy
      </a>
    </div>

  <include-fragment src="/togethercomputer/together-py/hovercards/citation/sidebar_partial?tree_name=main" data-nonce="v2:cb0ba074-d866-cbc2-1501-de97be737629" data-view-component="true">
  

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
      <a href="/togethercomputer/together-py/activity" data-view-component="true" class="Link Link--muted"><svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pulse mr-2">
    <path d="M6 2c.306 0 .582.187.696.471L10 10.731l1.304-3.26A.751.751 0 0 1 12 7h3.25a.75.75 0 0 1 0 1.5h-2.742l-1.812 4.528a.751.751 0 0 1-1.392 0L6 4.77 4.696 8.03A.75.75 0 0 1 4 8.5H.75a.75.75 0 0 1 0-1.5h2.742l1.812-4.529A.751.751 0 0 1 6 2Z"></path>
</svg>
        <span class="color-fg-muted">Activity</span></a>    </div>

    <div class="mt-2">
      <a href="/togethercomputer/together-py/custom-properties" data-view-component="true" class="Link Link--muted"><svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-note mr-2">
    <path d="M0 3.75C0 2.784.784 2 1.75 2h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14H1.75A1.75 1.75 0 0 1 0 12.25Zm1.75-.25a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25ZM3.5 6.25a.75.75 0 0 1 .75-.75h7a.75.75 0 0 1 0 1.5h-7a.75.75 0 0 1-.75-.75Zm.75 2.25h4a.75.75 0 0 1 0 1.5h-4a.75.75 0 0 1 0-1.5Z"></path>
</svg>
        <span class="color-fg-muted">Custom properties</span></a>    </div>

    <h3 class="sr-only">Stars</h3>
    <div class="mt-2">
      <a href="/togethercomputer/together-py/stargazers" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        <strong>7</strong>
        stars</a>    </div>

    <h3 class="sr-only">Watchers</h3>
    <div class="mt-2">
      <a href="/togethercomputer/together-py/watchers" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye mr-2">
    <path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path>
</svg>
        <strong>3</strong>
        watching</a>    </div>

    <h3 class="sr-only">Forks</h3>
    <div class="mt-2">
      <a href="/togethercomputer/together-py/forks" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
        <strong>0</strong>
        forks</a>    </div>


    <div class="mt-2">
      <a class="Link--muted" href="/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Ftogethercomputer%2Ftogether-py&amp;report=togethercomputer+%28user%29">
          Report repository
</a>    </div>
</div>

    </div>
  </div>

  
      <div class="BorderGrid-row">
        <div class="BorderGrid-cell">
          <h2 class="h4 tmp-mb-3" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
  <a href="/togethercomputer/together-py/releases" data-view-component="true" class="Link--primary no-underline Link">Releases
      <span title="55" data-view-component="true" class="Counter">55</span></a></h2>

  <a class="Link--primary d-flex no-underline" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/togethercomputer/together-py/releases/tag/v2.3.2">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tag flex-shrink-0 mt-1 color-fg-success">
    <path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path>
</svg>
    <div class="ml-2 min-width-0">
      <div class="d-flex">
        <span class="css-truncate css-truncate-target text-bold mr-2" style="max-width: none;">v2.3.2</span>
        <span title="Label: Latest" data-view-component="true" class="Label Label--success flex-shrink-0">
          Latest
</span>      </div>
      <div class="text-small color-fg-muted"><relative-time datetime="2026-03-09T19:00:06Z" class="no-wrap">Mar 9, 2026</relative-time></div>
    </div>
</a>    <div data-view-component="true" class="tmp-mt-3">
      <a text="small" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/togethercomputer/together-py/releases" data-view-component="true" class="Link">+ 54 releases</a></div>
        </div>
      </div>

  
  
  
      <div class="BorderGrid-row">
        <div class="BorderGrid-cell">
          
<include-fragment aria-busy="true" aria-label="Loading latest packages" src="/togethercomputer/together-py/packages_list?current_repository=together-py" data-nonce="v2:cb0ba074-d866-cbc2-1501-de97be737629" data-view-component="true">
  
  <h2 class="h4 tmp-mb-3">
  <a href="/orgs/togethercomputer/packages?repo_name=together-py" data-view-component="true" class="Link--primary no-underline Link d-flex flex-items-center">Packages
      <span title="0" hidden="hidden" data-view-component="true" class="Counter ml-1">0</span></a></h2>


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

  
  
    <div class="BorderGrid-row">
      <div class="BorderGrid-cell">
        <include-fragment aria-busy="true" aria-label="Loading contributors" src="/togethercomputer/together-py/contributors_list?current_repository=together-py&amp;deferred=true" data-nonce="v2:cb0ba074-d866-cbc2-1501-de97be737629" data-view-component="true">
  
  <h2 class="h4 tmp-mb-3">
    <a href="/togethercomputer/together-py/graphs/contributors" data-view-component="true" class="Link--primary no-underline Link d-flex flex-items-center">Contributors</a>  </h2>

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
    <span style="background-color:#3572A5 !important;;width: 99.7%;" itemprop="keywords" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
    <span style="background-color:#ededed !important;;width: 0.3%;" itemprop="keywords" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
</span></div>
<ul class="list-style-none">
    <li class="d-inline">
        <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small tmp-mr-3" href="/togethercomputer/together-py/search?l=python"  data-ga-click="Repository, language stats search click, location:repo overview">
          <svg style="color:#3572A5;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
          <span class="color-fg-default text-bold mr-1">Python</span>
          <span>99.7%</span>
        </a>
    </li>
    <li class="d-inline">
      <span class="d-inline-flex flex-items-center flex-nowrap text-small tmp-mr-3">
        <svg style="color:#ededed;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
        <span class="color-fg-default text-bold mr-1">Other</span>
        <span>0.3%</span>
      </span>
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
    <path d="M10.303 16.652c-2.837-.344-4.835-2.385-4.835-5.028 0-1.074.387-2.235 1.031-3.008-.279-.709-.236-2.214.086-2.837.86-.107 2.02.344 2.708.967.816-.258 1.676-.386 2.728-.386 1.053 0 1.913.128 2.686.365.666-.602 1.848-1.053 2.708-.946.3.581.344 2.085.064 2.815.688.817 1.053 1.913 1.053 3.03 0 2.643-1.998 4.641-4.877 5.006.73.473 1.224 1.504 1.224 2.686v2.235c0 .644.537 1.01 1.182.752 3.889-1.483 6.94-5.372 6.94-10.185 0-6.081-4.942-11.044-11.022-11.044-6.081 0-10.98 4.963-10.98 11.044a10.84 10.84 0 0 0 7.112 10.206c.58.215 1.139-.172 1.139-.752v-1.719a2.768 2.768 0 0 1-1.032.215c-1.418 0-2.256-.773-2.857-2.213-.237-.58-.495-.924-.989-.988-.258-.022-.344-.129-.344-.258 0-.258.43-.451.86-.451.623 0 1.16.386 1.719 1.181.43.623.881.903 1.418.903.537 0 .881-.194 1.375-.688.365-.365.645-.687.903-.902Z"></path>
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
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
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


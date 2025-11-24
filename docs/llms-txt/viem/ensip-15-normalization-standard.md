# Source: https://github.com/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md







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

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light-8e973f836952.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light_high_contrast-34b642d57214.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark-4bce7af39e21.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark_high_contrast-ad512d3e2f3b.css" /><link data-color-theme="light" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light-8e973f836952.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-34b642d57214.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-54be93e666a7.css" /><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-8ae7edf5489c.css" /><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-84d50df427c0.css" /><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-a80873375146.css" /><link data-color-theme="dark" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark-4bce7af39e21.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-ad512d3e2f3b.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-d152d6cd6879.css" /><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-fa4060c1a9da.css" /><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-d7bad0fb00bb.css" /><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-4a0107c0f60c.css" /><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-045e6b6ac094.css" /><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-5de537db5e79.css" />

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-primitives-15839d47b75d.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-a5c85403da8c.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-7c26792eb3de.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/github-490b3f68bf33.css" />
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/repository-5d735668c600.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-9c9b8dc61e74.css" />

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["a11y_status_checks_ruleset","actions_custom_images_public_preview_visibility","actions_custom_images_storage_billing_ui_visibility","actions_enable_snapshot_keyword","actions_image_version_event","alternate_user_config_repo","api_insights_show_missing_data_banner","attestations_filtering","attestations_sorting","client_version_header","codespaces_prebuild_region_target_update","contentful_lp_footnotes","copilot_agent_cli_public_preview","copilot_agent_task_list_v2","copilot_agent_tasks_btn_code_nav","copilot_agent_tasks_btn_code_view","copilot_agent_tasks_btn_code_view_lines","copilot_agent_tasks_btn_repo","copilot_api_agentic_issue_marshal_yaml","copilot_api_draft_issues_with_dependencies","copilot_api_github_draft_update_issue_skill","copilot_chat_agents_empty_state","copilot_chat_attach_multiple_images","copilot_chat_file_redirect","copilot_chat_input_commands","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_coding_agent_task_response","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_hide_in_dotcom_chat","copilot_extensions_removal_on_marketplace","copilot_features_raycast_logo","copilot_file_block_ref_matching","copilot_free_to_paid_telem","copilot_ftp_hyperspace_upgrade_prompt","copilot_ftp_settings_upgrade","copilot_ftp_upgrade_to_pro_from_models","copilot_ftp_your_copilot_settings","copilot_immersive_issues_readonly_viewer","copilot_immersive_issues_show_relationships","copilot_immersive_structured_model_picker","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_insights_column_chart_axis_legibility_fix","copilot_insights_public_preview","copilot_insights_usage_export_ndjson","copilot_no_floating_button","copilot_org_policy_page_focus_mode","copilot_security_alert_assignee_options","copilot_share_active_subthread","copilot_spaces_as_attachments","copilot_spaces_ga","copilot_spark_empty_state","copilot_spark_loading_webgl","copilot_spark_progressive_error_handling","copilot_spark_use_billing_headers","copilot_stable_conversation_view","copilot_swe_agent_progress_commands","copilot_swe_agent_use_subagents","copilot_workbench_agent_seed_tool","copilot_workbench_agent_user_edit_awareness","copilot_workbench_cache","copilot_workbench_preview_analytics","copilot_workbench_use_single_prompt","deployment_record_api","direct_to_salesforce","disable_dashboard_universe_2025_private_preview","dotcom_chat_client_side_skills","enterprise_ai_controls","failbot_report_error_react_apps_on_page","fetch_graphql_improved_error_serialization","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","global_search_multi_orgs","hyperspace_2025_logged_out_batch_1","hyperspace_nudges_universe25","hyperspace_nudges_universe25_post_event","initial_per_page_pagination_updates","inp_reduced_threshold","issue_fields_report_usage","issues_expanded_file_types","issues_lazy_load_comment_box_suggestions","issues_react_blur_item_picker_on_close","issues_react_bots_timeline_pagination","issues_react_prohibit_title_fallback","issues_react_remove_placeholders","issues_report_sidebar_interactions","issues_sticky_sidebar","item_picker_label_tsq_migration","item_picker_project_tsq_migration","item_picker_search_cancellation","kb_convert_to_space","lifecycle_label_name_updates","link_contact_sales_swp_marketo","marketing_pages_search_explore_provider","mcp_registry_install","mcp_registry_oss_v0_1_api","memex_default_issue_create_repository","memex_grouped_by_edit_route","memex_mwl_filter_field_delimiter","mission_control_use_body_html","new_traffic_page_banner","open_agent_session_in_vscode_insiders","open_agent_session_in_vscode_stable","pinned_issue_fields","primer_react_segmented_control_tooltip","projects_assignee_max_limit","react_fetch_graphql_ignore_expected_errors","record_sso_banner_metrics","repos_insights_remove_new_url","ruleset_deletion_confirmation","sample_network_conn_type","scheduled_reminders_updated_limits","site_features_copilot_universe","site_homepage_collaborate_video","site_homepage_contentful","site_homepage_eyebrow_banner","site_homepage_universe_animations","site_msbuild_webgl_hero","spark_fix_rename","spark_force_push_after_checkout","spark_improve_image_upload","spark_kv_encocoded_keys","spark_show_data_access_on_publish","spark_sync_repository_after_iteration","viewscreen_sandbox","webp_support","workbench_store_readonly"],"copilotApiOverrideUrl":"https://api.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/high-contrast-cookie-1a011967750c.js"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/wp-runtime-844053881031.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/913-ca2305638c53.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/6488-de87864e6818.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/environment-3bc3b3b3a6f6.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/11683-aa3d1ebe6648.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/43784-4652ae97a661.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/4712-809eac2badf7.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81028-5b8c5e07a4fa.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/74911-6a311b93ee8e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/91853-b5d2e5602241.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/78143-31968346cf4c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/52430-c46e2de36eb2.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/github-elements-5b3e77949adb.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/element-registry-6c3843facdbe.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/28546-ee41c9313871.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/17688-a9e16fb5ed13.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2869-a4ba8f17edb3.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/70191-5122bf27bf3e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/7332-e3769b714648.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/3200-a7d4487d8022.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/95964-56279d5d08b3.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/89708-cf8a683757b8.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/51519-dc0d4e14166a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/7534-44b89d9287f7.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/96384-750ef5263abe.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/19718-676a65610616.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-0e1db20ae607.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/48011-5b6f71a93de7.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/notifications-global-eb21f5b0029d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/53996-5a7cf1bdd2cd.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/code-menu-26fed944c925.js" defer="defer"></script>
  
  <script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/primer-react-1d943c070f89.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-lib-760965ba27bb.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-core-6bff7e7eaf4e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/octicons-react-a215e6ee021a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/58267-d3b3e418eb9c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/48775-3cc79d2cd30e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/42892-9fe102b0683f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/23832-db66abd83e08.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/99418-9d4961969e0d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/33915-05ba9b3edc31.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/35563-88b5576b2c6b.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/51220-ec5733320b36.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/32219-7472a62a38a8.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/83597-a037b23eee45.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/25407-6e094ff52623.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81929-06b7f240be06.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/40771-562cd0f045bd.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/66990-26254330a98f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/29665-aafd67585c49.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/19976-d9a685a90a0d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81725-de9dc2dbc3e4.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/3774-44ca4749f19f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/18406-6bc4085c106d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/36584-798b01636f52.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/29806-f2a98cce3c40.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-code-view-18f6d867fc0a.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/react-code-view.b17093118927c84cf318.module.css" />

  <script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/39560-ce417bb8213c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/notifications-subscriptions-menu-ffc5e2a27839.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/notifications-subscriptions-menu.933100a30c03fd4e8ae4.module.css" />


  <title>docs/ens-improvement-proposals/ensip-15-normalization-standard.md at 9edf9443de4333a0ea7ec658a870672d5d180d53 · ensdomains/docs · GitHub</title>



  <meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient>
  <meta name="route-controller" content="blob" data-turbo-transient>
  <meta name="route-action" content="show" data-turbo-transient>
  <meta name="fetch-nonce" content="v2:bfe21f2e-7e7c-5bc7-b014-2c6d41e095d4">

    
  <meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb">


  <meta name="request-id" content="D89A:150CC7:417C830:427B45D:691D07B2" data-pjax-transient="true"/><meta name="html-safe-nonce" content="fcf19507f0b705617147fb267d6c2e1f215f64210495d57a5ad94a6698441d33" data-pjax-transient="true"/><meta name="visitor-payload" content="eyJyZWZlcnJlciI6IiIsInJlcXVlc3RfaWQiOiJEODlBOjE1MENDNzo0MTdDODMwOjQyN0I0NUQ6NjkxRDA3QjIiLCJ2aXNpdG9yX2lkIjoiNTQ1MDMxOTE2NTQ0OTM3MzYxOCIsInJlZ2lvbl9lZGdlIjoic2VhIiwicmVnaW9uX3JlbmRlciI6InNlYSJ9" data-pjax-transient="true"/><meta name="visitor-hmac" content="ab8d87bd5c3c998af6ccd51a0d22f2826b4e9211c25706e471ecfdf552d2e219" data-pjax-transient="true"/>


    <meta name="hovercard-subject-tag" content="repository:172392769" data-turbo-transient>


  <meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-turbo-transient>
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true" />

  




    <meta name="user-login" content="">

  

    <meta name="viewport" content="width=device-width">

    

      <meta name="description" content="Documentation for the ENS protocol. Contribute to ensdomains/docs development by creating an account on GitHub.">

      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">

    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md" />

      <meta name="twitter:image" content="https://opengraph.githubassets.com/894879a625374e8d3bc41572af95a7df5ea77b4e01599d027a1cf45f674d7fc9/ensdomains/docs" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="docs/ens-improvement-proposals/ensip-15-normalization-standard.md at 9edf9443de4333a0ea7ec658a870672d5d180d53 · ensdomains/docs" /><meta name="twitter:description" content="Documentation for the ENS protocol. Contribute to ensdomains/docs development by creating an account on GitHub." />
  <meta property="og:image" content="https://opengraph.githubassets.com/894879a625374e8d3bc41572af95a7df5ea77b4e01599d027a1cf45f674d7fc9/ensdomains/docs" /><meta property="og:image:alt" content="Documentation for the ENS protocol. Contribute to ensdomains/docs development by creating an account on GitHub." /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="docs/ens-improvement-proposals/ensip-15-normalization-standard.md at 9edf9443de4333a0ea7ec658a870672d5d180d53 · ensdomains/docs" /><meta property="og:url" content="https://github.com/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md" /><meta property="og:description" content="Documentation for the ENS protocol. Contribute to ensdomains/docs development by creating an account on GitHub." />
  




      <meta name="hostname" content="github.com">



        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="84bda50d354166d1a28f9ebd0c28a9c2336f7b9ea7c89baf828e1d3f7e39ccf5" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="21a43568025709b66240454fc92d4f09335a96863f8ab1c46b4a07f6a5b67102" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="c82d7e8d645fe45d31c46ec82d16354828e0d43bb590b9784433628b6c38a45e" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="6ae24f79aecfaea6c694938904ebd44dc1021f358263b8792915fbb59e5e8c33" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient>

    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/ensdomains/docs git https://github.com/ensdomains/docs.git">

  <meta name="octolytics-dimension-user_id" content="34167658" /><meta name="octolytics-dimension-user_login" content="ensdomains" /><meta name="octolytics-dimension-repository_id" content="172392769" /><meta name="octolytics-dimension-repository_nwo" content="ensdomains/docs" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="172392769" /><meta name="octolytics-dimension-repository_network_root_nwo" content="ensdomains/docs" />



    

    <meta name="turbo-body-classes" content="logged-out env-production page-responsive">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="release" content="5e870228e9228246243705fa8c04b8138d343573">
  <meta name="ui-target" content="full">

  <link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg" data-base-href="https://github.githubassets.com/favicons/favicon">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark" />


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-responsive" style="word-wrap: break-word;" >
    <div data-turbo-body class="logged-out env-production page-responsive" style="word-wrap: break-word;">
      



    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="#start-of-content" data-skip-target-assigned="false" class="px-2 py-4 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/keyboard-shortcuts-dialog.29aaeaafa90f007c6f61.module.css" />

<react-partial
  partial-name="keyboard-shortcuts-dialog"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>





      

          

              
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/21481-a66c6eab7bbf.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/85110-f7be2f54525a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/sessions-8cc3729f6e8d.js" defer="defer"></script>

<header class="HeaderMktg header-logged-out js-details-container js-header Details f4 py-3" role="banner" data-is-top="true" data-color-mode=light data-light-theme=light data-dark-theme=dark>
  <h2 class="sr-only">Navigation Menu</h2>

  <button type="button" class="HeaderMktg-backdrop d-lg-none border-0 position-fixed top-0 left-0 width-full height-full js-details-target" aria-label="Toggle navigation">
    <span class="d-none">Toggle navigation</span>
  </button>

  <div class="d-flex flex-column flex-lg-row flex-items-center px-3 px-md-4 px-lg-5 height-full position-relative z-1">
    <div class="d-flex flex-justify-between flex-items-center width-full width-lg-auto">
      <div class="flex-1">
        <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="js-details-target js-nav-padding-recalculate js-header-menu-toggle Button--link Button--medium Button d-lg-none color-fg-inherit p-1">  <span class="Button-content">
    <span class="Button-label"><div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div></span>
  </span>
</button>
      </div>

      <a class="mr-lg-3 color-fg-inherit flex-order-2 js-prevent-focus-on-mobile-nav"
        href="/"
        aria-label="Homepage"
        data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Logomark;ref_loc:Header&quot;}">
        <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
      </a>

      <div class="d-flex flex-1 flex-order-2 text-right d-lg-none gap-2 flex-justify-end">
          <a
            href="/login?return_to=https%3A%2F%2Fgithub.com%2Fensdomains%2Fdocs%2Fblob%2F9edf9443de4333a0ea7ec658a870672d5d180d53%2Fens-improvement-proposals%2Fensip-15-normalization-standard.md"
            class="HeaderMenu-link HeaderMenu-button d-inline-flex f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit js-prevent-focus-on-mobile-nav"
            data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="d4c9043501ad1fadbfe42410e0b5a42e14ecc335318c17e4c48d4fa5faebf040"
            data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to Sign in&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}"
          >
            Sign in
          </a>
              <div class="AppHeader-appearanceSettings">
    <react-partial-anchor>
      <button data-target="react-partial-anchor.anchor" id="icon-button-25bd9425-20c8-4264-ae13-288f66f60af5" aria-labelledby="tooltip-c7f8ff0e-70ca-4040-97ab-6259d8dcaa28" type="button" disabled="disabled" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium AppHeader-button HeaderMenu-link border cursor-wait">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sliders Button-visual">
    <path d="M15 2.75a.75.75 0 0 1-.75.75h-4a.75.75 0 0 1 0-1.5h4a.75.75 0 0 1 .75.75Zm-8.5.75v1.25a.75.75 0 0 0 1.5 0v-4a.75.75 0 0 0-1.5 0V2H1.75a.75.75 0 0 0 0 1.5H6.5Zm1.25 5.25a.75.75 0 0 0 0-1.5h-6a.75.75 0 0 0 0 1.5h6ZM15 8a.75.75 0 0 1-.75.75H11.5V10a.75.75 0 1 1-1.5 0V6a.75.75 0 0 1 1.5 0v1.25h2.75A.75.75 0 0 1 15 8Zm-9 5.25v-2a.75.75 0 0 0-1.5 0v1.25H1.75a.75.75 0 0 0 0 1.5H4.5v1.25a.75.75 0 0 0 1.5 0v-2Zm9 0a.75.75 0 0 1-.75.75h-6a.75.75 0 0 1 0-1.5h6a.75.75 0 0 1 .75.75Z"></path>
</svg>
</button><tool-tip id="tooltip-c7f8ff0e-70ca-4040-97ab-6259d8dcaa28" for="icon-button-25bd9425-20c8-4264-ae13-288f66f60af5" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Appearance settings</tool-tip>

      <template data-target="react-partial-anchor.template">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/appearance-settings.753d458774a2f782559b.module.css" />

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
            <nav class="HeaderMenu-nav" aria-label="Global">
              <ul class="d-lg-flex list-style-none">
                  <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Platform
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>

      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 dropdown-menu-wide">
        <div class="d-lg-flex dropdown-menu-wide">
            <div class="HeaderMenu-column px-lg-4">
                <div class="">

                  <ul class="list-style-none f5" >
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description mb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_copilot&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_copilot_link_platform_navbar&quot;}" href="https://github.com/features/copilot">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-copilot color-fg-subtle mr-3">
    <path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          GitHub Copilot

        </div>

        Write better code with AI
      </div>

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description mb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_spark&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_spark_link_platform_navbar&quot;}" href="https://github.com/features/spark">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-sparkle-fill color-fg-subtle mr-3">
    <path d="M11.296 1.924c.24-.656 1.168-.656 1.408 0l.717 1.958a11.25 11.25 0 0 0 6.697 6.697l1.958.717c.657.24.657 1.168 0 1.408l-1.958.717a11.25 11.25 0 0 0-6.697 6.697l-.717 1.958c-.24.657-1.168.657-1.408 0l-.717-1.958a11.25 11.25 0 0 0-6.697-6.697l-1.958-.717c-.656-.24-.656-1.168 0-1.408l1.958-.717a11.25 11.25 0 0 0 6.697-6.697l.717-1.958Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          GitHub Spark

            <span class="HeaderMenu-label">
              New
            </span>
        </div>

        Build and deploy intelligent apps
      </div>

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description mb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_models&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_models_link_platform_navbar&quot;}" href="https://github.com/features/models">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-ai-model color-fg-subtle mr-3">
    <path d="M19.375 8.5a3.25 3.25 0 1 1-3.163 4h-3a3.252 3.252 0 0 1-4.443 2.509L7.214 17.76a3.25 3.25 0 1 1-1.342-.674l1.672-2.957A3.238 3.238 0 0 1 6.75 12c0-.907.371-1.727.97-2.316L6.117 6.846A3.253 3.253 0 0 1 1.875 3.75a3.25 3.25 0 1 1 5.526 2.32l1.603 2.836A3.25 3.25 0 0 1 13.093 11h3.119a3.252 3.252 0 0 1 3.163-2.5ZM10 10.25a1.75 1.75 0 1 0-.001 3.499A1.75 1.75 0 0 0 10 10.25ZM5.125 2a1.75 1.75 0 1 0 0 3.5 1.75 1.75 0 0 0 0-3.5Zm12.5 9.75a1.75 1.75 0 1 0 3.5 0 1.75 1.75 0 0 0-3.5 0Zm-14.25 8.5a1.75 1.75 0 1 0 3.501-.001 1.75 1.75 0 0 0-3.501.001Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          GitHub Models

            <span class="HeaderMenu-label">
              New
            </span>
        </div>

        Manage and compare prompts
      </div>

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description mb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_advanced_security&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_advanced_security_link_platform_navbar&quot;}" href="https://github.com/security/advanced-security">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-shield-check color-fg-subtle mr-3">
    <path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          GitHub Advanced Security

        </div>

        Find and fix vulnerabilities
      </div>

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;actions&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;actions_link_platform_navbar&quot;}" href="https://github.com/features/actions">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-workflow color-fg-subtle mr-3">
    <path d="M1 3a2 2 0 0 1 2-2h6.5a2 2 0 0 1 2 2v6.5a2 2 0 0 1-2 2H7v4.063C7 16.355 7.644 17 8.438 17H12.5v-2.5a2 2 0 0 1 2-2H21a2 2 0 0 1 2 2V21a2 2 0 0 1-2 2h-6.5a2 2 0 0 1-2-2v-2.5H8.437A2.939 2.939 0 0 1 5.5 15.562V11.5H3a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v6.5a.5.5 0 0 0 .5.5h6.5a.5.5 0 0 0 .5-.5V3a.5.5 0 0 0-.5-.5ZM14.5 14a.5.5 0 0 0-.5.5V21a.5.5 0 0 0 .5.5H21a.5.5 0 0 0 .5-.5v-6.5a.5.5 0 0 0-.5-.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          Actions

        </div>

        Automate any workflow
      </div>

    
</a></li>

                  </ul>
                </div>
            </div>
            <div class="HeaderMenu-column px-lg-4 pb-3 pb-lg-0 border-lg-right">
                <div class="border-bottom border-lg-bottom-0 pb-lg-0 pb-3">

                  <ul class="list-style-none f5" >
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description mb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;codespaces&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;codespaces_link_platform_navbar&quot;}" href="https://github.com/features/codespaces">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-codespaces color-fg-subtle mr-3">
    <path d="M3.5 3.75C3.5 2.784 4.284 2 5.25 2h13.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 18.75 13H5.25a1.75 1.75 0 0 1-1.75-1.75Zm-2 12c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v4a1.75 1.75 0 0 1-1.75 1.75H3.25a1.75 1.75 0 0 1-1.75-1.75ZM5.25 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h13.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Zm-2 12a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h17.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25Z"></path><path d="M10 17.75a.75.75 0 0 1 .75-.75h6.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          Codespaces

        </div>

        Instant dev environments
      </div>

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description mb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;issues&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;issues_link_platform_navbar&quot;}" href="https://github.com/features/issues">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-issue-opened color-fg-subtle mr-3">
    <path d="M12 1c6.075 0 11 4.925 11 11s-4.925 11-11 11S1 18.075 1 12 5.925 1 12 1ZM2.5 12a9.5 9.5 0 0 0 9.5 9.5 9.5 9.5 0 0 0 9.5-9.5A9.5 9.5 0 0 0 12 2.5 9.5 9.5 0 0 0 2.5 12Zm9.5 2a2 2 0 1 1-.001-3.999A2 2 0 0 1 12 14Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          Issues

        </div>

        Plan and track work
      </div>

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description mb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;code_review&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;code_review_link_platform_navbar&quot;}" href="https://github.com/features/code-review">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-code-review color-fg-subtle mr-3">
    <path d="M10.3 6.74a.75.75 0 0 1-.04 1.06l-2.908 2.7 2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M1.5 4.25c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v12.5a1.75 1.75 0 0 1-1.75 1.75h-9.69l-3.573 3.573A1.458 1.458 0 0 1 5 21.043V18.5H3.25a1.75 1.75 0 0 1-1.75-1.75ZM3.25 4a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h2.5a.75.75 0 0 1 .75.75v3.19l3.72-3.72a.749.749 0 0 1 .53-.22h10a.25.25 0 0 0 .25-.25V4.25a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          Code Review

        </div>

        Manage code changes
      </div>

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description mb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;discussions&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;discussions_link_platform_navbar&quot;}" href="https://github.com/features/discussions">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-comment-discussion color-fg-subtle mr-3">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          Discussions

        </div>

        Collaborate outside of code
      </div>

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;code_search&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;code_search_link_platform_navbar&quot;}" href="https://github.com/features/code-search">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-code-square color-fg-subtle mr-3">
    <path d="M10.3 8.24a.75.75 0 0 1-.04 1.06L7.352 12l2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M2 3.75C2 2.784 2.784 2 3.75 2h16.5c.966 0 1.75.784 1.75 1.75v16.5A1.75 1.75 0 0 1 20.25 22H3.75A1.75 1.75 0 0 1 2 20.25Zm1.75-.25a.25.25 0 0 0-.25.25v16.5c0 .138.112.25.25.25h16.5a.25.25 0 0 0 .25-.25V3.75a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          Code Search

        </div>

        Find more, search less
      </div>

    
</a></li>

                  </ul>
                </div>
            </div>
            <div class="HeaderMenu-column px-lg-4">
                <div class="border-bottom border-lg-bottom-0 pb-lg-0 mb-3 pb-3">

                      <span class="d-block h4 color-fg-default my-1" id="platform-explore-heading">Explore</span>

                  <ul class="list-style-none f5" aria-labelledby="platform-explore-heading">
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;why_github&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;why_github_link_platform_navbar&quot;}" href="https://github.com/why-github">
      Why GitHub

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;documentation&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;documentation_link_platform_navbar&quot;}" href="https://docs.github.com">
      Documentation

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_skills&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_skills_link_platform_navbar&quot;}" href="https://skills.github.com">
      GitHub Skills

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;blog&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;blog_link_platform_navbar&quot;}" href="https://github.blog">
      Blog

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                  </ul>
                </div>
                <div class="border-bottom border-lg-bottom-0 pb-lg-0 pb-3">

                      <span class="d-block h4 color-fg-default my-1" id="platform-integrations-heading">Integrations</span>

                  <ul class="list-style-none f5" aria-labelledby="platform-integrations-heading">
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_marketplace&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_marketplace_link_platform_navbar&quot;}" href="https://github.com/marketplace">
      GitHub Marketplace

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;mcp_registry&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;mcp_registry_link_platform_navbar&quot;}" href="https://github.com/mcp">
      MCP Registry

    
</a></li>

                  </ul>
                </div>
            </div>
        </div>

          <div class="HeaderMenu-trailing-link rounded-bottom-2 mt-lg-4 px-lg-4 py-4 py-lg-3 f5 text-semibold">
            <a data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all_features&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_features_link_platform_navbar&quot;}" href="https://github.com/features">
              View all features
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right HeaderMenu-trailing-link-icon">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</a>          </div>
      </div>
</li>


                  <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Solutions
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>

      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 dropdown-menu-wide">
        <div class="d-lg-flex dropdown-menu-wide">
            <div class="HeaderMenu-column px-lg-4 pb-3 pb-lg-0 border-lg-right">
                <div class="border-bottom border-lg-bottom-0 pb-lg-0 pb-3">

                      <span class="d-block h4 color-fg-default my-1" id="solutions-by-company-size-heading">By company size</span>

                  <ul class="list-style-none f5" aria-labelledby="solutions-by-company-size-heading">
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;enterprises&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;enterprises_link_solutions_navbar&quot;}" href="https://github.com/enterprise">
      Enterprises

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;small_and_medium_teams&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;small_and_medium_teams_link_solutions_navbar&quot;}" href="https://github.com/team">
      Small and medium teams

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;startups&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;startups_link_solutions_navbar&quot;}" href="https://github.com/enterprise/startups">
      Startups

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;nonprofits&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;nonprofits_link_solutions_navbar&quot;}" href="/solutions/industry/nonprofits">
      Nonprofits

    
</a></li>

                  </ul>
                </div>
            </div>
            <div class="HeaderMenu-column px-lg-4 pb-3 pb-lg-0 border-lg-right">
                <div class="border-bottom border-lg-bottom-0 pb-lg-0 pb-3">

                      <span class="d-block h4 color-fg-default my-1" id="solutions-by-use-case-heading">By use case</span>

                  <ul class="list-style-none f5" aria-labelledby="solutions-by-use-case-heading">
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;app_modernization&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;app_modernization_link_solutions_navbar&quot;}" href="/solutions/use-case/app-modernization">
      App Modernization

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;devsecops&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;devsecops_link_solutions_navbar&quot;}" href="/solutions/use-case/devsecops">
      DevSecOps

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;devops&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;devops_link_solutions_navbar&quot;}" href="/solutions/use-case/devops">
      DevOps

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;ci_cd&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;ci_cd_link_solutions_navbar&quot;}" href="/solutions/use-case/ci-cd">
      CI/CD

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all_use_cases&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_use_cases_link_solutions_navbar&quot;}" href="/solutions/use-case">
      View all use cases

    
</a></li>

                  </ul>
                </div>
            </div>
            <div class="HeaderMenu-column px-lg-4">
                <div class="border-bottom border-lg-bottom-0 pb-lg-0 pb-3">

                      <span class="d-block h4 color-fg-default my-1" id="solutions-by-industry-heading">By industry</span>

                  <ul class="list-style-none f5" aria-labelledby="solutions-by-industry-heading">
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;healthcare&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;healthcare_link_solutions_navbar&quot;}" href="/solutions/industry/healthcare">
      Healthcare

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;financial_services&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;financial_services_link_solutions_navbar&quot;}" href="/solutions/industry/financial-services">
      Financial services

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;manufacturing&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;manufacturing_link_solutions_navbar&quot;}" href="/solutions/industry/manufacturing">
      Manufacturing

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;government&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;government_link_solutions_navbar&quot;}" href="/solutions/industry/government">
      Government

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all_industries&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_industries_link_solutions_navbar&quot;}" href="/solutions/industry">
      View all industries

    
</a></li>

                  </ul>
                </div>
            </div>
        </div>

          <div class="HeaderMenu-trailing-link rounded-bottom-2 mt-lg-4 px-lg-4 py-4 py-lg-3 f5 text-semibold">
            <a data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all_solutions&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_solutions_link_solutions_navbar&quot;}" href="/solutions">
              View all solutions
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right HeaderMenu-trailing-link-icon">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</a>          </div>
      </div>
</li>


                  <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Resources
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>

      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4 dropdown-menu-wide">
        <div class="d-lg-flex dropdown-menu-wide">
            <div class="HeaderMenu-column px-lg-4 pb-3 pb-lg-0 border-lg-right">
                <div class="border-bottom border-lg-bottom-0 pb-lg-0 pb-3">

                      <span class="d-block h4 color-fg-default my-1" id="resources-topics-heading">Topics</span>

                  <ul class="list-style-none f5" aria-labelledby="resources-topics-heading">
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;ai&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;ai_link_resources_navbar&quot;}" href="/resources/articles?topic=ai">
      AI

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;devops&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;devops_link_resources_navbar&quot;}" href="/resources/articles?topic=devops">
      DevOps

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;security&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;security_link_resources_navbar&quot;}" href="/resources/articles?topic=security">
      Security

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;software_development&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;software_development_link_resources_navbar&quot;}" href="/resources/articles?topic=software-development">
      Software Development

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_link_resources_navbar&quot;}" href="/resources/articles">
      View all

    
</a></li>

                  </ul>
                </div>
            </div>
            <div class="HeaderMenu-column px-lg-4">
                <div class="border-bottom border-lg-bottom-0 pb-lg-0 border-bottom-0">

                      <span class="d-block h4 color-fg-default my-1" id="resources-explore-heading">Explore</span>

                  <ul class="list-style-none f5" aria-labelledby="resources-explore-heading">
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;learning_pathways&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;learning_pathways_link_resources_navbar&quot;}" href="https://resources.github.com/learn/pathways">
      Learning Pathways

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;events_amp_webinars&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;events_amp_webinars_link_resources_navbar&quot;}" href="https://github.com/resources/events">
      Events &amp; Webinars

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;ebooks_amp_whitepapers&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;ebooks_amp_whitepapers_link_resources_navbar&quot;}" href="https://github.com/resources/whitepapers">
      Ebooks &amp; Whitepapers

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;customer_stories&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;customer_stories_link_resources_navbar&quot;}" href="https://github.com/customer-stories">
      Customer Stories

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;partners&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;partners_link_resources_navbar&quot;}" href="https://github.com/partners">
      Partners

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;executive_insights&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;executive_insights_link_resources_navbar&quot;}" href="https://github.com/solutions/executive-insights">
      Executive Insights

    
</a></li>

                  </ul>
                </div>
            </div>
        </div>

      </div>
</li>


                  <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Open Source
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>

      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4">
        <div class="d-lg-flex dropdown-menu-wide">
            <div class="HeaderMenu-column px-lg-4">
                <div class="border-bottom mb-3 mb-lg-3 pb-3">

                  <ul class="list-style-none f5" >
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_sponsors&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_sponsors_link_open_source_navbar&quot;}" href="/sponsors">
      
      <div>
        <div class="color-fg-default h4">
          GitHub Sponsors

        </div>

        Fund open source developers
      </div>

    
</a></li>

                  </ul>
                </div>
                <div class="border-bottom mb-3 mb-lg-3 pb-3">

                  <ul class="list-style-none f5" >
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;the_readme_project&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;the_readme_project_link_open_source_navbar&quot;}" href="https://github.com/readme">
      
      <div>
        <div class="color-fg-default h4">
          The ReadME Project

        </div>

        GitHub community articles
      </div>

    
</a></li>

                  </ul>
                </div>
                <div class="border-bottom border-bottom-0">

                      <span class="d-block h4 color-fg-default my-1" id="open-source-repositories-heading">Repositories</span>

                  <ul class="list-style-none f5" aria-labelledby="open-source-repositories-heading">
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;topics&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;topics_link_open_source_navbar&quot;}" href="https://github.com/topics">
      Topics

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;trending&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;trending_link_open_source_navbar&quot;}" href="https://github.com/trending">
      Trending

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;collections&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;collections_link_open_source_navbar&quot;}" href="https://github.com/collections">
      Collections

    
</a></li>

                  </ul>
                </div>
            </div>
        </div>

      </div>
</li>


                  <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Enterprise
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>

      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4">
        <div class="d-lg-flex dropdown-menu-wide">
            <div class="HeaderMenu-column px-lg-4">
                <div class="border-bottom mb-3 mb-lg-3 pb-3">

                  <ul class="list-style-none f5" >
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;enterprise_platform&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;enterprise_platform_link_enterprise_navbar&quot;}" href="/enterprise">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-stack color-fg-subtle mr-3">
    <path d="M11.063 1.456a1.749 1.749 0 0 1 1.874 0l8.383 5.316a1.751 1.751 0 0 1 0 2.956l-8.383 5.316a1.749 1.749 0 0 1-1.874 0L2.68 9.728a1.751 1.751 0 0 1 0-2.956Zm1.071 1.267a.25.25 0 0 0-.268 0L3.483 8.039a.25.25 0 0 0 0 .422l8.383 5.316a.25.25 0 0 0 .268 0l8.383-5.316a.25.25 0 0 0 0-.422Z"></path><path d="M1.867 12.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path><path d="M1.867 16.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          Enterprise platform

        </div>

        AI-powered developer platform
      </div>

    
</a></li>

                  </ul>
                </div>
                <div class="border-bottom border-bottom-0">

                      <span class="d-block h4 color-fg-default my-1" id="enterprise-available-add-ons-heading">Available add-ons</span>

                  <ul class="list-style-none f5" aria-labelledby="enterprise-available-add-ons-heading">
                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description mb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_advanced_security&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_advanced_security_link_enterprise_navbar&quot;}" href="https://github.com/security/advanced-security">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-shield-check color-fg-subtle mr-3">
    <path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          GitHub Advanced Security

        </div>

        Enterprise-grade security features
      </div>

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description mb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;copilot_for_business&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;copilot_for_business_link_enterprise_navbar&quot;}" href="/features/copilot/copilot-business">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-copilot color-fg-subtle mr-3">
    <path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          Copilot for business

        </div>

        Enterprise-grade AI features
      </div>

    
</a></li>

                      <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;premium_support&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;premium_support_link_enterprise_navbar&quot;}" href="/premium-support">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-comment-discussion color-fg-subtle mr-3">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">
          Premium Support

        </div>

        Enterprise-grade 24/7 support
      </div>

    
</a></li>

                  </ul>
                </div>
            </div>
        </div>

      </div>
</li>


                  <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
    <a class="HeaderMenu-link no-underline px-0 px-lg-2 py-3 py-lg-2 d-block d-lg-inline-block" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;platform&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;platform_link_global_navbar&quot;}" href="https://github.com/pricing">Pricing</a>
</li>

              </ul>
            </nav>

        <div class="d-flex flex-column flex-lg-row width-full flex-justify-end flex-lg-items-center text-center mt-3 mt-lg-0 text-lg-left ml-lg-3">
                


<qbsearch-input class="search-input" data-scope="repo:ensdomains/docs" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="sADTQHI72WvIa7uyY8ns8tbIqVuuwzSKfQ4bElCZiSk-SIKk2xh3kCPaYgIw6RcKnumhXpJfepX8oL5ST9Y2tg" data-max-custom-scopes="10" data-header-redesign-enabled="false" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="ensdomains/docs" data-current-org="ensdomains" data-current-owner="" data-logged-in="false" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-retain-scroll-position="true">
  <div
    class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center mr-4 rounded"
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
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-4da5b3e8-ab10-457c-8ad5-36f654f3ec1e" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" />
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="hidden" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

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
      <div class="FormControl-inlineValidation" id="validation-4da5b3e8-ab10-457c-8ad5-36f654f3ec1e" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only"></div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
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
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="code-search-feedback-form" data-turbo="false" action="/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="IA8hUPNyK0f2/9e+BbhJRhFyq2V/gwnYgOUbooQxxFId+eY5qOKSRuPUwXcJMb8tbdAf5H+4JuqVKGc5FrtLQg==" />
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
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="custom-scopes-dialog-form" data-turbo="false" action="/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="Sk2rn5uFolHrBehYGAD4jFK5fL1imPM9P62DVzpr6pC0X6n6qkTA7hTo1BNQvHtsWz/w7LnO3DR/CNB4hdyx7Q==" />
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
              <input type="hidden" data-csrf="true" value="OZFDpAtK+U4/yHggBFpaXwGK2frqvnToR4zQNo17CbLcN1oSFANui4oP8ueJ88VczEwLhrBmflLq+23ou2ZKlA==" />
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
                href="/login?return_to=https%3A%2F%2Fgithub.com%2Fensdomains%2Fdocs%2Fblob%2F9edf9443de4333a0ea7ec658a870672d5d180d53%2Fens-improvement-proposals%2Fensip-15-normalization-standard.md"
                class="HeaderMenu-link HeaderMenu-link--sign-in HeaderMenu-button flex-shrink-0 no-underline d-none d-lg-inline-flex border border-lg-0 rounded px-2 py-1"
                style="margin-left: 12px;"
                data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="d4c9043501ad1fadbfe42410e0b5a42e14ecc335318c17e4c48d4fa5faebf040"
                data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}"
              >
                Sign in
              </a>
            </div>

              <a href="/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fblob%2Fshow&amp;source=header-repo&amp;source_repo=ensdomains%2Fdocs"
                class="HeaderMenu-link HeaderMenu-link--sign-up HeaderMenu-button flex-shrink-0 d-flex d-lg-inline-flex no-underline border color-border-default rounded px-2 py-1"
                data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="d4c9043501ad1fadbfe42410e0b5a42e14ecc335318c17e4c48d4fa5faebf040"
                data-analytics-event="{&quot;category&quot;:&quot;Sign up&quot;,&quot;action&quot;:&quot;click to sign up for account&quot;,&quot;label&quot;:&quot;ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show;ref_cta:Sign up;ref_loc:header logged out&quot;}"
              >
                Sign up
              </a>

                <div class="AppHeader-appearanceSettings">
    <react-partial-anchor>
      <button data-target="react-partial-anchor.anchor" id="icon-button-758c2b72-bbd1-42c7-8fb1-2a0b91d063ff" aria-labelledby="tooltip-6d4341a4-ec76-4023-81d1-a3e93d8a1340" type="button" disabled="disabled" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium AppHeader-button HeaderMenu-link border cursor-wait">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sliders Button-visual">
    <path d="M15 2.75a.75.75 0 0 1-.75.75h-4a.75.75 0 0 1 0-1.5h4a.75.75 0 0 1 .75.75Zm-8.5.75v1.25a.75.75 0 0 0 1.5 0v-4a.75.75 0 0 0-1.5 0V2H1.75a.75.75 0 0 0 0 1.5H6.5Zm1.25 5.25a.75.75 0 0 0 0-1.5h-6a.75.75 0 0 0 0 1.5h6ZM15 8a.75.75 0 0 1-.75.75H11.5V10a.75.75 0 1 1-1.5 0V6a.75.75 0 0 1 1.5 0v1.25h2.75A.75.75 0 0 1 15 8Zm-9 5.25v-2a.75.75 0 0 0-1.5 0v1.25H1.75a.75.75 0 0 0 0 1.5H4.5v1.25a.75.75 0 0 0 1.5 0v-2Zm9 0a.75.75 0 0 1-.75.75h-6a.75.75 0 0 1 0-1.5h6a.75.75 0 0 1 .75.75Z"></path>
</svg>
</button><tool-tip id="tooltip-6d4341a4-ec76-4023-81d1-a3e93d8a1340" for="icon-button-758c2b72-bbd1-42c7-8fb1-2a0b91d063ff" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Appearance settings</tool-tip>

      <template data-target="react-partial-anchor.template">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/appearance-settings.753d458774a2f782559b.module.css" />

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

    <button id="icon-button-98361040-e9eb-485d-984f-54a542161b67" aria-labelledby="tooltip-d933194c-ffef-45c5-b252-e4a7879671ef" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-d933194c-ffef-45c5-b252-e4a7879671ef" for="icon-button-98361040-e9eb-485d-984f-54a542161b67" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Dismiss alert</tool-tip>


  
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
      
      
    

    






  
  <div id="repository-container-header"  class="pt-3 hide-full-screen" style="background-color: var(--page-header-bgColor, var(--color-page-header-bg));" data-turbo-replace>

      <div class="d-flex flex-nowrap flex-justify-end mb-3  px-3 px-lg-5" style="gap: 1rem;">

        <div class="flex-auto min-width-0 width-fit">
            
  <div class=" d-flex flex-wrap flex-items-center wb-break-word f3 text-normal">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo color-fg-muted mr-2">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
    
    <span class="author flex-self-stretch" itemprop="author">
      <a class="url fn" rel="author" data-hovercard-type="organization" data-hovercard-url="/orgs/ensdomains/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ensdomains">
        ensdomains
</a>    </span>
    <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
    <strong itemprop="name" class="mr-2 flex-self-stretch">
      <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/ensdomains/docs">docs</a>
    </strong>

    <span></span><span class="Label Label--secondary v-align-middle mr-1">Public</span>
  </div>


        </div>

        <div id="repository-details-container" class="flex-shrink-0" data-turbo-replace style="max-width: 70%;">
            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
    
      

  <li>
            <a href="/login?return_to=%2Fensdomains%2Fdocs" rel="nofollow" id="repository-details-watch-button" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="d0e4638e5562443df768cd1c2617d2abe0b158645b82ad5b3a2247d0c24bd33b" aria-label="You must be signed in to change notification settings" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>Notifications
</a>    <tool-tip id="tooltip-490c74c1-5eeb-4dd0-88c1-ba1902247a87" for="repository-details-watch-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">You must be signed in to change notification settings</tool-tip>

  </li>

  <li>
          <a icon="repo-forked" id="fork-button" href="/login?return_to=%2Fensdomains%2Fdocs" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:172392769,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="880d58b7a971a932b0227e2ea682f3916deee33fc10ccd759fc1598df971f812" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>Fork
    <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="327" data-view-component="true" class="Counter">327</span>
</a>
  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <a href="/login?return_to=%2Fensdomains%2Fdocs" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:172392769,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="1b49f0b4bccf95d27b4814bb1b46990f8ef581dcfcb30f4e5a3befae505fca82" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-sw btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>          <span id="repo-stars-counter-star" aria-label="190 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="190" data-view-component="true" class="Counter js-social-count">190</span>
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
  <a id="code-tab" href="/ensdomains/docs" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /ensdomains/docs" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" aria-current="page" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="/ensdomains/docs/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /ensdomains/docs/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="6" data-view-component="true" class="Counter">6</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/ensdomains/docs/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /ensdomains/docs/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="5" data-view-component="true" class="Counter">5</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/ensdomains/docs/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /ensdomains/docs/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="/ensdomains/docs/security" data-tab-item="i4security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /ensdomains/docs/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          <include-fragment src="/ensdomains/docs/security/overall-count" accept="text/fragment+html" data-nonce="v2:bfe21f2e-7e7c-5bc7-b014-2c6d41e095d4" data-view-component="true">
  
  <div data-show-on-forbidden-error hidden>
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        <p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="" aria-label="Please reload this page">Please reload this page</a>.</p>
</p>

</div>  </div>
</div>  </div>
</include-fragment>

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="/ensdomains/docs/pulse" data-tab-item="i5insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /ensdomains/docs/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true">
  <focus-group direction="vertical" mnemonics retain>
    <button id="action-menu-b0ae42e6-db7e-4d08-b606-7ecf39a9c9bb-button" popovertarget="action-menu-b0ae42e6-db7e-4d08-b606-7ecf39a9c9bb-overlay" aria-controls="action-menu-b0ae42e6-db7e-4d08-b606-7ecf39a9c9bb-list" aria-haspopup="true" aria-labelledby="tooltip-66c16cf8-99e1-42d0-9652-20a0d1c4e186" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-66c16cf8-99e1-42d0-9652-20a0d1c4e186" for="action-menu-b0ae42e6-db7e-4d08-b606-7ecf39a9c9bb-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-b0ae42e6-db7e-4d08-b606-7ecf39a9c9bb-overlay" anchor="action-menu-b0ae42e6-db7e-4d08-b606-7ecf39a9c9bb-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list>
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-b0ae42e6-db7e-4d08-b606-7ecf39a9c9bb-button" id="action-menu-b0ae42e6-db7e-4d08-b606-7ecf39a9c9bb-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="hidden" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-faf9fb92-ea21-4070-8bac-0868236a44d0" href="/ensdomains/docs" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-6a07c917-2394-4145-a78e-79644c36d582" href="/ensdomains/docs/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-1a66ae0b-b2cd-4e52-8dcc-827c3a2e33f1" href="/ensdomains/docs/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-5e540c04-914d-4a36-ae13-2cb8eb7174dd" href="/ensdomains/docs/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
        <li hidden="hidden" data-menu-item="i4security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-d52f96cd-4d13-4c8c-9404-76c64ed7fc7a" href="/ensdomains/docs/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
        <li hidden="hidden" data-menu-item="i5insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-daf7dcd7-ecc7-4079-8249-a7ccfecfc7f0" href="/ensdomains/docs/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
  app-name="react-code-view"
  initial-path="/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md"
    style="display: block; min-height: calc(100vh - 64px);"
  data-attempted-ssr="false"
  data-ssr="false"
  data-lazy="false"
  data-alternate="false"
  data-data-router-enabled="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":false,"fileTree":{"ens-improvement-proposals":{"items":[{"name":"README.md","path":"ens-improvement-proposals/README.md","contentType":"file"},{"name":"ensip-1-ens.md","path":"ens-improvement-proposals/ensip-1-ens.md","contentType":"file"},{"name":"ensip-10-wildcard-resolution.md","path":"ens-improvement-proposals/ensip-10-wildcard-resolution.md","contentType":"file"},{"name":"ensip-11-evmchain-address-resolution.md","path":"ens-improvement-proposals/ensip-11-evmchain-address-resolution.md","contentType":"file"},{"name":"ensip-12-avatar-text-records.md","path":"ens-improvement-proposals/ensip-12-avatar-text-records.md","contentType":"file"},{"name":"ensip-13-secondary-authentication-for-ens.md","path":"ens-improvement-proposals/ensip-13-secondary-authentication-for-ens.md","contentType":"file"},{"name":"ensip-14-platform-source-parameter.md","path":"ens-improvement-proposals/ensip-14-platform-source-parameter.md","contentType":"file"},{"name":"ensip-15-normalization-standard.md","path":"ens-improvement-proposals/ensip-15-normalization-standard.md","contentType":"file"},{"name":"ensip-2-initial-hash-registrar.md","path":"ens-improvement-proposals/ensip-2-initial-hash-registrar.md","contentType":"file"},{"name":"ensip-3-reverse-resolution.md","path":"ens-improvement-proposals/ensip-3-reverse-resolution.md","contentType":"file"},{"name":"ensip-4-support-for-contract-abis.md","path":"ens-improvement-proposals/ensip-4-support-for-contract-abis.md","contentType":"file"},{"name":"ensip-5-text-records.md","path":"ens-improvement-proposals/ensip-5-text-records.md","contentType":"file"},{"name":"ensip-6-dns-in-ens.md","path":"ens-improvement-proposals/ensip-6-dns-in-ens.md","contentType":"file"},{"name":"ensip-7-contenthash-field.md","path":"ens-improvement-proposals/ensip-7-contenthash-field.md","contentType":"file"},{"name":"ensip-8-interface-discovery.md","path":"ens-improvement-proposals/ensip-8-interface-discovery.md","contentType":"file"},{"name":"ensip-9-multichain-address-resolution.md","path":"ens-improvement-proposals/ensip-9-multichain-address-resolution.md","contentType":"file"}],"totalCount":16},"":{"items":[{"name":".gitbook","path":".gitbook","contentType":"directory"},{"name":"contract-api-reference","path":"contract-api-reference","contentType":"directory"},{"name":"contract-developer-guide","path":"contract-developer-guide","contentType":"directory"},{"name":"dapp-developer-guide","path":"dapp-developer-guide","contentType":"directory"},{"name":"ens-improvement-proposals","path":"ens-improvement-proposals","contentType":"directory"},{"name":"ens-migration-february-2020","path":"ens-migration-february-2020","contentType":"directory"},{"name":"normalization-standard","path":"normalization-standard","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"SUMMARY.md","path":"SUMMARY.md","contentType":"file"},{"name":"bug-bounty-program.md","path":"bug-bounty-program.md","contentType":"file"},{"name":"deploying-ens-on-a-private-chain.md","path":"deploying-ens-on-a-private-chain.md","contentType":"file"},{"name":"dns-registrar-guide.md","path":"dns-registrar-guide.md","contentType":"file"},{"name":"ens-deployments.md","path":"ens-deployments.md","contentType":"file"},{"name":"frequently-asked-questions.md","path":"frequently-asked-questions.md","contentType":"file"},{"name":"permanent-registrar-faq.md","path":"permanent-registrar-faq.md","contentType":"file"},{"name":"terminology.md","path":"terminology.md","contentType":"file"}],"totalCount":16}},"fileTreeProcessingTime":48.149205,"foldersToFetch":[],"incompleteFileTree":false,"repo":{"id":172392769,"defaultBranch":"master","name":"docs","ownerLogin":"ensdomains","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2019-02-24T21:31:43.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/34167658?v=4","public":true,"private":false,"isOrgOwned":true},"codeLineWrapEnabled":false,"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"9edf9443de4333a0ea7ec658a870672d5d180d53","listCacheKey":"v0:1763045921.0","canEdit":false,"refType":"tree","currentOid":"9edf9443de4333a0ea7ec658a870672d5d180d53","canEditOnDefaultBranch":false,"fileExistsOnDefault":false},"path":"ens-improvement-proposals/ensip-15-normalization-standard.md","currentUser":null,"blob":{"rawLines":null,"stylingDirectives":null,"colorizedLines":null,"csv":null,"csvError":null,"copilotSWEAgentEnabled":false,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/ensdomains/docs/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null},"displayName":"ensip-15-normalization-standard.md","displayUrl":"https://github.com/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md?raw=true","headerInfo":{"blobSize":"19.7 KB","deleteTooltip":"You must be signed in to make or propose changes","editTooltip":"You must be signed in to make or propose changes","ghDesktopPath":null,"isGitLfs":false,"onBranch":false,"shortPath":"3146049","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fensdomains%2Fdocs%2Fblob%2F9edf9443de4333a0ea7ec658a870672d5d180d53%2Fens-improvement-proposals%2Fensip-15-normalization-standard.md","isCSV":false,"isRichtext":true,"toc":[{"level":1,"text":"ENSIP-15: ENS Name Normalization Standard","anchor":"ensip-15-ens-name-normalization-standard","htmlText":"ENSIP-15: ENS Name Normalization Standard"},{"level":2,"text":"Abstract","anchor":"abstract","htmlText":"Abstract"},{"level":2,"text":"Motivation","anchor":"motivation","htmlText":"Motivation"},{"level":2,"text":"Specification","anchor":"specification","htmlText":"Specification"},{"level":3,"text":"Versioning","anchor":"versioning","htmlText":"Versioning"},{"level":3,"text":"Algorithm","anchor":"algorithm","htmlText":"Algorithm"},{"level":3,"text":"Normalize","anchor":"normalize","htmlText":"Normalize"},{"level":3,"text":"Tokenize","anchor":"tokenize","htmlText":"Tokenize"},{"level":3,"text":"Validate","anchor":"validate","htmlText":"Validate"},{"level":3,"text":"Wholes","anchor":"wholes","htmlText":"Wholes"},{"level":2,"text":"Description of spec.json","anchor":"description-of-specjson","htmlText":"Description of spec.json"},{"level":2,"text":"Derivation","anchor":"derivation","htmlText":"Derivation"},{"level":2,"text":"Backwards Compatibility","anchor":"backwards-compatibility","htmlText":"Backwards Compatibility"},{"level":2,"text":"Security Considerations","anchor":"security-considerations","htmlText":"Security Considerations"},{"level":2,"text":"Copyright","anchor":"copyright","htmlText":"Copyright"},{"level":2,"text":"Appendix: Reference Specifications","anchor":"appendix-reference-specifications","htmlText":"Appendix: Reference Specifications"},{"level":2,"text":"Appendix: Validation Tests","anchor":"appendix-validation-tests","htmlText":"Appendix: Validation Tests"},{"level":2,"text":"Annex: Beautification","anchor":"annex-beautification","htmlText":"Annex: Beautification"}],"lineInfo":{"truncatedLoc":"340","truncatedSloc":"301"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplate":null,"discussionTemplate":null,"language":"Markdown","languageID":222,"large":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/ensdomains/docs/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/ensdomains/docs/raw/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-15-normalization-standard.md","renderImageOrRaw":false,"richText":"\u003carticle class=\"markdown-body entry-content container-lg\" itemprop=\"text\"\u003e\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch1 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eENSIP-15: ENS Name Normalization Standard\u003c/h1\u003e\u003ca id=\"user-content-ensip-15-ens-name-normalization-standard\" class=\"anchor\" aria-label=\"Permalink: ENSIP-15: ENS Name Normalization Standard\" href=\"#ensip-15-ens-name-normalization-standard\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cmarkdown-accessiblity-table\u003e\u003ctable\u003e\n\u003cthead\u003e\n\u003ctr\u003e\n\u003cth\u003e\u003cstrong\u003eAuthor\u003c/strong\u003e\u003c/th\u003e\n\u003cth\u003eAndrew Raffensperger \u0026lt;\u003ca href=\"mailto:raffy@me.com\"\u003eraffy@me.com\u003c/a\u003e\u0026gt;\u003c/th\u003e\n\u003c/tr\u003e\n\u003c/thead\u003e\n\u003ctbody\u003e\n\u003ctr\u003e\n\u003ctd\u003e\u003cstrong\u003eStatus\u003c/strong\u003e\u003c/td\u003e\n\u003ctd\u003eDraft\u003c/td\u003e\n\u003c/tr\u003e\n\u003ctr\u003e\n\u003ctd\u003e\u003cstrong\u003eCreated\u003c/strong\u003e\u003c/td\u003e\n\u003ctd\u003e2023-04-03\u003c/td\u003e\n\u003c/tr\u003e\n\u003c/tbody\u003e\n\u003c/table\u003e\u003c/markdown-accessiblity-table\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eAbstract\u003c/h2\u003e\u003ca id=\"user-content-abstract\" class=\"anchor\" aria-label=\"Permalink: Abstract\" href=\"#abstract\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThis ENSIP standardizes Ethereum Name Service (ENS) name normalization process outlined in \u003ca href=\"/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-1-ens#name-syntax\"\u003eENSIP-1 § Name Syntax\u003c/a\u003e.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eMotivation\u003c/h2\u003e\u003ca id=\"user-content-motivation\" class=\"anchor\" aria-label=\"Permalink: Motivation\" href=\"#motivation\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eSince \u003ca href=\"/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-1-ens\"\u003eENSIP-1\u003c/a\u003e (originally \u003ca href=\"https://eips.ethereum.org/EIPS/eip-137\" rel=\"nofollow\"\u003eEIP-137\u003c/a\u003e) was finalized in 2016, Unicode has \u003ca href=\"https://unicode.org/history/publicationdates.html\" rel=\"nofollow\"\u003eevolved\u003c/a\u003e from version 8.0.0 to 15.0.0 and incorporated many new characters, including complex emoji sequences.\u003c/li\u003e\n\u003cli\u003eENSIP-1 does not state the version of Unicode.\u003c/li\u003e\n\u003cli\u003eENSIP-1 implies but does not state an explicit flavor of IDNA processing.\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://unicode.org/reports/tr46/\" rel=\"nofollow\"\u003eUTS-46\u003c/a\u003e is insufficient to normalize emoji sequences. Correct emoji processing is only possible with \u003ca href=\"https://www.unicode.org/reports/tr51/\" rel=\"nofollow\"\u003eUTS-51\u003c/a\u003e.\u003c/li\u003e\n\u003cli\u003eValidation tests are needed to ensure implementation compliance.\u003c/li\u003e\n\u003cli\u003eThe success of ENS has encouraged spoofing via the following techniques:\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eInsertion of zero-width characters.\u003c/li\u003e\n\u003cli\u003eUsing names which normalize differently between algorithms.\u003c/li\u003e\n\u003cli\u003eUsing names which appear differently between applications and devices.\u003c/li\u003e\n\u003cli\u003eSubstitution of confusable (look-alike) characters.\u003c/li\u003e\n\u003cli\u003eMixing incompatible scripts.\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eSpecification\u003c/h2\u003e\u003ca id=\"user-content-specification\" class=\"anchor\" aria-label=\"Permalink: Specification\" href=\"#specification\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eVersioning\u003c/h3\u003e\u003ca id=\"user-content-versioning\" class=\"anchor\" aria-label=\"Permalink: Versioning\" href=\"#versioning\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eUnicode version \u003ccode\u003e15.0.0\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/normalization-standard/spec.json\"\u003espec.json\u003c/a\u003e contains all necessary data for normalization.\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/normalization-standard/nf.json\"\u003enf.json\u003c/a\u003e contains all necessary data for \u003ca href=\"https://unicode.org/reports/tr15/\" rel=\"nofollow\"\u003eUnicode Normalization Forms\u003c/a\u003e NFC and NFD.\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eAlgorithm\u003c/h3\u003e\u003ca id=\"user-content-algorithm\" class=\"anchor\" aria-label=\"Permalink: Algorithm\" href=\"#algorithm\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eNormalization is the process of canonicalizing a name before for hashing.\u003c/li\u003e\n\u003cli\u003eIt is idempotent: applying normalization multiple times produces the same result.\u003c/li\u003e\n\u003cli\u003eFor user convenience, leading and trailing whitespace should be trimmed before normalization, as all whitespace codepoints are disallowed.  Inner characters should remain unmodified.\u003c/li\u003e\n\u003cli\u003eNo string transformations (like case-folding) should be applied.\u003c/li\u003e\n\u003c/ul\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eSplit the name into \u003ca href=\"/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-1-ens#name-syntax\"\u003elabels\u003c/a\u003e.\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#normalize\"\u003eNormalize\u003c/a\u003e each label.\u003c/li\u003e\n\u003cli\u003eJoin the labels together into a name again.\u003c/li\u003e\n\u003cli\u003eThe result is normalized and ready for \u003ca href=\"/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-1-ens#namehash-algorithm\"\u003ehashing\u003c/a\u003e.\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eNormalize\u003c/h3\u003e\u003ca id=\"user-content-normalize\" class=\"anchor\" aria-label=\"Permalink: Normalize\" href=\"#normalize\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"#tokenize\"\u003eTokenize\u003c/a\u003e — transform the label into \u003cstrong\u003eText\u003c/strong\u003e and \u003cstrong\u003eEmoji\u003c/strong\u003e tokens.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eIf there are no tokens, the label cannot be normalized.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eApply NFC to each \u003cstrong\u003eText\u003c/strong\u003e token.\u003c/li\u003e\n\u003cli\u003eStrip \u003ccode\u003eFE0F\u003c/code\u003e from each \u003cstrong\u003eEmoji\u003c/strong\u003e token.\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#validate\"\u003eValidate\u003c/a\u003e — check if the tokens are valid and obtain the \u003cstrong\u003eLabel Type\u003c/strong\u003e.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eThe \u003cstrong\u003eLabel Type\u003c/strong\u003e and \u003cstrong\u003eRestricted\u003c/strong\u003e state may be presented to user for additional security.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eConcatenate the tokens together.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eReturn the normalized label.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eTokenize\u003c/h3\u003e\u003ca id=\"user-content-tokenize\" class=\"anchor\" aria-label=\"Permalink: Tokenize\" href=\"#tokenize\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eGiven a string, convert to codepoints, and produce a list of \u003cstrong\u003eText\u003c/strong\u003e and \u003cstrong\u003eEmoji\u003c/strong\u003e tokens, each with a payload of codepoints.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eAllocate an empty codepoint buffer.\u003c/li\u003e\n\u003cli\u003eFind the longest emoji sequence that matches the remaining input.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003eFE0F\u003c/code\u003e is optional from the input during matching.\u003c/li\u003e\n\u003cli\u003eExample: \u003ccode\u003eEmoji[A FE0F B]\u003c/code\u003e matches \u003ccode\u003e[A FE0F B]\u003c/code\u003e and \u003ccode\u003e[A B]\u003c/code\u003e but not \u003ccode\u003e[A FE0F FE0F B]\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eIf an emoji sequence is found:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eIf the buffer is nonempty, emit a \u003cstrong\u003eText\u003c/strong\u003e token, and clear the buffer.\u003c/li\u003e\n\u003cli\u003eEmit an \u003cstrong\u003eEmoji\u003c/strong\u003e token with the fully-qualified matching sequence.\u003c/li\u003e\n\u003cli\u003eRemove the matched sequence from the input.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eOtherwise:\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eRemove the leading codepoint from the input.\u003c/li\u003e\n\u003cli\u003eDetermine the codepoint type:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eIf \u003cstrong\u003evalid\u003c/strong\u003e, append the codepoint to the buffer.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eThis set can be precomputed from the union of characters in all groups and their NFD decompositions.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eIf \u003cstrong\u003emapped\u003c/strong\u003e, append the corresponding mapped codepoint(s) to the buffer.\u003c/li\u003e\n\u003cli\u003eIf \u003cstrong\u003eignored\u003c/strong\u003e, do nothing.\u003c/li\u003e\n\u003cli\u003eOtherwise, the label cannot be normalized.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/li\u003e\n\u003cli\u003eRepeat until all the input is consumed.\u003c/li\u003e\n\u003cli\u003eIf the buffer is nonempty, emit a final \u003cstrong\u003eText\u003c/strong\u003e token.\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eValidate\u003c/h3\u003e\u003ca id=\"user-content-validate\" class=\"anchor\" aria-label=\"Permalink: Validate\" href=\"#validate\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eGiven a list of \u003cstrong\u003eEmoji\u003c/strong\u003e and \u003cstrong\u003eText\u003c/strong\u003e tokens, determine if the composition is valid and return the \u003cstrong\u003eLabel Type\u003c/strong\u003e.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eIf only \u003cstrong\u003eEmoji\u003c/strong\u003e tokens:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eReturn \u003ccode\u003e\"Emoji\"\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eIf a single \u003cstrong\u003eText\u003c/strong\u003e token and every characters is ASCII (\u003ccode\u003e00..7F\u003c/code\u003e):\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e5F (_) LOW LINE\u003c/code\u003e can only occur at the start.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eMust match \u003ccode\u003e/^_*[^_]*$/\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eThe 3rd and 4th characters must not both be \u003ccode\u003e2D (-) HYPHEN-MINUS\u003c/code\u003e.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eMust not match \u003ccode\u003e/^..--/\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eReturn \u003ccode\u003e\"ASCII\"\u003c/code\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eThe label is free of \u003cstrong\u003eFenced\u003c/strong\u003e and \u003cstrong\u003eCombining Mark\u003c/strong\u003e characters, and not confusable.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eConcatenate all the tokens together.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e5F (_) LOW LINE\u003c/code\u003e can only occur at the start.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eMust match \u003ccode\u003e/^_*[^_]$/u\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eThe first and last characters cannot be \u003cstrong\u003eFenced\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eFenced\u003c/strong\u003e characters cannot be contiguous.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eThe first character of every \u003cstrong\u003eText\u003c/strong\u003e token must not be a \u003cstrong\u003eCombining Mark\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003eConcatenate the \u003cstrong\u003eText\u003c/strong\u003e tokens together.\u003c/li\u003e\n\u003cli\u003eFind the first \u003cstrong\u003eGroup\u003c/strong\u003e that contain every text character:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eIf no group is found, the label cannot be normalized.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eIf the group is not \u003cstrong\u003eCM Whitelisted\u003c/strong\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eApply NFD to the concatenated text characters.\u003c/li\u003e\n\u003cli\u003eFor every contiguous sequence of \u003cstrong\u003eNSM\u003c/strong\u003e characters:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eEach character must be unique.\u003c/li\u003e\n\u003cli\u003eNumber of characters cannot exceed \u003cstrong\u003eMaximum NSM\u003c/strong\u003e (4).\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#wholes\"\u003eWholes\u003c/a\u003e — check if text characters form a confusable.\u003c/li\u003e\n\u003cli\u003eThe label is valid.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eReturn the name of the group.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eWholes\u003c/h3\u003e\u003ca id=\"user-content-wholes\" class=\"anchor\" aria-label=\"Permalink: Wholes\" href=\"#wholes\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eA label is whole-script confusable if a similarly-looking valid label can be constructed using one alternative character from a different group.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eAllocate an empty character buffer.\u003c/li\u003e\n\u003cli\u003eStart with the set of all groups.\u003c/li\u003e\n\u003cli\u003eFor each unique character:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eIf the character is \u003cstrong\u003eConfused\u003c/strong\u003e (a member of a \u003cstrong\u003eWhole Confusable\u003c/strong\u003e):\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eRetain groups with \u003cstrong\u003eWhole Confusable\u003c/strong\u003e characters excluding the \u003cstrong\u003eConfusable Extent\u003c/strong\u003e of the matching \u003cstrong\u003eConfused\u003c/strong\u003e character.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eThe \u003cstrong\u003eConfusable Extent\u003c/strong\u003e is the fully-connected graph formed from different groups with the same confusable and different confusables of the same group.\u003c/li\u003e\n\u003cli\u003eThis mapping from \u003cstrong\u003eConfused\u003c/strong\u003e to \u003cstrong\u003eConfusable Extent\u003c/strong\u003e can be precomputed.\u003c/li\u003e\n\u003cli\u003eExample: \u003ccode\u003e\"o\"\u003c/code\u003e \u003cstrong\u003eWhole Confusable\u003c/strong\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e6F (o) LATIN SMALL LETTER O\u003c/code\u003e → \u003cem\u003eLatin\u003c/em\u003e, \u003cem\u003eHan\u003c/em\u003e, \u003cem\u003eJapanese\u003c/em\u003e, and \u003cem\u003eKorean\u003c/em\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e3007 (〇) IDEOGRAPHIC NUMBER ZERO\u003c/code\u003e → \u003cem\u003eHan\u003c/em\u003e, \u003cem\u003eJapanese\u003c/em\u003e, \u003cem\u003eKorean\u003c/em\u003e, and \u003cem\u003eBopomofo\u003c/em\u003e\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eConfusable Extent\u003c/strong\u003e is [\u003ccode\u003e6F\u003c/code\u003e, \u003ccode\u003e3007\u003c/code\u003e] ⊗ [\u003cem\u003eLatin\u003c/em\u003e, \u003cem\u003eHan\u003c/em\u003e, \u003cem\u003eJapanese\u003c/em\u003e, \u003cem\u003eKorean\u003c/em\u003e, \u003cem\u003eBopomofo\u003c/em\u003e]\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eIf no groups remain, the label is not confusable.\u003c/li\u003e\n\u003cli\u003eExample: \u003ccode\u003e\"тӕ\" [442 4D5]\u003c/code\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e\"т\"\u003c/code\u003e → \u003ccode\u003e442 (т) CYRILLIC SMALL LETTER TE\u003c/code\u003e and \u003ccode\u003e3C4 (τ) GREEK SMALL LETTER TAU\u003c/code\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003cstrong\u003eALL\u003c/strong\u003e ∩ [\u003cem\u003eCyrillic\u003c/em\u003e, \u003cem\u003eGreek\u003c/em\u003e] → [\u003cem\u003eCyrillic\u003c/em\u003e, \u003cem\u003eGreek\u003c/em\u003e]\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e\"ӕ\"\u003c/code\u003e → \u003ccode\u003eE6 (æ) LATIN SMALL LETTER AE\u003c/code\u003e and \u003ccode\u003e4D5 (ӕ) CYRILLIC SMALL LIGATURE A IE\u003c/code\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e[\u003cem\u003eCyrillic\u003c/em\u003e, \u003cem\u003eGreek\u003c/em\u003e] ∩ [\u003cem\u003eLatin\u003c/em\u003e, \u003cem\u003eCyrillic\u003c/em\u003e] → [\u003cem\u003eCyrillic\u003c/em\u003e]\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eIf the character is \u003cstrong\u003eUnique\u003c/strong\u003e, the label is not confusable.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eThis set can be precomputed from characters that appear in exactly one group and are not \u003cstrong\u003eConfused\u003c/strong\u003e.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eOtherwise:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eAppend the character to the buffer.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eIf any \u003cstrong\u003eConfused\u003c/strong\u003e characters were found:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eAssert none of the remaining groups contain any buffered characters.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eThe label is not confusable.\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDescription of \u003ccode\u003espec.json\u003c/code\u003e\u003c/h2\u003e\u003ca id=\"user-content-description-of-specjson\" class=\"anchor\" aria-label=\"Permalink: Description of spec.json\" href=\"#description-of-specjson\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003cstrong\u003eGroups\u003c/strong\u003e (\u003ccode\u003e\"groups\"\u003c/code\u003e) — groups of characters that can constitute a label\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e\"name\"\u003c/code\u003e — ASCII name of the group (or abbreviation if \u003cstrong\u003eRestricted\u003c/strong\u003e)\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003cem\u003eLatin\u003c/em\u003e, \u003cem\u003eJapanese\u003c/em\u003e, \u003cem\u003eEgyp\u003c/em\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eRestricted\u003c/strong\u003e (\u003ccode\u003e\"restricted\"\u003c/code\u003e) — \u003cstrong\u003e\u003ccode\u003etrue\u003c/code\u003e\u003c/strong\u003e if \u003ca href=\"https://www.unicode.org/reports/tr31#Table_Candidate_Characters_for_Exclusion_from_Identifiers\" rel=\"nofollow\"\u003eExcluded\u003c/a\u003e or \u003ca href=\"https://www.unicode.org/reports/tr31/#Table_Limited_Use_Scripts\" rel=\"nofollow\"\u003eLimited-Use\u003c/a\u003e script\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003cem\u003eLatin\u003c/em\u003e → \u003cstrong\u003e\u003ccode\u003efalse\u003c/code\u003e\u003c/strong\u003e, \u003cem\u003eEgyp\u003c/em\u003e → \u003cstrong\u003e\u003ccode\u003etrue\u003c/code\u003e\u003c/strong\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e\"primary\"\u003c/code\u003e — subset of characters that define the group\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e\"a\"\u003c/code\u003e → \u003cem\u003eLatin\u003c/em\u003e, \u003ccode\u003e\"あ\"\u003c/code\u003e → \u003cem\u003eJapanese\u003c/em\u003e, \u003ccode\u003e\"𓀀\"\u003c/code\u003e → \u003cem\u003eEgyp\u003c/em\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e\"secondary\"\u003c/code\u003e — subset of characters included with the group\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e\"0\"\u003c/code\u003e → \u003cem\u003eCommon\u003c/em\u003e but mixable with \u003cem\u003eLatin\u003c/em\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eCM Whitelisted\u003c/strong\u003e (\u003ccode\u003e\"cm\"\u003c/code\u003e) — (optional) set of allowed compound sequences in NFC\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e[[BaseCP, CM, ...], ...]\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003eThere are currently no compound sequences: \u003cstrong\u003e\u003ccode\u003etrue\u003c/code\u003e\u003c/strong\u003e if \u003ccode\u003e[]\u003c/code\u003e otherwise \u003cstrong\u003e\u003ccode\u003efalse\u003c/code\u003e\u003c/strong\u003e.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eIgnored\u003c/strong\u003e (\u003ccode\u003e\"ignored\"\u003c/code\u003e) — characters that are ignored during normalization\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e34F (�) COMBINING GRAPHEME JOINER\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eMapped\u003c/strong\u003e (\u003ccode\u003e\"mapped\"\u003c/code\u003e) — characters that are mapped to a sequence of \u003cstrong\u003evalid\u003c/strong\u003e characters\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e41 (A) LATIN CAPITAL LETTER A\u003c/code\u003e → \u003ccode\u003e[61 (a) LATIN SMALL LETTER A]\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003eExample: \u003ccode\u003e2165 (Ⅵ) ROMAN NUMERAL SIX\u003c/code\u003e → \u003ccode\u003e[76 (v) LATIN SMALL LETTER V, 69 (i) LATIN SMALL LETTER I]\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eWhole Confusable\u003c/strong\u003e (\u003ccode\u003e\"wholes\"\u003c/code\u003e) — groups of characters that look similar\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e\"valid\"\u003c/code\u003e — subset of confusable characters that are allowed\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e34 (4) DIGIT FOUR\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eConfused\u003c/strong\u003e (\u003ccode\u003e\"confused\"\u003c/code\u003e) — subset of confusable characters that confuse\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e13CE (Ꮞ) CHEROKEE LETTER SE\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eFenced\u003c/strong\u003e (\u003ccode\u003e\"fenced\"\u003c/code\u003e) — set of characters that cannot be first, last, or contiguous\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e2044 (⁄) FRACTION SLASH\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eEmoji\u003c/strong\u003e (\u003ccode\u003e\"emoji\"\u003c/code\u003e) — allowed emoji sequences\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e[1F468 200D 1F4BB] (👨‍💻) man technologist\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eCombining Marks / CM\u003c/strong\u003e (\u003ccode\u003e\"cm\"\u003c/code\u003e) — characters that are \u003ca href=\"https://www.unicode.org/Public/15.0.0/ucd/extracted/DerivedGeneralCategory\" rel=\"nofollow\"\u003eCombining Marks\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eNon-spacing Marks / NSM\u003c/strong\u003e (\u003ccode\u003e\"nsm\"\u003c/code\u003e) — valid subset of \u003cstrong\u003eCM\u003c/strong\u003e with general category (\u003ccode\u003e\"Mn\"\u003c/code\u003e or \u003ccode\u003e\"Me\"\u003c/code\u003e)\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eMaximum NSM\u003c/strong\u003e (\u003ccode\u003e\"nsm_max\"\u003c/code\u003e) — maximum sequence length of unique \u003cstrong\u003eNSM\u003c/strong\u003e\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eShould Escape\u003c/strong\u003e (\u003ccode\u003e\"escape\"\u003c/code\u003e) — characters that \u003ca href=\"https://github.com/adraffy/ens-normalize.js/blob/20230221-stable/derive/rules/chars-escape.js\"\u003eshouldn't be printed\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eNFC Check\u003c/strong\u003e (\u003ccode\u003e\"nfc_check\"\u003c/code\u003e) — valid characters that \u003ca href=\"https://unicode.org/reports/tr15/#NFC_QC_Optimization\" rel=\"nofollow\"\u003emay require NFC\u003c/a\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDerivation\u003c/h2\u003e\u003ca id=\"user-content-derivation\" class=\"anchor\" aria-label=\"Permalink: Derivation\" href=\"#derivation\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"https://unicode.org/Public/idna/15.0.0/IdnaMappingTable.txt\" rel=\"nofollow\"\u003eIDNA 2003\u003c/a\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003eUseSTD3ASCIIRules\u003c/code\u003e is \u003cstrong\u003e\u003ccode\u003etrue\u003c/code\u003e\u003c/strong\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003eVerifyDnsLength\u003c/code\u003e is \u003cstrong\u003e\u003ccode\u003efalse\u003c/code\u003e\u003c/strong\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003eTransitional_Processing\u003c/code\u003e is \u003cstrong\u003e\u003ccode\u003efalse\u003c/code\u003e\u003c/strong\u003e\u003c/li\u003e\n\u003cli\u003eThe following deviations are \u003cstrong\u003evalid\u003c/strong\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003eDF (ß) LATIN SMALL LETTER SHARP S\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e3C2 (ς) GREEK SMALL LETTER FINAL SIGMA\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003eCheckHyphens\u003c/code\u003e is \u003cstrong\u003e\u003ccode\u003efalse\u003c/code\u003e\u003c/strong\u003e (\u003ca href=\"https://url.spec.whatwg.org/#idna\" rel=\"nofollow\"\u003eWhatWG URL Spec § 3.3\u003c/a\u003e)\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003eCheckBidi\u003c/code\u003e is \u003cstrong\u003e\u003ccode\u003efalse\u003c/code\u003e\u003c/strong\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://datatracker.ietf.org/doc/html/rfc5892#appendix-A.1\" rel=\"nofollow\"\u003eContextJ\u003c/a\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e200C (�) ZERO WIDTH NON-JOINER\u003c/code\u003e (ZWNJ) is \u003cstrong\u003edisallowed everywhere\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e200D (�) ZERO WIDTH JOINER\u003c/code\u003e (ZWJ) is \u003cstrong\u003eonly allowed\u003c/strong\u003e in emoji sequences.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://datatracker.ietf.org/doc/html/rfc5892#appendix-A.3\" rel=\"nofollow\"\u003eContextO\u003c/a\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003eB7 (·) MIDDLE DOT\u003c/code\u003e is \u003cstrong\u003edisallowed\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e375 (͵) GREEK LOWER NUMERAL SIGN\u003c/code\u003e is \u003cstrong\u003edisallowed\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e5F3 (׳) HEBREW PUNCTUATION GERESH\u003c/code\u003e and \u003ccode\u003e5F4 (״) HEBREW PUNCTUATION GERSHAYIM\u003c/code\u003e are \u003cem\u003eGreek\u003c/em\u003e.\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e30FB (・) KATAKANA MIDDLE DOT\u003c/code\u003e is \u003cstrong\u003eFenced\u003c/strong\u003e and \u003cem\u003eHan\u003c/em\u003e, \u003cem\u003eJapanese\u003c/em\u003e, \u003cem\u003eKorean\u003c/em\u003e, and \u003cem\u003eBopomofo\u003c/em\u003e.\u003c/li\u003e\n\u003cli\u003eSome \u003ca href=\"https://en.wikipedia.org/wiki/Arabic_numerals\" rel=\"nofollow\"\u003eExtended Arabic Numerals\u003c/a\u003e are \u003cstrong\u003emapped\u003c/strong\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e6F0 (۰)\u003c/code\u003e → \u003ccode\u003e660 (٠) ARABIC-INDIC DIGIT ZERO\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e6F1 (۱)\u003c/code\u003e → \u003ccode\u003e661 (١) ARABIC-INDIC DIGIT ONE\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e6F2 (۲)\u003c/code\u003e → \u003ccode\u003e662 (٢) ARABIC-INDIC DIGIT TWO\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e6F3 (۳)\u003c/code\u003e → \u003ccode\u003e663 (٣) ARABIC-INDIC DIGIT THREE\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e6F7 (۷)\u003c/code\u003e → \u003ccode\u003e667 (٧) ARABIC-INDIC DIGIT SEVEN\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e6F8 (۸)\u003c/code\u003e → \u003ccode\u003e668 (٨) ARABIC-INDIC DIGIT EIGHT\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e6F9 (۹)\u003c/code\u003e → \u003ccode\u003e669 (٩) ARABIC-INDIC DIGIT NINE\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://datatracker.ietf.org/doc/html/rfc3492\" rel=\"nofollow\"\u003ePunycode\u003c/a\u003e is not decoded.\u003c/li\u003e\n\u003cli\u003eThe following ASCII characters are \u003cstrong\u003evalid\u003c/strong\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e24 ($) DOLLAR SIGN\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e5F (_) LOW LINE\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eOnly label separator is \u003ccode\u003e2E (.) FULL STOP\u003c/code\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eNo character maps to this character.\u003c/li\u003e\n\u003cli\u003eThis simplifies unnormalized name detection in unstructured text.\u003c/li\u003e\n\u003cli\u003eThe following alternatives are \u003cstrong\u003edisallowed\u003c/strong\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e3002 (。) IDEOGRAPHIC FULL STOP\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003eFF0E (．) FULLWIDTH FULL STOP\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003eFF61 (｡) HALFWIDTH IDEOGRAPHIC FULL STOP\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eMany characters are \u003cstrong\u003edisallowed\u003c/strong\u003e for \u003ca href=\"https://github.com/adraffy/ens-normalize.js/blob/20230221-stable/derive/rules/chars-disallow.js\"\u003evarious reasons\u003c/a\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eNearly all punctuation are \u003cstrong\u003edisallowed\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003eAll parentheses and brackets are \u003cstrong\u003edisallowed\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003eNearly all vocalization annotations are \u003cstrong\u003edisallowed\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003eObsolete, deprecated, and ancient characters are \u003cstrong\u003edisallowed\u003c/strong\u003e.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e463 (ѣ) CYRILLIC SMALL LETTER YAT\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eCombining, modifying, reversed, flipped, turned, and partial variations are \u003cstrong\u003edisallowed\u003c/strong\u003e.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e218A (↊) TURNED DIGIT TWO\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eWhen multiple weights of the same character exist, the variant closest to \"heavy\" is selected and the rest \u003cstrong\u003edisallowed\u003c/strong\u003e.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e🞡🞢🞣🞤✚🞥🞦🞧\u003c/code\u003e → \u003ccode\u003e271A (✚) HEAVY GREEK CROSS\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003eThis occasionally selects emoji.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eMany visually confusable characters are \u003cstrong\u003edisallowed\u003c/strong\u003e.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e131 (ı) LATIN SMALL LETTER DOTLESS I\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eMany ligatures, \u003cem\u003en\u003c/em\u003e-graphs, and \u003cem\u003en\u003c/em\u003e-grams are \u003cstrong\u003edisallowed.\u003c/strong\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003eA74F (ꝏ) LATIN SMALL LETTER OO\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eMany esoteric characters are \u003cstrong\u003edisallowed\u003c/strong\u003e.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e2376 (⍶) APL FUNCTIONAL SYMBOL ALPHA UNDERBAR\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eMany hyphen-like characters are \u003cstrong\u003emapped\u003c/strong\u003e to \u003ccode\u003e2D (-) HYPHEN-MINUS\u003c/code\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e2010 (‐) HYPHEN\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e2011 (‑) NON-BREAKING HYPHEN\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e2012 (‒) FIGURE DASH\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e2013 (–) EN DASH\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e2014 (—) EM DASH\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e2015 (―) HORIZONTAL BAR\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e2043 (⁃) HYPHEN BULLET\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e2212 (−) MINUS SIGN\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e23AF (⎯) HORIZONTAL LINE EXTENSION\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e23E4 (⏤) STRAIGHTNESS\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003eFE58 (﹘) SMALL EM DASH\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e2E3A (⸺) TWO-EM DASH\u003c/code\u003e → \u003ccode\u003e\"--\"\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e2E3B (⸻) THREE-EM DASH\u003c/code\u003e → \u003ccode\u003e\"---\"\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eCharacters are assigned to \u003cstrong\u003eGroups\u003c/strong\u003e according to \u003ca href=\"https://www.unicode.org/reports/tr24/#Script_Extensions_Def\" rel=\"nofollow\"\u003eUnicode Script_Extensions\u003c/a\u003e.\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eGroups\u003c/strong\u003e may contain \u003ca href=\"https://github.com/adraffy/ens-normalize.js/blob/20230221-stable/derive/rules/scripts.js\"\u003emultiple scripts\u003c/a\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eOnly \u003cem\u003eLatin\u003c/em\u003e, \u003cem\u003eGreek\u003c/em\u003e, \u003cem\u003eCyrillic\u003c/em\u003e, \u003cem\u003eHan\u003c/em\u003e, \u003cem\u003eJapanese\u003c/em\u003e, and \u003cem\u003eKorean\u003c/em\u003e have access to \u003cem\u003eCommon\u003c/em\u003e characters.\u003c/li\u003e\n\u003cli\u003e\u003cem\u003eLatin\u003c/em\u003e, \u003cem\u003eGreek\u003c/em\u003e, \u003cem\u003eCyrillic\u003c/em\u003e, \u003cem\u003eHan\u003c/em\u003e, \u003cem\u003eJapanese\u003c/em\u003e, \u003cem\u003eKorean\u003c/em\u003e, and \u003cem\u003eBopomofo\u003c/em\u003e only permit specific \u003cstrong\u003eCombining Mark\u003c/strong\u003e sequences.\u003c/li\u003e\n\u003cli\u003e\u003cem\u003eHan\u003c/em\u003e, \u003cem\u003eJapanese\u003c/em\u003e, and \u003cem\u003eKorean\u003c/em\u003e  have access to \u003ccode\u003ea-z\u003c/code\u003e.\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eRestricted\u003c/strong\u003e groups are always single-script.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eGroups\u003c/strong\u003e with multiple scripts are inspired from \u003ca href=\"https://www.unicode.org/reports/tr39/#Mixed_Script_Detection\" rel=\"nofollow\"\u003eUnicode augmented script sets\u003c/a\u003e.\u003c/li\u003e\n\u003cli\u003e\u003cem\u003eBraille\u003c/em\u003e, \u003cem\u003eLinear A\u003c/em\u003e, \u003cem\u003eLinear B\u003c/em\u003e, and \u003cem\u003eSignwriting\u003c/em\u003e scripts are \u003cstrong\u003edisallowed\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e27 (') APOSTROPHE\u003c/code\u003e is \u003cstrong\u003emapped\u003c/strong\u003e to \u003ccode\u003e2019 (’) RIGHT SINGLE QUOTATION MARK\u003c/code\u003e for convenience.\u003c/li\u003e\n\u003cli\u003eEthereum symbol (\u003ccode\u003e39E (Ξ) GREEK CAPITAL LETTER XI\u003c/code\u003e) is case-folded and \u003cem\u003eCommon\u003c/em\u003e.\u003c/li\u003e\n\u003cli\u003eEmoji sequences:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eAll sequences are \u003ca href=\"https://www.unicode.org/reports/tr51/#def_fully_qualified_emoji\" rel=\"nofollow\"\u003efully-qualified\u003c/a\u003e.\u003c/li\u003e\n\u003cli\u003eDigits (\u003ccode\u003e0-9\u003c/code\u003e) are \u003ca href=\"https://github.com/adraffy/ens-normalize.js/blob/20230221-stable/derive/rules/emoji.js#L28\"\u003enot emoji\u003c/a\u003e.\u003c/li\u003e\n\u003cli\u003eEmoji \u003ca href=\"https://github.com/adraffy/ens-normalize.js/blob/20230221-stable/derive/rules/emoji.js#L4\"\u003emapped to non-emoji by IDNA\u003c/a\u003e cannot be used as emoji.\u003c/li\u003e\n\u003cli\u003eEmoji \u003ca href=\"https://github.com/adraffy/ens-normalize.js/blob/20230221-stable/derive/rules/emoji.js#L46\"\u003edisallowed by IDNA\u003c/a\u003e and have default text-presentation are \u003cstrong\u003edisabled\u003c/strong\u003e:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e203C (‼️) double exclamation mark\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e2049 (⁉️) exclamation question mark \u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eRemaining \u003ccode\u003eEmoji\u003c/code\u003e characters are marked as \u003cstrong\u003edisallowed\u003c/strong\u003e (for text processing).\u003c/li\u003e\n\u003cli\u003eAll \u003ccode\u003eRGI_Emoji_ZWJ_Sequence\u003c/code\u003e are \u003cstrong\u003eenabled\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003eAll \u003ccode\u003eEmoji_Keycap_Sequence\u003c/code\u003e are \u003cstrong\u003eenabled\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003eAll \u003ccode\u003eRGI_Emoji_Tag_Sequence\u003c/code\u003e are \u003cstrong\u003eenabled\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003eAll \u003ccode\u003eRGI_Emoji_Modifier_Sequence\u003c/code\u003e are \u003cstrong\u003eenabled\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003eAll \u003ccode\u003eRGI_Emoji_Flag_Sequence\u003c/code\u003e are \u003cstrong\u003eenabled\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003eBasic_Emoji\u003c/code\u003e of the form \u003ccode\u003e[X FE0F]\u003c/code\u003e are \u003cstrong\u003eenabled\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003eEmoji\u003c/code\u003e with default emoji-presentation are \u003cstrong\u003eenabled\u003c/strong\u003e as \u003ccode\u003e[X FE0F]\u003c/code\u003e.\u003c/li\u003e\n\u003cli\u003eRemaining single-character \u003ccode\u003eEmoji\u003c/code\u003e are \u003cstrong\u003eenabled\u003c/strong\u003e as \u003ccode\u003e[X FE0F]\u003c/code\u003e (explicit emoji-styling).\u003c/li\u003e\n\u003cli\u003eAll singular \u003ca href=\"https://github.com/adraffy/ens-normalize.js/blob/20230221-stable/derive/rules/emoji.js#L64\"\u003eSkin-color Modifiers\u003c/a\u003e are \u003cstrong\u003edisabled\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003eAll singular \u003ca href=\"https://github.com/adraffy/ens-normalize.js/blob/20230221-stable/derive/rules/emoji.js#L74\"\u003eRegional Indicators\u003c/a\u003e are \u003cstrong\u003edisabled\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/adraffy/ens-normalize.js/blob/20230221-stable/derive/rules/emoji.js#L110\"\u003eBlacklisted emoji\u003c/a\u003e are \u003cstrong\u003edisabled\u003c/strong\u003e.\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/adraffy/ens-normalize.js/blob/20230221-stable/derive/rules/emoji.js#L116\"\u003eWhitelisted emoji\u003c/a\u003e are \u003cstrong\u003eenabled\u003c/strong\u003e.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eConfusables:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eEmoji are not confusable.\u003c/li\u003e\n\u003cli\u003eASCII confusables are case-folded.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eExample: \u003ccode\u003e61 (a) LATIN SMALL LETTER A\u003c/code\u003e confuses with \u003ccode\u003e13AA (Ꭺ) CHEROKEE LETTER GO\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eBackwards Compatibility\u003c/h2\u003e\u003ca id=\"user-content-backwards-compatibility\" class=\"anchor\" aria-label=\"Permalink: Backwards Compatibility\" href=\"#backwards-compatibility\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e99% of names are still valid.\u003c/li\u003e\n\u003cli\u003ePreserves as much IDNA and WhatWG URL compatibility as possible.\u003c/li\u003e\n\u003cli\u003eOnly valid emoji sequences are allowed.\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eSecurity Considerations\u003c/h2\u003e\u003ca id=\"user-content-security-considerations\" class=\"anchor\" aria-label=\"Permalink: Security Considerations\" href=\"#security-considerations\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eUnicode presentation may vary between applications and devices.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eUnicode text is ultimately subject to font-styling and display context.\u003c/li\u003e\n\u003cli\u003eUnsupported characters (\u003ccode\u003e�\u003c/code\u003e) may appear unremarkable.\u003c/li\u003e\n\u003cli\u003eUnsupported emoji sequences with ZWJ may appear indistinguishable from those without ZWJ.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eNames composed of labels with varying bidi properties may appear differently depending on context.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eNormalization does not enforce single-directional names.\u003c/li\u003e\n\u003cli\u003eNames may be composed of labels of different directions but normalized labels are never bidirectional.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eNot all normalized names are visually unambiguous.\u003c/li\u003e\n\u003cli\u003eThis ENSIP only addresses \u003cstrong\u003esingle-character\u003c/strong\u003e \u003ca href=\"https://www.unicode.org/reports/tr39/\" rel=\"nofollow\"\u003econfusables\u003c/a\u003e.\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eThere exist confusable-yet-distinct \u003cstrong\u003esingle-character\u003c/strong\u003e confusables:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e62 (b) LATIN SMALL LETTER B\u003c/code\u003e and \u003ccode\u003e13F4 (Ᏼ) CHEROKEE LETTER YV\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003eDF (ß) LATIN SMALL LETTER SHARP S\u003c/code\u003e and \u003ccode\u003e3B2 (β) GREEK SMALL LETTER BETA\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eThere exist confusable \u003cstrong\u003emulti-character\u003c/strong\u003e sequences:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e\"ஶ்ரீ\" [BB6 BCD BB0 BC0]\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e\"ஸ்ரீ\" [BB8 BCD BB0 BC0]\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eThere exist confusable \u003cstrong\u003eemoji\u003c/strong\u003e sequences:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003e🚴 [1F6B4]\u003c/code\u003e and \u003ccode\u003e🚴🏻 [1F6B4 1F3FB]\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e🇺🇸 [1F1FA 1F1F8]\u003c/code\u003e and \u003ccode\u003e🇺🇲 [1F1FA 1F1F2]\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003e♥ [2665] BLACK HEART SUIT\u003c/code\u003e and \u003ccode\u003e❤ [2764] HEAVY BLACK HEART\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eCopyright\u003c/h2\u003e\u003ca id=\"user-content-copyright\" class=\"anchor\" aria-label=\"Permalink: Copyright\" href=\"#copyright\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eCopyright and related rights waived via \u003ca href=\"https://creativecommons.org/publicdomain/zero/1.0/\" rel=\"nofollow\"\u003eCC0\u003c/a\u003e.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eAppendix: Reference Specifications\u003c/h2\u003e\u003ca id=\"user-content-appendix-reference-specifications\" class=\"anchor\" aria-label=\"Permalink: Appendix: Reference Specifications\" href=\"#appendix-reference-specifications\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"https://eips.ethereum.org/EIPS/eip-137\" rel=\"nofollow\"\u003eEIP-137: Ethereum Domain Name Service\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/ens-improvement-proposals/ensip-1-ens\"\u003eENSIP-1: ENS\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://unicode.org/reports/tr15/\" rel=\"nofollow\"\u003eUAX-15: Normalization Forms\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://www.unicode.org/reports/tr24/\" rel=\"nofollow\"\u003eUAX-24: Script Property\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://www.unicode.org/reports/tr31/\" rel=\"nofollow\"\u003eUAX-31: Identifier and Pattern Syntax\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://www.unicode.org/reports/tr39/\" rel=\"nofollow\"\u003eUTS-39: Security Mechanisms\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://unicode.org/reports/tr46/\" rel=\"nofollow\"\u003eUTS-46: IDNA Compatibility Processing\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://www.unicode.org/reports/tr51\" rel=\"nofollow\"\u003eUTS-51: Emoji\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://datatracker.ietf.org/doc/html/rfc3492\" rel=\"nofollow\"\u003eRFC-3492: Punycode\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://datatracker.ietf.org/doc/html/rfc5891\" rel=\"nofollow\"\u003eRFC-5891: IDNA: Protocol\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://datatracker.ietf.org/doc/html/rfc5892\" rel=\"nofollow\"\u003eRFC-5892: The Unicode Code Points and IDNA\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/unicode-org/cldr\"\u003eUnicode CLDR\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://url.spec.whatwg.org/#idna\" rel=\"nofollow\"\u003eWHATWG URL: IDNA\u003c/a\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eAppendix: Validation Tests\u003c/h2\u003e\u003ca id=\"user-content-appendix-validation-tests\" class=\"anchor\" aria-label=\"Permalink: Appendix: Validation Tests\" href=\"#appendix-validation-tests\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eA list of \u003ca href=\"/ensdomains/docs/blob/9edf9443de4333a0ea7ec658a870672d5d180d53/normalization-standard/tests.json\"\u003evalidation tests\u003c/a\u003e are provided with the following interpretation:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eAlready Normalized: \u003ccode\u003e{name: \"a\"}\u003c/code\u003e → \u003ccode\u003enormalize(\"a\")\u003c/code\u003e is \u003ccode\u003e\"a\"\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003eNeed Normalization: \u003ccode\u003e{name: \"A\", norm: \"a\"}\u003c/code\u003e → \u003ccode\u003enormalize(\"A\")\u003c/code\u003e is \u003ccode\u003e\"a\"\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003eExpect Error: \u003ccode\u003e{name: \"@\", error: true}\u003c/code\u003e → \u003ccode\u003enormalize(\"@\")\u003c/code\u003e throws\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eAnnex: Beautification\u003c/h2\u003e\u003ca id=\"user-content-annex-beautification\" class=\"anchor\" aria-label=\"Permalink: Annex: Beautification\" href=\"#annex-beautification\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eFollow \u003ca href=\"#algorithm\"\u003ealgorithm\u003c/a\u003e, except:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eDo not strip \u003ccode\u003eFE0F\u003c/code\u003e from \u003cstrong\u003eEmoji\u003c/strong\u003e tokens.\u003c/li\u003e\n\u003cli\u003eReplace \u003ccode\u003e3BE (ξ) GREEK SMALL LETTER XI\u003c/code\u003e with \u003ccode\u003e39E (Ξ) GREEK CAPITAL LETTER XI\u003c/code\u003e if the label isn't \u003cem\u003eGreek\u003c/em\u003e.\u003c/li\u003e\n\u003cli\u003eExample: \u003ccode\u003enormalize(\"‐Ξ1️⃣\") [2010 39E 31 FE0F 20E3]\u003c/code\u003e is \u003ccode\u003e\"-ξ1⃣\" [2D 3BE 31 20E3]\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003eExample: \u003ccode\u003ebeautify(\"-ξ1⃣\") [2D 3BE 31 20E3]\"\u003c/code\u003e is \u003ccode\u003e\"-Ξ1️⃣\" [2D 39E 31 FE0F 20E3]\u003c/code\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/article\u003e","renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":4,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"ENSIP-15: ENS Name Normalization Standard","kind":"section_1","ident_start":2,"ident_end":43,"extent_start":0,"extent_end":20212,"fully_qualified_name":"ENSIP-15: ENS Name Normalization Standard","ident_utf16":{"start":{"line_number":0,"utf16_col":2},"end":{"line_number":0,"utf16_col":43}},"extent_utf16":{"start":{"line_number":0,"utf16_col":0},"end":{"line_number":340,"utf16_col":0}}},{"name":"Abstract","kind":"section_2","ident_start":276,"ident_end":284,"extent_start":273,"extent_end":435,"fully_qualified_name":"Abstract","ident_utf16":{"start":{"line_number":7,"utf16_col":3},"end":{"line_number":7,"utf16_col":11}},"extent_utf16":{"start":{"line_number":7,"utf16_col":0},"end":{"line_number":11,"utf16_col":0}}},{"name":"Motivation","kind":"section_2","ident_start":438,"ident_end":448,"extent_start":435,"extent_end":1485,"fully_qualified_name":"Motivation","ident_utf16":{"start":{"line_number":11,"utf16_col":3},"end":{"line_number":11,"utf16_col":13}},"extent_utf16":{"start":{"line_number":11,"utf16_col":0},"end":{"line_number":25,"utf16_col":0}}},{"name":"Specification","kind":"section_2","ident_start":1488,"ident_end":1501,"extent_start":1485,"extent_end":7398,"fully_qualified_name":"Specification","ident_utf16":{"start":{"line_number":25,"utf16_col":3},"end":{"line_number":25,"utf16_col":16}},"extent_utf16":{"start":{"line_number":25,"utf16_col":0},"end":{"line_number":138,"utf16_col":0}}},{"name":"Versioning","kind":"section_3","ident_start":1509,"ident_end":1519,"extent_start":1505,"extent_end":1808,"fully_qualified_name":"Versioning","ident_utf16":{"start":{"line_number":27,"utf16_col":4},"end":{"line_number":27,"utf16_col":14}},"extent_utf16":{"start":{"line_number":27,"utf16_col":0},"end":{"line_number":32,"utf16_col":0}}},{"name":"Algorithm","kind":"section_3","ident_start":1812,"ident_end":1821,"extent_start":1808,"extent_end":2483,"fully_qualified_name":"Algorithm","ident_utf16":{"start":{"line_number":32,"utf16_col":4},"end":{"line_number":32,"utf16_col":13}},"extent_utf16":{"start":{"line_number":32,"utf16_col":0},"end":{"line_number":44,"utf16_col":0}}},{"name":"Normalize","kind":"section_3","ident_start":2487,"ident_end":2496,"extent_start":2483,"extent_end":2989,"fully_qualified_name":"Normalize","ident_utf16":{"start":{"line_number":44,"utf16_col":4},"end":{"line_number":44,"utf16_col":13}},"extent_utf16":{"start":{"line_number":44,"utf16_col":0},"end":{"line_number":55,"utf16_col":0}}},{"name":"Tokenize","kind":"section_3","ident_start":2993,"ident_end":3001,"extent_start":2989,"extent_end":4150,"fully_qualified_name":"Tokenize","ident_utf16":{"start":{"line_number":55,"utf16_col":4},"end":{"line_number":55,"utf16_col":12}},"extent_utf16":{"start":{"line_number":55,"utf16_col":0},"end":{"line_number":78,"utf16_col":0}}},{"name":"Validate","kind":"section_3","ident_start":4154,"ident_end":4162,"extent_start":4150,"extent_end":5559,"fully_qualified_name":"Validate","ident_utf16":{"start":{"line_number":78,"utf16_col":4},"end":{"line_number":78,"utf16_col":12}},"extent_utf16":{"start":{"line_number":78,"utf16_col":0},"end":{"line_number":109,"utf16_col":0}}},{"name":"Wholes","kind":"section_3","ident_start":5563,"ident_end":5569,"extent_start":5559,"extent_end":7398,"fully_qualified_name":"Wholes","ident_utf16":{"start":{"line_number":109,"utf16_col":4},"end":{"line_number":109,"utf16_col":10}},"extent_utf16":{"start":{"line_number":109,"utf16_col":0},"end":{"line_number":138,"utf16_col":0}}},{"name":"Description of `spec.json`","kind":"section_2","ident_start":7401,"ident_end":7427,"extent_start":7398,"extent_end":10052,"fully_qualified_name":"Description of `spec.json`","ident_utf16":{"start":{"line_number":138,"utf16_col":3},"end":{"line_number":138,"utf16_col":29}},"extent_utf16":{"start":{"line_number":138,"utf16_col":0},"end":{"line_number":172,"utf16_col":0}}},{"name":"Derivation","kind":"section_2","ident_start":10055,"ident_end":10065,"extent_start":10052,"extent_end":16840,"fully_qualified_name":"Derivation","ident_utf16":{"start":{"line_number":172,"utf16_col":3},"end":{"line_number":172,"utf16_col":13}},"extent_utf16":{"start":{"line_number":172,"utf16_col":0},"end":{"line_number":276,"utf16_col":0}}},{"name":"Backwards Compatibility","kind":"section_2","ident_start":16843,"ident_end":16866,"extent_start":16840,"extent_end":17016,"fully_qualified_name":"Backwards Compatibility","ident_utf16":{"start":{"line_number":276,"utf16_col":3},"end":{"line_number":276,"utf16_col":26}},"extent_utf16":{"start":{"line_number":276,"utf16_col":0},"end":{"line_number":282,"utf16_col":0}}},{"name":"Security Considerations","kind":"section_2","ident_start":17019,"ident_end":17042,"extent_start":17016,"extent_end":18367,"fully_qualified_name":"Security Considerations","ident_utf16":{"start":{"line_number":282,"utf16_col":3},"end":{"line_number":282,"utf16_col":26}},"extent_utf16":{"start":{"line_number":282,"utf16_col":0},"end":{"line_number":304,"utf16_col":0}}},{"name":"Copyright","kind":"section_2","ident_start":18370,"ident_end":18379,"extent_start":18367,"extent_end":18485,"fully_qualified_name":"Copyright","ident_utf16":{"start":{"line_number":304,"utf16_col":3},"end":{"line_number":304,"utf16_col":12}},"extent_utf16":{"start":{"line_number":304,"utf16_col":0},"end":{"line_number":308,"utf16_col":0}}},{"name":"Appendix: Reference Specifications","kind":"section_2","ident_start":18488,"ident_end":18522,"extent_start":18485,"extent_end":19425,"fully_qualified_name":"Appendix: Reference Specifications","ident_utf16":{"start":{"line_number":308,"utf16_col":3},"end":{"line_number":308,"utf16_col":37}},"extent_utf16":{"start":{"line_number":308,"utf16_col":0},"end":{"line_number":324,"utf16_col":0}}},{"name":"Appendix: Validation Tests","kind":"section_2","ident_start":19428,"ident_end":19454,"extent_start":19425,"extent_end":19795,"fully_qualified_name":"Appendix: Validation Tests","ident_utf16":{"start":{"line_number":324,"utf16_col":3},"end":{"line_number":324,"utf16_col":29}},"extent_utf16":{"start":{"line_number":324,"utf16_col":0},"end":{"line_number":332,"utf16_col":0}}},{"name":"Annex: Beautification","kind":"section_2","ident_start":19798,"ident_end":19819,"extent_start":19795,"extent_end":20212,"fully_qualified_name":"Annex: Beautification","ident_utf16":{"start":{"line_number":332,"utf16_col":3},"end":{"line_number":332,"utf16_col":24}},"extent_utf16":{"start":{"line_number":332,"utf16_col":0},"end":{"line_number":340,"utf16_col":0}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"copilotSpacesEnabled":false,"modelsAccessAllowed":false,"modelsRepoIntegrationEnabled":false,"isMarketplaceEnabled":true,"csrf_tokens":{"/ensdomains/docs/branches":{"post":"hoAPJ5MNv9mr3WsPZc7vitDv8RCg1_smuf0KGON0zR0lLYH4JDkoFL6V_YnfN6Chbc1QKUT-ppycctHQ4aw4Gw"},"/repos/preferences":{"post":"JsJnwp4XHuFDpGzZPFqoeR5vfbv_UAajDqpWeZ2Sopo70pgr3d1F1yYzNbP0XSN-NH4g5x-x7NZlpy3-rcP6Wg"}}},"title":"docs/ens-improvement-proposals/ensip-15-normalization-standard.md at 9edf9443de4333a0ea7ec658a870672d5d180d53 · ensdomains/docs","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-0cea8c6113ab.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-105a4a160ddd.js","githubDevUrl":null,"enabled_features":{"code_nav_ui_events":false,"react_blob_overlay":false,"accessible_code_button":true}}}</script>
  <div data-target="react-app.reactRoot"></div>
</react-app>
</turbo-frame>



  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo" >
  <h2 class='sr-only'>Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="GitHub Homepage" class="footer-octicon mr-2" href="https://github.com">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
</a>
      <span>
        &copy; 2025 GitHub,&nbsp;Inc.
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
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
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


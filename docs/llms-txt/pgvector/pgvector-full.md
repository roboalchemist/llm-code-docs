# Pgvector Documentation

Source: https://pgvector.dev/llms-full.txt

---








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

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light-dac525bbd821.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light_high_contrast-56ccf4057897.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark-784387e86ac0.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark_high_contrast-79bd5fd84a86.css" /><link data-color-theme="light" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light-dac525bbd821.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-56ccf4057897.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-0e24752a7d2b.css" /><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-412af2517363.css" /><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-6186e83663dc.css" /><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-9d33c7aea2e7.css" /><link data-color-theme="dark" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark-784387e86ac0.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-79bd5fd84a86.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-75db11311555.css" /><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-f2c1045899a2.css" /><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-f46d293c6ff3.css" /><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-e4b5684db29d.css" /><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-72c58078e707.css" /><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-956cb5dfcb85.css" />

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-primitives-c37d781e2da5.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-8bf3328b2828.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-df4c2156a48b.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/github-f7230554fa20.css" />
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/repository-5d735668c600.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-9c9b8dc61e74.css" />

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["a11y_status_checks_ruleset","actions_custom_images_public_preview_visibility","actions_custom_images_storage_billing_ui_visibility","actions_enable_snapshot_keyword","actions_image_version_event","allow_react_navs_in_turbo","alternate_user_config_repo","api_insights_show_missing_data_banner","arianotify_comprehensive_migration","arianotify_partial_migration","client_version_header","codespaces_prebuild_region_target_update","coding_agent_model_selection","contentful_lp_footnotes","copilot_agent_cli_public_preview","copilot_agent_sessions_alive_updates","copilot_agent_task_list_v2","copilot_agent_tasks_btn_code_nav","copilot_agent_tasks_btn_code_view","copilot_agent_tasks_btn_code_view_lines","copilot_agent_tasks_btn_repo","copilot_api_agentic_issue_marshal_yaml","copilot_api_draft_issue_reference_with_project_id","copilot_api_github_draft_update_issue_skill","copilot_chat_agents_empty_state","copilot_chat_attach_multiple_images","copilot_chat_clear_model_selection_for_default_change","copilot_chat_file_redirect","copilot_chat_input_commands","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_coding_agent_task_response","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_hide_in_dotcom_chat","copilot_extensions_removal_on_marketplace","copilot_features_raycast_logo","copilot_file_block_ref_matching","copilot_ftp_hyperspace_upgrade_prompt","copilot_icebreakers_experiment_dashboard","copilot_icebreakers_experiment_hyperspace","copilot_immersive_generate_thread_name_async","copilot_immersive_job_result_preview","copilot_immersive_structured_model_picker","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_org_policy_page_focus_mode","copilot_redirect_header_button_to_agents","copilot_security_alert_assignee_options","copilot_share_active_subthread","copilot_spaces_ga","copilot_spaces_individual_policies_ga","copilot_spaces_public_access_to_user_owned_spaces","copilot_spaces_read_access_to_user_owned_spaces","copilot_spaces_report_abuse","copilot_spark_empty_state","copilot_spark_handle_nil_friendly_name","copilot_spark_loading_webgl","copilot_stable_conversation_view","copilot_swe_agent_progress_commands","copilot_swe_agent_use_subagents","copilot_unconfigured_is_inherited","dashboard_universe_2025_feedback_dialog","direct_to_salesforce","dom_node_counts","dotcom_chat_client_side_skills","enterprise_ai_controls","failbot_report_error_react_apps_on_page","fetch_graphql_improved_error_serialization","flex_cta_groups_mvp","global_nav_react_edit_status_dialog","global_nav_react_feature_preview","global_nav_react_teams_settings_page","global_nav_react_top_repos_api_caching","hyperspace_2025_logged_out_batch_1","initial_per_page_pagination_updates","issue_fields_global_search","issue_fields_report_usage","issue_fields_timeline_events","issues_cca_assign_actor_with_agent","issues_expanded_file_types","issues_lazy_load_comment_box_suggestions","issues_react_bots_timeline_pagination","issues_react_chrome_container_query_fix","issues_react_client_side_caching_analytics","issues_react_prohibit_title_fallback","issues_report_sidebar_interactions","lifecycle_label_name_updates","link_contact_sales_swp_marketo","marketing_pages_search_explore_provider","memex_default_issue_create_repository","memex_grouped_by_edit_route","memex_mwl_filter_field_delimiter","mission_control_use_body_html","new_traffic_page_banner","open_agent_session_in_vscode_insiders","open_agent_session_in_vscode_stable","projects_assignee_max_limit","react_compiler_markdown_editor","react_custom_partial_router","react_fetch_graphql_ignore_expected_errors","render_user_display_name","repo_traffic_job","repos_insights_remove_new_url","ruleset_deletion_confirmation","sample_network_conn_type","scheduled_reminders_updated_limits","site_calculator_actions_2025","site_features_copilot_universe","site_homepage_collaborate_video","site_homepage_contentful","site_homepage_eyebrow_banner","site_homepage_universe_animations","site_msbuild_webgl_hero","spark_prompt_secret_scanning","swe_agent_member_requests","viewscreen_sandbox","webp_support","workbench_store_readonly"],"copilotApiOverrideUrl":"https://api.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/high-contrast-cookie-ff2c933fbe48.js"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/wp-runtime-496a4036f910.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/913-ca2305638c53.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/6488-de87864e6818.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/environment-b3d48626cc6e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/69676-3e4d0020216a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/43784-4652ae97a661.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/4712-6fc930a63a4b.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81028-5b8c5e07a4fa.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/97292-9890ce009c4e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/91853-2ed22fb46437.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/78143-31968346cf4c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/52430-2f44a4a36933.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/github-elements-8b5d9b8ccf1f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/element-registry-00f71b57ac82.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-lib-760965ba27bb.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-core-c947eff3bbc1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/28546-ee41c9313871.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/17688-a9e16fb5ed13.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2869-a4ba8f17edb3.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/70191-5122bf27bf3e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/7332-5ea4ccf72018.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/3561-5983d983527e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/24077-adc459723b71.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/51519-d3c416bc1076.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/27376-9825e0a74a24.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/96384-750ef5263abe.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/19718-676a65610616.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-e7ce3c2fbd67.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/48011-1f20a5c80dd7.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/notifications-global-54f7f2032e0d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/39713-8508e9483898.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/45688-b093405a7bf6.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/90787-3d665c8ee86e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/5903-3cd556b5e9d3.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/codespaces-5b6c0f0d4ee9.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/23387-1b12da426b92.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/72568-b0582cf2bbee.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/13974-18aebd0d0d21.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/14155-c583ca76c604.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/repositories-37aa1111d71f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/31615-236504c8966f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/code-menu-fa1d4025778b.js" defer="defer"></script>
  
  <script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/primer-react-4e701c638f8d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/octicons-react-a215e6ee021a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/31475-5e512a21dfc3.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/48775-3cc79d2cd30e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/42892-341e79a04903.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/23832-db66abd83e08.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/9288-386d049b3200.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/57972-df59401b9643.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/notifications-subscriptions-menu-d002081209f2.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.47239ec6cbe68138fe4c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/notifications-subscriptions-menu.933100a30c03fd4e8ae4.module.css" />

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.47239ec6cbe68138fe4c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/notifications-subscriptions-menu.933100a30c03fd4e8ae4.module.css" />


  <title>GitHub - supabase-community/chatgpt-your-files: Production-ready MVP for securely chatting with your documents using pgvector</title>



  <meta name="route-pattern" content="/:user_id/:repository" data-turbo-transient>
  <meta name="route-controller" content="files" data-turbo-transient>
  <meta name="route-action" content="disambiguate" data-turbo-transient>
  <meta name="fetch-nonce" content="v2:fc902795-443c-4768-14bd-518a2dc3c13e">

    
  <meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb">


  <meta name="request-id" content="D578:173A0B:2B33BB26:2D744304:69556BF5" data-pjax-transient="true"/><meta name="html-safe-nonce" content="02c91723c54bcd3d89eb11cda82003fbfbd16aeb8f552113684da03683787285" data-pjax-transient="true"/><meta name="visitor-payload" content="eyJyZWZlcnJlciI6IiIsInJlcXVlc3RfaWQiOiJENTc4OjE3M0EwQjoyQjMzQkIyNjoyRDc0NDMwNDo2OTU1NkJGNSIsInZpc2l0b3JfaWQiOiI2MTg2MzgyNTIwNDAzNTA3MDkiLCJyZWdpb25fZWRnZSI6InNlYSIsInJlZ2lvbl9yZW5kZXIiOiJzZWEifQ==" data-pjax-transient="true"/><meta name="visitor-hmac" content="1d87d70abed39e6a6313c20f2ca9e6081cbd0b0301f5f2950686cc4157b25743" data-pjax-transient="true"/>


    <meta name="hovercard-subject-tag" content="repository:701867516" data-turbo-transient>


  <meta name="github-keyboard-shortcuts" content="repository,copilot" data-turbo-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-turbo-transient>
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;" data-turbo-transient="true" />

  




    <meta name="user-login" content="">

  

    <meta name="viewport" content="width=device-width">

    

      <meta name="description" content="Production-ready MVP for securely chatting with your documents using pgvector - supabase-community/chatgpt-your-files">

      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">

    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/supabase-community/chatgpt-your-files" />

      <meta name="twitter:image" content="https://opengraph.githubassets.com/efbcb0f30cd23c49e7e8ca9798e7bd53014e5331dcf05b0032d9e8115e14dfd6/supabase-community/chatgpt-your-files" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="GitHub - supabase-community/chatgpt-your-files: Production-ready MVP for securely chatting with your documents using pgvector" /><meta name="twitter:description" content="Production-ready MVP for securely chatting with your documents using pgvector - supabase-community/chatgpt-your-files" />
  <meta property="og:image" content="https://opengraph.githubassets.com/efbcb0f30cd23c49e7e8ca9798e7bd53014e5331dcf05b0032d9e8115e14dfd6/supabase-community/chatgpt-your-files" /><meta property="og:image:alt" content="Production-ready MVP for securely chatting with your documents using pgvector - supabase-community/chatgpt-your-files" /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="GitHub - supabase-community/chatgpt-your-files: Production-ready MVP for securely chatting with your documents using pgvector" /><meta property="og:url" content="https://github.com/supabase-community/chatgpt-your-files" /><meta property="og:description" content="Production-ready MVP for securely chatting with your documents using pgvector - supabase-community/chatgpt-your-files" />
  




      <meta name="hostname" content="github.com">



        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="f7309bf0db674e9bdb7027f72caea451006cd9189ed4c4aa3a51229b8dcff3f0" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="21a43568025709b66240454fc92d4f09335a96863f8ab1c46b4a07f6a5b67102" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="03da391a01750e54015d0ebd9e7e968879f966ef76d8a697be72ccbc12abac55" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="d160f22ceda8d5f47865c85a7e7d2e666a68c4355b920de2105a2db9931f8b97" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta data-hydrostats="publish">
  <meta name="go-import" content="github.com/supabase-community/chatgpt-your-files git https://github.com/supabase-community/chatgpt-your-files.git">

  <meta name="octolytics-dimension-user_id" content="87650496" /><meta name="octolytics-dimension-user_login" content="supabase-community" /><meta name="octolytics-dimension-repository_id" content="701867516" /><meta name="octolytics-dimension-repository_nwo" content="supabase-community/chatgpt-your-files" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="701867516" /><meta name="octolytics-dimension-repository_network_root_nwo" content="supabase-community/chatgpt-your-files" />



      <link rel="canonical" href="https://github.com/supabase-community/chatgpt-your-files" data-turbo-transient>


    <meta name="turbo-body-classes" content="logged-out env-production page-responsive">
  <meta name="disable-turbo" content="false">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="release" content="06fa20ea1477abb0b8a8fd9ad0efced9a2f203e9">
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
      <a href="#start-of-content" data-skip-target-assigned="false" class="px-2 py-4 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.47239ec6cbe68138fe4c.module.css" />
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





      

          

              
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/43862-5c4df3ba1119.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/85110-f7be2f54525a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/sessions-36ef208f2f57.js" defer="defer"></script>

<style>
  /* Override primer focus outline color for marketing header dropdown links for better contrast */
  [data-color-mode="light"] .HeaderMenu-dropdown-link:focus-visible,
  [data-color-mode="light"] .HeaderMenu-trailing-link a:focus-visible {
    outline-color: var(--color-accent-fg);
  }
</style>

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
            href="/login?return_to=https%3A%2F%2Fgithub.com%2Fsupabase-community%2Fchatgpt-your-files"
            class="HeaderMenu-link HeaderMenu-button d-inline-flex f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit js-prevent-focus-on-mobile-nav"
            data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/supabase-community/chatgpt-your-files&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="b28131c32098a2843a445fdc61c1c73d2cd9ce9b44398a43a8138f21f5712bba"
            data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to Sign in&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}"
          >
            Sign in
          </a>
              <div class="AppHeader-appearanceSettings">
    <react-partial-anchor>
      <button data-target="react-partial-anchor.anchor" id="icon-button-54da0285-81cd-4d4d-9e38-932cecd23ef9" aria-labelledby="tooltip-105ddd47-bff6-42b2-a68b-9c0083e8fe7c" type="button" disabled="disabled" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium AppHeader-button HeaderMenu-link border cursor-wait">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sliders Button-visual">
    <path d="M15 2.75a.75.75 0 0 1-.75.75h-4a.75.75 0 0 1 0-1.5h4a.75.75 0 0 1 .75.75Zm-8.5.75v1.25a.75.75 0 0 0 1.5 0v-4a.75.75 0 0 0-1.5 0V2H1.75a.75.75 0 0 0 0 1.5H6.5Zm1.25 5.25a.75.75 0 0 0 0-1.5h-6a.75.75 0 0 0 0 1.5h6ZM15 8a.75.75 0 0 1-.75.75H11.5V10a.75.75 0 1 1-1.5 0V6a.75.75 0 0 1 1.5 0v1.25h2.75A.75.75 0 0 1 15 8Zm-9 5.25v-2a.75.75 0 0 0-1.5 0v1.25H1.75a.75.75 0 0 0 0 1.5H4.5v1.25a.75.75 0 0 0 1.5 0v-2Zm9 0a.75.75 0 0 1-.75.75h-6a.75.75 0 0 1 0-1.5h6a.75.75 0 0 1 .75.75Z"></path>
</svg>
</button><tool-tip id="tooltip-105ddd47-bff6-42b2-a68b-9c0083e8fe7c" for="icon-button-54da0285-81cd-4d4d-9e38-932cecd23ef9" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Appearance settings</tool-tip>

      <template data-target="react-partial-anchor.template">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.47239ec6cbe68138fe4c.module.css" />
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
            <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.47239ec6cbe68138fe4c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/marketing-navigation.8284bdfe1ee4804a58c1.module.css" />

<react-partial
  partial-name="marketing-navigation"
  data-ssr="true"
  data-attempted-ssr="true"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"should_use_dotcom_links":true}}</script>
  <div data-target="react-partial.reactRoot"><nav class="MarketingNavigation-module__nav--jA9Zq" aria-label="Global"><ul class="MarketingNavigation-module__list--r_vr2"><li><div class="NavDropdown-module__container--bmXM2 js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button--Hq9UR js-details-target" aria-expanded="false">Platform<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon--SR0Ke" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown--Ig57Y"><ul class="NavDropdown-module__list--RwSSK"><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">AI CODE CREATION</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/features/copilot" data-analytics-event="{&quot;action&quot;:&quot;github_copilot&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_copilot_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path></svg><span class="NavLink-module__title--xw3ok">GitHub Copilot</span><span class="NavLink-module__subtitle--qC15H">Write better code with AI</span></div></a></li><li><a href="https://github.com/features/spark" data-analytics-event="{&quot;action&quot;:&quot;github_spark&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_spark_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-sparkle-fill NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.296 1.924c.24-.656 1.168-.656 1.408 0l.717 1.958a11.25 11.25 0 0 0 6.697 6.697l1.958.717c.657.24.657 1.168 0 1.408l-1.958.717a11.25 11.25 0 0 0-6.697 6.697l-.717 1.958c-.24.657-1.168.657-1.408 0l-.717-1.958a11.25 11.25 0 0 0-6.697-6.697l-1.958-.717c-.656-.24-.656-1.168 0-1.408l1.958-.717a11.25 11.25 0 0 0 6.697-6.697l.717-1.958Z"></path></svg><span class="NavLink-module__title--xw3ok">GitHub Spark</span><span class="NavLink-module__subtitle--qC15H">Build and deploy intelligent apps</span></div></a></li><li><a href="https://github.com/features/models" data-analytics-event="{&quot;action&quot;:&quot;github_models&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_models_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-ai-model NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M19.375 8.5a3.25 3.25 0 1 1-3.163 4h-3a3.252 3.252 0 0 1-4.443 2.509L7.214 17.76a3.25 3.25 0 1 1-1.342-.674l1.672-2.957A3.238 3.238 0 0 1 6.75 12c0-.907.371-1.727.97-2.316L6.117 6.846A3.253 3.253 0 0 1 1.875 3.75a3.25 3.25 0 1 1 5.526 2.32l1.603 2.836A3.25 3.25 0 0 1 13.093 11h3.119a3.252 3.252 0 0 1 3.163-2.5ZM10 10.25a1.75 1.75 0 1 0-.001 3.499A1.75 1.75 0 0 0 10 10.25ZM5.125 2a1.75 1.75 0 1 0 0 3.5 1.75 1.75 0 0 0 0-3.5Zm12.5 9.75a1.75 1.75 0 1 0 3.5 0 1.75 1.75 0 0 0-3.5 0Zm-14.25 8.5a1.75 1.75 0 1 0 3.501-.001 1.75 1.75 0 0 0-3.501.001Z"></path></svg><span class="NavLink-module__title--xw3ok">GitHub Models</span><span class="NavLink-module__subtitle--qC15H">Manage and compare prompts</span></div></a></li><li><a href="https://github.com/mcp" data-analytics-event="{&quot;action&quot;:&quot;mcp_registry&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;mcp_registry_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-mcp NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.795 1.694a4.287 4.287 0 0 1 6.061 0 4.28 4.28 0 0 1 1.181 3.819 4.282 4.282 0 0 1 3.819 1.181 4.287 4.287 0 0 1 0 6.061l-6.793 6.793a.249.249 0 0 0 0 .353l2.617 2.618a.75.75 0 1 1-1.061 1.061l-2.617-2.618a1.75 1.75 0 0 1 0-2.475l6.793-6.793a2.785 2.785 0 1 0-3.939-3.939l-5.9 5.9a.734.734 0 0 1-.249.165.749.749 0 0 1-.812-1.225l5.9-5.901a2.785 2.785 0 1 0-3.939-3.939L2.931 10.68A.75.75 0 1 1 1.87 9.619l7.925-7.925Z"></path><path d="M12.42 4.069a.752.752 0 0 1 1.061 0 .752.752 0 0 1 0 1.061L7.33 11.28a2.788 2.788 0 0 0 0 3.94 2.788 2.788 0 0 0 3.94 0l6.15-6.151a.752.752 0 0 1 1.061 0 .752.752 0 0 1 0 1.061l-6.151 6.15a4.285 4.285 0 1 1-6.06-6.06l6.15-6.151Z"></path></svg><span class="NavLink-module__title--xw3ok">MCP Registry<sup class="NavLink-module__label--MrIhm">New</sup></span><span class="NavLink-module__subtitle--qC15H">Integrate external tools</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">DEVELOPER WORKFLOWS</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/features/actions" data-analytics-event="{&quot;action&quot;:&quot;actions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;actions_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-workflow NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 3a2 2 0 0 1 2-2h6.5a2 2 0 0 1 2 2v6.5a2 2 0 0 1-2 2H7v4.063C7 16.355 7.644 17 8.438 17H12.5v-2.5a2 2 0 0 1 2-2H21a2 2 0 0 1 2 2V21a2 2 0 0 1-2 2h-6.5a2 2 0 0 1-2-2v-2.5H8.437A2.939 2.939 0 0 1 5.5 15.562V11.5H3a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v6.5a.5.5 0 0 0 .5.5h6.5a.5.5 0 0 0 .5-.5V3a.5.5 0 0 0-.5-.5ZM14.5 14a.5.5 0 0 0-.5.5V21a.5.5 0 0 0 .5.5H21a.5.5 0 0 0 .5-.5v-6.5a.5.5 0 0 0-.5-.5Z"></path></svg><span class="NavLink-module__title--xw3ok">Actions</span><span class="NavLink-module__subtitle--qC15H">Automate any workflow</span></div></a></li><li><a href="https://github.com/features/codespaces" data-analytics-event="{&quot;action&quot;:&quot;codespaces&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;codespaces_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-codespaces NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.5 3.75C3.5 2.784 4.284 2 5.25 2h13.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 18.75 13H5.25a1.75 1.75 0 0 1-1.75-1.75Zm-2 12c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v4a1.75 1.75 0 0 1-1.75 1.75H3.25a1.75 1.75 0 0 1-1.75-1.75ZM5.25 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h13.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Zm-2 12a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h17.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25Z"></path><path d="M10 17.75a.75.75 0 0 1 .75-.75h6.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path></svg><span class="NavLink-module__title--xw3ok">Codespaces</span><span class="NavLink-module__subtitle--qC15H">Instant dev environments</span></div></a></li><li><a href="https://github.com/features/issues" data-analytics-event="{&quot;action&quot;:&quot;issues&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;issues_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M12 1c6.075 0 11 4.925 11 11s-4.925 11-11 11S1 18.075 1 12 5.925 1 12 1ZM2.5 12a9.5 9.5 0 0 0 9.5 9.5 9.5 9.5 0 0 0 9.5-9.5A9.5 9.5 0 0 0 12 2.5 9.5 9.5 0 0 0 2.5 12Zm9.5 2a2 2 0 1 1-.001-3.999A2 2 0 0 1 12 14Z"></path></svg><span class="NavLink-module__title--xw3ok">Issues</span><span class="NavLink-module__subtitle--qC15H">Plan and track work</span></div></a></li><li><a href="https://github.com/features/code-review" data-analytics-event="{&quot;action&quot;:&quot;code_review&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;code_review_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-code NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M15.22 4.97a.75.75 0 0 1 1.06 0l6.5 6.5a.75.75 0 0 1 0 1.06l-6.5 6.5a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L21.19 12l-5.97-5.97a.75.75 0 0 1 0-1.06Zm-6.44 0a.75.75 0 0 1 0 1.06L2.81 12l5.97 5.97a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-6.5-6.5a.75.75 0 0 1 0-1.06l6.5-6.5a.75.75 0 0 1 1.06 0Z"></path></svg><span class="NavLink-module__title--xw3ok">Code Review</span><span class="NavLink-module__subtitle--qC15H">Manage code changes</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">APPLICATION SECURITY</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/security/advanced-security" data-analytics-event="{&quot;action&quot;:&quot;github_advanced_security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_advanced_security_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-shield-check NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path></svg><span class="NavLink-module__title--xw3ok">GitHub Advanced Security</span><span class="NavLink-module__subtitle--qC15H">Find and fix vulnerabilities</span></div></a></li><li><a href="https://github.com/security/advanced-security/code-security" data-analytics-event="{&quot;action&quot;:&quot;code_security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;code_security_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-code-square NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.3 8.24a.75.75 0 0 1-.04 1.06L7.352 12l2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M2 3.75C2 2.784 2.784 2 3.75 2h16.5c.966 0 1.75.784 1.75 1.75v16.5A1.75 1.75 0 0 1 20.25 22H3.75A1.75 1.75 0 0 1 2 20.25Zm1.75-.25a.25.25 0 0 0-.25.25v16.5c0 .138.112.25.25.25h16.5a.25.25 0 0 0 .25-.25V3.75a.25.25 0 0 0-.25-.25Z"></path></svg><span class="NavLink-module__title--xw3ok">Code security</span><span class="NavLink-module__subtitle--qC15H">Secure your code as you build</span></div></a></li><li><a href="https://github.com/security/advanced-security/secret-protection" data-analytics-event="{&quot;action&quot;:&quot;secret_protection&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;secret_protection_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-lock NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6 9V7.25C6 3.845 8.503 1 12 1s6 2.845 6 6.25V9h.5a2.5 2.5 0 0 1 2.5 2.5v8a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 19.5v-8A2.5 2.5 0 0 1 5.5 9Zm-1.5 2.5v8a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1v-8a1 1 0 0 0-1-1h-13a1 1 0 0 0-1 1Zm3-4.25V9h9V7.25c0-2.67-1.922-4.75-4.5-4.75-2.578 0-4.5 2.08-4.5 4.75Z"></path></svg><span class="NavLink-module__title--xw3ok">Secret protection</span><span class="NavLink-module__subtitle--qC15H">Stop leaks before they start</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group--T925n NavGroup-module__hasSeparator--AJeNz"><span class="NavGroup-module__title--TdKyz">EXPLORE</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/why-github" data-analytics-event="{&quot;action&quot;:&quot;why_github&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;why_github_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Why GitHub</span></a></li><li><a href="https://docs.github.com" data-analytics-event="{&quot;action&quot;:&quot;documentation&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;documentation_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB" target="_blank" rel="noreferrer"><span class="NavLink-module__title--xw3ok">Documentation</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon--JurQ9" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.blog" data-analytics-event="{&quot;action&quot;:&quot;blog&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;blog_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB" target="_blank" rel="noreferrer"><span class="NavLink-module__title--xw3ok">Blog</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon--JurQ9" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.blog/changelog" data-analytics-event="{&quot;action&quot;:&quot;changelog&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;changelog_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB" target="_blank" rel="noreferrer"><span class="NavLink-module__title--xw3ok">Changelog</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon--JurQ9" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.com/marketplace" data-analytics-event="{&quot;action&quot;:&quot;marketplace&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;marketplace_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Marketplace</span></a></li></ul></div></li></ul><div class="NavDropdown-module__trailingLinkContainer--MNB5T"><a href="https://github.com/features" data-analytics-event="{&quot;action&quot;:&quot;view_all_features&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_features_link_platform_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">View all features</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon--g6Lip" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></div></div></div></li><li><div class="NavDropdown-module__container--bmXM2 js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button--Hq9UR js-details-target" aria-expanded="false">Solutions<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon--SR0Ke" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown--Ig57Y"><ul class="NavDropdown-module__list--RwSSK"><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">BY COMPANY SIZE</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/enterprise" data-analytics-event="{&quot;action&quot;:&quot;enterprises&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;enterprises_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Enterprises</span></a></li><li><a href="https://github.com/team" data-analytics-event="{&quot;action&quot;:&quot;small_and_medium_teams&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;small_and_medium_teams_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Small and medium teams</span></a></li><li><a href="https://github.com/enterprise/startups" data-analytics-event="{&quot;action&quot;:&quot;startups&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;startups_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Startups</span></a></li><li><a href="https://github.com/solutions/industry/nonprofits" data-analytics-event="{&quot;action&quot;:&quot;nonprofits&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;nonprofits_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Nonprofits</span></a></li></ul></div></li><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">BY USE CASE</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/solutions/use-case/app-modernization" data-analytics-event="{&quot;action&quot;:&quot;app_modernization&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;app_modernization_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">App Modernization</span></a></li><li><a href="https://github.com/solutions/use-case/devsecops" data-analytics-event="{&quot;action&quot;:&quot;devsecops&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;devsecops_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">DevSecOps</span></a></li><li><a href="https://github.com/solutions/use-case/devops" data-analytics-event="{&quot;action&quot;:&quot;devops&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;devops_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">DevOps</span></a></li><li><a href="https://github.com/solutions/use-case/ci-cd" data-analytics-event="{&quot;action&quot;:&quot;ci/cd&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;ci/cd_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">CI/CD</span></a></li><li><a href="https://github.com/solutions/use-case" data-analytics-event="{&quot;action&quot;:&quot;view_all_use_cases&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_use_cases_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">View all use cases</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon--g6Lip" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">BY INDUSTRY</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/solutions/industry/healthcare" data-analytics-event="{&quot;action&quot;:&quot;healthcare&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;healthcare_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Healthcare</span></a></li><li><a href="https://github.com/solutions/industry/financial-services" data-analytics-event="{&quot;action&quot;:&quot;financial_services&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;financial_services_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Financial services</span></a></li><li><a href="https://github.com/solutions/industry/manufacturing" data-analytics-event="{&quot;action&quot;:&quot;manufacturing&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;manufacturing_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Manufacturing</span></a></li><li><a href="https://github.com/solutions/industry/government" data-analytics-event="{&quot;action&quot;:&quot;government&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;government_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Government</span></a></li><li><a href="https://github.com/solutions/industry" data-analytics-event="{&quot;action&quot;:&quot;view_all_industries&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_industries_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">View all industries</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon--g6Lip" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></li></ul></div></li></ul><div class="NavDropdown-module__trailingLinkContainer--MNB5T"><a href="https://github.com/solutions" data-analytics-event="{&quot;action&quot;:&quot;view_all_solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_solutions_link_solutions_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">View all solutions</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon--g6Lip" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></div></div></div></li><li><div class="NavDropdown-module__container--bmXM2 js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button--Hq9UR js-details-target" aria-expanded="false">Resources<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon--SR0Ke" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown--Ig57Y"><ul class="NavDropdown-module__list--RwSSK"><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">EXPLORE BY TOPIC</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/resources/articles?topic=ai" data-analytics-event="{&quot;action&quot;:&quot;ai&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;ai_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">AI</span></a></li><li><a href="https://github.com/resources/articles?topic=software-development" data-analytics-event="{&quot;action&quot;:&quot;software_development&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;software_development_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Software Development</span></a></li><li><a href="https://github.com/resources/articles?topic=devops" data-analytics-event="{&quot;action&quot;:&quot;devops&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;devops_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">DevOps</span></a></li><li><a href="https://github.com/resources/articles?topic=security" data-analytics-event="{&quot;action&quot;:&quot;security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;security_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Security</span></a></li><li><a href="https://github.com/resources/articles" data-analytics-event="{&quot;action&quot;:&quot;view_all_topics&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;view_all_topics_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">View all topics</span><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavLink-module__arrowIcon--g6Lip" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">EXPLORE BY TYPE</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/customer-stories" data-analytics-event="{&quot;action&quot;:&quot;customer_stories&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;customer_stories_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Customer stories</span></a></li><li><a href="https://github.com/resources/events" data-analytics-event="{&quot;action&quot;:&quot;events__webinars&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;events__webinars_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Events &amp; webinars</span></a></li><li><a href="https://github.com/resources/whitepapers" data-analytics-event="{&quot;action&quot;:&quot;ebooks__reports&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;ebooks__reports_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Ebooks &amp; reports</span></a></li><li><a href="https://github.com/solutions/executive-insights" data-analytics-event="{&quot;action&quot;:&quot;business_insights&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;business_insights_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Business insights</span></a></li><li><a href="https://skills.github.com" data-analytics-event="{&quot;action&quot;:&quot;github_skills&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_skills_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB" target="_blank" rel="noreferrer"><span class="NavLink-module__title--xw3ok">GitHub Skills</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon--JurQ9" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">SUPPORT &amp; SERVICES</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://docs.github.com" data-analytics-event="{&quot;action&quot;:&quot;documentation&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;documentation_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB" target="_blank" rel="noreferrer"><span class="NavLink-module__title--xw3ok">Documentation</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon--JurQ9" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://support.github.com" data-analytics-event="{&quot;action&quot;:&quot;customer_support&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;customer_support_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB" target="_blank" rel="noreferrer"><span class="NavLink-module__title--xw3ok">Customer support</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon--JurQ9" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.com/orgs/community/discussions" data-analytics-event="{&quot;action&quot;:&quot;community_forum&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;community_forum_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Community forum</span></a></li><li><a href="https://github.com/trust-center" data-analytics-event="{&quot;action&quot;:&quot;trust_center&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;trust_center_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Trust center</span></a></li><li><a href="https://github.com/partners" data-analytics-event="{&quot;action&quot;:&quot;partners&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;partners_link_resources_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Partners</span></a></li></ul></div></li></ul></div></div></li><li><div class="NavDropdown-module__container--bmXM2 js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button--Hq9UR js-details-target" aria-expanded="false">Open Source<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon--SR0Ke" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown--Ig57Y"><ul class="NavDropdown-module__list--RwSSK"><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">COMMUNITY</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/sponsors" data-analytics-event="{&quot;action&quot;:&quot;github_sponsors&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_sponsors_link_open_source_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-sponsor-tiers NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M16.004 1.25C18.311 1.25 20 3.128 20 5.75c0 2.292-1.23 4.464-3.295 6.485-.481.47-.98.909-1.482 1.31l.265 1.32 1.375 7.5a.75.75 0 0 1-.982.844l-3.512-1.207a.75.75 0 0 0-.488 0L8.37 23.209a.75.75 0 0 1-.982-.844l1.378-7.512.261-1.309c-.5-.4-1-.838-1.481-1.31C5.479 10.215 4.25 8.043 4.25 5.75c0-2.622 1.689-4.5 3.996-4.5 1.55 0 2.947.752 3.832 1.967l.047.067.047-.067a4.726 4.726 0 0 1 3.612-1.962l.22-.005ZM13.89 14.531c-.418.285-.828.542-1.218.77l-.18.103a.75.75 0 0 1-.734 0l-.071-.04-.46-.272c-.282-.173-.573-.36-.868-.562l-.121.605-1.145 6.239 2.3-.79a2.248 2.248 0 0 1 1.284-.054l.18.053 2.299.79-1.141-6.226-.125-.616ZM16.004 2.75c-1.464 0-2.731.983-3.159 2.459-.209.721-1.231.721-1.44 0-.428-1.476-1.695-2.459-3.16-2.459-1.44 0-2.495 1.173-2.495 3 0 1.811 1.039 3.647 2.844 5.412a19.624 19.624 0 0 0 3.734 2.84l-.019-.011-.184-.111.147-.088a19.81 19.81 0 0 0 3.015-2.278l.37-.352C17.46 9.397 18.5 7.561 18.5 5.75c0-1.827-1.055-3-2.496-3Z"></path></svg><span class="NavLink-module__title--xw3ok">GitHub Sponsors</span><span class="NavLink-module__subtitle--qC15H">Fund open source developers</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">PROGRAMS</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://securitylab.github.com" data-analytics-event="{&quot;action&quot;:&quot;security_lab&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;security_lab_link_open_source_navbar&quot;}" class="NavLink-module__link--n48VB" target="_blank" rel="noreferrer"><span class="NavLink-module__title--xw3ok">Security Lab</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon--JurQ9" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://maintainers.github.com" data-analytics-event="{&quot;action&quot;:&quot;maintainer_community&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;maintainer_community_link_open_source_navbar&quot;}" class="NavLink-module__link--n48VB" target="_blank" rel="noreferrer"><span class="NavLink-module__title--xw3ok">Maintainer Community</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon--JurQ9" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li><li><a href="https://github.com/accelerator" data-analytics-event="{&quot;action&quot;:&quot;accelerator&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;accelerator_link_open_source_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Accelerator</span></a></li><li><a href="https://archiveprogram.github.com" data-analytics-event="{&quot;action&quot;:&quot;archive_program&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;archive_program_link_open_source_navbar&quot;}" class="NavLink-module__link--n48VB" target="_blank" rel="noreferrer"><span class="NavLink-module__title--xw3ok">Archive Program</span><svg aria-hidden="true" focusable="false" class="octicon octicon-link-external NavLink-module__externalIcon--JurQ9" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg></a></li></ul></div></li><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">REPOSITORIES</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/topics" data-analytics-event="{&quot;action&quot;:&quot;topics&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;topics_link_open_source_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Topics</span></a></li><li><a href="https://github.com/trending" data-analytics-event="{&quot;action&quot;:&quot;trending&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;trending_link_open_source_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Trending</span></a></li><li><a href="https://github.com/collections" data-analytics-event="{&quot;action&quot;:&quot;collections&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;collections_link_open_source_navbar&quot;}" class="NavLink-module__link--n48VB"><span class="NavLink-module__title--xw3ok">Collections</span></a></li></ul></div></li></ul></div></div></li><li><div class="NavDropdown-module__container--bmXM2 js-details-container js-header-menu-item"><button type="button" class="NavDropdown-module__button--Hq9UR js-details-target" aria-expanded="false">Enterprise<svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon--SR0Ke" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div class="NavDropdown-module__dropdown--Ig57Y"><ul class="NavDropdown-module__list--RwSSK"><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">ENTERPRISE SOLUTIONS</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/enterprise" data-analytics-event="{&quot;action&quot;:&quot;enterprise_platform&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;enterprise_platform_link_enterprise_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-stack NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.063 1.456a1.749 1.749 0 0 1 1.874 0l8.383 5.316a1.751 1.751 0 0 1 0 2.956l-8.383 5.316a1.749 1.749 0 0 1-1.874 0L2.68 9.728a1.751 1.751 0 0 1 0-2.956Zm1.071 1.267a.25.25 0 0 0-.268 0L3.483 8.039a.25.25 0 0 0 0 .422l8.383 5.316a.25.25 0 0 0 .268 0l8.383-5.316a.25.25 0 0 0 0-.422Z"></path><path d="M1.867 12.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path><path d="M1.867 16.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path></svg><span class="NavLink-module__title--xw3ok">Enterprise platform</span><span class="NavLink-module__subtitle--qC15H">AI-powered developer platform</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group--T925n"><span class="NavGroup-module__title--TdKyz">AVAILABLE ADD-ONS</span><ul class="NavGroup-module__list--M8eGv"><li><a href="https://github.com/security/advanced-security" data-analytics-event="{&quot;action&quot;:&quot;github_advanced_security&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_advanced_security_link_enterprise_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-shield-check NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path></svg><span class="NavLink-module__title--xw3ok">GitHub Advanced Security</span><span class="NavLink-module__subtitle--qC15H">Enterprise-grade security features</span></div></a></li><li><a href="https://github.com/features/copilot/copilot-business" data-analytics-event="{&quot;action&quot;:&quot;copilot_for_business&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;copilot_for_business_link_enterprise_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path></svg><span class="NavLink-module__title--xw3ok">Copilot for Business</span><span class="NavLink-module__subtitle--qC15H">Enterprise-grade AI features</span></div></a></li><li><a href="https://github.com/premium-support" data-analytics-event="{&quot;action&quot;:&quot;premium_support&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;premium_support_link_enterprise_navbar&quot;}" class="NavLink-module__link--n48VB"><div class="NavLink-module__text--SdWkb"><svg aria-hidden="true" focusable="false" class="octicon octicon-comment-discussion NavLink-module__icon--h0sw7" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path></svg><span class="NavLink-module__title--xw3ok">Premium Support</span><span class="NavLink-module__subtitle--qC15H">Enterprise-grade 24/7 support</span></div></a></li></ul></div></li></ul></div></div></li><li><a href="https://github.com/pricing" data-analytics-event="{&quot;action&quot;:&quot;pricing&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;pricing&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;pricing_link_pricing_navbar&quot;}" class="NavLink-module__link--n48VB MarketingNavigation-module__navLink--U9Uuk"><span class="NavLink-module__title--xw3ok">Pricing</span></a></li></ul></nav><script type="application/json" id="__PRIMER_DATA_:R0:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>



        <div class="d-flex flex-column flex-lg-row width-full flex-justify-end flex-lg-items-center text-center mt-3 mt-lg-0 text-lg-left ml-lg-3">
                


<qbsearch-input class="search-input" data-scope="repo:supabase-community/chatgpt-your-files" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="VlCHyMw7_KWALoIeQ6FuPMDQ2IJXujDV_i0cm78YPU_-jwJEKZvbdRexf65t-vtuXHhZ7MJ2rPXWUj0UENA2Ew" data-max-custom-scopes="10" data-header-redesign-enabled="false" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="supabase-community/chatgpt-your-files" data-current-org="supabase-community" data-current-owner="" data-logged-in="false" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-retain-scroll-position="true">
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
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-808684e4-6499-4b88-b089-85a06398b48f" data-target="query-builder.input" data-action="
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
      <div class="FormControl-inlineValidation" id="validation-808684e4-6499-4b88-b089-85a06398b48f" hidden="hidden">
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
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="code-search-feedback-form" data-turbo="false" action="/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="JPDlwR2XZUHAL5h1jdKvZBPxCmZVUQVEnUBBtNDniVBcpNMDVMKpKf7ZIZWQLULz9znb1cLM/zUoQ/QWm+Ia/w==" />
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
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="custom-scopes-dialog-form" data-turbo="false" action="/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="UXTADd6xge1aYeBLV179qhD2xDZyx9y7HA1TfXnSL61SB2nTFgUNu1WN/qMOK4tARpdKuZq2huY3IvFq3j1ziQ==" />
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
              <input type="hidden" data-csrf="true" value="El7iiNvalt/WxO7/7d0OfB4OLnf3AIviS3zNW8jH8WZ95Wkn50L/3S2g/+rlYS7Z+H5Ylq7vIrVApKH0HIC76w==" />
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
                href="/login?return_to=https%3A%2F%2Fgithub.com%2Fsupabase-community%2Fchatgpt-your-files"
                class="HeaderMenu-link HeaderMenu-link--sign-in HeaderMenu-button flex-shrink-0 no-underline d-none d-lg-inline-flex border border-lg-0 rounded px-2 py-1"
                style="margin-left: 12px;"
                data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/supabase-community/chatgpt-your-files&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="b28131c32098a2843a445fdc61c1c73d2cd9ce9b44398a43a8138f21f5712bba"
                data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}"
              >
                Sign in
              </a>
            </div>

              <a href="/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&amp;source=header-repo&amp;source_repo=supabase-community%2Fchatgpt-your-files"
                class="HeaderMenu-link HeaderMenu-link--sign-up HeaderMenu-button flex-shrink-0 d-flex d-lg-inline-flex no-underline border color-border-default rounded px-2 py-1"
                data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/supabase-community/chatgpt-your-files&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="b28131c32098a2843a445fdc61c1c73d2cd9ce9b44398a43a8138f21f5712bba"
                data-analytics-event="{&quot;category&quot;:&quot;Sign up&quot;,&quot;action&quot;:&quot;click to sign up for account&quot;,&quot;label&quot;:&quot;ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;;ref_cta:Sign up;ref_loc:header logged out&quot;}"
              >
                Sign up
              </a>

                <div class="AppHeader-appearanceSettings">
    <react-partial-anchor>
      <button data-target="react-partial-anchor.anchor" id="icon-button-eaa4989b-6387-44b3-8b6a-00eb7cb43857" aria-labelledby="tooltip-db604d9f-26ab-4a4e-8fa5-67fb78695902" type="button" disabled="disabled" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium AppHeader-button HeaderMenu-link border cursor-wait">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sliders Button-visual">
    <path d="M15 2.75a.75.75 0 0 1-.75.75h-4a.75.75 0 0 1 0-1.5h4a.75.75 0 0 1 .75.75Zm-8.5.75v1.25a.75.75 0 0 0 1.5 0v-4a.75.75 0 0 0-1.5 0V2H1.75a.75.75 0 0 0 0 1.5H6.5Zm1.25 5.25a.75.75 0 0 0 0-1.5h-6a.75.75 0 0 0 0 1.5h6ZM15 8a.75.75 0 0 1-.75.75H11.5V10a.75.75 0 1 1-1.5 0V6a.75.75 0 0 1 1.5 0v1.25h2.75A.75.75 0 0 1 15 8Zm-9 5.25v-2a.75.75 0 0 0-1.5 0v1.25H1.75a.75.75 0 0 0 0 1.5H4.5v1.25a.75.75 0 0 0 1.5 0v-2Zm9 0a.75.75 0 0 1-.75.75h-6a.75.75 0 0 1 0-1.5h6a.75.75 0 0 1 .75.75Z"></path>
</svg>
</button><tool-tip id="tooltip-db604d9f-26ab-4a4e-8fa5-67fb78695902" for="icon-button-eaa4989b-6387-44b3-8b6a-00eb7cb43857" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Appearance settings</tool-tip>

      <template data-target="react-partial-anchor.template">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.47239ec6cbe68138fe4c.module.css" />
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

    <button id="icon-button-fd38d634-87ce-4891-9bc2-327302c86c73" aria-labelledby="tooltip-ed943110-7676-4f21-a8b9-be811388bdc4" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-ed943110-7676-4f21-a8b9-be811388bdc4" for="icon-button-fd38d634-87ce-4891-9bc2-327302c86c73" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Dismiss alert</tool-tip>


  
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
      <a class="url fn" rel="author" data-hovercard-type="organization" data-hovercard-url="/orgs/supabase-community/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/supabase-community">
        supabase-community
</a>    </span>
    <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
    <strong itemprop="name" class="mr-2 flex-self-stretch">
      <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/supabase-community/chatgpt-your-files">chatgpt-your-files</a>
    </strong>

    <span></span><span class="Label Label--secondary v-align-middle mr-1">Public</span>
  </div>


        </div>

        <div id="repository-details-container" class="flex-shrink-0" data-turbo-replace style="max-width: 70%;">
            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
    
      

  <li>
            <a href="/login?return_to=%2Fsupabase-community%2Fchatgpt-your-files" rel="nofollow" id="repository-details-watch-button" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/supabase-community/chatgpt-your-files&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="4a4e243fa14fc46343d343af55dc021b01c63c51bcde8991180eeb31da89ac3c" aria-label="You must be signed in to change notification settings" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>Notifications
</a>    <tool-tip id="tooltip-9727b677-cc98-45f6-b59b-9f609955c313" for="repository-details-watch-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">You must be signed in to change notification settings</tool-tip>

  </li>

  <li>
          <a icon="repo-forked" id="fork-button" href="/login?return_to=%2Fsupabase-community%2Fchatgpt-your-files" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:701867516,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/supabase-community/chatgpt-your-files&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="bef37a28681daf9b520564c1839e10289616cb590983e6396c49971dacb87bba" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>Fork
    <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="193" data-view-component="true" class="Counter">193</span>
</a>
  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <a href="/login?return_to=%2Fsupabase-community%2Fchatgpt-your-files" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:701867516,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/supabase-community/chatgpt-your-files&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="41eefc129648a9865e2ad19109be0b58875159cb93f22cde372f3c7d5e139305" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-sw btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>          <span id="repo-stars-counter-star" aria-label="507 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="507" data-view-component="true" class="Counter js-social-count">507</span>
</a></div>
  </li>

</ul>

        </div>
      </div>

        <div id="responsive-meta-container" data-turbo-replace>
      <div class="d-block d-md-none mb-2 px-3 px-md-4 px-lg-5">
      <p class="f4 mb-3 ">
        Production-ready MVP for securely chatting with your documents using pgvector
      </p>
      <div class="mb-2 d-flex flex-items-center Link--secondary">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link flex-shrink-0 mr-2">
    <path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path>
</svg>
        <span class="flex-auto min-width-0 css-truncate css-truncate-target width-fit">
          <a title="https://youtu.be/ibzlEQmgPPY" role="link" target="_blank" class="text-bold" rel="noopener noreferrer" href="https://youtu.be/ibzlEQmgPPY">youtu.be/ibzlEQmgPPY</a>
        </span>
      </div>

    

    <div class="mb-3">
        <a class="Link--secondary no-underline mr-3" href="/supabase-community/chatgpt-your-files/stargazers">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-1">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
          <span class="text-bold">507</span>
          stars
</a>        <a class="Link--secondary no-underline mr-3" href="/supabase-community/chatgpt-your-files/forks">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-1">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
          <span class="text-bold">193</span>
          forks
</a>        <a class="Link--secondary no-underline mr-3 d-inline-block" href="/supabase-community/chatgpt-your-files/branches">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch mr-1">
    <path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path>
</svg>
          <span>Branches</span>
</a>        <a class="Link--secondary no-underline d-inline-block" href="/supabase-community/chatgpt-your-files/tags">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tag mr-1">
    <path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path>
</svg>
          <span>Tags</span>
</a>        <a class="Link--secondary no-underline d-inline-block" href="/supabase-community/chatgpt-your-files/activity">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pulse mr-1">
    <path d="M6 2c.306 0 .582.187.696.471L10 10.731l1.304-3.26A.751.751 0 0 1 12 7h3.25a.75.75 0 0 1 0 1.5h-2.742l-1.812 4.528a.751.751 0 0 1-1.392 0L6 4.77 4.696 8.03A.75.75 0 0 1 4 8.5H.75a.75.75 0 0 1 0-1.5h2.742l1.812-4.529A.751.751 0 0 1 6 2Z"></path>
</svg>
          <span>Activity</span>
</a>    </div>
      <div class="d-flex flex-wrap gap-2">
        <div class="flex-1">
            <div data-view-component="true" class="BtnGroup d-flex">
        <a href="/login?return_to=%2Fsupabase-community%2Fchatgpt-your-files" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:701867516,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/supabase-community/chatgpt-your-files&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="41eefc129648a9865e2ad19109be0b58875159cb93f22cde372f3c7d5e139305" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-sw btn-sm btn btn-block">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>
</a></div>
        </div>
        <div class="flex-1">
                <a href="/login?return_to=%2Fsupabase-community%2Fchatgpt-your-files" rel="nofollow" id="files-overview-watch-button" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/supabase-community/chatgpt-your-files&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="4a4e243fa14fc46343d343af55dc021b01c63c51bcde8991180eeb31da89ac3c" aria-label="You must be signed in to change notification settings" data-view-component="true" class="btn-sm btn btn-block">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>Notifications
</a>    <tool-tip id="tooltip-b91d8ce3-4187-414e-bb84-8f7101cddb1b" for="files-overview-watch-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">You must be signed in to change notification settings</tool-tip>

        </div>
        <span>
          

        </span>
      </div>
  </div>

</div>


          <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="/supabase-community/chatgpt-your-files" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /supabase-community/chatgpt-your-files" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" aria-current="page" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="/supabase-community/chatgpt-your-files/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /supabase-community/chatgpt-your-files/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-react-nav="issues-react" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="11" data-view-component="true" class="Counter">11</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/supabase-community/chatgpt-your-files/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /supabase-community/chatgpt-your-files/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="2" data-view-component="true" class="Counter">2</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/supabase-community/chatgpt-your-files/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /supabase-community/chatgpt-your-files/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="/supabase-community/chatgpt-your-files/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /supabase-community/chatgpt-your-files/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="/supabase-community/chatgpt-your-files/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /supabase-community/chatgpt-your-files/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          <include-fragment src="/supabase-community/chatgpt-your-files/security/overall-count" accept="text/fragment+html" data-nonce="v2:fc902795-443c-4768-14bd-518a2dc3c13e" data-view-component="true">
  
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
  <a id="insights-tab" href="/supabase-community/chatgpt-your-files/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /supabase-community/chatgpt-your-files/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true">
  <focus-group direction="vertical" mnemonics retain>
    <button id="action-menu-c93a8c4e-810c-457a-b3ee-95a2dc59fa94-button" popovertarget="action-menu-c93a8c4e-810c-457a-b3ee-95a2dc59fa94-overlay" aria-controls="action-menu-c93a8c4e-810c-457a-b3ee-95a2dc59fa94-list" aria-haspopup="true" aria-labelledby="tooltip-69852810-e4b1-4186-9c06-14afe9766eef" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-69852810-e4b1-4186-9c06-14afe9766eef" for="action-menu-c93a8c4e-810c-457a-b3ee-95a2dc59fa94-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-c93a8c4e-810c-457a-b3ee-95a2dc59fa94-overlay" anchor="action-menu-c93a8c4e-810c-457a-b3ee-95a2dc59fa94-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list>
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-c93a8c4e-810c-457a-b3ee-95a2dc59fa94-button" id="action-menu-c93a8c4e-810c-457a-b3ee-95a2dc59fa94-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="hidden" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-0c201761-69a2-451a-a001-707fbaf2ee86" href="/supabase-community/chatgpt-your-files" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-5ee7bc14-6234-482e-a69b-464a5b56bf5e" href="/supabase-community/chatgpt-your-files/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-04cc96ef-c4b4-4133-89ea-85e5835eeb96" href="/supabase-community/chatgpt-your-files/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-267645c3-5684-4b06-a7dc-76df493c52b8" href="/supabase-community/chatgpt-your-files/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-e03e75e3-a6af-42c0-9ee2-260cc493af38" href="/supabase-community/chatgpt-your-files/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-2a49468a-7607-4749-9802-d02ebd3bbcd7" href="/supabase-community/chatgpt-your-files/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    
    
    <a tabindex="-1" id="item-956d553e-6508-412c-891e-16316753c72a" href="/supabase-community/chatgpt-your-files/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
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
    



    
      
  <h1 class='sr-only'>supabase-community/chatgpt-your-files</h1>
  <div class="clearfix container-xl px-md-4 px-lg-5 px-3">
    <div>

  <div style="max-width: 100%" data-view-component="true" class="Layout Layout--flowRow-until-md react-repos-overview-margin Layout--sidebarPosition-end Layout--sidebarPosition-flowRow-end">
  <div data-view-component="true" class="Layout-main">      <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.47239ec6cbe68138fe4c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/67240.5e03be13ea8a0f937111.module.css" />

<react-partial
  partial-name="repos-overview"
  data-ssr="true"
  data-attempted-ssr="true"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"initialPayload":{"allShortcutsEnabled":false,"path":"/","repo":{"id":701867516,"defaultBranch":"main","name":"chatgpt-your-files","ownerLogin":"supabase-community","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-10-07T19:48:52.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/87650496?v=4","public":true,"private":false,"isOrgOwned":true},"currentUser":null,"refInfo":{"name":"main","listCacheKey":"v0:1718950578.0","canEdit":false,"refType":"branch","currentOid":"39f1403ed1c5aad57a7527c63638930e7c131e20"},"tree":{"items":[{"name":".vscode","path":".vscode","contentType":"directory"},{"name":"app","path":"app","contentType":"directory"},{"name":"assets","path":"assets","contentType":"directory"},{"name":"components","path":"components","contentType":"directory"},{"name":"lib","path":"lib","contentType":"directory"},{"name":"sample-files","path":"sample-files","contentType":"directory"},{"name":"supabase","path":"supabase","contentType":"directory"},{"name":".env.local.example","path":".env.local.example","contentType":"file"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"components.json","path":"components.json","contentType":"file"},{"name":"middleware.ts","path":"middleware.ts","contentType":"file"},{"name":"next.config.js","path":"next.config.js","contentType":"file"},{"name":"package-lock.json","path":"package-lock.json","contentType":"file"},{"name":"package.json","path":"package.json","contentType":"file"},{"name":"postcss.config.js","path":"postcss.config.js","contentType":"file"},{"name":"tailwind.config.js","path":"tailwind.config.js","contentType":"file"},{"name":"tsconfig.json","path":"tsconfig.json","contentType":"file"}],"templateDirectorySuggestionUrl":null,"readme":null,"totalCount":18,"showBranchInfobar":false},"fileTree":null,"fileTreeProcessingTime":null,"foldersToFetch":[],"userNameDisplayConfiguration":"handle","treeExpanded":false,"symbolsExpanded":false,"copilotSWEAgentEnabled":false,"isOverview":true,"overview":{"banners":{"shouldRecommendReadme":false,"isPersonalRepo":false,"showUseActionBanner":false,"actionSlug":null,"actionId":null,"showProtectBranchBanner":false,"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_repo","releasePath":"/supabase-community/chatgpt-your-files/releases/new?marketplace=true","showPublishActionBanner":false},"interactionLimitBanner":null,"showInvitationBanner":false,"inviterName":null,"actionsMigrationBannerInfo":{"releaseTags":[],"showImmutableActionsMigrationBanner":false,"initialMigrationStatus":null},"showDeployBanner":false,"detectedStack":{"framework":null,"packageManager":null}},"codeButton":{"contactPath":"/contact","isEnterprise":false,"local":{"protocolInfo":{"httpAvailable":true,"sshAvailable":null,"httpUrl":"https://github.com/supabase-community/chatgpt-your-files.git","showCloneWarning":null,"sshUrl":null,"sshCertificatesRequired":null,"sshCertificatesAvailable":null,"ghCliUrl":"gh repo clone supabase-community/chatgpt-your-files","defaultProtocol":"http","newSshKeyUrl":"/settings/ssh/new","setProtocolPath":"/users/set_protocol"},"platformInfo":{"cloneUrl":"https://desktop.github.com","showVisualStudioCloneButton":false,"visualStudioCloneUrl":"https://windows.github.com","showXcodeCloneButton":false,"xcodeCloneUrl":"xcode://clone?repo=https%3A%2F%2Fgithub.com%2Fsupabase-community%2Fchatgpt-your-files","zipballUrl":"/supabase-community/chatgpt-your-files/archive/refs/heads/main.zip"}},"newCodespacePath":"/codespaces/new?hide_repo_select=true\u0026repo=701867516"},"popovers":{"rename":null,"renamedParentRepo":null},"commitCount":"55","overviewFiles":[{"displayName":"README.md","repoName":"chatgpt-your-files","refName":"main","path":"README.md","preferredFileType":"readme","tabName":"README","richText":"\u003carticle class=\"markdown-body entry-content container-lg\" itemprop=\"text\"\u003e\u003cp dir=\"auto\"\u003e\u003ca target=\"_blank\" rel=\"noopener noreferrer\" href=\"/supabase-community/chatgpt-your-files/blob/main/assets/hero.png\"\u003e\u003cimg alt=\"pgvector to Prod in 2 hours\" src=\"/supabase-community/chatgpt-your-files/raw/main/assets/hero.png\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch1 align=\"center\" tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eWorkshop: pgvector to Prod in 2 hours\u003c/h1\u003e\u003ca id=\"user-content-workshop-pgvector-to-prod-in-2-hours\" class=\"anchor\" aria-label=\"Permalink: Workshop: pgvector to Prod in 2 hours\" href=\"#workshop-pgvector-to-prod-in-2-hours\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp align=\"center\" dir=\"auto\"\u003e\nCreate a production-ready MVP for securely chatting with your documents.\n\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e☑️ Features\u003c/h2\u003e\u003ca id=\"user-content-️-features\" class=\"anchor\" aria-label=\"Permalink: ☑️ Features\" href=\"#️-features\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003cstrong\u003eInteractive Chat Interface:\u003c/strong\u003e Interact with your documentation, leveraging the capabilities of OpenAI’s GPT models and retrieval augmented generation (RAG).\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eLogin With \u0026lt;3rd Party\u0026gt;:\u003c/strong\u003e Integrate one-click 3rd party login with any of our 18 auth providers and user/password.\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eDocument Storage:\u003c/strong\u003e Securely upload, store, and retrieve user uploaded documents.\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eREST API:\u003c/strong\u003e Expose a flexible REST API that we’ll consume to build the interactive front-end.\u003c/li\u003e\n\u003cli\u003e\u003cstrong\u003eRow-level Security:\u003c/strong\u003e Secure all of your user data user data with production-ready row-level security.\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e🎥 YouTube video\u003c/h2\u003e\u003ca id=\"user-content--youtube-video\" class=\"anchor\" aria-label=\"Permalink: 🎥 YouTube video\" href=\"#-youtube-video\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThis entire workshop was recorded as a YouTube video. Feel free to watch it here:\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca href=\"https://www.youtube.com/watch?v=ibzlEQmgPPY\" rel=\"nofollow\"\u003ehttps://www.youtube.com/watch?v=ibzlEQmgPPY\u003c/a\u003e\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e📄 Workshop Instructions\u003c/h2\u003e\u003ca id=\"user-content--workshop-instructions\" class=\"anchor\" aria-label=\"Permalink: 📄 Workshop Instructions\" href=\"#-workshop-instructions\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThanks for joining! Let's dive in.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca target=\"_blank\" rel=\"noopener noreferrer\" href=\"/supabase-community/chatgpt-your-files/blob/main/assets/instructions.png\"\u003e\u003cimg src=\"/supabase-community/chatgpt-your-files/raw/main/assets/instructions.png\" alt=\"Workshop instructions\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003e\u003cstrong\u003eClone repo:\u003c/strong\u003e Clone this repo at tag \u003ccode\u003estep-1\u003c/code\u003e:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"git clone -b step-1 https://github.com/supabase-community/chatgpt-your-files.git\"\u003e\u003cpre\u003egit clone -b step-1 https://github.com/supabase-community/chatgpt-your-files.git\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThis will automatically clone at \u003ca href=\"#step-1---storage\"\u003estep 1\u003c/a\u003e, our starting point.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003e\u003cstrong\u003eGit checkpoints:\u003c/strong\u003e The workshop is broken down into steps (git tags). There's a step for every major feature we are building.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eFeel free to follow along live with the presenter. When it's time to jump to the next step, run:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"git stash push -u # stash your working directory\ngit checkout step-X # jump to a checkpoint (replace X wit step #)\"\u003e\u003cpre\u003egit stash push -u \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e stash your working directory\u003c/span\u003e\ngit checkout step-X \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e jump to a checkpoint (replace X wit step #)\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003e\u003cstrong\u003eStep-by-step guide:\u003c/strong\u003e These steps are written out line-by-line. Feel free to follow along using the \u003ca href=\"#step-by-step\"\u003esteps below\u003c/a\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e🧱 Pre-req’s\u003c/h2\u003e\u003ca id=\"user-content--pre-reqs\" class=\"anchor\" aria-label=\"Permalink: 🧱 Pre-req’s\" href=\"#-pre-reqs\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eUnix-based OS (if Windows, WSL2)\u003c/li\u003e\n\u003cli\u003eDocker\u003c/li\u003e\n\u003cli\u003eNode.js 18+\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e💿 Sample Data\u003c/h2\u003e\u003ca id=\"user-content--sample-data\" class=\"anchor\" aria-label=\"Permalink: 💿 Sample Data\" href=\"#-sample-data\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThis repository includes 3 sample markdown files that we'll use to test the app:\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca href=\"/supabase-community/chatgpt-your-files/blob/main/sample-files/roman-empire-1.md\"\u003e\u003ccode\u003e./sample-files/roman-empire-1.md\u003c/code\u003e\u003c/a\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca href=\"/supabase-community/chatgpt-your-files/blob/main/sample-files/roman-empire-2.md\"\u003e\u003ccode\u003e./sample-files/roman-empire-2.md\u003c/code\u003e\u003c/a\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca href=\"/supabase-community/chatgpt-your-files/blob/main/sample-files/roman-empire-3.md\"\u003e\u003ccode\u003e./sample-files/roman-empire-3.md\u003c/code\u003e\u003c/a\u003e\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e🪜 Step-by-step\u003c/h2\u003e\u003ca id=\"user-content--step-by-step\" class=\"anchor\" aria-label=\"Permalink: 🪜 Step-by-step\" href=\"#-step-by-step\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eJump to a step:\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"#step-1---storage\"\u003eStorage\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-2---documents\"\u003eDocuments\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-3---embeddings\"\u003eEmbeddings\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-4---chat\"\u003eChat\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-5---database-types-bonus\"\u003eDatabase Types\u003c/a\u003e (Bonus)\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#youre-done\"\u003eYou're done!\u003c/a\u003e\u003c/li\u003e\n\u003c/ol\u003e\n\u003chr\u003e\n\u003cdetails\u003e\n\u003csummary\u003e\u003cstrong\u003eStep 0 - Setup\u003c/strong\u003e \u003cem\u003e(Optional)\u003c/em\u003e\u003c/summary\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e\u003ccode\u003eStep 0\u003c/code\u003e - Setup\u003c/h3\u003e\u003ca id=\"user-content-step-0---setup\" class=\"anchor\" aria-label=\"Permalink: Step 0 - Setup\" href=\"#step-0---setup\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eUse this command to jump to the \u003ccode\u003estep-0\u003c/code\u003e checkpoint.\u003c/em\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"git checkout step-0\"\u003e\u003cpre\u003egit checkout step-0\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThe beginning of step 0 is aka to:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx create-next-app -e with-supabase\"\u003e\u003cpre\u003enpx create-next-app -e with-supabase\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eRefer to this step if you want to learn about the additions added on top of \u003ccode\u003ecreate-next-app\u003c/code\u003e to get us up and running quicker for this workshop \u003cem\u003e(VS Code settings, UI components/styles/layouts)\u003c/em\u003e. Otherwise, skip straight to \u003ca href=\"#step-1---storage\"\u003e\u003ccode\u003estep-1\u003c/code\u003e\u003c/a\u003e.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eInstall Supabase as dev dependency.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npm i -D supabase@1.102.0\"\u003e\u003cpre\u003enpm i -D supabase@1.102.0\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eInitialize Supabase project.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase init\"\u003e\u003cpre\u003enpx supabase init\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003e(Optional) Setup VSCode environment.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"mkdir -p .vscode \u0026amp;\u0026amp; cat \u0026gt; .vscode/settings.json \u0026lt;\u0026lt;- EOF\n{\n  \u0026quot;deno.enable\u0026quot;: true,\n  \u0026quot;deno.lint\u0026quot;: true,\n  \u0026quot;deno.unstable\u0026quot;: false,\n  \u0026quot;deno.enablePaths\u0026quot;: [\n    \u0026quot;supabase\u0026quot;\n  ],\n  \u0026quot;deno.importMap\u0026quot;: \u0026quot;./supabase/functions/import_map.json\u0026quot;\n}\nEOF\"\u003e\u003cpre\u003emkdir -p .vscode \u003cspan class=\"pl-k\"\u003e\u0026amp;\u0026amp;\u003c/span\u003e cat \u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e .vscode/settings.json \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-k\"\u003e\u0026lt;\u0026lt;\u003c/span\u003e- \u003cspan class=\"pl-k\"\u003eEOF\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e{\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e  \"deno.enable\": true,\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e  \"deno.lint\": true,\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e  \"deno.unstable\": false,\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e  \"deno.enablePaths\": [\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e    \"supabase\"\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e  ],\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e  \"deno.importMap\": \"./supabase/functions/import_map.json\"\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e}\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-k\"\u003eEOF\u003c/span\u003e\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003e(Optional) Setup VSCode recommended extensions.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"cat \u0026gt; .vscode/extensions.json \u0026lt;\u0026lt;- EOF\n{\n \u0026quot;recommendations\u0026quot;: [\n   \u0026quot;denoland.vscode-deno\u0026quot;,\n   \u0026quot;esbenp.prettier-vscode\u0026quot;,\n   \u0026quot;dbaeumer.vscode-eslint\u0026quot;,\n   \u0026quot;bradlc.vscode-tailwindcss\u0026quot;,\n ],\n}\nEOF\"\u003e\u003cpre\u003ecat \u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e .vscode/extensions.json \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-k\"\u003e\u0026lt;\u0026lt;\u003c/span\u003e- \u003cspan class=\"pl-k\"\u003eEOF\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e{\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e \"recommendations\": [\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e   \"denoland.vscode-deno\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e   \"esbenp.prettier-vscode\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e   \"dbaeumer.vscode-eslint\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e   \"bradlc.vscode-tailwindcss\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e ],\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e}\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-k\"\u003eEOF\u003c/span\u003e\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThen \u003ccode\u003ecmd\u003c/code\u003e+\u003ccode\u003eshift\u003c/code\u003e+\u003ccode\u003ep\u003c/code\u003e → \u003ccode\u003e\u0026gt;show recommended extensions\u003c/code\u003e → install all \u003cem\u003e(or whichever you like)\u003c/em\u003e\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate \u003ccode\u003eimport_map.json\u003c/code\u003e with dependencies for our Supabase Edge Functions. We'll talk more about this in \u003ca href=\"#step-2---documents\"\u003estep 2\u003c/a\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"cat \u0026gt; supabase/functions/import_map.json \u0026lt;\u0026lt;- EOF\n {\n   \u0026quot;imports\u0026quot;: {\n     \u0026quot;@std/\u0026quot;: \u0026quot;https://deno.land/std@0.168.0/\u0026quot;,\n\n     \u0026quot;@supabase/supabase-js\u0026quot;: \u0026quot;https://esm.sh/@supabase/supabase-js@2.21.0\u0026quot;,\n     \u0026quot;openai\u0026quot;: \u0026quot;https://esm.sh/openai@4.10.0\u0026quot;,\n     \u0026quot;common-tags\u0026quot;: \u0026quot;https://esm.sh/common-tags@1.8.2\u0026quot;,\n     \u0026quot;ai\u0026quot;: \u0026quot;https://esm.sh/ai@2.2.13\u0026quot;,\n\n     \u0026quot;mdast-util-from-markdown\u0026quot;: \u0026quot;https://esm.sh/v132/mdast-util-from-markdown@2.0.0\u0026quot;,\n     \u0026quot;mdast-util-to-markdown\u0026quot;: \u0026quot;https://esm.sh/v132/mdast-util-to-markdown@2.1.0\u0026quot;,\n     \u0026quot;mdast-util-to-string\u0026quot;: \u0026quot;https://esm.sh/v132/mdast-util-to-string@4.0.0\u0026quot;,\n     \u0026quot;unist-builder\u0026quot;: \u0026quot;https://esm.sh/v132/unist-builder@4.0.0\u0026quot;,\n     \u0026quot;mdast\u0026quot;: \u0026quot;https://esm.sh/v132/@types/mdast@4.0.0/index.d.ts\u0026quot;,\n\n     \u0026quot;https://esm.sh/v132/decode-named-character-reference@1.0.2/esnext/decode-named-character-reference.mjs\u0026quot;: \u0026quot;https://esm.sh/decode-named-character-reference@1.0.2?target=deno\u0026quot;\n   }\n }\n EOF\"\u003e\u003cpre\u003ecat \u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e supabase/functions/import_map.json \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-k\"\u003e\u0026lt;\u0026lt;\u003c/span\u003e- \u003cspan class=\"pl-k\"\u003eEOF\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e {\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e   \"imports\": {\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"@std/\": \"https://deno.land/std@0.168.0/\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"@supabase/supabase-js\": \"https://esm.sh/@supabase/supabase-js@2.21.0\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"openai\": \"https://esm.sh/openai@4.10.0\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"common-tags\": \"https://esm.sh/common-tags@1.8.2\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"ai\": \"https://esm.sh/ai@2.2.13\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"mdast-util-from-markdown\": \"https://esm.sh/v132/mdast-util-from-markdown@2.0.0\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"mdast-util-to-markdown\": \"https://esm.sh/v132/mdast-util-to-markdown@2.1.0\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"mdast-util-to-string\": \"https://esm.sh/v132/mdast-util-to-string@4.0.0\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"unist-builder\": \"https://esm.sh/v132/unist-builder@4.0.0\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"mdast\": \"https://esm.sh/v132/@types/mdast@4.0.0/index.d.ts\",\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e     \"https://esm.sh/v132/decode-named-character-reference@1.0.2/esnext/decode-named-character-reference.mjs\": \"https://esm.sh/decode-named-character-reference@1.0.2?target=deno\"\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e   }\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e }\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e EOF\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eScaffold Frontend\u003c/h4\u003e\u003ca id=\"user-content-scaffold-frontend\" class=\"anchor\" aria-label=\"Permalink: Scaffold Frontend\" href=\"#scaffold-frontend\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWe use \u003ca href=\"https://ui.shadcn.com/docs\" rel=\"nofollow\"\u003e\u003ccode\u003eshadcn/ui\u003c/code\u003e\u003c/a\u003e for our UI components.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eInitialize \u003ccode\u003eshadcn-ui\u003c/code\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx shadcn-ui@latest init\"\u003e\u003cpre\u003enpx shadcn-ui@latest init\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"Would you like to use TypeScript (recommended)? yes\nWhich style would you like to use? › Default\nWhich color would you like to use as base color? › Slate\nWhere is your global CSS file? › › app/globals.css\nDo you want to use CSS variables for colors? › yes\nWhere is your tailwind.config.js located? › tailwind.config.js\nConfigure the import alias for components: › @/components\nConfigure the import alias for utils: › @/lib/utils\nAre you using React Server Components? › yes\"\u003e\u003cpre\u003eWould you like to use TypeScript (recommended)\u003cspan class=\"pl-k\"\u003e?\u003c/span\u003e yes\nWhich style would you like to use\u003cspan class=\"pl-k\"\u003e?\u003c/span\u003e › Default\nWhich color would you like to use as base color\u003cspan class=\"pl-k\"\u003e?\u003c/span\u003e › Slate\nWhere is your global CSS file\u003cspan class=\"pl-k\"\u003e?\u003c/span\u003e › › app/globals.css\nDo you want to use CSS variables \u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e colors\u003cspan class=\"pl-k\"\u003e?\u003c/span\u003e › yes\nWhere is your tailwind.config.js located\u003cspan class=\"pl-k\"\u003e?\u003c/span\u003e › tailwind.config.js\nConfigure the import \u003cspan class=\"pl-c1\"\u003ealias\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e components: › @/components\nConfigure the import \u003cspan class=\"pl-c1\"\u003ealias\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e utils: › @/lib/utils\nAre you using React Server Components\u003cspan class=\"pl-k\"\u003e?\u003c/span\u003e › yes\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eAdd components.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx shadcn-ui@latest add button input toast\"\u003e\u003cpre\u003enpx shadcn-ui@latest add button input toast\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eInstall dependencies.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npm i @tanstack/react-query three-dots\"\u003e\u003cpre\u003enpm i @tanstack/react-query three-dots\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eWrap the app in a \u003ccode\u003e\u0026lt;QueryClientProvider\u0026gt;\u003c/code\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eBuild layouts.\u003c/p\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/details\u003e\n\u003chr\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e\u003ccode\u003eStep 1\u003c/code\u003e - Storage\u003c/h3\u003e\u003ca id=\"user-content-step-1---storage\" class=\"anchor\" aria-label=\"Permalink: Step 1 - Storage\" href=\"#step-1---storage\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eUse this command to jump to the \u003ccode\u003estep-1\u003c/code\u003e checkpoint.\u003c/em\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"git checkout step-1\"\u003e\u003cpre\u003egit checkout step-1\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWe'll start by handling file uploads. Supabase has a built-in object storage (backed by S3 under the hood) that integrates directly with your Postgres database.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eInstall dependencies\u003c/h4\u003e\u003ca id=\"user-content-install-dependencies\" class=\"anchor\" aria-label=\"Permalink: Install dependencies\" href=\"#install-dependencies\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eFirst install NPM dependencies.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npm i\"\u003e\u003cpre\u003enpm i\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eSetup Supabase stack\u003c/h4\u003e\u003ca id=\"user-content-setup-supabase-stack\" class=\"anchor\" aria-label=\"Permalink: Setup Supabase stack\" href=\"#setup-supabase-stack\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWhen developing a project in Supabase, you can choose to develop locally or directly on the cloud.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch5 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eLocal\u003c/h5\u003e\u003ca id=\"user-content-local\" class=\"anchor\" aria-label=\"Permalink: Local\" href=\"#local\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eStart a local version of Supabase \u003cem\u003e(runs in Docker)\u003c/em\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase start\"\u003e\u003cpre\u003enpx supabase start\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eStore the Supabase URL \u0026amp; public anon key in \u003ccode\u003e.env.local\u003c/code\u003e for Next.js.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase status -o env \\\n  --override-name api.url=NEXT_PUBLIC_SUPABASE_URL \\\n  --override-name auth.anon_key=NEXT_PUBLIC_SUPABASE_ANON_KEY |\n    grep NEXT_PUBLIC \u0026gt; .env.local\"\u003e\u003cpre\u003enpx supabase status -o env \\\n  --override-name api.url=NEXT_PUBLIC_SUPABASE_URL \\\n  --override-name auth.anon_key=NEXT_PUBLIC_SUPABASE_ANON_KEY \u003cspan class=\"pl-k\"\u003e|\u003c/span\u003e\n    grep NEXT_PUBLIC \u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e .env.local\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch5 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eCloud\u003c/h5\u003e\u003ca id=\"user-content-cloud\" class=\"anchor\" aria-label=\"Permalink: Cloud\" href=\"#cloud\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate a Supabase project at \u003ca href=\"https://database.new\" rel=\"nofollow\"\u003ehttps://database.new\u003c/a\u003e, or via the CLI:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase projects create -i \u0026quot;ChatGPT Your Files\u0026quot;\"\u003e\u003cpre\u003enpx supabase projects create -i \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eChatGPT Your Files\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eYour Org ID can be found in the URL after \u003ca href=\"https://supabase.com/dashboard/org/_/general\" rel=\"nofollow\"\u003eselecting an org\u003c/a\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eLink your CLI to the project.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase link --project-ref=\u0026lt;project-id\u0026gt;\"\u003e\u003cpre\u003enpx supabase link --project-ref=\u003cspan class=\"pl-k\"\u003e\u0026lt;\u003c/span\u003eproject-id\u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eYou can get the project ID from the \u003ca href=\"https://supabase.com/dashboard/project/_/settings/general\" rel=\"nofollow\"\u003egeneral settings page\u003c/a\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eStore Supabase URL \u0026amp; public anon key in \u003ccode\u003e.env.local\u003c/code\u003e for Next.js.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"NEXT_PUBLIC_SUPABASE_URL=\u0026lt;api-url\u0026gt;\nNEXT_PUBLIC_SUPABASE_ANON_KEY=\u0026lt;anon-key\u0026gt;\"\u003e\u003cpre\u003eNEXT_PUBLIC_SUPABASE_URL=\u003cspan class=\"pl-k\"\u003e\u0026lt;\u003c/span\u003eapi-url\u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e\nNEXT_PUBLIC_SUPABASE_ANON_KEY=\u003cspan class=\"pl-k\"\u003e\u0026lt;\u003c/span\u003eanon-key\u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eYou can get the project API URL and anonymous key from the \u003ca href=\"https://supabase.com/dashboard/project/_/settings/api\" rel=\"nofollow\"\u003eAPI settings page\u003c/a\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eBuild a SQL migration\u003c/h4\u003e\u003ca id=\"user-content-build-a-sql-migration\" class=\"anchor\" aria-label=\"Permalink: Build a SQL migration\" href=\"#build-a-sql-migration\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate migration file.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase migration new files\"\u003e\u003cpre\u003enpx supabase migration new files\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eA new file will be created under \u003ccode\u003e./supabase/migrations\u003c/code\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eWithin that file, create a private schema.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create schema private;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eschema\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eprivate\u003c/span\u003e;\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eAdd bucket called 'files' via the \u003ccode\u003ebuckets\u003c/code\u003e table in the \u003ccode\u003estorage\u003c/code\u003e schema.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"insert into storage.buckets (id, name)\nvalues ('files', 'files')\non conflict do nothing;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003einsert into\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ebuckets\u003c/span\u003e (id, name)\n\u003cspan class=\"pl-k\"\u003evalues\u003c/span\u003e (\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003efiles\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003efiles\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e)\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e conflict do nothing;\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eAdd RLS policies to restrict access to files.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create policy \u0026quot;Authenticated users can upload files\u0026quot;\non storage.objects for insert to authenticated with check (\n  bucket_id = 'files' and owner = auth.uid()\n);\n\ncreate policy \u0026quot;Users can view their own files\u0026quot;\non storage.objects for select to authenticated using (\n  bucket_id = 'files' and owner = auth.uid()\n);\n\ncreate policy \u0026quot;Users can update their own files\u0026quot;\non storage.objects for update to authenticated with check (\n  bucket_id = 'files' and owner = auth.uid()\n);\n\ncreate policy \u0026quot;Users can delete their own files\u0026quot;\non storage.objects for delete to authenticated using (\n  bucket_id = 'files' and owner = auth.uid()\n);\"\u003e\u003cpre\u003ecreate policy \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eAuthenticated users can upload files\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eobjects\u003c/span\u003e for insert to authenticated with \u003cspan class=\"pl-k\"\u003echeck\u003c/span\u003e (\n  bucket_id \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003efiles\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eand\u003c/span\u003e owner \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e()\n);\n\ncreate policy \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eUsers can view their own files\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eobjects\u003c/span\u003e for \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e to authenticated using (\n  bucket_id \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003efiles\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eand\u003c/span\u003e owner \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e()\n);\n\ncreate policy \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eUsers can update their own files\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eobjects\u003c/span\u003e for \u003cspan class=\"pl-k\"\u003eupdate\u003c/span\u003e to authenticated with \u003cspan class=\"pl-k\"\u003echeck\u003c/span\u003e (\n  bucket_id \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003efiles\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eand\u003c/span\u003e owner \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e()\n);\n\ncreate policy \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eUsers can delete their own files\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eobjects\u003c/span\u003e for \u003cspan class=\"pl-k\"\u003edelete\u003c/span\u003e to authenticated using (\n  bucket_id \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003efiles\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eand\u003c/span\u003e owner \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e()\n);\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eModify frontend\u003c/h4\u003e\u003ca id=\"user-content-modify-frontend\" class=\"anchor\" aria-label=\"Permalink: Modify frontend\" href=\"#modify-frontend\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eNext let's update \u003ccode\u003e./app/files/page.tsx\u003c/code\u003e to support file upload.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eSetup Supabase client at the top of the component.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const supabase = createClientComponentClient();\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ecreateClientComponentClient\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eHandle file upload in the \u003ccode\u003e\u0026lt;Input\u0026gt;\u003c/code\u003e's \u003ccode\u003eonChange\u003c/code\u003e prop.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"await supabase.storage\n  .from('files')\n  .upload(`${crypto.randomUUID()}/${selectedFile.name}`, selectedFile);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003efrom\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'files'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eupload\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e`\u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ecrypto\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003erandomUUID\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e/\u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eselectedFile\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003ename\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e`\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eselectedFile\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eImprove upload RLS policy\u003c/h4\u003e\u003ca id=\"user-content-improve-upload-rls-policy\" class=\"anchor\" aria-label=\"Permalink: Improve upload RLS policy\" href=\"#improve-upload-rls-policy\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWe can improve our previous RLS policy to require a UUID in the uploaded file path.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate \u003ccode\u003euuid_or_null()\u003c/code\u003e function.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create or replace function private.uuid_or_null(str text)\nreturns uuid\nlanguage plpgsql\nas $$\nbegin\n  return str::uuid;\n  exception when invalid_text_representation then\n    return null;\n  end;\n$$;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate or replace\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efunction\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eprivate\u003c/span\u003e.uuid_or_null(str \u003cspan class=\"pl-k\"\u003etext\u003c/span\u003e)\nreturns uuid\nlanguage plpgsql\n\u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e $$\n\u003cspan class=\"pl-k\"\u003ebegin\u003c/span\u003e\n  return str::uuid;\n  exception when invalid_text_representation then\n    return \u003cspan class=\"pl-k\"\u003enull\u003c/span\u003e;\n  end;\n$$;\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eModify insert policy to check for UUID in the first path segment \u003cem\u003e(Postgres arrays are 1-based)\u003c/em\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create policy \u0026quot;Authenticated users can upload files\u0026quot;\non storage.objects for insert to authenticated with check (\n  bucket_id = 'files' and\n    owner = auth.uid() and\n    private.uuid_or_null(path_tokens[1]) is not null\n);\"\u003e\u003cpre\u003ecreate policy \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eAuthenticated users can upload files\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eobjects\u003c/span\u003e for insert to authenticated with \u003cspan class=\"pl-k\"\u003echeck\u003c/span\u003e (\n  bucket_id \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003efiles\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eand\u003c/span\u003e\n    owner \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e() \u003cspan class=\"pl-k\"\u003eand\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eprivate\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euuid_or_null\u003c/span\u003e(path_tokens[\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e]) \u003cspan class=\"pl-k\"\u003eis not null\u003c/span\u003e\n);\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eApply the migration to our local database.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase migration up\"\u003e\u003cpre\u003enpx supabase migration up\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eor if you are developing directly on the cloud, push your migrations up:\u003c/p\u003e\n\u003cdiv class=\"snippet-clipboard-content notranslate position-relative overflow-auto\" data-snippet-clipboard-copy-content=\"npx supabase db push\"\u003e\u003cpre class=\"notranslate\"\u003e\u003ccode\u003enpx supabase db push\n\u003c/code\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003chr\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e\u003ccode\u003eStep 2\u003c/code\u003e - Documents\u003c/h3\u003e\u003ca id=\"user-content-step-2---documents\" class=\"anchor\" aria-label=\"Permalink: Step 2 - Documents\" href=\"#step-2---documents\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eJump to a step:\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"#step-1---storage\"\u003eStorage\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-2---documents\"\u003eDocuments\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-3---embeddings\"\u003eEmbeddings\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-4---chat\"\u003eChat\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-5---database-types-bonus\"\u003eDatabase Types\u003c/a\u003e (Bonus)\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#youre-done\"\u003eYou're done!\u003c/a\u003e\u003c/li\u003e\n\u003c/ol\u003e\n\u003chr\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eUse these commands to jump to the \u003ccode\u003estep-2\u003c/code\u003e checkpoint.\u003c/em\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"git stash push -u -m \u0026quot;my work on step-1\u0026quot;\ngit checkout step-2\"\u003e\u003cpre\u003egit stash push -u -m \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003emy work on step-1\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\ngit checkout step-2\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eNext we'll need to process our files for retrieval augmented generation (RAG). Specifically we'll split the contents of our markdown documents by heading, which will allow us to query smaller and more meaningful sections.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eLet's create a \u003ccode\u003edocuments\u003c/code\u003e and \u003ccode\u003edocument_sections\u003c/code\u003e table to store our processed files.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca target=\"_blank\" rel=\"noopener noreferrer\" href=\"/supabase-community/chatgpt-your-files/blob/main/assets/step-2-er-diagram.png\"\u003e\u003cimg src=\"/supabase-community/chatgpt-your-files/raw/main/assets/step-2-er-diagram.png\" alt=\"Documents ER diagram\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eAdd a new SQL migration\u003c/h4\u003e\u003ca id=\"user-content-add-a-new-sql-migration\" class=\"anchor\" aria-label=\"Permalink: Add a new SQL migration\" href=\"#add-a-new-sql-migration\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate migration file.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase migration new documents\"\u003e\u003cpre\u003enpx supabase migration new documents\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eEnable \u003ccode\u003epgvector\u003c/code\u003e and \u003ccode\u003epg_net\u003c/code\u003e extensions.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eWe'll use \u003ccode\u003epg_net\u003c/code\u003e later to send HTTP requests to our edge functions.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create extension if not exists pg_net with schema extensions;\ncreate extension if not exists vector with schema extensions;\"\u003e\u003cpre\u003ecreate extension if not exists pg_net with schema extensions;\ncreate extension if not exists vector with schema extensions;\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate \u003ccode\u003edocuments\u003c/code\u003e table.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create table documents (\n  id bigint primary key generated always as identity,\n  name text not null,\n  storage_object_id uuid not null references storage.objects (id),\n  created_by uuid not null references auth.users (id) default auth.uid(),\n  created_at timestamp with time zone not null default now()\n);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003etable\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edocuments\u003c/span\u003e (\n  id \u003cspan class=\"pl-k\"\u003ebigint\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eprimary key\u003c/span\u003e generated always \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e identity,\n  name \u003cspan class=\"pl-k\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enot null\u003c/span\u003e,\n  storage_object_id uuid \u003cspan class=\"pl-k\"\u003enot null\u003c/span\u003e \u003cspan class=\"pl-k\"\u003ereferences\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eobjects\u003c/span\u003e (id),\n  created_by uuid \u003cspan class=\"pl-k\"\u003enot null\u003c/span\u003e \u003cspan class=\"pl-k\"\u003ereferences\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eusers\u003c/span\u003e (id) default \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e(),\n  created_at \u003cspan class=\"pl-k\"\u003etimestamp with time zone\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enot null\u003c/span\u003e default now()\n);\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eWe'll also create a view \u003ccode\u003edocuments_with_storage_path\u003c/code\u003e that provides easy access to the storage object path.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create view documents_with_storage_path\nwith (security_invoker=true)\nas\n  select documents.*, storage.objects.name as storage_object_path\n  from documents\n  join storage.objects\n    on storage.objects.id = documents.storage_object_id;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eview\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edocuments_with_storage_path\u003c/span\u003e\nwith (security_invoker\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003etrue)\n\u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e documents.\u003cspan class=\"pl-k\"\u003e*\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eobjects\u003c/span\u003e.name \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e storage_object_path\n  \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e documents\n  \u003cspan class=\"pl-k\"\u003ejoin\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eobjects\u003c/span\u003e\n    \u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eobjects\u003c/span\u003e.id \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003edocuments\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003estorage_object_id\u003c/span\u003e;\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate \u003ccode\u003edocument_sections\u003c/code\u003e table.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create table document_sections (\n  id bigint primary key generated always as identity,\n  document_id bigint not null references documents (id),\n  content text not null,\n  embedding vector (384)\n);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003etable\u003c/span\u003e \u003cspan class=\"pl-en\"\u003edocument_sections\u003c/span\u003e (\n  id \u003cspan class=\"pl-k\"\u003ebigint\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eprimary key\u003c/span\u003e generated always \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e identity,\n  document_id \u003cspan class=\"pl-k\"\u003ebigint\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enot null\u003c/span\u003e \u003cspan class=\"pl-k\"\u003ereferences\u003c/span\u003e documents (id),\n  content \u003cspan class=\"pl-k\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enot null\u003c/span\u003e,\n  embedding vector (\u003cspan class=\"pl-c1\"\u003e384\u003c/span\u003e)\n);\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: Since the video was published, \u003ccode\u003eon delete cascade\u003c/code\u003e was\nadded as a new migration so that the lifecycle of \u003ccode\u003edocument_sections\u003c/code\u003e\nis tied to their respective document.\u003c/em\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"alter table document_sections\ndrop constraint document_sections_document_id_fkey,\nadd constraint document_sections_document_id_fkey\n  foreign key (document_id)\n  references documents(id)\n  on delete cascade;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ealter\u003c/span\u003e \u003cspan class=\"pl-k\"\u003etable\u003c/span\u003e document_sections\ndrop \u003cspan class=\"pl-k\"\u003econstraint\u003c/span\u003e document_sections_document_id_fkey,\nadd \u003cspan class=\"pl-k\"\u003econstraint\u003c/span\u003e document_sections_document_id_fkey\n  \u003cspan class=\"pl-k\"\u003eforeign key\u003c/span\u003e (document_id)\n  \u003cspan class=\"pl-k\"\u003ereferences\u003c/span\u003e documents(id)\n  \u003cspan class=\"pl-k\"\u003eon delete cascade\u003c/span\u003e;\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eAdd HNSW index.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eUnlike IVFFlat indexes, HNSW indexes can be create immediately on an empty table.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create index on document_sections using hnsw (embedding vector_ip_ops);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eindex\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eon\u003c/span\u003e document_sections using hnsw (embedding vector_ip_ops);\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eSetup RLS to control who has access to which documents.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"alter table documents enable row level security;\nalter table document_sections enable row level security;\n\ncreate policy \u0026quot;Users can insert documents\u0026quot;\non documents for insert to authenticated with check (\n  auth.uid() = created_by\n);\n\ncreate policy \u0026quot;Users can query their own documents\u0026quot;\non documents for select to authenticated using (\n  auth.uid() = created_by\n);\n\ncreate policy \u0026quot;Users can insert document sections\u0026quot;\non document_sections for insert to authenticated with check (\n  document_id in (\n    select id\n    from documents\n    where created_by = auth.uid()\n  )\n);\n\ncreate policy \u0026quot;Users can update their own document sections\u0026quot;\non document_sections for update to authenticated using (\n  document_id in (\n    select id\n    from documents\n    where created_by = auth.uid()\n  )\n) with check (\n  document_id in (\n    select id\n    from documents\n    where created_by = auth.uid()\n  )\n);\n\ncreate policy \u0026quot;Users can query their own document sections\u0026quot;\non document_sections for select to authenticated using (\n  document_id in (\n    select id\n    from documents\n    where created_by = auth.uid()\n  )\n);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ealter\u003c/span\u003e \u003cspan class=\"pl-k\"\u003etable\u003c/span\u003e documents enable row level security;\n\u003cspan class=\"pl-k\"\u003ealter\u003c/span\u003e \u003cspan class=\"pl-k\"\u003etable\u003c/span\u003e document_sections enable row level security;\n\ncreate policy \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eUsers can insert documents\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e documents for insert to authenticated with \u003cspan class=\"pl-k\"\u003echeck\u003c/span\u003e (\n  \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e() \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e created_by\n);\n\ncreate policy \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eUsers can query their own documents\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e documents for \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e to authenticated using (\n  \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e() \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e created_by\n);\n\ncreate policy \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eUsers can insert document sections\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e document_sections for insert to authenticated with \u003cspan class=\"pl-k\"\u003echeck\u003c/span\u003e (\n  document_id \u003cspan class=\"pl-k\"\u003ein\u003c/span\u003e (\n    \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e id\n    \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e documents\n    \u003cspan class=\"pl-k\"\u003ewhere\u003c/span\u003e created_by \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e()\n  )\n);\n\ncreate policy \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eUsers can update their own document sections\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e document_sections for \u003cspan class=\"pl-k\"\u003eupdate\u003c/span\u003e to authenticated using (\n  document_id \u003cspan class=\"pl-k\"\u003ein\u003c/span\u003e (\n    \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e id\n    \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e documents\n    \u003cspan class=\"pl-k\"\u003ewhere\u003c/span\u003e created_by \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e()\n  )\n) with \u003cspan class=\"pl-k\"\u003echeck\u003c/span\u003e (\n  document_id \u003cspan class=\"pl-k\"\u003ein\u003c/span\u003e (\n    \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e id\n    \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e documents\n    \u003cspan class=\"pl-k\"\u003ewhere\u003c/span\u003e created_by \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e()\n  )\n);\n\ncreate policy \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eUsers can query their own document sections\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e document_sections for \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e to authenticated using (\n  document_id \u003cspan class=\"pl-k\"\u003ein\u003c/span\u003e (\n    \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e id\n    \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e documents\n    \u003cspan class=\"pl-k\"\u003ewhere\u003c/span\u003e created_by \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003euid\u003c/span\u003e()\n  )\n);\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eIf developing locally, add \u003ccode\u003esupabase_url\u003c/code\u003e secret to \u003ccode\u003e./supabase/seed.sql\u003c/code\u003e. We will use this to query our Edge Functions within our local environment.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"select vault.create_secret(\n  'http://api.supabase.internal:8000',\n  'supabase_url'\n);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003evault\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate_secret\u003c/span\u003e(\n  \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003ehttp://api.supabase.internal:8000\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e,\n  \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003esupabase_url\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e\n);\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eIf you are developing directly on the cloud, open up the \u003ca href=\"https://supabase.com/dashboard/project/_/sql/new\" rel=\"nofollow\"\u003eSQL Editor\u003c/a\u003e and set this to your Supabase project's API URL:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"select vault.create_secret(\n  '\u0026lt;api-url\u0026gt;',\n  'supabase_url'\n);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003evault\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ecreate_secret\u003c/span\u003e(\n  \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u0026lt;api-url\u0026gt;\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e,\n  \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003esupabase_url\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e\n);\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eYou can get the project API URL from the \u003ca href=\"https://supabase.com/dashboard/project/_/settings/api\" rel=\"nofollow\"\u003eAPI settings page\u003c/a\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate a function to retrieve the URL.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create function supabase_url()\nreturns text\nlanguage plpgsql\nsecurity definer\nas $$\ndeclare\n  secret_value text;\nbegin\n  select decrypted_secret into secret_value from vault.decrypted_secrets where name = 'supabase_url';\n  return secret_value;\nend;\n$$;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efunction\u003c/span\u003e \u003cspan class=\"pl-en\"\u003esupabase_url\u003c/span\u003e()\nreturns \u003cspan class=\"pl-k\"\u003etext\u003c/span\u003e\nlanguage plpgsql\nsecurity definer\n\u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e $$\ndeclare\n  secret_value \u003cspan class=\"pl-k\"\u003etext\u003c/span\u003e;\n\u003cspan class=\"pl-k\"\u003ebegin\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e decrypted_secret into secret_value \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003evault\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003edecrypted_secrets\u003c/span\u003e \u003cspan class=\"pl-k\"\u003ewhere\u003c/span\u003e name \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003esupabase_url\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e;\n  return secret_value;\nend;\n$$;\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate a trigger to process new documents when they're inserted. This uses \u003ccode\u003epg_net\u003c/code\u003e to send an HTTP request to our Edge Function (coming up next).\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create function private.handle_storage_update()\nreturns trigger\nlanguage plpgsql\nas $$\ndeclare\n  document_id bigint;\n  result int;\nbegin\n  insert into documents (name, storage_object_id, created_by)\n    values (new.path_tokens[2], new.id, new.owner)\n    returning id into document_id;\n\n  select\n    net.http_post(\n      url := supabase_url() || '/functions/v1/process',\n      headers := jsonb_build_object(\n        'Content-Type', 'application/json',\n        'Authorization', current_setting('request.headers')::json-\u0026gt;\u0026gt;'authorization'\n      ),\n      body := jsonb_build_object(\n        'document_id', document_id\n      )\n    )\n  into result;\n\n  return null;\nend;\n$$;\n\ncreate trigger on_file_upload\n  after insert on storage.objects\n  for each row\n  execute procedure private.handle_storage_update();\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efunction\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eprivate\u003c/span\u003e.handle_storage_update()\nreturns trigger\nlanguage plpgsql\n\u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e $$\ndeclare\n  document_id \u003cspan class=\"pl-k\"\u003ebigint\u003c/span\u003e;\n  result \u003cspan class=\"pl-k\"\u003eint\u003c/span\u003e;\n\u003cspan class=\"pl-k\"\u003ebegin\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003einsert into\u003c/span\u003e documents (name, storage_object_id, created_by)\n    \u003cspan class=\"pl-k\"\u003evalues\u003c/span\u003e (\u003cspan class=\"pl-c1\"\u003enew\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003epath_tokens\u003c/span\u003e[\u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e], \u003cspan class=\"pl-c1\"\u003enew\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eid\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003enew\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eowner\u003c/span\u003e)\n    returning id into document_id;\n\n  \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003enet\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ehttp_post\u003c/span\u003e(\n      url :\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e supabase_url() \u003cspan class=\"pl-k\"\u003e||\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e/functions/v1/process\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e,\n      headers :\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e jsonb_build_object(\n        \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003eContent-Type\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003eapplication/json\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e,\n        \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003eAuthorization\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e, current_setting(\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003erequest.headers\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e)::json\u003cspan class=\"pl-k\"\u003e-\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e\u0026gt;\u0026gt;\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003eauthorization\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e\n      ),\n      body :\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e jsonb_build_object(\n        \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003edocument_id\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e, document_id\n      )\n    )\n  into result;\n\n  return \u003cspan class=\"pl-k\"\u003enull\u003c/span\u003e;\nend;\n$$;\n\n\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003etrigger\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eon_file_upload\u003c/span\u003e\n  after insert \u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eobjects\u003c/span\u003e\n  for each row\n  execute procedure \u003cspan class=\"pl-c1\"\u003eprivate\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ehandle_storage_update\u003c/span\u003e();\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eApply the migration to our local database.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase migration up\"\u003e\u003cpre\u003enpx supabase migration up\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eor if you are developing directly on the cloud, push your migrations up:\u003c/p\u003e\n\u003cdiv class=\"snippet-clipboard-content notranslate position-relative overflow-auto\" data-snippet-clipboard-copy-content=\"npx supabase db push\"\u003e\u003cpre class=\"notranslate\"\u003e\u003ccode\u003enpx supabase db push\n\u003c/code\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eEdge function for \u003ccode\u003eprocess\u003c/code\u003e\u003c/h4\u003e\u003ca id=\"user-content-edge-function-for-process\" class=\"anchor\" aria-label=\"Permalink: Edge function for process\" href=\"#edge-function-for-process\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate the Edge Function file.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase functions new process\"\u003e\u003cpre\u003enpx supabase functions new process\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThis will create the file \u003ccode\u003e./supabase/functions/process/index.ts\u003c/code\u003e.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eMake sure you have the latest version of \u003ccode\u003edeno\u003c/code\u003e installed\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"brew install deno\"\u003e\u003cpre\u003ebrew install deno\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eFirst let's note how dependencies are resolved using an import map - \u003ccode\u003e./supabase/functions/import_map.json\u003c/code\u003e.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eImport maps aren't required in Deno, but they can simplify imports and keep dependency versions consistent. All of our dependencies come from NPM, but since we're using Deno we fetch them from a CDN like \u003ca href=\"https://esm.sh\" rel=\"nofollow\"\u003ehttps://esm.sh\u003c/a\u003e or \u003ca href=\"https://cdn.jsdelivr.net\" rel=\"nofollow\"\u003ehttps://cdn.jsdelivr.net\u003c/a\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-json notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"{\n  \u0026quot;imports\u0026quot;: {\n    \u0026quot;@std/\u0026quot;: \u0026quot;https://deno.land/std@0.168.0/\u0026quot;,\n\n    \u0026quot;@supabase/supabase-js\u0026quot;: \u0026quot;https://esm.sh/@supabase/supabase-js@2.21.0\u0026quot;,\n    \u0026quot;openai\u0026quot;: \u0026quot;https://esm.sh/openai@4.10.0\u0026quot;,\n    \u0026quot;common-tags\u0026quot;: \u0026quot;https://esm.sh/common-tags@1.8.2\u0026quot;,\n    \u0026quot;ai\u0026quot;: \u0026quot;https://esm.sh/ai@2.2.13\u0026quot;,\n\n    \u0026quot;mdast-util-from-markdown\u0026quot;: \u0026quot;https://esm.sh/mdast-util-from-markdown@2.0.0\u0026quot;,\n    \u0026quot;mdast-util-to-markdown\u0026quot;: \u0026quot;https://esm.sh/mdast-util-to-markdown@2.1.0\u0026quot;,\n    \u0026quot;mdast-util-to-string\u0026quot;: \u0026quot;https://esm.sh/mdast-util-to-string@4.0.0\u0026quot;,\n    \u0026quot;unist-builder\u0026quot;: \u0026quot;https://esm.sh/unist-builder@4.0.0\u0026quot;,\n    \u0026quot;mdast\u0026quot;: \u0026quot;https://esm.sh/v132/@types/mdast@4.0.0/index.d.ts\u0026quot;,\n\n    \u0026quot;https://esm.sh/v132/decode-named-character-reference@1.0.2/esnext/decode-named-character-reference.mjs\u0026quot;: \u0026quot;https://esm.sh/decode-named-character-reference@1.0.2?target=deno\u0026quot;\n  }\n}\"\u003e\u003cpre\u003e{\n  \u003cspan class=\"pl-ent\"\u003e\"imports\"\u003c/span\u003e: {\n    \u003cspan class=\"pl-ent\"\u003e\"@std/\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://deno.land/std@0.168.0/\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e,\n\n    \u003cspan class=\"pl-ent\"\u003e\"@supabase/supabase-js\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://esm.sh/@supabase/supabase-js@2.21.0\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-ent\"\u003e\"openai\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://esm.sh/openai@4.10.0\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-ent\"\u003e\"common-tags\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://esm.sh/common-tags@1.8.2\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-ent\"\u003e\"ai\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://esm.sh/ai@2.2.13\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e,\n\n    \u003cspan class=\"pl-ent\"\u003e\"mdast-util-from-markdown\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://esm.sh/mdast-util-from-markdown@2.0.0\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-ent\"\u003e\"mdast-util-to-markdown\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://esm.sh/mdast-util-to-markdown@2.1.0\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-ent\"\u003e\"mdast-util-to-string\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://esm.sh/mdast-util-to-string@4.0.0\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-ent\"\u003e\"unist-builder\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://esm.sh/unist-builder@4.0.0\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e,\n    \u003cspan class=\"pl-ent\"\u003e\"mdast\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://esm.sh/v132/@types/mdast@4.0.0/index.d.ts\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e,\n\n    \u003cspan class=\"pl-ent\"\u003e\"https://esm.sh/v132/decode-named-character-reference@1.0.2/esnext/decode-named-character-reference.mjs\"\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003ehttps://esm.sh/decode-named-character-reference@1.0.2?target=deno\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\n  }\n}\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: URL based imports and import maps aren't a Deno invention. These are a \u003ca href=\"https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script/type/importmap\" rel=\"nofollow\"\u003eweb standard\u003c/a\u003e that Deno follows as closely as possible.\u003c/em\u003e\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eIn \u003ccode\u003eprocess/index.ts\u003c/code\u003e, first grab the Supabase environment variables.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import { createClient } from '@supabase/supabase-js';\nimport { processMarkdown } from '../_lib/markdown-parser.ts';\n\n// These are automatically injected\nconst supabaseUrl = Deno.env.get('SUPABASE_URL');\nconst supabaseAnonKey = Deno.env.get('SUPABASE_ANON_KEY');\n\nDeno.serve(async (req) =\u0026gt; {\n  if (!supabaseUrl || !supabaseAnonKey) {\n    return new Response(\n      JSON.stringify({\n        error: 'Missing environment variables.',\n      }),\n      {\n        status: 500,\n        headers: { 'Content-Type': 'application/json' },\n      }\n    );\n  }\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ecreateClient\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'@supabase/supabase-js'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eprocessMarkdown\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'../_lib/markdown-parser.ts'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e// These are automatically injected\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabaseUrl\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDeno\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eenv\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eget\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'SUPABASE_URL'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabaseAnonKey\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDeno\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eenv\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eget\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'SUPABASE_ANON_KEY'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-v\"\u003eDeno\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eserve\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-k\"\u003easync\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ereq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u0026gt;\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esupabaseUrl\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e||\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esupabaseAnonKey\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n        \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'Missing environment variables.'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n        \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n        \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: These environment variables are automatically injected into the edge runtime for you. Even so, we check for their existence as a TypeScript best practice (type narrowing).\u003c/em\u003e\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003e(Optional)\u003c/em\u003e If you are using VS Code, you may get prompted to cache your imported dependencies. You can do this by hitting \u003ccode\u003ecmd\u003c/code\u003e+\u003ccode\u003eshift\u003c/code\u003e+\u003ccode\u003ep\u003c/code\u003e and type \u003ccode\u003e\u0026gt;Deno: Cache Dependencies\u003c/code\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate Supabase client and configure it to inherit the original user’s permissions via the authorization header. This way we can continue to take advantage of our RLS policies.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const authorization = req.headers.get('Authorization');\n\nif (!authorization) {\n  return new Response(\n    JSON.stringify({ error: `No authorization header passed` }),\n    {\n      status: 500,\n      headers: { 'Content-Type': 'application/json' },\n    }\n  );\n}\n\nconst supabase = createClient(supabaseUrl, supabaseAnonKey, {\n  global: {\n    headers: {\n      authorization,\n    },\n  },\n  auth: {\n    persistSession: false,\n  },\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eauthorization\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ereq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eget\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'Authorization'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eauthorization\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e`No authorization header passed`\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ecreateClient\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esupabaseUrl\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabaseAnonKey\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eglobal\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      authorization\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003epersistSession\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003efalse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eGrab the \u003ccode\u003edocument_id\u003c/code\u003e from the request body and query it.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const { document_id } = await req.json();\n\nconst { data: document } = await supabase\n  .from('documents_with_storage_path')\n  .select()\n  .eq('id', document_id)\n  .single();\n\nif (!document?.storage_object_path) {\n  return new Response(\n    JSON.stringify({ error: 'Failed to find uploaded document' }),\n    {\n      status: 500,\n      headers: { 'Content-Type': 'application/json' },\n    }\n  );\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e document_id \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ereq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003ejson\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003edata\u003c/span\u003e: \u003cspan class=\"pl-smi\"\u003edocument\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003efrom\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'documents_with_storage_path'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eselect\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eeq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'id'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edocument_id\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003esingle\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-smi\"\u003edocument\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e?.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003estorage_object_path\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'Failed to find uploaded document'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eUse the Supabase client to download the file by storage path.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const { data: file } = await supabase.storage\n  .from('files')\n  .download(document.storage_object_path);\n\nif (!file) {\n  return new Response(\n    JSON.stringify({ error: 'Failed to download storage object' }),\n    {\n      status: 500,\n      headers: { 'Content-Type': 'application/json' },\n    }\n  );\n}\n\nconst fileContents = await file.text();\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003edata\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003efile\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003efrom\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'files'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003edownload\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-smi\"\u003edocument\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003estorage_object_path\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003efile\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'Failed to download storage object'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003efileContents\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003efile\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003etext\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eProcess the markdown file and store the resulting subsections into the \u003ccode\u003edocument_sections\u003c/code\u003e table.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: \u003ccode\u003eprocessMarkdown()\u003c/code\u003e is pre-built into this repository for convenience. Feel free to read through its code to learn how it splits the markdown content.\u003c/em\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const processedMd = processMarkdown(fileContents);\n\nconst { error } = await supabase.from('document_sections').insert(\n  processedMd.sections.map(({ content }) =\u0026gt; ({\n    document_id,\n    content,\n  }))\n);\n\nif (error) {\n  console.error(error);\n  return new Response(\n    JSON.stringify({ error: 'Failed to save document sections' }),\n    {\n      status: 500,\n      headers: { 'Content-Type': 'application/json' },\n    }\n  );\n}\n\nconsole.log(\n  `Saved ${processedMd.sections.length} sections for file '${document.name}'`\n);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eprocessedMd\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eprocessMarkdown\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003efileContents\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e error \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003efrom\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'document_sections'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003einsert\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n  \u003cspan class=\"pl-s1\"\u003eprocessedMd\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003esections\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003emap\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e content \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u0026gt;\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    document_id\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    content\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eerror\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-smi\"\u003econsole\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eerror\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eerror\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'Failed to save document sections'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n\u003cspan class=\"pl-smi\"\u003econsole\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003elog\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n  \u003cspan class=\"pl-s\"\u003e`Saved \u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eprocessedMd\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003esections\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003elength\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e sections for file '\u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-smi\"\u003edocument\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003ename\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e'`\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eReturn a success response.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"return new Response(null, {\n  status: 204,\n  headers: { 'Content-Type': 'application/json' },\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003enull\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e204\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eIf developing locally, open a new terminal and serve the edge functions.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase functions serve\"\u003e\u003cpre\u003enpx supabase functions serve\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: Local Edge Functions are automatically served as part of \u003ccode\u003enpx supabase start\u003c/code\u003e, but this command allows us to also monitor their logs.\u003c/em\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eIf you're developing directly on the cloud, deploy your edge function:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase functions deploy\"\u003e\u003cpre\u003enpx supabase functions deploy\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eDisplay documents on the frontend\u003c/h4\u003e\u003ca id=\"user-content-display-documents-on-the-frontend\" class=\"anchor\" aria-label=\"Permalink: Display documents on the frontend\" href=\"#display-documents-on-the-frontend\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eLet's update \u003ccode\u003e./app/files/page.tsx\u003c/code\u003e to list out the uploaded documents.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eAt the top of the component, fetch documents using the \u003ccode\u003euseQuery\u003c/code\u003e hook:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const { data: documents } = useQuery(['files'], async () =\u0026gt; {\n  const { data, error } = await supabase\n    .from('documents_with_storage_path')\n    .select();\n\n  if (error) {\n    toast({\n      variant: 'destructive',\n      description: 'Failed to fetch documents',\n    });\n    throw error;\n  }\n\n  return data;\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003edata\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003edocuments\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003euseQuery\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e[\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'files'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e]\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-k\"\u003easync\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u0026gt;\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e data\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e error \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003efrom\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'documents_with_storage_path'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eselect\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n  \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eerror\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-en\"\u003etoast\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003evariant\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'destructive'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003edescription\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'Failed to fetch documents'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n    \u003cspan class=\"pl-k\"\u003ethrow\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eerror\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edata\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eIn each document's \u003ccode\u003eonClick\u003c/code\u003e handler, download the respective file.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const { data, error } = await supabase.storage\n  .from('files')\n  .createSignedUrl(document.storage_object_path, 60);\n\nif (error) {\n  toast({\n    variant: 'destructive',\n    description: 'Failed to download file. Please try again.',\n  });\n  return;\n}\n\nwindow.location.href = data.signedUrl;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e data\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e error \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003estorage\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003efrom\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'files'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003ecreateSignedUrl\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-smi\"\u003edocument\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003estorage_object_path\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e60\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eerror\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-en\"\u003etoast\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003evariant\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'destructive'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003edescription\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'Failed to download file. Please try again.'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n\u003cspan class=\"pl-smi\"\u003ewindow\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003elocation\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003ehref\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edata\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003esignedUrl\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003chr\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e\u003ccode\u003eStep 3\u003c/code\u003e - Embeddings\u003c/h3\u003e\u003ca id=\"user-content-step-3---embeddings\" class=\"anchor\" aria-label=\"Permalink: Step 3 - Embeddings\" href=\"#step-3---embeddings\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eJump to a step:\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"#step-1---storage\"\u003eStorage\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-2---documents\"\u003eDocuments\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-3---embeddings\"\u003eEmbeddings\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-4---chat\"\u003eChat\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-5---database-types-bonus\"\u003eDatabase Types\u003c/a\u003e (Bonus)\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#youre-done\"\u003eYou're done!\u003c/a\u003e\u003c/li\u003e\n\u003c/ol\u003e\n\u003chr\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eUse these commands to jump to the \u003ccode\u003estep-3\u003c/code\u003e checkpoint.\u003c/em\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"git stash push -u -m \u0026quot;my work on step-2\u0026quot;\ngit checkout step-3\"\u003e\u003cpre\u003egit stash push -u -m \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003emy work on step-2\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\ngit checkout step-3\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eNow let's add logic to generate embeddings automatically anytime new rows are added to the \u003ccode\u003edocument_sections\u003c/code\u003e table.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eCreate SQL migration\u003c/h4\u003e\u003ca id=\"user-content-create-sql-migration\" class=\"anchor\" aria-label=\"Permalink: Create SQL migration\" href=\"#create-sql-migration\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate migration file\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase migration new embed\"\u003e\u003cpre\u003enpx supabase migration new embed\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate \u003ccode\u003eembed()\u003c/code\u003e trigger function. We'll use this general purpose trigger function to asynchronously generate embeddings on arbitrary tables using a new \u003ccode\u003eembed\u003c/code\u003e Edge Function (coming up).\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create function private.embed()\nreturns trigger\nlanguage plpgsql\nas $$\ndeclare\n  content_column text = TG_ARGV[0];\n  embedding_column text = TG_ARGV[1];\n  batch_size int = case when array_length(TG_ARGV, 1) \u0026gt;= 3 then TG_ARGV[2]::int else 5 end;\n  timeout_milliseconds int = case when array_length(TG_ARGV, 1) \u0026gt;= 4 then TG_ARGV[3]::int else 5 * 60 * 1000 end;\n  batch_count int = ceiling((select count(*) from inserted) / batch_size::float);\nbegin\n  -- Loop through each batch and invoke an edge function to handle the embedding generation\n  for i in 0 .. (batch_count-1) loop\n  perform\n    net.http_post(\n      url := supabase_url() || '/functions/v1/embed',\n      headers := jsonb_build_object(\n        'Content-Type', 'application/json',\n        'Authorization', current_setting('request.headers')::json-\u0026gt;\u0026gt;'authorization'\n      ),\n      body := jsonb_build_object(\n        'ids', (select json_agg(ds.id) from (select id from inserted limit batch_size offset i*batch_size) ds),\n        'table', TG_TABLE_NAME,\n        'contentColumn', content_column,\n        'embeddingColumn', embedding_column\n      ),\n      timeout_milliseconds := timeout_milliseconds\n    );\n  end loop;\n\n  return null;\nend;\n$$;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efunction\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eprivate\u003c/span\u003e.embed()\nreturns trigger\nlanguage plpgsql\n\u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e $$\ndeclare\n  content_column \u003cspan class=\"pl-k\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e TG_ARGV[\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e];\n  embedding_column \u003cspan class=\"pl-k\"\u003etext\u003c/span\u003e \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e TG_ARGV[\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e];\n  batch_size \u003cspan class=\"pl-k\"\u003eint\u003c/span\u003e \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e case when array_length(TG_ARGV, \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e) \u003cspan class=\"pl-k\"\u003e\u0026gt;=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e then TG_ARGV[\u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e]::\u003cspan class=\"pl-k\"\u003eint\u003c/span\u003e else \u003cspan class=\"pl-c1\"\u003e5\u003c/span\u003e end;\n  timeout_milliseconds \u003cspan class=\"pl-k\"\u003eint\u003c/span\u003e \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e case when array_length(TG_ARGV, \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e) \u003cspan class=\"pl-k\"\u003e\u0026gt;=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e4\u003c/span\u003e then TG_ARGV[\u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e]::\u003cspan class=\"pl-k\"\u003eint\u003c/span\u003e else \u003cspan class=\"pl-c1\"\u003e5\u003c/span\u003e \u003cspan class=\"pl-k\"\u003e*\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e60\u003c/span\u003e \u003cspan class=\"pl-k\"\u003e*\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1000\u003c/span\u003e end;\n  batch_count \u003cspan class=\"pl-k\"\u003eint\u003c/span\u003e \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e ceiling((\u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ecount\u003c/span\u003e(\u003cspan class=\"pl-k\"\u003e*\u003c/span\u003e) \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e inserted) \u003cspan class=\"pl-k\"\u003e/\u003c/span\u003e batch_size::float);\n\u003cspan class=\"pl-k\"\u003ebegin\u003c/span\u003e\n  \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e--\u003c/span\u003e Loop through each batch and invoke an edge function to handle the embedding generation\u003c/span\u003e\n  for i \u003cspan class=\"pl-k\"\u003ein\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e .. (batch_count\u003cspan class=\"pl-k\"\u003e-\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e) loop\n  perform\n    \u003cspan class=\"pl-c1\"\u003enet\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003ehttp_post\u003c/span\u003e(\n      url :\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e supabase_url() \u003cspan class=\"pl-k\"\u003e||\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e/functions/v1/embed\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e,\n      headers :\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e jsonb_build_object(\n        \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003eContent-Type\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003eapplication/json\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e,\n        \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003eAuthorization\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e, current_setting(\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003erequest.headers\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e)::json\u003cspan class=\"pl-k\"\u003e-\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e\u0026gt;\u0026gt;\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003eauthorization\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e\n      ),\n      body :\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e jsonb_build_object(\n        \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003eids\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e, (\u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e json_agg(\u003cspan class=\"pl-c1\"\u003eds\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eid\u003c/span\u003e) \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e (\u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e id \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e inserted \u003cspan class=\"pl-k\"\u003elimit\u003c/span\u003e batch_size offset i\u003cspan class=\"pl-k\"\u003e*\u003c/span\u003ebatch_size) ds),\n        \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003etable\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e, TG_TABLE_NAME,\n        \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003econtentColumn\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e, content_column,\n        \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003eembeddingColumn\u003cspan class=\"pl-pds\"\u003e'\u003c/span\u003e\u003c/span\u003e, embedding_column\n      ),\n      timeout_milliseconds :\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e timeout_milliseconds\n    );\n  end loop;\n\n  return \u003cspan class=\"pl-k\"\u003enull\u003c/span\u003e;\nend;\n$$;\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eAdd embed trigger to \u003ccode\u003edocument_sections\u003c/code\u003e table\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create trigger embed_document_sections\n  after insert on document_sections\n  referencing new table as inserted\n  for each statement\n  execute procedure private.embed(content, embedding);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003etrigger\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eembed_document_sections\u003c/span\u003e\n  after insert \u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e document_sections\n  referencing new table \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e inserted\n  for each statement\n  execute procedure \u003cspan class=\"pl-c1\"\u003eprivate\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eembed\u003c/span\u003e(content, embedding);\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eNote we pass 2 trigger arguments to \u003ccode\u003eembed()\u003c/code\u003e:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eThe first specifies which column contains the text content to embed.\u003c/li\u003e\n\u003cli\u003eThe second specifies the destination column to save the embedding into.\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp dir=\"auto\"\u003eThere are also 2 more optional trigger arguments available:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create trigger embed_document_sections\n  after insert on document_sections\n  referencing new table as inserted\n  for each statement\n  execute procedure private.embed(content, embedding, 5, 300000);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate\u003c/span\u003e \u003cspan class=\"pl-k\"\u003etrigger\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eembed_document_sections\u003c/span\u003e\n  after insert \u003cspan class=\"pl-k\"\u003eon\u003c/span\u003e document_sections\n  referencing new table \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e inserted\n  for each statement\n  execute procedure \u003cspan class=\"pl-c1\"\u003eprivate\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eembed\u003c/span\u003e(content, embedding, \u003cspan class=\"pl-c1\"\u003e5\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e300000\u003c/span\u003e);\u003c/pre\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eThe third argument specifies the batch size (number of records to include in each edge function call). Default is 5.\u003c/li\u003e\n\u003cli\u003eThe fourth argument specifies the HTTP connection timeout for each edge function call. Default is 300000 ms (5 minutes).\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp dir=\"auto\"\u003eFeel free to adjust these according to your needs. A larger batch size will require a longer timeout per request, since each invocation will have more embeddings to generate. A smaller batch size can use a lower timeout.\u003c/p\u003e\n\u003cdetails\u003e\n\u003csummary\u003e\u003ci\u003eNote: Lifecycle of triggered edge functions\u003c/i\u003e\u003c/summary\u003e\nIf the triggered edge function fails, you will end up with\ndocument sections missing embeddings. During development,\nwe can run `supabase db reset` to reset the database. In production,\nsome potential options are:\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eAdd another function that can be triggered manually which checks for \u003ccode\u003edocument_sections\u003c/code\u003e with missing embeddings and invokes the \u003ccode\u003e/embed\u003c/code\u003e edge function for them.\u003c/li\u003e\n\u003cli\u003eCreate a \u003ca href=\"https://supabase.com/docs/guides/functions/schedule-functions\" rel=\"nofollow\"\u003escheduled function\u003c/a\u003e that periodically checks for \u003ccode\u003edocument_sections\u003c/code\u003e with missing embeddings and re-generates them. We would likely need to add a locking mechanism (ie. via another column) to prevent the scheduled function from conflicting with the normal \u003ccode\u003eembed\u003c/code\u003e trigger.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/details\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eApply the migration to our local database.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase migration up\"\u003e\u003cpre\u003enpx supabase migration up\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eor if you are developing directly on the cloud, push your migrations up:\u003c/p\u003e\n\u003cdiv class=\"snippet-clipboard-content notranslate position-relative overflow-auto\" data-snippet-clipboard-copy-content=\"npx supabase db push\"\u003e\u003cpre class=\"notranslate\"\u003e\u003ccode\u003enpx supabase db push\n\u003c/code\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eCreate Edge Function for \u003ccode\u003eembed\u003c/code\u003e\u003c/h4\u003e\u003ca id=\"user-content-create-edge-function-for-embed\" class=\"anchor\" aria-label=\"Permalink: Create Edge Function for embed\" href=\"#create-edge-function-for-embed\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate edge function file.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase functions new embed\"\u003e\u003cpre\u003enpx supabase functions new embed\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eIn \u003ccode\u003eembed/index.ts\u003c/code\u003e, create an inference session using Supabase's AI inference engine.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"// Setup type definitions for built-in Supabase Runtime APIs\n/// \u0026lt;reference types=\u0026quot;https://esm.sh/@supabase/functions-js/src/edge-runtime.d.ts\u0026quot; /\u0026gt;\n\nimport { createClient } from '@supabase/supabase-js';\n\nconst model = new Supabase.ai.Session('gte-small');\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e// Setup type definitions for built-in Supabase Runtime APIs\u003c/span\u003e\n\u003cspan class=\"pl-c\"\u003e/// \u0026lt;reference types=\"https://esm.sh/@supabase/functions-js/src/edge-runtime.d.ts\" /\u0026gt;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ecreateClient\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'@supabase/supabase-js'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eSupabase\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eai\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eSession\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'gte-small'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: The original code from the video tutorial used Transformers.js to perform inference in the Edge Function. We've since released \u003ca href=\"https://supabase.com/docs/guides/functions/ai-models\" rel=\"nofollow\"\u003eSupabase.ai APIs\u003c/a\u003e that can perform inference natively within the runtime itself (vs. WASM) which is faster and uses less CPU time.\u003c/em\u003e\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eJust like before, grab the Supabase variables and check for their existence \u003cem\u003e(type narrowing)\u003c/em\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"// These are automatically injected\nconst supabaseUrl = Deno.env.get('SUPABASE_URL');\nconst supabaseAnonKey = Deno.env.get('SUPABASE_ANON_KEY');\n\nDeno.serve(async (req) =\u0026gt; {\n  if (!supabaseUrl || !supabaseAnonKey) {\n    return new Response(\n      JSON.stringify({\n        error: 'Missing environment variables.',\n      }),\n      {\n        status: 500,\n        headers: { 'Content-Type': 'application/json' },\n      }\n    );\n  }\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c\"\u003e// These are automatically injected\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabaseUrl\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDeno\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eenv\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eget\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'SUPABASE_URL'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabaseAnonKey\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDeno\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eenv\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eget\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'SUPABASE_ANON_KEY'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-v\"\u003eDeno\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eserve\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-k\"\u003easync\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ereq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u0026gt;\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esupabaseUrl\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e||\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esupabaseAnonKey\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n        \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'Missing environment variables.'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n        \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n        \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate a Supabase client and configure to inherit the user’s permissions.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const authorization = req.headers.get('Authorization');\n\nif (!authorization) {\n  return new Response(\n    JSON.stringify({ error: `No authorization header passed` }),\n    {\n      status: 500,\n      headers: { 'Content-Type': 'application/json' },\n    }\n  );\n}\n\nconst supabase = createClient(supabaseUrl, supabaseAnonKey, {\n  global: {\n    headers: {\n      authorization,\n    },\n  },\n  auth: {\n    persistSession: false,\n  },\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eauthorization\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ereq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eget\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'Authorization'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eauthorization\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e`No authorization header passed`\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ecreateClient\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esupabaseUrl\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabaseAnonKey\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eglobal\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      authorization\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003epersistSession\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003efalse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eFetch the text content from the specified table/column.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const { ids, table, contentColumn, embeddingColumn } = await req.json();\n\nconst { data: rows, error: selectError } = await supabase\n  .from(table)\n  .select(`id, ${contentColumn}` as '*')\n  .in('id', ids)\n  .is(embeddingColumn, null);\n\nif (selectError) {\n  return new Response(JSON.stringify({ error: selectError }), {\n    status: 500,\n    headers: { 'Content-Type': 'application/json' },\n  });\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e ids\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e table\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e contentColumn\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e embeddingColumn \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ereq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003ejson\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003edata\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003erows\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003eselectError\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003efrom\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003etable\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eselect\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e`id, \u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003econtentColumn\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e`\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'*'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003ein\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'id'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eids\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eis\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eembeddingColumn\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003enull\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eselectError\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003eselectError\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eGenerate an embedding for each piece of text and update the respective rows.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-ts notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"for (const row of rows) {\n  const { id, [contentColumn]: content } = row;\n\n  if (!content) {\n    console.error(`No content available in column '${contentColumn}'`);\n    continue;\n  }\n\n  const output = (await model.run(content, {\n    mean_pool: true,\n    normalize: true,\n  })) as number[];\n\n  const embedding = JSON.stringify(output);\n\n  const { error } = await supabase\n    .from(table)\n    .update({\n      [embeddingColumn]: embedding,\n    })\n    .eq('id', id);\n\n  if (error) {\n    console.error(\n      `Failed to save embedding on '${table}' table with id ${id}`\n    );\n  }\n\n  console.log(\n    `Generated embedding ${JSON.stringify({\n      table,\n      id,\n      contentColumn,\n      embeddingColumn,\n    })}`\n  );\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003erow\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eof\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003erows\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e id\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e[\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003econtentColumn\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e]\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003econtent\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003erow\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n  \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003econtent\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-smi\"\u003econsole\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eerror\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e`No content available in column '\u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003econtentColumn\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e'`\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n    \u003cspan class=\"pl-k\"\u003econtinue\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n  \u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eoutput\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003emodel\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003erun\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003econtent\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003emean_pool\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003etrue\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003enormalize\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003etrue\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e \u003cspan class=\"pl-smi\"\u003enumber\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e[\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e]\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n  \u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eembedding\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eoutput\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n  \u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e error \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003efrom\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003etable\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eupdate\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-kos\"\u003e[\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eembeddingColumn\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e]\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003eembedding\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eeq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'id'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eid\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n  \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eerror\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-smi\"\u003econsole\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eerror\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n      \u003cspan class=\"pl-s\"\u003e`Failed to save embedding on '\u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003etable\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e' table with id \u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eid\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e`\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n  \u003cspan class=\"pl-smi\"\u003econsole\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003elog\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n    \u003cspan class=\"pl-s\"\u003e`Generated embedding \u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-s1\"\u003e      table\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-s1\"\u003e      id\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-s1\"\u003e      contentColumn\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-s1\"\u003e      embeddingColumn\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-s1\"\u003e    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e`\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eReturn a success response.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"return new Response(null, {\n  status: 204,\n  headers: { 'Content-Type': 'application/json' },\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003enull\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e204\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eIf you're developing directly on the cloud, deploy your edge function:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase functions deploy\"\u003e\u003cpre\u003enpx supabase functions deploy\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003chr\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e\u003ccode\u003eStep 4\u003c/code\u003e - Chat\u003c/h3\u003e\u003ca id=\"user-content-step-4---chat\" class=\"anchor\" aria-label=\"Permalink: Step 4 - Chat\" href=\"#step-4---chat\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eJump to a step:\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"#step-1---storage\"\u003eStorage\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-2---documents\"\u003eDocuments\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-3---embeddings\"\u003eEmbeddings\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-4---chat\"\u003eChat\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-5---database-types-bonus\"\u003eDatabase Types\u003c/a\u003e (Bonus)\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#youre-done\"\u003eYou're done!\u003c/a\u003e\u003c/li\u003e\n\u003c/ol\u003e\n\u003chr\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eUse these commands to jump to the \u003ccode\u003estep-4\u003c/code\u003e checkpoint.\u003c/em\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"git stash push -u -m \u0026quot;my work on step-3\u0026quot;\ngit checkout step-4\"\u003e\u003cpre\u003egit stash push -u -m \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003emy work on step-3\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\ngit checkout step-4\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eFinally, let's implement the chat functionality. For this workshop, we're going to generate our query embedding client side using a new custom hook called \u003ccode\u003eusePipeline()\u003c/code\u003e.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eUpdate Frontend\u003c/h4\u003e\u003ca id=\"user-content-update-frontend\" class=\"anchor\" aria-label=\"Permalink: Update Frontend\" href=\"#update-frontend\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eInstall dependencies\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npm i @xenova/transformers ai\"\u003e\u003cpre\u003enpm i @xenova/transformers ai\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWe'll use \u003ca href=\"https://github.com/xenova/transformers.js\"\u003eTransformers.js\u003c/a\u003e to perform inference directly in the browser.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eConfigure \u003ccode\u003enext.config.js\u003c/code\u003e to support Transformers.js\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-js notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"  webpack: (config) =\u0026gt; {\n    config.resolve.alias = {\n      ...config.resolve.alias,\n      sharp$: false,\n      'onnxruntime-node$': false,\n    };\n    return config;\n  },\"\u003e\u003cpre\u003e  \u003cspan class=\"pl-s1\"\u003ewebpack\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003econfig\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u0026gt;\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-s1\"\u003econfig\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eresolve\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003ealias\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      ...\u003cspan class=\"pl-s1\"\u003econfig\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eresolve\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003ealias\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003esharp$\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003efalse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-s\"\u003e'onnxruntime-node$'\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003efalse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n    \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003econfig\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eImport dependencies\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import { usePipeline } from '@/lib/hooks/use-pipeline';\nimport { createClientComponentClient } from '@supabase/auth-helpers-nextjs';\nimport { useChat } from 'ai/react';\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eusePipeline\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'@/lib/hooks/use-pipeline'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ecreateClientComponentClient\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'@supabase/auth-helpers-nextjs'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003euseChat\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'ai/react'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: \u003ccode\u003eusePipeline()\u003c/code\u003e was pre-built into this repository for convenience. It uses Web Workers to asynchronously generate embeddings in another thread using Transformers.js.\u003c/em\u003e\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate a Supabase client in \u003ccode\u003echat/page.tsx\u003c/code\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const supabase = createClientComponentClient();\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ecreateClientComponentClient\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate embedding pipeline.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const generateEmbedding = usePipeline(\n  'feature-extraction',\n  'Supabase/gte-small'\n);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003egenerateEmbedding\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eusePipeline\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n  \u003cspan class=\"pl-s\"\u003e'feature-extraction'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-s\"\u003e'Supabase/gte-small'\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: it's important that the embedding model you set here matches the model used in the Edge Function, otherwise your future matching logic will be meaningless.\u003c/em\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eTransformers.js requires models to exist in the ONNX format. Specifically\nthe Hugging Face model you specify in the pipeline must have an \u003ccode\u003e.onnx\u003c/code\u003e file\nunder the \u003ccode\u003e./onnx\u003c/code\u003e folder, otherwise you will see the error\n\u003ccode\u003eCould not locate file [...] xxx.onnx\u003c/code\u003e. Check out\n\u003ca href=\"https://www.youtube.com/watch?v=QdDoFfkVkcw\u0026amp;t=3825s\" rel=\"nofollow\"\u003ethis explanation\u003c/a\u003e for more details.\nTo convert an existing model (eg. PyTorch, Tensorflow, etc) to ONNX, see\nthe \u003ca href=\"https://huggingface.co/docs/transformers.js/en/custom_usage#convert-your-models-to-onnx\" rel=\"nofollow\"\u003ecustom usage documentation\u003c/a\u003e.\u003c/em\u003e\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eManage chat messages and state with \u003ccode\u003euseChat()\u003c/code\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const { messages, input, handleInputChange, handleSubmit, isLoading } =\n  useChat({\n    api: `${process.env.NEXT_PUBLIC_SUPABASE_URL}/functions/v1/chat`,\n  });\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e messages\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e input\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e handleInputChange\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e handleSubmit\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e isLoading \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\n  \u003cspan class=\"pl-en\"\u003euseChat\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eapi\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e`\u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eprocess\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eenv\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eNEXT_PUBLIC_SUPABASE_URL\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e/functions/v1/chat`\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: \u003ccode\u003euseChat()\u003c/code\u003e is a convenience hook provided by Vercel's \u003ccode\u003eai\u003c/code\u003e package to handle chat message state and streaming. We'll point it to an Edge Function called \u003ccode\u003echat\u003c/code\u003e (coming up).\u003c/em\u003e\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eSet the ready status to \u003ccode\u003etrue\u003c/code\u003e when pipeline has loaded.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const isReady = !!generateEmbedding;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eisReady\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003egenerateEmbedding\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eConnect \u003ccode\u003einput\u003c/code\u003e and \u003ccode\u003ehandleInputChange\u003c/code\u003e to our \u003ccode\u003e\u0026lt;Input\u0026gt;\u003c/code\u003e props.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"\u0026lt;Input\n  type=\u0026quot;text\u0026quot;\n  autoFocus\n  placeholder=\u0026quot;Send a message\u0026quot;\n  value={input}\n  onChange={handleInputChange}\n/\u0026gt;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c1\"\u003e\u0026lt;\u003c/span\u003e\u003cspan class=\"pl-v\"\u003eInput\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003etype\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"text\"\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eautoFocus\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eplaceholder\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"Send a message\"\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003evalue\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003einput\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eonChange\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ehandleInputChange\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e/\u0026gt;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eGenerate an embedding and submit messages on form submit.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"if (!generateEmbedding) {\n  throw new Error('Unable to generate embeddings');\n}\n\nconst output = await generateEmbedding(input, {\n  pooling: 'mean',\n  normalize: true,\n});\n\nconst embedding = JSON.stringify(Array.from(output.data));\n\nconst {\n  data: { session },\n} = await supabase.auth.getSession();\n\nif (!session) {\n  return;\n}\n\nhandleSubmit(e, {\n  options: {\n    headers: {\n      authorization: `Bearer ${session.access_token}`,\n    },\n    body: {\n      embedding,\n    },\n  },\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003egenerateEmbedding\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ethrow\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eError\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'Unable to generate embeddings'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eoutput\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-en\"\u003egenerateEmbedding\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003einput\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003epooling\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'mean'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003enormalize\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003etrue\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eembedding\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-v\"\u003eArray\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003efrom\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eoutput\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003edata\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003edata\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e session \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003egetSession\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esession\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n\u003cspan class=\"pl-en\"\u003ehandleSubmit\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ee\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eoptions\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eauthorization\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e`Bearer \u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esession\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eaccess_token\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e`\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003ebody\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      embedding\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eDisable send button until the component is ready.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"\u0026lt;Button type=\u0026quot;submit\u0026quot; disabled={!isReady}\u0026gt;\n  Send\n\u0026lt;/Button\u0026gt;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-c1\"\u003e\u0026lt;\u003c/span\u003e\u003cspan class=\"pl-v\"\u003eButton\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003etype\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\"submit\"\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003edisabled\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eisReady\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e\u0026gt;\u003c/span\u003e\n  Send\n\u003cspan class=\"pl-kos\"\u003e\u0026lt;/\u003c/span\u003e\u003cspan class=\"pl-v\"\u003eButton\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e\u0026gt;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eSQL Migration\u003c/h4\u003e\u003ca id=\"user-content-sql-migration\" class=\"anchor\" aria-label=\"Permalink: SQL Migration\" href=\"#sql-migration\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate migration file for a new match function\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase migration new match\"\u003e\u003cpre\u003enpx supabase migration new match\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate a \u003ccode\u003ematch_document_sections\u003c/code\u003e Postgres function.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-sql notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"create or replace function match_document_sections(\n  embedding vector(384),\n  match_threshold float\n)\nreturns setof document_sections\nlanguage plpgsql\nas $$\n#variable_conflict use_variable\nbegin\n  return query\n  select *\n  from document_sections\n  where document_sections.embedding \u0026lt;#\u0026gt; embedding \u0026lt; -match_threshold\n\torder by document_sections.embedding \u0026lt;#\u0026gt; embedding;\nend;\n$$;\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003ecreate or replace\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efunction\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ematch_document_sections\u003c/span\u003e(\n  embedding vector(\u003cspan class=\"pl-c1\"\u003e384\u003c/span\u003e),\n  match_threshold float\n)\nreturns setof document_sections\nlanguage plpgsql\n\u003cspan class=\"pl-k\"\u003eas\u003c/span\u003e $$\n\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003evariable_conflict use_variable\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003ebegin\u003c/span\u003e\n  return query\n  \u003cspan class=\"pl-k\"\u003eselect\u003c/span\u003e \u003cspan class=\"pl-k\"\u003e*\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e document_sections\n  \u003cspan class=\"pl-k\"\u003ewhere\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003edocument_sections\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eembedding\u003c/span\u003e \u003cspan class=\"pl-k\"\u003e\u0026lt;\u003c/span\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e\u0026gt; embedding \u0026lt; -match_threshold\u003c/span\u003e\n\t\u003cspan class=\"pl-k\"\u003eorder by\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003edocument_sections\u003c/span\u003e.\u003cspan class=\"pl-c1\"\u003eembedding\u003c/span\u003e \u003cspan class=\"pl-k\"\u003e\u0026lt;\u003c/span\u003e\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e\u0026gt; embedding;\u003c/span\u003e\nend;\n$$;\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThis function uses pgvector's negative inner product operator \u003ccode\u003e\u0026lt;#\u0026gt;\u003c/code\u003e to perform similarity search. Inner product requires less computations than other distance functions like cosine distance \u003ccode\u003e\u0026lt;=\u0026gt;\u003c/code\u003e, and therefore provides better query performance.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: Our embeddings are normalized, so inner product and cosine similarity are equivalent in terms of output. Note though that pgvector's \u003ccode\u003e\u0026lt;=\u0026gt;\u003c/code\u003e operator is cosine distance, not cosine similarity, so \u003ccode\u003einner product == 1 - cosine distance\u003c/code\u003e.\u003c/em\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eWe also filter by a \u003ccode\u003ematch_threshold\u003c/code\u003e in order to return only the most relevant results (1 = most similar, -1 = most dissimilar).\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: \u003ccode\u003ematch_threshold\u003c/code\u003e is negated because \u003ccode\u003e\u0026lt;#\u0026gt;\u003c/code\u003e is a negative inner product. See the pgvector docs for more details on why \u003ccode\u003e\u0026lt;#\u0026gt;\u003c/code\u003e is negative.\u003c/em\u003e\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eApply the migration to our local database.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase migration up\"\u003e\u003cpre\u003enpx supabase migration up\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eor if you are developing directly on the cloud, push your migrations up:\u003c/p\u003e\n\u003cdiv class=\"snippet-clipboard-content notranslate position-relative overflow-auto\" data-snippet-clipboard-copy-content=\"npx supabase db push\"\u003e\u003cpre class=\"notranslate\"\u003e\u003ccode\u003enpx supabase db push\n\u003c/code\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eCreate \u003ccode\u003echat\u003c/code\u003e Edge Function\u003c/h4\u003e\u003ca id=\"user-content-create-chat-edge-function\" class=\"anchor\" aria-label=\"Permalink: Create chat Edge Function\" href=\"#create-chat-edge-function\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cstrong\u003eNote:\u003c/strong\u003e In this tutorial we use models provided by OpenAI to implement the chat logic.\nHowever since making this tutorial, many new LLM providers exist, such as:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"https://docs.together.ai/docs/openai-api-compatibility#nodejs\" rel=\"nofollow\"\u003etogether.ai\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://readme.fireworks.ai/docs/openai-compatibility\" rel=\"nofollow\"\u003efireworks.ai\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://docs.endpoints.anyscale.com/examples/work-with-openai/\" rel=\"nofollow\"\u003eendpoints.anyscale.com\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/ollama/ollama/blob/main/docs/openai.md#openai-javascript-library\"\u003elocal models served with Ollama\u003c/a\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp dir=\"auto\"\u003eWhichever provider you choose, you can reuse the code below (that uses the OpenAI lib) as long as they offer an OpenAI-compatible API \u003cem\u003e(all of providers listed above do)\u003c/em\u003e. We'll discuss how to do this in each step using Ollama, but the same logic applies to the other providers.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eFirst generate an API key from \u003ca href=\"https://platform.openai.com/account/api-keys\" rel=\"nofollow\"\u003eOpenAI\u003c/a\u003e and save it in \u003ccode\u003esupabase/functions/.env\u003c/code\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"cat \u0026gt; supabase/functions/.env \u0026lt;\u0026lt;- EOF\nOPENAI_API_KEY=\u0026lt;your-api-key\u0026gt;\nEOF\"\u003e\u003cpre\u003ecat \u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e supabase/functions/.env \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-k\"\u003e\u0026lt;\u0026lt;\u003c/span\u003e- \u003cspan class=\"pl-k\"\u003eEOF\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003eOPENAI_API_KEY=\u0026lt;your-api-key\u0026gt;\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-k\"\u003eEOF\u003c/span\u003e\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate the edge function file.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase functions new chat\"\u003e\u003cpre\u003enpx supabase functions new chat\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eLoad the OpenAI and Supabase keys.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import { createClient } from '@supabase/supabase-js';\nimport { OpenAIStream, StreamingTextResponse } from 'ai';\nimport { codeBlock } from 'common-tags';\nimport OpenAI from 'openai';\n\nconst openai = new OpenAI({\n  apiKey: Deno.env.get('OPENAI_API_KEY'),\n});\n\n// These are automatically injected\nconst supabaseUrl = Deno.env.get('SUPABASE_URL');\nconst supabaseAnonKey = Deno.env.get('SUPABASE_ANON_KEY');\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ecreateClient\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'@supabase/supabase-js'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eOpenAIStream\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eStreamingTextResponse\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'ai'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ecodeBlock\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'common-tags'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eOpenAI\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'openai'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eopenai\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eOpenAI\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eapiKey\u003c/span\u003e: \u003cspan class=\"pl-v\"\u003eDeno\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eenv\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eget\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'OPENAI_API_KEY'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-c\"\u003e// These are automatically injected\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabaseUrl\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDeno\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eenv\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eget\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'SUPABASE_URL'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabaseAnonKey\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDeno\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eenv\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eget\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'SUPABASE_ANON_KEY'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cdetails\u003e\n\u003csummary\u003e\u003ci\u003eNote: Ollama support\u003c/i\u003e\u003c/summary\u003e\n\u003cp dir=\"auto\"\u003eFor Ollama (and other OpenAI-compatible providers), adjust the \u003ccode\u003ebaseURL\u003c/code\u003e and \u003ccode\u003eapiKey\u003c/code\u003e when instantiating \u003ccode\u003eopenai\u003c/code\u003e:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const openai = new OpenAI({\n  baseURL: 'http://host.docker.internal:11434/v1/',\n  apiKey: 'ollama',\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eopenai\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eOpenAI\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003ebaseURL\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'http://host.docker.internal:11434/v1/'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eapiKey\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'ollama'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eWe assume here that you're running \u003ccode\u003eollama serve\u003c/code\u003e locally\nwith the default port \u003ccode\u003e:11434\u003c/code\u003e.\nSince local edge functions run inside a Docker container,\nwe specify \u003ccode\u003ehost.docker.internal\u003c/code\u003e instead of \u003ccode\u003elocalhost\u003c/code\u003e\nin order to reach Ollama running on your host.\u003c/p\u003e\n\u003c/details\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eSince our frontend is served at a different domain origin than our Edge Function, we must handle cross origin resource sharing (CORS).\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"export const corsHeaders = {\n  'Access-Control-Allow-Origin': '*',\n  'Access-Control-Allow-Headers':\n    'authorization, x-client-info, apikey, content-type',\n};\n\nDeno.serve(async (req) =\u0026gt; {\n  // Handle CORS\n  if (req.method === 'OPTIONS') {\n    return new Response('ok', { headers: corsHeaders });\n  }\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eexport\u003c/span\u003e \u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ecorsHeaders\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-s\"\u003e'Access-Control-Allow-Origin'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'*'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-s\"\u003e'Access-Control-Allow-Headers'\u003c/span\u003e:\n    \u003cspan class=\"pl-s\"\u003e'authorization, x-client-info, apikey, content-type'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-v\"\u003eDeno\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eserve\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-k\"\u003easync\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ereq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u0026gt;\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c\"\u003e// Handle CORS\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ereq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003emethod\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e===\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'OPTIONS'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'ok'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003ecorsHeaders\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eHandle CORS simply by checking for an \u003ccode\u003eOPTIONS\u003c/code\u003e HTTP request and returning the CORS headers (\u003ccode\u003e*\u003c/code\u003e = allow any domain). In production, consider limiting the origins to specific domains that serve your frontend.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCheck for environment variables and create Supabase client.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"if (!supabaseUrl || !supabaseAnonKey) {\n  return new Response(\n    JSON.stringify({\n      error: 'Missing environment variables.',\n    }),\n    {\n      status: 500,\n      headers: { 'Content-Type': 'application/json' },\n    }\n  );\n}\n\nconst authorization = req.headers.get('Authorization');\n\nif (!authorization) {\n  return new Response(\n    JSON.stringify({ error: `No authorization header passed` }),\n    {\n      status: 500,\n      headers: { 'Content-Type': 'application/json' },\n    }\n  );\n}\n\nconst supabase = createClient(supabaseUrl, supabaseAnonKey, {\n  global: {\n    headers: {\n      authorization,\n    },\n  },\n  auth: {\n    persistSession: false,\n  },\n});\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esupabaseUrl\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e||\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esupabaseAnonKey\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'Missing environment variables.'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eauthorization\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ereq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eget\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'Authorization'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003eauthorization\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e`No authorization header passed`\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ecreateClient\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003esupabaseUrl\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabaseAnonKey\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eglobal\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      authorization\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003eauth\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003epersistSession\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003efalse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eThe first step of RAG is to perform similarity search using our \u003ccode\u003ematch_document_sections()\u003c/code\u003e function. Postgres functions are executed using the \u003ccode\u003e.rpc()\u003c/code\u003e method.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const { chatId, message, messages, embedding } = await req.json();\n\nconst { data: documents, error: matchError } = await supabase\n  .rpc('match_document_sections', {\n    embedding,\n    match_threshold: 0.8,\n  })\n  .select('content')\n  .limit(5);\n\nif (matchError) {\n  console.error(matchError);\n\n  return new Response(\n    JSON.stringify({\n      error: 'There was an error reading your documents, please try again.',\n    }),\n    {\n      status: 500,\n      headers: { 'Content-Type': 'application/json' },\n    }\n  );\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e chatId\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e message\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e messages\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e embedding \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ereq\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003ejson\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003edata\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003edocuments\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003ematchError\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003erpc\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'match_document_sections'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    embedding\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003ematch_threshold\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e0.8\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eselect\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'content'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003elimit\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e5\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ematchError\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-smi\"\u003econsole\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003eerror\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ematchError\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003eJSON\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003estringify\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eerror\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'There was an error reading your documents, please try again.'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003estatus\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e500\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'Content-Type'\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'application/json'\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eThe second step of RAG is to build our prompt, injecting in the relevant documents retrieved from our previous similarity search.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const injectedDocs =\n  documents \u0026amp;\u0026amp; documents.length \u0026gt; 0\n    ? documents.map(({ content }) =\u0026gt; content).join('\\n\\n')\n    : 'No documents found';\n\nconst completionMessages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] =\n  [\n    {\n      role: 'user',\n      content: codeBlock`\n          You're an AI assistant who answers questions about documents.\n\n          You're a chat bot, so keep your replies succinct.\n\n          You're only allowed to use the documents below to answer the question.\n\n          If the question isn't related to these documents, say:\n          \u0026quot;Sorry, I couldn't find any information on that.\u0026quot;\n\n          If the information isn't available in the below documents, say:\n          \u0026quot;Sorry, I couldn't find any information on that.\u0026quot;\n\n          Do not go off topic.\n\n          Documents:\n          ${injectedDocs}\n        `,\n    },\n    ...messages,\n  ];\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003einjectedDocs\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\n  \u003cspan class=\"pl-s1\"\u003edocuments\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e\u0026amp;\u0026amp;\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003edocuments\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003elength\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e\u0026gt;\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e\n    ? \u003cspan class=\"pl-s1\"\u003edocuments\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003emap\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e content \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u0026gt;\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003econtent\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003ejoin\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e'\\n\\n'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\n    : \u003cspan class=\"pl-s\"\u003e'No documents found'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ecompletionMessages\u003c/span\u003e: \u003cspan class=\"pl-v\"\u003eOpenAI\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eChat\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eCompletions\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-smi\"\u003eChatCompletionMessageParam\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e[\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e]\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e[\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003erole\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'user'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n      \u003cspan class=\"pl-c1\"\u003econtent\u003c/span\u003e: \u003cspan class=\"pl-en\"\u003ecodeBlock\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e`\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e          You're an AI assistant who answers questions about documents.\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e          You're a chat bot, so keep your replies succinct.\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e          You're only allowed to use the documents below to answer the question.\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e          If the question isn't related to these documents, say:\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e          \"Sorry, I couldn't find any information on that.\"\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e          If the information isn't available in the below documents, say:\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e          \"Sorry, I couldn't find any information on that.\"\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e          Do not go off topic.\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e          Documents:\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e          \u003cspan class=\"pl-s1\"\u003e\u003cspan class=\"pl-kos\"\u003e${\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003einjectedDocs\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/span\u003e\u003c/span\u003e\n\u003cspan class=\"pl-s\"\u003e        `\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    ...\u003cspan class=\"pl-s1\"\u003emessages\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e]\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: the \u003ccode\u003ecodeBlock\u003c/code\u003e template tag is a convenience function that will strip away indentations in our multiline string. This allows us to format our code nicely while preserving the intended indentation.\u003c/em\u003e\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eFinally, create a completion stream and return it.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"const completionStream = await openai.chat.completions.create({\n  model: 'gpt-3.5-turbo-0125',\n  messages: completionMessages,\n  max_tokens: 1024,\n  temperature: 0,\n  stream: true,\n});\n\nconst stream = OpenAIStream(completionStream);\nreturn new StreamingTextResponse(stream, { headers: corsHeaders });\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003ecompletionStream\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-k\"\u003eawait\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003eopenai\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003echat\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003ecompletions\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-en\"\u003ecreate\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003emodel\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'gpt-3.5-turbo-0125'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003emessages\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003ecompletionMessages\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003emax_tokens\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e1024\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003etemperature\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-c1\"\u003estream\u003c/span\u003e: \u003cspan class=\"pl-c1\"\u003etrue\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003estream\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eOpenAIStream\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003ecompletionStream\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enew\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eStreamingTextResponse\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-s1\"\u003estream\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eheaders\u003c/span\u003e: \u003cspan class=\"pl-s1\"\u003ecorsHeaders\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e\u003ccode\u003eOpenAIStream\u003c/code\u003e and \u003ccode\u003eStreamingTextResponse\u003c/code\u003e are convenience helpers from Vercel's \u003ccode\u003eai\u003c/code\u003e package that translate OpenAI's response stream into a format that \u003ccode\u003euseChat()\u003c/code\u003e understands on the frontend.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eNote: we must also return CORS headers here (or anywhere else we send a response).\u003c/em\u003e\u003c/p\u003e\n\u003cdetails\u003e\n\u003csummary\u003e\u003ci\u003eNote: Ollama support\u003c/i\u003e\u003c/summary\u003e\nChange the model to a model you're serving locally, for example:\n\u003cdiv class=\"highlight highlight-source-diff notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"-     model: 'gpt-3.5-turbo-0125',\n+     model: 'dolphin-mistral',\"\u003e\u003cpre\u003e\u003cspan class=\"pl-md\"\u003e\u003cspan class=\"pl-md\"\u003e-\u003c/span\u003e     model: 'gpt-3.5-turbo-0125',\u003c/span\u003e\n\u003cspan class=\"pl-mi1\"\u003e\u003cspan class=\"pl-mi1\"\u003e+\u003c/span\u003e     model: 'dolphin-mistral',\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/details\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eIf you're developing directly on the cloud, set your \u003ccode\u003eOPENAI_API_KEY\u003c/code\u003e secret in the cloud:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase secrets set OPENAI_API_KEY=\u0026lt;openai-key\u0026gt;\"\u003e\u003cpre\u003enpx supabase secrets \u003cspan class=\"pl-c1\"\u003eset\u003c/span\u003e OPENAI_API_KEY=\u003cspan class=\"pl-k\"\u003e\u0026lt;\u003c/span\u003eopenai-key\u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eThen deploy your edge function:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase functions deploy\"\u003e\u003cpre\u003enpx supabase functions deploy\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch4 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eTry it!\u003c/h4\u003e\u003ca id=\"user-content-try-it\" class=\"anchor\" aria-label=\"Permalink: Try it!\" href=\"#try-it\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eLet's try it out! Here are some questions you could try asking:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eWhat kind of buildings did they live in?\u003c/li\u003e\n\u003cli\u003eWhat was the most common food?\u003c/li\u003e\n\u003cli\u003eWhat did people do for fun?\u003c/li\u003e\n\u003c/ul\u003e\n\u003chr\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e\u003ccode\u003eStep 5\u003c/code\u003e - Database Types (Bonus)\u003c/h3\u003e\u003ca id=\"user-content-step-5---database-types-bonus\" class=\"anchor\" aria-label=\"Permalink: Step 5 - Database Types (Bonus)\" href=\"#step-5---database-types-bonus\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eJump to a step:\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"#step-1---storage\"\u003eStorage\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-2---documents\"\u003eDocuments\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-3---embeddings\"\u003eEmbeddings\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-4---chat\"\u003eChat\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-5---database-types-bonus\"\u003eDatabase Types\u003c/a\u003e (Bonus)\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#youre-done\"\u003eYou're done!\u003c/a\u003e\u003c/li\u003e\n\u003c/ol\u003e\n\u003chr\u003e\n\u003cp dir=\"auto\"\u003e\u003cem\u003eUse these commands to jump to the \u003ccode\u003estep-5\u003c/code\u003e checkpoint.\u003c/em\u003e\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"git stash push -u -m \u0026quot;my work on step-4\u0026quot;\ngit checkout step-5\"\u003e\u003cpre\u003egit stash push -u -m \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003emy work on step-4\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\ngit checkout step-5\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eYou may have noticed that all of our DB data coming back from the \u003ccode\u003esupabase\u003c/code\u003e client has had an \u003ccode\u003eany\u003c/code\u003e type (such as \u003ccode\u003edocuments\u003c/code\u003e or \u003ccode\u003edocument_sections\u003c/code\u003e). This isn't great, since we're missing relevant type information and lose type safety \u003cem\u003e(making our app more error-prone)\u003c/em\u003e.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThe Supabase CLI comes with a built-in command to generate TypeScript types based on your database's schema.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eGenerate TypeScript types based on local DB schema.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"supabase gen types typescript --local \u0026gt; supabase/functions/_lib/database.ts\"\u003e\u003cpre\u003esupabase gen types typescript --local \u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e supabase/functions/_lib/database.ts\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eAdd the \u003ccode\u003e\u0026lt;Database\u0026gt;\u003c/code\u003e generic to all Supabase clients across our project.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eIn React\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import { Database } from '@/supabase/functions/_lib/database';\n\nconst supabase = createClientComponentClient\u0026lt;Database\u0026gt;();\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDatabase\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'@/supabase/functions/_lib/database'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ecreateClientComponentClient\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e\u0026lt;\u003c/span\u003e\u003cspan class=\"pl-smi\"\u003eDatabase\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e\u0026gt;\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import { Database } from '@/supabase/functions/_lib/database';\n\nconst supabase = createServerComponentClient\u0026lt;Database\u0026gt;();\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDatabase\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'@/supabase/functions/_lib/database'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ecreateServerComponentClient\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e\u0026lt;\u003c/span\u003e\u003cspan class=\"pl-smi\"\u003eDatabase\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e\u0026gt;\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eIn Edge Functions\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"import { Database } from '../_lib/database.ts';\n\nconst supabase = createClient\u0026lt;Database\u0026gt;(...);\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eimport\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e \u003cspan class=\"pl-v\"\u003eDatabase\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e \u003cspan class=\"pl-k\"\u003efrom\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e'../_lib/database.ts'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\n\u003cspan class=\"pl-k\"\u003econst\u003c/span\u003e \u003cspan class=\"pl-s1\"\u003esupabase\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-en\"\u003ecreateClient\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e\u0026lt;\u003c/span\u003e\u003cspan class=\"pl-smi\"\u003eDatabase\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e\u0026gt;\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e...\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eFix type errors 😃\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eLooks like we found a type error in \u003ccode\u003e./app/files/page.tsx\u003c/code\u003e! Let's add this check to top of the document's click handler \u003cem\u003e(type narrowing)\u003c/em\u003e.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-tsx notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"if (!document.storage_object_path) {\n  toast({\n    variant: 'destructive',\n    description: 'Failed to download file, please try again.',\n  });\n  return;\n}\"\u003e\u003cpre\u003e\u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e!\u003c/span\u003e\u003cspan class=\"pl-smi\"\u003edocument\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e.\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003estorage_object_path\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e \u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n  \u003cspan class=\"pl-en\"\u003etoast\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e(\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e{\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003evariant\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'destructive'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n    \u003cspan class=\"pl-c1\"\u003edescription\u003c/span\u003e: \u003cspan class=\"pl-s\"\u003e'Failed to download file, please try again.'\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e,\u003c/span\u003e\n  \u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e)\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n  \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e\u003cspan class=\"pl-kos\"\u003e;\u003c/span\u003e\n\u003cspan class=\"pl-kos\"\u003e}\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch3 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eYou're done!\u003c/h3\u003e\u003ca id=\"user-content-youre-done\" class=\"anchor\" aria-label=\"Permalink: You're done!\" href=\"#youre-done\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003e🎉 Congrats! You've built your own full stack pgvector app in 2 hours.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eIf you would like to jump directly to the completed app, simply checkout the \u003ccode\u003emain\u003c/code\u003e branch:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"git checkout main\"\u003e\u003cpre\u003egit checkout main\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eJump to a previous step:\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"#step-1---storage\"\u003eStorage\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-2---documents\"\u003eDocuments\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-3---embeddings\"\u003eEmbeddings\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-4---chat\"\u003eChat\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#step-5---database-types-bonus\"\u003eDatabase Types\u003c/a\u003e (Bonus)\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#youre-done\"\u003eYou're done!\u003c/a\u003e\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e🚀 Going to prod\u003c/h2\u003e\u003ca id=\"user-content--going-to-prod\" class=\"anchor\" aria-label=\"Permalink: 🚀 Going to prod\" href=\"#-going-to-prod\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eIf you've been developing the app locally, follow these instructions to deploy your app to a production Supabase project.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eCreate a Supabase project at \u003ca href=\"https://database.new\" rel=\"nofollow\"\u003ehttps://database.new\u003c/a\u003e, or via the CLI:\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase projects create -i \u0026quot;ChatGPT Your Files\u0026quot;\"\u003e\u003cpre\u003enpx supabase projects create -i \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003eChatGPT Your Files\u003cspan class=\"pl-pds\"\u003e\"\u003c/span\u003e\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eLink the CLI with your Supabase project.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase link --project-ref=\u0026lt;project-ref\u0026gt;\"\u003e\u003cpre\u003enpx supabase link --project-ref=\u003cspan class=\"pl-k\"\u003e\u0026lt;\u003c/span\u003eproject-ref\u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eYou can grab your project's reference ID in your \u003ca href=\"https://supabase.com/dashboard/project/_/settings/general\" rel=\"nofollow\"\u003eproject’s settings\u003c/a\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003ePush migrations to remote database.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase db push\"\u003e\u003cpre\u003enpx supabase db push\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eSet Edge Function secrets (OpenAI key).\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase secrets set OPENAI_API_KEY=\u0026lt;openai-key\u0026gt;\"\u003e\u003cpre\u003enpx supabase secrets \u003cspan class=\"pl-c1\"\u003eset\u003c/span\u003e OPENAI_API_KEY=\u003cspan class=\"pl-k\"\u003e\u0026lt;\u003c/span\u003eopenai-key\u003cspan class=\"pl-k\"\u003e\u0026gt;\u003c/span\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eDeploy Edge Functions.\u003c/p\u003e\n\u003cdiv class=\"highlight highlight-source-shell notranslate position-relative overflow-auto\" dir=\"auto\" data-snippet-clipboard-copy-content=\"npx supabase functions deploy\"\u003e\u003cpre\u003enpx supabase functions deploy\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eDeploy to Vercel \u003cem\u003e(or CDN of your choice - must support Next.js API routes for authentication)\u003c/em\u003e.\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eFollow Vercel’s \u003ca href=\"https://nextjs.org/docs/app/getting-started/deploying\" rel=\"nofollow\"\u003edeploy instructions\u003c/a\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003cli\u003e\n\u003cp dir=\"auto\"\u003eBe sure to set \u003ccode\u003eNEXT_PUBLIC_SUPABASE_URL\u003c/code\u003e and \u003ccode\u003eNEXT_PUBLIC_SUPABASE_ANON_KEY\u003c/code\u003e for your Supabase project.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eYou can find these in your \u003ca href=\"https://supabase.com/dashboard/project/_/settings/api\" rel=\"nofollow\"\u003eproject’s API settings\u003c/a\u003e.\u003c/p\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e📈 Next steps\u003c/h2\u003e\u003ca id=\"user-content--next-steps\" class=\"anchor\" aria-label=\"Permalink: 📈 Next steps\" href=\"#-next-steps\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eFeel free to extend this app in any way you like. Here are some ideas for next steps:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eRecord message history in the database (and generate embeddings on them for RAG memory)\u003c/li\u003e\n\u003cli\u003eSupport more file formats than just markdown\u003c/li\u003e\n\u003cli\u003ePull in documents from the Notion API\u003c/li\u003e\n\u003cli\u003eRestrict chat to user-selected documents\u003c/li\u003e\n\u003cli\u003ePerform RAG on images using CLIP embeddings\u003c/li\u003e\n\u003c/ul\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e💬 Feedback and issues\u003c/h2\u003e\u003ca id=\"user-content--feedback-and-issues\" class=\"anchor\" aria-label=\"Permalink: 💬 Feedback and issues\" href=\"#-feedback-and-issues\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003ePlease file feedback and issues on the \u003ca href=\"https://github.com/supabase-community/chatgpt-your-files/issues/new/choose\"\u003eon this repo's issue board\u003c/a\u003e.\u003c/p\u003e\n\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch2 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003e🔗 Supabase Vector resources\u003c/h2\u003e\u003ca id=\"user-content--supabase-vector-resources\" class=\"anchor\" aria-label=\"Permalink: 🔗 Supabase Vector resources\" href=\"#-supabase-vector-resources\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"https://supabase.com/docs/guides/ai\" rel=\"nofollow\"\u003eSupabase AI \u0026amp; Vector\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://supabase.com/docs/guides/ai/vector-columns\" rel=\"nofollow\"\u003epgvector Columns\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://supabase.com/docs/guides/ai/vector-indexes\" rel=\"nofollow\"\u003epgvector Indexes\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://supabase.com/docs/guides/ai/quickstarts/generate-text-embeddings\" rel=\"nofollow\"\u003eGenerate Embeddings using Edge Functions\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://supabase.com/docs/guides/ai/going-to-prod\" rel=\"nofollow\"\u003eGoing to Production\u003c/a\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/article\u003e","loaded":true,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":[{"level":1,"text":"Workshop: pgvector to Prod in 2 hours","anchor":"workshop-pgvector-to-prod-in-2-hours","htmlText":"Workshop: pgvector to Prod in 2 hours"},{"level":2,"text":"☑️ Features","anchor":"️-features","htmlText":"☑️ Features"},{"level":2,"text":"🎥 YouTube video","anchor":"-youtube-video","htmlText":"🎥 YouTube video"},{"level":2,"text":"📄 Workshop Instructions","anchor":"-workshop-instructions","htmlText":"📄 Workshop Instructions"},{"level":2,"text":"🧱 Pre-req’s","anchor":"-pre-reqs","htmlText":"🧱 Pre-req’s"},{"level":2,"text":"💿 Sample Data","anchor":"-sample-data","htmlText":"💿 Sample Data"},{"level":2,"text":"🪜 Step-by-step","anchor":"-step-by-step","htmlText":"🪜 Step-by-step"},{"level":3,"text":"Step 0 - Setup","anchor":"step-0---setup","htmlText":"Step 0 - Setup"},{"level":4,"text":"Scaffold Frontend","anchor":"scaffold-frontend","htmlText":"Scaffold Frontend"},{"level":3,"text":"Step 1 - Storage","anchor":"step-1---storage","htmlText":"Step 1 - Storage"},{"level":4,"text":"Install dependencies","anchor":"install-dependencies","htmlText":"Install dependencies"},{"level":4,"text":"Setup Supabase stack","anchor":"setup-supabase-stack","htmlText":"Setup Supabase stack"},{"level":5,"text":"Local","anchor":"local","htmlText":"Local"},{"level":5,"text":"Cloud","anchor":"cloud","htmlText":"Cloud"},{"level":4,"text":"Build a SQL migration","anchor":"build-a-sql-migration","htmlText":"Build a SQL migration"},{"level":4,"text":"Modify frontend","anchor":"modify-frontend","htmlText":"Modify frontend"},{"level":4,"text":"Improve upload RLS policy","anchor":"improve-upload-rls-policy","htmlText":"Improve upload RLS policy"},{"level":3,"text":"Step 2 - Documents","anchor":"step-2---documents","htmlText":"Step 2 - Documents"},{"level":4,"text":"Add a new SQL migration","anchor":"add-a-new-sql-migration","htmlText":"Add a new SQL migration"},{"level":4,"text":"Edge function for process","anchor":"edge-function-for-process","htmlText":"Edge function for process"},{"level":4,"text":"Display documents on the frontend","anchor":"display-documents-on-the-frontend","htmlText":"Display documents on the frontend"},{"level":3,"text":"Step 3 - Embeddings","anchor":"step-3---embeddings","htmlText":"Step 3 - Embeddings"},{"level":4,"text":"Create SQL migration","anchor":"create-sql-migration","htmlText":"Create SQL migration"},{"level":4,"text":"Create Edge Function for embed","anchor":"create-edge-function-for-embed","htmlText":"Create Edge Function for embed"},{"level":3,"text":"Step 4 - Chat","anchor":"step-4---chat","htmlText":"Step 4 - Chat"},{"level":4,"text":"Update Frontend","anchor":"update-frontend","htmlText":"Update Frontend"},{"level":4,"text":"SQL Migration","anchor":"sql-migration","htmlText":"SQL Migration"},{"level":4,"text":"Create chat Edge Function","anchor":"create-chat-edge-function","htmlText":"Create chat Edge Function"},{"level":4,"text":"Try it!","anchor":"try-it","htmlText":"Try it!"},{"level":3,"text":"Step 5 - Database Types (Bonus)","anchor":"step-5---database-types-bonus","htmlText":"Step 5 - Database Types (Bonus)"},{"level":3,"text":"You're done!","anchor":"youre-done","htmlText":"You're done!"},{"level":2,"text":"🚀 Going to prod","anchor":"-going-to-prod","htmlText":"🚀 Going to prod"},{"level":2,"text":"📈 Next steps","anchor":"-next-steps","htmlText":"📈 Next steps"},{"level":2,"text":"💬 Feedback and issues","anchor":"-feedback-and-issues","htmlText":"💬 Feedback and issues"},{"level":2,"text":"🔗 Supabase Vector resources","anchor":"-supabase-vector-resources","htmlText":"🔗 Supabase Vector resources"}],"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fsupabase-community%2Fchatgpt-your-files"}},{"displayName":"CODE_OF_CONDUCT.md","repoName":".github","refName":"main","path":"CODE_OF_CONDUCT.md","preferredFileType":"code_of_conduct","tabName":"Code of conduct","richText":null,"loaded":false,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":null,"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fsupabase-community%2Fchatgpt-your-files"}},{"displayName":"CONTRIBUTING.md","repoName":".github","refName":"main","path":"CONTRIBUTING.md","preferredFileType":"contributing","tabName":"Contributing","richText":null,"loaded":false,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":null,"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fsupabase-community%2Fchatgpt-your-files"}}],"overviewFilesProcessingTime":0,"copilotSWEAgentEnabled":false}},"appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-0cea8c6113ab.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-dc3831241a86.js","githubDevUrl":null,"enabled_features":{"copilot_workspace":null,"code_nav_ui_events":false,"react_blob_overlay":false,"accessible_code_button":true}}}}</script>
  <div data-target="react-partial.reactRoot"> <!-- --> <!-- --> <div class="OverviewContent-module__Box--uNd1J"><div class="OverviewHeader-module__Box--fFKf5"></div><div class="OverviewContent-module__Box_1--RhaEy"><div class="OverviewContent-module__Box_2--uHewD"><div class="OverviewContent-module__Box_3--NEYWl"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" style="min-width:0" aria-label="main branch" data-testid="anchor-button" class="prc-Button-ButtonBase-9n-Xk overview-ref-selector width-full RefSelectorAnchoredOverlay-module__RefSelectorOverlayBtn--D34zl" data-loading="false" data-size="medium" data-variant="default" id="ref-picker-repos-header-ref-selector"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayContainer--mCbv8"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayHeader--D4cnZ"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="ref-selector-button-text-container RefSelectorAnchoredOverlay-module__RefSelectorBtnTextContainer--yO402"><span class="RefSelectorAnchoredOverlay-module__RefSelectorText--bxVhQ"> <!-- -->main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-testid="ref-selector-hotkey-button" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="OverviewContent-module__Box_4--rOz8J"><a type="button" href="/supabase-community/chatgpt-your-files/branches" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button--MDoYP" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Branches</span></span></a><a type="button" href="/supabase-community/chatgpt-your-files/tags" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button--MDoYP" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-tag" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Tags</span></span></a></div><div class="OverviewContent-module__Box_5--PPbL1"><a type="button" aria-label="Go to Branches page" href="/supabase-community/chatgpt-your-files/branches" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button_1--_1Ng2" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></a><a type="button" aria-label="Go to Tags page" href="/supabase-community/chatgpt-your-files/tags" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button_1--_1Ng2" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible"><svg aria-hidden="true" focusable="false" class="octicon octicon-tag" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path></svg></a></div></div><div class="OverviewContent-module__Box_6--wV7Tw"><div class="OverviewContent-module__Box_7--SbxdI"><div class="OverviewContent-module__Box_8--oumpR"><!--$--><div class="Box-sc-62in7e-0 OverviewContent-module__FileResultsList--irMg6"><span class="TextInput__StyledTextInput-sc-ttxlvl-0 d-flex FileResultsList-module__FilesSearchBox--fSAh3 TextInput-wrapper prc-components-TextInputWrapper-Hpdqi prc-components-TextInputBaseWrapper-wY-n0" data-leading-visual="true" data-trailing-visual="true" aria-busy="false"><span class="TextInput-icon" id=":R535ab:" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autoCorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby=":R535ab: :R535abH1:" data-component="input" class="prc-components-Input-IwWrt" value=""/><span class="TextInput-icon" id=":R535abH1:" aria-hidden="true"></span></span></div><!--/$--></div><div class="OverviewContent-module__Box_9--mQYON"><button type="button" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Go to file</span></span></button></div></div><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-size="medium" data-variant="primary" id=":R75ab:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-code hide-sm" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Code</span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><div class="OverviewContent-module__Box_10--ULKAG"><button data-component="IconButton" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby=":R7p5ab:" id=":R95ab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id=":R7p5ab:">Open more actions menu</span></div></div></div><div class="OverviewContent-module__Box_11--Tqhu2"><div data-hpc="true"><button hidden="" data-testid="focus-next-element-button" data-hotkey="j"></button><button hidden="" data-testid="focus-previous-element-button" data-hotkey="k"></button><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="folders-and-files">Folders and files</h2><table class="Table-module__Box--KyMHK" aria-labelledby="folders-and-files"><thead class="DirectoryContent-module__OverviewHeaderRow--FlrUZ Table-module__Box_1--DkRqs"><tr class="Table-module__Box_2--l1wjV"><th colSpan="2" class="DirectoryContent-module__Box--y3Nvf"><span class="text-bold">Name</span></th><th colSpan="1" class="DirectoryContent-module__Box_1--xeAhp"><span class="text-bold">Name</span></th><th class="hide-sm"><div class="width-fit prc-Truncate-Truncate-2G1eo" data-inline="true" title="Last commit message" style="--truncate-max-width:125px"><span class="text-bold">Last commit message</span></div></th><th colSpan="1" class="DirectoryContent-module__Box_2--h912w"><div class="width-fit prc-Truncate-Truncate-2G1eo" data-inline="true" title="Last commit date" style="--truncate-max-width:125px"><span class="text-bold">Last commit date</span></div></th></tr></thead><tbody><tr class="DirectoryContent-module__Box_3--zI0N1"><td colSpan="3" class="bgColor-muted p-1 rounded-top-2"><div class="LatestCommit-module__Box--Fimpo"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">Latest commit</h2><div style="width:120px" class="Skeleton Skeleton--text" data-testid="loading"> </div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">History</h2><a href="/supabase-community/chatgpt-your-files/commits/main/" class="prc-Button-ButtonBase-9n-Xk d-none d-lg-flex LinkButton-module__code-view-link-button--thtqc flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="fgColor-default">55 Commits</span></span></span></a><div class="d-sm-none"></div><div class="d-flex d-lg-none"><span role="tooltip" aria-label="55 Commits" id="history-icon-button-tooltip" class="prc-Tooltip-Tooltip-JLsri prc-Tooltip-Tooltip--n-SqCQ- tooltipped-n"><a aria-label="View commit history for this file." href="/supabase-community/chatgpt-your-files/commits/main/" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__code-view-link-button--thtqc flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby="history-icon-button-tooltip"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-0"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".vscode" aria-label=".vscode, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/.vscode" data-discover="true">.vscode</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".vscode" aria-label=".vscode, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/.vscode" data-discover="true">.vscode</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-1"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="app" aria-label="app, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/app" data-discover="true">app</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="app" aria-label="app, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/app" data-discover="true">app</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-2"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="assets" aria-label="assets, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/assets" data-discover="true">assets</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="assets" aria-label="assets, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/assets" data-discover="true">assets</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-3"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="components" aria-label="components, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/components" data-discover="true">components</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="components" aria-label="components, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/components" data-discover="true">components</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-4"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="lib" aria-label="lib, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/lib" data-discover="true">lib</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="lib" aria-label="lib, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/lib" data-discover="true">lib</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-5"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="sample-files" aria-label="sample-files, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/sample-files" data-discover="true">sample-files</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="sample-files" aria-label="sample-files, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/sample-files" data-discover="true">sample-files</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-6"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="supabase" aria-label="supabase, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/supabase" data-discover="true">supabase</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill icon-directory" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="supabase" aria-label="supabase, (Directory)" class="Link--primary" href="/supabase-community/chatgpt-your-files/tree/main/supabase" data-discover="true">supabase</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-7"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".env.local.example" aria-label=".env.local.example, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/.env.local.example" data-discover="true">.env.local.example</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".env.local.example" aria-label=".env.local.example, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/.env.local.example" data-discover="true">.env.local.example</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-8"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".gitignore" aria-label=".gitignore, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/.gitignore" data-discover="true">.gitignore</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title=".gitignore" aria-label=".gitignore, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/.gitignore" data-discover="true">.gitignore</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row undefined" id="folder-row-9"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="README.md" aria-label="README.md, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/README.md" data-discover="true">README.md</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="README.md" aria-label="README.md, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/README.md" data-discover="true">README.md</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-10"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="components.json" aria-label="components.json, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/components.json" data-discover="true">components.json</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="components.json" aria-label="components.json, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/components.json" data-discover="true">components.json</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-11"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="middleware.ts" aria-label="middleware.ts, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/middleware.ts" data-discover="true">middleware.ts</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="middleware.ts" aria-label="middleware.ts, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/middleware.ts" data-discover="true">middleware.ts</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-12"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="next.config.js" aria-label="next.config.js, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/next.config.js" data-discover="true">next.config.js</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="next.config.js" aria-label="next.config.js, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/next.config.js" data-discover="true">next.config.js</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-13"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="package-lock.json" aria-label="package-lock.json, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/package-lock.json" data-discover="true">package-lock.json</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="package-lock.json" aria-label="package-lock.json, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/package-lock.json" data-discover="true">package-lock.json</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-14"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="package.json" aria-label="package.json, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/package.json" data-discover="true">package.json</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="package.json" aria-label="package.json, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/package.json" data-discover="true">package.json</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-15"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="postcss.config.js" aria-label="postcss.config.js, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/postcss.config.js" data-discover="true">postcss.config.js</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="postcss.config.js" aria-label="postcss.config.js, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/postcss.config.js" data-discover="true">postcss.config.js</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-16"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="tailwind.config.js" aria-label="tailwind.config.js, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/tailwind.config.js" data-discover="true">tailwind.config.js</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="tailwind.config.js" aria-label="tailwind.config.js, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/tailwind.config.js" data-discover="true">tailwind.config.js</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="react-directory-row truncate-for-mobile" id="folder-row-17"><td class="react-directory-row-name-cell-small-screen" colSpan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="tsconfig.json" aria-label="tsconfig.json, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/tsconfig.json" data-discover="true">tsconfig.json</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colSpan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="tsconfig.json" aria-label="tsconfig.json, (File)" class="Link--primary" href="/supabase-community/chatgpt-your-files/blob/main/tsconfig.json" data-discover="true">tsconfig.json</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div class="Skeleton Skeleton--text"> </div></td><td><div class="Skeleton Skeleton--text"> </div></td></tr><tr class="show-for-mobile DirectoryContent-module__Box_4--QyUbd" data-testid="view-all-files-row"><td colSpan="3" class="DirectoryContent-module__Box_5--OJZQU"><div><button class="prc-Link-Link-9ZwDx">View all files</button></div></td></tr></tbody></table></div><div class="OverviewRepoFiles-module__Box_1--xSt0T"><div class="OverviewRepoFiles-module__Box_2--yIjMp"><div itemscope="" itemType="https://schema.org/abstract" class="OverviewRepoFiles-module__Box_3--Bi2jM"><h2 class="prc-src-InternalVisuallyHidden-2YaI6">Repository files navigation</h2><nav class="prc-components-UnderlineWrapper-eT-Yj OverviewRepoFiles-module__UnderlineNav--BHfFi" aria-label="Repository files" data-variant="inset"><ul class="prc-components-UnderlineItemList-xKlKC" role="list"><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="#" aria-current="page" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-book" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path></svg></span><span data-component="text" data-content="README">README</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="#" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-code-of-conduct" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8.048 2.241c.964-.709 2.079-1.238 3.325-1.241a4.616 4.616 0 0 1 3.282 1.355c.41.408.757.86.996 1.428.238.568.348 1.206.347 1.968 0 2.193-1.505 4.254-3.081 5.862-1.496 1.526-3.213 2.796-4.249 3.563l-.22.163a.749.749 0 0 1-.895 0l-.221-.163c-1.036-.767-2.753-2.037-4.249-3.563C1.51 10.008.007 7.952.002 5.762a4.614 4.614 0 0 1 1.353-3.407C3.123.585 6.223.537 8.048 2.24Zm-1.153.983c-1.25-1.033-3.321-.967-4.48.191a3.115 3.115 0 0 0-.913 2.335c0 1.556 1.109 3.24 2.652 4.813C5.463 11.898 6.96 13.032 8 13.805c.353-.262.758-.565 1.191-.905l-1.326-1.223a.75.75 0 0 1 1.018-1.102l1.48 1.366c.328-.281.659-.577.984-.887L9.99 9.802a.75.75 0 1 1 1.019-1.103l1.384 1.28c.295-.329.566-.661.81-.995L12.92 8.7l-1.167-1.168c-.674-.671-1.78-.664-2.474.03-.268.269-.538.537-.802.797-.893.882-2.319.843-3.185-.032-.346-.35-.693-.697-1.043-1.047a.75.75 0 0 1-.04-1.016c.162-.191.336-.401.52-.623.62-.748 1.356-1.637 2.166-2.417Zm7.112 4.442c.313-.65.491-1.293.491-1.916v-.001c0-.614-.088-1.045-.23-1.385-.143-.339-.357-.633-.673-.949a3.111 3.111 0 0 0-2.218-.915c-1.092.003-2.165.627-3.226 1.602-.823.755-1.554 1.637-2.228 2.45l-.127.154.562.566a.755.755 0 0 0 1.066.02l.794-.79c1.258-1.258 3.312-1.31 4.594-.032.396.394.792.791 1.173 1.173Z"></path></svg></span><span data-component="text" data-content="Code of conduct">Code of conduct</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="#" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-people" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path></svg></span><span data-component="text" data-content="Contributing">Contributing</span></a></li></ul></nav><button type="button" aria-label="Outline" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk OverviewRepoFiles-module__ActionMenu_Button--xB9DS" data-loading="false" data-size="medium" data-variant="invisible" id=":Rr9ab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-list-unordered" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg></button></div><div class="Box-sc-62in7e-0 js-snippet-clipboard-copy-unpositioned DirectoryRichtextContent-module__SharedMarkdownContent--BTKsc" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><p dir="auto"><a target="_blank" rel="noopener noreferrer" href="/supabase-community/chatgpt-your-files/blob/main/assets/hero.png"><img alt="pgvector to Prod in 2 hours" src="/supabase-community/chatgpt-your-files/raw/main/assets/hero.png" style="max-width: 100%;"></a></p>
<div class="markdown-heading" dir="auto"><h1 align="center" tabindex="-1" class="heading-element" dir="auto">Workshop: pgvector to Prod in 2 hours</h1><a id="user-content-workshop-pgvector-to-prod-in-2-hours" class="anchor" aria-label="Permalink: Workshop: pgvector to Prod in 2 hours" href="#workshop-pgvector-to-prod-in-2-hours"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p align="center" dir="auto">
Create a production-ready MVP for securely chatting with your documents.
</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">☑️ Features</h2><a id="user-content-️-features" class="anchor" aria-label="Permalink: ☑️ Features" href="#️-features"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li><strong>Interactive Chat Interface:</strong> Interact with your documentation, leveraging the capabilities of OpenAI’s GPT models and retrieval augmented generation (RAG).</li>
<li><strong>Login With &lt;3rd Party&gt;:</strong> Integrate one-click 3rd party login with any of our 18 auth providers and user/password.</li>
<li><strong>Document Storage:</strong> Securely upload, store, and retrieve user uploaded documents.</li>
<li><strong>REST API:</strong> Expose a flexible REST API that we’ll consume to build the interactive front-end.</li>
<li><strong>Row-level Security:</strong> Secure all of your user data user data with production-ready row-level security.</li>
</ul>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🎥 YouTube video</h2><a id="user-content--youtube-video" class="anchor" aria-label="Permalink: 🎥 YouTube video" href="#-youtube-video"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">This entire workshop was recorded as a YouTube video. Feel free to watch it here:</p>
<p dir="auto"><a href="https://www.youtube.com/watch?v=ibzlEQmgPPY" rel="nofollow">https://www.youtube.com/watch?v=ibzlEQmgPPY</a></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">📄 Workshop Instructions</h2><a id="user-content--workshop-instructions" class="anchor" aria-label="Permalink: 📄 Workshop Instructions" href="#-workshop-instructions"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Thanks for joining! Let's dive in.</p>
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="/supabase-community/chatgpt-your-files/blob/main/assets/instructions.png"><img src="/supabase-community/chatgpt-your-files/raw/main/assets/instructions.png" alt="Workshop instructions" style="max-width: 100%;"></a></p>
<ol dir="auto">
<li>
<p dir="auto"><strong>Clone repo:</strong> Clone this repo at tag <code>step-1</code>:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="git clone -b step-1 https://github.com/supabase-community/chatgpt-your-files.git"><pre>git clone -b step-1 https://github.com/supabase-community/chatgpt-your-files.git</pre></div>
<p dir="auto">This will automatically clone at <a href="#step-1---storage">step 1</a>, our starting point.</p>
</li>
<li>
<p dir="auto"><strong>Git checkpoints:</strong> The workshop is broken down into steps (git tags). There's a step for every major feature we are building.</p>
<p dir="auto">Feel free to follow along live with the presenter. When it's time to jump to the next step, run:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="git stash push -u # stash your working directory
git checkout step-X # jump to a checkpoint (replace X wit step #)"><pre>git stash push -u <span class="pl-c"><span class="pl-c">#</span> stash your working directory</span>
git checkout step-X <span class="pl-c"><span class="pl-c">#</span> jump to a checkpoint (replace X wit step #)</span></pre></div>
</li>
<li>
<p dir="auto"><strong>Step-by-step guide:</strong> These steps are written out line-by-line. Feel free to follow along using the <a href="#step-by-step">steps below</a>.</p>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🧱 Pre-req’s</h2><a id="user-content--pre-reqs" class="anchor" aria-label="Permalink: 🧱 Pre-req’s" href="#-pre-reqs"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li>Unix-based OS (if Windows, WSL2)</li>
<li>Docker</li>
<li>Node.js 18+</li>
</ul>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">💿 Sample Data</h2><a id="user-content--sample-data" class="anchor" aria-label="Permalink: 💿 Sample Data" href="#-sample-data"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">This repository includes 3 sample markdown files that we'll use to test the app:</p>
<p dir="auto"><a href="/supabase-community/chatgpt-your-files/blob/main/sample-files/roman-empire-1.md"><code>./sample-files/roman-empire-1.md</code></a></p>
<p dir="auto"><a href="/supabase-community/chatgpt-your-files/blob/main/sample-files/roman-empire-2.md"><code>./sample-files/roman-empire-2.md</code></a></p>
<p dir="auto"><a href="/supabase-community/chatgpt-your-files/blob/main/sample-files/roman-empire-3.md"><code>./sample-files/roman-empire-3.md</code></a></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🪜 Step-by-step</h2><a id="user-content--step-by-step" class="anchor" aria-label="Permalink: 🪜 Step-by-step" href="#-step-by-step"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Jump to a step:</p>
<ol dir="auto">
<li><a href="#step-1---storage">Storage</a></li>
<li><a href="#step-2---documents">Documents</a></li>
<li><a href="#step-3---embeddings">Embeddings</a></li>
<li><a href="#step-4---chat">Chat</a></li>
<li><a href="#step-5---database-types-bonus">Database Types</a> (Bonus)</li>
<li><a href="#youre-done">You're done!</a></li>
</ol>
<hr>
<details>
<summary><strong>Step 0 - Setup</strong> <em>(Optional)</em></summary>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><code>Step 0</code> - Setup</h3><a id="user-content-step-0---setup" class="anchor" aria-label="Permalink: Step 0 - Setup" href="#step-0---setup"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><em>Use this command to jump to the <code>step-0</code> checkpoint.</em></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="git checkout step-0"><pre>git checkout step-0</pre></div>
<p dir="auto">The beginning of step 0 is aka to:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx create-next-app -e with-supabase"><pre>npx create-next-app -e with-supabase</pre></div>
<p dir="auto">Refer to this step if you want to learn about the additions added on top of <code>create-next-app</code> to get us up and running quicker for this workshop <em>(VS Code settings, UI components/styles/layouts)</em>. Otherwise, skip straight to <a href="#step-1---storage"><code>step-1</code></a>.</p>
<ol dir="auto">
<li>
<p dir="auto">Install Supabase as dev dependency.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npm i -D supabase@1.102.0"><pre>npm i -D supabase@1.102.0</pre></div>
</li>
<li>
<p dir="auto">Initialize Supabase project.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase init"><pre>npx supabase init</pre></div>
</li>
<li>
<p dir="auto">(Optional) Setup VSCode environment.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="mkdir -p .vscode &amp;&amp; cat &gt; .vscode/settings.json &lt;&lt;- EOF
{
  &quot;deno.enable&quot;: true,
  &quot;deno.lint&quot;: true,
  &quot;deno.unstable&quot;: false,
  &quot;deno.enablePaths&quot;: [
    &quot;supabase&quot;
  ],
  &quot;deno.importMap&quot;: &quot;./supabase/functions/import_map.json&quot;
}
EOF"><pre>mkdir -p .vscode <span class="pl-k">&amp;&amp;</span> cat <span class="pl-k">&gt;</span> .vscode/settings.json <span class="pl-s"><span class="pl-k">&lt;&lt;</span>- <span class="pl-k">EOF</span></span>
<span class="pl-s">{</span>
<span class="pl-s">  "deno.enable": true,</span>
<span class="pl-s">  "deno.lint": true,</span>
<span class="pl-s">  "deno.unstable": false,</span>
<span class="pl-s">  "deno.enablePaths": [</span>
<span class="pl-s">    "supabase"</span>
<span class="pl-s">  ],</span>
<span class="pl-s">  "deno.importMap": "./supabase/functions/import_map.json"</span>
<span class="pl-s">}</span>
<span class="pl-s"><span class="pl-k">EOF</span></span></pre></div>
</li>
<li>
<p dir="auto">(Optional) Setup VSCode recommended extensions.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="cat &gt; .vscode/extensions.json &lt;&lt;- EOF
{
 &quot;recommendations&quot;: [
   &quot;denoland.vscode-deno&quot;,
   &quot;esbenp.prettier-vscode&quot;,
   &quot;dbaeumer.vscode-eslint&quot;,
   &quot;bradlc.vscode-tailwindcss&quot;,
 ],
}
EOF"><pre>cat <span class="pl-k">&gt;</span> .vscode/extensions.json <span class="pl-s"><span class="pl-k">&lt;&lt;</span>- <span class="pl-k">EOF</span></span>
<span class="pl-s">{</span>
<span class="pl-s"> "recommendations": [</span>
<span class="pl-s">   "denoland.vscode-deno",</span>
<span class="pl-s">   "esbenp.prettier-vscode",</span>
<span class="pl-s">   "dbaeumer.vscode-eslint",</span>
<span class="pl-s">   "bradlc.vscode-tailwindcss",</span>
<span class="pl-s"> ],</span>
<span class="pl-s">}</span>
<span class="pl-s"><span class="pl-k">EOF</span></span></pre></div>
<p dir="auto">Then <code>cmd</code>+<code>shift</code>+<code>p</code> → <code>&gt;show recommended extensions</code> → install all <em>(or whichever you like)</em></p>
</li>
<li>
<p dir="auto">Create <code>import_map.json</code> with dependencies for our Supabase Edge Functions. We'll talk more about this in <a href="#step-2---documents">step 2</a>.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="cat &gt; supabase/functions/import_map.json &lt;&lt;- EOF
 {
   &quot;imports&quot;: {
     &quot;@std/&quot;: &quot;https://deno.land/std@0.168.0/&quot;,

     &quot;@supabase/supabase-js&quot;: &quot;https://esm.sh/@supabase/supabase-js@2.21.0&quot;,
     &quot;openai&quot;: &quot;https://esm.sh/openai@4.10.0&quot;,
     &quot;common-tags&quot;: &quot;https://esm.sh/common-tags@1.8.2&quot;,
     &quot;ai&quot;: &quot;https://esm.sh/ai@2.2.13&quot;,

     &quot;mdast-util-from-markdown&quot;: &quot;https://esm.sh/v132/mdast-util-from-markdown@2.0.0&quot;,
     &quot;mdast-util-to-markdown&quot;: &quot;https://esm.sh/v132/mdast-util-to-markdown@2.1.0&quot;,
     &quot;mdast-util-to-string&quot;: &quot;https://esm.sh/v132/mdast-util-to-string@4.0.0&quot;,
     &quot;unist-builder&quot;: &quot;https://esm.sh/v132/unist-builder@4.0.0&quot;,
     &quot;mdast&quot;: &quot;https://esm.sh/v132/@types/mdast@4.0.0/index.d.ts&quot;,

     &quot;https://esm.sh/v132/decode-named-character-reference@1.0.2/esnext/decode-named-character-reference.mjs&quot;: &quot;https://esm.sh/decode-named-character-reference@1.0.2?target=deno&quot;
   }
 }
 EOF"><pre>cat <span class="pl-k">&gt;</span> supabase/functions/import_map.json <span class="pl-s"><span class="pl-k">&lt;&lt;</span>- <span class="pl-k">EOF</span></span>
<span class="pl-s"> {</span>
<span class="pl-s">   "imports": {</span>
<span class="pl-s">     "@std/": "https://deno.land/std@0.168.0/",</span>
<span class="pl-s"></span>
<span class="pl-s">     "@supabase/supabase-js": "https://esm.sh/@supabase/supabase-js@2.21.0",</span>
<span class="pl-s">     "openai": "https://esm.sh/openai@4.10.0",</span>
<span class="pl-s">     "common-tags": "https://esm.sh/common-tags@1.8.2",</span>
<span class="pl-s">     "ai": "https://esm.sh/ai@2.2.13",</span>
<span class="pl-s"></span>
<span class="pl-s">     "mdast-util-from-markdown": "https://esm.sh/v132/mdast-util-from-markdown@2.0.0",</span>
<span class="pl-s">     "mdast-util-to-markdown": "https://esm.sh/v132/mdast-util-to-markdown@2.1.0",</span>
<span class="pl-s">     "mdast-util-to-string": "https://esm.sh/v132/mdast-util-to-string@4.0.0",</span>
<span class="pl-s">     "unist-builder": "https://esm.sh/v132/unist-builder@4.0.0",</span>
<span class="pl-s">     "mdast": "https://esm.sh/v132/@types/mdast@4.0.0/index.d.ts",</span>
<span class="pl-s"></span>
<span class="pl-s">     "https://esm.sh/v132/decode-named-character-reference@1.0.2/esnext/decode-named-character-reference.mjs": "https://esm.sh/decode-named-character-reference@1.0.2?target=deno"</span>
<span class="pl-s">   }</span>
<span class="pl-s"> }</span>
<span class="pl-s"> EOF</span></pre></div>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Scaffold Frontend</h4><a id="user-content-scaffold-frontend" class="anchor" aria-label="Permalink: Scaffold Frontend" href="#scaffold-frontend"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">We use <a href="https://ui.shadcn.com/docs" rel="nofollow"><code>shadcn/ui</code></a> for our UI components.</p>
<ol dir="auto">
<li>
<p dir="auto">Initialize <code>shadcn-ui</code>.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx shadcn-ui@latest init"><pre>npx shadcn-ui@latest init</pre></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="Would you like to use TypeScript (recommended)? yes
Which style would you like to use? › Default
Which color would you like to use as base color? › Slate
Where is your global CSS file? › › app/globals.css
Do you want to use CSS variables for colors? › yes
Where is your tailwind.config.js located? › tailwind.config.js
Configure the import alias for components: › @/components
Configure the import alias for utils: › @/lib/utils
Are you using React Server Components? › yes"><pre>Would you like to use TypeScript (recommended)<span class="pl-k">?</span> yes
Which style would you like to use<span class="pl-k">?</span> › Default
Which color would you like to use as base color<span class="pl-k">?</span> › Slate
Where is your global CSS file<span class="pl-k">?</span> › › app/globals.css
Do you want to use CSS variables <span class="pl-k">for</span> colors<span class="pl-k">?</span> › yes
Where is your tailwind.config.js located<span class="pl-k">?</span> › tailwind.config.js
Configure the import <span class="pl-c1">alias</span> <span class="pl-k">for</span> components: › @/components
Configure the import <span class="pl-c1">alias</span> <span class="pl-k">for</span> utils: › @/lib/utils
Are you using React Server Components<span class="pl-k">?</span> › yes</pre></div>
</li>
<li>
<p dir="auto">Add components.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx shadcn-ui@latest add button input toast"><pre>npx shadcn-ui@latest add button input toast</pre></div>
</li>
<li>
<p dir="auto">Install dependencies.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npm i @tanstack/react-query three-dots"><pre>npm i @tanstack/react-query three-dots</pre></div>
</li>
<li>
<p dir="auto">Wrap the app in a <code>&lt;QueryClientProvider&gt;</code>.</p>
</li>
<li>
<p dir="auto">Build layouts.</p>
</li>
</ol>
</details>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><code>Step 1</code> - Storage</h3><a id="user-content-step-1---storage" class="anchor" aria-label="Permalink: Step 1 - Storage" href="#step-1---storage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><em>Use this command to jump to the <code>step-1</code> checkpoint.</em></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="git checkout step-1"><pre>git checkout step-1</pre></div>
<p dir="auto">We'll start by handling file uploads. Supabase has a built-in object storage (backed by S3 under the hood) that integrates directly with your Postgres database.</p>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Install dependencies</h4><a id="user-content-install-dependencies" class="anchor" aria-label="Permalink: Install dependencies" href="#install-dependencies"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">First install NPM dependencies.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npm i"><pre>npm i</pre></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Setup Supabase stack</h4><a id="user-content-setup-supabase-stack" class="anchor" aria-label="Permalink: Setup Supabase stack" href="#setup-supabase-stack"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">When developing a project in Supabase, you can choose to develop locally or directly on the cloud.</p>
<div class="markdown-heading" dir="auto"><h5 tabindex="-1" class="heading-element" dir="auto">Local</h5><a id="user-content-local" class="anchor" aria-label="Permalink: Local" href="#local"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>
<p dir="auto">Start a local version of Supabase <em>(runs in Docker)</em>.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase start"><pre>npx supabase start</pre></div>
</li>
<li>
<p dir="auto">Store the Supabase URL &amp; public anon key in <code>.env.local</code> for Next.js.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase status -o env \
  --override-name api.url=NEXT_PUBLIC_SUPABASE_URL \
  --override-name auth.anon_key=NEXT_PUBLIC_SUPABASE_ANON_KEY |
    grep NEXT_PUBLIC &gt; .env.local"><pre>npx supabase status -o env \
  --override-name api.url=NEXT_PUBLIC_SUPABASE_URL \
  --override-name auth.anon_key=NEXT_PUBLIC_SUPABASE_ANON_KEY <span class="pl-k">|</span>
    grep NEXT_PUBLIC <span class="pl-k">&gt;</span> .env.local</pre></div>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h5 tabindex="-1" class="heading-element" dir="auto">Cloud</h5><a id="user-content-cloud" class="anchor" aria-label="Permalink: Cloud" href="#cloud"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>
<p dir="auto">Create a Supabase project at <a href="https://database.new" rel="nofollow">https://database.new</a>, or via the CLI:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase projects create -i &quot;ChatGPT Your Files&quot;"><pre>npx supabase projects create -i <span class="pl-s"><span class="pl-pds">"</span>ChatGPT Your Files<span class="pl-pds">"</span></span></pre></div>
<p dir="auto">Your Org ID can be found in the URL after <a href="https://supabase.com/dashboard/org/_/general" rel="nofollow">selecting an org</a>.</p>
</li>
<li>
<p dir="auto">Link your CLI to the project.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase link --project-ref=&lt;project-id&gt;"><pre>npx supabase link --project-ref=<span class="pl-k">&lt;</span>project-id<span class="pl-k">&gt;</span></pre></div>
<p dir="auto">You can get the project ID from the <a href="https://supabase.com/dashboard/project/_/settings/general" rel="nofollow">general settings page</a>.</p>
</li>
<li>
<p dir="auto">Store Supabase URL &amp; public anon key in <code>.env.local</code> for Next.js.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="NEXT_PUBLIC_SUPABASE_URL=&lt;api-url&gt;
NEXT_PUBLIC_SUPABASE_ANON_KEY=&lt;anon-key&gt;"><pre>NEXT_PUBLIC_SUPABASE_URL=<span class="pl-k">&lt;</span>api-url<span class="pl-k">&gt;</span>
NEXT_PUBLIC_SUPABASE_ANON_KEY=<span class="pl-k">&lt;</span>anon-key<span class="pl-k">&gt;</span></pre></div>
<p dir="auto">You can get the project API URL and anonymous key from the <a href="https://supabase.com/dashboard/project/_/settings/api" rel="nofollow">API settings page</a>.</p>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Build a SQL migration</h4><a id="user-content-build-a-sql-migration" class="anchor" aria-label="Permalink: Build a SQL migration" href="#build-a-sql-migration"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>
<p dir="auto">Create migration file.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase migration new files"><pre>npx supabase migration new files</pre></div>
<p dir="auto">A new file will be created under <code>./supabase/migrations</code>.</p>
</li>
<li>
<p dir="auto">Within that file, create a private schema.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create schema private;"><pre><span class="pl-k">create</span> <span class="pl-k">schema</span> <span class="pl-en">private</span>;</pre></div>
</li>
<li>
<p dir="auto">Add bucket called 'files' via the <code>buckets</code> table in the <code>storage</code> schema.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="insert into storage.buckets (id, name)
values ('files', 'files')
on conflict do nothing;"><pre><span class="pl-k">insert into</span> <span class="pl-c1">storage</span>.<span class="pl-c1">buckets</span> (id, name)
<span class="pl-k">values</span> (<span class="pl-s"><span class="pl-pds">'</span>files<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>files<span class="pl-pds">'</span></span>)
<span class="pl-k">on</span> conflict do nothing;</pre></div>
</li>
<li>
<p dir="auto">Add RLS policies to restrict access to files.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create policy &quot;Authenticated users can upload files&quot;
on storage.objects for insert to authenticated with check (
  bucket_id = 'files' and owner = auth.uid()
);

create policy &quot;Users can view their own files&quot;
on storage.objects for select to authenticated using (
  bucket_id = 'files' and owner = auth.uid()
);

create policy &quot;Users can update their own files&quot;
on storage.objects for update to authenticated with check (
  bucket_id = 'files' and owner = auth.uid()
);

create policy &quot;Users can delete their own files&quot;
on storage.objects for delete to authenticated using (
  bucket_id = 'files' and owner = auth.uid()
);"><pre>create policy <span class="pl-s"><span class="pl-pds">"</span>Authenticated users can upload files<span class="pl-pds">"</span></span>
<span class="pl-k">on</span> <span class="pl-c1">storage</span>.<span class="pl-c1">objects</span> for insert to authenticated with <span class="pl-k">check</span> (
  bucket_id <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>files<span class="pl-pds">'</span></span> <span class="pl-k">and</span> owner <span class="pl-k">=</span> <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>()
);

create policy <span class="pl-s"><span class="pl-pds">"</span>Users can view their own files<span class="pl-pds">"</span></span>
<span class="pl-k">on</span> <span class="pl-c1">storage</span>.<span class="pl-c1">objects</span> for <span class="pl-k">select</span> to authenticated using (
  bucket_id <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>files<span class="pl-pds">'</span></span> <span class="pl-k">and</span> owner <span class="pl-k">=</span> <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>()
);

create policy <span class="pl-s"><span class="pl-pds">"</span>Users can update their own files<span class="pl-pds">"</span></span>
<span class="pl-k">on</span> <span class="pl-c1">storage</span>.<span class="pl-c1">objects</span> for <span class="pl-k">update</span> to authenticated with <span class="pl-k">check</span> (
  bucket_id <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>files<span class="pl-pds">'</span></span> <span class="pl-k">and</span> owner <span class="pl-k">=</span> <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>()
);

create policy <span class="pl-s"><span class="pl-pds">"</span>Users can delete their own files<span class="pl-pds">"</span></span>
<span class="pl-k">on</span> <span class="pl-c1">storage</span>.<span class="pl-c1">objects</span> for <span class="pl-k">delete</span> to authenticated using (
  bucket_id <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>files<span class="pl-pds">'</span></span> <span class="pl-k">and</span> owner <span class="pl-k">=</span> <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>()
);</pre></div>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Modify frontend</h4><a id="user-content-modify-frontend" class="anchor" aria-label="Permalink: Modify frontend" href="#modify-frontend"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Next let's update <code>./app/files/page.tsx</code> to support file upload.</p>
<ol dir="auto">
<li>
<p dir="auto">Setup Supabase client at the top of the component.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const supabase = createClientComponentClient();"><pre><span class="pl-k">const</span> <span class="pl-s1">supabase</span> <span class="pl-c1">=</span> <span class="pl-en">createClientComponentClient</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">Handle file upload in the <code>&lt;Input&gt;</code>'s <code>onChange</code> prop.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="await supabase.storage
  .from('files')
  .upload(`${crypto.randomUUID()}/${selectedFile.name}`, selectedFile);"><pre><span class="pl-k">await</span> <span class="pl-s1">supabase</span><span class="pl-kos">.</span><span class="pl-c1">storage</span>
  <span class="pl-kos">.</span><span class="pl-en">from</span><span class="pl-kos">(</span><span class="pl-s">'files'</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">upload</span><span class="pl-kos">(</span><span class="pl-s">`<span class="pl-s1"><span class="pl-kos">${</span><span class="pl-s1">crypto</span><span class="pl-kos">.</span><span class="pl-en">randomUUID</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">}</span></span>/<span class="pl-s1"><span class="pl-kos">${</span><span class="pl-s1">selectedFile</span><span class="pl-kos">.</span><span class="pl-c1">name</span><span class="pl-kos">}</span></span>`</span><span class="pl-kos">,</span> <span class="pl-s1">selectedFile</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Improve upload RLS policy</h4><a id="user-content-improve-upload-rls-policy" class="anchor" aria-label="Permalink: Improve upload RLS policy" href="#improve-upload-rls-policy"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">We can improve our previous RLS policy to require a UUID in the uploaded file path.</p>
<ol dir="auto">
<li>
<p dir="auto">Create <code>uuid_or_null()</code> function.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create or replace function private.uuid_or_null(str text)
returns uuid
language plpgsql
as $$
begin
  return str::uuid;
  exception when invalid_text_representation then
    return null;
  end;
$$;"><pre><span class="pl-k">create or replace</span> <span class="pl-k">function</span> <span class="pl-en">private</span>.uuid_or_null(str <span class="pl-k">text</span>)
returns uuid
language plpgsql
<span class="pl-k">as</span> $$
<span class="pl-k">begin</span>
  return str::uuid;
  exception when invalid_text_representation then
    return <span class="pl-k">null</span>;
  end;
$$;</pre></div>
</li>
<li>
<p dir="auto">Modify insert policy to check for UUID in the first path segment <em>(Postgres arrays are 1-based)</em>.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create policy &quot;Authenticated users can upload files&quot;
on storage.objects for insert to authenticated with check (
  bucket_id = 'files' and
    owner = auth.uid() and
    private.uuid_or_null(path_tokens[1]) is not null
);"><pre>create policy <span class="pl-s"><span class="pl-pds">"</span>Authenticated users can upload files<span class="pl-pds">"</span></span>
<span class="pl-k">on</span> <span class="pl-c1">storage</span>.<span class="pl-c1">objects</span> for insert to authenticated with <span class="pl-k">check</span> (
  bucket_id <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>files<span class="pl-pds">'</span></span> <span class="pl-k">and</span>
    owner <span class="pl-k">=</span> <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>() <span class="pl-k">and</span>
    <span class="pl-c1">private</span>.<span class="pl-c1">uuid_or_null</span>(path_tokens[<span class="pl-c1">1</span>]) <span class="pl-k">is not null</span>
);</pre></div>
</li>
<li>
<p dir="auto">Apply the migration to our local database.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase migration up"><pre>npx supabase migration up</pre></div>
<p dir="auto">or if you are developing directly on the cloud, push your migrations up:</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="npx supabase db push"><pre class="notranslate"><code>npx supabase db push
</code></pre></div>
</li>
</ol>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><code>Step 2</code> - Documents</h3><a id="user-content-step-2---documents" class="anchor" aria-label="Permalink: Step 2 - Documents" href="#step-2---documents"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Jump to a step:</p>
<ol dir="auto">
<li><a href="#step-1---storage">Storage</a></li>
<li><a href="#step-2---documents">Documents</a></li>
<li><a href="#step-3---embeddings">Embeddings</a></li>
<li><a href="#step-4---chat">Chat</a></li>
<li><a href="#step-5---database-types-bonus">Database Types</a> (Bonus)</li>
<li><a href="#youre-done">You're done!</a></li>
</ol>
<hr>
<p dir="auto"><em>Use these commands to jump to the <code>step-2</code> checkpoint.</em></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="git stash push -u -m &quot;my work on step-1&quot;
git checkout step-2"><pre>git stash push -u -m <span class="pl-s"><span class="pl-pds">"</span>my work on step-1<span class="pl-pds">"</span></span>
git checkout step-2</pre></div>
<p dir="auto">Next we'll need to process our files for retrieval augmented generation (RAG). Specifically we'll split the contents of our markdown documents by heading, which will allow us to query smaller and more meaningful sections.</p>
<p dir="auto">Let's create a <code>documents</code> and <code>document_sections</code> table to store our processed files.</p>
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="/supabase-community/chatgpt-your-files/blob/main/assets/step-2-er-diagram.png"><img src="/supabase-community/chatgpt-your-files/raw/main/assets/step-2-er-diagram.png" alt="Documents ER diagram" style="max-width: 100%;"></a></p>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Add a new SQL migration</h4><a id="user-content-add-a-new-sql-migration" class="anchor" aria-label="Permalink: Add a new SQL migration" href="#add-a-new-sql-migration"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>
<p dir="auto">Create migration file.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase migration new documents"><pre>npx supabase migration new documents</pre></div>
</li>
<li>
<p dir="auto">Enable <code>pgvector</code> and <code>pg_net</code> extensions.</p>
<p dir="auto">We'll use <code>pg_net</code> later to send HTTP requests to our edge functions.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create extension if not exists pg_net with schema extensions;
create extension if not exists vector with schema extensions;"><pre>create extension if not exists pg_net with schema extensions;
create extension if not exists vector with schema extensions;</pre></div>
</li>
<li>
<p dir="auto">Create <code>documents</code> table.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create table documents (
  id bigint primary key generated always as identity,
  name text not null,
  storage_object_id uuid not null references storage.objects (id),
  created_by uuid not null references auth.users (id) default auth.uid(),
  created_at timestamp with time zone not null default now()
);"><pre><span class="pl-k">create</span> <span class="pl-k">table</span> <span class="pl-en">documents</span> (
  id <span class="pl-k">bigint</span> <span class="pl-k">primary key</span> generated always <span class="pl-k">as</span> identity,
  name <span class="pl-k">text</span> <span class="pl-k">not null</span>,
  storage_object_id uuid <span class="pl-k">not null</span> <span class="pl-k">references</span> <span class="pl-c1">storage</span>.<span class="pl-c1">objects</span> (id),
  created_by uuid <span class="pl-k">not null</span> <span class="pl-k">references</span> <span class="pl-c1">auth</span>.<span class="pl-c1">users</span> (id) default <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>(),
  created_at <span class="pl-k">timestamp with time zone</span> <span class="pl-k">not null</span> default now()
);</pre></div>
</li>
<li>
<p dir="auto">We'll also create a view <code>documents_with_storage_path</code> that provides easy access to the storage object path.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create view documents_with_storage_path
with (security_invoker=true)
as
  select documents.*, storage.objects.name as storage_object_path
  from documents
  join storage.objects
    on storage.objects.id = documents.storage_object_id;"><pre><span class="pl-k">create</span> <span class="pl-k">view</span> <span class="pl-en">documents_with_storage_path</span>
with (security_invoker<span class="pl-k">=</span>true)
<span class="pl-k">as</span>
  <span class="pl-k">select</span> documents.<span class="pl-k">*</span>, <span class="pl-c1">storage</span>.<span class="pl-c1">objects</span>.name <span class="pl-k">as</span> storage_object_path
  <span class="pl-k">from</span> documents
  <span class="pl-k">join</span> <span class="pl-c1">storage</span>.<span class="pl-c1">objects</span>
    <span class="pl-k">on</span> <span class="pl-c1">storage</span>.<span class="pl-c1">objects</span>.id <span class="pl-k">=</span> <span class="pl-c1">documents</span>.<span class="pl-c1">storage_object_id</span>;</pre></div>
</li>
<li>
<p dir="auto">Create <code>document_sections</code> table.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create table document_sections (
  id bigint primary key generated always as identity,
  document_id bigint not null references documents (id),
  content text not null,
  embedding vector (384)
);"><pre><span class="pl-k">create</span> <span class="pl-k">table</span> <span class="pl-en">document_sections</span> (
  id <span class="pl-k">bigint</span> <span class="pl-k">primary key</span> generated always <span class="pl-k">as</span> identity,
  document_id <span class="pl-k">bigint</span> <span class="pl-k">not null</span> <span class="pl-k">references</span> documents (id),
  content <span class="pl-k">text</span> <span class="pl-k">not null</span>,
  embedding vector (<span class="pl-c1">384</span>)
);</pre></div>
<p dir="auto"><em>Note: Since the video was published, <code>on delete cascade</code> was
added as a new migration so that the lifecycle of <code>document_sections</code>
is tied to their respective document.</em></p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="alter table document_sections
drop constraint document_sections_document_id_fkey,
add constraint document_sections_document_id_fkey
  foreign key (document_id)
  references documents(id)
  on delete cascade;"><pre><span class="pl-k">alter</span> <span class="pl-k">table</span> document_sections
drop <span class="pl-k">constraint</span> document_sections_document_id_fkey,
add <span class="pl-k">constraint</span> document_sections_document_id_fkey
  <span class="pl-k">foreign key</span> (document_id)
  <span class="pl-k">references</span> documents(id)
  <span class="pl-k">on delete cascade</span>;</pre></div>
</li>
<li>
<p dir="auto">Add HNSW index.</p>
<p dir="auto">Unlike IVFFlat indexes, HNSW indexes can be create immediately on an empty table.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create index on document_sections using hnsw (embedding vector_ip_ops);"><pre><span class="pl-k">create</span> <span class="pl-k">index</span> <span class="pl-en">on</span> document_sections using hnsw (embedding vector_ip_ops);</pre></div>
</li>
<li>
<p dir="auto">Setup RLS to control who has access to which documents.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="alter table documents enable row level security;
alter table document_sections enable row level security;

create policy &quot;Users can insert documents&quot;
on documents for insert to authenticated with check (
  auth.uid() = created_by
);

create policy &quot;Users can query their own documents&quot;
on documents for select to authenticated using (
  auth.uid() = created_by
);

create policy &quot;Users can insert document sections&quot;
on document_sections for insert to authenticated with check (
  document_id in (
    select id
    from documents
    where created_by = auth.uid()
  )
);

create policy &quot;Users can update their own document sections&quot;
on document_sections for update to authenticated using (
  document_id in (
    select id
    from documents
    where created_by = auth.uid()
  )
) with check (
  document_id in (
    select id
    from documents
    where created_by = auth.uid()
  )
);

create policy &quot;Users can query their own document sections&quot;
on document_sections for select to authenticated using (
  document_id in (
    select id
    from documents
    where created_by = auth.uid()
  )
);"><pre><span class="pl-k">alter</span> <span class="pl-k">table</span> documents enable row level security;
<span class="pl-k">alter</span> <span class="pl-k">table</span> document_sections enable row level security;

create policy <span class="pl-s"><span class="pl-pds">"</span>Users can insert documents<span class="pl-pds">"</span></span>
<span class="pl-k">on</span> documents for insert to authenticated with <span class="pl-k">check</span> (
  <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>() <span class="pl-k">=</span> created_by
);

create policy <span class="pl-s"><span class="pl-pds">"</span>Users can query their own documents<span class="pl-pds">"</span></span>
<span class="pl-k">on</span> documents for <span class="pl-k">select</span> to authenticated using (
  <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>() <span class="pl-k">=</span> created_by
);

create policy <span class="pl-s"><span class="pl-pds">"</span>Users can insert document sections<span class="pl-pds">"</span></span>
<span class="pl-k">on</span> document_sections for insert to authenticated with <span class="pl-k">check</span> (
  document_id <span class="pl-k">in</span> (
    <span class="pl-k">select</span> id
    <span class="pl-k">from</span> documents
    <span class="pl-k">where</span> created_by <span class="pl-k">=</span> <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>()
  )
);

create policy <span class="pl-s"><span class="pl-pds">"</span>Users can update their own document sections<span class="pl-pds">"</span></span>
<span class="pl-k">on</span> document_sections for <span class="pl-k">update</span> to authenticated using (
  document_id <span class="pl-k">in</span> (
    <span class="pl-k">select</span> id
    <span class="pl-k">from</span> documents
    <span class="pl-k">where</span> created_by <span class="pl-k">=</span> <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>()
  )
) with <span class="pl-k">check</span> (
  document_id <span class="pl-k">in</span> (
    <span class="pl-k">select</span> id
    <span class="pl-k">from</span> documents
    <span class="pl-k">where</span> created_by <span class="pl-k">=</span> <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>()
  )
);

create policy <span class="pl-s"><span class="pl-pds">"</span>Users can query their own document sections<span class="pl-pds">"</span></span>
<span class="pl-k">on</span> document_sections for <span class="pl-k">select</span> to authenticated using (
  document_id <span class="pl-k">in</span> (
    <span class="pl-k">select</span> id
    <span class="pl-k">from</span> documents
    <span class="pl-k">where</span> created_by <span class="pl-k">=</span> <span class="pl-c1">auth</span>.<span class="pl-c1">uid</span>()
  )
);</pre></div>
</li>
<li>
<p dir="auto">If developing locally, add <code>supabase_url</code> secret to <code>./supabase/seed.sql</code>. We will use this to query our Edge Functions within our local environment.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="select vault.create_secret(
  'http://api.supabase.internal:8000',
  'supabase_url'
);"><pre><span class="pl-k">select</span> <span class="pl-c1">vault</span>.<span class="pl-c1">create_secret</span>(
  <span class="pl-s"><span class="pl-pds">'</span>http://api.supabase.internal:8000<span class="pl-pds">'</span></span>,
  <span class="pl-s"><span class="pl-pds">'</span>supabase_url<span class="pl-pds">'</span></span>
);</pre></div>
<p dir="auto">If you are developing directly on the cloud, open up the <a href="https://supabase.com/dashboard/project/_/sql/new" rel="nofollow">SQL Editor</a> and set this to your Supabase project's API URL:</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="select vault.create_secret(
  '&lt;api-url&gt;',
  'supabase_url'
);"><pre><span class="pl-k">select</span> <span class="pl-c1">vault</span>.<span class="pl-c1">create_secret</span>(
  <span class="pl-s"><span class="pl-pds">'</span>&lt;api-url&gt;<span class="pl-pds">'</span></span>,
  <span class="pl-s"><span class="pl-pds">'</span>supabase_url<span class="pl-pds">'</span></span>
);</pre></div>
<p dir="auto">You can get the project API URL from the <a href="https://supabase.com/dashboard/project/_/settings/api" rel="nofollow">API settings page</a>.</p>
</li>
<li>
<p dir="auto">Create a function to retrieve the URL.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create function supabase_url()
returns text
language plpgsql
security definer
as $$
declare
  secret_value text;
begin
  select decrypted_secret into secret_value from vault.decrypted_secrets where name = 'supabase_url';
  return secret_value;
end;
$$;"><pre><span class="pl-k">create</span> <span class="pl-k">function</span> <span class="pl-en">supabase_url</span>()
returns <span class="pl-k">text</span>
language plpgsql
security definer
<span class="pl-k">as</span> $$
declare
  secret_value <span class="pl-k">text</span>;
<span class="pl-k">begin</span>
  <span class="pl-k">select</span> decrypted_secret into secret_value <span class="pl-k">from</span> <span class="pl-c1">vault</span>.<span class="pl-c1">decrypted_secrets</span> <span class="pl-k">where</span> name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>supabase_url<span class="pl-pds">'</span></span>;
  return secret_value;
end;
$$;</pre></div>
</li>
<li>
<p dir="auto">Create a trigger to process new documents when they're inserted. This uses <code>pg_net</code> to send an HTTP request to our Edge Function (coming up next).</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create function private.handle_storage_update()
returns trigger
language plpgsql
as $$
declare
  document_id bigint;
  result int;
begin
  insert into documents (name, storage_object_id, created_by)
    values (new.path_tokens[2], new.id, new.owner)
    returning id into document_id;

  select
    net.http_post(
      url := supabase_url() || '/functions/v1/process',
      headers := jsonb_build_object(
        'Content-Type', 'application/json',
        'Authorization', current_setting('request.headers')::json-&gt;&gt;'authorization'
      ),
      body := jsonb_build_object(
        'document_id', document_id
      )
    )
  into result;

  return null;
end;
$$;

create trigger on_file_upload
  after insert on storage.objects
  for each row
  execute procedure private.handle_storage_update();"><pre><span class="pl-k">create</span> <span class="pl-k">function</span> <span class="pl-en">private</span>.handle_storage_update()
returns trigger
language plpgsql
<span class="pl-k">as</span> $$
declare
  document_id <span class="pl-k">bigint</span>;
  result <span class="pl-k">int</span>;
<span class="pl-k">begin</span>
  <span class="pl-k">insert into</span> documents (name, storage_object_id, created_by)
    <span class="pl-k">values</span> (<span class="pl-c1">new</span>.<span class="pl-c1">path_tokens</span>[<span class="pl-c1">2</span>], <span class="pl-c1">new</span>.<span class="pl-c1">id</span>, <span class="pl-c1">new</span>.<span class="pl-c1">owner</span>)
    returning id into document_id;

  <span class="pl-k">select</span>
    <span class="pl-c1">net</span>.<span class="pl-c1">http_post</span>(
      url :<span class="pl-k">=</span> supabase_url() <span class="pl-k">||</span> <span class="pl-s"><span class="pl-pds">'</span>/functions/v1/process<span class="pl-pds">'</span></span>,
      headers :<span class="pl-k">=</span> jsonb_build_object(
        <span class="pl-s"><span class="pl-pds">'</span>Content-Type<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>application/json<span class="pl-pds">'</span></span>,
        <span class="pl-s"><span class="pl-pds">'</span>Authorization<span class="pl-pds">'</span></span>, current_setting(<span class="pl-s"><span class="pl-pds">'</span>request.headers<span class="pl-pds">'</span></span>)::json<span class="pl-k">-</span><span class="pl-k">&gt;&gt;</span><span class="pl-s"><span class="pl-pds">'</span>authorization<span class="pl-pds">'</span></span>
      ),
      body :<span class="pl-k">=</span> jsonb_build_object(
        <span class="pl-s"><span class="pl-pds">'</span>document_id<span class="pl-pds">'</span></span>, document_id
      )
    )
  into result;

  return <span class="pl-k">null</span>;
end;
$$;

<span class="pl-k">create</span> <span class="pl-k">trigger</span> <span class="pl-en">on_file_upload</span>
  after insert <span class="pl-k">on</span> <span class="pl-c1">storage</span>.<span class="pl-c1">objects</span>
  for each row
  execute procedure <span class="pl-c1">private</span>.<span class="pl-c1">handle_storage_update</span>();</pre></div>
</li>
<li>
<p dir="auto">Apply the migration to our local database.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase migration up"><pre>npx supabase migration up</pre></div>
<p dir="auto">or if you are developing directly on the cloud, push your migrations up:</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="npx supabase db push"><pre class="notranslate"><code>npx supabase db push
</code></pre></div>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Edge function for <code>process</code></h4><a id="user-content-edge-function-for-process" class="anchor" aria-label="Permalink: Edge function for process" href="#edge-function-for-process"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>
<p dir="auto">Create the Edge Function file.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase functions new process"><pre>npx supabase functions new process</pre></div>
<p dir="auto">This will create the file <code>./supabase/functions/process/index.ts</code>.</p>
<p dir="auto">Make sure you have the latest version of <code>deno</code> installed</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="brew install deno"><pre>brew install deno</pre></div>
</li>
<li>
<p dir="auto">First let's note how dependencies are resolved using an import map - <code>./supabase/functions/import_map.json</code>.</p>
<p dir="auto">Import maps aren't required in Deno, but they can simplify imports and keep dependency versions consistent. All of our dependencies come from NPM, but since we're using Deno we fetch them from a CDN like <a href="https://esm.sh" rel="nofollow">https://esm.sh</a> or <a href="https://cdn.jsdelivr.net" rel="nofollow">https://cdn.jsdelivr.net</a>.</p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="{
  &quot;imports&quot;: {
    &quot;@std/&quot;: &quot;https://deno.land/std@0.168.0/&quot;,

    &quot;@supabase/supabase-js&quot;: &quot;https://esm.sh/@supabase/supabase-js@2.21.0&quot;,
    &quot;openai&quot;: &quot;https://esm.sh/openai@4.10.0&quot;,
    &quot;common-tags&quot;: &quot;https://esm.sh/common-tags@1.8.2&quot;,
    &quot;ai&quot;: &quot;https://esm.sh/ai@2.2.13&quot;,

    &quot;mdast-util-from-markdown&quot;: &quot;https://esm.sh/mdast-util-from-markdown@2.0.0&quot;,
    &quot;mdast-util-to-markdown&quot;: &quot;https://esm.sh/mdast-util-to-markdown@2.1.0&quot;,
    &quot;mdast-util-to-string&quot;: &quot;https://esm.sh/mdast-util-to-string@4.0.0&quot;,
    &quot;unist-builder&quot;: &quot;https://esm.sh/unist-builder@4.0.0&quot;,
    &quot;mdast&quot;: &quot;https://esm.sh/v132/@types/mdast@4.0.0/index.d.ts&quot;,

    &quot;https://esm.sh/v132/decode-named-character-reference@1.0.2/esnext/decode-named-character-reference.mjs&quot;: &quot;https://esm.sh/decode-named-character-reference@1.0.2?target=deno&quot;
  }
}"><pre>{
  <span class="pl-ent">"imports"</span>: {
    <span class="pl-ent">"@std/"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://deno.land/std@0.168.0/<span class="pl-pds">"</span></span>,

    <span class="pl-ent">"@supabase/supabase-js"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://esm.sh/@supabase/supabase-js@2.21.0<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"openai"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://esm.sh/openai@4.10.0<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"common-tags"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://esm.sh/common-tags@1.8.2<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"ai"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://esm.sh/ai@2.2.13<span class="pl-pds">"</span></span>,

    <span class="pl-ent">"mdast-util-from-markdown"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://esm.sh/mdast-util-from-markdown@2.0.0<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"mdast-util-to-markdown"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://esm.sh/mdast-util-to-markdown@2.1.0<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"mdast-util-to-string"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://esm.sh/mdast-util-to-string@4.0.0<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"unist-builder"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://esm.sh/unist-builder@4.0.0<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"mdast"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://esm.sh/v132/@types/mdast@4.0.0/index.d.ts<span class="pl-pds">"</span></span>,

    <span class="pl-ent">"https://esm.sh/v132/decode-named-character-reference@1.0.2/esnext/decode-named-character-reference.mjs"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://esm.sh/decode-named-character-reference@1.0.2?target=deno<span class="pl-pds">"</span></span>
  }
}</pre></div>
<p dir="auto"><em>Note: URL based imports and import maps aren't a Deno invention. These are a <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script/type/importmap" rel="nofollow">web standard</a> that Deno follows as closely as possible.</em></p>
</li>
<li>
<p dir="auto">In <code>process/index.ts</code>, first grab the Supabase environment variables.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import { createClient } from '@supabase/supabase-js';
import { processMarkdown } from '../_lib/markdown-parser.ts';

// These are automatically injected
const supabaseUrl = Deno.env.get('SUPABASE_URL');
const supabaseAnonKey = Deno.env.get('SUPABASE_ANON_KEY');

Deno.serve(async (req) =&gt; {
  if (!supabaseUrl || !supabaseAnonKey) {
    return new Response(
      JSON.stringify({
        error: 'Missing environment variables.',
      }),
      {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      }
    );
  }
});"><pre><span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-s1">createClient</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'@supabase/supabase-js'</span><span class="pl-kos">;</span>
<span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-s1">processMarkdown</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'../_lib/markdown-parser.ts'</span><span class="pl-kos">;</span>

<span class="pl-c">// These are automatically injected</span>
<span class="pl-k">const</span> <span class="pl-s1">supabaseUrl</span> <span class="pl-c1">=</span> <span class="pl-v">Deno</span><span class="pl-kos">.</span><span class="pl-c1">env</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">'SUPABASE_URL'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-k">const</span> <span class="pl-s1">supabaseAnonKey</span> <span class="pl-c1">=</span> <span class="pl-v">Deno</span><span class="pl-kos">.</span><span class="pl-c1">env</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">'SUPABASE_ANON_KEY'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-v">Deno</span><span class="pl-kos">.</span><span class="pl-en">serve</span><span class="pl-kos">(</span><span class="pl-k">async</span> <span class="pl-kos">(</span><span class="pl-s1">req</span><span class="pl-kos">)</span> <span class="pl-c1">=&gt;</span> <span class="pl-kos">{</span>
  <span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">supabaseUrl</span> <span class="pl-c1">||</span> <span class="pl-c1">!</span><span class="pl-s1">supabaseAnonKey</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span>
      <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
        <span class="pl-c1">error</span>: <span class="pl-s">'Missing environment variables.'</span><span class="pl-kos">,</span>
      <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
      <span class="pl-kos">{</span>
        <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
        <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
      <span class="pl-kos">}</span>
    <span class="pl-kos">)</span><span class="pl-kos">;</span>
  <span class="pl-kos">}</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
<p dir="auto"><em>Note: These environment variables are automatically injected into the edge runtime for you. Even so, we check for their existence as a TypeScript best practice (type narrowing).</em></p>
</li>
<li>
<p dir="auto"><em>(Optional)</em> If you are using VS Code, you may get prompted to cache your imported dependencies. You can do this by hitting <code>cmd</code>+<code>shift</code>+<code>p</code> and type <code>&gt;Deno: Cache Dependencies</code>.</p>
</li>
<li>
<p dir="auto">Create Supabase client and configure it to inherit the original user’s permissions via the authorization header. This way we can continue to take advantage of our RLS policies.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const authorization = req.headers.get('Authorization');

if (!authorization) {
  return new Response(
    JSON.stringify({ error: `No authorization header passed` }),
    {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    }
  );
}

const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  global: {
    headers: {
      authorization,
    },
  },
  auth: {
    persistSession: false,
  },
});"><pre><span class="pl-k">const</span> <span class="pl-s1">authorization</span> <span class="pl-c1">=</span> <span class="pl-s1">req</span><span class="pl-kos">.</span><span class="pl-c1">headers</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">'Authorization'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">authorization</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span>
    <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span> <span class="pl-c1">error</span>: <span class="pl-s">`No authorization header passed`</span> <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
    <span class="pl-kos">{</span>
      <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
      <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span>
  <span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span>

<span class="pl-k">const</span> <span class="pl-s1">supabase</span> <span class="pl-c1">=</span> <span class="pl-en">createClient</span><span class="pl-kos">(</span><span class="pl-s1">supabaseUrl</span><span class="pl-kos">,</span> <span class="pl-s1">supabaseAnonKey</span><span class="pl-kos">,</span> <span class="pl-kos">{</span>
  <span class="pl-c1">global</span>: <span class="pl-kos">{</span>
    <span class="pl-c1">headers</span>: <span class="pl-kos">{</span>
      authorization<span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">,</span>
  <span class="pl-c1">auth</span>: <span class="pl-kos">{</span>
    <span class="pl-c1">persistSession</span>: <span class="pl-c1">false</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">Grab the <code>document_id</code> from the request body and query it.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const { document_id } = await req.json();

const { data: document } = await supabase
  .from('documents_with_storage_path')
  .select()
  .eq('id', document_id)
  .single();

if (!document?.storage_object_path) {
  return new Response(
    JSON.stringify({ error: 'Failed to find uploaded document' }),
    {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    }
  );
}"><pre><span class="pl-k">const</span> <span class="pl-kos">{</span> document_id <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">req</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-kos">{</span> <span class="pl-c1">data</span>: <span class="pl-smi">document</span> <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">supabase</span>
  <span class="pl-kos">.</span><span class="pl-en">from</span><span class="pl-kos">(</span><span class="pl-s">'documents_with_storage_path'</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">select</span><span class="pl-kos">(</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">eq</span><span class="pl-kos">(</span><span class="pl-s">'id'</span><span class="pl-kos">,</span> <span class="pl-s1">document_id</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">single</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-smi">document</span><span class="pl-kos">?.</span><span class="pl-c1">storage_object_path</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span>
    <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span> <span class="pl-c1">error</span>: <span class="pl-s">'Failed to find uploaded document'</span> <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
    <span class="pl-kos">{</span>
      <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
      <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span>
  <span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span></pre></div>
</li>
<li>
<p dir="auto">Use the Supabase client to download the file by storage path.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const { data: file } = await supabase.storage
  .from('files')
  .download(document.storage_object_path);

if (!file) {
  return new Response(
    JSON.stringify({ error: 'Failed to download storage object' }),
    {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    }
  );
}

const fileContents = await file.text();"><pre><span class="pl-k">const</span> <span class="pl-kos">{</span> <span class="pl-c1">data</span>: <span class="pl-s1">file</span> <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">supabase</span><span class="pl-kos">.</span><span class="pl-c1">storage</span>
  <span class="pl-kos">.</span><span class="pl-en">from</span><span class="pl-kos">(</span><span class="pl-s">'files'</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">download</span><span class="pl-kos">(</span><span class="pl-smi">document</span><span class="pl-kos">.</span><span class="pl-c1">storage_object_path</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">file</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span>
    <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span> <span class="pl-c1">error</span>: <span class="pl-s">'Failed to download storage object'</span> <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
    <span class="pl-kos">{</span>
      <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
      <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span>
  <span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span>

<span class="pl-k">const</span> <span class="pl-s1">fileContents</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">file</span><span class="pl-kos">.</span><span class="pl-en">text</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">Process the markdown file and store the resulting subsections into the <code>document_sections</code> table.</p>
<p dir="auto"><em>Note: <code>processMarkdown()</code> is pre-built into this repository for convenience. Feel free to read through its code to learn how it splits the markdown content.</em></p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const processedMd = processMarkdown(fileContents);

const { error } = await supabase.from('document_sections').insert(
  processedMd.sections.map(({ content }) =&gt; ({
    document_id,
    content,
  }))
);

if (error) {
  console.error(error);
  return new Response(
    JSON.stringify({ error: 'Failed to save document sections' }),
    {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    }
  );
}

console.log(
  `Saved ${processedMd.sections.length} sections for file '${document.name}'`
);"><pre><span class="pl-k">const</span> <span class="pl-s1">processedMd</span> <span class="pl-c1">=</span> <span class="pl-en">processMarkdown</span><span class="pl-kos">(</span><span class="pl-s1">fileContents</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-kos">{</span> error <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">supabase</span><span class="pl-kos">.</span><span class="pl-en">from</span><span class="pl-kos">(</span><span class="pl-s">'document_sections'</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-en">insert</span><span class="pl-kos">(</span>
  <span class="pl-s1">processedMd</span><span class="pl-kos">.</span><span class="pl-c1">sections</span><span class="pl-kos">.</span><span class="pl-en">map</span><span class="pl-kos">(</span><span class="pl-kos">(</span><span class="pl-kos">{</span> content <span class="pl-kos">}</span><span class="pl-kos">)</span> <span class="pl-c1">=&gt;</span> <span class="pl-kos">(</span><span class="pl-kos">{</span>
    document_id<span class="pl-kos">,</span>
    content<span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">)</span>
<span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">error</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-smi">console</span><span class="pl-kos">.</span><span class="pl-en">error</span><span class="pl-kos">(</span><span class="pl-s1">error</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
  <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span>
    <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span> <span class="pl-c1">error</span>: <span class="pl-s">'Failed to save document sections'</span> <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
    <span class="pl-kos">{</span>
      <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
      <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span>
  <span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span>

<span class="pl-smi">console</span><span class="pl-kos">.</span><span class="pl-en">log</span><span class="pl-kos">(</span>
  <span class="pl-s">`Saved <span class="pl-s1"><span class="pl-kos">${</span><span class="pl-s1">processedMd</span><span class="pl-kos">.</span><span class="pl-c1">sections</span><span class="pl-kos">.</span><span class="pl-c1">length</span><span class="pl-kos">}</span></span> sections for file '<span class="pl-s1"><span class="pl-kos">${</span><span class="pl-smi">document</span><span class="pl-kos">.</span><span class="pl-c1">name</span><span class="pl-kos">}</span></span>'`</span>
<span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">Return a success response.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="return new Response(null, {
  status: 204,
  headers: { 'Content-Type': 'application/json' },
});"><pre><span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span><span class="pl-c1">null</span><span class="pl-kos">,</span> <span class="pl-kos">{</span>
  <span class="pl-c1">status</span>: <span class="pl-c1">204</span><span class="pl-kos">,</span>
  <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">If developing locally, open a new terminal and serve the edge functions.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase functions serve"><pre>npx supabase functions serve</pre></div>
<p dir="auto"><em>Note: Local Edge Functions are automatically served as part of <code>npx supabase start</code>, but this command allows us to also monitor their logs.</em></p>
<p dir="auto">If you're developing directly on the cloud, deploy your edge function:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase functions deploy"><pre>npx supabase functions deploy</pre></div>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Display documents on the frontend</h4><a id="user-content-display-documents-on-the-frontend" class="anchor" aria-label="Permalink: Display documents on the frontend" href="#display-documents-on-the-frontend"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Let's update <code>./app/files/page.tsx</code> to list out the uploaded documents.</p>
<ol dir="auto">
<li>
<p dir="auto">At the top of the component, fetch documents using the <code>useQuery</code> hook:</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const { data: documents } = useQuery(['files'], async () =&gt; {
  const { data, error } = await supabase
    .from('documents_with_storage_path')
    .select();

  if (error) {
    toast({
      variant: 'destructive',
      description: 'Failed to fetch documents',
    });
    throw error;
  }

  return data;
});"><pre><span class="pl-k">const</span> <span class="pl-kos">{</span> <span class="pl-c1">data</span>: <span class="pl-s1">documents</span> <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-en">useQuery</span><span class="pl-kos">(</span><span class="pl-kos">[</span><span class="pl-s">'files'</span><span class="pl-kos">]</span><span class="pl-kos">,</span> <span class="pl-k">async</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-c1">=&gt;</span> <span class="pl-kos">{</span>
  <span class="pl-k">const</span> <span class="pl-kos">{</span> data<span class="pl-kos">,</span> error <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">supabase</span>
    <span class="pl-kos">.</span><span class="pl-en">from</span><span class="pl-kos">(</span><span class="pl-s">'documents_with_storage_path'</span><span class="pl-kos">)</span>
    <span class="pl-kos">.</span><span class="pl-en">select</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

  <span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">error</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-en">toast</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
      <span class="pl-c1">variant</span>: <span class="pl-s">'destructive'</span><span class="pl-kos">,</span>
      <span class="pl-c1">description</span>: <span class="pl-s">'Failed to fetch documents'</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-k">throw</span> <span class="pl-s1">error</span><span class="pl-kos">;</span>
  <span class="pl-kos">}</span>

  <span class="pl-k">return</span> <span class="pl-s1">data</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">In each document's <code>onClick</code> handler, download the respective file.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const { data, error } = await supabase.storage
  .from('files')
  .createSignedUrl(document.storage_object_path, 60);

if (error) {
  toast({
    variant: 'destructive',
    description: 'Failed to download file. Please try again.',
  });
  return;
}

window.location.href = data.signedUrl;"><pre><span class="pl-k">const</span> <span class="pl-kos">{</span> data<span class="pl-kos">,</span> error <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">supabase</span><span class="pl-kos">.</span><span class="pl-c1">storage</span>
  <span class="pl-kos">.</span><span class="pl-en">from</span><span class="pl-kos">(</span><span class="pl-s">'files'</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">createSignedUrl</span><span class="pl-kos">(</span><span class="pl-smi">document</span><span class="pl-kos">.</span><span class="pl-c1">storage_object_path</span><span class="pl-kos">,</span> <span class="pl-c1">60</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">error</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-en">toast</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
    <span class="pl-c1">variant</span>: <span class="pl-s">'destructive'</span><span class="pl-kos">,</span>
    <span class="pl-c1">description</span>: <span class="pl-s">'Failed to download file. Please try again.'</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
  <span class="pl-k">return</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span>

<span class="pl-smi">window</span><span class="pl-kos">.</span><span class="pl-c1">location</span><span class="pl-kos">.</span><span class="pl-c1">href</span> <span class="pl-c1">=</span> <span class="pl-s1">data</span><span class="pl-kos">.</span><span class="pl-c1">signedUrl</span><span class="pl-kos">;</span></pre></div>
</li>
</ol>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><code>Step 3</code> - Embeddings</h3><a id="user-content-step-3---embeddings" class="anchor" aria-label="Permalink: Step 3 - Embeddings" href="#step-3---embeddings"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Jump to a step:</p>
<ol dir="auto">
<li><a href="#step-1---storage">Storage</a></li>
<li><a href="#step-2---documents">Documents</a></li>
<li><a href="#step-3---embeddings">Embeddings</a></li>
<li><a href="#step-4---chat">Chat</a></li>
<li><a href="#step-5---database-types-bonus">Database Types</a> (Bonus)</li>
<li><a href="#youre-done">You're done!</a></li>
</ol>
<hr>
<p dir="auto"><em>Use these commands to jump to the <code>step-3</code> checkpoint.</em></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="git stash push -u -m &quot;my work on step-2&quot;
git checkout step-3"><pre>git stash push -u -m <span class="pl-s"><span class="pl-pds">"</span>my work on step-2<span class="pl-pds">"</span></span>
git checkout step-3</pre></div>
<p dir="auto">Now let's add logic to generate embeddings automatically anytime new rows are added to the <code>document_sections</code> table.</p>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Create SQL migration</h4><a id="user-content-create-sql-migration" class="anchor" aria-label="Permalink: Create SQL migration" href="#create-sql-migration"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>
<p dir="auto">Create migration file</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase migration new embed"><pre>npx supabase migration new embed</pre></div>
</li>
<li>
<p dir="auto">Create <code>embed()</code> trigger function. We'll use this general purpose trigger function to asynchronously generate embeddings on arbitrary tables using a new <code>embed</code> Edge Function (coming up).</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create function private.embed()
returns trigger
language plpgsql
as $$
declare
  content_column text = TG_ARGV[0];
  embedding_column text = TG_ARGV[1];
  batch_size int = case when array_length(TG_ARGV, 1) &gt;= 3 then TG_ARGV[2]::int else 5 end;
  timeout_milliseconds int = case when array_length(TG_ARGV, 1) &gt;= 4 then TG_ARGV[3]::int else 5 * 60 * 1000 end;
  batch_count int = ceiling((select count(*) from inserted) / batch_size::float);
begin
  -- Loop through each batch and invoke an edge function to handle the embedding generation
  for i in 0 .. (batch_count-1) loop
  perform
    net.http_post(
      url := supabase_url() || '/functions/v1/embed',
      headers := jsonb_build_object(
        'Content-Type', 'application/json',
        'Authorization', current_setting('request.headers')::json-&gt;&gt;'authorization'
      ),
      body := jsonb_build_object(
        'ids', (select json_agg(ds.id) from (select id from inserted limit batch_size offset i*batch_size) ds),
        'table', TG_TABLE_NAME,
        'contentColumn', content_column,
        'embeddingColumn', embedding_column
      ),
      timeout_milliseconds := timeout_milliseconds
    );
  end loop;

  return null;
end;
$$;"><pre><span class="pl-k">create</span> <span class="pl-k">function</span> <span class="pl-en">private</span>.embed()
returns trigger
language plpgsql
<span class="pl-k">as</span> $$
declare
  content_column <span class="pl-k">text</span> <span class="pl-k">=</span> TG_ARGV[<span class="pl-c1">0</span>];
  embedding_column <span class="pl-k">text</span> <span class="pl-k">=</span> TG_ARGV[<span class="pl-c1">1</span>];
  batch_size <span class="pl-k">int</span> <span class="pl-k">=</span> case when array_length(TG_ARGV, <span class="pl-c1">1</span>) <span class="pl-k">&gt;=</span> <span class="pl-c1">3</span> then TG_ARGV[<span class="pl-c1">2</span>]::<span class="pl-k">int</span> else <span class="pl-c1">5</span> end;
  timeout_milliseconds <span class="pl-k">int</span> <span class="pl-k">=</span> case when array_length(TG_ARGV, <span class="pl-c1">1</span>) <span class="pl-k">&gt;=</span> <span class="pl-c1">4</span> then TG_ARGV[<span class="pl-c1">3</span>]::<span class="pl-k">int</span> else <span class="pl-c1">5</span> <span class="pl-k">*</span> <span class="pl-c1">60</span> <span class="pl-k">*</span> <span class="pl-c1">1000</span> end;
  batch_count <span class="pl-k">int</span> <span class="pl-k">=</span> ceiling((<span class="pl-k">select</span> <span class="pl-c1">count</span>(<span class="pl-k">*</span>) <span class="pl-k">from</span> inserted) <span class="pl-k">/</span> batch_size::float);
<span class="pl-k">begin</span>
  <span class="pl-c"><span class="pl-c">--</span> Loop through each batch and invoke an edge function to handle the embedding generation</span>
  for i <span class="pl-k">in</span> <span class="pl-c1">0</span> .. (batch_count<span class="pl-k">-</span><span class="pl-c1">1</span>) loop
  perform
    <span class="pl-c1">net</span>.<span class="pl-c1">http_post</span>(
      url :<span class="pl-k">=</span> supabase_url() <span class="pl-k">||</span> <span class="pl-s"><span class="pl-pds">'</span>/functions/v1/embed<span class="pl-pds">'</span></span>,
      headers :<span class="pl-k">=</span> jsonb_build_object(
        <span class="pl-s"><span class="pl-pds">'</span>Content-Type<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>application/json<span class="pl-pds">'</span></span>,
        <span class="pl-s"><span class="pl-pds">'</span>Authorization<span class="pl-pds">'</span></span>, current_setting(<span class="pl-s"><span class="pl-pds">'</span>request.headers<span class="pl-pds">'</span></span>)::json<span class="pl-k">-</span><span class="pl-k">&gt;&gt;</span><span class="pl-s"><span class="pl-pds">'</span>authorization<span class="pl-pds">'</span></span>
      ),
      body :<span class="pl-k">=</span> jsonb_build_object(
        <span class="pl-s"><span class="pl-pds">'</span>ids<span class="pl-pds">'</span></span>, (<span class="pl-k">select</span> json_agg(<span class="pl-c1">ds</span>.<span class="pl-c1">id</span>) <span class="pl-k">from</span> (<span class="pl-k">select</span> id <span class="pl-k">from</span> inserted <span class="pl-k">limit</span> batch_size offset i<span class="pl-k">*</span>batch_size) ds),
        <span class="pl-s"><span class="pl-pds">'</span>table<span class="pl-pds">'</span></span>, TG_TABLE_NAME,
        <span class="pl-s"><span class="pl-pds">'</span>contentColumn<span class="pl-pds">'</span></span>, content_column,
        <span class="pl-s"><span class="pl-pds">'</span>embeddingColumn<span class="pl-pds">'</span></span>, embedding_column
      ),
      timeout_milliseconds :<span class="pl-k">=</span> timeout_milliseconds
    );
  end loop;

  return <span class="pl-k">null</span>;
end;
$$;</pre></div>
</li>
<li>
<p dir="auto">Add embed trigger to <code>document_sections</code> table</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create trigger embed_document_sections
  after insert on document_sections
  referencing new table as inserted
  for each statement
  execute procedure private.embed(content, embedding);"><pre><span class="pl-k">create</span> <span class="pl-k">trigger</span> <span class="pl-en">embed_document_sections</span>
  after insert <span class="pl-k">on</span> document_sections
  referencing new table <span class="pl-k">as</span> inserted
  for each statement
  execute procedure <span class="pl-c1">private</span>.<span class="pl-c1">embed</span>(content, embedding);</pre></div>
<p dir="auto">Note we pass 2 trigger arguments to <code>embed()</code>:</p>
<ul dir="auto">
<li>The first specifies which column contains the text content to embed.</li>
<li>The second specifies the destination column to save the embedding into.</li>
</ul>
<p dir="auto">There are also 2 more optional trigger arguments available:</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create trigger embed_document_sections
  after insert on document_sections
  referencing new table as inserted
  for each statement
  execute procedure private.embed(content, embedding, 5, 300000);"><pre><span class="pl-k">create</span> <span class="pl-k">trigger</span> <span class="pl-en">embed_document_sections</span>
  after insert <span class="pl-k">on</span> document_sections
  referencing new table <span class="pl-k">as</span> inserted
  for each statement
  execute procedure <span class="pl-c1">private</span>.<span class="pl-c1">embed</span>(content, embedding, <span class="pl-c1">5</span>, <span class="pl-c1">300000</span>);</pre></div>
<ul dir="auto">
<li>The third argument specifies the batch size (number of records to include in each edge function call). Default is 5.</li>
<li>The fourth argument specifies the HTTP connection timeout for each edge function call. Default is 300000 ms (5 minutes).</li>
</ul>
<p dir="auto">Feel free to adjust these according to your needs. A larger batch size will require a longer timeout per request, since each invocation will have more embeddings to generate. A smaller batch size can use a lower timeout.</p>
<details>
<summary><i>Note: Lifecycle of triggered edge functions</i></summary>
If the triggered edge function fails, you will end up with
document sections missing embeddings. During development,
we can run `supabase db reset` to reset the database. In production,
some potential options are:
<ul dir="auto">
<li>Add another function that can be triggered manually which checks for <code>document_sections</code> with missing embeddings and invokes the <code>/embed</code> edge function for them.</li>
<li>Create a <a href="https://supabase.com/docs/guides/functions/schedule-functions" rel="nofollow">scheduled function</a> that periodically checks for <code>document_sections</code> with missing embeddings and re-generates them. We would likely need to add a locking mechanism (ie. via another column) to prevent the scheduled function from conflicting with the normal <code>embed</code> trigger.</li>
</ul>
</details>
</li>
<li>
<p dir="auto">Apply the migration to our local database.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase migration up"><pre>npx supabase migration up</pre></div>
<p dir="auto">or if you are developing directly on the cloud, push your migrations up:</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="npx supabase db push"><pre class="notranslate"><code>npx supabase db push
</code></pre></div>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Create Edge Function for <code>embed</code></h4><a id="user-content-create-edge-function-for-embed" class="anchor" aria-label="Permalink: Create Edge Function for embed" href="#create-edge-function-for-embed"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>
<p dir="auto">Create edge function file.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase functions new embed"><pre>npx supabase functions new embed</pre></div>
</li>
<li>
<p dir="auto">In <code>embed/index.ts</code>, create an inference session using Supabase's AI inference engine.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="// Setup type definitions for built-in Supabase Runtime APIs
/// &lt;reference types=&quot;https://esm.sh/@supabase/functions-js/src/edge-runtime.d.ts&quot; /&gt;

import { createClient } from '@supabase/supabase-js';

const model = new Supabase.ai.Session('gte-small');"><pre><span class="pl-c">// Setup type definitions for built-in Supabase Runtime APIs</span>
<span class="pl-c">/// &lt;reference types="https://esm.sh/@supabase/functions-js/src/edge-runtime.d.ts" /&gt;</span>

<span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-s1">createClient</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'@supabase/supabase-js'</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-s1">model</span> <span class="pl-c1">=</span> <span class="pl-k">new</span> <span class="pl-v">Supabase</span><span class="pl-kos">.</span><span class="pl-c1">ai</span><span class="pl-kos">.</span><span class="pl-c1">Session</span><span class="pl-kos">(</span><span class="pl-s">'gte-small'</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
<p dir="auto"><em>Note: The original code from the video tutorial used Transformers.js to perform inference in the Edge Function. We've since released <a href="https://supabase.com/docs/guides/functions/ai-models" rel="nofollow">Supabase.ai APIs</a> that can perform inference natively within the runtime itself (vs. WASM) which is faster and uses less CPU time.</em></p>
</li>
<li>
<p dir="auto">Just like before, grab the Supabase variables and check for their existence <em>(type narrowing)</em>.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="// These are automatically injected
const supabaseUrl = Deno.env.get('SUPABASE_URL');
const supabaseAnonKey = Deno.env.get('SUPABASE_ANON_KEY');

Deno.serve(async (req) =&gt; {
  if (!supabaseUrl || !supabaseAnonKey) {
    return new Response(
      JSON.stringify({
        error: 'Missing environment variables.',
      }),
      {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      }
    );
  }
});"><pre><span class="pl-c">// These are automatically injected</span>
<span class="pl-k">const</span> <span class="pl-s1">supabaseUrl</span> <span class="pl-c1">=</span> <span class="pl-v">Deno</span><span class="pl-kos">.</span><span class="pl-c1">env</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">'SUPABASE_URL'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-k">const</span> <span class="pl-s1">supabaseAnonKey</span> <span class="pl-c1">=</span> <span class="pl-v">Deno</span><span class="pl-kos">.</span><span class="pl-c1">env</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">'SUPABASE_ANON_KEY'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-v">Deno</span><span class="pl-kos">.</span><span class="pl-en">serve</span><span class="pl-kos">(</span><span class="pl-k">async</span> <span class="pl-kos">(</span><span class="pl-s1">req</span><span class="pl-kos">)</span> <span class="pl-c1">=&gt;</span> <span class="pl-kos">{</span>
  <span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">supabaseUrl</span> <span class="pl-c1">||</span> <span class="pl-c1">!</span><span class="pl-s1">supabaseAnonKey</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span>
      <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
        <span class="pl-c1">error</span>: <span class="pl-s">'Missing environment variables.'</span><span class="pl-kos">,</span>
      <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
      <span class="pl-kos">{</span>
        <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
        <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
      <span class="pl-kos">}</span>
    <span class="pl-kos">)</span><span class="pl-kos">;</span>
  <span class="pl-kos">}</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">Create a Supabase client and configure to inherit the user’s permissions.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const authorization = req.headers.get('Authorization');

if (!authorization) {
  return new Response(
    JSON.stringify({ error: `No authorization header passed` }),
    {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    }
  );
}

const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  global: {
    headers: {
      authorization,
    },
  },
  auth: {
    persistSession: false,
  },
});"><pre><span class="pl-k">const</span> <span class="pl-s1">authorization</span> <span class="pl-c1">=</span> <span class="pl-s1">req</span><span class="pl-kos">.</span><span class="pl-c1">headers</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">'Authorization'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">authorization</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span>
    <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span> <span class="pl-c1">error</span>: <span class="pl-s">`No authorization header passed`</span> <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
    <span class="pl-kos">{</span>
      <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
      <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span>
  <span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span>

<span class="pl-k">const</span> <span class="pl-s1">supabase</span> <span class="pl-c1">=</span> <span class="pl-en">createClient</span><span class="pl-kos">(</span><span class="pl-s1">supabaseUrl</span><span class="pl-kos">,</span> <span class="pl-s1">supabaseAnonKey</span><span class="pl-kos">,</span> <span class="pl-kos">{</span>
  <span class="pl-c1">global</span>: <span class="pl-kos">{</span>
    <span class="pl-c1">headers</span>: <span class="pl-kos">{</span>
      authorization<span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">,</span>
  <span class="pl-c1">auth</span>: <span class="pl-kos">{</span>
    <span class="pl-c1">persistSession</span>: <span class="pl-c1">false</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">Fetch the text content from the specified table/column.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const { ids, table, contentColumn, embeddingColumn } = await req.json();

const { data: rows, error: selectError } = await supabase
  .from(table)
  .select(`id, ${contentColumn}` as '*')
  .in('id', ids)
  .is(embeddingColumn, null);

if (selectError) {
  return new Response(JSON.stringify({ error: selectError }), {
    status: 500,
    headers: { 'Content-Type': 'application/json' },
  });
}"><pre><span class="pl-k">const</span> <span class="pl-kos">{</span> ids<span class="pl-kos">,</span> table<span class="pl-kos">,</span> contentColumn<span class="pl-kos">,</span> embeddingColumn <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">req</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-kos">{</span> <span class="pl-c1">data</span>: <span class="pl-s1">rows</span><span class="pl-kos">,</span> <span class="pl-c1">error</span>: <span class="pl-s1">selectError</span> <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">supabase</span>
  <span class="pl-kos">.</span><span class="pl-en">from</span><span class="pl-kos">(</span><span class="pl-s1">table</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">select</span><span class="pl-kos">(</span><span class="pl-s">`id, <span class="pl-s1"><span class="pl-kos">${</span><span class="pl-s1">contentColumn</span><span class="pl-kos">}</span></span>`</span> <span class="pl-k">as</span> <span class="pl-s">'*'</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">in</span><span class="pl-kos">(</span><span class="pl-s">'id'</span><span class="pl-kos">,</span> <span class="pl-s1">ids</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">is</span><span class="pl-kos">(</span><span class="pl-s1">embeddingColumn</span><span class="pl-kos">,</span> <span class="pl-c1">null</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">selectError</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span><span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span> <span class="pl-c1">error</span>: <span class="pl-s1">selectError</span> <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span> <span class="pl-kos">{</span>
    <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
    <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span></pre></div>
</li>
<li>
<p dir="auto">Generate an embedding for each piece of text and update the respective rows.</p>
<div class="highlight highlight-source-ts notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="for (const row of rows) {
  const { id, [contentColumn]: content } = row;

  if (!content) {
    console.error(`No content available in column '${contentColumn}'`);
    continue;
  }

  const output = (await model.run(content, {
    mean_pool: true,
    normalize: true,
  })) as number[];

  const embedding = JSON.stringify(output);

  const { error } = await supabase
    .from(table)
    .update({
      [embeddingColumn]: embedding,
    })
    .eq('id', id);

  if (error) {
    console.error(
      `Failed to save embedding on '${table}' table with id ${id}`
    );
  }

  console.log(
    `Generated embedding ${JSON.stringify({
      table,
      id,
      contentColumn,
      embeddingColumn,
    })}`
  );
}"><pre><span class="pl-k">for</span> <span class="pl-kos">(</span><span class="pl-k">const</span> <span class="pl-s1">row</span> <span class="pl-k">of</span> <span class="pl-s1">rows</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-k">const</span> <span class="pl-kos">{</span> id<span class="pl-kos">,</span> <span class="pl-kos">[</span><span class="pl-s1">contentColumn</span><span class="pl-kos">]</span>: <span class="pl-s1">content</span> <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-s1">row</span><span class="pl-kos">;</span>

  <span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">content</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-smi">console</span><span class="pl-kos">.</span><span class="pl-en">error</span><span class="pl-kos">(</span><span class="pl-s">`No content available in column '<span class="pl-s1"><span class="pl-kos">${</span><span class="pl-s1">contentColumn</span><span class="pl-kos">}</span></span>'`</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-k">continue</span><span class="pl-kos">;</span>
  <span class="pl-kos">}</span>

  <span class="pl-k">const</span> <span class="pl-s1">output</span> <span class="pl-c1">=</span> <span class="pl-kos">(</span><span class="pl-k">await</span> <span class="pl-s1">model</span><span class="pl-kos">.</span><span class="pl-en">run</span><span class="pl-kos">(</span><span class="pl-s1">content</span><span class="pl-kos">,</span> <span class="pl-kos">{</span>
    <span class="pl-c1">mean_pool</span>: <span class="pl-c1">true</span><span class="pl-kos">,</span>
    <span class="pl-c1">normalize</span>: <span class="pl-c1">true</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">)</span> <span class="pl-k">as</span> <span class="pl-smi">number</span><span class="pl-kos">[</span><span class="pl-kos">]</span><span class="pl-kos">;</span>

  <span class="pl-k">const</span> <span class="pl-s1">embedding</span> <span class="pl-c1">=</span> <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-s1">output</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

  <span class="pl-k">const</span> <span class="pl-kos">{</span> error <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">supabase</span>
    <span class="pl-kos">.</span><span class="pl-en">from</span><span class="pl-kos">(</span><span class="pl-s1">table</span><span class="pl-kos">)</span>
    <span class="pl-kos">.</span><span class="pl-en">update</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
      <span class="pl-kos">[</span><span class="pl-s1">embeddingColumn</span><span class="pl-kos">]</span>: <span class="pl-s1">embedding</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">)</span>
    <span class="pl-kos">.</span><span class="pl-en">eq</span><span class="pl-kos">(</span><span class="pl-s">'id'</span><span class="pl-kos">,</span> <span class="pl-s1">id</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

  <span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">error</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-smi">console</span><span class="pl-kos">.</span><span class="pl-en">error</span><span class="pl-kos">(</span>
      <span class="pl-s">`Failed to save embedding on '<span class="pl-s1"><span class="pl-kos">${</span><span class="pl-s1">table</span><span class="pl-kos">}</span></span>' table with id <span class="pl-s1"><span class="pl-kos">${</span><span class="pl-s1">id</span><span class="pl-kos">}</span></span>`</span>
    <span class="pl-kos">)</span><span class="pl-kos">;</span>
  <span class="pl-kos">}</span>

  <span class="pl-smi">console</span><span class="pl-kos">.</span><span class="pl-en">log</span><span class="pl-kos">(</span>
    <span class="pl-s">`Generated embedding <span class="pl-s1"><span class="pl-kos">${</span><span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span></span></span>
<span class="pl-s"><span class="pl-s1">      table<span class="pl-kos">,</span></span></span>
<span class="pl-s"><span class="pl-s1">      id<span class="pl-kos">,</span></span></span>
<span class="pl-s"><span class="pl-s1">      contentColumn<span class="pl-kos">,</span></span></span>
<span class="pl-s"><span class="pl-s1">      embeddingColumn<span class="pl-kos">,</span></span></span>
<span class="pl-s"><span class="pl-s1">    <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">}</span></span>`</span>
  <span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span></pre></div>
</li>
<li>
<p dir="auto">Return a success response.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="return new Response(null, {
  status: 204,
  headers: { 'Content-Type': 'application/json' },
});"><pre><span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span><span class="pl-c1">null</span><span class="pl-kos">,</span> <span class="pl-kos">{</span>
  <span class="pl-c1">status</span>: <span class="pl-c1">204</span><span class="pl-kos">,</span>
  <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">If you're developing directly on the cloud, deploy your edge function:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase functions deploy"><pre>npx supabase functions deploy</pre></div>
</li>
</ol>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><code>Step 4</code> - Chat</h3><a id="user-content-step-4---chat" class="anchor" aria-label="Permalink: Step 4 - Chat" href="#step-4---chat"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Jump to a step:</p>
<ol dir="auto">
<li><a href="#step-1---storage">Storage</a></li>
<li><a href="#step-2---documents">Documents</a></li>
<li><a href="#step-3---embeddings">Embeddings</a></li>
<li><a href="#step-4---chat">Chat</a></li>
<li><a href="#step-5---database-types-bonus">Database Types</a> (Bonus)</li>
<li><a href="#youre-done">You're done!</a></li>
</ol>
<hr>
<p dir="auto"><em>Use these commands to jump to the <code>step-4</code> checkpoint.</em></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="git stash push -u -m &quot;my work on step-3&quot;
git checkout step-4"><pre>git stash push -u -m <span class="pl-s"><span class="pl-pds">"</span>my work on step-3<span class="pl-pds">"</span></span>
git checkout step-4</pre></div>
<p dir="auto">Finally, let's implement the chat functionality. For this workshop, we're going to generate our query embedding client side using a new custom hook called <code>usePipeline()</code>.</p>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Update Frontend</h4><a id="user-content-update-frontend" class="anchor" aria-label="Permalink: Update Frontend" href="#update-frontend"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>
<p dir="auto">Install dependencies</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npm i @xenova/transformers ai"><pre>npm i @xenova/transformers ai</pre></div>
<p dir="auto">We'll use <a href="https://github.com/xenova/transformers.js">Transformers.js</a> to perform inference directly in the browser.</p>
</li>
<li>
<p dir="auto">Configure <code>next.config.js</code> to support Transformers.js</p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="  webpack: (config) =&gt; {
    config.resolve.alias = {
      ...config.resolve.alias,
      sharp$: false,
      'onnxruntime-node$': false,
    };
    return config;
  },"><pre>  <span class="pl-s1">webpack</span>: <span class="pl-kos">(</span><span class="pl-s1">config</span><span class="pl-kos">)</span> <span class="pl-c1">=&gt;</span> <span class="pl-kos">{</span>
    <span class="pl-s1">config</span><span class="pl-kos">.</span><span class="pl-c1">resolve</span><span class="pl-kos">.</span><span class="pl-c1">alias</span> <span class="pl-c1">=</span> <span class="pl-kos">{</span>
      ...<span class="pl-s1">config</span><span class="pl-kos">.</span><span class="pl-c1">resolve</span><span class="pl-kos">.</span><span class="pl-c1">alias</span><span class="pl-kos">,</span>
      <span class="pl-c1">sharp$</span>: <span class="pl-c1">false</span><span class="pl-kos">,</span>
      <span class="pl-s">'onnxruntime-node$'</span>: <span class="pl-c1">false</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">;</span>
    <span class="pl-k">return</span> <span class="pl-s1">config</span><span class="pl-kos">;</span>
  <span class="pl-kos">}</span><span class="pl-kos">,</span></pre></div>
</li>
<li>
<p dir="auto">Import dependencies</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import { usePipeline } from '@/lib/hooks/use-pipeline';
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs';
import { useChat } from 'ai/react';"><pre><span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-s1">usePipeline</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'@/lib/hooks/use-pipeline'</span><span class="pl-kos">;</span>
<span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-s1">createClientComponentClient</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'@supabase/auth-helpers-nextjs'</span><span class="pl-kos">;</span>
<span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-s1">useChat</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'ai/react'</span><span class="pl-kos">;</span></pre></div>
<p dir="auto"><em>Note: <code>usePipeline()</code> was pre-built into this repository for convenience. It uses Web Workers to asynchronously generate embeddings in another thread using Transformers.js.</em></p>
</li>
<li>
<p dir="auto">Create a Supabase client in <code>chat/page.tsx</code>.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const supabase = createClientComponentClient();"><pre><span class="pl-k">const</span> <span class="pl-s1">supabase</span> <span class="pl-c1">=</span> <span class="pl-en">createClientComponentClient</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">Create embedding pipeline.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const generateEmbedding = usePipeline(
  'feature-extraction',
  'Supabase/gte-small'
);"><pre><span class="pl-k">const</span> <span class="pl-s1">generateEmbedding</span> <span class="pl-c1">=</span> <span class="pl-en">usePipeline</span><span class="pl-kos">(</span>
  <span class="pl-s">'feature-extraction'</span><span class="pl-kos">,</span>
  <span class="pl-s">'Supabase/gte-small'</span>
<span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
<p dir="auto"><em>Note: it's important that the embedding model you set here matches the model used in the Edge Function, otherwise your future matching logic will be meaningless.</em></p>
<p dir="auto"><em>Transformers.js requires models to exist in the ONNX format. Specifically
the Hugging Face model you specify in the pipeline must have an <code>.onnx</code> file
under the <code>./onnx</code> folder, otherwise you will see the error
<code>Could not locate file [...] xxx.onnx</code>. Check out
<a href="https://www.youtube.com/watch?v=QdDoFfkVkcw&amp;t=3825s" rel="nofollow">this explanation</a> for more details.
To convert an existing model (eg. PyTorch, Tensorflow, etc) to ONNX, see
the <a href="https://huggingface.co/docs/transformers.js/en/custom_usage#convert-your-models-to-onnx" rel="nofollow">custom usage documentation</a>.</em></p>
</li>
<li>
<p dir="auto">Manage chat messages and state with <code>useChat()</code>.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const { messages, input, handleInputChange, handleSubmit, isLoading } =
  useChat({
    api: `${process.env.NEXT_PUBLIC_SUPABASE_URL}/functions/v1/chat`,
  });"><pre><span class="pl-k">const</span> <span class="pl-kos">{</span> messages<span class="pl-kos">,</span> input<span class="pl-kos">,</span> handleInputChange<span class="pl-kos">,</span> handleSubmit<span class="pl-kos">,</span> isLoading <span class="pl-kos">}</span> <span class="pl-c1">=</span>
  <span class="pl-en">useChat</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
    <span class="pl-c1">api</span>: <span class="pl-s">`<span class="pl-s1"><span class="pl-kos">${</span><span class="pl-s1">process</span><span class="pl-kos">.</span><span class="pl-c1">env</span><span class="pl-kos">.</span><span class="pl-c1">NEXT_PUBLIC_SUPABASE_URL</span><span class="pl-kos">}</span></span>/functions/v1/chat`</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
<p dir="auto"><em>Note: <code>useChat()</code> is a convenience hook provided by Vercel's <code>ai</code> package to handle chat message state and streaming. We'll point it to an Edge Function called <code>chat</code> (coming up).</em></p>
</li>
<li>
<p dir="auto">Set the ready status to <code>true</code> when pipeline has loaded.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const isReady = !!generateEmbedding;"><pre><span class="pl-k">const</span> <span class="pl-s1">isReady</span> <span class="pl-c1">=</span> <span class="pl-c1">!</span><span class="pl-c1">!</span><span class="pl-s1">generateEmbedding</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">Connect <code>input</code> and <code>handleInputChange</code> to our <code>&lt;Input&gt;</code> props.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="&lt;Input
  type=&quot;text&quot;
  autoFocus
  placeholder=&quot;Send a message&quot;
  value={input}
  onChange={handleInputChange}
/&gt;"><pre><span class="pl-c1">&lt;</span><span class="pl-v">Input</span>
  <span class="pl-c1">type</span><span class="pl-c1">=</span><span class="pl-s">"text"</span>
  <span class="pl-c1">autoFocus</span>
  <span class="pl-c1">placeholder</span><span class="pl-c1">=</span><span class="pl-s">"Send a message"</span>
  <span class="pl-c1">value</span><span class="pl-c1">=</span><span class="pl-kos">{</span><span class="pl-s1">input</span><span class="pl-kos">}</span>
  <span class="pl-c1">onChange</span><span class="pl-c1">=</span><span class="pl-kos">{</span><span class="pl-s1">handleInputChange</span><span class="pl-kos">}</span>
<span class="pl-kos">/&gt;</span></pre></div>
</li>
<li>
<p dir="auto">Generate an embedding and submit messages on form submit.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="if (!generateEmbedding) {
  throw new Error('Unable to generate embeddings');
}

const output = await generateEmbedding(input, {
  pooling: 'mean',
  normalize: true,
});

const embedding = JSON.stringify(Array.from(output.data));

const {
  data: { session },
} = await supabase.auth.getSession();

if (!session) {
  return;
}

handleSubmit(e, {
  options: {
    headers: {
      authorization: `Bearer ${session.access_token}`,
    },
    body: {
      embedding,
    },
  },
});"><pre><span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">generateEmbedding</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-k">throw</span> <span class="pl-k">new</span> <span class="pl-v">Error</span><span class="pl-kos">(</span><span class="pl-s">'Unable to generate embeddings'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span>

<span class="pl-k">const</span> <span class="pl-s1">output</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-en">generateEmbedding</span><span class="pl-kos">(</span><span class="pl-s1">input</span><span class="pl-kos">,</span> <span class="pl-kos">{</span>
  <span class="pl-c1">pooling</span>: <span class="pl-s">'mean'</span><span class="pl-kos">,</span>
  <span class="pl-c1">normalize</span>: <span class="pl-c1">true</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-s1">embedding</span> <span class="pl-c1">=</span> <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-v">Array</span><span class="pl-kos">.</span><span class="pl-en">from</span><span class="pl-kos">(</span><span class="pl-s1">output</span><span class="pl-kos">.</span><span class="pl-c1">data</span><span class="pl-kos">)</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-kos">{</span>
  <span class="pl-c1">data</span>: <span class="pl-kos">{</span> session <span class="pl-kos">}</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">supabase</span><span class="pl-kos">.</span><span class="pl-c1">auth</span><span class="pl-kos">.</span><span class="pl-en">getSession</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">session</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-k">return</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span>

<span class="pl-en">handleSubmit</span><span class="pl-kos">(</span><span class="pl-s1">e</span><span class="pl-kos">,</span> <span class="pl-kos">{</span>
  <span class="pl-c1">options</span>: <span class="pl-kos">{</span>
    <span class="pl-c1">headers</span>: <span class="pl-kos">{</span>
      <span class="pl-c1">authorization</span>: <span class="pl-s">`Bearer <span class="pl-s1"><span class="pl-kos">${</span><span class="pl-s1">session</span><span class="pl-kos">.</span><span class="pl-c1">access_token</span><span class="pl-kos">}</span></span>`</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">,</span>
    <span class="pl-c1">body</span>: <span class="pl-kos">{</span>
      embedding<span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">Disable send button until the component is ready.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="&lt;Button type=&quot;submit&quot; disabled={!isReady}&gt;
  Send
&lt;/Button&gt;"><pre><span class="pl-c1">&lt;</span><span class="pl-v">Button</span> <span class="pl-c1">type</span><span class="pl-c1">=</span><span class="pl-s">"submit"</span> <span class="pl-c1">disabled</span><span class="pl-c1">=</span><span class="pl-kos">{</span><span class="pl-c1">!</span><span class="pl-s1">isReady</span><span class="pl-kos">}</span><span class="pl-c1">&gt;</span>
  Send
<span class="pl-kos">&lt;/</span><span class="pl-v">Button</span><span class="pl-c1">&gt;</span></pre></div>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">SQL Migration</h4><a id="user-content-sql-migration" class="anchor" aria-label="Permalink: SQL Migration" href="#sql-migration"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>
<p dir="auto">Create migration file for a new match function</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase migration new match"><pre>npx supabase migration new match</pre></div>
</li>
<li>
<p dir="auto">Create a <code>match_document_sections</code> Postgres function.</p>
<div class="highlight highlight-source-sql notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="create or replace function match_document_sections(
  embedding vector(384),
  match_threshold float
)
returns setof document_sections
language plpgsql
as $$
#variable_conflict use_variable
begin
  return query
  select *
  from document_sections
  where document_sections.embedding &lt;#&gt; embedding &lt; -match_threshold
	order by document_sections.embedding &lt;#&gt; embedding;
end;
$$;"><pre><span class="pl-k">create or replace</span> <span class="pl-k">function</span> <span class="pl-en">match_document_sections</span>(
  embedding vector(<span class="pl-c1">384</span>),
  match_threshold float
)
returns setof document_sections
language plpgsql
<span class="pl-k">as</span> $$
<span class="pl-c"><span class="pl-c">#</span>variable_conflict use_variable</span>
<span class="pl-k">begin</span>
  return query
  <span class="pl-k">select</span> <span class="pl-k">*</span>
  <span class="pl-k">from</span> document_sections
  <span class="pl-k">where</span> <span class="pl-c1">document_sections</span>.<span class="pl-c1">embedding</span> <span class="pl-k">&lt;</span><span class="pl-c"><span class="pl-c">#</span>&gt; embedding &lt; -match_threshold</span>
	<span class="pl-k">order by</span> <span class="pl-c1">document_sections</span>.<span class="pl-c1">embedding</span> <span class="pl-k">&lt;</span><span class="pl-c"><span class="pl-c">#</span>&gt; embedding;</span>
end;
$$;</pre></div>
<p dir="auto">This function uses pgvector's negative inner product operator <code>&lt;#&gt;</code> to perform similarity search. Inner product requires less computations than other distance functions like cosine distance <code>&lt;=&gt;</code>, and therefore provides better query performance.</p>
<p dir="auto"><em>Note: Our embeddings are normalized, so inner product and cosine similarity are equivalent in terms of output. Note though that pgvector's <code>&lt;=&gt;</code> operator is cosine distance, not cosine similarity, so <code>inner product == 1 - cosine distance</code>.</em></p>
<p dir="auto">We also filter by a <code>match_threshold</code> in order to return only the most relevant results (1 = most similar, -1 = most dissimilar).</p>
<p dir="auto"><em>Note: <code>match_threshold</code> is negated because <code>&lt;#&gt;</code> is a negative inner product. See the pgvector docs for more details on why <code>&lt;#&gt;</code> is negative.</em></p>
</li>
<li>
<p dir="auto">Apply the migration to our local database.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase migration up"><pre>npx supabase migration up</pre></div>
<p dir="auto">or if you are developing directly on the cloud, push your migrations up:</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="npx supabase db push"><pre class="notranslate"><code>npx supabase db push
</code></pre></div>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Create <code>chat</code> Edge Function</h4><a id="user-content-create-chat-edge-function" class="anchor" aria-label="Permalink: Create chat Edge Function" href="#create-chat-edge-function"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Note:</strong> In this tutorial we use models provided by OpenAI to implement the chat logic.
However since making this tutorial, many new LLM providers exist, such as:</p>
<ul dir="auto">
<li><a href="https://docs.together.ai/docs/openai-api-compatibility#nodejs" rel="nofollow">together.ai</a></li>
<li><a href="https://readme.fireworks.ai/docs/openai-compatibility" rel="nofollow">fireworks.ai</a></li>
<li><a href="https://docs.endpoints.anyscale.com/examples/work-with-openai/" rel="nofollow">endpoints.anyscale.com</a></li>
<li><a href="https://github.com/ollama/ollama/blob/main/docs/openai.md#openai-javascript-library">local models served with Ollama</a></li>
</ul>
<p dir="auto">Whichever provider you choose, you can reuse the code below (that uses the OpenAI lib) as long as they offer an OpenAI-compatible API <em>(all of providers listed above do)</em>. We'll discuss how to do this in each step using Ollama, but the same logic applies to the other providers.</p>
<ol dir="auto">
<li>
<p dir="auto">First generate an API key from <a href="https://platform.openai.com/account/api-keys" rel="nofollow">OpenAI</a> and save it in <code>supabase/functions/.env</code>.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="cat &gt; supabase/functions/.env &lt;&lt;- EOF
OPENAI_API_KEY=&lt;your-api-key&gt;
EOF"><pre>cat <span class="pl-k">&gt;</span> supabase/functions/.env <span class="pl-s"><span class="pl-k">&lt;&lt;</span>- <span class="pl-k">EOF</span></span>
<span class="pl-s">OPENAI_API_KEY=&lt;your-api-key&gt;</span>
<span class="pl-s"><span class="pl-k">EOF</span></span></pre></div>
</li>
<li>
<p dir="auto">Create the edge function file.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase functions new chat"><pre>npx supabase functions new chat</pre></div>
</li>
<li>
<p dir="auto">Load the OpenAI and Supabase keys.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import { createClient } from '@supabase/supabase-js';
import { OpenAIStream, StreamingTextResponse } from 'ai';
import { codeBlock } from 'common-tags';
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: Deno.env.get('OPENAI_API_KEY'),
});

// These are automatically injected
const supabaseUrl = Deno.env.get('SUPABASE_URL');
const supabaseAnonKey = Deno.env.get('SUPABASE_ANON_KEY');"><pre><span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-s1">createClient</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'@supabase/supabase-js'</span><span class="pl-kos">;</span>
<span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-v">OpenAIStream</span><span class="pl-kos">,</span> <span class="pl-v">StreamingTextResponse</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'ai'</span><span class="pl-kos">;</span>
<span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-s1">codeBlock</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'common-tags'</span><span class="pl-kos">;</span>
<span class="pl-k">import</span> <span class="pl-v">OpenAI</span> <span class="pl-k">from</span> <span class="pl-s">'openai'</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-s1">openai</span> <span class="pl-c1">=</span> <span class="pl-k">new</span> <span class="pl-v">OpenAI</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
  <span class="pl-c1">apiKey</span>: <span class="pl-v">Deno</span><span class="pl-kos">.</span><span class="pl-c1">env</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">'OPENAI_API_KEY'</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-c">// These are automatically injected</span>
<span class="pl-k">const</span> <span class="pl-s1">supabaseUrl</span> <span class="pl-c1">=</span> <span class="pl-v">Deno</span><span class="pl-kos">.</span><span class="pl-c1">env</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">'SUPABASE_URL'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-k">const</span> <span class="pl-s1">supabaseAnonKey</span> <span class="pl-c1">=</span> <span class="pl-v">Deno</span><span class="pl-kos">.</span><span class="pl-c1">env</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">'SUPABASE_ANON_KEY'</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
<details>
<summary><i>Note: Ollama support</i></summary>
<p dir="auto">For Ollama (and other OpenAI-compatible providers), adjust the <code>baseURL</code> and <code>apiKey</code> when instantiating <code>openai</code>:</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const openai = new OpenAI({
  baseURL: 'http://host.docker.internal:11434/v1/',
  apiKey: 'ollama',
});"><pre><span class="pl-k">const</span> <span class="pl-s1">openai</span> <span class="pl-c1">=</span> <span class="pl-k">new</span> <span class="pl-v">OpenAI</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
  <span class="pl-c1">baseURL</span>: <span class="pl-s">'http://host.docker.internal:11434/v1/'</span><span class="pl-kos">,</span>
  <span class="pl-c1">apiKey</span>: <span class="pl-s">'ollama'</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
<p dir="auto">We assume here that you're running <code>ollama serve</code> locally
with the default port <code>:11434</code>.
Since local edge functions run inside a Docker container,
we specify <code>host.docker.internal</code> instead of <code>localhost</code>
in order to reach Ollama running on your host.</p>
</details>
</li>
<li>
<p dir="auto">Since our frontend is served at a different domain origin than our Edge Function, we must handle cross origin resource sharing (CORS).</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="export const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers':
    'authorization, x-client-info, apikey, content-type',
};

Deno.serve(async (req) =&gt; {
  // Handle CORS
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders });
  }
});"><pre><span class="pl-k">export</span> <span class="pl-k">const</span> <span class="pl-s1">corsHeaders</span> <span class="pl-c1">=</span> <span class="pl-kos">{</span>
  <span class="pl-s">'Access-Control-Allow-Origin'</span>: <span class="pl-s">'*'</span><span class="pl-kos">,</span>
  <span class="pl-s">'Access-Control-Allow-Headers'</span>:
    <span class="pl-s">'authorization, x-client-info, apikey, content-type'</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">;</span>

<span class="pl-v">Deno</span><span class="pl-kos">.</span><span class="pl-en">serve</span><span class="pl-kos">(</span><span class="pl-k">async</span> <span class="pl-kos">(</span><span class="pl-s1">req</span><span class="pl-kos">)</span> <span class="pl-c1">=&gt;</span> <span class="pl-kos">{</span>
  <span class="pl-c">// Handle CORS</span>
  <span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">req</span><span class="pl-kos">.</span><span class="pl-c1">method</span> <span class="pl-c1">===</span> <span class="pl-s">'OPTIONS'</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span><span class="pl-s">'ok'</span><span class="pl-kos">,</span> <span class="pl-kos">{</span> <span class="pl-c1">headers</span>: <span class="pl-s1">corsHeaders</span> <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
  <span class="pl-kos">}</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
<p dir="auto">Handle CORS simply by checking for an <code>OPTIONS</code> HTTP request and returning the CORS headers (<code>*</code> = allow any domain). In production, consider limiting the origins to specific domains that serve your frontend.</p>
</li>
<li>
<p dir="auto">Check for environment variables and create Supabase client.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="if (!supabaseUrl || !supabaseAnonKey) {
  return new Response(
    JSON.stringify({
      error: 'Missing environment variables.',
    }),
    {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    }
  );
}

const authorization = req.headers.get('Authorization');

if (!authorization) {
  return new Response(
    JSON.stringify({ error: `No authorization header passed` }),
    {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    }
  );
}

const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  global: {
    headers: {
      authorization,
    },
  },
  auth: {
    persistSession: false,
  },
});"><pre><span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">supabaseUrl</span> <span class="pl-c1">||</span> <span class="pl-c1">!</span><span class="pl-s1">supabaseAnonKey</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span>
    <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
      <span class="pl-c1">error</span>: <span class="pl-s">'Missing environment variables.'</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
    <span class="pl-kos">{</span>
      <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
      <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span>
  <span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span>

<span class="pl-k">const</span> <span class="pl-s1">authorization</span> <span class="pl-c1">=</span> <span class="pl-s1">req</span><span class="pl-kos">.</span><span class="pl-c1">headers</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">'Authorization'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">authorization</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span>
    <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span> <span class="pl-c1">error</span>: <span class="pl-s">`No authorization header passed`</span> <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
    <span class="pl-kos">{</span>
      <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
      <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span>
  <span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span>

<span class="pl-k">const</span> <span class="pl-s1">supabase</span> <span class="pl-c1">=</span> <span class="pl-en">createClient</span><span class="pl-kos">(</span><span class="pl-s1">supabaseUrl</span><span class="pl-kos">,</span> <span class="pl-s1">supabaseAnonKey</span><span class="pl-kos">,</span> <span class="pl-kos">{</span>
  <span class="pl-c1">global</span>: <span class="pl-kos">{</span>
    <span class="pl-c1">headers</span>: <span class="pl-kos">{</span>
      authorization<span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">,</span>
  <span class="pl-c1">auth</span>: <span class="pl-kos">{</span>
    <span class="pl-c1">persistSession</span>: <span class="pl-c1">false</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">The first step of RAG is to perform similarity search using our <code>match_document_sections()</code> function. Postgres functions are executed using the <code>.rpc()</code> method.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const { chatId, message, messages, embedding } = await req.json();

const { data: documents, error: matchError } = await supabase
  .rpc('match_document_sections', {
    embedding,
    match_threshold: 0.8,
  })
  .select('content')
  .limit(5);

if (matchError) {
  console.error(matchError);

  return new Response(
    JSON.stringify({
      error: 'There was an error reading your documents, please try again.',
    }),
    {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    }
  );
}"><pre><span class="pl-k">const</span> <span class="pl-kos">{</span> chatId<span class="pl-kos">,</span> message<span class="pl-kos">,</span> messages<span class="pl-kos">,</span> embedding <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">req</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-kos">{</span> <span class="pl-c1">data</span>: <span class="pl-s1">documents</span><span class="pl-kos">,</span> <span class="pl-c1">error</span>: <span class="pl-s1">matchError</span> <span class="pl-kos">}</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">supabase</span>
  <span class="pl-kos">.</span><span class="pl-en">rpc</span><span class="pl-kos">(</span><span class="pl-s">'match_document_sections'</span><span class="pl-kos">,</span> <span class="pl-kos">{</span>
    embedding<span class="pl-kos">,</span>
    <span class="pl-c1">match_threshold</span>: <span class="pl-c1">0.8</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">select</span><span class="pl-kos">(</span><span class="pl-s">'content'</span><span class="pl-kos">)</span>
  <span class="pl-kos">.</span><span class="pl-en">limit</span><span class="pl-kos">(</span><span class="pl-c1">5</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">matchError</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-smi">console</span><span class="pl-kos">.</span><span class="pl-en">error</span><span class="pl-kos">(</span><span class="pl-s1">matchError</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

  <span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">Response</span><span class="pl-kos">(</span>
    <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
      <span class="pl-c1">error</span>: <span class="pl-s">'There was an error reading your documents, please try again.'</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">,</span>
    <span class="pl-kos">{</span>
      <span class="pl-c1">status</span>: <span class="pl-c1">500</span><span class="pl-kos">,</span>
      <span class="pl-c1">headers</span>: <span class="pl-kos">{</span> <span class="pl-s">'Content-Type'</span>: <span class="pl-s">'application/json'</span> <span class="pl-kos">}</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span>
  <span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span></pre></div>
</li>
<li>
<p dir="auto">The second step of RAG is to build our prompt, injecting in the relevant documents retrieved from our previous similarity search.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const injectedDocs =
  documents &amp;&amp; documents.length &gt; 0
    ? documents.map(({ content }) =&gt; content).join('\n\n')
    : 'No documents found';

const completionMessages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] =
  [
    {
      role: 'user',
      content: codeBlock`
          You're an AI assistant who answers questions about documents.

          You're a chat bot, so keep your replies succinct.

          You're only allowed to use the documents below to answer the question.

          If the question isn't related to these documents, say:
          &quot;Sorry, I couldn't find any information on that.&quot;

          If the information isn't available in the below documents, say:
          &quot;Sorry, I couldn't find any information on that.&quot;

          Do not go off topic.

          Documents:
          ${injectedDocs}
        `,
    },
    ...messages,
  ];"><pre><span class="pl-k">const</span> <span class="pl-s1">injectedDocs</span> <span class="pl-c1">=</span>
  <span class="pl-s1">documents</span> <span class="pl-c1">&amp;&amp;</span> <span class="pl-s1">documents</span><span class="pl-kos">.</span><span class="pl-c1">length</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span>
    ? <span class="pl-s1">documents</span><span class="pl-kos">.</span><span class="pl-en">map</span><span class="pl-kos">(</span><span class="pl-kos">(</span><span class="pl-kos">{</span> content <span class="pl-kos">}</span><span class="pl-kos">)</span> <span class="pl-c1">=&gt;</span> <span class="pl-s1">content</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-en">join</span><span class="pl-kos">(</span><span class="pl-s">'\n\n'</span><span class="pl-kos">)</span>
    : <span class="pl-s">'No documents found'</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-s1">completionMessages</span>: <span class="pl-v">OpenAI</span><span class="pl-kos">.</span><span class="pl-c1">Chat</span><span class="pl-kos">.</span><span class="pl-c1">Completions</span><span class="pl-kos">.</span><span class="pl-smi">ChatCompletionMessageParam</span><span class="pl-kos">[</span><span class="pl-kos">]</span> <span class="pl-c1">=</span>
  <span class="pl-kos">[</span>
    <span class="pl-kos">{</span>
      <span class="pl-c1">role</span>: <span class="pl-s">'user'</span><span class="pl-kos">,</span>
      <span class="pl-c1">content</span>: <span class="pl-en">codeBlock</span><span class="pl-s">`</span>
<span class="pl-s">          You're an AI assistant who answers questions about documents.</span>
<span class="pl-s"></span>
<span class="pl-s">          You're a chat bot, so keep your replies succinct.</span>
<span class="pl-s"></span>
<span class="pl-s">          You're only allowed to use the documents below to answer the question.</span>
<span class="pl-s"></span>
<span class="pl-s">          If the question isn't related to these documents, say:</span>
<span class="pl-s">          "Sorry, I couldn't find any information on that."</span>
<span class="pl-s"></span>
<span class="pl-s">          If the information isn't available in the below documents, say:</span>
<span class="pl-s">          "Sorry, I couldn't find any information on that."</span>
<span class="pl-s"></span>
<span class="pl-s">          Do not go off topic.</span>
<span class="pl-s"></span>
<span class="pl-s">          Documents:</span>
<span class="pl-s">          <span class="pl-s1"><span class="pl-kos">${</span><span class="pl-s1">injectedDocs</span><span class="pl-kos">}</span></span></span>
<span class="pl-s">        `</span><span class="pl-kos">,</span>
    <span class="pl-kos">}</span><span class="pl-kos">,</span>
    ...<span class="pl-s1">messages</span><span class="pl-kos">,</span>
  <span class="pl-kos">]</span><span class="pl-kos">;</span></pre></div>
<p dir="auto"><em>Note: the <code>codeBlock</code> template tag is a convenience function that will strip away indentations in our multiline string. This allows us to format our code nicely while preserving the intended indentation.</em></p>
</li>
<li>
<p dir="auto">Finally, create a completion stream and return it.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="const completionStream = await openai.chat.completions.create({
  model: 'gpt-3.5-turbo-0125',
  messages: completionMessages,
  max_tokens: 1024,
  temperature: 0,
  stream: true,
});

const stream = OpenAIStream(completionStream);
return new StreamingTextResponse(stream, { headers: corsHeaders });"><pre><span class="pl-k">const</span> <span class="pl-s1">completionStream</span> <span class="pl-c1">=</span> <span class="pl-k">await</span> <span class="pl-s1">openai</span><span class="pl-kos">.</span><span class="pl-c1">chat</span><span class="pl-kos">.</span><span class="pl-c1">completions</span><span class="pl-kos">.</span><span class="pl-en">create</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
  <span class="pl-c1">model</span>: <span class="pl-s">'gpt-3.5-turbo-0125'</span><span class="pl-kos">,</span>
  <span class="pl-c1">messages</span>: <span class="pl-s1">completionMessages</span><span class="pl-kos">,</span>
  <span class="pl-c1">max_tokens</span>: <span class="pl-c1">1024</span><span class="pl-kos">,</span>
  <span class="pl-c1">temperature</span>: <span class="pl-c1">0</span><span class="pl-kos">,</span>
  <span class="pl-c1">stream</span>: <span class="pl-c1">true</span><span class="pl-kos">,</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-s1">stream</span> <span class="pl-c1">=</span> <span class="pl-v">OpenAIStream</span><span class="pl-kos">(</span><span class="pl-s1">completionStream</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-k">return</span> <span class="pl-k">new</span> <span class="pl-v">StreamingTextResponse</span><span class="pl-kos">(</span><span class="pl-s1">stream</span><span class="pl-kos">,</span> <span class="pl-kos">{</span> <span class="pl-c1">headers</span>: <span class="pl-s1">corsHeaders</span> <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
<p dir="auto"><code>OpenAIStream</code> and <code>StreamingTextResponse</code> are convenience helpers from Vercel's <code>ai</code> package that translate OpenAI's response stream into a format that <code>useChat()</code> understands on the frontend.</p>
<p dir="auto"><em>Note: we must also return CORS headers here (or anywhere else we send a response).</em></p>
<details>
<summary><i>Note: Ollama support</i></summary>
Change the model to a model you're serving locally, for example:
<div class="highlight highlight-source-diff notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="-     model: 'gpt-3.5-turbo-0125',
+     model: 'dolphin-mistral',"><pre><span class="pl-md"><span class="pl-md">-</span>     model: 'gpt-3.5-turbo-0125',</span>
<span class="pl-mi1"><span class="pl-mi1">+</span>     model: 'dolphin-mistral',</span></pre></div>
</details>
</li>
<li>
<p dir="auto">If you're developing directly on the cloud, set your <code>OPENAI_API_KEY</code> secret in the cloud:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase secrets set OPENAI_API_KEY=&lt;openai-key&gt;"><pre>npx supabase secrets <span class="pl-c1">set</span> OPENAI_API_KEY=<span class="pl-k">&lt;</span>openai-key<span class="pl-k">&gt;</span></pre></div>
<p dir="auto">Then deploy your edge function:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase functions deploy"><pre>npx supabase functions deploy</pre></div>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">Try it!</h4><a id="user-content-try-it" class="anchor" aria-label="Permalink: Try it!" href="#try-it"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Let's try it out! Here are some questions you could try asking:</p>
<ul dir="auto">
<li>What kind of buildings did they live in?</li>
<li>What was the most common food?</li>
<li>What did people do for fun?</li>
</ul>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><code>Step 5</code> - Database Types (Bonus)</h3><a id="user-content-step-5---database-types-bonus" class="anchor" aria-label="Permalink: Step 5 - Database Types (Bonus)" href="#step-5---database-types-bonus"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Jump to a step:</p>
<ol dir="auto">
<li><a href="#step-1---storage">Storage</a></li>
<li><a href="#step-2---documents">Documents</a></li>
<li><a href="#step-3---embeddings">Embeddings</a></li>
<li><a href="#step-4---chat">Chat</a></li>
<li><a href="#step-5---database-types-bonus">Database Types</a> (Bonus)</li>
<li><a href="#youre-done">You're done!</a></li>
</ol>
<hr>
<p dir="auto"><em>Use these commands to jump to the <code>step-5</code> checkpoint.</em></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="git stash push -u -m &quot;my work on step-4&quot;
git checkout step-5"><pre>git stash push -u -m <span class="pl-s"><span class="pl-pds">"</span>my work on step-4<span class="pl-pds">"</span></span>
git checkout step-5</pre></div>
<p dir="auto">You may have noticed that all of our DB data coming back from the <code>supabase</code> client has had an <code>any</code> type (such as <code>documents</code> or <code>document_sections</code>). This isn't great, since we're missing relevant type information and lose type safety <em>(making our app more error-prone)</em>.</p>
<p dir="auto">The Supabase CLI comes with a built-in command to generate TypeScript types based on your database's schema.</p>
<ol dir="auto">
<li>
<p dir="auto">Generate TypeScript types based on local DB schema.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="supabase gen types typescript --local &gt; supabase/functions/_lib/database.ts"><pre>supabase gen types typescript --local <span class="pl-k">&gt;</span> supabase/functions/_lib/database.ts</pre></div>
</li>
<li>
<p dir="auto">Add the <code>&lt;Database&gt;</code> generic to all Supabase clients across our project.</p>
<ol dir="auto">
<li>
<p dir="auto">In React</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import { Database } from '@/supabase/functions/_lib/database';

const supabase = createClientComponentClient&lt;Database&gt;();"><pre><span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-v">Database</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'@/supabase/functions/_lib/database'</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-s1">supabase</span> <span class="pl-c1">=</span> <span class="pl-en">createClientComponentClient</span><span class="pl-c1">&lt;</span><span class="pl-smi">Database</span><span class="pl-c1">&gt;</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import { Database } from '@/supabase/functions/_lib/database';

const supabase = createServerComponentClient&lt;Database&gt;();"><pre><span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-v">Database</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'@/supabase/functions/_lib/database'</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-s1">supabase</span> <span class="pl-c1">=</span> <span class="pl-en">createServerComponentClient</span><span class="pl-c1">&lt;</span><span class="pl-smi">Database</span><span class="pl-c1">&gt;</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
<li>
<p dir="auto">In Edge Functions</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="import { Database } from '../_lib/database.ts';

const supabase = createClient&lt;Database&gt;(...);"><pre><span class="pl-k">import</span> <span class="pl-kos">{</span> <span class="pl-v">Database</span> <span class="pl-kos">}</span> <span class="pl-k">from</span> <span class="pl-s">'../_lib/database.ts'</span><span class="pl-kos">;</span>

<span class="pl-k">const</span> <span class="pl-s1">supabase</span> <span class="pl-c1">=</span> <span class="pl-en">createClient</span><span class="pl-c1">&lt;</span><span class="pl-smi">Database</span><span class="pl-c1">&gt;</span><span class="pl-kos">(</span>...<span class="pl-kos">)</span><span class="pl-kos">;</span></pre></div>
</li>
</ol>
</li>
<li>
<p dir="auto">Fix type errors 😃</p>
<ol dir="auto">
<li>
<p dir="auto">Looks like we found a type error in <code>./app/files/page.tsx</code>! Let's add this check to top of the document's click handler <em>(type narrowing)</em>.</p>
<div class="highlight highlight-source-tsx notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="if (!document.storage_object_path) {
  toast({
    variant: 'destructive',
    description: 'Failed to download file, please try again.',
  });
  return;
}"><pre><span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-smi">document</span><span class="pl-kos">.</span><span class="pl-c1">storage_object_path</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
  <span class="pl-en">toast</span><span class="pl-kos">(</span><span class="pl-kos">{</span>
    <span class="pl-c1">variant</span>: <span class="pl-s">'destructive'</span><span class="pl-kos">,</span>
    <span class="pl-c1">description</span>: <span class="pl-s">'Failed to download file, please try again.'</span><span class="pl-kos">,</span>
  <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
  <span class="pl-k">return</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span></pre></div>
</li>
</ol>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">You're done!</h3><a id="user-content-youre-done" class="anchor" aria-label="Permalink: You're done!" href="#youre-done"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">🎉 Congrats! You've built your own full stack pgvector app in 2 hours.</p>
<p dir="auto">If you would like to jump directly to the completed app, simply checkout the <code>main</code> branch:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="git checkout main"><pre>git checkout main</pre></div>
<p dir="auto">Jump to a previous step:</p>
<ol dir="auto">
<li><a href="#step-1---storage">Storage</a></li>
<li><a href="#step-2---documents">Documents</a></li>
<li><a href="#step-3---embeddings">Embeddings</a></li>
<li><a href="#step-4---chat">Chat</a></li>
<li><a href="#step-5---database-types-bonus">Database Types</a> (Bonus)</li>
<li><a href="#youre-done">You're done!</a></li>
</ol>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🚀 Going to prod</h2><a id="user-content--going-to-prod" class="anchor" aria-label="Permalink: 🚀 Going to prod" href="#-going-to-prod"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">If you've been developing the app locally, follow these instructions to deploy your app to a production Supabase project.</p>
<ol dir="auto">
<li>
<p dir="auto">Create a Supabase project at <a href="https://database.new" rel="nofollow">https://database.new</a>, or via the CLI:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase projects create -i &quot;ChatGPT Your Files&quot;"><pre>npx supabase projects create -i <span class="pl-s"><span class="pl-pds">"</span>ChatGPT Your Files<span class="pl-pds">"</span></span></pre></div>
</li>
<li>
<p dir="auto">Link the CLI with your Supabase project.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase link --project-ref=&lt;project-ref&gt;"><pre>npx supabase link --project-ref=<span class="pl-k">&lt;</span>project-ref<span class="pl-k">&gt;</span></pre></div>
<p dir="auto">You can grab your project's reference ID in your <a href="https://supabase.com/dashboard/project/_/settings/general" rel="nofollow">project’s settings</a>.</p>
</li>
<li>
<p dir="auto">Push migrations to remote database.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase db push"><pre>npx supabase db push</pre></div>
</li>
<li>
<p dir="auto">Set Edge Function secrets (OpenAI key).</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase secrets set OPENAI_API_KEY=&lt;openai-key&gt;"><pre>npx supabase secrets <span class="pl-c1">set</span> OPENAI_API_KEY=<span class="pl-k">&lt;</span>openai-key<span class="pl-k">&gt;</span></pre></div>
</li>
<li>
<p dir="auto">Deploy Edge Functions.</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="npx supabase functions deploy"><pre>npx supabase functions deploy</pre></div>
</li>
<li>
<p dir="auto">Deploy to Vercel <em>(or CDN of your choice - must support Next.js API routes for authentication)</em>.</p>
<ul dir="auto">
<li>
<p dir="auto">Follow Vercel’s <a href="https://nextjs.org/docs/app/getting-started/deploying" rel="nofollow">deploy instructions</a>.</p>
</li>
<li>
<p dir="auto">Be sure to set <code>NEXT_PUBLIC_SUPABASE_URL</code> and <code>NEXT_PUBLIC_SUPABASE_ANON_KEY</code> for your Supabase project.</p>
<p dir="auto">You can find these in your <a href="https://supabase.com/dashboard/project/_/settings/api" rel="nofollow">project’s API settings</a>.</p>
</li>
</ul>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">📈 Next steps</h2><a id="user-content--next-steps" class="anchor" aria-label="Permalink: 📈 Next steps" href="#-next-steps"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Feel free to extend this app in any way you like. Here are some ideas for next steps:</p>
<ul dir="auto">
<li>Record message history in the database (and generate embeddings on them for RAG memory)</li>
<li>Support more file formats than just markdown</li>
<li>Pull in documents from the Notion API</li>
<li>Restrict chat to user-selected documents</li>
<li>Perform RAG on images using CLIP embeddings</li>
</ul>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">💬 Feedback and issues</h2><a id="user-content--feedback-and-issues" class="anchor" aria-label="Permalink: 💬 Feedback and issues" href="#-feedback-and-issues"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Please file feedback and issues on the <a href="https://github.com/supabase-community/chatgpt-your-files/issues/new/choose">on this repo's issue board</a>.</p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🔗 Supabase Vector resources</h2><a id="user-content--supabase-vector-resources" class="anchor" aria-label="Permalink: 🔗 Supabase Vector resources" href="#-supabase-vector-resources"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li><a href="https://supabase.com/docs/guides/ai" rel="nofollow">Supabase AI &amp; Vector</a></li>
<li><a href="https://supabase.com/docs/guides/ai/vector-columns" rel="nofollow">pgvector Columns</a></li>
<li><a href="https://supabase.com/docs/guides/ai/vector-indexes" rel="nofollow">pgvector Indexes</a></li>
<li><a href="https://supabase.com/docs/guides/ai/quickstarts/generate-text-embeddings" rel="nofollow">Generate Embeddings using Edge Functions</a></li>
<li><a href="https://supabase.com/docs/guides/ai/going-to-prod" rel="nofollow">Going to Production</a></li>
</ul>
</article></div></div></div></div></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA_:R0:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


      <input type="hidden" data-csrf="true" value="9kj+FF44pc+gbwCRBP/GuFDpPN9irpNG2Cr+hpfIhUmiC8JHLlLyMMC2hYlua7plqGF6pQTj8UJR1wUyXi6uLA==" />
</div>
  <div data-view-component="true" class="Layout-sidebar">      

      <div class="BorderGrid about-margin" data-pjax>
        <div class="BorderGrid-row">
          <div class="BorderGrid-cell">
            <div class="hide-sm hide-md">
  <h2 class="mb-3 h4">About</h2>

      <p class="f4 my-3">
        Production-ready MVP for securely chatting with your documents using pgvector
      </p>
      <div class="my-3 d-flex flex-items-center">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link flex-shrink-0 mr-2">
    <path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path>
</svg>
        <span class="flex-auto min-width-0 css-truncate css-truncate-target width-fit">
          <a title="https://youtu.be/ibzlEQmgPPY" role="link" target="_blank" rel="noopener noreferrer nofollow" class="text-bold" href="https://youtu.be/ibzlEQmgPPY">youtu.be/ibzlEQmgPPY</a>
        </span>
      </div>

    <h3 class="sr-only">Topics</h3>
    <div class="my-3">
        <div class="f6">
      <a href="/topics/ai" title="Topic: ai" data-view-component="true" class="topic-tag topic-tag-link">
  ai
</a>
      <a href="/topics/vector" title="Topic: vector" data-view-component="true" class="topic-tag topic-tag-link">
  vector
</a>
      <a href="/topics/ml" title="Topic: ml" data-view-component="true" class="topic-tag topic-tag-link">
  ml
</a>
      <a href="/topics/embeddings" title="Topic: embeddings" data-view-component="true" class="topic-tag topic-tag-link">
  embeddings
</a>
      <a href="/topics/db" title="Topic: db" data-view-component="true" class="topic-tag topic-tag-link">
  db
</a>
      <a href="/topics/rag" title="Topic: rag" data-view-component="true" class="topic-tag topic-tag-link">
  rag
</a>
      <a href="/topics/supabase" title="Topic: supabase" data-view-component="true" class="topic-tag topic-tag-link">
  supabase
</a>
  </div>

    </div>

    <h3 class="sr-only">Resources</h3>
    <div class="mt-2">
      <a class="Link--muted" data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:readme&quot;}" href="#readme-ov-file">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book mr-2">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        Readme
</a>    </div>

  

    <h3 class="sr-only">Code of conduct</h3>
    <div class="mt-2">
      <a href="#coc-ov-file"
        class="Link--muted"
        
        data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:code of conduct&quot;}"
      >
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-of-conduct mr-2">
    <path d="M8.048 2.241c.964-.709 2.079-1.238 3.325-1.241a4.616 4.616 0 0 1 3.282 1.355c.41.408.757.86.996 1.428.238.568.348 1.206.347 1.968 0 2.193-1.505 4.254-3.081 5.862-1.496 1.526-3.213 2.796-4.249 3.563l-.22.163a.749.749 0 0 1-.895 0l-.221-.163c-1.036-.767-2.753-2.037-4.249-3.563C1.51 10.008.007 7.952.002 5.762a4.614 4.614 0 0 1 1.353-3.407C3.123.585 6.223.537 8.048 2.24Zm-1.153.983c-1.25-1.033-3.321-.967-4.48.191a3.115 3.115 0 0 0-.913 2.335c0 1.556 1.109 3.24 2.652 4.813C5.463 11.898 6.96 13.032 8 13.805c.353-.262.758-.565 1.191-.905l-1.326-1.223a.75.75 0 0 1 1.018-1.102l1.48 1.366c.328-.281.659-.577.984-.887L9.99 9.802a.75.75 0 1 1 1.019-1.103l1.384 1.28c.295-.329.566-.661.81-.995L12.92 8.7l-1.167-1.168c-.674-.671-1.78-.664-2.474.03-.268.269-.538.537-.802.797-.893.882-2.319.843-3.185-.032-.346-.35-.693-.697-1.043-1.047a.75.75 0 0 1-.04-1.016c.162-.191.336-.401.52-.623.62-.748 1.356-1.637 2.166-2.417Zm7.112 4.442c.313-.65.491-1.293.491-1.916v-.001c0-.614-.088-1.045-.23-1.385-.143-.339-.357-.633-.673-.949a3.111 3.111 0 0 0-2.218-.915c-1.092.003-2.165.627-3.226 1.602-.823.755-1.554 1.637-2.228 2.45l-.127.154.562.566a.755.755 0 0 0 1.066.02l.794-.79c1.258-1.258 3.312-1.31 4.594-.032.396.394.792.791 1.173 1.173Z"></path>
</svg>
        Code of conduct
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


  <include-fragment src="/supabase-community/chatgpt-your-files/hovercards/citation/sidebar_partial?tree_name=main" data-nonce="v2:fc902795-443c-4768-14bd-518a2dc3c13e" data-view-component="true">
  

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
    <div class="mt-2">
      <a href="/supabase-community/chatgpt-your-files/activity" data-view-component="true" class="Link Link--muted"><svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pulse mr-2">
    <path d="M6 2c.306 0 .582.187.696.471L10 10.731l1.304-3.26A.751.751 0 0 1 12 7h3.25a.75.75 0 0 1 0 1.5h-2.742l-1.812 4.528a.751.751 0 0 1-1.392 0L6 4.77 4.696 8.03A.75.75 0 0 1 4 8.5H.75a.75.75 0 0 1 0-1.5h2.742l1.812-4.529A.751.751 0 0 1 6 2Z"></path>
</svg>
        <span class="color-fg-muted">Activity</span></a>    </div>

    <div class="mt-2">
      <a href="/supabase-community/chatgpt-your-files/custom-properties" data-view-component="true" class="Link Link--muted"><svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-note mr-2">
    <path d="M0 3.75C0 2.784.784 2 1.75 2h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14H1.75A1.75 1.75 0 0 1 0 12.25Zm1.75-.25a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25ZM3.5 6.25a.75.75 0 0 1 .75-.75h7a.75.75 0 0 1 0 1.5h-7a.75.75 0 0 1-.75-.75Zm.75 2.25h4a.75.75 0 0 1 0 1.5h-4a.75.75 0 0 1 0-1.5Z"></path>
</svg>
        <span class="color-fg-muted">Custom properties</span></a>    </div>

    <h3 class="sr-only">Stars</h3>
    <div class="mt-2">
      <a href="/supabase-community/chatgpt-your-files/stargazers" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        <strong>507</strong>
        stars</a>    </div>

    <h3 class="sr-only">Watchers</h3>
    <div class="mt-2">
      <a href="/supabase-community/chatgpt-your-files/watchers" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye mr-2">
    <path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path>
</svg>
        <strong>12</strong>
        watching</a>    </div>

    <h3 class="sr-only">Forks</h3>
    <div class="mt-2">
      <a href="/supabase-community/chatgpt-your-files/forks" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
        <strong>193</strong>
        forks</a>    </div>


    <div class="mt-2">
      <a class="Link--muted" href="/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fsupabase-community%2Fchatgpt-your-files&amp;report=supabase-community+%28user%29">
          Report repository
</a>    </div>
</div>

          </div>
        </div>

        
            <div class="BorderGrid-row">
              <div class="BorderGrid-cell">
                <h2 class="h4 mb-3" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
  <a href="/supabase-community/chatgpt-your-files/releases" data-view-component="true" class="Link--primary no-underline Link">Releases</a></h2>

    <a class="Link--primary no-underline" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/supabase-community/chatgpt-your-files/tags">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tag color-fg-muted">
    <path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path>
</svg>
      <span class="text-bold">6</span>
      <span class="color-fg-muted">tags</span>
</a>
              </div>
            </div>

        
        
            <div class="BorderGrid-row">
              <div class="BorderGrid-cell">
                
  <h2 class="h4 mb-3">
  <a href="/orgs/supabase-community/packages?repo_name=chatgpt-your-files" data-view-component="true" class="Link--primary no-underline Link d-flex flex-items-center">Packages
      <span title="0" hidden="hidden" data-view-component="true" class="Counter ml-1">0</span></a></h2>


      <div class="text-small color-fg-muted" >
        No packages published <br>
      </div>



              </div>
            </div>

        
            <div class="BorderGrid-row" hidden>
              <div class="BorderGrid-cell">
                <include-fragment src="/supabase-community/chatgpt-your-files/used_by_list" accept="text/fragment+html" data-nonce="v2:fc902795-443c-4768-14bd-518a2dc3c13e" data-view-component="true">
  

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
              </div>
            </div>

        
            <div class="BorderGrid-row">
              <div class="BorderGrid-cell">
                <h2 class="h4 mb-3">
  <a href="/supabase-community/chatgpt-your-files/graphs/contributors" data-view-component="true" class="Link--primary no-underline Link d-flex flex-items-center">Contributors
      <span title="6" data-view-component="true" class="Counter ml-1">6</span></a></h2>


    <include-fragment aria-busy="true" aria-label="Loading contributors" src="/supabase-community/chatgpt-your-files/contributors_list?count=6&amp;current_repository=chatgpt-your-files&amp;items_to_show=6" data-nonce="v2:fc902795-443c-4768-14bd-518a2dc3c13e" data-view-component="true">
  
      <ul class="list-style-none d-flex flex-wrap mb-n2">
          <li class="mb-2 ">
            <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
          </li>
          <li class="mb-2 ">
            <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
          </li>
          <li class="mb-2 ">
            <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
          </li>
          <li class="mb-2 ">
            <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
          </li>
          <li class="mb-2 ">
            <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
          </li>
          <li class="mb-2 ">
            <div class="Skeleton avatar avatar-user mr-2" style="width:32px;height:32px;"></div>
          </li>
      </ul>

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


              </div>
            </div>

        
        
            <div class="BorderGrid-row">
              <div class="BorderGrid-cell">
                <h2 class="h4 mb-3">Languages</h2>
<div class="mb-2">
  <span data-view-component="true" class="Progress">
    <span style="background-color:#3178c6 !important;;width: 85.8%;" itemprop="keywords" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
    <span style="background-color:#336790 !important;;width: 9.2%;" itemprop="keywords" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
    <span style="background-color:#f1e05a !important;;width: 3.1%;" itemprop="keywords" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
    <span style="background-color:#663399 !important;;width: 1.9%;" itemprop="keywords" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
</span></div>
<ul class="list-style-none">
    <li class="d-inline">
        <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3" href="/supabase-community/chatgpt-your-files/search?l=typescript"  data-ga-click="Repository, language stats search click, location:repo overview">
          <svg style="color:#3178c6;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
          <span class="color-fg-default text-bold mr-1">TypeScript</span>
          <span>85.8%</span>
        </a>
    </li>
    <li class="d-inline">
        <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3" href="/supabase-community/chatgpt-your-files/search?l=plpgsql"  data-ga-click="Repository, language stats search click, location:repo overview">
          <svg style="color:#336790;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
          <span class="color-fg-default text-bold mr-1">PLpgSQL</span>
          <span>9.2%</span>
        </a>
    </li>
    <li class="d-inline">
        <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3" href="/supabase-community/chatgpt-your-files/search?l=javascript"  data-ga-click="Repository, language stats search click, location:repo overview">
          <svg style="color:#f1e05a;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
          <span class="color-fg-default text-bold mr-1">JavaScript</span>
          <span>3.1%</span>
        </a>
    </li>
    <li class="d-inline">
        <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3" href="/supabase-community/chatgpt-your-files/search?l=css"  data-ga-click="Repository, language stats search click, location:repo overview">
          <svg style="color:#663399;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
          <span class="color-fg-default text-bold mr-1">CSS</span>
          <span>1.9%</span>
        </a>
    </li>
</ul>

              </div>
            </div>

              </div>
</div>
  
</div></div>

  </div>


  </div>

</turbo-frame>


    </main>
  </div>

  </div>

          <footer class="footer pt-7 pb-6 f6 color-fg-muted color-border-subtle p-responsive" role="contentinfo" >
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


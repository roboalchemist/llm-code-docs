# Source: https://docs.envzero.com/changelogs/2025/06/polish-improvements-june-2025.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ✨ Polish & Improvements: June 2025

We’ve continued to roll out improvements focused on streamlining workflows, resolving common issues, and refining the experience, driven by user feedback. Here’s a brief overview of the latest updates.

## Environment Output Variables in Workflow Templates

You can now more effectively define variable dependencies within Workflows using **Environment Outputs** and **Workflow Templates**. This enhancement lets you use outputs as inputs within the same workflow, making it easier to configure reusable Workflows across different environments.\
To learn more visit our docs: [Workflow Variables](/guides/admin-guide/variables/workflow-variables) and [Environment Outputs](/guides/admin-guide/variables/environment-outputs).

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/06/workflow_template_configuration_showing_environment_output_variables_and_dependencies.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=d637bf83b73743f66607d051bba8e785" alt="Workflow template configuration showing environment output variables and dependencies" width="2704" height="1322" data-path="images/changelogs/2025/06/workflow_template_configuration_showing_environment_output_variables_and_dependencies.png" />
</Frame>

## Audit Log Forwarding

You can now forward env zero Audit Logs to supported observability tools. This update introduces a new configuration interface under the **Integrations** page, allowing you to connect both Deployment Logs and Audit Logs to any of the available integrations. [Learn more](/guides/integrations/logs-forwarding)

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/06/integrations_page_showing_audit_log_forwarding_configuration_options.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=b6f34c1850fb414a6b243f244328ec39" alt="Integrations page showing audit log forwarding configuration options" width="3456" height="1844" data-path="images/changelogs/2025/06/integrations_page_showing_audit_log_forwarding_configuration_options.png" />
</Frame>

## Plugin Caching for Self-Hosted Agents

Customers using the Self-Hosted Agent can now boost deployment performance with our new plugin cache. This feature stores previously downloaded provider plugins on a persistent volume, enabling reuse across runs within the same environment. [Learn more](/guides/admin-guide/self-hosted-kubernetes-agent/cache-with-pvc)

## Project Level Credentials

Credentials management is now more flexible with the introduction of **Project-level credentials**. You can add credentials directly in a Project’s settings, and they will be scoped *exclusively* to that project and its child projects.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/06/project-level_credentials_configuration_interface_in_project_settings.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=fd3edbd63aa7f8cd9a8b21a2a6c6fae0" alt="Project-level credentials configuration interface in project settings" width="1032" height="1378" data-path="images/changelogs/2025/06/project-level_credentials_configuration_interface_in_project_settings.png" />
</Frame>

In the Organization Credentials page, Admins can view all credentials across the organization - including project-level ones - clearly marked in the Scope column. [Learn more](/guides/getting-started/getting-started/connect-your-cloud-account#credentials-management)

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/06/organization_credentials_page_showing_project-level_credentials_with_scope_column.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=bd2e287def565b393547ba9244717327" alt="Organization credentials page showing project-level credentials with scope column" width="2370" height="1248" data-path="images/changelogs/2025/06/organization_credentials_page_showing_project-level_credentials_with_scope_column.png" />
</Frame>

## Dry Run support for safe planning

You can now trigger Dry Runs - plan executions that skip the apply step. Dry Runs allow you to preview changes without affecting the environment status or modifying any related configurations.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/06/dry_run_execution_interface_showing_plan-only_mode_for_safe_environment_testing.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=7782a507123c786a217cbc4a7aa145b7" alt="Dry run execution interface showing plan-only mode for safe environment testing" width="950" height="816" data-path="images/changelogs/2025/06/dry_run_execution_interface_showing_plan-only_mode_for_safe_environment_testing.png" />
</Frame>

## Manually unlock remote state

You can now manually force unlock remote state when it's locked. The unlock option becomes available to users with the appropriate permissions whenever a state lock is detected.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/06/remote_state_unlock_interface_showing_manual_unlock_option_for_locked_state.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=ff32b4bc4b0e68abb97c3608e71d7640" alt="Remote state unlock interface showing manual unlock option for locked state" width="1536" height="753" data-path="images/changelogs/2025/06/remote_state_unlock_interface_showing_manual_unlock_option_for_locked_state.png" />
</Frame>

## Multiple VCS User Mappings

Organizations using more than one VCS provider can now map multiple VCS user accounts to a single env zero user. This makes it easier to manage identity and permissions across providers.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/06/vcs_user_mapping_interface_showing_multiple_provider_account_connections_to_single_env0_user.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=45a206b89bbbe7c097b9a1780045ca48" alt="VCS user mapping interface showing multiple provider account connections to single env zero user" width="2754" height="1110" data-path="images/changelogs/2025/06/vcs_user_mapping_interface_showing_multiple_provider_account_connections_to_single_env0_user.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).

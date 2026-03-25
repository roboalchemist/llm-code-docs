# Source: https://docs.envzero.com/changelogs/2025/05/new-in-drift-remediation-automated-code-updates-to-keep-iac-in-sync.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔄 New in Drift Remediation: Automated Code Updates to Keep IaC in Sync

Say hello to a smarter way to manage drift: now you can instantly capture changes made directly in your cloud environment and update your Infrastructure as Code with just a few clicks.

Drift remediation has typically involved aligning cloud resources back to match your code. Now, because different situations call for different approaches, env zero gives you an additional option: When a change is detected in the cloud, whether it's a manual fix, a security hotfix, or an optimization tool adjustment, env zero enables you to generate a pull request that captures the detected changes in your Infrastructure as Code. You can then choose to update your code automatically or manually based on the situation.

When drift is detected, env zero presents the details and lets you choose whether to:

* Align the cloud with your code
* Update your code with the detected cloud-side change

<br />

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/05/drift_detection_interface_showing_options_to_align_cloud_with_code_or_update_code_with_cloud_changes.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=effc7817d5df2f8e113bce4f373802cb" alt="Drift detection interface showing options to align cloud with code or update code with cloud changes" width="259" height="174" data-path="images/changelogs/2025/05/drift_detection_interface_showing_options_to_align_cloud_with_code_or_update_code_with_cloud_changes.png" />
</Frame>

<br />

If you choose to update your code, env zero will automatically generate a pull request through your Version Control System (VCS).

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/05/automated_pull_request_generation_interface_showing_vcs_integration_for_code_updates.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=1afb654a298bc99261c39bd67c22b7aa" alt="Automated pull request generation interface showing VCS integration for code updates" width="789" height="865" data-path="images/changelogs/2025/05/automated_pull_request_generation_interface_showing_vcs_integration_for_code_updates.png" />
</Frame>

<br />

You can also configure env zero to take action automatically based on your policies.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/05/policy_configuration_interface_for_automated_drift_remediation_settings.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=3d0c5f00ff266e0bd4b47f25d711f8f9" alt="Policy configuration interface for automated drift remediation settings" width="815" height="347" data-path="images/changelogs/2025/05/policy_configuration_interface_for_automated_drift_remediation_settings.png" />
</Frame>

This enhancement gives you full flexibility to decide how to manage changes while keeping your environments consistent, secure, and reliable.

Learn more about [drift remediation](/guides/admin-guide/environments/drift-detection/automatic-drift-remediation) and [how to automate it](/guides/policies-governance/drift-detection-policy#configuring-automatic-drift-remediation).

Built with [Mintlify](https://mintlify.com).

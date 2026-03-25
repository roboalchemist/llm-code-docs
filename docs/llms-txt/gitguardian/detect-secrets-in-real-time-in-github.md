# Source: https://docs.gitguardian.com/internal-monitoring/prevent/detect-secrets-in-real-time-in-github.md

# Detect secrets in GitHub PRs

> Describes how GitGuardian GitHub Check Runs detect secrets in pull requests and how to configure check run conclusions and per-repository settings.

## Overview

[GitHub Check Runs](https://docs.github.com/en/rest/checks/runs) will be triggered on GitHub pull requests on repositories monitored by GitGuardian. Secret scans in the context of GitHub Check Runs will run server-side on the VCS, at the post-receive stage.

GitGuardian secret scans run **on each individual commit that makes up the pull request, and not only the final state of the code** in the pull request. This deep scanning helps uncover cases where one commit A adds a secret and one commit B removes the same secret within the same pull request.

This allows the individual developer to get notified when an incident is detected by GitGuardian, **directly in the GitHub
interface**. This is particularly useful when a developer opens a pull request to merge an individual branch into a collaborative one. The Check Run will alert the developer before the commits are merged, **limiting the incident to their branch and giving them the opportunity of easier remediation**. The result is secrets-free collaborative branches such as the ones used for QA, staging, and production environments.

## How it looks

In the GitHub UI, a GitGuardian check run presents **a table with all findings and their relevant details**:
- the **id** of the corresponding secret incident on GitGuardian
- the **status** of the corresponding secret incident on GitGuardian
  Keep in mind that if secret incidents are closed on the GitGuardian dashboard, they will no longer be raised by GitHub checkruns.
- the secret type
- the commit sha
- the filename
- and also links to the GitGuardian dashboard if the user wishes to view the incident there and act on it (change status, leave notes, resolve, etc.).

![Checkruns conclusion in GitHub UI](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_conclusion_in_github.png)

![Checkruns details in GitHub UI](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_details_in_github.png)

Secrets incidents detected during check runs and raised in the GitGuardian dashboard also link back to the original GitHub pull request.

![Incidents details with pull request links](/img/internal-monitoring/integrate-sources/vcs-integrations/github/pull_requests_list_in_incident_detail.png)

> Please note that only GitHub pull requests created after February 10th, 2022 will be visible.

## Manage your GitHub check runs

### Activate or deactivate the GitGuardian check runs

As a workspace Manager, you can decide to turn the GitHub Check Runs On or Off for the monitored repositories directly in your [GitHub settings page](https://dashboard.gitguardian.com/settings/integrations/github) or [GitHub Enterprise Server settings page](https://dashboard.gitguardian.com/settings/integrations/github_enterprise_server).

![GitHub Check Runs](/img/internal-monitoring/integrate-sources/vcs-integrations/github/check_runs_settings.png)

> Note: If you have integrated both GitHub.com and GitHub Enterprise Server, you will have two different check runs settings.

### Choose the conclusion of check runs when secrets are detected

You also have the option to determine the conclusion of the GitHub check runs when secrets are detected. You can choose between two options:
- either `Failed` 
   This conclusion will **prevent your developers from merging the pull request** if you have protected branches in place, ensuring that your secrets do not make it to production.
   To prevent full blockages, GitGuardian provides skip action buttons for developers to bypass blocking check runs. More details can be found below.
- or `Neutral`
   This conclusion **does not block pull requests**.
   Developers will be notified of secret presence, especially if you enable GitGuardian to post a comment to enhance visibility of detected secrets in the pull request. Refer to the section below for more information.

![Checkruns status setting](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_conclusion_setting.png)

### Enable or disable skip actions

When the conclusion of the checkruns if secrets are detected is "Failed", pull requests are unable to be merged.
However, since the detection of secrets is probabilistic, **GitGuardian offers skip action buttons to prevent complete hindrance to developers**.
These skip actions mirror the ignore reasons available on the dashboard, with the understanding that skipping a checkrun containing a secret is akin to ignoring the associated incident. The available skip actions include:
- `Skip: false positive`
- `Skip: test credential`
- `Skip: low risk`

![GitHub checkruns skip buttons](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_skip_buttons.png)

When a skip action is taken, the corresponding secret incident is tagged to inform dashboard users that a developer intentionally skipped the checkrun after encountering the secret alert. The tags for skipped incidents include:
- `Skipped in check run as false positive`
- `Skipped in check run as test credential`
- `Skipped in check run as low risk`

![Skip actions tags](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_skip_actions_tags.png)

As a workspace manager, you have the option to disable the ability to skip check runs entirely in [your settings](https://dashboard.gitguardian.com/settings/integrations/github).

![Skip actions setting](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_skip_actions_setting.png)

### Post a comment in the pull request timeline

To extend the visibility of checkrun results and ensure your developers do not miss it, GitGuardian posts a comment when a secret is detected.

![Pull request comment](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_pull_request_comment.png)

Such behavior can be enabled or disabled in [your settings](https://dashboard.gitguardian.com/settings/integrations/github) by workspace Managers:

![Pull request comment setting](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_pull_request_comment_setting.png)

### Customize remediation guidelines

As a workspace Manager, you can customize the remediation guidelines. These guidelines will be displayed in the GitHub interface both in the check run body and in the comment posted on the pull request timeline.

![Customize remediation guidelines](/img/internal-monitoring/integrate-sources/vcs-integrations/github/check_runs_how_to_remediate_guidelines.png)

### Use public share links for incident details

When enabled, check runs will automatically generate public share links that allow developers to access and resolve incident details directly from the pull request interface, without requiring GitGuardian dashboard access.

The behavior works in conjunction with the "Auto-share incident access to the author of the leak" playbook: **public share links are used when the incident is created by a non-workspace member with a non-generic email address**, while **workspace members receive authenticated URLs** to the GitGuardian dashboard. This requires the [Auto-share incident access playbook](../../platform/automate-with-playbooks/available-playbooks.md#auto-share-incident-public-link-to-involved-developer) and [public sharing capability](../../platform/enterprise-administration/workspace-settings#public-sharing) to be enabled. Share links inherit the same security controls and expiration times as the auto-share playbook.

As a workspace Manager, you can enable or disable this feature in [your GitHub settings](https://dashboard.gitguardian.com/settings/integrations/github).

## Dependencies

### GitHub branch protection: rulesets vs branch protection rules

GitHub offers two ways to protect your branches: **rulesets** and **branch protection rules**. Understanding the difference is important when configuring GitGuardian check runs:

#### Using rulesets

If you're using a **ruleset** and require GitGuardian security checks to pass:

- You should also enable **"Require a pull request before merging"**. Without this setting, GitHub will block any push made directly to the protected branch, since rulesets apply to all commits including direct pushes.
- Your **repository must be actively monitored by GitGuardian**. If it is not, GitHub will be waiting for a check run from GitGuardian that will never be provided, causing a perpetual pending check run.
- If the check run conclusion is `Failed`, GitHub will display a specific warning. The `Neutral` conclusion is considered the same as a successful check run.

![rulesets](/img/internal-monitoring/integrate-sources/vcs-integrations/github/gh_rulesets.png)

#### Using branch protection rules

If you're using **branch protection rules** with the **"Require status checks to pass before merging"** setting:

![Branch protection rule](/img/internal-monitoring/integrate-sources/vcs-integrations/github/gh_branch_protection_rule.png)

- **Branch protection rules** only apply to pull requests, not to direct pushes to the branch, so they work seamlessly with GitGuardian check runs without additional configuration.
- Your **repository must be actively monitored by GitGuardian**.
   If it is not, GitHub will be waiting for a check run from GitGuardian that will never be provided, causing a perpetual pending check run.
   ![Required and pending check run](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_required_and_pending.png)
- If the check run conclusion is `Failed`, GitHub will display a specific warning.
   The `Neutral` conclusion is considered the same as a successful check run.
   ![Required and failed check run](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_required_and_failed.png)

### Working with forked repositories

In a fork process, there are two repositories:

1. **Forked repository**: Your personal copy of the upstream repo, marked as `fork = true` on GitHub.
2. **Upstream repository**: The original repository.

#### Forked repositories

By default, GitGuardian does **not** generate check runs on monitored forked repositories to prevent rate limiting errors.

This issue arises because many forked repositories automatically generate numerous pull requests to stay up-to-date with their upstream repositories, which often have high activity levels. These automated pull requests are resource-intensive and can lead to rate limiting errors during GitGuardian check runs.

However, managers of workspaces under the Business plan have the option to [enable GitGuardian check runs on their monitored forked repositories](https://dashboard.gitguardian.com/settings/integrations/github).

![Check runs on monitored forked repositories setting](/img/internal-monitoring/integrate-sources/vcs-integrations/github/check_runs_on_monitored_forked_repositories_setting.png)

#### Upstream repositories

Check runs are created on monitored upstream repositories.
However, when a pull request originating from a forked repository contains secrets, GitGuardian cannot propose the usual "Skip" actions buttons. In this scenario, GitGuardian provides a simple `Skip` button to avoid blocking the developer.

![Forked repositories PR](/img/internal-monitoring/integrate-sources/vcs-integrations/github/checkruns_forked_repositories.png)

### GitHub Merge Queue support

When a pull request is added to a GitHub merge queue, GitGuardian responds with a neutral check run because:

- Secret scanning is already performed on pull requests **before** they enter the merge queue
- The merge queue doesn't create new commits that could introduce new secrets
- PRs must pass GitGuardian check runs before being eligible for the merge queue

This neutral status will not block the merge queue validation, even if the GitGuardian check is marked as required.

## Going further: customizing check runs on a per-repository basis

GitGuardian offers you the ability to customize the behavior of GitGuardian check runs at the repository level by utilizing GitHub's native features to override the configuration set on the GitGuardian dashboard.

### Using GitHub custom properties

[GitHub custom properties](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization) allow you to customize check runs both at the organization level and the repository level:
- whether the checkrun is present or not
- specifying the conclusion as either `Failed` or `Neutral` when secrets are detected.
- whether the [skip actions](detect-secrets-in-real-time-in-github#enable-or-disable-skip-actions) are available or not.

![custom properties to override check run settings](/img/internal-monitoring/integrate-sources/vcs-integrations/github/create_organization_custom_property_to_override_checkruns_settings.png)

> It is crucial to use the exact names of the custom properties given below to ensure the feature functions properly.

#### Overriding check runs presence

> Supported property types: (Text, Single select, True/False)

   
      
         GitGuardian global configuration
         Custom property `gitguardian-check-runs-enabled`
         
         
      
   
   
      
         
         `true`
         `false`
         `null`
      
      
         Check runs are activated â
         check runs will be present â
         check runs wonât be present ð«
         check runs will be present â
      
      
         Check runs are deactivated ð«
         check runs will be present â
         check runs wonât be present ð«
         check runs wonât be present ð«
      
   

#### Overriding check runs conclusion

> Supported property types: (Text, Single select)

   
      
         GitGuardian global configuration
         Custom property `gitguardian-check-runs-secrets-conclusion`
         
         
      
   
   
      
         
         `neutral`
         `failed`
         `null` or other
      
      
         Check runs conclusion if secrets is Neutral â¬
         check runs conclusion if secrets will be Neutral â¬
         check runs conclusion if secrets will be Failed â (blocking the PR)
         check runs conclusion if secrets will be Neutral â¬
      
      
         Check runs conclusion if secrets is Failure â
         check runs conclusion if secrets will be Neutral â¬
         check runs conclusion if secrets will be Failed â (blocking the PR)
         check runs conclusion if secrets will be Failed â (blocking the PR)
      
   

#### Overriding check runs skip actions presence when the conclusion is Failed

> Supported property types: (Text, Single select, True/False)

   
      
         GitGuardian global configuration
         Custom property `gitguardian-check-runs-actions-enabled`
         
         
      
   
   
      
         
         `true`
         `false`
         `null`
      
      
         Skip action buttons are enabled â
         skip action buttons will be present â
         skip action buttons wonât be present ð«
         skip action buttons will be present â
      
      
         Skip action buttons are disabled ð«
         skip action buttons will be present â
         skip action buttons wonât be present ð«
         skip action buttons wonât be present ð«
      
   

### Using GitHub labels for GitHub Enterprise Server < 3.13

:::caution
Using [GitHub labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) to customize check runs is deprecated and will be removed in January 2026.
Please migrate to [Custom properties](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization) which are available starting from GitHub Enterprise Server version 3.13.

Please get in touch with your account manager to have this feature activated.
:::

On GitHub Enterprise Server < 3.13, [GitHub labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) allow you to customize check runs at the repository level:
- whether the check run is present or not.
- specifying the conclusion as either `Failed` or `Neutral` when secrets are detected.
- whether the [skip actions](detect-secrets-in-real-time-in-github#enable-or-disable-skip-actions) are available or not.

![Repo label to override check run settings](/img/internal-monitoring/integrate-sources/vcs-integrations/github/create_repository_label_to_override_checkruns_settings.png)

> You are free to customize the label's description and color, but it is essential that the label name remains exact.

#### Overriding check runs presence

| GitGuardian global configuration | GitHub Enterprise Server repository labels |                                   |                               |                              |
| -------------------------------- | ------------------------------------------ | --------------------------------- | ----------------------------- | ---------------------------- |
|                                  | `gitguardian:check-runs-enabled`           | `gitguardian:check-runs-disabled` | No labels                     | Both labels present          |
| Check runs are activated â       | check runs will be present â               | check runs wonât be present ð«     | check runs will be present â  | check runs will be present â |
| Check runs are deactivated ð«     | check runs will be present â               | check runs wonât be present ð«     | check runs wonât be present ð« | check runs will be present â |

#### Overriding check runs conclusion

| GitGuardian global configuration              | GitHub Enterprise Server repository labels          |                                                                      |                                                                    |                                                    |
| --------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------- |
|                                               | `gitguardian:check-runs-secrets-conclusion-neutral` | `gitguardian:check-runs-secrets-conclusion-failed`                   | No labels                                                          | Both labels present                                |
| Check runs conclusion if secrets is Neutral â¬ | check runs conclusion if secrets will be Neutral â¬  | check runs conclusion if secrets will be Failed  â (blocking the PR) | check runs conclusion if secrets will be Neutral â¬                 | check runs conclusion if secrets will be Neutral â¬ |
| Check runs conclusion if secrets is Failure â | check runs conclusion if secrets will be Neutral â¬  | check runs conclusion if secret will be Failed â (blocking the PR)   | check runs conclusion if secret will be Failed â (blocking the PR) | check runs conclusion if secrets will be Neutral â¬ |

#### Overriding check runs skip actions presence when the conclusion is Failed

| GitGuardian global configuration   | GitHub Enterprise Server repository labels |                                           |                                        |                                       |
| ---------------------------------- | ------------------------------------------ | ----------------------------------------- | -------------------------------------- | ------------------------------------- |
|                                    | `gitguardian:check-runs-actions-enabled`   | `gitguardian:check-runs-actions-disabled` | No labels                              | Both labels present                   |
| Skip action buttons are enabled â  | skip action buttons will be present â      | skip action buttons wonât be present ð«    | skip action buttons will be present â  | skip action buttons will be present â |
| Skip action buttons are disabled ð« | skip action buttons will be present â      | skip action buttons wonât be present ð«    | skip action buttons wonât be present ð« | skip action buttons will be present â |

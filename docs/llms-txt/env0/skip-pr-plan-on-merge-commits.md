# Source: https://docs.envzero.com/guides/policies-governance/skip-pr-plan-on-merge-commits.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Skipping PR Plans on Merge Commits

> Prevent unnecessary PR plans from running on merge commits by considering only PR file changes in env zero

This policy helps you ignore a [PR Plan](/guides/admin-guide/environments/plan-on-pull-request) for merge commit in the case that the merge commit includes file changes that cause a PR Plan to run.

By default, we consider file changes between two commits, but when you push merge commit we could consider file changes that are not included in the PR.

In case you enable this policy we will consider only files that are included in the PR.

<Warning>
  Updated PR plan

  In case you enable this policy - we may not update the PR plan for the environment even if the environment revision was changed. until you cause the PR Plan trigger for this PR.
</Warning>

<Info>
  **Supported VCS**

  GitHub, Bitbucket, Gitlab and Bitbucket Server
</Info>

Configure this policy in Organization Settings -> POLICIES

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/organization_settings_policies_configuration.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=70b8070d934390f143433c9f06be3eb8" alt="Organization settings policies configuration" width="1410" height="457" data-path="images/guides/policies-governance/organization_settings_policies_configuration.png" />
</Frame>

<Info>
  Additional Content

* [Alternative to Atlantis](https://www.env0.com/alternatives/atlantis-alternative)
* [Migrating from Atlantis to env zero](https://www.env0.com/blog/video-tutorial-how-to-migrate-from-atlantis-to-env0)
</Info>

Built with [Mintlify](https://mintlify.com).

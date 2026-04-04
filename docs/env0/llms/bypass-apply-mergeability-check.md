# Source: https://docs.envzero.com/guides/policies-governance/bypass-apply-mergeability-check.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bypass Apply Mergeability Check

> Resolve circular dependency when env zero Apply status check is required in GitHub branch protection

When using [Plan and Apply via PR Comments](/guides/admin-guide/environments/plan-and-apply-from-pr-comments), env zero checks that a pull request is mergeable before running an apply. If you also set the `env0/Apply` commit status as a **required status check** in GitHub branch protection, this creates a circular dependency: the PR is not mergeable because `env0/Apply` has not passed yet, but apply cannot run because the PR is not mergeable.

The **Bypass Apply Mergeability Check** policy resolves this by evaluating the PR's mergeability while **excluding env zero's own Apply status checks** from the requirements.

<Note>
  This policy applies to **GitHub and GitHub Enterprise** only. Other VCS providers are not affected.
</Note>

## How It Works

When this policy is enabled, env zero evaluates the PR's mergeability by querying GitHub's branch protection rules and repository rulesets directly, rather than relying on GitHub's merged mergeability state. During this evaluation, env zero excludes its own Apply-related status checks (such as `env0/Apply`) from the required checks list.

This means all other branch protection requirements (such as required reviews and other CI checks) are still enforced. Only the env zero Apply checks are bypassed.

## Enabling the Policy

Navigate to **Organization Settings** → **Policies**, and under **Plan and Apply from PR comments**, check **Bypass PR mergeability check for env0/Apply (GitHub only)**.

<img src="https://mintcdn.com/envzero-b61043c8/fkSDibxEZKnzmu2I/images/guides/policies-governance/bypass_apply_mergeability_check_setting.png?fit=max&auto=format&n=fkSDibxEZKnzmu2I&q=85&s=301b8b354bc764be357eb8c8f1e571c8" alt="" width="2674" height="228" data-path="images/guides/policies-governance/bypass_apply_mergeability_check_setting.png" />

## When to Use This Policy

Enable this policy if you:

1. Use [PR comment applies](/guides/admin-guide/environments/plan-and-apply-from-pr-comments)
2. Have GitHub branch protection or repository rulesets that require the `env0/Apply` status check to pass before merging

<Warning>
  If you do not have `env0/Apply` set as a required status check in your GitHub branch protection rules, you do not need this policy.
</Warning>

Built with [Mintlify](https://mintlify.com).

# Source: https://docs.jit.io/docs/policies.md

# Policies

Policies let you define organization-wide security rules that apply consistently across repositories and SCMs.

Use policies to:

* Enforce development guardrails in pull/merge requests (PR/MR)
* Standardize security behavior across repositories
* Roll out enforcement gradually (e.g., start with warnings before blocking merges)

## Where policies apply

Policies are configured in the Jit platform and evaluated automatically when relevant events occur (for example, when a pull request is opened or updated).

## Available policies

> More policies will be documented here over time.

* [SLA Enforcement on Pull Requests](https://docs.jit.io/docs/sla-enforcement-on-pull-requests) - Warn or block PRs when overdue security findings exist in the target branch and are not resolved by the PR.

> Tip: Some policies may be gated behind a feature flag. If you don’t see a policy in your environment, contact Jit support.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f207fd06f44d61d59eb465329e632e75b196e0699f39c86899004472528dde6a-Screenshot_2026-02-22_at_15.34.38.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]
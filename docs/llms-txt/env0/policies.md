# Source: https://docs.envzero.com/guides/policies-governance/policies.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Policies

> Overview of runtime and deployment policies for governing cloud resources in env zero

Policies are used to regulate cloud usage within an organization. env zero supports runtime and deployment policies as described below.

Policies are used to:

* Enforce organizational policies of cloud resources provisioning (who can provision, when can they provision, and what resources can they provision)
* Implement best practices
* Mitigate risks by applying guardrails

All while maintaining flexibility and autonomy within env zero.

## Runtime Policies

Runtime policies are native to the env zero system, and are consistently monitored and enforced, when creating, deploying or configuring environments.

The policies are enforced both in the UI and when using the API.

Runtime policies include

* [Environment Destroy Protection](/guides/policies-governance/destroy-protection)
* [Environment Limits](/guides/policies-governance/environment-limits)
* [Environment Time to Live](/guides/policies-governance/policy-ttl)
* [Default Auto-Approve](/guides/policies-governance/default-auto-approve)
* [Cost Estimation](/guides/policies-governance/cost-estimation)
* [Skip Apply Step](/guides/policies-governance/skip-apply-step)
* [Skip Redundant Deployments](/guides/policies-governance/skip-redundant-deployments)
* [Skip PR Plan on Merge Commits](/guides/policies-governance/skip-pr-plan-on-merge-commits)
* [Do Not Report Skipped Status Check](/guides/policies-governance/do-not-report-skipped-status-check)
* [Bypass Apply Mergeability Check](/guides/policies-governance/bypass-apply-mergeability-check)
* [Force Remote Backend](/guides/policies-governance/force-remote-backend)
* [Drift Detection](/guides/policies-governance/drift-detection-policy)
* [Allow Saving Secrets](/guides/policies-governance/allow-env0-secrets)

## Deployment Policies

Deployment policies are enforced when deploying or redeploying an environment (whenever changes are made to the environment) to ensure compliance with security, governance, or other standards.

Deployment policies are based on the [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/) (OPA) framework and are invoked at the appropriate deployment stage using the [Approval Policies](/guides/policies-governance/approval-policies) feature.

Built with [Mintlify](https://mintlify.com).

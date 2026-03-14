# Source: https://docs.gitguardian.com/secrets-detection/customize-detection/validity-checks.md

# Validity checks

> Describes how GitGuardian validity checks verify whether detected secrets are still active through non-intrusive API calls.

### How validity checks work

To provide you with high-precision alerts, GitGuardian tries to **verify the validity of secrets through non-intrusive API calls made to the host, if and when possible**.

![Secret validity preview and filter](/img/internal-monitoring/remediate/incidents/secret_validity_filter.png)

The validity check can return 5 possible values:

- **valid:** the secret can still be exploited and needs to be revoked and rotated .
- **invalid:** the secret has been revoked.
- **failed to check**: GitGuardian was not able determine the validity of the secret. It happens when it is not possible to distinguish the error caused by an invalid secret and an IP allowlist or another mechanism preventing the validity check. It can also mean the service provider is temporarily unavailable.
- **cannot check:** the service provider or the secret type do not allow for checks by GitGuardian. This status is also displayed when secret validity checks are disabled by a workspace Manager.
- **unknown:** GitGuardian has recently introduced a validity checker, this secretâs validity has not been verified yet.

GitGuardian automatically runs the secret validity checks in the background. The frequency of these checks depends on your plan and the status and age of secret incidents:

| Plan     | Incident status | Incident age         | Frequency   |
| -------- | --------------- | -------------------- | ----------- |
| Business | Open            | Less than a year old | Daily       |
| Free     | Open            | Less than a year old | Weekly      |
| Business | Open            | More than a year old | Weekly      |
| Free     | Open            | More than a year old | Monthly     |
| Business | Ignored         | Less than a year old | Monthly     |
| Free     | Ignored         | Less than a year old | Half-yearly |
| Business | Ignored         | More than a year old | Half-yearly |
| Free     | Ignored         | More than a year old | Never       |
| Business | Resolved        | Less than a year old | Monthly     |
| Free     | Resolved        | Less than a year old | Half-yearly |
| Business | Resolved        | More than a year old | Half-yearly |
| Free     | Resolved        | More than a year old | Never       |

> If you use GitGuardian self-hosted, you can change these frequencies in your [admin area](../../self-hosting/management/application-management/admin-area.md).

### Enabling and disabling validity checks

It is possible to disable the validity checks for the entire GitGuardian workspace.

New secrets that could be marked as `valid` or `invalid` will have their validity set to `unknown` since their associated validity checker is toggled off. Re-enabling the validity checker will trigger the verification process on all existing incidents, if and when possible.

![Secrets detection settings](/img/secrets-detection/customize-detection/secrets_detection_global_validity_checks.png)

Please note that these settings also apply to the API and ggshield. Detectors requiring validity checks to be enabled to be active will be deactivated and the rest of the detectors will return the value `unknown` for secrets validity checks.

:::caution
However, please be advised that **some detectors require validity checks to be enabled to be active**. If you choose to keep validity checks globally disabled, these detectors will be deactivated and will no longer raise any incidents.

To verify if a detector requires validity checks to be enabled to raise incidents, go to the detector's dedicated page in the [Secrets Detection documentation](../../secrets-detection/secrets-detection-engine/detectors/supported_credentials) and look for the flag `Only valid secrets raise an alert: True` (eg: [Agora API keys](../../secrets-detection/secrets-detection-engine/detectors/specifics/agora_api_keys.md)).

![Secret detector only valid true](/img/secrets-detection/customize-detection/secrets_detection_global_validity_detector_valid_only_true.png)
:::

### Customize validity checks

GitGuardian allows customization of validity checks for certain detectors by specifying a custom host.

Consider the [`GitLab token`](../../secrets-detection/secrets-detection-engine/detectors/specifics/gitlab_token.md) detector. By default, it checks secrets against `gitlab.com` (GitLab SaaS). However, if you have a self-hosted GitLab instance, you can provide the URL of your instance. GitGuardian will then verify any detected `GitLab token` secrets against your self-hosted environment.

A validity checker endpoint includes:
- a host
- a path

You **only need to provide the host**. GitGuardian uses the same path as the default host for the custom check.

So let's say that the validity checker of the GitLab token is `https://gitlab.com/the-route-to-check-the-validity`.
You simply need to provide the host (eg: `https://my_gitlab.self_hosted_instance.corp`) and GitGuardian builds the validity checker `https://my_gitlab.self_hosted_instance.corp/the-route-to-check-the-validity`.

![Secret detector custom host](/img/internal-monitoring/remediate/custom-host-for-validity-check/secret_detector_custom_host.png)

When you submit a custom host for validity checks, all previously detected secrets for that detector will be re-checked against the new host. This ensures that you have the most accurate validity information.

![Secret valid on custom host](/img/internal-monitoring/remediate/custom-host-for-validity-check/secret_valid_on_custom_host.png)

:::info
Only detectors that support validity checks and have the attribute `On-premise instance exist: True` can be customized with a custom host URL for validity checks.

![Secret detector eligible for custom host](/img/internal-monitoring/remediate/custom-host-for-validity-check/secrets_detector_eligible_for_custom_host.png)

If you are under Business plan, you can see the list on the eligible detectors in the [table of detectors](https://dashboard.gitguardian.com/settings/secrets/detectors).

![Table of detectors eligible for custom host](/img/internal-monitoring/remediate/custom-host-for-validity-check/table_of_detectors_eligible_to_custom_host.png)
:::

> This feature is only available for workspaces under our Business plan.

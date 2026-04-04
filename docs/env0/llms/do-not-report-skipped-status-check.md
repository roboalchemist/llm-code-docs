# Source: https://docs.envzero.com/guides/policies-governance/do-not-report-skipped-status-check.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Omitting Skipped Status Checks

> Stop env zero from reporting skipped PR plan status checks to reduce noise in pull requests

When [Plan on Pull Request](/guides/admin-guide/environments/plan-on-pull-request) is enabled, for every commit of a Pull Request, we report a commit status check based on the status of the associated PR Plan that ran in env zero. See [Plan on Pull Request](/guides/admin-guide/environments/plan-on-pull-request) for more info on commit statuses.

By default, if there was a PR commit that didn't include any changes that are relevant to the env zero environment, because the commit doesn't include changes in a file that is part of the glob pattern or template directory, then env zero reports the commit as status "skipped" in GitHub, or "success" in other VCS-es.

Marking the commit as "skipped" allows you to set those status checks as "required" in your VCS.\
However, for some use-cases you might want env zero not to set those status checks as "skipped". For example, if you have a lot of env zero status checks on your PR that you don't want to see there.

For that, we have the "Do not report skipped status checks" policy. When setting it, env zero will not create the status checks at all, instead of marking them as "skipped".

Setting the policy could be very helpful for a monorepo setup that includes many [Templates](/guides/admin-guide/templates), for example.

<Warning>
  Required Status Check

  If you want to make an env zero status check be required in your VCS - you can't use this policy. If a PR Plan is not run and this policy is checked, then we won't create a status check at all, and merge will be blocked
</Warning>

Configure this policy in Organization Settings -> POLICIES

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/b6c925a-screenshot_2023-01-01_at_10.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=dcc7220a44d8b7b5dfc743c2201498a0" alt="" width="1444" height="587" data-path="images/guides/policies-governance/b6c925a-screenshot_2023-01-01_at_10.png" />

**Setting this policy can help avoid the following situation in your pull requests:**

<Frame caption="Pull Request status checks">
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/pull_request_status_checks_display.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=90417feca6618c35610fe7c02edd1e46" alt="Pull request status checks display" width="784" height="104" data-path="images/guides/policies-governance/pull_request_status_checks_display.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).

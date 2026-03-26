# Source: https://momentic.ai/docs/failure-recovery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Failure recovery (Beta)

<Warning>
  Failure recovery is in beta and subject to change or be deprecated in the
  future.
</Warning>

Momentic can automatically attempt to recover from certain transient test
failures, such as slow page loads, temporary modals, and UI race conditions.

<Info>
  Failure recovery is best effort. It reduces noise from temporary conditions,
  but it is not guaranteed to recover every run. Recovery behavior can change
  over time.
</Info>

## Recovery behavior

When an eligible test fails, Momentic analyzes the failure and classifies it as
recoverable or not recoverable.

* **Recoverable**: transient, explainable conditions where the failed step can
  likely succeed after restoring the page to a good state.
* **Not recoverable**: legitimate failures, infrastructure issues, or ambiguous
  cases where retrying could hide a real problem.

For recoverable failures, Momentic generates and executes recovery steps, then
automatically retries the failed step. If the retry succeeds, the test
continues. If not, the run is marked failed.

<Info>
  Failure recovery adds runtime latency. The initial diagnosis ranges from 5-20
  seconds. Recovery steps are also generated dynamically, which can add up to 10
  seconds per newly generated step (plus normal step execution time).
</Info>

Recovery activity is visible in the run viewer and CLI output. In the run
viewer, you can filter tests by recovery status to quickly find recovered runs.

## Configuration

Failure recovery can be enabled or disabled per test in test options. You can
also set defaults in your organization's [CLI configuration](/cli/configuration)
for local executions or on the
[AI settings page](https://app.momentic.ai/settings/ai) for Cloud runs.

Failure recovery uses your test description to preserve test intent. You can
also use test options to describe custom scenarios that should or should not be
treated as recoverable.

## Limitations

A single test run is eligible for failure recovery up to 3 times. Only primitive
steps can be recovered: steps that contain other steps such as modules and AI
actions are not eligible.

Only tests running in CI (detected through the `CI` environment variable) are
eligible for failure recovery. Interactive editor sessions never trigger failure
recovery.

In addition, the following scenarios are not eligible for failure recovery:

* **Infrastructure issues**: Momentic will not recover from infrastructure
  issues such as network timeouts, server errors, full-page errors, or 500
  response codes. We recommend you configure retries on your test or configure
  your CI to wait until fixtures are ready before invoking Momentic.
* **Legitimate failures**: if all steps were executed correctly and the test
  fails due to a legitimate error, failure recovery will not be triggered. This
  includes permanent user behavior and flow changes where the test is now out of
  sync with the application and needs to be updated.
* **Configuration errors**: Momentic will not attempt to salvage tests that have
  incorrect step options or nonsensical action sequences.

## Examples

Recoverable examples:

* A cookie consent modal temporarily blocks the intended click target.
* A page transition is still in progress when an assertion runs.
* A stale cached target causes a mis-click, and retrying with fresh targeting
  can recover.

Not recoverable examples:

* Login now requires a new permanent **Continue** step after entering username.
* The app returns a full-page 500 error after form submission.
* A network timeout or backend outage prevents required data from loading.
* The browser/page process crashes during the run.
* A CAPTCHA or anti-bot challenge blocks further progress.
* A required action is blocked by account plan limits or missing permissions.

## Usage guidance

If a test is recovered frequently, treat it as unstable test behavior, not a
successful long-term state.

* Do not rely on failure recovery as the only reason a test passes.
* Fix the test or app behavior to remove recurring recovery conditions.
* Quarantine persistently flaky tests until they are corrected (see
  [quarantine](/quarantine)).
* Use run viewer recovery-status filters to monitor and triage recurring
  recoveries.


Built with [Mintlify](https://mintlify.com).
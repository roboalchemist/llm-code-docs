# Source: https://docs.bugbug.io/best-practices.md

# Best practices

## How to prepare your app for testing

#### 1) Ensure your environment is reachable from where tests run

Before you invest time in test coverage, decide where you will run tests:

* **Local** runs are fast for debugging.
* **Cloud** runs are best for schedules and uninterrupted monitoring.

If your app is behind a [VPN, firewall, or private network,](https://docs.bugbug.io/troubleshooting/vpn-or-a-firewall) cloud runners may not reach it without preparation. In that case, plan allowlisting or an accessible test environment.&#x20;

{% hint style="info" %}
[Read if cloud runs are intermittently failing.](https://docs.bugbug.io/troubleshooting/cloud-tests-sometimes-failing)
{% endhint %}

#### 2) Add stable selectors (before you record tests)

Unstable selectors are the #1 cause of “element not found / element not visible” failures. Avoid relying on auto-generated CSS classes, dynamic IDs, or positional selectors (“second row”, “third button”). Instead, add stable attributes to key UI elements (for example `data-testid` or `data-test`).

What to tag first (Level 1 smoke paths):

* Primary CTA buttons (save, submit, checkout, confirm)
* Login inputs and submit button
* Navigation items
* Critical page headings and section titles you assert on
* Notifications/toasts and error banners

{% hint style="info" %}
Learn more about [Selectors](https://docs.bugbug.io/preventing-failed-tests/selectors) and [Common selectors issues](https://docs.bugbug.io/troubleshooting/common-selectors-issues).&#x20;
{% endhint %}

#### 3) Make UI behavior deterministic (remove randomness)

Automation works best when the same inputs produce the same UI every time. The usual sources of randomness are:

* A/B tests and feature flags that change layout or labels per session
* Personalization based on cookies/localStorage
* Non-deterministic data ordering in lists/tables

Practical patterns that work well:

* Disable experiments for automation traffic, or force a single variant.
* Provide a “test mode” parameter (for example `?e2e=1`) that disables non-essential UI variability.
* Keep a stable test dataset (seeded data, predictable records).

If experiments are involved, address them early, otherwise “flaky” becomes permanent background noise.

#### 4) Treat CAPTCHA as an environment constraint (not a test step)

CAPTCHA is designed to block automation. If your flows include CAPTCHA (signup, password reset, forms), plan a bypass for test runs.

A reliable approach is to implement a backend “skip CAPTCHA” mechanism that activates only when a secret custom header is present in requests from BugBug.

{% hint style="info" %}
Learn more about [CAPTCHA in automation testing.](https://docs.bugbug.io/troubleshooting/captcha-in-automation-testing)
{% endhint %}

#### 5) Secure your environment with HTTPS

Ensure your testing environment has a valid SSL certificate, as BugBug runs in incognito mode, which can block access to non-HTTPS sites or trigger security warnings that interfere with the test.

#### 6) Set up dedicated test accounts

Create specialized "test user" accounts dedicated solely to automation. If your product has different combinations of preferences or roles, create a separate user for each combination to reduce the number of steps in each test.

#### 7) Use waiting conditions and timeouts intentionally

Many failures are timing-related: the UI is correct, but the test attempts the next action before the element is ready.

Two levers matter most:

* [Waiting conditions](https://docs.bugbug.io/preventing-failed-tests/waiting-conditions) (reduce the need for fragile “sleep” steps)
* [Timeouts](https://docs.bugbug.io/preventing-failed-tests/timeout) (especially in cloud, where pages can load slower)

#### 8) Whitelisting for cloud access

If your application is behind a firewall or uses services like Cloudflare, you must whitelist BugBug cloud runner IP addresses to prevent "No Internet" or 403 errors during cloud execution.

#### 9) Manage MFA Exceptions

You should either create security exceptions for BugBug IPs or use specific testing accounts configured to bypass MFA.

#### 10) Parameterize environments and test data with variables

Hardcoding URLs and values across many tests becomes a maintenance trap (especially when you have staging/pre-prod variants).

Use variables to store:

* Base URL / domain
* Test user emails
* Common input values (product names, ZIP codes, etc.)

{% hint style="info" %}
Learn more about [Variables](https://docs.bugbug.io/editing-tests/variables) and [Local Variables](https://docs.bugbug.io/editing-tests/local-variables).
{% endhint %}

#### 11) Optimize network traffic

Investigate if your app sends frequent background requests (like monitoring pings). If these stack up, they can trigger timeouts because the runner waits for network requests to finish before moving to the next step.

{% hint style="info" %}
In BugBug, you can set the number of background requests as a waiting condition and adjust it to the specifics of your app.
{% endhint %}

#### 12) Build in observable checkpoints (assertions)

Stable automation is not only about clicking; it’s about verifying that the app is in the expected state.

Add assertions to confirm:

* Correct page/section is visible
* Expected text is present
* Error banners are absent (or present when expected)

{% hint style="info" %}
Learn more about [Assertions](https://docs.bugbug.io/editing-tests/assertions).
{% endhint %}

## Mistakes to avoid

#### 1) Automation overload

Avoid the mistake of trying to automate every single feature immediately. Start with 5 to 10 short, simple tests that cover your "core features" - functions used by more than 80% of your users.

#### 2) Recording long “do-everything” tests too early

Long tests are hard to debug and fail for unrelated reasons. Prefer short, atomic tests that validate one intent at a time (login, create record, checkout, etc.). This improves signal and reduces maintenance.

#### 3) Relying on volatile selectors (dynamic classes, structure, position)

Avoid selectors that depend on:

* Auto-generated CSS class names
* Dynamic IDs
* Deep DOM structure that changes with minor UI refactors
* Positional targeting (“the second button in the row”)

#### 4) Forgetting "GoTo" steps

Every test or suite run must begin with a navigation to a URL. Skipping this step will cause immediate failure.

#### 5) Treating CAPTCHA as “something to click through”

If your flow has CAPTCHA, it will eventually block automated runs. Use a controlled bypass in a test environment (or a secure “test mode” mechanism).

#### 6) Running locally and minimizing the test window

Chrome may put minimized tabs into standby mode, which can stop JavaScript execution and break local runs. For uninterrupted operation, run tests in the cloud.

{% hint style="info" %}
Learn more about [Prohibited behaviors](https://docs.bugbug.io/troubleshooting/prohibited-behaviors).
{% endhint %}

#### 7) Using static sleeps instead of waiting conditions

Hard-coded delays make tests slow and still unreliable (too short fails; too long wastes time). Prefer waiting conditions and tune timeouts where needed.

#### 8) Neglecting manual "Hover" recording

Do not assume the recorder will automatically catch all menu interactions; if your navigation relies on mouse movements, you must manually click the "Hover" action during recording.

{% hint style="info" %}
Learn more about [Hover test step](https://docs.bugbug.io/recording-tests-steps/recording-hover).
{% endhint %}

#### 9) Using shared accounts for Parallel runs

Do not use a single shared account for multiple tests intended to run in parallel. This often causes users to be suddenly logged out when another runner attempts to sign in. Unique accounts should be assigned to each test to maximize parallel potential.

#### 10) Ignoring the “cloud vs local” reality

Cloud environments can be slower than your laptop. If a test is stable locally but fails in the cloud:

1. Increase timeout for cloud runs.&#x20;
2. Confirm waiting conditions are enabled and appropriate.&#x20;
3. Check cloud [troubleshooting guidance](https://docs.bugbug.io/troubleshooting).

#### 11) Ignoring test data cleanup

A common mistake is failing to clean up data created by a test. If a test creates a record but fails before it can archive it, the next run may fail due to duplicate entries; set up an initial group to check for and clean existing records as a failsafe.

#### 12) Duplicating shared flows everywhere instead of reusing them

If you copy/paste the same login flow into many tests, maintenance cost grows linearly. When you reach repeated blocks, consider extracting shared flows into reusable [components](https://docs.bugbug.io/editing-tests/components).

###

### When something breaks: fast triage

If a test fails, this sequence resolves most issues quickly:

1. Confirm selector stability: [Selectors](https://docs.bugbug.io/preventing-failed-tests/selectors).
2. Check responsive duplicates / hidden elements: [Common selectors issues](https://docs.bugbug.io/troubleshooting/common-selectors-issues).&#x20;
3. Review timing and cloud differences: [Timeout](https://docs.bugbug.io/preventing-failed-tests/timeout) and [Cloud tests sometimes failing](https://docs.bugbug.io/troubleshooting/cloud-tests-sometimes-failing).
4. If the flow includes CAPTCHA: [CAPTCHA in automation testing](https://docs.bugbug.io/troubleshooting/captcha-in-automation-testing).&#x20;
5. Contact our helpful [Customer Support Team](https://bugbug.io/contact/).

{% hint style="danger" %}
[Check the list of error codes.](https://docs.bugbug.io/debugging-tests/error-codes)
{% endhint %}

## Discover how to work with BugBug

We’ve prepared a short guide with essential recommendations on test automation that we created specifically for startups. We divided the guide into 3 levels:

[★☆☆ Level 1: get the most out of basic automation](https://bugbug.io/blog/software-testing/automation-testing-guide-for-startups-level-1/)

[★★☆ Level 2: automate hundreds of regression tests](https://bugbug.io/blog/software-testing/automation-testing-guide-for-startups-level-2/)

[★★★ Level 3: integrate with CI/CD builds](https://bugbug.io/blog/software-testing/automation-testing-guide-for-startups-level-3/)

## Also see&#x20;

If you're a beginner, don't forget to check our guide dedicated to non-technical people: [beginner's tutorial to automation testing with BugBug](https://docs.bugbug.io/in-depth-guides/beginners-tutorial-to-automation-testing)

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F4U22qkYFHtgX01lJaxkh%2F_efa56381-fd31-40f9-ad1b-445a37f57534%20(3).png?alt=media&#x26;token=a7fd99b1-9962-4c42-b445-e722a0b6638b" alt="" width="375"><figcaption></figcaption></figure>

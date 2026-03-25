# Bugbug Documentation

Source: https://docs.bugbug.io/llms-full.txt

---

# Documentation

Step into the BugBug documentation section, where you'll find complete resources on how to use our tool and how to start with test automation for your website.

BugBug is a modern browser-based app for software testers, developers, or product managers in need of quick & reliable *test automation*. BugBug allows you to effortlessly create and run end-to-end tests for web applications, e-commerce, landing pages, etc.&#x20;

* Are you new to the concept of automated browser tests? Read our step-by-step[ tutorial for beginners](https://docs.bugbug.io/in-depth-guides/beginners-tutorial-to-automation-testing).&#x20;
* Are you a seasoned QA engineer? Learn more about BugBug [best practices](https://docs.bugbug.io/best-practices) and advanced features such as [components](https://docs.bugbug.io/editing-tests/components), [variables](https://docs.bugbug.io/editing-tests/variables), and [waiting conditions](https://docs.bugbug.io/preventing-failed-tests/waiting-conditions).
* Are you a CEO, CTO or project manager? See our [tech leader's guide to automation testing.](https://bugbug.io/blog/guides/tech-leaders-guide-to-automation-testing/)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FgyyeRURordhyJZ479wy1%2Fbugbug-docs-illustration.png?alt=media\&token=4f84ac81-35de-4c87-93e3-726ed153520c)


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


# BugBug App FAQ

<details>

<summary>What is BugBug, and how can it help me?</summary>

[BugBug](https://bugbug.io/) is a user-friendly, codeless test automation tool that enables teams to create and run automated tests for web applications—**no programming skills required**.

With BugBug, you can perform end-to-end (E2E), regression, functional, and UI testing, among others.

It's ideal for fast-growing **startups**, **SaaS** teams, and **e-commerce** businesses, BugBug eliminates the complexity of enterprise solutions.&#x20;

BugBug is perfect for QAs, developers, and product managers looking for an efficient, hassle-free testing tool.

</details>

<details>

<summary>Do I need any technical skills to use BugBug?</summary>

No, BugBug is designed for non-technical users. With its intuitive, no-code test recorder ([BugBug Chrome extension](https://chromewebstore.google.com/detail/bugbug-automation-testing/oiedehaafceacbnnmindilfblafincjb?hl=en)), you can easily create and manage tests—no programming experience required.

</details>

<details>

<summary>What is the BugBug Chrome extension?</summary>

[The BugBug Chrome extension](https://chromewebstore.google.com/detail/bugbug-automation-testing/oiedehaafceacbnnmindilfblafincjb?hl=en) is a user-friendly **test recorder** that you can easily add to your browser to record and execute tests.

**Important!** To maintain test independence, BugBug launches each test in a fresh incognito window, ensuring a clean session free of cookies, cache, and local storage.

</details>

<details>

<summary>Can BugBug handle more complex testing scenarios?</summary>

Yes! BugBug is a simple yet powerful app, capable of testing even complex web applications.

With BugBug, you can use custom selectors, variables, and manually add advanced step types or assertions.&#x20;

You can also incorporate custom JavaScript code—giving you the flexibility to handle more demanding testing scenarios.

</details>

<details>

<summary>Do you offer unlimited users/seats?</summary>

With BugBug, you can invite **unlimited** team members to your organization for **free**, making it easy to collaborate on creating and managing test suites.

</details>

<details>

<summary>How do I record a test?</summary>

To record an automated test with BugBug, follow these steps:

1. **Install the BugBug Chrome extension:** Download and install the BugBug Chrome extension to enable test recording.
2. **Create a new test:** In the BugBug app, click the “New test” button to create a new test and enter then the URL of the web application or website you want to test.
3. **Start recording:** Click the "Start recording" button; an incognito Chrome window will open, and BugBug will automatically record your interactions, such as clicks and form inputs.
4. **Perform test actions:** Navigate through your application, performing the actions you want to include in the test. BugBug captures each step.
5. **Finish and save:** Once you've completed the desired actions, click the "Finish and close" button in the recorder menu to save your test.

For more detailed guidance, refer to BugBug's[ Beginners tutorial to automation testing](https://docs.bugbug.io/in-depth-guides/beginners-tutorial-to-automation-testing) or watch the [demo video](https://bugbug.io/demo/).

</details>

<details>

<summary>How do I run a test?</summary>

To run an automated test with BugBug, follow these steps:

1. **Execute the test run:** Once you’ve recorded your test, click the “Run” button from the level of the recorded test steps.
2. **Observe BugBug repeating your actions:** Don't move your mouse cursor over the running test window. Don't minimize the window, as Chrome may stop executing the test if it's not visible.
3. **Check the test run result:** If your test passed, congrats! If your test failed, don’t worry; there might be several reasons for that. [Check the most common reasons here](https://docs.bugbug.io/in-depth-guides/beginners-tutorial-to-automation-testing#does-the-test-fail-fix-it-with-record-from-here).

</details>

<details>

<summary>How do I fix a failed test?</summary>

It really depends on the type of error.&#x20;

Check [how to prepare your app for testing](https://docs.bugbug.io/best-practices) and [the most common pitfalls](https://docs.bugbug.io/best-practices#mistakes-to-avoid) .

Check other ways to troubleshoot your test [here](https://docs.bugbug.io/troubleshooting/prohibited-behaviors).

</details>

<details>

<summary>Does BugBug support parallel test run execution?</summary>

Yes, you can run your tests [in the cloud](https://docs.bugbug.io/running-tests/in-cloud-on-server) *in parallel*, which means that more than one test will be executed at the same time.&#x20;

You can purchase parallel runs on the **PRO** and **BUSINESS** plans—either directly in the BugBug app or when selecting your plan.

Simply go to the **Subscription tab**, choose the number of parallel runs you need, and proceed to checkout.

Each additional parallel run costs **$80/month** for users on a monthly subscription.

If you're on an annual plan, you’ll receive a **15% discount** on this price.

</details>

<details>

<summary>How do I generate a test run report?</summary>

1. Go to `Runs History`
2. Switch to the `Suites` tab
3. Select a test suite.&#x20;
4. Click `Download PDF Report` button to generate and download the report.

**Learn more** about suite run reports [here](https://docs.bugbug.io/debugging-tests/runs-history#download-a-suite-run-report).

</details>

<details>

<summary>Can I export test results (PDF/CSV/JUnit XML)?</summary>

Yes.

* **PDF + JUnit XML:** Available as [Standard reports](https://docs.bugbug.io/organizing-tests/reporting/standard-reports) (downloadable from Runs history) in the PRO plan.
* **CSV:** Available via [Advanced reports](https://docs.bugbug.io/organizing-tests/reporting/advanced-reports) (includes CSV/JSON/ZIP + detailed PDF with step screenshots) and is limited to the BUSINESS plan.

</details>

<details>

<summary>Can I add my own JavaScript code in a test run?</summary>

Yes, adding a step with any JavaScript code as part of a test run is possible.

**Read more** about [custom JavaScript actions here](https://docs.bugbug.io/editing-tests/custom-javascript-actions).

</details>

<details>

<summary>Can recorded test runs be exported as code?</summary>

Not right now, but we're planning to add this feature soon.

</details>

<details>

<summary>Can I run BugBug tests in CI/CD pipelines?</summary>

Yes, you can integrate BugBug with your CI/CD build pipelines, such as Github, Gitlab, Travis, Jenkins, or Bitbucket, via Command Line Interface (CLI) or BugBug's public API.

</details>

<details>

<summary>Does BugBug integrate with other tools we use?</summary>

Yes, BugBug seamlessly integrates with popular tools like Slack, Zapier, GitHub, GitLab, Bitbucket, JIRA, and Trello, making your workflow more efficient.

**Learn more** about BugBug's [integrations](https://docs.bugbug.io/integrations/api).

</details>

<details>

<summary>Do you support testing native applications for Windows, iOS or Android?</summary>

No, BugBug is specifically designed for **testing web applications**. At this moment, we do not support testing native mobile or desktop applications.

</details>

<details>

<summary>Which browsers are compatible with BugBug?</summary>

BugBug supports all **Chromium-based** browsers, including Google Chrome, Edge, Opera, and Brave.&#x20;

We don't support Firefox or Safari. This is a conscious trade-off. We are dedicated to providing the best-in-class experience of creating and running tests, and Chrome is the most popular browser with the best API to achieve that.

</details>

<details>

<summary>Where is customer data hosted (EU/US)?</summary>

BugBug’s primary infrastructure is hosted in the EU specifically, BugBug's servers are located in Gdańsk, Poland.

</details>

<details>

<summary>How is data from recorded test runs stored?</summary>

The data used in test runs is securely recorded in our database and stored in the **IQ cloud** (Poland -[ https://www.iq.pl/data-center](https://www.iq.pl/data-center)).&#x20;

**Important!** Access to the database is **strictly limited** to the BugBug application infrastructure. We take every precaution to prevent data leaks.

</details>

<details>

<summary>How secure is BugBug?</summary>

We've put a lot of effort into securing BugBug. Most of our team have experience in security or compliance. Even the CEO has a security background.

* We built BugBug with the best software practices (SSL, encrypted passwords).
* We do security audits yearly, with a top security researcher (who is a shareholder of BugBug, by the way).
* BugBug uses physical infrastructure with Proxmox virtualization, giving us extra secure containerization.
* Our servers are located in Gdansk (Poland - <https://www.iq.pl/data-center>).
* Tests in the cloud are run separately from each other, which significantly reduces the risks.
* We have an internal policy with different roles for our employees. Only the IT department has access to the customers' data.&#x20;

</details>

<details>

<summary>Is a standalone version of BugBug available?</summary>

Currently, BugBug is only available as a cloud-based Software as a Service (SaaS), meaning it cannot be installed on-premises or on a local network. However, we plan to introduce this option in the future.&#x20;

</details>

<details>

<summary>Is it possible to make a request to the external API?</summary>

Yes, it is possible to make a request to the external API and check the result as a part of a test run when you use your own JavaScript code, such as &#x61;**`fetch()`** function.

</details>

<details>

<summary>What kind of support is available if I encounter issues?</summary>

BugBug provides fast and reliable support via email. Need assistance? Contact our Customer Support team at <info@bugbug.io> or use [contact form](https://bugbug.io/contact/).

</details>

<details>

<summary>Where can I find tutorials or guides to help me learn BugBug?</summary>

BugBug provides comprehensive [documentation](https://docs.bugbug.io/) and [in-depth guides](https://docs.bugbug.io/best-practices), including a beginner's tutorial to automation testing.

**Tip!** Watch the full BugBug demo video [here](https://bugbug.io/demo/).

</details>


# What is test automation?

Learn what is test automation. BugBug allows you to create test automation faster and maintain it without the hassle or coding.

{% hint style="success" %}
[Read how to prepare your app for automated testing and avoid common pitfalls.](https://docs.bugbug.io/best-practices#how-to-prepare-your-app-for-testing)
{% endhint %}

### Testing doesn't need to be manual

Without automated tests, you need to manually click on your website and check if everything works correctly. Automated tests do it for you - the tests execute instructions and click on the website for you. If you want to learn the basic concepts of test automation with step-by-step screenshots, check out our [**tutorial for beginners -->**](https://docs.bugbug.io/in-depth-guides/beginners-tutorial-to-automation-testing)

### Automate your repetitive testing

Test automation is the process of creating a set of instructions that are automatically executed in the browser. You just click "Run the test" and **the browser simulates user clicks and keyboard typing for you** so that you can do a more important job.&#x20;

There's a challenge to it! Computers are not intelligent and until now required super detailed scripts that required coding skills and dedicated QA engineers to maintain the tests. BugBug's mission is to change it and allow you to create robust automated browser tests without coding.

{% hint style="info" %}
Automatic tests that simulate user interactions are often [**End-to-end tests**](https://bugbug.io/blog/software-testing/what-is-end-to-end-testing/) or [**Functional tests**](https://bugbug.io/blog/software-testing/what-is-functional-testing-types-and-examples/)
{% endhint %}

### Effortless test automation with BugBug

BugBug allows you to create your test automation faster and maintain it without the hassle and without coding. And you can [start for free!](https://docs.bugbug.io/quick-start/start-for-free)


# Start for free

Start your test automation for free with BugBug. Sign up for a free plan with unlimited local test runs and try our advanced features for 14 days.

## **Quick and hassle-free setup**

* BugBug set-up takes only a few minutes
* It doesn't require any engineering skills, you just need a basic knowledge of HTML
* You can try BugBug for free, no credit card is required
* The free 14-day trial will start automatically and give you access to premium features right away
* After the trial ends you can stay on a free plan or start a subscription - see [pricing](https://bugbug.io/pricing/)

## Sign up

You have few options to [sign up](https://app.bugbug.io/sign-up/)&#x20;

* with your email address
* with GitHub account
* with your Google account.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUcsNfJDZRyZK4hOLRPyu%2FScreenshot%202022-04-12%20at%2011.45.34.png?alt=media\&token=769a9250-5341-4b8a-a34c-a03a117ed0c2)

After registration go to your email inbox and confirm your BugBug account

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F5BIoFTNrpcC3dLx04VQC%2FScreenshot%202022-04-12%20at%2011.47.37.png?alt=media\&token=a7fd4de6-6622-453d-933c-6b9cd18cc9c4)

Once you confirm your account you can fill in your profile information or you can skip this step.

<br>

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FAOyC6rJsCj8iX3bf0gQH%2FScreenshot%202022-04-12%20at%2011.47.52.png?alt=media\&token=0599f41f-83c5-4c08-bf3c-f3c52472682f)

## Set up your organization

You can invite others to collaborate on your tests - to do this you need to choose your organization name. You can change it anytime later in Organization Settings.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FzHxAleixSs0jlbmjUthv%2FScreenshot%202022-04-12%20at%2011.47.59.png?alt=media\&token=721b5325-480b-4e36-a7d4-0dacc46b25a6)

###


# Create your first project

You have logged in to BugBug and let's take a ride! Create your first project to organize your automated tests and suites.

## What is a project?

* Use projects to organize your tests and suites
* Each project has separate independent project settings
* Everyone in your organization can access all projects

**How to name a project?** Usually, project name is the same as the name of the app or a website that you want to test. For example if you want to test the ticket reservation system of `ExampleAirlines.com` name your project "Example Airlines"

**How many projects should I have?** If you work on one product only, you probably only need one project. Add more projects if you work for several clients, different products or very complex products that require splitting for multiple setups.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F4FjVuL3YSe7f7UOqgvEk%2FScreenshot%202022-04-07%20at%2013.00.47.png?alt=media\&token=4fbc6758-36b1-45e3-a25c-8a99e96316f7)

## Create a new project

1. Click the BugBug logo in the top-left to see the list of projects
2. Click `New Project` button.
3. Enter the name of a new project. Usually, this is just the name of your product brand.
4. Enter the URL of the product you are about to test.
5. Submit by clicking the `Create project` button.

## Check out the Example Project

You can also learn about BugBug features by exploring the Example Project, that is immediately available after you register your new account.

The example project shows a couple of simple tests on a fake registration page. After you see these simple examples, learn more about [testing registration & login with variables](https://docs.bugbug.io/editing-tests/variables#test-user-registration-and-login-using-variables).

**Where is the example project?**

1. Click the BugBug logo to see the list of projects
2. Click `Example Project`
3. You can see or modify existing test cases or start your own test

##


# Install Chrome extension

Run and record your tests with BugBug Chrome Extension in incognito mode. See how easy is the process of setting up BugBug for your test automation.

### Why do you need the extension?

To run and record the tests, BugBug requires you to install a BugBug Chrome Extension and enable it in Incognito mode.

### Why does the extension require incognito mode?

All your tests should be independent of each other. Every test should begin with a **clean session, without any cookies, cache, localStorage, etc.** To achieve this BugBug runs the tests in incognito mode. Every time you run the test, the previous incognito session is closed and a new incognito window opens, with a completely clean session.

### Install the extension

Go to [BugBug Extension on the Chrome Webstore](https://chrome.google.com/webstore/detail/bugbug-no-code-test-autom/oiedehaafceacbnnmindilfblafincjb/related) and install it.

![If you try to run or record the test without the extension you will see a prompt](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fkwl3iaM0fzv5Ji7v1QrA%2FScreenshot%202022-04-07%20at%2014.48.24.png?alt=media\&token=3072bb20-8367-4d44-aeb4-61cb7fbabcdb)

![https://chrome.google.com/webstore/detail/bugbug-no-code-test-autom/oiedehaafceacbnnmindilfblafincjb/related](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FALDLrppRVkKuaNoMXf9g%2FScreenshot%202022-04-07%20at%2014.48.34.png?alt=media\&token=7a5e071b-b25f-4ea0-9844-25ba46b385ed)

### Enable the extension in incognito mode

![If you don't enable the extension in incognito mode, you will ba asked to do so before running a test](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F6eLSsZYC9RKvB0NlhN7r%2FScreenshot%202022-04-07%20at%2014.49.06.png?alt=media\&token=019b459b-b55f-49f3-960d-4b93e5aab030)

1. Go to extension settings by clicking the "Go to extension settings" button or use the link below

`chrome://extensions/?id=oiedehaafceacbnnmindilfblafincjb`

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FDTMw0qB0RKMgqGjqJEz9%2FScreenshot%202022-04-07%20at%2014.57.41.png?alt=media\&token=f09bfd21-70d9-4715-aac6-039905eb1315)

2\. Scroll down, then enable the switch near "Allow in Incognito"

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FZKqLbTNOhoxAyEdhJ8KL%2Fimage.png?alt=media\&token=b8baca1f-2fbb-4e56-adcf-219e5cc1d02a)

**That's it! You're ready to run and record the tests now.**

***

#### \[Opera Only] Allow access to search page results

The BugBug extension requires the 'Allow access to search page results' permission to function properly in Opera. When this option is disabled, Opera blocks access to sandboxed iframes, such as reCAPTCHA. Therefore, attaching to tabs containing these types of frames is not allowed.

{% hint style="info" %}
We take your privacy seriously. This permission is used solely for recording and running tests.\
We never collect, store, or share your search queries or personal data.
{% endhint %}

1. Go to extension settings by clicking the "Go to extension settings" button or use the link below

   `chrome://extensions/?id=oiedehaafceacbnnmindilfblafincjb`&#x20;
2. Scroll down, then enable the switch near "Allow access to search page results"

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FbYjT9lCWPJTdlEHbIypj%2Fbugbug-incognito-enable-screen%20-%20opera%2004.11.2025.png?alt=media&#x26;token=3090b95e-d8be-4c19-877d-465ac58f94ed" alt=""><figcaption></figcaption></figure>


# Create and run the tests

Learn the process of creating and running your tests with BugBug. Create, run, edit and maintain the growing number and complexity of your tests.

BugBug covers all the basic flow of the testing process. You can easily create, run, edit and maintain the growing number and complexity of your tests.&#x20;

1. [Creating tests](https://docs.bugbug.io/creating-tests)
2. [Recording test steps](https://docs.bugbug.io/recording-tests-steps) - step-by-step instructions of actions like clicking, keyboard typing, hovers, etc.
3. [Editing test steps](https://docs.bugbug.io/editing-tests) manually if you want to make the tests easier to maintain
4. [Running the tests](https://docs.bugbug.io/running-tests/running-tests) to see if they passed or failed
5. Fixing randomly failed tests by [re-recording steps](https://docs.bugbug.io/recording-tests-steps/re-recording-steps)
6. Monitoring your web app by [running the tests in the cloud](https://docs.bugbug.io/running-tests/in-cloud-on-server) on a [schedule](https://docs.bugbug.io/running-tests/schedules)
7. Preventing failed tests with [unique features that minimize irrelevant tests failures](https://docs.bugbug.io/preventing-failed-tests)
8. Organizing tests in [suites](https://docs.bugbug.io/organizing-tests/suites)
9. [Debugging tests](https://docs.bugbug.io/debugging-tests)

Using BugBug is **faster than traditional coding solutions, yet it offers a similar amount of control over the tests.**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FYwWJSmVIPDFQvVsZc3T2%2Fbugbug-guide-03.png?alt=media&#x26;token=0fb22369-96b1-42f0-8040-03b06cb90de7" alt=""><figcaption></figcaption></figure>

**Also read our** [**guide for beginners**](https://docs.bugbug.io/in-depth-guides/beginners-tutorial-to-automation-testing)**:**

{% content-ref url="../in-depth-guides/beginners-tutorial-to-automation-testing" %}
[beginners-tutorial-to-automation-testing](https://docs.bugbug.io/in-depth-guides/beginners-tutorial-to-automation-testing)
{% endcontent-ref %}


# Your first test

Learn the basics of creating your first automated test with BugBug. The process is very simple and doesn't require any coding knowledge. See how easy it is to run your first test.

## Learn the basics

If you're new to test automation, see our "[**how to" guide -->**](https://docs.bugbug.io/in-depth-guides/beginners-tutorial-to-automation-testing)

{% hint style="success" %}
[Read how to prepare your app for automated testing and avoid common pitfalls.](https://docs.bugbug.io/best-practices#how-to-prepare-your-app-for-testing)
{% endhint %}

## Create your first test

1. Think upfront of what do you want to test - choose a one simple use case
2. Create a new test
3. Enter the URL of the web app or website that you want to test
4. Click "Record" - if you [installed the extension](https://docs.bugbug.io/quick-start/install-chrome-extension), the incognito Chrome browser window should appear
5. Carefully click the elements to navigate - each click will be recorded automatically
6. Don't forget that [hovers are not automatically recorded](https://docs.bugbug.io/recording-tests-steps/recording-hover)
7. When you are ready with the test case click the `Finish and close` button in the [overlay menu](https://docs.bugbug.io/recording-tests-steps/bugbug-test-recorder) on the right
8. Now run the test to see if everything was correctly recorded

{% hint style="danger" %}
**Hovers are not automatically recorded!** You need to [record in hover mode](https://docs.bugbug.io/recording-tests-steps/recording-hover) by activating it in the [recording overlay](https://docs.bugbug.io/recording-tests-steps/bugbug-test-recorder).
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSVabXzKBYBD13XBpARXb%2FZrzut%20ekranu%202023-03-15%20111506.png?alt=media&#x26;token=666c3f5f-1460-4356-ab3a-876d472f812b" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FBqslGIjETFsBom7hUYzM%2Fbugbug-guide-03.png?alt=media&#x26;token=615cce9b-0b80-4f8b-a8a8-e45408e80b50" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FDeGHovPyw9Qrv7z34cpS%2Fbugbug-guide-05.png?alt=media&#x26;token=41721452-19c2-4783-899e-a7df658e1871" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fa5JQwTklQleOtHB4KEy0%2Fbugbug-guide-11.png?alt=media&#x26;token=60d8e1cb-5be5-4e95-acdb-498ec187f837" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
BugBug recording does not support multiple browser window testing. You can only record in one window, but we support multiple tabs and user movement between them.
{% endhint %}

## Manually reviewing and adding steps after the recording

You don't need to use recording, you can also create your tests step by step by adding particular actions and their parameters. This is however much slower!&#x20;

You can [manually edit steps](https://docs.bugbug.io/editing-tests/manually-creating-the-test) anywhere in your test by clicking the plus symbol between the rows.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhCzAvhQrc6DallYjtFxs%2FScreenshot%202022-04-07%20at%2016.41.49.png?alt=media\&token=90844dd1-fe78-47a6-b6d2-b1239234ec97)

You can modify the particular step when some element is not correctly caught by the BugBug's recording. Edit, run the test again, and check if it is working!&#x20;


# Independent tests

Learn why independent tests are crucial for end-to-end testing process. A good practice in automation testing is that every test is completely independent of other tests.

## Why create atomic, independent tests?

A good practice in automation testing is that every test is completely independent of other tests.

**Atomic tests:**

* do not rely on their order&#x20;
* have no dependencies between them, no shared variables
* do not require any additional manual preparation
* they are small, they should verify just one feature

**Benefits of independent end-to-end test cases:**

* Easier debugging
* Can be run in[ parallel](https://docs.bugbug.io/running-tests/parallel-mode)
* Easier team collaboration

## Can I order tests?

Ordering tests it's not recommended practice, because end-to-end tests should be atomic (see [above](#why-create-atomic-independent-tests)).

**Example test case:** \
[register a new user](https://docs.bugbug.io/editing-tests/variables#test-user-registration-and-login-using-variables) --> login to an admin panel --> check if the user exists --> delete the user&#x20;

You might be tempted to create one test for user registration and one for checking if the user is created. **But all of these steps should be in one test only.** You can't split it because one of the tests would need to wait until the first is finished. You won't be able to run the second test without running the first one, it will just lead to problems and so-called *spaghetti* between the tests.&#x20;

Solution: simply create a single test with all of these steps, no dependencies, no problems :smile:

That's why BugBug doesn't allow you to order tests and combine them or create separate "before & after" steps, even in a [test suite](https://docs.bugbug.io/organizing-tests/suites). It's better to [duplicate the tests](https://docs.bugbug.io/creating-tests/duplicating-tests) and use [components to share steps between tests](https://docs.bugbug.io/editing-tests/components).

Here's an e


# Duplicating tests

See how to duplicate your tests with BugBug without a need to create them from scratch.

You don't need to create tests from scratch. You can duplicate them and then edit them. You can also use "[New test from here](https://docs.bugbug.io/creating-tests/new-test-from-here)". This will keep all the shared [components](https://docs.bugbug.io/editing-tests/components).

You can duplicate tests

* from the tests list
* from the test details, when editing a test

![Duplicate from the tests list](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F9ElCY6D9mb8bpNzLpOgD%2FScreenshot%202022-04-07%20at%2016.50.17.png?alt=media\&token=74d8fb79-7785-4b47-ab89-c0ec4035f613)

&#x20;

![Duplicate from test details](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FdRmNtJJEg3zKpCVZiipz%2FScreenshot%202022-04-07%20at%2016.43.30.png?alt=media\&token=29fa5b33-3ddd-444c-bf18-592ee98f537f)


# New test from here

See how to avoid recording the same test steps multiple times. With BugBug you can duplicate them so that only part of the steps is copied over.

To avoid recording the same test steps multiple times you can duplicate them so that only part of the steps is copied over.&#x20;

This is useful if you want to test different variants of the same user flow or if you want to reuse your previously recorded [components](https://docs.bugbug.io/editing-tests/components).

{% hint style="info" %}
**Important!** "New test from here" action is not available between individual steps of a group. Use it before or after a group, so between the groups.&#x20;
{% endhint %}

See the image below - all the groups below the purple line will be removed in the newly duplicated test.&#x20;

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0F41y9SC5VxumIDYhDBJ%2FScreenshot%202022-04-07%20at%2017.11.41.png?alt=media\&token=d18c2319-967e-4bdf-bfd1-c75564b64f0b)


# BugBug test recorder

Learn how BugBug overlay works while recording your test. Record all clicks, catch selecting form elements, navigate to URLs and record typing in the text fields.

When you run a test in the recording mode, you can notice that there is an additional BugBug action panel on the right.&#x20;

{% hint style="info" %}
To run or record the tests, you need to install[ BugBug Chrome extension](https://docs.bugbug.io/quick-start/install-chrome-extension).
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXWm8rOp8gtAq3Ml0140l%2Fimage.png?alt=media&#x26;token=5bfd68bf-0884-46c0-ba6e-104a44c8aa16" alt=""><figcaption><p>BugBug test recorder</p></figcaption></figure>

By default, BugBug is [recording all clicks](https://docs.bugbug.io/recording-tests-steps/recording-clicks), but also it catches selecting form elements and navigating to URLs, and [typing in the text fields](https://docs.bugbug.io/recording-tests-steps/recording-keyboard-typing).&#x20;

Use the recorder's buttons to change what you want to:

* [record hover](https://docs.bugbug.io/recording-tests-steps/recording-hover)
* [add assertions during recording](https://docs.bugbug.io/recording-tests-steps/recording-assertions)
* [record drag & drop](https://docs.bugbug.io/recording-tests-steps/recording-drag-and-drop)


# Recording clicks

See how recording clicks work. By default, when you record a test, BugBug records all your clicks. You don't need to activate any recording mode.

By default, when you record a test, BugBug records all your clicks. You don't need to activate any recording mode.

When hovering over an item you will see a subtle border - this helps you to see which element you're about to click.

Clicking in the form elements is also automatically recorded, selecting radio buttons, checkboxes, and select options.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FWGT8qU3XRjbagiFq7KZU%2Fimage.png?alt=media&#x26;token=fd49763b-10f8-4f52-94e8-d6e1302078f9" alt=""><figcaption><p>Border around element pointed by mouse coursor</p></figcaption></figure>


# Recording hover

BugBug won't record hover events automatically. There is no reliable way of automatically detecting that something changed on the page because of cursor movement.

BugBug will not record hover (mouseover) events automatically. There is no reliable way of automatically detecting that something changed on the page because of cursor movement. You need to record a specific instruction that you want to hover an element.&#x20;

1. During the recording, click "Hover" in the [recording overlay](https://docs.bugbug.io/recording-tests-steps/bugbug-test-recorder).
2. Click the element that you want to hover.
3. Click "Exit hover mode".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FT729X9RW9geVJAA7mD7h%2Fimage.png?alt=media&#x26;token=8f6b733e-0b80-489f-a12d-9fac852df904" alt=""><figcaption><p>To record mouseover steps you have to use Add hover</p></figcaption></figure>

{% hint style="info" %}
**Tip!** When you are in the hover mode, the elements are highlighted with a yellow color.
{% endhint %}


# Recording keyboard typing

See how to record keyboard typing with BugBug. During the recording, BugBug will automatically record everything you type in the text fields. You don't need to activate anything.

During the recording, BugBug will automatically record everything you type in the text fields. You don't need to activate anything.&#x20;

You can later [edit the recorded text manually](https://docs.bugbug.io/editing-tests/manually-creating-the-test) if needed. Typing is reflected by `Type text` type of action.

{% hint style="info" %}
**Did you know?** When running a test, BugBug will simulate every keystroke, as if the user was really typing the text letter by letter. Learn more about [running tests](https://docs.bugbug.io/running-tests).
{% endhint %}

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0mxpYI4S2dpupTUSZr23%2Fimage.png?alt=media\&token=2e8f2c70-096e-4c1f-a610-125ca34341b7)


# Recording assertions

Learn what an assertion is and how to use it during recording your test with BugBug. Use assertions to check if your page behaves as it should, without interacting with it.

## What is an assertion?

You assert that some condition is met, and if it isn't, the test should fail.

## How to record an assertion?

You can add more advanced assertions manually - learn more about [assertions and their types](https://docs.bugbug.io/editing-tests/assertions).

1. Start [recording test steps](https://docs.bugbug.io/recording-tests-steps)
2. Click `Add assert`
3. Click the element that you want to check: every time the test is run BugBug will check if this element contains the same text or is visible on the page

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FajwinFAOINHq2qLaqh0d%2F1_addAssert.png?alt=media&#x26;token=9f838c72-6f8c-4a26-ba67-18baf68696a7" alt=""><figcaption><p>Add assert option on the recorder</p></figcaption></figure>

You can also enable the "**Add multiple**" toggle, to select various elements on the page at once. Such as checking if all the elements are in place in the main navigation menu.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FlmJqxbYigDroO4eiU9In%2F2_addAssert.png?alt=media&#x26;token=c551943d-dec9-42a8-a5d3-5c3592d00a4b" alt=""><figcaption><p>"Add multiple" toggle disabled</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FTnK4M4NPuk9V9MWlOfsm%2F3_addMultipleAssertions.png?alt=media&#x26;token=c1b451de-692a-47f3-be3d-d3ec160d9bd7" alt=""><figcaption><p>"Add multiple" toggle enabled</p></figcaption></figure>


# Recording drag & drop

{% hint style="warning" %}
**Coming soon!** We are working hard to add support for recording of drag & drop soon.
{% endhint %}


# Record from here

Read about Record from here feature. BugBug allows you to start recording from any step in your test. No need to record from scratch every time.

You do not need to record from scratch every time! Need that in the middle of an existing test? No problem!  ✨

You can start recording from any step in an existing test. Go to the test details and:

1. Hover on a step you want to record from
2. Click `+` icon
3. Click `Record from here` option
4. The recording window will open, and the test will run until the given step
5. The recording mode will activate, and you can continue recording new steps *from here*

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F66hD3gpAmNOPw3Ct9WQm%2Fimage.png?alt=media&#x26;token=1baa7490-b41d-4e8c-b45a-f8b4bd427084" alt=""><figcaption><p>Click "Record from here" to execute test to a given position and enable recording mode</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FPznSvOTHxbfFbTCOCNbG%2Fimage.png?alt=media&#x26;token=d9ed6909-d478-4738-8518-c6a177ef7235" alt=""><figcaption><p>Recording mode in the webapp UI</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F76vVIgu52DUmOaCYYmO5%2Fimage.png?alt=media&#x26;token=c742700a-4b16-4e50-bb8d-264d5aa57794" alt=""><figcaption><p>Recording mode is activated in the browser window with a test</p></figcaption></figure>

All newly recorded steps will be automatically added to a test without any extra confirmation and will have a `NEW` badge, as shown in the screenshot below.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F18ElPmvagA5KNQh0Bdxo%2Fimage.png?alt=media&#x26;token=58cd147b-19d9-4d99-bef0-c22f4512ba85" alt=""><figcaption><p>Newly recorded steps with the NEW badge</p></figcaption></figure>

### Changing the recording position

BugBug also allows you to **change the current recording position**. To do this, drag & drop the recording position from the web app UI.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F6MFAetDBQQVGX0wkRtuT%2Fimage.png?alt=media&#x26;token=d4604616-b53d-4069-afed-7e02041d48e0" alt=""><figcaption><p>Movable recoding position</p></figcaption></figure>

This feature lets you record new steps in multiple test positions within a single recording session. If you want to pause the recording to set your application state manually and continue recording again, you can do this by clicking `Pause` button, and then you can continue recording by clicking the `Record` button.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FESPhRQH0JE5RDxLmI24O%2Fimage.png?alt=media&#x26;token=f8f499c5-61eb-4904-8cf5-a773497edc6f" alt=""><figcaption><p>You can pause recording and enable it again by clicking Record button</p></figcaption></figure>

You can also continue recording from the current end of a test case - just click the button `Record from here` at the end of a test. Newly recorded steps will appear in the new group.&#x20;

![Record from here at the end of the test](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCjPDyELf1ndYx9FEShn5%2Fimage.png?alt=media\&token=94c2f16c-a62b-4a16-9c1f-a0d81052f004)

### Resume execution after recording new steps

BugBug allows you to resume executing the test after recording without starting the test from the beginning. This awesome feature significantly reduces the time spent on fixing the test.

The common scenario looks like this:

* Record new steps inside the test
* Pause recording
* Change playback position before newly recorded steps
* Resume a test

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FPZlWg0dicbXhP8KL0gEy%2Fimage.png?alt=media&#x26;token=1d13dcd2-d57d-4c17-9a3a-1979d763f2a7" alt=""><figcaption><p>Change playback position and click Resume button to execute newly recorded steps</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fyhw7dDH519WMxv5kTJ3T%2Fimage.png?alt=media&#x26;token=abc95091-49d4-41f9-b215-4b9ba1a29890" alt=""><figcaption><p>You can resume execution from BugBug overlay</p></figcaption></figure>

You can repeat the record and replay sequence as many times as you like. Enjoy BugBug's flexibility!

{% hint style="info" %}
We also recommend reading about [edit-and-rewind](https://docs.bugbug.io/workflow-tips/edit-and-rewind "mention") feature that explains more about how to fix broken tests easily.
{% endhint %}


# Re-recording steps

See how easy it is to re-record test steps with BugBug. If your test failed and you need to fix it, it's way faster to record the steps "from here" rather than edit them manually.

If your test failed and you need to fix it, it's faster to [record the steps "from here"](https://docs.bugbug.io/recording-tests-steps/record-from-here) rather than [edit them manually](https://docs.bugbug.io/editing-tests/manually-creating-the-test).

1. Find the step that failed
2. Delete it
3. Record from here
4. Record a new step(s)
5. Stop recording

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fs3g3bXrrCOWExULhfDzc%2FScreenshot%202022-04-11%20at%2016.37.06.png?alt=media\&token=9399cd05-8fb3-4628-addf-a369fc905459)

New recorded steps will have the `NEW` badge. BugBug allows you to record & execute recorded steps in the same session using [edit-and-rewind](https://docs.bugbug.io/workflow-tips/edit-and-rewind "mention") feature.


# Recording pop-up window actions

## Problem statement

Currently, you can record actions on pop-up windows both during the recording process and while running tests.

This is especially helpful in scenarios where, for example, the user logs in to his or her account using authorization from an external third-party service - e.g. *Google authentication* or similar.

### How does it work?

To put it simply, BugBug forces the opening of a pop-up window in a new browser tab and changes the context for it, e.g. in the scenario of logging in with an external account *(e.g. Google auth.)*,  and after correct authorization, the browser tab is automatically closed as if it had happened with a pop-up window.<br>

{% hint style="info" %}
As an example, we used the Podio page.
{% endhint %}

#### **Regular view:**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0VpGf83sBn9iOgW3uRBK%2FRegular_popup_window.png?alt=media&#x26;token=e09688b6-ef71-4b1c-97b0-17a0977443ee" alt=""><figcaption><p>Regular pop-up window</p></figcaption></figure>

####

#### While recording the same step/flow in BugBug:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FN3i0ZYCd8vG2dfnDtqlJ%2FRecording_popup_1.png?alt=media&#x26;token=74e0f1e7-29ca-478c-a54b-c16d5f616b57" alt=""><figcaption><p>The tab pop-up doesn't appear yet</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fd0x20l86EZgcfpbL81lP%2FRecording_popup_2.png?alt=media&#x26;token=f17a642c-3633-4e0f-b2b3-d212db9c9623" alt=""><figcaption><p>The pop-up opens in a new browser tab</p></figcaption></figure>

## Recording a test with pop-up window handling

1. Create a new test (or edit an existing one)
2. Start recording new steps&#x20;
3. Record a click action on a button/element that opens a new popup window. Instead of a new pop-up, the page will open in a new browser tab, and the context will automatically switch to that tab as the active tab
4. Perform all actions on this tab, i.e. provide login details and complete the whole flow. Based on the login flow using an external 3rd party account (e.g. Google account), the tab will be automatically closed when it is completed - just as it would be in a pop-up window, and all actions will be recorded.&#x20;
5. When you automatically switch to the currently active tab, you can continue to record actions on that tab


# Using keyboard shortcuts

## Overview

To make it easier to work around the recording action, we have added keyboard shortcuts that can be used during test recording. This should make it easier to switch between different options within the BugBug test ecorder.

{% hint style="info" %}
Generally, the shortcut *number* represents the button position for each option.
{% endhint %}

![BugBug Recorder](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FS0LGULMgJXdZ4wkH8t65%2Fimage.png?alt=media\&token=345ec1dc-325d-431c-b5ad-bafedfec6265)<br>

## Possible uses and combinations of keyboard shortcuts

{% hint style="info" %}
This description and keyboard shortcuts are based on a **Windows and Linux** operating system.

If you are using a different operating system, please note that you will need to use an appropriate related shortcut, e.g. for **MacOS** users use i.e. ***"Control + Option + ${key}"***.&#x20;

However, in BugBug Recorder we display shortcuts that are adapted to the system you are working on.
{% endhint %}

| Shortcut combination | Feature           | Comments                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ctrl + Alt + 1**   | *Add assert*      | If *"Add Assert"* mode is enabled and you use the shortcut again, it will be disabled.                                                                                                                                                                                                                                          |
| **Ctrl + Alt + 2**   | *Add hover*       | As before, using the shortcut again will disable this mode.                                                                                                                                                                                                                                                                     |
| **Ctrl + Alt + 3**   | *Inbox*           | It will show you the "*Open Inbox for a special test email address"* view with realted options.                                                                                                                                                                                                                                 |
| **Ctrl + Alt + 4**   | *Variables*       | It will show you the "*Variables"* view with realted options.                                                                                                                                                                                                                                                                   |
| **Ctrl + Alt + 5**   | *Pause recording* | <p>This will bring up the "<em>Pause recording"</em> view with its associated options.<br><br>While you are in this view, you can alternatively use two other shortcuts:<br>\* <strong>Ctrl + Alt + 1</strong> to resume recording<br>\* <strong>Ctrl + Alt + 2</strong> that will finish and close your recording session.</p> |
| **Ctrl + Alt + 6**   | Finish and close  | It will end and close your recording session.                                                                                                                                                                                                                                                                                   |

##

## Workflow tips

Some of the shortcuts are also available in the BugBug Runner view, so you can use them there as well.

Meaning:

* **Ctrl + Alt + 1** to start recording additional steps
* **Ctrl + Alt + 2** to finish the test and close the window

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FnRJTsl0cLmDmMksfP4eG%2Fimage.png?alt=media&#x26;token=4b1f1c73-76d5-4546-88b6-bc325b3f466c" alt=""><figcaption><p>BugBug Runner</p></figcaption></figure>


# Grouping steps

Learn how to group your test steps. BugBug supports "step groups" to make sure you can easily navigate in large projects. Very useful feature if you work on a large amount of test cases.

## Why group your steps?

If you work on a large amount of test cases and complex user flows, you need to [organize your tests](https://docs.bugbug.io/organizing-tests) and keep your project nice and tidy.&#x20;

Use "step groups" to make sure you can easily navigate in large projects. Most importantly **you need to use groups to use** [**components**](https://docs.bugbug.io/editing-tests/components)**.**

{% hint style="info" %}
**Important! All steps are always inside a group**\
In BugBug all your steps are always in some kind of a group. By default when you record a test, all your steps will be in just one "Unnamed group" that you can later split into more groups.&#x20;
{% endhint %}

## Creating a group

The most productive way is to use "Split group here" action.&#x20;

1. Move your mouse between the step rows
2. Click the "plus" icon
3. Click "Split here"
4. Name the group

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUNrwsakVHrH2jbpQlAZC%2Fsplit-group-here.png?alt=media\&token=bfe1fa8f-6b4e-48fd-b3bc-d034de8b7c83)

**Result:** you will get 2 new groups. The first one keeps the old name. You can immediately rename the new group.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNxgUS7tpQl6Qtw3iS14z%2Fgroup-edit-name.png?alt=media\&token=4355b8cb-c62e-42c2-b0f4-d78e3696d340)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fu5P8pdRWAS3iyInE8UJo%2Fgroup-named.png?alt=media\&token=df51deb1-b0ab-425c-88d0-43a328b4c428)

You can have multiple groups in one test. Each group can be converted to [components - reusable test steps that allow you to edit multiple tests at once.](https://docs.bugbug.io/editing-tests/components)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F1JhwQ5GahZ9n9owyt3qz%2FScreenshot%202022-04-11%20at%2016.49.48.png?alt=media\&token=0afc8018-be3c-4507-9e94-433cd46a2a08)

## Renaming a group

Click the name of the group - that's it, you can edit the name. No need to click "Save" button.

## Groups vs. components

Groups are just organizing your test steps. They become powerful when you convert them to [components - a group of steps that is shared across multiple tests](https://docs.bugbug.io/editing-tests/components).


# Components

Learn about BugBug Components that can save a lot of your time when you want to work with test automation for complex products. BugBug always make the test automation process ultra-simple.

## What are components?

Components are groups of steps that are shared across multiple tests. So basically, if you don't want to repeat the most often-used steps, such as visiting the main page and logging in using valid credentials, you create a new component that will contain all those steps and use it easily, and fast across all your tests that will require this action.

## Why use components?

Once you create a new component, remember that **when you change something inside that group it will be changed in all tests where you used that group.**

**To save time!** This can save you time when you want to work with test automation for complex products. With components, you can change your test only once, instead of [re-recording the steps](https://docs.bugbug.io/recording-tests-steps/re-recording-steps) hundreds of times or manually copy-pasting them between tests.

**How many components do you need?** It's better to have more than less. It's not a problem if all your groups are components.

{% hint style="info" %}
**Example:** make a component from `click` action on your "Sign up" button. All your tests that [test user registration](https://docs.bugbug.io/variables#test-user-registration-and-login-using-variables) can now use such a component and if you change the "Sign up" button [selector](https://docs.bugbug.io/preventing-failed-tests/selectors) in the future you can do it only once.
{% endhint %}

## Where are the components?

The "Components" module can be found under the same name in the main navigation. For starters, the list is empty, but this will change as soon as new components are added.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FBV1qnkgpnr2959zTbr0z%2F1emptyScreen.png?alt=media&#x26;token=0d51c2f4-7034-4ae9-aa6c-120eb16a34fd" alt=""><figcaption><p>Components page</p></figcaption></figure>

### Components list

When new components are added, they will be displayed on the list, where those that are used in the most tests are displayed at the top.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQWUlTh6thQVuGq3g4fub%2F3listOfComponents.png?alt=media&#x26;token=79690ecb-c519-41c9-97bf-d45c86a499c0" alt=""><figcaption><p>Components list</p></figcaption></figure>

## How to make a reusable component?

Firstly you need to have a group of steps that are repeatable and useful in many tests.

1. [Group test steps](https://docs.bugbug.io/editing-tests/grouping-steps)
2. Make a component from this group

To create a component go to test view and choose the group of steps that will become your one component. Then click on the `MAKE COMPONENT` button on their group name.&#x20;

**From now on, every change you make in this component will also apply to other tests that have this component.**&#x20;

{% hint style="info" %}
**Tip:** Use "[new test from here](https://docs.bugbug.io/creating-tests/new-test-from-here)" to quickly work with tests that use components.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fglpy1G5YbYf42aVqp6dp%2F11makeComponent.png?alt=media&#x26;token=f816b890-0e6c-4b92-9230-c42d5a929b4a" alt=""><figcaption></figcaption></figure>

## Insert an existing component

You can also add an existing component to an existing test:&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkNBE3lt21AOBZ2UCD3ZS%2F11insertComponent.png?alt=media&#x26;token=1019f450-c561-4d48-ada0-72b28c5392b0" alt=""><figcaption></figcaption></figure>

This can be also done when creating a completely new test:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FG0CdalUKB3JQifHSzDJS%2F2addToNewTest.png?alt=media&#x26;token=506ee579-5e59-408c-9c3d-1e56e3811086" alt=""><figcaption><p>Insert a component to a new test</p></figcaption></figure>

You can browse all your components here and search for a specific one that you want to add:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F78jqh3Z4VCJQ9VTPeNqn%2F2addToNewTest2.png?alt=media&#x26;token=4c17f555-5abe-4765-8f5b-6c343837db48" alt=""><figcaption><p>List of existing components when adding to a new test</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FqQBdMTWbgR22PkFwCR0C%2Fimage.png?alt=media&#x26;token=745a2ffe-1036-4192-9842-0bdf46bb1b26" alt=""><figcaption><p>Inserting component</p></figcaption></figure>

## Inserting the same component multiple times

You can add the same component multiple times in a single test.&#x20;

As with components in general, a change to one instance will be reflected in the others.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FdyjW418yNpuKJ3DKmQc5%2Fimage.png?alt=media&#x26;token=6e869946-e035-4c66-b1c7-0cbf4f37cd0b" alt=""><figcaption><p>Inserting component multiple times in a single test</p></figcaption></figure>

### Parametrizing components

If you want to reuse the same component in a test multiple times but with different parameters, you can achieve that using variables and the ability to override them. A typical scenario involves reusing the login component for various roles within the same application. To do that, you have to:

1. Create a `{{login}}` [variable](https://docs.bugbug.io/editing-tests/variables) (could be empty by default).
2. Create a `{{password}}` [variable](https://docs.bugbug.io/editing-tests/variables) (could be empty by default).
3. Create a component that uses those variables to log in to the application.
4. Create a group **before** the instance of the component that you want to parametrize.
5. Override login and password variables using the `Set variable` step.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FsYo836ymmZ920Mms9xyR%2Fimage.png?alt=media&#x26;token=4328cdb8-04e8-40a7-8444-784d2772ed7d" alt=""><figcaption><p>Parametrizing components with overrided variables</p></figcaption></figure>

## Unlinking components

When you unlink a component, it will convert it to a regular group and append a "duplicate" to the group name. **This will only unlink it in this specific test!** Use it for making a small modification that is not required in any other test.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FewUsvXbKuGxdxqBSTBgu%2F4unlinkComponent.png?alt=media&#x26;token=298aa3a2-2034-4916-b0e9-dbc107884a7e" alt=""><figcaption><p>Unlink a component from a test</p></figcaption></figure>

## Splitting components

This works exactly the same as splitting a group. You will get two new components after splitting a component and you can immediately rename them. **All instances of this component in all tests will also be split.**&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FyJPEurnghYTZLs2ra4Mu%2F11splitComponent.png?alt=media&#x26;token=7961e4ee-1ed2-46a6-b6ff-c3c84ab18b5a" alt=""><figcaption></figcaption></figure>

## Removing components from a test

You can remove the component from a specific test.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FncllwjDyqgyHlW2jrIDs%2F5removeComponent.png?alt=media&#x26;token=e676760e-efe1-485c-bec5-544741f85825" alt=""><figcaption><p>Removing a component from a test</p></figcaption></figure>

* "Remove from this test" - This will only remove it from this test, but not from other tests.

{% hint style="info" %}
**Important!** When you remove the last instance of a component, it is **not** removed from your project and will still appear in the "Components" and be available through "Insert an existing component".
{% endhint %}

### Changing back the component to a regular group

You can always change your group back to being a regular one and not a component anymore, simply by clicking on the yellow label with "Component" text:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F2JLl9HCs7xkfXOqN7EjN%2F5removeComponent2.png?alt=media&#x26;token=d8216659-e06e-4a23-ac45-0e86521ca096" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important!** This won't delete the created component, so you can still preview it on the "Components" page, and use it in your tests.
{% endhint %}

## Edit components

{% hint style="warning" %}
You can edit a component in the context of a specific test. However, remember that this will affect other tests that use it.
{% endhint %}

Edit is located within the test, and there are two ways to get there - by navigating to the test via the "Tests" page, or by searching for the component in the "Components" page, and then through the list of tests that use it.

&#x20;Here on its details page click on the "**Edit component**" button:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FeiKzxeQTO6K3XC3r4b3D%2F6editComponent.png?alt=media&#x26;token=e57bb341-5bf9-4178-a2c0-f1dc65bc9ab5" alt=""><figcaption><p>Component's details page</p></figcaption></figure>

Next, click on the linked test from the list to enter the edit mode. \
\
On this screen, you will see a list of all the tests in which this component has been used, and you can choose one that best suits you when editing the component.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F2dZgvE6qs205jVKl5xSX%2F6editComponent2.png?alt=media&#x26;token=0617234e-23b5-42af-99d6-7622126b8a68" alt=""><figcaption><p>List of connected tests</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F5QTdqoRnIM6vYBFmbQRm%2F6editComponent3.png?alt=media&#x26;token=a8827803-c74c-4f94-80c7-105bdaf10259" alt=""><figcaption><p>Edit mode of a component used in a test</p></figcaption></figure>

{% hint style="info" %}
Editing a component won't be possible if it's not linked with any test. To enable editing link it first to any of your tests.
{% endhint %}

#### Preview steps that are within a component

When you are in the details of the component, you can see a preview of each step by clicking on it. This is done in the read-only view.

## Additional actions on single component

Being on the list of all components or on a view of a single component you can perform additional actions by clicking on the more menu, such as:

* **Duplicate** - This will duplicate the selected component by adding `- duplicate` prefix in its name. \
  Also, please remember that by default the duplicated item **won't** be connected to any test.<br>
* **Rename** - This will let you change the name of the selected component, which will apply to all tests that use it. Furthermore, the name must be unique.<br>
* **Show related tests** - This will show you a preview of all related tests with that component. They can be previewed by clicking on any of them in the list (which will open in a new tab). If there are a lot of them, you may also find the search box useful.<br>

  \
  This is accessible in the details of the component:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FxkjPBK1X7A5XMRkeD33c%2F33showRelatedTests3.png?alt=media&#x26;token=7ea83da5-0742-4c02-8b6c-f2a357fc445c" alt=""><figcaption><p>Show related tests</p></figcaption></figure>

Also from the "Actions" menu:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVOgUVGzB8lxeJKpeeblQ%2F7editShowRelatedTests2.png?alt=media&#x26;token=3564890e-62d4-4001-96ef-e8cc8ec02f9f" alt=""><figcaption><p>Show related tests</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fn7jhnlIGxDI8SiD8J2nF%2F7editShowRelatedTests3.png?alt=media&#x26;token=36a91c07-78c1-4ba8-bcec-d1ef1356a628" alt=""><figcaption><p>List of related tests with a component</p></figcaption></figure>

If a component isn't linked to any test, this field will be disabled:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FrEBzGhBuiPKH4HEj5rL1%2F7editShowRelatedTests.png?alt=media&#x26;token=e895caa2-d2da-4803-b8d7-0dfbdb03bd8e" alt=""><figcaption><p>No related tests with a component</p></figcaption></figure>

* **Delete** - This allows you to delete components you no longer need, to keep the list tidy. Please note that deleting a component will permanently delete all instances of that component and cannot be undone.

Yet to not do it accidentally we distinguish two scenarios.&#x20;

1. Deleting a component when **it's not** linked to any test. A confirmation modal will show up:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FjJRo2o0MKLLeN88fkOO4%2F8deleteSingleComponent.png?alt=media&#x26;token=440eb9ea-d535-41e9-b228-fcf7a6730494" alt=""><figcaption><p>Deleting a component without any connected test</p></figcaption></figure>

2. Deleting a component when **it's** linked to a test you need to additionally confirm this action by typing the safe word on the confirmation modal:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FwfM5frFPNflcO8Hey5sI%2F8deleteMultiComponent.png?alt=media&#x26;token=74f416b6-89b6-433c-9a80-c57a1af4df68" alt=""><figcaption><p>Deleting a component with multiple connected tests</p></figcaption></figure>

## Additional bulk actions on components

For now, you can select multiple components from the list on the Components page and perform bulk actions such as:

* Delete - This will delete all selected components from the list

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FpHvffbHDEhX9riqy5FNq%2F22bulkActions.png?alt=media&#x26;token=f2868a58-383a-493e-a4f1-e50f158a5d5c" alt=""><figcaption><p>Delete in bulk</p></figcaption></figure>

* Deselect all - This will remove the selection&#x20;


# Manually editing steps

BugBug allows users to manually edit test steps. Although this is not a recommended way of updating tests. It's often much faster to fix the tests by removing the failed steps and recording them again

Before you jump into manually editing, make sure you learn [how to re-record test steps](https://docs.bugbug.io/recording-tests-steps/re-recording-steps), as this is a recommended way of updating your tests. It's often much faster to fix the tests by removing the failed steps and recording them again, rather than manually updating step settings.

## Manually adding steps

You don't need to use recording, you can also create your tests step by step by adding particular actions and their parameters. You can manually add steps anywhere in your test by clicking the plus symbol between the rows.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhCzAvhQrc6DallYjtFxs%2FScreenshot%202022-04-07%20at%2016.41.49.png?alt=media\&token=90844dd1-fe78-47a6-b6d2-b1239234ec97)

## Step details panel

Make your manual changes to the tests in the step details sidebar. Here you can see all the parameters for a selected step.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FjfPQZya5QULm80XbyCFr%2Fimage.png?alt=media\&token=4ce1c722-4a79-4c49-b884-8d73e200141f)

{% hint style="info" %}
**Important!** Don't forget to save your changes after editing a step.
{% endhint %}

{% hint style="success" %}
When editing the actions don't forget that you can use [variables](https://docs.bugbug.io/editing-tests/variables).
{% endhint %}

### Operations on the test steps

* `Duplicate` step
* `Run to this place`
* `Deactivate step`
* `Delete` step

### Reordering steps

You can also `Drag to reorder` the steps within the test:

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FfjPrjvl0oFMVCdNOqSiw%2Fimage.png?alt=media\&token=765cc9e9-0cd3-4578-be9b-df8dd5d68595)

###


# Actions

Learn about Actions that you can choose while adding test steps manually. BugBug provides mouse actions, input actions, window actions and some advanced actions like running custom JavaScript.

When you [manually add steps](https://docs.bugbug.io/editing-tests/manually-creating-the-test), first you need to choose a type of step.

There are two basic types of steps:

* [Actions](#action-types-available-for-a-step)&#x20;
* [Assertions](https://docs.bugbug.io/editing-tests/assertions)

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHTnnoNv67UWK9C7RRp7B%2Fimage.png?alt=media&#x26;token=6e8b54dd-c8a2-4c17-ad11-ff175146b131" alt=""><figcaption></figcaption></figure>

## Action types available for a step

### [**Mouse actions**](#mouse-actions-details)

* [Click ](#click)
* [Double click](#double-click)
* [Right click](#right-click)
* [Hover](#hover)
* [Scroll](#scroll)
* [Drag\&Drop (BETA)](#drag-and-drop-beta)
* [Press mouse button](#press-mouse-button)
* [Release mouse button](#release-mouse-button)

### [**Input actions**](#input-actions-details)

* [Type text](#type-text)
* [Select option](#select-option)
* [Clear input](#clear-input)
* [Change value](#change-value)
* [Upload file](#upload-file)
* [Paste from clipboard](#paste-from-clipboard)

### [**Window actions**](#window-actions-details)

* [Go to URL](#go-to-url)
* [New tab](#new-tab)
* [Close tab](#close-tab)
* [Reload page](#reload-page)

### [**Advanced actions**](#advanced-actions-details)

* [Set variable](#set-variable)
* [Switch context](#switch-context)
* [Run custom JavaScript](#run-custom-javascript)
* [Answer a prompt](#answer-a-prompt)

## Actions - detailed descriptions & tips

### Mouse actions - details

#### Click

When you want to click a specific element.

This is the most common action for navigating the web. This also serves as a "tap" action if you [test mobile resolutions](https://docs.bugbug.io/workflow-tips/mobile-version-testing).

<div align="left"><figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNJ8hSuAamUD69ZhPywN4%2Fimage.png?alt=media&#x26;token=abb41b9d-20c2-4b10-97be-e42108bc0a99" alt=""><figcaption><p>Click parameters</p></figcaption></figure></div>

Parameter&#x73;*:*

* *Position (default: Smart detection)* - By default, BugBug utilizes its own mechanism to calculate the correct x,y position for clicking on the given element (selector). If you wish, you can modify this parameter and choose where to click (Top Left, Top Center, Top Right, Left, Center, Right, Bottom Left, Bottom Center, Bottom Right).&#x20;
* *Modifier keys (default: None) -* If you need to click with an extra keyboard modifier, it's possible to set it here (Ctrl, Shift, Alt, Meta / Command).

#### Double click&#x20;

When your app has a specific interaction, such as a double-click, for example, to open a file.

#### Right click

When your app has a custom context menu on right-click.

#### Hover

{% hint style="warning" %}
**Important! This action is not recorded automatically. You need to** [**enter "Hover" mode during the recording**](https://docs.bugbug.io/recording-tests-steps/recording-hover)**.**&#x20;
{% endhint %}

Examples when to use it:

* Navigation bar with menus that appear on mouseover
* Cart preview that appears  on hover
* Actions that only appear when you move your mouse over a table row&#x20;

#### Scroll

When you need to force BugBug to scroll to specific coordinates.

Usually, you don't need to add it manually, because BugBug [handles the scroll automatically](https://docs.bugbug.io/preventing-failed-tests/smart-scroll).

#### Drag\&Drop (BETA)

When your app has a slider that is interacted with by a drag-and-drop interaction.

#### Press mouse button

This action will initiate the `mouseDown` event.

You can use it in combination with "hover" and "Release mouse button" to simulate drag & drop from one element to another element.&#x20;

#### Release mouse button

Release the mouse button (`mouseUp`) on a specific element.

### Input actions - details

#### Type text

Type text into `input`, `textarea` or `contenteditable` fields. Simulates keyboard presses, entering characters one by one.

To escape text like {{ }}, you must put it between `{% raw %}` and `{% endraw %}` blocks.

Example:\
This is not a {% raw %}{{not\_a\_variable}}{% endraw %}

#### Select option

Chooses a specific option in a native HTML `select` dropdown (also called "combobox" menu).

#### Clear input

Removes all characters from a text `input` field, `textarea` or `contenteditable` .

#### Change value

Sets a value of any form element. HTML has many form controls, and some of them can be set to a specific value, for example, radio groups. Technically, a JS "change" event is triggered and the value is updated immediately, without typing letter by letter. Use it for typing longer texts.

#### Upload file

Simulates the "choose file" action in a form type `file` for uploading in forms. You can customize the file that will be uploaded.

#### Paste from clipboard

This step simulates the paste action (Ctrl+V) that the user can perform using the keyboard or mouse.

It's useful when you have "*Copy to clipboard*" actions in your app's UI and you want to use the value later in your test scenario.

### Window actions - details

#### Go to URL

Load the given page URL.

The step is marked as *passed* when the browser emits the [`onDOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onDOMContentLoaded) event.

This action doesn't verify the status of the loaded page. If the URL returns an HTTP status different than 200 (OK), for example, 404, but still loads correctly (browser emits the [`onDOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onDOMContentLoaded) event), the step will be marked as "*passed*".&#x20;

Parameters:

* *Password protected* - If your application is behind [basic auth](https://en.wikipedia.org/wiki/Basic_access_authentication), you can add those credentials by enabling this checkbox.\
  \
  ![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F3L9o5R4LQtyhja3Td4TX%2Fimage.png?alt=media\&token=7e934628-4a92-40ac-9b0e-3836b0129602)

#### New tab

Open a new tab and load the given page URL.

This step works similarly to [Go to URL](#go-to-url), but opens in a new tab.

#### Close tab

Close the current, active tab. Focus will be switched to the previous tab.

If the browser has only one active tab, the browser will be closed and the test will be stopped.

#### Reload page

Reload the page. Nothing less, nothing more.

This step is helpful if you expect that the previous step changed something in the app, but your app is not refreshing automatically (i.e., an asynchronous action).&#x20;

### Advanced actions - details

#### **Set variable**

This action can be used to store local variables from tested sources. You can use a selector to find a text value on the tested web application.\
Now you can store any text value from the tested web page in a variable and use it in feature steps. For example, to find out newly registered unique users in your CRM. This variable is also cross-domain.

{% hint style="info" %}
For more detailed information, check out "[Variables during recording](https://docs.bugbug.io/editing-tests/local-variables)".
{% endhint %}

#### **Switch context**

You can use this action for [working with iframes](https://docs.bugbug.io/editing-tests/tabs-and-iframes) or [multiple tabs](https://docs.bugbug.io/editing-tests/tabs-and-iframes).

#### Run custom JavaScript

#### **Answer a prompt**

Accept or decline browser alerts initiated by `alert()`, `confirm()` or provide a custom text answer for a browser `prompt()`.

This action is automatically [recorded](https://docs.bugbug.io/recording-tests-steps), and most of the time you don't need to edit it manually.

* To confirm the window prompt, enter `true` in the answer field.&#x20;
* To reject enter `false`.&#x20;
* For `prompt()` questions, enter a custom text that should be provided as an answer

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUTqZmjEvF703V1Gfo8ld%2FScreen%20Shot%202022-10-24%20at%2017.55.38.png?alt=media&#x26;token=2ee71d2d-3334-4a4a-873f-3be83ab1909e" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F3W3uT0EMTVp1wSNNSvYY%2FScreen%20Shot%202022-10-24%20at%2017.58.39.png?alt=media&#x26;token=8723f786-8fb4-49b4-afcc-eb96e5b7df0f" alt=""><figcaption></figcaption></figure>


# Assertions

Enhance your software testing with BugBug's Tests Assertions. Discover how to create powerful assertions to validate your test behavior. Streamline your debugging process.

## Why add assertions?

Use assertions to **observe** if everything works as it should.&#x20;

An assertion is a check that does not interact with your page, for example, you can check if your page shows a specific text without clicking anything.

{% hint style="info" %}
[Here](https://docs.bugbug.io/recording-tests-steps/recording-assertions) you can read about how to record assertions for a test.
{% endhint %}

## Types of assertions

By default, BugBug records two types of assertions:

1. `Element is visible`
2. `Element has text`

which you can edit later in your recorded test details view, and switch between a wider list of available ones, such as:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhlpH8pssBgh2cZtE2Hu0%2FAdd_a_new_assertions_step.png?alt=media&#x26;token=f1b3014c-7bfa-41f9-bf49-bebc78b77171" alt=""><figcaption><p>List of available assertions</p></figcaption></figure>

Select one of the following assertion types.

{% hint style="info" %}
We are regularly adding more assertion types to this list - please contact us if you need a new assertion type.
{% endhint %}

| Type of assertion                | What happens                                                                                                                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Element is visible               | BugBug checks if the element is actually visible on the screen, if the element is not covered or scrolled outside of the viewport                                               |
| Element is not visible           | BugBug checks if the element isn't visible on the screen                                                                                                                        |
| Element has text                 | BugBug checks if the element is visible, but also checks if it has a specific text                                                                                              |
| Form field has value             | BugBug checks if any form input has a specific value, for example, you can check if your radio buttons group is selected to "No" after the user clicks "No" button              |
| Form input is checked            | BugBug checks if the checkbox is checked. You can claim that your radio button was checked after the user clicked it                                                            |
| Form input is not checked        | BugBug checks if the checkbox is unchecked. You can claim that your radio button was disabled after the user clicked it twice                                                   |
| Page shows specific text         | BugBug checks if there is text anywhere on the page                                                                                                                             |
| Page does not show specific text | BugBug checks if there is no text anywhere on the page. Helpful with negative assertions                                                                                        |
| Page has title                   | BugBug checks the document.title                                                                                                                                                |
| URL address                      | BugBug checks the URL of the page. You can verify that the redirect works fine                                                                                                  |
| Download started                 | BugBug checks if the download process for a selected file has started within the browser *(however, there is no verification that the download has been successful)*            |
| Custom JavaScript                | Run any JS function and if it returns true, the assertion is passed - learn more in [custom javascript actions](https://docs.bugbug.io/editing-tests/custom-javascript-actions) |
| \</> DOM element does exist      | BugBug checks if there is an element on the page you're looking for                                                                                                             |
| \</> DOM element does not exist  | BugBug checks if there is no element on the page you're looking for. Helpful with negative assertions                                                                           |
| Number of elements in DOM        | BugBug checks if there are a certain number of elements on the page you're looking for                                                                                          |
| Variable value                   | BugBug checks if the variable's output value matches the set condition                                                                                                          |

## Editing assertions

By default, BugBug records assertions that are best suited to what you are looking for. But you can also create advanced assertions, such as checking if a number is greater than a certain value. Select options from the drop-down menu to perform a more thorough check of your test case.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FJkhSMNTXhUmenBz2GSA2%2F2_editingAssertions.png?alt=media&#x26;token=600da1c1-6694-40b3-8e28-27b290da78d2" alt=""><figcaption><p>Example of assertion modification after recording</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FajNZqb0nGix1XgOASOPT%2FProjekt%20bez%20tytu%C5%82u%202.png?alt=media&#x26;token=708b7a31-32b3-43ba-aad4-4e4505c29a3d" alt=""><figcaption><p>Values can be confirmed under certain conditions</p></figcaption></figure>

| Assertion                        | Use it when                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Element is visible               | You want to check if an element is visible, meaning that it's in the viewport, opacity is not 0, and its visibility is not set to hidden. For example, you can assert that some error message is shown and visible to the user                                                                                                                                      |
| Element is not visible           | You want to check if an element is in DOM but not visible, meaning that it's not in the viewport or opacity is 0 or its visibility is set to hidden                                                                                                                                                                                                                 |
| Element has text                 | You want to assert the text in an element, for example, if a registration button contains a "`Sign up"` text. This is the most common type of assertion                                                                                                                                                                                                             |
| Form input has value             | You want to check if the value of the form element matches specific conditions. Only works with `form` elements like `input`, `select`, `checkbox`, `radio`, etc.                                                                                                                                                                                                   |
| Form input is checked            | You want to check if a checkbox or radio button is checked, meaning that it is selected, enabled                                                                                                                                                                                                                                                                    |
| Form input is not checked        | You want to check if a checkbox or radio button is unselected, unchecked                                                                                                                                                                                                                                                                                            |
| Download started                 | You want to check whether the download process for a selected file has started from the server. Additional settings for this assertion focus on the file name                                                                                                                                                                                                       |
| Custom JavaScript                | You need to do an advanced assertion, ex. comparing the element text with [variables](https://docs.bugbug.io/editing-tests/variables), making an API request, or using `localStorage`. When your JS function returns `true`, the assertion will be marked as `passed.` Also see [custom JS actions](https://docs.bugbug.io/editing-tests/custom-javascript-actions) |
| \</> DOM element exists          | You want to check if an element exists in the DOM (HTML structure), but not necessarily is visible                                                                                                                                                                                                                                                                  |
| \</> DOM element does not exists | You want to check if an element is not present in the DOM (HTML structure), ex. you want to make sure that some element disappeared completely from the page, and that it's not just set to `"display: none"`                                                                                                                                                       |
| Number of elements in DOM        | You want to check the number of elements that match a given selector, for example, you want to assert that a list shows 10 elements                                                                                                                                                                                                                                 |
| Variable value                   | You want to check if its computed value matches the set condition between: is/is not/contains/does not contain/matches regex                                                                                                                                                                                                                                        |

&#x20;


# Tabs & iframes

Enhance your test editing skills with BugBug's comprehensive guide on Tabs and iframes. Learn how to effectively optimize your test scenarios. Discover valuable tips to streamline your testing process

BugBug <mark style="color:green;">**fully supports testing in iframes or multiple tabs**</mark>. This is handled automatically during the recording but can also be controlled manually. You will notice the `Switch context` action if you work with iframes or multiple tabs.&#x20;

### What is the "Switch context" action?

When you record something in a different tab or iframe, an additional step will be recorded before the actual action for switching the context to this new frame or tab.

This defines the context for all the following test steps until you switch the context again to a different frame or a tab.

### Locating the right frame

The first tab you visit during the test is `Tab number` **0** and `context` identified as **`Top`**. This is the **default text execution context**, and if you don't interact in your test with iframes or other tabs, you don't need to add the `Switch context` step.

{% hint style="info" %}
The **default** test execution context is `Tab number` **0** and `context` **Top,** and adding this at the beginning of the test is unnecessary.
{% endhint %}

If you navigate to different tabs or iframes during the test, they will be identified by:

* Tab number \[`number`]
* Context \[`Top`|`Iframe`]
* Frame element (if the context is `Iframe`)

Tabs are numerated from 0, so each frame you open during the recording session will have incremented numbers.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHp8H9t7lmc42B4eFDViQ%2Fimage.png?alt=media&#x26;token=d76d29bc-932d-4a70-a918-6e23f8c041ff" alt=""><figcaption><p>Tab numbers starting from 0</p></figcaption></figure>

If the interaction **is not** in an `Iframe`, the context should be set to your default tab context: `Top`.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkI261Tzem4B3JxaUzRtU%2Fimage.png?alt=media&#x26;token=6b4b0b06-b8da-4852-9eff-c2b50e183fe2" alt=""><figcaption><p>Default tab context - Top</p></figcaption></figure>

If the interaction **is inside** an `iframe`, the context should be set to `Iframe` and the correct iframe selector is needed:

&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQxYKEMDDRDQhJMdlmSzv%2Fimage.png?alt=media&#x26;token=b6e95a58-d1fb-4dd0-a080-7abaaaa3f9c6" alt=""><figcaption><p>Switch to the iframe identified by XPath //IFRAME[id="frame1"] in the first browser tab (tab 0)</p></figcaption></figure>

BugBug also supports nested iframes during a regular recording session. You can read more about [nested selectors](https://docs.bugbug.io/preventing-failed-tests/selectors#nested-selectors) here.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FH2UElyfso2hgJytxmjiB%2Fimage.png?alt=media&#x26;token=9521698e-d222-450e-b1ce-ec7a799489a9" alt=""><figcaption><p>Switch test execution context to nested iframe</p></figcaption></figure>

A test scenario when you operate in your first tab, then in an iframe, in the nested iframe, and then again in the first tab looks like the below:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FyjjJ6gMBBGuk6dNYxf5F%2Fimage.png?alt=media&#x26;token=12914416-f901-424d-b5c5-7f5fd4bc64d9" alt=""><figcaption><p>Mixed test contexts</p></figcaption></figure>

If you have mixed contexts in your tests, it's important to remember which context you're in to make sure the test works correctly.


# Variables

## Intro to Variables

### Why use variables?&#x20;

Variables enable you to **run and maintain tests efficiently** in any of the following situations:

* You work with multiple development environments
* You have multiple tests that use the same value in multiple form fields or assertions
* You want to test forms that require users to enter random and unique data, e.g. registration with an email address
* You want to run the same tests with different form inputs, e.g. testing product searching against various search queries or testing different zip codes

### What are variables?

Variables are **dynamic pieces of text that you can use in your tests**. [Use variables in tests](#use-variables-in-tests) by entering their name in curly brackets to place a variable in any text field in the test steps ex. `{{myCustomVariable}}`

Variables are good for storing:

* Fragments of URL addresses like domains, subdomains, hostnames, etc.&#x20;
* Email addresses
* Input values like product names, brands, phone numbers, ZIP codes, etc.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FeYzk3QfYNkJEsGJxTIJM%2F21.03.2023%2012_11_58.png?alt=media&#x26;token=bd1ed665-5f4f-4c9a-bb23-cae5e5660564" alt=""><figcaption><p>Example: variable "hostname" used in an URL</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F23ul12snZCDN1vTPGcd7%2FZrzut%20ekranu%202023-03-21%20123230.png?alt=media&#x26;token=daac65a2-abb5-43fe-9941-790ea4ff1b56" alt=""><figcaption><p>Example: definition of variable "hostname" in the variables tab</p></figcaption></figure>

Variables do not have to be simple text assignments. Some [built-in variables](#use-built-in-variables-for-dynamic-or-random-values) are different each time you run the test for example `{{timestamp}}` or generate random values like `{{testRunId}}`.&#x20;

You can also write your own [javascript variables](#javascript-variables) - functions that return a value that is calculated every time you use the variable.

## Using text variables

### Create custom text variables&#x20;

This is the most basic type of variable. Go to the "Variables" tab and click on the "New variable" button.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F2KQwTRNtCsfA6rJ2CTwh%2FnewVariable_new.png?alt=media&#x26;token=cca5eb19-b48e-4123-9db2-307aab8e9380" alt=""><figcaption></figcaption></figure>

Add a name and value for your variable.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FxehmJ0ZANjm4Gt0UGXQv%2F1newVar2.png?alt=media&#x26;token=f7f06d24-f181-40b0-9181-678f551ae94e" alt=""><figcaption></figcaption></figure>

Then click on the "Create variable" button to save it.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXogYdHSLR558bX3EMYSx%2F1newVar3.png?alt=media&#x26;token=1f747217-bf8d-4581-8275-19286183f76a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important!** You can't use spaces in a variable name. We recommend that you use [camelCase](https://en.wikipedia.org/wiki/Camel_case).&#x20;
{% endhint %}

### Create custom JavaScript variables

Previously, a custom variable containing a text value was added. Now you can go further and use it with a JS variable that can generate a unique value. As a support, you are going to use the built-in variables in BugBug as well.

For starters, once again click on the "Create variable" button to create a new one, yet this time on the modal select the "Custom JavaScript" in the "Type" field.

Also, paste the JS code into the "JavaScript code" field. As an example, a simple function was used here:

```
return variables.testVariable + ' ' + variables.testRunId;
```

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fs8QnU5UugZAWtYSpaakw%2FvariableSettings_new.png?alt=media&#x26;token=7725c7d0-b68d-49ac-9d76-f3877f8a9f2c" alt=""><figcaption><p>Variable settings</p></figcaption></figure>

Next, click on the "Create variable" button, and we're all set.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FFvRouzh1HmMK5yFPwS6w%2F2newJSvar2.png?alt=media&#x26;token=54cced63-21a4-41c5-8418-a5b88f59e77c" alt=""><figcaption><p>List of added custom variables</p></figcaption></figure>

Now you're ready to use the names of our created variables when editing a test. To do this, simply use the names of the existing variables, i.e. place them in the target field(s) on a page that's being tested.

```javascript
{{testVariable}} or {{taskName}}
```

In general, the applied variables in your test might look like this:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FEcanpADx7QBgWeauqdFW%2FvarUsageInTest2.png?alt=media&#x26;token=4bad7f10-99c5-4d74-8c1f-36b579c9c67b" alt=""><figcaption><p>Variables used in a test</p></figcaption></figure>

###

### Use variables in tests&#x20;

Use a variable name in curly brackets to place a variable **in any text field in the test steps**. You can combine variables with normal text, for example `{{hostname}}/v1/index.html`

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FeYzk3QfYNkJEsGJxTIJM%2F21.03.2023%2012_11_58.png?alt=media&#x26;token=bd1ed665-5f4f-4c9a-bb23-cae5e5660564" alt=""><figcaption><p>Example: a variable used in "Go to url" action</p></figcaption></figure>

You can use variables in other types of actions, such as typing text in a form, assertions, and **even CSS selectors.**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0rMfCwY1CjysQI3Amlho%2FZrzut%20ekranu%202023-03-24%20125442.png?alt=media&#x26;token=0478e2f3-897c-4cd6-87ac-d5079d217c2f" alt=""><figcaption><p><strong>Use variables in selectors, assertions, etc.</strong></p></figcaption></figure>

**Combining variables with curly brackets**

You can also combine variables with `{{ }}` signs if you need to. To escape curly brackets, use `{% raw %}` and `{% endraw %}` blocks.

Here is an example:

Input:

* *variable: projectName* = `Foo`&#x20;
* *format*: `{{ projectName }}{% raw %} {Put this text in brackets}{% endraw %}`

Output:

* `Foo {Put this text in brackets}`

### Use built-in variables for dynamic or random values

Use BugBug's pre-defined set of variables to handle your complex testing scenarios. Here are some examples of what you can do with built-in variables

<table><thead><tr><th width="218.62315752406113">Built-in variable name</th><th width="92">Type</th><th width="188.744109669127">Description</th><th>Usage example</th></tr></thead><tbody><tr><td><h4>testRunId</h4></td><td>Text</td><td>The current id of the running test (UUID format).</td><td>You want to have a new random unique value for one specific test run, for example you want to <a href="#test-user-registration-and-login-using-variables">test user sign-up and then log in.</a> </td></tr><tr><td><h4>testId</h4><p></p></td><td>Text</td><td>The current id of the test (UUID format).</td><td>You want to test add/edit/remove operations in one test, for example, add a product and then remove the same product with a name <code>Test Product {{testId}}</code></td></tr><tr><td><h4>suiteRunId</h4></td><td>Text</td><td>The current id of the suite (if the test is running from a suite, UUID format).</td><td>You want to have a new, random unique value that is the same across all the test runs in one suite.</td></tr><tr><td><h4>runMode</h4></td><td>Text</td><td>The current run mode for the test ("local" or "server").</td><td>You want to have different input or assertion value when the test is run on server. </td></tr><tr><td><strong>randomNameFixed</strong></td><td>Text</td><td>Random name that remains unchanged during the test run (8 letters).</td><td>You want to have a new, random uniqe name that is the same across all the  test and used multiple time </td></tr><tr><td><h4>scheduleId</h4></td><td>Text</td><td>The current id of the schedule (if the test has been started via a schedule, UUID format).</td><td>You want to have a new, random unique value that is the same across all schedule run.</td></tr><tr><td><h4>timestamp</h4></td><td>Text</td><td>The current Unix Time in milliseconds (int format, e.g.: 1645710937798).</td><td>You want to know when your test runs or use it similar to <strong>randomNumber</strong></td></tr><tr><td><h4>randomNumberFixed</h4></td><td>Text</td><td>Random number that remains unchanged during the test run (10 digits).</td><td>If you want to edit an element, find it later in test steps and use it or remove it.</td></tr><tr><td><h4>profileName</h4></td><td>Text</td><td>The current profile name for the test. Default: "Default".</td><td>If you want to enter a production/test URL depending on the profile, test runs</td></tr><tr><td><h4>suiteName</h4></td><td>Text</td><td>The current suite name for the test (if the test is running from a suite).</td><td>If you want to create an email that inform you about suit name that was run </td></tr><tr><td><h4>testName</h4></td><td>Text</td><td>The current test name.</td><td>You can mix it with timestamp to create a new subscription notification test.</td></tr></tbody></table>

Built-in variables also give you access to generators of random numbers and names that you can use right away in your tests.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FfJfFAIGfICSZDi0ZIOeR%2FZrzut%20ekranu%202023-03-20%20111515.png?alt=media&#x26;token=6af6e495-b35f-4d96-a43f-1345d9408c13" alt=""><figcaption></figcaption></figure>

### Recording and working with variables

Currently, you can use variables during recording.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FiTjofjLxq5nsC3rxjjY2%2FvarBtn.png?alt=media&#x26;token=b850827e-1d13-4c0a-bf70-483cbfb858d4" alt="" width="279"><figcaption></figcaption></figure>

* You can **insert** pre-prepared or built-in **variables** when **recording tests.**
* You can also dynamically **create variables** during recording based on the source being tested.
* You can also record the steps and then edit them manually.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FlSuvQyItDk84UwsceiR9%2FZrzut%20ekranu%202023-04-03%20120138.png?alt=media&#x26;token=8bdbff18-3807-4a60-8f0a-99baedd17446" alt=""><figcaption><p>Two option for variables action in overlay</p></figcaption></figure>

{% hint style="info" %}
&#x20;For more details, go to the "[Variables During Recording](https://docs.bugbug.io/editing-tests/local-variables)" document.&#x20;
{% endhint %}

## User registration and login using the BugBug Testing Inbox

The [BugBug Testing Inbox](https://bugbug-inbox.com/) solves several problems of testing user registration and login.

> **Test case:** As a user, I go to the home page and click the "Login" button. I enter my email and password. I receive a verification email. I click on the link. I use my previous email and password to log in.

&#x20;You can use inbox to solve several problems, such as:

* How to get a unique random email address
* How to receive the email with the verification link
* How to use previously generated unique email and password in the login form&#x20;

#### **Create your test using BugBug**&#x20;

First, start the test recording with a page that requires registration. Add steps that lead to the registration process. You don't need to set it up any particular way at this point. Record it as normal users perform their actions.

### Use the BugBug Testing Inbox to generate a unique email address&#x20;

When you're ready to enter the email address, look at the BugBug extension overlay menu. There is an option called **"Inbox"**. Click it, but do not stop the recording.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FnEiwj28K9BCm1lA0N9iQ%2Finbox%20menu.png?alt=media&#x26;token=45c7dfb3-2570-4146-8452-12a0f696621d" alt=""><figcaption></figcaption></figure>

When you open it, you will see two options. Focus on the **"Auto-generated random email unique for this test"** option.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FI0zjD3V8Yj4X0QHii60T%2Finbox%20open.png?alt=media&#x26;token=eefe3fef-6cf6-4960-8f1b-e57fb5a5c425" alt=""><figcaption></figcaption></figure>

This option creates a random email address using the variable **{{testRunId}}** and the domain **@bugbug-inbox.com**. \
The {{testRunId}} variable is unique per test run, so the generated email address will be constant during a single test run. If you rerun the test, a new email address will be generated using this variable. On the BugBug web application, in steps, you will see it as **{{testRunId}}@bugbug-inbox.com**.

You can copy it directly from the extension using the copy **icon.**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fcx2X7nyCfMU3jLuK5QKR%2FCopy%20icon.png?alt=media&#x26;token=5eb1bc55-f756-46d2-932e-f9b7ae3c7818" alt=""><figcaption></figcaption></figure>

And use it directly to register. If the registration process does not require a verification email, you can now go back to the extension menu and continue. If you need to confirm a verification email, go to the verification flow.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F3nj5NCqhVLwvQlbgM2Cz%2Fgo%20back.png?alt=media&#x26;token=86180729-dffb-44c8-bbfb-0bb9725d766d" alt=""><figcaption></figcaption></figure>

You can find the email address based on a variable in the test step. Now your test is free of duplicate registration email problems every time you run it.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FfNaWVjORrYyt6uLgUjrY%2Fsteps.png?alt=media&#x26;token=a0a008c8-dcbc-4780-9185-d41ac516ebfe" alt=""><figcaption></figcaption></figure>

### Using the BugBug Testing Inbox to activate the registration email

Most of the registration processes require opening the verification email and confirming the address. With the BugBug Testing Inbox, you can open an email, automatically confirm it as a test step, and complete the process without using third-party providers. \
\
When you reach the moment of providing an email in the test steps, just **copy the email address** by an icon. Submit the form and **open our inbox in a different tab** by clicking the "open inbox" button. Do not stop the recording. \
\
Opening a new tab will be recorded and required.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FmkOstuMtUjKkvYZWbaLW%2Fopen%20inbox.png?alt=media&#x26;token=0f8afda4-f776-4d9a-8e3d-31fafd404ea4" alt=""><figcaption></figcaption></figure>

In a new tab, you will see an inbox created specifically for an email address you used in the previous steps. Wait for a confirmation email.&#x20;

\
The inbox refreshes automatically, so there is no need to do it manually.

{% hint style="warning" %}
The BugBug inbox only saves emails for **10 minutes**. After that time, all emails will be removed.
{% endhint %}

Open the registration email by clicking on "subject".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNW7uSzFQy4nI1Q18395B%2Fsubject.png?alt=media&#x26;token=41252ac9-5902-4f80-a3e1-116c351d9b67" alt=""><figcaption><p>The BugBug confirmation email is used only as an example of the process.</p></figcaption></figure>

{% hint style="info" %}
**Important! Make sure you click the subject line of the email!** \
BugBug needs to always open the most recent email, so your [selector](https://docs.bugbug.io/preventing-failed-tests/selectors) here needs to click the first email with a specific subject line, for example `//SPAN[normalize-space(text())="`Confirm your e-mail address`"]`
{% endhint %}

Now just click the button with the authorization link and continue recording.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F9NP3qGDS80IJvNbEWPmi%2Fconfirm%20button.png?alt=media&#x26;token=38dbfa9b-e71c-496c-9542-84c92385a62c" alt=""><figcaption><p>The BugBug confirmation email is used only as an example of the process.</p></figcaption></figure>

<details>

<summary>If your email doesn't have a button but just a verification link </summary>

If your verification link is shown directly as a string, this string will be different every time. BugBug will record a selector that matches exactly this string, for example //A\[normalize-space(text())="`https://`acmecorp`.com/#/activate`?key=60f0ae29-542a-4418-8529-41a01bf22fcc"]

In such case, you may need to manually update your selector after the recording so that it only checks if the text contains the beginning of the verification URL, for example `//*[contains(text(), "https://`acmecorp`.com/#/activate")`

</details>

When your email is confirmed you can return to the test page tab and continue.&#x20;

### Using specific email and virtual inbox features  &#x20;

If you need to use an email address with a specific alias during a test you can also use the BugBug Testing Inbox. The menu provides an option for a custom alias.&#x20;

Just select the **"Specific test email"** option.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F8aiEJBCp2TDmG9uGpoGk%2FmyEmail.png?alt=media&#x26;token=b90ea3be-24fc-4d79-b1ce-ec7b1f7a7dd2" alt=""><figcaption></figcaption></figure>

If this option is selected, you can create your email alias by typing.

{% hint style="info" %}
You create only an Alias for **@bugbug-inbox.com**.&#x20;

Do not put other domains.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FtzYOJ7Ny15JkGUDwKSOC%2Falias.png?alt=media&#x26;token=d6e11de1-47a9-4278-a1be-a3471fe3924c" alt=""><figcaption></figcaption></figure>

This option also allows you to **open Inbox** with a specific email you set.

{% hint style="warning" %}
If you decide to create an alias, make sure it's unique. We do not limit inboxes per project or test. Make sure that other users will not be able to interrupt your tests with the same email address.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FyVMlbyPcraF06pWjAESs%2Faliasinbox.png?alt=media&#x26;token=87176eb6-716b-43bc-8151-0761be206176" alt=""><figcaption></figcaption></figure>

### Using variables with BugBug Testing Inbox

By default, inbox uses only the **testRunId** variable, but you can boost it by freely changing it in your recorded steps.&#x20;

You can mix or change variables simply by changing the alias of the email and adding eg. a **timestamp** variable.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FYm07pvUf03GdeOJ6uj5i%2FtypeTextId.png?alt=media&#x26;token=92881833-04fb-420f-a5e3-dd63d2ba6efd" alt=""><figcaption><p>Add any variable as alias </p></figcaption></figure>

{% hint style="info" %}
You can open a virtual inbox by combining **<https://bugbug-inbox.com/>** and any **variable**.&#x20;
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQLD6M7ixalr454fyE10I%2Ftab.png?alt=media&#x26;token=a430c859-947d-4a2b-a3a9-19b1d8841508" alt=""><figcaption><p>Combined URL </p></figcaption></figure>

## Profiles

### What are profiles?

Profiles are your own **presets for different variable values**. You can run tests or suites with profiles to override your default variables to a specific value. This is especially useful when [working with multiple development environments. ](#work-with-different-development-environments)

{% hint style="info" %}
**Important** To see the profile section in the test, you need to have at least 2 profiles. &#x20;
{% endhint %}

![You can quickly swap the profile in the menu near the "Run" button. This menu will not appear if you only have one default profile.](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUrAZiXTITShS4lPbEWlI%2Fimage.png?alt=media\&token=03154cf6-a084-4523-bbe1-e2dd25750686)

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FPzxcCgXllhhgMhHkCwHG%2Fnew%20profile.png?alt=media&#x26;token=95e11ba1-031d-4a8e-b31e-60732dc49e2c" alt=""><figcaption><p>To add, remove and edit profiles go to the "Variables" tab</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FyyPRzALolmimuNPJoBLq%2FZrzut%20ekranu%202023-03-21%20152825.png?alt=media&#x26;token=ceb83aea-7c45-4338-8d53-23743af97ae3" alt=""><figcaption><p>Override variables in the profile settings. Leave an empty field to keep the default value.</p></figcaption></figure>

### Run a test with a profile to override variables

First, make sure that you have read about [what profiles](#what-are-profiles)[ are](#what-are-profiles), and then:

1. Create a profile in the "Variables" tab
2. Go to test editing
3. Swap profiles before running the test in the menu near the "Run" button

You can also run tests with a [profile from the command line](#override-variables-and-profiles-from-command-line-cli) in your pipeline

{% hint style="info" %}
**Important!** Profiles selection is not saved in the test. \
If you run the test from the tests list, we will ask you to select a profile.&#x20;
{% endhint %}

{% hint style="info" %}
**Tip!** Your tests should pass on all profiles. Don't create tests that only work in one profile.&#x20;
{% endhint %}

### Run a suite with a profile

You can have multiple suites and each suite can run your tests with a specific profile. For example, you create suites for "Production smoke tests" and "Staging all tests". Each suite will have different sets of tests that will run on different profiles with different variables.

1. Go to "Suites" and select a suite to edit
2. Choose with which profile this suite will run

{% hint style="info" %}
**Important!** This suite will always run with this profile. The profile selection is saved in the suite settings.&#x20;
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FdQGIdHRxuoHKoopfMcml%2Fprofile.png?alt=media&#x26;token=f8343800-6334-4ba6-9ae7-5c4337ff4b8a" alt=""><figcaption></figcaption></figure>

### Work with different development environments

Let's say you have 3 environments: *production, staging, and local*. They are all exactly the same, but they have different URL addresses. You want to run the test sometimes on production and sometimes on staging.

| Environment | URL              |
| ----------- | ---------------- |
| Production  | `acme.com`       |
| Staging     | `stage.acme.com` |
| Local       | `localhost:3000` |

**Prepare the variables and profiles**

1. Create a variable named `hostname` with default value `https://acme.com`
2. Create 2 profiles named `Staging` and `Local`
3. Override the hostname variable in the profile Staging for `https://stage.acme.com`
4. Override the hostname variable in the profile `Local` for `https://localhost:3000`

#### Update the URLs with your variable

1. In the tests, find your steps with `Go to url` action
2. Replace the `acme.com` with `{{hostname}}`.&#x20;

**Tip:** You can also combine the curly brackets with the rest of the URL for example `{{hostname}}/registration` or `app.{{hostname}}`

Now you can [run the tests with different profiles](#run-a-test-with-a-profile-to-override-variables) and quickly swap between your dev environments.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FL9chpQmQrcDRZqlePYfh%2Fimage.png?alt=media\&token=891f04a1-ffdb-4215-b979-25dfaa011e3f)

### Override variables and profiles from the command line (CLI)

Use [BugBug CLI ](https://docs.bugbug.io/integrations/api)to integrate with your build pipelines and run tests with variables that you can adjust to multiple environments.&#x20;

If you run tests or suites from the command line, you can override each variable or profile with parameters, for example,  `--variable val1=value` and `--profile=profileName`. Read more in the [CLI documentation](https://www.npmjs.com/package/@testrevolution/bugbug-cli).

## JavaScript variables

Javascript variables allow you to compute dynamic values every time the variable is used in a test.&#x20;

#### Use JavaScript variables for:

* Getting data from API, for example, SMS codes, authorization magic links
* Mathematical calculations such as adding, subtracting, multiplying, etc.
* Generating unique strings that need to meet specific validation criteria such as social security numbers,  postal codes
* Values that are different depending on conditions, for example, if your app shows a different text during night and daytime

#### **To create a JavaScript variable**&#x20;

1. Go to the "Variables" tab and click "New variable"
2. Change the variable type to "Custom JavaScript"
3. Enter a JavaScript function that will be executed every time this variable is used in the test

{% hint style="info" %}
**Important!** Remember that your function needs to have a `return` statement - it needs to return a specific value.
{% endhint %}

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FJhTTD3ywHYBnZXbGEb71%2FScreenshot%202022-04-05%20at%2011.47.15.png?alt=media\&token=77a74fc9-329a-40db-905a-4040277515e7)

### Example JavaScript variable functions

Return a simple string value:

```
async function(variables) {
    let firstName = "John";
    let lastName = "Smith";
    return firstName + lastName;
}
```

Return a different value when the day of the week is Sunday:

```
async function(variables) {
    const d = new Date();
    let day = d.getDay();
    if (day === '7') {
        return "Delivery in 48 hours"
    } else {
       return "Delivery in 24 hours"
    }
}
```

### Use the "variables" argument in your JavaScript function

Your custom JS variable can also read your other variables. The `variables` argument stores all the built-in variables, your custom variables, and local variables recorded during the test run. <br>

If you run a custom javascript step with a function `console.log(variables)` you will get such an output in the console:&#x20;

```
{
    hostname: "https://marmelab.com/react-admin-demo/"
    profileName: "Default"
    runMode: "local"
    scheduleId: null //only for scheduled runs
    scheduleName: null //only for scheduled runs
    startDemoURL: "https://marmelab.com/react-admin-demo/"
    suiteId: "54bd4384-ad9c-4e83-946f-111392ed0a82"
    suiteName: "All tests"
    suiteRunId: "18e1e3c3-ec2a-45c9-b817-8f48a56a0807"
    testId: "37e64599-31a9-4707-9fed-a64cdec24294"
    testName: "Test"
    testRunId: "6498c9bd-81a5-412f-a275-2c7f1cfc4d45"
    timestamp: 1665667075470
    username: "demo"
}
```

You can use this to operate on the variables, combine them, calculate, etc.&#x20;

```
async function(variables) {
    return variables.firstName + variables.lastName
}
```

```
async function(variables) {
    return variables.userEmail + variables.testRunId
}
```

```
async function(variables) {
    return variables.userHeightInCentimeters + 20;
}
```

{% hint style="info" %}
**Important!** Variables are calculated immediately before a step is executed. If you want to calculate variable only once per test, use `localStorage` to cache the result and then access it with [custom javascript steps](https://docs.bugbug.io/editing-tests/custom-javascript-actions).
{% endhint %}

{% hint style="warning" %}
**Important!** Other Custom JavaScript variables are not available in the `variables` object. This is impossible because you can't specify the order in which the JS variables are calculated or control the dependencies. See the `localStorage` workaround below.
{% endhint %}

{% hint style="info" %}
**Important!** Do not use the local variable and its combination in steps before BugBug captures the wanted value. Otherwise, BugBug will return an <mark style="color:red;">`undefined`</mark> string instead of the desired [local value](https://docs.bugbug.io/editing-tests/local-variables).
{% endhint %}

### Use localStorage to pass on data between variables

If you want to access a variable that was already calculated in a previous step, use `localStorage`.&#x20;

1. At the end of the function in the first variable, store the result in `localStorage`.&#x20;

```
async function(variables) {
    let name = variables.firstName + variables.lastName;
    localStorage.setItem('bugbugUserName', name);
    return name;
}
```

2\. At the beginning of the next variable get the value from `localStorage`.

```
async function(variables) {
    let name = localStorage.getItem('bugbugUserName', name);
    if (name === 'Carl') {
        ...
    }
}
```


# Local variables

BugBug has the option to set up and insert a variable from the tested source during test recording. Now you can store any text value from the web page you are testing in a variable and use it in feature steps. For example, to find out newly registered unique users in your CRM. Also, you can use built-in variables or custom variables added to the project.&#x20;

A new option for **variables** in the test recording process can be found in the **BugBug Extension overlay**.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FzXt74muO2oZ029AEiahi%2F1_recorder.png?alt=media&#x26;token=6e5c59cf-bf71-45f1-8a51-af54048bc1c8" alt="" width="284"><figcaption><p>Variables button in recorder</p></figcaption></figure>

When you click on the "**Variables**" button there will be two options:

* Save variable for later
* Insert variable

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FFDlqqL5U1IM7gdyr5ioH%2FZrzut%20ekranu%202023-04-03%20120138.png?alt=media&#x26;token=713c1990-5c94-453b-9bc0-deb0cb3c723d" alt=""><figcaption></figcaption></figure>

### Save variable for later&#x20;

This option is used to save the new text value as a variable during the test recording. You can find an element and copy the value directly from the browser. Now there is no need to hardcode values and change them later in a BugBug web app steps edition. You can move forward. <br>

Click on the "**Save variable for later**" button. Saving a variable mode is now active.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FL77P8Hp2JW8vInPErfoi%2F2_saveForLater.png?alt=media&#x26;token=a1ae9b0a-92d2-4157-8199-4f078463791e" alt=""><figcaption><p>Click on a "Save variable for later" button</p></figcaption></figure>

At this time you can click on an element with text value on a tested web app and save it into a variable. For example, you can save the search phrase - *"Bugbug automation tool"*.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQdEsHgQ75H4HLOS3PDRh%2F3_saveForLater.png?alt=media&#x26;token=f1804c1f-f448-41eb-87cb-9612df3701fd" alt=""><figcaption><p>Click the item with the desired text value</p></figcaption></figure>

When an element is selected and a value is recorded, you will see an input in the BugBug extension menu where you can save the name for the new variable. Later this name will be visible in a list of variables in the BugBug extension menu.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCsxfMkjlyduJ7KZwsRfr%2F4_saveForLater.png?alt=media&#x26;token=c0535a58-54c3-4245-bc6d-dffcf04cec02" alt=""><figcaption><p>No spaces or other special characters allowed</p></figcaption></figure>

When you save a variable, you will be taken to the main menu of the BugBug extension and can continue recording steps.

{% hint style="info" %}
The saved variable is a cross-domain feature. Now you can use the saved value on different web apps in one test. eg. You can open a new tab and use the stored value there.&#x20;
{% endhint %}

{% hint style="warning" %}
The variable can be overwritten several times during the test recording by using the same name. If you want to avoid this situation, use some unique names each time.
{% endhint %}

{% hint style="warning" %}
Using the same name of the variable as the built-in or custom variable name will override the data. This can cause a problem if your test is based on them and overriding these variables is not intended.
{% endhint %}

### Insert a variable during step recording

Now you can insert a variable during step recording in BugBug. You can use saved variables from previous steps, use custom variables from the project, or use global variables that are predefined by default.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Ffdtbsex1j77lbwFzgZbC%2FInsert%20variable.png?alt=media&#x26;token=fed2a6b6-a490-4da1-8b52-48146cee592a" alt=""><figcaption></figcaption></figure>

Click the "**Insert Variable**" button. A variable menu will open. As you can see, we suggest the last saved variable by default. Every variable has a name and length-limited value presented below the name. You can open the drop-down menu to select another variable from the list. [Available variables](#available-variables.) will be discussed in another chapter. Now we will focus on how to insert our saved variable into the designated input.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FAQdlfhKDX7r4BD3Qwfpo%2F5_useVariable.png?alt=media&#x26;token=40533faf-2168-4819-9ed9-f3bdf15c1e45" alt=""><figcaption></figcaption></figure>

When you open the "**Insert variable**" menu the insert variable mode is now active for the selected variable. Now let's move on to the web application we're testing.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FoupFn143LvDibgHKYVbH%2F5_useVariable.png?alt=media&#x26;token=2d6ef13e-28f4-4754-8499-a5655eb98e78" alt=""><figcaption><p>Find an input you want to fill with the variable</p></figcaption></figure>

If you have an input that you want to automatically fill and you have opened the Insert Variable menu with the selected variable, you can simply click on an input to fill it with a value.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCNAc0moYBvht30EMIhnd%2F6_useVariable.png?alt=media&#x26;token=cc3d22a6-5b5f-42c7-ae9c-70abad3af45b" alt=""><figcaption></figcaption></figure>

The "**Insert variable**" menu closes. The entry is saved with the value, and you can continue recording steps such as clicking Enter to open search results.

### Available variables &#x20;

During recording, you can also insert a variable added by default from BugBug such as: <br>

* Built-in variables&#x20;
* Custom variables&#x20;

All these variables are described in the [Variables](https://docs.bugbug.io/editing-tests/variables) section of BugBug documentation. <br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FzbsFJ26KV2LXm0bkjeHL%2FVariables.png?alt=media&#x26;token=6a30e561-f0cc-4cc4-a238-ed84337a16ae" alt=""><figcaption><p>Variables added by default to insert list. </p></figcaption></figure>

Using built-in or custom variables is now easy and you do not need to edit steps in the BugBug web application UI. You can find them in the list.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fk4SSziLYXVIIV53dvsoq%2FZrzut%20ekranu%202023-04-04%20104323.png?alt=media&#x26;token=9f9e9f7a-22e2-4fb2-8e66-a2ee8fbe32a6" alt=""><figcaption></figcaption></figure>

### Unavailable variables during step recording &#x20;

#### Built-in variables based on a suit or scheduled run &#x20;

We cannot provide data such as {{suiteRunId}} because when recording, there is no suiteRunId. It's only accessible when the suite is running. You can insert this variable in normal test-edit mode on the BugBug web app UI for a case.&#x20;

{% hint style="info" %}
Some of the built-in variables are now disabled with notification. BugBug cannot import data from these variables. You can use it in step edit on the BugBug web app UI.&#x20;
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fk4SSziLYXVIIV53dvsoq%2FZrzut%20ekranu%202023-04-04%20104323.png?alt=media&#x26;token=9f9e9f7a-22e2-4fb2-8e66-a2ee8fbe32a6" alt=""><figcaption></figcaption></figure>

#### Custom JS variables&#x20;

Currently, there is no way to use a custom js variable during test recording. We are working on providing such a feature, but for now, we can only use variables with values that are accessible before the test starts recording.\
You can use custom JS variables in step edit on BugBug web app as we [suggest](https://docs.bugbug.io/editing-tests/custom-javascript-actions) in our documentation.&#x20;

### Search variables on the list&#x20;

You can search for variables on the BugBug extension list by the variable name.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fy84RjN8eshJOxU3okem7%2FSearch.png?alt=media&#x26;token=e418d3e1-5be5-48d0-bf68-0b038e786b6c" alt=""><figcaption></figcaption></figure>

### Local variables in web app UI&#x20;

There is a new step form for local variables recorded from the tested source. You can edit this variable freely. The recorded variable can be found in the step list as a "set variable".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FtSzKRtcGOaBOPau7cVLA%2Fset%20variable.png?alt=media&#x26;token=fe70fe60-180c-466b-971d-4e69301a8974" alt=""><figcaption><p>Recorded step for local variable</p></figcaption></figure>

You can edit values such as the variable name or the correct item selector in the BugBug web application UI after you have finished recording.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FaWlbEurlJk5QlsSa19r1%2Fset%20variable%202.png?alt=media&#x26;token=90a84b37-3c0a-474a-9a39-44a740aab9c2" alt=""><figcaption></figcaption></figure>

**Use a local variable**

You can use local variables by selecting the "Insert variable" option during recording in the BugBug overlay. At the end of the recording session, the step using the local variable will be saved as "Type text" with the variable name used in the "value" field.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FrcZ6iPvtNUWqj0lA6Fdm%2Fput%20variable.png?alt=media&#x26;token=c2ddd315-2e8b-4a9e-931a-da06af0f4b86" alt=""><figcaption></figcaption></figure>

You can also add a local variable from the BugBug web app UI by selecting "add a new step" on the list and filling it all manually.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXTLThjLWAc5iIrwxZ3D9%2FZrzut%20ekranu%202023-04-11%20105018.png?alt=media&#x26;token=1c4648a8-8fa9-47e6-ac56-91c5f7259a35" alt=""><figcaption></figcaption></figure>

Select "Set variable" from the modal.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FBomqwpOcrAWB8vyvIknU%2FZrzut%20ekranu%202023-04-11%20105541.png?alt=media&#x26;token=1963733d-3e36-4713-8206-444df33e610b" alt=""><figcaption></figcaption></figure>

And fill in the requested inputs&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FG1dh8mjDTmYQ5VShouen%2FZrzut%20ekranu%202023-04-11%20105752.png?alt=media&#x26;token=4cc37aab-67f4-4ed9-959d-f09034a9cc3b" alt=""><figcaption></figcaption></figure>

Any recorded local variable can be used in the following steps by mentioning the local variable name in double curly brackets e.g. {{savedVariable}} in any text field like an assertion or custom selector. For more info check out [what are variables](https://docs.bugbug.io/editing-tests/variables#what-are-variables).

### Combine local and other variables in one JS custom variable&#x20;

You can create a new variable using two different values in the JS form, which allows you to combine stored variables from the recording process and those that we provide as default global variables.<br>

When you set variable from recording&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F8FCPhPrahqbIM5pAOmQ0%2Fset%20variable.png?alt=media&#x26;token=4c0531c6-e6ea-4746-9879-418e21672523" alt=""><figcaption></figcaption></figure>

You can use its name when creating a [new custom JS variable](https://docs.bugbug.io/variables#javascript-variables). All stored variables are accessible in JS form by using the argument <mark style="color:red;">`variables`</mark> combined with the variable name.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSaJLzRgI152agxEc5HbV%2Fvariable%20name.png?alt=media&#x26;token=b766b633-d26d-47b5-bf6c-605fb7f7751c" alt=""><figcaption></figcaption></figure>

When you use a new custom JS variable in step, BugBug will automatically combine the stored value with another variable that you want. These options allow you to combine values from all saved variables. You can call them as many times as you like.

To use a newly created variable, just put a variable name in double braces. After the first test run, you can find the calculated value of your variable from the previous test run in Step Details.\ <br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fp1eIWL2BdeiQ8GcrtT1h%2Fcomputed%20value.png?alt=media&#x26;token=d4516ffe-b067-46af-bfa9-8e747b4a64b2" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Do not use the local variable and its combination in steps before BugBug captures the wanted value. Otherwise, BugBug will return an <mark style="color:red;">`undefined`</mark> string instead of the desired local value.
{% endhint %}


# Custom JavaScript actions

## JavaScript Steps

If you know how to code in JavaScript, you can overcome any limitations of BugBug features. With the power and flexibility of custom code actions, you can run any function during your tests.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FWuBVtMLXu5qAAzmZXlN8%2Fadd%20step%20js.png?alt=media&#x26;token=7752a161-5eea-4dcc-9be4-8903b46fa6b4" alt=""><figcaption></figcaption></figure>

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fw9x0527Xs1N6FC1HJtL1%2FScreenshot%202022-04-11%20at%2014.16.17.png?alt=media\&token=137aa5b5-02dc-490f-ac13-ff4c39c099df)

{% hint style="info" %}
**Hint!** You can call native JS functions, ex. you can request data via `XMLHttpRequest`, or store values in `localStorage`, etc.&#x20;
{% endhint %}

{% hint style="info" %}
**Remember!** You can also use [variables](https://docs.bugbug.io/variables#use-the-variables-argument-in-your-javascript-function) in your custom code
{% endhint %}

### Advanced JavaScript assertions

Use JS code to add complex assertions. Run any function and if it returns `true` the assertions will pass.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0oEE681NfPegM7oGuVdG%2FAssertion%20JS.png?alt=media&#x26;token=464972a4-0ee9-4b47-85ac-56caddb6311a" alt=""><figcaption></figcaption></figure>

**Example: assert if an input element has a specific placeholder text.**

1. Record a regular assertion to the input.&#x20;
2. Change its type to "Custom Javascript assertion"&#x20;
3. Enter custom JS code that checks the placeholder of the element, for example \
   `if (element.placeholder === 'Username') { return true } else {return false}`

{% embed url="<https://youtu.be/g7CsE-WHrwQ>" %}

### Make an API request from a custom Javascript code

Using the custom JS you can really do anything. For example, you can request some data from your API and use this data in a [custom javascript variable](https://docs.bugbug.io/variables#javascript-variables) or in an assertion.&#x20;

Here's an example of how to make a server-side request from Javascript.&#x20;

```
const response = await fetch('https://reqres.in/api/users', { 
    cors: 'no-cors'
});
const json = await response.json();
return json.data[0].email; //return the first user email
```

{% hint style="info" %}
**Note!** This is coding, so it adds complexity and more problems to solve. If you encounter cookie complications or  "Access-Control-Allow-Origin” ask a developer for help or contact BugBug support. We recommend keeping things simple and finding another solution to achieve a similar goal.&#x20;
{% endhint %}

{% hint style="info" %}
**Learn more** in the full [Fetch Web API documentation](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)&#x20;
{% endhint %}

We listed several ideas on what you can achieve with API requests via code:

| Use API request to                                                                 | Example use case                                                                      |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Compare the data displayed in your app with the data returned from the server      | Check if your currency exchange is up-to-date                                         |
| Get a list of test users and their parameters from a centralized testing data file | Get a login and password for your random test user, skipping the registration process |
| Get the latest item from a server and its ID                                       | Check if the most recently added product is shown on the list of search results       |


# Running the tests

Discover how to efficiently run tests with BugBug. Learn the best practices and techniques to optimize your testing process. Improve your software quality today

## Different ways of running the tests

### How to initiate test runs?

* simply [by clicking "Run"](#how-to-run-a-test-manually)
* automatically with Schedules
* via API using [BugBug CLI](https://docs.bugbug.io/integrations/api)

### Running locally or in the cloud

* [locally](https://docs.bugbug.io/running-tests/test-in-your-browser) - the test will run on your computer in Chrome browser in incognito mode
* [cloud](https://docs.bugbug.io/running-tests/in-cloud-on-server) - the test will run on BugBug servers on a virtual machine

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FRMj9J6I566CtDGFmBRZ4%2Fimage.png?alt=media\&token=2c6285a1-20d6-43bc-9cde-c5fb628e3703)

## The simplest way to run a test

1. Go to a project and click the test that you want to run
2. Click `Run` button
3. See the incognito Chrome browser opening and the test running

{% hint style="info" %}
**Make sure you don't have any unsaved work in other incognito windows.** If you have other incognito windows open, BugBug will need to close them before running the tests. When you click "Close all windows", then all the incognito Chrome windows will be closed.&#x20;
{% endhint %}

After you run the test, check the result - [learn more about test statuses](https://docs.bugbug.io/running-tests/statuses).


# Statuses

Learn about BugBug's test status functionalities and improve your testing process. Explore different test statuses for effective test management.

When you run a test, you will see one of the following statuses:

### Test passed

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FTnYdtUoAUgqOvE5gWcQ8%2FScreenshot%202022-04-11%20at%2017.59.23.png?alt=media\&token=b267fbf9-452c-4808-825b-1a7c47057cd5)&#x20;

Everything worked as it should

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MKixgeBPbLvnD0l1eiV%2F-MMDDkyLR29CghHPRNnB%2F-MMDFTD5fAs-HhT7DMJW%2FScreenshot%202020-11-16%20at%2000.33.22.png?alt=media\&token=c761b425-4791-40ef-9a90-23640b0cd1a5)

### Test failed

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FWE6t2PANQIiRsVQzwXYR%2FScreenshot%202022-04-11%20at%2017.59.34.png?alt=media\&token=d9c6b2b3-772e-43be-87d1-ac5ced342c95)

The test has not finished because an assertion failed or it was not possible to continue running the test steps and the test finished because of the [timeout](https://docs.bugbug.io/preventing-failed-tests/timeout).

You will get additional error information when this happens and tips on what to do to fix it.

Learn more on how to [debug and modify a step](https://docs.bugbug.io/debugging-tests).

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FN95fsW44SEozToyA84rl%2FScreenshot%202022-04-11%20at%2017.54.21.png?alt=media\&token=135b4813-b6ca-43d6-8e0d-9f3947cd0de9)

### Test passed but some waiting conditions were skipped

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FC2lXfvvmcitqOIMHwcyu%2FScreenshot%202022-04-11%20at%2017.59.19.png?alt=media\&token=4dc50070-1cf7-4729-ab9d-8f63656be3b0)&#x20;

This status is indicated by a green circle that's empty inside.

This is a unique BugBug feature for preventing failed tests. This indicates that the user is able to finish your test, but you can take a look at the reason for skipped [waiting conditions](https://docs.bugbug.io/preventing-failed-tests/waiting-conditions) just to make sure that your tests are in a good condition.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FRYPY0BHacucKtrvnH0M7%2FScreenshot%202022-04-11%20at%2017.55.51.png?alt=media\&token=e5fd992e-22ca-42d9-9360-14a10b72631c)

### Test error / crashed

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FidZQ2QiqrT2nDkmjoXdf%2FScreenshot%202022-04-11%20at%2018.00.47.png?alt=media\&token=2a95018f-6d21-473f-8145-a0e12133341e)

The test encountered an error, which is not a result of the test steps, ex. internal server error, BugBug extension error, etc. This is most likely caused by a bug - please contact us if you see this status often.

### Test paused for debugging

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FwYl7wXuG4TXehSExdHfh%2FScreenshot%202022-04-12%20at%2010.58.47.png?alt=media\&token=7d8977ad-98f3-4360-8cb5-c1a49130f015)

You used a [breakpoint](https://docs.bugbug.io/debugging-tests/breakpoint-run-step-by-step) or paused the test in the middle of execution using "Pause" button

### Test stopped

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUSZIYgOmuJis6bt9ClH9%2FScreenshot%202022-04-12%20at%2011.00.02.png?alt=media\&token=e17d03a3-9f90-4e24-ba92-1ff5b6c2fbaf)

You stopped the test before it finished running, before it reached a conclusion.

### Test running

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FU2cuozFzTskMVzUvcD8h%2FScreenshot%202022-04-12%20at%2011.01.37.png?alt=media\&token=790e9bcd-059d-42cb-b38c-9a04ebccb538)

Test is running, execution in progress


# Run (locally)

Discover how to run tests in your browser with BugBug's comprehensive guide. Streamline your testing process for efficient software development. Learn more now!

This is the simplest way to run your tests (see [other ways](https://docs.bugbug.io/running-tests/running-tests)).&#x20;

To run a test with your own browser:

1. Go to test view
2. Click the `Run` button
3. Then BugBug will open a new Chrome incognito window for your test run

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhmWdSYpham7BxEcrwn2I%2Fimage.png?alt=media\&token=a84224c4-1d38-4f9d-834e-699b5b73a249)


# Run and pause here

If you want to run a test to a certain point, you can easily do this with the `Run and pause here` option.&#x20;

To use this function, you have to:

1. Hover on a step you want to run to.
2. Click `+` icon.
3. Click `Run and pause here` option.
4. The test execution window will open, and the test will run until the given step.
5. The paused mode will activate, and you can continue running step-by-step or resume a test execution.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FzL5T57SlFaB7E79FeykE%2Fimage.png?alt=media&#x26;token=99b7ec2e-46b5-4fc7-bf5d-a809e87061ae" alt=""><figcaption><p>Run and pause here in the webapp UI</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkJKh6cThWS6zLfJMURxQ%2Fimage.png?alt=media&#x26;token=f8b9380d-eb92-47c3-b1a2-2a29c047add5" alt=""><figcaption><p>Test execution window with option to resume running or run step-by-step</p></figcaption></figure>

When the test is paused, you can record new steps, change the playback position, resume execution, or modify steps from the UI. BugBug gives you a lot of control. Read more about it on the page [edit-and-rewind](https://docs.bugbug.io/workflow-tips/edit-and-rewind "mention").&#x20;


# Run in cloud

Discover how to run tests in the cloud or on your server with BugBug's comprehensive guide. Improve your testing efficiency and scalability today.

### Why run in the cloud?

Thanks to running in the cloud, you don't need to use your computer to monitor your website for bugs.

Running in the cloud is required for

* [scheduling tests](https://docs.bugbug.io/running-tests/schedules)
* integrating with build pipelines ([running via CLI](https://docs.bugbug.io/running-tests/running-via-api))
* making use of [parallel runs](https://docs.bugbug.io/running-tests/parallel-mode)

### How to run in the cloud?

1. Go to test view and choose `Run in cloud`option on the right.&#x20;
2. Then you will use BugBug cloud for your test run:
3. You will not see any window for cloud runs, just observe the status of the test steps

Now that your tests pass in the cloud, you can [set up a schedule to automatically run them every hour](https://docs.bugbug.io/running-tests/schedules).

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhbPFg3yk32Ft0T59i4ey%2Fimage.png?alt=media\&token=5a7fa9a4-fecc-44f7-abb2-f0e359995905)

{% hint style="info" %}
**Important!** You can't run tests in the cloud on a FREE plan. Start a free trial or upgrade your plan to "PRO" - see [pricing](https://bugbug.io/pricing/).&#x20;
{% endhint %}


# Schedules

Discover BugBug's comprehensive guide on how to use test schedules. Learn efficient techniques to optimize your testing process and enhance software quality.

## Run automated tests in the cloud regularly

### Why use schedules?

When you've already prepared automated tests, you should run them on a regular basis to monitor if your web app works properly.&#x20;

Fortunately, you don't need to log in to BugBug and click "Run" every week :smile:. BugBug can [run the tests in the cloud](https://docs.bugbug.io/running-tests/in-cloud-on-server) automatically and notify you about failed tests with [email notifications](#get-email-notifications-with-reports-for-scheduled-results).&#x20;

{% hint style="info" %}
To use schedule and cloud runs you need to have a paid subscription - [see pricing](https://bugbug.io/pricing/)
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F9bl4qLUOtQmgKqx1Y4sb%2F3_meptyScreen.png?alt=media&#x26;token=ffc7e243-f929-4b1d-bf2a-ef47aaa110a1" alt=""><figcaption><p>Empty screen for Schedules</p></figcaption></figure>

## Run all tests every hour

{% hint style="info" %}
Creating an hourly schedule is not the only option you can choose. You can also select and create from other available schedules, such as: \
\&#xNAN;***Every 5 minutes / Hourly / Daily / Weekly / Monthly***.
{% endhint %}

Scheduling cloud monitoring with automated tests doesn't require any engineering knowledge or additional infrastructure. Here's how to do it:

1. Make sure your selected test suite passes when you [run them in the cloud](https://docs.bugbug.io/running-tests/in-cloud-on-server)
2. Go to "Schedules"
3. Click on the "New schedule" button
4. Select "Hourly" and fill out all of the required fields
5. Select "All suites" **or** any other specific suite
6. Make sure "Schedule enabled" is turned on
7. Click on the "Create schedule" button

That's it! Based on this example, BugBug will now run your tests every hour. You will receive email notifications when all tests have been completed.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FTLvb3quBjWTjMcA85mnJ%2Fnew_schedule_options_list.png?alt=media&#x26;token=5a2deab2-f204-43ea-b4f9-8cb6bc90277e" alt=""><figcaption><p>Add new schedule modal</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSYdSVwwJBKluXdQY2MgW%2F2_scheduleModal.png?alt=media&#x26;token=ef66d8db-f2c4-4d35-92b8-348167c190ab" alt=""><figcaption><p>Filled form for with a new schedule</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FE2nWogwLwjdmE8a7Bn7K%2F1_schedule.png?alt=media&#x26;token=6b6b42fd-ca0c-48f8-8320-36c0287fbe0e" alt=""><figcaption><p>Enabled schedule with all tests running every hour</p></figcaption></figure>

## Get email notifications with reports for scheduled results

You will receive notifications with scheduled test results directly in your inbox. You can [configure who gets notifications in project settings](https://docs.bugbug.io/collaboration/alerts).

Emails notifying about failed schedules are marked with a :x: symbol.

{% hint style="info" %}
**Important!** By default all suites use the [auto-retry failed tests](https://docs.bugbug.io/organizing-tests/suites#auto-retry-failed-cloud-tests-to-prevent-flaky-tests-notifications) setting to avoid sending you false-alarm notifications from unstable, flaky tests.&#x20;
{% endhint %}

{% hint style="info" %}
**Tip!** Add a filter in your email to avoid inbox clutter. Or [disable notifications for passed runs](https://docs.bugbug.io/collaboration/alerts#choose-when-people-get-email-notifications).
{% endhint %}

![Email notifications with various statuses](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F1pmN01MLwPRnDKYTltqc%2Femail%20notifications.png?alt=media\&token=fe628ce9-946f-482d-83f5-136aa89758e2)

The email contains details about the results and direct links to the tests that failed. After clicking the link you will see a read-only report of this run from the [run history](https://docs.bugbug.io/debugging-tests/runs-history).

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F90llpevS86SoUvQU2LDC%2Femail_schedule1.png?alt=media&#x26;token=f0accff2-f972-46a0-808e-90637275a699" alt=""><figcaption><p>Email notification for a failed schedule</p></figcaption></figure>

{% hint style="info" %}
**Did you know?** You can also [integrate BugBug notifications with your Slack](https://docs.bugbug.io/integrations/slack)
{% endhint %}

## Customize schedule

If you work on a large project, you may want to have more than one schedule. For example, you can run production tests every hour but monitor your [test environment](https://docs.bugbug.io/editing-tests/variables#work-with-different-development-environments) just once a day at night.&#x20;

Create more schedules to have control over which suites are run and when.

{% hint style="info" %}
**Important!** Only suites can be scheduled - you can't schedule running individual tests.
{% endhint %}

1. Create separate test suites
2. Go to "Schedules"
3. Click the "New schedule" button
4. Fill out the name field
5. In the "Time" section, select the type of run from ***Every 5 minutes/Hourly/Daily/Weekly/Monthly*** (for this example, we'll select Daily).
6. Select the suites you want to run and set the scheduled time range
7. Make sure "Enabled" is turned on
8. Click on the "Create schedule" button

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FlXUPr4AcsqzXRC8sHQVR%2F4_newscheduleDaily.png?alt=media&#x26;token=276c47fb-9792-45d2-bf63-e48cd4185361" alt=""><figcaption><p>Test suites selected for the daily schedule</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXVaeVrx3fFHT9NKL5fcN%2F5_schedulespageOverview.png?alt=media&#x26;token=2b2e1af7-681b-41b8-ab1f-4efb46de38dc" alt=""><figcaption><p>List of all created schedules</p></figcaption></figure>


# Parallel runs

Discover the power of parallel mode in test execution with BugBug. Boost productivity and efficiency with simultaneous test runs. Get started for free now!

## Why run tests in parallel?

You can run your tests [in the cloud](https://docs.bugbug.io/running-tests/in-cloud-on-server) *in parallel*, which means that more than one test will be executed at the same time. Multiple tests will run simultaneously, resulting in **up to 32x shorter testing time.**

You can have up to 32 parallel runs, depending on your subscription plan.

## Parallel testing pricing

You can purchase parallel runs on the **PRO** and **BUSINESS** plans—either directly in the BugBug app or when selecting your plan.

Each additional parallel run costs **$80/month** for users on a monthly subscription.\
If you're on an annual plan, you’ll receive a **15% discount** on this price.

**PRO** plan pricing with extra parallels

<table><thead><tr><th width="212">Number of parallel test runs</th><th width="70">-</th><th width="73">2</th><th width="78">4</th><th width="87">8</th><th width="94">16</th><th>32</th></tr></thead><tbody><tr><td>Billed monthly</td><td>$219</td><td>$299</td><td>$459</td><td>$779</td><td>$1,419</td><td>$2,699</td></tr><tr><td>Billed yearly</td><td>$189</td><td>$257</td><td>$393 </td><td>$665</td><td>$1,209</td><td>$2,297</td></tr></tbody></table>

**BUSINESS** plan pricing with extra parallels

<table><thead><tr><th width="212">Number of parallel test runs</th><th width="70">-</th><th width="73">2</th><th width="78">4</th><th width="87">8</th><th width="94">16</th><th>32</th></tr></thead><tbody><tr><td>Billed monthly</td><td>$659</td><td>$739</td><td>$899</td><td>$1,219</td><td>$1,859</td><td>$3,139</td></tr><tr><td>Billed yearly</td><td>$559</td><td>$627</td><td>$763 </td><td>$1,035</td><td>$1,579</td><td>$2,667</td></tr></tbody></table>

## Enable parallel runs

1. Go to **Suites** view
2. Edit or create a suite
3. Change the option for Parallel cloud runs

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FLWiceSCVQhGi8kvZrnUe%2Fimage.png?alt=media\&token=03b1471e-b2b1-42b5-a5cb-3a9b75c41366)

When you trigger suite to run, your tests in that suite will run in parallel.&#x20;

{% hint style="info" %}
**Parallel testing is only possible when tests are** [**run in the cloud**](https://docs.bugbug.io/running-tests/in-cloud-on-server)

Suites run in your local browser will always run sequentially because your browser cookies and storage are shared among all incognito windows, so only one test can be run at a time.&#x20;

All cloud runs can be performed in parallel, regardless of whether they are manually triggered or [initiated via API](https://docs.bugbug.io/running-tests/running-via-api).
{% endhint %}

## Parallel runs within your organization

**Parallel runs let you run more than 1 test at the same time.**&#x20;

The number of tests you can simultaneously run within your [organization](https://docs.bugbug.io/collaboration/organization-settings#what-are-organizations) depends on your subscription plan.

If you are using BugBug with one of the paid subscriptions, you can run tests in the cloud, but only 1 test can be in progress at the same time.&#x20;

If you have multiple projects and run tests at the same time, they will be queued, they won't run in parallel - they will be executed one by one.&#x20;

**To run more tests in parallel you need to upgrade to one of the paid plans and purchase parallel runs either directly in the BugBug app or when selecting your plan.**

We support up to 32 parallel tests.


# Running via API

Discover how to run tests via API with BugBug's comprehensive documentation. Connect BugBug to your CI/CD pipeline. Streamline your automation testing process.

BugBug allows you to connect to your CI/CD pipeline. You can run tests and suites in the cloud using BugBug's [Command Line Interface](https://docs.bugbug.io/integrations/api) or public API.

### BugBug API documentation&#x20;

You can check out all helpful API commands in our online documentation in two formats.&#x20;

### 1. Swagger doc

Easy way to check your project data outside of the BugBug Web App. Just find your [API Token ](https://docs.bugbug.io/integrations/api#get-your-api-token)and play with the data.&#x20;

{% hint style="info" %}
[BugBug public API](https://app.bugbug.io/docs/swagger/) Swagger &#x20;
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FqgEnORJVeGTM2nb2LNAS%2Fswagger-banner.webp?alt=media&#x26;token=d34b2348-18ae-4efa-a5e1-5e05c074ef70" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}

#### Swagger authorization: &#x20;

Enter the [API Key](https://docs.bugbug.io/integrations/api#get-your-api-token) with the <mark style="color:orange;">**`Token`**</mark> prefix, e.g. "Token abcde12345". You will find that key in the BugBug web app in the Integration tab.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FEdG4eoBvF5N9qQwZgZyB%2FSwagger.png?alt=media&#x26;token=f7b03cb9-30f6-4e0e-9f6b-755c111704fc" alt=""><figcaption><p>Open authorization modal </p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FiSUbswKk5KNpWrLV9aIp%2FSwagger2.png?alt=media&#x26;token=3f465148-3b64-4e5f-8427-586667d2dea2" alt=""><figcaption><p>Add "Token" prefix and paste the API token</p></figcaption></figure>

### 2. Redoc API documentation

If you prefer the Redoc style you can find it with this link below:&#x20;

{% hint style="info" %}
[BugBug Public API Redoc ](https://app.bugbug.io/docs/redoc/)
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FesVbHNtlfgrLjyRL2Y64%2Fredoc.png?alt=media&#x26;token=82612eb3-2c40-45df-9b25-3848a6d86058" alt=""><figcaption></figcaption></figure>


# Test your local build or protected web page using ngrok

Learn how to test your local build or protected web page using ngrok. BugBug provides step-by-step instructions and tips for seamless testing. Start testing for free!

You can use BugBug to test your local build or private site with restricted access. For this action, you have to use a third-party tool like ngrok.&#x20;

{% hint style="info" %}
ngrok is **not** part of BugBug. It's a 3rd party tool that exposes your website to a public URL address. Before you decide to use this tool, you may want to contact your network administrator.
{% endhint %}

ngrok opens a dedicated, secure tunnel that publicizes your local port for Internet access. When your local build or protected page is accessible through the public URL address created by ngrok, BugBug can open that site through a dedicated URL and start running tests or help you record steps.

### Set up ngrok&#x20;

First, visit a ngrok website and download the application to set up a tool, then unzip it to a designated location.

When you launch ngrok, you will need to provide an auth token. You need to register and open your account on the ngrok website.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F77YucDF70YsYnacOGNSE%2Fng%20auth%20token.png?alt=media&#x26;token=0804357e-e579-4bb4-aac2-2cb1ab26db16" alt=""><figcaption></figcaption></figure>

Then open a ngrok command-line shell and copy-paste the command&#x20;

<pre><code><strong>$ ./ngrok config add-authtoken {{yourAuthToken}}
</strong></code></pre>

### Fire up the ngrok&#x20;

Once you have opened and configured the auth token for ngrok, you can publish your local build or private page to the public.

#### Set up your local build and verify the localhost port.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FdOc21hLl0FptbfoGAuY9%2FZrzut%20ekranu%202023-04-21%20095724.png?alt=media&#x26;token=f2e17c00-48a4-46a5-b25d-b4886c515ed7" alt=""><figcaption></figcaption></figure>

Then enter in your terminal **ngrok** command with the port related to your application, e.g., for **3000**:

```
$ ./ngrok http 3000
```

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FLyRKAa1MOaM0bSTVUljo%2FZrzut%20ekranu%202023-04-20%20155026.png?alt=media&#x26;token=e08c0c19-0e63-4b5f-bff2-8292df16208c" alt=""><figcaption></figcaption></figure>

Then ngrok opens a secure tunnel where your local build gets a public URL that can be used in BugBug tests (screenshot below).<br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F17wld6wsZR8JRD5FNZMy%2FZrzut%20ekranu%202023-04-21%20100114.png?alt=media&#x26;token=b3f69e44-6118-4663-a195-24ff2593e6d8" alt=""><figcaption><p>You can check out it in the browser. </p></figcaption></figure>

#### If your page is on a private server&#x20;

**If the website is running on a private server** then you are likely using a URL like `http://private.mycompany.com` to access it. In this case, you’ll create a tunnel to that URL using this command (with the private server URL swapped in):

```
$ ./ngrok http -host-header=rewrite private.mycompany.com:80
```

ngrok will print the same connection status to the console as above, with the public URL that is accessible to BugBug.&#x20;

### Record a test &#x20;

Once you successfully create a public URL with your local build or protected page, you can start recording tests with BugBug. Just use a URL provided by ngrok at the beginning of the process.<br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNTeLBaml8TwbIOsbOWL3%2FZrzut%20ekranu%202023-04-21%20102545.png?alt=media&#x26;token=bc256662-5461-494d-9040-1b8b2ee441c4" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
On the free plan, ngrok changes the URL each time it is restarted. So you need to update the test URL when ngrok provides a new one.
{% endhint %}

If you want to avoid this problem, you can use paid plans and set up a dedicated domain for your account. See the [ngrok doc](https://ngrok.com/docs/guides/how-to-set-up-a-custom-domain/) for more information.

To easily update the URL address follow these steps.

1. Open a test and go to the first step.&#x20;
2. Then change the URL address <br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FraznaE9fpfgOsT0Hy0xE%2Fng%20url.png?alt=media&#x26;token=5dd26400-4124-4b98-874a-e76e5fdad61e" alt=""><figcaption></figcaption></figure>

To make it easier to maintain a large number of tests, use a local variable that helps you to change the URL only in one place for all tests that use it.

<div><figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FDFG8T0C08BpSte1zPurz%2FZrzut%20ekranu%202023-04-21%20104317.png?alt=media&#x26;token=f61b6625-90b7-41a6-b180-75eedb0f6709" alt=""><figcaption><p>Create a variable </p></figcaption></figure> <figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F3hvknFbC5iLgyXHuUGSB%2FZrzut%20ekranu%202023-04-21%20104402.png?alt=media&#x26;token=1e77596f-ca7d-4c0f-9d8a-b71da2b88ccd" alt=""><figcaption><p>Use it in test </p></figcaption></figure></div>

For more info about variables, please visit [Variables](https://docs.bugbug.io/editing-tests/variables) in our documentation.

### Alternatives

Like many solutions, ngrok has alternatives, and you can choose something else.

* [Serveo](http://serveo.net/)
* [Localhost](http://localhost.run/)
* [Cloudfared](https://github.com/cloudflare/cloudflared)
* [LocalTunnel](https://github.com/localtunnel/localtunnel)


# Waiting conditions

Learn effective waiting conditions to prevent failed tests. Improve your test automation process with BugBug's expert guidance. Start your test automation today.

## Smart waiting before running a step

Before running each test step, BugBug will do a series of checks if your page is ready for this action.&#x20;

For example, before BugBug tries to click a button, it will check if the page finished loading, if the button exists and if it's visible. If those conditions are met, BugBug will attempt to click the button. Such conditions are called **"*****Waiting conditions*****"**.

Benefits:

* **more stable tests**
* you don't need to hardcode manual delays
* more intelligent tests running, behaving more like a human and not a machine

## Available waiting conditions&#x20;

### Document readyState is complete

BugBug waits until your page is ready to interact with and if all the basic assets are loaded. In technical terms this is waiting for `onload` window event.

### Page network requests are finished

BugBug waits until your page has finished loading additional data via other network requests.&#x20;

Even after the page is loaded, your web app needs to request additional data from a server. BugBug will wait until your server requests are more or less finished - by default BugBug will stop waiting when there are not more than 2 unfinished requests for more than 1 second. You can change this in Project Settings.

### Element is visible

BugBug will not interact with the element until it is visible. For example, if you have a "Done" button than only appears after several seconds, BugBug will wait until it appears. That's why you should avoid adding manual delays/sleep.

### Element is not covered by the other one

Same as in "Element is visible" above. BugBug will try not to click something that is covered by another element.

### Element is not animating

This ensures that the animation of the element stopped before BugBug interacts with it.&#x20;

For example, if you have a collapsed section that expands with an animation, BugBug **will wait until it is fully expanded before interacting with its contents**.

This waiting condition is enabled if during the recording you clicked an element that was not animating. If the element has a looping animation, BugBug will disable this waiting condition by default.

### Element must be active

This applies to form elements, that can have a `disabled` attribute. BugBug will hold the step execution until the form element is active. This waiting condition is automatically disabled if during the recording you actually clicked on a disabled element.

### Element has focus

This applies to text input elements. BugBug will wait before typing the letters until it verifies that a text `input` or `textarea` has focus, (meaning that the blinking typing cursor is present the right field)

### Element has an attribute

BugBug will check if element has a attribute with expected value, before interacting with it.

You can add this waiting condition manually, by clicking on "Add condition" in step's "Waiting condition" section.

It requires the expected value to be specified using a specific pattern: `key="value"`, where `key` is the attribute name and `value` is the expected attribute value, e.g. `class="bugbug"`.

### Page will navigate after step execution

This is a special waiting condition that is added automatically by BugBug while recording. If BugBug notices that after a click there's a change in the URL, BugBug will not continue running the next step immediately - it will wait until the URL changes. This also applies to URL history state changes for Single Page Applications.

## Enable or disable waiting conditions

Global waiting conditions can be set up in the project settings.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F4lP77zb3Mk7qsLFDeguj%2FScreenshot%202022-04-11%20at%2018.39.36.png?alt=media\&token=f7e33698-b850-4d27-b480-92d2a945bb72)

You can override waiting conditions per each step. Sometimes you need to disable one of them to prevent unnecessary failed tests.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FRkz8oaNZfPO9pTFytqER%2Fimage.png?alt=media\&token=e9f2b38e-a154-418e-ac51-2396430bef03)

## Skipped waiting conditions

If some waiting conditions are not met, BugBug will anyway try to perform the action. For example, if the page networking has not finished, BugBug will anyway click the button after 30 seconds.&#x20;

You will be notified about skipped waiting conditions by a different green indicator![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FK728O2urlEVlpTbR6p46%2FScreenshot%202022-04-11%20at%2017.59.19.png?alt=media\&token=74c4ecc5-1fe2-45a1-8a4e-186ca914dda8)

[More about test statues](https://docs.bugbug.io/running-tests/statuses)


# Smart click

Discover BugBug's smart click feature to prevent failed tests efficiently. Improve your testing process and enhance software quality with ease.

## Simulating real cursor clicks

BugBug simulates real clicks as if the user was moving a mouse. So if the element is not visible or covered by something else, it is not possible to click it.&#x20;

BugBug will not fake-click the elements with JavaScript events.&#x20;

## Smart preventing incorrect clicks

BugBug prevents randomly failed tests by being smart about clicking elements.

**1) BugBug will retry the click if the right element was suddenly covered**

After clicking an element, BugBug will check if the right item was clicked. This prevents a situation when the click event was received by a different element, for example, you wanted to click a button but it was covered by a cookie popup overlay or scrolled outside of the viewport.&#x20;

**2) BugBug will click the element even if it's partially covered**

Your test will not fail if the button is partially covered. BugBug will click the remaining visible button area.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVNoXB6U1dc8WTNkxnlNv%2FScreenshot%202022-04-11%20at%2018.50.08.png?alt=media\&token=99d9f554-5666-4300-8054-4e2037ac945c)

## Smart position detection&#x20;

BugBug will first try to click the element in the center, but if this will not work, BugBug will automatically find different coordinates for clicking an element, that is not covered by anything else and is visible on the screen.&#x20;

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F1tGZQKG3XgqKjjAymLSp%2FScreenshot%202022-04-11%20at%2018.40.32.png?alt=media\&token=5967df3b-26a4-47a5-8046-17c148eed278)


# Smart scroll

Discover how to prevent failed tests with smart scroll. Improve your test efficiency and reliability using BugBug's smart scroll feature. Learn more now!

BugBug simulates [real user clicks and mouse movements](https://docs.bugbug.io/preventing-failed-tests/smart-click), so the element needs to be visible in the viewport to actually click it.

BugBug will try to behave like a human: we will automatically attempt to scroll the page to see the element and interact with it.

**So you don't need to maintain the scroll actions!** :tada:

Your tests <mark style="color:green;">**will not fail**</mark> if:

* some content on the page changed and pushed the clickable element down outside of the browser viewport
* some fixed popup or an ad covered the element completely, but it is still reachable if you scroll more

{% hint style="info" %}
You can still [manually add scroll steps](https://docs.bugbug.io/editing-tests/manually-creating-the-test), for handling more complex scrolling and items with their own overflow scroll.&#x20;
{% endhint %}


# Selectors

Learn how to prevent failed tests with efficient selectors. BugBug's comprehensive guide provides valuable insights and best practices. Start optimizing your testing process today!

What is a selector?

Human users just see the page and use their intelligent brains to **find the right element to interact with**.

Computers on the contrary need more specific instructions to know what to click. **"Selector" is a way of describing a specific element on your page that can be clearly identified.**&#x20;

For example, a *selector* can describe an instruction to `Find an element with a text "Add to cart"` or `Find the first element with id "primary-button-submit"`

## Automatic vs. manual selectors&#x20;

**Automatic selectors** --> BugBug creates them automatically when your [record a test](https://docs.bugbug.io/recording-tests-steps)

**Manual selectors** --> You create them on your own using your own human intelligence. Sometimes manual selectors is the only way of creating a reliable automation testing

{% hint style="info" %}
**See** [**our simple tool for building XPath selectors without code -->**](https://bugbug.io/xpath-selector-builder/?ref=docs)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FeZuqZJE019x7Mf3MJLz7%2FScreen%20Shot%202022-11-03%20at%2011.37.32.png?alt=media\&token=258375ab-7891-4507-baac-7e9282d965f8)
{% endhint %}

## Automatic selectors

If you are recording the tests, you don't need to be worried about selectors too much. During the recording, BugBug will automatically create several selectors and decide which is the best.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FdkJQ2Mh5v86noXyDw9Q1%2Fimage.png?alt=media&#x26;token=f81e56ba-1ee2-4f5b-a2a5-80adbe4629a8" alt=""><figcaption><p>Selector generated by BugBug during recording session</p></figcaption></figure>

## Manual selectors

You can also enter your own custom XPath or CSS selector. In the details of selected test step click on existing selector and select "Customize" option (last position).

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FApEq2xEopvdf6SbVmVtC%2Fimage.png?alt=media&#x26;token=96d95702-4157-4fcf-9bbe-40c75af651d8" alt=""><figcaption><p>Selector customization</p></figcaption></figure>

BugBug can understand selectors in the following formats:

* CSS selectors, for example `[id="submit"]`
* XPath selectors, for example `//*[@id="submit"]`

Manual selectors sometimes is the best way of creating stable automated tests in complex apps.

For example you if you have a long table with buttons inside each row, you may need to create a selector that first points to the right row and then to the right action button.&#x20;

{% hint style="info" %}
**Learn the basics of HTML**

To write reliable selectors you need a basic knowledge of HTML and understand what are *tags*, *attributes*, *parents* and *children*. You can learn it in our **extensive tutorial in the** [**no-code XPath selector tool**](https://bugbug.io/xpath-selector-builder/?ref=docs).
{% endhint %}

### Nested selectors

BugBug allows you to create nested selectors. This is especially helpful when dealing with dynamic table data or nested iframes. Each selector narrows down the context, which gives the superpower to make the right selector for an element.

In the below example, BugBug will first narrow down the context of the document with&#x20;

`//*[@data-testid="todo-list"]`

and then will find a **child** of this element using the next selector `//li`

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fd2j8Nk1mrWjtuxyIOGWo%2Fimage.png?alt=media&#x26;token=162eebed-481f-4bef-90d8-1b280aab64bc" alt=""><figcaption><p>Nested selectors with BugBug.</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FKajDyTdmwXKRNgyrx5GO%2Fimage.png?alt=media&#x26;token=780496e5-821c-48db-a0e6-76765d6321e4" alt=""><figcaption><p>The right box is the parent selector, the pink box is the child selector.</p></figcaption></figure>

In nested selectors, you can refer to **parent**, **child,** or **sibling**.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNzCfhcumhHicwUrpKfuT%2Fimage.png?alt=media&#x26;token=f34dfdf7-f34c-4864-93bb-6af03d8fd615" alt=""><figcaption><p>Nested selectors options.</p></figcaption></figure>

If you want to read more about XPath and selectors in general you can check out our [BugBug Selector Builder](https://bugbug.io/xpath-selector-builder/).

## Set priority of automatic selectors

You can decide about the priorities of automatic selectors and configure your custom attributes in [project settings](https://docs.bugbug.io/preventing-failed-tests/project-settings). This is an advanced setting and usually there's no need to change it.&#x20;

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FbKFwKP65w8x8P8EFDIwk%2FScreenshot%202022-04-11%20at%2019.08.53.png?alt=media\&token=b921d690-19d8-4fe0-bb3f-d73f1657cd94)

## Use custom attributes for selectors

To create robust tests, your app should be coded with additional special attributes that are dedicated to testing automation. The usual convention is to use `data-test` or `data-testid` attributes.

BugBug will automatically prioritize such robust selectors when it recognizes them. So if you're working on a complex app, **we highly recommend** that you talk to your front-end developers and ask them to add such attributes. This will also make their life easier because they will see from the code that an element is a subject of testing automation.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fmx9CxOn0e8vCLzp4TkuR%2Fimage.png?alt=media\&token=46bb80ef-54b1-47fe-a446-b0555c9bdccd)

## The "element not found" error

When your test fails with an error "element not found" or "element not visible", this might be caused by an incorrect [selector](https://docs.bugbug.io/preventing-failed-tests/selectors).

Common problems with selectors are:

* It is too specific, contains some kind of unique ID that is changing every time you run the test
* It is depending on the order of elements, but the order of elements changes, like a list of products in e-commerce might change every day (you can avoid this problem by [building a selector manually](#automatic-vs.-manual-selectors))
* It is pointing to more than one element and some of them are not visible (for example your page has some hidden buttons with `display: none`)
* the text in your app changed and you were using a [text-based selector](#fix-text-based-selectors)&#x20;

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fg89baEK9bYPbv1mpau8R%2FScreenshot%202022-04-12%20at%2010.41.05.png?alt=media\&token=fc38bccf-7ae8-4d94-a7e5-3b057861839c)

## Tips on fixing selectors

### Use Chrome debugging

Chrome is very powerful in debugging and it's worth learning [how to use Chrome developer features](https://docs.bugbug.io/debugging-tests/debug-in-chrome).&#x20;

### Copy selector to clipboard

* Click the button near the selector field&#x20;
* Open Chrome dev tools
* Click cmd+f
* Paste the selector in the search field
* Chrome will highlight the element that is matching your selector
* If no element is matched, you may try to manually update the selector or just [re-record the step](https://docs.bugbug.io/recording-tests-steps/re-recording-steps)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FIQWcH0gfKFjVCiLjJZKu%2Fimage.png?alt=media\&token=708489b4-a602-434d-9470-d45dbc0e9288)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fo3cyOjY3FqlMkG7qKgo7%2FScreenshot%202022-04-12%20at%2010.49.54.png?alt=media\&token=4aa112e2-757b-4226-87b4-3e1958b02496)

### Prevent incorrect selectors

Prevent failed tests by using [custom attributes for selectors](#use-custom-attributes-for-selectors)

### Fix text-based selectors

Some selectors are just finding any element that contains a specific text. Here's an example of such a selector:

`//DIV[normalize-space(text())="Create account in Example Project"]`

{% hint style="info" %}
**Tip:** you can [use variables in selectors](https://docs.bugbug.io/editing-tests/variables#using-text-variables)
{% endhint %}

If this text changes in your app, you will get an "element not found" error. The element is in fact still there, but the selector does not work anymore. You can [manually update](https://docs.bugbug.io/editing-tests/manually-creating-the-test) the selector or [re-record this step](https://docs.bugbug.io/recording-tests-steps/re-recording-steps).


# Timeout

Discover effective strategies to prevent failed tests due to timeouts. Learn how to optimize your test environments and code execution for smooth test runs.

BugBug will not immediately fail the test if it can't click an element right away (or do any other interaction or assertion).

By default, it will wait for 30 seconds and reattempt to run the test step and hold until [waiting conditions](https://docs.bugbug.io/preventing-failed-tests/waiting-conditions) are met. If it was not possible to continue the test after such time, the test will be marked as failed.

## Configure global timeout

You configure the timeout waiting time in Project settings.

Increase the timeout if your page is slow or fails in the cloud.

Decrease the default timeout if you don't want to wait 30 seconds for failed tests results.

Increase the timeout for cloud runs if your [local runs are passed but cloud runs fail](https://docs.bugbug.io/troubleshooting/cloud-tests-sometimes-failing).

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQDkpjcmwuUYOLSSQDQHL%2FScreen%20Shot%202022-11-24%20at%2013.20.21.png?alt=media&#x26;token=2ac1af3f-abcc-423d-9b55-8bb403925d16" alt=""><figcaption></figcaption></figure>

## Change timeout for individual steps

You can override the timeout for each step separately

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FdkUGZF5M3AI7PAIScCTi%2FScreenshot%202022-04-11%20at%2019.22.39.png?alt=media\&token=969ce483-dc8e-4263-ad9d-c5aff531a9ea)


# Delay / Sleep

Learn how to prevent failed tests and improve test reliability with delay and sleep techniques. Explore BugBug's comprehensive guide for efficient test execution.

Using manual delay is not recommended because BugBug has other ways of [smart waiting](https://docs.bugbug.io/preventing-failed-tests/waiting-conditions).&#x20;

But sometimes you may want to hardcode a delay for a step, as this might be a faster way to fix the test instead of debugging.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FxiksPKFV9ae5EKKQSCks%2FScreenshot%202022-04-11%20at%2019.27.20.png?alt=media\&token=4d880d62-ec87-43d9-9e91-16dfc362fa67)


# Project settings

Learn about BugBug's project settings. BugBug's comprehensive guide provides effective strategies and solutions. Start testing for free now!

Project settings contain various global parameters and configurations for all your tests and suites.

**What can you do in the project settings?**

**General tab:**

* Change [project](https://docs.bugbug.io/organizing-tests/projects) name&#x20;
* Change timezone
* Set the default [timeout](https://docs.bugbug.io/preventing-failed-tests/timeout) for local and cloud runs - this can help you to solve a situation when [cloud tests are sometimes failing](https://docs.bugbug.io/troubleshooting/cloud-tests-sometimes-failing)
* Decide if you want to close the window after a successful test run automatically

**Browser tab:**&#x20;

* Enable/disable incognito mode for testing sessions, cookies, or local storage &#x20;
* Set a custom user-agent or custom HTTP request headers (for example, you can use it to let BugBug access an environment behind a [VPN or a firewall](https://docs.bugbug.io/troubleshooting/vpn-or-a-firewall))
* Set browser language&#x20;

#### Screen size tab:&#x20;

* Set window width and height for desktop or mobile screen size - this enables you to [test mobile resolutions](https://docs.bugbug.io/workflow-tips/mobile-version-testing)

**Selectors tab:**&#x20;

* Set and define the priorities for the automatic smart [selectors](https://docs.bugbug.io/preventing-failed-tests/selectors), and define your own custom attributes, input names, text content, id, href, class name, etc.&#x20;

**Waiting conditions tab:**&#x20;

* Set default behavior of [waiting conditions](https://docs.bugbug.io/preventing-failed-tests/waiting-conditions)<br>

**Note:** If you're looking for an [API token](https://docs.bugbug.io/running-tests/running-via-api) see the [integrations](https://docs.bugbug.io/integrations) tab

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FZqKd4mqBmahatSex2zp3%2F1projectSettingsMain.png?alt=media&#x26;token=42ed7ceb-23eb-40d1-b12c-0b5083899ce2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHjLJOmmpx0hoszZXyx36%2F1projectSettingsBrowser.png?alt=media&#x26;token=f43a5151-1abc-4844-835d-bd3ff264f7ba" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FZuqPWbHjxddo56Q8tnjz%2F1projectSettingsScreensize.png?alt=media&#x26;token=2fc3e974-8b86-4072-8234-0283e480187e" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F7GQFHhq5iNiPxan1YKsl%2F1projectSettingsSelectors.png?alt=media&#x26;token=fc92136e-d166-4e29-8edf-6cb250b739a4" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FmINbyzLq6XsTkeF8eeZP%2F1projectSettingsWaitingconditions.png?alt=media&#x26;token=219311ab-e417-4cdd-9bf8-debbbd21cac9" alt=""><figcaption></figcaption></figure>


# Runs history

Explore BugBug's Runs History for efficient test debugging. Access logs, track progress, and review your past tests and suites runs. Try it now!

## Why use runs history?

In the "Runs history" tab you can review your past tests and suites runs. Access the reports, errors, and logs of your runs to debug them.

* review past runs (both local and cloud)
* clear history
* stop all running tests
* navigate to a specific test that fails
* download a suite run report

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FENQYBFOFP0a6gzcoNPbu%2FScreenshot%202022-04-12%20at%2010.06.04.png?alt=media\&token=2dbec99d-7460-4c84-9cdc-d84c3baa5ab0)

{% hint style="info" %}
**Important!** The "Tests" tab also shows tests initiated via a suite. This tab simply shows all your past test runs.
{% endhint %}

## Read-only test details

When you click a test in the "Runs history" it will open its details in a read-only mode. This is because your current version of the test might be different that the one you're reviewing.

To quickly jump to the most up-to-date version of this test, click the "Go to test" button.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FFjNTNzAW0ix2APsDvXnA%2FScreenshot%202022-04-12%20at%2010.07.17.png?alt=media\&token=081646d2-dfdf-4992-b08e-8608d4501486)

## Download a suite run report

When you enter a specific test suite details page apart from the general information, execution statuses, and so on, you can also download a report with a summary.

Simply just click on the "**Download PDF report**" button to generate and download one.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCe0rcIJMUv6AjW48RnTd%2F1downloadButton.png?alt=media&#x26;token=8e30ce38-c381-47f7-929a-53b0402faf26" alt=""><figcaption></figcaption></figure>

As a next step, you can add additional information eg. a reason why some tests are skipped.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FTWPYqyXGZ9puHa2hM2CH%2F1confirmationModal.png?alt=media&#x26;token=2e74c8bb-1bbb-4808-8039-47ccc68bc842" alt=""><figcaption></figcaption></figure>

When you confirm the action, and save the file as PDF you can locally preview it or share it with other related parties.


# Screenshots

Discover BugBug's powerful debugging tests screenshots feature. Streamline bug identification and resolution with clear visual evidence. Try it now!

You can use screenshots to debug your tests and understand what was the reason for the failure.&#x20;

When a test step is executed, **BugBug automatically takes screenshots**:

* of the whole window
* of the individual element

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FrZjlWLhBgovJ7MVa2Yol%2Fimage.png?alt=media\&token=89bef946-142a-4c2d-b862-2cfb9bc6206a)

Click the screenshots to see the full preview.

BugBug also keeps the screenshots history, so that you can also compare screenshots from previous runs. Just go to the ["Runs history" tab](https://docs.bugbug.io/debugging-tests/runs-history).&#x20;

{% hint style="info" %}
**How long screenshots are kept?** It depends on your subscription plan, learn more in [pricing](https://bugbug.io/pricing/).
{% endhint %}

&#x20;


# Debug in Chrome

Discover effective debugging techniques in Chrome with BugBug. Streamline your test debugging process and solve issues efficiently. Try it for free now!

When your test failed, the browser window will not close automatically. You can debug the test using all the native Chrome features, DOM navigator, network tab, etc. This is very useful when you need to [fix selectors because an "element was not found"](https://docs.bugbug.io/preventing-failed-tests/selectors#tips-on-fixing-selectors).

To open Chrome Dev tools **just right click on your page and click "Inspect".**

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F1DCMhBIrCVN6np1RdNUk%2FScreenshot%202022-04-12%20at%2010.14.50.png?alt=media\&token=92827621-1b6c-4389-956d-7a3887104472)

&#x20;


# Breakpoint (run step-by-step)

Master the art of debugging tests with BugBug's comprehensive guide on using breakpoints. Enhance your troubleshooting skills and boost software quality.

You can run a test until a certain point and then pause, so that you can investigate what you need using in-browser [Chrome debugging tools](https://docs.bugbug.io/debugging-tests/debug-in-chrome).

## Run step-by-step

BugBug supports step-by-step execution of the tests. To do this, click `Run and stop here` between steps. This will activate the **paused mode**. In this mode, you can run a test step-by-step and completely control an execution process.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FS3kJzqmnhiVm4qNcNxvs%2Fimage.png?alt=media&#x26;token=b75f3e10-e12f-4eac-958f-7175fb7553e8" alt=""><figcaption><p>To enable step-by-step execution, click on the "Run and stop here" action.</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FgRMEhR3OE8GDyA7yPW99%2Fimage.png?alt=media&#x26;token=8dc448ef-672b-46d4-8e5c-91a39477005b" alt=""><figcaption><p>Paused mode. To execute next step click on the "Run next step and pause" icon</p></figcaption></figure>

When a test is paused, a browser window with a test will display BugBug's overlay with options to control the execution process.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fwvgnn4Ehlc3VbdPewBRD%2Fimage.png?alt=media&#x26;token=46d07999-34bd-41bb-9552-5b9b8caf08e9" alt=""><figcaption><p>Paused mode in a window with a test. BugBug's overlay has options to control the execution process</p></figcaption></figure>

BugBug allows you also to rewind or fast-forward the execution process. You can read more about it here [edit-and-rewind](https://docs.bugbug.io/workflow-tips/edit-and-rewind "mention")


# Error codes

### Element & Selector Errors

#### ELEMENT\_DOES\_NOT\_EXIST

It was not possible to find the element using the selector

**When occurs?**:

* Element doesn't exist
* Element removed from DOM during execution
* Page is not ready yet, so element is not available

**What to do?**:

* Ensure selected selector is stable (e.g., it does not contain any dynamic content)
* Re-record this step
* Add waiting conditions

#### ELEMENT\_REMOVED

Element was found but unexpectedly removed during the step execution and BugBug was not able to find it again.

**When occurs?**:

* Parent element removed
* JavaScript removes element
* Dynamic reload
* SPA navigation
* Iframe removed

#### SELECTOR\_REQUIRED

Related step has an empty selector.

**What to do?**:

* Provide a valid custom selector
* Re-record this step again

#### INVALID\_ELEMENT\_SELECTOR

Provided element selector is invalid.

**When occurs?**:

* Malformed XPath eg. `//div[[@id`
* Invalid CSS eg. `invalid:selector`
* Unclosed brackets eg. `div[@id="test"`
* Invalid pseudo-selector eg. `div:fst-child`

**What to do?**:

* Re-record this step
* Fix selector manually (e.g., use selector editor)
  * Fix syntax errors
  * Validate in DevTools
* Use [XPath Selector Builder](https://bugbug.io/xpath-selector-builder/), if needed

#### INTERACTION\_POSITION\_OUT\_OF\_VIEWPORT

It was not possible to reach interaction coordinates in the current viewport size.

**When occurs?**:

* Click at (2000,1500) in 1920x1080 viewport
* Selector points to container
* Element off-screen

**What to do?**:

* Check the selector, perhaps it incorrectly points to a large container instead of its child element
* Check the scroll coordinates in previous steps and make sure that the element is fully scrolled to view
* Check the interaction position settings

### Frame & Context Errors

#### FRAME\_DOES\_NOT\_EXIST

Related step was supposed to be executed in an iframe but the iframe was not found.

**When occurs?**:

* Iframe removed during step execution
* Conditional iframe
* Wrong iframe selector

**What to do?**:

* Take a look at the previous steps and find a "Switch context" step
* Make sure it uses a correct selector to a correct iframe
* You can also re-record some steps again
  * remove the "switch context" step and the following iframe steps
  * use "record from here"

#### FRAME\_LOADS\_TOO\_LONG

BugBug waited for a requested frame until it is ready, but loading took too much time.

**When occurs?**:

* Iframe stuck loading
* Third-party issues
* 404/server error
* CORS/CSP blocking

**What to do?**:

* Take a look at the previous steps and find a "Switch context" step.
* Make sure it uses a correct selector to a correct iframe.
* Re-record some steps again
  * remove the "switch context" step and the following iframe steps
  * use "record from here"
* Increase timeout
* Check console for CORS/CSP errors
* Check console for network errors

#### WINDOW\_OR\_TAB\_DOES\_NOT\_EXIST

Window or tab with specified number does not exist

**When occurs?**:

* Switch to tab #3 with only 2 tabs
* Tab closed during execution
* Different tab count than while recording

**What to do?**:

* Take a look at the previous steps and find a "Switch context" step
* Record this step again by using "record from here" or manually update the tab number
* Verify tab number (default tab number is 0)
* Ensure tabs are opened
* Check for accidental tab closures

#### TAB\_CLOSED

User closed tab during running test

**When occurs?**:

* Manual tab closure
* Clicking X button
* Keyboard shortcut Cmd/Ctrl+W

**What to do?**:

* Don't interact with browser during test
* Rerun without interference

#### WINDOW\_CLOSED

Window closed while the test was running

**When occurs?**:

* Too many "Close tab" steps
* Manual window closure
* Closing last tab
* Unexpected window\.close() calls

**What to do?**:

* Make sure you don't have too many steps that close tabs
* Don't close window during test
* Ensure at least one tab remains open
* Check for unexpected window\.close() calls

#### WINDOW\_MINIMIZED

The window with the running test has been minimized

**When occurs?**:

* User minimizes window
* Keyboard shortcut
* Forced by another app

**What to do?**:

* Don't minimize the window when a test is running
* Browser cannot execute steps when window is minimized
* Keep window visible during test execution
* Rerun without minimizing

#### UNEXPECTED\_WINDOW\_STATE\_CHANGE

The window with the running test has been minimized or lost focus by other user actions

**When occurs?**:

* MacOS Space switching
* Clicking other app
* System dialog
* Screen saver activation

**What to do?**:

* Avoid minimizing the window while a test is running
* If you are using MacOS, avoid switching from space with pending test run to another
* Disable notifications/screen saver
* Don't interact with other apps during test

### Form & Input Errors

#### UNCHANGABLE\_ELEMENT

Wrong type of element - expected a form input, textarea, select, checkbox or radio.

**When occurs?**:

* "Change"/"Type" step on `div`, `span`, `p`, `button` or other non-input element
* "Select option" step on non-select element
* "Clear" step on non-input element or element which value cannot be cleared

**What to do?**:

* Check if selector points to correct element
* Update selector to form input (input/textarea/select/checkbox/radio)
* Re-record step
* Use different step type

#### TYPED\_TEXT\_DIFFERENT\_THAN\_EXPECTED

The typing step was completed, but the end result was not as expected

**When occurs?**:

* User interference
* JavaScript modifies value in background
* Auto-complete changes value

**What to do?**:

* Rerun the test and remember not to interact with the page during execution
* Check for JavaScript modifications in your code
* Switch "Type" step to "Change" step
* Contact support if problem persists

#### INVALID\_FIELD\_VALUE

Could not verify that the value in the form was changed properly

**When occurs?**:

* New field value doesn't match expected value due to invalid execution
* User interference
* JavaScript modifies value in background
* Auto-complete changes value

**What to do?**:

* Verify value is valid
* Check for validation/event handlers that might modify the value
* Switch "Type" step to "Change" step
* Add wait after change to allow value to settle

#### INVALID\_OPTION\_INDEX

Provided option index is not a number

**When occurs?**:

* Index "abc" instead of "2"
* Variable resolves to non-numeric

**What to do?**:

* Use numeric index (0,1,2)
* Check variable value, if variable is used
* Use "Select by text/value" instead

#### MISSING\_OPTION\_VALUE

Option with provided value does not exist on available options list

**When occurs?**:

* Value "premium" doesn't exist
* Options changed since recording
* Dynamic options differ
* Typo in value

**What to do?**:

* Verify option exists
* Re-record step
* Check for typos
* Use select by text/index instead
* Ensure dynamic options loaded

#### MISSING\_OPTION\_TEXT

Option with provided text does not exist on available options list

**When occurs?**:

* Text "Szczecin" doesn't exist
* Text changed
* Language/locale changed
* Whitespace mismatch

**What to do?**:

* Verify exact text match (including whitespace)
* Re-record step
* Use "Select by value/index" instead
* Check locale changes

#### MISSING\_OPTION\_INDEX

Option with provided index does not exist on available options list

**When occurs?**:

* Index 5 with only 3 options
* List shortened
* Conditional options missing
* Zero-based indexing confusion

**What to do?**:

* Verify index exists (first option always has index 0)
* Use "Select by text/value" instead
* Check if app uses dynamic options
* Re-record step

#### SELECT\_OPTION\_FAILED

BugBug was not able to select expected option

**When occurs?**:

* Selected value differs from expected
* Options changed since recording
* Browser bug
* Multi-select fails

**What to do?**:

* Verify if options are correct
* Check for event handlers that might revert the selection
* Re-record step
* Contact support if problem persists

#### MULTIPLE\_OPTIONS\_WITH\_VALUE

Could not verify which option should be selected - multiple select options reference the same value

**When occurs?**:

* Duplicated options
* Application bug

**What to do?**:

* Use "Select by text/index" instead
* Contact support if problem persists

### Navigation & Page Loading Errors

#### MISSING\_GOTO\_STEP

Test doesn't start with goto step

**When occurs?**:

* First step is Click
* Deleted goto step
* Manual test without goto
* Copied steps without goto

**What to do?**:

* Every test should begin with a navigation to a URL, so you need to add a "Go to URL" step at the very beginning of the test
* Re-record test from the beginning

#### INVALID\_URL

Provided URL is not valid

**When occurs?**:

* "htp\://example.com" (typo)
* Missing protocol "example.com"
* Spaces in URL
* Variable resolves to invalid URL

**What to do?**:

* Check if URL starts with: "http\://" or "https\://"
* Verify variable resolves correctly
* Fix other typos
* Test URL in browser

#### PAGE\_LOADING\_ERROR

BugBug handles browser's error pages. Full list of those errors can be found [here](https://support.google.com/chrome/answer/95669?hl=en#zippy=%2Cpage-loading-errors):

**When occurs?**:

* Connection timeout (e.g. "ERR\_CONNECTION\_TIMED\_OUT")
* Internet disconnected (e.g. "ERR\_INTERNET\_DISCONNECTED")
* Server down (e.g. "ERR\_CONNECTION\_REFUSED")
* DNS failure (e.g. "ERR\_NAME\_NOT\_RESOLVED")
* SSL protocol error (e.g. "ERR\_SSL\_PROTOCOL\_ERROR")
* Invalid certificate (e.g. "ERR\_CERT\_INVALID")

**What to do?**:

* Verify URL accessible
* Check internet connection
* Verify server running
* Check SSL certificate
* Try URL in browser
* Contact server admin

### JavaScript & Code Execution Errors

#### CODE\_EXECUTION\_ERROR

JavaScript code has runtime error

**When occurs?**:

* Typo "consle.log"
* Syntax error missing brace
* Runtime error element doesn't exist
* ReferenceError undefined variable

**What to do?**:

* Fix syntax errors
* Test in browser console
* Add error handling
* Verify elements/variables exist
* Check console for details

#### INVALID\_EXECUTION\_RESULT

Function didn't return boolean, which is required for assertion

**When occurs?**:

* Returns string "true" not boolean
* Returns undefined/null
* Returns number 1
* Async doesn't resolve to boolean

**What to do?**:

* Ensure returns boolean (true/false)
* Convert with !!value or Boolean(value)
* Test in console

### Variable Errors

#### VARIABLE\_DOES\_NOT\_EXIST

Variable used in step definition doesn't exist

**When occurs?**:

* Using {{userEmail}}, which was never created
* Typo {{userName}} vs {{username}}
* Variable in different test
* Case-sensitive mismatch

**What to do?**:

* Make sure that you use a proper variable name
* Create variable before using (Set variable step)
* Check spelling and case
* Verify in same test/suite
* Use correct syntax {{variableName}}

#### VARIABLE\_NESTING\_LIMIT\_EXCEEDED

Nesting variables is limited to 3 levels and the variable you used contains too many nesting levels.

**When occurs?**:

* {{var1}} contains {{var2}} contains {{var3}} contains {{var4}}
* Complex chains
* Circular references

**What to do?**:

* Simplify to max 3 levels
* Break into separate steps
* Avoid circular references
* Use Execute step for complex values

### Event & Interaction Errors

#### EVENT\_DISPATCHED\_ON\_INVALID\_ELEMENT

BugBug found the element, but could not click it - some other element interrupted the click

**When occurs?**:

* Modal overlay covers button
* Cookie banner covers element
* Loading spinner appears
* Fixed header covers element

**What to do?**:

* Check the screenshots and analyze where the cursor is located
* Investigate why the target element could not be clicked
* Close covering elements first
* Add wait for covering elements to disappear
* Add additional test steps using "record from here" to make sure the clickable element is accessible

#### EVENT\_DISPATCH\_FAILED

BugBug found the element, dispatched the requested event, but could not resolve the event correctly

**When occurs?**:

* Need double-click not click
* Event listener prevents default
* Element disabled or pointer-events:none
* Framework blocks event
* Incorrect event type used

**What to do?**:

* This usually occurs when an incorrect event type is used (e.g., using "click" instead of "double-click")
* Try different step type
* Check if element enabled/interactive
* Verify no CSS preventing interaction
* Re-record step

### Other Step-Specific Errors

#### FAILED\_WAITING\_CONDITIONS

Waiting conditions timeout

**When occurs?**:

* Element never visible
* Network never idle
* Element can't get focus
* Element stays covered

**What to do?**:

* Increase step timeout
* Review and adjust conditions
* Check if achievable
* Remove/modify problematic conditions
* Add explicit waits

#### PROMPT\_DOES\_NOT\_EXIST

Prompt not found

**When occurs?**:

* Answer prompt step with no dialog
* Previous step didn't trigger alert
* Dialog auto-closed
* Page uses custom modal not browser prompt

**What to do?**:

* Ensure the prompt has been opened in a previous step
* Don't close the prompt manually when a test is running
* Remove Answer prompt step if none appears
* Check for custom modals

#### UNHANDLED\_PROMPT

Execution of this step was blocked by unhandled prompt

**When occurs?**:

* Alert without Answer prompt step
* Unexpected window\.confirm()
* JavaScript prompt() without handler
* "Leave site?" dialog

**What to do?**:

* Ensure the prompt has been closed in a previous step
* Record or add manually "Answer prompt" step to close the prompt
* Identify triggering step and add handler
* Check for unexpected prompts
* Disable beforeunload events if possible

#### NEXT\_STEP\_ELEMENT\_REQUIRED

Element from the next step was not found

**When occurs?**:

* Scroll until next step visible but next step has wrong selector
* Next step element doesn't exist
* Selector empty/invalid
* Next step deleted

**What to do?**:

* Related step is set to "Scroll until element from next step is visible" so the next step needs to have a correct selector
* Verify next step selector correct
* Ensure next step element exists
* Fix/add selector to next step

#### NEXT\_ACTIVE\_STEP\_WITH\_ELEMENT\_REQUIRED

Related step is set to "Scroll until element from next step is visible" so the next step needs to have a related element

**When occurs?**:

* Scroll until next step visible but next step is Execute JavaScript (no element)
* Next step is Wait/Set variable
* Next step disabled
* Next step is Goto

**What to do?**:

* Check what is the type of the next step
* Make sure that it is set to a type that has an element
* Change next step to one with element (Click, Change, etc.)
* Remove scroll until next step condition
* Add intermediate step with element

#### ASSERT\_FAILED

Assertion condition not met

**When occurs?**:

* Text equals "Success" but shows "Error"
* Element visible but hidden
* URL contains "/dashboard" but is "/login"
* Variable value mismatch

**What to do?**:

* Verify expected value correct
* Check page state
* Add wait before assertion
* Review test flow
* Update assertion to match behavior

#### SCROLL\_FAILED

Scroll operation failed

**When occurs?**:

* Scroll position doesn't match expected
* Page prevents scrolling with overflow:hidden
* JavaScript interferes
* Scroll target beyond boundaries

**What to do?**:

* Check page allows scrolling
* Verify scroll target reachable
* Check for JavaScript interference
* Adjust scroll coordinates

### Timeout & Performance Errors

#### TIMEOUT

Step couldn't complete within time limit.

**When occurs?**:

* Slow API response
* Page loads too long
* Complex JavaScript exceeds timeout

**What to do?**:

* Increase step timeout in settings
* Optimize page performance
* Add explicit wait steps
* Break into multiple steps
* Check network/server performance

#### SINGLE\_TEST\_TIME\_EXCEEDED

Test exceeded maximum test duration for current plan.

**When occurs?**:

* 65 minutes with 60 minute limit
* Free plan 10 min limit exceeded
* Waits/delays accumulate

**What to do?**:

* Optimize test to run faster
* Upgrade plan for higher limits
* Split into multiple shorter tests
* Reduce/remove explicit waits

### Browser & Extension Errors

#### UNSUPPORTED\_BROWSER

You are using an outdated and unsupported browser

**When occurs?**:

* Chrome 80 when minimum is 90
* Old version missing APIs
* Beta/canary with incompatible changes
* Chromium missing features

**What to do?**:

* We suggest updating it to the most recent version
* Update browser to latest stable version
* Use supported version (check docs)
* Switch to Chrome if using alternative

#### DEBUGGER\_DETACHED

Chrome debugger detached

**When occurs?**:

* User clicks "Cancel" on debugging notification
* Manually detaching from DevTools
* Debugger lost due to crash

**What to do?**:

* Don't click "Cancel" in the Chrome toolbar saying "BugBug is debugging your browser"
* Don't manually detach debugger
* Try to run the test again
* Restart browser if crashed

#### BLOCKED\_BY\_BROWSER\_POLICY

BugBug could not run on this page due to extension settings policy

**When occurs?**:

* Chrome Enterprise blocks extensions on domains
* Sandboxed iframe (reCAPTCHA) blocks execution
* Opera without "Allow access to search page results"
* Corporate IT policy restricts permissions
* Site access settings block domain

**What to do?**:

* If using Opera browser, turn on "Allow access to search page results" option in BugBug extension settings
* Verify if your app is using any sandboxed iframe which blocks BugBug from running (e.reCAPTCHA)
* If your organization is using Chrome Enterprise, contact your IT administrator
* Check extension site access settings

### Configuration & Settings Errors

#### INVALID\_CUSTOM\_HEADERS

Custom headers provided in project's browser settings are invalid

**When occurs?**:

* Header with spaces "invalid header:value"
* Missing colon "Authorization Bearer token"
* Invalid characters "X-Custom-Header!: value"
* Malformed list

**What to do?**:

* Verify they follow the correct format (e.g., key:value, x-second-key:value)
* Ensure colon separator between key and value
* Ensure headers' names do not contain any spaces or other forbidden characters
* Check line breaks in header list

#### INVALID\_DATA\_FORMAT

Provided data has not valid format

**When occurs?**:

* Invalid date "2024-13-45"
* Malformed JSON
* Invalid email format
* Wrong data type (string instead of number)

**What to do?**:

* You need to update a value in the field or re-record this step
* Fix date format
* Validate JSON syntax
* Correct email format
* Use correct data type

### System Errors

#### RUNTIME\_ERROR

Unexpected runtime error

**When occurs?**:

* "Failed to resume runner"
* Tab context not found
* Unexpected extension state
* Memory/resource exhaustion

**What to do?**:

* Rerun test
* Reload extension
* Restart browser
* Contact support with error details

#### INTERNAL\_ERROR

Critical internal error

**When occurs?**:

* Severe internal failures
* Unhandled exception in core logic
* Data corruption
* Critical bug

**What to do?**:

* Rerun test
* Reload extension
* Clear browser cache and extension data
* Contact support with detailed information

#### INITIALIZATION\_ERROR

Error during test run initialization

**When occurs?**:

* Failed browser session setup
* Can't connect debugger
* Error opening window
* Failed script injection

**What to do?**:

* Rerun test
* Restart browser
* Check browser permissions
* Ensure no other debugging tools attached
* Contact support

#### STEP\_RUN\_INITIALIZATION\_ERROR

Error during step run initialization

**When occurs?**:

* Failed step environment preparation
* Can't access step data
* Error setting up resources
* Previous state not cleaned

**What to do?**:

* Rerun test
* Check step configuration
* Verify test data valid
* Contact support

#### UNRECOGNIZED\_STEP\_TYPE

Step type not supported

**When occurs?**:

* Corrupted step data
* Test from newer version
* Database corruption
* Custom step type not recognized

**What to do?**:

* Update extension to latest version
* Re-create step with correct type
* Check for data corruption
* Contact support

#### FRAME\_IS\_NOT\_INITIALIZED

Frame exists but not initialized

**When occurs?**:

* Scripts not injected
* Iframe loads too quickly
* Security policy prevents injection

**What to do?**:

* Add wait step
* Increase timeout
* Check console for security errors
* Contact support

#### INVALID\_MOUSE\_INPUT\_PARAMS

Mouse parameters invalid

**When occurs?**:

* Invalid button type
* Negative coordinates
* Invalid modifier keys
* Corrupted event data

**What to do?**:

* Re-record step
* Check configuration for invalid values
* Contact support

#### FILE\_DOES\_NOT\_EXIST

Upload file doesn't exist

**When occurs?**:

* Non-existent file path
* File deleted/moved
* Wrong path

#### FILE\_UPLOAD\_ERROR

Generic file upload error

**When occurs?**:

* Insufficient permissions
* File locked by another process
* File size exceeds limits
* File type not accepted

**What to do?**:

* Check file permissions
* Ensure file not open elsewhere
* Verify file size within limits
* Check file type accepted
* Try different file

#### VALUE\_COMPUTING\_ERROR

There was an error while parsing variables

**When occurs?**:

* Single braces {variable}
* Malformed {{variable}
* Invalid characters {{user-name}}
* Nested braces

**What to do?**:

* If you are going to use variables, make sure you use double braces like this: {{variable}}
* Ensure complete syntax
* Use alphanumeric and underscores only
* Check for typos

#### WEBSOCKET\_ERROR

WebSocket connection error

**When occurs?**:

* Connection fails during cloud run
* Firewall blocks WebSocket
* WebSocket server down/unreachable
* Connection drops during test

**What to do?**:

* Check network/firewall settings
* Verify WebSocket server availability
* Check for network stability
* Contact support for cloud runs

#### WEBSOCKET\_SETUP\_ERROR

Failed to set up WebSocket

**When occurs?**:

* Can't establish initial connection for cloud runs
* Invalid WebSocket URL/credentials
* Proxy/firewall blocks handshake
* SSL/TLS certificate issues

**What to do?**:

* Verify WebSocket URL and credentials
* Check proxy/firewall settings
* Verify SSL/TLS certificates
* Contact support

#### REQUEST\_ERROR

API request failed

**When occurs?**:

* BugBug API is noit responsive
* Network timeout during request

**What to do?**:

* Verify network connection
* Contact support

#### LOGS\_UPLOAD\_TIMEOUT

Log upload exceeded timeout

**When occurs?**:

* Network issues prevent upload
* Very large log file
* Connection interrupted

**What to do?**:

* Optimize test or app to reduce log size
* Switch logs settings from to "Console logs"
* Disable logs

#### EXTENSION\_DOES\_NOT\_RESPONSE

Extension doesn't respond within timeout

**When occurs?**:

* Extension unresponsive
* Heavy page load causes hang
* Browser throttles extension
* Communication timeout

**What to do?**:

* Increase step timeout
* Reload extension and retry
* Check browser performance and close tabs
* Update browser
* Contact support

#### EXTENSION\_DISCONNECTED

Your BugBug extension has been disconnected

**When occurs?**:

* Network issues interrupt communication
* Extension reloaded during test
* Browser update forces restart
* Extension crashes

**What to do?**:

* Check your internet connection
* Don't reload extension during test
* Avoid browser updates during test
* Try again

#### EXTENSION\_DISCONNECTED\_ERROR

Your BugBug extension has been disconnected

**When occurs?**:

* Extension crashes due to memory
* Extension disabled by user
* Browser kills extension for resource usage
* Extension update interrupts test

**What to do?**:

* Check your internet connection
* Check extension status
* Close unnecessary tabs to free resources

#### TAKING\_SCREENSHOT\_TIMEOUT

Screenshot capture exceeded timeout

**When occurs?**:

* Screenshot takes >10 seconds
* Page with very large images/canvas
* Browser under heavy load
* Graphics driver issues

**What to do?**:

* Optimize page images/canvas size
* Close unnecessary tabs to reduce load
* Update graphics drivers

#### MISSING\_STEP\_SCREENSHOT

Step screenshot missing

**When occurs?**:

* Screenshot capture failed
* Browser API returned null
* Insufficient memory
* Tab closed before screenshot

**What to do?**:

* Ensure sufficient memory available
* Don't close tabs during test
* Rerun test
* Contact suppoer if issue persists

#### MISSING\_ELEMENT\_SCREENSHOT

Element screenshot missing

**When occurs?**:

* Element screenshot failed
* Element moved/disappeared
* Element outside viewport
* Browser API error

**What to do?**:

* Scroll element into view
* Rerun test
* Contact suppoer if issue persists


# Naming your tests

Learn how you can structure your tests to make it clean and useful! Learn effective test organization techniques to streamline your testing process with BugBug's comprehensive guide.

Think of a smart convention for naming your tests so that you can handle hundreds of test cases in the future.

You can use special characters in the names of the tests so that you can quickly filter them using the search box, for example, use slashes, emojis, etc.&#x20;

The [searching](https://docs.bugbug.io/organizing-tests/searching-tests) is case insensitive - that means that it doesn't matter if you use capital or small letters in the names of your tests.

You can edit the test name in two ways

#### Renaming tests on the tests list

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fe0iZMgpytgxx3O1F44Q8%2FScreenshot%202022-04-11%20at%2012.19.26.png?alt=media\&token=79410e5e-d9b6-4ff2-962b-107345dab8bf)

#### Renaming when editing the test, by clicking its title

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F6qMcRxpR1OhFHEPXtD5R%2FScreenshot%202022-04-11%20at%2012.18.37.png?alt=media\&token=a3fddcdf-71f3-40c0-a9f3-17c413c89657)


# Searching tests

Learn how to efficiently search and organize your tests using BugBug's comprehensive documentation. Boost your testing productivity today!

### Use the search in table

The search box is located at the top of the table with your tests. Just type in the keyword and see the results. The search is case insensitive - that means that it doesn't matter if you use capital or small letters in the names of your tests.

Tip: if you have hundreds of test cases, think [how to name your tests.](https://docs.bugbug.io/organizing-tests/organising-your-tests)&#x20;

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F70E7QsZckKj5nhKYId7o%2FScreenshot%202022-04-11%20at%2012.27.34.png?alt=media\&token=6f220f46-a924-4290-a6ae-78c11f92b8bd)

### Sorting the tests list

If you want to see only failed tests, you can sort the table by status. Just click the table header once or twice to find the right sorting order.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHajiHkjI8t4mdDo26EJi%2FScreenshot%202022-04-11%20at%2012.25.18.png?alt=media\&token=a227a256-d5ce-4b38-9159-42df3b51873b)


# Suites

Explore BugBug's comprehensive guide on organizing test suites efficiently. Learn how to gorup test cases to run them in parallel. Start testing for free!

### Why use suites?

Suites are great for grouping test cases to run them in parallel. They are simply groups of multiple tests. Organise your tests into Suites to quickly **run several tests at once**.

By default BugBug has one suite called "All tests", where you will find all tests you created in a project. All newly created tests will be automatically added to this suite.&#x20;

Suites can be [scheduled](https://docs.bugbug.io/running-tests/schedules) to run in the cloud and are useful for [working with different environments](https://docs.bugbug.io/editing-tests/variables#work-with-different-development-environments).&#x20;

### What suites should I have?&#x20;

Here are some examples of suites that usually help with test automation workflow.

* you can have a suite that monitors only core features on your production, [scheduled](https://docs.bugbug.io/running-tests/schedules) every hour
* you can have a full regression suite that you run manually before the release
* you can have a "feature branch" suite that has work in progress tests that are not yet ready to be run on production, but after the release you will add them to the production suite&#x20;
* you can have suites that run the same tests with different [profiles](https://docs.bugbug.io/editing-tests/variables#profiles), for example checking your app on multiple languages

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fd6nPniE24PTM8GBvNPPy%2FScreenshot%202022-04-12%20at%2012.29.38.png?alt=media\&token=7beee9f3-a4da-4e69-98c3-8a01b0d5c748)

### Create new custom suite

You can create custom suites in the Suites tab:

1. Click `Create new suite` button
2. Add `Suite name`
3. Choose tests that you want to include in a suite
4. Choose options for a suite
5. Save

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fk0ci2wakHK2pWEe13XgZ%2FScreenshot%202022-04-12%20at%2012.29.40.png?alt=media\&token=e302a55f-6234-4b20-87d7-8d0970f3afed)

### Auto-retry failed cloud tests to prevent flaky tests notifications

If your suite sometimes randomly fails, but there is no certain reason for that, you may be annoyed by the "failed" false positive [notifications](https://docs.bugbug.io/collaboration/alerts). The industry term for tests that fail randomly for no reason is *flaky tests*.&#x20;

*Flakiness* can be caused by many different factors:&#x20;

* a slowdown in the internet connection
* busy server side
* temporary machine CPU overload

You probably don't want to get notifications for such randomly failed tests - your app works as it should, it was just a temporary problem that doesn't require attention. BugBug allows you to prevent such unnecessary alerts.   &#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F1g8dkJ5itLxoFBgDf38q%2FScreenshot_2024-06-11_08-51-38.png?alt=media&#x26;token=969c03d2-78c6-4c82-b806-f07c5eeda594" alt=""><figcaption></figcaption></figure>

**When auto-retry is enabled:**

* If one of the tests in a suite fails, it will be automatically run again
* if another attempt passes, we will mark the suite as "passed", but you can still see the failed test attempt in the [test runs history](https://docs.bugbug.io/debugging-tests/runs-history), marked as "auto-retried"
* If the test  fails for the second time, it will be again restarted
* If the test fails the specified number of times, we will mark the suite as "failed"

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhDSQKzxBZtqP2IZACeRZ%2FScreen%20Shot%202022-09-21%20at%2019.18.20.png?alt=media&#x26;token=56aa9cc6-16cc-44be-9e76-ea5eea776023" alt=""><figcaption><p>Example suite run history with auto-retry enabled. There were 3 attempts to run the same test.</p></figcaption></figure>

**When auto-retry is disabled:**

* If any of the tests fail, the suite will continue running and after all the tests are finished it will be marked as "failed"

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQ84ZhLkhKwfrBDiJ3AKO%2FScreen%20Shot%202022-09-21%20at%2019.20.02.png?alt=media&#x26;token=c0b19765-beb5-49b5-9dbf-02d58ce96c26" alt=""><figcaption><p>Example suite run history with auto-retry disabled. There was just one attempt to run the test.</p></figcaption></figure>

{% hint style="info" %}
**Important!** Auto-retry only works in suites run in the BugBug cloud. [Pro subscription](https://bugbug.io/pricing) is required.&#x20;
{% endhint %}


# Projects

Discover BugBug's guide on organizing tests within projects. Learn effective strategies for seamless test automation management and maximize your testing efficiency. Start now!

## What is a project?

Projects are a higher level "folder" for your tests, suites and schedules. Learn about it in [your first project section](https://docs.bugbug.io/quick-start/your-first-test) of our quick start guide.

## Switching projects

To change the project you are currently working on, click the BugBug logo in the top left. This will navigate to the list of projects.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FZ7OlWTN9U6KMP4esRbcv%2Fimage.png?alt=media\&token=1067c523-475a-4c12-bf78-91775271bf70)

## Duplicating a project

If you want to make a copy of a project, click the "three dots" icon and select "Duplicate project".&#x20;

{% hint style="info" %}
**Important!** Project duplication can take several minutes. You will get an email notification when it's done.
{% endhint %}

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FookJCkTTUIxR1lTpKyrN%2Fimage.png?alt=media\&token=87d8d8f7-7ebc-4669-8fae-9caa1009366e)

## Transfer a project to a different organization

You can move projects to another organization. This is helpful when you need to transfer tests to a different account managed by your client or a different department.&#x20;

Just ask our [support](https://bugbug.io/contact) and we will do it for you. Send us a link to the project you want to transfer and the link to the target organization. Please note that our support would need to authorize you before the transfer by sending an email with a confirmation request.&#x20;


# Reporting


# Standard reports

BugBug provides standard reports for both **test runs** and **suite runs**. You can access all reports in the [Runs History](https://docs.bugbug.io/running-tests/test-in-your-browser) module.

{% hint style="success" %}
Standard reports are available only in [paid plans](https://bugbug.io/pricing/).
{% endhint %}

### Available report types

* **PDF summary** - visual summary of test results. Test run report includes general information and step statuses. Suite run report provides general information and test run statuses.&#x20;

> You can view an example [here](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FaSpE2N3Rn1rJNpcqJp9A%2FStaging_-_E2E_Regression_tests_2025-10-31_90490.pdf?alt=media\&token=1d8c9f31-a37d-427c-bfaa-0c5c313dec93).

* **JUnit XML** – A structured summary of test results in the output format used by software testing frameworks.

> You can view an example [here](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNYRS6j4VtZq8FbRM2cV4%2FStaging_-_E2E_Regression_tests_2025-10-31_90490.xml?alt=media\&token=ffd6e1dc-fb2f-4451-b8a6-1d8a8b7b6f16).

{% hint style="info" %}
If you need more detailed reports — including screenshots for each step or raw data in CSV or JSON format — see the [Advanced Reports](https://docs.bugbug.io/organizing-tests/reporting/advanced-reports) section.
{% endhint %}

### How to download a standard report

1. Go to the desired **test run** or **suite run**.
2. Open the dropdown menu and click `Download report` .<br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fje3jTjyK85GxUdgNLNOG%2Fimage.png?alt=media&#x26;token=9de173c0-f802-4002-9bf6-f4084044d282" alt=""><figcaption></figcaption></figure>

3. Select the report type that you need and click `Continue`.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F3TbHHYjeptC4dEhCYYQD%2Fimage.png?alt=media&#x26;token=73c14cfa-6d82-4f56-8a0c-a158298f94c9" alt=""><figcaption></figcaption></figure>

4. Add a custom note if you need to include some additional context in the report, and click `Download`.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FbUuJthHccpy8wZiPBDyT%2Fimage.png?alt=media&#x26;token=3487c706-6234-4de0-9266-48cafcf5c033" alt=""><figcaption></figcaption></figure>

### Examples of standard reports

Below, you can see examples of a PDF and a JUnit XML report for a single suite run containing multiple tests.

{% file src="<https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FaSpE2N3Rn1rJNpcqJp9A%2FStaging_-_E2E_Regression_tests_2025-10-31_90490.pdf?alt=media&token=1d8c9f31-a37d-427c-bfaa-0c5c313dec93>" %}

{% file src="<https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNYRS6j4VtZq8FbRM2cV4%2FStaging_-_E2E_Regression_tests_2025-10-31_90490.xml?alt=media&token=ffd6e1dc-fb2f-4451-b8a6-1d8a8b7b6f16>" %}


# Advanced reports

BugBug provides **compliance-ready test reports** that include detailed **PDFs with step-by-step screenshots**. You can easily export your test run and suite run data in multiple formats, including JSON, CSV, and more.

{% hint style="success" %}
Advance reports are available only in the [BUSINESS](https://bugbug.io/pricing/) plan.
{% endhint %}

### Available report types

* **Detailed PDF report with screenshots** - Comprehensive, compliance-friendly report including each step and screenshot. Perfect for audits and documentation.
* **CSV** - Spreadsheet format containing all tests, steps, and selectors. Ideal for data analysis or importing into BI tools.
* **JSON** - Structured data format designed for sending results to other apps or integrating with external systems.
* **ZIP with screenshots** - A packaged folder containing separate CSV and JSON files for each test, along with all related screenshots.

{% @arcade/embed flowId="L6kL6B3udaDyLJBCe1it" url="<https://app.arcade.software/share/L6kL6B3udaDyLJBCe1it>" %}

###

### How to download an Advanced report for a suite run

1. Go to the specific suite run in Runs history.
2. Click `Download report` in the top-right corner.<br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Ff6fEgsergwpcccsM1ZF0%2Fimage.png?alt=media&#x26;token=d3ecca04-83f1-4ef9-bf6d-dd41240ab081" alt=""><figcaption></figcaption></figure>

3. Select your preferred format and click `Continue`.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSIY6sWd3MlIXP3Hl6pUM%2Fimage.png?alt=media&#x26;token=b2d2d2fe-711e-4e6a-9a79-00482ce05d6f" alt=""><figcaption></figcaption></figure>

5. If you want to include additional context, you can add a custom note to the report before downloading. Once ready, click  `Download` to start the report generation process.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FxfS5TmPXDGiFwelJhAGf%2Fimage.png?alt=media&#x26;token=ffdfd268-87e3-4686-9bce-6f5b6e4cbf42" alt=""><figcaption></figcaption></figure>

6. Report generation will begin, and you’ll receive a download link via email once it’s ready.\
   The process runs asynchronously, as generating detailed reports with screenshots may take a few minutes.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fu7eOaiIqyJ18cJSFmVRi%2Fimage.png?alt=media&#x26;token=27c9ec1b-c232-49af-9939-57daf8aa305c" alt=""><figcaption></figcaption></figure>

7. Click the `Download PDF report`  button in your email. You’ll be redirected to the BugBug app, where the report download will start automatically.

{% hint style="warning" %}
All advanced reports are available for **24 hours** after generation.\
After that, the download links will expire, and you’ll need to generate a new report if needed.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FMqom4oNN6AY5OPp08hcI%2Fimage.png?alt=media&#x26;token=f82c3f5e-6d62-4f01-8695-ba56f0ed89aa" alt=""><figcaption></figcaption></figure>

> Advanced reports that include screenshots — such as **detailed PDF** or **ZIP with screenshots** — can be quite large, sometimes exceeding **hundreds of megabytes**, since each test step includes its own screenshot. Keep this in mind when downloading or sharing reports.

###

### Examples of advanced reports

Below, you can find an example of how advanced reports look like for a single suite run with multiple tests inside.&#x20;

{% file src="<https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FoQwEGiHQ63JuKss9j96H%2FStaging_-_E2E_Regression_tests_2025-11-03_90490.pdf?alt=media&token=de5fb8cb-d7e9-40de-a53e-f6c25dceeba0>" %}

{% file src="<https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Ftt71oA9YGH3CmNIshHex%2FStaging_-_E2E_Regression_tests_2025-11-03_90490.csv?alt=media&token=ec8b4ffd-e63c-4ccc-9d32-ea94b0af21c3>" %}

{% file src="<https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQ0ELyHi9OY3J2BkmS9N3%2FStaging_-_E2E_Regression_tests_2025-11-03_90490.json?alt=media&token=48776641-b1a1-401b-9023-018f1f9f0246>" %}

{% file src="<https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fmg2UfLrMhTsww450Dbqd%2FStaging_-_E2E_Regression_tests_2025-11-03_90490.zip?alt=media&token=d7b3bc37-c425-4b6b-ae6b-7fb241b43fe4>" %}


# Edit & Rewind

BugBug supports unique functionality that allows you to easily record and execute steps in a very flexible way. Let's dive into the typical maintenance problem in end-to-end tests.

### A long test breaks down, and you have to fix it

This is a very common scenario when dealing with end-to-end testing.&#x20;

Imagine that you have a test that executes in 5 minutes. Of course, the recommendation for e2e tests is to have as short tests as possible, but the reality is very often different.<br>

This scenario is typically resolved as follows:

* Run a test and wait 5 minutes.
* The test fails.
* Fix broken steps or record new steps.
* Re-run the test from the beginning and wait another 5 minutes to reach the problematic part.
* If it passes, it's excellent. If not, you need to fix it again, run it, wait another 5 minutes, and loop it until it succeeds. This takes time - **a lot** of time.

Keeping this in mind, we've implemented a feature that allows you to run a test, pause it, record a new step, rewind the playback position, and continue test execution from the given position. You can run and record a test in any combination.

How to fix a test using BugBug’s Edit & Rewind freature:

* Run a test and wait until the end of execution.
* The test failed.
* Fix broken steps or record new steps.
* Rewind the playback position. **You don't have to start execution from the beggining!**
* Continue test execution from the given position.
* If it passes, excellent. If not, you have to fix it again and rewind the playback position bypassing the need to wait for earlier steps to complete. Simply verify only fixed steps.
* Profit.

#### **What does that mean for you?**

With Edit & Rewind, you can <mark style="background-color:green;">tremendously reduce the time spent on the maintenance</mark> of the tests.

Sounds awesome? Let's see it in action!

{% embed url="<https://vimeo.com/1017561827>" %}
Edit & Rewind in action
{% endembed %}

#### When else will Edit & Rewind be helpful

There are many more scenarios in which you can use this functionality.

1. **If you want to record new steps in multiple places in the test**

Pause and enable the recording multiple times, changing the recording position in the web UI where needed.

2. **If you want to record new steps somewhere in a test but don't want to wait for the whole execution process to reach this position**

Run the test and pause it. Change the playback position. In the window with a test set the right app state and start recording.

3. **If you want to debug the test step-by-step**

Pause the test execution and use the `Run next step` button. You can rewind and replay as many times as you like.

Do you feel it? Life is better now. You can rest.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fqig01LcU1N7eqK9eWvkq%2Fimage.png?alt=media&#x26;token=d8759564-e7a9-4023-b12b-06eea513e487" alt=""><figcaption><p>You after using Edit &#x26; Rewind functionality. Source <a href="https://www.reddit.com/r/wholesomememes/comments/evgnfp/resting_is_important_to_your_wellbeing/">https://www.reddit.com/r/wholesomememes/comments/evgnfp/resting_is_important_to_your_wellbeing/</a></p></figcaption></figure>


# Changing the test screen size

Discover BugBug tips on changing the test screen size in your testing workflow. Optimize your automation testing process for better results. Read now!

### What is a Screen Size option?&#x20;

The Screen Size option is used to set the screen size for a browser running your tests. Different sizes can render your website differently and you may want to test this or test different views for mobile devices. Where can you set it?

### Creating a new test&#x20;

When you create a new test, we offer two different screen resolution options.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FLwCSbznwjBpZC01N772o%2FNew%20test.png?alt=media&#x26;token=a762bacf-e6bb-413a-9e25-f9cb7743b7dc" alt=""><figcaption><p>You can select screen size optiom from dropdown menu </p></figcaption></figure>

* **Desktop**&#x20;

  As the default window size for your primary web application testing
* **Mobile** \
  Optional for small screen testing

You can change the test screen size to mobile or desktop using test settings from the menu. &#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHm0tfu2847JtIZPd1tvS%2Ftest%20setting.png?alt=media&#x26;token=47a45c71-362f-48e8-ba92-efb80179c2e5" alt=""><figcaption><p>open meatball menu and choose Test settings</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FDTuGlBa0RC6MMBrVZo9Z%2Ftest%20setting2.png?alt=media&#x26;token=57305fdb-4a6a-4db5-a909-bd0b24824b53" alt=""><figcaption><p>choose an option from Screen size dropdown menu</p></figcaption></figure>

### Changing screen size for desktop and mobile

If you want to change the default screen size, you need to set it in the Project Settings. Each project has its own default screen size. If you want to test other sizes, simply duplicate the project and change the settings from the default.\
\
**Note: Due the Chrome limitations the minimal value for Screen size is 500**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhzqaMNmrwyXpiY7VaOlA%2Fproject%20setting.png?alt=media&#x26;token=da3540bd-4be2-4358-ae90-1c6d71569559" alt=""><figcaption><p>Go to the side menu and select Project Settings. Then select the Screen Sizes tab.</p></figcaption></figure>

Also, you can use a quick link from the project menu&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FeS8Tk69NLY44ykMbLtRB%2Fproject%20setting2.png?alt=media&#x26;token=6ae6c9f2-85d3-4e86-9c50-2628d601b5b0" alt=""><figcaption><p>Open meatball menu, choose test setting and use link from Sreen size dropdown menu</p></figcaption></figure>

### Easy way to check your screen size for tests

We have added a new column for easy identification of the screen size set for a test.

* In the list of tests, you will see an icon informing you that the test is set for desktop or mobile.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FA9AjsJsyq71k5xHBk0eB%2FTest%20list.png?alt=media&#x26;token=7ead6478-27e1-462c-b980-d2c5befdce80" alt=""><figcaption><p>Icon will only be added if you set two different screen sizes for each test.</p></figcaption></figure>

* On Runs history there is also info about the screen size

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNM8n9hBleO8L39Sp9u0P%2Frun%20history.png?alt=media&#x26;token=ba871b19-4e08-4082-ae37-e0b048f0b324" alt=""><figcaption></figcaption></figure>

###


# Integrating with build systems

Learn about integrating BugBug with your build systems for seamless test management. Integrate with your CI/CD pipelines, GitHub, GitLab, Bitbucket, Bamboo, Jenkis and many more.

BugBug can be easily integrated into your continuous integration, CI/CD pipelines, Github actions, Gitlab, Bitbucket pipelines, Bamboo, Jenkins, etc.

You can do this with our simple yet powerful CLI - [BugBug command-line interface that you can install with NPM.](https://docs.bugbug.io/integrations/api)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fgo6WNrVFziMKr7olsJCJ%2FScreenshot%202022-04-12%20at%2011.21.52.png?alt=media\&token=76b566f9-273e-4136-a3cf-00fbec851e11)


# Mobile version testing

Enhance your mobile version testing workflow with BugBug's tips. Optimize your website's performance and user experience on mobile devices.

### What is a mobile version / RWD?

Your website may behave differently when opened on smaller screens, such as a smartphone or a tablet. This behavior is called Responsive Web Design (RWD) or simply a mobile version of your website - your website is designed in a way that adapts to different screen widths.

### When to test more than one screen width?

If your app is very similar on mobile and desktop, there's no need to create separate mobile tests - it will just double your work without much value added. We recommend that you focus on one screen resolution - the one that has the most users. You can still create 5 - 10 additional tests for different resolutions, but focus on the major differences between the mobile and desktop versions - just check if these specific core differences work correctly. &#x20;

If your app has many differences between mobile and desktop, for example very different navigation and user journeys, it makes sense to develop tests for mobile and desktop in parallel, as completely independent projects.

### How to create tests for different screen resolutions?

The easiest way to test the mobile version (responsive web design / RWD) is to have 2 different projects: one for desktop tests and one for mobile tests. Set a different window width per project in its [project settings](https://docs.bugbug.io/preventing-failed-tests/project-settings).&#x20;

We recommend doing this in the following way:

1. Create all the important desktop tests
2. Duplicate the project
3. Rename the new project and add `- Mobile` suffix to the project name
4. Change the screen size to "Mobile" in the project settings
5. Adapt the tests to the mobile version via [re-recording test steps](https://docs.bugbug.io/recording-tests-steps/re-recording-steps).

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FlGZC12L6SOkYpDQF4M8O%2Fimage.png?alt=media&#x26;token=534e92c9-dcdf-410b-8da9-f0a99c98956f" alt=""><figcaption><p>Duplicate the project and change its name</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F9jW3KMcPZnvqm6MOQ1VC%2FZrzut%20ekranu%202023-03-15%20111526.png?alt=media&#x26;token=7337642c-d861-4094-89ed-767d13ead9f1" alt=""><figcaption><p>You can choose a mobile option when creating a new test </p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F4CiUJoL12Py0VzPa5fMN%2FZrzut%20ekranu%202023-03-15%20114211.png?alt=media&#x26;token=86f76954-3bf4-47b0-86bc-8ed87ca64b4d" alt=""><figcaption><p>or change to mobile screen size in test settings. </p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHmJppQqEBjlfvNAqTqVU%2FZrzut%20ekranu%202023-03-15%20114222.png?alt=media&#x26;token=016fa209-fa63-4bfe-9478-7b1571a975aa" alt=""><figcaption><p>When You copy an existing test </p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FzwWT4J0dfBHPogKfNSd7%2Fimage.png?alt=media&#x26;token=c2358d47-fe19-4b0a-b4a1-69b14dcccc43" alt=""><figcaption><p>Run tests with smaller mobilewindow width</p></figcaption></figure>

{% hint style="info" %}
**Tip!** You can [ask support to move the tests between projects or accounts](https://docs.bugbug.io/organizing-tests/projects#transfer-a-project-to-a-different-organization).&#x20;
{% endhint %}


# Organizations

Discover BugBug's collaboration and organization settings. You can modify, add or delete information regarding your organization. Optimize teamwork and enhance your productivity.

## What are organizations?

Invite people to your organization to collaborate on the tests.&#x20;

"Organization" is your team's workspace, that shares the following:

* projects
* subscription
* organization settings
* [scheduled tests](https://docs.bugbug.io/running-tests/schedules) notifications

You can have unlimited projects in one organization. Everyone in the organization can access all the projects.

{% hint style="info" %}
**Important!** Only the organization admin can edit credit card information.
{% endhint %}

## Organization settings

To access Organization settings click the top-right user icon and select "Organization settings"

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FEGrnL9F9zDMHHEAISXEQ%2FScreenshot%202022-04-11%20at%2011.45.30.png?alt=media\&token=c7f73d43-77ad-4cb5-afce-522059a2870a)

In the organization settings you are able to:

* change your organization's name (rename an organization)
* invite other people to your organization and give them different roles like `admin` or `editor`
* enter your billing data
* choose or change the subscription plan
* modify your credit card details (only organization Admin can do this)
* check your invoices

## Creating a new organization

You can create a new organization any time using the top dropdown. Here you can also switch between organizations if you have more than one.&#x20;

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F75crfZnKRhUx66HOaLeA%2Fimage.png?alt=media\&token=641ef826-2db5-4ada-b9f5-84c21d6b3e5c)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FOu5RjPlXFTQ4oO9FaGMn%2FScreenshot%202022-04-11%20at%2012.38.40.png?alt=media\&token=ad4b9ec6-327c-4f99-a9b5-25ca824c3ddb)

## Related

[Parallel runs within your organization](https://docs.bugbug.io/running-tests/parallel-mode#parallel-runs-within-your-organization)


# Inviting team members

Learn how to invite team members and enhance your team collaboration with BugBug. You can work together on test cases, share links to test results, empower developers and many more.

## Why invite collaborators?

Working in a team on test automation is easier if all of your team members have access to BugBug.

* Work together on test cases
* Share direct links to test results
* Empower developers to [run tests locally ](https://docs.bugbug.io/running-tests/test-in-your-browser)
* Let developers see test results by clicking a link in[ build pipelines](https://docs.bugbug.io/integrations/api)
* Get all-team [notifications](https://docs.bugbug.io/collaboration/alerts) for scheduled cloud runs

{% hint style="info" %}
**Hint!** If you're a software agency, you don't need to invite your clients to send them email notifications. You can add them as "additional email addresses" in [project notification settings](https://docs.bugbug.io/collaboration/alerts).
{% endhint %}

## How many users can I invite?

You can invite an unlimited number of users, <mark style="color:green;">**free of charge**</mark>. No paid subscription is required.

## How to invite collaborators?

Go to "Organization settings" and switch to the "User" tab. Here you can see who has access and their role.&#x20;

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FMda2chT6UDJoss7OcoRM%2FScreenshot%202022-04-11%20at%2012.39.37.png?alt=media\&token=d0e9c5ca-2e61-4c0a-81d6-9aa257385ab9)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FOgkUiFzHswCLzza2jw4o%2FScreenshot%202022-04-11%20at%2012.40.07.png?alt=media\&token=ff5f5ff2-306b-4457-9e5c-7b67eb5df861)

## User roles

| Role   | Can                                                                                                           |
| ------ | ------------------------------------------------------------------------------------------------------------- |
| Editor | Access & Edit assigned projects                                                                               |
| Admin  | <p>Access & Edit all projects<br>Manage Billing<br>Update credit card information<br>Change subscriptions</p> |


# Project access management

The BugBug [BUSINESS](https://bugbug.io/pricing/) plan allows you to assign users to specific projects. By default, every user is assigned to every project. To modify this, navigate to ***Organization settings > Users*** and make the necessary changes.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FWon6iO7sY1twLrpVbmL2%2Fimage.png?alt=media&#x26;token=aae16e94-1c2e-4b14-824e-2f755b03ad46" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FL2h2079LfRfi5OWsZxnZ%2Fimage.png?alt=media&#x26;token=da0056ac-643a-40c9-8a80-a2d299c79dc6" alt=""><figcaption></figcaption></figure>

Please note that the ***Admin*** role has access to all projects, which cannot be modified. To assign a specific user to a project, you must first change their role to ***Editor.***

{% hint style="info" %}
You can read more about the differences between **Admin** and **Editor** roles [here](https://docs.bugbug.io/inviting-team-members#user-roles).
{% endhint %}


# Alerts

Stay connected and informed with BugBug's collaboration notifications feature. Streamline teamwork and never miss your test results. Try it now for free!

By default, BugBug is sending email notifications about [scheduled runs](https://docs.bugbug.io/running-tests/schedules) to all members of your [organization](https://docs.bugbug.io/collaboration/organization-settings). This makes sure that as soon as your app is not working as it should you will get an email alert.

You can change this rule on the Alerts page:

* when people get notifications
* who will receive them

You can also send additional notifications to email addresses who are not members of your organization, for example, clients or colleagues.&#x20;

{% hint style="info" %}
Alerts are configured **per project**, each project has independent settings.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCnjTrZaAAAWBqgB6qs8h%2F1emptyScreen.png?alt=media&#x26;token=b7a7f8d7-dc6b-4e61-a32a-fc12c750be0c" alt=""><figcaption><p>Blank screen without alerts</p></figcaption></figure>

## Adding a new alert to your project&#x20;

By clicking on the "**New alert**" button you can set up alerts related to a specific project.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXQHOlnygRe59osvk6d3A%2F1newAlertbtn.png?alt=media&#x26;token=0f0b190f-4256-4fc6-9c1a-3180adf70842" alt=""><figcaption><p>Blank screen without alerts</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhoUAb20wDeONyXYFslMo%2F1setupAnAlertscrn.png?alt=media&#x26;token=e41ef818-ce6a-4d7e-9896-a0a9a32ea09c" alt=""><figcaption><p>Alerts setup modal</p></figcaption></figure>

### Choose when the alerts should be sent

You can easily select when the alerts should be triggered by clicking and expanding the drop-down list in the "*When*" section.&#x20;

Available options:

* Test started
* Test finished
* Suite started
* Suite finished
* Schedule started
* Schedule finished

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FI2zPNGyHQ1Odw38ePuAP%2F1whenAlert.png?alt=media&#x26;token=d62493bf-fadf-473a-b72a-fa198a1a7905" alt=""><figcaption><p>List of available conditions</p></figcaption></figure>

#### Along with other conditions, such as:

* **Which suites/tests/schedules** - allows you to select various suites, tests, or schedules.
* **Results -** "*Passed*" and "*Failed*" are selected by default, but you can also choose a third option - "*BugBug internal erro*r" that will send an alert when, for example, some technical issues occur on BugBug's side that could impact the test run results.&#x20;
* **Methods&#x20;*****-*** contains "*Local browser*" and "*Cloud*" options to be selected, but this is dependent on your subscription plan settings.
* **Profile** *- a* profile that was used in selected runs.
* **Run by** *-* define what causes the run. Select between: "*Manually by a use*r", "*API*", or "*Automatically by scheduler*".
* **Frequency** *-* define when you want to get an alert. Select between:
  * "*Every time*" - get an alert always when the trigger with the given parameters occurs.
  * "*Only once when the result changes*" - reduce the noise. Don't get alerts if the result is the same as the previous one. For example, if the result is failed 5 times in a row, you will only get an alert the first time.

{% hint style="info" %}
Remember that these fields will change based on what type of event you will select in the "When" section from the listed options.
{% endhint %}

### Set what type of action should be executed\*

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSCKyzJ58BjMYlxoA32Rg%2FZrzut%20ekranu%202024-03-20%20o%2014.10.48.png?alt=media&#x26;token=57e0ff0b-d223-4fe1-a1d7-c2079ba9a246" alt=""><figcaption></figcaption></figure>

Currently you can choose one of those options:

* [Send email notification](https://docs.bugbug.io/collaboration/alerts/sending-email-notification)
* [Send webhook](https://docs.bugbug.io/collaboration/alerts/sending-webhook)
* [Send Slack message](https://docs.bugbug.io/collaboration/alerts/sending-slack-message)
* [Send Teams message](https://docs.bugbug.io/collaboration/alerts/sending-teams-message)

{% hint style="info" %}
**\*Note:** More will come soon, such as: creating a Jira ticket and sending a notification to other team communicators like Discord, etc.
{% endhint %}

***

## Alerts list and management

Having all the data filled you can add your alert by clicking on the "**Create alert**" button to see it on the list.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FYqX2RI8EFfJ1HYdCrppJ%2F1newAlertAdded.png?alt=media&#x26;token=031c36df-847a-4a2a-baea-729193f20c66" alt=""><figcaption></figcaption></figure>

### Manage your existing alerts

From this level, you can easily manage your listed alerts. From enabling or disabling to duplication them with a few clicks. Editing is also possible - just simply click on a listed alert's box.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FKtVAvwDRsl66HvJkVwgm%2F1multiAlerts.png?alt=media&#x26;token=d2fe503c-cf37-498f-a189-d04bf6556393" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Click on the toggle button to enable/disable each alert.
{% endhint %}

Click on the "**...**" to display the drop-down menu and select between available options:

* Edit
* Duplicate
* Delete

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FONemII4QgmeFWuFZHr2T%2F1moreOptions.png?alt=media&#x26;token=c42e8d02-627a-4c9d-a29f-0c6a28a403c9" alt=""><figcaption></figcaption></figure>

If some alerts aren't needed anymore and you want to tidy your list, just simply delete the selected item.


# Sending email notification

### Select who should be notified

In the "Send to" drop-down section you can select who should be notified when alerts are triggered. You can select between:

* All people (in the selected project)
* Selected user(s)

### Additional email addresses for notifications

You can also send notifications to other people, who are not members of your organization. For example:

* notify your clients about their app status without granting them access to the whole project
* notify other teams who don't want to sign up for BugBug but still want to be notified when something is not working as it should

You can enter several additional email addresses, separated by a comma.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FqZR8katVU0ITOm9Qrg6c%2F2SendTo.png?alt=media&#x26;token=dda68bb6-8f3c-4fec-a409-3c89a2493bf0" alt=""><figcaption><p>Send to setup options for email notifications</p></figcaption></figure>


# Sending webhook

Outgoing webhooks are a powerful feature for advanced users that can be used to integrate BugBug into your current workflow, such as sending custom notifications to your team's communicator like Slack.

Before proceeding to the next step, remember to first set up a webhook in your external service. You will need the webhook configuration to populate the form fields.

{% hint style="info" %}
**Note**: You can use built-in variables in any field, e.g. **{{testRunId}}**.
{% endhint %}

### Set basic request data

In the first two fields, you need to define the request **method** and the **webhook URL**. Currently, we support the most popular webhook request methods like POST and GET.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F102guqauEIfxPSXUTz93%2FZrzut%20ekranu%202023-09-25%20o%2014.49.29.png?alt=media&#x26;token=969898a0-47f0-4b47-ad1f-83bc0178ff32" alt=""><figcaption><p>Method and Webohook URL fields on the setup screen</p></figcaption></figure>

### Define POST request body message

The **Body** is an optional field that consumes data in JSON format. Its value depends on your needs and the requirements of your external service provider.

If you need to send additional data through the webhook request, it's the best place to do so.

### Testing a webhook alert

Before creating a new webhook alert, it's possible to check how it works by clicking on the **"Trigger Alert"** button.

It's a good practice to do this. It allows you to avoid unexpected errors in the future, for example, invalid credentials or wrong body format.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F88vc4LzDb5ao8ouPU165%2FZrzut%20ekranu%202023-09-25%20o%2015.00.29.png?alt=media&#x26;token=c12b54f6-ab8a-4735-8950-1bd42dd8e47a" alt=""><figcaption><p>Verify alert configuration</p></figcaption></figure>

### Define the POST request body message by using a built-in variable

When it comes to setting up the **Body** of your webhook, you can easily use **only** the built-in variables within BugBug, so the overall configuration will be more intuitive. Knowing this, for instance, you can set an alert that will send the name of the test with the usage of the POST method that contains within its **Body** a variable that reflects the finished test's name, like here:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F5wlYUcFkpNQ0I2NpSx7M%2F2_requestBodyWithVariable.png?alt=media&#x26;token=13b1e733-0bff-4941-9dc6-19819820c456" alt=""><figcaption><p>Request body with a bult-in variable</p></figcaption></figure>

```javascript
{
  "test name of a finished test": "{{testName}}"
}
```

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fl2eLLPIIEVtKf3NCNUpD%2F5_testNameVar.png?alt=media&#x26;token=2705eca2-5402-4c71-a198-95b50f5a7ed3" alt=""><figcaption><p>List of built-in variables</p></figcaption></figure>

&#x20;&#x20;

The `{{testName}}` built-in variable was used here, which resulted in an output of a webhook alert (after the test finished) in the "Raw Content" section in the tested Webhook service:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FlzppEeVm5949Z963YGFn%2F3_requestResponse.png?alt=media&#x26;token=1c550c30-76e2-4b0b-9f91-17c917d835a3" alt=""><figcaption><p>Webook alert for the triggered action</p></figcaption></figure>

&#x20;This matches the test's name that exists and was executed:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FLk9nRAc62kCuAKC0G13g%2F4_testsList.png?alt=media&#x26;token=978b098e-1a0a-44e7-ab75-c85432ad9ab0" alt=""><figcaption><p>List of created tests</p></figcaption></figure>


# Sending Slack message

Sending Slack messages to your project channel or directly to people is the best way to keep your team updated on the status of test/suite/schedule runs.

{% hint style="warning" %}
Keep in mind that the "Alerts" feature is only available on paid plans.\
So any related features, such as Slack alerts, will not be available on the free plan.

More information about pricing can be found here: <https://bugbug.io/pricing/>
{% endhint %}

Before proceeding to the first step, remember to [integrate your Slack workspace with BugBug](https://docs.bugbug.io/integrations/slack#connect-your-slack-workspace-with-bugbug).\
If you haven't done so yet, don't worry - BugBug will prompt you for permissions when you start creating an alert.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUUB3iGJGE3hRxH44y4yk%2FScreenshot%20at%20Oct%2024%2015-21-10.png?alt=media&#x26;token=ea65ed99-17cc-4d43-9b81-bc416ea9bcf2" alt=""><figcaption></figcaption></figure>

Already connected? Great! Follow the steps below.

### Set Slack message type&#x20;

In the first field, you need to specify the messaging method. We currently support two different ways to send a Slack message:

* Channel message *(most common)*&#x20;
* Direct message

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQkrz4I82vV1n37meUuQ5%2FZrzut%20ekranu%202023-10-23%20o%2015.45.52.png?alt=media&#x26;token=00b64f6f-a950-4ae0-b88f-855d585d61fd" alt=""><figcaption></figcaption></figure>

### Choose a recipient/channel

In the next box, you need to select a channel or person to receive the messages.\
BugBug will provide you with a list of all available Slack members.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FZRvIaEUUPlEUZRNuT4dM%2FZrzut%20ekranu%202023-10-24%20o%2015.09.05.png?alt=media&#x26;token=1f2a666c-a216-411b-817e-d20077a0233f" alt=""><figcaption></figcaption></figure>

### Testing a Slack alert

Before creating a new Slack alert, it's possible to check how it works by clicking on the **"Trigger Alert"** button.

{% hint style="info" %}
The Slack message template is predefined for all users.\
If you need to customize the message, [create a webhook alert instead](https://docs.bugbug.io/collaboration/alerts/sending-webhook).
{% endhint %}


# Sending Teams message

Sending Teams messages to your project channel or directly to people is the best way to keep your team updated on the status of test/suite/schedule runs.

{% hint style="warning" %}
Keep in mind that the "Alerts" feature is only available on paid plans.\
So any related features, such as Teams alerts, will not be available on the free plan.

More information about pricing can be found here: <https://bugbug.io/pricing/>
{% endhint %}

Before proceeding to the first step, remember to [integrate your Teams channel with BugBug](https://docs.bugbug.io/collaboration/alerts/broken-reference).\
If you haven't done so yet, don't worry - BugBug will prompt you for permissions when you start creating an alert.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNdbKUsxEkEGwyIOZ2SzU%2FZrzut%20ekranu%202024-03-20%20o%2014.10.41.png?alt=media&#x26;token=3b457c71-c075-4449-988f-b65084840d8f" alt=""><figcaption></figcaption></figure>

Already connected? Great! Follow the steps below.

### Set a team&#x20;

In the first field, you need to specify the team, where you will found expected channel.\
BugBug will provide you  a list of all **connected** teams.

### Choose a channel

In the next box, you need to select a channel to receive the messages.\
BugBug will provide you a list of all **connected** Teams channels.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FG5BrZtCH2yb1w25XeykU%2FZrzut%20ekranu%202024-03-20%20o%2014.15.09.png?alt=media&#x26;token=9ab52c6e-dd2a-4d30-a1f2-d936a6d7afe2" alt=""><figcaption></figcaption></figure>

### Testing a Teams alert

Before creating a new Teams alert, it's possible to check how it works by clicking on the **"Trigger Alert"** button.

{% hint style="info" %}
The Teams message template is predefined for all users.\
If you need to customize the message, [create a webhook alert instead](https://docs.bugbug.io/collaboration/alerts/sending-webhook).
{% endhint %}


# CLI

Integrate BugBug with any continuous integration (CI) or continuous deployment (CD) pipelines or build system hooks.

## Integrate with CI/CD using BugBug Command Line Interface

You can operate BugBug via the Command Line Interface (CLI). This empowers you to integrate with any continuous integration (CI) or continuous deployment (CD) pipelines or build system hooks.

{% embed url="<https://www.npmjs.com/package/@testrevolution/bugbug-cli>" %}

## Install via NPM

Open your terminal. First of all, you need  [Node.js](https://nodejs.org/en/download/) installed on your machine and [npm](https://www.npmjs.com/get-npm) installed.&#x20;

{% hint style="info" %}
You need Node.js **version 20** **or newer**
{% endhint %}

After you have **NodeJS** and **npm** installed simply run:

```
npm install -g @testrevolution/bugbug-cli
```

Remember that you need to have admin user permissions on NodeJS execution.

## Get your API token

You need to take **the API token** of the project you want to run with CLI. You will find that in the BugBug web app in the Integrations tab from the side menu:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FTLFXZqhMmHCNmsoKoVyt%2FZrzut%20ekranu%202023-03-16%20105458.png?alt=media&#x26;token=3f55bec1-c35d-488d-8025-bc60533db619" alt=""><figcaption><p>The API token for the project</p></figcaption></figure>

Then configure CLI with the project's API token:

```
bugbug config set-token <api-token-from-project-settings>
```

## Run tests from terminal

On BugBug npm's page, you find the available commands. You can also just strike `bugbug help` to see what you can do and how.

Example: list suites within the connected project:

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MKixgeBPbLvnD0l1eiV%2F-MOTTs00Id1fYue98q_t%2F-MOTX5rk6pQWIegiDMU3%2FScreenshot%202020-12-14%20at%2000.55.58.png?alt=media\&token=f4e7b5e3-def1-4f36-b57f-85c6ba7e603a)

To run a particular test via CLI you need to find the ID of the test. It's easy, just go to your test, expand `3 dots`, and select `Run via CLI`. Just simply copy the command for running, open the terminal, and paste and run. The command looks as below:

```
bugbug remote run test <test-id>
```

## Find your suite ID

You can run the whole suite as well by going to `Suites` the tab, expanding the details, and selecting `Run via CLI`. The command is the same but SUITE\_ID is different. That's how we recognize you want to run the whole suite!

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FFzJQlRDUfr2yEyxINkra%2FCLI_1.png?alt=media&#x26;token=d75399bb-8d42-4661-9776-70b7989de2f4" alt=""><figcaption><p>Run in CLI option in the more drop-down menu</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FOIMY5rs0NvZWZdeLMc0H%2FCLI_2.png?alt=media&#x26;token=5e3dee99-10a6-4185-9c89-b3ee8a361c3e" alt=""><figcaption><p>Run this suite via CLI modal</p></figcaption></figure>

## Run tests from your build pipeline

Update your CI/CD build scripts to see test results directly in your build management tool *(for example in Bitbucket)*

Here's an example of what you can add to your build script:&#x20;

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FGztFcxAwzJBUTbYVthpv%2Fapi-example-script-safe.png?alt=media\&token=3d51c755-6f68-45d5-b0b3-0377ac78b409)

You can also override individual [variables](https://docs.bugbug.io/editing-tests/variables#intro-to-variables) from the command line with `--variable variableName="customVariableValue"`. This allows you to run different combinations of test data in different environments, for example, you can insert a different user password on prod and a different one on staging.&#x20;

{% hint style="info" %}
**If you're ambitious**&#x20;

Command line variables override allows you to test various combinations of test data. You could create a `for each` type of script and execute a suite with all the combinations.&#x20;
{% endhint %}

When you run your pipeline, BugBug tests would be triggered and your build will only be successful if all tests passed.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0Kxb7lJq47YCFbQKlBPv%2Fpipeline-example-safe.png?alt=media\&token=de42ab99-42b4-4052-8a7a-c3267bf9ea57)

Also read: [our advanced guide to automation testing for startups](https://bugbug.io/blog/software-testing/automation-testing-guide-for-startups-level-3/)

## Available commands list

Here is a list of the commands that may be in use with different options and/or flags:

### **`bugbug help <option>`**

| Options                                                                                        | Flags | Description                            |
| ---------------------------------------------------------------------------------------------- | ----- | -------------------------------------- |
| <ul><li><code>config</code></li><li><code>remote</code></li><li><code>version</code></li></ul> | N/A   | Show help menu for a specific command. |

### **`bugbug config <option>`**

| Options             | Flags | Description                                                                                                   |
| ------------------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| `set-token <token>` | N/A   | <p></p><p>You can use this option for the command to set a valid token from your web app project settings</p> |

### **`bugbug remote <option>`**

| Options                       | Flags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description                                       |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `list test`                   | <ul><li><code>--no-wait</code> <br><em>Exit immediately without waiting for the result</em></li><li><code>--no-progress</code><br><em>Don't show progress spinner</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Returns a list of all existing tests              |
| `list suite`                  | <ul><li><code>--no-wait</code> <br><em>Exit immediately without waiting for the result</em></li><li><code>--no-progress</code><br><em>Don't show progress spinner</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Returns a list of all existing test suites        |
| `list profile`                | <ul><li><code>--no-wait</code> <br><em>Exit immediately without waiting for the result</em></li><li><code>--no-progress</code><br><em>Don't show progress spinner</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Returns a list of all existing test profiles      |
| `run test <test-id>`          | <ul><li><code>--no-wait</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--with-details</code><br> <em>Show result with details</em></li><li><code>--profile</code> <br><code>"\<profile-name>"</code><br> <em>Run with a specific, existing profile</em><br></li><li><code>--variable</code> <br><code>"\<variable-name>"</code><br> <em>Override default variable during a single run</em><br></li><li><code>--reporter</code><br> <em>The name of the reporter to use (default: "inline"). Instead of "inline" you can also set "junit" for the report to be exported to an XML file</em><br></li><li><code>--output-path</code><br> <em>The path to save the test report. Relative to the current working directory</em></li></ul> | Runs a specific test based on its ID              |
| `stop test <test-run-id>`     | <ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code><br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--result-timeout \<int></code><br><em>Modify the default result waiting time (minutes, default: 60)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Stop the test run based on its ID                 |
| `run suite <suite-id>`        | <ul><li><code>--no-wait</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--with-details</code><br><em>Show result with details</em></li><li><code>--profile</code> <br><code>"\<profile-name>"</code><br><em>Run with a specific, existing profile</em></li><li><code>--variable</code> <br><code>"\<variable-name>"</code><br><em>Override default variable during a single run</em></li><li><code>--reporter</code><br><em>The name of the reporter to use (default: "inline"). Instead of "inline" you can also set "<strong>junit</strong>" for the report to be exported to an XML file</em></li><li><code>--output-path</code><br><em>The path to save the test report. Relative to the current working directory</em></li></ul> | Runs a specific test suite based on its ID        |
| `stop suite <suite-run-id>`   | <p></p><ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code><br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--result-timeout \<int></code><br><em>Modify the default result waiting time (minutes, default: 60)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Stop the test suite run based on its ID           |
| `status test <test-id>`       | <ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Display the test's status based on a run ID       |
| `status suite <suite-run-id>` | <ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Display the test suite's status based on a run ID |
| `result test <test-run-id>`   | <ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--with-details</code><br><em>Show results with details</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Display the test result based on a run ID         |
| `result suite <test-run-id>`  | <ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--with-details</code><br><em>Show results with details</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Display the test suite's result based on a run ID |

## Examples of usage

### Check the status of a test run by its ID:

```
bugbug remote status test <test-run-id>
```

**Output:**

```
ℹ Test name: [REG] Popup handling #2 (testRunId: 10a696b2-3ce6-4b45-8b9f-0a0a0abc00000)
✔ Status: passed
```

### Generate a report of a test run by its ID:

{% hint style="info" %}
By default "reporter" option is set to "inline".
{% endhint %}

```
bugbug remote status test <test-run-id> --reporter
```

**Output:**

```
ℹ Test name: Test number 71 (testRunId: ba5e19d8-609d-4529-95f6-0c6179e59614)
✔ Status: passed
```

### Generate a report of a test run by its ID that's exported to a junit format (XML file):

<pre><code><strong>bugbug remote status test &#x3C;test-run-id> --reporter junit
</strong></code></pre>

**Output:**

```
bugbug remote status test <test-run-id> --reporter junit
⠹ Waiting for result...
```

The XML file is automatically exported to your project's main directory:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FtSdkYPHlyvsjBAec1MTZ%2Fxml-report.png?alt=media&#x26;token=9e8915f3-bfb8-460c-87dd-c5db4951f52d" alt=""><figcaption><p>Preview of a test report exported to an XML file</p></figcaption></figure>

### Execute a test suite by its ID:

<pre><code><strong>bugbug remote run suite &#x3C;test-suite-id>
</strong></code></pre>

**Output:**

```
bugbug remote status suite bceb9701-23d3-4b67-bfb7-a000a000a00
✔ Status: passed
```

### Check test suite run's status:

<pre><code><strong>bugbug remote status suite &#x3C;suite-run-id>
</strong></code></pre>

**Output:**

```
bugbug remote status suite 8de73c22-c8a3-4141-c111-0a0a0a0a0a
✔ Status: passed
```


# Zapier

Discover seamless integration between BugBug and Zapier for efficient test automation. Streamline processes and boost QA productivity effortlessly.

## Connect BugBug to hundreds of other apps with Zapier

[Zapier](https://zapier.com/apps/BugBug/integrations) lets you connect BugBug to 2,000+ other web services. Automated connections called Zaps, set up in minutes with no coding, can automate your day-to-day tasks and build workflows between apps that otherwise wouldn't be possible.

Each Zap has one app as the **Trigger**, where your information comes from and which causes one or more **Actions** in other apps, where your data gets sent automatically.

### Flexible integrations

Explore multiple [**ways of integrating BugBug with other apps like Slack or Jira**](https://zapier.com/apps/bugbug/integrations)

![https://zapier.com/apps/bugbug/integrations](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSyffwC62NF5MXhLHeQRF%2FScreenshot%202022-04-12%20at%2011.11.30.png?alt=media\&token=e8a80a88-d873-4f20-98f2-13bd74c15d07)

![https://zapier.com/apps/bugbug/integrations](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F1SoV4FIJLnwRZ69oe8gf%2FScreenshot%202022-04-12%20at%2011.11.20.png?alt=media\&token=2236a953-f463-4a7b-9247-dfbc6e5b4ea0)

###

### Start with BugBug integrations for free

Zapier allows you to execute up to 100 automated tasks per month for free.

### How do I connect BugBug to Zapier?

Log in to your [Zapier account](https://zapier.com/app/login) or create a [new account](https://zapier.com/sign-up). Next, click on the "***Explore apps***" buton from the top menu bar or "***App Connections***" in the sidebar. Search for "BugBug" and add a new connection.&#x20;

Use your credentials (API Key) to connect your BugBug account to Zapier. Once that's done you can start creating an automation!&#x20;

Use a pre-made Zap or create your own with the Zap Editor. Creating a Zap requires no coding knowledge and you'll be walked step-by-step through the setup.&#x20;

Need inspiration? See everything that's possible with [BugBug and Zapier](https://zapier.com/apps/BugBug/integrations).

If you have any additional questions, you can reach out to <contact@zapier.com>.&#x20;


# Slack

Discover seamless integration between BugBug and Slack for efficient bug tracking and collaboration. Streamline your workflow with ease. Learn more!

<div align="center"><figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fp8XCK2J71Q8pj9vOq6Wa%2FSlack-logo-RGB.png?alt=media&#x26;token=61edb988-5fa7-476f-a1d7-a2a86c900eee" alt="Slack logo" width="300"><figcaption></figcaption></figure></div>

## How to integrate test automation with Slack?

BugBug’s integration for Slack is designed to elevate your testing and issue management to a whole new level.

Stay informed about:

* failed test runs
* schedule suites results
* unexpected errors
* ...and many more.

Currently, it is possible to do that in two ways:

1. [Creating a Slack message alert](#creating-a-slack-message-alert) *(recommended)*
2. [Using Zapier integration](#using-zapier-integration)

## Creating a Slack message alert

If you use Slack on a daily basis, need real-time updates, and want to set it up as seamlessly as possible, this is the easiest way to go.

{% hint style="warning" %}
Keep in mind that Slack integration is only available on paid plans. So any related features, such as Slack alerts, will not be available on the free plan.

More information about pricing can be found here: <https://bugbug.io/pricing/>
{% endhint %}

### Connect your Slack workspace with BugBug

Before you can create a new Slack Alert, you need to provide access to your Slack workspace.\
To do this:

1. Go to the "Integrations" page
2. Find Slack on the integrations list
3. Click on the "Manage" button
4. Continue by clicking on the "Connect" button
5. "Allow" BugBug to access your workspace data

{% hint style="info" %}
BugBug only needs information about available channels/users and permission to send messages to them.

More information about our privacy policy can be found here: <https://bugbug.io/privacy-policy/>
{% endhint %}

After the last step, you will be automatically redirected to the "Integration Details" page.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F55AV3vJ9dg5PAR62moje%2FZrzut%20ekranu%202023-10-23%20o%2016.15.28.png?alt=media&#x26;token=dec4a65b-c284-4825-a58c-76176eac1ded" alt=""><figcaption></figcaption></figure>

### Create a Slack message alert

On this page, you can click the "Send a Slack message alert" link. This takes you to the "New Alert" view, where you can configure your first Slack message alert, eg. the message type or recipient.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FtxP4FCzdVvltMtIauuo5%2FZrzut%20ekranu%202023-11-24%20o%2009.14.22.png?alt=media&#x26;token=c805ee21-1be9-4069-a985-585205616cec" alt=""><figcaption></figcaption></figure>

If you don't know how to set up [Alerts](https://docs.bugbug.io/collaboration/alerts), you can read more about how to do it [here](https://docs.bugbug.io/collaboration/alerts#adding-a-new-alert-to-your-project).

***

## Using Zapier integration

[Use Zapier for connecting BugBug to Slack to get notifications -->](https://docs.bugbug.io/integrations/zapier)

### Explore other ways of integrating BugBug with Slack

Check out other templates for [integrating BugBug with Slack](https://zapier.com/apps/bugbug/integrations)

![https://zapier.com/apps/bugbug/integrations](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FJsLZNScygAt3afP61qfx%2FScreenshot%202022-04-12%20at%2011.31.43.png?alt=media\&token=f836cf87-bb0f-4d94-ad64-0958af904ddb)


# GitHub

Streamline your GitHub workflow with BugBug's seamless integration. Collaborate efficiently and track issues effortlessly. Try it now for free!

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FGQ9yQqBrF806pbfVfHJF%2FScreenshot%202022-04-12%20at%2011.23.14.png?alt=media\&token=63b9e3ff-656a-419c-8b24-4bcf31e7ca14)

Integrate with GitHub to streamline testing into your CI/CD pipeline, providing real-time feedback within your repository. Run tests and suites on BugBug Cloud to ensure that only high-quality, thoroughly tested code is deployed to production environments, reducing the risk of introducing regressions or bugs.

Currently, it is possible to integrate in two ways:

1. Using [official GitHub Action](#official-github-action) **(recommended)**
2. Via [BugBug Command Line Interface (CLI)](https://docs.bugbug.io/integrations/api)

## Official GitHub Action

GitHub Actions allows developers to create automated workflows directly within their GitHub repositories. Integrating with [BugBug Cloud Runner](https://github.com/marketplace/actions/bugbug-cloud-runner) lets them seamlessly incorporate testing into your CI/CD pipeline to receive instant feedback on test results and quickly identify issues.

{% hint style="warning" %}
Keep in mind that BugBug Cloud Runner is only available on paid plans. \
More information about pricing can be found here: <https://bugbug.io/pricing/>
{% endhint %}

To add BugBug action to your workflow:

1. Go to the "Integrations" page
2. Find GitHub on the integrations list
3. Click on the "Manage" button
4. Continue by clicking on the "Open Github Action" button
5. Follow the instructions on [GitHub Marketplace](https://github.com/marketplace/actions/bugbug-cloud-runner) to add BugBug Cloud Runner to your .yml files

{% hint style="info" %}
Find your API token by following the instructions provided [here](https://docs.bugbug.io/api#get-your-api-token).

Discover where to find your suite ID by referring to the information available on this [page](https://docs.bugbug.io/api#find-your-suite-id).
{% endhint %}


# Bitbucket

Discover seamless integration between BugBug and Bitbucket for efficient bug tracking. Streamline your test automation process today!

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FEPmmD6nh55MA8k1hyySc%2FScreenshot%202022-04-12%20at%2011.26.11.png?alt=media\&token=105a9f95-f0ef-4c7a-9743-5e722d3aebb8)

[**Integrate testing automation with Bitbucket Pipelines using BugBug CLI -->** ](https://docs.bugbug.io/integrations/api)


# Gitlab

Discover seamless GitLab integration with BugBug. Run your test automation from GitLab CI/CD pipelines using our CLI.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FZyZ0pyos6zl8tHZjgXK9%2FScreenshot%202022-04-12%20at%2011.27.36.png?alt=media\&token=01ff5c3d-ccea-4c1c-834a-cad0f2b27a40)

[**Run your test automation from Gitlab CI/CD pipelines using BugBug CLI -->**](https://docs.bugbug.io/integrations/api)


# Trello

Seamlessly integrate Trello with BugBug to enhance collaboration and create Trello tasks when the scheduled tests failed. Explore our integration guide!

You can automatically create Trello tasks when the scheduled tests failed. Use [Zapier integration to connect BugBug to Trello](https://docs.bugbug.io/integrations/zapier).

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FOfN1UmCB3jiNeJgDzep7%2FScreenshot%202022-04-12%20at%2012.31.12.png?alt=media\&token=52a6245c-812a-449a-8afc-e88919180088)


# Jira

Discover seamless integration between BugBug and Jira for efficient bug tracking and project management. Jira integration allows you to integrate BugBug runs with your development process.

Jira integration allows you to integrate BugBug runs with your development process. You can automatically create Jira issues when the scheduled tests failed. Use [Zapier and get updates on your BugBug tests in Jira.](https://docs.bugbug.io/integrations/zapier)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F44BRib2EkV7vTRXuiWOS%2FScreenshot%202022-04-12%20at%2011.32.41.png?alt=media\&token=ea9ead8a-14ef-4b8c-911a-69f8105104d0)


# Account settings

Optimize your BugBug account settings for better performance and personalized experiences. Explore our comprehensive guide to fine-tune your preferences.

Here you can set your account formal conditions.

To access the account settings:

1.Click dropdown with "person icon" on the right:

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MKixgeBPbLvnD0l1eiV%2F-MO16Ez2brHPISot35Pz%2F-MO17R0O052ZwDabTJg5%2FScreenshot%202020-12-08%20at%2012.34.03.png?alt=media\&token=bb7030d0-3255-4328-9891-06ef067debf2)

2\. Choose Account settings.

The settings you can access to:

* first name and last name
* change password
* notifications

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MKixgeBPbLvnD0l1eiV%2F-MfEwfXN1pgzESbHJLVX%2F-MfEyIb5QOULDacf6gio%2Fimage.png?alt=media\&token=82ffaac3-e283-41b2-9b71-8d68a6a1eb5a)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MKixgeBPbLvnD0l1eiV%2F-MfEwfXN1pgzESbHJLVX%2F-MfEywRaPTOEWoQu5D6N%2Fimage.png?alt=media\&token=76df7abd-f518-444b-bcf0-8e883ee6ad7e)

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MKixgeBPbLvnD0l1eiV%2F-MfEwfXN1pgzESbHJLVX%2F-MfEz58XeWgv7XaC47xc%2Fimage.png?alt=media\&token=a0a9cf8c-6b91-4c5a-969e-1cd3960e3e8d)


# Edit your name and email

Effortlessly update your account details in BugBug app. Edit your name and email hassle-free to keep your profile information up to date.

If you collaborate with others, don't forget to fill out your profile first name and last name. You can do this by clicking the top-right user menu and going to "Account settings"

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fv4WrBs61pzOMl4ZNYy9Y%2FScreenshot%202022-04-07%20at%2014.45.53.png?alt=media\&token=1a453fa1-49a5-45bd-aff0-eb26d27ff579)


# Forgot password

Reset your BugBug account password hassle-free. Follow the simple steps provided in our guide.

1. Go to sign in page <https://app.bugbug.io/sign-in/>
2. Click `Forgot password?` link
3. Write email address you are registered with
4. Click `Reset password` button
5. Go to your email inbox - after a minute you should see reset link - click it and set new password
6. You should be able to sign in with new password


# Manage Subscriptions

Manage your BugBug subscriptions and stay up to date with the latest BugBug versions.

To upgrade or downgrade your plan, click the top-right user icon and go to **Organization Settings**, then to the **Subscriptions tab**.&#x20;

[Learn more about BugBug plans.](https://bugbug.io/pricing/)

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FcnbEFd55qN2pcIAXlEpm%2FScreenshot%202025-09-22%20at%2012.40.21.png?alt=media&#x26;token=f7ea82f9-a9a9-453d-9985-27870670ec53" alt="BugBug Pricing"><figcaption></figcaption></figure>

## Upgrading or downgrading your plan

When your test base grows, it can be useful to upgrade your BugBug plan. Here how to do that:

1. Go to [BugBug app home view](https://app.bugbug.io/), click your account dropdown on the right top corner and then choose `Organization settings`
2. Choose `Subscription` item
3. Select the plan you need
4. Fill the billing address form and payment details&#x20;
5. Finish payment process with Stripe vendor
6. See confirmation of your upgraded plan

## Closing your account or organization

If you wish to close and remove your account completely, please [contact BugBug support.](https://bugbug.io/contact/)


# Account FAQ

Discover answers to frequently asked questions about BugBug accounts. Learn how to manage your account settings and use BugBug for test automation.

<details>

<summary>How does a 14-day trial work?</summary>

You can fully explore BugBug’s capabilities for **free** with a 14-day trial. After the trial ends, your account stays open, but some features will be limited.

</details>

<details>

<summary>Is there a free version of BugBug available?</summary>

Yes! BugBug offers a free plan with **unlimited** local test runs and users. This plan is perfect for testing simple web apps directly in your browser.

Learn more about the [FREE plan here](https://bugbug.io/pricing/).

</details>

<details>

<summary>What payment methods do you support?</summary>

You can pay with a credit card. The secure payment is provided by the Stripe system.

</details>

<details>

<summary>Can I change my plan?</summary>

Yes, any time. When you buy a higher plan, it is activated instantly. If you downgrade, the change takes effect after your current billing period ends.

**Important!** You can change your plan anytime you want in your subscription settings.

</details>

<details>

<summary>Can I cancel my plan?</summary>

You can cancel your plan anytime (switch to the FREE Plan).

**Learn how to** [**manage your subscription here.**](https://docs.bugbug.io/your-account/subscriptions-bugbug-versions)&#x20;

</details>

<details>

<summary>Can many users collaborate at the same time? </summary>

Yes, you can invite new users within your [organization](https://docs.bugbug.io/collaboration/organization-settings) and collaborate on test automation together.

</details>

<details>

<summary>Which plan to choose?</summary>

When choosing the right BugBug plan, it's essential to assess your testing needs and team requirements.&#x20;

Here's a breakdown of each plan to help you decide:

**1. FREE Plan: For individuals who want to start testing simple web apps in their browser**

**Cost:** $0 per month

**Features:**

* Unlimited users
* Unlimited tests
* Unlimited local test runs
* Unlimited suites
* Components
* Edit & Rewind
* Smart waiting conditions
* Screenshots
* 7 days of test history

**Best suited for:**

* **Individual testers:** If you're working solo and need to perform basic testing tasks without incurring costs.
* **Small projects:** Suitable for projects that don't require advanced features or cloud-based test executions.

**Considerations:**

* No cloud test runs; tests are executed locally in your browser.
* Lacks advanced features like scheduling, notifications, and integrations.

**2. PRO Plan: For growing teams and start-ups looking to build a test automation process**

**Cost**: $219 per month (monthly billing) or $189 per month (annual billing - **$359 saved**)

**Features**:

* Includes all Free Plan features
* Unlimited cloud runs
* Scheduling
* Email notifications
* Slack notifications
* CI/CD integrations
* BugBug CLI
* Variables & Profiles
* Custom JavaScript steps
* Inbox for email testing
* Webhooks
* PDF reports for suite runs
* Console logs
* 1-month test history
* Optional parallel capabilities: up to 32x faster testing via parallel test execution in the cloud​

**Best suited for:**

* **Growing projects:** Teams looking for balance between cost and advanced features.
* **Startups & E-commerce Platforms:** Businesses needing regular monitoring and integration within their development pipelines.

**3. BUSINESS Plan: For scaling companies wanting to speed up their testing process**

**Cost:** $659 per month (monthly billing) or $559 per month (annual billing - **$300 saved**)

**Features:**

* Includes all PRO Plan features​
* REST API access
* Longer cloud run time
* Scheduled runs every minute
* 2 months of tests history
* Priority customer support​
* Optional parallel capabilities: up to 32x faster testing via parallel test execution in the cloud​

**Best suited for:**

* **Large QA Teams:** Organizations with extensive testing needs requiring rapid test executions.
* **Enterprises:** Companies that demand premium support and faster testing cycles.​

**Considerations:**

* Customizable to fit specific organizational requirements.​
* Ideal for teams needing simultaneous test executions to expedite release cycles.

**Additional considerations:**

* **Unlimited Users:** All plans support unlimited users, facilitating seamless collaboration across teams.
* **Free Trial:** BugBug offers a 14-day free trial of premium features, allowing you to explore the tool before committing.
* **No Credit Card Required:** Signing up for the free trial or the FREE Plan doesn't require credit card information.

**See more** [**detailed plan comparison here**](https://bugbug.io/pricing/)**.**

</details>

<details>

<summary>What billing type is best for me?</summary>

There are a few factors to consider when deciding if you want to pay monthly or pay for a full year upfront.

**Commitment vs Cost-effectiveness:**

* **Monthly Billing:** Monthly billing provides less commitment, allowing you to reassess your testing needs regularly. However, it comes with a higher cost on a month-to-month basis.
* **Annual Billing:** Choosing an annual plan involves a bigger commitment, but it comes with a cost-saving discount. This is beneficial if you're confident in your long-term usage and want to save money.

**Long-Term Planning:**

* **Monthly Billing:** Ideal for those who are uncertain about their long-term testing needs or want the freedom to switch services more frequently.
* **Annual Billing:** Suited for individuals or businesses with a clear, long-term testing strategy and who are looking to maximize cost efficiency.

</details>

<details>

<summary>How can I contact the Customer Service?</summary>

You can reach out to our support team through our [contact form](https://bugbug.io/contact/) or send us a direct message to info\[@]bugbug.io.

</details>


# Prohibited behaviors

Discover common prohibited behaviors and effective troubleshooting techniques of BugBug app. Get insights to overcome some certain limitations.

{% hint style="success" %}
[Read how to prepare your app for automated testing and avoid common pitfalls.](https://docs.bugbug.io/best-practices#how-to-prepare-your-app-for-testing)
{% endhint %}

## You cannot minimalize the test window&#x20;

If there is a test in progress, you cannot minimize the window that is running the local test. **Minimizing** the browser window has some limitations from the Chrome browser, which puts the minimized tab into standby mode. In this case, the JS code is not executed, so the **test stops** automatically.\
\
If you want to run tests without disrupting your work, you can run tests in the cloud.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fg6ozQFnZjNaceU72ujfi%2FProjekt%20bez%20tytu%C5%82u.png?alt=media&#x26;token=831ea469-6935-4a9e-9843-44efe24f54bc" alt=""><figcaption></figcaption></figure>

## BugBug doesn't support multiple windows

BugBug does not support multiple windows for recording and running tests. You are able to record tests with multiple tabs, but if your app use for example *window\.open()* or 3rd party popups BugBug will not handle them. We have that on our roadmap.&#x20;

## LastPass extension modifies DOM&#x20;

If you use the LastPass extension during recording, you may have some problems with element selectors. As we know, LastPass changes the DOM of your page, so also selectors can be different. This can cause a failed test if you run it in cloud mode or another person will perform a local test on a different browser. Please disable the LastPass extension for incognito mode before recording or editing a test.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FofOak3Rce90kDiahRVUZ%2FLastPassLogoShadow.png?alt=media&#x26;token=6c7a6695-528c-42cb-96f3-4a3ef7840b5a" alt=""><figcaption></figcaption></figure>


# Updating Chrome extension

Find solutions and troubleshooting tips for updating your BugBug Chrome extension. Get step-by-step guidance and fix compatibility issues.

If you encountered problems with the BugBug web application or tests recording, please follow the steps below to make sure you have the latest BugBug Chrome extension installed.

1. Go to Chrome extensions

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FstXJhQGtO7KWtFWL3iFQ%2Fimage.png?alt=media\&token=959dee81-9e8f-420a-bc75-bcd4eea06a14)

2\. Turn on "Developer mode"

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FsJQxSIrLFJeNxHLwoPEL%2Fimage.png?alt=media\&token=429389b2-bad1-4c96-9866-232cfc221e17)

3\. Click "Update"

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FH7k6VpxqxKuRBcMOHcoB%2Fimage.png?alt=media\&token=b17d4a5d-4530-41f1-855b-10ff708a5a13)

4\. After the update is finished, please refresh the BugBug web app page.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fat1YbWLiczJsbPy7eRbX%2Fimage.png?alt=media\&token=93b73d47-72b4-4f47-aea6-ab00909eeefe)


# Clear cookies and site data for BugBug

Learn how to troubleshoot and clear cookies and site data for BugBug. Watch our video now

If you encounter problems with BugBug application, please try to clear cookies and site data just for BugBug domains.&#x20;

Here's a video on how to do this.

{% embed url="<https://youtu.be/6jUJPCxjvF0>" %}


# Testing basic auth password protected websites

Learn how to troubleshoot and test basic auth password-protected websites with BugBug's comprehensive guide.

## Websites with basic authentication

BugBug allows you to test websites that require a *basic authentication* password.

Basic authentication or "basic auth" is a simple way to protect a website from being viewed before you publish it. Developers often use it to hide the testing environment from the external world. That means that when you enter an URL you need to provide a username and password.

{% hint style="info" %}
**Important!** BugBug will not automatically record this step. You need to manually add "basic auth" to the "Go to URL" step. See below.
{% endhint %}

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FM71m8oVozyT9IPWRedz7%2Fbasic-auth-example.png?alt=media\&token=909b6725-c343-4fc9-9c9c-4642e2b332d0)

## Add basic auth to "Go to URL" step

1. &#x20;[Manually add](https://docs.bugbug.io/editing-tests/manually-creating-the-test) a "Go to URL" action
2. Click it to see the details on the right-hand side
3. Click "Password protected"
4. Enter the username and password here
5. Save the step
6. [Run the test](https://docs.bugbug.io/running-tests) to see if the page is loaded correctly

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fl0zHX8hGNJaAMXHCnrsF%2Fimage.png?alt=media&#x26;token=494189e1-0104-4b35-9cb1-1f6cab89b804" alt=""><figcaption></figcaption></figure>


# Common selectors issues

### How to create good selectors for apps with tables and interactive lists? <a href="#how-to-create-good-selectors-for-apps-with-tables-and-interactive-lists" id="how-to-create-good-selectors-for-apps-with-tables-and-interactive-lists"></a>

Here's a typical problem to solve: you have an app with list of orders in a table. Each row has a checkbox in it. You want to create a test automation that clicks the checkbox in the second row.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F2bOPxr5oz0IdoMLvfbfw%2Fimage.png?alt=media&#x26;token=fddc3962-377d-41d9-ac65-60bfe78d3b44" alt=""><figcaption><p>The above example comes from an <a href="https://marmelab.com/react-admin-demo/#/commands">open-source demo app</a></p></figcaption></figure>

The problem is that there is no way to write a unique selector directly to this checkbox. There are more checkboxes on the list and we don't want to rely on the order of elements. We don't want the second checkbox, we want a *specific* checkbox.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkyW2Ic5RtzXSwWcXSSGs%2Fimage.png?alt=media&#x26;token=c57d0b25-5218-4749-9f56-5593330b7481" alt=""><figcaption></figcaption></figure>

There is nothing unique in the HTML element itself. Wait, is that class attribute unique? It is, but it's not good for test automation selectors. It's a random string that changes with every app deployment.&#x20;

**‍XPath traversing comes to the rescue!**\
We will guide you step by step how to create a reliable selector, that first identifies the right row in the table and then finds the checkbox inside. The result selector will "traverse" the parents and children in 3 steps.

1. Find a specific text in the table

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FJo9gLsyLr1bsRajPkDqH%2Fimage.png?alt=media&#x26;token=abed7b48-2a7a-417a-aab3-d68a019c66ff" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FG0Nz2SAvuwV80BMXivO3%2Fimage.png?alt=media&#x26;token=c6b89c04-5e01-4251-a566-a201bae5741a" alt=""><figcaption></figcaption></figure>

2. Find the parent table row by searching ancestors of the element from step 1

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FjyUxk28BK9g5A8yRnnP4%2Fimage.png?alt=media&#x26;token=e94cb47c-9759-4b16-ac7a-ab716c55093f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F7fcduEHDCGlxpK3bNDZ8%2Fimage.png?alt=media&#x26;token=396c244a-48df-43cb-8e0a-ceb26c22dfff" alt=""><figcaption></figcaption></figure>

3. Find the checkbox inside the row

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FiMru6svHlAGBKttMELn9%2Fimage.png?alt=media&#x26;token=2321bb6f-39c5-4623-9dc8-d204e62cce8d" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkBJ0NUCavGSuTWDDpbBm%2Fimage.png?alt=media&#x26;token=1788810f-fc03-4723-b2f6-008f950fc681" alt=""><figcaption></figcaption></figure>

Here's how to do this with our no-code tool. You need to use "Then find..." button and connect these 3 steps into one sophisticated and powerful XPath selector:

{% code overflow="wrap" %}

```
//*[contains(text(), "KYDGHM") ]/ancestor::tr/descendant::input[​@type="checkbox"]
```

{% endcode %}

You can apply the same technique to multiple other test cases.

### Capitalization of selectors values matters <a href="#capitalisation-matters" id="capitalisation-matters"></a>

Make sure your selector uses the same capitalisation of characters as in the page. Pay attention to uppercase and lowercase letters! Ideally copy-paste the text from HTML via Chrome developer tools.

### My selector works on desktop but doesn't work on mobile. Why? <a href="#my-selector-works-on-desktop-but-doesn-t-work-on-mobile.-why" id="my-selector-works-on-desktop-but-doesn-t-work-on-mobile.-why"></a>

Your app may have 2 different button "duplicates", one dedicated for desktop and one for mobile. One is always hidden, depending on the window width.

In such situation, the best solution is to create 2 separate tests for mobile and desktop with 2 different selectors.

Or try refactoring the code so that there is only one button present at a time - not hiding, but removing the button from the document.

You can also try to write a clunky selector that matches the 2 buttons, but somehow remove the hidden button with the `not` operator, for example:

{% code overflow="wrap" %}

```markup
//button[contains(text(), "Example") and not(ancestor::div[contains(@style, 'display:none')]) and not(ancestor::div[contains(@style, 'display:none')])]
```

{% endcode %}

### How to check if your selector works in Chrome? <a href="#how-to-check-if-your-selector-works-in-chrome" id="how-to-check-if-your-selector-works-in-chrome"></a>

In the [above example](#how-to-create-good-selectors-for-apps-with-tables-and-interactive-lists) we created a selector, now we should check if it works.

1. Open this [demo app](https://marmelab.com/react-admin-demo/#/commands) and login with "demo / demo", then go to "Orders" tab
2. Open Chrome developer tools
3. Click Ctrl+F to open the "Find" box (Cmd+F on Mac)
4. Paste the selector
5. Click enter
6. The matching element will be highlighted
7. Click enter several times to make sure that this is the only element that has a match

Here's a quick video that shows the whole XPath selector verification process in Chrome:

{% embed url="<https://www.youtube.com/watch?v=GiZGk7LYjaA>" %}


# CAPTCHA in automation testing

Discover effective troubleshooting tips for resolving captcha challenges in automation testing. Learn how to overcome obstacles and improve your testing process. BugBug Documentation.

## What is CAPTCHA?

[CAPTCHA](https://en.wikipedia.org/wiki/CAPTCHA) makes test automation more difficult, as it was specifically designed to prevent automated bots from using your web app.&#x20;

For example, if you have a registration form, it might be protected by [reCAPTCHA](https://en.wikipedia.org/wiki/ReCAPTCHA) to prevent fake account registrations.&#x20;

<img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0BWcufBQr1bKceIB1aP7%2FScreenshot%202022-08-18%20at%2012.29.42.png?alt=media&#x26;token=a2e84b4a-e610-4cdd-9f9f-34834a698796" alt="" data-size="original">

## Disable the captcha on test environments

There are multiple captcha providers and each has a different way to disable it. For example, if you use reCAPTCHA you need to set a [special "site key"](https://developers.google.com/recaptcha/docs/faq#id-like-to-run-automated-tests-with-recaptcha.-what-should-i-do).

![Excerpt from the reCAPTCHA documentation](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkV5I3kFNTADKQiZc9RmQ%2Frecaptcha%20screenshot.png?alt=media\&token=c0638e49-aa0b-4abf-ab7a-1b5fe2303ed7)

## Allow BugBug to skip CAPTCHA during the automation testing

You can implement a special secret flag in your backend code to allow BugBug to skip the captcha.&#x20;

1. Add a custom header in your project settings with a secret string of your choice
2. On your backend code, add a condition, that the captcha is not required if the request header contains this secret string

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FsjHu2vHLkKdw6eVhkZjL%2Fcustom-headers%20\(1\).png?alt=media\&token=04d3550d-e540-4a2c-9234-d32815579f0e)


# Cloud tests sometimes failing

Discover effective troubleshooting techniques for resolving intermittent cloud test failures. BugBug's comprehensive guide helps you tackle testing challenges.

By default, BugBug will attempt to run a test step for 30 seconds locally and 60 seconds in the cloud. If BugBug is not able able to perform a test step in this amount of time, it will mark the step as failed - this is called a *timeout*.

If your local tests are stable, but only cloud tests are sometimes failing randomly, most likely it is caused by the fact, that BugBug cloud virtual machines are not as fast as your own computer. It may take longer for the page to process in the cloud.&#x20;

To prevent this you can **increase the timeout of cloud runs**:

1. Go to project settings
2. Change the "Cloud runs timeout" to a higher value
3. Save settings

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F8o1CvbgZhB7OzJUGoVSF%2Fcloud%20run%20timeout.png?alt=media\&token=f5736c8c-4d53-45b2-a2d6-7c64696de9ee)

Now BugBug will give your website more time in the cloud to load and operate.


# IPs list of cloud runners

If you want to know which IPs BugBug is running tests from in the cloud so that you can whitelist them in your infrastructure, you can find them by opening the link below. We have an API interface for this, so if this list changes one day, the change will be reflected in this API response.

**We do not change this frequently. The last change was 3 years ago.**

{% embed url="<https://app.bugbug.io/api/v1/config/ips/>" %}

If you are looking into how to configure your VPN or Firewall, please read this page: [VPN or a Firewall](https://docs.bugbug.io/troubleshooting/vpn-or-a-firewall).


# VPN or a Firewall

Resolve VPN or Firewall issues with BugBug's comprehensive troubleshooting guide. Get expert tips and solutions for seamless network connectivity.

If your app [environment](https://docs.bugbug.io/editing-tests/variables#work-with-different-development-environments) is not publicly available, for example only available in your local network or a private network with a VPN or behind a firewall, you can't run the [cloud tests](https://docs.bugbug.io/running-tests/in-cloud-on-server) because BugBug will not be able to access your app. You have several potential workarounds though.&#x20;

{% hint style="warning" %}
Recommended solution:\
\
Set your VPN/Firewall/Server settings to allow BugBug to connect from our IP range. You can find the IP list here:[ BugBug IP list](https://app.bugbug.io/api/v1/config/ips/)&#x20;
{% endhint %}

{% hint style="info" %}
We provide an IP list generated from the API in case of feature changes on our site. Please do not hardcode it to avoid future problems. Use API response. We are still developing for the better.&#x20;
{% endhint %}

## **Other options:**&#x20;

### **Solution A:** Publish your app but protect it with a password

Use a tool such as [ngrok.com](https://ngrok.com/) and publish your app publicly at the specific password-protected subdomain with authentication. More about ngrok? See [our documentation](https://docs.bugbug.io/running-tests/test-your-local-build-or-protected-web-page-using-ngrok) on setting up this tool

### Solution B: Add an exception in your firewall/VPN

Let in BugBug based on custom headers or custom user-agent.&#x20;

1. In the project settings set your custom header to some shared secret value
2. In your VPN/Firewall/Server settings add a rule to allow traffic with headers containing this shared secret

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F8YJettgG4aJVAXuR7L6d%2FZrzut%20ekranu%202023-03-17%20104152.png?alt=media&#x26;token=5f613d89-5940-40ef-8234-9a16d2afc9d0" alt=""><figcaption></figcaption></figure>

### **Solution C: run tests locally**&#x20;

You can still [execute the tests manually](https://docs.bugbug.io/running-tests/test-in-your-browser) on a machine that has access to the app environment. The disadvantage is that you can't [schedule tests](https://docs.bugbug.io/running-tests/schedules).

{% hint style="danger" %}
**Upcoming feature:** we are working on a command line interface that would allow you to run BugBug tests remotely on your own internal development server.
{% endhint %}


# A/B tests

Running some A/B tests on your website under tests could make tests flaky because your website renders differently depending on the browser session and the A/B test drawn.  This is especially problematic for smoke tests in production environments.

There are a few solutions to prevent this situation:

1. Disable A/B tests for specific IP addresses. This is probably the easiest solution, but it depends on the A/B testing tool that you use. Some of them have the option to disable A/B tests for specific IPs. In this case, you should disable A/B tests for our cloud runners [IP list of cloud runners](https://docs.bugbug.io/troubleshooting/ips-list-of-cloud-runners) but also your local IP address.
2. Exclude A/B testing script based on query string parameter. Using Google Tag Manager and loading custom JavaScript code from an external A/B tool is popular. You can exclude the loading of this script based on the query string parameter. To do this, add `?bugbug=1` to your Goto URL step in tests and exclude loading of the A/B test script based on this parameter.
3. Manually mark your browser session as A or B version. This requires some development knowledge. A/B testing tools use cookies or local storage to store information about the test version. If you are familiar with DevTools, you can check what kind of cookies or localStorage item has been added and set this manually in your tests using [Custom JavaScript](https://docs.bugbug.io/editing-tests/custom-javascript-actions#javascript-steps) to bind the same website version with tests.


# Report a bug

Need to report a bug? Our comprehensive troubleshooting guide helps you navigate the process smoothly.

If you noticed problems with BugBug, don't hesitate to send us a bug report. Just write an email to <mark style="color:purple;">**<info@bugbug.io>**</mark> and tell us what's wrong.&#x20;

We try to respond to every report within 24 hours.


# Beginners tutorial to automation testing

Learn the basics of automation testing with our comprehensive beginner's tutorial. Boost your test automation skills with BugBug's in-depth guide.

Automation testing (whether e2e or unit testing) is **the process of using software tools to execute test script on an application,** comparing the actual results to the expected outcomes. It helps save time and effort by automating repetitive tasks and allows for quicker feedback on the application's quality.&#x20;

Testing process can be done in test automation tool like [**BugBug**](https://bugbug.io/) or **Selenium**. The choice of automation testing tool depends on various factors like the type of application being tested, the programming language used, test data, testing framework, the team's expertise, and the testing requirements.

## How to use BugBug?

This **tutorial will guide you through the best practices of creating test automation** with the BugBug testing tool, even if you're not a manual tester with technical knowledge. You're going to:

* Learn the basics of software testing concepts and terminology
* Follow the step-by-step screenshots
* Understand what to automate

This is not an ultimate guide with all there is to be known about test automation. We're going to explain everything **assuming you have zero technical background** but **you're good with computers**, unlike this guy:

{% embed url="<https://www.youtube.com/watch?v=o_XaJdDqQA0>" %}

## Manual testing vs. automated testing

When software developers make changes in the code, they can break something in the app that has already been working. To make sure that nothing is broken, you need to test everything...

{% hint style="success" %}
[Read how to prepare your app for automated testing and avoid common pitfalls.](https://docs.bugbug.io/best-practices#how-to-prepare-your-app-for-testing)
{% endhint %}

### **Manual testing**

You just click everything in the app with your own computer and make sure there are no bugs. This is super boring and can take multiple days to complete!

It makes you feel like this:

![regression testing meme](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fh18ttQLdT3gMIAYkoMpW%2Fregression-testing-again%20\(1\).jpg?alt=media\&token=b98c8be0-1567-4b8c-9ef2-bfc6f016defb)

### **Automated testing**

You create step-by-step instructions for the computer to click everything for you automatically. You don't click on your own, but let the computer do the tedious work.

When you use this method you can feel like this:

![automsted tests meme](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXqrJyLAc1oZlEKIK9ISF%2FScreen%20Shot%202022-10-27%20at%2011.53.03.png?alt=media\&token=3380ba12-8b24-4a28-ba7c-d3c49e942c6f)

You click "Run" and BugBug is clicking according to your instructions called **test steps**. Here's an example of an automated test where BugBug checks if the login works.

{% embed url="<https://youtu.be/Cbk8i0A27no>" %}

If BugBug is able to finish all the test step&#x73;**,** the test is marked as successfully finished & <mark style="color:green;">**passed**</mark>. It means that everything works as it should.

If BugBug is not able to finish, the test is <mark style="color:red;">**failed**</mark><mark style="color:red;">.</mark> It means that something doesn't work right or your test steps are incorrect.

Keep reading to learn how to create such an automated test 💪&#x20;

## Create your first test via "recording"

Create your first automated test that checks if the login works. You will create a set of step-by-step instructions for BugBug that will tell it what exactly should be clicked or entered in the text fields.

{% hint style="warning" %}
Before you continue make sure you've set up your BugBug account and have access to a [project](https://docs.bugbug.io/organizing-tests/projects) and [installed the BugBug Chrome extension](https://docs.bugbug.io/quick-start/install-chrome-extension).&#x20;
{% endhint %}

{% hint style="info" %}
Throughout this guide, we use [this open-source demo app](https://marmelab.com/react-admin-demo/) called React Admin Posters Galore.&#x20;

You can learn by creating a new blank project and following each step together with us.
{% endhint %}

The next steps would guide us to test execution:&#x20;

1. **Create a new project**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FEpGOVhr6kNmbRsB9q6jb%2Fnew%20project.png?alt=media&#x26;token=ca0527da-cb36-4f76-8137-a43d13f5a0e5" alt="Create a new project - BugBug test automation tool"><figcaption></figcaption></figure>

**2. Name it "Posters Galore" and enter a URL that will be the starting point of your app**

In our example use [https://marmelab.com/react-admin-demo/](https://marmelab.com/react-admin-demo/#/)

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVci5VCxJMtyMqb3T0IMz%2Fcreate%20proj.png?alt=media&#x26;token=8a177509-7501-4680-aada-472174474642" alt="Create a new project - BugBug test automation tool"><figcaption></figcaption></figure>

**3. Create a new test**

We're going to create a test that checks if login to our app works, so we will name it simply "Login". In this case we are using functional testing - a type of software testing where the application under test is checked against its functional requirements.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FIeX2jCZMO7WQcjXg8OdU%2Fcreate%20test.png?alt=media&#x26;token=f6e2ffbf-e5f7-4f29-b744-e861c6b16b54" alt="Create a new test - BugBug test automation tool"><figcaption></figcaption></figure>

**4. Start the recording**

Your test is empty for now. That means that it has no instructions - no test steps. The URL you entered before is already pre-filled, so you can click "start recording".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FO1gXFIu3OMqxCSCaEMKR%2Frecord.png?alt=media&#x26;token=bb436e83-d06f-44c5-8927-049e652ae79d" alt="Start test recording - BugBug test automation tool"><figcaption></figcaption></figure>

**5. Wait 5-10 seconds until BugBug loads your page in an incognito window**

{% hint style="info" %}
**Why incognito?** Testing needs to always start from a clean state. There should be no cookies or browser cache for your page before starting the test.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVbAOUMF5EHnbmgaHsSbU%2FZrzut%20ekranu%202023-05-25%20144141.png?alt=media&#x26;token=e7cf0ebd-944d-4949-abe7-859b5302cc79" alt="Test recording - BugBug test automation tool"><figcaption></figcaption></figure>

On the right side of the page, you can see a BugBug panel with actions dedicated to recording. We call it "recording overlay". By default, BugBug records every click and keyboard typing, but using this panel you can also record additional special actions. BugBug is providing automation scripts as you click and navigate on the website.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fo6cAaiBy5cjUPHJk0Who%2Frecording%20overlay.png?alt=media&#x26;token=2b53319b-d1ea-4752-8e2d-e6abbb2299ab" alt="Test recording overlay - BugBug test automation tool"><figcaption></figcaption></figure>

**6. Carefully enter login credentials using "demo" for login and password fields**

{% hint style="info" %}
**Why carefully?** BugBug records every click, so it's better to be slow while recording and think about every click. You don't want to accidentally click in the empty background!
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FBiM7PUdUHyC9h3XVcgSe%2Fusername.png?alt=media&#x26;token=b4a6058c-ec62-494b-8627-fd89122a462b" alt="Test recording - BugBug test automation tool"><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FqDn07Hxhh5YWFTWrhbFP%2Fhaslo.png?alt=media&#x26;token=afa4e60f-7b82-4eac-b21e-96dcf2eb0b69" alt="Test recording - BugBug test automation tool"><figcaption></figcaption></figure>

BugBug shows "Saved" after each click or keyboard typing. Each of these recorded actions will become a "test step".

**7. Click "Sign in"**&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUbxSFlSGjuSJQtU2Cbnf%2Fsign%20in.png?alt=media&#x26;token=531a70d0-a2ac-4a53-8210-90e0598be53e" alt="Test recording - BugBug test automation tool"><figcaption></figcaption></figure>

You should now see the "Posters Galore" admin panel.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FInSBbORn2UoCkBvSt6Yw%2FZrzut%20ekranu%202023-05-25%20145328.png?alt=media&#x26;token=3dde5b56-f9a4-42ea-bd61-a3f620686fd3" alt="Test recording - BugBug test automation tool"><figcaption></figcaption></figure>

**8. Add an assertion**

We've successfully logged in, now we need to create an instruction for BugBug that will check if the page actually has logged in. What should appear on the page that clearly tells us that the login worked? What should we *assert*?

{% hint style="info" %}
**Assertion** = a test step that checks if something specific appears on the page, or if the page matches some specific expectations.
{% endhint %}

The simplest way of checking if the login has been successful is to **check if the page shows some specific text**. In our case we can assert if the text "Welcome to the react admin e-commerce demo" is visible. If it is visible everything is fine, if not, the test will fail.

Click "Assert" in the recording overlay

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVDAFCXHlCt77GHfBn8Jt%2Fassert.png?alt=media&#x26;token=5fc444f9-9f86-407c-8b1f-a9fa2904a6de" alt="Adding assertion - BugBug test automation tool"><figcaption></figcaption></figure>

&#x20;Click the text on the page that you want to check every time BugBug runs this test.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FA7SLXmgpSLKd8pgTqcgS%2Fass.png?alt=media&#x26;token=cfa01568-35db-456b-8fb9-3c0dbc544a47" alt="Test assertion - BugBug test automation tool"><figcaption></figcaption></figure>

**9. Finish recording the test**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FAUGlwxmFIiL3RQ7SyUOz%2Ffinish.png?alt=media&#x26;token=ec1efdc0-8f66-4f2a-8528-241780981e83" alt="Finish test recording - BugBug test automation tool"><figcaption></figcaption></figure>

See that everything you clicked is now recorded as "test steps".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVVFRjy7twnQ526vyMG5i%2FZrzut%20ekranu%202023-05-25%20145749.png?alt=media&#x26;token=d5801c46-2338-427a-8962-79ae6e54f47d" alt="Test steps - BugBug test automation tool"><figcaption></figcaption></figure>

**10. Run the test to see if it works**&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FeV5zN8yUAfHzWrFvJ9Qb%2Fru.png?alt=media&#x26;token=41f5a7d3-760a-4e7f-b2dc-fad17575e3d6" alt="Test Run - BugBug test automation tool"><figcaption></figcaption></figure>

Observe how BugBug is repeating your actions.&#x20;

{% hint style="info" %}
**When running the test:**

* Don't move your mouse cursor over the running test window.
* Don't minimize the window, as Chrome may stop executing the test if it's not visible.
  {% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FPQnMyEEsluPbEXkWAlWv%2FZrzut%20ekranu%202023-05-25%20152005.png?alt=media&#x26;token=d905669c-c80c-448a-90e2-aa47cdeb4115" alt="Test Run - BugBug test automation tool"><figcaption></figcaption></figure>

**11. Check if the test has passed**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F9I1oR0JfhF6X3FiEgBXY%2Fpass.png?alt=media&#x26;token=46c770f3-bb2c-49bf-9f73-0c02e23eb81d" alt="Test Run - BugBug test automation tool"><figcaption></figcaption></figure>

If your test has not passed and it's failed, it can be caused be several common problems which we will cover later.

**12. Close the finished test**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FrgUHQ8b2TYuN3B5hghSI%2Fclo.png?alt=media&#x26;token=29c03399-694b-4473-b643-8ee9c8704eaf" alt="Test Finish - BugBug test automation tool"><figcaption></figcaption></figure>

All your test steps are green! The login works as it should.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FKbbgK1aSmm6MCCnVBmUu%2FZrzut%20ekranu%202023-05-25%20152551.png?alt=media&#x26;token=8208a578-2b19-4eb6-b625-d2df2104b1ab" alt="Test Result - BugBug test automation tool"><figcaption></figcaption></figure>

**13. Achievement unlocked!**

🎉 You have successfully automated your first test. Now to check if login works, you don't need to click on your own, you can just click "Run test" and BugBug will do it for you.

## Does the test fail? Fix it with "Record from here"

Sometimes after you finished the initial recording, your test may still not pass. There might be several reasons for that:

* You forgot to record the mouse "hover"
* You clicked an incorrect element during the recording
* Your page has dynamic content, for example, you wanted to check if your homepage shows recommended products, but these products change every time you load the page
* Your page HTML is not built with automation testing in mind and uses unusual development patterns and solutions that are not industry-standard (see more advanced info on [data-testid](https://docs.bugbug.io/preventing-failed-tests/selectors#use-custom-attributes-for-selectors))

​We're going to walk you through an example, where we record a test, but it doesn't work because we forgot to record mouse "hover". Then we're going to fix the test using the "record from here" action and add the missing hover step.

{% hint style="info" %}
For this example, we're using our [Playground page](https://playground.bugbug.io/pl/others/nested-element-dynamically-added-to-dom-on-hover), which is dedicated to testing.

You can learn by creating a new blank project and following each step together with us.&#x20;
{% endhint %}

**1. Create a new project** with our playground example page `https://playground.bugbug.io/pl/others/nested-element-dynamically-added-to-dom-on-hover`

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F5NpN7zJFgGiKhWYtwPnN%2Fimage.png?alt=media&#x26;token=7ed5c7fb-3a98-4fbc-a65a-19d4be8bc769" alt=""><figcaption></figcaption></figure>

**2. Create a new test and start recording** (use the example app URL provided above).

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FrrNRaoRGvoSV6t2qGG7q%2Fimage.png?alt=media&#x26;token=03c6244e-241a-4c14-afb4-f57c56447ff8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUMrcIXUlDDU2GRTf4Hz5%2Fimage.png?alt=media&#x26;token=1c704209-2ecb-4f28-ab44-d44484a6a2ac" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNdflawAHz4VgcZ6DyYa3%2Fimage.png?alt=media&#x26;token=5c084e55-a17c-40f0-aef6-7db8f5c8ba2f" alt=""><figcaption></figcaption></figure>

**3. Hover over a dropdown menu "Trigger" and click the "Item 1" element.**

Attention! This element only appears when you hover your mouse over the dropdown menu. We deliberately skip recording this hover to demonstrate the consequences.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FvkWvDHmSAdtOTyTlE35u%2Fimage.png?alt=media&#x26;token=c08f7723-7ebc-44c4-b71a-c2ccbe04dbac" alt=""><figcaption></figcaption></figure>

**4. Finish your recording.**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FxzBIjwsuh7iFqwTtnjMJ%2Fimage.png?alt=media&#x26;token=173e8342-105e-46c2-845c-3aef1253c6ce" alt=""><figcaption></figcaption></figure>

**5. Run the test to see if it works...** But it fails because we forgot to record the "hover".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FIZmsCbBuotTzGNn7N5IG%2Fimage.png?alt=media&#x26;token=7008c029-89bd-4907-a9ec-b9fa7a31a42f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FIeENGna5vojDYXa0UXqw%2Fimage.png?alt=media&#x26;token=1ae01293-ae00-4946-bd26-03fae3866323" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQQ9FDtMExCa0o9inSRzP%2Fimage.png?alt=media&#x26;token=61c336a4-ca30-45a9-9ddb-e60789aee8f2" alt=""><figcaption></figcaption></figure>

Now, it's time to fix the test by recording the missing "hover" step.

**6. In the existing window within the test, click the "Edit and rewind" button.**

This option will switch you to [Edit and Rewind mode](https://docs.bugbug.io/workflow-tips/edit-and-rewind), in which you can record new steps to fix our test.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F8d36s4I4b2ti5HKximNS%2Fimage.png?alt=media&#x26;token=4e983e90-07a2-4ff0-a5b7-dec916ffafa9" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Ffm0oOI79YZyOwSM4adBg%2Fimage.png?alt=media&#x26;token=463609ba-5ed5-498f-8f4d-4bcfd261a8ce" alt=""><figcaption></figcaption></figure>

**7. Click "Record from here".**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FK6ORPT5ZAhetoM8ZUXZG%2Fimage.png?alt=media&#x26;token=80d1b79b-1669-49c5-83e2-50d46f232316" alt=""><figcaption></figcaption></figure>

**8. Click the "Add hover" button in the recording overlay.**

You can see that the test is ready for recording when the BugBug overlay shows the "REC" icon.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F7R8sxx75K9HZqx89pBgV%2Fimage.png?alt=media&#x26;token=a47ab1f6-56a7-41aa-a3ac-a3643e2bbea7" alt=""><figcaption></figcaption></figure>

**9. Click the dropdown menu.**

This tells BugBug that the mouse should be moved to this element before attempting to click the "Item 1" element.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCwb8PGMSEn92pAYnMbiz%2Fimage.png?alt=media&#x26;token=7924d433-ecee-4605-ba18-888961998f92" alt=""><figcaption></figcaption></figure>

**10. Finish your recording and confirm the recorded steps.**

You can see that we only added one step, "Hover."

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FadCkeNvbmscBvayjK0bi%2Fimage.png?alt=media&#x26;token=f143814b-814f-40d0-8df3-11c3a76d0de8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FS5BeVk1lMCkWENIQVh0Y%2Fimage.png?alt=media&#x26;token=8d449923-b27b-4617-a44a-3834c371bf40" alt=""><figcaption></figcaption></figure>

**11. Run the test to check if it works now.**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F27Oh7TbFNSCadwDWFxt4%2Fimage.png?alt=media&#x26;token=1f230059-1e7b-4dc2-b80f-f0f38cff3607" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHTHQ95boy4ktDOP6ica1%2Fimage.png?alt=media&#x26;token=601a0ea0-e3c5-4d4e-b1c8-8cb83cab8504" alt=""><figcaption></figcaption></figure>

**12. Achievement unlocked!**

🎉 It worked! You've fixed a test with "Record from here". You can use this technique for more advanced problems. Conclusion: if you see that your test fails, try to "Record from here" and replace the failed steps with a new recording. It's the simplest way of fixing tests!

{% hint style="info" %}
If you want to know more about fixing and debugging your tests, read more about [edit-and-rewind](https://docs.bugbug.io/workflow-tips/edit-and-rewind "mention") and [breakpoint-run-step-by-step](https://docs.bugbug.io/debugging-tests/breakpoint-run-step-by-step "mention")&#x20;
{% endhint %}

## What to test?

You might think now: "Hold on, how can I test everything? Is it possible?"&#x20;

In short: no, you will never be 100% sure if everything works as it should. But your goal is to **lower the risk of app users encountering a bug**. You should focus on testing features that are critical for your business.

{% hint style="info" %}
Checking if there are no new bugs is called [**regression testing**](https://bugbug.io/blog/software-testing/everything-you-need-to-know-about-regression-testing/)**.** If you notice a bug in something that has been working before, it's called **a regression.**
{% endhint %}

Examples of features and consequences of their bugs:

| Feature                                              | What if it breaks:                                | Is it critical? |
| ---------------------------------------------------- | ------------------------------------------------- | --------------- |
| Login                                                | Users can't use your app                          | Yes             |
| Homepage / Landing page                              | New clients can't register                        | Yes             |
| Registration                                         | New clients can't register                        | Yes             |
| Creating new items                                   | Users can't achieve their basic goal              | Yes             |
| Password reset                                       | Only users who forgot their password can't access | No              |
| Some checkbox in an obscure feature that nobody uses | Probably no-one will notice                       | Hell no         |

{% hint style="info" %}
A list of things that you want to test is called a list of [**test cases**](https://bugbug.io/blog/software-testing/how-to-write-automation-test-cases/)**.** An individual **test case** should focus on just one process in your app.
{% endhint %}

## How many tests should you create?

If you're just starting with test automation, your first goal is to create about 5 to 15 tests that check your core website functionality.

Later on, you can even have hundreds of tests, checking all the conditions and less critical features, but it's better to **first focus on a small number of useful tests**.

Here's an example list of tests that covers the most critical paths in a web app Software-as-a-Service product.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FgWkyYEJaLDGKuAz7M3IP%2FScreen%20Shot%202022-11-02%20at%2014.09%201.png?alt=media&#x26;token=1d9a475c-d7bf-4d74-a94a-cb52f0c8aef1" alt="List of tests - BugBug Test Automation Tool"><figcaption></figcaption></figure>

## How many steps should a test have?

Shorter tests are better. Write automated tests that are short, avoiding long test cases.&#x20;

Why? Because shorter tests are easier to maintain and fix.&#x20;

Imagine a very long test that takes 10 minutes to run. But it fails at the end. Every time you want to fix it, you would need to wait these 10 minutes until the test goes through the previous steps. Test automation is supposed to make your work faster, so avoid such long tests.

## **How to make shorter tests?**

**Use multiple test accounts**

Don't use your own personal login and password in automated tests. Create a dedicated test user for that. Each user can have a different configuration. For example, one of your test users can be a business user, and one can be a personal user. You create separate tests for each type of login.&#x20;

Make a list of your test accounts and their params and store it somewhere in a spreadsheet, for example like this:

<table><thead><tr><th>Email</th><th width="160">Password</th><th width="143">Type</th><th>Parameters</th></tr></thead><tbody><tr><td>test-automation-standard@xyz.com</td><td>qwe123qwe</td><td>Business</td><td>User with default configuration for business accounts</td></tr><tr><td>test-automation-trial@xyz.com</td><td>asd4rftha</td><td>Personal</td><td>Trial account</td></tr><tr><td>test-automation-subscribed@xyz.com</td><td>46dghbn90</td><td>Business</td><td>Paying user, with a subscription active</td></tr></tbody></table>

**Split user paths to independent tests**

Here's an example of a too long:

| Test name    | Steps                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Landing page | <p>go to landing page URL</p><p>click "features" </p><p>assert all the features</p><p>click "contact"</p><p>assert contact information </p> |

Split it to 2 independent tests:

| Test name             | Steps                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------- |
| Landing page features | <p>go to landing page URL</p><p>click "features" </p><p>assert all the features</p>   |
| Landing page contact  | <p>go to landing page URL</p><p>click "contact"</p><p>assert contact information </p> |

**Remember that tests need to be independent!**&#x20;

Tests should be independent of each other. You should not create 2 tests and then run them in a specific order. Every test needs to be self-contained. Learn more about it in our tips on [atomic test cases](https://docs.bugbug.io/creating-tests/independent-tests).

## What not to test?

A test automation framework is a set of guidelines, best practices, tools, and libraries that provide a structured approach to designing, organizing, and executing automated tests. It aims to standardize the testing process, increase test efficiency, and improve test maintenance.&#x20;

That's why some features are known for being **more difficult to automate.** We recommend that you automate them later after you are done with the easier test cases.

* **Registration**: it's difficult to automate because you can't register the same email twice, so you need to [generate a random email and verify it afterward](https://docs.bugbug.io/editing-tests/variables#test-user-registration-and-login-using-variables).
* **Collaboration**: one user is adding something, and the second user sees the changes. You need one long test where you log in with the first user, then log out and log in again with the second user.
* **Dynamic lists** such as search results, product listings, exchange rates, and lists that change all the time. Automation requires a good understanding of how to make the list more predictable.
* **Downloading files** and checking their contents.
* **Multi-language**: you can have lots of tests for different languages, but it's hard to maintain unless your app supports [selectors](https://docs.bugbug.io/preventing-failed-tests/selectors) based on [data-testid attributes](https://docs.bugbug.io/preventing-failed-tests/selectors#use-custom-attributes-for-selectors).&#x20;
* **Dates and calendars**: the current date changes every day, so it's not easy to record and repeat.

## Suites: when do you need them?

Test [suites](https://docs.bugbug.io/organizing-tests/suites) are groups of individual tests. They allow you to run several tests at once with one click.&#x20;

By default, BugBug creates an "All tests" suite for you. All new tests will be automatically added to this suite. If you're a beginner, you don't need to set up anything else for now, this one suite should cover the basic needs.

{% hint style="info" %}
You will need more suites later on, once you have more advanced tests that cover [different testing environments](https://docs.bugbug.io/editing-tests/variables#work-with-different-development-environments).&#x20;
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVmFEDRFbANThePLExnG1%2FZrzut%20ekranu%202023-05-26%20164755.png?alt=media&#x26;token=52587bba-9f91-45ce-93ca-2f2af55b0c8a" alt="Test suites - BugBug Test Automation Tool"><figcaption></figcaption></figure>

## Run tests in the cloud

You might think that if you created your 5 essential automated tests, now to run them you need to open up your computer and click "Run" and block your computer for several minutes. Good news - there's no need for that! You can run tests **in the cloud** and even **schedule** them to run automatically, even when you're asleep. :magic\_wand:

{% hint style="info" %}
**Run in cloud** = run on some other machine in a data center, not on your own computer

**Run locally** = run on your own computer in your own browser&#x20;
{% endhint %}

Check if your tests are passed when you run them in the cloud.&#x20;

1. Go to "Suites"&#x20;
2. Find "All tests"
3. Click "Run in cloud"
4. Wait until the suite is finished and passed

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fkm2APHq3T12iB2pzJZrX%2Fcloud.png?alt=media&#x26;token=ff038a64-297f-4253-b879-cbaab5b4bbf2" alt="Test run in cloud - BugBug Test Automation Tool"><figcaption></figcaption></figure>

If the tests are passed locally but fail in the cloud, please [contact our support](https://bugbug.io/contact/). Usually, that should never happen.&#x20;

## Schedule automated tests

You can monitor your web app and run automated tests every hour and get notifications when your test fails. Learn more in our [separate article about scheduling tests](https://docs.bugbug.io/running-tests/schedules).

## Take automation to a next level

This guide only covered the very beginning of what you can achieve with BugBug test coverage. Keep exploring and challenging yourself with more and more difficult test cases! Once you're comfortable with the basics, read our other in-depth guides, where we cover advanced techniques and a more strategic approach to automation testing in a startup.&#x20;

If you have questions or comments on this guide, please [contact us](https://bugbug.io/contact/), our support team is very responsive and interested in your feedback.&#x20;

Happy (automated) testing! :beers:



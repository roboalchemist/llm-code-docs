# Source: https://docs.bugbug.io/bugbug-app-faq.md

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

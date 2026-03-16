# Source: https://docs.bugbug.io/organizing-tests/suites.md

# Suites

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
